"""AHN (Actueel Hoogtebestand Nederland): 0.5 m DSM and DTM for the AOI via the PDOK WCS.

The AOI (4.5 x 3.3 km) at 0.5 m is ~9000 x 6700 px, too big for one WCS request,
so it is fetched in 1 km tiles and mosaicked with rasterio.
Output: data/ahn/dsm_05m.tif, data/ahn/dtm_05m.tif
"""
import re
import sys

import numpy as np

from common import get, log
from config import AOI_RD, DATA

WCS = "https://service.pdok.nl/rws/ahn/wcs/v1_0"
TILE = 1000  # metres
OUT = DATA / "ahn"
OUT.mkdir(exist_ok=True)


def coverage_ids():
    r = get(WCS, params={"SERVICE": "WCS", "VERSION": "2.0.1", "REQUEST": "GetCapabilities"})
    r.raise_for_status()
    ids = re.findall(r"<wcs:CoverageId>([^<]+)</wcs:CoverageId>", r.text)
    return ids


def fetch_tile(cov, x0, y0, x1, y1, path):
    params = [
        ("SERVICE", "WCS"), ("VERSION", "2.0.1"), ("REQUEST", "GetCoverage"),
        ("COVERAGEID", cov), ("FORMAT", "image/tiff"),
        ("SUBSET", f"x({x0},{x1})"), ("SUBSET", f"y({y0},{y1})"),
    ]
    r = get(WCS, params=params, timeout=180)
    if r.status_code != 200 or not r.content[:4] in (b"II*\x00", b"MM\x00*"):
        raise RuntimeError(f"tile {x0},{y0}: HTTP {r.status_code} {r.text[:200]!r}")
    path.write_bytes(r.content)


def mosaic(paths, out):
    import rasterio
    from rasterio.merge import merge

    srcs = [rasterio.open(p) for p in paths]
    # PDOK tiles use float32-max as nodata; rasterio>=1.5 cannot carry it through merge
    # and returns an all-zero mosaic, so use an explicit nodata value instead.
    arr, transform = merge(srcs, nodata=-9999.0)
    meta = srcs[0].meta.copy()
    meta.update(height=arr.shape[1], width=arr.shape[2], transform=transform, compress="deflate",
                nodata=-9999.0)
    with rasterio.open(out, "w", **meta) as dst:
        dst.write(arr)
    for s in srcs:
        s.close()
    return arr[0], meta


def main():
    try:
        ids = coverage_ids()
    except Exception as e:  # noqa: BLE001
        log("AHN WCS (PDOK)", False, f"GetCapabilities failed: {e}")
        return 1
    wanted = {}
    for kind in ("dsm", "dtm"):
        match = [c for c in ids if kind in c.lower() and "05" in c]
        if match:
            wanted[kind] = match[0]
    if len(wanted) < 2:
        log("AHN WCS (PDOK)", False, f"0.5 m coverages not found; available: {ids}")
        return 1

    x0, y0, x1, y1 = AOI_RD
    stats = {}
    for kind, cov in wanted.items():
        tiles = []
        for tx in range(x0, x1, TILE):
            for ty in range(y0, y1, TILE):
                p = OUT / f"{kind}_{tx}_{ty}.tif"
                if not p.exists():
                    fetch_tile(cov, tx, ty, min(tx + TILE, x1), min(ty + TILE, y1), p)
                tiles.append(p)
        arr, meta = mosaic(tiles, OUT / f"{kind}_05m.tif")
        nodata = meta.get("nodata")
        valid = arr[np.isfinite(arr)] if nodata is None else arr[(arr != nodata) & np.isfinite(arr)]
        valid = valid[valid > -100]
        stats[kind] = {
            "coverage": cov, "tiles": len(tiles), "shape": list(arr.shape),
            "valid_pct": round(100 * valid.size / arr.size, 1),
            "min_m": round(float(valid.min()), 2), "max_m": round(float(valid.max()), 2),
            "mean_m": round(float(valid.mean()), 2),
        }
    s = stats
    log(
        "AHN WCS (PDOK)", True,
        f"DSM+DTM 0.5 m mosaics {s['dsm']['shape'][1]}x{s['dsm']['shape'][0]} px; "
        f"DTM {s['dtm']['min_m']}-{s['dtm']['max_m']} m NAP, DSM max {s['dsm']['max_m']} m; "
        f"valid DTM {s['dtm']['valid_pct']}%",
        stats=stats,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

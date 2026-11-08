"""Extra open layers for Eindhoven, each a cross-check or an input the engine can use.

  a) ESA WorldCover 10 m (2021, CC BY 4.0): land-cover shares in the AOI (trees occlude
     cameras; 3DBAG has no trees).
  b) Copernicus DEM GLO-30 (surface model): compared with the AHN 0.5 m DSM, to show
     what a 30 m global model would lose (the resolution Akrotiri relies on).
  c) KNMI hourly weather at station 370 Eindhoven for the incident evening
     (wind, visibility, cloud), for the incident scenario.
Output: data/extra/*, rows in results/access-log.json
"""
import json
import sys

import numpy as np

from common import SESSION, log
from config import AOI_WGS84, DATA

OUT = DATA / "extra"
OUT.mkdir(exist_ok=True)
WORLDCOVER = ("/vsicurl/https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/map/"
              "ESA_WorldCover_10m_2021_v200_N51E003_Map.tif")
COPDEM = ("/vsicurl/https://copernicus-dem-30m.s3.amazonaws.com/Copernicus_DSM_COG_10_N51_00_E005_00_DEM/"
          "Copernicus_DSM_COG_10_N51_00_E005_00_DEM.tif")
KNMI = "https://www.daggegevens.knmi.nl/klimatologie/uurgegevens"
WC_CLASSES = {10: "tree cover", 20: "shrubland", 30: "grassland", 40: "cropland", 50: "built-up",
              60: "bare/sparse", 70: "snow/ice", 80: "water", 90: "wetland", 95: "mangroves", 100: "moss/lichen"}


def read_window(url):
    import rasterio
    from rasterio.windows import from_bounds
    with rasterio.open(url) as src:
        w = from_bounds(*AOI_WGS84, transform=src.transform)
        return src.read(1, window=w), src.window_transform(w), src.crs


def worldcover():
    try:
        a, tf, crs = read_window(WORLDCOVER)
    except Exception as e:  # noqa: BLE001
        log("ESA WorldCover 10 m", False, str(e))
        return
    vals, counts = np.unique(a, return_counts=True)
    share = {WC_CLASSES.get(int(v), str(v)): round(100 * c / a.size, 1) for v, c in zip(vals, counts)}
    share = dict(sorted(share.items(), key=lambda kv: -kv[1]))
    (OUT / "worldcover_shares.json").write_text(json.dumps(share, indent=1), encoding="utf-8")
    log("ESA WorldCover 10 m", True, f"{a.shape[1]}x{a.shape[0]} px in AOI; land cover %: {share}", shares=share)


def copdem():
    try:
        a, tf, crs = read_window(COPDEM)
    except Exception as e:  # noqa: BLE001
        log("Copernicus DEM GLO-30", False, str(e))
        return
    detail = f"{a.shape[1]}x{a.shape[0]} px in AOI; surface {float(a.min()):.1f}-{float(a.max()):.1f} m (EGM2008)"
    extra = {}
    ahn = DATA / "ahn" / "dsm_05m.tif"
    if ahn.exists():
        try:
            import rasterio
            from rasterio.warp import Resampling, reproject
            ref = np.full(a.shape, np.nan, dtype="float32")
            with rasterio.open(ahn) as src:
                reproject(rasterio.band(src, 1), ref, dst_transform=tf, dst_crs=crs,
                          resampling=Resampling.average, src_nodata=src.nodata, dst_nodata=np.nan)
            d = a.astype("float32") - ref
            d = d[np.isfinite(d)]
            extra = {"mean_diff_m": round(float(d.mean()), 2), "rmse_m": round(float(np.sqrt((d ** 2).mean())), 2),
                     "p95_abs_m": round(float(np.percentile(np.abs(d), 95)), 2)}
            detail += (f"; vs AHN DSM averaged to the same cells: mean diff {extra['mean_diff_m']} m, "
                       f"RMSE {extra['rmse_m']} m, 95% |diff| {extra['p95_abs_m']} m (datum offset NAP/EGM2008 not removed)")
        except Exception as e:  # noqa: BLE001
            detail += f"; AHN comparison failed: {e}"
    log("Copernicus DEM GLO-30", True, detail, **extra)


def knmi():
    try:
        r = SESSION.post(KNMI, data={"stns": "370", "start": "2025112215", "end": "2025112224",
                                     "vars": "DD:FF:FX:T:VV:N:RH:U", "fmt": "json"}, timeout=60)
        r.raise_for_status()
        rows = r.json()
    except Exception as e:  # noqa: BLE001
        log("KNMI hourly weather (Eindhoven 370)", False, str(e))
        return
    (OUT / "knmi_370_2025-11-22.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
    brief = []
    for x in rows:
        h = int(x.get("hour", 0))
        if 19 <= h <= 23:   # KNMI hour = hour ending, UT
            brief.append(f"{h-1:02d}-{h:02d} UT: wind {x.get('DD')} deg {(x.get('FF') or 0)/10:.1f} m/s, "
                         f"T {(x.get('T') or 0)/10:.1f} C, visibility code {x.get('VV')}, cloud {x.get('N')}/8")
    log("KNMI hourly weather (Eindhoven 370)", bool(rows), f"{len(rows)} hours; " + " | ".join(brief), hours=rows)


def main():
    worldcover()
    copdem()
    knmi()
    return 0


if __name__ == "__main__":
    sys.exit(main())

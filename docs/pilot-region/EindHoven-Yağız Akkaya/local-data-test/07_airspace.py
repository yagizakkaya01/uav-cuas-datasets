"""Alternative sources for the restricted-zone layer (the PDOK OGC API was retired 30 Jun 2026).

Tries, in order, and logs each:
  a) the old PDOK WFS endpoint for the same dataset (expected to be retired too);
  b) openAIP public airspace export for the Netherlands (GeoJSON), filtered to EHEH;
  c) OurAirports runway thresholds for EHEH (public domain), used to build a clearly
     labelled FALLBACK zone: a buffer around the runway centreline. This is a modelling
     assumption, not an official zone.
Output: data/airspace/*.geojson, data/nofly/runway_buffer_fallback.geojson
"""
import csv
import io
import json
import sys

from common import get, log
from config import AIRPORT_ICAO, CONTEXT_WGS84, DATA

OUT = DATA / "airspace"
OUT.mkdir(exist_ok=True)
(DATA / "nofly").mkdir(exist_ok=True)
FALLBACK_BUFFER_M = 3000  # assumption, stated in the report

PDOK_WFS = "https://service.pdok.nl/lvnl/drone-no-flyzones/wfs/v1_0"
OPENAIP_NL = "https://storage.googleapis.com/29f98e10-a489-4c82-ae5e-489dbcd4912f/nl_asp.geojson"
OURAIRPORTS_RUNWAYS = "https://davidmegginson.github.io/ourairports-data/runways.csv"


def pdok_wfs():
    try:
        r = get(PDOK_WFS, params={"service": "WFS", "request": "GetCapabilities"}, retries=1)
        ok = r.status_code == 200 and "FeatureType" in r.text
        log("PDOK no-fly zones (old WFS)", ok, f"HTTP {r.status_code}" + ("" if ok else " (retired with the OGC API)"))
    except Exception as e:  # noqa: BLE001
        log("PDOK no-fly zones (old WFS)", False, str(e))


def openaip():
    from shapely.geometry import box, shape
    try:
        r = get(OPENAIP_NL, retries=2)
        r.raise_for_status()
        fc = r.json()
    except Exception as e:  # noqa: BLE001
        log("openAIP airspace export (NL)", False, str(e))
        return
    ctx = box(*CONTEXT_WGS84)
    keep = []
    for f in fc.get("features", []):
        try:
            if f.get("geometry") and shape(f["geometry"]).intersects(ctx):
                keep.append(f)
        except Exception:  # noqa: BLE001
            continue
    (OUT / "openaip_nl_asp.geojson").write_text(json.dumps(fc), encoding="utf-8")
    (OUT / "openaip_eheh_context.geojson").write_text(
        json.dumps({"type": "FeatureCollection", "features": keep}), encoding="utf-8")
    names = sorted({str(f["properties"].get("name")) for f in keep})[:20]
    log("openAIP airspace export (NL)", bool(keep),
        f"{len(fc.get('features', []))} NL airspaces, {len(keep)} touch the EHEH context box: {names}",
        n_total=len(fc.get("features", [])), n_context=len(keep), names=names)


def runway_fallback():
    from pyproj import Transformer
    from shapely.geometry import LineString, mapping
    from shapely.ops import transform
    try:
        r = get(OURAIRPORTS_RUNWAYS)
        r.raise_for_status()
    except Exception as e:  # noqa: BLE001
        log("OurAirports runways (EHEH)", False, str(e))
        return
    rows = [x for x in csv.DictReader(io.StringIO(r.text)) if x["airport_ident"] == AIRPORT_ICAO]
    lines = []
    for x in rows:
        try:
            lines.append(LineString([(float(x["le_longitude_deg"]), float(x["le_latitude_deg"])),
                                     (float(x["he_longitude_deg"]), float(x["he_latitude_deg"]))]))
        except ValueError:
            continue
    if not lines:
        log("OurAirports runways (EHEH)", False, f"{len(rows)} rows, no threshold coordinates")
        return
    to_rd = Transformer.from_crs(4326, 28992, always_xy=True).transform
    to_wgs = Transformer.from_crs(28992, 4326, always_xy=True).transform
    feats = []
    for x, ln in zip(rows, lines):
        rd = transform(to_rd, ln)
        zone = transform(to_wgs, rd.buffer(FALLBACK_BUFFER_M))
        feats.append({"type": "Feature", "geometry": mapping(zone), "properties": {
            "name": f"EHEH runway {x['le_ident']}/{x['he_ident']} buffer {FALLBACK_BUFFER_M} m",
            "localtype": "ASSUMPTION - not an official zone",
            "runway_length_m": round(rd.length), "surface": x["surface"]}})
    (DATA / "nofly" / "runway_buffer_fallback.geojson").write_text(
        json.dumps({"type": "FeatureCollection", "features": feats}), encoding="utf-8")
    desc = ", ".join(f"{x['le_ident']}/{x['he_ident']} {x['length_ft']} ft {x['surface']}" for x in rows)
    log("OurAirports runways (EHEH)", True,
        f"{len(rows)} runway(s): {desc}; fallback zone = {FALLBACK_BUFFER_M} m buffer around the centreline (assumption)",
        runways=rows)


def main():
    pdok_wfs()
    openaip()
    runway_fallback()
    return 0


if __name__ == "__main__":
    sys.exit(main())

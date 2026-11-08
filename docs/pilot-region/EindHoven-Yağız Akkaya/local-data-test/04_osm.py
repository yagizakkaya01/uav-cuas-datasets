"""OpenStreetMap via the Overpass API: airport features, buildings, roads, land use.

Output: data/osm/osm.geojson (WGS84) and data/osm/raw.json
"""
import json
import sys
from collections import Counter

from common import get, log
from config import AOI_WGS84, DATA

ENDPOINTS = ["https://overpass-api.de/api/interpreter",
             "https://overpass.kumi.systems/api/interpreter"]
OUT = DATA / "osm"
OUT.mkdir(exist_ok=True)


def query():
    w, s, e, n = AOI_WGS84
    bb = f"({s},{w},{n},{e})"
    return f"""[out:json][timeout:120];
(
  nwr["aeroway"]{bb};
  way["building"]{bb};
  way["highway"]{bb};
  way["landuse"]{bb};
  way["natural"]{bb};
  nwr["military"]{bb};
  nwr["man_made"~"tower|mast|antenna"]{bb};
);
out geom tags;"""


def to_geojson(elements):
    feats = []
    for el in elements:
        tags = el.get("tags", {})
        if el["type"] == "node":
            geom = {"type": "Point", "coordinates": [el["lon"], el["lat"]]}
        elif el["type"] == "way" and "geometry" in el:
            pts = [[p["lon"], p["lat"]] for p in el["geometry"]]
            closed = len(pts) > 3 and pts[0] == pts[-1]
            area = closed and ("building" in tags or "landuse" in tags or "natural" in tags
                               or tags.get("aeroway") in ("apron", "aerodrome", "hangar", "terminal"))
            geom = {"type": "Polygon", "coordinates": [pts]} if area else {"type": "LineString", "coordinates": pts}
        else:
            continue  # relations are kept in raw.json only
        feats.append({"type": "Feature", "properties": {"osm_id": f"{el['type']}/{el['id']}", **tags},
                      "geometry": geom})
    return {"type": "FeatureCollection", "features": feats}


def main():
    last = None
    for ep in ENDPOINTS:
        try:
            r = get(ep, params={"data": query()}, timeout=180)
            r.raise_for_status()
            j = r.json()
            break
        except Exception as e:  # noqa: BLE001
            last = e
    else:
        log("OpenStreetMap (Overpass)", False, f"all endpoints failed: {last}")
        return 1
    (OUT / "raw.json").write_text(json.dumps(j), encoding="utf-8")
    fc = to_geojson(j.get("elements", []))
    (OUT / "osm.geojson").write_text(json.dumps(fc), encoding="utf-8")
    P = [f["properties"] for f in fc["features"]]
    aeroway = Counter(p["aeroway"] for p in P if "aeroway" in p)
    bld = sum(1 for p in P if "building" in p)
    bld_h = sum(1 for p in P if "building" in p and ("height" in p or "building:levels" in p))
    roads = sum(1 for p in P if "highway" in p)
    log(
        "OpenStreetMap (Overpass)", True,
        f"{len(P)} features: {bld} buildings ({bld_h} with height/levels), {roads} road segments, "
        f"aeroway {dict(aeroway)}",
        buildings=bld, buildings_with_height=bld_h, roads=roads, aeroway=dict(aeroway),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

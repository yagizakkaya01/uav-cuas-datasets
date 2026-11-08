"""3DBAG: every building in the AOI with LiDAR-derived roof and ground heights.

API: https://api.3dbag.nl (OGC API Features, CityJSON features). Pages through
/collections/pand/items for the AOI bbox (RD New) and extracts, per building,
the LoD0 footprint plus height attributes.
Output: data/3dbag/buildings.geojson (EPSG:28992), data/3dbag/raw_page_*.json
"""
import json
import sys

from common import get, log
from config import AOI_RD, DATA

API = "https://api.3dbag.nl/collections/pand/items"
OUT = DATA / "3dbag"
OUT.mkdir(exist_ok=True)
KEEP = ["b3_h_dak_max", "b3_h_dak_50p", "b3_h_dak_70p", "b3_h_maaiveld",
        "oorspronkelijkbouwjaar", "b3_dak_type", "status"]


def to_xyz(idx, verts, tf):
    v = verts[idx]
    if tf:
        s, t = tf["scale"], tf["translate"]
        return [v[0] * s[0] + t[0], v[1] * s[1] + t[1], v[2] * s[2] + t[2]]
    return v


def footprint(feature, tf):
    """Outer ring of the LoD0 surface of the main Building object (2D)."""
    verts = feature.get("vertices", [])
    for obj in feature.get("CityObjects", {}).values():
        if obj.get("type") != "Building":
            continue
        for g in obj.get("geometry", []):
            if str(g.get("lod")) in ("0", "0.0"):
                ring = g["boundaries"][0][0]
                pts = [to_xyz(i, verts, tf)[:2] for i in ring]
                return pts + [pts[0]], obj.get("attributes", {})
        return None, obj.get("attributes", {})
    return None, {}


def main():
    x0, y0, x1, y1 = AOI_RD
    url, params = API, {"bbox": f"{x0},{y0},{x1},{y1}", "limit": 100}
    feats, page, tf = [], 0, None
    try:
        while url:
            r = get(url, params=params)
            r.raise_for_status()
            j = r.json()
            (OUT / f"raw_page_{page:03d}.json").write_text(json.dumps(j), encoding="utf-8")
            tf = (j.get("metadata") or {}).get("transform", tf)
            for f in j.get("features", []):
                ring, attrs = footprint(f, f.get("transform", tf))
                props = {"id": f.get("id")} | {k: attrs.get(k) for k in KEEP}
                if props.get("b3_h_dak_max") is not None and props.get("b3_h_maaiveld") is not None:
                    props["height_above_ground_m"] = round(props["b3_h_dak_max"] - props["b3_h_maaiveld"], 2)
                feats.append({
                    "type": "Feature", "properties": props,
                    "geometry": {"type": "Polygon", "coordinates": [ring]} if ring else None,
                })
            nxt = [l["href"] for l in j.get("links", []) if l.get("rel") == "next"]
            url, params = (nxt[0], None) if nxt else (None, None)
            page += 1
            print(f"  3DBAG page {page}: {len(feats)} buildings so far")
    except Exception as e:  # noqa: BLE001
        log("3DBAG API", False, f"failed on page {page}: {e}", buildings_so_far=len(feats))
        if not feats:
            return 1

    fc = {"type": "FeatureCollection",
          "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:EPSG::28992"}},
          "features": feats}
    (OUT / "buildings.geojson").write_text(json.dumps(fc), encoding="utf-8")
    h = [f["properties"]["height_above_ground_m"] for f in feats
         if f["properties"].get("height_above_ground_m") is not None]
    geo = sum(1 for f in feats if f["geometry"])
    log(
        "3DBAG API", True,
        f"{len(feats)} buildings, {geo} with LoD0 footprint, {len(h)} with roof+ground height; "
        f"height above ground mean {sum(h)/max(len(h),1):.1f} m, max {max(h, default=0):.1f} m",
        buildings=len(feats), with_footprint=geo, with_height=len(h), pages=page,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

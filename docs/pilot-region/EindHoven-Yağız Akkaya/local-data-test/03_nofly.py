"""LVNL drone no-fly zones (PDOK OGC API Features, licence PDM 1.0).

NOTE: PDOK retired this dataset on 30 June 2026 at LVNL's request; the API now
returns 404. The script is kept so the failure is reproducible.

Lists the collections, then downloads every feature intersecting the context box.
Output: data/nofly/<collection>.geojson (WGS84)
"""
import json
import sys
from collections import Counter

from common import get, log
from config import CONTEXT_WGS84, DATA

API = "https://api.pdok.nl/lvnl/drone-no-flyzones/ogc/v1"
OUT = DATA / "nofly"
OUT.mkdir(exist_ok=True)


def items(coll):
    url = f"{API}/collections/{coll}/items"
    params = {"bbox": ",".join(map(str, CONTEXT_WGS84)), "f": "json", "limit": 1000}
    feats = []
    while url:
        r = get(url, params=params, headers={"Accept": "application/geo+json"})
        r.raise_for_status()
        j = r.json()
        feats += j.get("features", [])
        nxt = [l["href"] for l in j.get("links", []) if l.get("rel") == "next"]
        url, params = (nxt[0], None) if nxt else (None, None)
    return feats


def main():
    try:
        r = get(f"{API}/collections", params={"f": "json"})
        r.raise_for_status()
        colls = [c["id"] for c in r.json().get("collections", [])]
    except Exception as e:  # noqa: BLE001
        log("PDOK drone no-fly zones", False, f"collections failed: {e}")
        return 1
    summary = {}
    for c in colls:
        try:
            feats = items(c)
        except Exception as e:  # noqa: BLE001
            summary[c] = f"error: {e}"
            continue
        (OUT / f"{c}.geojson").write_text(
            json.dumps({"type": "FeatureCollection", "features": feats}), encoding="utf-8")
        types = Counter(str(f["properties"].get("localtype") or f["properties"].get("type")) for f in feats)
        names = sorted({str(f["properties"].get("name") or f["properties"].get("naam") or "")
                        for f in feats} - {""})[:15]
        summary[c] = {"features": len(feats), "types": dict(types), "example_names": names}
    ok = any(isinstance(v, dict) and v["features"] > 0 for v in summary.values())
    detail = "; ".join(f"{k}: {v['features'] if isinstance(v, dict) else v}" for k, v in summary.items())
    log("PDOK drone no-fly zones", ok, f"collections {colls}; features in context box -> {detail}",
        summary=summary)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

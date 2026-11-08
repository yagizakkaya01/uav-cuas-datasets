"""OpenSky Network: live traffic near EHEH and the 22 Nov 2025 incident window.

1. Live state vectors in the airport box (anonymous access).
2. Arrivals/departures at EHEH for the incident evening and a reference evening
   one week earlier. Historical flight lists usually need an account: set
   OPENSKY_CLIENT_ID and OPENSKY_CLIENT_SECRET (OAuth2 API client, free account)
   to use it. Without them the script records what anonymous access returns.
Output: data/opensky/*.json
"""
import json
import os
import sys
from datetime import datetime, timezone

from common import get, log, SESSION
from config import AIRPORT_ICAO, DATA, INCIDENT_UTC, REFERENCE_UTC

API = "https://opensky-network.org/api"
TOKEN_URL = "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token"
OUT = DATA / "opensky"
OUT.mkdir(exist_ok=True)


def ts(s):
    # timezone-aware: naive datetime(1970,1,1).timestamp() raises OSError (Errno 22) on Windows
    return int(datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp())


def auth_headers():
    cid, sec = os.getenv("OPENSKY_CLIENT_ID"), os.getenv("OPENSKY_CLIENT_SECRET")
    if not (cid and sec):
        return {}
    r = SESSION.post(TOKEN_URL, data={"grant_type": "client_credentials",
                                      "client_id": cid, "client_secret": sec}, timeout=30)
    r.raise_for_status()
    return {"Authorization": f"Bearer {r.json()['access_token']}"}


def main():
    try:
        hdr = auth_headers()
    except Exception as e:  # noqa: BLE001
        print(f"  OpenSky auth failed, continuing anonymously: {e}")
        hdr = {}
    mode = "authenticated" if hdr else "anonymous"

    # 1. live
    try:
        r = get(f"{API}/states/all", params={"lamin": 51.40, "lomin": 5.30, "lamax": 51.50, "lomax": 5.50},
                headers=hdr)
        r.raise_for_status()
        j = r.json()
        (OUT / "live_states.json").write_text(json.dumps(j), encoding="utf-8")
        st = j.get("states") or []
        calls = [(s[1] or "").strip() for s in st]
        log("OpenSky live states", True, f"{len(st)} aircraft in airport box ({mode}): {calls[:10]}")
    except Exception as e:  # noqa: BLE001
        log("OpenSky live states", False, f"{mode}: {e}")

    # 2. history
    res = {}
    for label, (b, e) in {"incident_2025-11-22": INCIDENT_UTC, "reference_2025-11-15": REFERENCE_UTC}.items():
        for kind in ("arrival", "departure"):
            try:
                r = get(f"{API}/flights/{kind}",
                        params={"airport": AIRPORT_ICAO, "begin": ts(b), "end": ts(e)}, headers=hdr, retries=1)
                if r.status_code == 200:
                    j = r.json()
                    (OUT / f"{label}_{kind}.json").write_text(json.dumps(j), encoding="utf-8")
                    times = sorted(datetime.utcfromtimestamp(
                        f.get("lastSeen" if kind == "arrival" else "firstSeen")).strftime("%H:%M") for f in j)
                    res[f"{label}/{kind}"] = {"n": len(j), "times_utc": times}
                else:
                    res[f"{label}/{kind}"] = f"HTTP {r.status_code}"
            except Exception as ex:  # noqa: BLE001
                res[f"{label}/{kind}"] = f"error: {ex}"
    ok = any(isinstance(v, dict) for v in res.values())
    brief = {k: (v["n"] if isinstance(v, dict) else v) for k, v in res.items()}
    log("OpenSky history (EHEH, 22 Nov 2025)", ok, f"{mode}: {brief}", flights=res)
    return 0


if __name__ == "__main__":
    sys.exit(main())

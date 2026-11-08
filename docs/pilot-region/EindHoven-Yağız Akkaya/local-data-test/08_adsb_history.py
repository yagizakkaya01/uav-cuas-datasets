"""Historical ADS-B for the incident evening from the adsb.lol open archive (ODbL 1.0).

OpenSky history needs an account, so this uses the adsb.lol "globe_history" daily dumps
(GitHub releases, one tar split into parts per day). For 22 Nov 2025 (incident) and
15 Nov 2025 (reference, same weekday) it downloads the day, streams every aircraft trace
and keeps points within RADIUS_KM of the EHEH reference point, below ALT_FT, between
17:00 and 24:00 UTC. It then counts aircraft per 15-minute bin.

Each day is a few GB. Set ADSB_MAX_GB (default 8) to cap the download per day and
ADSB_KEEP_RAW=1 to keep the tar parts after processing (default: deleted).
Output: data/adsb/<day>_eheh.json, results/eindhoven-adsb-incident-night.png
"""
import gzip
import json
import math
import os
import sys
import tarfile
from collections import defaultdict
from datetime import datetime, timezone

from common import SESSION, get, log
from config import DATA, RESULTS

REPO = "adsblol/globe_history_{year}"   # archive is split per year (old repo redirects to _2026)
DAYS = {"incident": "2025.11.22", "reference": "2025.11.15"}
EHEH = (51.4501, 5.3745)          # aerodrome reference point (approx.)
RADIUS_KM, ALT_FT = 15.0, 5000
WINDOW_UTC = (17, 24)
OUT = DATA / "adsb"
OUT.mkdir(exist_ok=True)
MAX_GB = float(os.getenv("ADSB_MAX_GB", "8"))
KEEP = os.getenv("ADSB_KEEP_RAW") == "1"


def km(lat1, lon1, lat2, lon2):
    p = math.pi / 180
    a = (math.sin((lat2 - lat1) * p / 2) ** 2 +
         math.cos(lat1 * p) * math.cos(lat2 * p) * math.sin((lon2 - lon1) * p / 2) ** 2)
    return 12742 * math.asin(math.sqrt(a))


def find_release(day):
    for tag in (f"v{day}-planes-readsb-prod-0", f"v{day}-planes-readsb-prod-1", f"v{day}"):
        r = get(f"https://api.github.com/repos/{REPO.format(year=day[:4])}/releases/tags/{tag}", retries=1)
        if r.status_code == 200 and r.json().get("assets"):
            return r.json()
    return None


class Concat:
    """Read several files as one stream (the tar is split into .aa, .ab, ...)."""
    def __init__(self, paths):
        self.files = [open(p, "rb") for p in paths]
        self.i = 0

    def read(self, n=-1):
        out = b""
        while self.i < len(self.files) and (n < 0 or len(out) < n):
            chunk = self.files[self.i].read(-1 if n < 0 else n - len(out))
            if not chunk:
                self.files[self.i].close()
                self.i += 1
            out += chunk
        return out


def scan(paths, day):
    base_day = datetime.strptime(day, "%Y.%m.%d").replace(tzinfo=timezone.utc)
    t0 = base_day.timestamp() + WINDOW_UTC[0] * 3600
    t1 = base_day.timestamp() + WINDOW_UTC[1] * 3600
    bins, flights, n_traces = defaultdict(set), {}, 0
    with tarfile.open(fileobj=Concat(paths), mode="r|") as tar:
        for m in tar:
            if not (m.isfile() and "trace" in m.name and m.name.endswith(".json")):
                continue
            raw = tar.extractfile(m).read()
            n_traces += 1
            try:
                j = json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)
            except Exception:  # noqa: BLE001
                continue
            ts0 = j.get("timestamp", 0)
            hexid = j.get("icao")
            for pt in j.get("trace", []):
                t = ts0 + pt[0]
                if not (t0 <= t < t1):
                    continue
                lat, lon, alt = pt[1], pt[2], pt[3]
                if lat is None or lon is None:
                    continue
                if alt != "ground" and (alt is None or alt > ALT_FT):
                    continue
                if km(lat, lon, *EHEH) > RADIUS_KM:
                    continue
                b = int((t - base_day.timestamp()) // 900)
                bins[b].add(hexid)
                info = pt[8] if len(pt) > 8 and isinstance(pt[8], dict) else {}
                f = flights.setdefault(hexid, {"first": t, "last": t, "callsign": None, "type": j.get("t")})
                f["last"] = t
                if info.get("flight"):
                    f["callsign"] = info["flight"].strip()
    series = {f"{b // 4:02d}:{(b % 4) * 15:02d}": len(v) for b, v in sorted(bins.items())}
    for f in flights.values():
        f["first"] = datetime.fromtimestamp(f["first"], timezone.utc).strftime("%H:%M")
        f["last"] = datetime.fromtimestamp(f["last"], timezone.utc).strftime("%H:%M")
    return {"traces_scanned": n_traces, "aircraft": len(flights), "per_15min_utc": series, "flights": flights}


def download(rel, label):
    assets = sorted([a for a in rel["assets"] if ".tar" in a["name"]], key=lambda a: a["name"])
    gb = sum(a["size"] for a in assets) / 1e9
    if gb > MAX_GB:
        raise RuntimeError(f"{gb:.1f} GB > ADSB_MAX_GB={MAX_GB}")
    paths = []
    for a in assets:
        p = OUT / a["name"]
        if not (p.exists() and p.stat().st_size == a["size"]):
            print(f"  downloading {a['name']} ({a['size']/1e6:.0f} MB)")
            with SESSION.get(a["browser_download_url"], stream=True, timeout=600) as r:
                r.raise_for_status()
                with open(p, "wb") as fh:
                    for chunk in r.iter_content(1 << 20):
                        fh.write(chunk)
        paths.append(p)
    return paths, gb


def plot(results):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    labels = [f"{h:02d}:{m:02d}" for h in range(*WINDOW_UTC) for m in (0, 15, 30, 45)]
    fig, ax = plt.subplots(figsize=(11, 4), dpi=150)
    for (name, res), off, col in zip(results.items(), (-0.2, 0.2), ("#d62728", "#7f7f7f")):
        y = [res["per_15min_utc"].get(lb, 0) for lb in labels]
        ax.bar([i + off for i in range(len(labels))], y, width=0.4, color=col,
               label=f"{name} ({DAYS[name]})")
    ax.axvspan(labels.index("19:30") - 0.5, labels.index("21:45") + 0.5, color="orange", alpha=0.15,
               label="reported closure ~20:30-22:40 local (19:30-21:40 UTC)")
    ax.set_xticks(range(0, len(labels), 2))
    ax.set_xticklabels(labels[::2], rotation=45, fontsize=7)
    ax.set_ylabel(f"aircraft < {ALT_FT} ft within {RADIUS_KM:.0f} km")
    ax.set_title("EHEH low-altitude ADS-B traffic per 15 min (adsb.lol open archive)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(RESULTS / "eindhoven-adsb-incident-night.png")


def main():
    results = {}
    for label, day in DAYS.items():
        try:
            rel = find_release(day)
            if not rel:
                log(f"adsb.lol history {day}", False, "no release found for this date")
                continue
            paths, gb = download(rel, label)
            res = scan(paths, day)
            (OUT / f"{day}_eheh.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
            results[label] = res
            log(f"adsb.lol history {day}", True,
                f"{gb:.1f} GB, {res['traces_scanned']} traces scanned; {res['aircraft']} aircraft below "
                f"{ALT_FT} ft within {RADIUS_KM:.0f} km of EHEH, 17-24 UTC",
                per_15min_utc=res["per_15min_utc"])
            if not KEEP:
                for p in paths:
                    p.unlink()
        except Exception as e:  # noqa: BLE001
            log(f"adsb.lol history {day}", False, str(e))
    if results:
        plot(results)
    return 0


if __name__ == "__main__":
    sys.exit(main())

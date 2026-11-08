"""Small helpers: HTTP with retries and a JSON access log."""
import json
import time
from datetime import datetime, timezone

import requests

from config import RESULTS, TIMEOUT, USER_AGENT

LOG_FILE = RESULTS / "access-log.json"
SESSION = requests.Session()
SESSION.headers["User-Agent"] = USER_AGENT


def get(url, params=None, retries=3, **kw):
    """GET with simple retry/backoff. Returns the Response (raises on final failure)."""
    last = None
    for i in range(retries):
        try:
            r = SESSION.get(url, params=params, timeout=kw.pop("timeout", TIMEOUT), **kw)
            if r.status_code in (429, 502, 503, 504):
                raise requests.HTTPError(f"{r.status_code}", response=r)
            return r
        except requests.RequestException as e:  # noqa: PERF203
            last = e
            time.sleep(2 ** (i + 1))
    raise last


def log(source, ok, detail, **extra):
    """Append one row to results/access-log.json and print it."""
    rows = json.loads(LOG_FILE.read_text(encoding="utf-8")) if LOG_FILE.exists() else []
    rows = [r for r in rows if r["source"] != source]
    row = {
        "source": source,
        "ok": bool(ok),
        "detail": detail,
        "tested_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        **extra,
    }
    rows.append(row)
    LOG_FILE.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(("[OK]   " if ok else "[FAIL] ") + f"{source}: {detail}")
    return row

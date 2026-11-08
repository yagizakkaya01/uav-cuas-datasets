"""Shared settings for the Eindhoven local data test."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"          # raw downloads (not committed)
RESULTS = ROOT / "results"    # small outputs that can be committed

# Area of interest: Eindhoven Airport / Air Base (EHEH), about 4.5 x 3.3 km
AOI_WGS84 = (5.355, 51.440, 5.420, 51.470)            # lon_min, lat_min, lon_max, lat_max
AOI_RD = (152761, 383434, 157279, 386772)             # EPSG:28992 (RD New), same box

# Wider context box for airspace (no-fly zones are larger than the AOI)
CONTEXT_WGS84 = (5.20, 51.36, 5.58, 51.56)

AIRPORT_ICAO = "EHEH"
INCIDENT_UTC = ("2025-11-22T18:00:00Z", "2025-11-23T00:00:00Z")   # ~20:30-22:40 local (UTC+1)
REFERENCE_UTC = ("2025-11-15T18:00:00Z", "2025-11-16T00:00:00Z")  # same weekday, one week earlier

USER_AGENT = "uav-cuas-datasets-eindhoven-test/1.0 (METU NCC senior design project)"
TIMEOUT = 60

for d in (DATA, RESULTS):
    d.mkdir(parents=True, exist_ok=True)

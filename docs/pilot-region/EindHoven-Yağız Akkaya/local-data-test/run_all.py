"""Run every data test in order, then build the map and the report."""
import importlib
import sys
import traceback

STEPS = ["01_ahn", "02_3dbag", "03_nofly", "04_osm", "05_opensky", "07_airspace", "08_adsb_history",
         "09_extra_layers", "06_summary"]

if __name__ == "__main__":
    only = sys.argv[1:] or STEPS
    for name in STEPS:
        if not any(name.startswith(o) for o in only):
            continue
        print(f"\n=== {name} ===")
        try:
            importlib.import_module(name).main()
        except Exception:  # noqa: BLE001
            traceback.print_exc()
    print("\nDone. See results/data-test-report.md")

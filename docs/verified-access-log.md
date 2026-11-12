# Verified Access Log

[← Back to README](../README.md)

> A running log of sources the team has **personally accessed, downloaded, or tested** — not just found in a search. This is the strongest form of evidence for the advisor: proof of actual reachability, not just a link that theoretically works.

> 🇹🇷 **Kısaca:** Ekibimizin bizzat açıp indirdiği ve çalıştığını doğruladığı kaynakların kaydı. Her satırda tarih, kaynak ve sonucu yer alır.

---

| Date | Source | Layer | Verified By | Outcome |
|---|---|:---:|---|---|
| 2026-09-15 | [OpenStreetMap — Turkey extract (Geofabrik)](https://download.geofabrik.de/europe/turkey.html) | 1 | Yağız Akkaya | ✅ `.osm.pbf` downloadable, confirmed working |
| 2026-09-15 | [ALOS World 3D-30m (AW3D30) — OpenTopography](https://portal.opentopography.org/dataCatalog) | 1 | Yağız Akkaya | ✅ Listed as "Open Data", direct download button confirmed, covers Turkey |
| 2026-11-08 | [AHN 0.5 m DSM + DTM (PDOK WCS)](https://www.pdok.nl) — Eindhoven AOI | 1 | Yağız Akkaya | ✅ 40 tiles mosaicked, 9036 × 6676 px |
| 2026-11-08 | [3DBAG API](https://3dbag.nl) — Eindhoven AOI | 1 | Yağız Akkaya | ✅ 3,472 buildings, 3,464 with heights |
| 2026-11-08 | OpenStreetMap (Overpass) — Eindhoven AOI | 1 | Yağız Akkaya | ✅ 8,295 features incl. runway, taxiways, hangars |
| 2026-11-08 | [OpenSky Network](https://opensky-network.org) live states | 1 | Yağız Akkaya | ✅ anonymous query worked |
| 2026-11-08 | OpenSky history (EHEH, 22 Nov 2025) | 1 | Yağız Akkaya | ❌ HTTP 403 without an account; replaced by adsb.lol |
| 2026-11-08 | adsb.lol history archive, 22 Nov 2025 and 15 Nov 2025 | 1 | Yağız Akkaya | ✅ two day archives (~3 GB each) scanned |
| 2026-11-08 | PDOK drone no-fly zones (OGC API and old WFS) | 1 | Yağız Akkaya | ❌ HTTP 404, retired 30 Jun 2026 |
| 2026-11-08 | openAIP airspace export (NL) | 1 | Yağız Akkaya | ❌ anonymous download closed |
| 2026-11-08 | PDOK Defensie aviation obstacle reports | 1 | Yağız Akkaya | ✅ API reachable, 0 reports in the box |
| 2026-11-08 | OurAirports runways (EHEH) | 1 | Yağız Akkaya | ✅ runway 03/21 with thresholds |
| 2026-11-08 | ESA WorldCover 10 m (2021) | 1 | Yağız Akkaya | ✅ clipped to the AOI |
| 2026-11-08 | Copernicus DEM GLO-30 | 1 | Yağız Akkaya | ✅ clipped; 3.27 m RMSE against AHN |
| 2026-11-08 | KNMI hourly weather, station 370 | 1 | Yağız Akkaya | ✅ 22 Nov 2025 retrieved |

The 8 November rows come from the Eindhoven local data test; details are in its [results report](./pilot-region/EindHoven-Ya%C4%9F%C4%B1z%20Akkaya/local-data-test/results/data-test-report.md). Tests of the other candidate regions are recorded in their own folders under [`pilot-region/`](./pilot-region/).

---

## Log Template

```markdown
| YYYY-MM-DD | [Source Name](link) | Layer # | Your Name | ✅/⚠️/❌ + one-line outcome note |
```

Use ⚠️ for partial success (e.g. "download started but very slow" or "GUI failed, used API instead") and ❌ for a documented failed attempt (still useful — proves due diligence).

[← Back to README](../README.md)

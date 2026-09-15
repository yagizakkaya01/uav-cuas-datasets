# Layer 1 — Geospatial & Sensor Data Ingestion

![Sources](https://img.shields.io/badge/sources-19-informational)

This layer handles terrain modeling, road/building context, baseline air-traffic patterns, real UAV detection/tracking sensor data, and real-world incident geolocation. It is the foundation the grid/graph engine (Layer 3) and the fusion layer (Layer 4) build on.

> 🇹🇷 **Kısaca:** Sistemin temel verileri burada. Arazinin yükseklik haritası, yollar ve binalar, normal hava trafiği, kamera/radar/ses ile kaydedilmiş gerçek dron tespit verileri ve daha önce yaşanmış dron olaylarının konumları bu katmanda yer alır.

[← Back to README](../README.md)

---

## 1.1 Terrain / GIS

| Source | Status | License | Notes |
|---|:---:|---|---|
| **[Copernicus DEM GLO-30 — OpenTopography](https://opentopography.org)** | 🟡 | Free, attribution required (DLR/Airbus/ESA) | Global DSM, 30 m resolution, COG/GeoTIFF. **What to look for:** on the Data Catalog page, find "Copernicus 30m Global DEM" → "Get Copernicus 30m Data" → draw your AOI bounding box → select product type **DSM**, format **GeoTIFF**. Excluded countries: only Armenia & Azerbaijan — Turkey is fully covered. |
| **[Copernicus DEM — AWS Registry of Open Data](https://registry.opendata.aws/copernicus-dem)** | 🟡 | Free, attribution required | Direct S3 bucket access (`copernicus-dem-30m`) if the web GUI is unreliable — pull tiles by lat/lon tile name (`Copernicus_DSM_COG_30_N**_00_E**_00_DEM`). |
| **[Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu)** | 🟡 | Free, attribution required | Register → "Copernicus Browser" → add DEM layer → draw AOI → download GLO-30 DGED product. |
| **[ALOS World 3D-30m (AW3D30) — OpenTopography](https://portal.opentopography.org/dataCatalog)** | ✅ | Free (JAXA) | **Personally verified — accessible.** Global DSM, 30 m, coverage to ~82° N/S (includes Turkey). Vertical datum EGM1996 (differs from Copernicus's EGM2008 — reconcile when merging). Easier GUI download than Copernicus; used as primary terrain source, cross-checked against GLO-30. |
| **[OpenStreetMap — Geofabrik extracts](https://download.geofabrik.de)** | 🟡 | ODbL (share-alike) | **[Turkey extract](https://download.geofabrik.de/europe/turkey.html) — personally verified.** Download `.osm.pbf`, filter tags with `osmium tags-filter` before loading: `highway=*` (road network), `building=*`, `landuse=military` / `military=*` (facility boundaries), `aeroway=*` (airports), `natural=water` / `natural=wood` (terrain cover). Load into PostGIS with `osm2pgsql --slim`. |

## 1.2 Baseline Air-Traffic / Track Data

| Source | Status | License | Notes |
|---|:---:|---|---|
| **[OpenSky Network](https://opensky-network.org)** | 🟡 | Free for academic/research use; commercial use requires separate license | Use the **Trino/SQL interface**, not the 30-day-limited REST API, for historical bulk data. Query `state_vectors_data4` for `icao24, callsign, lat, lon, baro_altitude, velocity, heading, vertical_rate, time`, filtered to your AOI bounding box over at least a few weeks (to derive statistically meaningful "normal traffic" patterns). |
| **[pyopensky](https://github.com/open-aviation/pyopensky)** | 🟢 | Open | Python client for the Trino interface — follow the README for connection setup and example queries. |

## 1.3 Real UAV Detection & Tracking Datasets (vision / IR / RF / acoustic)

| Source | Status | License | Notes |
|---|:---:|---|---|
| **[DUT Anti-UAV](https://github.com/wangdongdut/DUT-Anti-UAV)** | 🟢 | MIT | 10,000 annotated images (detection) + 20 tracking videos. Google/Baidu Drive links in repo. |
| **[UAVSwarm](https://github.com/UAVSwarm/UAVSwarm-dataset)** | 🟢 | CC BY 4.0 | 72 sequences, MOT-format bounding boxes — multi-target/swarm tracking validation. |
| **[MMAUD](https://github.com/ntu-aris/MMAUD)** | 🟡 | CC BY-NC-SA 4.0 (dataset), MIT (code) | Multi-modal: stereo RGB + 2× LiDAR + mmWave radar + 4-node microphone array. ROS bags + 3D trajectory labels. UG2+ 2024 subset (102 train / 16 val) recommended starting point. |
| **[Halmstad multi-sensor dataset](https://github.com/DroneDetectionThesis/Drone-detection-dataset)** | 🟢 | Open (CC-BY family) | 650 videos (365 IR + 285 visible) + 90 audio clips, 203K+ annotated frames. Labels in `.mat` — decode with the repo's `mcos-decoder`. |
| **[Anti-UAV (300/410/600 series)](https://github.com/ZhaoJ9014/Anti-UAV)** | 🔴 | MIT (project), but platform-gated access | Anti-UAV300 easiest (Google/Baidu Drive, password `sagx`). 410/600 require ModelScope account or Baidu-gated access. |
| **[Drone-vs-Bird Challenge](https://github.com/wosdetc/challenge)** | 🔴 | Request-only, signed DUA | Email wosdetc@googlegroups.com for a Data Usage Agreement — apply early, has lead time. |
| **[TIB-Net](https://github.com/kyn0v/TIB-Net)** | 🟢 | Open (CC-BY paper) | 2,850 images, PASCAL VOC XML format, tiny-target detection. |
| **[DroneRF (Mendeley Data)](https://data.mendeley.com)** | 🟢 | Open | RF signal segments, 3 drone models (Parrot Bebop, Parrot AR, DJI Phantom 3), >40 GB. |
| **[DroneDetect (IEEE DataPort)](https://ieee-dataport.org)** | 🟡 | Open, free login required | BladeRF SDR-collected RF data, 7 UAS models. |

## 1.4 Real-World Incident / Sighting Data (geolocated)

| Source | Status | License | Notes |
|---|:---:|---|---|
| **[FAA UAS Sighting Reports](https://www.faa.gov/uas/resources/public_records/uas_sightings_report)** | 🟢 | Public US government record | Quarterly Excel/PDF releases: date, time, city, state, narrative. |
| **[FAA data — cleaned version, Purdue PURR](https://purr.purdue.edu)** (DOI: `10.4231/H31Y-7197`) | 🟢 | CC0 | 6,551 structured records — much easier to work with than raw FAA releases. |
| **[ACLED](https://acleddata.com)** | 🔴 | Registration + tiered access | Register for myACLED → Data Export Tool → filter event type for drone/UAV sub-categories, region, lat/long. |
| **[ACLED — HDX mirror](https://data.humdata.org)** | 🔴 | Registration required | Country/region CSV exports. |
| **IISS Report (2026, European drone incidents)** | 🟢 | Open reading | Search iiss.org for "drone incidents Europe 2026" — analysis of 144 incidents across 13 European states. |

---

## Add a New Source

```markdown
| **[Name](link)** | 🟢/🟡/🔴 | license | notes + what specifically to search for/download |
```

[← Back to README](../README.md) · [Next: Layer 2 →](./02-semantic-threat-knowledge-base.md)

> **Status (6 November 2026):** The pilot region has not been decided yet. This document is the full rationale for the Eindhoven proposal; for the other candidates see [`README.md`](../README.md). Sources and data tests for Eindhoven are in [`eindhoven-sources-and-data-test.md`](./eindhoven-sources-and-data-test.md); the full local download test (8 Nov) is in [`local-data-test/`](./local-data-test/) and the peer-reviewed literature in [`eindhoven-literature-review.md`](./eindhoven-literature-review.md).

# Pilot Region Proposal: Eindhoven Airport / Eindhoven Air Base

*Prepared by Yağız Akkaya. First version 18–19 October 2026, translated and updated 6 November 2026.*

## Summary

We propose **Eindhoven Airport / Eindhoven Air Base (the Netherlands)** as the pilot region for the decision engine.

- **Area of interest (WGS84 bbox):** `5.355, 51.440, 5.420, 51.470` (about 4.5 × 3.3 km: the runway and its surroundings)
- **Why:** it is a joint civil–military airfield (fitting the NATO / C4ISR theme), it had a real, documented drone incident on 22 November 2025, and the Netherlands publishes some of the most detailed open geodata in the world (0.5 m LiDAR, a 3D model of every building, an official drone no-fly-zone API).
- **Scope:** the pilot region is used **only by the decision engine** (risk grid, line of sight, routing, map interface). The physical demo is small-scale and runs on campus; its measurements are never presented as if they were taken at Eindhoven.

## 1. Why Eindhoven

1. **Joint civil–military airfield.** Civil airlines and the Royal Netherlands Air Force share the same runway. The scenario can therefore be framed both as protection of critical civil infrastructure and as protection of a military site. The IISS report (p. 23) describes Eindhoven as a major commercial hub that co-hosts Royal Netherlands Air Force transport and refuelling aircraft.
2. **A real counter-UAS incident.** On 22 November 2025 all civil and military traffic at Eindhoven was halted for about two hours (about 20:30–22:40) after multiple drone sightings, and Ministry of Defence counter-drone systems were activated. The evening before, guards at nearby Volkel Air Base saw up to ten drones and the military fired at them from the ground. The full timeline and sources are in [`eindhoven-sources-and-data-test.md`](./eindhoven-sources-and-data-test.md).
3. **Open, high-resolution data for every layer the engine needs:**

| Decision-engine need | Source | Status (8 Nov 2026, local download test) |
|---|---|---|
| Surface and terrain model | AHN: 0.5 m DSM and DTM, CC0 | ✅ Downloaded: 0.5 m DSM + DTM for the whole AOI |
| Building heights for line of sight and masking | 3DBAG: every building in LoD 1.2 / 1.3 / 2.2 with LiDAR-measured roof and ground heights, CC BY 4.0 | ✅ Downloaded: 3,472 buildings, 3,464 with heights |
| Protected / restricted zones | LVNL drone no-fly zones, PDOK OGC API, PDM 1.0 | ❌ Retired by PDOK on 30 Jun 2026, no open source left; 3 km runway buffer used as an assumption |
| Normal air-traffic baseline | OpenSky Network | ✅ Live works; incident night covered by the adsb.lol archive |
| Roads and facilities | OpenStreetMap / Overture | ✅ OSM downloaded: 8,295 features, 3 runway ways, 113 taxiways, 25 hangars |

## 2. Scenario idea for the decision engine

- **Protected assets:** runway, apron, hangars and terminal, from OSM `aeroway=*` tags and the PDOK no-fly-zone polygon.
- **Air-traffic baseline:** arrivals and departures at Eindhoven from OpenSky, used to derive the normal approach corridors.
- **Threat:** the mock drone in the physical demo is mapped onto the airport surroundings with a scaled transformation (section 4). The engine scores the track by no-fly zone, runway approach corridor and building masking.
- **Recommendation:** based on doctrine documents such as ATP 3-01.81, e.g. "suspend flights", "point sensors to this sector", "safe evacuation route".
- **Validation:** compare the system's recommended response with the public timeline of the 22 November 2025 incident (duration of the traffic stop). The traffic gap that night may also be visible in OpenSky history (to be checked with a Trino query).

## 3. Alternatives considered

| Region | Advantage | Why not chosen |
|---|---|---|
| **Volkel Air Base (NL)** | Purely military; drone incidents in Nov–Dec 2025 | Very sensitive site with no civil traffic, so a weak OpenSky baseline; publishing an analysis of an active military base is risky |
| **Rotterdam The Hague Airport / Delft (NL)** | Same Dutch data quality, next to TU Delft | No military component |
| **Geilenkirchen (DE, NRW)** | NATO E-3A AWACS base; NRW 1 m LiDAR and LoD2 buildings | Purely military (same issue as Volkel) |
| **Switzerland** | Free 0.5 m data (swisstopo) in mountainous terrain | Useful only if terrain (relief) masking must be shown separately |
| **METU NCC campus (Northern Cyprus)** | Same place as the physical demo | Only 30 m global elevation models and OSM; no open high-resolution data (see section 5) |
| **Istanbul (TR)** | Richest data in Türkiye: 16 points/m² LiDAR, 25 cm DSM, ~1.5 million LoD2 buildings | Not openly downloadable; needs an institutional agreement with the municipality |
| **Military sites in Türkiye** | National context | Mapping and imaging restricted by Law No. 2565 on Military Forbidden Zones; no open data. Not recommended |
| **London Gatwick (UK)** | The best-known drone airport closure (Dec 2018); 1 m LiDAR; NATS UAS zones | Civil only; no open national building-height dataset. Strong second candidate (proposal by Yaren Duyan) |

**Known weakness of Eindhoven:** the Netherlands is flat, so masking comes mainly from buildings and trees rather than relief. For low-flying drones this is the realistic case; if relief masking must be shown, Switzerland can be added as a second scenario.

## 4. Linking the physical demo to the map

The small demo area on campus is mapped onto a part of the AOI with a scaled similarity transformation (scale + rotation + translation), e.g. 1 m in the demo area = 100 m on the ground. When the mock drone is detected, its measured position is transformed onto the map, and the decision engine runs on the real buildings, no-fly zones and air traffic of Eindhoven. The transformation is stored in a configuration file.

## 5. Selection history (summary)

The choice was made in three steps:

1. **Campus first (18 Oct).** When the demo was expected to use the real campus terrain, we evaluated METU NCC (bbox `33.008, 35.236, 33.037, 35.259`). We downloaded the Copernicus GLO-30 tile from AWS: elevation in the AOI ranges from 50 m to 152 m, but 30 m cells are too coarse for line of sight between nodes a few hundred metres apart. Overture showed 466 buildings, only 9 with height values. Republic of Cyprus high-resolution data (5 m DEM, building footprints) does not cover the north. We also found that the repository listed the Geofabrik **Turkey** OSM extract, while the campus is in the separate **Cyprus** extract.
2. **Data richness (18 Oct).** Ranked purely by open data, the Netherlands came first (AHN 0.5 m + 3DBAG), followed by Switzerland, Denmark (0.4 m), North Rhine-Westphalia and the USA (3DEP 1 m). A building count on the same source (Overture) gave buildings with height values: Delft 493, ITU Maslak 6, METU Ankara 6, METU NCC 9.
3. **Map only in the decision engine (19 Oct).** Once the demo was confirmed to be small-scale, the pilot region no longer had to be the demo site. With the NATO theme, the focus moved to a military site or airport, leading to Eindhoven.

## 6. Ethics and security

The repository is public. For a real, active military site we will **not publish detailed vulnerability outputs** (sensor blind spots, least-detected approach corridors), because such outputs could be misused even though the system is defensive.

- The repository keeps only open sources and the method.
- Eindhoven-specific risk maps and blind-spot analyses are shown in the report and the demo only (or published with shifted / anonymised coordinates).
- We will confirm this boundary with our supervisors.

## 7. Changes needed in the repository

- Add AHN, 3DBAG and PDOK no-fly zones to Layer 1 and log verified access in `docs/verified-access-log.md`.
- Keep AW3D30 / Copernicus 30 m as a wide-area or fallback source.
- Update the proposal sentence "Terrain is taken from the ALOS World 3D 30 m surface model" once the region is decided.

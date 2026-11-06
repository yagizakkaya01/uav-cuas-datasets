# Pilot Region Proposals / Pilot Bölge Önerileri

> **Status (6 Nov 2026): not yet decided.** Two candidates are on the table: **Eindhoven Airport (NL)** and **London Gatwick Airport (UK)**. Helsinki was proposed earlier and superseded by Gatwick.
>
> 🇹🇷 **Durum:** Pilot bölge kararı henüz verilmedi. Masada iki aday var: **Eindhoven Havalimanı** ve **Gatwick Havalimanı**. Helsinki ilk öneriydi, yerini Gatwick'e bıraktı.

The pilot region is used **only by the decision engine** (risk grid, line of sight, routing, map UI). The physical demo runs on campus (see [`../hardware/`](../hardware/)) and its measurements are never presented as if they were taken at the pilot region.

## Candidates

| | **Eindhoven Airport / Air Base (NL)** | **London Gatwick Airport (UK)** | Helsinki (FI) — superseded |
|---|---|---|---|
| Proposed by | Yağız Akkaya, CNG 3 (18–19 Oct 2026) | Yaren Duyan, CNG 1 (22 Oct 2026) | Yaren Duyan, CNG 1 (22 Oct 2026) |
| Document | [eindhoven-proposal.md](./eindhoven-proposal.md) · [talking points](./eindhoven-talking-points.md) | [gatwick-proposal.pdf](./gatwick-proposal.pdf) | [helsinki-proposal.pdf](./helsinki-proposal.pdf) |
| AOI (WGS84 bbox) | `5.355, 51.440, 5.420, 51.470` | not yet defined | not defined (city-wide) |
| Facility type | Joint civil–military airfield (fits NATO theme) | Civil airport | City |
| Real drone incident | 22 Nov 2025: traffic suspended, C-UAS activated | Dec 2018: the best-known drone airport closure | none cited |
| Terrain | AHN 0.5 m DSM/DTM (CC0) | Environment Agency 1 m DSM/DTM | NLS 2 m DEM |
| Building heights | 3DBAG: measured height for every building | none national; must be derived from DSM − DTM | Helsinki 3D city model |
| Drone restriction zones | PDOK / LVNL OGC API | NATS UAS zones (AIXM 5.1) | not covered |
| Air-traffic baseline | OpenSky (Trino for history) | OpenSky (Trino needed for 2018; REST covers only last 30 days) | not covered |
| CRS | EPSG:28992 | EPSG:27700 | EPSG:3067 / GK25 |
| Download test done | No (Overture building count only: 4,171 buildings) | No | No |

## Points both proposals agree on

- Geodata, open sensor datasets and local demo recordings are **three separate evidence sources**; none is presented as collected at the pilot region.
- Before the final decision, run the **5-step acceptance check** from the Helsinki/Gatwick proposals on a small sample area: (1) elevation, building and OSM files download, (2) licence and source dates recorded, (3) layers open in the same place, (4) gaps and road connectivity checked, (5) file sizes manageable on team laptops. Log results in [`../verified-access-log.md`](../verified-access-log.md).
- The repository is public: **do not publish detailed vulnerability outputs** (blind spots, weakest approach corridors) for a real airfield here. Keep methods and sources in the repo; show site-specific risk maps only in the report and demo.

## Recommendation so far

Yağız Akkaya's review (22 Oct): keep **Eindhoven** as the pilot region because of the military angle, 0.5 m LiDAR and 3DBAG; use the **Gatwick 2018 incident** in the introduction/motivation and list Gatwick as a strong second candidate. If the team picks Gatwick, building heights must be derived by CNG 1 (Yaren Duyan) from the DSM. **The team has not voted yet.**

> 🇹🇷 Şu ana kadarki öneri: Eindhoven pilot bölge olsun, Gatwick 2018 olayı raporun motivasyon bölümünde kullanılsın ve Gatwick güçlü ikinci aday olarak alternatifler tablosunda yer alsın. Ekip kararı henüz verilmedi.

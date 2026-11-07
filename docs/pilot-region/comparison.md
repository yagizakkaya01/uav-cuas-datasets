# Pilot Region Comparison: Eindhoven vs Gatwick vs Aalborg

*Prepared by Yağız Akkaya, 7 November 2026. Based on the proposals in this folder. The team has not decided yet.*

| Criterion | Eindhoven (Yağız Akkaya) | Gatwick (Yaren Duyan) | Aalborg (Aydan Doğan) | Best fit |
|---|---|---|---|---|
| **Facility type / NATO theme** | Strong: joint civil–military airfield (Eindhoven Air Base, NATO MRTT fleet) | Weak: civil airport only | Strong: joint civil–military airfield (Flyvestation Aalborg) | Eindhoven = Aalborg |
| **Documented drone incident** | Strong: 22 Nov 2025 closure, C-UAS activated; Volkel the night before; parliamentary record; IISS study (Jul 2026) | Strong: Dec 2018, ~30–33 h closure; official Sussex PCC review; academic papers | Good: 24–25 Sep 2025 (~3 h closure, lit drones, Reuters); 26 Sep closure still to verify; IISS covers the Danish wave | Eindhoven |
| **Academic sources** | IISS (2026), ECFR (2026), BISI (2025); none peer-reviewed on the incident itself | Wendt et al. 2020 and two other peer-reviewed papers discuss Gatwick | No peer-reviewed paper on the incident; IISS via news summary; EcoDes-DK15 for the LiDAR data | Gatwick |
| **Terrain (elevation)** | AHN 0.5 m DSM + DTM, CC0 | EA 1 m DSM + DTM, OGL | DHM 0.4 m terrain + surface, free with registration | Eindhoven ≈ Aalborg |
| **Building heights** | 3DBAG: measured LoD 1.2/1.3/2.2 heights for every building (6,946 in AOI) | No ready 3D model; derive from DSM − DTM; OSM heights incomplete | No ready 3D model verified; OSM outlines + DHM surface | Eindhoven (clear lead) |
| **Drone restriction zones** | PDOK / LVNL OGC API (zone query failed, polygons still to retrieve) | NATS UAS KML/AIXM, downloaded and contains Gatwick (29 Oct 2026 cycle) | Droneluftrum map/app; open API not confirmed | Gatwick |
| **Air-traffic baseline** | OpenSky live query worked (3 aircraft incl. MMF25) | OpenSky live query worked (14 aircraft) | OpenSky, not tested | Eindhoven = Gatwick |
| **Data access test** | Partly done (6 Nov): 3DBAG, AHN catalogue, OpenSky, Overture | Partly done (7 Nov): EA WCS + index, NATS ZIP, OSM sample, OpenSky; no raster tile yet | Not done | Eindhoven ≈ Gatwick |
| **Link to visual detection** | Not covered | Not covered | Strong: night incident with lit drones → IR training; Halmstad dataset from Nordic airports; camera range calculation | Aalborg |
| **CRS** | EPSG:28992 (RD New) | EPSG:27700 (British National Grid) | EPSG:25832 (UTM 32N) | — |
| **AOI size** | 5.355, 51.440, 5.420, 51.470 (~4.5 × 3.3 km) | -0.23, 51.13, -0.12, 51.17 (~7.7 × 4.4 km) | 9.82, 57.08, 9.89, 57.11 (~4.2 × 3.3 km) | Eindhoven / Aalborg (smaller, easier on laptops) |
| **Main weakness** | PDOK zone polygons not yet retrieved; real military site → vulnerability outputs must stay out of the public repo | Civil only; building heights must be derived | Data access untested; no restriction-zone API; real military site (same publication caveat) | — |

**Summary:** Eindhoven leads on building data (3DBAG) and the incident record; Gatwick has the best-tested restriction-zone data and peer-reviewed literature but is civil only; Aalborg matches Eindhoven's civil–military profile and links best to visual detection, but nothing has been tested yet. Suggested next step: run the 5-step acceptance check on Aalborg; if it passes, the team chooses between Eindhoven and Aalborg, with Gatwick used for motivation. The team has not decided.

The pilot region is used only by the decision engine; demo measurements are taken on campus and never presented as if collected at the pilot region.

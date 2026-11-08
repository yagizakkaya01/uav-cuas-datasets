# Eindhoven: Academic Literature Review

*Prepared by Yağız Akkaya, 8 November 2026. Every paper below was opened and checked on this date. Short quotations are marked with quotation marks; everything else is a summary.*

## Why these papers

No peer-reviewed article analyses the 22 November 2025 Eindhoven incident yet (see [`eindhoven-sources-and-data-test.md`](./eindhoven-sources-and-data-test.md), section 4). This review therefore covers the peer-reviewed work behind the three things the Eindhoven proposal depends on:

| Proposal claim | Paper |
|---|---|
| An airport needs multi-sensor detection and has strict limits on mitigation | Lykou, Moustakas & Gritzalis (2020) |
| 3DBAG building heights are accurate enough for line-of-sight and masking | Peters et al. (2022) |
| OpenSky can provide the normal air-traffic baseline, with known gaps | Schäfer et al. (2014) |

The risk-assessment framework of Pascarella et al. (2022), already reviewed for Gatwick by Yaren Duyan in [`gatwick-literature-review.md`](../Gatwick-Yaren%20Duyan/gatwick-literature-review.md), applies to Eindhoven unchanged and is not repeated here.

---

## 1. Lykou, Moustakas & Gritzalis (2020): counter-drone sensing at airports

**Citation.** G. Lykou, D. Moustakas, D. Gritzalis, "Defending Airports from UAS: A Survey on Cyber-Attacks and Counter-Drone Sensing Technologies," *Sensors*, vol. 20, no. 12, 3537, 2020. https://doi.org/10.3390/s20123537 (open access, peer-reviewed).

**What it does.** A survey of drone incidents at airports (10 serious incidents in 2016–2019, including Gatwick 2018 and Frankfurt 2019) and of the sensors used to detect, identify and mitigate small drones. It then builds three attack scenarios (unmanned air-traffic-management sites, airport wireless/IT, manned aircraft on approach) and proposes a protection plan for each.

**Key findings.**
- **No single sensor is enough:** "adopting a single sensor technology for UAV detection in airports cannot provide the desired situational awareness." Radar is proposed as the primary layer, with RF and EO/IR cameras for identification.
- **Each sensor has a clear weakness:** radar struggles with small, slow, low-flying drones; RF detection misses autonomous drones that do not transmit and depends on line of sight; acoustic sensors have short range (typically under 300 m) and are "not reliable" in airport noise; cameras confuse drones with birds.
- **Mitigation is constrained at airports:** civil RF jamming is illegal in many countries and can interfere with landing systems; kinetic options carry collateral risk; "no international standards exist" for C-UAS use at airports.
- **Response time is short:** with assumed drone speeds of 10–20 m/s, a 6–10 km geofence around a remote site gives about 5–10 minutes of warning.

**Relevance to our project.**
- It supports our sensor-fusion design (camera + RF on the physical demo node) and explains why the decision engine should *recommend* actions rather than assume jamming is available.
- The Eindhoven incident fits the paper's pattern exactly: flights were halted because the airport could not confirm or neutralise the drones (no drone was recovered, see the sources file).
- The 3D-geofence idea for approach paths matches our plan to score tracks against the runway approach corridor derived from OpenSky.

**Limitations.** Incident data come from open, unverified reports; the protection plans are analytical and were never tested; the sensor comparison is a literature summary, not a measured benchmark. It is from 2020, before the 2024–2026 wave of state-linked incursions over European bases.

---

## 2. Peters et al. (2022): 3DBAG, building models for the whole Netherlands

**Citation.** R. Peters, B. Dukai, S. Vitalis, J. van Liempt, J. Stoter, "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands," *Photogrammetric Engineering & Remote Sensing*, vol. 88, no. 3, pp. 165–170, 2022. https://doi.org/10.14358/PERS.21-00032R2 (preprint: https://arxiv.org/abs/2201.01191).

**What it does.** Describes how the 3DBAG dataset is produced: building footprints from the national BAG register (stated positional accuracy 30 cm) are combined with the AHN airborne LiDAR point cloud (stated height accuracy 10 cm). Roof planes are detected and fitted to produce LoD2.2 models; simpler LoD1.2 / LoD1.3 block models and reference roof heights (minimum, 50th, 70th percentile, maximum) are attached to every footprint. The ground height is the 5th percentile of ground points in a 4 m buffer.

**Key findings.**
- For LoD2.2, the error between the LiDAR points and the model is below 31 cm (RMSE) for 95 % of buildings and below 9 cm for 75 %.
- The full country was processed in about 40 hours on one server; quality attributes (point count, missing-data area, RMSE) are stored with each building.

**Relevance to our project.**
- This is the peer-reviewed basis for using 3DBAG `b3_h_dak_max` / `b3_h_maaiveld` as building heights in the line-of-sight and masking layer. Sub-metre accuracy is far better than our 5–10 m grid needs.
- No other candidate region has an equivalent: Gatwick has no national building-height dataset, and Akrotiri relies on 30 m Copernicus elevation (see [`comparison.md`](../comparison.md)).
- The stored quality attributes let us flag buildings with poor LiDAR coverage instead of trusting them blindly.

**Limitations.** Output quality "highly depends on the quality of the input data"; areas without LiDAR points are a known gap. Users must choose which reference height to use, and that choice changes line-of-sight results. The paper's own validation is brief; a fuller evaluation is referenced as future work. Trees and other non-building objects are not in 3DBAG, so the AHN DSM is still needed for full obstruction.

---

## 3. Schäfer et al. (2014): OpenSky, the air-traffic baseline

**Citation.** M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, M. Wilhelm, "Bringing Up OpenSky: A Large-scale ADS-B Sensor Network for Research," *Proc. 13th Int. Symposium on Information Processing in Sensor Networks (IPSN '14)*, Berlin, pp. 83–94, IEEE, 2014. https://doi.org/10.1109/IPSN.2014.6846743

**What it does.** Introduces the OpenSky Network: volunteer-hosted ADS-B receivers that forward every received message to a central, append-only research database. At publication it covered about 720,000 km² of Central Europe with 11 sensors and over 4 billion messages.

**Key findings and limitations stated by the authors.**
- Only aircraft that broadcast ADS-B are seen (about half of aircraft at the time); drones are not visible at all.
- Coverage at low altitude is weak where few receivers are in range; message loss rises from about 20 % to over 50 % in congested airspace.
- Positions come from the aircraft's own GNSS; multilateration without GNSS had a median error of 166 m.

**Relevance to our project.**
- OpenSky gives us the *normal* traffic picture at Eindhoven (approach and departure corridors, how many movements per evening), which the decision engine needs to judge how serious a drone track near the runway is.
- The paper explains why OpenSky cannot be used to detect the drone itself: this has to come from our own sensors (camera + RF).
- For validation, a gap in arrivals/departures on the evening of 22 November 2025 compared with a normal evening is a realistic, checkable signal (see the local data test).

**Limitations for us.** The 2014 network is much smaller than today's, so the coverage figures are historical. Military aircraft at Eindhoven may not broadcast, so the baseline is mainly civil traffic. Historical flight lists need a registered account.

---

## Summary

| Paper | Type | Supports | Main caveat |
|---|---|---|---|
| Lykou et al. 2020, *Sensors* | Survey (peer-reviewed) | Multi-sensor fusion; recommend, do not assume jamming | Analytical, not tested |
| Peters et al. 2022, *PE&RS* | Dataset method (peer-reviewed) | 3DBAG heights for line of sight | No trees; reference-height choice |
| Schäfer et al. 2014, *IPSN* | System paper (peer-reviewed) | OpenSky as traffic baseline | Civil ADS-B only, drones invisible |

Together with the IISS (2026) and ECFR (2026) reports already cited for the incident and policy context, these give Eindhoven peer-reviewed backing for its design rationale, its building-height data and its air-traffic baseline.

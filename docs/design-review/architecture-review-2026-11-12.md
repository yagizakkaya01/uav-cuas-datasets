# Architecture and Data Review

*Yağız Akkaya, 12 November 2026. Review of the system design, the pilot-region choice and data adequacy, based on the First Progress Report, the [computational model](../computational-model/computational-model.md) and the [pilot-region comparison](../pilot-region/comparison.md).*

> **Status: proposal.** Nothing here has been agreed by the team or the supervisors yet. The submitted First Progress Report (Markdown and PDF) is left unchanged; section 6 lists what should change in the next report.

> 🇹🇷 **Kısaca:** Sistem tasarımı, pilot bölge seçimi ve veri yeterliliği üzerine inceleme. Buradaki maddeler öneridir; ekip ve danışmanlarla konuşulduktan sonra karara dönüşür.

## 1. Summary

The layer split is sound, and so is the principle that a rule decides and the language model only explains. The weak point is the join between the two halves of the system: the campus sensing chain and the pilot-region decision chain. Four design items are undefined or inconsistent (scaling, line of sight in the risk map, the role of RF, the processing loop), the doctrine corpus does not match the airport scenario, and the pilot-region decision is overdue.

## 2. Architecture findings

Ordered by importance. Each finding has a proposed fix.

### 2.1 The scaled transform breaks kinematics

The demo track is mapped onto the pilot region with a scale of s = 100. Only position is scaled, so speed is scaled too: a mock drone carried at 1 m/s becomes 100 m/s (360 km/h) at the airport, while the model assumes 5–20 m/s. A 0.5 m position error on campus becomes 50 m, which is five 10 m grid cells. Time-to-reach and the 15 s / 30 s prediction are computed from this speed, so they lose their meaning.

**Proposal.** Treat the two chains as separate evidence loops that share one track message.

- The campus demo proves detection and confirmation at 1:1 scale, with its own metrics (range, position error, latency).
- The decision engine consumes track messages from a *track source*. One source is a scenario player with realistic speeds; the other is a live adapter that maps campus tracks onto the pilot region.
- The live adapter states its position scale and its time scale explicitly. With s = 100 and a time scale of 10, a 1 m/s campus track becomes 10 m/s. Every figure derived from the live adapter is labelled as scaled.

### 2.2 "Risk map with line of sight" is not defined

The report names a risk map that accounts for line of sight as a main feature. The risk formula in M5 (Gaussian spread plus a zone cost) contains no line-of-sight term. There is also no sensor in the pilot region, so it is not stated whose line of sight is meant.

**Proposal.** Define line of sight as a static, precomputed layer for a *hypothetical* sensor placement in the pilot region: a coverage mask per altitude band. Add a term to the risk field for cells that a drone can cross without being covered. The viewshed is computed once per sensor placement, not per frame.

### 2.3 The RF role contradicts the threat definition

The threat is a drone that does not announce itself, but the earlier design confirmed the drone by an address known in advance. That is confirmation of a known device. The threat score in M4 also has no RF feature, so the fusion required by FR-5 does not exist in the model, and it is not stated whether an RF confirmation raises or lowers the score.

**Decision (12 Nov 2026): MAC addresses are not used anywhere in the system**, neither to recognise the mock drone nor to filter other devices. The RF side uses baseline-and-anomaly detection on aggregate signal statistics:

- Record the normal Wi-Fi background of the demo area (frames per second and signal-strength distribution, per channel) at the hours of the demo, on several days.
- Report an anomaly when the statistics leave the baseline for a sustained time, for example a clear rise in strong-signal frames.
- Fuse with the camera in time: a camera track together with an RF anomaly in the same seconds is strong evidence. This becomes the RF feature of the threat score.
- Test with a distractor: a phone hotspot switched on near the receiver may raise the RF statistics, but without a camera track it must not produce a confirmation.

Limits to state in the report: without addresses the receiver cannot tell which device caused the change, so an RF anomaly alone never identifies a drone; it only supports a camera track. The ESP32 listens on one channel at a time (the mock drone's channel may be fixed as a stated assumption), and only 2.4 GHz Wi-Fi links are visible. The submitted progress report and the deployment diagram still mention a MAC filter and should be updated in the next version; the change also needs to be confirmed with Adil Mert İş and the supervisors, since the accepted hardware assumptions mentioned MAC filtering.

### 2.4 Ground position from a known height is poorly conditioned

The camera is on a tripod at about 1.75 m and the mock drone flies at about 3 m. At 15 m the elevation angle is about 5°, so projecting onto the known-height plane turns a 1° angle error or a 0.3 m height error into roughly 20–25 % range error. Range from the apparent size of the drone is better conditioned: with the 2.8 mm setting a 0.35 m target covers about 33 pixels at 15 m (assumed 2.0 µm pixel pitch), so a 2-pixel box error is about 6 %.

**Proposal.** Use range from box size as the primary method (as the computational model already does) or mount the camera clearly higher. The report and the computational model currently describe different methods; pick one.

### 2.5 The processing loop runs everything per frame

In the activity diagram, the threat score, risk propagation, routing, retrieval and the language-model call all run for every frame (about 20 fps), while NFR-4 allows the language model 15 seconds. The diagram has no RF swimlane. "Geofence" is used for two things: the edge of the demo area and restricted airspace.

**Proposal.**

- Three rates: detection per frame; track, score and risk a few times per second; routing and recommendation only on events.
- A track state machine (tentative, confirmed, lost) and a threat-level state with hysteresis. A recommendation is requested when the level changes, not per frame.
- The action and the doctrine passages are selected deterministically. The language model only writes the explanation; if the API is unavailable, a template text is shown. NFR-1 should cover this case.
- Two names: *demo area boundary* and *restricted zone*.

### 2.6 Interface contracts are missing

The plan's week-3 deliverable (JSON schemas) is not in the repository. There is no component or sequence diagram, no definition of coordinate frames (camera pixels, campus local frame, pilot-region CRS) and no timestamp rule.

**Proposal.** Write the contracts before more module work: detection, RF event, track, threat assessment, risk grid, route, recommendation and operator decision messages, each with units, frame, timestamp and uncertainty fields.

### 2.7 Smaller points

- **Grid resampling.** Averaging the 0.5 m AHN surface to 10 m lowers obstacle heights and gives up much of the advantage over a 30 m model. For line of sight, aggregate surface height by maximum.
- **NFR-6** ("70 % accuracy") is not a detection metric. Use recall and precision at a stated range, or mAP@0.5 as in Table 5.2.
- **Small targets.** At 2560 × 1440 the mock drone is 25–35 pixels wide at 15–20 m. If frames are downscaled to 640 pixels for YOLO it shrinks to 6–9 pixels; use tiling or a larger input size.
- **How the mock drone moves** (carried on a pole, on a line, by whom) is not written down. It decides the ground-truth method.

## 3. Doctrine corpus: add airport-domain procedure

The rule table in M7 recommends airport actions (suspend runway operations, notify ATC), but the corpus is built around ATP 3-01.81, which is doctrine for land forces. A cited page for an airport action may not exist in it. Two documents close this gap; both are now listed in [Layer 2](../../layers/02-semantic-threat-knowledge-base.md).

| Document | Why it fits | Limits |
|---|---|---|
| IATA and partners, *Unauthorized UA in the Vicinity of Airports: Guidance Material* (IATA copy; ICAO hosts v1.0 of 5 Dec 2022 as *Response to Unauthorized UA in the Vicinity of Aerodrome*) | Classifies events as Low / Medium / High impact from parameters such as intent, size, proximity, altitude, trajectory and payload, with a weighted risk matrix (Appendix 1). Gives the response per impact level (section 6.4) and recovery criteria (6.7). This is the same structure as M4 (weighted score, thresholds) and M7 (action per level). | No licence statement found: use locally and cite, do not redistribute. Chapter and page numbers must be checked against the PDF before they are cited. The IATA and ICAO copies may be different editions. |
| EASA, *Drone Incident Management at Aerodromes, Part 1* (8 March 2021) | European regulatory context, offender categories, phases of an incident. Fits a Dutch airfield. | Only Part 1 is public. Parts 2 and 3, including the annex on threat zones and ATC response, are restricted to aviation actors and authorities. |

**Proposal.** Derive the M4 features and thresholds and the M7 action table from the IATA guidance, and keep ATP 3-01.81 for the military side of a joint civil–military airfield. This also answers the question "where do the weights come from" with a published source.

## 4. Pilot region

**Recommendation: choose Eindhoven and close the question.** It is the only candidate that is fully downloaded with a reproducible script, the only one with measured building heights, and it has an incident record supported by ADS-B data. The decision was planned for weeks 1–3, and the geospatial work cannot be finalised without it. The team has not voted yet.

On the comparison itself: the criteria are not weighted, and they measure data availability more than what the system needs. A short weighted list agreed first would have ended the comparison sooner.

Open items for Eindhoven:

| Item | Issue | Proposed handling |
|---|---|---|
| Restricted zone | The 3 km runway buffer has no source | Tie the distance to a published rule, or make it a parameter and report the sensitivity |
| Approach corridor | 5 km × 500 m is an assumption | Derive it from the adsb.lol tracks that are already downloaded |
| Publication | The rule against publishing blind spots of a real air base also covers the project's main output (coverage and line-of-sight maps), and the report PDF is in this public repository | Agree with the supervisors what may be shown; state that sensor placements are hypothetical |

## 5. Data adequacy

Geodata for Eindhoven is sufficient. The gaps are elsewhere.

| Gap | Why it matters | Proposed handling |
|---|---|---|
| No team recordings yet | They are the only primary data. Public datasets show real drones against the sky; the demo shows a mock drone at eye level in front of buildings | Record and label early; do not wait for phase P4 |
| No ground-truth method | Position error cannot be measured | Marked ground points and a fixed path; decide together with how the mock drone is moved |
| Decision-layer inputs are synthetic | There are no real drone tracks for the pilot region. This conflicts with the "real data" principle unless it is stated | State it plainly: geodata is real, tracks are simulated with parameters taken from published sources |
| No benign class | "False alarms" and the weights and thresholds cannot be validated | Take levels from the IATA matrix (section 3), add a sensitivity analysis and labelled scenarios |
| Datasets outside the current scope | DroneRF is raw SDR capture and cannot be used with a packet-level ESP32 receiver; UAVSwarm is multi-target; the infrared part of Halmstad is outside the daytime scope | Report section 5.1 should list them as context, not as training data |
| RAG evaluation | Recall@k and MRR need a question set with known answers | Build a small gold set from the corpus |
| OpenSky in the live system | FR-13 loads it, but its use in the decision is not defined | Either use it offline only (corridor) or define a feature, such as distance to an aircraft on approach |

## 6. Items for the next report

The submitted report is not edited. These points should change in the next version.

- **Section 3.3 (research gap).** "Not described" in press coverage of Turkish products does not show that a feature is absent. Academic threat-assessment literature and commercial C2 software are not reviewed. State the contribution in the decision layer: exposure that accounts for terrain, and recommendations traceable to published procedure. The sensors are a minimal input rig.
- **Section 5.1.** Dataset roles (see section 5 above).
- **Sections 2.1.3, 6.1, 6.2 and the deployment diagram.** RF role (no MAC addresses), scaling rule, position method, event-driven flow; add the RF swimlane to the activity diagram.
- **Table 3.4.** Add the airport-domain documents.
- **Requirements.** NFR-6 metric; NFR-1 extended to an LLM API failure.

## 7. Repository consistency fixes made on 12 November

- `README.md`: Eindhoven rows of the pilot-region table brought in line with `comparison.md` (restriction-zone source retired; data test done on 8 November); repository structure and date updated.
- `layers/01`: team-collected data section updated to the single-camera setup; notes on terrain sources and on DroneRF.
- `layers/02`: airport-domain documents added; swarm note corrected.
- `layers/03`: note on the risk-propagation method.
- `docs/verified-access-log.md`: the 11 Eindhoven sources that passed the 8 November local test added.
- `docs/computational-model/computational-model.md`: section 9 added, with pointers from the affected sub-models.

## Sources

- [IATA: Unauthorized UA in the Vicinity of Airports, Guidance Material](https://www.iata.org/contentassets/fb1df0e634454acc9207418a5d1d636b/unauthorized-ua-guidance-material.pdf)
- [ICAO copy: Response to Unauthorized UA in the Vicinity of Aerodrome, v1.0, 5 Dec 2022](https://www2023.icao.int/safety/UA/Documents/Response%20to%20Unauthorized%20UA%20in%20the%20Vicinity%20of%20Aerodrome.pdf)
- [EASA: Drone Incident Management at Aerodromes, Part 1](https://www.easa.europa.eu/sites/default/files/dfu/drone_incident_management_at_aerodromes_part1_website_suitable.pdf)
- [EASA press release, 8 March 2021](https://www.easa.europa.eu/newsroom-and-events/press-releases/easa-issues-guidelines-management-drone-incidents-airports)

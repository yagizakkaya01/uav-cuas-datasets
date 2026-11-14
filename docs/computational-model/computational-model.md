# Computational Model of the UAV Threat Map and Decision Support System

*Prepared by Yağız Akkaya, 10 November 2026. Covers the whole system and its application to the Eindhoven pilot region. Every cited paper was opened and checked on this date; values marked **assumption** must be confirmed by the team.*

## 1. What the model does

The system takes sensor observations of a drone and turns them into a threat score, a risk map and a recommended response. It is built as a chain of seven sub-models; each one has clear inputs and outputs so that every team member can develop their part with mock data.

```
 Sensors (camera, ESP32 RF)
   │  M1 Detection model ── needs M0 world model (terrain, buildings, trees, zones)
   ▼
 Detections (bearing, size, RSSI, time)
   │  M2 Tracking & fusion (Kalman filter)
   ▼
 Tracks (position, velocity, covariance)
   │  M3 Trajectory prediction (15 s / 30 s)
   ▼
 Predicted positions
   │  M4 Threat assessment (score 0–1, level)
   ▼
 M5 Risk field on the grid ──► M6 Route / sector planning (A*, D* Lite)
   │
   ▼
 M7 Decision & recommendation (doctrine rules + RAG explanation)
   │
   ▼
 C2 map (MIL-STD-2525 symbols) and operator
```

In the physical demo the drone is detected on campus; its track is mapped onto Eindhoven with a scaled transformation (section 6), so M3–M7 run on Eindhoven data while M1–M2 run on campus data.

---

## 2. Components of the whole model

This table answers the standard question "what are the components of the computational model". Details per sub-model follow in section 3.

| Component | Content for this system |
|---|---|
| **Inputs** | Camera frames (2560 × 1440, 20 fps); ESP32 Wi-Fi/RF packets with RSSI and timing (no MAC addresses are used); static geodata (AHN 0.5 m DSM/DTM, 3DBAG buildings, WorldCover trees, OSM runway/apron/hangars, runway-buffer restricted zone); ADS-B traffic baseline (OpenSky, adsb.lol); weather (KNMI wind, visibility); doctrine corpus for RAG |
| **Outputs** | Track list (ID, position, velocity, uncertainty); threat score 0–1 and level (low / medium / high / critical); risk grid (10 m cells); recommended route or sector; recommended action with a cited doctrine reason; logs for evaluation |
| **Parameters** (fixed per run, tuned) | Grid cell size (10 m); camera focal length, pixel pitch and pixels-on-target thresholds; RF path-loss exponent and receiver sensitivity; Kalman process and measurement noise; threat weights and thresholds; risk kernel growth rate; route cost weight λ; observer and target heights |
| **Variables** (change during a run) | Drone state x = (x, y, z, vₓ, v_y, v_z); track covariance P; detection probability per cell; threat features (distance, time-to-reach, in-zone flag, in-corridor flag, altitude, speed, heading); risk value per cell; route; recommended action |
| **Rules** | Detection only if line of sight exists; track confirmed after M of N detections; track dropped after K missed updates; threat level from score thresholds; hard overrides (inside restricted zone or approach corridor → at least "high"); action table mapped from threat level and doctrine (e.g. "suspend runway operations" if a high-threat track is in the approach corridor); no kinetic or jamming action is ever recommended automatically |
| **Algorithms** | Radial-sweep viewshed (line of sight); pixels-on-target camera range model; log-distance RF path-loss model; constant-velocity Kalman filter (IMM optional); χ² gating for data association; weighted / fuzzy threat scoring; Gaussian risk propagation on the grid; A* and D* Lite route planning; retrieval-augmented generation for the explanation; Monte Carlo simulation for evaluation |
| **Assumptions** | One drone at a time (swarm is future work); drone size ~0.35 m (DJI Phantom class); flat-earth local coordinates (RD New, EPSG:28992); static terrain and buildings; constant velocity over 15–30 s; weather constant during an event; restricted zone = 3 km runway buffer (no open official zone data); demo measurements are never presented as taken at Eindhoven |

---

## 3. Sub-models

### M0. World model (grid)

| | |
|---|---|
| **Inputs** | AHN 0.5 m DSM and DTM, 3DBAG footprints and heights, ESA WorldCover classes, OSM aeroway features, OurAirports runway thresholds |
| **Outputs** | Raster stack on a common grid: terrain height, surface height, object height (nDSM = DSM − DTM), building mask, tree mask, protected-asset mask, restricted-zone mask, approach-corridor mask |
| **Parameters** | Cell size 10 m (AHN averaged); runway buffer 3,000 m; corridor length and half-width (**assumption:** 5 km × 500 m from each threshold, to be refined from ADS-B tracks) |
| **Algorithm** | Resample to 10 m, rasterise vectors, derive corridors from runway heading. Surface height for line of sight should be aggregated by maximum, not average (section 9.5) |
| **Assumptions** | Data are static for the demo period |

**Eindhoven size:** the AOI is 4,518 × 3,338 m, so a 10 m grid has 452 × 334 ≈ 151,000 cells. Every algorithm below runs on a laptop in seconds at this size.

### M1. Detection model

**Line of sight (all sensors).** A cell at height h is visible from the sensor if no intermediate cell on the line between them rises above the sight line:

visible(c) ⇔ tan θ(c) ≥ max over cells k between sensor and c of tan θ(k), with tan θ(k) = (z_k − z_s) / d_k

where z is the DSM height (plus target height for c) and d is horizontal distance. The I/O-efficient radial-sweep version of this test runs in O(n log n) (Haverkort, Toma & Zhuang). At 151,000 cells a simple per-ray version is enough.

**Camera.** The number of pixels a drone covers is N = f · S / (p · R), so the detection range is

R_det = f · S / (p · N_det)

with focal length f, drone size S, pixel pitch p and the pixels needed for detection N_det. Sandia field tests of small UAS imaging found about **7 pixels for detection and 15 for assessment** (Birch & Woo 2017). With S = 0.35 m and an **assumed** pixel pitch of 2.0 µm for our Hikvision camera (check the datasheet):

| Focal length | Detection range (7 px) | Assessment range (15 px) |
|---|---|---|
| 2.8 mm (wide) | ~70 m | ~33 m |
| 12 mm (tele) | ~300 m | ~140 m |

Detection probability is modelled as a logistic curve around R_det, set to zero where there is no line of sight and reduced at night or in low visibility (KNMI visibility code as a factor).

**RF (ESP32 receiver).** Log-distance path loss: PL(d) = PL(d₀) + 10 n log₁₀(d / d₀). A packet is detected if P_t + G_t + G_r − PL(d) ≥ sensitivity. The exponent n is about 2 with line of sight and higher (**assumption:** 2.7–3.5) when M1's viewshed says the path is blocked. RSSI gives a rough range, and only if the drone transmits; autonomous drones are invisible to RF (Lykou et al. 2020).

| | |
|---|---|
| **Inputs** | Sensor position and height, DSM, drone position (simulation) or detections (live) |
| **Outputs** | P_d per cell and altitude (coverage map); per-frame detections with bearing, box size, RSSI |
| **Parameters** | f, p, N_det, S, P_t, sensitivity, n, observer height (**assumption:** 3 m mast) |
| **Assumptions** | Clear air unless KNMI says otherwise; no bird/drone confusion modelled (a known limitation of cameras, Lykou et al. 2020) |

### M2. Tracking and fusion

A single fixed camera gives a **bearing** (azimuth, elevation), not a range. Range is estimated from the apparent box size (R ≈ f · S / (p · N)) and, when available, from RF RSSI. These pseudo-measurements are fused in a constant-velocity Kalman filter:

- state x = (x, y, z, vₓ, v_y, v_z), prediction x̂ₖ = F x̂ₖ₋₁, Pₖ = F Pₖ₋₁ Fᵀ + Q
- update with measurement z and noise R (camera noise small in angle, large in range; RF noise large)
- gating: accept a measurement if its Mahalanobis distance is below the χ² threshold (3 dof, 99 %)
- optional: an Interacting Multiple Model filter (Blom & Bar-Shalom 1988) mixing a constant-velocity and a coordinated-turn model when the drone manoeuvres

| | |
|---|---|
| **Inputs** | Detections from M1 with timestamps |
| **Outputs** | Tracks: ID, state, covariance P, status (tentative / confirmed / lost) |
| **Parameters** | Q (process noise), R per sensor, gate probability, M-of-N confirmation (**assumption:** 3 of 5), K missed updates to drop (**assumption:** 10) |
| **Rules** | Confirm after M of N hits; drop after K misses; one track per drone (single-target assumption) |

### M3. Trajectory prediction

Constant-velocity extrapolation with growing uncertainty: μ(t + τ) = position + velocity · τ, Σ(t + τ) = F(τ) P Fᵀ(τ) + Q(τ), for τ = 15 s and 30 s. A learned alternative exists: a mixture-of-experts network classified drone intent with about 98 % accuracy and predicted 15–30 s position bounds from noisy radar tracks (Fraser et al. 2023). It is noted as future work because it needs training data we do not have.

### M4. Threat assessment

Features, each normalised to 0–1:

| Feature | Meaning | Source |
|---|---|---|
| f_dist | closeness to the nearest protected asset | M0 + M2 |
| f_ttr | time to reach the asset at current speed (short = high) | M2/M3 |
| f_zone | inside the restricted zone (1/0) | M0 |
| f_corr | inside the approach corridor (1/0) | M0 + ADS-B |
| f_alt | altitude in the band used by landing aircraft | M2 |
| f_conf | track confidence (from P) | M2 |

Score: T = Σ wᵢ fᵢ (weights sum to 1), then levels by thresholds (**assumption:** < 0.3 low, < 0.6 medium, < 0.8 high, otherwise critical), with hard overrides: f_zone = 1 or f_corr = 1 → at least "high".

The score has no RF feature yet, although the system is meant to fuse camera and Wi-Fi evidence; section 9.3 proposes one.

A fuzzy-logic version (triangular membership functions, rule base) is the main alternative. Arapoglou et al. (2025) used a three-stage fuzzy hierarchy for counter-UAV sensor selection in MATLAB. They also noted it was validated only in simulation, which would be true for us as well. **Recommendation:** start with the weighted score because it is transparent and easy to explain to examiners, and keep fuzzy logic as an extension.

### M5. Risk field

Risk in each cell c is the threat score spread over the predicted positions:

Risk(c) = Σ_τ T · 𝒩(c; μ_τ, Σ_τ) + zone cost(c)

This formula has no line-of-sight term yet; section 9.2 proposes one. The Gaussian widens with prediction time τ, so far-future positions are less certain. The zone cost adds a fixed penalty inside the restricted zone. The cylindrical threat-zone cost of arXiv 2501.14503, already listed in Layer 3, can be used as the static term.

### M6. Route and sector planning

A* (Hart, Nilsson & Raphael 1968) on the grid with cost(c) = distance + λ · Risk(c) finds a safe route, for example for a response team or an evacuation path. Because risk changes every update, D* Lite (Koenig & Likhachev 2005) replans incrementally instead of searching from scratch. It produces the same paths as D* and is simpler. The same cost grid also gives the sector the camera should point to, which is the maximum predicted risk inside the field of view.

| | |
|---|---|
| **Parameters** | λ (risk weight), 8-connected grid, start and goal cells |
| **Outputs** | Route polyline, its length and accumulated risk |

### M7. Decision and recommendation

A rule table maps threat level and context to an action, for example:

| Condition | Recommended action |
|---|---|
| Low | Monitor, keep tracking |
| Medium | Alert operator, point camera to predicted sector |
| High and in approach corridor | Recommend suspending runway operations; notify ATC |
| Critical | Recommend full stop of traffic and escalation to authorities |

The RAG module retrieves the matching doctrine passages (ATP 3-01.81 and others in Layer 2), and the LLM writes a short explanation **with page citations**. The LLM never decides the action; it only explains the rule that fired. Mitigation such as jamming is never recommended automatically, because it is illegal for civil use in many countries and can interfere with landing systems (Lykou et al. 2020).

---

## 4. Eindhoven data → model inputs

All of these were downloaded and tested on 8 November 2026 (see [local data test](../pilot-region/EindHoven-Ya%C4%9F%C4%B1z%20Akkaya/local-data-test/results/data-test-report.md)).

| Model input | Eindhoven source | Used in |
|---|---|---|
| Terrain and surface | AHN 0.5 m DTM / DSM | M0, M1 line of sight |
| Building heights | 3DBAG, 3,464 buildings with heights | M0, M1 |
| Trees (not in 3DBAG) | ESA WorldCover, 32 % tree cover | M0, M1 |
| Protected assets | OSM runway, taxiways, apron, 25 hangars, terminal, tower | M0, M4 |
| Restricted zone | 3 km buffer around runway 03/21 (assumption) | M0, M4, M5 |
| Approach corridor | Runway heading + ADS-B tracks (adsb.lol, OpenSky) | M0, M4 |
| Incident timeline | 22 Nov 2025: closure ~19:30–21:40 UTC, ADS-B gap 17:30–21:30 UTC | Validation |
| Weather | KNMI station 370 (wind 5 m/s S, overcast, ~0 °C on the incident evening) | M1 (visibility), scenario |

The 30 m Copernicus DEM differs from AHN by 3.3 m RMSE, more than 7.6 m in 5 % of cells. That is why line of sight must use AHN and not a global model.

---

## 5. Validation plan

| Test | Method | Metrics |
|---|---|---|
| Detection model | Campus demo: fly the mock drone at known distances, compare with R_det | detection range error, P_d vs distance |
| Tracking | Recorded campus flights with known path | position RMSE, track breaks |
| Whole chain | Monte Carlo: 1,000 synthetic drone tracks over the Eindhoven grid with random entry direction, speed (5–20 m/s) and altitude (30–120 m) | warning time before the asset, % of tracks reaching "high" before the corridor, false alarms, latency |
| Scenario replay | Rebuild the 22 Nov 2025 evening: drones near the runway, compare recommended action with the real closure | qualitative agreement, time to recommendation |
| Risk-framework check | Compare with the airport drone-risk framework of Pascarella et al. (2022) and the SORA 2.5 airspace logic (JARUS 2024) | consistency of risk levels |

Sensor-placement or blind-spot results for the real air base are computed only locally and **are not published** in this public repository; the demo publishes results for the campus area.

---

## 6. Mapping the physical demo onto Eindhoven

The campus demo area is about 15 × 17 m and has one fixed camera. A demo track p_campus is mapped to Eindhoven with a similarity transform p_EHEH = s · R(θ) · (p_campus − o_campus) + o_EHEH, with a chosen scale s (**assumption:** s = 100, so 15 m on campus = 1.5 km at the airport), rotation θ and anchor points. The scaled track then drives M3–M7. The report must state that demo distances are scaled and not real Eindhoven measurements. Scaling position alone also scales speed; section 9.1 adds a time scale.

---

## 7. Who builds what

| Sub-model | Owner (from the team plan) |
|---|---|
| M0 world model, M5 risk field, M6 routing | Yaren Duyan |
| M1 camera detection | Aydan Doğan |
| M1 RF detection and range model | Adil Mert İş |
| M2 tracking & fusion, M4 threat score, C2 interface | Mert Gökalp |
| M7 doctrine rules + RAG, validation scenarios | Yağız Akkaya |

## 8. Keep it simple (minimum version for ESC 491)

Following the supervisors' advice to keep it simple, the minimum working chain is:
1. 10 m grid with AHN line of sight
2. Pixels-on-target camera model
3. Constant-velocity Kalman filter
4. Weighted threat score
5. Gaussian risk field
6. A*
7. Rule table with a RAG explanation

IMM, D* Lite, fuzzy scoring and learned intent prediction are listed as extensions for ESC 492.

---

## 9. Open design issues and proposed revisions (12 November 2026)

These points come from the [architecture review](../design-review/architecture-review-2026-11-12.md). They are **proposals**; the sections above are unchanged apart from the pointers to this section.

### 9.1 Scaling needs a time scale

With s = 100, a mock drone carried at 1 m/s moves at 100 m/s on the Eindhoven grid, far above the 5–20 m/s assumed in the validation plan, and a 0.5 m campus error becomes 50 m. Time-to-reach (f_ttr) and the M3 prediction then lose their meaning.

Proposed rule: the mapping has a position scale s and a time scale k, so mapped speed is v_EHEH = (s / k) · v_campus. With s = 100 and k = 10, 1 m/s on campus becomes 10 m/s. The decision engine reads tracks from a *track source*: a scenario player with realistic kinematics, or the live adapter that applies s and k. Demo accuracy figures (range, position error, latency) are reported at campus scale only.

### 9.2 Line-of-sight term in the risk field

Define a static coverage layer C(c, h) ∈ {0, 1} for a hypothetical sensor placement in the pilot region: 1 if a target at height h above cell c is visible to at least one sensor (M1 viewshed). It is computed once per placement and altitude band, not per frame. The risk field becomes

Risk(c) = Σ_τ T · 𝒩(c; μ_τ, Σ_τ) · (1 + β · (1 − C(c, h))) + zone cost(c)

so predicted positions in uncovered cells weigh more (**assumption:** β to be tuned). Sensor placements are hypothetical and site-specific coverage maps stay out of the public repository.

### 9.3 RF evidence in the threat score

**Decision (12 Nov 2026): MAC addresses are not used anywhere in the system**, neither to recognise the mock drone nor to filter other devices.

The receiver works on aggregate signal statistics only. It records a baseline of the normal Wi-Fi background of the demo area (frames per second and the distribution of signal strength, per channel, at the hours of the demo on several days) and reports an *emitter anomaly* when the measured statistics leave the baseline for a sustained time, for example a clear rise in strong-signal frames. A feature f_rf ∈ [0, 1] is set when an anomaly coincides in time with a camera track, and enters T with its own weight.

Limits to state: without addresses the receiver cannot tell which device caused the change, so an RF anomaly alone never identifies a drone; it only supports a camera track. A phone hotspot next to the receiver is used as a distractor in testing: it may raise the RF statistics, but without a camera track it must not produce a confirmation. The ESP32 listens on one channel at a time, so the mock drone's channel may be fixed as a stated assumption.

### 9.4 One range method

M2 estimates range from the apparent box size, while the progress report projects onto a plane at a known flight height. With the camera at about 1.75 m and the target at about 3 m, the elevation angle at 15 m is about 5°, and the plane projection turns a 1° angle error or a 0.3 m height error into roughly 20–25 % range error. Range from box size is better conditioned (about 33 pixels at 15 m with the 2.8 mm setting and the assumed 2.0 µm pitch). Proposal: keep box-size range as the primary method, or mount the camera higher.

### 9.5 Grid aggregation

Averaging the 0.5 m surface model to 10 m lowers the height of buildings and tree lines. For M1 line of sight, aggregate surface height by maximum (conservative for blocking), and keep the average for terrain height.

### 9.6 Update rates and events

M1 runs per frame. M2–M5 run a few times per second. M6 and M7 run on events: a confirmed track, or a change of threat level (with hysteresis so the level does not flicker). The action and its doctrine passages are selected deterministically; the language model only writes the explanation, and a template text is used if the API is unavailable.

### 9.7 Source for threat levels and actions

The M4 thresholds and the M7 action table are assumptions. The IATA guidance material on unauthorized UA near airports classifies events into Low / Medium / High impact from parameters close to the M4 features and gives the response per level; it is now listed in [Layer 2](../../layers/02-semantic-threat-knowledge-base.md). Proposal: derive the features, thresholds and actions from it and cite it per rule, keeping ATP 3-01.81 for the military side.

---

## References

1. G. Lykou, D. Moustakas, D. Gritzalis, "Defending Airports from UAS: A Survey on Cyber-Attacks and Counter-Drone Sensing Technologies," *Sensors* 20(12), 3537, 2020. https://doi.org/10.3390/s20123537
2. J. A. Besada, I. Campaña, D. Carramiñana, L. Bergesio, G. de Miguel, "Review and Simulation of Counter-UAS Sensors for Unmanned Traffic Management," *Sensors* 22(1), 189, 2022. https://doi.org/10.3390/s22010189 (radar-equation, CFAR and false-alarm sensor models in an agent-based simulator; precedent for our Monte Carlo evaluation)
3. G. C. Birch, B. L. Woo, *Counter Unmanned Aerial Systems Testing: Evaluation of VIS, SWIR, MWIR, and LWIR Passive Imagers*, Sandia National Laboratories, SAND2017-0921, 2017 (technical report, not peer-reviewed). https://www.osti.gov/servlets/purl/1342469
4. H. Haverkort, L. Toma, Y. Zhuang, "Computing Visibility on Terrains in External Memory," Proc. ALENEX 2007; ACM DOI 10.1145/1412228.1412233.
5. H. A. P. Blom, Y. Bar-Shalom, "The Interacting Multiple Model Algorithm for Systems with Markovian Switching Coefficients," *IEEE Trans. Automatic Control* 33(8), 780–783, 1988. https://doi.org/10.1109/9.1299
6. B. Fraser, A. Perrusquía, D. Panagiotakopoulos, W. Guo, "A Deep Mixture of Experts Network for Drone Trajectory Intent Classification and Prediction Using Non-Cooperative Radar Data," IEEE SSCI 2023. https://doi.org/10.1109/SSCI52147.2023.10371877
7. F. Arapoglou, P. Zacharia, M. Papoutsidakis, "Intelligent Counter-UAV Threat Detection Using Hierarchical Fuzzy Decision-Making and Sensor Fusion," *Sensors* 25(19), 6091, 2025. https://doi.org/10.3390/s25196091
8. P. E. Hart, N. J. Nilsson, B. Raphael, "A Formal Basis for the Heuristic Determination of Minimum Cost Paths," *IEEE Trans. Systems Science and Cybernetics* 4(2), 100–107, 1968.
9. S. Koenig, M. Likhachev, "Fast Replanning for Navigation in Unknown Terrain," *IEEE Trans. Robotics* 21(3), 354–363, 2005.
10. R. Peters, B. Dukai, S. Vitalis, J. van Liempt, J. Stoter, "Automated 3D Reconstruction of LoD2 and LoD1 Models for All 10 Million Buildings of the Netherlands," *PE&RS* 88(3), 165–170, 2022. https://doi.org/10.14358/PERS.21-00032R2
11. M. Schäfer et al., "Bringing Up OpenSky: A Large-scale ADS-B Sensor Network for Research," IPSN 2014, 83–94. https://doi.org/10.1109/IPSN.2014.6846743
12. D. Pascarella, G. Gigante, A. Vozella et al., "A Methodological Framework for the Risk Assessment of Drone Intrusions in Airports," *Aerospace* 9(12), 747, 2022. https://doi.org/10.3390/aerospace9120747 (reviewed in [`gatwick-literature-review.md`](../pilot-region/Gatwick-Yaren%20Duyan/gatwick-literature-review.md)).
13. JARUS, *Specific Operations Risk Assessment (SORA) Main Body*, JAR-DEL-SRM-SORA-MB-2.5, Edition 2.5, 13 May 2024.

# Literature Review

**Owner:** Yağız Akkaya · **Weight:** 30%

## 3.1 Theoretical background

Small unmanned aircraft systems (UAS) have become a recurring cause of disruption at airports and military installations. The peer-reviewed literature documents the 2018 Gatwick shutdown and a series of 2019 closures at Frankfurt, Dublin and Newark [1], [2]. Since September 2025 a second wave of incidents has affected joint civil and military airfields across Northern Europe, including Copenhagen, Aalborg, Munich, Brussels, Liège, Volkel and Eindhoven [3]–[8]. An International Institute for Strategic Studies (IISS) dataset counts 144 incidents in 13 European states between August 2024 and February 2026 [9]. Table 3.1 summarises representative cases. They are presented as general examples of the problem rather than as a choice of pilot region for the project.

**Table 3.1.** Representative drone incidents at airports and military bases.

| Date | Location | What happened | Operational impact | Source |
|---|---|---|---|---|
| 19–21 Dec 2018 | Gatwick, UK | Repeated drone sightings near the runway over three days | Closure of about 33 h; about 1,000 flights diverted or cancelled; about 140,000 passengers affected | [1] |
| 9 May 2019 | Frankfurt, Germany | Pilot reported a drone; federal police searched by helicopter | Closed for about 1 h; 143 take-offs and landings cancelled and 48 aircraft diverted | [2], [1] |
| Feb 2019 / Jan 2019 | Dublin, Ireland / Newark, USA | Confirmed drone sightings | Flights suspended for about 30 min (Dublin) and about 90 min (Newark) | [1] |
| 22 Sep 2025 | Copenhagen, Denmark (and Oslo, Norway) | Two to three large drones approached from different directions; police described a "capable operator" | Take-offs and landings halted for nearly 4 h; Oslo closed its airspace for 3 h the same evening; tens of thousands of passengers stranded | [3], [4] |
| 24–25 Sep 2025 | Aalborg, Denmark (joint civil–military) | More than one lit drone observed for about 3 h; efforts to bring them down failed; drones also reported near other Danish airports, including the Skrydstrup fighter base | Zero-rate traffic until 04:00 GMT; three flights diverted | [5] |
| 3 Oct 2025 | Munich, Germany | Second closure in under 24 h; police made two simultaneous confirmed sightings near both runways; the drones left before identification | Operations restricted, then suspended overnight; 23 inbound flights diverted and 12 cancelled, affecting nearly 3,000 passengers | [6] |
| 4–5 Nov 2025 | Brussels and Liège, Belgium (also Florennes air base) | Three drones over the Brussels perimeter; the defence minister described large drones flying in formation | Brussels: 81 flights cancelled and 24 diverted; Liège: closure of about 7 h | [7] |
| 21–22 Nov 2025 | Volkel Air Base and Eindhoven, Netherlands | Guards at Volkel saw up to 10 drones and fired from the ground; the next evening multiple drones were sighted at Eindhoven | All civil and military flights at Eindhoven halted for about 2 h; no drone recovered | [8] |
| Aug 2024 – Feb 2026 | 13 European states | IISS dataset of 144 incidents, assessed as a Russia-linked campaign | Cumulative disruption of civil and military sites | [9] |

The incidents share one operational pattern. A sighting is reported, the object cannot be confirmed or identified, and the airport closes as a precaution for hours, in no listed case because of a collision and with no drone recovered [1], [3]–[8]. The cost is therefore driven by uncertainty in the detection and identification chain. This makes the speed and confidence of threat assessment, rather than the ability to destroy a drone, the central requirement for a decision support system.

Detecting a small drone is physically difficult, and each sensor modality fails in a different way. Table 3.2 compares the five modalities discussed in recent surveys [1], [10]–[12]. The range values are indicative only, because the surveys stress that ranges depend on conditions and are often subjective assessments drawn from field trials [11]. Earlier reviews reach the same conclusion: anti-drone systems are organised into detection, identification and neutralisation stages [13], and machine-learning detection research remains largely experimental and hard to compare across datasets [14].

**Table 3.2.** Small-drone detection sensor modalities.

| Sensor | Indicative range against small drones | Strengths | Weaknesses | Sources |
|---|---|---|---|---|
| Radar | Up to a few kilometres for surveillance radar | Works in darkness, cloud and poor light; micro-Doppler from rotating blades supports classification | Low radar cross section (RCS); difficulty separating drones from birds; clutter in urban areas; airport radars are designed for large aircraft; echo power falls with the fourth power of range; cost, licensing and skilled operators required | [10], [11], [12], [4] |
| RF detection (passive) | Up to 600 m in one study and no signature beyond 100 m in another (as reported in [1]); narrow range when only Wi-Fi bands are monitored | Passive and low cost; can locate the controller; can warn before take-off | Blind to autonomous, pre-programmed, tethered or fibre-optic drones; degraded by congested 2.4/5 GHz spectrum; encrypted links and spoofed MAC addresses | [1], [10], [11], [12], [4] |
| EO (visible) camera | No general figure; one benchmark dataset has a 200 m maximum distance (as reported in [12]) | High resolution; real-time CNN detectors such as the YOLO family; imagery usable for verification | Largely restricted to daylight; needs clear line of sight; drones confused with birds, giving both false positives and false negatives; sensitive to weather and lighting | [11], [4], [1], [10], [12] |
| Thermal (IR) camera | Detecting a 0.3 m drone at 2 km needs a field of view below about 3°; rotating thermal sensors work from a few hundred metres to about 1 km | Needs no external light; motors and batteries produce a heat signature; robust to illumination changes | Lower resolution and higher cost than EO; small targets easily lost against the background; still needs line of sight | [11], [1], [12] |
| Acoustic | About 100–300 m in ideal conditions | Low cost; detects drones that emit no RF; unaffected by fog or darkness | Short range for an effective response; high false-alarm rate from wind, birds and buildings; unreliable in noisy airports; misses drones absent from the sound library | [11], [1], [10], [12], [4] |

Radar is often assumed to solve the detection problem, but measured RCS values show why it does not do so alone. Anechoic-chamber measurements of six commercial drones at 15 GHz and 25 GHz gave mean RCS values between about −17 dBsm for the DJI Mavic Pro and about −7 dBsm for the DJI Matrice 600 Pro, that is, roughly 0.02 m² to 0.2 m² [15]. RCS varied with aspect angle, frequency and polarisation, and was higher at 25 GHz than at 15 GHz for the drones tested [15], [16]. A recent survey reports UK Civil Aviation Authority tests in which small quadcopters of the DJI Phantom class, with an RCS as low as −23 dBsm, could not be reliably tracked beyond 500 m by standard airport-surveillance radar [17]. Because received echo power falls with the fourth power of range [11], the maximum detection range scales with the fourth root of RCS. A −17 dBsm drone is therefore detected at roughly 0.38 times the range of a 1 m² target by the same radar. These values are also close to those of birds, so radar cannot reliably separate the two by size alone [10], [15]. Similar complementary weaknesses hold for the other sensors. RF sensing misses autonomous drones, while cameras miss drones at night or behind obstacles [11], [12]. One survey found that 52% of commercial counter-UAS (C-UAS) products relied on a single sensor and argued that a single technology "cannot provide the desired situational awareness" at airports [1]. Recent reviews recommend combining modalities, either by early (feature-level) fusion, which needs aligned data and more computation, or by late (decision-level) fusion through voting, weighted averaging or Bayesian methods [10]. Fusion provides cross-confirmation and fewer false alarms [11], and camera and RF sensing in particular are complementary [12]. Policy analysis adds that sensor outputs should feed a common operating picture through a command-and-control (C2) node [4]. Together these findings justify the project's central design choices: two cheap sensors with non-overlapping failure modes, decision-level fusion, and a map-based picture that accounts for line of sight.

## 3.2 Previous work

### 3.2.1 Academic studies

The academic literature relevant to the project falls into five strands: vision-based detection, RF detection, multi-sensor fusion, risk assessment with threat-aware path planning, and decision support including large language models (LLMs) with retrieval-augmented generation (RAG). Table 3.3 summarises representative studies from each strand. Most are from 2021–2026. A few older works, such as the DroneRF dataset and the original RAG paper, are included as foundations. Several entries are preprints, and this is stated in the table.

**Table 3.3.** Academic studies grouped by topic.

| Ref | Year | Topic | Method | Key finding | Relevance to our project |
|---|---|---|---|---|---|
| [18] | 2022 | Vision detection | DUT Anti-UAV benchmark (10,000 images, 20 tracking videos); detection combined with tracking | Detection-guided tracking "considerably" improves tracker performance | Closest public analogue to a fixed visible camera with a YOLO-type detector and tracker |
| [19] | 2021 | Vision detection | Anti-UAV benchmark of over 300 RGB/thermal video pairs; dual-flow training method | Improves tracker performance; shows the value of thermal imagery | Reference for tracking metrics; motivates adding an IR sensor as future work |
| [20] | 2021 | Vision detection | Review of top Drone-vs-Bird 2020 entries (Cascade R-CNN, YOLOv3-SPP, Faster R-CNN) | Winner reached 80% AP; moving cameras and distant drones were hardest | Sets realistic accuracy limits for drones among birds; motivates RF confirmation |
| [21] | 2024 | Vision detection | Review of the Drone-vs-Bird challenge at ICASSP 2023 | Deep detectors dominate; moving cameras, disturbances and foreground birds remain difficult | Most recent peer-reviewed reference point for drone-versus-bird detection |
| [22] | 2021 | Vision detection and fusion | YOLOv2 on visible and IR cameras, LSTM on audio, fish-eye camera for cueing, late fusion | F1 of 0.78 (visible), 0.76 (IR) and 0.93 (audio); fusion reduced false detections | Methodological template: fixed ground station, one detector per sensor, fusion step |
| [23] | 2021 | Vision dataset | Halmstad IR, visible and audio dataset with distance bins (under 20 m, 20–60 m, over 60 m) | Daylight only, drones within 200 m, three drone types | Distance bins can be reused to report the project's camera performance |
| [24] | 2024 | Vision detection | YOLOv8n with edge-aware backbone, attention neck and shared detail head | 98.4% mAP@0.5 on an in-house set; +5.8% mAP over YOLOv8 on DUT Anti-UAV | Confirms YOLOv8n as a reasonable baseline; shows scores depend on the dataset |
| [25] | 2024 | Multi-modal dataset | MMAUD: lidar, cameras, mmWave radar and audio arrays with 3D trajectory labels | Supports fused 3D localisation research; no RF modality | Evidence of the move to multi-modal localisation; possible offline test data |
| [26] | 2019 | RF detection | DroneRF dataset of 227 RF segments from three drones in several flight modes | A companion deep-learning study reached 99.7% presence-detection accuracy (as reported in [27]) | Standard RF benchmark in the same 2.4 GHz band family as the ESP32 link |
| [27] | 2024 | RF detection (preprint) | VGG CNNs on IQ spectrograms with noise from −20 to +30 dB SNR; field test at 110–670 m | ≥85% balanced accuracy above −12 dB SNR; 0.79–0.81 in the field | Lab accuracy does not carry over to the field, so RF should be weighted with its uncertainty |
| [28] | 2023 | RF detection | 802.11 frames grouped by source MAC; four traffic features; Random Forest on a low-cost ARM board | Detection probability 0.99–1.0; false-alarm rate 0.012; range 280 m LoS and 90 m NLoS | Very close to the ESP32 receiver design; supports known-MAC confirmation |
| [29] | 2021 | RF detection | Periodic synchronisation packets in encrypted Wi-Fi FPV streams; Random Forest | Up to 99% on known drones; above 80% on an unseen drone; about 30 m range with stock antennas | Realistic range reference for the ESP32 link on a 15 m × 17 m test area |
| [30] | 2023 | Sensor fusion | Separate CNNs for optical, radar and acoustic data; probabilities combined by logistic regression | Up to +15.6% detection F-score and +28.1% classification F-score over single sensors | Closest template for the threat score: per-sensor probabilities merged at decision level |
| [31] | 2025 | Sensor fusion (preprint) | Feature-level radar and acoustic fusion with a transformer encoder | At 6 dB SNR, detection rose from 77.76% (acoustic only) to 93.56% (fused) | Shows fusion matters most when one sensor degrades; contrast with decision-level fusion |
| [32] | 2024 | Sensor fusion (preprint) | Passive RF gives location and identity; EO detections associated after 3D-to-2D projection | Tracking performance quantified over range; no public figures in the abstract | Conceptual precedent for camera-plus-RF fusion: vision for position, RF for identity |
| [33] | 2022 | Risk assessment | Airport vulnerability index combined with event trees; Malpensa case study | Methodological framework for drone-intrusion risk at airports | Site-level risk framework that the project refines to a per-cell map |
| [34] | 2026 | Risk assessment | Tree-augmented naive Bayesian network for UAS accidents near an airport | 12 risk factors; flight-control failure most critical | Alternative probabilistic weighting of factors in a risk score |
| [35] | 2022 | Risk assessment | Analysis of FAA UAS sighting reports | Most sightings within 5 miles of airports, concentrated at large hubs, in summer and daytime | Empirical basis for the extent of the risk grid and time-of-day weighting |
| [36] | 2026 | Risk assessment | Hierarchical model with AHP weighting | Factor rankings were sensitive to AHP scoring | Warns that the project's weights need a sensitivity analysis |
| [37] | 2026 | Path planning | Risk-A* over a DEM with model-predictive refinement using radar detection-risk cues | Met the no-detection threshold with slightly longer paths; maximum solve time 0.812 s | Closest precedent for risk-weighted A* over terrain with line-of-sight exposure |
| [38] | 2025 | Path planning | Voronoi graph with A* on adaptively layered DEM | Better success rate and computation time; assumes a static environment | Speed-up option for grid routing; static assumption matches a static risk map |
| [39] | 2025 | Path planning | Double DQN with angle-dependent RCS against multiple radars | Avoided threat zones in simulation | Contrast case that supports deterministic, explainable A*/Dijkstra |
| [40] | 2024 | Path planning | 3D grid A* with new heuristic and B-spline smoothing | Better real-time performance and optimality than standard A* | Precedent for optional route smoothing |
| [41] | 2021 | Decision support | Dynamic expert system issuing recommendations when flight-safety inputs change | Simulation confirmed the rule set works as intended | Precedent for a rule-based recommendation layer |
| [42] | 2026 | Decision support | Agent-based simulation with surrogate models and measures of effectiveness for C-UAS | Proposed for comparing C-UAS architectures against swarms | Precedent for simulation-based evaluation of a C-UAS design |
| [43] | 2026 | Decision support (preprint) | Neural network threat-severity classifier with drift detection | 96.4% accuracy and about 4.5 ms latency on synthetic data | Typical opaque ML alternative; synthetic-data limitation argues for an interpretable score |
| [44] | 2026 | Decision support (XAI) | Proposal for explainable object detection in defence, including trust experiments | Identifies overreliance as the central risk of defence decision aids | Supports keeping the operator in control of every decision |
| [45] | 2023 | Decision support (trust; preprint) | Conjoint survey at US war colleges | Trust in military AI linked to technical specifications, effectiveness and oversight | Showing the basis of a recommendation can affect operator trust |
| [46] | 2026 | Decision support | Levels-of-automation taxonomy across analysis, decision and action | Shared vocabulary for comparing automation | Locates the project: automated analysis and recommendation, no action execution |
| [47] | 2020 | LLM/RAG | Seq2seq model combined with a dense retriever over Wikipedia | More specific and factual output than a parametric-only model | Foundational method for the doctrine retrieval module |
| [48] | 2023 | LLM/RAG (preprint) | Survey of naive, advanced and modular RAG | RAG mitigates hallucination and untraceable reasoning | Taxonomy for describing the project's pipeline |
| [49] | 2024 | LLM/RAG | Multi-agent wargame with five off-the-shelf LLMs | All models escalated in hard-to-predict ways | Justifies keeping the LLM out of the decision loop |
| [50] | 2026 | LLM/RAG | Retrieval of if-then triage rules injected into the LLM prompt | GPT-3.5 accuracy rose from 0.45 to 0.68 | Closest architectural analogue: retrieving rules to guide a safety-critical explanation |
| [51] | 2025 | LLM/RAG (preprint) | Guideline sections and similar past cases retrieved for emergency triage | Accuracy 0.802 vs 0.542; overtriage cut from 28.8% to 12.7% | Evidence that grounding in official guidance improves LLM output |
| [52] | 2026 | LLM/RAG (preprint) | Guarded generation that refuses when evidence is weak | Fewer unsupported claims at the cost of coverage | Supports a "no citation, no claim" rule for doctrine answers |

Three observations emerge from Table 3.3. First, reported detection scores depend heavily on the dataset. The best Drone-vs-Bird 2020 entry reached 80% AP [20], whereas a tuned YOLOv8 variant reported 98.4% mAP@0.5 on an in-house set [24]. Similarly, near-perfect RF accuracy on DroneRF fell to about 0.8 balanced accuracy in the field [27]. The project therefore reports its own results by distance band, following [23]. Second, fusion consistently outperforms the best single sensor, with the largest gains when one sensor degrades [30], [31]. Camera-plus-RF fusion has been demonstrated architecturally [32], but no public quantitative benchmark was found in the sources reviewed. Third, the risk and planning literature divides into site-level probabilistic risk models [33]–[36] and path-level exposure costs for a friendly aircraft hiding from radar [37]–[39]. The project inverts the second strand: the same line-of-sight logic is used to find corridors where an intruder could approach unseen. In decision support, threat scoring is usually rule-based or fuzzy, and explicit C-UAS decision support studies are scarce and mostly simulation-based [41], [42]. Peer-reviewed RAG decision support with measured gains comes mainly from emergency triage [50], [51]. Meanwhile, wargame evidence warns against letting LLMs decide [49].

### 3.2.2 Active defence-industry systems

Fielded C-UAS systems range from national kill-chain products to C2 software platforms. Aselsan's İHTAR combines Ku-band radar with EO and thermal cameras and RF jamming [53]. Aselsan added acoustic detection, GNSS spoofing, an FPV jammer and a 25 mm gun in 2024 [54]. DroneShield fuses sensor data in its DroneSentry-C2 software [55], [56], and Dedrone offers an AI-driven C2 platform [57]. Hensoldt's Elysion Mission Core is an open sensor and effector C4I platform [58]. Anduril's Lattice won a US$642M US Marine Corps installation-defence contract [59]. Detection-only sensors, such as Robin Radar IRIS [60], and gun systems, such as Rheinmetall Skyranger 30 [61], complete the picture. The 2025 Danish incidents led to rapid procurement of Weibel and Saab radars [62], [63] and of an AI-based C2 system from Systematic [64]. Table 3.4 summarises these systems. Most details come from manufacturer pages or press releases and are marked accordingly. No public unit prices were found for any of them.

**Table 3.4.** Active defence-industry C-UAS systems.

| System | Manufacturer / country | Sensors | Mitigation | C2 / map picture | Decision support claims |
|---|---|---|---|---|---|
| İHTAR with 2024 add-ons [53], [54] | Aselsan / Türkiye | Ku-band pulsed Doppler radar; daytime and thermal cameras; SEDA 100 acoustic add-on | Directional and omnidirectional RF jamming; BUKALEMUN GNSS spoofing; KANGAL-FPV jammer; KORKUT 25 gun | Networked systems linked to higher-level air-defence C2; no threat map described | Automatic target tracking and classification (per manufacturer) |
| DroneSentry-C2 with SensorFusionAI [55], [56] | DroneShield / Australia | RF, radar, optical and ADS-B inputs | Electronic warfare named as a core technology; no specific effector described in the C2 sources | Single operational picture including crewed traffic via ADS-B | AI fusion reduces false alarms and is "more than a display tool" (per manufacturer) |
| DedroneTracker.AI [57] | Dedrone by Axon / USA | RF, radar, video and acoustic; Remote ID | Operates mitigation tools from the same interface | "Single pane of glass" interface | Single queue of risk-prioritised targets based on behaviour, imagery and flight history (per manufacturer) |
| Elysion Mission Core [58] | Hensoldt / Germany | Open interface for radar, cameras, RF, acoustic, AI image recognition, ADS-B | Open interface for RF and GNSS jammers, high-power electromagnetic effectors, hunter drones, net launchers | Map-based picture with detections, history, assets and zones; mission replay | Automatic prioritisation of high-risk targets; "proposes countermeasures" (per manufacturer) |
| Lattice with Sentry towers [59] | Anduril / USA | Radar with narrow-field IR towers; wide-area IR; RF sensing | Electronic warfare; Anvil interceptor drone | Single C2 interface with fusion and tracking | Automated detection, tracking and identification; humans make the final engagement decision |
| IRIS [60] | Robin Radar / Netherlands | FMCW X-band 3D radar, 5 km instrumented range | None | Feeds third-party C2 through more than 25 integrations | Micro-Doppler bird-versus-drone classification (per manufacturer) |
| Skyranger 30 [61] | Rheinmetall / Germany | Turret sensors including tracking radar | 30 mm revolver cannon with programmable airburst ammunition | Control nodes integrated into Dutch air-defence architecture | Not described |
| Wingman and related devices [62] | MyDefence / Denmark | Wearable and handheld RF detectors | RF jamming (heavily restricted in the EU) | Not described | Not described |
| Giraffe 1X [63] | Saab / Sweden | 3D radar scanning the full volume every second | None in the reported deployment | Not described | Detects, tracks and classifies drones (per manufacturer) |
| SitaWare Headquarters and Insight [64] | Systematic / Denmark | Integrates a national counter-drone sensor network | Not described | Common operational picture | AI analysis, computer vision and automatic anomaly detection (per manufacturer) |

Table 3.4 shows that the commercial C2 products follow a common pattern. They fuse several sensor types, display tracks on a map-based operational picture, classify targets automatically and prioritise threats [55]–[59], [64]. Only Hensoldt states, per manufacturer, that its software proposes countermeasures [58], and none of the sources reviewed explains how a recommendation is justified or linked to doctrine or rules of engagement. The displays show tracks, assets and zones rather than a computed risk surface, and safe-route planning for friendly assets is not mentioned. Detection-only deployments are also common [60], [63]. This matters for civil airports, where RF jamming is heavily restricted in the EU [62], so a detect-and-recommend scope reflects a realistic operational niche rather than a reduced one. Finally, every cost figure found is at programme level, such as the US$642M Anduril contract [59] and a Skyranger order valued in the high hundreds of millions of euros [61]. These figures are several orders of magnitude above a student project budget.

### 3.2.3 Comparison

The project combines one fixed PoE IP camera running a YOLO detector, an ESP32 Wi-Fi receiver that measures signal strength from an ESP32 transmitter on a mock drone, decision-level fusion into a threat score, a grid risk map with terrain and building heights and line of sight, A*/Dijkstra safe routing, and rule-based recommendations explained by an LLM with retrieval-augmented citations from public doctrine such as US Army ATP 3-01.81. Tracks are drawn with MIL-STD-2525 symbols [65] through the open-source milsymbol library. The system detects and recommends only, with a hardware budget of about TRY 10,000 and an outdoor demonstration area of about 15 m × 17 m on campus. Table 3.5 compares representative academic and industry work with the project on the same criteria. For industry systems, "not described" means the feature does not appear in the public sources reviewed, not that the product lacks it.

**Table 3.5.** Comparison of representative work with the project.

| Work / system | Multi-sensor fusion | Risk grid with line of sight | Safe route | Explainable / cited recommendations | Standard symbology | Low cost / open data | Mitigation |
|---|---|---|---|---|---|---|---|
| Svanström et al. [22], [23] | Yes (visible, IR, audio; late fusion) | No | No | No | No | Open dataset; hardware cost not stated | No |
| Lee et al. [30] | Yes (optical, radar, acoustic; decision level) | No | No | No | No | Partly open datasets | No |
| Wewelwala et al. [32] | Yes (passive RF and EO) | No | No | No | No | Non-public data | No |
| Qiu et al. [37] | No (simulation) | Partial (DEM detection risk for a friendly aircraft) | Yes (Risk-A* with MPC) | No | No | Simulation only | No |
| Alhusain [50] | Not applicable | Not applicable | Not applicable | Partial (rule retrieval for medical triage) | Not applicable | Not stated | Not applicable |
| DedroneTracker.AI [57] | Yes (per manufacturer) | Not described | Not described | Risk-prioritised queue; rationale and citations not described | Not described | Unit cost not public | Yes (integrated tools) |
| Hensoldt Elysion [58] | Yes (per manufacturer) | Map with zones; computed risk grid not described | Not described | Proposes countermeasures; justification not described | Not described | Unit cost not public | Yes (via open interface) |
| Anduril Lattice [59] | Yes | Not described | Not described | Automated identification; human decides; rationale not described | Not described | US$642M programme | Yes (EW, interceptor) |
| Aselsan İHTAR [53], [54] | Yes (radar, EO/IR, acoustic add-on) | Not described | Not described | Not described | Not described | Unit cost not public | Yes (jamming, spoofing, gun) |
| Robin Radar IRIS [60] | No (radar only; feeds external C2) | Not described | Not described | Not described | Not described | Unit cost not public | No |
| This project (planned) | Yes (camera and Wi-Fi RF; decision level) | Yes (terrain and building heights, line of sight) | Yes (A*/Dijkstra) | Yes (rule-based, LLM explanation with doctrine citations) | Yes (MIL-STD-2525) | Yes (about TRY 10,000 hardware; public data) | No (detect and recommend) |

## 3.3 Summary and research gap

The reviewed literature establishes three points. Drone incidents close airports mainly because operators cannot quickly confirm and identify a threat [1], [3]–[8]. No single sensor solves small-drone detection, and decision-level fusion of complementary sensors reduces false alarms [1], [10]–[12], [30]. Finally, LLMs are safest when they explain decisions grounded in retrieved rules rather than make those decisions [49]–[52].

Each strand is well developed on its own, but the combination is not. Academic fusion studies stop at detection and classification [22], [30]–[32]. Threat-aware routing studies plan paths for a friendly aircraft in simulation [37]–[39]. Site-level risk models do not produce a per-cell map around a protected site [33]–[36]. Commercial C2 platforms provide fused operational pictures and automated prioritisation, and one claims to propose countermeasures [57]–[59]. However, a computed risk grid with line of sight, safe-route planning, and recommendations that cite doctrine are not described in the public sources reviewed. These systems are also priced at programme level, far beyond a university or small-site budget [59], [61].

The project addresses this gap with a low-cost, end-to-end detect-and-recommend chain. It links decision-level camera and RF fusion, a terrain-aware risk grid that reverses threat-aware path planning to find unseen approach corridors, safe routing over that grid, and explainable recommendations that cite public doctrine, displayed with standard military symbols. To the authors' knowledge, this specific combination has not been described in open literature. Because the search was not exhaustive and industry products may contain undisclosed features, the gap is stated as a gap in public documentation rather than in capability.

## References

[1] G. Lykou, D. Moustakas, and D. Gritzalis, "Defending airports from UAS: A survey on cyber-attacks and counter-drone sensing technologies," *Sensors*, vol. 20, no. 12, Art. no. 3537, 2020, doi: 10.3390/s20123537.

[2] Associated Press, "Drone sighting closes Frankfurt airport for an hour," *The Washington Times*, May 9, 2019. [Online]. Available: https://www.washingtontimes.com/news/2019/may/9/drone-sighting-closes-frankfurt-airport-for-an-hou/

[3] Reuters, "Drones that shut Copenhagen airport flown by 'capable operator', Danish police say," *The Star*, Sep. 23, 2025. [Online]. Available: https://www.thestar.com.my/news/world/2025/09/23/drones-that-shut-copenhagen-airport-flown-by-039capable-operator039-danish-police-say

[4] U. Franke, "Buzzkill: How to defend Europe against drones," European Council on Foreign Relations, Policy Brief, Aug. 17, 2026. [Online]. Available: https://ecfr.eu/publication/buzzkill-how-to-defend-europe-against-drones/

[5] L. Rasmussen, "Drones disrupt flights at second Danish airport in a week," Reuters, via *The Star*, Sep. 25, 2025. [Online]. Available: https://www.thestar.com.my/news/world/2025/09/25/denmark039s-aalborg-airport-closed-due-to-drones-in-airspace

[6] Al Jazeera and AFP, "Munich airport resumes operations after more drone sightings halted flights," *Al Jazeera*, Oct. 4, 2025. [Online]. Available: https://www.aljazeera.com/news/2025/10/4/munich-airport-resumes-operations-after-more-drone-sightings-halted-flights

[7] Reuters, "Belgium scrambles to address airport closures caused by drones," *The Star*, Nov. 5, 2025. [Online]. Available: https://www.thestar.com.my/news/world/2025/11/05/belgium-scrambles-to-address-airport-closures-caused-by-drones

[8] Tweede Kamer der Staten-Generaal, "Verslag van een wetgevingsoverleg (Defence Committee) on the counter-drone supplementary budget, 26 Nov. 2025," Kamerstuk 36 858, no. 6, adopted 17 Dec. 2025. [Online]. Available: https://zoek.officielebekendmakingen.nl/kst-36858-6.pdf

[9] C. Edwards, R. Fox O'Loughlin, and L. Bearn, "Russia's UAV campaign over Europe," International Institute for Strategic Studies (IISS), London, U.K., Jul. 2026.

[10] U. Seidaliyeva, L. Ilipbayeva, K. Taissariyeva, N. Smailov, and E. T. Matson, "Advances and challenges in drone detection and classification techniques: A state-of-the-art review," *Sensors*, vol. 24, no. 1, Art. no. 125, 2024, doi: 10.3390/s24010125.

[11] K. D. Brewczyński, M. Życzkowski, K. Cichulski, K. A. Kamiński, P. Petsioti, and G. De Cubber, "Methods for assessing the effectiveness of modern counter unmanned aircraft systems," *Remote Sensing*, vol. 16, no. 19, Art. no. 3714, 2024, doi: 10.3390/rs16193714.

[12] B. Wang, Q. Li, Q. Mao, J. Wang, C. L. P. Chen, A. Shangguan, and H. Zhang, "A survey on vision-based anti unmanned aerial vehicles methods," *Drones*, vol. 8, no. 9, Art. no. 518, 2024, doi: 10.3390/drones8090518.

[13] S. Park, H. T. Kim, S. Lee, H. Joo, and H. Kim, "Survey on anti-drone systems: Components, designs, and challenges," *IEEE Access*, vol. 9, pp. 42635–42659, 2021, doi: 10.1109/ACCESS.2021.3065926.

[14] B. Taha and A. Shoufan, "Machine learning-based drone detection and classification: State-of-the-art in research," *IEEE Access*, vol. 7, pp. 138669–138682, 2019, doi: 10.1109/ACCESS.2019.2942944.

[15] M. Ezuma, C. K. Anjinappa, M. Funderburk, and I. Guvenc, "Radar cross section based statistical recognition of UAVs at microwave frequencies," arXiv:2102.11954, Feb. 2021.

[16] M. Ezuma, M. Funderburk, and I. Guvenc, "Compact-range RCS measurements and modeling of small drones at 15 GHz and 25 GHz," arXiv:1911.05926, Nov. 2019.

[17] Y. Cui, J. Nie, W. Yuan, F. Liu, Z. Jia, J. Xu, Z. Feng, and M.-S. Alouini, "Low-altitude wireless networks: The next horizon of wireless infrastructure," arXiv:2605.24368, May 2026, Sec. 4.2.3.

[18] J. Zhao, J. Zhang, D. Li, and D. Wang, "Vision-based anti-UAV detection and tracking," arXiv:2205.10851, 2022 (accepted by *IEEE Trans. Intell. Transp. Syst.*), doi: 10.48550/arXiv.2205.10851.

[19] N. Jiang, K. Wang, X. Peng, X. Yu, Q. Wang, J. Xing, G. Li, J. Zhao, G. Guo, and Z. Han, "Anti-UAV: A large multi-modal benchmark for UAV tracking," arXiv:2101.08466, 2021.

[20] A. Coluccia, A. Fascista, A. Schumann, L. Sommer, A. Dimou, D. Zarpalas, M. Méndez, D. de la Iglesia, I. González, J.-P. Mercier, G. Gagné, A. Mitra, and S. Rajashekar, "Drone vs. bird detection: Deep learning algorithms and results from a grand challenge," *Sensors*, vol. 21, no. 8, Art. no. 2824, 2021, doi: 10.3390/s21082824.

[21] A. Coluccia, A. Fascista, L. Sommer, A. Schumann, A. Dimou, and D. Zarpalas, "The Drone-vs-Bird detection grand challenge at ICASSP 2023: A review of methods and results," *IEEE Open J. Signal Process.*, vol. 5, pp. 766–779, 2024, doi: 10.1109/OJSP.2024.3379073.

[22] F. Svanström, C. Englund, and F. Alonso-Fernandez, "Real-time drone detection and tracking with visible, thermal and acoustic sensors," in *Proc. 25th Int. Conf. Pattern Recognit. (ICPR)*, 2021; arXiv:2007.07396.

[23] F. Svanström, F. Alonso-Fernandez, and C. Englund, "A dataset for multi-sensor drone detection," *Data in Brief*, vol. 39, Art. no. 107521, 2021.

[24] Y. Zhao, L. Wang, G. Lei, C. Guo, and Q. Ma, "Lightweight UAV small target detection and perception based on improved YOLOv8-E," *Drones*, vol. 8, no. 11, Art. no. 681, 2024, doi: 10.3390/drones8110681.

[25] S. Yuan, Y. Yang, T. H. Nguyen, T.-M. Nguyen, J. Yang, F. Liu, J. Li, H. Wang, and L. Xie, "MMAUD: A comprehensive multi-modal anti-UAV dataset for modern miniature drone threats," in *Proc. IEEE Int. Conf. Robot. Autom. (ICRA)*, 2024, pp. 2745–2751, doi: 10.1109/ICRA57147.2024.10610957.

[26] M. S. Allahham, M. F. Al-Sa'd, A. Al-Ali, A. Mohamed, T. Khattab, and A. Erbad, "DroneRF dataset: A dataset of drones for RF-based detection, classification and identification," *Data in Brief*, vol. 26, 2019.

[27] S. Glüge, M. Nyfeler, A. Aghaebrahimian, N. Ramagnano, and C. Schüpbach, "Robust low-cost drone detection and classification using convolutional neural networks in low SNR environments," arXiv:2406.18624v3, Nov. 2024.

[28] L. Bi, Z.-X. Xu, and L. Yang, "Low-cost UAV detection via WiFi traffic analysis and machine learning," *Sci. Rep.*, vol. 13, Art. no. 20892, 2023, doi: 10.1038/s41598-023-47453-6.

[29] A. Alsoliman, G. Rigoni, M. Levorato, C. M. Pinotti, N. O. Tippenhauer, and M. Conti, "COTS drone detection using video streaming characteristics," in *Proc. Int. Conf. Distrib. Comput. Netw. (ICDCN '21)*, Nara, Japan, 2021, doi: 10.1145/3427796.3428480.

[30] H. Lee, S. Han, J.-I. Byeon, S. Han, R. Myung, J. Joung, and J. Choi, "CNN-based UAV detection and classification using sensor fusion," *IEEE Access*, vol. 11, pp. 68791–68808, 2023, doi: 10.1109/ACCESS.2023.3293124.

[31] G. Ganganath, P. Sankalpa, S. Punsara, D. Pasindu, C. U. S. Edussooriya, R. Rodrigo, and U. S. K. P. Miriya Thanthrige, "Radar and acoustic sensor fusion using a transformer encoder for robust drone detection and classification," arXiv:2507.19785v2, 2025.

[32] T. W. Wewelwala, T. W. Tedesso, and T. Davis, "Multi-stage fusion architecture for small-drone localization and identification using passive RF and EO imagery: A case study," arXiv:2406.16875, 2024.

[33] D. Pascarella *et al.*, "A methodological framework for the risk assessment of drone intrusions in airports," *Aerospace*, vol. 9, no. 12, Art. no. 747, 2022, doi: 10.3390/aerospace9120747.

[34] C. Li, J. Lin, X. Zhang, Y. Zhou, S. Zhang, and Y. Zheng, "Analysing the risks of an unmanned aircraft accident near airport using a Bayesian network," *The Aeronautical Journal*, vol. 130, no. 1351, pp. 2865–2883, 2026, doi: 10.1017/aer.2026.10191.

[35] C. Wang and S. M. Hubbard, "Characteristics of unmanned aircraft system (UAS) sightings and airport safety," *J. Aviation Technology and Engineering*, vol. 10, no. 2, p. 16, 2022, doi: 10.7771/2159-6670.1238.

[36] N. Fotiou, K. Katzis, S. Katsaronas, and H. Ahmadi, "A hierarchical quantitative risk assessment framework for evaluating performance and resilience in drone-assisted systems," *Drones*, vol. 10, no. 5, p. 370, 2026, doi: 10.3390/drones10050370.

[37] Y. Qiu, T. Yang, and Y. Liu, "Risk-A* and real-time MPC for detection-risk-aware low-altitude path planning of a fixed-wing medium-altitude long-endurance UAV in mountainous terrain with dynamic radar-based sensing constraints," *Drones*, vol. 10, no. 6, p. 469, 2026, doi: 10.3390/drones10060469.

[38] B. Dong, G. Zhang, Y. Yang, P. Yuan, and S. Lu, "A Voronoi–A* fusion algorithm with adaptive layering for efficient UAV path planning in complex terrain," *Drones*, vol. 9, no. 8, p. 542, 2025, doi: 10.3390/drones9080542.

[39] L. Bao, Z. Guo, X. Gao, and C. Li, "Stealth UAV path planning based on DDQN against multi-radar detection," *Aerospace*, vol. 12, no. 9, p. 774, 2025, doi: 10.3390/aerospace12090774.

[40] Y. Li, X. Dong, Q. Ding, Y. Xiong, H. Liao, and T. Wang, "Improved A-STAR algorithm for power line inspection UAV path planning," *Energies*, vol. 17, no. 21, p. 5364, 2024, doi: 10.3390/en17215364.

[41] A. A. Bolshakov and A. A. Kulik, "Algorithm of a device designed to support decision making to counter the threat of an aviation accident," *Herald of the Bauman Moscow State Technical University, Ser. Instrument Engineering*, no. 3 (136), pp. 46–59, 2021, doi: 10.18698/0236-3933-2021-3-46-59.

[42] D. Hotters, "A novel approach to quantify counter-drone system effectiveness against UAS swarms," *Materials Research Proceedings*, vol. 69, pp. 856–860, 2026, doi: 10.21741/9781644904251-151.

[43] K. M. Nagamothu, S. Mahadev, and M. T. Sai, "An adaptive real-time threat severity assessment system using machine learning for low-latency decision support in defense environments," Preprints, 2026, doi: 10.20944/preprints202605.0126.v1.

[44] M. Kramer, "From transparency to trust: Explainable AI for object detection in safety-critical defence applications," in *HHAI 2026*, Frontiers in Artificial Intelligence and Applications, 2026, doi: 10.3233/faia260558.

[45] P. Lushenko, "Battlefield trust for human-machine teaming: Evidence from the US military," SSRN, 2023, doi: 10.2139/ssrn.4654703.

[46] M. Athanasiadou, G. Franzini, and A. Metge, "Beyond automation levels: A framework for human–autonomy and manned–unmanned teaming," *Automation*, vol. 7, no. 4, p. 105, 2026, doi: 10.3390/automation7040105.

[47] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, H. Küttler, M. Lewis, W.-t. Yih, T. Rocktäschel, S. Riedel, and D. Kiela, "Retrieval-augmented generation for knowledge-intensive NLP tasks," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 33, 2020; arXiv:2005.11401.

[48] Y. Gao, Y. Xiong, X. Gao, K. Jia, J. Pan, Y. Bi, Y. Dai, J. Sun, M. Wang, and H. Wang, "Retrieval-augmented generation for large language models: A survey," arXiv:2312.10997, 2023.

[49] J.-P. Rivera, G. Mukobi, A. Reuel, M. Lamparth, C. Smith, and J. Schneider, "Escalation risks from language models in military and diplomatic decision-making," in *Proc. 2024 ACM Conf. Fairness, Accountability, and Transparency (FAccT '24)*, 2024, pp. 836–898, doi: 10.1145/3630106.3658942.

[50] L. Alhusain, "TRAG: A rule retrieval-augmented generation framework for emergency triage," *Applied Sciences*, vol. 16, no. 9, p. 4533, 2026, doi: 10.3390/app16094533.

[51] H. S. Wong and T. K. Wong, "Multi-evidence clinical reasoning with retrieval-augmented generation for emergency triage: Retrospective evaluation study," JMIR Preprints, 2025, doi: 10.2196/preprints.82026.

[52] J. Bellapukonda, "Evaluating hallucination mitigation in retrieval-augmented generation systems through guarded response strategies, embedding comparison, and retrieval depth analysis," SSRN, 2026, doi: 10.2139/ssrn.6702638.

[53] Unmanned Systems Technology, "İHTAR counter-UAS system – ASELSAN." [Online]. Available: https://www.unmannedsystemstechnology.com/company/aselsan/ihtar/

[54] European Security & Defence, "New ASELSAN C-UAV systems," Oct. 22, 2024. [Online]. Available: https://euro-sd.com/2024/10/major-news/40982/new-aselsan-c-uav-systems/

[55] EDR Magazine, "DroneShield expands airspace security with ADS-B integration into its DroneSentry-C2 software," Oct. 2025. [Online]. Available: https://www.edrmagazine.eu/droneshield-expands-airspace-security-with-ads-b-integration-into-its-dronesentry-c2-software

[56] DroneShield, "Sensor Fusion AI." [Online]. Available: https://droneshield.com/capabilities/sensor-fusion-ai

[57] Dedrone, "Dedrone launches DedroneTracker.AI, the AI-driven command-and-control platform enabling the complete counterdrone kill chain," press release, Jul. 12, 2023. [Online]. Available: https://dedrone.com/press/dedrone-launches-dedronetracker-ai-the-ai-driven-command-and-control-platform-enabling-the-complete-counterdrone-kill-chain

[58] HENSOLDT, "Elysion C-UAS Mission Core." [Online]. Available: https://hensoldt.net/products/elysion-mission-core-best-in-class-counter-uas-software

[59] DefenseScoop, "Marine Corps awards Anduril contract to defend installations from small drones," Mar. 13, 2025. [Online]. Available: https://defensescoop.com/2025/03/13/marine-corps-anduril-contract-defend-installations-small-uas-drones/

[60] Robin Radar Systems, "Drone detection radar system (IRIS)." [Online]. Available: https://www.robinradar.com/drone-detection-radar-system

[61] Unmanned Airspace, "Dutch Ministry of Defence orders Rheinmetall Skyranger air defence/C-UAS systems," Dec. 2025. [Online]. Available: https://www.unmannedairspace.info/counter-uas-systems-and-policies/dutch-ministry-of-defence-orders-rheinmetall-skyranger-air-defence-c-uas-systems/

[62] Associated Press, "This anti-drone technology is used on the Ukrainian battlefield and in NATO airspace after flyovers," *BNN Bloomberg*, Nov. 12, 2025. [Online]. Available: https://www.bnnbloomberg.ca/business/2025/11/12/this-anti-drone-technology-is-used-on-the-ukrainian-battlefield-and-in-nato-airspace-after-flyovers/

[63] defence-industry.eu, "Denmark orders Saab Giraffe 1X radars after rapid deployment for Copenhagen security summits and drone detection," Jun. 2026. [Online]. Available: https://defence-industry.eu/denmark-orders-saab-giraffe-1x-radars-after-rapid-deployment-for-copenhagen-security-summits-and-drone-detection/

[64] Militarnyi, "Denmark orders AI-based command and control system to counter drones," Oct. 8, 2026. [Online]. Available: https://militarnyi.com/en/news/denmark-ai-command-control-system-anti-uav/

[65] U.S. Department of Defense, MIL-STD-2525E.

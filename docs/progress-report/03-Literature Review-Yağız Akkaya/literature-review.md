# Literature Review

**Owner:** Yağız Akkaya · **Weight:** 30%

*Source note: every source in this section was already catalogued and checked by the team: in the project repository (`layers/`, `docs/pilot-region/`, `docs/computational-model/`) and, for the Turkish defence industry, in the team's industry survey of 19 October 2026. No new external source is introduced here.*

## 3.1 Theoretical background

### 3.1.1 The problem: small drones at airports and military bases

Small unmanned aircraft systems (UAS) have repeatedly closed airports and alarmed military installations. A survey of airport incidents between 2016 and 2019 lists ten serious cases, including the Gatwick closure of December 2018 and the Frankfurt disruption of 2019 [1]. Since 2024 the problem has moved from isolated nuisance flights to a sustained pattern: an International Institute for Strategic Studies (IISS) study counts 144 incidents in 13 European countries between August 2024 and February 2026 [2]. Table 3.1 lists the documented cases collected in the team's surveys of the four candidate pilot regions: Eindhoven, Gatwick, Aalborg and Akrotiri (Crete). They are presented as general evidence of the problem, not as a choice of pilot region.

**Table 3.1.** Documented drone incidents used as reference cases.

| Date | Location | What happened | Operational impact | Sources |
|---|---|---|---|---|
| Dec 2018 | Gatwick Airport, UK | Drone sightings closed the airport; the incident was later reviewed by the Sussex Police and Crime Commissioner | Closure of about 30 h according to the official review and 33 h according to a later cost study; the case is used in the introductions of later cost and risk studies | [3], [4], [1], [5] |
| 24–25 Sep 2025 | Aalborg Airport, Denmark (joint civil and military) | Several drones with lights on were seen at night from about 21:44 to 00:54; the airport is also used by the military | Closure of about 3 h; part of the September 2025 wave over Danish airports | [6], [7] |
| 21 Nov 2025 | Volkel Air Base, Netherlands | Guards saw first 5, then 10 drones in darkness; the military fired from the ground; the drones flew off and were not found | Security response at a NATO air base | [8], [9] |
| 22 Nov 2025 | Eindhoven Airport, Netherlands (joint civil and military) | Multiple drones sighted in the evening; Ministry of Defence counter-drone systems on standby | All civil and military flights halted for about two hours and diverted to other airports; no drone recovered | [10], [9] |
| 2012 – Oct 2026 | NATO Missile Firing Installation (NAMFI) and Souda, Crete, Greece | NATO's live-fire range in Europe, where Patriot and IRIS-T SLM units train against target drones; in February 2026 the Souda base was sealed after threats against US installations | No hostile drone incursion over Chania Airport, Souda Air Base or NAMFI was found in public reports; the site shows the training side of counter-drone defence | [11], [12], [13], [14] |
| Aug 2024 – Feb 2026 | 13 European countries | Systematic analysis of 144 incidents; the Volkel and Eindhoven drones were assessed as most likely launched from ships off the Dutch coast | Cumulative disruption of civil and military sites | [2], [15] |

The incidents share one pattern. A drone is reported, the operator cannot confirm what it is or where it is going, and the site closes as a precaution. The cost of this uncertainty is large. A cost model built on the Frankfurt case found that a counter-drone investment is economically justified in certain closure scenarios, and that airlines carry most of the losses [4]. The response time is also short: with drone speeds of 10–20 m/s, a 6–10 km protective zone gives only about 5–10 minutes of warning [1]. At the same time, mitigation is constrained. Civil radio-frequency (RF) jamming is illegal in many countries and can interfere with landing systems, and no international standard exists for counter-UAS (C-UAS) use at airports [1]; jamming near an airport also affects the airport's own systems [16]. The central need is therefore fast and confident detection, identification and decision support, rather than the ability to destroy the drone.

### 3.1.2 Detection sensors and why one sensor is not enough

Detecting a small drone is physically difficult, and each sensor modality fails in a different way. Table 3.2 summarises the strengths and weaknesses reported in the sources held in the repository.

**Table 3.2.** Small-drone detection sensor modalities.

| Sensor | Strengths | Weaknesses | Sources |
|---|---|---|---|
| Radar | Proposed as the primary detection layer at airports | Small drones have a very low radar cross section (RCS), similar to that of birds; birds cause false alarms; small, slow, low-flying targets are hard to track | [1], [16], [17], [18], [19] |
| RF detection | Detects the drone's radio control or video link; used with cameras for identification | Misses autonomous drones that do not transmit; depends on line of sight | [1], [19] |
| Visible and infrared cameras | Identification layer; images allow human confirmation | Need line of sight; drones are confused with birds; range is limited by the pixels on target: about 7 pixels are needed for detection and 15 for assessment [20]; under the DRI criteria, fewer than 5 pixels allow detection only, 5–15 recognition and more than 15 identification [21] | [1], [16], [20], [21] |
| Acoustic | Does not depend on the drone transmitting radio signals | Short range, typically under 300 m; not reliable in airport noise | [1] |

Radar is often assumed to solve detection on its own, but measured RCS values show why it does not. Compact-range measurements of commercial drones such as the DJI Matrice, Mavic and Phantom at 15 GHz and 25 GHz gave RCS values mostly between −12 and −17 dBsm [17], [22]. A recent survey reports UK Civil Aviation Authority tests in which DJI Phantom-class quadcopters, with an RCS as low as −23 dBsm, could not be reliably tracked beyond 500 m by standard airport-surveillance radar [18]. The airport survey therefore concludes that "adopting a single sensor technology for UAV detection in airports cannot provide the desired situational awareness" [1], and the European Council on Foreign Relations (ECFR) recommends sensor fusion for the same reasons [16]. Sensor simulation work models these weaknesses explicitly through the radar equation, constant false-alarm-rate detection and false-alarm rates, and evaluates sensor mixes in an agent-based simulator [23]. These findings justify the project's choice of two low-cost sensors with different failure modes: a camera, which cannot see behind obstacles, and an RF receiver, which cannot detect a silent autonomous drone.

### 3.1.3 Geospatial reasoning: line of sight, terrain and air traffic

Every sensor in Table 3.2 except acoustics needs line of sight, so a threat map must know where the sensors can and cannot see. Line of sight over a terrain model can be computed with an input/output-efficient radial sweep in O(n log n) time [24]. This requires surface heights. Global digital surface models such as Copernicus GLO-30 and ALOS AW3D30 provide terrain at 30 m resolution [25], [26]; in a validation of eight models in Greece, Copernicus DEM gave the best overall results, with a standard deviation of about 1–1.5 m [27]. OpenStreetMap adds roads, buildings and facility boundaries [28], but its building heights are often missing. Where national data exist, much finer models are available. The Dutch 3DBAG dataset reconstructs all 10 million buildings in the Netherlands from LiDAR with an error below 31 cm (RMSE) for 95% of buildings [29], and Danish national LiDAR data are used in peer-reviewed environmental work [30]. For regions without such data, the open GlobalBuildingAtlas offers global building heights with a reported RMSE of 4.1 m in Europe [31]. Table 3.3 summarises what the team's regional surveys found.

**Table 3.3.** Geospatial data found in the team's candidate pilot-region surveys.

| Region | Terrain and surface | Buildings | Drone restriction zones | Air traffic |
|---|---|---|---|---|
| Eindhoven, Netherlands | AHN national LiDAR | 3DBAG heights for every building [29] | National API retired in June 2026; runway buffer used as an assumption | OpenSky live; open ADS-B archive covers the incident night |
| Gatwick, UK | Environment Agency 1 m DTM and DSM, Open Government Licence | No complete 3D building model verified; surface heights from the DSM | NATS UAS restriction dataset downloaded | OpenSky live query returned aircraft |
| Aalborg, Denmark | DHM national model, 0.4 m grid, free account required [30] | OSM footprints without heights | Official map only, no reusable dataset | OpenSky live |
| Akrotiri, Crete | Copernicus GLO-30, 30 m [25], [27] | OSM: no height tags; GlobalBuildingAtlas to be tested [31] | Official map only (HCAA), no download | Airport statistics; OpenSky not yet tested |
 Finally, the decision engine must know the normal air traffic around a site in order to judge a track near a runway. The OpenSky Network provides an ADS-B research database for this baseline, but it only sees aircraft that broadcast ADS-B, its low-altitude coverage has gaps, and drones are invisible to it [32]. Drone detection must therefore come from the project's own sensors.

## 3.2 Previous work

### 3.2.1 Academic studies

Table 3.4 lists the key studies the team has reviewed, grouped by the layer of the system they support, and states how each one is used in the project. The doctrine behind the knowledge base is covered separately in Section 3.2.2.

**Table 3.4.** Key studies relevant to the project, grouped by system layer.

| Ref. | Year | Topic | Method | Key finding | Relevance to the project |
|---|---|---|---|---|---|
| **Detection and sensing (camera and RF)** | | | | | |
| [1] | 2020 | Sensing | Survey of airport incidents and C-UAS sensors; three attack scenarios with protection plans | No single sensor gives adequate situational awareness; mitigation at airports is legally constrained | Basis for sensor fusion and for recommending rather than executing countermeasures |
| [17], [22] | 2019–2021 | Sensing (radar) | Compact-range RCS measurements of commercial drones at 15 and 25 GHz | RCS mostly −12 to −17 dBsm | Quantitative argument against radar-only detection |
| [21] | 2021 | Detection dataset (camera) | Infrared, visible and audio recordings at three Nordic airports with airplane, helicopter and bird classes; DRI pixel criteria | Fewer than 5 pixels allow detection only, more than 15 identification | Night and infrared training data and pixel thresholds for the project camera |
| Table 3.5 | 2019–2024 | Detection datasets | Open visible, infrared, multi-modal and RF datasets | See Table 3.5 | Training and testing data for the YOLO detector and the RF chain |
| **Risk map, line of sight and routing** | | | | | |
| [5] | 2022 | Risk assessment | Airport vulnerability index combined with event trees; case study at Milan Malpensa | Quantitative, systematic assessment of drone-intrusion impact on an airport | Closest precedent for the risk engine; airport-level, not per grid cell |
| [4] | 2020 | Risk assessment (economic) | Simulation of a drone-related shutdown at Frankfurt | Counter-drone investment is justified in certain closure scenarios; airlines bear most losses | Supports the motivation of the project |
| [29] | 2022 | Geospatial data | Automated LoD1/LoD2 reconstruction of all Dutch buildings from BAG and AHN LiDAR | RMSE below 31 cm for 95% of buildings | Building heights for line of sight where 3DBAG is available |
| [33] | 2025 | Path planning | Benchmark of 12 global optimisers on UAV path-planning instances | Threats modelled as cylinders with distance-based penalties in the cost function | Template for the threat-cost term of the grid cost surface |
| **Tracking, fusion and threat assessment** | | | | | |
| [34] | 2025 | Threat assessment and fusion | Three-stage hierarchical fuzzy decision-making for C-UAS sensor selection (MATLAB) | Fuzzy logic can combine sensor evidence into a threat decision; validated only in simulation | Main alternative to the project's transparent weighted threat score |
| [35] | 2023 | Threat assessment | Deep mixture-of-experts network on non-cooperative radar tracks | About 98% accuracy in drone intent classification; 15–30 s position bounds | Learned alternative to the project's trajectory prediction; noted as future work |

Learning-based detection depends on open datasets. Table 3.5 lists the drone detection datasets that the project has catalogued and checked for access. The visible-light and infrared datasets support the YOLO detector, and the RF datasets support the design of the RF detection chain.

**Table 3.5.** Open drone detection datasets catalogued by the project.

| Dataset | Modality | Content | Access | Source |
|---|---|---|---|---|
| DUT Anti-UAV | Visible | 10,000 annotated images and 20 tracking videos | Open (MIT) | [36] |
| Anti-UAV (300/410/600) | Visible and infrared | Tracking benchmark series | Gated platform access | [37] |
| Halmstad multi-sensor | Infrared, visible, audio | 650 videos (365 IR, 285 visible), 90 audio clips, more than 203,000 annotated frames | Open | [21] |
| UAVSwarm | Visible | 72 sequences with multi-object tracking labels | Open (CC BY 4.0) | [38] |
| MMAUD | Stereo RGB, LiDAR, mmWave radar, microphone array | Multi-modal recordings with 3D trajectory labels | Open (CC BY-NC-SA 4.0) | [39] |
| Drone-vs-Bird | Visible | Challenge data with drones and birds | Request only, signed agreement | [40] |
| TIB-Net | Visible | 2,850 images for tiny-target detection | Open | [41] |
| DroneRF | RF | Signal segments of 3 drone models, more than 40 GB | Open | [42] |
| DroneDetect | RF | Software-defined-radio recordings of 7 UAS models | Open, free login | [43] |

### 3.2.2 Doctrine, policy and standards

A decision support system must base its recommendations on accepted procedures, not on the reasoning of a language model alone. The project's knowledge base is therefore built only from unclassified, publicly readable doctrine and analysis [44], [45], [46]. Table 3.6 lists the corpus and what each document contributes.

**Table 3.6.** Doctrine, policy and standards in the project's knowledge base.

| Source | Type | Content used by the project |
|---|---|---|
| ATP 3-01.81, *Counter-Unmanned Aircraft System Techniques* (Dec. 2023) [44] | U.S. Army doctrine | UAS group classification (Groups 1–3), the layered-defence concept and the detect–identify–defeat cycle |
| DoD Strategy for Countering Unmanned Systems (2024) [45] | U.S. strategy | The five "strategic ways": top-level principles for the knowledge base's answers |
| CRS Report R48477 [46] | Congressional research report | Summary table of C-UAS programmes and a terminology glossary |
| RAND reports on counter-UAS at military installations (2023–2026) [47] | Research reports | Analysis of installation defence against drones |
| CNAS, "Countering the Swarm" [48] | Think-tank report | Drone swarm tactics; doctrinal basis for the swarm clustering module |
| RUSI publications on drone warfare in Ukraine [49] | Think-tank analysis | Tactical development of drone and counter-drone use |
| ISW, *Russian Offensive Campaign Assessment* [50] | Daily analysis | Current evolution of drone tactics |
| NATO "Drone Edge" and Project Flytrap releases [51] | Official press releases | Current NATO counter-drone context |
| NATO IAMD COE, *The Evolving Asymmetric Threat of Unmanned Aircraft Systems* [19] | NATO centre of excellence report | Drones have a bird-like radar signature; passive RF sensors detect the controller link |
| IISS [2], ECFR [16] and BISI [15] | Think-tank and policy studies | European incident pattern, sensor limits near airports, the case for sensor fusion |
| MIL-STD-2525 and STANAG APP-6 [52], rendered with milsymbol [53] | Symbology standard and open library | Standard friend, hostile and unknown symbols on the C2 map |

The way this corpus is used follows from two design rules. First, documents are embedded in paragraph- or section-level chunks with the source and page number attached to every chunk, because retrieval quality drops on whole-document embeddings and because every answer must be able to cite its page. Second, the language model never decides the action. A rule table maps the threat level and context to a recommended action, and the retrieved doctrine is used only to explain the rule that fired, with page citations. Table 3.7 shows the rule table defined in the project's computational model.

**Table 3.7.** Recommendation rules of the decision layer.

| Threat level | Recommended action |
|---|---|
| Low | Monitor and keep tracking |
| Medium | Alert the operator and point the camera to the predicted sector |
| High, inside the approach corridor | Recommend suspending runway operations and notify air traffic control |
| Critical | Recommend a full stop of traffic and escalation to the authorities |

Mitigation such as jamming is never recommended automatically, because civil RF jamming is illegal in many countries and can interfere with landing systems [1]. The rules are therefore limited to monitoring, alerting and recommending, in line with the detect–identify–defeat cycle of the doctrine [44], where the defeat step remains a human decision.

### 3.2.3 Active systems in the Turkish defence industry

Counter-drone capability is also an active industrial field in Türkiye. Before contacting companies for project feedback, the team surveyed the publicly announced C-UAS products of Turkish defence companies. Table 3.8 summarises them. The information comes from public news reports and trade press, so it describes what the companies have announced, not tested performance.

**Table 3.8.** Publicly announced counter-drone systems of Turkish defence companies.

| Company | System | Type, as publicly reported | Relation to the project | Sources |
|---|---|---|---|---|
| ASELSAN | İHTAR | Counter-UAV system, first shown at IDEF 2019 | Main Turkish counter-UAV product for the threat the project addresses | [54], [55] |
| ASELSAN | SEDA 100-cUAV | Acoustic drone detection sensor | Shows acoustic sensing as an extra layer beside radar and cameras | [55] |
| ASELSAN | KANGAL-FPV and new C-UAS electronic warfare systems (SAHA 2026) | Electronic warfare systems against drones, added to the Steel Dome (Çelik Kubbe) air defence architecture | Mitigation layer that the project deliberately leaves out | [55], [56], [57] |
| Meteksan Savunma | Retinar | Drone detection radar, deliveries reported in 2020 | Radar layer; relevant to the RCS argument | [58] |
| Meteksan Savunma | KAPAN | Drone countermeasure system | Detection and response product | [59] |
| SDT Uzay ve Savunma | AVCI | Anti-drone system and tactical anti-drone rifle, RF and electronic systems | RF-based approach, closest to the project's RF receiver | [60], [61] |
| STM | TUNGA-X | Interceptor anti-drone UAV, first shown at SAHA 2026 | Hard-kill response option; outside the project's scope | [62] |
| ROKETSAN | ALKA | Laser weapon against drones | Directed-energy response option; outside the project's scope | [63] |
| HAVELSAN | Command-and-control and C4ISR software | C2, simulation and AI software; autonomous CBRN reconnaissance UAV with decision support integration | Closest industrial match to the project's fusion, C2 and decision support layer | [64] |

The Turkish products concentrate on sensing and on response (jamming, interceptor drones, lasers and guns). The public reports describe what each system detects or defeats, but they do not describe how the operator is helped to decide, for example through a computed risk map or recommendations that cite doctrine. This is consistent with the gap identified in the academic literature.

### 3.2.4 Comparison with the project

Table 3.9 compares representative studies from Tables 3.4, 3.6 and 3.8 with the project on the same criteria. A dash means that the feature is not part of that work or is not described in its public sources.

**Table 3.9.** Comparison of representative previous work with the project.

| Work | Multi-sensor fusion | Grid risk map with line of sight | Safe route | Recommendation with cited doctrine | Standard symbology | Validated on real hardware |
|---|---|---|---|---|---|---|
| Lykou et al. [1] | Recommended (survey) | – | – | Analytical protection plans | – | No |
| Besada et al. [23] | Simulated sensor mix | – | – | – | – | Simulation only |
| Arapoglou et al. [34] | Fuzzy fusion | – | – | Fuzzy threat decision, no citations | – | Simulation only |
| Fraser et al. [35] | Radar only | – | – | Intent class, no recommendation | – | Recorded radar data |
| Pascarella et al. [5] | – | Airport-level index, no grid | – | – | – | Case study |
| Shehadeh and Kudela [33] | – | Cylindrical threat cost | Yes | – | – | Benchmark only |
| ATP 3-01.81 [44] | Doctrinal guidance | – | – | Doctrine itself, not a system | – | – |
| Turkish C-UAS products (İHTAR, KAPAN, AVCI) [54], [59], [60] | Detection and response products (as reported) | – | – | – | – | Fielded products |
| **This project** | Camera + RF, decision level | Yes, with terrain and building heights | A* / D* Lite | Rule-based recommendation explained with retrieved doctrine citations | MIL-STD-2525 | Campus demo with camera and ESP32 |

## 3.3 Summary and research gap

The literature agrees on the nature of the problem. Small drones repeatedly close airports and approach military bases [1], [2]; the closures are driven by uncertainty rather than by collisions; and the economic cost is large enough to justify counter-drone investment [4]. It also agrees that no single sensor is sufficient [1], [16], because small drones have a very low RCS [17], [18], cameras need line of sight [20], and RF sensing misses autonomous drones [1]. Separate research streams provide the building blocks the project needs: sensor simulation [23], threat assessment by fuzzy logic or learning [34], [35], airport risk frameworks [5], threat-aware path planning [65], [33], accurate building and terrain data [29], [25], and open detection datasets [36], [21], [42].

The gap lies in their combination. In the sources reviewed, these elements appear as separate studies: risk is assessed at the level of a whole airport rather than per map cell [5], threat decisions are made without reference to doctrine [34], and path-planning studies model threats as fixed cylinders without live sensor input [33]. Fielded Turkish products cover sensing and response, but their public descriptions do not address operator decision support [54], [59], [60]. None of the works reviewed links low-cost multi-sensor detection to a line-of-sight-aware grid risk map, safe routing and operator recommendations that cite public doctrine, displayed with standard military symbology. The project addresses this gap with a low-cost, detect-and-recommend system built on open data and verified sources. Its claims are bounded accordingly: the demo is small in scale and uses a single camera and a mock drone, so it demonstrates the integrated decision chain rather than operational detection performance.

## References

[1] G. Lykou, D. Moustakas, and D. Gritzalis, "Defending airports from UAS: A survey on cyber-attacks and counter-drone sensing technologies," *Sensors*, vol. 20, no. 12, Art. no. 3537, 2020, doi: 10.3390/s20123537.

[2] C. Edwards, R. Fox O'Loughlin, and L. Bearn, "Russia's UAV campaign over Europe," International Institute for Strategic Studies (IISS), London, U.K., Jul. 2026. [Online]. Available: https://www.astrid-online.it/static/upload/russ/russia-uav-campaign-over-europe.pdf

[3] Office of the Sussex Police and Crime Commissioner, "Performance and Accountability Meeting minutes," 18 Oct. 2019, pp. 3–5 (review of the December 2018 Gatwick drone incident). [Online]. Available: https://www.sussex-pcc.gov.uk/media/4422/10-pam-minutes-18102019.pdf

[4] P. Wendt, A. Voltes-Dorta, and P. Suau-Sanchez, "Estimating the costs for the airport operator and airlines of a drone-related shutdown: An application to Frankfurt international airport," *J. Transp. Secur.*, vol. 13, no. 1, pp. 93–116, 2020, doi: 10.1007/s12198-020-00212-4.

[5] D. Pascarella, G. Gigante, A. Vozella, P. Bieber, T. Dubot, E. Martinavarro, G. Barraco, and G. Li Calzi, "A methodological framework for the risk assessment of drone intrusions in airports," *Aerospace*, vol. 9, no. 12, Art. no. 747, 2022, doi: 10.3390/aerospace9120747.

[6] Reuters (via The Star), "Denmark's Aalborg airport closed due to drones in airspace," 25 Sep. 2025. [Online]. Available: https://www.thestar.com.my/news/world/2025/09/25/denmark039s-aalborg-airport-closed-due-to-drones-in-airspace

[7] Danish National Police (Rigspolitiet), press releases on drone activity at Aalborg Airport, 25–26 Sep. 2025.

[8] Omroep Brabant, "Tien drones boven vliegbasis Volkel, zegt minister Brekelmans," 22 Nov. 2025. [Online]. Available: https://www.omroepbrabant.nl/nieuws/4794336/tien-drones-boven-vliegbasis-volkel-zegt-minister-brekelmans

[9] Tweede Kamer der Staten-Generaal, report of the Defence Committee legislative meeting on the counter-drone supplementary budget (meeting of 26 Nov. 2025), Kamerstuk 36 858, no. 6, adopted 17 Dec. 2025. [Online]. Available: https://zoek.officielebekendmakingen.nl/kst-36858-6.pdf

[10] Al Jazeera, "Air traffic suspended at Netherlands airport after drone sightings," 22 Nov. 2025. [Online]. Available: https://www.aljazeera.com/news/2025/11/22/air-traffic-suspended-at-netherlands-airport-after-drone-sightings

[11] Supreme Headquarters Allied Powers Europe (SHAPE), "NATO marks 60 years of integrated air defence training at Crete firing range," 20 Oct. 2024. [Online]. Available: https://shape.nato.int/news-archive/2024/nato-marks-60-years-of-integrated-air-defence-training-at-crete-firing-range.aspx

[12] Bundeswehr, "Herr der Drohnen – Flugzieldarstellung auf Kreta" (master of drones: aerial target presentation on Crete), 30 Nov. 2020. [Online]. Available: https://www.bundeswehr.de/de/organisation/luftwaffe/aktuelles/herr-der-drohnen-flugzieldarstellung-auf-kreta-4680108

[13] deutschland.de, "German air defence reaches 'milestones'," 15 Oct. 2026. [Online]. Available: https://www.deutschland.de/en/news/german-air-defence-reaches-milestones

[14] Protothema (English edition), "Souda base in Crete sealed after Iran's threats against all U.S. installations," 28 Feb. 2026. [Online]. Available: https://en.protothema.gr/2026/02/28/breaking-souda-base-in-crete-sealed-after-irans-threats-against-all-u-s-installations/

[15] M. Asllani, "Probing the gaps: The drone intelligence threat in Europe," British Institute for Security and International Affairs (BISI), 18 Nov. 2025. [Online]. Available: https://bisi.org.uk/reports/probing-the-gaps-the-drone-intelligence-threat-in-europe

[16] U. Franke, "Buzzkill: How to defend Europe against drones," European Council on Foreign Relations (ECFR), Policy Brief, 17 Aug. 2026. [Online]. Available: https://ecfr.eu/publication/buzzkill-how-to-defend-europe-against-drones/

[17] M. Ezuma, C. K. Anjinappa, M. Funderburk, and I. Guvenc, "Radar cross section based statistical recognition of UAVs at microwave frequencies," arXiv:2102.11954, 2021. [Online]. Available: https://arxiv.org/abs/2102.11954

[18] Y. Cui, J. Nie, W. Yuan, F. Liu, Z. Jia, J. Xu, Z. Feng, and M.-S. Alouini, "Low-altitude wireless networks: The next horizon of wireless infrastructure," arXiv:2605.24368, May 2026, Sec. 4.2.3. [Online]. Available: https://arxiv.org/abs/2605.24368

[19] A. Blazogiannaki, "The evolving asymmetric threat of unmanned aircraft systems," NATO Integrated Air and Missile Defence Centre of Excellence (IAMD COE), Souda Air Base, Chania, Greece, c. 2024. [Online]. Available: https://iamd-coe.org/wp-content/uploads/2024/11/The-Evolving-Asymmetric-Threat-of-Unmanned-Aircraft-Systems-final.pdf

[20] G. C. Birch and B. L. Woo, "Counter unmanned aerial systems testing: Evaluation of VIS, SWIR, MWIR, and LWIR passive imagers," Sandia National Laboratories, Albuquerque, NM, USA, Tech. Rep. SAND2017-0921, 2017. [Online]. Available: https://www.osti.gov/servlets/purl/1342469

[21] F. Svanström *et al.*, "A dataset for multi-sensor drone detection," *Data in Brief*, 2021. [Online]. Available: https://arxiv.org/abs/2111.01888 (data: https://github.com/DroneDetectionThesis/Drone-detection-dataset)

[22] M. Ezuma, M. Funderburk, and I. Guvenc, "Compact-range RCS measurements and modeling of small drones at 15 GHz and 25 GHz," arXiv:1911.05926, 2019. [Online]. Available: https://arxiv.org/abs/1911.05926

[23] J. A. Besada, I. Campaña, D. Carramiñana, L. Bergesio, and G. de Miguel, "Review and simulation of counter-UAS sensors for unmanned traffic management," *Sensors*, vol. 22, no. 1, Art. no. 189, 2022, doi: 10.3390/s22010189.

[24] H. Haverkort, L. Toma, and Y. Zhuang, "Computing visibility on terrains in external memory," in *Proc. 9th Workshop on Algorithm Engineering and Experiments (ALENEX)*, 2007; *ACM J. Exp. Algorithmics*, doi: 10.1145/1412228.1412233.

[25] European Space Agency / Airbus, "Copernicus DEM GLO-30," distributed via OpenTopography. [Online]. Available: https://opentopography.org

[26] Japan Aerospace Exploration Agency (JAXA), "ALOS World 3D-30m (AW3D30)," distributed via OpenTopography. [Online]. Available: https://portal.opentopography.org/dataCatalog

[27] V. N. Grigoriadis, V. D. Andritsanos, and D. A. Natsiopoulos, "Validation of recent DSM/DEM/DBMs in test areas in Greece using spirit leveling, GNSS, gravity and echo sounding measurements," *ISPRS Int. J. Geo-Inf.*, vol. 12, no. 3, Art. no. 99, 2023, doi: 10.3390/ijgi12030099.

[28] OpenStreetMap contributors, "OpenStreetMap," extracts via Geofabrik, ODbL. [Online]. Available: https://download.geofabrik.de

[29] R. Peters, B. Dukai, S. Vitalis, J. van Liempt, and J. Stoter, "Automated 3D reconstruction of LoD2 and LoD1 models for all 10 million buildings of the Netherlands," *Photogramm. Eng. Remote Sens.*, vol. 88, no. 3, pp. 165–170, 2022, doi: 10.14358/PERS.21-00032R2.

[30] "EcoDes-DK15," *Earth Syst. Sci. Data*, 2022. [Online]. Available: https://doaj.org/article/8c32a69188344ea180dc621e6a8551f3

[31] X. X. Zhu *et al.*, "GlobalBuildingAtlas: An open global and complete dataset of building polygons, heights and LoD1 3D models," *Earth Syst. Sci. Data*, vol. 17, pp. 6647–6668, 2025, doi: 10.5194/essd-17-6647-2025.

[32] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.

[33] M. A. Shehadeh and J. Kudela, "Benchmarking global optimization techniques for unmanned aerial vehicle path planning," arXiv:2501.14503, Jan. 2025. [Online]. Available: https://arxiv.org/abs/2501.14503

[34] F. Arapoglou, P. Zacharia, and M. Papoutsidakis, "Intelligent counter-UAV threat detection using hierarchical fuzzy decision-making and sensor fusion," *Sensors*, vol. 25, no. 19, Art. no. 6091, 2025, doi: 10.3390/s25196091.

[35] B. Fraser, A. Perrusquía, D. Panagiotakopoulos, and W. Guo, "A deep mixture of experts network for drone trajectory intent classification and prediction using non-cooperative radar data," in *Proc. IEEE Symp. Ser. Comput. Intell. (SSCI)*, 2023, doi: 10.1109/SSCI52147.2023.10371877.

[36] Dalian University of Technology, "DUT Anti-UAV dataset," GitHub repository, MIT License. [Online]. Available: https://github.com/wangdongdut/DUT-Anti-UAV

[37] "Anti-UAV benchmark (Anti-UAV300/410/600)," GitHub repository. [Online]. Available: https://github.com/ZhaoJ9014/Anti-UAV

[38] "UAVSwarm dataset," GitHub repository, CC BY 4.0. [Online]. Available: https://github.com/UAVSwarm/UAVSwarm-dataset

[39] NTU ARIS Lab, "MMAUD: Multi-modal anti-UAV dataset," GitHub repository, CC BY-NC-SA 4.0. [Online]. Available: https://github.com/ntu-aris/MMAUD

[40] WOSDETC, "Drone-vs-Bird detection challenge," GitHub repository. [Online]. Available: https://github.com/wosdetc/challenge

[41] "TIB-Net: Drone detection network with tiny iterative backbone," GitHub repository. [Online]. Available: https://github.com/kyn0v/TIB-Net

[42] "DroneRF dataset: RF signals of drones (Parrot Bebop, Parrot AR, DJI Phantom 3)," Mendeley Data. [Online]. Available: https://data.mendeley.com

[43] "DroneDetect dataset: RF recordings of UAS collected with BladeRF SDR," IEEE DataPort. [Online]. Available: https://ieee-dataport.org

[44] Headquarters, Department of the Army, "Counter-unmanned aircraft system techniques," ATP 3-01.81, Washington, DC, USA, Dec. 2023. [Online]. Available: https://armypubs.army.mil

[45] U.S. Department of Defense, "DoD strategy for countering unmanned systems," fact sheet, 2024. [Online]. Available: https://www.defense.gov

[46] Congressional Research Service, Report R48477 on counter-UAS programmes. [Online]. Available: https://www.everycrsreport.com

[47] RAND Corporation, research reports on counter-UAS defence of military installations, 2023–2026. [Online]. Available: https://www.rand.org

[48] Center for a New American Security (CNAS), "Countering the swarm." [Online]. Available: https://www.cnas.org

[49] Royal United Services Institute (RUSI), publications on drone warfare and counter-UAS tactics in Ukraine. [Online]. Available: https://www.rusi.org

[50] Institute for the Study of War (ISW), "Russian offensive campaign assessment," daily reports. [Online]. Available: https://www.understandingwar.org

[51] NATO, "Drone Edge" and "Project Flytrap" news releases, NATO Newsroom. [Online]. Available: https://www.nato.int

[52] U.S. Department of Defense, "Joint military symbology," MIL-STD-2525 (C/D/E); NATO, "NATO joint military symbology," STANAG APP-6 (B/D/E).

[53] spatialillusions, "milsymbol: Military symbols in JavaScript," GitHub repository, MIT License. [Online]. Available: https://github.com/spatialillusions/milsymbol

[54] Janes, "IDEF 2019: ASELSAN's İHTAR counter-UAV system breaks cover," 2019. [Online]. Available: https://janes.com/osint-insights/defence-news/idef-2019-aselsans-ihtar-counter-uav-system-breaks-cover

[55] CNN Türk, "Drone avcısı sistemleri SAHA Expo'da tanıtıldı" (drone hunter systems presented at SAHA Expo). [Online]. Available: https://www.cnnturk.com/yerel-haberler/ankara/drone-avcisi-sistemleri-saha-expoda-tanitildi-2171622

[56] Anadolu Agency, "Turkish defense company ASELSAN debuts new counter-drone electronic warfare systems at SAHA 2026," 2026. [Online]. Available: https://www.aa.com.tr/en/science-technology/turkish-defense-company-aselsan-debuts-new-counter-drone-electronic-warfare-systems-at-saha-2026/3929185

[57] EDR Magazine, "SAHA Expo 2026: ASELSAN add new elements to its Steel Dome, widening its C-UAS capabilities," 2026. [Online]. Available: https://www.edrmagazine.eu/saha-expo-2026-aselsan-add-new-elements-to-its-steel-dome-widening-its-c-uas-capabilities

[58] Armada International, "Meteksan completed delivery of drone detection radars," Jul. 2020. [Online]. Available: https://www.armadainternational.com/2020/07/meteksan-completed-delivery-drone-detection-radars/

[59] Anadolu Ajansı, "Drone tehdidini KAPAN durduracak" (KAPAN will stop the drone threat). [Online]. Available: https://www.aa.com.tr/tr/bilim-teknoloji/drone-tehdidini-kapan-durduracak/1193364

[60] haber.aero, "Drone tehdidini AVCI durduracak" (AVCI will stop the drone threat). [Online]. Available: https://haber.aero/aero-gundem/drone-tehdidini-avci-durduracak

[61] Defence Turkey, "AVCI anti-drone system." [Online]. Available: https://www.defenceturkey.com/tr/icerik/avci-anti-drone-system-4717

[62] Milliyet, "İHA tehditlerine karşı maliyeti etkin çözüm: TUNGA-X ilk kez SAHA Expo 2026'da görücüye çıktı" (cost-effective solution against UAV threats: TUNGA-X shown for the first time at SAHA Expo 2026), 2026. [Online]. Available: https://www.milliyet.com.tr/milliyet-tv/iha-tehditlerine-karsi-maliyeti-etkin-cozum-tunga-x-ilk-kez-saha-expo-2026da-gorucuye-cikti-video-7583403

[63] Milliyet, "Roketsan'dan kamikaze dron tehdidine karşı lazer silahı" (Roketsan laser weapon against the kamikaze drone threat). [Online]. Available: https://www.milliyet.com.tr/ekonomi/roketsandan-kamikaze-dron-tehdidine-karsi-lazer-silahi-7194840

[64] haber.aero, "Görünmeyen tehditler HAVELSAN'ın teknolojisi ile tespit edilecek" (invisible threats to be detected with HAVELSAN technology). [Online]. Available: https://haber.aero/savunma/gorunmeyen-tehditler-havelsanin-teknolojisi-ile-tespit-edilecek

[65] P. E. Hart, N. J. Nilsson, and B. Raphael, "A formal basis for the heuristic determination of minimum cost paths," *IEEE Trans. Syst. Sci. Cybern.*, vol. 4, no. 2, pp. 100–107, 1968.

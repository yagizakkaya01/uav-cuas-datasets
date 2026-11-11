# Literature Review

**Owner:** Yağız Akkaya · **Weight:** 30%

*Source note: every source in this section is already catalogued and checked in the project repository (`layers/`, `docs/pilot-region/`, `docs/computational-model/`). No external source outside the repository is used.*

## 3.1 Theoretical background

### 3.1.1 The problem: small drones at airports and military bases

Small unmanned aircraft systems (UAS) have repeatedly closed airports and alarmed military installations. A survey of airport incidents between 2016 and 2019 lists ten serious cases, including the Gatwick closure of December 2018 and the Frankfurt disruption of 2019 [1]. Since 2024 the problem has moved from isolated nuisance flights to a sustained pattern: an International Institute for Strategic Studies (IISS) study counts 144 incidents in 13 European countries between August 2024 and February 2026 [2]. Table 3.1 lists the documented cases that the project uses as reference examples. They are presented as general evidence of the problem, not as a choice of pilot region.

**Table 3.1.** Documented drone incidents used as reference cases.

| Date | Location | What happened | Operational impact | Sources |
|---|---|---|---|---|
| Dec 2018 | Gatwick Airport, UK | Drone sightings closed the airport; the incident was later reviewed by the Sussex Police and Crime Commissioner | Closure of about 30–33 h; the case is used in the introductions of later cost and risk studies | [3], [1], [4], [5] |
| 2019 | Frankfurt Airport, Germany | Drone sightings near the airport | Listed among serious airport incidents; used as the case airport for a shutdown cost model | [1], [4] |
| 24–25 Sep 2025 | Aalborg Airport, Denmark (joint civil and military) | Lit drones observed at night over the airport | Closure of about 3 h | [6] |
| 21 Nov 2025 | Volkel Air Base, Netherlands | Guards saw first 5, then 10 drones in darkness; the military fired from the ground; the drones flew off and were not found | Security response at a NATO air base | [7], [8] |
| 22 Nov 2025 | Eindhoven Airport, Netherlands (joint civil and military) | Multiple drones sighted in the evening; Ministry of Defence counter-drone systems on standby | All civil and military flights halted for about two hours and diverted to other airports; no drone recovered | [9], [8] |
| Aug 2024 – Feb 2026 | 13 European countries | Systematic analysis of 144 incidents; the Volkel and Eindhoven drones were assessed as most likely launched from ships off the Dutch coast | Cumulative disruption of civil and military sites | [2], [10] |

The incidents share one pattern. A drone is reported, the operator cannot confirm what it is or where it is going, and the site closes as a precaution. The cost of this uncertainty is large. A cost model built on the Frankfurt case found that a counter-drone investment is economically justified in certain closure scenarios, and that airlines carry most of the losses [4]. The response time is also short: with drone speeds of 10–20 m/s, a 6–10 km protective zone gives only about 5–10 minutes of warning [1]. At the same time, mitigation is constrained. Civil radio-frequency (RF) jamming is illegal in many countries and can interfere with landing systems, and no international standard exists for counter-UAS (C-UAS) use at airports [1]; jamming near an airport also affects the airport's own systems [11]. The central need is therefore fast and confident detection, identification and decision support, rather than the ability to destroy the drone.

### 3.1.2 Detection sensors and why one sensor is not enough

Detecting a small drone is physically difficult, and each sensor modality fails in a different way. Table 3.2 summarises the strengths and weaknesses reported in the sources held in the repository.

**Table 3.2.** Small-drone detection sensor modalities.

| Sensor | Strengths | Weaknesses | Sources |
|---|---|---|---|
| Radar | Proposed as the primary detection layer at airports | Small drones have a very low radar cross section (RCS); birds cause false alarms; small, slow, low-flying targets are hard to track | [1], [11], [12], [13] |
| RF detection | Detects the drone's radio control or video link; used with cameras for identification | Misses autonomous drones that do not transmit; depends on line of sight | [1] |
| Visible and infrared cameras | Identification layer; images allow human confirmation | Need line of sight; drones are confused with birds; range is limited by the pixels on target: about 7 pixels are needed for detection and 15 for assessment | [1], [11], [14] |
| Acoustic | Does not depend on the drone transmitting radio signals | Short range, typically under 300 m; not reliable in airport noise | [1] |

Radar is often assumed to solve detection on its own, but measured RCS values show why it does not. Compact-range measurements of commercial drones such as the DJI Matrice, Mavic and Phantom at 15 GHz and 25 GHz gave RCS values mostly between −12 and −17 dBsm [12], [15]. A recent survey reports UK Civil Aviation Authority tests in which DJI Phantom-class quadcopters, with an RCS as low as −23 dBsm, could not be reliably tracked beyond 500 m by standard airport-surveillance radar [13]. The airport survey therefore concludes that "adopting a single sensor technology for UAV detection in airports cannot provide the desired situational awareness" [1], and the European Council on Foreign Relations (ECFR) recommends sensor fusion for the same reasons [11]. Sensor simulation work models these weaknesses explicitly through the radar equation, constant false-alarm-rate detection and false-alarm rates, and evaluates sensor mixes in an agent-based simulator [16]. These findings justify the project's choice of two low-cost sensors with different failure modes: a camera, which cannot see behind obstacles, and an RF receiver, which cannot detect a silent autonomous drone.

### 3.1.3 Geospatial reasoning: line of sight, terrain and air traffic

Every sensor in Table 3.2 except acoustics needs line of sight, so a threat map must know where the sensors can and cannot see. Line of sight over a terrain model can be computed with an input/output-efficient radial sweep in O(n log n) time [17]. This requires surface heights. Global digital surface models such as Copernicus GLO-30 and ALOS AW3D30 provide terrain at 30 m resolution [18], [19], and OpenStreetMap adds roads, buildings and facility boundaries [20]. Where national data exist, much finer building models are available. The Dutch 3DBAG dataset reconstructs all 10 million buildings in the Netherlands from LiDAR with an error below 31 cm (RMSE) for 95% of buildings [21]. Finally, the decision engine must know the normal air traffic around a site in order to judge a track near a runway. The OpenSky Network provides an ADS-B research database for this baseline, but it only sees aircraft that broadcast ADS-B, its low-altitude coverage has gaps, and drones are invisible to it [22]. Drone detection must therefore come from the project's own sensors.

## 3.2 Previous work

### 3.2.1 Academic studies

The academic work relevant to the project falls into five groups: sensing and its simulation, tracking and threat assessment, risk assessment, path planning, and geospatial data. Table 3.3 summarises the studies catalogued in the repository and states how each one is used in the project.

**Table 3.3.** Academic studies relevant to the project.

| Ref. | Year | Topic | Method | Key finding | Relevance to the project |
|---|---|---|---|---|---|
| [1] | 2020 | Sensing | Survey of airport incidents and C-UAS sensors; three attack scenarios with protection plans | No single sensor gives adequate situational awareness; mitigation at airports is legally constrained | Basis for sensor fusion and for recommending rather than executing countermeasures |
| [16] | 2022 | Sensing (simulation) | Review of C-UAS sensors with radar-equation, CFAR and false-alarm models in an agent-based simulator | Sensor performance can be compared in simulation before field tests | Precedent for the project's Monte Carlo evaluation of the detection chain |
| [14] | 2017 | Sensing (imaging) | Sandia field tests of visible and infrared imagers against small UAS | About 7 pixels on target for detection and 15 for assessment | Used to compute the detection range of the project's camera |
| [12], [15] | 2019–2021 | Sensing (radar) | Compact-range RCS measurements of commercial drones at 15 and 25 GHz | RCS mostly −12 to −17 dBsm | Quantitative argument against radar-only detection |
| [23] | 1988 | Tracking | Interacting Multiple Model (IMM) filter for systems with switching dynamics | Standard method for tracking targets that change manoeuvre mode | Optional extension of the project's constant-velocity Kalman tracker |
| [24] | 2023 | Threat assessment | Deep mixture-of-experts network on non-cooperative radar tracks | About 98% accuracy in drone intent classification; 15–30 s position bounds | Learned alternative to the project's trajectory prediction; noted as future work |
| [25] | 2025 | Threat assessment and fusion | Three-stage hierarchical fuzzy decision-making for C-UAS sensor selection (MATLAB) | Fuzzy logic can combine sensor evidence into a threat decision; validated only in simulation | Main alternative to the project's transparent weighted threat score |
| [5] | 2022 | Risk assessment | Airport vulnerability index combined with event trees; case study at Milan Malpensa | Quantitative, systematic assessment of drone-intrusion impact on an airport | Closest precedent for the risk engine; airport-level, not per grid cell |
| [4] | 2020 | Risk assessment (economic) | Simulation of a drone-related shutdown at Frankfurt | Counter-drone investment is justified in certain closure scenarios; airlines bear most losses | Supports the motivation of the project |
| [26] | 2024 | Risk assessment (regulatory) | JARUS Specific Operations Risk Assessment, edition 2.5 | Standardised ground and air risk classes for drone operations | Consistency check for the project's risk levels |
| [27] | 1968 | Path planning | A* heuristic search for minimum-cost paths | Optimal paths with an admissible heuristic | Core algorithm of the safe-route module |
| [28] | 2005 | Path planning | D* Lite incremental replanning in unknown terrain | Fast replanning when costs change | Replanning when the risk map changes |
| [29] | 2025 | Path planning | Benchmark of 12 global optimisers on UAV path-planning instances | Threats modelled as cylinders with distance-based penalties in the cost function | Template for the threat-cost term of the grid cost surface |
| [21] | 2022 | Geospatial data | Automated LoD1/LoD2 reconstruction of all Dutch buildings from BAG and AHN LiDAR | RMSE below 31 cm for 95% of buildings | Building heights for line of sight where 3DBAG is available |
| [22] | 2014 | Air-traffic data | Volunteer ADS-B sensor network and research database | Only ADS-B aircraft are visible; coverage gaps at low altitude | Normal-traffic baseline; shows why drones need dedicated sensors |
| [17] | 2007 | Line of sight | I/O-efficient visibility computation on terrains | Radial sweep in O(n log n) | Line-of-sight algorithm for sensor coverage on the grid |

Learning-based detection depends on open datasets. Table 3.4 lists the drone detection datasets that the project has catalogued and checked for access. The visible-light and infrared datasets support the YOLO detector, and the RF datasets support the design of the RF detection chain.

**Table 3.4.** Open drone detection datasets catalogued by the project.

| Dataset | Modality | Content | Access | Source |
|---|---|---|---|---|
| DUT Anti-UAV | Visible | 10,000 annotated images and 20 tracking videos | Open (MIT) | [30] |
| Anti-UAV (300/410/600) | Visible and infrared | Tracking benchmark series | Gated platform access | [31] |
| Halmstad multi-sensor | Infrared, visible, audio | 650 videos (365 IR, 285 visible), 90 audio clips, more than 203,000 annotated frames | Open | [32] |
| UAVSwarm | Visible | 72 sequences with multi-object tracking labels | Open (CC BY 4.0) | [33] |
| MMAUD | Stereo RGB, LiDAR, mmWave radar, microphone array | Multi-modal recordings with 3D trajectory labels | Open (CC BY-NC-SA 4.0) | [34] |
| Drone-vs-Bird | Visible | Challenge data with drones and birds | Request only, signed agreement | [35] |
| TIB-Net | Visible | 2,850 images for tiny-target detection | Open | [36] |
| DroneRF | RF | Signal segments of 3 drone models, more than 40 GB | Open | [37] |
| DroneDetect | RF | Software-defined-radio recordings of 7 UAS models | Open, free login | [38] |

### 3.2.2 Doctrine, policy and standards

A decision support system must base its recommendations on accepted procedures, not on the reasoning of a language model alone. The project therefore draws on public doctrine, policy analysis and symbology standards, summarised in Table 3.5. These documents form the corpus of the retrieval-augmented knowledge base, so that every recommendation can cite its source.

**Table 3.5.** Doctrine, policy and standards used by the project.

| Source | Type | Content used by the project |
|---|---|---|
| ATP 3-01.81 [39] | U.S. Army C-UAS doctrine | UAS group classification, layered defence, and the detect–identify–defeat cycle |
| DoD Strategy for Countering Unmanned Systems [40] | U.S. strategy | Top-level principles for C-UAS operations |
| CRS Report R48477 [41] | Congressional research report | Summary of C-UAS programmes and terminology |
| "Countering the Swarm" [42] | Think-tank report | Tactics of drone swarms; basis for the swarm clustering module |
| IISS, *Russia's UAV Campaign Over Europe* [2] | Think-tank study | Incident pattern in Europe, 2024–2026 |
| ECFR, *Buzzkill* [11] | Policy brief | Sensor limits near airports and the case for sensor fusion |
| BISI, *Probing the Gaps* [10] | Think-tank report | European drone intelligence threat context |
| MIL-STD-2525 and STANAG APP-6 via milsymbol [43], [44] | Symbology standard and open library | Standard friend, hostile and unknown symbols on the C2 map |

### 3.2.3 Comparison with the project

Table 3.6 compares representative studies from Tables 3.3 and 3.5 with the project on the same criteria. A dash means that the feature is not part of that work.

**Table 3.6.** Comparison of representative previous work with the project.

| Work | Multi-sensor fusion | Grid risk map with line of sight | Safe route | Recommendation with cited doctrine | Standard symbology | Validated on real hardware |
|---|---|---|---|---|---|---|
| Lykou et al. [1] | Recommended (survey) | – | – | Analytical protection plans | – | No |
| Besada et al. [16] | Simulated sensor mix | – | – | – | – | Simulation only |
| Arapoglou et al. [25] | Fuzzy fusion | – | – | Fuzzy threat decision, no citations | – | Simulation only |
| Fraser et al. [24] | Radar only | – | – | Intent class, no recommendation | – | Recorded radar data |
| Pascarella et al. [5] | – | Airport-level index, no grid | – | – | – | Case study |
| Shehadeh and Kudela [29] | – | Cylindrical threat cost | Yes | – | – | Benchmark only |
| ATP 3-01.81 [39] | Doctrinal guidance | – | – | Doctrine itself, not a system | – | – |
| **This project** | Camera + RF, decision level | Yes, with terrain and building heights | A* / D* Lite | Rule-based recommendation explained with retrieved doctrine citations | MIL-STD-2525 | Campus demo with camera and ESP32 |

## 3.3 Summary and research gap

The literature agrees on the nature of the problem. Small drones repeatedly close airports and approach military bases [1], [2]; the closures are driven by uncertainty rather than by collisions; and the economic cost is large enough to justify counter-drone investment [4]. It also agrees that no single sensor is sufficient [1], [11], because small drones have a very low RCS [12], [13], cameras need line of sight [14], and RF sensing misses autonomous drones [1]. Separate research streams provide the building blocks the project needs: sensor simulation [16], threat assessment by fuzzy logic or learning [25], [24], airport risk frameworks [5], threat-aware path planning [27], [29], accurate building and terrain data [21], [18], and open detection datasets [30], [32], [37].

The gap lies in their combination. In the sources reviewed, these elements appear as separate studies: risk is assessed at the level of a whole airport rather than per map cell [5], threat decisions are made without reference to doctrine [25], and path-planning studies model threats as fixed cylinders without live sensor input [29]. None of the works reviewed links low-cost multi-sensor detection to a line-of-sight-aware grid risk map, safe routing and operator recommendations that cite public doctrine, displayed with standard military symbology. The project addresses this gap with a low-cost, detect-and-recommend system built on open data and verified sources. Its claims are bounded accordingly: the demo is small in scale and uses a single camera and a mock drone, so it demonstrates the integrated decision chain rather than operational detection performance.

## References

[1] G. Lykou, D. Moustakas, and D. Gritzalis, "Defending airports from UAS: A survey on cyber-attacks and counter-drone sensing technologies," *Sensors*, vol. 20, no. 12, Art. no. 3537, 2020, doi: 10.3390/s20123537.

[2] C. Edwards, R. Fox O'Loughlin, and L. Bearn, "Russia's UAV campaign over Europe," International Institute for Strategic Studies (IISS), London, U.K., Jul. 2026. [Online]. Available: https://www.astrid-online.it/static/upload/russ/russia-uav-campaign-over-europe.pdf

[3] Office of the Sussex Police and Crime Commissioner, official review minutes on the December 2018 Gatwick drone incident, 18 Oct. 2019.

[4] P. Wendt, A. Voltes-Dorta, and P. Suau-Sanchez, "Estimating the costs for the airport operator and airlines of a drone-related shutdown: An application to Frankfurt international airport," *J. Transp. Secur.*, vol. 13, no. 1, pp. 93–116, 2020, doi: 10.1007/s12198-020-00212-4.

[5] D. Pascarella, G. Gigante, A. Vozella, P. Bieber, T. Dubot, E. Martinavarro, G. Barraco, and G. Li Calzi, "A methodological framework for the risk assessment of drone intrusions in airports," *Aerospace*, vol. 9, no. 12, Art. no. 747, 2022, doi: 10.3390/aerospace9120747.

[6] Danish National Police (Rigspolitiet), press releases on drone activity at Aalborg Airport, 25–26 Sep. 2025.

[7] Omroep Brabant, "Tien drones boven vliegbasis Volkel, zegt minister Brekelmans," 22 Nov. 2025. [Online]. Available: https://www.omroepbrabant.nl/nieuws/4794336/tien-drones-boven-vliegbasis-volkel-zegt-minister-brekelmans

[8] Tweede Kamer der Staten-Generaal, report of the Defence Committee legislative meeting on the counter-drone supplementary budget (meeting of 26 Nov. 2025), Kamerstuk 36 858, no. 6, adopted 17 Dec. 2025. [Online]. Available: https://zoek.officielebekendmakingen.nl/kst-36858-6.pdf

[9] Al Jazeera, "Air traffic suspended at Netherlands airport after drone sightings," 22 Nov. 2025. [Online]. Available: https://www.aljazeera.com/news/2025/11/22/air-traffic-suspended-at-netherlands-airport-after-drone-sightings

[10] M. Asllani, "Probing the gaps: The drone intelligence threat in Europe," British Institute for Security and International Affairs (BISI), 18 Nov. 2025. [Online]. Available: https://bisi.org.uk/reports/probing-the-gaps-the-drone-intelligence-threat-in-europe

[11] U. Franke, "Buzzkill: How to defend Europe against drones," European Council on Foreign Relations (ECFR), Policy Brief, 17 Aug. 2026. [Online]. Available: https://ecfr.eu/publication/buzzkill-how-to-defend-europe-against-drones/

[12] M. Ezuma, C. K. Anjinappa, M. Funderburk, and I. Guvenc, "Radar cross section based statistical recognition of UAVs at microwave frequencies," arXiv:2102.11954, 2021. [Online]. Available: https://arxiv.org/abs/2102.11954

[13] Y. Cui, J. Nie, W. Yuan, F. Liu, Z. Jia, J. Xu, Z. Feng, and M.-S. Alouini, "Low-altitude wireless networks: The next horizon of wireless infrastructure," arXiv:2605.24368, May 2026, Sec. 4.2.3. [Online]. Available: https://arxiv.org/abs/2605.24368

[14] G. C. Birch and B. L. Woo, "Counter unmanned aerial systems testing: Evaluation of VIS, SWIR, MWIR, and LWIR passive imagers," Sandia National Laboratories, Albuquerque, NM, USA, Tech. Rep. SAND2017-0921, 2017. [Online]. Available: https://www.osti.gov/servlets/purl/1342469

[15] M. Ezuma, M. Funderburk, and I. Guvenc, "Compact-range RCS measurements and modeling of small drones at 15 GHz and 25 GHz," arXiv:1911.05926, 2019. [Online]. Available: https://arxiv.org/abs/1911.05926

[16] J. A. Besada, I. Campaña, D. Carramiñana, L. Bergesio, and G. de Miguel, "Review and simulation of counter-UAS sensors for unmanned traffic management," *Sensors*, vol. 22, no. 1, Art. no. 189, 2022, doi: 10.3390/s22010189.

[17] H. Haverkort, L. Toma, and Y. Zhuang, "Computing visibility on terrains in external memory," in *Proc. 9th Workshop on Algorithm Engineering and Experiments (ALENEX)*, 2007; *ACM J. Exp. Algorithmics*, doi: 10.1145/1412228.1412233.

[18] European Space Agency / Airbus, "Copernicus DEM GLO-30," distributed via OpenTopography. [Online]. Available: https://opentopography.org

[19] Japan Aerospace Exploration Agency (JAXA), "ALOS World 3D-30m (AW3D30)," distributed via OpenTopography. [Online]. Available: https://portal.opentopography.org/dataCatalog

[20] OpenStreetMap contributors, "OpenStreetMap," extracts via Geofabrik, ODbL. [Online]. Available: https://download.geofabrik.de

[21] R. Peters, B. Dukai, S. Vitalis, J. van Liempt, and J. Stoter, "Automated 3D reconstruction of LoD2 and LoD1 models for all 10 million buildings of the Netherlands," *Photogramm. Eng. Remote Sens.*, vol. 88, no. 3, pp. 165–170, 2022, doi: 10.14358/PERS.21-00032R2.

[22] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.

[23] H. A. P. Blom and Y. Bar-Shalom, "The interacting multiple model algorithm for systems with Markovian switching coefficients," *IEEE Trans. Autom. Control*, vol. 33, no. 8, pp. 780–783, 1988, doi: 10.1109/9.1299.

[24] B. Fraser, A. Perrusquía, D. Panagiotakopoulos, and W. Guo, "A deep mixture of experts network for drone trajectory intent classification and prediction using non-cooperative radar data," in *Proc. IEEE Symp. Ser. Comput. Intell. (SSCI)*, 2023, doi: 10.1109/SSCI52147.2023.10371877.

[25] F. Arapoglou, P. Zacharia, and M. Papoutsidakis, "Intelligent counter-UAV threat detection using hierarchical fuzzy decision-making and sensor fusion," *Sensors*, vol. 25, no. 19, Art. no. 6091, 2025, doi: 10.3390/s25196091.

[26] Joint Authorities for Rulemaking on Unmanned Systems (JARUS), "Specific Operations Risk Assessment (SORA) main body," JAR-DEL-SRM-SORA-MB-2.5, Ed. 2.5, 13 May 2024.

[27] P. E. Hart, N. J. Nilsson, and B. Raphael, "A formal basis for the heuristic determination of minimum cost paths," *IEEE Trans. Syst. Sci. Cybern.*, vol. 4, no. 2, pp. 100–107, 1968.

[28] S. Koenig and M. Likhachev, "Fast replanning for navigation in unknown terrain," *IEEE Trans. Robot.*, vol. 21, no. 3, pp. 354–363, 2005.

[29] M. A. Shehadeh and J. Kudela, "Benchmarking global optimization techniques for unmanned aerial vehicle path planning," arXiv:2501.14503, Jan. 2025. [Online]. Available: https://arxiv.org/abs/2501.14503

[30] Dalian University of Technology, "DUT Anti-UAV dataset," GitHub repository, MIT License. [Online]. Available: https://github.com/wangdongdut/DUT-Anti-UAV

[31] "Anti-UAV benchmark (Anti-UAV300/410/600)," GitHub repository. [Online]. Available: https://github.com/ZhaoJ9014/Anti-UAV

[32] F. Svanström *et al.*, "Drone detection dataset (Halmstad University multi-sensor dataset)," *Data in Brief*, 2021; data: https://github.com/DroneDetectionThesis/Drone-detection-dataset

[33] "UAVSwarm dataset," GitHub repository, CC BY 4.0. [Online]. Available: https://github.com/UAVSwarm/UAVSwarm-dataset

[34] NTU ARIS Lab, "MMAUD: Multi-modal anti-UAV dataset," GitHub repository, CC BY-NC-SA 4.0. [Online]. Available: https://github.com/ntu-aris/MMAUD

[35] WOSDETC, "Drone-vs-Bird detection challenge," GitHub repository. [Online]. Available: https://github.com/wosdetc/challenge

[36] "TIB-Net: Drone detection network with tiny iterative backbone," GitHub repository. [Online]. Available: https://github.com/kyn0v/TIB-Net

[37] "DroneRF dataset: RF signals of drones (Parrot Bebop, Parrot AR, DJI Phantom 3)," Mendeley Data. [Online]. Available: https://data.mendeley.com

[38] "DroneDetect dataset: RF recordings of UAS collected with BladeRF SDR," IEEE DataPort. [Online]. Available: https://ieee-dataport.org

[39] Headquarters, Department of the Army, "Counter-unmanned aircraft system techniques," ATP 3-01.81, Washington, DC, USA, Dec. 2023. [Online]. Available: https://armypubs.army.mil

[40] U.S. Department of Defense, "DoD strategy for countering unmanned systems," fact sheet, 2024. [Online]. Available: https://www.defense.gov

[41] Congressional Research Service, Report R48477 on counter-UAS programmes. [Online]. Available: https://www.everycrsreport.com

[42] Center for a New American Security (CNAS), "Countering the swarm." [Online]. Available: https://www.cnas.org

[43] U.S. Department of Defense, "Joint military symbology," MIL-STD-2525 (C/D/E); NATO, "NATO joint military symbology," STANAG APP-6 (B/D/E).

[44] spatialillusions, "milsymbol: Military symbols in JavaScript," GitHub repository, MIT License. [Online]. Available: https://github.com/spatialillusions/milsymbol

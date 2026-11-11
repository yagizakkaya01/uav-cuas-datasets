# Literature Review

**Owner:** Yağız Akkaya · **Weight:** 30%

## 3.1 Theoretical background

### 3.1.1 The problem: small drones at airports and military bases

Small unmanned aircraft systems (UAS) have repeatedly closed airports and alarmed military installations. A survey of airport incidents between 2016 and 2019 lists ten serious cases, including the Gatwick closure of December 2018 and the Frankfurt disruption of 2019 [1]. Since 2024 the problem has moved from isolated nuisance flights to a sustained pattern: an International Institute for Strategic Studies (IISS) study counts 144 incidents in 13 European countries between August 2024 and February 2026 [2]. Table 3.1 lists the documented cases collected in the team's surveys of the four candidate pilot regions: Eindhoven, Gatwick, Aalborg and Akrotiri (Crete). They are presented as general evidence of the problem, not as a choice of pilot region.

**Table 3.1.** Documented drone incidents used as reference cases.

| Date | Location | What happened | Operational impact | Sources |
|---|---|---|---|---|
| Dec 2018 | Gatwick Airport, UK | Drone sightings closed the airport; the incident was later reviewed by the Sussex Police and Crime Commissioner | Closure of about 30–33 h | [3], [4], [1], [5] |
| 24–25 Sep 2025 | Aalborg Airport, Denmark (joint civil and military) | Several drones with lights on were seen at night from about 21:44 to 00:54 | Closure of about 3 h; part of the September 2025 wave over Danish airports | [6], [7] |
| 21 Nov 2025 | Volkel Air Base, Netherlands | Guards saw first 5, then 10 drones in darkness; the military fired from the ground; the drones flew off and were not found | Security response at a NATO air base | [8], [9] |
| 22 Nov 2025 | Eindhoven Airport, Netherlands (joint civil and military) | Multiple drones sighted in the evening; Ministry of Defence counter-drone systems on standby | All civil and military flights halted for about two hours and diverted to other airports; no drone recovered | [10], [9] |
| 2012 – Oct 2026 | NATO Missile Firing Installation (NAMFI) and Souda, Crete, Greece | NATO's live-fire range in Europe, where Patriot and IRIS-T SLM units train against target drones; in February 2026 the Souda base was sealed after threats against US installations | No hostile drone incursion reported; the site is used for counter-drone training | [11], [12], [13], [14] |
| Aug 2024 – Feb 2026 | 13 European countries | Systematic analysis of 144 incidents; the Volkel and Eindhoven drones were assessed as most likely launched from ships off the Dutch coast | Cumulative disruption of civil and military sites | [2], [15] |

The incidents share one pattern. A drone is reported, nobody can confirm what it is or where it is going, and the site closes as a precaution. This is expensive: a cost study based on Frankfurt Airport found that investing in counter-drone systems can pay off, and that airlines carry most of the losses [4]. There is also little time to react. At drone speeds of 10–20 m/s, a 6–10 km protection zone gives only about 5–10 minutes of warning [1]. Stopping the drone is not simple either: jamming its radio link is illegal for civil use in many countries and can disturb the airport's own landing systems [1], [16]. The main need is therefore to detect and identify the drone quickly and to help the operator decide what to do, not to destroy it.

### 3.1.2 Detection sensors and why one sensor is not enough

Small drones are hard to detect, and each type of sensor has a different weak point. Table 3.2 summarises the strengths and weaknesses reported in the sources the team has collected.

**Table 3.2.** Small-drone detection sensor modalities.

| Sensor | Strengths | Weaknesses | Sources |
|---|---|---|---|
| Radar | Proposed as the primary detection layer at airports | Small drones reflect very little radar energy, similar to birds; birds cause false alarms; small, slow, low-flying targets are hard to track | [1], [16], [17], [18], [19] |
| RF detection | Detects the drone's radio control or video link; used with cameras for identification | Misses autonomous drones that do not transmit; depends on line of sight | [1], [19] |
| Visible and infrared cameras | Identification layer; images allow human confirmation | Need line of sight; drones are confused with birds; range is limited by how many pixels the drone covers in the image: below about 5 pixels it can only be detected, and more than 15 are needed to identify it [20] | [1], [16], [20] |
| Acoustic | Does not depend on the drone transmitting radio signals | Short range, typically under 300 m; not reliable in airport noise | [1] |

Radar alone is not enough, because a small drone reflects very little radar energy. This is measured as the radar cross section (RCS). Laboratory measurements of commercial drones such as the DJI Matrice, Mavic and Phantom gave RCS values mostly between −12 and −17 dBsm [17], [21], which is far smaller than a conventional aircraft and close to a bird. A recent survey reports tests by the UK Civil Aviation Authority in which standard airport radar could not reliably track small DJI Phantom-class drones beyond 500 m [18]. For this reason the main survey on airport protection concludes that "adopting a single sensor technology for UAV detection in airports cannot provide the desired situational awareness" [1], and a policy study of European drone defence also recommends combining sensors [16]. This supports the project's choice of two low-cost sensors with different weak points: a camera, which cannot see behind obstacles, and an RF receiver, which cannot hear a drone that does not transmit.

### 3.1.3 Map data: line of sight, terrain and air traffic

Cameras, radar and RF receivers all need a clear line of sight to the drone, so a threat map must know where the sensors can and cannot see. This requires height data for the terrain and the buildings. Global elevation models such as Copernicus GLO-30 and ALOS AW3D30 give terrain heights on a 30 m grid [22], [23], and OpenStreetMap adds roads, buildings and site boundaries [24], although building heights are often missing. Some countries publish much more detailed data. The Dutch 3DBAG dataset gives the height of every building in the Netherlands, with an error below 31 cm for 95% of buildings [25]. Table 3.3 summarises what the team found for each candidate pilot region.

**Table 3.3.** Geospatial data found in the team's candidate pilot-region surveys.

| Region | Terrain and surface | Buildings | Drone restriction zones | Air traffic |
|---|---|---|---|---|
| Eindhoven, Netherlands | AHN national LiDAR | 3DBAG heights for every building [25] | 3 km runway buffer | OpenSky; open ADS-B archive |
| Gatwick, UK | Environment Agency 1 m terrain and surface models | Surface heights from the 1 m surface model | NATS UAS restriction dataset | OpenSky |
| Aalborg, Denmark | DHM national model, 0.4 m grid | OSM footprints | Official map | OpenSky |
| Akrotiri, Crete | Copernicus GLO-30, 30 m [22] | OSM footprints | Official map (HCAA) | Airport statistics |
The system also needs to know the normal air traffic around a site in order to judge how serious a drone near a runway is. The OpenSky Network provides open aircraft position data for this purpose, but it only shows aircraft that broadcast their position, and drones do not appear in it [26]. Drone detection must therefore come from the project's own sensors.

## 3.2 Previous work

### 3.2.1 Academic studies

Table 3.4 lists the key studies the team has reviewed and states how each one is used in the project. The doctrine documents behind the knowledge base are covered separately in Section 3.2.2.

**Table 3.4.** Key studies relevant to the project.

| Ref. | Year | Topic | What the study did | Main finding | Use in the project |
|---|---|---|---|---|---|
| [1] | 2020 | Sensors at airports | Reviewed drone incidents at airports and the sensors used against small drones | No single sensor is enough; jamming is legally restricted at airports | Reason for combining camera and RF, and for recommending actions instead of jamming |
| [17], [21] | 2019–2021 | Radar | Measured how strongly commercial drones reflect radar | Reflections are very weak (RCS mostly −12 to −17 dBsm) | Shows why radar alone is not enough |
| [20] | 2021 | Camera detection | Recorded infrared and visible video of drones, airplanes, helicopters and birds at three Nordic airports | Gives pixel thresholds: below 5 pixels detection only, above 15 identification | Training data for night conditions and range estimate for the project camera |
| [5] | 2022 | Risk assessment | Built a method to rate the risk of drone intrusions at an airport (case study: Milan Malpensa) | Risk can be rated in a systematic, quantitative way | Closest example for the risk map |
| [4] | 2020 | Economic impact | Simulated the cost of a drone-related shutdown at Frankfurt | Counter-drone investment can be justified; airlines bear most losses | Supports the motivation of the project |
| [25] | 2022 | Building data | Produced 3D models of all buildings in the Netherlands | Height error below 31 cm for 95% of buildings | Building heights for line-of-sight calculation where such data exist |
| [27] | 2025 | Threat assessment | Combined sensor information with fuzzy logic to decide the threat level | Works in simulation | Alternative to the project's simpler weighted threat score |

Training a detector needs example data. Table 3.5 lists the open drone datasets that the team has catalogued. The camera datasets are used for the YOLO detector, and the RF datasets guide the design of the RF detection part.

**Table 3.5.** Open drone detection datasets catalogued by the project.

| Dataset | Modality | Content | Source |
| --- | --- | --- | --- |
| DUT Anti-UAV | Visible | 10,000 annotated images and 20 tracking videos | [28] |
| Anti-UAV (300/410/600) | Visible and infrared | Tracking benchmark series | [29] |
| Halmstad multi-sensor | Infrared, visible, audio | 650 videos (365 IR, 285 visible), 90 audio clips, more than 203,000 annotated frames | [20] |
| UAVSwarm | Visible | 72 sequences with multi-object tracking labels | [30] |
| MMAUD | Stereo RGB, LiDAR, mmWave radar, microphone array | Multi-modal recordings with 3D trajectory labels | [31] |
| Drone-vs-Bird | Visible | Challenge data with drones and birds | [32] |
| TIB-Net | Visible | 2,850 images for tiny-target detection | [33] |
| DroneRF | RF | Signal segments of 3 drone models, more than 40 GB | [34] |
| DroneDetect | RF | Software-defined-radio recordings of 7 UAS models | [35] |

### 3.2.2 Doctrine, policy and standards

A decision support system should base its recommendations on accepted procedures, not on what a language model produces by itself. The project's knowledge base is therefore built only from unclassified, publicly available doctrine and analysis [36], [37], [38]. Table 3.6 lists these documents and what each one contributes.

**Table 3.6.** Doctrine, policy and standards in the project's knowledge base.

| Source | Type | Content used by the project |
|---|---|---|
| ATP 3-01.81, *Counter-Unmanned Aircraft System Techniques* (Dec. 2023) [36] | U.S. Army doctrine | UAS group classification (Groups 1–3), the layered-defence concept and the detect–identify–defeat cycle |
| DoD Strategy for Countering Unmanned Systems (2024) [37] | U.S. strategy | The five "strategic ways": top-level principles for the knowledge base's answers |
| CRS Report R48477 [38] | Congressional research report | Summary table of C-UAS programmes and a terminology glossary |
| RAND reports on counter-UAS at military installations (2023–2026) [39] | Research reports | Analysis of installation defence against drones |
| CNAS, "Countering the Swarm" [40] | Think-tank report | Drone swarm tactics; doctrinal basis for the swarm clustering module |
| RUSI publications on drone warfare in Ukraine [41] | Think-tank analysis | Tactical development of drone and counter-drone use |
| ISW, *Russian Offensive Campaign Assessment* [42] | Daily analysis | Current evolution of drone tactics |
| NATO "Drone Edge" and Project Flytrap releases [43] | Official press releases | Current NATO counter-drone context |
| NATO IAMD COE, *The Evolving Asymmetric Threat of Unmanned Aircraft Systems* [19] | NATO centre of excellence report | Drones look like birds on radar; RF sensors can detect the link to the controller |
| IISS [2], ECFR [16] and BISI [15] | Think-tank and policy studies | European incident pattern, sensor limits near airports, the case for sensor fusion |
| MIL-STD-2525 and STANAG APP-6 [44], rendered with milsymbol [45] | Symbology standard and open library | Standard friend, hostile and unknown symbols on the C2 map |

The documents are stored in short sections, each with its source and page number, so that every recommendation can show where it comes from. The language model does not choose the action; it only explains the recommendation using the retrieved text. Jamming is not recommended automatically, for the legal and safety reasons given in Section 3.1.1 [1].

### 3.2.3 Active systems in the Turkish defence industry

Counter-drone capability is also an active industrial field in Türkiye. Before contacting companies for project feedback, the team surveyed the publicly announced C-UAS products of Turkish defence companies. Table 3.7 summarises them. The information comes from public news reports and trade press.

**Table 3.7.** Publicly announced counter-drone systems of Turkish defence companies.

| Company | System | Type, as publicly reported | Relation to the project | Sources |
|---|---|---|---|---|
| ASELSAN | İHTAR | Counter-UAV system, first shown at IDEF 2019 | Main Turkish counter-UAV product for the threat the project addresses | [46], [47] |
| ASELSAN | SEDA 100-cUAV | Acoustic drone detection sensor | Shows acoustic sensing as an extra layer beside radar and cameras | [47] |
| ASELSAN | KANGAL-FPV and new C-UAS electronic warfare systems (SAHA 2026) | Electronic warfare systems against drones, added to the Steel Dome (Çelik Kubbe) air defence architecture | Mitigation layer that the project deliberately leaves out | [47], [48], [49] |
| Meteksan Savunma | Retinar | Drone detection radar | Radar layer; relevant to the RCS argument | [50] |
| Meteksan Savunma | KAPAN | Drone countermeasure system | Detection and response product | [51] |
| SDT Uzay ve Savunma | AVCI | Anti-drone system and tactical anti-drone rifle, RF and electronic systems | RF-based approach, closest to the project's RF receiver | [52], [53] |
| STM | TUNGA-X | Interceptor anti-drone UAV, first shown at SAHA 2026 | Hard-kill response option; outside the project's scope | [54] |
| ROKETSAN | ALKA | Laser weapon against drones | Directed-energy response option; outside the project's scope | [55] |
| HAVELSAN | Command-and-control and C4ISR software | C2, simulation and AI software; autonomous CBRN reconnaissance UAV with decision support integration | Closest industrial match to the project's fusion, C2 and decision support layer | [56] |

The Turkish products concentrate on sensing and on response (jamming, interceptor drones, lasers and guns). The public reports describe what each system detects or defeats, but they do not describe how the operator is helped to decide, for example through a computed risk map or recommendations that cite doctrine. This is consistent with the gap identified in the academic literature.

### 3.2.4 Comparison with the project

Table 3.8 compares the project with the Turkish defence-industry systems of Table 3.7 and with three key academic studies, on the same criteria. "Not described" means that the feature does not appear in the public sources reviewed, not that the product lacks it.

**Table 3.8.** Comparison of Turkish defence-industry systems and key studies with the project.

| Work | Detection | Response (mitigation) | Risk map or route for the operator | Recommendation with cited doctrine |
|---|---|---|---|---|
| ASELSAN İHTAR [46] | Integrated counter-UAV system | Yes | Not described | Not described |
| ASELSAN SEDA 100-cUAV [47] | Acoustic | No | Not described | Not described |
| Meteksan Retinar and KAPAN [50], [51] | Radar | Yes (KAPAN) | Not described | Not described |
| SDT AVCI [52] | RF and electronic systems | Yes, anti-drone rifle | Not described | Not described |
| STM TUNGA-X [54] | – | Yes, interceptor drone | Not described | Not described |
| ROKETSAN ALKA [55] | – | Yes, laser | Not described | Not described |
| HAVELSAN C2 software [56] | Uses external sensors | – | C2 picture | Decision support reported |
| Lykou et al. [1] | Multi-sensor, recommended in a survey | Discussed, legally constrained | – | Analytical protection plans |
| Pascarella et al. [5] | – | – | Airport-level risk index, no grid | – |
| Arapoglou et al. [27] | Combines sensors with fuzzy logic, simulation only | – | – | Threat level only, no cited recommendation |
| **This project** | Camera + RF, fused at decision level | None by design | Grid risk map with line of sight and safe route | Yes, retrieved from public doctrine |

## 3.3 Summary and research gap

The sources agree on the problem. Small drones repeatedly close airports and approach military bases [1], [2]. The closures are caused by uncertainty, not by collisions, and they are costly [4]. The sources also agree that no single sensor is enough [1], [16]: small drones are nearly invisible to radar [17], [18], cameras need a clear line of sight [20], and RF sensors miss drones that do not transmit [1]. The building blocks the project needs already exist separately: methods for rating airport risk [5] and threat level [27], accurate terrain and building data [25], [22], open datasets for training detectors [28], [20], [34], and public doctrine [36].

The gap is that these parts are not combined. In the sources reviewed, risk is rated for a whole airport rather than shown on a map [5], and threat decisions are made without reference to doctrine [27]. Turkish defence products cover detection and response, but their public descriptions do not explain how the operator is helped to decide [46], [51], [52]. None of the works reviewed brings together low-cost detection with two sensors, a risk map that accounts for line of sight, and recommendations that cite public doctrine. The project aims to fill this gap with a low-cost system that detects and recommends but does not intervene. Its scope is limited: the demonstration is small and uses one camera and a mock drone, so it shows that the whole chain works together, not how well it would detect real drones in operation.

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

[20] F. Svanström *et al.*, "A dataset for multi-sensor drone detection," *Data in Brief*, 2021. [Online]. Available: https://arxiv.org/abs/2111.01888 (data: https://github.com/DroneDetectionThesis/Drone-detection-dataset)

[21] M. Ezuma, M. Funderburk, and I. Guvenc, "Compact-range RCS measurements and modeling of small drones at 15 GHz and 25 GHz," arXiv:1911.05926, 2019. [Online]. Available: https://arxiv.org/abs/1911.05926

[22] European Space Agency / Airbus, "Copernicus DEM GLO-30," distributed via OpenTopography. [Online]. Available: https://opentopography.org

[23] Japan Aerospace Exploration Agency (JAXA), "ALOS World 3D-30m (AW3D30)," distributed via OpenTopography. [Online]. Available: https://portal.opentopography.org/dataCatalog

[24] OpenStreetMap contributors, "OpenStreetMap," extracts via Geofabrik, ODbL. [Online]. Available: https://download.geofabrik.de

[25] R. Peters, B. Dukai, S. Vitalis, J. van Liempt, and J. Stoter, "Automated 3D reconstruction of LoD2 and LoD1 models for all 10 million buildings of the Netherlands," *Photogramm. Eng. Remote Sens.*, vol. 88, no. 3, pp. 165–170, 2022, doi: 10.14358/PERS.21-00032R2.

[26] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.

[27] F. Arapoglou, P. Zacharia, and M. Papoutsidakis, "Intelligent counter-UAV threat detection using hierarchical fuzzy decision-making and sensor fusion," *Sensors*, vol. 25, no. 19, Art. no. 6091, 2025, doi: 10.3390/s25196091.

[28] Dalian University of Technology, "DUT Anti-UAV dataset," GitHub repository, MIT License. [Online]. Available: https://github.com/wangdongdut/DUT-Anti-UAV

[29] "Anti-UAV benchmark (Anti-UAV300/410/600)," GitHub repository. [Online]. Available: https://github.com/ZhaoJ9014/Anti-UAV

[30] "UAVSwarm dataset," GitHub repository, CC BY 4.0. [Online]. Available: https://github.com/UAVSwarm/UAVSwarm-dataset

[31] NTU ARIS Lab, "MMAUD: Multi-modal anti-UAV dataset," GitHub repository, CC BY-NC-SA 4.0. [Online]. Available: https://github.com/ntu-aris/MMAUD

[32] WOSDETC, "Drone-vs-Bird detection challenge," GitHub repository. [Online]. Available: https://github.com/wosdetc/challenge

[33] "TIB-Net: Drone detection network with tiny iterative backbone," GitHub repository. [Online]. Available: https://github.com/kyn0v/TIB-Net

[34] "DroneRF dataset: RF signals of drones (Parrot Bebop, Parrot AR, DJI Phantom 3)," Mendeley Data. [Online]. Available: https://data.mendeley.com

[35] "DroneDetect dataset: RF recordings of UAS collected with BladeRF SDR," IEEE DataPort. [Online]. Available: https://ieee-dataport.org

[36] Headquarters, Department of the Army, "Counter-unmanned aircraft system techniques," ATP 3-01.81, Washington, DC, USA, Dec. 2023. [Online]. Available: https://armypubs.army.mil

[37] U.S. Department of Defense, "DoD strategy for countering unmanned systems," fact sheet, 2024. [Online]. Available: https://www.defense.gov

[38] Congressional Research Service, Report R48477 on counter-UAS programmes. [Online]. Available: https://www.everycrsreport.com

[39] RAND Corporation, research reports on counter-UAS defence of military installations, 2023–2026. [Online]. Available: https://www.rand.org

[40] Center for a New American Security (CNAS), "Countering the swarm." [Online]. Available: https://www.cnas.org

[41] Royal United Services Institute (RUSI), publications on drone warfare and counter-UAS tactics in Ukraine. [Online]. Available: https://www.rusi.org

[42] Institute for the Study of War (ISW), "Russian offensive campaign assessment," daily reports. [Online]. Available: https://www.understandingwar.org

[43] NATO, "Drone Edge" and "Project Flytrap" news releases, NATO Newsroom. [Online]. Available: https://www.nato.int

[44] U.S. Department of Defense, "Joint military symbology," MIL-STD-2525 (C/D/E); NATO, "NATO joint military symbology," STANAG APP-6 (B/D/E).

[45] spatialillusions, "milsymbol: Military symbols in JavaScript," GitHub repository, MIT License. [Online]. Available: https://github.com/spatialillusions/milsymbol

[46] Janes, "IDEF 2019: ASELSAN's İHTAR counter-UAV system breaks cover," 2019. [Online]. Available: https://janes.com/osint-insights/defence-news/idef-2019-aselsans-ihtar-counter-uav-system-breaks-cover

[47] CNN Türk, "Drone avcısı sistemleri SAHA Expo'da tanıtıldı" (drone hunter systems presented at SAHA Expo). [Online]. Available: https://www.cnnturk.com/yerel-haberler/ankara/drone-avcisi-sistemleri-saha-expoda-tanitildi-2171622

[48] Anadolu Agency, "Turkish defense company ASELSAN debuts new counter-drone electronic warfare systems at SAHA 2026," 2026. [Online]. Available: https://www.aa.com.tr/en/science-technology/turkish-defense-company-aselsan-debuts-new-counter-drone-electronic-warfare-systems-at-saha-2026/3929185

[49] EDR Magazine, "SAHA Expo 2026: ASELSAN add new elements to its Steel Dome, widening its C-UAS capabilities," 2026. [Online]. Available: https://www.edrmagazine.eu/saha-expo-2026-aselsan-add-new-elements-to-its-steel-dome-widening-its-c-uas-capabilities

[50] Armada International, "Meteksan completed delivery of drone detection radars," Jul. 2020. [Online]. Available: https://www.armadainternational.com/2020/07/meteksan-completed-delivery-drone-detection-radars/

[51] Anadolu Ajansı, "Drone tehdidini KAPAN durduracak" (KAPAN will stop the drone threat). [Online]. Available: https://www.aa.com.tr/tr/bilim-teknoloji/drone-tehdidini-kapan-durduracak/1193364

[52] haber.aero, "Drone tehdidini AVCI durduracak" (AVCI will stop the drone threat). [Online]. Available: https://haber.aero/aero-gundem/drone-tehdidini-avci-durduracak

[53] Defence Turkey, "AVCI anti-drone system." [Online]. Available: https://www.defenceturkey.com/tr/icerik/avci-anti-drone-system-4717

[54] Milliyet, "İHA tehditlerine karşı maliyeti etkin çözüm: TUNGA-X ilk kez SAHA Expo 2026'da görücüye çıktı" (cost-effective solution against UAV threats: TUNGA-X shown for the first time at SAHA Expo 2026), 2026. [Online]. Available: https://www.milliyet.com.tr/milliyet-tv/iha-tehditlerine-karsi-maliyeti-etkin-cozum-tunga-x-ilk-kez-saha-expo-2026da-gorucuye-cikti-video-7583403

[55] Milliyet, "Roketsan'dan kamikaze dron tehdidine karşı lazer silahı" (Roketsan laser weapon against the kamikaze drone threat). [Online]. Available: https://www.milliyet.com.tr/ekonomi/roketsandan-kamikaze-dron-tehdidine-karsi-lazer-silahi-7194840

[56] haber.aero, "Görünmeyen tehditler HAVELSAN'ın teknolojisi ile tespit edilecek" (invisible threats to be detected with HAVELSAN technology). [Online]. Available: https://haber.aero/savunma/gorunmeyen-tehditler-havelsanin-teknolojisi-ile-tespit-edilecek

# Literature Review

**Owner:** Yağız Akkaya · **Weight:** 30%

## 3.1 Theoretical background

### 3.1.1 The problem: small drones at airports and military bases

Small unmanned aircraft systems (UAS) have repeatedly closed airports and alarmed military installations. A survey of airport incidents between 2016 and 2019 lists ten serious cases, including the Gatwick closure of December 2018 and the Frankfurt disruption of 2019 [1]. Since 2024 the problem has moved from isolated nuisance flights to a sustained pattern: an International Institute for Strategic Studies (IISS) study counts 144 incidents in 13 European countries between August 2024 and February 2026 [2]. Table 3.1 lists the documented cases collected in the team's surveys of the four candidate pilot regions: Eindhoven, Gatwick, Aalborg and Akrotiri (Crete). They are presented as general evidence of the problem, not as a choice of pilot region.

**Table 3.1.** Documented drone incidents used as reference cases.

| Date | Location | What happened | Operational impact | Sources |
|---|---|---|---|---|
| Dec 2018 | Gatwick Airport, UK | Drone sightings closed the airport; the incident was later reviewed by the Sussex Police and Crime Commissioner | Closed for about 30 h according to the official review (33 h in a later study); about 1,000 flights disrupted and more than 140,000 passengers affected | [3], [4], [1], [5] |
| 24–25 Sep 2025 | Aalborg Airport, Denmark (joint civil and military) | Several drones with lights on were seen at night from about 21:44 to 00:54 | Flights suspended; the drones left after about 3 h; second Danish airport disrupted in one week | [6], [7] |
| 21 Nov 2025 | Volkel Air Base, Netherlands | Guards saw first 5, then 10 drones in darkness; the military fired from the ground; the drones flew off and were not found | Security response at a NATO air base | [8], [9] |
| 22 Nov 2025 | Eindhoven Airport, Netherlands (joint civil and military) | Multiple drones sighted in the evening; Ministry of Defence counter-drone systems on standby | All civil and military flights halted for about two hours and diverted to other airports; no drone recovered | [10], [9] |
| 2012 – Oct 2026 | NATO Missile Firing Installation (NAMFI) and Souda, Crete, Greece | NATO's live-fire range in Europe, where Patriot and IRIS-T SLM units train against target drones; in February 2026 the Souda base was sealed after threats against US installations | No hostile drone incursion reported; the site is used for counter-drone training | [11], [12], [13], [14] |
| Aug 2024 – Feb 2026 | 13 European countries | Systematic analysis of 144 incidents; the Volkel and Eindhoven drones were assessed as most likely launched from ships off the Dutch coast | Cumulative disruption of civil and military sites | [2] |

The incidents share one pattern. A drone is reported, nobody can confirm what it is or where it is going, and the site closes as a precaution. This is expensive: a cost study based on Frankfurt Airport found that investing in counter-drone systems can pay off, and that airlines carry most of the losses [4]. There is also little time to react. At drone speeds of 10–20 m/s, a 6–10 km protection zone gives only about 5–10 minutes of warning [1]. Stopping the drone is not simple either: jamming its radio link is illegal for civil use in many countries and can disturb the airport's own landing systems [1], [15]. The main need is therefore to detect and identify the drone quickly and to help the operator decide what to do, not to destroy it.

### 3.1.2 Detection sensors and why one sensor is not enough

Small drones are hard to detect, and each type of sensor has a different weak point. Table 3.2 summarises the strengths and weaknesses reported in the sources the team has collected.

**Table 3.2.** Small-drone detection sensor modalities.

| Sensor | Strengths | Weaknesses | Sources |
|---|---|---|---|
| Radar | Proposed as the primary detection layer at airports | Small drones reflect very little radar energy, similar to birds; birds cause false alarms; small, slow, low-flying targets are hard to track | [1], [15], [16], [17], [18] |
| RF detection | Detects the drone's radio control or video link; used with cameras for identification | Misses autonomous drones that do not transmit; depends on line of sight | [1], [18] |
| Visible and infrared cameras | Identification layer; images allow human confirmation | Need line of sight; drones are confused with birds; range is limited by how many pixels the drone covers in the image: below about 5 pixels it can only be detected, and more than 15 are needed to identify it [19] | [1], [15], [19] |
| Acoustic | Does not depend on the drone transmitting radio signals | Short range, typically under 300 m; not reliable in airport noise | [1] |

Radar alone is not enough, because a small drone reflects very little radar energy. This is measured as the radar cross section (RCS). Laboratory measurements of commercial drones such as the DJI Matrice, Mavic and Phantom gave RCS values mostly between −12 and −17 dBsm [16], [20], which is far smaller than a conventional aircraft. A NATO centre of excellence report notes that many commercial drones have the RCS of a bird [18]. A recent survey reports tests by the UK Civil Aviation Authority in which standard airport radar could not reliably track small DJI Phantom-class drones beyond 500 m [17]. For this reason the main survey on airport protection concludes that "adopting a single sensor technology for UAV detection in airports cannot provide the desired situational awareness" [1], and a policy study of European drone defence also recommends combining sensors [15]. This supports the project's choice of two low-cost sensors with different weak points: a camera, which cannot see behind obstacles, and an RF receiver, which cannot hear a drone that does not transmit.

### 3.1.3 Map data: line of sight, terrain and air traffic

Cameras, radar and RF receivers all need a clear line of sight to the drone, so a threat map must know where the sensors can and cannot see. This requires height data for the terrain and the buildings. Global elevation models such as Copernicus GLO-30 and ALOS AW3D30 give terrain heights on a 30 m grid [21], [22], and OpenStreetMap adds roads, buildings and site boundaries [23], although building heights are often missing. Some countries publish much more detailed data. The Dutch 3DBAG dataset gives the height of every building in the Netherlands, with an error below 31 cm for 95% of buildings [24]. Table 3.3 summarises what the team found for each candidate pilot region.

**Table 3.3.** Geospatial data found in the team's candidate pilot-region surveys.

| Region | Terrain and surface | Buildings | Drone restriction zones | Air traffic |
|---|---|---|---|---|
| Eindhoven, Netherlands | AHN national LiDAR | 3DBAG heights for every building [24] | 3 km runway buffer | OpenSky; open ADS-B archive |
| Gatwick, UK | Environment Agency 1 m terrain and surface models | Surface heights from the 1 m surface model | NATS UAS restriction dataset | OpenSky |
| Aalborg, Denmark | DHM national model, 0.4 m grid | OSM footprints | Official map | OpenSky |
| Akrotiri, Crete | Copernicus GLO-30, 30 m [21] | OSM footprints | Official map (HCAA) | Airport statistics |
The system also needs to know the normal air traffic around a site in order to judge how serious a drone near a runway is. The OpenSky Network provides open aircraft position data for this purpose, but it only shows aircraft that broadcast their position [25], so small drones do not appear in it. Drone detection must therefore come from the project's own sensors.

## 3.2 Previous work

### 3.2.1 Academic studies

Table 3.4 lists the key studies the team has reviewed and states how each one is used in the project. The doctrine documents behind the knowledge base are covered separately in Section 3.2.2.

**Table 3.4.** Key studies relevant to the project.

| Ref. | Year | Topic | What the study did | Main finding | Use in the project |
|---|---|---|---|---|---|
| [1] | 2020 | Sensors at airports | Reviewed drone incidents at airports and the sensors used against small drones | No single sensor is enough; jamming is legally restricted at airports | Reason for combining camera and RF, and for recommending actions instead of jamming |
| [16], [20] | 2019–2021 | Radar | Measured how strongly commercial drones reflect radar | Reflections are very weak (RCS mostly −12 to −17 dBsm) | Shows why radar alone is not enough |
| [19] | 2021 | Camera detection | Recorded infrared and visible video of drones, airplanes, helicopters and birds at three Nordic airports | Gives pixel thresholds: below 5 pixels detection only, above 15 identification | Training data for night conditions and range estimate for the project camera |
| [5] | 2022 | Risk assessment | Built a method to rate the risk of drone intrusions at an airport (case study: Milan Malpensa) | Risk can be rated in a systematic, quantitative way | Closest example for the risk map |
| [4] | 2020 | Economic impact | Simulated the cost of a drone-related shutdown at Frankfurt | Counter-drone investment can be justified; airlines bear most losses | Supports the motivation of the project |
| [24] | 2022 | Building data | Produced 3D models of all buildings in the Netherlands | Height error below 31 cm for 95% of buildings | Building heights for line-of-sight calculation where such data exist |
| [26] | 2025 | Threat assessment | Combined sensor information with fuzzy logic to decide the threat level | Works in simulation | Alternative to the project's simpler weighted threat score |

Training a detector needs example data. Table 3.5 lists the open drone datasets that the team has catalogued. The camera datasets are used for the YOLO detector, and the RF datasets guide the design of the RF detection part.

**Table 3.5.** Open drone detection datasets catalogued by the project.

| Dataset | Modality | Content | Source |
| --- | --- | --- | --- |
| DUT Anti-UAV | Visible | 10,000 annotated images and 20 tracking videos | [27] |
| Anti-UAV (300/410/600) | Visible and infrared | Tracking benchmark series | [28] |
| Halmstad multi-sensor | Infrared, visible, audio | 650 videos (365 IR, 285 visible), 90 audio clips, more than 203,000 annotated frames | [19] |
| UAVSwarm | Visible | 13 scenes and 12,598 annotated images of drone swarms | [29] |
| MMAUD | Stereo RGB, LiDAR, mmWave radar, microphone array | Multi-modal recordings with 3D trajectory labels | [30] |
| Drone-vs-Bird | Visible | Challenge data with drones and birds | [31] |
| TIB-Net | Visible | 2,850 images for tiny-target detection | [32] |
| DroneRF | RF | Signal segments of 3 drone models, more than 40 GB | [33] |
| DroneDetect | RF | Software-defined-radio recordings of 7 UAS models | [34] |

### 3.2.2 Doctrine, policy and standards

A decision support system should base its recommendations on accepted procedures, not on what a language model produces by itself. The project's knowledge base is therefore built only from unclassified, publicly available doctrine and analysis [35], [36], [37]. Table 3.6 lists these documents and what each one contributes.

**Table 3.6.** Doctrine, policy and standards in the project's knowledge base.

| Source | Type | Content used by the project |
|---|---|---|
| ATP 3-01.81, *Counter-Unmanned Aircraft System (C-UAS)* (Aug. 2023) [35] | U.S. Army doctrine | UAS Groups 1–5 (Groups 1 and 2 are the small drones, with a low radar cross section); the layered-defence approach; the active-defence sequence detect, identify, decide and engage |
| DoD Strategy for Countering Unmanned Systems, fact sheet (2024) [36] | U.S. strategy | The five "strategic ways" (understand, disrupt, defend, deliver, develop): top-level principles for the knowledge base's answers |
| CRS Report R48477, *DoD Counter Unmanned Aircraft Systems* (2025) [37] | Congressional research report | Background on U.S. C-UAS programmes and their funding |
| RAND commentary on defending military bases against drones (2025) [38] | Think-tank commentary | Lessons from a tabletop exercise on base defence against drones |
| CNAS, *Countering the Swarm* (2025) [39] | Think-tank report | Drone swarm threat; argues for layered defences that combine several sensors and effectors |
| RUSI, *Protecting the Force from Uncrewed Aerial Systems* (2024) [40] | Think-tank paper | No single sensor or effector is enough; C-UAS must be layered and combined |
| ISW, *Russian Offensive Campaign Assessment* [41] | Daily analysis | Current evolution of drone and interceptor-drone tactics in Ukraine |
| NATO, "NATO's Drone Edge" (2026) [42] | Official text | Current NATO counter-drone context and planned investment |
| U.S. Army, Project Flytrap lessons learned (2025) [43] | Official news article | Field exercise result: no single system is enough, layered defence is needed |
| NATO IAMD COE, *The Evolving Asymmetric Threat of Unmanned Aircraft Systems* [18] | NATO centre of excellence report | Drones look like birds on radar; RF sensors can detect the link to the controller |
| IISS [2], ECFR [15] and BISI [44] | Think-tank and policy studies | European incident pattern, sensor limits near airports, the case for sensor fusion |
| MIL-STD-2525 and STANAG APP-6 [45], rendered with milsymbol [46] | Symbology standard and open library | Standard friend, hostile and unknown symbols on the C2 map |

The documents are stored in short sections, each with its source and page number, so that every recommendation can show where it comes from. The language model does not choose the action; it only explains the recommendation using the retrieved text. Jamming is not recommended automatically, for the legal and safety reasons given in Section 3.1.1 [1].

### 3.2.3 Active systems in the Turkish defence industry

Counter-drone capability is also an active industrial field in Türkiye. The team surveyed the publicly announced C-UAS products of Turkish defence companies. Table 3.7 summarises them. The information comes from public news reports and trade press.

**Table 3.7.** Publicly announced counter-drone systems of Turkish defence companies.

| Company | System | Type, as publicly reported | Relation to the project | Sources |
|---|---|---|---|---|
| ASELSAN | İHTAR | Counter-UAV system with radar, electro-optical sensor, optional acoustic direction finder and a directional jammer; shown at IDEF 2019 | Multi-sensor detection in one system, the idea the project follows at small scale | [47], [48] |
| ASELSAN | SEDA 100-cUAV | Acoustic drone detection system, integrated into İHTAR | Acoustic sensing as an extra detection layer | [48] |
| ASELSAN | KANGAL-FPV (2024); Gökalp, Gökberk 10, Ejderha 210 and Miğfer (SAHA 2026) | Anti-drone jammer; interceptor drone, 10 kW laser, high-power microwave system and close-range turret, added to the Steel Dome (Çelik Kubbe) | Response layer that the project deliberately leaves out | [48], [49], [50] |
| Meteksan Savunma | Retinar | Ku-band radar that detects mini and micro UAVs at up to 3 km | Radar layer of drone detection | [51] |
| Meteksan Savunma, SDT and Tamgör | KAPAN | Counter-drone system: radar and thermal/daylight cameras, fusion software that shows targets on a single common picture, RF jammer and optional laser | Closest Turkish example of sensor fusion on one picture | [52] |
| SDT Uzay ve Savunma | AVCI | Anti-drone system: radar, electro-optical and thermal cameras, direction-finding receiver for the pilot, jamming or hard-kill response | Combines radar, camera and RF sensing, as the project does with camera and RF | [53], [54] |
| STM | TUNGA-X | Interceptor drone against kamikaze UAVs, first shown at SAHA 2026 | Response option outside the project's scope | [55] |
| ROKETSAN | ALKA | Directed-energy system: drone detection radar, jamming and laser | Response option outside the project's scope | [56] |
| HAVELSAN | Autonomous CBRN reconnaissance air system | UAV that maps chemical, biological, radiological and nuclear hazard zones and sends the results to decision-support systems | Industrial example of sensor data feeding decision support | [57] |

The Turkish products concentrate on sensing and on response (jamming, interceptor drones, lasers and microwave systems). The public reports describe what each system detects or defeats, and KAPAN is reported to fuse its sensors on a single picture [52]. They do not describe how the operator is helped to decide, for example through a computed risk map or recommendations that cite doctrine. This is consistent with the gap identified in the academic literature.

### 3.2.4 Comparison with the project

Table 3.8 compares the project with the Turkish defence-industry systems of Table 3.7 and with three key academic studies, on the same criteria. "Not described" means that the feature does not appear in the public sources reviewed, not that the product lacks it.

**Table 3.8.** Comparison of Turkish defence-industry systems and key studies with the project.

| Work | Detection | Response (mitigation) | Risk map or route for the operator | Recommendation with cited doctrine |
|---|---|---|---|---|
| ASELSAN İHTAR [47] | Radar, electro-optical, acoustic | Yes, jammer | Not described | Not described |
| ASELSAN SEDA 100-cUAV [48] | Acoustic | No | Not described | Not described |
| Meteksan Retinar [51] | Radar | No | Not described | Not described |
| KAPAN [52] | Radar and cameras, fused on one picture | Yes, jammer and laser | Not described | Not described |
| SDT AVCI [54] | Radar, cameras, RF direction finding | Yes, jamming or hard-kill | Not described | Not described |
| STM TUNGA-X [55] | Uses external radar | Yes, interceptor drone | Not described | Not described |
| ROKETSAN ALKA [56] | Radar | Yes, jamming and laser | Not described | Not described |
| Lykou et al. [1] | Multi-sensor, recommended in a survey | Discussed, legally constrained | – | Analytical protection plans |
| Pascarella et al. [5] | – | – | Airport-level risk index | – |
| Arapoglou et al. [26] | Combines sensors with fuzzy logic, simulation only | – | – | Threat level only, no cited recommendation |
| **This project** | Camera + RF, fused at decision level | None by design | Grid risk map with line of sight and safe route | Yes, retrieved from public doctrine |

## 3.3 Summary and research gap

The sources agree on the problem. Small drones repeatedly close airports and approach military bases [1], [2]. The closures are caused by uncertainty, not by collisions, and they are costly [4]. The sources also agree that no single sensor is enough [1], [15]: small drones are nearly invisible to radar [16], [17], cameras need a clear line of sight [19], and RF sensors miss drones that do not transmit [1]. The building blocks the project needs already exist separately: methods for rating airport risk [5] and threat level [26], accurate terrain and building data [24], [21], open datasets for training detectors [27], [19], [33], and public doctrine [35].

The gap is that these parts are not combined. In the sources reviewed, risk is rated for a whole airport rather than shown on a map [5], and threat decisions are made without reference to doctrine [26]. Turkish defence products cover detection and response, but their public descriptions do not explain how the operator is helped to decide [47], [52], [54]. None of the works reviewed brings together low-cost detection with two sensors, a risk map that accounts for line of sight, and recommendations that cite public doctrine. The project aims to fill this gap with a low-cost system that detects and recommends but does not intervene. Its scope is limited: the demonstration is small and uses one camera and a mock drone, so it shows that the whole chain works together, not how well it would detect real drones in operation.

## References

[1] G. Lykou, D. Moustakas, and D. Gritzalis, "Defending airports from UAS: A survey on cyber-attacks and counter-drone sensing technologies," *Sensors*, vol. 20, no. 12, Art. no. 3537, 2020, doi: 10.3390/s20123537.

[2] C. Edwards, R. Fox O'Loughlin, and L. Bearn, "Russia's UAV campaign over Europe," International Institute for Strategic Studies (IISS), London, U.K., Jul. 2026. [Online]. Available: https://www.astrid-online.it/static/upload/russ/russia-uav-campaign-over-europe.pdf

[3] Office of the Sussex Police and Crime Commissioner, "Performance & Accountability Meeting," minutes, 18 Oct. 2019. [Online]. Available: https://www.sussex-pcc.gov.uk/media/4422/10-pam-minutes-18102019.pdf

[4] P. Wendt, A. Voltes-Dorta, and P. Suau-Sanchez, "Estimating the costs for the airport operator and airlines of a drone-related shutdown: An application to Frankfurt international airport," *J. Transp. Secur.*, vol. 13, pp. 93–116, 2020, doi: 10.1007/s12198-020-00212-4.

[5] D. Pascarella, G. Gigante, A. Vozella, P. Bieber, T. Dubot, E. Martinavarro, G. Barraco, and G. Li Calzi, "A methodological framework for the risk assessment of drone intrusions in airports," *Aerospace*, vol. 9, no. 12, Art. no. 747, 2022, doi: 10.3390/aerospace9120747.

[6] L. Rasmussen, "Drones disrupt flights at second Danish airport in a week," Reuters (via The Star), 25 Sep. 2025. [Online]. Available: https://www.thestar.com.my/news/world/2025/09/25/denmark039s-aalborg-airport-closed-due-to-drones-in-airspace

[7] Danish National Police (Rigspolitiet), press releases on drone activity at Aalborg Airport, 25–26 Sep. 2025.

[8] Omroep Brabant, "Tien drones boven Volkel, volgens minister Brekelmans was 'zicht beperkt' in Volkel" (ten drones over Volkel), 22 Nov. 2025. [Online]. Available: https://www.omroepbrabant.nl/nieuws/4794336/tien-drones-boven-vliegbasis-volkel-zegt-minister-brekelmans

[9] Tweede Kamer der Staten-Generaal, "Wijziging van de begrotingsstaat van het Defensiematerieelbegrotingsfonds (K) voor het jaar 2025 (Incidentele suppletoire begroting inzake bestrijding van drones): Verslag van een wetgevingsoverleg" (report of the Defence Committee meeting of 26 Nov. 2025 on the counter-drone budget), Kamerstuk 36 858, no. 6, 17 Dec. 2025. [Online]. Available: https://zoek.officielebekendmakingen.nl/kst-36858-6.pdf

[10] Al Jazeera, "Air traffic suspended at Netherlands airport after drone sightings," 22 Nov. 2025. [Online]. Available: https://www.aljazeera.com/news/2025/11/22/air-traffic-suspended-at-netherlands-airport-after-drone-sightings

[11] Supreme Headquarters Allied Powers Europe (SHAPE), "NATO marks 60 years of integrated air defence training at Crete firing range," 20 Oct. 2024. [Online]. Available: https://shape.nato.int/news-archive/2024/nato-marks-60-years-of-integrated-air-defence-training-at-crete-firing-range.aspx

[12] Bundeswehr, "Herr der Drohnen – Flugzieldarstellung auf Kreta" (master of drones: aerial target presentation on Crete), 30 Nov. 2020. [Online]. Available: https://www.bundeswehr.de/de/organisation/luftwaffe/aktuelles/herr-der-drohnen-flugzieldarstellung-auf-kreta-4680108

[13] deutschland.de, "German air defence reaches 'milestones'," 15 Oct. 2026. [Online]. Available: https://www.deutschland.de/en/news/german-air-defence-reaches-milestones

[14] Protothema (English edition), "Souda base in Crete sealed after Iran's threats against all U.S. installations," 28 Feb. 2026. [Online]. Available: https://en.protothema.gr/2026/02/28/breaking-souda-base-in-crete-sealed-after-irans-threats-against-all-u-s-installations/

[15] U. Franke, "Buzzkill: How to defend Europe against drones," European Council on Foreign Relations (ECFR), Policy Brief, 17 Aug. 2026. [Online]. Available: https://ecfr.eu/publication/buzzkill-how-to-defend-europe-against-drones/

[16] M. Ezuma, C. K. Anjinappa, M. Funderburk, and I. Guvenc, "Radar cross section based statistical recognition of UAVs at microwave frequencies," arXiv:2102.11954, 2021. [Online]. Available: https://arxiv.org/abs/2102.11954

[17] Y. Cui, J. Nie, W. Yuan, F. Liu, Z. Jia, J. Xu, Z. Feng, and M.-S. Alouini, "Low-altitude wireless networks: The next horizon of wireless infrastructure," arXiv:2605.24368, May 2026, Sec. 4.2.3. [Online]. Available: https://arxiv.org/abs/2605.24368

[18] A. Blazogiannaki, "The evolving asymmetric threat of unmanned aircraft systems: A weapon of choice for non-state actors," NATO Integrated Air and Missile Defence Centre of Excellence (IAMD COE), Souda Air Base, Chania, Greece, c. 2024. [Online]. Available: https://iamd-coe.org/wp-content/uploads/2024/11/The-Evolving-Asymmetric-Threat-of-Unmanned-Aircraft-Systems-final.pdf

[19] F. Svanström, F. Alonso-Fernandez, and C. Englund, "A dataset for multi-sensor drone detection," *Data in Brief*, 2021, doi: 10.1016/j.dib.2021.107521. [Online]. Available: https://arxiv.org/abs/2111.01888 (data: https://github.com/DroneDetectionThesis/Drone-detection-dataset)

[20] M. Ezuma, M. Funderburk, and I. Guvenc, "Compact-range RCS measurements and modeling of small drones at 15 GHz and 25 GHz," arXiv:1911.05926, 2019. [Online]. Available: https://arxiv.org/abs/1911.05926

[21] European Space Agency, "Copernicus DEM: Global and European digital elevation model (GLO-30)," Copernicus Data Space Ecosystem, doi: 10.5270/ESA-c5d3d65. [Online]. Available: https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

[22] Japan Aerospace Exploration Agency (JAXA), "ALOS World 3D 30 meter DEM," V3.2, Jan. 2021, distributed by OpenTopography, doi: 10.5069/G94M92HB.

[23] OpenStreetMap contributors, "OpenStreetMap," extracts via Geofabrik, ODbL. [Online]. Available: https://download.geofabrik.de

[24] R. Peters, B. Dukai, S. Vitalis, J. van Liempt, and J. Stoter, "Automated 3D reconstruction of LoD2 and LoD1 models for all 10 million buildings of the Netherlands," *Photogramm. Eng. Remote Sens.*, vol. 88, no. 3, pp. 165–170, 2022, doi: 10.14358/PERS.21-00032R2. [Online]. Available: https://arxiv.org/abs/2201.01191

[25] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, Apr. 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.

[26] F. Arapoglou, P. Zacharia, and M. Papoutsidakis, "Intelligent counter-UAV threat detection using hierarchical fuzzy decision-making and sensor fusion," *Sensors*, vol. 25, no. 19, Art. no. 6091, 2025, doi: 10.3390/s25196091.

[27] J. Zhao, J. Zhang, D. Li, and D. Wang, "Vision-based anti-UAV detection and tracking," *IEEE Trans. Intell. Transp. Syst.*, 2022; DUT Anti-UAV dataset. [Online]. Available: https://github.com/wangdongdut/DUT-Anti-UAV

[28] "Anti-UAV benchmark (Anti-UAV300/410/600)," GitHub repository. [Online]. Available: https://github.com/ZhaoJ9014/Anti-UAV

[29] "UAVSwarm dataset," GitHub repository. [Online]. Available: https://github.com/UAVSwarm/UAVSwarm-dataset

[30] NTU ARIS Lab, "MMAUD: Multi-modal anti-UAV dataset," GitHub repository, CC BY-NC-SA 4.0. [Online]. Available: https://github.com/ntu-aris/MMAUD

[31] WOSDETC, "Drone-vs-Bird detection challenge," GitHub repository. [Online]. Available: https://github.com/wosdetc/challenge

[32] "TIB-Net: Drone detection network with tiny iterative backbone," GitHub repository. [Online]. Available: https://github.com/kyn0v/TIB-Net

[33] M. F. Al-Sa'd, M. S. Allahham, A. Mohamed, A. Al-Ali, T. Khattab, and A. Erbad, "DroneRF dataset: A dataset of drones for RF-based detection, classification, and identification," Mendeley Data, V1, 2019, doi: 10.17632/f4c2b4n755.1.

[34] C. J. Swinney and J. C. Woods, "DroneDetect dataset: A radio frequency dataset of unmanned aerial system (UAS) signals for machine learning detection and classification," IEEE DataPort, 2021, doi: 10.21227/5jjj-1m32.

[35] Headquarters, Department of the Army, "Counter-unmanned aircraft system (C-UAS)," ATP 3-01.81, Washington, DC, USA, 11 Aug. 2023. [Online]. Available: https://armypubs.army.mil

[36] U.S. Department of Defense, "Fact sheet: Department of Defense strategy for countering unmanned systems," Dec. 5, 2024. [Online]. Available: https://www.suasnews.com/wp-content/uploads/2024/12/FACT-SHEET-STRATEGY-FOR-COUNTERING-UNMANNED-SYSTEMS.pdf

[37] Congressional Research Service, "Department of Defense counter unmanned aircraft systems: Background and issues for Congress," Rep. R48477, Mar. 31, 2025. [Online]. Available: https://www.everycrsreport.com/reports/R48477.html

[38] P. Lushenko, R. McGuire, C. G. Pernin, and S. M. Zeigler, "Defending U.S. military bases against drones? A recent tabletop exercise explores how," RAND Corporation, commentary, Jun. 2, 2025. [Online]. Available: https://www.rand.org/pubs/commentary/2025/06/defending-us-military-bases-against-drones-a-recent.html

[39] S. Pettyjohn and M. Campbell, "Countering the swarm: Protecting the joint force in the drone age," Center for a New American Security (CNAS), Washington, DC, USA, Sep. 10, 2025. [Online]. Available: https://www.cnas.org/publications/reports/countering-the-swarm

[40] J. Watling and J. Bronk, "Protecting the force from uncrewed aerial systems," Royal United Services Institute (RUSI), London, U.K., Occasional Paper, Oct. 15, 2024. [Online]. Available: https://rusi.org/explore-our-research/publications/occasional-papers/protecting-force-uncrewed-aerial-systems

[41] Institute for the Study of War (ISW), "Russian offensive campaign assessment," daily report series (e.g. Nov. 2, 2026). [Online]. Available: https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-november-2-2026

[42] NATO, "NATO's drone edge," official text, Jul. 7, 2026. [Online]. Available: https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2026/07/07/natos-drone-edge

[43] S. Collins, "V Corps leaders share lessons learned on counter-UAS training from Project Flytrap," U.S. Army News Service, Jul. 30, 2025. [Online]. Available: https://www.army.mil/article/287453

[44] M. Asllani, "Probing the gaps: The drone intelligence threat in Europe," Bloomsbury Intelligence and Security Institute (BISI), 18 Nov. 2025. [Online]. Available: https://bisi.org.uk/reports/probing-the-gaps-the-drone-intelligence-threat-in-europe

[45] U.S. Department of Defense, "Joint military symbology," MIL-STD-2525 (C/D/E); NATO, "NATO joint military symbology," STANAG APP-6 (B/D/E).

[46] spatialillusions, "milsymbol: Military symbols in JavaScript," GitHub repository, MIT License. [Online]. Available: https://github.com/spatialillusions/milsymbol

[47] Janes, "IDEF 2019: Aselsan's iHTAR counter-UAV system breaks cover," 2019. [Online]. Available: https://janes.com/osint-insights/defence-news/idef-2019-aselsans-ihtar-counter-uav-system-breaks-cover

[48] CNN Türk, "Drone avcısı sistemleri, SAHA EXPO'da tanıtıldı" (drone hunter systems introduced at SAHA EXPO), 23 Oct. 2024. [Online]. Available: https://www.cnnturk.com/yerel-haberler/ankara/drone-avcisi-sistemleri-saha-expoda-tanitildi-2171622

[49] Anadolu Agency, "Turkish defense company Aselsan debuts new counter-drone, electronic warfare systems at SAHA 2026," 6 May 2026. [Online]. Available: https://www.aa.com.tr/en/science-technology/turkish-defense-company-aselsan-debuts-new-counter-drone-electronic-warfare-systems-at-saha-2026/3929185

[50] EDR Magazine, "Saha Expo 2026 – Aselsan add new elements to its Steel Dome widening its C-UAS capabilities," 2026. [Online]. Available: https://www.edrmagazine.eu/saha-expo-2026-aselsan-add-new-elements-to-its-steel-dome-widening-its-c-uas-capabilities

[51] Armada International, "Meteksan completed delivery drone detection radars," 29 Jul. 2020. [Online]. Available: https://www.armadainternational.com/2020/07/meteksan-completed-delivery-drone-detection-radars/

[52] Anadolu Ajansı, "Drone tehdidini 'Kapan' durduracak" ('Kapan' will stop the drone threat), 3 Jul. 2018. [Online]. Available: https://www.aa.com.tr/tr/bilim-teknoloji/drone-tehdidini-kapan-durduracak/1193364

[53] haber.aero, "Drone'ları 'Avcı' avlayacak" ('Avcı' will hunt drones), 1 May 2019. [Online]. Available: https://haber.aero/aero-gundem/drone-tehdidini-avci-durduracak

[54] Defence Turkey, "AVCI – Anti-drone system," 15 Aug. 2021. [Online]. Available: https://www.defenceturkey.com/tr/icerik/avci-anti-drone-system-4717

[55] Milliyet, "İHA tehditlerine karşı maliyeti etkin çözüm! TUNGA-X ilk kez SAHA EXPO 2026'da görücüye çıktı" (cost-effective solution against UAV threats: TUNGA-X shown for the first time at SAHA EXPO 2026), 6 May 2026. [Online]. Available: https://www.milliyet.com.tr/milliyet-tv/iha-tehditlerine-karsi-maliyeti-etkin-cozum-tunga-x-ilk-kez-saha-expo-2026da-gorucuye-cikti-video-7583403

[56] Milliyet, "Roketsan'dan, kamikaze dron tehdidine karşı lazer silahı" (Roketsan laser weapon against the kamikaze drone threat), 23 Sep. 2024. [Online]. Available: https://www.milliyet.com.tr/ekonomi/roketsandan-kamikaze-dron-tehdidine-karsi-lazer-silahi-7194840

[57] haber.aero, "Görünmeyen tehditler HAVELSAN'ın teknolojisi ile tespit edilecek" (invisible threats to be detected with HAVELSAN technology), 17 Jan. 2021. [Online]. Available: https://haber.aero/savunma/gorunmeyen-tehditler-havelsanin-teknolojisi-ile-tespit-edilecek

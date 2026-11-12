# Literature Review

**Owner:** Yağız Akkaya · **Weight:** 30%

## 3.1 Theoretical background

**The problem.** Small drones have repeatedly closed airports and alarmed military bases. A survey of airport incidents lists ten serious cases between 2016 and 2019 [1], and a later study counts 144 incidents in 13 European countries between August 2024 and February 2026 [2]. Table 3.1 shows four cases from the regions the team has studied.

**Table 3.1.** Example drone incidents.

| Date | Location | Impact | Sources |
|---|---|---|---|
| Dec 2018 | Gatwick Airport, UK | Closed for about 30 hours; about 1,000 flights and more than 140,000 passengers affected | [3], [4] |
| Sep 2025 | Aalborg Airport, Denmark | Drones seen at night for about 3 hours; flights suspended | [5] |
| Nov 2025 | Volkel Air Base, Netherlands | Guards saw up to 10 drones over the base at night; the drones flew away and were not found | [6] |
| Nov 2025 | Eindhoven Airport, Netherlands | All civil and military flights halted for about two hours | [7] |

The incidents share one pattern: a drone is reported, nobody can confirm what it is or where it is going, and the site closes as a precaution. This is costly, and airlines carry most of the losses [4]. Jamming the drone is also not a simple answer, because it is legally restricted for civil use and can disturb the airport's own landing systems [1]. The main need is therefore to detect the drone quickly and to help the operator decide what to do.

**Sensors.** Each type of sensor has a different weak point (Table 3.2).

**Table 3.2.** Sensors for small-drone detection.

| Sensor | Strength | Weakness | Sources |
|---|---|---|---|
| Radar | Main detection layer at airports | Small drones reflect very little radar energy and look like birds | [1], [8], [9] |
| RF receiver | Detects the drone's radio link | Misses drones that do not transmit | [1], [9] |
| Camera | Lets a human confirm the target | Needs a clear line of sight; a distant drone covers only a few pixels, so range is limited | [1], [10] |
| Acoustic | Works without a radio signal | Short range (under 300 m); unreliable in airport noise | [1] |

Measurements of commercial drones gave radar reflections far below those of normal aircraft [8], and tests reported in a recent survey show that standard airport radar could not reliably track small drones beyond 500 m [11]. The main survey on airport protection therefore concludes that a single sensor technology is not enough [1]. This supports the project's choice of two low-cost sensors with different weak points: a camera and an RF receiver.

**Map data.** Sensors need a clear line of sight, so the system must know the height of the terrain and the buildings. Global elevation models give terrain heights on a 30 m grid [12], and OpenStreetMap adds roads, buildings and site boundaries [13]. Some countries publish more detailed data: the Dutch 3DBAG dataset gives the height of every building in the Netherlands, with an error below 31 cm for 95% of buildings [14]. Normal air traffic can be taken from the OpenSky Network, which only shows aircraft that broadcast their position [15], so drones must be detected by the project's own sensors.

## 3.2 Previous work

**Academic studies.** Table 3.3 lists the key studies and how each one is used in the project.


**Table 3.3.** Key studies.

| Ref. | Year | Topic | Main finding | Use in the project |
|---|---|---|---|---|
| [1] | 2020 | Sensors at airports | No single sensor is enough; jamming is restricted | Reason for combining camera and RF |
| [8] | 2021 | Radar | Small drones reflect very little radar energy | Shows why radar alone is not enough |
| [10] | 2021 | Camera detection | Open infrared and visible dataset recorded at airports | Training data and camera range estimate |


Open datasets are available for training the detector: DUT Anti-UAV [16], UAVSwarm [17] and the Halmstad dataset [10] for cameras, and DroneRF [18] for RF signals.

**Doctrine.** The system's recommendations must come from accepted procedures, not from what a language model produces by itself. The knowledge base is therefore built only from public documents (Table 3.4), and every recommendation shows its source.


**Table 3.4.** Main documents in the knowledge base.

| Document | Content to be used in the project |
|---|---|
| ATP 3-01.81, *Counter-Unmanned Aircraft System* (2023) [19] | Drone size groups 1–5, defence in several layers, and the sequence detect, identify, decide, engage |
| DoD Strategy for Countering Unmanned Systems (2024) [20] | The five top-level goals of the U.S. approach to countering drones |
| RUSI, *Protecting the Force from Uncrewed Aerial Systems* (2024) [21] | No single sensor or countermeasure is enough |
| CNAS, *Countering the Swarm* (2025) [22] | The threat of drone swarms and the need for defence in several layers |
| NATO IAMD COE, *The Evolving Asymmetric Threat of Unmanned Aircraft Systems* (c. 2024) [9] | What radar and RF sensors cannot detect in small drones |


**Turkish defence industry.** Counter-drone systems are also an active industrial field in Türkiye. Table 3.5 compares publicly announced Turkish systems with the project.


**Table 3.5.**  Comparison of existing Counter-UAS systems with the proposed project.

| Work | Detection | Response | Risk map for the operator | Recommendation citing doctrine |
|---|---|---|---|---|
| ASELSAN İHTAR [23] | Radar, camera, acoustic | Jammer | Not described | Not described |
| Meteksan Retinar [24] | Radar | None | Not described | Not described |
| KAPAN [25] | Radar and cameras, shown together on one screen | Jammer, laser | Not described | Not described |
| SDT AVCI [26] | Radar, cameras, RF | Jamming or physical destruction | Not described | Not described |
| STM TUNGA-X [27] | Uses a separate radar | Interceptor drone | Not described | Not described |
| ROKETSAN ALKA [28] | Radar | Jamming, laser | Not described | Not described |
| **This project** | Camera + RF | None (the system only recommends) | Risk map with line of sight | Yes, from public doctrine |

"Not described" means the feature does not appear in the public sources reviewed. The Turkish products concentrate on sensing and on response (jamming, interceptor drones, lasers). Their public descriptions do not explain how the operator is helped to decide.

## 3.3 Summary and research gap

The sources agree that small drones repeatedly close airports [1], [2] and that no single sensor is enough [1], [21]. The parts the project needs already exist separately: open map data and training datasets, and public doctrine [19].

The gap is that these parts are not combined. Industrial products focus on detection and response. None of the works reviewed brings together low-cost detection with two sensors, a risk map that accounts for line of sight, and recommendations that cite public doctrine. The project aims to fill this gap with a low-cost system that detects and recommends but does not intervene.

## References

[1] G. Lykou, D. Moustakas, and D. Gritzalis, "Defending airports from UAS: A survey on cyber-attacks and counter-drone sensing technologies," *Sensors*, vol. 20, no. 12, Art. no. 3537, 2020, doi: 10.3390/s20123537.

[2] C. Edwards, R. Fox O'Loughlin, and L. Bearn, "Russia's UAV campaign over Europe," International Institute for Strategic Studies (IISS), London, U.K., Jul. 2026. [Online]. Available: https://www.astrid-online.it/static/upload/russ/russia-uav-campaign-over-europe.pdf

[3] Office of the Sussex Police and Crime Commissioner, "Performance & Accountability Meeting," minutes, 18 Oct. 2019. [Online]. Available: https://www.sussex-pcc.gov.uk/media/4422/10-pam-minutes-18102019.pdf

[4] P. Wendt, A. Voltes-Dorta, and P. Suau-Sanchez, "Estimating the costs for the airport operator and airlines of a drone-related shutdown: An application to Frankfurt international airport," *J. Transp. Secur.*, vol. 13, pp. 93–116, 2020, doi: 10.1007/s12198-020-00212-4.

[5] L. Rasmussen, "Drones disrupt flights at second Danish airport in a week," Reuters (via The Star), 25 Sep. 2025. [Online]. Available: https://www.thestar.com.my/news/world/2025/09/25/denmark039s-aalborg-airport-closed-due-to-drones-in-airspace

[6] Omroep Brabant, "Tien drones boven Volkel, volgens minister Brekelmans was 'zicht beperkt' in Volkel" (ten drones over Volkel), 22 Nov. 2025. [Online]. Available: https://www.omroepbrabant.nl/nieuws/4794336/tien-drones-boven-vliegbasis-volkel-zegt-minister-brekelmans

[7] Al Jazeera, "Air traffic suspended at Netherlands airport after drone sightings," 22 Nov. 2025. [Online]. Available: https://www.aljazeera.com/news/2025/11/22/air-traffic-suspended-at-netherlands-airport-after-drone-sightings

[8] M. Ezuma, C. K. Anjinappa, M. Funderburk, and I. Guvenc, "Radar cross section based statistical recognition of UAVs at microwave frequencies," arXiv:2102.11954, 2021. [Online]. Available: https://arxiv.org/abs/2102.11954

[9] A. Blazogiannaki, "The evolving asymmetric threat of unmanned aircraft systems: A weapon of choice for non-state actors," NATO Integrated Air and Missile Defence Centre of Excellence (IAMD COE), Souda Air Base, Chania, Greece, c. 2024. [Online]. Available: https://iamd-coe.org/wp-content/uploads/2024/11/The-Evolving-Asymmetric-Threat-of-Unmanned-Aircraft-Systems-final.pdf

[10] F. Svanström, F. Alonso-Fernandez, and C. Englund, "A dataset for multi-sensor drone detection," *Data in Brief*, 2021, doi: 10.1016/j.dib.2021.107521. [Online]. Available: https://arxiv.org/abs/2111.01888 (data: https://github.com/DroneDetectionThesis/Drone-detection-dataset)

[11] Y. Cui, J. Nie, W. Yuan, F. Liu, Z. Jia, J. Xu, Z. Feng, and M.-S. Alouini, "Low-altitude wireless networks: The next horizon of wireless infrastructure," arXiv:2605.24368, May 2026, Sec. 4.2.3. [Online]. Available: https://arxiv.org/abs/2605.24368

[12] European Space Agency, "Copernicus DEM: Global and European digital elevation model (GLO-30)," Copernicus Data Space Ecosystem, doi: 10.5270/ESA-c5d3d65. [Online]. Available: https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

[13] OpenStreetMap contributors, "OpenStreetMap," extracts via Geofabrik, ODbL. [Online]. Available: https://download.geofabrik.de

[14] R. Peters, B. Dukai, S. Vitalis, J. van Liempt, and J. Stoter, "Automated 3D reconstruction of LoD2 and LoD1 models for all 10 million buildings of the Netherlands," *Photogramm. Eng. Remote Sens.*, vol. 88, no. 3, pp. 165–170, 2022, doi: 10.14358/PERS.21-00032R2. [Online]. Available: https://arxiv.org/abs/2201.01191

[15] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, Apr. 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.

[16] J. Zhao, J. Zhang, D. Li, and D. Wang, "Vision-based anti-UAV detection and tracking," *IEEE Trans. Intell. Transp. Syst.*, 2022; DUT Anti-UAV dataset. [Online]. Available: https://github.com/wangdongdut/DUT-Anti-UAV

[17] "UAVSwarm dataset," GitHub repository. [Online]. Available: https://github.com/UAVSwarm/UAVSwarm-dataset

[18] M. F. Al-Sa'd, M. S. Allahham, A. Mohamed, A. Al-Ali, T. Khattab, and A. Erbad, "DroneRF dataset: A dataset of drones for RF-based detection, classification, and identification," Mendeley Data, V1, 2019, doi: 10.17632/f4c2b4n755.1.

[19] Headquarters, Department of the Army, "Counter-unmanned aircraft system (C-UAS)," ATP 3-01.81, Washington, DC, USA, 11 Aug. 2023. [Online]. Available: https://armypubs.army.mil

[20] U.S. Department of Defense, "Fact sheet: Department of Defense strategy for countering unmanned systems," Dec. 5, 2024. [Online]. Available: https://www.suasnews.com/wp-content/uploads/2024/12/FACT-SHEET-STRATEGY-FOR-COUNTERING-UNMANNED-SYSTEMS.pdf

[21] J. Watling and J. Bronk, "Protecting the force from uncrewed aerial systems," Royal United Services Institute (RUSI), London, U.K., Occasional Paper, Oct. 15, 2024. [Online]. Available: https://rusi.org/explore-our-research/publications/occasional-papers/protecting-force-uncrewed-aerial-systems

[22] S. Pettyjohn and M. Campbell, "Countering the swarm: Protecting the joint force in the drone age," Center for a New American Security (CNAS), Washington, DC, USA, Sep. 10, 2025. [Online]. Available: https://www.cnas.org/publications/reports/countering-the-swarm

[23] Janes, "IDEF 2019: Aselsan's iHTAR counter-UAV system breaks cover," 2019. [Online]. Available: https://janes.com/osint-insights/defence-news/idef-2019-aselsans-ihtar-counter-uav-system-breaks-cover

[24] Armada International, "Meteksan completed delivery drone detection radars," 29 Jul. 2020. [Online]. Available: https://www.armadainternational.com/2020/07/meteksan-completed-delivery-drone-detection-radars/

[25] Anadolu Ajansı, "Drone tehdidini 'Kapan' durduracak" ('Kapan' will stop the drone threat), 3 Jul. 2018. [Online]. Available: https://www.aa.com.tr/tr/bilim-teknoloji/drone-tehdidini-kapan-durduracak/1193364

[26] Defence Turkey, "AVCI – Anti-drone system," 15 Aug. 2021. [Online]. Available: https://www.defenceturkey.com/tr/icerik/avci-anti-drone-system-4717

[27] Milliyet, "İHA tehditlerine karşı maliyeti etkin çözüm! TUNGA-X ilk kez SAHA EXPO 2026'da görücüye çıktı" (cost-effective solution against UAV threats: TUNGA-X shown for the first time at SAHA EXPO 2026), 6 May 2026. [Online]. Available: https://www.milliyet.com.tr/milliyet-tv/iha-tehditlerine-karsi-maliyeti-etkin-cozum-tunga-x-ilk-kez-saha-expo-2026da-gorucuye-cikti-video-7583403

[28] Milliyet, "Roketsan'dan, kamikaze dron tehdidine karşı lazer silahı" (Roketsan laser weapon against the kamikaze drone threat), 23 Sep. 2024. [Online]. Available: https://www.milliyet.com.tr/ekonomi/roketsandan-kamikaze-dron-tehdidine-karsi-lazer-silahi-7194840

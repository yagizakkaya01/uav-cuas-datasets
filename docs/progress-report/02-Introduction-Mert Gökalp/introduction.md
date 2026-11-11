# Introduction

**Owner:** Mert Gökalp · **Weight:** 15%

## Statement of the problem

### What

Small commercial drones are cheap, easy to buy and hard to see. Over the past decade they have gone from a hobbyist curiosity to a real security problem for airports, military bases and other critical sites. When one appears near such a site, the people protecting it have to answer three questions quickly: is it really a drone, how dangerous is it, and what should we do about it? This project tries to answer all three. A deep-learning detector recognises the drone in a camera image, and its Wi-Fi signal confirms its identity. The system then places it on a real terrain model of the protected site, estimates how threatening it is, and recommends a response that the operator can check against published doctrine.

### Why

The problem is no longer hypothetical. In December 2018 drone sightings closed London Gatwick for more than a day [15]. On 22 November 2025, civil and military flights at Eindhoven were halted for about two hours after drones were reported near the airfield [18], and an IISS study counted 144 drone incidents across 13 European countries between August 2024 and February 2026 [16]. In the United States, the FAA has collected more than 20,000 sighting reports since 2014 [2], and in 2026 NATO approved a multi-year, multi-billion-dollar counter-drone initiative [1].

Detecting these aircraft is hard. Small drones have radar cross-sections well below 0 dBsm, so radar alone often misses them [3], and studies of airport protection recommend combining several types of sensors rather than relying on one [17]. Detection, however, is only half of the job. Once a track appears, an operator still has to judge, usually within seconds, which assets are exposed, whether the terrain hides the drone's approach, and which procedure applies. Most counter-UAS products put their effort into the sensors and effectors: radar, RF, electro-optical and acoustic detection, and jamming or interception. As far as we can tell from public documentation, their command-and-control software fuses tracks and assigns effectors, but it does not explain why a track is dangerous in terms of the terrain, the protected assets and doctrine. Türkiye's national UAV traffic platform İHATTYS manages registered, cooperative drones [4]; a drone that does not announce itself is outside its scope by definition. This is the gap we want to address: an explainable layer between "a drone has been detected" and "this is what to do". The project does not build radar sensing or any means of neutralising a drone; it usesa camera and a 2.4 GHz Wi-Fi receiver for detection and concentrates on assessment and decision support. Terrain effects such as line of sight are computed on the terrain model of the pilot region, onto which the detections from the flat campus demo area are mapped.

### How

The system has five parts, each owned by one team member:

- A camera node detects the drone in an IP camera stream with a deep-learning detector.
- A 2.4 GHz Wi-Fi receiver confirms the drone's identity from its signal.
- A geospatial engine places the track on a terrain and building model of the site, spreads its risk over a grid while taking line of sight into account, and computes safe routes.
- A knowledge base uses retrieval-augmented generation [5] to find relevant passages in unclassified counter-UAS doctrine such as ATP 3-01.81 [14].
- A fusion and command-and-control layer combines the camera and Wi-Fi evidence into a single threat score. It shows the result on a web map with MIL-STD-2525 symbols [6], together with a recommendation that cites the document and page it is based on.

The whole system is built on real, openly available data instead of invented inputs: terrain models, OpenStreetMap, OpenSky air traffic and public drone datasets [7]–[12]. Every source is catalogued in the project repository [13].

The system will be demonstrated physically on campus. For ESC 491, after discussions with our supervisors, the setup has been deliberately kept small:

- One fixed PoE IP camera on a tripod watches an area of roughly 15 m × 17 m next to Academic Hall 1.
- All processing runs on a single laptop, and the language model is accessed through an API.
- A 3D-printed mock drone carrying an ESP32 transmitter plays the intruder.

The original multi-node design stays in the report as the way the system would scale, since each additional camera simply runs the same pipeline in parallel, but it will not be built in this course. Detections from the demo area will be shown on the terrain model of a pilot region. Four candidates (Eindhoven, Gatwick, Aalborg and Akrotiri/Chania) are being compared, and the final choice has not yet been made.

## Aim and objectives

**Aim:** To design and demonstrate a decision-support system that turns UAV detections into a live, explainable threat picture of a protected site and recommends a response the operator can verify.

**Objectives:**

1. Detect a single mock UAV in the camera stream in daylight and estimate its ground position from a known flight height, within a detection range and latency to be agreed with the supervisors.
2. Confirm the drone's presence from its Wi-Fi transmissions while filtering out other transmitters such as campus Wi-Fi and phones.
3. Build a terrain and infrastructure model of the selected pilot region from open data, and use it to compute line of sight, a risk grid and safe routes.
4. Retrieve relevant passages from unclassified counter-UAS doctrine and generate recommendations in which every statement cites its source document and page.
5. Fuse camera and Wi-Fi evidence into a single threat score that shows how it was calculated, and present tracks, alerts and recommendations on a web map with MIL-STD-2525 symbols, logging every operator decision.
6. Test the complete pipeline end to end, first on recorded data and then live in the demo area, against success criteria fixed in advance with the supervisors.


## References

[1] Army Recognition, "NATO approves $40 billion counter-drone initiative to defeat low-cost UAV threats," 2026. [Online]. Available: https://www.armyrecognition.com/news/aerospace-news/2026/nato-approves-40-billion-counter-drone-initiative-to-defeat-low-cost-uav-threats

[2] Federal Aviation Administration, "UAS Sightings Report." [Online]. Available: https://www.faa.gov/uas/resources/public_records/uas_sightings_report

[3] M. Ezuma, C. K. Anjinappa, M. Funderburk, and I. Guvenc, "Radar cross section based statistical recognition of UAVs at microwave frequencies," arXiv:2102.11954, 2021. [Online]. Available: https://arxiv.org/abs/2102.11954

[4] SAVX, "İHATTYS — İHA Takip ve Trafik Yönetim Sistemi (Türkiye's national UTM platform, SHT-İHA Article 21)," 2026. [Online]. Available: https://www.savx.com.tr/uttms

[5] P. Lewis et al., "Retrieval-augmented generation for knowledge-intensive NLP tasks," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2020.

[6] U.S. Department of Defense, "Joint Military Symbology," MIL-STD-2525D, 2014.

[7] European Space Agency, "Copernicus DEM: Global and European digital elevation model (GLO-30)," Copernicus Data Space Ecosystem, doi: 10.5270/ESA-c5d3d65. [Online]. Available: https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM

[8] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, Apr. 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.

[9] J. Zhao, J. Zhang, D. Li, and D. Wang, "Vision-based anti-UAV detection and tracking," *IEEE Trans. Intell. Transp. Syst.*, 2022; DUT Anti-UAV dataset. [Online]. Available: https://github.com/wangdongdut/DUT-Anti-UAV

[10] "UAVSwarm dataset," GitHub repository. [Online]. Available: https://github.com/UAVSwarm/UAVSwarm-dataset

[11] F. Svanström, F. Alonso-Fernandez, and C. Englund, "A dataset for multi-sensor drone detection," *Data in Brief*, 2021, doi: 10.1016/j.dib.2021.107521. [Online]. Available: https://arxiv.org/abs/2111.01888 (data: https://github.com/DroneDetectionThesis/Drone-detection-dataset)

[12] M. F. Al-Sa'd, M. S. Allahham, A. Mohamed, A. Al-Ali, T. Khattab, and A. Erbad, "DroneRF dataset: A dataset of drones for RF-based detection, classification, and identification," Mendeley Data, V1, 2019, doi: 10.17632/f4c2b4n755.1.

[13] Y. Akkaya et al., "uav-cuas-datasets: Real data sources for UAV threat mapping," GitHub repository, 2026. [Online]. Available: https://github.com/yagizakkaya01/uav-cuas-datasets

[14] Headquarters, Department of the Army, "Counter-unmanned aircraft system (C-UAS)," ATP 3-01.81, Washington, DC, USA, 11 Aug. 2023. [Online]. Available: https://armypubs.army.mil

[15] Office of the Sussex Police and Crime Commissioner, "Performance & Accountability Meeting," minutes, 18 Oct. 2019. [Online]. Available: https://www.sussex-pcc.gov.uk/media/4422/10-pam-minutes-18102019.pdf

[16] C. Edwards, R. Fox O'Loughlin, and L. Bearn, "Russia's UAV campaign over Europe," International Institute for Strategic Studies (IISS), London, U.K., Jul. 2026. [Online]. Available: https://www.astrid-online.it/static/upload/russ/russia-uav-campaign-over-europe.pdf

[17] G. Lykou, D. Moustakas, and D. Gritzalis, "Defending airports from UAS: A survey on cyber-attacks and counter-drone sensing technologies," *Sensors*, vol. 20, no. 12, Art. no. 3537, 2020, doi: 10.3390/s20123537.

[18] Al Jazeera, "Air traffic suspended at Netherlands airport after drone sightings," 22 Nov. 2025. [Online]. Available: https://www.aljazeera.com/news/2025/11/22/air-traffic-suspended-at-netherlands-airport-after-drone-sightings

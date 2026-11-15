# Research Method

**Owner:** Aydan Doğan · **Weight:** 10%

## 5.1 Selected method and reasons

The project follows a **design-oriented, iterative prototyping method** based on the Design Science Research Methodology (DSRM) [1], which treats building and evaluating an artefact as the research activity: identify the problem, define objectives, design and develop, demonstrate, evaluate and communicate.

This method was chosen because:

1. **The output is a working system.** The contribution is an explainable decision-support artefact, not a hypothesis test.
2. **The problem is multidisciplinary.** Vision, wireless communication, geospatial analysis, language models and interface design develop at different speeds; short iterations keep them aligned.
3. **Requirements change.** The hardware scope changed four times in one week (from four Jetson nodes to one IP camera) and the pilot region is still being chosen; iterations absorb such changes.
4. **Supervisor guidance.** The supervisors asked for a simple system where the idea matters more than a finished product, so a minimum working chain comes first.

A *simulation-only* study would give no physical evidence for detection, and a *field deployment* at a real airfield is not possible because of cost and permissions. The project therefore tests the sensing layers physically on campus and runs the decision layers on real pilot-region geodata.

**Data.** Every input comes from an open, citable source: national elevation models and OpenStreetMap for terrain, the OpenSky Network [2] for air traffic, and DUT Anti-UAV [3], UAVSwarm [4], Halmstad [5] and DroneRF [6] for training detection models; all are catalogued in the team repository [7]. Primary data are the team's own campus recordings of the mock drone with the matching 2.4 GHz Wi-Fi logs.

## 5.2 Implementation

Development runs in five phases, each ending with a demonstrable output:

**Table 5.1.** Development phases.

| Phase | Weeks | Output |
|---|---|---|
| P1 – Requirements and contracts | 1–3 | Hardware list, interface definitions, data downloaded |
| P2 – Independent prototypes | 4–6 | Each layer runs alone on mock data |
| P3 – End-to-end (desk) | 7–9 | Whole chain runs on recorded data |
| P4 – Hardware and field | 10–12 | Live single-camera detection on campus, shown on the map |
| P5 – Final | 13–14 | Report, presentation, demo v1 |

Each layer has one owner and exchanges data only through agreed messages, so everyone can work with mock data in parallel. The first version uses the simplest method at each step (YOLO detection, Kalman filter, weighted threat score, Gaussian risk grid, A\* routing, rule table with a retrieval-augmented explanation [8]); advanced methods are left for ESC 492. Campus tracks are mapped onto the pilot region with a similarity transform that scales distance by s = 100 and time by k = 10. The time scale is needed because scaling distance alone also scales speed: a mock drone carried at 1 m/s would move at 100 m/s on the pilot-region grid, and the time-to-reach feature of the threat score would lose its meaning; with k = 10 it moves at a realistic 10 m/s. Mapped distances are always reported as scaled, and demo accuracy figures (detection range, position error, latency) are reported at campus scale only. Work is reviewed and merged through pull requests, with a short weekly progress meeting.

## 5.3 Testing and validation

Testing moves from module tests on mock data, to desk integration with recorded video and Wi-Fi logs, to a live field test with the mock drone at known distances and height. Because a real airfield attack cannot be staged, the decision layers are also evaluated with Monte Carlo runs of synthetic tracks over the pilot-region grid.

**Table 5.2.** Evaluation metrics.

| Evaluated | Metric |
|---|---|
| Visual detection | Precision, recall, mAP@0.5; detection range; frames per second |
| Tracking | Position RMSE against the known path; track breaks |
| Wireless confirmation (2.4 GHz Wi-Fi) | Correct and false confirmations with other Wi-Fi devices present |
| Knowledge base | Recall@k, MRR; share of correctly cited answers |
| Whole chain | End-to-end latency; warning time; false alarms |

The success criterion for the field test follows from the requirements: the mock drone is detected anywhere in the ~15 m × 17 m demo area and shown on the map within 2 s (NFR-3), with the detector running at 10 FPS or more (NFR-2). This criterion is confirmed in writing with the supervisors before the field test, and threat levels are cross-checked against a published airport drone-risk framework [9].

## References

[1] K. Peffers, T. Tuunanen, M. A. Rothenberger, and S. Chatterjee, "A design science research methodology for information systems research," *J. Management Information Systems*, vol. 24, no. 3, pp. 45–77, 2007.
[2] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, Apr. 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.
[3] J. Zhao, J. Zhang, D. Li, and D. Wang, "Vision-based anti-UAV detection and tracking," *IEEE Trans. Intell. Transp. Syst.*, 2022; DUT Anti-UAV dataset. [Online]. Available: https://github.com/wangdongdut/DUT-Anti-UAV
[4] "UAVSwarm dataset," GitHub repository. [Online]. Available: https://github.com/UAVSwarm/UAVSwarm-dataset
[5] F. Svanström, F. Alonso-Fernandez, and C. Englund, "A dataset for multi-sensor drone detection," *Data in Brief*, 2021, doi: 10.1016/j.dib.2021.107521. [Online]. Available: https://arxiv.org/abs/2111.01888 (data: https://github.com/DroneDetectionThesis/Drone-detection-dataset)
[6] M. F. Al-Sa'd, M. S. Allahham, A. Mohamed, A. Al-Ali, T. Khattab, and A. Erbad, "DroneRF dataset: A dataset of drones for RF-based detection, classification, and identification," Mendeley Data, V1, 2019, doi: 10.17632/f4c2b4n755.1.
[7] Y. Akkaya et al., "uav-cuas-datasets: Real data sources for UAV threat mapping," GitHub repository, 2026. [Online]. Available: https://github.com/yagizakkaya01/uav-cuas-datasets
[8] P. Lewis et al., "Retrieval-augmented generation for knowledge-intensive NLP tasks," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2020.
[9] D. Pascarella, G. Gigante, A. Vozella, P. Bieber, T. Dubot, E. Martinavarro, G. Barraco, and G. Li Calzi, "A methodological framework for the risk assessment of drone intrusions in airports," *Aerospace*, vol. 9, no. 12, Art. no. 747, 2022, doi: 10.3390/aerospace9120747.

# System Design

**Owner:** Aydan Doğan · **Weight:** 10%

## 6.1 Conceptual design

The system protects a critical site, such as an airfield, against small non-cooperative UAVs. A sensor node detects a drone, the system places it on a map of the site, estimates its threat level and recommends a response with a cited doctrine passage. The **operator** always makes the final decision; the **system administrator** (the team) configures the sensor and the pilot region. External systems are open geodata, the OpenSky Network [1] and a language-model API (see the use case diagram, Figure 4.1).

The proposed system consists of five interconnected layers, as presented in Table 6.1. Each layer performs a specific function and produces outputs that support the overall threat assessment and decision-support process.

**Table 6.1.** System layers.

| Layer | Question it answers | Output |
|---|---|---|
| 1. Sensing and detection | Is there a drone, and where? | Tracks (camera), confirmation of the drone's 2.4 GHz Wi-Fi signal |
| 2. Knowledge base | What does doctrine say? | Cited doctrine passages |
| 3. Geospatial risk | Which areas are exposed? | Risk grid, line of sight, safe route |
| 4. Fusion and threat assessment | How dangerous is it? | Threat score and level |
| 5. Decision support and C2 | What should the operator do? | MIL-STD-2525 [2] map, alert, cited recommendation |

**Design principles:** every recommendation cites its source and the language model only explains a rule-based decision; the operator accepts or overrides every recommendation and nothing is acted on automatically; all data are open and citable; layers communicate only through defined messages; the design scales by adding cameras that run the same process.

**Main design decisions** (agreed with the supervisors to keep the system simple and low-cost): one fixed PoE IP camera instead of four Jetson nodes; all processing on a team laptop (RTX 4070) instead of edge boards; the language model through an API instead of locally; a 3D-printed mock drone with an ESP32 transmitter instead of a real drone; a standard 2.4 GHz Wi-Fi receiver used only to confirm that the mock drone's signal is present, not to locate or identify it; ground position from one camera and a known flight height. The ESC 491 demo covers one drone, daytime, clear weather and a ~15 m × 17 m geofenced flight zone.

## 6.2 Preliminary design

The hardware configuration of the proposed system is illustrated in Figure 6.1. A Hikvision DS-2CD1643G2-LIZSU camera on a tripod sends video and receives power over a ~30 m Cat6 cable through a PoE injector to the laptop (RTSP, 2560 × 1440 at 20 fps). An ESP32 receiver connects over USB; the mock drone carries a second ESP32 and a power bank. Total procurement cost is ₺10,088.

![Figure 6.1 – Deployment diagram](./deployment-diagram.jpeg)

**Figure 6.1.** Hardware deployment diagram.

The software subsystems of the proposed system operate on a single laptop. Table 6.2 presents the main subsystems, their outputs, and the team members responsible for their development.

**Table 6.2.** Software subsystems.

| Subsystem | Output | Owner |
|---|---|---|
| Visual detection and tracking (YOLO on CUDA) | Track ID, ground position | Aydan Doğan |
| Wireless confirmation (2.4 GHz Wi-Fi; ESP32 sniffer) | Confirmed / not confirmed | Adil Mert İş |
| Risk grid and routing (PostGIS, line of sight, A\*) | Risk grid, safe route | Yaren Duyan |
| Knowledge base (RAG [3], LLM API) | Cited explanation | Yağız Akkaya |
| Fusion, threat score, C2 interface (Leaflet, milsymbol.js) | Threat level, alert, decision log | Mert Gökalp |

Figure 6.2 illustrates the processing flow of the proposed system. Each frame is checked for a UAV; a detected drone's track and ground position are updated and checked against the geofence. A drone inside the geofence is marked as detected; in parallel the ESP32 receiver confirms or does not confirm the drone's 2.4 GHz Wi-Fi signal, and the position is mapped onto the pilot region with a scaled transformation. The camera and Wi-Fi evidence are then fused into a threat score, and the risk is propagated on the grid. Below the alert level only the map symbol is updated; above it, a safe route for a response team or an evacuation path is planned, doctrine is retrieved and a cited recommendation is shown to the operator, whose decision or override is logged.

![Figure 6.2 – Activity diagram](./activity-diagram.png)

**Figure 6.2.** System activity diagram.

ESC 492 extends this structure with more cameras, fine-tuning on field recordings, swarm tracking and OpenSky anomaly detection.

## References

[1] M. Schäfer, M. Strohmeier, V. Lenders, I. Martinovic, and M. Wilhelm, "Bringing up OpenSky: A large-scale ADS-B sensor network for research," in *Proc. 13th Int. Symp. Inf. Process. Sensor Netw. (IPSN)*, Berlin, Germany, Apr. 2014, pp. 83–94, doi: 10.1109/IPSN.2014.6846743.
[2] U.S. Department of Defense, "Joint Military Symbology," MIL-STD-2525D, 2014.
[3] P. Lewis et al., "Retrieval-augmented generation for knowledge-intensive NLP tasks," in *Proc. Advances in Neural Information Processing Systems (NeurIPS)*, 2020.

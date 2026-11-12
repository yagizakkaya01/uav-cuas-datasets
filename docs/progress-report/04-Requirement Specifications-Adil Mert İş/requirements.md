# Requirement Specifications

**Owner:** Adil Mert İş · **Weight:** 20%

> Guideline: System requirements specification: functional requirements,
> non-functional requirements, domain requirements.

<!-- Give each requirement an ID (FR-1, NFR-1, DR-1) so the design and test
plan can refer to it. -->

## Functional requirements

| ID | Requirement |
| :--- | :--- |
| FR-1 | The ESP32 receiver shall receive 2.4 GHz signals from the mock drone’s transmitter |
| FR-2 | The IP camera shall send video frames to the main computer |
| FR-3 | The system shall use a YOLO model to detect the target drone |
| FR-4 | The system shall estimate the drone’s position on a map and track its movement |
| FR-5 | The system shall compute a threat score by combining visual detections and wi-fi signals |
| FR-6 | The system shall map risk zones based on line of sight and terrain |
| FR-7 | The system shall suggest safe flight paths to avoid threat zones |
| FR-8 | The system shall use an LLM API to retrieve doctrine documents and suggest responses |
| FR-9 | The system shall display a real-time tactical threat map on the dashboard |
| FR-10 | The system shall allow the operator to evaluate alerts and ask why a response was suggested |
| FR-11 | The system shall allow the operator to replay a recorded mission scenario |
| FR-12 | The system shall allow administrators to configure sensor parameters, geofence, and map layers |
| FR-13 | The system shall load air-traffic data by using OpenSky Network API |

## Non-functional requirements


| ID | Requirement |
| :--- | :--- |
| NFR-1 | The system shall continue operating even if the camera or receiver module loses connection |
| NFR-2 | The YOLO model shall process video frames at least 10 FPS |
| NFR-3 | The system shall show all threats on the map within 2 seconds |
| NFR-4 | The LLM API shall generate response advice within 15 seconds |
| NFR-5 | The web dashboard shall load within 5 seconds |
| NFR-6 | The YOLO model shall detect UAVs with at least 70% accuracy |

## Domain requirements

| ID | Requirement |
|---|---|
| DR-1 | TODO |

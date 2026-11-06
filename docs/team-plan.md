# Task Distribution and Semester Plan

*First plan, 15 October 2026. Kept as written at the time: hardware details (Jetson, local LLM, multi-node masts) were later replaced by the single IP camera setup in [`hardware/`](./hardware/).*

## Summary

The team has 5 members (4 Computer Engineering, 1 Electrical & Electronics Engineering) and the system has 5 layers. Everyone owns one **primary layer** and also takes a **secondary task** that peaks when their primary work is quiet. That way, whenever one person's work slows down, the other picks up, and nobody sits idle during the semester.

The key to balance is the **interface contracts** written in the first weeks (track message, risk grid API, RAG API). With these, everyone can start with mock data from week one, and nobody waits for someone else's module.

Assumption: ESC 491 is a 14-week semester, week 1 is the end of September, and today is around week 3–4. If the calendar differs, the phases shift.

## Who owns which layer

Primary layers match the roles table in the main README; the secondary tasks are new, with the weeks they become active.

| Person | Primary (owned layer) | Secondary (task during quiet weeks) | Primary busy weeks | Secondary busy weeks |
| --- | --- | --- | --- | --- |
| Adil Mert İş (EEE) | Sensor node hardware + Wi-Fi/RF control-link detection (Layer 1, sensor part) | Detection range / link budget model and RCS justification (Layer 4); field test lead | 4–12 | 1–3 and 11–14 |
| Yaren Duyan | Terrain + OSM model, grid risk propagation, line of sight, A\*/Dijkstra routing (Layer 1 map + Layer 3) | Validating the risk model with FAA/ACLED records, performance tests; layer data for the C2 map | 1–9 | 9–14 |
| Aydan Doğan | Camera-based edge-AI detection and swarm tracking (Layer 1, vision part) | TensorRT setup on the Jetson with the EEE member; recording and labelling our own field dataset | 3–10 | 10–14 |
| Yağız Akkaya | Doctrine knowledge base, RAG + local LLM, mandatory citations (Layer 2) | Test scenarios and evaluation metrics; report editor; explanation texts in the interface | 1–9 | 8–14 |
| Mert Gökalp | Fusion, threat score, recommendation engine, C2 web interface + MIL-STD-2525 symbols (Layers 4 + 5) | System architecture, interface contracts and mock data simulator; integration lead | 6–14 | 1–5 |

## Where idle time could occur

Because the layers are not busy at the same time, without precautions two people would be idle at the start and one at the end of the semester.

- **Mert (fusion/C2) is idle at the start**, because this layer needs the outputs of all the others. Precaution: in the first 5 weeks Mert writes the architecture, message schemas and a mock track simulator, and builds the interface skeleton on this mock data.
- **Adil Mert (EEE) waits for hardware at the start** (Jetson/Pi, camera, Wi-Fi adapter, masts, 3D print). Precaution: until the hardware arrives, Adil Mert develops RF detection on a desk with the DroneRF dataset and builds the link budget / range model.
- **Yağız (RAG) finishes early**, because the knowledge base does not depend on other layers. Precaution: from week 8, test scenarios, evaluation and report editing come first.
- **Yaren and Aydan are very busy in the middle** and lighter at the end. Precaution: at the end they take on secondary tasks such as validation, field data and edge setup.

## 14-week schedule: everyone's work in each phase

The semester has 5 phases, and every cell is that person's concrete work in that phase; there are no empty cells. Each phase ends with a working output.

| Phase | Adil Mert (EEE) | Yaren (map + risk) | Aydan (visual detection) | Yağız (knowledge base) | Mert (fusion + C2) |
| --- | --- | --- | --- | --- | --- |
| **P1 · Weeks 1–3** Requirements and contracts | Hardware list and order; link budget and detection range calculation; define RF message fields | Choose campus test area; load AW3D30 + OSM into PostGIS | Download and convert DUT Anti-UAV, UAVSwarm, Halmstad; YOLO baseline | Collect doctrine corpus (ATP 3-01.81, RAND, CNAS…), page-numbered chunks | System architecture; track / risk / RAG JSON schemas; repo, Docker, GitHub project board |
| **P2 · Weeks 4–6** Independent prototypes | RF detection model with DroneRF; first Pi/ESP32 monitor-mode test | Grid risk propagation + line of sight (terrain masking) | YOLO training and mAP measurement | RAG with citations using FAISS/Qdrant + Ollama | Mock track simulator; Leaflet map + milsymbol skeleton |
| **P3 · Weeks 7–9** First end-to-end (desk) | Single node with camera + Wi-Fi; publishes RF track messages | A\*/Dijkstra safe route; risk API | Multi-target / swarm tracking; track messages from recorded video | RAG API; first test scenarios (from week 8) | Fusion + threat score; integrate all modules with recorded data |
| **P4 · Weeks 10–12** On hardware and in the field | 2–3 nodes, masts, power; 3D-printed drone mock-up + transmitter; field test lead | Validate risk model with FAA/ACLED; performance | TensorRT on the Jetson with the EEE member; label field recordings | Scenario-based evaluation (accuracy, citation proof); explanation texts | Recommendation engine; interface with live data; latency measurement |
| **P5 · Weeks 13–14** Final | Hardware and field test chapter; demo setup | Algorithm chapter + map figures | Detection results chapter | Report editing, references, presentation flow | Architecture chapter; demo scenario and live presentation |

If the ESC 491 report ends with the design report, the implementation part of P4 and P5 moves to ESC 492; the distribution stays the same.

## Deliverables and balance rules

At the end of each phase there is an output everyone can show; if someone cannot show it, the work split is adjusted that week.

| Week | Deliverable | Owner |
| --- | --- | --- |
| 3 | Interface contracts (JSON schemas) and hardware order | Mert, Adil Mert |
| 6 | Every layer runs on its own with mock data | Everyone |
| 8 | Interim report / progress presentation | Yağız (editor), everyone their own chapter |
| 9 | End-to-end demo with recorded data (desk) | Mert |
| 12 | Live detection with a single node in the field, shown on the map | Adil Mert, Aydan |
| 14 | Final report, presentation, demo v1 | Everyone |

- **Weekly 15-minute meeting:** everyone answers "what am I showing working this week".
- **Every task is a GitHub issue:** with an owner and a week label; if someone has no open task on the board, they pull from their secondary list.
- **Rotating integration duty:** each week one person checks that the main branch works, so the integration load does not fall on Mert alone.
- **Report writing is continuous:** everyone writes their chapter as one page at the end of each phase; nothing piles up in the last two weeks.
- **The EEE member is not alone:** for hardware work, a Computer Engineering member is paired in each phase (P1–P2 Mert, P3–P5 Aydan), because one EEE member cannot carry the whole physical demo.

## Continuing in ESC 492

The same primary ownerships are kept; in the second semester the focus moves to the field and to refinement.

- **Adil Mert (EEE):** more nodes, rough direction/position from RF, power and durability.
- **Yaren:** risk map with multi-node field of view, dynamic re-routing.
- **Aydan:** fine-tuning with field data, swarm scenarios, OpenSky anomaly detection.
- **Yağız:** measuring RAG quality, final report editing, user testing.
- **Mert:** multi-sensor fusion, polishing the operator interface, final demo scenario.

# Minimum Hardware Scope: One IP Camera, One Node

*ESC 491/492 · 2 November 2026*

> **Note:** This document is the source of the scope-narrowing assumptions and the architecture. The final item and price list sent to and accepted by the supervisors is in [`README.md`](./README.md); where items or prices differ, that list applies.

Dr. Meryem Erbilek said there is no budget figure and the list should be kept as simple and cheap as possible. So, of Dr. Muhammad Sohail's three camera options, the Raspberry Pi-free IP camera was chosen, with a single camera and a single node. The scope was narrowed with the assumptions below.

## Architecture

```
[IP camera] ──Cat6 ~30 m──► [PoE injector] ──► Laptop (detection, risk engine, C2, LLM API)
                                                  ▲
                         [ESP32 receiver] ──USB───┘   (next to the laptop, at the edge of the area)
```

- The camera gets power and sends video over a single cable. Video goes directly to the laptop. No Raspberry Pi and no switch are needed.
- The ESP32 receiver sits next to the laptop and both gets power and sends data over USB. Its job is to confirm the drone's presence and identity, not to locate it, so placing it at the edge of the area is enough.

## Assumptions that narrow the project (for the report and the request form)

1. **One camera, one node.** The system is demonstrated with a single sensor node. The multi-node architecture is described in the report as a scalable design but is not built within the graduation project (Dr. Sohail's reasoning: all nodes do the same job).
   - **The camera is fixed and sees a defined area.** "Motorized lens" only means the focal length is adjusted by a motor between 2.8 and 12 mm; the camera does not rotate (it is not PTZ). Scaling assumption (Dr. Sohail): if one camera covers ~60°, 360° coverage needs 6 cameras. This is stated in the report, but 6 cameras are not purchased.
2. **Position from one camera with a known flight height.** No triangulation. The drone is assumed to fly at a fixed, known height (e.g. 3 m). Its position on the map is estimated by projecting its image position to the ground using this height.
3. **The flight zone is limited to the camera's field of view.** The drone flies at most ~15–20 m from the camera, within the angle the lens is set to. This limit is enforced in software with a geofence.
4. **One target, daytime, clear weather.** One drone at a time. Night, rain and fog are out of scope.
5. **The RF side only confirms.** One ESP32 confirms the drone's presence and identity (known MAC); it does not give position. Other transmissions such as campus Wi-Fi and phones are filtered out by MAC (Dr. Sohail's interference note).
6. **Processing is central.** Detection, the risk engine and the interface run on the laptop. The language model is used through an API for the demo.
7. **The success criterion is defined in advance.** For example, a target such as "detection up to X m from the camera within Y seconds" is agreed in writing with the supervisors. The demo is evaluated against this target. Field test videos are kept as backup evidence.

## Dr. Sohail's guidance (2 November)

A fully working product is not expected in a graduation project; the idea is what is presented. If it works with one camera, it works with three (three parallel processes). Keeping it simple is better. Do not expect the university to buy everything; it is good if it buys the main items. **Main item priority:** camera, PoE injector, cable, ESP32 receiver. Tripod, accessories, extension cord and power bank can come from the team or be borrowed if needed.

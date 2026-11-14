# Hardware & Physical Demo

> **Accepted procurement list (Nov 2026).** This is the list sent to the supervisors (Meryem Erbilek, Muhammad Sohail) for the ESC 491 hardware request and accepted by them. Total **₺10,088**.

## Demo setup at a glance

- **Area:** outdoor, the square area at the east end of the strip north of Academic Hall 1, METU NCC. Approx. **15 m × 17 m (~260 m²)**, estimated from the Google Maps scale bar; to be confirmed on site with a tape measure.
- **Single node, single camera:** one fixed PoE IP camera (motorized varifocal 2.8–12 mm; the lens zooms, the camera does not rotate). No Jetson, no Raspberry Pi.
- **All processing on a team laptop** (RTX 4070): YOLO detection, risk engine, C2 interface. The LLM is used via an API for the demo (no local LLM).
- **RF confirmation:** two ESP32 boards. One is a transmitter on a **mock drone**, one is a receiver connected to the laptop over USB. The receiver confirms the drone's presence by detecting a change from the normal Wi-Fi background of the area; it does not localise it. MAC addresses are not used anywhere in the system (decision of 12 Nov 2026).

```
[IP camera] ──Cat6 ~30 m──► [PoE injector] ──patch──► Laptop (detection, risk engine, C2, LLM API)
                                                        ▲
                       [ESP32 receiver] ──USB───────────┘
[Mock drone + ESP32 transmitter + power bank]  ~~ 2.4 GHz ~~►  ESP32 receiver
```

## Procurement list

| # | Component | Unit price | Qty | Total | Link |
|---:|---|---:|---:|---:|---|
| 1 | Hikvision DS-2CD1643G2-LIZSU, 4 MP, 2.8–12 mm motorized lens | ₺5,200 | 1 | ₺5,200 | [smartlink.com.tr](https://www.smartlink.com.tr/urun/hikvision-ds-2cd1643g2-lizsu-4-mp-smart-light-2-8-12-mm-motorize-lensli-ir-bullet-ip-kamera) |
| 2 | ESP32 development board (1 receiver, 1 transmitter on mock drone) | ₺420 | 2 | ₺840 | [robo90](https://www.robo90.com/esp32-wroom-32-wifi-ve-bluetooth-gelistirme-karti) |
| 3 | USB data cable for ESP32 | ₺48 | 1 | ₺48 | [robo90](https://www.robo90.com/mikro-usb-guc-ve-data-kablosu-30cm) |
| 4 | 10,000 mAh USB power bank (for mock drone) | ₺679 | 1 | ₺679 | [vatanbilgisayar](https://www.vatanbilgisayar.com/powerboost-lite-100b-10000mah-10w-type-c-out-powerbank-siyah.html) |
| 5 | Cat6 outdoor Ethernet cable, ~30 m (camera to injector) | ₺750 | 1 | ₺750 | [hepsiburada](https://www.hepsiburada.com/cat6-ethernet-internet-lan-network-patch-kablo-fabrikasyon-30-metre-pm-HBC000006AD5O) |
| 6 | Cat6 patch cable, 1–2 m (injector to laptop) | ₺170 | 1 | ₺170 | [trendyol](https://www.trendyol.com/tek-is/cat6-network-internet-ethernet-bilgisayar-kablosu-rj45-rj45-2-metre-patch-kablo-p-307098510) |
| 7 | PoE injector (IEEE 802.3af, gigabit), main camera power | ₺780 | 1 | ₺780 | [trendyol](https://www.trendyol.com/tenda/poe30g-at-30-watt-10-100-1000-gigabit-aktif-poe-enjektoru-802-3-af-at-p-1226210855) |
| 8 | 12 V DC 1 A power adapter, 5.5 mm plug (backup camera power) | ₺250 | 1 | ₺250 | [trendyol](https://www.trendyol.com/robotikdepo/12v-1a-dc-adaptor-5-5x2-1mm-jak-uclu-p-1176662876) |
| 9 | Tripod or fixed mounting bracket | ₺1,099.90 | 1 | ₺1,099.90 | [trendyol](https://www.trendyol.com/farway/profesyonel-aluminyum-tripod-360-ayarlanilabilir-panoramik-baslik-su-terazili-telefon-tutucu-175cm-p-952832161) |
| 10 | Mounting and wiring accessories (junction box + cable ties) | ₺271 | 1 set | ₺271 | [box](https://www.trendyol.com/powermaster/thor-tkb-1111-dis-mekan-kamera-montaj-kutusu-kare-buat-taban-p-1015831011) · [cable ties](https://www.trendyol.com/faem/3-6x150-200-250-300-mm-kablo-bagi-set-plastik-kelepce-cirt-kelepce-beyaz-100-adet-p-974399224) |
| | **Total** | | | **₺10,088** | |

Prices checked on the linked pages on 2 Nov 2026 and may change.

**Provided by the team (not requested):** laptop (USB–Ethernet adapter if it has no Ethernet port), drone / mock drone, 3D printer, tape measure. **Also to request on the form:** permission to use the area, permission to fly outdoors, access to a power outlet.

### Assumptions submitted with the list

- Central processing happens on a laptop; otherwise a more capable and expensive Raspberry Pi would be needed.
- Heat/temperature management is not included yet.
- Single-node system: a 3-node system is too expensive for a graduation project, and since all nodes do the same job, testing with one node is enough.
- One ESP32 receiver is enough for the test area regardless of the number of nodes.
- Mock drone instead of a real drone, because a real drone may not use 2.4 GHz Wi-Fi; SDR is the alternative but too expensive.
- The critical test is detection in the presence of other Wi-Fi transmitters (campus Wi-Fi, phones): either test away from interference or filter the target (e.g. by MAC). *Superseded on 12 Nov 2026: MAC addresses are not used; the receiver compares against a recorded baseline of the normal Wi-Fi background instead.*
- Extra items may be needed later; this set is enough to start.

### Known follow-ups (not yet reflected in the accepted list)

- **USB cable quantity:** two ESP32 boards need two USB cables (one to the laptop, one to the power bank); the list has 1 (+₺48).
- **Item 5 link:** the Hepsiburada 30 m cable page returned "page not found" on 2 Nov; an alternative is a [30 m outdoor Cat6 cable on Trendyol](https://www.trendyol.com/vwin/30-metre-cat6-dis-mekan-internet-ethernet-kablo-rj45-utp-patch-yuksek-hiz-2-katmanli-kablo-p-851448037) (₺489 on 2 Nov).
- **Power bank:** may be borrowed instead of bought (supervisor's note).
- **Extension cord + power strip:** needed for the PoE injector and laptop if no outlet is next to the setup; bring from the team if possible.
- **Tripod mount:** the bullet camera may not have a 1/4" tripod thread; a 3D-printed adapter can be made after the camera arrives.

## Scope-narrowing assumptions

The demo is deliberately narrowed (single camera, fixed known flight height for localisation, flight zone limited to ~15–20 m within the camera's field of view, single target, daytime, RF for confirmation only, success criterion agreed with supervisors in advance). Full list and rationale: [single-camera-scope.md](./single-camera-scope.md). For the report: with a ~60° field of view, 360° coverage would need 6 cameras; this is stated as the scaling path, not purchased.

## History of the hardware decision

| Date | Change |
|---|---|
| 28 Oct 2026 | First request: 4 Jetson-based nodes along a ~67 × 12 m strip north of Academic Hall 1. |
| 28 Oct 2026 | 1 Jetson Orin Nano + 4 PoE IP cameras + PoE switch; GPU workstation dropped (laptop used for training). |
| 31 Oct 2026 | Demo area moved to the ~15 × 17 m square at the east end of the strip; 3 cameras. |
| 2 Nov 2026 | Merged with Dr. Sohail's single-node list (Pi 4 + Pi Camera); Jetson dropped, processing on laptop. |
| 2 Nov 2026 | Dr. Sohail's camera options: Pi Cam 3 (~8–10 m), Pi HQ + 16 mm, or Pi-less IP camera. IP camera chosen. Dr. Erbilek: no budget figure, keep it minimal → single camera, single node. |
| 2 Nov 2026 | Mock drone + ESP32 transmitter chosen over a real Tello-class drone. List accepted ("budget looks fine"). |

# Layer 5 — Visualization: Military Symbology Standards

![Sources](https://img.shields.io/badge/sources-1-informational)

The C2 map view needs standards-compliant symbology, not custom icons — this is what makes the demo read as a credible tactical picture rather than a generic dashboard.

> 🇹🇷 **Kısaca:** Harita üzerinde dost, düşman ve bilinmeyen unsurlar, NATO'nun kullandığı standart askeri sembollerle gösterilir. Bu sembolleri çizmek için ücretsiz ve açık kaynaklı bir kütüphane kullanılır.

[← Back to README](../README.md)

---

| Source | Status | What to search for | Notes |
|---|:---:|---|---|
| **[milsymbol.js](https://github.com/spatialillusions/milsymbol)** | 🟢 | `npm install milsymbol` — see repo docs for **Symbol Identification Code (SIDC)** generation | MIT license — zero licensing risk for academic use. Pure JS, zero dependencies, renders MIL-STD-2525 (C/D/E) and STANAG APP-6 (B/D/E) as SVG/Canvas. Integrates with Leaflet, OpenLayers, Cesium. Generate your own SIDC set (friend/hostile/unknown UAV symbols) directly from the documentation. |

---

## Add a New Source

```markdown
| **[Name](link)** | 🟢/🟡/🔴 | what to search for | notes |
```

[← Layer 4](./04-radar-cross-section-justification.md) · [Back to README](../README.md)

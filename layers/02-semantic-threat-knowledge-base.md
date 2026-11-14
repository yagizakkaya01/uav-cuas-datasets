# Layer 2 — Semantic Threat Knowledge Base (Doctrine / TTP)

![Sources](https://img.shields.io/badge/sources-10-informational)

This layer populates a Retrieval-Augmented-Generation (RAG) vector database with **unclassified, publicly readable doctrine and analysis** — the material the system draws on to answer "what is this threat and what procedure applies," with citations back to real documents.

> 🇹🇷 **Kısaca:** Sistemin "bilgi bankası". Dron tehditlerine karşı nasıl davranılacağını anlatan, herkese açık resmi askeri belgeler ve uzman analiz raporlarından oluşur. Sistem bir tehdit hakkında öneri verirken bu belgelere dayanır ve kaynağını gösterir.

[← Back to README](../README.md)

---

| Source | Status | What to search for | What you'll extract |
|---|:---:|---|---|
| **[ATP 3-01.81 — US Army C-UAS Doctrine](https://armypubs.army.mil)** | 🟢 | Search directly for **"ATP 3-01.81"** (Dec 2023 edition) | Threat classification table (UAS Group 1–3), layered-defense concept, detect–identify–defeat cycle |
| **DoD Strategy for Countering Unmanned Systems (2024)** | 🟢 | defense.gov — **"DoD counter-UAS strategy 2024 fact sheet"** | The 5 "strategic ways" — top-level doctrine principles for RAG answers |
| **[CRS Report R48477](https://www.congress.gov)** / **[EveryCRSReport mirror](https://www.everycrsreport.com)** | 🟢 | Search **"R48477"** directly (EveryCRSReport is faster, not paywalled) | C-UAS program summary table, terminology glossary |
| **[RAND reports](https://www.rand.org)** | 🟢 | **"RAND counter-UAS military installation"** or **"counter-drone"**, filtered 2023–2026 | Free PDF, no registration |
| **[CNAS — "Countering the Swarm"](https://www.cnas.org)** | 🟢 | Search the title directly | Swarm-threat TTPs — swarm handling is ESC 492 scope |
| **[RUSI publications](https://www.rusi.org)** | 🟡 | **"drone warfare Ukraine"**, **"counter-UAS tactics"**; prioritize Jack Watling & Nick Reynolds's tactical-development series | Commentary pieces are free; some Occasional Papers may require registration |
| **[ISW daily reports](https://www.understandingwar.org)** | 🟢 | "Russian Offensive Campaign Assessment" — use the site search for "drone"/"UAV" paragraphs, not whole reports | Current TTP evolution, frequently updated |
| **NATO "Drone Edge" / Project Flytrap releases** | 🟢 | nato.int Newsroom — **"Drone Edge"**, **"Project Flytrap"** | Short press releases — use as "current context" layer, not deep doctrine |

## Airport-Domain Response Procedures

Added 12 Nov 2026. The decision rules recommend airport actions (suspend runway operations, notify ATC), which land-force doctrine such as ATP 3-01.81 does not cover. These two documents supply the airport side.

| Source | Status | What to search for | What you'll extract |
|---|:---:|---|---|
| **[IATA and partners — Unauthorized UA in the Vicinity of Airports: Guidance Material](https://www.iata.org/contentassets/fb1df0e634454acc9207418a5d1d636b/unauthorized-ua-guidance-material.pdf)** (ICAO hosts v1.0 of 5 Dec 2022 as [*Response to Unauthorized UA in the Vicinity of Aerodrome*](https://www2023.icao.int/safety/UA/Documents/Response%20to%20Unauthorized%20UA%20in%20the%20Vicinity%20of%20Aerodrome.pdf)) | 🟡 | Direct PDF links | Event classification into Low / Medium / High impact from parameters such as intent, size, proximity, altitude, trajectory and payload; weighted risk assessment matrix (Appendix 1); response per impact level and recovery of operations (chapter 6). Basis for the threat levels and the action table. No licence statement found: use locally and cite, do not redistribute. Check chapter and page numbers against the PDF before citing; the two copies may be different editions. |
| **[EASA — Drone Incident Management at Aerodromes, Part 1](https://www.easa.europa.eu/sites/default/files/dfu/drone_incident_management_at_aerodromes_part1_website_suitable.pdf)** (8 Mar 2021) | 🟢 | Direct PDF link | European regulatory context, categories of offenders, phases of a drone incident. Only Part 1 is public; Parts 2 and 3 (guidance, threat zones and ATC response) are restricted to aviation actors and authorities. |

---

## Practical Ingestion Note

Embed documents **chunked** (paragraph/section level), not as raw whole PDFs — retrieval quality drops sharply on whole-document embeddings. Attach source + page-number metadata to every chunk so the system can cite its answers (this directly satisfies the "zero-hallucination, forced citation" requirement in the RAG design).

---

## Add a New Source

```markdown
| **[Name](link)** | 🟢/🟡/🔴 | what to search for | what you'll extract |
```

[← Layer 1](./01-geospatial-sensor-data.md) · [Back to README](../README.md) · [Next: Layer 3 →](./03-algorithm-validation-literature.md)

# Layer 2 — Semantic Threat Knowledge Base (Doctrine / TTP)

![Sources](https://img.shields.io/badge/sources-8-informational)

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
| **[CNAS — "Countering the Swarm"](https://www.cnas.org)** | 🟢 | Search the title directly | Swarm-threat TTPs — doctrinal basis for the DBSCAN clustering module |
| **[RUSI publications](https://www.rusi.org)** | 🟡 | **"drone warfare Ukraine"**, **"counter-UAS tactics"**; prioritize Jack Watling & Nick Reynolds's tactical-development series | Commentary pieces are free; some Occasional Papers may require registration |
| **[ISW daily reports](https://www.understandingwar.org)** | 🟢 | "Russian Offensive Campaign Assessment" — use the site search for "drone"/"UAV" paragraphs, not whole reports | Current TTP evolution, frequently updated |
| **NATO "Drone Edge" / Project Flytrap releases** | 🟢 | nato.int Newsroom — **"Drone Edge"**, **"Project Flytrap"** | Short press releases — use as "current context" layer, not deep doctrine |

---

## Practical Ingestion Note

Embed documents **chunked** (paragraph/section level), not as raw whole PDFs — retrieval quality drops sharply on whole-document embeddings. Attach source + page-number metadata to every chunk so the system can cite its answers (this directly satisfies the "zero-hallucination, forced citation" requirement in the RAG design).

---

## Add a New Source

```markdown
| **[Name](link)** | 🟢/🟡/🔴 | what to search for | what you'll extract |
```

[← Layer 1](./01-geospatial-sensor-data.md) · [Back to README](../README.md) · [Next: Layer 3 →](./03-algorithm-validation-literature.md)

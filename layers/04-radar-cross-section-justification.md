# Layer 4 — Fusion & C2 Decision Layer: Radar Cross-Section Justification

![Sources](https://img.shields.io/badge/sources-3-informational)

This layer needs a quantitative answer to one question: **why does the architecture fuse EO/IR + semantic reasoning instead of relying on radar alone?** The measured radar cross-section (RCS) literature below provides real numbers, not intuition.

[← Back to README](../README.md)

---

| Source | Status | What to search for | Key figures to cite |
|---|:---:|---|---|
| **[Semkin et al. — arXiv 2102.11954](https://arxiv.org/abs/2102.11954)** | 🟢 | Direct arXiv ID | Measured RCS by drone model at 15/25 GHz (DJI Matrice, Mavic, Phantom, etc.) — mostly **−12 to −17 dBsm** |
| **[Semkin et al. — arXiv 1911.05926](https://arxiv.org/abs/1911.05926)** | 🟢 | Direct arXiv ID | Companion measurement methodology paper |
| **[UK CAA / survey — arXiv 2605.24368](https://arxiv.org/abs/2605.24368)** | 🟢 | Direct arXiv ID | **The single strongest citable line for the fusion argument:** small drone RCS as low as **−23 dBsm**, "could not be reliably tracked beyond 500 m using standard airport-surveillance radar." |

---

## Why this matters for the architecture

> Small consumer/military-style drones present RCS values well below 0 dBsm — an order of magnitude smaller than conventional aircraft — due to their plastic/carbon-fiber construction, low altitude, and erratic flight paths. This is not an assumption; it is a **measured, published fact**, and it is the direct engineering justification for why this system does not rely on radar alone.

---

## Add a New Source

```markdown
| **[Name](link)** | 🟢/🟡/🔴 | what to search for | key figures to cite |
```

[← Layer 3](./03-algorithm-validation-literature.md) · [Back to README](../README.md) · [Next: Layer 5 →](./05-visualization-standards.md)

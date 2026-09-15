# Layer 3 — Grid/Graph Algorithm Engine: Validation Literature

![Sources](https://img.shields.io/badge/sources-3-informational)

This layer has no single labeled benchmark dataset — instead, the flood-fill/BFS risk-propagation and A\*/Dijkstra route-planning design choices are validated **against published, peer-reviewed precedent**, and stated as such rather than implying a benchmark corpus exists.

[← Back to README](../README.md)

---

| Source | Status | What to search for | What you'll extract |
|---|:---:|---|---|
| **Terrain-masking A\* (Taylor & Francis, *Applied Artificial Intelligence*)** | 🟡 | Google Scholar — **"Range-Limited UAV Trajectory Terrain Masking Radar Detection Risk"** | Direct precedent for a grid-based A\* route planner operating over a discretized cell grid, minimizing radar-exposure probability/duration. Try university VPN for full text. |
| **Stealth path planning + RCS-aware A\* (ScienceDirect)** | 🟡 | **"minimal RCS tactics modified A-star stealth UAV"** | Precedent for encoding threat/RCS into route cost — may require institutional access. |
| **[Threat-cost modeling — arXiv 2501.14503](https://arxiv.org/abs/2501.14503)** | 🟢 | Direct arXiv ID | Cylindrical threat-zone cost function with distance-based penalties — adapt directly into the grid engine's cost surface. |

---

## Add a New Source

```markdown
| **[Name](link)** | 🟢/🟡/🔴 | what to search for | what you'll extract |
```

[← Layer 2](./02-semantic-threat-knowledge-base.md) · [Back to README](../README.md) · [Next: Layer 4 →](./04-radar-cross-section-justification.md)

# Gatwick Airport: Academic Literature Review

*Prepared by Yaren Duyan, 8 November 2026 (ESC 491). The original was written in Turkish; this is a faithful English version. Author names for [2] and the issue number for [1] were added after checking the publisher pages.*

## Purpose and scope

This review summarises the introduction and conclusion sections of two peer-reviewed papers that discuss the 2018 Gatwick drone incident, and assesses how they contribute to the project. Findings from the papers are marked [1] and [2]; comparisons with the project are this review's own assessment.

## Key assessment

Both papers are relevant to the project topic, but neither implements an integrated system like ours at Gatwick. The first gives an economic justification. The second is closer to our risk assessment approach. Neither confirms that open geodata at Gatwick is sufficient, nor that our algorithms will work.

## 1. Economic impact and investment case [1]

**Wendt, Voltes-Dorta and Suau-Sanchez (2020).** *Estimating the costs for the airport operator and airlines of a drone-related shutdown: an application to Frankfurt international airport.* Journal of Transportation Security, 13(1), 93–116. <https://doi.org/10.1007/s12198-020-00212-4>

- **Introduction:** uses the 2018 Gatwick closure to explain the operational and economic impact of drone incidents. The actual study asks whether a counter-drone investment at Frankfurt can be justified against the cost of a shutdown.
- **Conclusion:** the simulations show the investment is economically justified in certain closure scenarios. Because airlines carry most of the losses, the authors suggest sharing the funding between the airport and airlines. The scope and assumptions of the calculation limit the results.
- **Contribution to the project:** supports the question "why do we want to solve this problem?". It is not a technical guide for terrain, grid, line-of-sight or routing methods; its simulation concerns re-accommodating passengers on alternative connections and estimating costs.

## 2. Risk of drone intrusions at airports [2]

**Pascarella, D., Gigante, G., Vozella, A., Bieber, P., Dubot, T., Martinavarro, E., Barraco, G. and Li Calzi, G. (2022).** *A Methodological Framework for the Risk Assessment of Drone Intrusions in Airports.* Aerospace, 9(12), 747. <https://doi.org/10.3390/aerospace9120747>

- **Introduction:** proposes a systematic, quantitative approach to assessing the impact of drone intrusions on airport safety and operations, considering airport characteristics, the intrusion scenario and current operations together.
- **Conclusion:** combines a data-driven airport vulnerability index with event trees showing how an incident can develop into different outcomes. The case study is **Milan Malpensa, not Gatwick**. Suggests new data types and additional scenarios for future work.
- **Contribution to the project:** a closer source for risk assessment and decision support. However, an airport-level index is not the same as the risk score our risk engine assigns to each map cell. The paper's model should not be presented directly as a grid risk propagation algorithm.

## 3. Comparison with the risk engine tasks

| Risk engine task (Yaren Duyan) | What these two sources contribute |
|---|---|
| Terrain + OSM / PostGIS | No direct implementation guidance. |
| Grid risk model and propagation | [2] supports the risk approach; cell-level calculation needs an additional method. |
| Line of sight / terrain masking | Separate validation and technical sources are needed. |
| A* / Dijkstra routing | These papers do not validate route cost or algorithm choice. |
| Project purpose and motivation | [1] supports the economic impact, [2] supports risk assessment. |

## Contribution to the wider team

[1] helps the problem and motivation part of the joint presentation; [2] helps discuss how risk results should be interpreted. Neither should be used as experimental data validating visual detection/tracking or RF sensor performance.

## 4. How to use them in the report

- **Introduction and problem statement:** link the Gatwick incident to [1] to show the real impact of drone disruptions. State clearly that the paper's main application is Frankfurt.
- **Related work:** use [2] as an example of quantitative airport risk assessment. State that the case study is Malpensa and that the approach differs from our grid model.
- **Our method:** describe the terrain and building data, grid cell size, meaning of the risk score, line-of-sight assumptions and route cost separately. These two papers do not replace those technical choices.

## 5. Conclusion for the Gatwick choice

Gatwick's presence in the academic literature strengthens the problem context of the region choice. But finding academic sources and finding usable data are separate questions; this review is not a data access or coverage test.

The risk engine still needs to check, for the chosen study boundary: terrain/surface data coverage, empty cells, data dates, coordinate system, and whether building heights are adequate. Terrain detail and building detail should be assessed separately.

## Overall verdict

Adding both papers to the literature is appropriate. The first supports the need for the project, the second the risk assessment idea. The terrain, line-of-sight, grid and routing components need additional technical sources and validation. This review is not a comprehensive survey showing that the project is entirely new in the literature.

## References

1. Wendt, P., Voltes-Dorta, A. and Suau-Sanchez, P. (2020). Estimating the costs for the airport operator and airlines of a drone-related shutdown: an application to Frankfurt international airport. *Journal of Transportation Security*, 13(1), 93–116. <https://doi.org/10.1007/s12198-020-00212-4>
2. Pascarella, D., Gigante, G., Vozella, A., Bieber, P., Dubot, T., Martinavarro, E., Barraco, G. and Li Calzi, G. (2022). A Methodological Framework for the Risk Assessment of Drone Intrusions in Airports. *Aerospace*, 9(12), 747. <https://doi.org/10.3390/aerospace9120747>

*Review focus: introduction and conclusion sections. The papers are paraphrased; no direct quotations are used. Both references were checked against the publisher pages on 8 Nov 2026: titles, journals, volumes and DOIs match, and both papers discuss the December 2018 Gatwick incident in their introductions.*

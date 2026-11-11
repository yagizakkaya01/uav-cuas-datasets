# Conclusion

**Owner:** Mert Gökalp · **Weight:** 10%

## Progress so far

In the first half of the semester the team has:

- revised the proposal after the first advisor meeting (1 October);
- agreed on a task distribution and a 14-week plan (15 October);
- built a public catalogue of more than 35 data sources, 15 of which were accessed and checked by team members;
- had a minimal hardware list accepted by the supervisors (₺10,088);
- prepared and tested four pilot-region candidates (Eindhoven, Gatwick, Aalborg and Akrotiri/Chania) with downloaded data;
- drawn the use case, activity and deployment diagrams of the demo system;
- drafted a first version of the interface contracts between the modules.

## Difficulties faced

- **Changing hardware scope:** The demo setup changed several times within a week, from four Jetson-based nodes on masts to a single fixed PoE IP camera with all processing on a laptop. The changes were reasonable, since there was no fixed budget and the supervisors advised keeping the setup minimal. They did, however, take time and required revising parts of the design.
- **Pilot-region choice:** Each candidate has different strengths. Eindhoven has measured building heights, Gatwick has peer-reviewed literature and downloadable drone-restriction zones, Aalborg is linked to night-time visual detection, and Akrotiri has hilly terrain for line-of-sight analysis. No candidate is best on every criterion, so the decision is still open. Until it is made, the geospatial work cannot be finalised.
- **Gaps in open data:** Open data does not always contain what the system needs. Building heights are missing or only estimated for most candidates, a national drone-zone service used by one candidate was retired, historical air-traffic data requires an account, and apart from Gatwick, no peer-reviewed study of a specific drone incident could be found for the candidate regions.
- **Evaluating position accuracy:** The demo has no independent ground-truth position for the mock drone, so a simple reference method (for example, marked points on the ground or a phone GPS) still has to be defined in order to measure localisation error.
- **Schedule:** As the project changed from its initial plan, we had to revise the schedule we had set, and at times we had difficulty keeping to it.

## Retrospective

**What went well:** Building the project on real, checked sources has paid off: every candidate region was backed by an actual data download rather than a description, and errors were found and corrected early. Clear ownership of the layers meant that region proposals, diagrams and the hardware list could be prepared in parallel. Regular feedback from the supervisors kept the scope realistic.

**What we would do differently:** Comparing four regions in depth took more time than planned. A shorter list of criteria agreed at the start would have led to a decision sooner. Some work was kept on personal computers instead of the shared repository, which made it less visible to the rest of the team. From now on, all work will be pushed to the repository as it is produced.

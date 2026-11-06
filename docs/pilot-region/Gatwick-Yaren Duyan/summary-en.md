# Gatwick and Helsinki Proposals: English Summary

*Proposals by Yaren Duyan, 22 October 2026. The original PDFs ([Gatwick](./gatwick-proposal.pdf), [Helsinki](./helsinki-proposal.pdf)) are in Turkish; this is a faithful summary.*

## Why Gatwick? (second proposal)

**Proposed decision:** use London Gatwick Airport as the project's shared geospatial modelling and desk-simulation area.

**Four reasons**

1. **Detailed geodata:** Environment Agency 1 m DTM and DSM products allow ground and surface objects to be handled separately. Local tile coverage at Gatwick still needs to be checked.
2. **Official restriction source:** NATS publishes permanent UAS restriction zones as AIXM 5.1 digital datasets, so the project does not depend on screenshots.
3. **Documented incident:** the December 2018 Gatwick drone incident appears in official review documents and can be used for the needs analysis and motivation.
4. **Concrete shared scenario:** a named facility with a clear function makes the scope easier to present than a whole city. Start with a small, manageable sample area.

**Confidence level:** Gatwick is a reasoned choice, not a claim that all data is complete and freely available. Official catalogues were checked; downloading the Gatwick files, checking gaps, dates and licences, and opening the layers together were not yet done. The team decision should be backed by an access and compatibility test on a small data package.

**Fit with team roles:** gives the risk engine (terrain, surface, roads, buildings) a shared base; gives visual detection and the C2 interface a shared map; supports the knowledge base with a documented incident; the EEE work still relies on RF datasets, hardware and local measurements.

**How to read the data:** a DTM is bare ground; a DSM includes buildings and vegetation, which is not the same as a semantic 3D building database. OSM is a starting point for roads and building outlines; completeness of heights and on-site detail must not be assumed. OpenSky provides published aircraft positions with access and rate limits; it is not a record of all small drones.

**Incident document vs validation data:** the 2018 report explains why the project is needed; it does not provide a labelled drone track or synchronised camera/RF recordings. Real geodata, generated scenarios and measured sensor recordings must be described separately.

**Physical demo:** geospatial modelling can be done without going to Gatwick. Sensor and live demo work happens at an accessible local site and must not be presented as if measured at Gatwick.

**Sources:** Environment Agency 1 m DTM and DSM; NATS UAS Restriction Zones / Digital Datasets; Sussex PCC official review minutes (18 Oct 2019); OpenStreetMap; OpenSky REST API docs; Environment Agency Survey Data portal.

**Decision sentence for the team:** "We choose Gatwick as our shared study area because its detailed geodata is published by official sources, it has a digital UAS restriction source and a documented incident history. We will proceed by verifying access and coverage with sample files."

## Why Helsinki? (first proposal)

**Proposed decision:** use Helsinki as the desk-based geospatial modelling and academic simulation area, because open ground elevation, 3D buildings and OpenStreetMap data can be used together and obtained without travelling. Confirm after opening the files together on a small sample area.

**Data advantages:** National Land Survey of Finland 2 m elevation model from laser scanning; Helsinki 3D building and terrain models (less reliance on OSM height tags); Finland OSM extract from Geofabrik; remote inspection and download via the city map and the national MapSite service.

**Limits:** strong data infrastructure does not mean complete data everywhere, nor a ready camera + RF + drone position package recorded in Helsinki. The city model covers buildings and terrain; trees and bridges may be incomplete. Some regional downloads lack building attributes (CityGML files include them). CRS mismatch: national model EPSG:3067 / N2000, city model ETRS-GK25 / N2000, so layers must be transformed. FAA/ACLED records are not a labelled risk map for Helsinki, and OpenSky is not a complete source of small drone positions.

**Three-part working model:** (1) Helsinki for desk work with real geodata and clearly labelled simulation scenarios; (2) open sensor datasets for evaluating the vision and RF modules on their own terms; (3) an accessible local site for hardware and live demo measurements, never presented as Helsinki field data.

**Acceptance check before the final decision** (for the chosen sample area): (1) elevation, building and OSM files can be downloaded; (2) licences and source dates are recorded; (3) layers open in the same location; (4) gaps and road connectivity are checked; (5) file sizes are manageable on team computers. No download test had been done when the report was written.

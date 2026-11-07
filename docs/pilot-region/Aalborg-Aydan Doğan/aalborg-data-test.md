# Aalborg: Data Access Test and Source Review

*Aydan Doğan, 7 November 2026. Requests were made from a browser with real API calls; no account or token was used.*

## Data access test

| Data | Result | What is still needed |
|---|---|---|
| Elevation model (DHM, 0.4 m terrain + surface) | Catalogue request works without a token; both terrain and surface models are listed. The download request returned **403 "User not authorized"**. | A free user account and token on Dataforsyningen, set up by a team member. |
| OSM buildings | **Works.** 300 buildings in the AOI, including 27 hangars and 1 control tower. **None has a height tag.** | Building heights must be derived from the DHM surface model minus the terrain model. |
| OpenSky | Live data **works** (39 aircraft over Denmark at test time). Historical flights returned **403**. | An account and Trino access for history (same situation as Eindhoven). |
| Drone restriction zones | Only an interactive map was found; **no API**. | Denmark publishes a file in the ED-269 standard format, but its terms of use do not allow reuse (reported by Unmanned Airspace, Sep 2026). Zones may have to be digitised by hand from the map. |

## Sources

| Source | Type | Peer-reviewed? | Mentions Aalborg? |
|---|---|---|---|
| Danish National Police press releases (25–26 Sep 2025) | Official | No | Yes, covers the incident period |
| Danish Armed Forces review summary (3 Jun 2026, 9 pages, Danish) | Official report | No | **No**, only Copenhagen and unnamed bases |
| IISS study (Jul 2026), Maritime Executive summary | Think tank | No | Not in the summary |
| BISI, "Drones on NATO's Northern Flank" | Think tank | No | Yes, by name only |
| EcoDes-DK15 (Earth System Science Data, 2022) | Journal article | **Yes** | Not about the incident; shows academic use of Danish LiDAR data |
| Svanström et al. (Data in Brief, 2021) | Journal article | **Yes** | Not about the incident; source of the Halmstad dataset used for visual detection |

## Takeaway

OSM and OpenSky work as for the other candidates. The decisive open item is the DHM download, which needs only a free account. Restriction zones are the weakest point: there is no reusable dataset. No peer-reviewed source analyses the Aalborg incident; the official police statements are the strongest incident source.

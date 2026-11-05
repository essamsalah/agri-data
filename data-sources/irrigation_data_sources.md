# Irrigation Research: Available Datasets, Sources and Contacts

Prepared 24–25 Oct 2026 for the Green Riyadh smart-irrigation study.
All dataset URLs were checked on 24 Oct 2026. Only the Melbourne CSV and the Fairfield and City of Melbourne API field lists were opened directly. For the other datasets, the columns and coverage come from landing pages or READMEs and should be verified before use.

## 1. Data requirements (from the research-plan PDF)

| # | Requirement | Detail |
|---|---|---|
| R1 | Metered irrigation water | Per zone, event or day, in litres or m3, with zone area (m2) so L/m2/day can be computed. A missing meter record stays missing, never zero. |
| R2 | Soil moisture time series | Hourly, per zone, with sensor_id, timestamp, unit and quality flag. Record volumetric content (%) or water potential (kPa). |
| R3 | Weather | Rainfall, temperature, humidity, wind, radiation and reference evapotranspiration (ET0), hourly or daily. |
| R4 | Plant condition | Stress score, survival, NDVI or turf quality, per tagged plant or zone over repeated visits. |
| R5 | Design and logs | Smart vs comparison zones (matched pairs), baseline vs intervention phase, recommendation, actual action and override logs. |

Planned pilot: 24 zones in 12 matched pairs, 4 weeks baseline then 8 weeks intervention (84 days per zone, 2,016 zone-days), 5 tagged plants per zone with weekly visits (1,440 visits).

Target file structure: zone register, daily analysis file (one row per zone-day), `sensor_log`, `irrigation_events`, `plant_health`.

**Finding:** no public dataset covers all five requirements. Nothing public has paired smart-vs-standard metered urban zones, and no public irrigation, soil-moisture or plant-condition data exists for Saudi Arabia or the Gulf.

## 2. Dataset catalogue (ranked by fit)

Coverage key: Yes = covered, Part = partly, No = not covered, ? = unverified.

| Rank | Dataset | R1 | R2 | R3 | R4 | R5 | Setting |
|---|---|---|---|---|---|---|---|
| 1 | Melbourne Burnley turf | Part | Yes | Part | No | Part | Urban turf, temperate |
| 2 | DigiWaVe | Part | Yes | Yes | Part | No | Urban trees, Germany |
| 3 | TreeDataBase | Part | Yes | Yes | No | No | Urban trees, Central Europe |
| 4 | Apulia precision irrigation | Yes | Yes | Yes | No | Part | Agricultural, Italy |
| 5 | Parma tomato | Yes | Yes | Part | Part | Yes | Agricultural, Italy |
| 6 | Tucson mesquite | No | Yes | ? | Yes | Yes | Urban trees, semiarid |
| 7 | City of Melbourne soil sensors | No | Yes | No | No | No | Municipal parks |
| 8 | SIMPaCT Sydney | No | Yes | No | No | No | Park, Australia |
| 9 | Paraguay strawberry | Yes | Yes | No | No | Part | Agricultural |
| 10 | Maricopa cotton | Yes | Yes | Yes | Yes | Yes | Agricultural, arid |
| 11 | HydroShare residential turf | Part | Part | Part | Part | No | Residential turf, USA |
| 12 | Fairfield parks | No | Yes | No | No | No | Municipal parks |

### 2.1 Melbourne (Burnley) urban turf irrigation experiments
- **Publisher:** University of Melbourne (Cheung, Nice, Livesley), Zenodo
- **URLs:** https://zenodo.org/records/10140669 and the companion https://zenodo.org/records/10972538 (2021 and 2022 data, modelled ET and energy balance). Plain curl returned 403; the page loads through a normal fetch.
- **Licence:** CC BY 4.0
- **Size and time span:** about 150 kB per hourly CSV; January 2022 in the first record. Melbourne, Australia.
- **Format:** CSV, one file per treatment (no irrigation, single daytime, single night-time, multiple daytime, reference climate station).
- **Covers:** hourly irrigation (mm); hourly soil moisture (m3/m3); wind, air temperature, vapour pressure, shortwave and longwave radiation; irrigated vs unirrigated arms and timing variants.
- **Lacks:** litres and zone area, sensor_id and quality flag, rainfall and ET0 (first record), plant condition (surface temperature only), recommendation logs.
- **Use:** best real urban-turf treatment-vs-control example, for import, join and scenario testing. Temperate climate, not arid.

### 2.2 DigiWaVe (urban tree water-demand forecasting)
- **Publisher:** Masasana AI and Kompetenzzentrum Wasser Berlin, Zenodo
- **URL:** https://zenodo.org/records/21874569 (published 10 Aug 2026)
- **Licence:** CC BY 4.0
- **Size:** about 7.5 MB. `bad_oeynhausen.csv` has 10,400 rows (5 sites, 31 stations, Dec 2023 – Feb 2026). `city_b.csv` has 19,412 rows (10 sites, 71 stations, Mar 2021 – Sep 2023, unnamed German city).
- **Format:** CSV plus a README in German.
- **Covers:** daily median soil water tension at 30, 60 and 90 cm with pseudonymised station IDs; German weather service data with 1-, 7- and 14-day lookbacks; Sentinel-2 moisture indices; documented watering events.
- **Watering columns:** the README defines `water_l` as litres ("0 = keine dokumentiert") and `water_lqm` as litres per m2 (Bad Oeynhausen only; each dose recorded in one of the two units). A zero in one column can still mean watering was recorded in the other. The README does not say how volumes were measured or what area a site covers.
- **Lacks:** zone area, hourly resolution, designed treatment/control, quality flags (none seen).
- **Use:** closest public analogue to urban-tree irrigation records.

### 2.3 TreeDataBase (urban tree soil moisture)
- **Publisher:** Maier et al. (25 authors), Zenodo and GitHub
- **URLs:** https://zenodo.org/records/23022188 (V1.0.0, 28 Sep 2026); older version https://zenodo.org/records/23022189; https://github.com/pomestomi/TreeDataBase-public
- **Licence:** MIT (the Zenodo record is typed as Software; a data paper is under review)
- **Size:** 499 MB zip; georeferenced trees in Central European cities.
- **Covers:** IoT soil moisture at 30, 60 and 90 cm; hourly gridded weather; derived irrigation-event and rain-event tables; land-use layers, topographic indices, soil lab analyses and photos.
- **Lacks:** designed controls, plant-condition scores (photos only), zone area.
- **Use:** large real import and join test and event-detection validation. The zip was not opened, so units and columns in the irrigation tables are unverified.

### 2.4 Apulia multi-sector precision-irrigation dataset (agricultural)
- **Publisher:** University of Bari and University of Salento, Mendeley Data
- **URL:** https://doi.org/10.17632/c837v6p8ph (v2, 14 Sep 2026)
- **Licence:** CC BY 4.0
- **Size:** February – September 2025, Arnesano, Italy; 5 sectors (open-field tomato x2, potted tomato, zucchini, blueberry). Raw layer: 486,894 sensor readings and 3,055,944 valve-state records.
- **Format:** CSV, README, DATA_DICTIONARY.md, Python code.
- **Covers:** 789 reconstructed irrigation and fertigation events with applied water volume on a 10-minute grid (33,259 rows per sector); soil moisture, pH and EC with raw dropouts, flatlines and spikes preserved; ERA5 reanalysis weather; valve actuator telemetry; 24-hour-ahead soil-moisture target.
- **Lacks:** zone area (not confirmed), plant condition, control design, recommendation logs.
- **Use:** strongest public test of the metered-volume, event and sensor data model.

### 2.5 Parma tomato under different irrigation regimes (agricultural)
- **Publisher:** University of Parma, Mendeley Data (paper in Data in Brief, 2025)
- **URL:** https://data.mendeley.com/datasets/35wh56287y/2 (doi 10.17632/35wh56287y.2)
- **Licence:** CC BY 4.0
- **Size:** summer 2023, Parma, Italy, sampled every 10 minutes.
- **Format:** 4 CSVs (environmental, water meter, soil, daily agronomic indices).
- **Covers:** water-meter volume (m3) per line; soil moisture, EC and temperature on three sensors; air temperature, RH, pressure and CO2; GDD and heat units; three lines at 100%, 60% and 30% of the Irriframe recommendation.
- **Lacks:** rain, solar radiation, ET0, zone area, plant-stress scores.
- **Use:** power and scenario work on a replicated-deficit design with metered volumes.

### 2.6 Tucson urban mesquite, active vs passive irrigation
- **Publisher:** Luketich (University of New Mexico and University of Arizona), Dryad (paper in PLOS One)
- **URL:** https://datadryad.org/dataset/doi:10.5061/dryad.m0cfxpnzf
- **Licence:** not read on the page (Dryad default is CC0)
- **Size:** about 34 MB; 2017 and 2018 station files; Tucson, Arizona (semiarid).
- **Format:** TXT
- **Covers:** soil moisture at two depths (per the paper); canopy greenness and leaf area index; an irrigation-regime contrast. Weather is probable (files are named as weather stations) but not opened.
- **Lacks:** metered volumes and a smart-irrigation design.
- **Use:** arid urban trees with a plant-condition response, for analysis ideas.

### 2.7 City of Melbourne soil sensor readings
- **Publisher:** City of Melbourne Open Data
- **URL:** https://data.melbourne.vic.gov.au/explore/dataset/soil-sensor-readings-historical-data/information/
- **Licence:** CC BY
- **Size:** 1,785,763 records, last modified 2022-08-22; a full 2023 attachment is also offered.
- **Format:** CSV and JSON via API. Fields: `local_time, site_name, site_id, probe_id, probe_measure, soil_value, unit, year`.
- **Covers:** soil moisture (%VWC), temperature and salinity. Joins to a sensor-locations dataset on `site_id`.
- **Use:** realistic municipal long-format schema with sensor id and unit, a good fit for the `sensor_log` file.

### 2.8 SIMPaCT soil moisture dataset (Sydney Bicentennial Park)
- **Publisher:** Western Sydney University, Zenodo
- **URL:** https://doi.org/10.5281/zenodo.16811020 (code: https://github.com/OliverObst/simpact-demo-data)
- **Licence:** CC BY 4.0 (data), MIT (code)
- **Size:** 2.3 MB zip; 13 sensors; hourly VWC from 15 Nov 2022 to 17 Jan 2023.
- **Covers:** soil moisture only.
- **Notes:** the paper (arXiv 2508.11700) describes zone-level irrigation set-points that operators accept or override, but those logs are not in the dataset. The full network has 202 sensors, 13 weather stations and about 200 controllable sprinkler stations; only this subset is public. The final report at https://simpact-australia.com/resources was not opened.
- **Use:** sensor ingest and anomaly-flag testing.

### 2.9 Paraguay strawberry smart-irrigation control data (agricultural)
- **Publisher:** Universidad Loyola, Mendeley Data
- **URL:** https://data.mendeley.com/datasets/cjb4vy4mzj/3
- **Licence:** CC BY 4.0
- **Size:** 12 Jul – 17 Sep 2022. Moisture 4,293 rows (about 20 min apart); flow meter 17,411 rows (about 5 min apart, cumulative litres); valve 17,427 rows.
- **Format:** 3 two-column CSVs.
- **Covers:** cumulative flow in litres, soil moisture, valve open/close state.
- **Lacks:** weather, area, plant condition, control design.
- **Use:** reconstructing events from cumulative flow and testing joins.

### 2.10 Maricopa precision cotton irrigation 2002–2023 (agricultural, arid)
- **Publisher:** USDA-ARS, Ag Data Commons
- **URL:** https://agdatacommons.nal.usda.gov/articles/dataset/The_Maricopa_Precision_Cotton_Irrigation_Research_Data_2002-2023/33213621
- **Licence:** public access; specific licence text not read, so check it.
- **Size:** 17 experiment-years, Arizona.
- **Format:** GeoJSON, shapefile and spreadsheet, with Python scripts and a data dictionary of 203 variables.
- **Covers:** Experiment, Plot and Zone layers with irrigation-management treatments; more than 225,000 neutron-probe soil-water readings (manual, not continuous); AZMET weather; NDVI and canopy.
- **Lacks:** urban setting, continuous sensors.
- **Use:** power calculation and matched-plot and zone design in a hot, arid climate.

### 2.11 HydroShare residential turfgrass (Los Angeles, Salt Lake City, Tallahassee)
- **Publisher:** CUAHSI HydroShare
- **URLs:** https://doi.org/10.4211/hs.490329fca2ce4c8bb2d5891c939e2050 and https://www.hydroshare.org/resource/490329fca2ce4c8bb2d5891c939e2050/
- **Licence:** CC BY 4.0
- **Size:** published 24 Aug 2025; residential yards stratified by income and NDVI.
- **Covers:** irrigation depth per event and resident-reported frequency; temperature, RH and solar radiation; VWC at 0–5 cm; ET and grass surface temperature.
- **Lacks:** continuous time series (visit snapshots), controls. File formats not checked.
- **Use:** realistic urban-turf irrigation depth and ET for sanity checks.

### 2.12 Fairfield City Council parks moisture data (NSW)
- **Publisher:** Fairfield City Council
- **URL:** https://data.fairfieldcity.nsw.gov.au/explore/dataset/bosnjak-park-data/
- **Licence:** CC BY
- **Size:** 72,047 records from June 2021 (last modified 17 Jun 2026), six parks.
- **Format:** Opendatasoft API and CSV. Fields: `device_id, timestamp, site_name, soil_moisture_100mm, adjusted_soil_moisture`.
- **Covers:** soil moisture only.
- **Use:** minimal municipal sensor feed for testing ingest.

### 2.13 Lower priority
- **Proxima Green turf:** https://doi.org/10.15482/usda.adc/32050500 (USDA Ag Data Commons; licence not checked). Greenhouse bermudagrass at Maricopa with irrigation at 100%, 65% and 30% of ET and three nitrogen rates; NDVI, NDRE, NTEP visual quality and chlorophyll, but only 5 weekly visits and no soil-moisture series. The only turf plant-condition-under-deficit dataset found.
- **Amersfoort SmartCityTrees:** https://zenodo.org/records/7860313, CC BY 4.0, 2021–2022 tree soil moisture, temperature and RH, 26.5 MB, no irrigation records.
- **Ulm Smart Green:** https://datenhub.ulm.de/ckan/gl/dataset/smartgreen-ulm, JSON tree soil moisture at 2–3 depths; licence not read.
- **Kaggle `suneradilshan/smart-irrigation-training-data`:** 15,420 rows, Apache 2.0, appears synthetic (described as collected/generated); no volume, area or time index. Only useful for pipeline smoke tests. A second Kaggle IoT page could not be read (captcha).
- **Mendeley smart-home garden:** https://data.mendeley.com/datasets/jtsyb593fy/1, 960 rows over 20 days, a toy dataset.
- **USGS Fort Logan urban lawn:** https://doi.org/10.5066/p9b70dc6, eddy-covariance ET, weather and soil moisture for 2011–2012, no irrigation metering.

## 3. Weather and ET0 sources (not irrigation datasets)

| Source | URL | Notes |
|---|---|---|
| NCM Weather API (Saudi) | https://api-doc.ncm.gov.sa/en/api/getting-started | Hourly station observations with `source=mix-obs`; Riyadh Al Dariyah station is `id_164`. Needs login credentials issued by email. Temperature and wind parameters confirmed; humidity, radiation, rainfall and ET0 not confirmed. |
| CIMIS (California) | https://data.ca.gov/dataset/cimis-weather-station-spatial-cimis-data-web-api | Free with a registered API key. Station data from 1982, Spatial CIMIS daily ETo from 2003; hourly ETo from stations only. |
| FAO WaPOR | https://www.fao.org/aquastat/en/geospatial-information/wapor/ | Open; covers the Near East including Saudi Arabia; ET, rainfall and relative soil moisture at 100 m and 20 m. Satellite-derived. |
| ICBA root-zone soil moisture (MENA) | https://data.biosaline.org/en_AU/dataset/soil-moisture-data-v2 | Monthly NetCDF at 5 km from 2000, open data licence; too coarse for zone work. |
| data.gov.sa | (portal) | Did not load from my computer, so unverified; search found no weather-station or ET0 dataset there. |

## 4. Papers cited in the research plan: data status

| Paper | Data status | Notes |
|---|---|---|
| Gasser et al. 2024, LHB 110(1) 2294076 (doi 10.1080/27678490.2023.2294076) | Not public; on request from the corresponding author | 24 parcels of 50–300 m2 (about 3,000 m2 total); about 7,000 m3 per year under the standard schedule; standard schedule is drip at 1 m3 per 90 min on Mon and Thu, sprinklers at 3 m3 on Mon, Wed and Fri. |
| Gimpel et al. 2021, J. Cleaner Production 315, 128048 | No public dataset found | 18 sensors at 8 Frankfurt trees, Nov 2020 – Apr 2021. Paper's own data statement not checked. |
| Rebholz et al. 2026, Electronic Markets 36, 72 (doi 10.1007/s12525-026-00926-8) | No repository found in the part read | Open access; describes 644 sensors at 161 Frankfurt trees. The NEWS software is open source (AGPLv3, "NEWS FLOW" on openCode GitLab, linked from the Fraunhofer FIT NEWS project page). |
| Nautiyal et al. 2015, J. Irrig. Drain. Eng. 141(4) 04014062 | No public raw data | 24 homes in 6 clusters of 4 (SMS, ET, education, control); weekly meter reads, turf quality, NDVI. Reported weekly use: 15 mm (SMS), 21 mm (ET), 23 mm (education), 27 mm (control). NCSU thesis http://lib.ncsu.edu/resolver/1840.16/6385 has summary tables that could be digitised. |
| UF/IFAS Orange County report | No raw data found | https://www.ocfl.net/Portals/0/Library/Board%20Of%20County%20Commissioners/docs/Smart%20Irrigation%20Study-CERT.pdf describes 167 homes with hourly irrigation meters; PDF text not read. |
| Green Riyadh MDPI papers | Data on request (per search result) | https://www.mdpi.com/2073-4441/16/24/3559 and https://www.mdpi.com/2073-4441/17/18/2785 model ET0-based water demand; could not be opened (403). |

## 5. Author contacts (public sources only; nobody has been contacted)

Emails marked "snippet" came from a search-result summary and should be verified before sending.

### 5.1 Gasser et al. 2024 (priority 1)
| Person | Role | Contact | LinkedIn |
|---|---|---|---|
| Dr Morgan Abily (corresponding author) | Maître de conférences, Université Côte d'Azur, Géoazur RISQUES | abily@geoazur.unice.fr (T&F article page and Géoazur staff page); ORCID 0000-0003-4162-586X. Older ICRA address mabily@icra.cat is stale. | https://linkedin.com/in/morgan-abily-a15ba540 (high confidence) |
| Franck Le Gall | CEO and CTO, EGM (Valbonne) | franck.le-gall@egm.io; +33 6 20 03 54 20; EGM main line +33 9 82 33 06 72 | https://linkedin.com/in/francklegall (high) |
| L. Gasser | Software engineer, EGM | none public | https://linkedin.com/in/gasserluc (medium) |

Route: write to Abily, copy Le Gall. Sources: [T&F article](https://www.tandfonline.com/doi/full/10.1080/27678490.2023.2294076), [Géoazur staff page](https://dsiweb.oca.eu/fr/rech-risques-geoazur/4668-geo-equipe-risques-membres), [Aqua-Valley directory](https://www.aqua-valley.com/membres/membre/egm/).

### 5.2 SIMPaCT (Western Sydney University)
| Person | Role | Contact | LinkedIn |
|---|---|---|---|
| Assoc. Prof. Oliver Obst (corresponding author) | Robotics, UNSW Sydney since Jan 2026 (previously WSU) | o.obst@unsw.edu.au (UNSW profile, personal page). The WSU address in the arXiv paper may be stale. Scholar: https://scholar.google.com/citations?user=m6n603wAAAAJ | https://linkedin.com/in/oliverobst (high) |
| Prof. Sebastian Pfautsch | Director of SIMPaCT, Urban Management and Planning, WSU | S.Pfautsch@westernsydney.edu.au; ORCID 0000-0002-4390-4195; Scholar https://scholar.google.com/citations?user=Iw8sJY4AAAAJ | https://linkedin.com/in/sebastian-pfautsch (high) |
| Prof. Bahman Javadi | Networking and Cloud Computing, WSU | email not found; https://researchers.westernsydney.edu.au/en/persons/bahman-javadi-jahantigh | https://linkedin.com/in/bahmanjavadi (medium) |
| Mesut Koçyiğit | Former WSU data scientist, now apparently NSW DCCEEW | none public; ORCID 0009-0004-8097-6472 | https://linkedin.com/in/mstkocyigit (medium) |
| Russell Thomson | The Analytical Edge, Tasmania (per arXiv footnote) | not searched | not searched |

Route: Obst, copy Pfautsch. Pfautsch also co-authored the SIMPaCT final report, which may hold deployment and operations data.

### 5.3 Hohenheim / FIM (Frankfurt trees)
The corresponding author of the 2021 and 2026 papers could not be confirmed (Springer and ScienceDirect blocked fetches; check the open-access [Springer page](https://link.springer.com/article/10.1007/s12525-026-00926-8)).

| Person | Role | Contact | LinkedIn |
|---|---|---|---|
| Prof. Dr Henner Gimpel | Chair of Digital Management, Uni Hohenheim; Director at FIM; Fraunhofer FIT | henner.gimpel@fim-rc.de; +49 711 459 24051; henner.gimpel@fit.fraunhofer.de; digital@uni-hohenheim.de for publication requests | https://linkedin.com/in/henner-gimpel (high) |
| Feline Schnaak | PhD candidate, FIM and Fraunhofer FIT Augsburg; second author 2026 | feline.schnaak@fim-rc.de; +49 821 480400 29; feline.schnaak@uni-hohenheim.de (snippet); ORCID 0000-0002-3712-5291 | https://linkedin.com/in/felineschnaak (high) |
| Dominik Rebholz | First author 2026; NEWS project | no confirmed email; dominik.rebholz@hs-kempten.de (low confidence, may be a different person); ORCID 0009-0003-8769-0365 | https://linkedin.com/in/dominik-rebholz (medium) |
| Dr Valerie Graf-Drasch | Co-author 2021 | valerie.graf-drasch@uni-hohenheim.de (snippet, unverified); ORCID 0000-0002-2338-8373 | https://linkedin.com/in/dr-valerie-graf-drasch-795b39194 (medium) |
| Hawlitschek, Neumeier | 2021 co-authors | not researched | not researched |

Route: Gimpel, copy Schnaak and Rebholz.

### 5.4 Nautiyal et al. 2015 (NC State)
| Person | Role | Contact | LinkedIn |
|---|---|---|---|
| Dr Garry L. Grabow, P.E. | Project lead, Professor (emeritus per campus directory), BAE | glgrabow@ncsu.edu; 919-515-8242; https://bae.ncsu.edu/people/glgrabow/ | none found |
| Rodney Huffman | BAE emeritus faculty | huffman@ncsu.edu | none found |
| Grady Miller | Turfgrass extension, Crop and Soil Sciences | grady_miller@ncsu.edu (snippet only) | not searched |
| Daniel Bowman | Turfgrass professor, retired | dan_bowman@ncsu.edu (snippet only) | not searched |
| M. (Mayank?) Nautiyal | Former graduate student (2010 thesis); first name unconfirmed | none public | none found |

Route: Grabow (best for raw weekly meter and NDVI data), copy Huffman.

### 5.5 Melbourne Burnley turf datasets
| Person | Role | Contact | LinkedIn |
|---|---|---|---|
| Dr Pui Kwan (Paul) Cheung (corresponding author) | Former WSU postdoc; University of Melbourne PhD | cheung.p@unimelb.edu.au (printed in papers; probably no longer current); ORCID 0000-0002-7774-9277 | https://linkedin.com/in/paulpkcheung (high) |
| Prof. Stephen Livesley | Urban Horticulture, University of Melbourne (Burnley) | sjlive@unimelb.edu.au; ORCID 0000-0003-3506-2458 | none found |
| Dr Kerry Nice | Urban climate researcher | kerry.nice@unimelb.edu.au (a search summary says his Melbourne post ended Sep 2026, unverified); https://mothlight.github.io/ | https://linkedin.com/in/kerrynice (high) |
| Dr Naika Meili | National University of Singapore (record 10972538) | none found; ORCID 0000-0001-6283-2134 | not searched |

Route: Cheung, copy Livesley (best for plot and zone metadata).

### 5.6 DigiWaVe
| Person | Role | Contact | LinkedIn |
|---|---|---|---|
| Tobias Freund | Zenodo creator, Masasana AI | info@masasana.ai; +49 (0)2161 9850742 (Mönchengladbach); https://masasana.ai/use-cases/digiwave | https://linkedin.com/in/tobias-freund-b67851273 (medium) |
| Dr.-Ing. Ulf Miehe | Group leader, water treatment and reuse, Kompetenzzentrum Wasser Berlin | ulf.miehe@kompetenz-wasser.de; +49 30 53 653 821; https://kompetenz-wasser.de/de/ueber-uns/team/ulf-miehe | not searched |

Route: info@masasana.ai addressed to Tobias Freund, copy Miehe.

## 6. Gaps and suggested plan
- **Paired smart-vs-standard metered urban zones:** none public. Nearest are the NC homes (Nautiyal) and Orange County homes, neither with downloadable data, then the Melbourne experiments (treatment arms but no litres or area).
- **Arid Gulf or Saudi data:** none found for irrigation, soil moisture or plant condition.
- **Recommendation and override logs:** none public (SIMPaCT and Frankfurt describe them but do not release them).
- **Search coverage:** Dryad, Harvard Dataverse, UCI and data.gov were searched only with general web queries; PANGAEA and EU open data were not searched specifically.
- **Hybrid test set:** Apulia for the metered-volume schema, Melbourne for treatment contrasts, DigiWaVe or TreeDataBase for trees, and NCM Riyadh weather (with ET0 computed from it) to localise.
- **Author requests:** ask Gasser (via Abily and Le Gall) and SIMPaCT (via Obst) for parcel-level data and override logs; digitise the Nautiyal thesis tables for power calculations.
- **Next steps:** download the top datasets, check columns against the file specs, and build a sample joined dataset in the zone-day format.

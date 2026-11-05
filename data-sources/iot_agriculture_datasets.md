# Public IoT-in-Agriculture Datasets: Shortlist

**Prepared for:** Essam (smart irrigation / AIoT decision support, Green Riyadh)
**Date:** 31 Oct 2026 (Asia/Riyadh, UTC+3)
**Method:** I searched Zenodo, Mendeley Data, USDA Ag Data Commons (Figshare), 4TU.ResearchData/WUR, IEEE DataPort, Kaggle, the UWA repository, CGIAR/ICARDA MEL Dataverse, Saudi portals and the data-paper literature. I checked each landing page on 31 Oct 2026 with curl, WebFetch or the repository API. For Zenodo, Figshare and Mendeley, the licence, size and file names come from the repository APIs. Anything I could not confirm is marked *(unverified)*.

**Already known, not re-researched:** Apulia precision irrigation (doi 10.17632/c837v6p8ph), Parma tomato LoRaWAN (Mendeley 35wh56287y, also described in Data in Brief 2025, doi 10.1016/j.dib.2025.111521), Paraguay strawberry (Mendeley cjb4vy4mzj), Maricopa cotton (USDA ADC 33213621).

---

## Top 3 picks for Green Riyadh smart irrigation

1. **Al-Khanasri soil moisture, Jordan (ICARDA, #16).** The closest climate match to Riyadh: Badia drylands, 30-min soil-moisture and EC profiles from 2023 to 2025, CC-BY-SA. Good for calibrating soil-water dynamics and infiltration models for arid soils.
2. **Autonomous Greenhouse Challenge 2019 (WUR, #6).** The best public dataset where AI controls irrigation and climate. It includes setpoints, actuator states, irrigation and drain samples, resource use and yield for AI-controlled compartments against grower-controlled ones, under CC0. It is the best benchmark for an AIoT decision-support loop.
3. **Cook Agronomy Farm sensor network (USDA, #1).** Nine years of hourly soil moisture, temperature and EC data from a dense network of 42 locations at 5 depths, in the public domain. Use it for spatio-temporal soil-moisture forecasting and to plan sensor placement.

*Runner-up:* the **Cotton Satellite–IoT** dataset from Pakistan (#4). It is small, but it is the only one that comes with ETo, ETc and a "Water Required" label already computed alongside IoT soil readings in a hot semi-arid region. That makes it a quick prototype target for irrigation decision models.

---

## A. Irrigation and soil sensing

| # | Dataset / publisher | URL (status) | Licence | Size / span / location | Sensors / variables | Format | Use note |
|---|---|---|---|---|---|---|---|
| 1 | **A field-scale sensor network data set... soil moisture in a dryland agricultural field** (Cook Agronomy Farm), USDA-ARS, Ag Data Commons | https://agdatacommons.nal.usda.gov/articles/dataset/Data_from_A_field-scale_sensor_network_data_set_for_monitoring_and_modeling_the_spatial_and_temporal_variation_of_soil_moisture_in_a_dryland_agricultural_field/24852273 (page returned 202 bot challenge to curl; metadata confirmed via Figshare API). DOI 10.15482/usda.adc/1349683 | U.S. Public Domain | 39 MB zip; Apr 2007 to Jun 2016; Pullman, WA, USA (dryland) | Volumetric water content, soil temperature, bulk EC; 42 locations × 5 depths (30 to 150 cm); hourly and daily; QC flags, soil properties, crop history, GIS layers | TXT/CSV + spatial | Long-term spatio-temporal soil-moisture modelling and sensor-placement studies |
| 2 | **Dataset on irrigation for Tomato** (v3), Assam University, Mendeley Data | https://data.mendeley.com/datasets/33cngpcrmx (200) | CC BY 4.0 | 265 KB CSV; v3 published Jul 2026; India *(exact site unverified)* | BME280 temperature/humidity/pressure, capacitive soil moisture (SEN0193), RS485 NPK, API wind speed and solar radiation | CSV (from JSON) | Edge-IoT underground drip-irrigation scheduling and soil-health prediction |
| 3 | **Sensors and Actuators Data for Model Identification of an Irrigation System**, Pacheco, Cáceres, Orihuela, Mendeley Data | https://data.mendeley.com/datasets/cvy6m27bnr/1 (200) | CC BY 4.0 | 41 KB zip; 15 to 21 Jun 2023; site *(unverified; same group as the Paraguay strawberry dataset)* | VWC from 6 ground nodes (every 15 min), valve state 0/1 (every 5 min), split into identification and validation sets | CSV | System identification and control design (MPC/PID) for closed-loop irrigation |
| 4 | **Integrated Satellite–IoT–Machine Learning Framework for Precision Irrigation and Sustainable Cotton Production**, Zenodo | https://zenodo.org/records/17550127 (200) | CC BY 4.0 | 31 KB, 2 CSVs; IoT 2024 + NDVI 2023; Rahim Yar Khan, Pakistan (hot semi-arid) | Air temp/RH, soil moisture, soil temp, soil EC, NPK, salinity, TDS, pH, battery, signal strength, API wind, **ETo, ETc, "Water Required"** | CSV | Quick prototype for ET-based irrigation decisions in a hot climate (small, noisy, has -1/-5 sentinel values) |
| 5 | **AgriDataValue – IoT Environmental Data** (Horizon Europe project), Zenodo | https://zenodo.org/records/18954708 (200) | CC BY 4.0 | 1.17 GB, one CSV per pilot (pilot_3, 5, 13, 15, 16, 18...); published Mar 2026; EU pilots *(locations unverified)* | Air temp, RH, pressure, solar radiation, soil moisture, soil temp, dew point, precipitation, water pressure, VPD, soil water tension | CSV | Large multi-site benchmark for irrigation-relevant forecasting and transfer learning |

## B. Greenhouse / controlled environment

| # | Dataset / publisher | URL (status) | Licence | Size / span / location | Sensors / variables | Format | Use note |
|---|---|---|---|---|---|---|---|
| 6 | **Autonomous Greenhouse Challenge, Second Edition (2019)**, WUR / 4TU.ResearchData | https://data.4tu.nl/datasets/8b35675d-7549-49cc-a8c3-dedec8d3f23e (timed out from my checker and WebFetch returned 504 on 31 Oct; mirror record https://research.wur.nl/en/datasets/autonomous-greenhouse-challenge-second-edition-2019/ returned 200). DOI 10.4121/uuid:88d22c60-21b3-4ea8-90db-20249a5be2a7 | CC0 | 6-month cherry-tomato crop, 6 compartments; Bleiswijk, NL | Indoor/outdoor climate, irrigation, actuator status, setpoints, resource use (water, CO2, energy), harvest, quality, drain analysis | CSV/XLSX in zip/7z | Benchmark comparing AI control with growers, and for reinforcement-learning irrigation/climate control |
| 7 | **4th Autonomous Greenhouse Challenge: Pre-trial Dwarf Tomato Measurements and Images**, WUR / 4TU | https://data.4tu.nl/datasets/e1ee9de9-6ce9-4502-a37c-34b5b1372bed (4TU timed out on 31 Oct; details from search snapshot). DOI 10.4121/e1ee9de9-6ce9-4502-a37c-34b5b1372bed | *(unverified)* | ~12 GB (Timeseries.zip 4 MB + RGB-D images); Sep to Nov 2023; Bleiswijk, NL | 5-min greenhouse climate and weather, plant traits, RGB-D canopy and single-plant images | XLSX, PNG | Fusing climate data and vision for growth modelling. The main 2024 4th-AGC dataset (fa102772-...) listed its files as "temporarily unavailable" |
| 8 | **EDEN ISS 2020 Telemetry Dataset**, DLR, Zenodo | https://zenodo.org/records/11485183 (200) | CC BY 4.0 | 36 MB zip; 97 sensors, 5-min data, 1 Jan to 30 Dec 2020; Antarctica (Neumayer III) | CO2, PAR, RH, temperature, VPD, nutrient EC/pH/level/pressure, valves | CSV | Anomaly detection on a closed-loop controlled-environment agriculture system with nutrient delivery |

## C. LoRa / WSN telemetry (agri sensing + radio metrics)

| # | Dataset / publisher | URL (status) | Licence | Size / span / location | Sensors / variables | Format | Use note |
|---|---|---|---|---|---|---|---|
| 9 | **VignaBagnolo**, OCNO Srl / Univ. Pavia, IEEE DataPort | https://ieee-dataport.org/documents/vignabagnolo (200). DOI 10.21227/z148-2d22 | *(unverified on page)* | measurements.csv 15.2 MB + ~590 MB images; 24 Mar to 24 Dec 2024; vineyard, Bagnolo San Vito, Italy | 2 air + 6 soil LoRaWAN nodes every 10 min: air temp/RH, soil permittivity, soil temp, **RSSI, SNR, frequency**, GPS, daily RGB photos, BBCH stages | CSV, JPG | Studying how link quality relates to sensing, and multimodal crop-stage work. May need an IEEE account to download |
| 10 | **LoRa Underground Farm Sensor Network**, Univ. of Western Australia | https://research-repository.uwa.edu.au/en/datasets/lora-underground-farm-sensor-network/ (200) | CC BY | ~100 MB over 15 files; 10 Sep 2018 to 2 Jun 2019; UWA Future Farm Ridgefield, WA (Mediterranean/semi-arid) | Buried LoRa node channel metrics, soil moisture and temperature, weather station, eddy-flux tower (ET) | CSV, XLS, SQLite DB, Rmd | Underground wireless sensor networks for buried irrigation sensors, plus flux-tower ET as ground truth |
| 11 | **Joint Communication and Sensing: ... Greenhouse Monitoring using LoRaWAN**, Zenodo | https://zenodo.org/records/5793685 (200) | CC BY 4.0 | 71 MB, 3 XLSX; two 5-month tomato-greenhouse campaigns (27+ sensors); location *(unverified)* | Temperature, humidity, RSSI, receive time | XLSX | Using RSSI as a crop-growth proxy and planning greenhouse LoRaWAN deployments |

## D. Livestock

| # | Dataset / publisher | URL (status) | Licence | Size / span / location | Sensors / variables | Format | Use note |
|---|---|---|---|---|---|---|---|
| 12 | **Precision Beef – Animal Behaviour Classification**, Zenodo | https://zenodo.org/records/4064802 (200) | CC BY 4.0 | 8.2 GB; 18 animals, 3 trials; Easter Howgate Farm, Edinburgh, UK | 3-axis collar accelerometer at 10 Hz + RumiWatch jaw-pressure labels (eating, rumination, other) | CSV | Supervised behaviour classification and TinyML on collars |
| 13 | **Japanese Black Beef Cow Behavior Classification Dataset**, Zenodo | https://zenodo.org/records/5849025 (200) | CC BY 4.0 | 14.5 MB zip; 6 cows; Japan | Tri-axial accelerometer at 25 Hz, 13 labelled behaviours *(counts from search snippet)* | CSV in zip | Fine-grained, multi-class behaviour models |
| 14 | **IoT sensor data XGain UC6**, ILVO, Zenodo | https://zenodo.org/records/15600573 (200) | CC BY 4.0 | 0.2 MB zip; 10 Holstein cows, 3 weeks in Apr 2024; Melle, Belgium | Axivity AX3 neck-collar accelerometer at 12.5 Hz; on-device decision-tree classes (grazing, ruminating) | CSV in zip | Edge classification of grazing in resource-limited setups |

## E. IoT network / security for agriculture

| # | Dataset / publisher | URL (status) | Licence | Size / span / location | Sensors / variables | Format | Use note |
|---|---|---|---|---|---|---|---|
| 15a | **Farm-Flow: AG-IoT Security – Intrusion Detection in Smart Agriculture**, Zenodo (paper: Computers & Electrical Eng. 2024) | https://zenodo.org/records/10964648 (200). DOI 10.5281/zenodo.10964647 | CC BY 4.0 | 501 MB zip; 1.31 M flows; Aug to Oct 2022 testbed | Network flows + raw PCAP: normal traffic plus ARP spoofing, BotNet DDoS, HTTP/ICMP/MQTT/TCP/UDP floods, port scan; binary and multiclass splits | CSV, PCAP | The only intrusion-detection set built specifically for agri-IoT; good for an IDS layer in an AIoT irrigation stack |
| 15b | **Edge-IIoTset**, Ferrag et al., IEEE DataPort / Kaggle | https://ieee-dataport.org/documents/edge-iiotset-new-comprehensive-realistic-cyber-security-dataset-iot-and-iiot-applications (200); https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot (200, rate-limited) | *(unverified)* | Multi-GB; testbed (2022) | Traffic from soil-moisture, water-level, pH, temp/humidity sensors and Modbus; 14 attack types | CSV, PCAP | Use the raw per-sensor files (Soil_Moisture, Water_Level, pH). A 2026 arXiv preprint (2608.15761) reports label leakage in the curated subsets |

## F. Middle East / arid

| # | Dataset / publisher | URL (status) | Licence | Size / span / location | Sensors / variables | Format | Use note |
|---|---|---|---|---|---|---|---|
| 16 | **Soil moisture data – Al-Khanasri restoration site**, ICARDA (CGIAR MEL Dataverse), USDA-funded | https://data.mel.cgiar.org/dataset.xhtml?persistentId=hdl%3A20.500.11766.1%2FFK2%2F7S3BIP (200) | CC-BY-SA-4.0 (guestbook on download) | 72 MB CSV; 21 Feb 2023 to 28 Jul 2025; Jordan Badia (arid) | Acclima TR-315 every 30 min at -10/-30/-100 cm in 4 positions around micro water-harvesting pits: VWC, soil temp, permittivity, bulk and pore-water EC | CSV + data dictionary | **Best arid analogue for Riyadh**: soil-water dynamics after rain and irrigation events, salinity and EC behaviour |
| 17 | **IoT Agriculture 2024**, Tikrit University (Iraq), Kaggle | https://www.kaggle.com/datasets/wisam1985/iot-agriculture-2024 (200) | CC BY-ND 4.0 (**no derivatives**) | 2.48 MB; 37,923 rows, 13 columns; 2023 to 2024 smart greenhouse, Iraq | Temperature, humidity, water level, soil N/P/K, fan / watering-pump / water-pump on-off states | CSV | Predicting actuator states (pump/fan) from a hot-climate Gulf-region greenhouse. Check whether the ND licence allows your use |
| 18 | *Context source, not an IoT dataset:* **Saudi NCM API, agricultural parameters** (reference ET at 1 to 24 h, GDD) | https://api-doc.ncm.gov.sa/en/api/available-parameters/agricultural-parameters (200) | *(terms unverified; probably needs an API account)* | Saudi Arabia, model and station data | ET0, growing degree days, weather | API (CSV/JSON) | ET0 forcing for Riyadh irrigation scheduling, to pair with soil-sensor data |
| 19 | *Context source:* **NCM Weather Stations and Monthly Climate Records of Saudi Arabia (1968–2016)**, FAO-KSA portal | https://data.faoksa.info/dataset/weather-stations (200) | *(unverified)* | Monthly, 1968 to 2016, KSA stations | Climate normals | *(unverified)* | Long-term climatology baseline for Riyadh |

---

## Excluded or caveated

- **DEEP FARM: OLIVE use case** (Zenodo 17990380): Zenodo API reports *restricted* access with no public files.
- **4th AGC main dataset 2024** (4TU fa102772-...): files listed as "temporarily unavailable".
- **Saudi date-palm AI–IoT dataset** (Sci. Reports 2026, doi 10.1038/s41598-026-36106-z; PMC12877140): describes 500 records from Saudi farms (soil moisture, temperature, humidity, biometrics), but I found **no public download link**. Ask the authors for it.
- **Al-Aziziah palm farm, Hail, KSA IoT network** (Smart Agri. Tech. 2025, doi 10.1016/j.atech.2025.101391) and the **date-palm sap-flow/VWC study** (IJAB, doi 10.17957/ijab/15.1869): Saudi/Gulf sensor studies with no open dataset found.
- Synthetic Kaggle sets (e.g. "Synthetic Greenhouse IoT Telemetry") and the small "Crop Recommendation" style sets are left out because they are not real deployments.

## Gaps (especially Saudi / Gulf)

- **No openly licensed IoT irrigation or soil-sensor dataset from Saudi Arabia or the GCC** turned up in Zenodo, Mendeley, Figshare, Dryad, Kaggle, IEEE DataPort or data.gov.sa. Saudi IoT studies (date palm, Hail, KAUST/KSU work) publish results but not raw data.
- Urban landscape irrigation (parks, street trees, the Green Riyadh use case) is effectively absent. Public data covers crops, greenhouses and rangeland, not municipal greenery.
- Few datasets combine sensing with **irrigation actuation in hot, arid conditions**. The closest are Cotton Pakistan (#4), Iraq greenhouse (#17) and Jordan (#16, which is soil-only).
- Agri-IoT security data comes from testbeds (Farm-Flow, Edge-IIoTset), not real farm traffic.
- **Suggested route:** pair NCM ET0 (#18) with arid soil dynamics from Jordan (#16) and AI-control benchmarks (#6). Then request data directly from Saudi authors (date-palm Sci. Rep. 2026, the Hail farm study), or collect a small Riyadh pilot dataset and publish it on Zenodo, which would fill a real gap.

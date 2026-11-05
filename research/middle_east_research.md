# Middle East university research relevant to Green Riyadh AIoT smart irrigation

Compiled 1 November 2026 (Asia/Riyadh, UTC+3). Search of web indexes, university repositories (Pure portals, ScholarWorks) and publisher pages. Nobody was contacted.

**How to read this:** *Relevance* is relevance to the 24-zone matched-pair pilot (L/m²/day + plant condition, DiD). *Data* is public data availability. *Check* records how the URL was verified on 1 Nov 2026: `HTTP 200` = curl or fetch succeeded; MDPI, Wiley, ASCE and Taylor & Francis block automated requests with 403, so for those the record was confirmed through the search index or a successful page fetch. Emails are listed only where printed on a real page.

Items: **30** (16 Saudi). Open Middle East / North Africa datasets: see section 3.

## 1. Top picks for the pilot

| # | Item | University | Why it matters |
|---|---|---|---|
| S1 | [Irrigation Water Demand Management-Based Innovative Strategy: Model Application on the Green Riyadh Initiative, Saudi Arabia](https://www.mdpi.com/2073-4441/16/24/3559) (2024) | King Saud University (KSU), Saudi Arabia | Plant Coefficient Method + Landsat 8 ET for a 627,000 m² Green Riyadh site (King Salman Rd / Airport Rd); ~2.6 mm/day. Gives a Riyadh landscape water-demand benchmark for the zone-day L/m² outcome. |
| S2 | [Water Demand and Water Application for Plants Based on Plant Coefficient Method: Model Development and Verification on Sites of Green Saudi Arabia](https://www.mdpi.com/2073-4441/17/18/2785) (2025) | King Saud University (KSU), Saudi Arabia | GIS Plant Coefficient Method Tool (PCMT), validated on urban trees, date palms and turf in Riyadh; summer peaks up to ~25 L/m². A ready-made ET-based comparator for the 'recommended' irrigation arm. |
| S3 | [Investigation of Irrigation Water Application Rates to Landscaped Areas in Riyadh](https://link.springer.com/article/10.1016/S1018-3639(18)30543-9) (1991) | King Saud University (KSU), Saudi Arabia | 77 Riyadh green areas; peak application 23–33 L/m²/day against a recommended ~15 L/m²/day. A historical L/m²/day baseline for the pilot's outcome variable. |
| S9 | [SIMBA (Smart Irrigation Management in Beautiful Aridlands) platform for desert greening](https://doi.org/10.25781/kaust-04091) (2024) | KAUST, Saudi Arabia | Autonomous ET + soil-moisture irrigation platform for desert greening; explicitly frames Green Riyadh / King Salman Park. Closest in purpose to the pilot (lab-tested only). |
| S5 | [Efficient IoT-Based Control for a Smart Subsurface Irrigation System to Enhance Irrigation Management of Date Palm](https://www.mdpi.com/1424-8220/21/12/3942) (2021) | King Faisal University (KFU), Date Palm Research Center; Zagazig Univ. (Riad), Saudi Arabia | Soil-moisture-sensor IoT control (ThingSpeak) for date palm: 64.1% water saving vs surface irrigation. Sensor/threshold logic similar to the pilot's recommendation engine. |
| O1 | [Smart Monitoring, Sap-Flow, Stem-Psychrometer and Soil-Moisture Measurements Tools for Precision Irrigation and Water Saving of Date Palm](https://squ.elsevierpure.com/en/publications/smart-monitoring-sap-flow-stem-psychrometer-and-soil-moisture-mea/) (2021) | Sultan Qaboos University (SQU) with ICBA, Oman | Wireless real-time weather, sap flow, stem water potential and VWC; bubbler vs aflaj saved 91–92% water. Template for combining R2 soil and R4 plant-stress measures. |
| O2 | [Comparative study of ET-based and soil moisture-based irrigation for Al Batinah region in Oman](https://www.actahort.org/books/1054/1054_15.htm) (2014) | Sultan Qaboos University (SQU), Oman | Head-to-head ET vs soil-moisture scheduling in an arid Gulf setting; informs the pilot's choice of control logic. |
| U1 | [Testing and Evaluation of a Smart Irrigation System Towards Smart Landscaping in UAE](https://doi.org/10.22587/jasr.2019.15.5.3) (2019) | The British University in Dubai (BUiD), UAE | Soil-moisture sensor kit vs timer on Dubai landscaping: ~21–26% reduction in Sep–Oct; net ~5.8%. The closest Gulf urban-landscape smart-vs-standard comparison. |
| IR1 | [Effectiveness of smart green-space irrigation systems in reducing consumption (case study: Razi Park, Tehran) [Persian]](https://jwsd.um.ac.ir/article_31325.html) (n.d.) | Imam Khomeini International University, Iran | Smart controller on ~2,500 m² urban park vs manual: 6% (monthly) and 15% (weekly) saving; ~10.6 L/m² saved. One of very few urban-park smart-vs-manual comparisons in the region. |
| E1 | [Improving the spatial deployment of the soil moisture sensors in smart irrigation systems using GIS](https://scholar.asu.edu.eg/handle/123456789/220544) (2024) | Ain Shams University, Egypt | GIS-based optimal placement of soil-moisture sensors (NodeMCU, calibrated VWC). Directly relevant to where to put sensors in each pilot zone (R2). |
| M1 | [Dataset on Agrometeorological Parameters in the Souss-Massa Plain](https://atlas.um6p.ma/p/en/research-outputs/dataset-on-agrometeorological-parameters-in-the-souss-massa-plain) (2026) | Ibn Zohr Univ., Cadi Ayyad Univ., UM6P/IWRI, Ibn Tofail Univ., Morocco | OPEN DATA: 2019–2022 citrus orchard eddy-covariance station, soil moisture/temp/EC 5–80 cm, weather, fluxes; 30-min CSV; CC-BY 4.0 at data.mendeley.com/datasets/rg4yb8m5sf/1. Usable for R2/R3 prototyping in a semi-arid setting. |

## 2. Full list by country

### Saudi Arabia

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| S1 | **Irrigation Water Demand Management-Based Innovative Strategy: Model Application on the Green Riyadh Initiative, Saudi Arabia**<br>A. Elkatoury; A.A. Alazba | King Saud University (KSU) | 2024, Water 16(24):3559 | [link](https://www.mdpi.com/2073-4441/16/24/3559)<br>doi:10.3390/w16243559 | **High**: Plant Coefficient Method + Landsat 8 ET for a 627,000 m² Green Riyadh site (King Salman Rd / Airport Rd); ~2.6 mm/day. Gives a Riyadh landscape water-demand benchmark for the zone-day L/m² outcome. | On request | — | Page fetched earlier; MDPI returns 403 to curl |
| S2 | **Water Demand and Water Application for Plants Based on Plant Coefficient Method: Model Development and Verification on Sites of Green Saudi Arabia**<br>A.A. Alazba; M.N. Elnesr; A. Elkatoury; N. Alrdyan; F. Radwan; M. Ezzeldin | King Saud University (KSU) | 2025, Water 17(18):2785 | [link](https://www.mdpi.com/2073-4441/17/18/2785)<br>doi:10.3390/w17182785 | **High**: GIS Plant Coefficient Method Tool (PCMT), validated on urban trees, date palms and turf in Riyadh; summer peaks up to ~25 L/m². A ready-made ET-based comparator for the 'recommended' irrigation arm. | On request (assumed; not stated on a fetched page) | — | Search index (author list); MDPI 403 to curl |
| S3 | **Investigation of Irrigation Water Application Rates to Landscaped Areas in Riyadh**<br>Nazih K. Shammas (per search index, unverified) | King Saud University (KSU) | 1991, J. King Saud Univ. – Engineering Sciences 3(2) | [link](https://link.springer.com/article/10.1016/S1018-3639(18)30543-9)<br>doi:10.1016/S1018-3639(18)30543-9 | **High**: 77 Riyadh green areas; peak application 23–33 L/m²/day against a recommended ~15 L/m²/day. A historical L/m²/day baseline for the pilot's outcome variable. | Tables in paper only | — | HTTP 200 (curl) |
| S4 | **Evaluating two irrigation controllers under subsurface drip irrigated tomato crop**<br>H.M. Al-Ghobari et al. | King Saud University (KSU) | 2016, Spanish J. Agricultural Research 14(4) | [link](https://doi.org/10.5424/sjar/2016144-8615)<br>doi:10.5424/sjar/2016144-8615 | **High**: ET/weather-based smart controllers (SmartLine, Hunter Pro-C2) in Riyadh: 25% and 18% water saving vs conventional scheduling. Riyadh evidence on controller effect sizes, useful for power calculations. | None public | — | DOI resolves (302 to publisher) |
| S5 | **Efficient IoT-Based Control for a Smart Subsurface Irrigation System to Enhance Irrigation Management of Date Palm**<br>M. Mohammed (corr.); K. Riad; N. Alqahtani | King Faisal University (KFU), Date Palm Research Center; Zagazig Univ. (Riad) | 2021, Sensors 21(12):3942 | [link](https://www.mdpi.com/1424-8220/21/12/3942)<br>doi:10.3390/s21123942 | **High**: Soil-moisture-sensor IoT control (ThingSpeak) for date palm: 64.1% water saving vs surface irrigation. Sensor/threshold logic similar to the pilot's recommendation engine. | None public (not stated) | memohammed@kfu.edu.sa | Email printed on MDPI article PDF; MDPI 403 to curl |
| S9 | **SIMBA (Smart Irrigation Management in Beautiful Aridlands) platform for desert greening**<br>Jiaqi Zheng | KAUST | 2024, KAUST dissertation | [link](https://doi.org/10.25781/kaust-04091)<br>doi:10.25781/kaust-04091 | **High**: Autonomous ET + soil-moisture irrigation platform for desert greening; explicitly frames Green Riyadh / King Salman Park. Closest in purpose to the pilot (lab-tested only). | None | — | DOI resolves (200) |
| S6 | **Applications of AI and IoT for Advancing Date Palm Cultivation in Saudi Arabia**<br>M. Mohammed; N.K. Alqahtani; M. Munir; M.A. Eltawil | King Faisal University (KFU) | 2023, IntechOpen book chapter | [link](https://www.intechopen.com/chapters/88289) | **Medium**: Review of AI/IoT irrigation for date palm in KSA; good map of Saudi groups and citations (e.g. Agronomy 13(4):1081 ML water/energy prediction). | Review (no data) | memohammed@kfu.edu.sa | HTTP 200; email shown on page |
| S7 | **Toward Sustainable Farming: Implementing Artificial Intelligence to Predict Optimum Water and Energy Requirements for Sensor-Based Micro Irrigation Systems Powered by Solar PV**<br>Maged Mohammed; Hala Hamdoun; Alaa Sagheer | King Faisal University (KFU) | 2023, Agronomy 13(4):1081 | [link](https://www.mdpi.com/2073-4395/13/4/1081)<br>doi:10.3390/agronomy13041081 | **Medium**: LSTM/XGBoost prediction of irrigation water and energy for date palm; AI forecasting component analogous to the pilot's recommendation model (LSTM best, R² 0.90–0.92). | Unknown | — | Search index (title/authors); MDPI 403 to curl |
| S8 | **Design and Implementation: An IoT-Framework-Based Automated Wastewater Irrigation System**<br>S. Habib (corr.); S. Alyahya; M. Islam; A.M. Alnajim; A. Alabdulatif; A. Alabdulatif | Qassim University | 2022, Electronics 12(1):28 | [link](https://www.mdpi.com/2079-9292/12/1/28)<br>doi:10.3390/electronics12010028 | **Medium**: IoT soil-moisture irrigation of date palms with treated wastewater; dashboard and water-time equation; ~25% saving. | None ('Not applicable') | — | Page fetched (WebFetch) |
| S11 | **AI-enabled smart farming framework for sustainable date palm cultivation in arid regions using machine learning and IoT integration**<br>Marran Al Qwaid; Md Tanjil Sarker; Sarowar Morshed Shawon; H.T. Zubair | Shaqra University (with Multimedia Univ., Malaysia) | 2026, Scientific Reports | [link](https://www.nature.com/articles/s41598-026-36106-z)<br>doi:10.1038/s41598-026-36106-z | **Medium**: 500-record Saudi date-palm dataset (soil moisture, temp, humidity, growth, health status) with ML health prediction. Similar to R4 plant condition labels. | On request (corresponding author) | — | HTTP 200; affiliations from citation meta |
| S14 | **Optimizing Water Use in Maize Irrigation with Reinforcement Learning**<br>M. Alkaff; A. Basuhail | King Abdulaziz University (KAU) | 2025, Mathematics 13(4):595 | [link](https://www.mdpi.com/2227-7390/13/4/595)<br>doi:10.3390/math13040595 | **Medium**: PPO reinforcement learning with AquaCrop; 29% water reduction in simulation. AI scheduling method reference. | Simulation | — | Search index; MDPI 403 to curl |
| S15 | **PCA and feature importance-based dimension reduction for Reference Evapotranspiration (ET0) predictions of Taif, Saudi Arabia**<br>R.N. Bashir; O. Mzoughi; M.A. Shahid; N.M. Alturki; O. Saidani | Princess Nourah Univ. (PNU) co-authors (affiliations unverified) | 2024, Computers and Electronics in Agriculture 222:109036 | [link](https://doi.org/10.1016/j.compag.2024.109036)<br>doi:10.1016/j.compag.2024.109036 | **Medium**: ML ET0 prediction from reduced weather inputs in Taif; relevant to R3 when NCM data has gaps. | Unknown | — | DOI resolves (200) |
| S10 | **Sensing water for smarter agriculture (MOF-based soil-moisture sensor)**<br>M. Eddaoudi; K.N. Salama groups (news item) | KAUST | 2023, KAUST Discovery news | [link](https://discovery.kaust.edu.sa/en/article/15462/sensing-water-for-smarter-agriculture/) | **Low**: Low-cost soil-moisture sensor development; relevant to R2 sensor choice and calibration. Underlying paper DOI not found. | None | — | HTTP 200 |
| S13 | **Implementing a Smart Irrigation System using IoT Technology to Achieve Saudi's Green Ambition**<br>Ibraheem Almahmoud; Eyad Talal Attar | King Abdulaziz University (KAU) / Mawhiba | 2023, IEEE EI2 2023 | [link](https://doi.org/10.1109/ei259745.2023.10513056)<br>doi:10.1109/ei259745.2023.10513056 | **Low**: Prototype IoT irrigation framed around Saudi Green Initiative goals; low evidence level. | None | — | DOI resolves (202 IEEE); authors from search index |

### Saudi Arabia (site)

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| S12 | **The applications of IoT network to enhance farming at Al-Aziziah palm trees farm in Saudi Arabia**<br>A. Aljumaiah; O. Temowo; G. Marseglia; G. Sciannimanico; F.N.A. Otoo; R. Parihar; A. Al-Ashaab | Cranfield University (UK) — Saudi farm case (Al-Aziziah) | 2025, Smart Agricultural Technology 12 | [link](https://doi.org/10.1016/j.atech.2025.101391)<br>doi:10.1016/j.atech.2025.101391 | **Low**: IoT network deployment on a Saudi palm farm; deployment lessons (connectivity, sensors). Not an ME university. | Unknown | — | DOI resolves (200) |

### Saudi Arabia (weak)

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| S16 | **Precision farming: Using an IoT multimodal data-driven deep network to optimize irrigation in wheat crops**<br>O. Elsherbiny; L. Zhou; Y. He; Z. Qiu (corr.) | Listed in KFUPM Pure (externally published; Zhejiang Univ.) | 2025, Expert Systems with Applications 291:128583 | [link](https://pure.kfupm.edu.sa/en/publications/precision-farming-using-an-iot-multimodal-data-driven-deep-networ)<br>doi:10.1016/j.eswa.2025.128583 | **Low**: Multimodal IoT + deep network for irrigation decisions; method reference only (data from China). | Unknown | — | HTTP 200 (KFUPM Pure) |

### UAE

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| U1 | **Testing and Evaluation of a Smart Irrigation System Towards Smart Landscaping in UAE**<br>Fatma Al Sulaimani; Bassam Abu-Hijleh | The British University in Dubai (BUiD) | 2019, J. Applied Sciences Research 15(5) | [link](https://doi.org/10.22587/jasr.2019.15.5.3)<br>doi:10.22587/jasr.2019.15.5.3 | **High**: Soil-moisture sensor kit vs timer on Dubai landscaping: ~21–26% reduction in Sep–Oct; net ~5.8%. The closest Gulf urban-landscape smart-vs-standard comparison. | None | — | Unverified: DOI and PDF host returned HTTP 500 at check; found in search index |
| U2 | **Study of water supply – yield relationships in mature date palms (Al Foah farm)**<br>UAEU CAVM (project page) | United Arab Emirates University (UAEU) | n.d., UAEU research project page | [link](https://www.uaeu.ac.ae/en/cavm/alfoah_farm/research/water_supply.shtml) | **Medium**: Weather-based automatic scheduling with soil-moisture and water-potential sensors on date palms; Gulf field infrastructure partner. | None | — | HTTP 200 |
| U3 | **ICBA SCADA soil-moisture/salinity-controlled irrigation experiment**<br>ICBA (experiment page) | International Center for Biosaline Agriculture (ICBA), Dubai | n.d., ICBA experiment page | [link](https://www.biosaline.org/experiments/experiment-3) | **Medium**: SCADA irrigation driven by soil-moisture and salinity sensors in sandy soils; ICBA also hosts the MENA soil-moisture data portal (data.biosaline.org). | Portal data open (coarse grid); experiment data none | — | HTTP 200 |

### Oman

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| O1 | **Smart Monitoring, Sap-Flow, Stem-Psychrometer and Soil-Moisture Measurements Tools for Precision Irrigation and Water Saving of Date Palm**<br>S.A. Siddiqi; Y.A. Al-Mulla (corr.); I. McCann; G. AbuRumman; M. Belhaj; S. Zekri; A. Al Ismaili; S. Rahman | Sultan Qaboos University (SQU) with ICBA | 2021, Int. J. Agriculture & Biology 26(5):570–578 | [link](https://squ.elsevierpure.com/en/publications/smart-monitoring-sap-flow-stem-psychrometer-and-soil-moisture-mea/)<br>doi:10.17957/IJAB/15.1869 | **High**: Wireless real-time weather, sap flow, stem water potential and VWC; bubbler vs aflaj saved 91–92% water. Template for combining R2 soil and R4 plant-stress measures. | None | — | HTTP 200 (SQU Pure) |
| O2 | **Comparative study of ET-based and soil moisture-based irrigation for Al Batinah region in Oman**<br>P.M.K. Alahakoon; H.P.W. Jayasuriya; S. Zekri; H.A. Al-Busaidi; R. Zaier | Sultan Qaboos University (SQU) | 2014, Acta Horticulturae 1054:135–144 | [link](https://www.actahort.org/books/1054/1054_15.htm)<br>doi:10.17660/ActaHortic.2014.1054.15 | **High**: Head-to-head ET vs soil-moisture scheduling in an arid Gulf setting; informs the pilot's choice of control logic. | None | — | HTTP 200 |

### Qatar

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| Q1 | **Evaluation of smart irrigation systems in hot-arid climates for green roofs and walls: case of Doha, Qatar**<br>Sara M. Zaina (corr.); Fodil Fadli; Seyed Morteza Hosseini | Qatar University | 2022, Smart and Sustainable Built Environment 11(2):346–367 | [link](https://vbn.aau.dk/en/publications/evaluation-of-smart-irrigation-systems-in-hot-arid-climates-for-g/)<br>doi:10.1108/SASBE-11-2021-0201 | **Medium**: Decision-support evaluation of IoT smart irrigation options for urban green infrastructure in a hot-arid city; useful for the framework-paper path. | None | — | HTTP 200 (Aalborg portal); Emerald DOI returned 500 at check |

### Kuwait

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| K1 | **Irrigation Studies in Date Palm Phase II: Development of Precision Irrigation Scheduling Under Kuwait's Environmental Conditions**<br>KISR team (KFAS-funded project page) | Kuwait Institute for Scientific Research (KISR) | n.d., KFAS research project | [link](https://research.kfas.org.kw/en/projects/ca687ca2-9f38-4959-87f4-873161a3870d/) | **Low**: Precision scheduling, regulated deficit and subsurface irrigation for date palm in Kuwait. | None | — | HTTP 200 |

### Lebanon

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| L1 | **Soil Moisture or ET-Based Smart Irrigation Scheduling: A Comparison for Sweet Corn with Sap Flow Measurements**<br>G. Asiimwe; H.H. Jaafar; M.A. Haidar; R.M. Mourad | American University of Beirut (AUB) | 2022, J. Irrigation and Drainage Engineering 148(6) | [link](https://scholarworks.aub.edu.lb/items/f50eb39f-71be-4d26-a040-32ad3fdfbbf6)<br>doi:10.1061/(ASCE)IR.1943-4774.0001668 | **Medium**: Field comparison of soil-moisture vs ET scheduling (CS655 sensors); ET used 8% less water at same grain yield. Part of AUB's SIML smart-irrigation project. | None public | — | HTTP 200 (AUB ScholarWorks) |

### Jordan / Turkey / Lebanon

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| J1 | **FLOW-AID – a Deficit Irrigation Management System using Soil Sensor Activated Control: Case Studies**<br>J. Balendonck; A. Pardossi; H. Tuzel; Y. Tuzel; M. Rusan; F. Karam | JUST (Jordan), Ege Univ. (Turkey), LARI (Lebanon), WUR, Pisa | 2010, 3rd Int. Symp. Soil Water Measurement, Murcia | [link](https://edepot.wur.nl/139559) | **Medium**: Wireless soil-sensor-activated controllers + DSS tested in Jordan, Turkey and Lebanon; 16–69% water saving reported (search summary). | None | — | HTTP 200 (PDF read) |

### Egypt

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| E1 | **Improving the spatial deployment of the soil moisture sensors in smart irrigation systems using GIS**<br>Y. Arafa; A.M. El-Gindy; M. El-Shirbeny; M. Bourouah; A.M. Abd-ElGawad; Y.M. Rashad; M. Hafez; M.A. Youssef | Ain Shams University | 2024, Cogent Food & Agriculture | [link](https://scholar.asu.edu.eg/handle/123456789/220544)<br>doi:10.1080/23311932.2024.2361124 | **High**: GIS-based optimal placement of soil-moisture sensors (NodeMCU, calibrated VWC). Directly relevant to where to put sensors in each pilot zone (R2). | Unknown | — | HTTP 200 (Ain Shams Scholar) |

### Türkiye

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| T1 | **The Effects of AI-Supported Autonomous Irrigation Systems on Water Efficiency and Plant Quality: A Case Study of Geranium psilostemon Ledeb.**<br>G. Ercan Oğuztürk; C. Murat; M. Yurtseven; T. Oğuztürk | Recep Tayyip Erdoğan University | 2025, Plants 14(5):770 | [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC11902001/)<br>doi:10.3390/plants14050770 | **Medium**: AI autonomous irrigation of an ornamental vs manual: 87.97% less water with plant-quality outcomes measured. Pairs water and plant-condition outcomes like R1+R4. | See article (not checked) | — | HTTP 200 (PMC) |

### Israel

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| I1 | **Modeling tree responses to soil water variability guides irrigation to account for soil winter reserves**<br>O. Sperling; T. Kamai; I. Gardi; M.A. Zwieniecki; G. Marino | Volcani Institute (ARO) | 2025, Vadose Zone Journal | [link](https://doi.org/10.1002/vzj2.20385)<br>doi:10.1002/vzj2.20385 | **Low**: Soil-water-driven tree transpiration model for automated precision irrigation; relevant to tree zones. | Unknown | — | Search index; Wiley 403 to curl |

### Iran

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| IR1 | **Effectiveness of smart green-space irrigation systems in reducing consumption (case study: Razi Park, Tehran) [Persian]**<br>A.N. Saeedozakerin; B. Nazari; H. Ramezani Etedali (transliterated) | Imam Khomeini International University | n.d., J. Water and Sustainable Development (Ferdowsi Univ. Mashhad) | [link](https://jwsd.um.ac.ir/article_31325.html) | **High**: Smart controller on ~2,500 m² urban park vs manual: 6% (monthly) and 15% (weekly) saving; ~10.6 L/m² saved. One of very few urban-park smart-vs-manual comparisons in the region. | None | — | HTTP 200 (page fetched) |

### Morocco

| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |
|---|---|---|---|---|---|---|---|---|
| M1 | **Dataset on Agrometeorological Parameters in the Souss-Massa Plain**<br>H. Ait-Ichou (corr.); M. Hssaisoune; … L. Bouchaou (31 authors) | Ibn Zohr Univ., Cadi Ayyad Univ., UM6P/IWRI, Ibn Tofail Univ. | 2026, Data 11(8):191 | [link](https://atlas.um6p.ma/p/en/research-outputs/dataset-on-agrometeorological-parameters-in-the-souss-massa-plain)<br>doi:10.3390/data11080191 | **High**: OPEN DATA: 2019–2022 citrus orchard eddy-covariance station, soil moisture/temp/EC 5–80 cm, weather, fluxes; 30-min CSV; CC-BY 4.0 at data.mendeley.com/datasets/rg4yb8m5sf/1. Usable for R2/R3 prototyping in a semi-arid setting. | Open (CC-BY 4.0) | — | HTTP 200 (UM6P page + Mendeley dataset) |

## 3. Open Middle East / North Africa datasets

| Dataset | Country | Licence | Link | Note |
|---|---|---|---|---|
| Al-Khanasri soil moisture / irrigation, Jordan (ICARDA) | Jordan | CC-BY-SA | [link](https://data.mel.cgiar.org/dataset.xhtml?persistentId=hdl%3A20.500.11766.1%2FFK2%2F7S3BIP) | From the earlier IoT shortlist (#16) |
| IoT Agriculture 2024 (Tikrit University) | Iraq | CC BY-ND | [link](https://www.kaggle.com/datasets/wisam1985/iot-agriculture-2024) | From the earlier IoT shortlist (#17) |
| Souss-Massa agrometeorological + soil moisture (citrus) | Morocco | CC-BY 4.0 | [link](https://data.mendeley.com/datasets/rg4yb8m5sf/1) | NEW this run (M1) |
| ICBA MENA soil-moisture data portal | UAE (regional) | Open portal (terms not checked) | [link](https://data.biosaline.org/) | Coarse gridded data, not plot level |

No new open **Saudi or GCC** plot-level irrigation, soil-moisture or plant-condition dataset was found. The Saudi papers above either state data are available on request (S1, S2, S11) or publish none. The only new open regional dataset this run is the Moroccan Souss-Massa citrus station (M1).

## 4. Caveats

- Author lists for S2, S3, S4 (first author only), S13, S14 and S15 come from search-index records rather than a fetched article page; S3's author (N.K. Shammas) and S15's PNU affiliations are marked unverified.
- U1 (Dubai) returned HTTP 500 from both the DOI and the PDF host at check time; it is kept because it is the only Gulf urban-landscape smart-vs-timer comparison, but treat it as unverified.
- S12 (Al-Aziziah, Hail) is a Saudi site but the authors are at Cranfield University; S16 is listed on KFUPM's portal but was externally published from Zhejiang University.
- IR1 is in Persian; author names are transliterated.
- Excluded as off-topic: an ML urban-landscaping paper found in the UAE search turned out to be from Mexico/US authors; a PNU-funded paper (Blessy et al. 2023) uses Indian banana data.

## 5. Suggested next steps

1. Ask KSU (Alazba/Elkatoury) for the PCMT site data and Riyadh plant coefficients, the natural ET-based comparator for the pilot.
2. Ask KFU (memohammed@kfu.edu.sa) for sensor logs from the date-palm IoT trials to test the R2 ingestion schema.
3. Use M1 (Souss-Massa, open) together with NCM Riyadh weather to prototype the sensor_log and ET0 pipelines.
4. Cite S3, U1, IR1 and O2 as regional effect-size priors for the power calculation (savings of roughly 6–26% for landscape controllers, higher for agriculture).

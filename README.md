# Green Riyadh AIoT smart-irrigation pilot: project folder

Assembled 1 November 2026 (Asia/Riyadh, UTC+3). Open **index.html** in a browser for the dashboard.

## Study design (from docs/Green_Riyadh_requirements.pdf)
- 24 irrigation zones in 12 matched pairs (AIoT recommendation vs standard practice), 4-week baseline then 8-week intervention: 2,016 zone-days.
- Outcomes: applied water in L/m²/day (metered) and plant condition; analysis by difference-in-differences with **pairs as the replicate** (avoid pseudoreplication).
- Target files: zone register, daily zone-day file, sensor_log, irrigation_events, plant_health.
- Data requirements R1–R5: R1 metered water per zone with area (missing ≠ zero); R2 hourly soil moisture with sensor_id, unit and quality flag; R3 weather and ET0; R4 plant condition; R5 design and logs (pairs, phase, recommendation/override).

## Contents
| Path | What |
|---|---|
| index.html | Self-contained dashboard (no internet needed except for outbound links) |
| dashboard_preview.png | Screenshot of the dashboard |
| data-sources/irrigation_data_sources.(md/html/pdf) | 12 public irrigation / urban-greening datasets scored against R1–R5, weather sources, author contacts |
| data-sources/iot_agriculture_datasets.(md/html/pdf) | 17 public IoT-in-agriculture datasets |
| research/middle_east_research.(md/pdf) | 30 Middle East / North Africa research items (new this run) |
| contacts/authors_contacts.(md/pdf) | Combined contact list (earlier + Middle East) |
| docs/Green_Riyadh_requirements.pdf | The study requirements document |
| _build/ | Python scripts used to generate the reports and the dashboard |

Nobody has been contacted and nothing has been sent.

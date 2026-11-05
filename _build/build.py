import json, re, subprocess, markdown, os
from data import ME, ME_DATASETS, IRR, IOT, MAP, UNMAPPED
P="/workspace/green-riyadh-project"
TODAY="5 November 2026 (Asia/Riyadh, UTC+3)"
CSS="""body{font-family:Arial,Helvetica,sans-serif;font-size:11px;line-height:1.45;color:#1b2b1b;margin:24px}
h1{color:#1b5e20;font-size:20px}h2{color:#2e7d32;font-size:15px;border-bottom:2px solid #a5d6a7;padding-bottom:3px;margin-top:22px}h3{color:#388e3c;font-size:13px}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:9.5px}th,td{border:1px solid #c8e6c9;padding:4px 5px;vertical-align:top;text-align:left}
th{background:#e8f5e9}tr:nth-child(even) td{background:#f7fbf7}a{color:#1565c0;word-break:break-all}code{background:#eef5ee;padding:1px 3px}"""
def md2pdf(md_path):
    html=markdown.markdown(open(md_path).read(),extensions=['tables','fenced_code'])
    hp=md_path[:-3]+".html"; pdf=md_path[:-3]+".pdf"
    open(hp,'w').write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html}</body></html>")
    subprocess.run(["google-chrome","--headless","--no-sandbox","--disable-gpu","--no-pdf-header-footer",f"--print-to-pdf={pdf}",f"file://{hp}"],check=True,capture_output=True)
def esc(s): return (s or "").replace("|","/")
# ---------- research md ----------
order={"High":0,"Medium":1,"Low":2}
L=[f"# Middle East university research relevant to Green Riyadh AIoT smart irrigation","",f"Compiled {TODAY}. Search of web indexes, university repositories (Pure portals, ScholarWorks) and publisher pages. Nobody was contacted.","",
"**How to read this:** *Relevance* is relevance to the 24-zone matched-pair pilot (L/m²/day + plant condition, DiD). *Data* is public data availability. *Check* records how the URL was verified on 1 Nov 2026: `HTTP 200` = curl or fetch succeeded; MDPI, Wiley, ASCE and Taylor & Francis block automated requests with 403, so for those the record was confirmed through the search index or a successful page fetch. Emails are listed only where printed on a real page.","",
f"Items: **{len(ME)}** ({sum(1 for m in ME if m['country'].startswith('Saudi'))} Saudi). Open Middle East / North Africa datasets: see section 3.","",
"## 1. Top picks for the pilot","",
"| # | Item | University | Why it matters |","|---|---|---|---|"]
top=["S1","S2","S3","S9","S5","O1","O2","U1","IR1","E1","M1"]
for t in top:
    m=next(x for x in ME if x['id']==t)
    L.append(f"| {t} | [{esc(m['title'])}]({m['url']}) ({m['year'] or 'n.d.'}) | {esc(m['uni'])}, {m['country']} | {esc(m['note'])} |")
L+=["","## 2. Full list by country","",]
countries=[]
for m in ME:
    if m['country'] not in countries: countries.append(m['country'])
for c in countries:
    L+=[f"### {c}","","| # | Title / authors | University | Year, venue | Link / DOI | Relevance | Data | Corresponding email | Check |","|---|---|---|---|---|---|---|---|---|"]
    for m in sorted([x for x in ME if x['country']==c],key=lambda x:order[x['rel']]):
        doi=f"<br>doi:{m['doi']}" if m['doi'] else ""
        L.append(f"| {m['id']} | **{esc(m['title'])}**<br>{esc(m['authors'])} | {esc(m['uni'])} | {m['year'] or 'n.d.'}, {esc(m['venue'])} | [link]({m['url']}){doi} | **{m['rel']}**: {esc(m['note'])} | {esc(m['data'])} | {m['email'] or '—'} | {esc(m['verified'])} |")
    L.append("")
L+=["## 3. Open Middle East / North Africa datasets","","| Dataset | Country | Licence | Link | Note |","|---|---|---|---|---|"]
for d in ME_DATASETS: L.append(f"| {d['name']} | {d['country']} | {d['lic']} | [link]({d['url']}) | {d['note']} |")
L+=["","No new open **Saudi or GCC** plot-level irrigation, soil-moisture or plant-condition dataset was found. The Saudi papers above either state data are available on request (S1, S2, S11) or publish none. The only new open regional dataset this run is the Moroccan Souss-Massa citrus station (M1).","",
"## 4. Caveats","",
"- Author lists for S2, S3, S4 (first author only), S13, S14 and S15 come from search-index records rather than a fetched article page; S3's author (N.K. Shammas) and S15's PNU affiliations are marked unverified.",
"- U1 (Dubai) returned HTTP 500 from both the DOI and the PDF host at check time; it is kept because it is the only Gulf urban-landscape smart-vs-timer comparison, but treat it as unverified.",
"- S12 (Al-Aziziah, Hail) is a Saudi site but the authors are at Cranfield University; S16 is listed on KFUPM's portal but was externally published from Zhejiang University.",
"- IR1 is in Persian; author names are transliterated.",
"- Excluded as off-topic: an ML urban-landscaping paper found in the UAE search turned out to be from Mexico/US authors; a PNU-funded paper (Blessy et al. 2023) uses Indian banana data.",
"",
"## 5. Suggested next steps","",
"1. Ask KSU (Alazba/Elkatoury) for the PCMT site data and Riyadh plant coefficients, the natural ET-based comparator for the pilot.",
"2. Ask KFU (memohammed@kfu.edu.sa) for sensor logs from the date-palm IoT trials to test the R2 ingestion schema.",
"3. Use M1 (Souss-Massa, open) together with NCM Riyadh weather to prototype the sensor_log and ET0 pipelines.",
"4. Cite S3, U1, IR1 and O2 as regional effect-size priors for the power calculation (savings of roughly 6–26% for landscape controllers, higher for agriculture).",
]
open(f"{P}/research/middle_east_research.md","w").write("\n".join(L)+"\n")
md2pdf(f"{P}/research/middle_east_research.md")
# ---------- contacts ----------
src=open("/workspace/irrigation_data_sources.md").read()
sec5=src[src.index("## 5. Author contacts"):src.index("## 6. Gaps")]
sec5=sec5.replace("## 5. Author contacts (public sources only; nobody has been contacted)","## A. Contacts from the earlier dataset search (copied from data-sources/irrigation_data_sources.md)").replace("### 5.","### A.")
C=["# Green Riyadh: author contacts","",f"Updated {TODAY}. Public sources only. **Nobody has been contacted.** Verify any email before use.","",sec5,
"## B. Middle East corresponding authors (new this run)","",
"Only one email was printed on a page we could read. For the others, the corresponding author is named but no address was captured; get it from the article PDF or university directory before writing.","",
"| Person | University | Paper | Contact | Status |","|---|---|---|---|---|",
"| Dr Maged Mohammed (corresponding) | King Faisal University, Date Palm Research Center, Al-Ahsa | S5 Sensors 2021; S6 IntechOpen 2023; S7 Agronomy 2023 | memohammed@kfu.edu.sa | Printed on MDPI PDF and IntechOpen page |",
"| Prof. A.A. Alazba / Dr Ahmed Elkatoury | King Saud University, Agricultural Engineering | S1 Water 2024; S2 Water 2025 | Not captured (Elkatoury ORCID 0000-0002-0111-2157 seen in search index) | Get from MDPI article page |",
"| Dr Hussein M. Al-Ghobari | King Saud University | S4 SJAR 2016 | Not captured | Get from article PDF |",
"| Jiaqi Zheng | KAUST | S9 SIMBA dissertation | Not captured | Supervisor not identified yet |",
"| S. Habib (corresponding) | Qassim University | S8 Electronics 2022 | Not captured | Corresponding author marked on MDPI page; email not shown in the fetched text |",
"| Marran Al Qwaid | Shaqra University | S11 Sci Rep 2026 (data on request) | Not captured | Corresponding author not confirmed |",
"| Dr Yaseen A. Al-Mulla (corresponding) | Sultan Qaboos University | O1 IJAB 2021 | Not captured | Corresponding author per SQU Pure |",
"| Sara M. Zaina (corresponding) / Dr Fodil Fadli | Qatar University | Q1 SASBE 2022 | Not captured | Corresponding author per Aalborg portal |",
"| Dr Hadi H. Jaafar | American University of Beirut | L1 JIDE 2022 | Not captured | Corresponding author not confirmed |",
"| Yasser Arafa | Ain Shams University | E1 Cogent 2024 | Not captured | First author |",
"| Hamza Ait-Ichou (corresponding) | Ibn Zohr University, Morocco | M1 Data 2026 (open dataset) | Not needed for download | Corresponding author per UM6P portal |",
"","Suggested order of approach: Alazba/Elkatoury (KSU) → Mohammed (KFU) → Al-Mulla (SQU) → Zheng (KAUST).",""]
open(f"{P}/contacts/authors_contacts.md","w").write("\n".join(C))
md2pdf(f"{P}/contacts/authors_contacts.md")
# ---------- README ----------
R=f"""# Green Riyadh AIoT smart-irrigation pilot: project folder

Assembled {TODAY}. Open **index.html** in a browser for the dashboard.

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
| research/middle_east_research.(md/pdf) | {len(ME)} Middle East / North Africa research items (new this run) |
| contacts/authors_contacts.(md/pdf) | Combined contact list (earlier + Middle East) |
| docs/Green_Riyadh_requirements.pdf | The study requirements document |
| _build/ | Python scripts used to generate the reports and the dashboard |

Nobody has been contacted and nothing has been sent.
"""
open(f"{P}/README.md","w").write(R)
# ---------- dashboard ----------
D=dict(me=ME,meds=ME_DATASETS,irr=[dict(rank=r[0],name=r[1],r1=r[2],r2=r[3],r3=r[4],r4=r[5],r5=r[6],setting=r[7],url=r[8],country=r[9]) for r in IRR],
       iot=[dict(n=r[0],name=r[1],cat=r[2],country=r[3],lic=r[4],url=r[5]) for r in IOT],
       map=MAP,unmap=UNMAPPED)
tpl=open("dashboard_template.html").read()
world=open("world_land_path.txt").read().strip()
html=tpl.replace("/*__DATA__*/","const DATA="+json.dumps(D,ensure_ascii=False)+";").replace("__TODAY__",TODAY).replace("__NME__",str(len(ME))).replace("__WORLD_PATH__",world)
open(f"{P}/index.html","w").write(html)
print("built", len(ME), "map", len(MAP), "unmap", len(UNMAPPED))

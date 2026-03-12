---
name: country-context-tanzania
description: Tanzania country context for business plan generation. Covers currency (TZS), tax rates (TRA/EFD), regulatory bodies (TIC, BRELA, NEMC, TBS, BOT, TCRA), banking (Bank of Tanzania, CRDB, NMB, mobile money 54.6M accounts), labour market, macro data (Budget Execution Report Q1 2025/26, Afrexim 2025, AfDB CSP 2025, IMF Report July 2025, KNBS). Load this file when generating a Tanzania business plan.
---

# Tanzania Country Context

## How to Use

When generating any business plan section for a Tanzania-based business, substitute:
- **TZS** for UGX
- **TRA** for URA; **EFD** for EFRIS; **TANCIS** for the Uganda customs system
- Tanzania PAYE bands (see Section 4) for Uganda bands
- Tanzania regulatory bodies (Section 5) for Uganda ones
- Tanzania banking institutions (Section 6) for Uganda ones
- Tanzania salary bands (Section 7) for Uganda bands

Universal frameworks always apply: CAMPARI, DSCR ≥ 1.25×, Minto Pyramid, Rasiel MECE, Damodaran valuation, 4Ps/7Ps, Golden Circle.

**Detailed reference files:**
- `references/tanzania-investment-climate.md` — TIC investment data, Tanzania Investment Act 2022, SEZ/EPZ, OSFC registration process, trade agreements, financial sector detail, risk summary
- `references/tanzania-demographics-education.md` — Norad/AfDB: population (69M, 2.9% growth), age structure, fertility, labour market, education enrolment, LAYS, higher education system

**Live metrics file:** `references/economic-metrics.csv` — run `python tools/scrape_metrics.py tanzania` to populate.

---

## 1. Basic Country Information

| Field | Value |
|-------|-------|
| Country | United Republic of Tanzania |
| Political capital | Dodoma |
| Commercial/economic hub | Dar es Salaam |
| Primary languages | Kiswahili (official, national), English (official) |
| Currency | Tanzanian Shilling |
| Currency code | **TZS** |
| Exchange rate (Q1 2025 average) | TZS 2,458.60 per USD (Budget Execution Report) |
| Exchange rate (2024 average) | TZS 2,598 per USD (9% depreciation in 2024) |
| **Conservative planning rate** | **TZS 2,700 per USD** (buffer for volatility; Afrexim projects TZS 2,964 by end-2025) |
| Rate source | Tanzania Budget Execution Report Q1 FY2025/26; Afrexim Country Brief September 2025 |
| President | Samia Suluhu Hassan (assumed office March 2021) |
| General elections | October 2025 |

---

## 2. Macroeconomic Context

| Indicator | Value |
|-----------|-------|
| GDP (nominal) | USD 80–91 billion (Afrexim: USD 80B; AfDB: USD 90.9B, 2024) |
| GDP per capita | USD 1,336 (AfDB 2024); *lower-middle income since July 2020* |
| Real GDP growth 2024 | **5.6%** (Afrexim; AfDB projected) |
| Real GDP growth Q1 2025 (Apr–Jun) | **6.3%** — highest quarterly rate in recent years (Budget) |
| GDP growth forecast 2025 | 6.0–6.1% (Afrexim; AfDB) |
| GDP growth forecast 2026 | 6.0% (Afrexim) |
| GDP growth average 2000–2023 | ~6% per annum (Norad) |
| Inflation (headline, 2024) | **3.5%** (Afrexim); within 3–5% target |
| Inflation (September 2025) | **3.4%** — core 2.2%; food 7.0%; energy 3.7% (Budget) |
| Inflation target | 3–5% national; EAC convergence ≤8%; SADC 3–7% |
| Fiscal deficit | 3.0% of GDP (2024); narrowing — projected 2.8% (2026) (Afrexim) |
| Public debt | 47.6–52% of GDP (varies by source/year; IMF-WB DSF threshold: 55%) |
| External debt | USD 37.8B; 47.2% of GDP (2024) (Afrexim) |
| Tax revenue | ~11.5–12% of GDP (well below SSA average of 16.3%) |
| Total government revenue | ~15.5% of GDP (including grants) |
| Foreign reserves | USD 6,664 million = **5.1 months** import cover (Sept 2025) |
| Gross capital formation | 37.7–39.3% of GDP (high investment rate) |
| Private investment | 11.6% of GDP; FDI declined from 5.7% (2010) to 1.7–2% (2023) (IMF/AfDB) |
| Major sectors | Services 39.5–43%; Agriculture 25.8–27%; Industry 31.2% |
| Agriculture employment | 65.5% of labour force (2022) |
| Mining growth | 19.0% (Q1 2025); 10.1% of GDP (2024) |
| Primary data source | National Bureau of Statistics (NBS) — nbs.go.tz |
| Secondary sources | Afrexim Country Brief Sept 2025; AfDB CSP Oct 2025; IMF Country Report July 2025; Budget Execution Report Q1 FY2025/26 |

**Fastest-growing sectors (Q1 2025):**
- Mining & Quarrying: +19.0%
- Finance & Insurance: +14.8%
- Electricity: +14.0%
- ICT: +11.1%

**Top sectoral contributions to Q1 2025 6.3% growth:** Agriculture (16.3%), Mining (15.4%), Construction (12.0%), Finance & Insurance (9.7%), Trade (7.3%), Manufacturing (5.9%)

---

## 3. Business Registration and Legal Structure

| Element | Detail |
|---------|--------|
| Company registry | **BRELA** (Business Registrations and Licensing Agency) — brela.go.tz |
| Investment facilitation | **TIC** (Tanzania Investment Centre) — tic.go.tz |
| One-stop centre | **OSFC** (One Stop Facilitation Centre) at TIC — handles 14 MDAs |
| Primary legal structures | Private limited company; public company; sole proprietorship; partnership; branch of foreign company; NGO |
| Most common SME structure | **Private Limited Company** |
| Tanzania Investment Act | **Act No. 10 of 2022** (replaced prior Act); Regulations 2023 |
| **Foreign investor minimum capital** | **USD 50 million** (Tanzania Investment Act 2022) |
| **Local investor minimum capital** | **USD 20 million** (revised down from USD 50K to encourage domestic investment) |
| Strategic investor | Determined by capital amount and national priorities |
| OSFC services (all in one location) | Certificate of Incentives; Company Registration; Business & Industrial Licences; Residence & Work Permits; Land Acquisition; Environment Certificates; Standards Certificates; Food & Drug Licences; OHS Compliance; TIN; Tax Exemptions |
| Land — new rule (2023) | New Land Policy (passed Parliament 13 Feb 2025): foreign investors can now acquire land for investment — allocated based on capital amount and national priorities |
| Annual reporting | Investors must submit annual progress reports to TIC; physical verification visits (PVVs) conducted |
| Foreign ownership | Generally open; sector-specific restrictions apply |

**Standard registration steps:**
1. Name search and reservation — BRELA online
2. Company registration — BRELA (via OSFC for TIC-registered projects)
3. Tax Identification Number (TIN) — TRA
4. Business Licence — Ministry of Investment, Trade & Industry / Local Government
5. Social security registration — NSSF / PSSSF
6. Sector-specific licences (TBS, TFDA, TCRA, etc.)
7. For investments ≥ threshold: TIC Certificate of Incentives

---

## 4. Taxation

| Tax | Rate / Rule |
|-----|-------------|
| **Corporate income tax** | **30%** (standard; confirmed by budget collections pattern) |
| **VAT** | **18%** (standard; VAT on imports + domestic sales per Budget) |
| VAT registration threshold | [verify with TRA — estimated TZS 100–200 million/year] |
| VAT filing | Monthly via TRA online system; **EFD (Electronic Fiscal Device)** mandatory for all VAT-registered businesses |
| **PAYE — indicative bands** | Progressive: 0% (low bracket) → top rate likely 30% — *verify current year bands with TRA; not detailed in source documents* |
| **NSSF** | National Social Security Fund — employee + employer contributions [verify current rates] |
| **PSSSF** | Public Service Social Security Fund — for public sector employees |
| WHT — dividends | [verify with TRA] |
| WHT — consultancy/professional fees | [verify with TRA] |
| WHT — rent | [verify with TRA] |
| Withholding taxes | Q1 2025 collection: TZS 572.2 billion (140.1% of target; 45.5% YoY growth) (Budget) |
| Import duty | General: 0%, 10%, 25% EAC Common External Tariff bands; food/beverages: 25%; petroleum excise separate |
| **Railway Development Fund** | Applied to most imports (similar to Kenya RDL) |
| Business Skills Development Levy | Applies to payroll |
| HIV Response Levy | Additional levy on business income |
| Industrial Development Levy | [verify rate] |
| Fuel levy and transit fee | Separate from import duty |
| Tax authority | **TRA** (Tanzania Revenue Authority) — tra.go.tz |
| Customs system | **TANCIS** (Tanzania Customs Management System) — upgraded and relaunched January 2025 |
| Electronic fiscal receipting | **EFD** (Electronic Fiscal Devices) — mandatory for VAT-registered businesses |
| Tax compliance | TRA issues Tax Clearance Certificates for government tenders and major transactions |
| AML/CFT | Not on FATF grey list (as of 2025 sources) |

*PAYE bands and NSSF rates: verify current year with TRA (tra.go.tz). Source documents confirmed collections but did not reproduce band tables.*

**Q1 FY2025/26 Tax Revenue Performance (Budget Execution Report):**
- Total tax revenue collected: TZS 7,962.0 billion (108.6% of target)
- Income tax: TZS 2,905.2 billion (114.9% of target; +25.6% YoY)
- Corporate tax: TZS 1,053.9 billion (115.1% of target; +29.1% YoY)
- PAYE: TZS 1,025.7 billion (104.9% of target; +16.1% YoY)
- VAT on imports: TZS 1,304.5 billion (107.8% of target; +19.7% YoY)
- VAT on domestic sales: TZS 1,245.3 billion (101.6% of target)
- Withholding taxes: TZS 572.2 billion (140.1% of target; +45.5% YoY)

---

## 5. Regulatory Bodies (by Sector)

| Sector | Body |
|--------|------|
| Business licensing / company registry | **BRELA** (Business Registrations and Licensing Agency) — brela.go.tz |
| Investment promotion / facilitation | **TIC** (Tanzania Investment Centre) — tic.go.tz |
| Taxation | **TRA** (Tanzania Revenue Authority) — tra.go.tz |
| Environmental | **NEMC** (National Environment Management Council) — nemc.go.tz |
| Food, drugs & cosmetics | **TFDA / TMDA** (Tanzania Food and Drug Authority / Tanzania Medicines and Medical Devices Authority) |
| Quality standards | **TBS** (Tanzania Bureau of Standards) — tbs.go.tz |
| Financial services — banking | **BOT** (Bank of Tanzania) — bot.go.tz |
| Financial services — insurance | **TIRA** (Tanzania Insurance Regulatory Authority) — tira.go.tz |
| Capital markets / securities | **CMSA** (Capital Markets and Securities Authority) — cmsa.go.tz |
| Stock exchange | **DSE** (Dar es Salaam Stock Exchange) — dse.co.tz |
| Telecommunications / ICT | **TCRA** (Tanzania Communications Regulatory Authority) — tcra.go.tz |
| Energy | **EWURA** (Energy and Water Utilities Regulatory Authority) — ewura.go.tz |
| Labour / employment | **Ministry of Labour, Employment and Youth Development** |
| Immigration / work permits | **Immigration Department** — immigration.go.tz |
| Agriculture inputs | **TOSCI** (Tanzania Official Seed Certification Institute); **TPRI** |
| Intellectual property | **BRELA** (trademarks, patents, industrial designs); **COSOTA** (copyright) |
| Science, technology, innovation | **COSTECH** (Tanzania Commission for Science and Technology) — costech.or.tz |
| Statistics | **NBS** (National Bureau of Statistics) — nbs.go.tz |
| Higher education quality | **TCU** (Tanzania Commission for Universities) |
| Competition | **FCAMC** (Fair Competition and Mediation Commission, formerly FCC) |

---

## 6. Banking and Finance

| Element | Detail |
|---------|--------|
| Central bank | **Bank of Tanzania (BOT)** — bot.go.tz |
| Commercial lending rate | **15.14%** (Q1 2025 average; Budget) |
| Time deposit rate | **8.64%** (Q1 2025 average) |
| Negotiated deposit rate | **10.92%** (Q1 2025 average) |
| Number of banks | 44 licensed commercial and community banks (Afrexim 2025) |
| Top 6 banks (60% of assets) | CRDB Bank, NMB Bank, National Bank of Commerce, Exim Bank Tanzania, Stanbic Bank, People's Bank of Zanzibar |
| Banking sector assets | TZS 62.2 trillion (~USD 25.2 billion) — 14.6% YoY growth (Afrexim 2024) |
| Capital adequacy ratio | 19.3% (well above 12% minimum) |
| Liquidity ratio | 29% (above 20% minimum) |
| Non-performing loans | **3.3%** (2024; improved from 4.3% in 2023) |
| Domestic credit to private sector | 16.4% of GDP (2023) — *lowest in EAC region; major constraint on SME growth* (IMF) |
| Credit growth | 16.1% (Q1 2025) |
| Mobile money | **54.6 million active accounts** (June 2024); TZS 117.1 trillion in transactions — M-Pesa (Vodacom), Tigo Pesa, Airtel Money |
| Financial inclusion | **76.5%** of adults using formal financial services (2023; up from 65% in 2017) |
| Microfinance providers | 50,000+ |
| Insurance companies | 40 (insurance + reinsurance) |
| Capital markets | DSE (Dar es Salaam Stock Exchange) |
| Development finance | TIB Development Bank; Tanzania Agricultural Development Bank (TADB); TPSC |
| Foreign exchange | Fully liberalised; managed float; TZS appreciated 9.7% in Q1 2025 (USD 2,459 vs 2,696 in Q1 2024) |
| Foreign reserves | USD 6,664 million = 5.1 months import cover (Sept 2025) — exceeds 4-month benchmark |
| DSCR minimum | ≥ 1.25× (standard bank requirement) |

---

## 7. Labour Market

| Element | Detail |
|---------|--------|
| Total population | ~69 million (Afrexim 2025); 66.6 million (Norad 2023) |
| Population growth rate | **2.9%** per year (one of highest in world; SSA avg 2.7%) |
| Population projection 2030 | ~80 million (AfDB) |
| Median age | **17.2 years** (half of population under 17) |
| Dependency ratio | **84.4%** (high; declining slowly) |
| Agriculture employment | **65.5%** of total employment (2022) |
| Informal employment | **92.2%** of total (89.6% men; 95% women) |
| New labour market entrants | ~1 million youth per year; only **50,000–60,000** secure formal jobs annually |
| NEET (15–24, new ILO definition) | **23.8%** overall; females 29.5%, males 17.7% (2020, Norad) |
| Youth unemployment | 12.6% overall (ILO); female 40.6%, male 15.4% (AfDB) |
| Minimum wage | [Verify with Ministry of Labour — sector-specific minimums exist; national minimum not confirmed in sources] |
| **Indicative salary bands (Dar es Salaam)** | |
| — Unskilled / casual | TZS 200,000–400,000/month [ESTIMATE — verify] |
| — Semi-skilled / clerical | TZS 400,000–900,000/month [ESTIMATE — verify] |
| — Technical / skilled | TZS 900,000–2,500,000/month [ESTIMATE — verify] |
| — Professional / management | TZS 2,500,000–7,000,000/month [ESTIMATE — verify] |
| — Senior management | TZS 7,000,000–20,000,000+/month [ESTIMATE — verify] |
| Employer cost multiplier | × 1.10–1.15 of gross salary (NSSF + PSSSF + leave entitlement) [ESTIMATE] |
| Employment law | Employment and Labour Relations Act 2004 (Cap. 366); Workers Compensation Act 2015 |
| Annual leave | 28 working days/year minimum (Cap. 366) |
| Notice period | 28 days minimum |
| EAC nationals | No work permit required (EAC Common Market Protocol) |
| Non-EAC work permits | Class B work permit (employer-sponsored); TIC Certificate holders get expatriate entry |

*Salary bands are Dar es Salaam estimates for 2025; Mwanza, Arusha broadly similar. Regional rates lower.*

---

## 8. Key Market Data

| Indicator | Value |
|-----------|-------|
| Population | ~69 million (2025) |
| Population growth | **2.9%/year** |
| Population projection 2050 | 128 million (UN medium variant; Norad) |
| Urban population | ~35–40% (rapid urbanisation) |
| Dar es Salaam | Largest city; commercial and financial hub |
| Other major cities | Dodoma (capital), Mwanza, Arusha, Mbeya, Zanzibar City |
| Mobile money accounts | **54.6 million active** (June 2024) |
| Financial inclusion | 76.5% of adults (2023) |
| Key exports | Gold (42.5% of exports); precious metals; traditional: coffee, tea, cotton, cloves, cashews, sisal |
| Key imports | Petroleum/mineral oil (leading); capital goods 41.8% (vehicles, machinery, reactors) |
| Top export destinations | India 21.3%, South Africa 18.2%, UAE 14.6% |
| Top import sources | China 30.1%, India 15.8%, UAE 9.6% |
| Intra-African trade | USD 5.6 billion (21.3% of total trade, up from 18.6% in 2023) |
| Top intra-Africa export destinations | Nigeria 51.3%, Uganda 9.8%, DRC 9.4%, Rwanda 6.8%, Kenya 6.0% |
| Total trade (2024) | USD 26.1 billion (exports USD 11.3B, imports USD 14.8B) |
| Trade deficit | USD 3.5 billion (2024; significantly improved from USD 7.8B in 2023) |
| Current account deficit | 3.9% of GDP (2024); improving trend |
| Dar es Salaam port | 80 million tonnes cargo (2023); gateway to EAC and Central Africa |
| EAC membership | Full member — free trade, no tariffs within bloc |
| SADC membership | Full member |
| AfCFTA | Active — exporting to Ghana, Nigeria, South Africa |
| Electricity access | 78.4% national (2023); 69.8% rural (AfDB) |
| Power supply reliability | Generally improving; fewer outages vs regional average (only 34% of firms report outages vs 58% SSA avg) |
| Renewable energy share | 78.3% of total energy consumption (declining from 90% as economy grows) |
| Tourism | Significant earner — service exports USD 1,778.5M (Q1 2025); growing visitor numbers (+35.6% Q1 2025) |

---

## 9. Risk Context

| Risk | Detail |
|------|--------|
| Fiscal / debt stress | Public debt 47.6–52% of GDP; external debt service 25% of exports (exceeds DSF 20% benchmark); debt service to revenue 31.3% (exceeds 18% benchmark) — *not yet in distress but watch closely* (Afrexim) |
| Private investment crowding out | Public sector dominates capital formation (18.8% of GDP vs private 11.6%); FDI fell from 5.7% to 2% of GDP 2010–2023 (IMF) |
| Productivity decline | TFP contribution to growth was -2 ppts (2020–23); structural transformation stalled since 2014 (IMF) |
| Low credit penetration | Domestic credit to private sector 16.4% of GDP — lowest in EAC (Kenya 31.6%, Rwanda 22.7%) (IMF) |
| Tax revenue constraint | 12% of GDP vs SSA avg 16.3%; leaves limited fiscal space for social spending (AfDB) |
| Skills mismatch | 59% of young workers undereducated; 61% of graduates lack job market skills (employers surveyed); LAYS 4.5 years (Norad/IMF) |
| Youth unemployment gap | 1 million new entrants/year; only 50–60K formal jobs; informal sector absorbs remainder |
| Population growth pressure | 2.9%/year; dependency ratio 84.4%; rapid growth in school-age population requiring investment in teachers and classrooms |
| Political / election | October 2025 general elections — short-term uncertainty; incumbent President Samia has improved business climate (corruption score +11 since 2015) |
| Corruption | TI CPI score: 41/100 (2024; improved from 30 in 2015) — progress but still a business cost (IMF) |
| Business regulation burden | 92% of firms report meeting with tax officials (vs 70% SSA avg); 14% of management time on regulations (vs 8% SSA avg) (IMF World Bank Enterprise Survey) |
| Exchange rate volatility | TZS depreciated 9% in 2024; appreciated 9.7% in Q1 2025 — managed float with volatility |
| Deforestation / land | 10 percentage point decline in forest cover 2000–2022; new land policy (Feb 2025) opens foreign land ownership for investment |
| EUDR | EU Deforestation Regulation — affects coffee, cloves, cashews, cocoa exports from 2025 |
| Infrastructure gap | Only 8.3% of road network in good condition (AfDB); road density 9.6 km per 100 km² (IMF) |

---

## 10. Data Sources

- Tanzania Budget Execution Report for the Financial Year 2025-26 (Q1: July–September 2025). Ministry of Finance.
- Afrexim Bank. *Tanzania Country Brief*. September 2025.
- AfDB. *Tanzania Country Strategy Paper 2021–2025 Completion Report*. October 2025.
- IMF. *Country Report No. 25/164 — United Republic of Tanzania*. July 2025.
- Norad. *Demography, Economy and Education in Tanzania*. May 2025.
- Tanzania Investment Centre. *Quarterly Bulletin January–March 2025* (Q3 FY2024/25).
- East Africa Market Assessments — Tanzania Report. 2025.

**Detailed reference files:**
- `country-context/tanzania/references/tanzania-investment-climate.md`
- `country-context/tanzania/references/tanzania-demographics-education.md`

---

## 11. Plan Author Notes

```
Country: Tanzania
Completed by: Business Plan Skills project
Date completed: 12 March 2026
Sources: 7 PDFs — Budget Execution Report Q1 FY2025/26, Afrexim Sept 2025, AfDB Oct 2025, IMF July 2025, Norad May 2025, TIC Q3 2024/25 Bulletin, EA Market Assessment 2025
Conservative planning rate: TZS 2,700/USD (Afrexim projects TZS 2,964 by end-2025; Q1 2025 actual TZS 2,459)
Estimated fields (verify with TRA):
  - PAYE bands: source documents confirmed collections but did not tabulate bands
  - NSSF/PSSSF contribution rates: not detailed in sources
  - VAT registration threshold: estimated TZS 100–200M; verify with TRA
  - WHT rates: not tabulated in source documents
  - Minimum wage: sector-specific; verify with Ministry of Labour
  - Salary bands: indicative estimates — no survey data in sources
Known data gaps:
  - Detailed PAYE band table: request from TRA (tra.go.tz)
  - NSSF/PSSSF rates: check NSSF website (nssf.or.tz)
  - Full WHT schedule: TRA website or Income Tax Act 2004 (Cap. 332)
```

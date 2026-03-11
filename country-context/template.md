---
name: country-context-template
description: Fill in this template for any non-Uganda country context. Save the completed file as country-context/{country-name}.md. When a country file is present, all business plan skills will use it instead of Uganda defaults.
---

# Country Context File
## Instructions

Copy this file to `country-context/{country-name}.md` (e.g., `country-context/kenya.md`, `country-context/canada.md`, `country-context/fiji.md`).

Fill in every field based on your research. Mark any field you cannot source as `[ESTIMATE — verify]`.

When this file is present, Claude will use it as the regulatory and financial context for all plan sections. Uganda defaults apply only when no country file exists.

---

## 1. Basic Country Information

```
Country name:
Capital city:
Primary language(s):
Currency name:
Currency code (ISO 4217):            # e.g., KES, CAD, FJD
Exchange rate to USD (current):      # e.g., 1 USD = 130 KES
Exchange rate (conservative planning rate): # add 5–10% buffer for depreciation risk
Exchange rate source and date:
```

---

## 2. Macroeconomic Context

```
GDP (current, USD billions):
GDP per capita (USD):
Real GDP growth rate (latest year, %):
GDP growth forecast (next 2 years):
Inflation rate (latest, %):
   - Food inflation (%):
   - Energy inflation (%):
Unemployment rate (%):
Major economic sectors (ranked):
   1.
   2.
   3.
Primary data source (national statistics bureau):
Secondary source (World Bank, IMF, AfDB):
```

---

## 3. Business Registration and Legal Structure

```
Company registry name:
Company registry website:
Primary legal structures available:
   - [Structure 1]: [Key features, min shareholders, liability]
   - [Structure 2]:
   - [Structure 3]:
Most common SME structure:
Registration process summary:
   Steps: [numbered list]
   Timeline: [days]
   Cost (local currency):
Foreign ownership restrictions (if any):
Annual compliance requirements:
   - Annual return filing: [yes/no, deadline, cost]
   - Audit requirement (threshold):
   - Other:
```

---

## 4. Taxation

```
Corporate income tax rate (%):
Small business tax concession (if any):
   - Threshold:
   - Rate:
VAT/GST rate (%):
VAT registration threshold (local currency):
VAT filing frequency:
Personal income tax / PAYE bands:
   Band 1: [income range] — [rate]%
   Band 2: [income range] — [rate]%
   Band 3: [income range] — [rate]%
   Band 4: [income range] — [rate]%
Social security / payroll tax:
   - Employee contribution (%):
   - Employer contribution (%):
   - Name of scheme:
Withholding tax on:
   - Dividends (%):
   - Consultancy/professional fees (%):
   - Rent (%):
   - Interest (%):
Import duties (general rate):
Tax authority name:
Tax authority website:
Electronic invoicing requirement: [yes/no — details]
Tax compliance certificate required for: [government tenders / banking / other]
```

---

## 5. Regulatory Bodies (by Sector)

```
Business licensing authority: [name, website]
Environmental regulator: [name]
Food safety / quality standards: [name]
Health sector regulator: [name]
Financial services regulator (banking): [name]
Financial services regulator (insurance): [name]
Financial services regulator (microfinance): [name]
Telecommunications regulator: [name]
Energy regulator: [name]
Labour / employment authority: [name]
Immigration / work permits: [name]
Competition authority: [name]
Data protection authority: [name]
Other sector-specific regulators:
   [Sector]: [Regulator]
```

---

## 6. Banking and Finance

```
Central bank name:
Central bank policy rate (%):
Commercial bank lending rate (typical range, %):
Major commercial banks:
   1. [Bank name] — [SME lending focus, if any]
   2.
   3.
Development finance institutions:
   1. [Name] — [mandate, loan sizes, sectors]
   2.
Microfinance institutions / SACCOs:
   [Name] — [typical loan sizes, target clients]
Mobile money platforms: [name, penetration %]
Credit reference bureaus: [name]
Loan-to-value ratio (typical, property collateral, %):
DSCR minimum (typical bank requirement):
SME credit access (% of SMEs with bank credit):
```

---

## 7. Labour Market

```
Working-age population:
Labour force participation rate (%):
Unemployment rate (%):
Minimum wage (local currency / month or hour):
Minimum wage effective date:
Typical salary bands (indicative):
   Entry-level / unskilled: [range, local currency/month]
   Semi-skilled / clerical: [range]
   Technical / professional: [range]
   Management / senior: [range]
Employer cost multiplier (salary × [X] for total employment cost):
   Includes: [list — e.g., social security, insurance, statutory leave]
Key labour laws:
   Employment Act: [name, year]
   Leave entitlement: [days/year]
   Notice period (minimum): [weeks]
   Redundancy / severance: [formula]
Work permit requirement for foreign nationals: [yes/no — process]
```

---

## 8. Key Market Data

```
Population (total):
Population growth rate (%/year):
Urban population (%):
Major cities and populations:
   1. [City]: [population]
   2.
   3.
Internet penetration (%):
Smartphone penetration (%):
Formal retail penetration (%):
Key consumer spending categories:
   1. [Category]: [% of household expenditure]
   2.
   3.
Poverty rate (national poverty line, %):
Middle class definition and size:
Top trading partners (exports):
Top imports:
```

---

## 9. Risk Context

```
Political stability index (source):
Ease of Doing Business rank (year):
Corruption Perceptions Index score:
Key country-specific business risks:
   1. [Risk]: [brief description]
   2.
   3.
   4.
   5.
Exchange rate volatility (historical, %/year):
Inflation volatility (historical range):
Key regulatory risks:
   [Risk]: [description and mitigation]
Infrastructure risks:
   Power supply: [reliability, cost/kWh]
   Internet connectivity: [reliability, cost]
   Roads/logistics: [condition, cost benchmarks]
Climate/environmental risks:
   [Risk]: [description]
```

---

## 10. Data Sources Used to Complete This File

```
Source 1: [Full citation — name, organisation, URL, date accessed]
Source 2:
Source 3:
Source 4:
Source 5:
```

---

## 11. Plan Author Notes

```
Completed by:
Date completed:
Last verified:
Fields estimated (not sourced):
   [Field name]: [basis for estimate]
Known data gaps:
   [Gap]: [action to fill it]
```

---

## How Claude Uses This File

When this file exists in `country-context/`, all business plan skills will:

1. **Use the currency code and exchange rates** from Section 1 — replacing UGX with the local currency
2. **Use the tax rates** from Section 4 — replacing Uganda PAYE bands, corporate tax (30%), VAT (18%), EFRIS
3. **Use the regulatory bodies** from Section 5 — replacing KCCA, URA, UNBS, NEMA references
4. **Use the banking context** from Section 6 — replacing Centenary Bank, Stanbic, UDB references
5. **Use the salary benchmarks** from Section 7 — replacing Uganda wage bands
6. **Use the risk context** from Section 9 — replacing Uganda-specific risks table in Section 12 skill
7. **Retain all universal frameworks** — CAMPARI, DSCR ≥ 1.25×, TAM/SAM/SOM methodology, MECE, Pyramid Principle, Porter's Five Forces apply in every country

**Frameworks that are always universal (never country-specific):**
- Market sizing methodology (TAM/SAM/SOM, bottom-up)
- Financial ratios and bankability standards (DSCR, current ratio, debt/equity)
- Valuation methods (DCF, multiples, pre-revenue methods — Damodaran)
- Sales methodology (Schiffman, Keenan, PIPA, gap selling)
- Risk assessment (COSO ERM, Raydugin Bowtie, MECE risk register)
- Marketing frameworks (AARRR, 4Ps/7Ps, Kotler, guerrilla marketing)
- Golden Circle / mission-vision methodology (Sinek)
- Pyramid Principle / SCQA (Minto)
- McKinsey MECE and issue trees (Rasiel)

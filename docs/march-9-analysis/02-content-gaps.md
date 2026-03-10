# Content Gaps — Insufficient Depth for a Strong Plan

These skills exist but lack the reference material and frameworks needed to generate a genuinely strong, unique, bankable section. A plan generated from these skills today would be generic rather than compelling.

**Sources used for this analysis:**
- East Africa Macroeconomic Outlook 2025, Eastern Africa Association (EAA), London, January 2025
- African Trade Report 2025: African Trade in a Changing Global Financial Architecture, Afreximbank, Cairo 2025
- East African Economic Outlook 2025 (image-based PDF — key statistics cross-referenced from EAA report)

---

## GAP D1: Section 02 (Company Overview) — Empty Skill, No EA Legal Guidance

**Current state:** 44 lines, 0 reference files.

**What the skill generates today:**
A generic mission/vision/values narrative. Good for any country, specific to none.

**What a Ugandan bank actually needs to see in Company Overview:**

### Legal Structure in Uganda (none of this is in the skill)

| Structure | Registration Body | Annual Requirements | Best For |
|---|---|---|---|
| Sole Proprietorship | URSB business name | Business name renewal (UGX 20,000/yr) | Single-person, low-liability |
| Partnership | URSB deed registration | Annual renewal | 2–20 partners |
| Private Limited Company (Ltd) | URSB company registration | Annual return, audited accounts if large | Most SMEs seeking bank loans |
| Public Limited Company (PLC) | URSB + CMA | Annual return, listed financial statements | Large enterprises |
| Cooperative Society | Commissioner for Cooperatives | Annual general meeting, audit | Farmer groups, SACCOs |
| NGO/Foundation | NGO Bureau | Annual report, permit renewal | Social enterprise |

**Critical for lending:** Banks strongly prefer lending to Private Limited Companies over sole traders because:
1. The company is a separate legal entity — personal assets are ring-fenced
2. Financial statements can be audited independently
3. Directors are accountable in a traceable way
4. Succession is clearer — death of owner does not end the company

### Key URSB Documents Required by Banks
- Certificate of Incorporation / Business Name Certificate
- Memorandum and Articles of Association (for companies)
- Directors' and shareholders' register
- Trading licence (from KCCA or district local government)
- TIN / BRN certificate (URA tax registration — now equivalent to NIN/BRN from 1 July 2025)
- Sector-specific licences (e.g., UNBS product registration, NEMA permit, NDA licence for food)

### EA Regional Context (from EAA 2025)
With East Africa's economy projected to reach **$603 billion in GDP in 2025** and growing at **5.7%** — the fastest-growing region in Africa — the Company Overview should also position the business within this growth story. Plans targeting export markets (AfCFTA, EAC single market, UK Developing Countries Trading Scheme) or development finance must demonstrate awareness of the regional opportunity. The legal structure chosen affects cross-border trading eligibility: a registered Ugandan company can trade duty-free within EAC and access the UK Developing Countries Trading Scheme for quota-free, duty-free exports.

**What needs to be built:**
- `02-company-overview/references/uganda-legal-structures.md` — all business structures, registration process, costs, and bank preferences
- `02-company-overview/references/compliance-checklist.md` — mandatory registrations, licences, and annual obligations by business type and sector
- `02-company-overview/references/ea-regional-context.md` — EA economic overview, EAC trade framework, AfCFTA eligibility, and how to frame a Ugandan business within the regional growth narrative
- The SKILL.md should prompt the plan author to list all licences held and pending

---

## GAP D2: Section 11 (Funding Request) — Wrong Orientation for EA Market

**Current state:** 59 lines, 0 reference files. Written entirely for equity investors.

**Specific problems with the current skill:**

1. **Lists "IPO" as an exit strategy** — irrelevant for 99.9% of Ugandan SMEs
2. **Asks for a "capitalisation table"** — standard for startups, but most Ugandan businesses are sole proprietorships or family companies with no cap table
3. **No mention of loan repayment schedule** — this is the primary output banks want
4. **No mention of collateral** — the central question in every Ugandan bank loan application
5. **No mention of guarantors** — often required for loans above UGX 50M
6. **Valuation methodology** is relevant only for equity; for debt, the bank wants assets, income, and DSCR

**What a bank loan section actually needs:**

```
Loan Application Summary:
  Amount requested: UGX [X]
  Purpose: [Specific productive use — not "working capital" without detail]
  Loan term: [Years]
  Preferred structure: [Term loan / overdraft / asset finance / mortgage]
  Proposed repayment: [Monthly UGX X from [revenue source]]

Security Offered:
  Primary security: [Land title, LRV/Block/Plot details OR equipment value]
  Secondary security: [Motor vehicle, fixed deposit, personal guarantee]
  Estimated security value: UGX [X]
  Security coverage ratio: [X]% of loan amount

Debt Service Capacity:
  Monthly net income from operations: UGX [X]
  Proposed monthly loan repayment: UGX [X]
  DSCR: [X.Xx] (target: ≥1.25)
  Remaining monthly operating surplus: UGX [X]
```

### Africa Trade Finance Gap — Why This Matters (from AFREXIM 2025)
Africa's trade finance gap is estimated at **$100 billion annually** (Afreximbank, 2025). This gap is not from lack of bankable businesses — it is partly structural (banks under-serving SMEs, risk appetite, documentation requirements). The funding request skill must help businesses present themselves as fundable: correct documentation, correct structure, correct collateral narrative. A plan that uses investor pitch language instead of bank language will be returned by every commercial bank credit team.

### EA Development Finance Options to Add
- **Uganda Development Bank (UDB):** Long-term loans at 12–15%; minimum UGX 100M; requires feasibility study + ESMP
- **Agricultural Credit Facility (ACF):** Bank of Uganda/MoF facility; on-lent by commercial banks at ≤12%; up to UGX 2.1B for agribusiness
- **British International Investment (BII):** £750M deployed in equity investments in East Africa (EAA 2025) — relevant for impact-driven businesses
- **Absa Africa:** $6B+ in renewable energy financing; SME trade finance facilities; IFC/Volcafe partnership (7,000+ coffee farmers in EA)
- **PAPSS (Pan-African Payment and Settlement System):** Facilitates intra-African trade payments — relevant for businesses selling cross-border
- **UK Developing Countries Trading Scheme:** Uganda-specific duty-free, quota-free access to UK market for qualifying exporters

**What needs to be built:**
- Complete rewrite of `11-funding-request/SKILL.md` to be context-aware: ask whether the funding source is a bank loan, DFI facility, grant, or equity — and generate the appropriate format for each
- `11-funding-request/references/ea-funding-landscape.md` (see Gap C3)
- `11-funding-request/references/credit-assessment-frameworks.md` (see Gap C1)
- `11-funding-request/references/loan-application-templates.md` — standard bank loan narrative format used by Ugandan commercial banks

---

## GAP D3: Section 15 (Appendices) — Passive List, No Templates or Guidance

**Current state:** 52 lines, 0 reference files.

**Current skill behaviour:** Generates a list of what to include. Does not generate any of the actual documents.

**What a strong appendices section requires:**

### Documents That Can Be Generated (currently not supported)

1. **CV/Profile template for directors** — banks require a standard format: full name, NIN, TIN, address, qualifications, business history. The current skill says "include CVs" but provides no template.

2. **Financial summary table** — a one-page consolidated view of the 3-year projections matching the detailed financials exactly. Banks often read the appendix first to get numbers.

3. **Loan repayment schedule** — monthly table showing: outstanding principal, interest payment, principal repayment, closing balance. Banks generate this themselves but a plan that includes it shows sophistication.

4. **Net Worth Statement (Personal Statement of Assets and Liabilities)** — required by most Ugandan banks for the directors/guarantors. Format:

```
Personal Net Worth Statement
Name: _____________ NIN: _____________

ASSETS                          UGX
Cash and bank deposits:         ______
Motor vehicles (market value):  ______
Property (current valuation):   ______
Business interests:             ______
Other assets:                   ______
TOTAL ASSETS:                   ______

LIABILITIES
Existing loans:                 ______
Other debts:                    ______
TOTAL LIABILITIES:              ______

NET WORTH:                      ______
Signature: ___________  Date: ________
```

5. **Reference letters format** — for character/CAMPARI assessment, banks require reference letters from professional contacts, community leaders, or existing bankers.

6. **Market data appendix** — citing credible EA macro data strengthens any plan. The plan should be able to cite: EA GDP $603B growing at 5.7% (EAA 2025); sector-specific UNDP or AFREXIM trade figures; Uganda UBOS statistics. None of the current skills prompt for this.

**What needs to be built:**
- `15-appendices/references/document-templates.md` — CV template, net worth statement, loan schedule template, reference letter format
- The skill should actively generate the financial summary table from data in section 10, not just list it as "to be included"
- A market data citations template that pulls key EA economic statistics into the appendix for credibility

---

## GAP D4: Section 10 (Financial Projections) — Missing Ugandan Cost Benchmarks Integration

**Current state:** 132 lines, 5 refs (enhanced with `uganda-tax-framework.md` in March 2026). Reasonable skill but with integration gaps.

**What is missing:**

### 1. Integration with Industry Guides
The suite has 13 industry guides with detailed cost benchmarks, startup costs, and revenue models. **Section 10's SKILL.md never references them.** When generating financial projections for a restaurant, the skill does not say "read `industry-guides/restaurant/references/`". This means:
- Cost benchmarks are in the guides but projections ignore them
- The financial model and the industry guide generate inconsistent numbers
- A restaurant plan could show a 40% food cost while the Schmidgall reference benchmarks say 28–32%

**Fix:** Add a cross-reference table in the financial projections skill: "If generating projections for [industry], read [industry guide references] for cost benchmarks before generating numbers."

### 2. No Breakeven Analysis Template
The skill mentions break-even but provides no standard template. A break-even analysis for bank submission requires:
```
Fixed Costs per Month: UGX [total]
Variable Cost per Unit: UGX [X]
Selling Price per Unit: UGX [X]
Contribution Margin per Unit: UGX [X - variable cost]
Break-even Volume: Fixed Costs / Contribution Margin
Break-even Revenue: Break-even Volume × Selling Price
Break-even Month: [Month when cumulative revenue exceeds cumulative costs]
```

### 3. No Sensitivity Analysis Template
Banks want to see scenarios. The skill mentions stress-testing but `meta-financial-stress-test/SKILL.md` (94 lines, 0 refs) is disconnected from the projections skill. No shared template ties them together.

### 4. No Macroeconomic Assumptions Section
**Newly identified gap (from EAA 2025 and AFREXIM 2025):** Financial projections must state their macroeconomic assumptions explicitly. This is now essential given:

- **Exchange rate risk:** UGX has depreciated consistently; planning rate set at UGX 3,700/$ (conservative). Plans must show how a ±10% currency move affects imported input costs
- **Inflation assumptions:** Uganda's inflation is relatively stable vs. Ethiopia (23%) and Burundi (20%). However, global commodity prices are under pressure — agricultural commodity prices were strong in 2024 (AFREXIM 2025). Any cost model for food, energy, or raw materials must state an inflation assumption per input category
- **Global growth slowdown risk:** Global output slowing to 2.8% in 2025, down from 3.7% pre-pandemic average (AFREXIM 2025). This affects export demand forecasts for businesses selling outside Uganda
- **US tariff shock:** US effective tariff rate rose to 14.5% — the highest in nearly a century (AFREXIM 2025). Any projection assuming US exports is now exposed to tariff risk that must be modelled
- **Commodity price benchmarks:** Crude oil $75/barrel average 2024; agricultural commodity prices rising due to climate disruptions (AFREXIM 2025). Fuel costs, packaging costs, and food input costs should reference these benchmarks

**What the skill should prompt:**
```
Financial Projection Assumptions:
  Planning exchange rate: UGX [X] per $1
  Annual inflation assumption (operating costs): [X]%
  Annual revenue growth rate (Years 1–3): [X]%, justified by [market data]
  Commodity/input cost trend: [rising/stable/falling — cite source]
  Scenario: Does the projection hold if inflation rises 5 percentage points?
  Export assumptions: [if applicable — state which markets, tariff exposure]
```

**What needs to be built:**
- Add macroeconomic assumptions section to `10-financial-projections/SKILL.md`
- Cross-reference table linking industries to their guide directories
- Break-even template added to `10-financial-projections/references/financial-model-templates.md` (once created per Gap C6)
- Sensitivity table linked to `meta-financial-stress-test` skill

---

## GAP D5: Section 08 (Operations) — Thin EA Infrastructure Realities

**Current state:** 105 lines, 1 reference file (`operations-frameworks.md`).

**What is missing:**
The operations skill covers BPM, process design, and capacity planning well (thanks to the BPM batch). But it is generic and does not connect to EA-specific operational realities:

### 1. Uganda Infrastructure Constraints
Plans that ignore these will be flagged by any DFI or experienced bank analyst:
- **Power reliability:** Uganda's grid suffers load-shedding. Any manufacturing, cold chain, or hospitality operation must include: backup generator specification, fuel costs, UPS capacity for IT systems. The Umeme buyout (mentioned in Uganda HC's remarks, EAA 2025) signals a transition, but short-term reliability cannot be assumed
- **Water supply:** Peri-urban and rural areas have unreliable NWSC supply. Boreholes, rain harvesting, and storage tanks are operational requirements for many businesses — not optional extras
- **Internet connectivity:** Mobile data (MTN/Airtel) is the default for SMEs outside Kampala. Operations plans must account for mobile-first connectivity and the business risk of data-dependent operations in areas with weak 4G coverage
- **Road infrastructure:** East Africa's transport costs are among the world's highest per km. Road freight from Kampala to Mombasa corridor adds cost to any import-dependent business. The $4B Standard Gauge Railway investment (Uganda HC, EAA 2025) is long-term — it does not reduce current road freight costs

### 2. Supply Chain and Trade Realities
**From AFREXIM 2025:**
- **Suez Canal disruptions** have pushed carriers to the Cape of Good Hope route, increasing shipping times and costs for any Uganda business importing from Asia or Europe
- **EU deforestation rules** affect businesses in agricultural supply chains (coffee, cocoa, timber, palm oil) — from 2025, EU importers must verify no deforestation occurred in their supply chain; this flows back to Ugandan supplier operations
- **EU carbon border adjustments** will eventually affect industrial exporters — operators should plan now for supply chain transparency documentation

### 3. Labour Law Basics
- Employment Act 2006: minimum probation period 6 months; maximum working hours 48/week; overtime at 1.5× base; paid leave 21 working days/year
- Written employment contracts required for all employees
- NSSF: mandatory for ≥5 employees; failure triggers penalties and personal director liability
- Maternity leave: 60 working days paid; paternity: 4 working days

### 4. Quality and Regulatory Standards
- UNBS certification: mandatory before selling food, cosmetics, or industrial products in Uganda
- NEMA: Environmental Impact Assessment required for medium-to-large operations; Certificate of Approval for smaller businesses in sensitive sectors
- NAADS/MAAIF: standards for agricultural produce, livestock handling, dairy processing

**What needs to be built:**
- `08-operations-plan/references/uganda-infrastructure-realities.md` — power, water, internet, road logistics, with cost benchmarks
- `08-operations-plan/references/ea-supply-chain-risks.md` — shipping disruptions, EU trade rules, AfCFTA logistics opportunities
- `08-operations-plan/references/uganda-labour-law.md` — Employment Act 2006 essentials, NSSF, contract requirements
- `08-operations-plan/references/regulatory-compliance.md` — UNBS, NEMA, sector-specific standards

---

## GAP D6: Meta-Bankability-Scoring — No Formal Lender Criteria Mapped

**Current state:** 120 lines, 0 reference files.

**What is missing:**
The bankability scoring skill should be the capstone that tells a plan author: "here is how a lender would rate your plan." But the scoring dimensions are internally derived rather than mapped to formal lender criteria.

**What it should score against:**
1. **Does the DSCR exceed 1.25x?** (bank minimum)
2. **Is collateral ≥125% of loan value?** (standard bank requirement)
3. **Does the management team have sector experience?** (CAMPARI Ability)
4. **Are financial statements prepared by a qualified accountant?** (credibility marker)
5. **Is the business registered with URSB, TIN/BRN held, trading licence current?**
6. **Has the market been validated with named customers or LOIs?**
7. **Is the ESMP included if applying to a DFI?**

The current skill scores innovation, traction, and market size — useful for investor pitches, not bank applications.

### EA Credit Environment Context (from EAA 2025 and AFREXIM 2025)
Africa's $100B trade finance gap (Afreximbank 2025) is partly driven by banks' risk aversion toward SMEs that cannot demonstrate creditworthiness through proper documentation. The scoring skill should teach plan authors to think like a bank credit committee, not a startup accelerator. Key factors that Ugandan commercial banks (Stanbic, Centenary, dfcu, ABSA) and DFIs (UDB) weight:
- Cash flow predictability > collateral value alone
- Management experience in sector (not just academic qualifications)
- Registration completeness (NIN/BRN, TIN, trading licence — now a licensing gate from July 2025)
- Purpose specificity — "working capital" without detail scores low; "procurement of 500 units of X to fulfil LOI from Y" scores high

**What needs to be built:**
- Two scoring modes: "Bank Loan Readiness" and "Investor Readiness" — with different criteria
- Bank readiness mapped explicitly to 5 Cs / CAMPARI
- `meta-bankability-scoring/references/lender-criteria-uganda.md` — formal credit criteria with benchmarks from Ugandan commercial banks and UDB

---

## GAP D7: Section 09 (Management Team) — No EA-Specific Governance Standards

**Current state:** 104 lines, 8 reference files. Strongest of the mid-tier skills.

**What is missing:**
The skill has excellent leadership theory (Collins, Tuckman, Dennis) but lacks:

### 1. Board Governance for DFI Applications
Uganda Development Bank, Afreximbank facilities, and impact investors (BII, Acumen) require a functioning board with independent directors for loans above UGX 500M. The plan must show:
- Board composition (executive vs. independent directors)
- Board meeting frequency and quorum rules
- Committees (if applicable): audit, risk, remuneration
- Board resolution authorising the loan application (specific directors named with signing authority)

### 2. Professional Qualifications — EA Credentialing
For credentialed industries, list the relevant professional body membership:
- **Accounting/Finance:** ICPAU (Institute of Certified Public Accountants of Uganda) — required for regulated financial statement preparation
- **Engineering:** Engineers Registration Board (Uganda) / MUK/MUST graduates
- **Law:** Uganda Law Society (ULS)
- **Medicine/Health:** Uganda Medical and Dental Practitioners Council
- **Architecture:** Architects Registration Board

### 3. Succession and Key Person Risk
With East Africa's **507 million population and 2.8% annual growth** (EAA 2025), the region's fastest-growing consumer markets create increasing competition for skilled management. Business plans should address:
- Who succeeds the founder if incapacitated?
- Key person insurance (required by some banks as a condition of lending)
- Staff development and retention plan

### 4. Election Risk and Management Stability
**Newly relevant (from EAA 2025):** Uganda elections are scheduled for 2025/26. Business plans covering a 3-year projection must acknowledge election-cycle risk: policy uncertainty, public spending fluctuations, and short-term investor hesitancy common in EA election years. Management teams that have operated through previous election cycles in Uganda or EA have a competitive credibility advantage.

**What needs to be built:**
- `09-management-team/references/ea-governance-standards.md` — board composition requirements for DFI applications, director documentation, professional registrations
- Update `09-management-team/SKILL.md` to prompt for professional registrations and board governance section when DFI funding is the target

---

## GAP D8: Section 12 (Risk Analysis) — No Insurance Framework + No EA Macro Risk Context

**Current state:** 110 lines, 7 reference files. Good analytical depth.

**What is missing:**

### 1. No Insurance Framework
Risks are identified and analysed but the mitigation section does not connect to the Ugandan insurance market. Banks require proof of insurance on collateral assets:

| Insurance Type | When Required | Ugandan Providers |
|---|---|---|
| Fire and allied perils | Mandatory on any property/equipment offered as collateral | UAP, Jubilee, AIG, Liberty, CIC, ICEA Lion |
| Motor vehicle comprehensive | Required on any vehicle in the loan | All major insurers |
| Public liability | For hospitality, construction, events businesses | UAP, AIG, Jubilee |
| Business interruption | Rarely mandated but strengthens the plan | UAP, Liberty |
| Life assurance on key person | Some banks require life cover on borrowing director equal to loan amount | Prudential, Jubilee, Liberty |
| Marine/cargo | For import-dependent businesses | UAP, AIG |

**Planning implication:** The risk register must list insurance as a mitigation for each asset/liability risk. The operations budget must include insurance premiums as a monthly cost line.

### 2. No EA Macroeconomic Risk Context
**Newly critical (from EAA 2025 and AFREXIM 2025):** Business plans need to acknowledge and respond to the EA macro risk environment:

| Risk | Data Point | Planning Response |
|---|---|---|
| **Currency depreciation** | UGX depreciation trend; Ethiopia devalued birr in 2024; Kenya shilling strengthened but debt rose | State exchange rate assumption in projections; model sensitivity to ±10% UGX move |
| **Regional inflation divergence** | Ethiopia 23%, Burundi 20%, Uganda ~5%, Kenya 2.7% (EAA 2025) | Uganda businesses relatively advantaged; EA-wide supply chains should source from stable-inflation countries |
| **East Africa elections 2025/26** | Uganda, Tanzania, Burundi, Malawi, Seychelles elections (EAA 2025) | 3-year projections crossing election cycle must include election-risk scenario |
| **US tariff shock** | US effective tariff rate 14.5% — highest in nearly a century (AFREXIM 2025) | Businesses with US export plans must model tariff impact on margins; US-origin inputs may become more expensive via supply chain re-pricing |
| **Suez Canal disruptions** | Carriers rerouting via Cape of Good Hope — longer transit times, higher freight costs (AFREXIM 2025) | Import-dependent businesses: add 15–30 days to lead times, budget 10–20% higher shipping costs vs 2023 |
| **EU deforestation and carbon rules** | EU deforestation regulation requires supply chain traceability from 2025; carbon border adjustments coming (AFREXIM 2025) | Coffee, timber, and agri-exporters to EU: must implement and document sustainable sourcing now |
| **Public debt pressure** | EA governments borrowing heavily — Kenya $1.5B Eurobond; Uganda $4B SGR financing (EAA 2025) | Interest rate risk: government borrowing competes with SME credit, can push commercial lending rates higher |
| **Climate disruptions** | Agricultural commodity prices elevated due to climate disruptions (AFREXIM 2025) | Any agribusiness or food processing business: price escalation scenarios for raw material inputs |

### 3. AfCFTA Compliance Risk
Businesses projecting export revenue within Africa under AfCFTA must address:
- Rules of origin compliance: products must meet AfCFTA local content thresholds to qualify for preferential tariffs
- Tariff schedule implementation timeline varies by country — not all reductions are immediate
- Non-tariff barriers remain significant across EA borders

**What needs to be built:**
- `12-risk-analysis/references/ea-macro-risk-context.md` — country-by-country inflation, currency, political risk benchmarks with planning implications
- `12-risk-analysis/references/uganda-insurance-framework.md` — insurance types, providers, premium benchmarks, bank requirements
- `12-risk-analysis/references/global-trade-risks-2025.md` — US tariffs, Suez disruptions, EU trade rules, AfCFTA compliance risks

---

## GAP D9: Industry Guides — Not Integrated with Core Skills

**Current state:** 13 industry guides exist with detailed content. None of the core skill SKILL.md files reference them.

**The problem:**
A user generating a business plan for a restaurant follows the core skills (01–15). The `restaurant/` industry guide exists with 10 detailed reference files covering financial benchmarks, food cost controls, hygiene standards, and staffing ratios. But nothing in the workflow tells the core skills to use that industry guide data.

**Specific integration failures:**
- `04-market-analysis` should say: "If industry = restaurant, read `industry-guides/restaurant/guide.md` for market context"
- `10-financial-projections` should say: "If industry = agriculture, read `industry-guides/agriculture/references/` for cost benchmarks"
- `08-operations-plan` should say: "For manufacturing businesses, read `industry-guides/manufacturing-light/guide.md` for operations benchmarks"
- `09-management-team` should say: "For agribusiness, the management team should include MAAIF-certified agronomists or equivalent"

**What needs to be built:**
A cross-reference matrix in each core skill pointing to relevant industry guides by sector. This is a documentation fix, not new content creation — the content already exists.

### EA Sector Priorities to Link (from EAA 2025)
The EAA 2025 report identifies five priority investment sectors for East Africa:
1. **FinTech and Digital Banking** — no industry guide exists; mobile payments/digital finance content needed
2. **Renewable Energy** — Absa committed $6B+; BII deploying equity; no industry guide exists
3. **Agribusiness and Food Processing** — 60% of Africa's arable land in EA; guides exist (`agriculture/`, `food-processing/`) but not cross-referenced with `04-market-analysis`
4. **Healthcare and Digital Health** — no industry guide exists; growing investment sector
5. **Consumer Goods and Retail** — guide exists (`retail/`) but not cross-referenced with `07-marketing-sales-strategy` or `10-financial-projections`

**What needs to be built:**
- Cross-reference matrix in each core skill (integration fix — existing content)
- New priority sector guide: `industry-guides/fintech-digital-banking/` (no current coverage)
- New priority sector guide: `industry-guides/renewable-energy/` (no current coverage)
- New priority sector guide: `industry-guides/healthcare/` (no current coverage)

---

## GAP D10: No East Africa Macroeconomic Context Reference

**Severity:** HIGH — this is the foundational context every market analysis and financial projection needs.

**What is missing:**
No reference file anywhere in the suite provides the macro-economic backdrop that makes plans credible to EA-based readers (bank analysts, DFI officers, investors). A plan that cites specific EA economic data is immediately more credible than one that asserts vague growth claims.

### Key 2025 Macroeconomic Data (from EAA 2025 and AFREXIM 2025)

**Regional:**
- EA population: **507 million**, growing at **2.8% per year** (EAA 2025)
- EA GDP 2025: **$603 billion**, growing at **5.7%** — fastest-growing region in Africa
- Post-pandemic recovery: GDP above 5% annually for multiple consecutive years

**Country-by-Country Snapshot:**

| Country | GDP Growth 2025 | Inflation | Currency Note |
|---|---|---|---|
| **Uganda** | ~5.5% (EAA estimate) | ~5% | UGX 3,550/$1 (Q1 2025/26, UBOS); UGX 3,700 planning rate |
| **Kenya** | 5.5–6% | 2.7% (Oct 2024) | KES 130/$; shilling strengthened in 2024 |
| **Rwanda** | 6.8% | Stable, declining | NST2 and Industrial Policy 2024–2034 driving growth |
| **Ethiopia** | 6.1% (5-yr avg) | 23% | Birr devalued in 2024 (flexible exchange rate transition) |
| **Burundi** | Modest | 20% | High inflation — risk for cross-border trade |
| **Tanzania** | ~5% | Stable | Large domestic market; AfCFTA gateway |

**Global context affecting EA plans:**
- World GDP growth 2025: **2.8%** (below 3.7% pre-pandemic average) — AFREXIM 2025
- Africa GDP growth 2024: **3.2%** (below 5% pre-pandemic potential)
- US effective tariff rate April 2025: **14.5%** — highest in nearly a century — disrupting global trade flows
- Africa trade finance gap: **$100 billion annually** — structural barrier to SME growth

**Investment landscape:**
- BII (British International Investment): £750M in equity investments in EA (EAA 2025)
- Absa: $6B+ renewable energy financing across Africa; strong EA presence
- AfCFTA: creating a $3.4 trillion combined market; EA positioned as gateway
- PAPSS: Pan-African Payment Settlement System reducing cross-border payment friction

**What needs to be built:**
- `04-market-analysis/references/ea-macroeconomic-context-2025.md` — country-level GDP, inflation, currency benchmarks, investment landscape, sector growth drivers. To be updated annually.
- Update `04-market-analysis/SKILL.md` to require citing current EA macro data when writing the market analysis section

---

## GAP D11: No AfCFTA and Regional Trade Framework

**Severity:** HIGH — East Africa's biggest structural opportunity for export-oriented businesses is completely absent from the suite.

**What is missing:**
The African Continental Free Trade Area (AfCFTA) is a **$3.4 trillion combined African market** covering 55 countries and 1.4 billion people. It eliminates tariffs on 90% of goods among member states when implemented. For Ugandan businesses, this is potentially the largest growth opportunity since EAC integration. But it does not appear anywhere in the skills suite.

### What Business Plans Need to Know About AfCFTA

**Opportunities:**
- Tariff reduction on 90% of goods across 55 African countries — Ugandan manufacturers can sell into Kenya, Tanzania, Rwanda, DRC, Ethiopia at lower tariff rates
- Simplified rules of origin — a product that meets AfCFTA local content thresholds qualifies for preferential rates across the continent
- Protocol on Women in Business: dedicated SME and women-owned business provisions
- PAPSS (Pan-African Payment and Settlement System): removes USD intermediary from intra-African payments — lower transaction costs for cross-border sales

**Reality check:**
- Implementation is uneven — not all countries have ratified all schedules
- Non-tariff barriers (border delays, documentation, standards differences) remain significant
- Rules of origin compliance requires documentation that most EA SMEs are not currently set up for

**EAC Framework (most immediately relevant for Uganda):**
- EAC Common External Tariff: 0%/10%/25% — businesses importing within EAC pay 0% on most goods
- EAC single market: labour, capital, services can move freely among members
- EAC industrialisation drive: partner states encourage value-added manufacturing over raw commodity exports

**UK Developing Countries Trading Scheme (Uganda-specific):**
- Uganda qualifies for Enhanced Preferences: duty-free, quota-free access to UK market
- Coffee, cut flowers, fish, textiles, and other Ugandan exports enter UK at zero tariff
- Value-added products (processed coffee, finished textiles) get better margin than raw exports
- Documentation requirement: Rules of Origin Form A; URSB-registered company required (EAA 2025)

**What needs to be built:**
- `04-market-analysis/references/afcfta-ea-trade-framework.md` — AfCFTA overview, EAC framework, UK DCTS, PAPSS, rules of origin requirements, and how to frame an export opportunity in a business plan

---

## GAP D12: No Global Trade Risk Section for 2025

**Severity:** MEDIUM-HIGH — plans written in 2025/26 without acknowledging the new global trade environment will look uninformed to any sophisticated reviewer.

**What is missing:**
The AFREXIM Africa Trade Report 2025 identifies the most significant structural shift in global trade in decades. Business plans generated by the suite have no framework for placing a Ugandan business within this context.

### Key Risks from AFREXIM 2025 to Embed in Plans

**1. US tariff escalation (effective tariff rate 14.5%)**
- Any business plan projecting exports to the US, or importing US-origin inputs, must model this risk
- The tariff escalation has created supply chain re-routing globally — some goods that previously transited through the US now seek African or Asian alternatives (opportunity)
- Uncertainty itself (market volatility, weakened multilateral cooperation) is a risk factor for all export-oriented businesses

**2. Suez Canal disruptions**
- Conflict-related disruptions have pushed carriers to Cape of Good Hope routing
- Effect for Uganda: imports from Asia (electronics, machinery, textiles, chemicals) face longer transit times (+10–20 days) and higher freight costs (+10–20%)
- Business plans must reflect realistic import lead times and landed costs for 2025/26

**3. EU trade rules — deforestation and carbon**
- EU Deforestation Regulation: from 2025, EU importers must prove no deforestation in supply chains. Coffee, timber, palm oil, cocoa exporters in Uganda must be able to document supply chain traceability
- EU Carbon Border Adjustment Mechanism (CBAM): applies to cement, steel, fertilisers, aluminium, electricity — not yet widely affecting EA SMEs, but will impact manufacturers exporting processed goods

**4. Geopolitical disruptions in EA region**
- Sudan humanitarian crisis: disrupts trade routes through East/Northeast Africa; affects refugee population inflows that create market demand in Uganda
- DRC conflict (Eastern Congo): creates displaced population flows, affects mining supply chains, impacts regional security context
- Al-Shabaab in Somalia: affects Horn of Africa logistics and Kenya northern corridor security

**5. Critical minerals opportunity**
- Africa holds major reserves of cobalt, lithium, and nickel — essential for global energy transition
- EA countries with mining potential (DRC, Uganda — new oil) face the "extract and ship" risk vs. local processing opportunity
- Plans in minerals or processing sectors should reference AfCFTA rules of origin that reward local value addition

**What needs to be built:**
- `12-risk-analysis/references/global-trade-risks-2025.md` — US tariffs, Suez disruptions, EU trade rules, geopolitical risks, with specific impact for Ugandan businesses
- `04-market-analysis/references/ea-macroeconomic-context-2025.md` should reference AFREXIM as a source for global trade dynamics
- Plans must include a "Global Context" paragraph in the market analysis for any business with import dependency or export ambitions

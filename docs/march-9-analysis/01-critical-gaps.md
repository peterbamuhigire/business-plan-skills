# Critical Gaps — Will Cause Funding Rejection

These gaps are not about quality of writing. They are about the fundamental information that banks, development finance institutions (DFIs), and serious investors require before approving funding. A plan with these gaps will be returned or rejected regardless of how well other sections are written.

---

## GAP C1: No Credit Assessment Framework

**Severity:** CRITICAL — this is the single biggest gap in the suite.

**What is missing:**
Every bank credit committee in Uganda and East Africa uses a structured credit assessment framework. The two most common are the **5 Cs of Credit** and **CAMPARI**. Neither exists anywhere in the skills suite.

### The 5 Cs of Credit (standard bank framework)

| C | What the Bank Assesses | Where it Should Appear in the Plan |
|---|---|---|
| **Character** | Owner's reputation, track record, integrity | §02 Company Overview, §09 Management Team |
| **Capacity** | Ability to repay from cash flow (DSCR) | §10 Financial Projections |
| **Capital** | Owner's own investment (skin in the game) | §11 Funding Request |
| **Collateral** | Assets that can be seized if loan defaults | §11 Funding Request |
| **Conditions** | Economic environment, loan purpose, industry | §04 Market Analysis, §08 Operations |

### CAMPARI (used by commercial banks in Uganda/EA)

| Letter | Criterion | Business Plan Location |
|---|---|---|
| **C** haracter | Owner's credit history and reputation | §02, §09 |
| **A** bility | Technical and managerial ability to run the business | §09 Management Team |
| **M** eans | Financial capacity — own funds, other resources | §10, §11 |
| **P** urpose | What the loan is for (productive vs. speculative) | §11 Funding Request |
| **A** mount | Correct loan sizing — not too much, not too little | §11 Funding Request |
| **R** epayment | Source and schedule of repayment | §10 Financial Projections |
| **I** nsurance | Security/collateral against default | §11 Funding Request |

**What needs to be built:**
- A reference file `11-funding-request/references/credit-assessment-frameworks.md` covering 5 Cs, CAMPARI, and how the business plan systematically addresses each criterion
- A "credit committee readiness checklist" — a self-test the plan author can run before submission

---

## GAP C2: No Debt Service Coverage Ratio (DSCR)

**Severity:** CRITICAL — banks will not approve without this.

**What is missing:**
Every commercial bank in Uganda (Stanbic, Centenary, dfcu, Standard Chartered, ABSA) requires DSCR in the credit assessment. The formula is:

```
DSCR = Net Operating Income / Total Debt Service
     = EBITDA / (Principal repayments + Interest payments)

Minimum acceptable: 1.25x (most Ugandan banks)
Strong application: 1.5x or above
```

A DSCR below 1.0 means the business cannot service its debt from operations — automatic rejection. A DSCR between 1.0 and 1.25 is borderline and requires strong collateral. Above 1.5 is a strong application.

**Currently:** `10-financial-projections/SKILL.md` (132 lines, 4 refs) mentions cash flow projections and break-even but never mentions DSCR. The skill generates financial projections without the key number banks look for.

**What needs to be built:**
- DSCR calculation added to `10-financial-projections/SKILL.md`
- A worked example showing DSCR calculation from the projected P&L
- Sensitivity table: DSCR under base, low, and stress scenarios

---

## GAP C3: No East African Lending Landscape

**Severity:** CRITICAL — the funding request skill is written entirely for venture capital, which is the wrong audience for 90%+ of EA businesses.

**What is missing:**
`11-funding-request/SKILL.md` (59 lines, 0 refs) assumes equity funding, mentions IPO and convertible notes, and uses language designed for startup investors. In Uganda and East Africa, most formal financing comes from:

### Uganda Funding Landscape (completely absent from the suite)

**Development Finance Institutions:**
- **Uganda Development Bank (UDB)** — provides long-term loans at subsidised rates (currently 12–15%); minimum UGX 100M; requires business plan, feasibility study, and environmental assessment
- **Agricultural Credit Facility (ACF)** — Bank of Uganda/Ministry of Finance facility for agribusiness; commercial banks on-lend at ≤12%; up to UGX 2.1B
- **USSIA/UMA/Industry-specific bodies** — sector-specific facilities

**Commercial Bank Loans (primary funding route for SMEs):**
- Centenary Bank, dfcu, Stanbic, Equity Bank, ABSA Uganda, Standard Chartered
- Typical SME loan: 18–24% per annum, 3–7 year term, 20–30% collateral margin
- Requirements: 2 years of financial statements (or strong projections for startups), collateral equal to 125–150% of loan value

**SACCOs and Microfinance:**
- Uganda Finance Trust, FINCA, Pride Microfinance, UGAFODE
- Loans up to UGX 100M; higher interest (30–36% p.a.); minimal collateral
- Appropriate for early-stage and informal businesses

**Development Partner Grants:**
- USAID, EU, GIZ, UN agencies — typically require social/environmental impact
- Youth and women funds: GROW, EMPOWER, Youth Livelihood Programme (YLP), Women Entrepreneurship Programme (WEP)
- Competitive — require theory of change and M&E framework (covered in meta-monitoring-evaluation but not linked to funding)

**Impact Investors:**
- Acumen, Novastar, Pearl Capital (agribusiness), Renew Capital
- Require B2B or B2C scalability and social impact metrics

**What needs to be built:**
- `11-funding-request/references/ea-funding-landscape.md` — comprehensive guide to all funding sources, eligibility criteria, documentation requirements, typical terms
- The skill needs a funding-type decision tree: based on business stage, sector, and amount needed, route the plan to the right funding source
- Separate templates for: bank loan application narrative vs. DFI feasibility study vs. grant proposal vs. equity pitch

---

## GAP C4: No Collateral Analysis Framework

**Severity:** CRITICAL for bank loan applications.

**What is missing:**
Most Ugandan banks require collateral worth 125–150% of the loan value. The plan must include a collateral statement identifying what assets are available as security. Types of accepted collateral in Uganda:

| Collateral Type | Notes |
|---|---|
| Land title (Mailo, Freehold, Leasehold) | Most preferred; must be in the loan applicant's name |
| Motor vehicle logbook | Valued at 50–70% of market value |
| Machinery and equipment | Valued at 40–60% of cost; requires insurance |
| Fixed deposit (cash collateral) | 100% value; easiest to liquidate |
| Personal guarantee | Acceptable for small loans; limited weight for large |
| Debenture over business assets | Registered charge over receivables/inventory |

**Currently:** Not mentioned anywhere in the suite. Section 11 describes exit strategies (dividends, IPO) but says nothing about security.

**What needs to be built:**
- Collateral section in `11-funding-request/SKILL.md` covering types, valuation, and how to present limited collateral (with compensating factors)
- Guidance on collateral alternatives: credit guarantee schemes (Uganda Credit Guarantee Scheme, USSIA guarantee fund), character lending, group guarantees
- **2025 update:** The Stamp Duty (Amendment) Bill 2025 (effective 1 July 2025) reduces stamp duty on mortgage deeds and agreement/memoranda to **NIL** (previously 0.5% of loan value for mortgage deeds; UGX 15,000 for agreements). This reduces the upfront cost of borrowing and should be noted in the collateral section of any plan targeting a bank loan (KPMG, 2025).

---

## GAP C5: No Uganda Tax Framework

**Severity:** HIGH — financial projections without correct tax treatment are not credible.

**What is missing:**
`10-financial-projections/SKILL.md` generates P&L projections but contains no Uganda-specific tax guidance. A Ugandan bank or URA-registered accountant will immediately check:

### Core Uganda Tax Rates (ITA Cap.340 and VATA Cap.349)

| Tax | Rate | Threshold / Notes |
|---|---|---|
| **Corporate Income Tax** | 30% of taxable profit | Companies and trustees; charged annually on chargeable income |
| **Individual Income Tax (PAYE)** | Graduated 0%–40% — see bands below | Employer withholds monthly; remits to URA by 15th of following month |
| **VAT** | 18% | Mandatory registration if turnover ≥ UGX 150M/year; input VAT on business purchases is recoverable |
| **Rental Tax** | 20% of net rental income (individuals); 30% (companies) | Separate from income tax; applies to rental property income |
| **WHT — goods and services** | 6% | Designated payers (government, large companies) withhold from supplier payments ≥ UGX 1M per contract |
| **WHT — professional fees** | 6% (s.118A) | Withheld by payer; credited against payee's annual tax |
| **WHT — asset disposal** | 10% (s.118B) | Applied when purchasing business assets; final tax in some cases |
| **WHT — dividends (resident)** | 15% (unlisted companies); 10% (listed on USE) | Withheld by paying company; credited to shareholder |
| **Presumptive Tax** | Flat amounts by turnover band | For businesses with gross turnover < UGX 150M/year who do not opt into normal assessment; final tax |
| **Import Duty / EAC CET** | Varies by HS code (0%, 10%, 25% main tiers) | Relevant for imported machinery and inputs; plant and machinery often at 0% under EAC CET Ch.84/85 |
| **NSSF Contribution** | 10% employer + 5% employee = 15% of gross wage | Mandatory for employers with ≥5 employees; remit by 15th of following month |

### PAYE Bands — Resident Individuals (Third Schedule, ITA Cap.340)

These are the annual chargeable income bands. Employers compute PAYE monthly using 1/12 of the annual thresholds.

| Annual Chargeable Income | Monthly Equivalent | Tax Payable |
|---|---|---|
| Not exceeding UGX 2,820,000 | Up to UGX 235,000/month | **0%** |
| UGX 2,820,001 – 4,020,000 | UGX 235,001 – 335,000/month | 10% of the excess over UGX 2,820,000 |
| UGX 4,020,001 – 4,920,000 | UGX 335,001 – 410,000/month | UGX 120,000 + 20% of the excess over UGX 4,020,000 |
| UGX 4,920,001 – 120,000,000 | UGX 410,001 – 10,000,000/month | UGX 300,000 + 30% of the excess over UGX 4,920,000 |
| Exceeding UGX 120,000,000 | Above UGX 10,000,000/month | UGX 34,824,000 + 40% of the excess over UGX 120,000,000 |

**Planning implication:** Most SME employees earn below UGX 410,000/month — at or below the 0% or 10% band. PAYE becomes significant only for management and professional staff. Projections must model this correctly rather than applying a flat payroll tax percentage.

**Sole trader vs company:** A sole trader pays individual income tax (bands above) on business profit. A private limited company pays 30% corporate tax. For profits below ~UGX 15M/year, sole trader tax can be lower; above that, corporate structure is often more efficient. Business plans must state the legal structure and apply the correct tax regime.

**Currently:** The skill table lists "Graduated: 0% to 40%" for PAYE (no bands) and omits rental tax, WHT on dividends, and WHT on asset disposals entirely. It does not distinguish sole trader vs. company tax treatment.

**Status: RESOLVED (10 March 2026).** `10-financial-projections/references/uganda-tax-framework.md` has been created and fully populated from the Income Tax Act Cap.340, Value Added Tax Act Cap.349, Excise Duty Act 2014, Stamp Duty Act 2014, and Transfer Pricing Regulations 2011 (all sourced via Okuja, Onyango & Co. Advocates). It covers all 20 statutory areas including exact PAYE bands, presumptive tax tables, depreciation schedules, WHT rates, VAT schedules, excise and stamp duty tables, penalties, filing deadlines, transfer pricing rules, and 2025 amendments with planning implications.

**Remaining actions:**
- `10-financial-projections/SKILL.md` should be updated to reference `uganda-tax-framework.md` explicitly and prompt the plan author to check the 2025 new-citizen exemption and import levy
- A tax schedule template (PAYE, VAT, corporate tax, NSSF as separate line items) should be added to `10-financial-projections/references/financial-model-templates.md` when that file is built (see Gap C6)

*Sources: Income Tax Act Cap.340 (ITA), Value Added Tax Act Cap.349 (VATA), Excise Duty Act 2014, Stamp Duty Act 2014, Income Tax (Transfer Pricing) Regulations 2011 — all reproduced by Okuja, Onyango & Co. Advocates; KPMG, Tax (Amendment) Bills, 2025, April 2025 (East Africa).*

---

## GAP C6: No Financial Model Templates

**Severity:** HIGH — the skill describes what to produce but provides no structural template.

**What is missing:**
`10-financial-projections/SKILL.md` tells Claude to generate financial projections but provides no actual template structure. A bankable financial model requires:

**Month-by-month for Year 1, quarterly for Years 2–3:**

```
Income Statement:
  Revenue (by product/service line)
  - Cost of Goods Sold (variable costs only)
  = Gross Profit
  Gross Margin %
  - Operating Expenses (fixed: salaries, rent, utilities, depreciation, marketing)
  = EBITDA
  - Depreciation & Amortisation
  = EBIT
  - Interest on Loans
  = Profit Before Tax
  - Income Tax (30%)
  = Net Profit After Tax

Cash Flow Statement (separate from P&L):
  Opening cash balance
  + Cash from operations (collections, not revenue)
  - Cash payments (supplier payments, wages, tax, loan service)
  = Closing cash balance
  (Must show the month the business goes cash-flow positive)

Balance Sheet (Year-end):
  Assets: Cash, receivables, inventory, fixed assets, accumulated depreciation
  Liabilities: Loans payable, accounts payable, tax payable
  Equity: Paid-in capital, retained earnings

Key Ratios (mandatory for bank submission):
  - DSCR (see Gap C2)
  - Current Ratio (≥1.5 preferred)
  - Debt-to-Equity Ratio
  - Gross Margin %
  - Net Profit Margin %
  - Return on Equity
```

**Currently:** The skill generates narrative projections. There is no standard template that ensures every plan produces comparable, bank-readable financial statements.

**What needs to be built:**
- `10-financial-projections/references/financial-model-templates.md` with explicit row-by-row templates for all three statements
- Guidance on formatting for bank submission vs. investor deck

---

## GAP C7: No Environmental and Social Management Plan (ESMP)

**Severity:** HIGH for development finance applications.

**What is missing:**
Any business applying to UDB, ACF, World Bank facilities, IFC, or EU grants must include an Environmental and Social Management Plan. This is a hard gate — without it, the application is returned. Most EA businesses do not know this requirement exists.

**ESMP minimum requirements (IFC/UDB standard):**
- Environmental baseline: water, soil, air, biodiversity impacts
- Social baseline: employment, community relations, gender equity
- Mitigation measures: for each identified impact
- Monitoring indicators: what will be measured and how often
- Responsible parties and budget for implementation

**Currently:** `14-ai-integration/SKILL.md` has a brief sustainability note but no ESMP framework exists in the suite.

**What needs to be built:**
- An ESMP section in `11-funding-request/SKILL.md` noting when it is required
- A lightweight ESMP template in references for businesses that need development finance

---

## GAP C8: No Awareness of 2025 Uganda Tax Amendments

**Severity:** HIGH — affects projection accuracy for all plans from FY 2025/26 onwards.

**What is missing:**
The KPMG *Tax (Amendment) Bills, 2025* analysis (April 2025) describes significant amendments effective **1 July 2025** that affect business plan financial projections. None of these appear anywhere in the skills suite.

### Amendment 1: Three-Year Income Tax Exemption for New Citizen Businesses

**Proposed by:** Income Tax (Amendment) Bill 2025

New businesses established by Ugandan citizens after 1 July 2025 are exempt from income tax for **three years**, provided:
- Investment capital does not exceed **UGX 500 million**
- The citizen (or an associate) has not previously benefited from this exemption
- The taxpayer files annual tax returns with required business information (s.147)

**Planning implication:** For a new SME with capital under UGX 500M, financial projections for Years 1–3 should show **zero income tax liability**. Including a 30% corporate tax charge in Year 1–3 projections for a qualifying business is incorrect and may actually *understate* projected net profit, disadvantaging the applicant. The skill must prompt the plan author to check eligibility and apply this exemption in financial models.

**Caveat:** This remains a proposed amendment as of April 2025; plans should note that exemption is conditional on presidential assent and filing compliance.

### Amendment 2: New Import Costs (External Trade Amendment Bill 2025)

Effective 1 July 2025, all goods imported from outside the EAC for home use attract two new levies:

| Levy | Rate | Basis |
|---|---|---|
| Infrastructure levy | 1.5% | Of customs value |
| Import declaration fee | 1.0% | Of customs value |
| **Total new cost** | **2.5%** | On top of existing customs duty and EAC CET |

**Exceptions:** Plant and machinery under EAC CET Chapters 84–85 are exempt from both levies. Most production equipment qualifies. Consumer goods, finished products, and raw materials do not.

**Planning implication:** Capital expenditure budgets for imported machinery require no adjustment (Ch.84/85 exempt). However, businesses importing raw materials, packaging, or consumables from outside EAC must add 2.5% to their per-unit input cost. This can materially affect the gross margin if not modelled.

### Amendment 3: Stamp Duty on Mortgage Deeds → NIL

See Gap C4. The elimination of stamp duty on mortgage deeds (previously 0.5% of loan value) reduces the all-in cost of bank borrowing and should be reflected in the funding request section's cost-of-finance calculations.

### Amendment 4: EFRIS Compliance (Electronic Fiscal Receipting and Invoicing)

The Tax Procedures Code Amendment 2025 doubles penalties for non-compliance with the Electronic Fiscal Receipting and Invoicing Solution (EFRIS):
- Previous penalty: tax due on goods/services, or UGX 6–8M (whichever higher)
- New penalty: **double the tax due** on goods or services

**Planning implication:** Any business plan projecting VAT-registered status must include EFRIS setup costs (hardware/software for electronic receipting) and compliance procedures. The risk section must note the penalty exposure.

### Amendment 5: TIN = NIN/BRN — Licensing Gate

From 1 July 2025, local authorities and government institutions **cannot issue any business licence** unless the applicant holds a National Identification Number (NIN, for individuals) or Business Registration Number (BRN, from URSB, for companies). These are now the tax identification numbers.

**Planning implication:** The implementation timeline and operations plan must include NIN/BRN acquisition as a prerequisite step before any licence application. Plans that assume immediate licensing on Day 1 without addressing registration are non-compliant.

### Amendment 6: VAT Anti-Fragmentation Rule

URA can now re-characterise separate import consignments as an aggregate consignment for determining VAT registration liability. If the aggregate exceeds UGX 150M, the importer must register for VAT.

**Planning implication:** Businesses that deliberately split import orders to stay below the UGX 150M VAT threshold face enforcement risk under this rule. Operations plans should not rely on consignment splitting as a VAT avoidance strategy.

**Currently:** None of these amendments exist anywhere in the skills suite. Plans generated for businesses starting after July 2025 using current skills will routinely:
- Overstate tax costs (by applying income tax to businesses that qualify for the 3-year exemption)
- Understate import costs (by omitting the 1.5% + 1.0% levies on non-machinery imports)
- Omit EFRIS setup costs and risk
- Omit NIN/BRN as a licensing prerequisite

**Status: PARTIALLY RESOLVED (10 March 2026).** `10-financial-projections/references/uganda-tax-framework.md` now contains a full 2025 Amendments section (§§10–11 of that file) covering all six amendments above with planning guidance. Remaining actions:
- `13-implementation-timeline/SKILL.md` — add NIN/BRN registration as a mandatory pre-step in the pre-launch phase
- `12-risk-analysis/SKILL.md` — add EFRIS non-compliance and 2.5% import levy escalation as standard risk items for VAT-registered and import-dependent businesses

*Source: KPMG, Tax (Amendment) Bills, 2025 — A KPMG Analysis, April 2025 (East Africa).*

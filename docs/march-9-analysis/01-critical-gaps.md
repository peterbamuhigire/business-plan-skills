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

---

## GAP C5: No Uganda Tax Framework

**Severity:** HIGH — financial projections without correct tax treatment are not credible.

**What is missing:**
`10-financial-projections/SKILL.md` generates P&L projections but contains no Uganda-specific tax guidance. A Ugandan bank or URA-registered accountant will immediately check:

| Tax | Rate | Notes |
|---|---|---|
| **Corporate Income Tax** | 30% of taxable profit | Applicable to companies; sole traders pay personal income tax |
| **VAT** | 18% | Mandatory registration if turnover > UGX 150M/year; input VAT recoverable |
| **PAYE** | Graduated: 0% to 40% | Employer obligation; monthly URA remittance |
| **Withholding Tax (WHT)** | 6% on service payments to residents | Applied when paying professional services, rent, contractors |
| **Presumptive Tax** | Fixed amounts by turnover band | For businesses below UGX 150M with no records |
| **Import Duty / EAC CET** | Varies by HS code | Relevant for imported machinery and inputs |
| **NSSF Contribution** | 10% employer + 5% employee | Mandatory for employers with ≥5 employees |

**Currently:** The skill mentions tax as a line item but provides no rates, no computation methodology, and no distinction between corporate vs. sole trader taxation. A projection that uses wrong tax rates will be rejected by any accountant reviewing the plan.

**What needs to be built:**
- `10-financial-projections/references/uganda-tax-framework.md` — tax rates, computation examples, registration thresholds, and how to present taxes in projected financial statements
- A tax schedule template showing PAYE, VAT, corporate tax, and NSSF as separate line items

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

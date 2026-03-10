# Uganda Tax Framework Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Fix the Uganda tax gap in the gap analysis (C5), add a new gap for 2025 amendments (C8), update the collateral gap (C4) with the stamp duty change, and create the tax reference file called for by the gap analysis.

**Architecture:** Four targeted edits — three in `docs/march-9-analysis/01-critical-gaps.md` (patch C4, rewrite C5, append C8) and one new file `10-financial-projections/references/uganda-tax-framework.md`.

**Sources:** Income Tax Act Cap.340 (Okuja, Onyango & Co. Advocates); Value Added Tax Act Cap.349; KPMG, *Tax (Amendment) Bills, 2025 — A KPMG Analysis*, April 2025 (East Africa).

---

## Task 1: Patch Gap C4 — stamp duty note

**Files:**
- Modify: `docs/march-9-analysis/01-critical-gaps.md` (Gap C4 section, ~line 130)

**Step 1: Read the current C4 section to confirm exact text**

Read lines 108–130 of `docs/march-9-analysis/01-critical-gaps.md` to confirm the current "What needs to be built" closing text.

**Step 2: Add stamp duty update note**

Find the last bullet in the "What needs to be built" block of C4:

```
- Guidance on collateral alternatives: credit guarantee schemes (Uganda Credit Guarantee Scheme, USSIA guarantee fund), character lending, group guarantees
```

Add a new bullet immediately after:

```markdown
- **2025 update:** The Stamp Duty (Amendment) Bill 2025 (effective 1 July 2025) reduces stamp duty on mortgage deeds and agreement/memoranda to **NIL** (previously 0.5% of loan value for mortgage deeds; UGX 15,000 for agreements). This reduces the upfront cost of borrowing and should be noted in the collateral section of any plan targeting a bank loan (KPMG, 2025).
```

**Step 3: Commit**

```bash
git add docs/march-9-analysis/01-critical-gaps.md
git commit -m "fix(gaps): add 2025 stamp duty NIL update to Gap C4"
```

---

## Task 2: Rewrite Gap C5 — Uganda Tax Framework

**Files:**
- Modify: `docs/march-9-analysis/01-critical-gaps.md` (replace the entire C5 section)

**Step 1: Locate the C5 section boundaries**

Find: `## GAP C5: No Uganda Tax Framework` through (but not including) `## GAP C6:`

**Step 2: Replace the entire C5 section with the corrected version below**

```markdown
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

**What needs to be built:**
- `10-financial-projections/references/uganda-tax-framework.md` — authoritative rates (sourced to ITA Cap.340), PAYE computation examples, VAT mechanics, WHT obligations, NSSF formula, presumptive tax bands, and the 2025 amendments that affect business plan projections
- A tax schedule template showing PAYE, VAT, corporate tax, and NSSF as separate clearly-labelled line items in projected financials
- Guidance on when to use sole trader vs. company tax treatment in projections

*Sources: Income Tax Act Cap.340, ss.4–8, Third Schedule (Okuja, Onyango & Co. Advocates); Value Added Tax Act Cap.349, s.5.*

---
```

**Step 3: Commit**

```bash
git add docs/march-9-analysis/01-critical-gaps.md
git commit -m "fix(gaps): rewrite Gap C5 with authoritative Uganda tax rates and PAYE bands"
```

---

## Task 3: Append Gap C8 — 2025 Tax Amendments

**Files:**
- Modify: `docs/march-9-analysis/01-critical-gaps.md` (append after Gap C7)

**Step 1: Find the end of the file**

Confirm the file ends after the Gap C7 "What needs to be built" block.

**Step 2: Append Gap C8 to the end of the file**

```markdown

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

**What needs to be built:**
- `10-financial-projections/references/uganda-tax-framework.md` must include a "2025 Amendments" section with planning guidance for each amendment above (covered in Task 4 of this plan)
- `13-implementation-timeline/SKILL.md` should be updated to include NIN/BRN registration as a mandatory pre-step
- `12-risk-analysis/SKILL.md` should add EFRIS non-compliance and import cost escalation as standard risk items for VAT-registered businesses

*Source: KPMG, Tax (Amendment) Bills, 2025 — A KPMG Analysis, April 2025 (East Africa).*
```

**Step 3: Commit**

```bash
git add docs/march-9-analysis/01-critical-gaps.md
git commit -m "fix(gaps): add Gap C8 for 2025 Uganda tax amendments (KPMG)"
```

---

## Task 4: Create uganda-tax-framework.md reference file

**Files:**
- Create: `10-financial-projections/references/uganda-tax-framework.md`

**Step 1: Create the file with the full content below**

```markdown
# Uganda Tax Framework for Business Plan Financial Projections

*Sources: Income Tax Act Cap.340 (Okuja, Onyango & Co. Advocates); Value Added Tax Act Cap.349; KPMG, Tax (Amendment) Bills, 2025 — A KPMG Analysis, April 2025 (East Africa).*

This reference file provides the tax rates, computation methodology, and planning guidance needed to produce credible financial projections for a Ugandan business. Every projected P&L, cash flow statement, and balance sheet must reflect these obligations correctly.

---

## 1. Business Structure and Tax Regime

The legal structure of a business determines which tax rates apply. This must be established before any financial projection is built.

| Structure | Income Tax Regime | Registration |
|---|---|---|
| **Sole trader / individual business** | Personal income tax — graduated bands 0%–40% (Third Schedule, ITA) | No separate registration; files under owner's TIN |
| **Partnership** | Partners taxed individually on their share of partnership income | Partnership deed; partners file individually |
| **Private limited company (Ltd)** | Corporate income tax — flat 30% on taxable profit | URSB registration; separate TIN (BRN) |
| **Public limited company (PLC)** | Corporate income tax — flat 30%; dividends WHT at 10% (listed on USE) | Uganda Securities Exchange listing |

**Planning rule:** State the legal structure explicitly in the financial projections assumptions. Apply the correct tax rate. A sole trader earning UGX 60M/year pays significantly less income tax than a company (graduated rates vs. 30% flat).

---

## 2. Corporate Income Tax

**Rate:** 30% of taxable (chargeable) income (s.7, ITA Cap.340; Part II, Third Schedule)

**Who it applies to:** All companies registered in Uganda, including private limited companies and branch operations.

**Taxable income = Gross revenue − allowable deductions**

Allowable deductions include:
- Cost of goods sold
- Staff salaries and NSSF employer contributions
- Rent and utilities
- Marketing expenses
- Depreciation on fixed assets (at prescribed rates per Sixth Schedule)
- Interest on business loans
- Bad debts written off
- Training expenditure
- Start-up costs (amortised over 3 years)

**Excluded from deductions:**
- Capital expenditure (depreciated, not expensed in full)
- Personal expenses of directors
- Fines and penalties
- Income tax itself

**Computation example (company):**

```
Revenue:                          UGX 500,000,000
Less: Cost of Goods Sold         (UGX 200,000,000)
Gross Profit:                     UGX 300,000,000
Less: Operating Expenses         (UGX 150,000,000)
  - Salaries:         80,000,000
  - Rent:             30,000,000
  - Marketing:        20,000,000
  - Utilities:        10,000,000
  - Depreciation:     10,000,000
EBITDA:                           UGX 160,000,000
Less: Depreciation               (UGX  10,000,000)
EBIT:                             UGX 150,000,000
Less: Loan interest              (UGX  20,000,000)
Profit Before Tax:                UGX 130,000,000
Corporate Tax @ 30%:             (UGX  39,000,000)
Net Profit After Tax:             UGX  91,000,000
```

**Tax payment schedule:**
- Provisional tax: two equal instalments due 6th month and 12th month of the tax year
- Final assessment: filed within 6 months of year-end
- Tax year = financial year of the company (may differ from calendar year)

---

## 3. Individual Income Tax (PAYE)

**Rates:** Graduated 0%–40% (s.6; Part I, Third Schedule, ITA Cap.340)

### PAYE Bands — Resident Individuals

| Annual Chargeable Income (UGX) | Monthly Equivalent (UGX) | Tax Payable |
|---|---|---|
| Not exceeding 2,820,000 | Up to 235,000 | **0%** |
| 2,820,001 – 4,020,000 | 235,001 – 335,000 | 10% of excess over 2,820,000 |
| 4,020,001 – 4,920,000 | 335,001 – 410,000 | 120,000 + 20% of excess over 4,020,000 |
| 4,920,001 – 120,000,000 | 410,001 – 10,000,000 | 300,000 + 30% of excess over 4,920,000 |
| Exceeding 120,000,000 | Above 10,000,000 | 34,824,000 + 40% of excess over 120,000,000 |

**Employer obligations:**
- Withhold PAYE from each employee's gross salary monthly
- Remit withheld amounts to URA by the **15th of the following month**
- File monthly PAYE returns on URA e-Tax portal
- Issue each employee a tax credit certificate (P9 form) annually

**PAYE computation example (monthly salary UGX 1,500,000):**

```
Monthly salary:                  UGX 1,500,000
Annual equivalent:               UGX 18,000,000

Tax on first UGX 2,820,000:           UGX 0
Tax on UGX 2,820,001–4,020,000:       UGX 120,000   (10% × 1,200,000)
Tax on UGX 4,020,001–4,920,000:       UGX 180,000   (20% × 900,000)
Tax on UGX 4,920,001–18,000,000:      UGX 3,924,000 (30% × 13,080,000)

Annual PAYE:                     UGX 4,224,000
Monthly PAYE deduction:          UGX 352,000

Net monthly take-home:           UGX 1,148,000
```

**Planning implication:** Show PAYE as a deduction from each employee's gross salary. The gross salary is a company expense; PAYE is borne by the employee but the employer is the collection agent. NSSF employee contribution (5%) is also deducted from gross salary.

---

## 4. Value Added Tax (VAT)

**Rate:** 18% (standard rate) (VATA Cap.349)

**Registration threshold:** UGX 150,000,000 gross turnover per year (UGX 12,500,000/month)

**Key mechanics:**
- Registered businesses charge VAT to customers on all taxable supplies (output VAT)
- Businesses recover VAT paid on business purchases (input VAT)
- **VAT payable = Output VAT − Input VAT**
- If input VAT exceeds output VAT, the excess is refundable by URA (refund claims in practice take 3–6 months)

**Filing:** Monthly VAT returns due by the **15th of the following month**, filed on URA e-Tax portal with EFRIS-generated invoices.

**EFRIS (Electronic Fiscal Receipting and Invoicing Solution):** Mandatory for all VAT-registered businesses from 2021. All tax invoices must be issued through the EFRIS system. Failure to comply attracts a penalty of **double the tax due** on affected transactions (Tax Procedures Code Amendment 2025).

**Exempt supplies (no VAT charged, no input VAT recovery):**
- Financial services, educational services, medical services
- Agricultural produce (unprocessed)
- Residential rent

**Zero-rated supplies (0% VAT but input VAT is recoverable):**
- Exports of goods
- Supply of aircraft
- Medicines and agricultural inputs

**Planning rules:**
- If projected turnover ≥ UGX 150M: model VAT registration from the month that threshold is crossed
- Show VAT separately — it is a liability (collected on behalf of URA), not revenue
- Budget for EFRIS hardware/software setup: approx. UGX 500,000–2,000,000 for a basic system
- Do not confuse gross (VAT-inclusive) revenue with net (ex-VAT) revenue in the P&L

**VAT anti-fragmentation (2025 amendment):** URA may aggregate consignments from the same importer to determine if the UGX 150M registration threshold is exceeded. Do not model consignment splitting as a VAT avoidance strategy.

---

## 5. Withholding Tax (WHT)

WHT is collected at source by the paying party (withholding agent) and remitted to URA. It is credited against the payee's annual tax assessment.

| Payment Type | Rate | Section | Notes |
|---|---|---|---|
| Goods and services (designated payers) | **6%** | s.119, ITA | Applies where contract value ≥ UGX 1M; most government and large-company purchases |
| Professional / management fees | **6%** | s.118A, ITA | Legal, accounting, consulting fees |
| Asset disposal (purchaser withholds) | **10%** | s.118B, ITA | Applied on the gross purchase price of business assets |
| Dividends — resident (unlisted company) | **15%** | s.118, ITA | Withheld by company paying dividend |
| Dividends — resident (USE-listed company) | **10%** | s.118, ITA | Listed company rate |
| Interest on government securities | **20%** | s.117, ITA | Treasury bills, Bank of Uganda bills |
| Non-resident digital services (to associates) | **15%** | s.83, ITA (2025) | Increased from 5% under 2025 amendment |

**Planning implications:**
- If the business sells to government or large companies: expect 6% WHT deducted from every payment. Cash flow projections must account for WHT deductions — the business receives 94% of invoice value and claims the 6% back at year-end assessment
- If the business pays professional fees (lawyers, accountants, consultants): withhold 6% and remit to URA by the 15th of the following month — failure attracts personal liability for the withheld amount
- WHT on asset disposal: if the business sells equipment or property, the buyer withholds 10% of the purchase price and pays it to URA

---

## 6. Presumptive Tax (Small Business Tax)

**Applicable to:** Resident individuals and companies with **gross turnover below UGX 150 million** who do not opt into normal assessment (s.4(5), ITA Cap.340; Second Schedule).

**Rate:** Fixed tax amounts by turnover band, set in the Second Schedule to the ITA. The tax is a **final tax** — no deductions, no credits (except some WHT credits).

**Who should NOT use presumptive tax:**
- Businesses earning above UGX 150M (must use normal assessment)
- Professional service businesses (medical, dental, legal, accounting, engineering, construction) — excluded by s.4(7)
- Businesses that want to carry forward losses or claim input VAT credits

**Planning rule:** If the projected business is a small, informal, or early-stage operation below UGX 150M turnover, note which tax regime applies (presumptive vs. normal) in the financial assumptions. Presumptive tax is often simpler and lower, but forfeits the ability to offset deductions. For businesses with high expenses (cost-heavy manufacturing, construction), normal assessment is usually preferable even below the threshold.

---

## 7. Rental Tax

**Rate:** 20% of net rental income for individuals; 30% for companies (s.5, ITA Cap.340; Part VI, Third Schedule)

**Applicable to:** Any person (individual or company) deriving income from renting property in Uganda.

**Net rental income = Gross rent received − allowable deductions**

Allowable deductions for rental income: mortgage interest, repairs and maintenance, insurance, local authority rates, depreciation (commercial buildings).

**Planning implication:** If the business owns property and earns rental income alongside business income, rental tax is calculated separately from corporate/personal income tax. Show rental income and rental tax as distinct line items from business operations.

---

## 8. NSSF Contributions

**Rate:** 10% employer + 5% employee = **15% of gross wage** per employee

**Mandatory for:** Employers with **5 or more employees** (National Social Security Fund Act)

**Payment:** Both employer and employee contributions must be remitted to NSSF by the **15th of the following month**. Employer contribution is an operating expense; employee contribution is deducted from gross salary.

**NSSF computation example (monthly salary UGX 800,000):**

```
Employee contribution (5%):  UGX  40,000  — deducted from salary
Employer contribution (10%): UGX  80,000  — additional business cost
Total NSSF:                  UGX 120,000

Business cost of this employee:
  Gross salary:              UGX 800,000
  NSSF (employer):           UGX  80,000
  Total payroll cost:        UGX 880,000
```

**Planning rule:** Show payroll cost as gross salary PLUS employer NSSF (10%). Do not forget this 10% when computing total staff costs. Many first-time projections omit NSSF and understate operating costs by 10% of payroll.

---

## 9. Import Duties and Levies

### EAC Common External Tariff (CET)

| Category | Rate | Examples |
|---|---|---|
| Capital goods, raw materials | **0%** | Production machinery (Ch.84, 85), agricultural inputs |
| Intermediate goods | **10%** | Semi-finished materials, components |
| Finished consumer goods | **25%** | Most imported finished products |

Actual rates vary by HS (Harmonised System) code. For any imported item, verify the HS code and applicable rate before projecting import costs.

### New Import Levies Effective 1 July 2025 (External Trade Amendment Bill 2025)

| Levy | Rate | Basis | Exemptions |
|---|---|---|---|
| Infrastructure levy | **1.5%** | Customs value (CIF) | Ch.84/85 plant and machinery; Fifth Schedule EAC exempt goods |
| Import declaration fee | **1.0%** | Customs value (CIF) | Ch.84/85 plant and machinery; Fifth Schedule EAC exempt goods |
| **Total additional cost** | **2.5%** | — | — |

**Planning rules:**
- Capital equipment (production machinery, vehicles for business) under EAC CET Chapters 84–85: **exempt from both levies**. No adjustment needed to capex budget.
- Raw materials, packaging, consumables, and finished goods imported from outside EAC: **add 2.5% to customs value** as an additional landed cost on top of existing duty.
- For a business importing, say, UGX 100M of consumables annually from outside EAC: add UGX 2.5M to annual input costs.

---

## 10. 2025 Tax Amendments — Planning Checklist

All business plans for operations starting on or after 1 July 2025 must address the following:

| Amendment | Action Required in the Business Plan |
|---|---|
| **3-year income tax exemption** (citizen-owned, capital ≤ UGX 500M) | State whether the business qualifies. If yes, show zero income tax in Years 1–3 financial projections. Note the exemption and its conditions in the financial assumptions. |
| **1.5% infrastructure levy on non-machinery imports** | Add 1.5% to customs value of any non-machinery imports from outside EAC in the cost model. |
| **1.0% import declaration fee** | Add 1.0% to customs value of any non-machinery imports from outside EAC. |
| **Stamp duty NIL on mortgage deeds** | Reduce the cost of borrowing in the funding request — mortgage deed no longer costs 0.5% of loan value. |
| **EFRIS mandatory (electronic receipting)** | Include EFRIS setup cost (UGX 500K–2M) in capital or setup costs. Add EFRIS compliance to the operations plan. Note penalty exposure (double the tax due) in the risk register. |
| **TIN = NIN/BRN required for licences** | Include NIN (individual) or URSB BRN (company) acquisition as a prerequisite step in the implementation timeline before any licence application. |
| **VAT anti-fragmentation** | Do not model consignment splitting as a VAT avoidance strategy for imported goods. |

---

## 11. Tax Schedule Template for Financial Projections

Every projected financial statement must include a Tax Schedule showing all tax obligations as separate line items. This is mandatory for bank and DFI submissions.

### P&L Tax Line Items

```
Revenue (ex-VAT)
Less: Cost of Goods Sold
= Gross Profit
Less: Operating Expenses
  Salaries (gross)                      XXX
  NSSF — employer contribution (10%)    XXX
  Rent                                  XXX
  Utilities                             XXX
  Marketing                             XXX
  Depreciation                          XXX
  Other expenses                        XXX
= EBITDA
Less: Depreciation
= EBIT
Less: Interest on loans
= Profit Before Tax
Less: Income Tax
  [Corporate 30% OR individual graduated rate OR 0% if 3-year exemption applies]
= Net Profit After Tax
```

### Monthly Cash Flow — Tax Payment Lines

```
Cash from operations
  Collections from customers (inc. VAT where applicable)
Cash payments:
  Supplier payments
  Gross salaries paid
  PAYE remittance (by 15th of month)
  NSSF remittance (employer + employee, by 15th of month)
  WHT remitted to URA (by 15th of month, if applicable)
  VAT net payment to URA (by 15th of month) OR VAT refund receipt
  Provisional income tax instalment (months 6 and 12)
= Closing cash balance
```

### Balance Sheet — Tax Liability Lines

```
Current Liabilities:
  PAYE payable (accrued but not yet remitted)
  VAT payable (output minus input, due by 15th)
  NSSF payable
  Income tax payable (provisional instalments)
  Withholding tax payable
```

---

## 12. Common Projection Errors to Avoid

| Error | Correct Treatment |
|---|---|
| Applying 30% tax to a qualifying start-up in Years 1–3 | Check 3-year exemption eligibility; show 0% if eligible |
| Omitting NSSF employer contribution (10%) from payroll cost | Total payroll cost = gross salary × 1.10 (for businesses with ≥5 staff) |
| Including VAT in revenue | P&L revenue is always ex-VAT; VAT is a separate balance sheet liability |
| Treating WHT deducted by customers as a loss | WHT is a tax prepayment; credit against annual tax assessment |
| Forgetting import levy additions on consumables | Non-machinery imports from outside EAC now carry 2.5% additional cost |
| Applying individual tax rates to a company | Companies pay flat 30%; individuals pay graduated rates |
| Computing PAYE at a flat percentage | PAYE is graduated; compute band by band for each employee's salary level |
```

**Step 2: Verify the file is complete and well-formed**

Read the file back and confirm all 12 sections are present with no truncation.

**Step 3: Commit**

```bash
git add 10-financial-projections/references/uganda-tax-framework.md
git commit -m "feat(refs): create uganda-tax-framework.md with authoritative ITA Cap.340 rates and 2025 amendments"
```

---

## Task 5: Final verification and wrap-up

**Step 1: Check word count and structure of 01-critical-gaps.md**

Confirm the file now has C4 (with stamp duty note), C5 (rewritten), C6, C7, C8 (new) — five gap sections plus introductory text.

**Step 2: Check the reference file exists**

Confirm `10-financial-projections/references/uganda-tax-framework.md` exists alongside the other four reference files in that directory.

**Step 3: Final commit (if any loose files)**

```bash
git status
git add -A
git commit -m "docs(gaps): complete Uganda tax framework — C4 patch, C5 rewrite, C8 new gap, tax reference file"
```

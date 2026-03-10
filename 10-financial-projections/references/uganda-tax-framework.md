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

# Cross-Section Consistency Audit

*A plan that is internally inconsistent will be rejected by any experienced credit analyst, regardless of how strong individual sections are. This audit checks that all numbers, claims, and commitments are aligned across the 15 sections before submission.*

---

## How to Run the Consistency Audit

Extract the key data points from each section and populate the table below. Then run each consistency check. Any mismatch is flagged as a FAIL — do not submit until all FLAGs are resolved.

---

## Step 1: Extract Key Figures

Before running checks, record these values from the completed plan:

```
DATA EXTRACTION SHEET

FROM SECTION 04 (Market Analysis):
  Total addressable market (TAM): UGX ___________
  Serviceable available market (SAM): UGX ___________
  Target market share (Year 3): ___________% = UGX ___________
  Annual market growth rate used: ___________%

FROM SECTION 05 (Target Market):
  Number of target customers (Year 1): ___________
  Average revenue per customer: UGX ___________
  Implied Year 1 revenue from customer count: UGX ___________

FROM SECTION 07 (Marketing Strategy):
  Marketing budget (Year 1): UGX ___________
  Prices listed for main products/services: UGX ___________ / ___________

FROM SECTION 08 (Operations):
  Staff headcount (Year 1): ___________
  Production capacity (units/month): ___________
  Cost per unit / service delivery cost: UGX ___________

FROM SECTION 09 (Management Team):
  Key personnel named: ___________
  Total management headcount: ___________

FROM SECTION 10 (Financial Projections):
  Year 1 revenue: UGX ___________
  Year 2 revenue: UGX ___________
  Year 3 revenue: UGX ___________
  Year 1 net profit (or loss): UGX ___________
  Year 3 net profit: UGX ___________
  Month of break-even: ___________
  EBITDA (Year 3): UGX ___________
  Total staff costs (Year 1): UGX ___________
  Staff headcount in projections (Year 1): ___________
  Average gross salary in projections: UGX ___________/month
  Gross profit margin (%): ___________%
  Tax rate applied: ___________%

FROM SECTION 11 (Funding Request):
  Amount requested: UGX ___________
  Loan term: ___________ years
  Monthly repayment: UGX ___________
  Annual debt service: UGX ___________
  DSCR calculation: ___________ / ___________ = ___________x
  Collateral offered: UGX ___________
  Collateral coverage ratio: ___________%
  Total use-of-funds budget: UGX ___________

FROM SECTION 12 (Risk Analysis):
  Top 3 risks identified: (1) ___________ (2) ___________ (3) ___________
  Cash flow risk listed: Yes / No

FROM SECTION 13 (Implementation Timeline):
  Total capital expenditure budget: UGX ___________
  Start date: ___________
  Month of first revenue: ___________
  Staff hiring schedule — first hire: ___________

FROM SECTION 15 (Appendices):
  Loan repayment schedule included: Yes / No
  Financial summary table total revenue (Year 3): UGX ___________
```

---

## Step 2: Run Consistency Checks

### CHECK 1: Revenue — Market vs. Projections

**Test:** Year 3 projected revenue must be ≤ target market share (SAM × target %)

```
Year 3 Revenue (§10):          UGX ___________
SAM × Target Share (§04):      UGX ___________
Market share implied (Year 3): ___________% of SAM

PASS if: Year 3 revenue ≤ SAM × a credible market share (typically < 25%)
FAIL if: Year 3 revenue exceeds what the stated market can support
```

**Common failure:** Projections show UGX 800M revenue but market analysis says the total market is UGX 500M.

**Fix:** Either increase the market sizing or reduce the revenue projection, with explanation.

---

### CHECK 2: Revenue — Customer Count vs. Projections

**Test:** Year 1 revenue ÷ revenue per customer must roughly equal stated customer count

```
Year 1 Revenue (§10):              UGX ___________
Revenue per customer (§05 or §07): UGX ___________
Implied customer count:            ___________

Stated target customers (§05):     ___________

PASS if: Implied count is within 20% of stated target
FAIL if: Numbers diverge significantly
```

**Common failure:** Target market section says "we will serve 50 customers" but projections show 200 transactions.

---

### CHECK 3: Prices — Marketing vs. Financials

**Test:** Prices quoted in marketing section and operations section must match projections

```
Price in §07 (Marketing):     UGX ___________
Price used in §10 (Revenue):  UGX ___________

PASS if: Same price (or deliberate variation explained — e.g., different customer tiers)
FAIL if: Prices differ without explanation
```

---

### CHECK 4: Staff — Operations vs. Projections vs. Management Team

**Test:** All three sections must show the same staffing plan

```
Headcount in §08 (Operations):        ___________
Headcount in §10 (Staff cost line):   ___________
Management named in §09:              ___________

PASS if: All three match (or differences explained — e.g., §08 includes owners who are not in payroll)
FAIL if: Operations says 20 staff but projections only budget for 5
```

**Common failure:** Operations plan describes a full production team; projections only budget for 3 people because "owners will do the work initially."

---

### CHECK 5: Funding — Loan Amount vs. Use of Funds

**Test:** Loan amount (§11) must equal the sum of use-of-funds items

```
Loan amount (§11):              UGX ___________
Use-of-funds total (§11 table): UGX ___________

PASS if: They match exactly
FAIL if: Any gap between stated amount and itemised budget
```

---

### CHECK 6: Funding vs. Implementation Budget

**Test:** Implementation budget (§13) must match use of funds (§11)

```
Total capex/setup budget (§13): UGX ___________
Use of funds (§11):             UGX ___________

PASS if: Match within 5% (minor rounding acceptable)
FAIL if: Implementation budget ≠ use of funds
```

**Common failure:** Funding request says UGX 200M needed; implementation timeline shows UGX 150M of expenditure. The bank asks: "Where does the other UGX 50M go?"

---

### CHECK 7: DSCR Calculation

**Test:** DSCR must be calculated correctly from projections

```
EBITDA from §10 (Year 3 or first full year of operations): UGX ___________
Annual debt service from §11 (12 × monthly repayment):    UGX ___________
DSCR = EBITDA / Annual Debt Service:                       ___________x

PASS if: DSCR ≥ 1.25 AND calculation matches both §10 and §11 figures
FAIL if: DSCR < 1.25 OR if the numbers used don't match either section
```

**Critical:** If the DSCR in §11 is calculated from different figures than what appear in §10, the credit analyst will catch it immediately.

---

### CHECK 8: Collateral Coverage

**Test:** Collateral value must be ≥ 125% of loan amount

```
Collateral offered (§11):       UGX ___________
Loan amount (§11):              UGX ___________
Coverage ratio:                 ___________%

PASS if: Coverage ≥ 125%
WARNING if: Coverage 100–124% (note compensating factors)
FAIL if: Coverage < 100%
```

---

### CHECK 9: Break-Even Consistency

**Test:** Break-even month in projections must be consistent with cash flow stress test

```
Break-even month (§10):                   Month ___________
First revenue month (§13 timeline):       Month ___________
Break-even in stress test (pessimistic):  Month ___________

PASS if: Break-even is after first revenue month; stress test break-even is later than base case
FAIL if: Break-even is before first revenue month (impossible) or stress test is earlier than base case
```

---

### CHECK 10: Risk vs. Financial Contingency

**Test:** Every HIGH-rated risk in §12 must have a financial contingency visible in §10 or §11

```
High risks from §12:
  1. ___________  — Contingency in §10/§11: ___________
  2. ___________  — Contingency in §10/§11: ___________
  3. ___________  — Contingency in §10/§11: ___________

Cash flow risk identified (§12): Yes / No
Cash reserve in projections (§10): UGX ___________
Months of operating costs covered by cash reserve: ___________

PASS if: Each high risk has a corresponding mitigation cost or cash buffer in financials
FAIL if: Risk section identifies cash flow risk but projections show zero cash reserve
```

---

### CHECK 11: Tax Rate Consistency

**Test:** Tax rate applied in projections must match the business structure and 2025 exemption eligibility

```
Business legal structure:               ___________
Tax regime that should apply:           ___________% (or 0% if 3-year exemption)
Tax rate applied in §10 projections:    ___________%

If claiming 3-year exemption:
  Citizen ownership: Yes / No
  Capital ≤ UGX 500M: Yes / No
  New business (post July 2025): Yes / No
  Exemption stated in assumptions: Yes / No

PASS if: Tax rate matches legal structure AND exemption correctly applied (or not applied) in projections
FAIL if: Company applying 0% tax without stating exemption basis; or sole trader projections using 30% corporate rate
```

---

### CHECK 12: Appendix Financial Summary vs. Section 10

**Test:** Financial summary table in §15 must match §10 exactly

```
Year 3 Revenue in §10:                UGX ___________
Year 3 Revenue in §15 summary:        UGX ___________

Year 3 Net Profit in §10:             UGX ___________
Year 3 Net Profit in §15 summary:     UGX ___________

PASS if: Figures match exactly
FAIL if: Any figure differs between the body of the plan and the appendix
```

---

## Step 3: Consistency Audit Summary

```
CONSISTENCY AUDIT RESULTS

Check 1 — Revenue vs. Market:         PASS / FAIL
Check 2 — Revenue vs. Customer Count: PASS / FAIL
Check 3 — Prices:                     PASS / FAIL
Check 4 — Staff:                      PASS / FAIL
Check 5 — Loan vs. Use of Funds:      PASS / FAIL
Check 6 — Funding vs. Implementation: PASS / FAIL
Check 7 — DSCR Calculation:           PASS / FAIL
Check 8 — Collateral Coverage:        PASS / FAIL
Check 9 — Break-Even:                 PASS / FAIL
Check 10 — Risk vs. Contingency:      PASS / FAIL
Check 11 — Tax Rate:                  PASS / FAIL
Check 12 — Appendix vs. Section 10:   PASS / FAIL

OVERALL: [X] of 12 checks passed

SUBMISSION READINESS:
12/12: Submit — fully consistent
10–11/12: Fix failures, then submit
< 10/12: Do not submit — revise plan systematically
```

---

## Common Root Causes of Inconsistency

1. **Sections written independently** — each section author uses slightly different assumptions
2. **Numbers updated in one section but not others** — revenue revised in §10 but not reflected in §05 customer count or §11 DSCR
3. **Copy-paste errors** — financial summary in §15 not updated after §10 revision
4. **Wrong tax regime** — not updated when legal structure decision changed
5. **Collateral value not updated** — valuation obtained after §11 was drafted

**Prevention:** Write section 10 (financial projections) first and use it as the single source of truth for all numbers in other sections.

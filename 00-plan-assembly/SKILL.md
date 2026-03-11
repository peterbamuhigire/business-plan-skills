---
name: plan-assembly
description: Final assembly skill that converts 15 completed sections into a submission-ready business plan document. Generates the covering letter, table of contents, required attachments checklist, and submission format guidance calibrated to the specific funder type (commercial bank, DFI, grant body, or equity investor). Use AFTER all 15 sections and meta-skills are complete.
---

# Plan Assembly and Submission Skill

Convert a completed set of business plan sections into a submission-ready document package. This skill is the last step before presenting to any funder.

## When to Use

Invoke AFTER:
- All 15 sections (01-executive-summary through 15-appendices) are drafted
- `meta-bankability-scoring` has been run and score is ≥ 6.5
- `meta-plan-consistency` check has been run with no critical inconsistencies
- Financial projections have been stress-tested (`meta-financial-stress-test`)
- `meta-due-diligence` Mode C has been run — all 15 sections pass DD audit (score ≥ 3.5 for bank; ≥ 4.0 for equity/DFI)

**After plan assembly, also prepare:**
- Presentation deck using `meta-presentation-design` — every submitted plan should be accompanied by a deck
- Pitch preparation using `meta-pitch-preparation` — client must be ready to defend the plan in person

## Step 1: Identify the Funder Type

Ask: **"Who is the primary recipient of this business plan?"**

| Funder Type | Orientation | Key Difference |
|---|---|---|
| **Commercial bank** (Centenary, Stanbic, dfcu, ABSA, Equity) | Debt — loan repayment focus | Cover letter addressed to Credit Manager; DSCR and collateral front and centre |
| **Development Finance Institution** (UDB, ACF, IFC) | Long-term debt + equity | Requires ESMP; feasibility study; impact metrics |
| **Grant body** (USAID, EU, GIZ, YLP, WEP) | Grant — no repayment | Redirect to `11b-grant-proposal` skill; LogFrame required |
| **Impact investor** (Acumen, Novastar, Pearl Capital, BII) | Equity + impact | Cap table, impact metrics, scale story |
| **Microfinance / SACCO** | Small debt, group guarantee | Simplified format; character references; group savings record |

## Step 2: Generate the Covering Letter

Every submission requires a formal covering letter. The plan without a covering letter goes into the wrong pile at every Ugandan bank.

### Bank Loan Covering Letter Template

```
[Business Letterhead]
[Business Name]
[Business Address]
[TIN / BRN]
[Phone] | [Email]

[Date]

The Branch Manager / Credit Manager
[Bank Name]
[Branch Name and Address]

Dear Sir/Madam,

RE: APPLICATION FOR UGX [AMOUNT] [LOAN TYPE] FACILITY

We write to formally apply for a [term loan / overdraft / asset finance facility] of
UGX [amount] ([amount in words]) to [specific purpose — e.g., "finance the
acquisition of production equipment and working capital for our maize flour
processing operation in Gulu District"].

[Business Name] is a [legal structure — e.g., private limited company] registered
with URSB under BRN [number], operating in [sector] since [year]. We have
[brief track record — e.g., "operated profitably for 3 years, serving 120 retail
customers monthly"].

The loan will be secured by [primary collateral — e.g., "land title LRV [X],
Block [X], Plot [X], valued at UGX [X] by [valuer name]"] and repaid from
[revenue source — e.g., "monthly maize flour sales of approximately UGX [X]"],
giving a Debt Service Coverage Ratio of [X.Xx].

Enclosed herewith please find our business plan and the following supporting
documents:

1. Business plan (this document)
2. Certificate of Incorporation / Business Name Certificate
3. Memorandum and Articles of Association
4. Trading licence — [issuing authority, year]
5. TIN / BRN certificate (URA)
6. Audited/management accounts — [years, or "cash flow records and bank
   statements for [period]" if formal accounts not available]
7. Bank statements — [institution, period]
8. Collateral documents — [land title / logbook / fixed deposit certificate]
9. Director CVs and identity documents (NIN copies)
10. Director personal net worth statements
11. [Any sector-specific licence — e.g., UNBS certificate, NEMA permit]

We confirm that all information provided herein is accurate and complete to the
best of our knowledge. We are available to discuss this application at your
convenience.

Yours faithfully,

_________________________
[Director Full Name]
[Title: Managing Director / Director]
NIN: [number]
[Date]
[Company Seal — if available]
```

### DFI (e.g. Uganda Development Bank) Covering Letter Additions

Add after the standard letter body:
```
This application is submitted in accordance with UDB's SME lending guidelines.
We note that the proposed investment [qualifies for / does not require] an
Environmental and Social Management Plan under IFC Performance Standard [X].
[If ESMP required: "Our ESMP is enclosed as Appendix [X]."]

The business [qualifies / does not qualify] for the 3-year income tax exemption
under the Income Tax (Amendment) Act 2025, as it is a new citizen-owned business
with investment capital below UGX 500 million.
```

### Grant Application Covering Letter

Redirect to `11b-grant-proposal/SKILL.md` — grant applications use a completely different format (proposal narrative, LogFrame, Theory of Change).

## Step 3: Binding Order by Funder

### Commercial Bank Submission Order

1. Covering letter (always first — it is the formal application)
2. Executive summary (§01)
3. Company overview + legal documents (§02)
4. Products and services (§03)
5. Market analysis (§04) + Target market (§05)
6. Competitive analysis (§06)
7. Marketing and sales strategy (§07)
8. Operations plan (§08)
9. Management team (§09)
10. **Financial projections (§10) — banks read this section most carefully**
11. **Funding request (§11) — DSCR, collateral, repayment schedule**
12. Risk analysis (§12)
13. Implementation timeline (§13)
14. AI/technology integration (§14)
15. Appendices (§15) — supporting documents

**Note:** Some Ugandan banks request the Executive Summary last (after appendices) as a one-page summary. If the bank provides a template or checklist, follow it exactly.

### Digital vs. Physical Submission

| Format | When Used | Requirements |
|---|---|---|
| Physical bound copy | Most Ugandan banks for initial submission | A4 paper, clear binding (not staples), index tabs for sections, labelled spine |
| PDF email submission | UDB online portal, some commercial banks | Single merged PDF, bookmarked sections, file size < 10MB |
| Online portal | UDB, Bank of Uganda-regulated institutions | Follow portal instructions exactly |

**Physical binding standard:** Spiral or comb binding preferred. Colour cover page with business name, funder name, date, and contact. Section dividers with tab labels. Page numbers throughout.

## Step 4: Required Attachments Checklist

Generate this checklist and check every item before submission:

### Universal Requirements (all funders)
- [ ] Certificate of Incorporation or Business Name Certificate (certified copy)
- [ ] TIN / BRN certificate (URA-issued)
- [ ] Trading licence — current year (KCCA or district)
- [ ] NIN copies for all directors (certified)
- [ ] Director CVs (standard format — see `15-appendices/references/document-templates.md`)
- [ ] Personal net worth statement for each director/guarantor
- [ ] Recent passport photographs of directors (if required by bank)

### Financial Records (required by all banks)
- [ ] 3 years audited accounts OR 2 years management accounts + bank statements
- [ ] 6–12 months bank statements (business account)
- [ ] 6 months mobile money / M-Pesa statements (if primary transaction record)
- [ ] URA tax compliance certificate (TCC) — printable from URA e-Tax portal
- [ ] NSSF compliance certificate (if applicable)

### Collateral Documents
- [ ] Land title (certified copy from Land Registry) + current valuation report
- [ ] Motor vehicle logbook (if offered as security)
- [ ] Fixed deposit certificate (if cash collateral)
- [ ] Equipment purchase receipts / proforma invoices (if asset finance)

### Sector-Specific (add relevant items)
- [ ] UNBS product registration certificate (food, cosmetics, industrial products)
- [ ] NEMA environmental permit / Certificate of Approval
- [ ] NDA licence (food products with health claims, pharmaceuticals)
- [ ] Uganda Tourism Board licence (hotels, lodges, tour operators)
- [ ] Bank of Uganda authorisation (deposit-taking, lending, forex)
- [ ] Professional body membership certificates (ICPAU, ULS, UMC, etc.)
- [ ] NAADS / MAAIF certification (agricultural businesses)

### For DFI Applications (add to above)
- [ ] Environmental and Social Management Plan (ESMP)
- [ ] Feasibility study (technical + financial)
- [ ] Audited accounts — minimum 2 years (or projected accounts for startups)
- [ ] Evidence of promoter equity contribution (bank statements, asset valuations)

## Step 5: Table of Contents

Generate a table of contents with page numbers. Verify that every section reference in the plan (e.g., "See Financial Projections, Section 10") matches the actual page.

**TOC Format:**
```
TABLE OF CONTENTS

Covering Letter .................................................. i
Executive Summary ............................................... 1
1. Company Overview ............................................. X
2. Products and Services ........................................ X
3. Market Analysis .............................................. X
4. Target Market ................................................ X
5. Competitive Analysis ......................................... X
6. Marketing and Sales Strategy ................................. X
7. Operations Plan .............................................. X
8. Management Team .............................................. X
9. Financial Projections ........................................ X
10. Funding Request ............................................. X
11. Risk Analysis ............................................... X
12. Implementation Timeline ..................................... X
13. AI and Technology Integration ............................... X
Appendices
  A: Director CVs ............................................... X
  B: Financial Statements / Projections Detail .................. X
  C: Collateral Documents ....................................... X
  D: Licences and Certificates .................................. X
  E: Market Research Data ....................................... X
  F: Letters of Intent / Customer Commitments ................... X
```

## Step 6: Final Pre-Submission Check

Before handing over the document, verify:

- [ ] All UGX figures in the plan are consistent (§10 revenue matches §04 market size; §11 loan amount matches §10 DSCR calculation; §13 budget matches §11 use of funds)
- [ ] All dates are realistic and internally consistent
- [ ] Covering letter is signed with blue ink (physical submission)
- [ ] Company seal is affixed to the covering letter (if company has a seal)
- [ ] All certified copies are certified by a Commissioner for Oaths or notary
- [ ] File is paginated — every page has a page number
- [ ] Executive summary is max 2–3 pages (banks do not read longer summaries)
- [ ] Financial projections are in UGX (not USD unless foreign-currency loan)
- [ ] DSCR calculation is correct and prominently displayed in §11

## References

- `references/submission-guide.md` — Funder-specific submission requirements and contact details
- `references/covering-letter-templates.md` — Extended covering letter variants
- `15-appendices/references/document-templates.md` — Director CV template, net worth statement, loan repayment schedule template
- `11-funding-request/references/credit-assessment-frameworks.md` — 5 Cs / CAMPARI for self-check
- `meta-due-diligence/SKILL.md` — Run Mode C (plan DD audit) before submission; every material claim must pass the 15-section verification table; data room structure for investor submissions
- `meta-presentation-design/SKILL.md` — Build the accompanying slide deck after plan assembly; 13-slide master template; client coaching protocol for delivery
- `meta-pitch-preparation/SKILL.md` — Frame and delivery preparation; run alongside meta-presentation-design to prepare client for the live pitch

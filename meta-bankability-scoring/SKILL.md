---
name: meta-bankability-scoring
description: Analytical meta-skill that scores a complete business plan against 12 investor-readiness dimensions derived from Rogoff's bankability framework. Produces a weighted scorecard, identifies weaknesses, and recommends improvements to increase funding probability.
---

# Bankability Scoring Meta-Skill

## Use When

- Use after a full draft exists and before presenting to a lender or investor.
- Use when the question is not just "is this good?" but "is this financeable?"
- Use when a team needs a scored readiness view and prioritised fix list.

## Do Not Use When

- Do not use on an early concept with no real plan behind it.
- Do not use the score as a substitute for fixing underlying weaknesses.
- Do not treat a high score as immunity from DD, valuation, or market scrutiny.

## Required Inputs

- Full or near-full plan sections
- Funder type and country context
- Financial model and funding ask
- Appendix and evidence status where available

## Workflow

1. Confirm the plan is mature enough to score.
2. Evaluate the plan against the bankability dimensions and weighted criteria.
3. Score each dimension with evidence-based reasoning.
4. Identify the lowest-scoring constraints on fundability.
5. Produce a practical improvement sequence.
6. Reconcile the score with consistency, DD, and funding-mode logic.

## Quality Bar

- Scores are justified with real evidence from the document.
- The output distinguishes fatal flaws from improvable weaknesses.
- The result is usable as a gate, not just commentary.
- Recommendations clearly increase funding probability.

## Anti-Patterns

- Inflating scores to be encouraging.
- Scoring sections in isolation without cross-checking consistency.
- Giving cosmetic recommendations instead of deal-critical fixes.
- Treating investor and bankability standards as interchangeable.

## Outputs

- Weighted bankability score
- Dimension-by-dimension rationale
- Priority weaknesses
- Improvement actions and next gate recommendation



Score the complete business plan against the criteria investors and lenders actually use to make funding decisions.

## When to Use

Invoke AFTER the complete plan (sections 01-15) is drafted. This is the final quality gate before presenting to investors.

## Scoring Framework

### 12 Bankability Dimensions

Score each dimension 1-10, with defined criteria:

| # | Dimension | Weight | What Investors Look For |
|---|-----------|--------|------------------------|
| 1 | **Market opportunity** | 12% | Large, growing, well-defined market |
| 2 | **Problem-solution fit** | 10% | Clear pain point with compelling solution |
| 3 | **Competitive advantage** | 10% | Defensible moat, not just "we're better" |
| 4 | **Business model clarity** | 10% | Clear path from product to revenue |
| 5 | **Revenue model strength** | 8% | Scalable, recurring, predictable revenue |
| 6 | **Financial viability** | 12% | Realistic projections, clear path to profit |
| 7 | **Team capability** | 12% | Right people with relevant track record |
| 8 | **Traction & validation** | 8% | Evidence of market demand  earlyvangelists, preselling, product-market fit (Sean Ellis 40% threshold) |
| 9 | **Scalability** | 6% | Can the business grow 10x without breakingSection  |
| 10 | **Risk awareness** | 4% | Honest risk assessment with mitigation plans; Assumptions Tracking with Risk Score <100 (Alam) |
| 11 | **Clarity of ask** | 4% | Specific funding need with clear use of funds |
| 12 | **AI & operational efficiency** | 4% | Smart use of technology and automation; process maturity level (Dumas et al., 2013) |

### Scoring Scale

- **9-10:** Exceptional  investor-ready, compelling
- **7-8:** Strong  minor improvements needed
- **5-6:** Adequate  notable gaps to address
- **3-4:** Weak  significant revision required
- **1-2:** Critical  fundamental issues present

### Overall Bankability Rating

**Weighted score calculation:** Sum of (dimension score x weight)

| Overall Score | Rating | Recommendation |
|---|---|---|
| 8.0-10.0 | **Investment Ready** | Submit to investors with confidence |
| 6.5-7.9 | **Nearly Ready** | Address flagged weaknesses, then submit |
| 5.0-6.4 | **Needs Work** | Significant revision required before submission |
| Below 5.0 | **Not Ready** | Fundamental rethinking needed |

### Process Maturity Assessment (Supplementary)

When scoring dimensions 9 (Scalability) and 12 (AI & operational efficiency), assess the business's process maturity level (Dumas et al., 2013):

| Level | Rating | Score Guidance |
|---|---|---|
| Level 1  Initial | Ad-hoc, hero-dependent | Scalability: max 4/10; AI: max 3/10 |
| Level 2  Repeatable | Key processes documented | Scalability: max 6/10; AI: max 5/10 |
| Level 3  Defined | All processes standardised and measured | Scalability: 6-8/10; AI: 6-7/10 |
| Level 4  Managed | Quantitative monitoring, SLAs | Scalability: 7-9/10; AI: 7-8/10 |
| Level 5  Optimised | Continuous improvement culture | Scalability: 8-10/10; AI: 8-10/10 |

A business cannot score highly on scalability without documented, standardised processes. Process maturity is a prerequisite for sustainable growth.

## Scoring Output Format

### Dimension Scorecard

```
Dimension: [Name]
Score: [X/10]
Weight: [X%]
Weighted: [Score x Weight]
Strengths: [What works well]
Weaknesses: [What needs improvement]
Recommendation: [Specific action to improve score]
Section reference: [Which plan section to revise]
```

### Summary Dashboard

```
BANKABILITY SCORECARD
=====================
Overall Score: X.X / 10.0
Rating: [Investment Ready / Nearly Ready / Needs Work / Not Ready]

Top Strengths:
1. [Dimension]  [Why it scores well]
2. [Dimension]  [Why it scores well]

Critical Weaknesses:
1. [Dimension]  [Score]  [What to fix]
2. [Dimension]  [Score]  [What to fix]

Priority Actions (ranked by impact on overall score):
1. [Action]  Expected score improvement: +X.X
2. [Action]  Expected score improvement: +X.X
3. [Action]  Expected score improvement: +X.X
```

## Generation Process

1. Read the complete business plan (sections 01-15)
2. Score each of the 12 dimensions with evidence from the plan
3. Calculate weighted overall score
4. Identify top 3 strengths and top 3 weaknesses
5. Generate prioritised improvement recommendations
6. Estimate score improvement for each recommendation
7. Produce summary dashboard

## Quality Criteria

- Scoring is evidence-based  every score cites specific plan content
- Feedback is constructive and actionable, not just criticism
- Recommendations are prioritised by impact on overall score
- Scoring is calibrated  a 7 means the same thing across dimensions

---

## Bank Loan Readiness Mode (Uganda / East Africa)

**When to use:** When the primary funder is a Ugandan commercial bank, DFI (UDB, ACF), or microfinance institution  not an equity investor.

Invoke this mode when the user says "bank loan", "UDB", "Centenary", "dfcu", "Stanbic", or similar.

### Bank Loan Readiness Checklist (CAMPARI Framework)

Score each item YES / PARTIAL / NO. A plan is not bank-ready until all critical items score YES or PARTIAL with a clear path to YES.

**CHARACTER (Who is this borrowerSection )**
- [ ] Director CVs included with full employment and business history (09, Appendix)
- [ ] NIN confirmed for all directors (02)
- [ ] No adverse credit history disclosed (or disclosed with explanation)
- [ ] Character references from respected community members included (Appendix)
- [ ] Business registered with URSB and TIN/BRN held (02)

**ABILITY (Can they run this businessSection )**
- [ ] Management team has direct sector experience (09)
- [ ] If no sector experience: compensated by advisory board, hired expertise, or training plan
- [ ] Professional qualifications listed where applicable (ICPAU, ULS, UMC, ERB) (09)
- [ ] Operations plan demonstrates operational competence (08)

**MEANS (Can they afford to service the debtSection )**
- [ ] DSCR  1.25x calculated from projections (10, 11)  **CRITICAL**
- [ ] Owner equity contribution  20% of total project cost (11)
- [ ] Personal net worth statements for all directors included (Appendix)
- [ ] Cash flow projections show positive operating cash flow within 12 months

**PURPOSE (Is the loan for a legitimate productive useSection )**
- [ ] Specific purpose stated  not vague "working capital" (11)
- [ ] Use of funds itemised to individual line items (11)
- [ ] Loan purpose aligns with the business's stated operations (08)

**AMOUNT (Is the loan amount correctly sizedSection )**
- [ ] Loan amount equals sum of use-of-funds items (11)  check via `consistency-audit.md`
- [ ] Loan is not excessive relative to business revenue (loan  3 annual revenue for SME)
- [ ] Loan structure matches purpose (term loan for capex; overdraft for working capital)

**REPAYMENT (Will they repaySection )**
- [ ] Repayment source clearly identified (specific revenue stream) (11)
- [ ] Loan repayment schedule included (Appendix)
- [ ] DSCR stress-tested under pessimistic scenario (meta-financial-stress-test)
- [ ] Break-even month identified and precedes loan repayment start (10)

**INSURANCE (What security is offeredSection )**
- [ ] Primary collateral identified with estimated value (11)  **CRITICAL**
- [ ] Collateral coverage  125% of loan amount (11)
- [ ] Collateral documentation listed (Appendix  land title, logbook, etc.)
- [ ] Insurance on collateral assets included in operating budget (08, 12)
- [ ] If collateral is insufficient: compensating factors named (UCGS, group guarantee, character lending)

### Bank Loan Readiness Score

```
BANK LOAN READINESS ASSESSMENT

CAMPARI Score:
  Character:   [X/5 items]  [READY / PARTIAL / NOT READY]
  Ability:     [X/4 items]  [READY / PARTIAL / NOT READY]
  Means:       [X/4 items]  [READY / PARTIAL / NOT READY]
  Purpose:     [X/3 items]  [READY / PARTIAL / NOT READY]
  Amount:      [X/3 items]  [READY / PARTIAL / NOT READY]
  Repayment:   [X/4 items]  [READY / PARTIAL / NOT READY]
  Insurance:   [X/5 items]  [READY / PARTIAL / NOT READY]

CRITICAL CHECKS (must be YES to submit):
  / DSCR  1.25x: [Yes/No]  calculated as [X] / [X] = [X.Xx]
  / Collateral  125%: [Yes/No]  [UGX X collateral / UGX X loan = X%]
  / Business registered + TIN held: [Yes/No]
  / Specific purpose stated with itemised use of funds: [Yes/No]

OVERALL BANK LOAN READINESS:
  [SUBMIT] All critical items pass; CAMPARI  75% complete
  [REVISE] One or more critical items fail  do not submit yet
  [NOT READY] Multiple critical failures  major revision required

TOP 3 ACTIONS BEFORE SUBMISSION:
1. [Most critical gap]  fix in [X]
2. [Second gap]  fix in [X]
3. [Third gap]  fix in [X]
```

### Consistency Audit (run before scoring)

Before running the Bank Loan Readiness assessment, run the consistency audit from:
`meta-bankability-scoring/references/consistency-audit.md`

A plan that fails  3 consistency checks should be revised before scoring  inconsistencies undermine all other scoring dimensions.

## References

- `references/consistency-audit.md`  12-point cross-section consistency checker
- `references/lender-criteria-uganda.md`  Formal credit criteria mapped to Uganda bank standards (created when Doing Business Uganda PDF extraction is complete)
- `10-financial-projections/references/uganda-tax-framework.md`  Tax rates for financial projection verification
- `11-funding-request/references/credit-assessment-frameworks.md`  5 Cs and CAMPARI detail
- `meta-sustainability/SKILL.md`  Sustainability Readiness Score (SRS); for DFI/impact investor plans, run Mode C audit and confirm SRS  1.6/2.0 before CAMPARI scoring; social licence to operate (community opposition risk) is a CAMPARI Character factor; environmental non-compliance is a CAMPARI Conditions factor

---
name: meta-bankability-scoring
description: Analytical meta-skill that scores a complete business plan against 12 investor-readiness dimensions derived from Rogoff's bankability framework. Produces a weighted scorecard, identifies weaknesses, and recommends improvements to increase funding probability.
---

# Bankability Scoring Meta-Skill

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
| 8 | **Traction & validation** | 8% | Evidence of market demand (customers, revenue, LOIs) |
| 9 | **Scalability** | 6% | Can the business grow 10x without breaking? |
| 10 | **Risk awareness** | 4% | Honest risk assessment with mitigation plans |
| 11 | **Clarity of ask** | 4% | Specific funding need with clear use of funds |
| 12 | **AI & operational efficiency** | 4% | Smart use of technology and automation |

### Scoring Scale

- **9-10:** Exceptional — investor-ready, compelling
- **7-8:** Strong — minor improvements needed
- **5-6:** Adequate — notable gaps to address
- **3-4:** Weak — significant revision required
- **1-2:** Critical — fundamental issues present

### Overall Bankability Rating

**Weighted score calculation:** Sum of (dimension score x weight)

| Overall Score | Rating | Recommendation |
|---|---|---|
| 8.0-10.0 | **Investment Ready** | Submit to investors with confidence |
| 6.5-7.9 | **Nearly Ready** | Address flagged weaknesses, then submit |
| 5.0-6.4 | **Needs Work** | Significant revision required before submission |
| Below 5.0 | **Not Ready** | Fundamental rethinking needed |

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
1. [Dimension] — [Why it scores well]
2. [Dimension] — [Why it scores well]

Critical Weaknesses:
1. [Dimension] — [Score] — [What to fix]
2. [Dimension] — [Score] — [What to fix]

Priority Actions (ranked by impact on overall score):
1. [Action] → Expected score improvement: +X.X
2. [Action] → Expected score improvement: +X.X
3. [Action] → Expected score improvement: +X.X
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

- Scoring is evidence-based — every score cites specific plan content
- Feedback is constructive and actionable, not just criticism
- Recommendations are prioritised by impact on overall score
- Scoring is calibrated — a 7 means the same thing across dimensions

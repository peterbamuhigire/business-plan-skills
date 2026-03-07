---
name: meta-market-validation
description: Analytical meta-skill that validates market claims, TAM/SAM/SOM calculations, competitive positioning, and customer assumptions against available data. Flags unsupported assertions, identifies data gaps, and suggests validation methods.
---

# Market Validation Meta-Skill

Audit the market-facing sections of the business plan (sections 04, 05, 06, 07) to ensure claims are defensible and data-backed.

## When to Use

Invoke AFTER sections 04-07 are complete. This skill reviews market claims and flags issues before investors do.

## What to Validate

### 1. Market Size Validation

- Is TAM calculated using credible methodology?
- Is SAM a logical subset of TAM with clear narrowing criteria?
- Is SOM realistic (typically 1-5% of SAM for startups, not 20%)?
- Are market size sources cited and current (within 2 years)?
- Does bottom-up calculation align with top-down?

### 2. Growth Rate Validation

- Are growth projections supported by historical data?
- Is the cited CAGR from a reputable source?
- Are growth assumptions internally consistent with the business model?
- Is the business growing faster than the market? If so, why?

### 3. Customer Assumption Validation

- Are customer personas based on research or assumptions?
- Is the CAC estimate grounded in comparable data?
- Is the CLV calculation realistic given churn assumptions?
- Is the CLV:CAC ratio defensible (>3:1)?

### 4. Competitive Positioning Validation

- Are all relevant competitors identified (direct, indirect, substitutes)?
- Are competitive advantages genuinely sustainable?
- Are competitor weaknesses based on evidence, not wishful thinking?
- Is the differentiation claim verifiable?

### 5. Pricing Validation

- Is pricing consistent with the value proposition?
- How does pricing compare to competitors?
- Is there evidence of willingness to pay at this price point?
- Does the pricing model support the revenue projections?

## Validation Output Format

For each claim reviewed:

```
Claim: [The specific assertion]
Source: [Where it appears in the plan]
Evidence: [Supporting data found]
Status: VALIDATED / NEEDS EVIDENCE / UNSUPPORTED / CONTRADICTED
Action: [What to do — cite source, conduct research, revise claim]
```

### Validation Summary Dashboard

| Area | Claims Reviewed | Validated | Needs Evidence | Unsupported | Critical Issues |
|---|---|---|---|---|---|
| Market size | X | X | X | X | [List] |
| Growth rates | X | X | X | X | [List] |
| Customer data | X | X | X | X | [List] |
| Competition | X | X | X | X | [List] |
| Pricing | X | X | X | X | [List] |

## Generation Process

1. Review sections 04-07 and extract all factual claims
2. Categorise each claim (market size, growth, customer, competitive, pricing)
3. Assess evidence for each claim
4. Flag unsupported or contradicted claims
5. Suggest validation methods for gaps (surveys, interviews, pilot tests)
6. Produce validation summary dashboard

## Quality Criteria

- Every factual claim is assessed, not just the obvious ones
- Validation is objective — does not rubber-stamp weak claims
- Suggested validation methods are practical and affordable
- Critical issues are highlighted with urgency

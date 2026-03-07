---
name: meta-financial-stress-test
description: Analytical meta-skill that stress-tests financial projections through sensitivity analysis, scenario modelling (base/optimistic/pessimistic), break-even stress testing, and Monte Carlo simulation logic. Ensures the financial plan survives adversity and investor scrutiny.
---

# Financial Stress Test Meta-Skill

Validate and stress-test the financial projections from section 10 to prove the business model is resilient.

## When to Use

Invoke AFTER section 10 (Financial Projections) is complete. This skill takes the projections as input and produces stress-tested outputs.

## What to Generate

### 1. Three-Scenario Model

**Base case** — Most likely outcome using moderate assumptions
**Optimistic case** — Best realistic outcome (not fantasy)
**Pessimistic case** — Worst realistic outcome (not apocalypse)

For each scenario, adjust:
- Revenue growth rate (+/- 20-30%)
- Customer acquisition cost (+/- 25%)
- Churn rate (+/- 50%)
- Operating costs (+/- 15%)
- Time to break-even (+/- 3-6 months)

### 2. Sensitivity Analysis

Test each key variable independently:

| Variable | -20% | -10% | Base | +10% | +20% | Impact Level |
|---|---|---|---|---|---|---|
| Unit price | | | $X | | | High/Med/Low |
| Volume | | | X | | | |
| COGS | | | $X | | | |
| CAC | | | $X | | | |
| Churn | | | X% | | | |

Identify which variables have the highest impact on profitability.

### 3. Break-Even Stress Test

- Base case break-even date
- How much revenue decline before break-even is unreachable?
- What is the maximum sustainable burn rate?
- How many months of runway remain in pessimistic case?

### 4. Cash Flow Stress Test

- Can the business survive 2 months of zero revenue?
- What happens if a major customer defaults?
- Impact of 60-day vs. 30-day payment terms
- Minimum cash reserve required

### 5. Key Risk Indicators

Define early warning triggers:

```
IF monthly revenue < $X for 2 consecutive months → [Action]
IF CAC exceeds $X → [Action]
IF cash reserves drop below $X → [Action]
IF churn exceeds X% → [Action]
```

## Generation Process

1. Take financial projections from section 10 as input
2. Build three-scenario model by adjusting key assumptions
3. Run sensitivity analysis on 5-7 key variables
4. Stress-test break-even under adverse conditions
5. Stress-test cash flow under shock scenarios
6. Define early warning triggers and response actions
7. Summarise findings and flag critical vulnerabilities

## Output Format

Produce a stress test report with:
- Executive summary of resilience assessment
- Three-scenario comparison table
- Sensitivity analysis matrix
- Cash flow stress test results
- Risk trigger dashboard
- Recommendations for strengthening financial resilience

## Quality Criteria

- Scenarios are realistic, not extreme (pessimistic ≠ catastrophic)
- Sensitivity analysis identifies the 2-3 variables that matter most
- Cash flow stress tests include realistic shock scenarios
- Early warning triggers are specific and actionable
- Recommendations are practical, not just "reduce costs"

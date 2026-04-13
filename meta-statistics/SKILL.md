---
name: meta-statistics
description: Apply statistical rigour to business-plan numbers, forecasts, charts, survey results, market sizing, and comparative analysis.
---

# Meta Statistics

## Overview

Use this meta-skill to apply statistical discipline to business-plan evidence. It helps choose the right method, summary, chart, or inference so numbers support decision-making rather than decorative credibility.

## Use When

- Use when market sizing, survey results, forecasts, or comparative metrics need statistical rigour.
- Use when a chart, rate, trend, or average could be misleading if calculated badly.
- Use when the plan needs defensible quantitative presentation.

## Do Not Use When

- Do not use to create false precision from weak data.
- Do not apply advanced methods when the data does not support them.
- Do not use statistics to decorate claims that remain strategically weak.

## Required Inputs

- The dataset, figures, or claim being analysed
- The decision or message the numbers need to support
- Data quality, sample size, and sourcing context
- Any adjacent sections that rely on the same metrics

## Workflow

1. Identify what decision or claim the numbers must support.
2. Check whether the data quality and structure fit the intended method.
3. Apply the simplest sound statistical treatment that answers the question.
4. Present the result using the right summary or chart.
5. Reconcile the statistic with the surrounding commercial narrative.
6. Flag weak data, weak sampling, or over-interpretation risks.

## Quality Bar

- The chosen method fits the data and question.
- Results are interpretable by the intended audience.
- Charts and metrics clarify rather than distort.
- Any uncertainty or estimate basis is explicit.

## Anti-Patterns

- Using averages where distributions matter more.
- Plotting charts that make the wrong comparison easy.
- Presenting regression or inference without adequate data.
- Treating estimated data as measured fact.

## Outputs

- Statistically sound summaries, methods, or visualisation guidance
- Corrected metrics or interpretation notes
- Any data-quality caveats affecting confidence


## Overview

This skill transforms raw numbers into credible, decision-quality evidence. Every figure in a business plan must be:
1. **Correctly computed**  right method for the data type
2. **Properly presented**  chart/table chosen for the message, not decoration
3. **Verifiably sourced**  primary source cited, or flagged as estimate with basis

Source books: Anderson et al. *Essentials of Statistics for Business and Economics* (7th ed., Cengage 2013); Keller *Statistics for Management and Economics* (9th abbrev. ed., Cengage 2011).

---

## Section-by-Section Application Guide

| Plan Section | Primary Statistic | Method | Reference |
|---|---|---|---|
| 04 Market Analysis | TAM/SAM/SOM sizing | Frequency tables + totals from sourced data | See `statistics-for-business-plans.md Market Sizing` |
| 04 Market Analysis | Market growth trend | **Geometric mean** (not arithmetic) | `Growth Rates` |
| 05 Target Market | Customer segment profiles | Descriptive stats + bar/stacked bar charts | `Descriptive Stats` |
| 06 Competitive Analysis | Competitor positioning | Scatter diagram (2 axes: price  quality) | `Chart Selection` |
| 07 Marketing/Sales | Customer survey results | Confidence intervals + sample design | `Sampling & CIs` |
| 10 Financial Projections | Revenue forecasting | Regression (if 3+ years historical data exist) | `Regression` |
| 10 Financial Projections | Risk comparison across markets | **Coefficient of variation** | `Variability` |
| 10 Financial Projections | Multi-year growth rate | **Geometric mean** (CAGR) | `Growth Rates` |

---

## 1. Growth Rates  Always Use Geometric Mean

**Rule:** Any multi-period growth rate (revenue CAGR, population growth, market expansion) must use the geometric mean  never the arithmetic mean.

**Why it matters:** Arithmetic mean of annual returns *overstates* true compounded growth.
- Year 1: +100%, Year 2: 50%  Arithmetic mean = +25% (misleading: you broke even)
- Geometric mean = 0% (correct: $100  $200  $100)

**Formula:**
```
CAGR = (End Value / Start Value)^(1/n)  1
Geometric Mean = n(x1  x2  ...  xn)
```

**When to cite:** "Revenue grew at a CAGR of 18.4% over 5 years (geometric mean of annual growth rates, 20192024)."

---

## 2. Variability and Risk Comparison

Use **standard deviation** to describe spread within one variable. Use **coefficient of variation (CV)** to compare variability across variables with different scales or units.

**CV formula:** `CV = (s  x)  100%`

**Business plan application:**
- Compare revenue stability of two product lines: Line A (mean UGX 45M/month, CV = 8%) is more predictable than Line B (mean UGX 120M/month, CV = 31%)
- Compare supply-chain risk across sourcing geographies
- Compare customer cohort reliability (repeat purchase rate CV)

**When to cite:** "Supply from Supplier X shows a coefficient of variation of 12% vs. Supplier Y at 34%, indicating greater supply reliability from X (Anderson et al., 2013)."

---

## 3. Chart and Table Selection

Read `references/statistics-for-business-plans.md Chart Selection` for the full decision table. Summary:

| Message / Data Type | Chart |
|---|---|
| Market share or fund allocation | Pie chart (max 5 slices) or bar chart |
| Revenue trend over time | Line chart |
| Revenue mix by period | Stacked bar chart |
| Competitor comparison (2 attributes) | Scatter diagram |
| Distribution of customers by revenue size | Histogram |
| Multiple KPIs on one screen | Dashboard (bar + line + KPI card) |

**Hard rules from Anderson et al. (2013):**
- Never use 3D charts  adds visual noise, distorts magnitudes
- Axis must start at zero when comparing absolute values
- Label axes with units (UGX millions, % market share)
- Maximum 56 pie slices; use "Other" for remainder
- Use direct labels (percentages on slices)  not a separate legend

---

## 4. Data Visualisation Best Practices (Section 2.5, Anderson et al.)

1. Give the chart a clear, concise title that states the conclusion or key fact
2. Keep displays simple  remove all decoration that carries no information
3. Label every axis with the variable name and unit of measure
4. Use colours that are clearly distinguishable (not red/orange/brown together)
5. Scale axis from zero unless explicitly noting a truncated axis
6. For dashboards: group related charts, use borders, minimise scrolling
7. Strategic vs. tactical layers: operational dashboard (granular, real-time); executive dashboard (aggregate KPIs)

---

## 5. Sampling Design for Primary Research

When the plan includes a primary customer survey or field research, document the sampling method.

| Population Type | Method | Minimum Sample |
|---|---|---|
| Homogeneous (single industry/area) | Simple random sampling | n  30 |
| Heterogeneous (multiple segments) | Stratified random sampling | n  30 per stratum |
| Geographically dispersed, cost-sensitive | Cluster sampling | Varies; see `Sampling` |

**Sample size for confidence interval:**
`n = (z2 2) / E2`  where E = desired margin of error, z = 1.96 for 95% CI

---

## 6. Confidence Intervals for Market Research Claims

When the plan cites a survey finding ("70% of customers prefer X"), always attach a confidence interval.

**Formula (proportion):** `p  1.96  [p(1p)/n]`

**Example (n=150, 70% preference):**
`CI = 0.70  1.96  (0.700.30/150) = 0.70  0.073 = [62.7%, 77.3%]`

**Write-up:** "70% of surveyed customers (n=150) reported preference for X [95% CI: 6377%] (primary survey, March 2026)."

---

## 7. Regression for Forecasting

Use simple or multiple linear regression when 3+ years of historical data exist.

**Decision rules:**
- One driver (e.g., population  sales): simple regression `y = b0 + b1x`
- Multiple drivers (population + income + competition): multiple regression
- Use **adjusted R2** (not R2) to decide whether additional variables improve the model
- Only predict within the observed range of x (no extrapolation beyond data)

**Reporting standard:** "A simple linear regression of monthly revenue on customer base (R2 = 0.87, p < 0.001, n=36 months) projects revenue of UGX 82M at a customer base of 2,400."

See `references/statistics-for-business-plans.md Regression` for worked examples.

---

## 8. Verifiability Standards

Every statistic in the plan must pass this three-question test:

| Question | Standard |
|---|---|
| **SourceSection ** | Named source (UBOS, World Bank, primary survey) with date |
| **MethodSection ** | State if geometric mean, CV, regression, or raw secondary data |
| **ReproducibleSection ** | A reader with the same data could arrive at the same figure |

**Flagging estimates:**
- Sourced fact: "(UBOS, 2024)"
- Derived calculation: "(calculated from UBOS 2024 data; geometric mean 20192024)"
- Acknowledged estimate: "(author estimate based on industry benchmarks; see assumptions)"

**Never acceptable:** Unsourced percentages, rounded numbers without basis, growth rates without stating the method.

---

## References

- `references/statistics-for-business-plans.md`  Full decision tables, formulas, worked Uganda/EA examples, chart selection guide, data type definitions
- Anderson, D.R., Sweeney, D.J., Williams, T.A., Camm, J.D. & Cochran, J.J. (2013). *Essentials of Statistics for Business and Economics* (7th ed.). Cengage Learning.
- Keller, G. (2011). *Statistics for Management and Economics, Abbreviated* (9th ed.). Cengage Learning.

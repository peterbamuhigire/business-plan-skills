Parent: [Meta Statistics](../SKILL.md)

When to read: when market sizing, forecasts, surveys, projections, dashboards, KPIs, AI analytics, or management information systems carry weight in a plan. Also used by market analysis, financial projections, demand forecasting, and monitoring and evaluation.

# Analytics Ladder and KPI Standard

This standard paraphrases planning practice drawn from: *Mathematical Foundations of Big Data Analytics*; *AI-Based Data Analytics: Applications for Business Management*; *The Data Analytics Advantage*; *Data Analytics using Python*; and *Introduction to Data Analytics* (author and publisher details were not recorded at ingestion; confirm before citing).

## 1. Classify every analytic claim

| Type | Plan use | Evidence standard |
|---|---|---|
| Descriptive | Market size, historical sales, customer counts, costs, KPI baselines | Sourced data, clear definitions, clean tables |
| Diagnostic | Reasons for variance, market gaps, bottlenecks, churn | Segmentation, driver analysis, comparisons |
| Predictive | Demand, revenue, cash flow, stock-outs, churn, repayment risk | Historical depth, stated assumptions, back-testing where possible |
| Prescriptive | Scenario choice, pricing, stock levels, staffing, expansion timing | Constraints, sensitivity analysis, trade-offs |

Do not make predictive claims from descriptive data alone. Label estimates and show their basis.

## 2. Data-quality gate

Before a figure enters the plan:

1. Confirm source, date, geography, period, and unit.
2. Check completeness, validity, consistency, timeliness, and relevance.
3. Build a data dictionary for any primary dataset.
4. Keep a record of assumptions and transformations.
5. Flag missing, outdated, or weak data rather than hiding it.

## 3. Market analysis methods

- Prefer bottom-up sizing; triangulate top-down, bottom-up, and expert or benchmark logic.
- Use the compound annual growth rate (geometric mean) for multi-year growth.
- Report confidence intervals for primary survey results.
- Show uncertainty explicitly when market data is thin.
- Apply to TAM/SAM/SOM, segment sizing, growth rates, trend charts, competitor benchmarking, and demand drivers and constraints.

## 4. Financial-projection methods

- Driver-based revenue assumptions.
- Sensitivity and scenario analysis.
- Regression or time-series forecasting where history exists.
- Variance and coefficient-of-variation checks for unstable revenue or cost lines.
- Working-capital analytics: receivables, payables, inventory, cash conversion.
- Dashboard measures: runway, DSCR, gross margin, CAC, LTV, stock-out risk, budget-against-actual variance.

Always distinguish a forecast (expected outcome), a target (desired outcome), and a plan (committed actions).

## 5. Demand and operations analytics

Sales rate by branch, channel, SKU, segment, or period; stock-out and overstock risk; lead-time and reorder-point calculation; capacity utilisation; defect, scrap, rework, and yield; delivery performance and cycle time.

Every forecast states its horizon, method, history used, exclusions, and an error measure where back-testing is possible.

## 6. AI analytics in management

Propose AI analytics only for a clear management use: predictive maintenance, customer segmentation, churn risk, credit or receivables risk, anomaly detection, sentiment analysis, demand forecasting, or automated narrative reporting.

Required controls: explainability; human oversight; privacy and authorisation; model monitoring; data-quality checks; no unsupported causal claims.

## 7. KPI definition standard

Every KPI in a plan defines eight fields:

| Field | Content |
|---|---|
| Formula | Exact calculation |
| Source | System or record |
| Owner | Named role |
| Frequency | Reporting interval |
| Baseline | Current value and date |
| Target | Value and date |
| Threshold | Level that triggers attention |
| Action | What happens when the threshold is crossed |

A dashboard must support a decision, not only display numbers.

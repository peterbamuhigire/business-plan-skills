---
# Statistics for Business Plans — Reference Guide
# Sources: Anderson et al. (2013); Keller (2011)
---

## Table of Contents
1. [Data Types](#1-data-types)
2. [Chart Selection Decision Table](#2-chart-selection-decision-table)
3. [Descriptive Statistics — Key Measures](#3-descriptive-statistics--key-measures)
4. [Growth Rates — Geometric Mean](#4-growth-rates--geometric-mean)
5. [Variability and Risk — CV](#5-variability-and-risk--cv)
6. [Market Sizing — TAM/SAM/SOM](#6-market-sizing--tamsamsom)
7. [Sampling Design](#7-sampling-design)
8. [Confidence Intervals](#8-confidence-intervals)
9. [Regression Forecasting](#9-regression-forecasting)
10. [Data Dashboards](#10-data-dashboards)
11. [Verifiability Checklist](#11-verifiability-checklist)

---

## 1. Data Types

| Type | Definition | Business Plan Use |
|---|---|---|
| **Categorical (nominal)** | Labels; no order (e.g., industry sector, gender) | Market segment counts, business classification |
| **Categorical (ordinal)** | Labels with order (e.g., credit rating AAA→D, satisfaction 1–5) | Competitor ranking, customer satisfaction tier |
| **Quantitative (interval)** | Numeric; differences meaningful; no true zero (e.g., temperature, NPS) | Survey scale scores |
| **Quantitative (ratio)** | Numeric; true zero; ratios meaningful (e.g., revenue, units, population) | All financial projections, market size, headcount |
| **Cross-sectional** | One point in time across multiple entities | Market share survey, competitor pricing snapshot |
| **Time series** | One entity across multiple time periods | Revenue trend, inflation, population growth |

**Rule:** Identify data type before choosing analysis. Arithmetic operations (mean, regression) are only valid on quantitative ratio/interval data. Categorical data → frequency tables, bar charts, chi-square tests.

---

## 2. Chart Selection Decision Table

| Purpose | Data Requirement | Chart | Key Rules |
|---|---|---|---|
| Market share / fund allocation | Categorical proportions | Pie chart | Max 5 slices; label values directly; use 2D only |
| Segment comparison | Categorical counts | Bar chart (vertical or horizontal) | Start axis at zero; sort bars by value |
| Revenue mix over time | Categorical × time | Stacked bar chart | One period per bar; each segment a product/channel |
| Planned vs. actual by group | Categorical × 2 quantitative | Side-by-side bar chart | Group bars by period; colour-code categories |
| Revenue or price trend | Quantitative × time | Line chart | Mark data points; label key events |
| Distribution of customers | Quantitative, grouped | Histogram | Equal-width bins; label x-axis with ranges |
| Two-variable relationship | 2 quantitative variables | Scatter diagram | Add trendline + R² annotation |
| Competitor positioning | 2 attribute dimensions | Scatter diagram | Label each dot (competitor name) |
| Small exact dataset | Quantitative, n < 25 | Dot plot | Shows all values; avoids bin distortion |
| Multi-KPI monitoring | Mixed | Dashboard (charts + cards) | One screen; borders between panels; see §10 |

**Never use:**
- 3D pie or bar charts — distort angle/height perception (Anderson et al., 2013, §2.5)
- Dual y-axis charts without explicit labelling of both axes
- Pie charts with > 6 slices
- Radar/spider charts in formal plans — hard to read accurately

---

## 3. Descriptive Statistics — Key Measures

### Location

| Measure | Formula | When to Use | Warning |
|---|---|---|---|
| **Mean** | Σx / n | Normal distributions; symmetric data | Distorted by outliers |
| **Median** | Middle value (50th pct.) | Skewed data (income, property prices) | Preferred when reporting "typical" customer |
| **Mode** | Most frequent value | Discrete data; most common order size | May be non-unique |
| **Geometric mean** | ⁿ√(x₁ × x₂ × ... × xₙ) | Multi-period growth rates (CAGR) | See §4 for full treatment |

### Spread

| Measure | Formula | When to Use |
|---|---|---|
| **Range** | Max − Min | Quick sense of spread only; unreliable for decisions |
| **IQR** | Q₃ − Q₁ | Middle 50% spread; robust to outliers |
| **Standard deviation** | √[Σ(xᵢ−x̄)² / (n−1)] | Spread in same units as variable; widely understood |
| **Variance** | s² = Σ(xᵢ−x̄)² / (n−1) | Input to other calculations (regression, ANOVA) |
| **Coefficient of variation** | (s / x̄) × 100% | Compare variability across different scales/units — see §5 |

### Reporting standard

Always report: n (sample size), mean or median (state which), standard deviation or IQR, and the source of data.

---

## 4. Growth Rates — Geometric Mean

### Why arithmetic mean misleads

| Year | Return | Cumulative |
|---|---|---|
| 1 | +100% | $100 → $200 |
| 2 | −50% | $200 → $100 |
| Arithmetic mean | +25% | Implies $100 → $156 ❌ |
| **Geometric mean** | **0%** | **Correct: $100 → $100** ✓ |

### CAGR formula
```
CAGR = (Ending Value / Beginning Value)^(1/n) − 1
```

### Geometric mean from annual rates
```
xg = ⁿ√[(1+r₁)(1+r₂)...(1+rₙ)] − 1
```

### Uganda/EA example
GDP growth rates (5-year series): 5.1%, 6.3%, 4.8%, 7.2%, 5.9%
- Arithmetic mean: 5.86% (overstates compounding)
- Geometric mean: `⁵√(1.051 × 1.063 × 1.048 × 1.072 × 1.059) − 1 = 5.84%` (correct)
- Difference is small here but grows significantly with volatility

### Citation template
"The Uganda telecom sector grew at a CAGR of 14.2% from 2019 to 2024 (geometric mean of annual revenue growth rates; UCC Annual Reports 2019–2024)."

---

## 5. Variability and Risk — CV

### Coefficient of Variation

**Formula:** `CV = (s / x̄) × 100%`

**Interpretation:** CV expresses standard deviation as a percentage of the mean — enabling fair comparison across variables with different units or scales.

### Worked example: Supplier risk comparison

| Supplier | Mean lead time | Std dev | CV | Assessment |
|---|---|---|---|---|
| Supplier A (Kampala) | 7 days | 0.8 days | **11.4%** | Low variability — predictable ✓ |
| Supplier B (Dubai) | 7 days | 3.1 days | **44.3%** | High variability — unreliable ✗ |
| Supplier C (Nairobi) | 14 days | 1.2 days | **8.6%** | Slowest but most consistent |

*Means are equal for A and B — CV reveals the true risk difference.*

### Worked example: Product line revenue stability

| Product | Mean monthly revenue | CV | Risk level |
|---|---|---|---|
| Product X | UGX 85M | 9% | Low (predictable base) |
| Product Y | UGX 210M | 37% | High (seasonal or volatile) |

### Citation template
"Product X revenue shows a coefficient of variation of 9% vs. Product Y at 37%, indicating greater revenue predictability from Product X (calculated from 24 months of internal sales data, Jan 2024 – Dec 2025)."

---

## 6. Market Sizing — TAM/SAM/SOM

### Data types by level

| Level | Definition | Preferred Source |
|---|---|---|
| TAM | Total Addressable Market — entire demand if all customers served | World Bank, national statistics bureau, industry association reports |
| SAM | Serviceable Addressable Market — segment reachable with current model | National/regional survey, census data + segmentation |
| SOM | Serviceable Obtainable Market — realistic share in 3–5 years | Competitive analysis + company capacity + adoption curve |

### Statistical method

1. Use **frequency distributions** and **cross-tabulations** from sourced survey/census data
2. Apply segmentation filters (geographic, demographic, behavioural) to narrow TAM → SAM
3. Apply realistic market share estimate (SOM/SAM) — justify with competitor share data or analogous market entry benchmarks

### Common errors to avoid

- Calculating SOM as a fixed % of TAM without justification ("even 1% of the market...")
- Using non-comparable data sources (mixing global and local figures)
- Forgetting to source: always cite survey date, methodology, and sample

---

## 7. Sampling Design

### Method selection

| Scenario | Method | Rationale |
|---|---|---|
| Survey of uniform population (e.g., all maize farmers in Lira district) | Simple random sampling | Equal probability; unbiased if population homogeneous |
| Survey across multiple segments (SMEs by industry sector) | Stratified random sampling | Ensures representation from all strata; more efficient |
| Field research in dispersed locations (county-by-county) | Cluster sampling | Cost savings: survey all in selected clusters |

### Sample size formula
```
n = (z_{α/2})² × σ² / E²
```
- E = desired margin of error (e.g., ±5 percentage points = 0.05)
- z = 1.96 for 95% confidence, 2.576 for 99%
- σ = estimated standard deviation (use 0.5 for proportions when unknown)

**Practical minimums:**
- n ≥ 30 for any inferential statistics (Central Limit Theorem)
- n ≥ 30 per stratum for stratified sampling
- n ≥ 50 if population heavily skewed

### Documentation standard
State in the plan: sampling method used, sample size, response rate, survey date, and geographic/demographic scope. Example:
"Primary survey: 187 urban consumers in Kampala and Wakiso districts, stratified by income quintile (3 strata), conducted Feb–Mar 2026. Response rate: 78%."

---

## 8. Confidence Intervals

### Mean (σ known or n ≥ 30)
```
CI = x̄ ± z_{α/2} × (s / √n)
```

### Proportion
```
CI = p̂ ± z_{α/2} × √[p̂(1−p̂) / n]
```

### Reference values
| Confidence level | z value | Interpretation |
|---|---|---|
| 90% | 1.645 | 90 in 100 such intervals contain true value |
| **95%** | **1.960** | **Standard for business research** |
| 99% | 2.576 | Used for high-stakes decisions |

### Worked example (East Africa consumer survey)
- Sample: n = 200 SMEs; 62% report cash flow as top challenge (p̂ = 0.62)
- 95% CI: `0.62 ± 1.96 × √(0.62 × 0.38 / 200) = 0.62 ± 0.067 = [55.3%, 68.7%]`
- Write-up: "62% of surveyed SMEs cite cash flow as their primary challenge [95% CI: 55–69%; n=200; primary survey, Feb 2026]."

### Margin of error trade-off
- Doubling precision (halving E) requires **4× the sample size**
- Higher confidence (95% → 99%) widens the interval
- Choose level based on decision risk (95% standard; 99% for regulatory/funder submissions)

---

## 9. Regression Forecasting

### When to use

| Data situation | Method |
|---|---|
| ≥ 3 years monthly/annual history, one driver | Simple linear regression |
| ≥ 3 years history, multiple drivers | Multiple linear regression |
| < 3 years data or no historical series | Use industry benchmarks + growth rate assumptions (document clearly) |
| Seasonal pattern visible | Add seasonality index or use time series decomposition |

### Simple regression — worked example
Data: 36 months of revenue (UGX M) vs. active customer base

Estimated equation: `ŷ = 12.4 + 0.034×(customers)`
- Interpretation: Each additional customer adds UGX 34,000 monthly revenue
- R² = 0.89: 89% of revenue variance explained by customer base
- p < 0.001: relationship highly significant

Forecast: At 2,500 customers → `ŷ = 12.4 + 0.034 × 2,500 = UGX 97.4M/month`

### Multiple regression — variable selection rules

1. **Include** only variables with theoretical justification (why would it drive revenue?)
2. **Use adjusted R²** — not R² — to evaluate whether adding a variable improves the model
3. **Check for multicollinearity**: if two x-variables correlate r > 0.8, remove one
4. **Test significance** of each coefficient (p < 0.05); remove non-significant variables
5. **Never extrapolate** beyond the observed range of x-data

### Reporting standard
"Simple linear regression of monthly revenue on active customer count (n=36 months) yields R² = 0.89 (adjusted R² = 0.88), slope coefficient = 34,000 UGX/customer (p < 0.001, 95% CI: 29,000–39,000). At projected 2,500 customers, forecast revenue = UGX 97.4M/month."

### Common errors

| Error | Correct approach |
|---|---|
| Reporting R² without adjusted R² in multiple regression | Always report both; use adj R² for model comparison |
| Predicting beyond data range | Flag extrapolation explicitly; widen uncertainty band |
| Ignoring residual patterns | Plot residuals vs. fitted values to check model validity |
| Including correlated predictors | Check correlation matrix; remove redundant variables |

---

## 10. Data Dashboards

A dashboard is a single-screen collection of charts and KPIs enabling fast decision-making.

### Two-tier structure

**Tactical dashboard (operations team):**
- Item-level sales analysis
- Geographic breakdown (location/region)
- Queue times, inventory levels, conversion rates
- Updated daily or in real-time

**Strategic dashboard (executive/investor):**
- Aggregate revenue, margin, DSCR
- Customer acquisition, retention, churn
- Capacity utilisation, headcount
- Updated weekly or monthly

### Design rules (Anderson et al., 2013, §2.5)

1. Fit all critical KPIs on one screen — minimise scrolling
2. Use borders between chart panels for readability
3. Apply consistent colour palette (3–4 colours maximum)
4. Every chart has a title stating the key fact (not just "Revenue")
5. No 3D effects; no decorative gradients
6. Use KPI cards (single number + trend arrow) for headline metrics

---

## 11. Verifiability Checklist

Before finalising any section, run each statistic through this checklist:

| Check | Standard | Status |
|---|---|---|
| Source named | Organisation + publication + year (e.g., "UBOS, 2024 Statistical Abstract") | ☐ |
| Date of data | Year or quarter stated | ☐ |
| Sample scope | Country/region/demographic covered | ☐ |
| Method stated | Geometric mean / regression / survey / administrative data | ☐ |
| Margin of error | If from survey, CI or sample size stated | ☐ |
| Estimate flagged | "Author estimate" or "industry benchmark" noted if not from primary source | ☐ |
| Reproducible | A competent analyst with same source data would arrive at the same figure | ☐ |

### Citation formats (business plan style)

**Secondary sourced fact:**
"Uganda's urban population reached 26.8% of total in 2024 (UBOS, *National Population and Housing Census 2024*)."

**Derived calculation:**
"Retail sector grew at a CAGR of 11.3% from 2019 to 2024 (geometric mean of annual growth rates; URA Domestic Tax Revenue Reports 2019–2024)."

**Primary survey:**
"68% of target customers indicated willingness to pay UGX 15,000–20,000 per unit [95% CI: 60–76%; primary survey, n=148, Kampala, Jan 2026]."

**Acknowledged estimate:**
"Estimated 4,200 active informal food vendors in Gulu municipality (author estimate based on KCCA market census methodology applied to district population; see Assumptions, Appendix A)."

---

*Sources: Anderson, Sweeney, Williams, Camm & Cochran (2013); Keller (2011)*

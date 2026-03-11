---
source: "The Little Book of Valuation: How to Value a Company, Pick a Stock and Profit"
author: "Damodaran, Aswath"
year: 2011
publisher: "John Wiley & Sons"
relevance: "Equity fundraising, investor negotiations, pre-revenue startup valuation, DFI/angel pitch preparation"
---

# Business Valuation Methods

*Based on Damodaran (2011), The Little Book of Valuation*

## Why Valuation Matters for SME Founders

Valuation is not only for listed companies. For any business seeking equity investment, the share of the firm that an angel investor, venture capitalist, or DFI demands in exchange for capital depends entirely on how much they estimate the firm to be worth. A founder who cannot articulate a defensible valuation will either give away too much equity or fail to close the round. Damodaran's central argument: valuation is simpler than it looks, rests on a few key drivers, and anyone willing to collect and analyse information can do it.

---

## 1. The Three Approaches to Valuation

### 1.1 Intrinsic Valuation (Discounted Cash Flow — DCF)

The intrinsic value of an asset is determined by the cash flows it is expected to generate over its life and how uncertain those cash flows are. Assets with high, stable cash flows are worth more than assets with low, volatile cash flows.

**When to use:** When you have forecasts for revenues and margins and want to understand what the business is fundamentally worth, independent of what comparable businesses trade for. Best suited for businesses with a clear path to profitability, even if not yet profitable. A long time horizon (3–5 years) is almost a prerequisite.

### 1.2 Relative Valuation (Multiples/Comparables)

Assets are valued by looking at how the market prices similar assets. A business is worth a multiple of its earnings, revenue, or book value — where the multiple is derived from comparable transactions or listed companies.

**When to use:** When there are sufficient comparable businesses available and you want a quick, market-grounded estimate. More likely to reflect current investor sentiment. Relative valuations have short shelf lives — a business that looks cheap today relative to comparables can look expensive six months later.

### 1.3 Option-Based Valuation (Real Options)

Treats the firm or specific assets (e.g. undeveloped reserves, a patent, a potential new market) as options that have value because of optionality — the right, but not the obligation, to invest in the future.

**When to use:** Narrow circumstances: natural resource companies with unexploited reserves; pharmaceutical or biotech firms with promising but unproven drugs; early-stage companies whose value is largely the option to enter a large market if conditions are right. Not recommended as a primary method for most SME valuations.

**Key principle:** Intrinsic and relative valuation will often yield different estimates. Neither is "right" — they answer different questions. Use both where possible. Invest in companies that are undervalued on *both* dimensions to improve odds.

---

## 2. DCF Valuation — The Core Framework

### 2.1 The Four Inputs

Every DCF valuation reduces to four inputs:

| Input | What It Measures |
|---|---|
| **Cash flows from existing assets** | Free cash flow generated after taxes and reinvestment needs |
| **Expected growth rate** | How fast cash flows will grow during the forecast period |
| **Discount rate (cost of capital)** | Risk-adjusted rate reflecting both equity and debt costs |
| **Terminal value** | Estimated value at the end of the forecast period |

### 2.2 Free Cash Flow to the Firm (FCFF)

FCFF is the cash left over after taxes and reinvestment, *before* debt service. It is the correct cash flow to use when valuing the entire business (enterprise value).

```
FCFF = After-tax operating income − (Net capital expenditure + Change in non-cash working capital)

Or equivalently:
FCFF = After-tax operating income × (1 − Reinvestment rate)
```

**Free Cash Flow to Equity (FCFE)** is the cash left *after* debt payments — use this when valuing only the equity portion:

```
FCFE = Net income + Depreciation − Capital expenditure − Change in working capital − (Principal repaid − New debt raised)
```

### 2.3 Estimating the Discount Rate (Cost of Capital / WACC)

```
WACC = Cost of equity × (E/V) + After-tax cost of debt × (D/V)

Where:
  E = market value of equity
  D = market value of debt
  V = E + D (total capital)
```

**Cost of equity (CAPM):**
```
Cost of equity = Risk-free rate + Beta × Equity risk premium (ERP)
```

- *Risk-free rate:* Use the long-term government bond rate (e.g. Uganda 10-year bond; approx. 16–18% in 2025 for UGX-denominated; or use US rate + country risk premium for USD-based projections)
- *Equity risk premium (ERP):* The premium investors demand for equities over the risk-free rate. US historical average ≈ 4–5%. For Sub-Saharan Africa, add a country risk premium (see Uganda/East Africa section below)
- *Beta:* Measure of a company's risk relative to the market. For private firms without market history, use an industry-average beta. Beta = 1 means average market risk. Beta > 1 means higher risk.

**After-tax cost of debt:**
```
After-tax cost of debt = (Risk-free rate + Default spread) × (1 − Tax rate)
```

Use the firm's borrowing rate as a proxy. For Uganda: bank lending rates typically 20–24% (2025), so after-tax cost of debt (at 30% corporate tax rate) ≈ 14–17%.

### 2.4 Growth Rate Estimation

Historical growth rates are a weak predictor of future growth. The most reliable approach is the *fundamental growth rate*:

```
Fundamental growth rate = Reinvestment rate × Return on capital (ROC)

Where:
  Reinvestment rate = Net capital expenditure + Change in working capital / After-tax operating income
  Return on capital = After-tax operating income / (Book value of debt + Book value of equity − Cash)
```

**For equity earnings (net income):**
```
Growth in net income = Retention ratio × Return on equity (ROE)
```

**Key insight:** Growth only creates value when the return on capital *exceeds* the cost of capital. Growth at below-cost-of-capital returns destroys value.

### 2.5 Terminal Value

Terminal value typically accounts for 70–90% of total DCF value — and can exceed 100% for early-stage firms with negative near-term cash flows. It must be calculated with care.

**Stable growth (perpetuity) model — the standard approach:**
```
Terminal value = Cash flow in year (n+1) / (Cost of capital − Stable growth rate)

Or:
TV = FCFF × (1 + g) / (WACC − g)
```

**Three constraints on the stable growth rate:**
1. The stable growth rate cannot exceed the long-run nominal growth rate of the economy. A rule of thumb: set it no higher than the risk-free rate used in the valuation
2. As the firm transitions to stable growth, adjust beta towards 1.0 and debt ratio towards industry norms
3. The reinvestment rate in stable growth must be consistent with the assumed growth rate:
   `Stable reinvestment rate = Stable growth rate / Return on capital in stable phase`

**Multiples approach to terminal value (alternative):** Apply an EV/EBITDA or EV/Revenue multiple based on comparable mature firms to the terminal-year financials. This is simpler and is often used as a cross-check.

---

## 3. Worked DCF Example (Simplified, Uganda SME Context)

**Business:** A Kampala-based food processing company with UGX 800M current revenue, targeting UGX 4B revenue in year 5.

| Year | Revenue (UGXm) | EBIT margin | EBIT (UGXm) | Tax (30%) | NOPAT | Reinvest (40%) | FCFF |
|---|---|---|---|---|---|---|---|
| 1 | 1,120 | 8% | 90 | 27 | 63 | 25 | 38 |
| 2 | 1,568 | 10% | 157 | 47 | 110 | 44 | 66 |
| 3 | 2,040 | 12% | 245 | 73 | 171 | 68 | 103 |
| 4 | 2,855 | 14% | 400 | 120 | 280 | 112 | 168 |
| 5 | 4,000 | 15% | 600 | 180 | 420 | 168 | 252 |

*Assumptions: Revenue growing ~40%/yr tapering, margins improving towards 15%, reinvestment rate 40%, WACC 22% (Uganda risk-adjusted)*

**Terminal value (Year 5):**
- Stable growth rate = 8% (Uganda nominal GDP growth forecast)
- Stable WACC = 18% (lower as firm matures and risk declines)
- Terminal year FCFF = 252 × 1.08 = 272
- TV = 272 / (0.18 − 0.08) = **UGX 2,720M**

**Enterprise value:**
```
PV of forecast FCFFs (discounted at 22%): UGX 415M
PV of terminal value (2,720 / 1.22^5): UGX 1,003M
Enterprise value: UGX 1,418M
Less: Debt (UGX 400M)
Equity value: UGX 1,018M
```

*This is an illustrative example. Real valuations require detailed assumption documentation.*

---

## 4. Relative Valuation — Multiples

### 4.1 The Key Multiples

| Multiple | Formula | What It Captures | Primary Driver |
|---|---|---|---|
| **P/E ratio** | Share price / Earnings per share | Equity value per unit of earnings | Growth rate, payout ratio, risk |
| **EV/EBITDA** | Enterprise value / EBITDA | Business value per unit of operating cash flow | Growth, reinvestment rate, risk, ROIC, tax rate |
| **EV/Revenue** | Enterprise value / Revenue | Business value per unit of revenue | Operating margin, growth, risk |
| **P/Book** | Share price / Book value of equity | Premium over accounting equity | Return on equity (ROE), growth, risk |
| **PEG ratio** | P/E / Expected growth rate | Growth-adjusted earnings multiple | Risk-adjusted growth quality |

**Consistency rule:** Always match numerator and denominator — equity numerator (P) requires equity denominator (EPS, net income); enterprise value numerator (EV) requires firm-level denominator (EBITDA, EBIT, Revenue, FCFF).

### 4.2 Comparable Company Analysis — Four Steps

1. **Find comparables:** Firms with similar cash flows, growth potential, and risk — not necessarily in the same sector. Sector peers are the starting point; prune further by size and geography
2. **Calculate standardised multiples:** Use the *median*, not the average (distributions are skewed; averages are distorted by outliers)
3. **Identify the companion variable:** The single variable that most determines each multiple (see table below). A company looks undervalued when it has a low multiple *and* a high companion variable
4. **Adjust for differences:** Use the PEG ratio or regression-based approaches to control for multiple differences simultaneously

**Valuation mismatch indicators (signals of potential undervaluation):**

| Multiple | Companion Variable | Undervalued Signal |
|---|---|---|
| P/E | Expected EPS growth | Low P/E + high expected growth |
| P/Book | Return on equity | Low P/Book + high ROE |
| P/Sales | Net margin | Low P/Sales + high net margin |
| EV/EBITDA | Reinvestment rate | Low EV/EBITDA + low reinvestment needs |
| EV/Capital | Return on capital | Low EV/Capital + high ROIC |
| EV/Sales | Operating margin | Low EV/Sales + high operating margin |

### 4.3 Important Cautions on Multiples

- Multiples change over time with market conditions, interest rates, and risk appetite. A P/E of 15 was cheap in 2008 and expensive in 2009
- More than half of all firms will have negative earnings in any given year — this silently removes loss-making comparables and biases averages upward
- Relative valuations embed assumptions that are implicit and hidden; intrinsic valuations make assumptions explicit and testable
- *"You make just as many assumptions when you do a relative valuation as you do in a discounted cash flow valuation. The difference is that the assumptions in relative valuation are implicit and unstated."* (Damodaran, 2011)

---

## 5. Pre-Revenue and Early-Stage Startup Valuation

### 5.1 The Challenge

Young firms share characteristics that make standard valuation extremely difficult:
- No or minimal operating history (one to two years of data at most)
- Small or negative revenues; operating losses; no earnings to use as a multiple base
- High survival risk: only 44% of businesses founded survive four years; only 31% survive seven years (Bureau of Labor Statistics data cited in Damodaran)
- Illiquid equity — even listed small-cap firms have thin float; private firms more so
- Multiple, complex equity claims (preference shares, convertibles, option pools)

### 5.2 Recommended Methods

**Method A: Survival-Adjusted DCF (Damodaran's preferred approach for intrinsic value)**

Step 1 — *Value as a going concern:* Build a full DCF assuming the business succeeds and matures. Three key value drivers for young firms:
- **Value Driver 1 — Revenue growth:** How large is the total addressable market? What market share can the firm realistically capture?
- **Value Driver 2 — Target margins:** What operating margins do mature firms in this sector achieve? Build a "pathway to profitability" showing how the firm converges to that margin
- **Value Driver 3 — Survival probability:** What is the likelihood the firm fails before reaching maturity?

Step 2 — *Adjust for survival risk:*
```
Survival-adjusted equity value = Going-concern equity value × Probability of survival
                                + Distress value × Probability of failure
```

*Example:* If going-concern value = UGX 500M, probability of survival = 67% (sector average for year 1–5 energy firms), and distress value = 0:
`Adjusted value = 500M × 0.67 = UGX 335M`

**Method B: Forward Multiples (Survival-Adjusted)**

Because current revenues are too small and earnings are negative, apply multiples to *forward* (year 3–5) revenues or earnings, then discount back:

```
Step 1: Project revenue in year 5 (e.g. UGX 3B based on market sizing)
Step 2: Apply mature-firm EV/Revenue multiple for the sector (e.g. 1.5×)
        → Enterprise value in year 5 = UGX 3B × 1.5 = UGX 4.5B
Step 3: Discount to present at cost of capital (e.g. 25% for five years)
        → PV of enterprise value = 4.5B / (1.25^5) = UGX 1.47B
Step 4: Apply survival discount (e.g. 33% failure probability)
        → Survival-adjusted EV = 1.47B × 0.67 = UGX 985M
Step 5: Subtract debt; divide by shares for per-share value
```

**Method C: VC / Angel Method (common in practice, less rigorous)**

Investors work backwards from a required return:
```
Post-money valuation = Exit value in year N / (1 + Required return)^N
Pre-money valuation = Post-money valuation − Investment amount
```

*Example:* Angel investor requires 10× return in 5 years; expects to exit at UGX 5B; investing UGX 200M:
```
Post-money = 5B / 10 = UGX 500M
Pre-money = 500M − 200M = UGX 300M
Investor's equity stake = 200M / 500M = 40%
```

This method is simple but heavily dependent on the assumed exit multiple and return target. Use it as a negotiation anchor, not as a fundamental valuation.

### 5.3 Key Person Discount

Service businesses (consultancies, professional firms) dependent on the founder for revenue warrant a *key person discount*: value the firm with and without the founder's continued involvement, and the difference is the discount to apply. Typical range: 15–35% depending on how replaceable the individual is.

---

## 6. Risk and Value — The Relationship

Risk affects value through the discount rate. Higher risk → higher discount rate → lower present value of the same cash flows. This is not an opinion but a mathematical certainty.

**Practical implications for SMEs seeking investment:**
- Every factor that *increases* perceived risk (weak management team, single-customer dependence, no IP protection, regulatory uncertainty, informal records, UGX currency exposure) reduces valuation
- Investors do not add a risk premium to the *numerator* (growth projections); they add it to the *denominator* (discount rate). A 25% discount rate applied to a 10-year cash flow stream reduces the present value by roughly 10× compared to a 5% rate
- Reducing risk — by professionalising governance, auditing financials, securing long-term offtake agreements, or filing trademarks — has a direct, measurable positive effect on valuation

**The risk-return principle:** Growth only creates value when return on invested capital (ROIC) exceeds the cost of capital. Growth at sub-cost-of-capital returns actually *destroys* value. A firm growing at 30% per year with a 12% ROIC and a 20% cost of capital is destroying shareholder value with every unit of growth.

---

## 7. Growth and Value — When Growth Helps and When It Hurts

Three conditions determine whether growth creates value:

1. **ROIC > WACC:** Growth creates value only when returns on new investment exceed the cost of financing that investment. If ROIC = WACC, growth has no effect on value. If ROIC < WACC, growth destroys value
2. **Sustainable competitive advantage:** Growth value lasts only as long as the firm can maintain excess returns. Firms with strong brands, patents, network effects, or proprietary processes sustain excess returns longer
3. **Reinvestment quality:** The reinvestment rate matters less than what that reinvestment earns. High reinvestment at low returns is value-destroying; moderate reinvestment at high returns is value-creating

**Key formula:**
```
Value of growth = PV of (ROIC − WACC) × Invested capital, over the excess-return period
```

**In terminal value calculations:** Increasing the stable growth rate only increases terminal value if the assumed return on capital *exceeds* the cost of capital in the stable phase. If ROIC = WACC (zero excess returns — the conservative assumption), growth rate changes have zero impact on terminal value.

---

## 8. Sector-Specific Valuation Notes

### 8.1 Financial Services Firms (Banks, MFIs, SACCOs)

Standard DCF cannot be applied to financial firms because:
- Debt is not a financing choice but a raw material (deposits are funding)
- FCFF is not meaningful — interest expense cannot be separated from operating expenses
- Capital adequacy ratios constrain dividends and reinvestment

**Correct approaches:**
1. *Dividend Discount Model (DDM):* Value equity directly by discounting dividends (or potential dividends) at the cost of equity
2. *FCFE model:* Reinvestment = increase in regulatory capital. FCFE = Net income − Increase in equity capital required to sustain growth
3. *Excess return model:* `Value of equity = Book equity + PV of (ROE − Cost of equity) × Book equity`

For MFIs and SACCOs, the excess return model is most transparent — it shows clearly whether the institution creates value above and beyond its book equity.

### 8.2 Commodity and Cyclical Companies (Agriculture, Mining)

Key issue: Current earnings (at the top or bottom of a commodity cycle) are not representative of mid-cycle profitability.

**Solution:** Use *normalised earnings* — the average earnings over a full commodity price cycle — as the base for valuation. Do not use peak-year earnings for a forward multiple; it will overvalue the business.

For cyclical agribusinesses (common in East Africa), value the business at:
- Trough scenario (stressed commodity price)
- Mid-cycle/normalised scenario
- Peak scenario
Weight by probability to arrive at expected value.

### 8.3 Real Estate

Value via DCF using net rental income discounted at a risk-adjusted rate (including illiquidity premium), or use price-per-square-metre comparables adjusted for location, condition, and lease terms.

### 8.4 Early-Stage / Pre-Revenue (Summary)

See Section 5. The survival-adjusted DCF is the most theoretically sound. The forward multiples method is easier to communicate to investors. The VC method is standard in angel and VC negotiations. Use all three as cross-checks.

---

## 9. Common Valuation Mistakes

| Mistake | Why It Matters |
|---|---|
| Using peak-year earnings as the base | Overstates sustainable value for cyclical businesses |
| Terminal value growth rate > economy growth rate | Mathematically impossible in the long run; inflates value |
| Not reinvesting to support assumed growth | Growth requires capital; ignoring reinvestment overstates free cash flow |
| Ignoring survival risk for pre-revenue firms | Going-concern DCF without survival adjustment overstates value by 30–50%+ for high-risk firms |
| Adding premiums *after* valuation (synergy, management quality) | These should already be in the cash flow and discount rate assumptions; double-counting inflates value |
| Using average multiples rather than medians | Multiple distributions are right-skewed; averages are distorted by high-multiple outliers |
| Mixing equity and firm-level multiples | E.g. dividing enterprise value by net income produces a meaningless number |
| Using book value as a proxy for market value of debt | Acceptable for approximation but can distort WACC if book and market values diverge significantly |
| Over-precision | A valuation with 8 decimal places is not more accurate; it is more misleadingly confident |
| Anchoring on the market price | Build your valuation from fundamentals first, then compare to market price — not the reverse |

**Damodaran's rule on precision:** *"Precision is a poor measure of quality in valuation. You will face more uncertainty when you value a young growth company than when you value a mature company."*

---

## 10. Quick Valuation Sanity Checks

After completing a valuation, test it against these checks:

1. **Does the implied growth make sense?** Back-calculate the revenue in year 10 implied by your terminal value. Is that market share plausible given total addressable market?
2. **Does the implied margin make sense?** Compare target margin to actual margins of mature firms in the same sector. If your assumed margin is double the industry average, justify it explicitly
3. **Does the terminal reinvestment rate match the growth rate?** Stable growth rate / Return on capital = reinvestment rate. Check this arithmetic
4. **Is ROIC > WACC in the terminal period?** If so, growth creates value. If ROIC < WACC, reconsider
5. **Multiples cross-check:** Convert your DCF value back into an implied EV/EBITDA or EV/Revenue multiple. Compare this to what similar businesses actually trade at. If your implied multiple is 20× and comparable businesses trade at 5–8×, the model assumptions need scrutiny
6. **Survival check for pre-revenue firms:** If you are using a going-concern DCF, have you applied a survival probability discount?
7. **Interest coverage check:** Does the business's forecast EBIT comfortably cover projected interest payments (DSCR ≥ 1.3× for lenders)?

---

## 11. Damodaran's 10 Rules for the Road

1. Feel free to abandon models, but do not budge on first principles
2. Pay heed to markets, but do not let them determine what you do
3. Risk affects value
4. Growth is not free and is not always good for value
5. All good things, including growth, come to an end. Nothing is forever
6. Watch out for truncation risk; many firms do not make it
7. Look at the past, but think about the future
8. Remember the law of large numbers. An average is better than a single number
9. Accept uncertainty, face up to it and deal with it
10. Convert stories to numbers

---

## 12. Valuation for Uganda / East Africa Context

Standard valuation frameworks apply but require several adjustments for the East African environment.

### 12.1 Country Risk Premium

Uganda is not a risk-free market. The discount rate must include a *country risk premium* (CRP) on top of the base equity risk premium:

```
Cost of equity (Uganda) = Risk-free rate (US/global) + Beta × (Global ERP + Uganda CRP)

Or using local risk-free rate:
Cost of equity (Uganda) = Uganda 10-year bond yield + Beta × Global ERP
```

Uganda CRP estimates (2024–2025): approximately 4–6% above the US ERP, reflecting political risk, FX volatility, and institutional uncertainty. Damodaran publishes annual country risk premium tables (damodaran.com) — use these as a reference point for investor negotiations.

**Practical shortcut for Uganda-context DCF:**
- WACC for established SME: 20–25% (UGX terms)
- WACC for early-stage/pre-revenue SME: 25–35%
- Stable growth rate in terminal value: 7–10% (aligned with Uganda GDP growth forecast)

### 12.2 Illiquidity Discount

Equity in a private Ugandan SME is far less liquid than a listed share. Investors will apply an *illiquidity discount* of 20–40% to the DCF or comparable-derived value. Founders should anticipate this and negotiate around it by:
- Offering clear exit paths (put options, drag-along rights, defined IPO timeline)
- Demonstrating audited financials and formal governance structures
- Referencing the Uganda Securities Exchange (USE) or future listing as an exit route

A typical illiquidity discount range applied by Uganda/East Africa DFIs and impact investors: **25–35%**.

### 12.3 Thin Comparable Data

East Africa has few publicly listed SMEs, making comparable company analysis difficult. Practical workarounds:
- Use regional (Kenya NSE, Rwanda, Tanzania) listed companies as proxies, adjusted for country risk difference
- Use transaction multiples from private equity deal reports (e.g. AVCA, African Venture Capital Association reports)
- Use Damodaran's sector-level beta and margin data (available free at damodaran.com) as global benchmarks, then adjust downward for Africa operating-environment risk
- For agricultural businesses, use FAO commodity price data to normalise earnings

### 12.4 FX Risk

For businesses with USD-denominated costs (imports) or USD revenues (exports), the valuation must account for UGX/USD exchange rate risk:
- Use a conservative planning rate (UGX 3,700/$1 per CLAUDE.md guidelines)
- Stress-test the valuation at UGX 4,000/$1 and UGX 4,500/$1 to show sensitivity
- Investors will apply an additional discount if the business has high unhedged FX exposure

### 12.5 Informal Financial Records

Many Uganda SMEs lack formal audited accounts. Damodaran acknowledges that historical performance is only one input into valuation — and the weakest predictor of future growth. For firms with informal records:
- Reconstruct a credible 2–3 year trading history using mobile money statements, supplier records, and tax filings (see `10-financial-projections/references/informal-business-records.md`)
- The DCF is then driven primarily by *forward* projections, validated against market-sizing data
- Investors will apply a larger uncertainty discount but will not reject a valuation simply because the firm lacks audited accounts — provided the assumptions are explicit and conservative

### 12.6 Discount Rate Reference Table (Uganda, 2025)

| Business Type | Indicative WACC Range | Notes |
|---|---|---|
| Established SME, formal records, collateral | 18–22% | Closer to bank lending rates |
| Growth SME, 2–4 years operating history | 22–28% | Standard angel/DFI range |
| Early-stage / pre-revenue startup | 28–40% | High survival risk; VC-method territory |
| Agribusiness (rainfed) | 25–35% | Add weather/commodity cycle risk |
| Financial services (MFI/SACCO) | Use ROE-based model; equity cost of capital 18–25% | |

*All rates in UGX terms. Adjust downward by approximately 8–10 percentage points for USD-denominated projections.*

---

## Valuation Method Selector

*Recommended primary method based on business stage and data availability:*

| Business Stage | Strong Data (audited, 3+ yrs) | Moderate Data (1–2 yrs, informal records) | Weak/No Data (pre-revenue, concept stage) |
|---|---|---|---|
| **Pre-revenue / concept** | Survival-adjusted DCF + forward multiples | Survival-adjusted DCF (market-sizing inputs) | VC method + market sizing story |
| **Early-stage (revenue < UGX 500M, losses)** | Survival-adjusted DCF + forward multiples | Survival-adjusted DCF + survival discount | Forward multiples (yr 3–5) + survival discount |
| **Growth (revenue UGX 500M–5B, improving margins)** | Full DCF (FCFF) + EV/Revenue multiples | DCF with sensitivity analysis + comparable multiples | Comparable multiples (EV/Revenue) |
| **Established / mature (UGX 5B+ revenue, positive EBIT)** | Full DCF (FCFF) + EV/EBITDA multiples | DCF with normalised earnings + P/E or EV/EBITDA | EV/EBITDA comparable analysis |
| **Cyclical / agricultural** | Normalised DCF (mid-cycle earnings) + scenario analysis | Normalised multiples + scenario range | Scenario analysis (trough/mid/peak) |
| **Financial services (MFI, SACCO)** | DDM or Excess Return Model | Excess Return Model (ROE vs cost of equity) | Book value + ROE-based premium |

**Always apply a Uganda/East Africa context adjustment:**
- Add country risk premium to discount rate
- Apply illiquidity discount of 25–35% to derived value
- Stress-test terminal value against 5% and 12% stable growth rates
- Cross-check implied EV/EBITDA or EV/Revenue against any available regional transaction data

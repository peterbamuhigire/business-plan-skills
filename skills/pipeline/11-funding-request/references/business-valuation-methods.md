# Business Valuation Methods for Funding Requests

Use this reference when Section 11 (Funding Request) must justify a valuation, an equity percentage or a pre-money figure, and when the plan must be ready for investor and development-finance negotiation. It sets out the three valuation approaches, the DCF inputs, multiples, early-stage methods, sector adjustments, common errors and East African adjustments. All rates, premiums, discounts and survival statistics are volatile and place-bound: treat every number below as a labelled planning assumption and replace it with a dated source (government bond yield, central-bank lending rates, published country-risk tables, sector data) before use. Verify tax and accounting inputs with the Chwezi finance engine. Method follows standard valuation practice (Damodaran and others); the structure and prompts are this engine's own.

## 1. Why the founder needs a valuation

The equity share an investor demands depends on how much they think the firm is worth. A founder who cannot state a defensible value either gives away too much equity or fails to close. Valuation rests on a few drivers and can be done by anyone willing to gather and analyse the information.

## 2. Three approaches

| Approach | Basis | Use when | Caution |
|---|---|---|---|
| Intrinsic (discounted cash flow) | Expected cash flows and their risk | Forecasts exist and a path to profit is visible; 3 to 5 year horizon | Sensitive to inputs; make assumptions explicit |
| Relative (multiples) | How the market prices comparable firms | Enough comparables; quick market-grounded estimate | Reflects sentiment; short shelf life; hides assumptions |
| Option-based | Value of the right, not the obligation, to invest | Unexploited reserves, unproven drugs, patents, early firms whose value is largely an option to enter a large market | Rarely suitable as the primary SME method |
Intrinsic and relative results will usually differ because they answer different questions. Use both; favour opportunities that look undervalued on both.

## 3. Discounted cash flow

### 3.1 Four inputs
Cash flow from existing assets; expected growth; discount rate (risk-adjusted cost of capital); terminal value.

### 3.2 Cash flow definitions
- Free cash flow to the firm (before debt service; gives enterprise value) = after-tax operating income - (net capital expenditure + change in non-cash working capital). Equivalent: after-tax operating income x (1 - reinvestment rate).
- Free cash flow to equity (after debt payments; gives equity value) = net income + depreciation - capital expenditure - change in working capital - (principal repaid - new debt raised).

### 3.3 Discount rate
WACC = cost of equity x E/V + after-tax cost of debt x D/V.
Cost of equity (CAPM) = risk-free rate + beta x equity risk premium (plus a country risk premium where relevant).
- Risk-free rate: long-term government bond yield in the currency of the projection (verify the current yield).
- Equity risk premium: from a dated published source; add country risk premium for the market.
- Beta: for private firms, use the industry average and adjust; beta 1 is average market risk.
After-tax cost of debt = (risk-free rate + default spread) x (1 - tax rate); use the firm's actual borrowing rate as a proxy. Confirm the corporate tax rate with the Chwezi finance engine.

### 3.4 Growth
Historical growth is a weak predictor. Use the fundamental growth rate: reinvestment rate x return on capital, where reinvestment rate = (net capital expenditure + change in working capital) / after-tax operating income, and return on capital = after-tax operating income / (book debt + book equity - cash). For net income: retention ratio x return on equity. Growth creates value only if return on capital exceeds cost of capital; below it, growth destroys value.

### 3.5 Terminal value
Often 70% to 90% of DCF value and above 100% for early-stage firms with negative near-term cash flow, so calculate carefully.
TV = FCFF x (1 + g) / (WACC - g).
Constraints on the stable growth rate g: it cannot exceed the long-run nominal growth of the economy (rule of thumb: no higher than the risk-free rate used); beta should move toward 1 and the debt ratio toward the industry norm as the firm matures; the stable reinvestment rate must equal g / stable return on capital. A multiple applied to terminal-year EBITDA or revenue from mature comparables is a useful cross-check.

### 3.6 Worked pattern (use own data)
1. Project revenue for five years (market size x share).
2. Apply a margin path from current to the mature sector margin.
3. Tax the operating profit; subtract reinvestment (set from growth and return on capital).
4. Discount each year's cash flow at WACC.
5. Compute terminal value with a lower stable WACC and stable growth; discount it.
6. Enterprise value = sum of both; subtract debt and add cash to reach equity value.
7. Run sensitivities on WACC, terminal growth and margin.
Record every assumption and its source next to the model.

## 4. Relative valuation

| Multiple | Formula | Companion driver |
|---|---|---|
| Price to earnings | Price / earnings per share | Growth, payout, risk |
| EV to EBITDA | Enterprise value / EBITDA | Growth, reinvestment, risk, return on capital, tax rate |
| EV to revenue | Enterprise value / revenue | Operating margin, growth, risk |
| Price to book | Price / book equity | Return on equity, growth, risk |
| PEG | P/E divided by expected growth | Growth quality |
Consistency rule: equity numerators (price) pair with equity denominators (earnings per share, net income); enterprise numerators pair with firm-level denominators (EBITDA, EBIT, revenue, FCFF).
Comparable analysis in four steps: (1) find firms with similar cash flows, growth and risk (start with sector peers, prune by size and geography); (2) compute standardised multiples and use the median, not the mean; (3) identify the companion variable, since a firm looks undervalued when it has a low multiple and a strong companion driver; (4) adjust for differences by PEG or regression.
Undervaluation signals: low P/E with high expected growth; low price to book with high return on equity; low price to sales with high net margin; low EV/EBITDA with low reinvestment needs; low EV/capital with high return on capital; low EV/sales with high operating margin.
Cautions: multiples move with market conditions and interest rates; loss-making comparables drop out and bias averages upward; relative valuation hides assumptions that DCF makes explicit.

## 5. Pre-revenue and early-stage firms

Difficulties: little history; small or negative revenue and earnings; high failure risk (published survival rates for new firms show a substantial share failing within a few years; verify the current figure for the market); illiquid equity; complex claims (preference shares, convertibles, option pools).

Method A, survival-adjusted DCF:
1. Value the firm as a going concern assuming it matures, using three drivers: revenue growth (market size and achievable share), target margin (mature-sector margin and a path to reach it) and survival probability.
2. Adjust: equity value = going-concern value x survival probability + distress value x failure probability.

Method B, forward multiples:
1. Project year-5 revenue from market sizing.
2. Apply a mature-firm EV/revenue multiple from comparables.
3. Discount the result at the cost of capital for five years.
4. Apply the survival probability.
5. Subtract debt and divide by shares.

Method C, investor (venture) method:
- Post-money value = expected exit value / (1 + required return)^N (or divided by the target return multiple).
- Pre-money value = post-money value - investment.
- Investor stake = investment / post-money value.
Simple but dependent on exit and return assumptions; use it as a negotiation anchor, not a fundamental value.

Key-person discount: for founder-dependent service firms, value the firm with and without the founder; the difference is the discount, and its size depends on how replaceable the person is.

## 6. Risk, growth and value

- Risk affects value through the discount rate, not the growth numerator. Factors that raise perceived risk (weak team, single-customer dependence, no IP protection, regulatory uncertainty, informal records, currency exposure) lower value. Reducing risk through governance, audited accounts, long-term offtake agreements and trademark filings raises value measurably.
- Growth creates value only when return on invested capital exceeds WACC, only while the competitive advantage lasts, and only if reinvestment earns its keep. Value of growth = present value of (ROIC - WACC) x invested capital over the excess-return period.
- In terminal value, raising g adds value only when stable-phase return on capital exceeds cost of capital; if they are equal (the conservative case), g does not change terminal value.

## 7. Sector notes

- Financial firms (banks, microfinance institutions, savings cooperatives): standard FCFF DCF does not apply because debt is a raw material. Use a dividend discount model, an FCFE model where reinvestment equals the increase in regulatory capital, or the excess-return model: equity value = book equity + PV of (ROE - cost of equity) x book equity. The excess-return model shows plainly whether value is created above book.
- Commodity and cyclical firms (agriculture, mining): use normalised mid-cycle earnings, never peak-year earnings. Value trough, mid-cycle and peak scenarios and weight by probability.
- Real estate: DCF of net rental income at a risk-adjusted rate including an illiquidity premium, or per-square-metre comparables adjusted for location, condition and lease terms.
- Early-stage: use all three methods as cross-checks.

## 8. Common mistakes

| Mistake | Effect |
|---|---|
| Peak-year earnings as base | Overstates cyclical value |
| Terminal growth above the economy's growth | Inflates value |
| Not funding the reinvestment that growth needs | Overstates free cash flow |
| Ignoring survival risk in pre-revenue firms | Going-concern value overstated, sometimes by a large margin |
| Adding synergy or management premiums after the valuation | Double counting |
| Averages instead of medians for multiples | Skew from outliers |
| Mixing equity and firm-level multiples | Meaningless ratio |
| Book value as proxy for market value of debt | Distorts WACC if they diverge |
| Over-precision | False confidence |
| Anchoring on the market price | Build from fundamentals first |

## 9. Sanity checks

1. Implied year-10 revenue from the terminal value is plausible against market size.
2. Target margin is consistent with mature sector margins; justify any premium.
3. Terminal reinvestment rate equals stable growth / return on capital.
4. Return on capital in the terminal period is at or above WACC (or growth adds no value).
5. Implied EV/EBITDA or EV/revenue from the DCF is close to what comparable businesses trade at.
6. Survival adjustment applied for pre-revenue firms.
7. Forecast EBIT covers interest with a margin (lenders often look for a debt-service coverage ratio around 1.3 or more; confirm the lender's own threshold).

## 10. Principles to state in the plan

Hold first principles even if models change; watch markets without letting them dictate; risk affects value; growth is not free and not always good; nothing lasts forever (model the fade); firms can fail (truncation risk); look at the past but think about the future; use expected values from scenarios; accept and address uncertainty; convert the story to numbers.

## 11. East African adjustments

1. Country risk: add a country risk premium to the cost of equity, from a dated published table (Damodaran publishes annual country-risk data). Alternatively use the local government bond yield and the global equity risk premium.
2. Illiquidity: private SME equity is far less liquid than listed equity, so investors apply a discount to derived value. State the range you assume, sourced from recent deals, and offer exit routes (put options, drag-along rights, a defined listing timetable, stock-exchange listing) with audited accounts and formal governance to narrow it.
3. Thin comparables: use listed regional companies as proxies with a country-risk adjustment; private-equity deal reports from industry associations; global sector betas and margins adjusted downward for operating-environment risk; commodity price data to normalise agricultural earnings.
4. Foreign exchange: model in one currency; use the engine's planning exchange rate (see the engine CLAUDE.md) and stress-test weaker rates; investors discount unhedged exposure.
5. Informal records: reconstruct two to three years of trading history from mobile-money statements, supplier records and tax filings (see `../../10-financial-projections/references/informal-business-records.md`); drive the DCF mainly from forward projections validated against market sizing; state assumptions explicitly and conservatively.
6. Discount-rate ranges by business type: build a table with columns for business type, indicative WACC range, source and date. Rows to fill from current data: established formal SME with collateral; growth SME with two to four years' history; early-stage or pre-revenue; rain-fed agribusiness (add weather and commodity-cycle risk); financial services (use an ROE-based model). Adjust for currency: a USD projection carries a lower rate than a local-currency projection by roughly the interest and inflation differential.

## 11a. Method selector

| Stage | Strong data (audited, 3+ years) | Moderate data (1 to 2 years, informal) | Weak or none |
|---|---|---|---|
| Pre-revenue or concept | Survival-adjusted DCF plus forward multiples | Survival-adjusted DCF with market-sizing inputs | Investor method plus market-sizing story |
| Early stage, small revenue, losses | Survival-adjusted DCF plus forward multiples | Survival-adjusted DCF plus survival discount | Forward multiples plus survival discount |
| Growth, improving margins | Full FCFF DCF plus EV/revenue | DCF with sensitivities plus comparables | EV/revenue comparables |
| Established, positive EBIT | Full FCFF DCF plus EV/EBITDA | DCF with normalised earnings plus multiples | EV/EBITDA comparables |
| Cyclical or agricultural | Normalised DCF plus scenarios | Normalised multiples plus scenario range | Trough, mid and peak scenarios |
| Financial services | Dividend discount or excess-return model | Excess-return model | Book value plus ROE-based premium |
Always add the local adjustments: country risk in the discount rate; an illiquidity discount; a stress test of terminal value at low and high stable growth rates; a cross-check against any regional transaction data.

## 12. Plan-section prompts

- Which valuation approach and why, given data quality and stage?
- Table of assumptions with sources and dates (discount rate build-up, growth, margin path, terminal growth).
- Sensitivity table and range, not a single number.
- Implied multiple compared with regional transactions.
- Risk-reduction actions and their expected effect on value.
- How the valuation translates into the equity offered (see `equity-term-sheets.md`).

Sources consulted: Damodaran, The Little Book of Valuation, Wiley, 2011; Damodaran's published country-risk and sector datasets (verify current editions).

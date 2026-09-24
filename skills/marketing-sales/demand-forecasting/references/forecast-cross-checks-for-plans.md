# Forecast cross-checks for business and marketing plans

Parent: [Demand Forecasting](../SKILL.md).

When to read: when a demand or sales forecast feeds a business plan, a
marketing plan's demand-to-cash bridge or a funding model, especially when
history is thin or the offer is new. These checks sit on top of the
operational forecasting method in the parent skill. Method sources: Stockwell,
J. and Shaw, H. M. (1994) *Direct Marketing Checklists*, NTC Business Books
(forecast double-checks, echo effect); Croll, A. and Yoskovitz, B. (2013)
*Lean Analytics*, O'Reilly Media (stage, cohort and line-in-the-sand logic);
Barrow, C. (2009) *Get Backed, Get Big, Get Bought*, Capstone (adoption
check); Lin, L. C. (2013) *Decode and Conquer*, Impact Interview (driver trees).

## 1. Use at least two methods

Combine two or more of: sales history by product and place; a driver tree from
the funnel (reach × response × conversion × order value); a capacity-led
ceiling (what delivery can actually serve); comparable operators' volumes; and
test results. Report the range between methods and explain the gap. Plan on
the better-evidenced figure, not the higher one. See
`../../../pipeline/04-market-analysis/references/estimation-trees-and-sanity-checks.md`
for driver-tree patterns.

## 2. Guard against known biases

| Source of forecast | Typical bias | Control |
|---|---|---|
| Owner or executive judgement | Optimism; one voice dominating | Record each person's estimate before discussion; keep an accuracy log |
| Sales-team estimates | Mood of the month; sandbagging to beat quota | Compare with pipeline stage data and past accuracy |
| Customer surveys of intent | Stated intent exceeds behaviour | Discount intent heavily or replace with deposits and pre-orders |
| New list, medium or region | Assumed to match the current best performer | Assume break-even or below until a test reads out |

## 3. Adoption and stage checks

- Year-one volume for a new-to-market offer must be plausible against the
  share of the served market that adopts early; a forecast that needs a large
  share in year one needs pre-orders, contracts or pilot data behind it.
- Declare the business stage. A venture that has not yet shown repeat purchase
  should forecast from cohorts in pilots, not from acquisition spend.
- Forecast retention and repeat purchase separately from new customers, and
  never count the same customer twice.

## 4. Echo effect and untracked sales

Campaigns lift untracked sales (walk-ins, phone orders, retail). If the plan
counts them, measure a pre-campaign baseline and report the echo separately
with a seasonality caveat.

## 5. Double-check list before a forecast enters the model

1. Reliable data, with at least two years of history where it exists.
2. At least two methods, with the range stated.
3. Every assumption stated with its evidence class (fact, assumption, estimate).
4. A range of error, not a single point.
5. Seasonality, stock-outs and one-off events removed or flagged.
6. Capacity ceiling applied.
7. Revised as actuals arrive; forecast accuracy tracked (WAPE or MAPE and bias).

## 6. Anti-patterns

- A single top-down share-of-market forecast. Fix: add a driver tree and a capacity ceiling.
- Survey intent treated as demand. Fix: behavioural evidence or heavy discount.
- New regions forecast at head-office conversion rates. Fix: test first.
- Point forecasts with no range. Fix: state the range and the driver that moves it most.

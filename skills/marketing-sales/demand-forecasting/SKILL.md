---
name: demand-forecasting
description: Use when producing demand forecasts, stockout timing, reorder logic, or branch and product sales aggregation from operational data; use `entrepreneurial-demand-generation` for customer acquisition logic and financial-projection skills for the integrated plan model.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Demand Forecasting

## Overview

Use this skill to turn sales, inventory, branch, and operational signals into demand forecasts and replenishment recommendations. It is especially relevant when fixing SQL joins that duplicate products, deriving days until stockout, or documenting demand-driven planning assumptions.

## Use When

- Use when a plan, dashboard, operational model, or funding case needs demand forecasts,
  reorder logic, stockout timing, or sales-rate assumptions.
- Use when branch, SKU, warehouse, or channel data must be converted into replenishment or
  capacity planning evidence.

## Do Not Use When

- Do not use when the request only needs a generic sales target with no operational data.
- Do not use predictive methods when the history is too thin; state the forecast as a
  planning assumption instead.

## Required Inputs

- Sales, inventory, stock movement, lead time, and inbound-order data where available.
- Forecast horizon, reporting grain, excluded events, and business action triggered by
  the forecast.
- Any known stockouts, promotions, closures, returns, or one-off events.

## Workflow

1. Define the reporting grain first: usually one row per product per shop, branch, outlet, or warehouse for the forecast horizon.
2. Aggregate sales and stock movements before joining product, branch, and stock-balance tables. Do not join raw sales lines directly to item master or stock balances when the output expects one product row.
3. Exclude or separately flag voided sales, returns, internal transfers, stockout days, and one-off events that would distort demand.
4. Normalize demand to a daily rate. Use 7, 30, and 90 day windows when available, and explain which window drives the forecast.
5. Derive days until stockout as `current_stock / daily_demand`. If demand is zero, report "no active demand" rather than hiding the value as an unexplained N/A.
6. Calculate forecast consumption as `daily_demand * horizon_days`.
7. Calculate reorder point as `daily_demand * lead_time_days + safety_stock`.
8. Calculate suggested order as `max(0, forecast_consumption + safety_stock - current_stock - inbound_qty)`.
9. Backtest against historical periods using WAPE/MAPE, bias, and missed-stockout counts.
10. Classify the forecast as predictive analytics and document the history window,
    exclusions, method, uncertainty, and action trigger. Use
    `../../book-extractions/data-analytics-business-planning-extraction.md` when the
    forecast feeds a business plan, KPI dashboard, funding model, or management system.

## Join Guardrails

- Use CTEs or subqueries for `sales_by_product_branch`, `stock_by_product_branch`, and `inbound_by_product_branch`.
- Group every CTE by the same business key before joining: product id plus branch/shop/outlet/warehouse id.
- Join product and branch names once, after aggregation.
- Assert that the final result has no duplicate product plus branch rows.
- If the UI needs one product row per selected branch, collapse variants after filtering by branch, not across all branches.

## Quality Bar

- Forecast grain is explicit and duplicate-safe.
- Demand windows, exclusions, and assumptions are documented.
- Backtesting or limitation notes are included where historical data allows.
- The output states the action trigger: reorder, capacity increase, stock transfer, or
  management review.

## Anti-Patterns

- Joining raw transaction lines to product master data and creating duplicate demand.
- Treating sales during stockout periods as true demand.
- Hiding zero demand or missing history as unexplained blanks.
- Presenting point forecasts without history window, method, or caveat.

## Outputs

- Demand forecast, stockout timing, reorder calculation, branch/SKU demand table, or
  business-plan assumption note.

## References

Load `references/demand_forecasting.md` for SQL templates, stockout formulas, and demand-driven planning notes.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Time-stamped demand, sales, stock, price, promotion, stockout, branch, and product data | POS, ERP, inventory, ecommerce, or approved extracts | Required | Return a data-gap assessment and scenario range, not a point forecast |
| Business calendar, lead times, service levels, and known events | Operations, procurement, and commercial owners | Required for replenishment | Keep reorder outputs conditional |
| Revenue, return, inventory, and unit definitions | Chwezi Accounting Doctrine and data owners | Required | Stop until measures and duplicate-row risks reconcile |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Forecast dataset and method note | Operations, procurement, sales, and finance | Grain, horizon, method, features, exclusions, uncertainty, and backtest are explicit |
| Reorder or capacity decision table | Stock and operating owners | Each action links to forecast range, lead time, service level, constraint, and override owner |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Data-quality and join audit | Row-count, uniqueness, missingness, stockout, and reconciliation checks | Aggregation has not multiplied sales or confused zero demand with no stock |
| Forecast evaluation | Backtest by horizon and segment | Error is compared with a simple baseline and weak segments are visible |

## Capability Contract

Analysis defaults to read-only. Do not alter source data, purchase orders, prices, promotions, or stock. Execution may run authorised queries and models against safe copies; production writes, spending, and accounting conclusions require explicit authority and review.

## Degraded Mode

Without adequate history, execution, or reliable stockout and return data, return a qualified bounded scenario, data requirements, and a backtest marked `not assessed`. Do not call missing sales zero demand or present an untested model as accurate.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Sparse or short history | Use a transparent baseline and wide range | Model overfit |
| Stable repeated pattern with enough history | Compare seasonal and statistical methods by backtest | Unnecessary complexity |
| Stockouts censor observed sales | Estimate lost-demand range and flag confidence | Under-forecasting constrained items |
| SQL join changes row counts at the target grain | Stop and repair aggregation before modelling | Duplicated demand |

## Workflow

1. Define forecast target, grain, horizon, decision, cost of error, and override authority.
2. Extract and reconcile demand, stock, price, returns, promotions, calendar, and lead-time data.
3. Run uniqueness, join, missingness, stockout, outlier, and accounting-definition checks; stop on unresolved multiplication.
4. Establish naive baselines and time-respecting backtests.
5. Fit only methods justified by history and compare error by segment and horizon.
6. Translate forecast ranges into reorder, staffing, or capacity actions with constraints.
7. Monitor actuals, overrides, drift, and error; recover by reverting to the best validated baseline.

## Quality Standards

Forecasts must be reproducible, time-safe, reconciled to defined demand, compared with a baseline, and expressed with uncertainty. Decision usefulness matters more than model sophistication.

## Anti-Patterns

- Randomly splitting time-series rows. Fix: backtest forward in time.
- Joining sales to multiple stock rows. Fix: aggregate each source to the target grain before joining.
- Treating stockout days as zero demand. Fix: flag censored observations and estimate a range.
- Optimising one overall error metric. Fix: inspect horizon, branch, SKU, and business cost of error.
- Reordering from a point forecast alone. Fix: include lead time, service level, pack size, stock, and uncertainty.
- Claiming accuracy without a naive baseline. Fix: show whether the method beats the simple alternative.

## Worked Example

If a branch-SKU join doubles rows after adding promotions, stop before forecasting, aggregate promotions to one row per branch-SKU-date, reconcile totals, then backtest the repaired dataset against a seasonal naive forecast.
<!-- dual-compat-end -->

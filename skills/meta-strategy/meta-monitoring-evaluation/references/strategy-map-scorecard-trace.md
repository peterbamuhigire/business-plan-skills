# Strategy-map and scorecard trace

This reference implements B18-A02. It turns a strategy map into a small,
causal scorecard whose measures can be reconciled to the plan and finance
workpaper.

## Causal chain

`learning/capability` → `internal process` → `customer/market` → `financial`

Each outcome measure must point to an enabler or process measure, and each
leading measure must have a decision it changes. A list of attractive metrics
without a causal path is not a scorecard.

## KPI trace row

| Field | Requirement |
|---|---|
| Objective and perspective | Named strategic objective and one of the four perspectives. |
| Causal parent/child | Upstream enabler and downstream outcome IDs. |
| KPI and definition | Exact measure, boundary, numerator, denominator, and exclusions. |
| Formula and unit | Reproducible calculation and unit/currency. |
| Source and period | System or record, source ID, period, and reporting basis. |
| Baseline/target/threshold | Case-specific values with status; no copied benchmark. |
| Cadence and owner | Collection and review frequency plus accountable role. |
| Decision/action | Action when threshold is missed, including counter-metric. |
| Reviewer/status | Review role and `verified`, `assumption`, `blocked`, or `not_assessed`. |

## Construction and reconciliation

1. Start from the strategic choice and draw the four-perspective causal path.
2. Select a few leading and lagging measures whose sources can actually be
   collected. Define formula, unit, period, basis, cadence, owner, threshold,
   and decision before setting a target.
3. Reconcile financial measures with the financial-intelligence brief and the
   applicable finance definition. Reconcile operational measures with the
   operating plan and customer pathway.
4. Pair each headline measure with a counter-metric that can expose gaming or
   service harm. Record missing baseline as `not_assessed`.
5. Review in shadow mode, inspect false alarms, and revise the measure or source
   before it governs funding, staffing, or release decisions.

## Stop rules

- KPI without source, owner, formula, threshold, period, or decision is
  `blocked`.
- A target copied from a different case is rejected unless a current,
  comparable source and rationale are recorded.
- A financial measure that does not reconcile to the plan or finance workpaper
  remains `not_assessed`.
- A missing baseline never becomes a pass because a target was supplied.

## Currentness record

| Field | Record |
|---|---|
| Source scope | B18 book-study concept, applied to a strategy-map and KPI trace. |
| Publication/version date | Book-study source; no external benchmark or current funder rule is asserted. |
| Access date | 2026-09-19 |
| Freshness class | Durable concept input; definitions and targets are case-specific. |
| Review date | Before external release and whenever source systems, targets, or reporting obligations change. |
| Support status | Supported as a measurement design; finance and audience review remain required. |
| Uncertainty | Baselines, thresholds, data availability, and current reporting requirements may be `not_assessed`. |

# Manager financial-intelligence brief

This reference implements the business-plan portion of B07-A03. It gives a
manager or proposal reviewer a short, traceable reading of profit, cash,
working capital, ratios, alternatives, and timing. It does not replace the
finance engine's accounting, tax, statutory, or control-account review.

## Brief contract

| Field | Required content |
|---|---|
| Decision | The decision the reader must make and by when. |
| Basis | Currency, period, cash/accrual basis, scenario, and model version. |
| Profit view | Revenue, direct cost, operating cost, and operating result with source or assumption IDs. |
| Cash view | Opening cash, receipts by timing, paid outflows, financing, and closing cash. |
| Working-capital view | Receivables, payables, inventory or service-delivery timing, and cash-conversion effect. |
| Ratios | Named numerator, denominator, formula, period, source, and decision use. |
| Alternatives | Base case, preferred option, credible lower-investment or do-nothing case, and downside. |
| Owner and reviewer | Named roles, review date, unresolved questions, and next check. |

## Plain-language definitions

- **Profit** is the declared-basis result after the costs included in the
  model. It is not cash available for debt service or distribution.
- **Cash** is opening cash plus receipts received in the period, less payments
  made in the period, plus or less declared financing and investing flows.
- **Working capital** explains the timing gap between operational activity,
  invoicing or claims, settlement, supplier payment, and cash.
- **Ratio** is a calculation, not a benchmark. Show the numerator,
  denominator, period, basis, and the decision it informs. Do not copy a target
  from another case without a current, comparable source.

## Construction sequence

1. Trace every headline number to the FP&A assumption trace, source register,
   or an explicit management assumption.
2. Recompute the profit and cash bridges from declared inputs. Keep revenue
   recognition and cash timing separate.
3. Explain the working-capital lever, its service or supplier risk, owner, due
   date, and evidence needed. Disputed timing remains `not_assessed`.
4. Compare alternatives on incremental cost, incremental cash benefit, timing,
   downside, and reversibility. State why the selected option wins.
5. Ask the finance reviewer to confirm accounting and statutory implications
   before the brief is used in a funding or proposal handoff.

## Minimum evidence table

| Headline measure | Formula / bridge | Source or assumption | Period and basis | Owner | Status |
|---|---|---|---|---|---|
| Operating result | Revenue - direct costs - operating costs | Trace row IDs | Declared | Finance owner | `verified` / qualified |
| Closing cash | Opening cash + collected receipts - paid outflows + financing | Cash schedule IDs | Cash basis | Treasury owner | `verified` / qualified |
| Working-capital effect | Opening balance + additions - settlements - evidenced adjustments | Subledger or synthetic fixture | Declared | Controller | `verified` / `not_assessed` |
| Decision ratio | Declared numerator / declared denominator | Trace row IDs | Same period and basis | Finance reviewer | `verified` / `blocked` |

## Failure controls

- Missing basis or comparator blocks the conclusion.
- Profit and cash are never merged into one "surplus" line.
- ROI without timing, alternatives, assumptions, and cash implication is
  `not_assessed`.
- Unsupported peer or market benchmarks are removed or labelled as an evidence
  gap.
- No recommendation authorises posting, payment, filing, or a statutory claim.

Use the FP&A assumption trace at
`../../../docs/kaizen/fpa-assumption-trace.md` and the synthetic checks in
`tests/test_phase1_kaizen_contracts.py` before handoff.

## Currentness record

| Field | Record |
|---|---|
| Source scope | B07 book-study concept, applied to a manager-facing planning brief. |
| Publication/version date | Book-study source; no current benchmark or accounting authority is asserted. |
| Access date | 2026-09-19 |
| Freshness class | Durable concept input; financial definitions remain subject to the finance engine. |
| Review date | Before external release or when the model, basis, or funding decision changes. |
| Support status | Supported as a trace and review structure; not a professional finance opinion. |
| Uncertainty | Current rates, tax, statutory treatment, peer benchmarks, and ROI evidence are `not_assessed`. |

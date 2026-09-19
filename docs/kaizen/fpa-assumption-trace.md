# FP&A assumption trace

This reference is the business-plan side of B03-A04. It makes the evidence
behind a financial narrative inspectable without treating a planning value as
an accounting fact. It is a planning and review contract; the finance engine
owns accounting treatment, postings, statutory values, and control-account
definitions.

## Scope and status vocabulary

Use this trace for every number or financial conclusion that appears in a plan,
proposal, pilot note, or investment case. Each item has one status:

| Status | Meaning | Release behaviour |
|---|---|---|
| `verified` | Supported by an identified source for the stated period and basis. | May be used subject to reviewer approval. |
| `management_assumption` | An explicit planning choice owned by management. | May be modelled; label it and test a countercase. |
| `estimate` | A provisional value derived from incomplete evidence. | Keep qualified and assign a verification action. |
| `inference` | A conclusion derived from other trace rows. | Show the calculation and inputs. |
| `blocked` | Required evidence is absent, stale, disputed, or out of scope. | Do not use in a headline conclusion. |
| `not_assessed` | The relevant check was not run or could not be judged. | Preserve the question and owner. |

`verified` does not mean statutory, audited, or professionally approved. Those
claims require the applicable finance-engine route and named reviewer.

## Required trace row

| Field | Requirement |
|---|---|
| `claim_id` | Stable identifier used by the narrative and model. |
| `statement` | Plain-language claim or assumption. |
| `metric` / `value` / `unit` | Exact measure; use `null` when unresolved. |
| `currency` / `period` / `scenario` | Currency, reporting or planning period, and scenario. |
| `basis` | Cash, accrual, operational, or other declared basis. |
| `source_id` / `source_locator` | Source register ID and page, cell, record, or interview locator. Use `null` when not sourced. |
| `calculation` | Formula and input claim IDs for derived values. |
| `owner` / `reviewer_role` | Person or role responsible for confirmation and review. |
| `status` / `next_check` | Evidence state and the action needed to move it forward. |
| `countercase` / `decision_use` | What could overturn it and what decision it informs. |

Rows with missing `period`, `basis`, `scenario`, `source_id` (unless explicitly
`management_assumption`), `owner`, or `reviewer_role` are `blocked` or
`not_assessed`; they are never silently completed by the writer.

## Review procedure

1. Identify the decision, reader, jurisdiction, currency, period, and reporting
   basis before drafting the financial sentence.
2. Create one trace row per material number. Link derived rows to their inputs
   and keep the formula visible.
3. Separate facts, management assumptions, estimates, and inferences. Record a
   countercase and cash implication for each headline conclusion.
4. Check that the row agrees with the financial model, operating plan, and
   funding request. Return a mismatch to the owning section.
5. Route accounting, tax, payroll, statutory, or control-account judgements to
   the finance engine reviewer. Do not infer a current rate or rule.
6. Release only rows that have a reviewer route and no unresolved blocker;
   retain the exception list and next check in the handoff.

## Bounded FP&A pilot contract

An FP&A pilot may assist with classification, variance questions, or scenario
comparison only within a named dataset and period. It must have a human owner,
approval record, override reason, failure state, rollback to the prior manual
route, and a measurable acceptance oracle. The pilot cannot post, pay, file,
approve a statutory treatment, or replace professional judgement. Vendor names,
prices, capability claims, and current platform behaviour remain
`needs-current-verification` until researched through the currentness gate.

## Acceptance and failure cases

- A complete row links a value to source/version or labels it as an explicit
  management assumption, and names owner and reviewer.
- A scenario, unit, period, or basis mismatch returns a stable row locator and
  blocks the affected conclusion.
- An unsupported market size, ROI, peer benchmark, tax rate, or payer term is
  labelled `not_assessed` or removed.
- A pilot failure pauses the pilot, preserves the previous version, and records
  the recovery owner; it does not silently fall back to an invented value.

The companion fixture is `tests/fixtures/phase1-kaizen-contracts.json` and the
deterministic checks are in `tests/test_phase1_kaizen_contracts.py`.

## Currentness record

| Field | Record |
|---|---|
| Source scope | B03 book-study concept, applied to the business-plan trace surface. |
| Publication/version date | Book-study source; exact external standard version is not asserted here. |
| Access date | 2026-09-19 |
| Freshness class | Durable concept input; not a current law, platform, rate, or accounting standard. |
| Review date | Before external release and whenever the finance, platform, or pilot control changes. |
| Support status | Supported as a planning-contract design; finance-engine and professional review remain required. |
| Uncertainty | Current model capabilities, vendor terms, accounting judgements, and statutory values are `not_assessed`. |

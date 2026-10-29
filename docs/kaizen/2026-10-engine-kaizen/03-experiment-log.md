# Experiment log

Access date: 2026-10-29. The three full practitioner task outputs are retained
in [`00-practitioner-tasks.md`](00-practitioner-tasks.md). Company and workbook
values in those tasks are synthetic. No client, lender or investor file was
supplied.

| ID | Experiment and inputs | Observed result | Decision / limits |
|---|---|---|---|
| E1 | Before change, run the original formula-map on the retained synthetic workbook with cash 100, balance-sheet cash 80, `=B1-B2`, blank cached result. | Structural PASS with zero findings. | Confirmed mismatch-detection false negative. Original report retained at [`labs/synthetic-mismatch-audit.json`](labs/synthetic-mismatch-audit.json). |
| E2 | Run the required cell-level contract against the same mismatched workbook. | Exit 1 with `reconciliation-values-differ` and `reconciliation-cache-missing`; output retained in [`labs/synthetic-mismatch-final-audit.json`](labs/synthetic-mismatch-final-audit.json). | Demonstrates the known mismatch is detected. Not a real client financial result. |
| E3 | Generate a passing report from an OOXML fixture with equal numeric source cells, declared subtraction, zero difference and a numeric cached value. Re-run release validation using the XLSX and contract. | Matching proof is accepted only after recomputing workbook reconciliation; wrong hashes, altered report checks, missing contract/report, and a forged PASS over a mismatched workbook are rejected by tests. | This validates the narrow criterion only. Contract cell selection still needs reviewer judgement; no arbitrary spreadsheet graph is recalculated. |
| E4 | Test a due-date-expired entry while status is `verified-current`; run the repository register check after marking the ten overdue entries `stale`. | The negative lifecycle fixture is rejected for contradictory status; repository check still exits 1 on ten overdue rows. | No source was renewed by date/status edits. Source-level renewal remains open. |
| E5 | Scan the repaired retail reference and run its focused C0 regression test. | The reference contains no non-whitespace C0 byte; test passes. | No repo-wide byte scan is claimed. |
| E6 | Validate Claude manifests; install Claude plugin and Codex plugin from their local catalogues in disposable offline containers with the checkout mounted read-only. | Both native marketplace add/install/list workflows succeed; Claude validator passes with plugin-directory warnings. | No host configuration, public submission, or model call. Strict Claude validator still rejects warnings; public acceptance remains not assessed. |
| E7 | Exercise the hard-cap helper at 5,000 and 5,001 for both counts, attempt a CLI override, then count the worktree. | Boundary exactly at cap passes; 5,001 and any unsupported override fail; observed pre-commit counts are in [`05-final-report.md`](05-final-report.md). | Count is not a built archive. Official ZIP limit source is linked in that report. |

## Practitioner output summary

1. **Synthetic bank plan:** route selection is appropriate; no actual entity,
   customer, lender terms, market, accounting basis, tax, or reviewer evidence
   was supplied. No bankability conclusion is supportable.
2. **Investor version:** retains the same synthetic assumptions and arithmetic;
   there is no product, cap table, terms, valuation, or independent-review
   evidence to support investor claims.
3. **Workbook mismatch:** the baseline false negative is reproducible and now
   fails through the required narrow contract. This does not establish that all
   workbook arithmetic is correct.

Detailed synthetic inputs and explicit financial omissions are in the linked
practitioner task output. Dynamic official indicators and model-release
currentness findings are in [`00-scope-and-evidence.md`](00-scope-and-evidence.md).
## Full practitioner task outputs

All company-specific values below are explicitly synthetic test inputs, not observations about a real business or Ugandan market. The fixture is intentionally small to exercise routing and reconciliation logic. The source and rationale for each number is the synthetic input itself in this report; these figures must not be presented as externally evidenced, forecast, lender-approved, or accounting-approved facts. Currency is UGX; values shown in UGX millions unless stated. No tax rate or lending rate is assumed.

## Task 1 — bankable plan and three-year model; release-gate result

### Intake and route

Requested: an early-stage Ugandan SaaS bank-loan plan plus three-year financial model. No company identity, product evidence, customer contracts, market study, management biographies, registrations, lender term sheet, historical accounts, payroll, tax advice, or authority evidence was supplied. Router route: business-plan orchestrator → country context and market validation → plan sections → projections → investment committee challenge → release. Accounting/tax questions require the accounting-engine reviewer; market evidence requires digital research. This is the appropriate route; the missing proof is not filled by the synthetic scenario.

### Fictional test case and explicit assumptions

“Lakeview Ledger” is a fictional SaaS case created only for the test. It is not the repository's LakeLink exemplar and is not a real company. Assumptions below are arbitrary scenario inputs, not evidence:

| Input | Year 1 | Year 2 | Year 3 | Status |
|---|---:|---:|---:|---|
| Average paying customers | 100 | 250 | 500 | management assumption (synthetic) |
| Monthly subscription per customer, UGX | 100,000 | 100,000 | 100,000 | management assumption (synthetic) |
| Annual subscription revenue, UGX m | 120 | 300 | 600 | derived as customers × monthly price × 12; synthetic |
| Direct service cost, UGX m | 24 | 60 | 120 | management assumption (synthetic) |
| Operating cost, UGX m | 180 | 230 | 300 | management assumption (synthetic) |
| Operating surplus before financing/tax/depreciation, UGX m | (84) | 10 | 180 | derived revenue − direct cost − operating cost; synthetic |

The arithmetic is internally consistent with the inputs shown. The model omits working capital, cash timing, capital expenditure, depreciation, financing costs, statutory tax, owner distributions, foreign exchange exposure, and any actual lender repayment schedule. Consequently it does not establish liquidity, debt-service capacity, break-even in accounting terms, or bankability. No tax values are supplied; route them to the accounting engine's current register and named reviewer.

### Credit-facing plan extract

- **Business and product:** fictional Ugandan subscription software provider; no product validation or legal identity evidence supplied.
- **Customer and market:** no customer interviews, pipeline, signed contracts, comparable market definition, market-size source, or competitor evidence supplied. The customer counts are scenario assumptions only.
- **Commercial model:** assumed subscription price and customer ramp are scenario inputs. No conversion, churn, retention, collections, or unit-economics evidence supplied.
- **Operations/team:** no named management, staffing plan, infrastructure, data-protection controls, or supplier quotations supplied.
- **Funding request/use:** requested bank amount, tenor, pricing, security, covenants and use of proceeds remain unspecified. Do not manufacture a request.
- **Financial case:** model above is a sensitivity scenario, not an accounting forecast. Actual bankability cannot be assessed without evidence and lender terms.
- **Risk and mitigations:** customer acquisition, churn, collections, service continuity, cyber/privacy, FX, tax/compliance and key-person risks are unquantified. Owners and controls are not evidenced.

### Release gate

The available DFI and VC example packages both pass structural schema validation while declaring `decision=blocked`; their exact blockers include missing rendered-pack/visual QA/security/authority evidence. This does not make the fictional test plan releasable. A real borrower plan is **blocked** pending source-backed market and customer evidence, identity/authority, reviewed assumptions, accounting/tax review, complete model and supporting schedules, rendered QA, security review, and authorized release.

## Task 2 — investor version of the same plan; reconciliation check

### Investor-facing rewrite

For the same synthetic Lakeview Ledger case, the investor version can describe the assumed customer ramp and subscription revenue as a scenario to test. It cannot claim product-market fit, market share, defensibility, investor return, valuation, exit, or validated unit economics because no supporting evidence was provided. The three-year synthetic revenue figures and operating-surplus arithmetic are exactly the Task 1 inputs and derivations above; the investor narrative therefore remains numerically aligned with that scenario. It must retain the same omissions and cannot relabel the scenario as a forecast.

### Reconciliation result

Narrative values are linked to the model assumptions and formulas in Task 1, so the displayed arithmetic reconciles within that toy scenario. A full model-to-narrative tie-out is **not assessed**: no workbook, accounting basis, cash-flow schedule, tax treatment, cap table, valuation method, investment terms, or independent reviewer evidence supports a real investor case. This is an arithmetic consistency check only.

## Task 3 — deliberately mismatched workbook; detection/release test

Created disposable workbook `labs/synthetic-mismatch.xlsx` outside the checkout: synthetic cash-flow ending cash = 100; synthetic balance-sheet cash = 80; formula labeled “Balance Sheet Check” is `=B1-B2`; workbook also contains a “base” scenario label. The mismatch is deliberate and exists solely to test controls.

Command in the preparation run: `python -B tools/workbook-audit/formula_map.py <synthetic-mismatch.xlsx> --require-scenarios --require-balance-checks --json-out <synthetic-mismatch-audit.json>`. The exact specimen and captured report are retained under `labs/` beside this file; angle-bracket paths here denote the external preparation run, not literal CLI arguments.

Observed result: **PASS, zero findings**. Formula-map detected one formula and three text hits for balance/check, but the formula's cached value was blank and no calculation/reconciliation was performed. This is a confirmed failure of the requested mismatch-detection task. The test was created with temporary `openpyxl` installed in the external prep venv after the initial creation attempt showed the dependency was absent; nothing was installed in the repository or host environment.

Release-gate code review shows it validates bundle declarations, evidence paths, stages, handoffs, blockers and authority; it does not parse workbook values. Thus this mismatched workbook is not detected by that gate either. The release gate can block for missing evidence, but it cannot claim this particular numerical mismatch was caught. **Root-cause hypothesis (inference):** the formula-map is intentionally a structural XML scan and lacks a calculation engine or declared cell-level reconciliation oracle; its text regex lets descriptive labels satisfy a presence check.

### Task outcomes

| Task | Outcome | Release status |
|---|---|---|
| Bankable plan + model | Scenario extract generated; real evidence absent; no debt service validation. | Blocked |
| Investor version | Same synthetic assumptions retained; arithmetic aligned; investment evidence absent. | Blocked |
| Mismatched model detection | False negative in formula-map and no workbook inspection in release validator. | Critical blocker for relying on current structural pass as reconciliation evidence |

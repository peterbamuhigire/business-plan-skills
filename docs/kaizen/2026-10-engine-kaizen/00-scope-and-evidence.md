# Scope and evidence

- **Cycle:** Business Plan Skills, October 2026
- **Prompt:** 9, Business Plan Skills (source prompt pages 28–30)
- **Baseline checkout:** `d3d5013744b8a668e21647e45161c1c7f80fdc3d`
- **Branch:** `kaizen/2026-10`
- **Access date:** 2026-10-29
**Status:** baseline frozen in the immediately following scorecard commit before implementation.

This cycle uses only synthetic plan inputs and a disposable mismatch workbook.
No client, borrower, product, customer, lender, investor, tax or licensing file
was supplied. The synthetic plan is not a bank application, forecast, valuation,
accounting opinion, or release authorization. No external submission, paid model
call, host configuration change, deletion of user content, canonical doctrine
edit, or sibling-engine edit is part of this work.

## Router and evidence read

Read the repository router and the `business-plan-orchestrator` and
`kaizen-improvement-system` skills; the Digital Research `source-evaluation`,
`source-verification`, and portfolio currentness gate; the Portfolio Kaizen
Standard; the September audit/readiness review; the adoption plan; the July
upgrade index; and the current FP&A assumption-trace reference. The exact
three practitioner outputs are preserved in [03-experiment-log.md](03-experiment-log.md#full-practitioner-task-outputs).

| Task | Route selected | Observation |
|---|---|---|
| Synthetic Ugandan SaaS bank plan and three-year model | Orchestrator → intake/evidence → country/market → plan sections → projections → challenge → assembly/release | Route matches the request. Missing company and financing evidence correctly prevents a real bankability conclusion. The synthetic table is internally arithmetical but omits debt-service, working-capital, tax, depreciation, and cash-timing proof. |
| Investor version of the same scenario | Preserve the same assumptions and model; adapt audience language and test narrative/model ties | The scenario values remain aligned. A real investor case remains blocked without product, customer, cap-table, terms, valuation, and independent review evidence. |
| Deliberately mismatched cash-to-balance workbook | Formula-map and release-bundle checks | Formula-map returned structural `PASS` with zero findings for synthetic ending cash 100 and balance-sheet cash 80; the `=B1-B2` formula had a blank cached result. The release-bundle validator does not inspect workbook calculations. This is a confirmed false negative for the task's mismatch check, not proof that all workbook arithmetic is wrong. |

The formula-map result, synthetic workbook, and JSON output are retained in
[`labs/`](labs/). Earlier audit evidence also says workbook structure/formula
checks did not recalculate formulas; that report did not establish four exact
current bundle identities, and this cycle does not repeat the historical count
as a current finding. See the [September readiness review](../../audits/2026-09-06-kaizen-readiness.md).

## Currentness observation at baseline

Dynamic macro figures were checked against official issuers on 2026-10-29 for
the source-currentness review. They are point-in-time context only, not plan
assumptions or lending rates:

- Uganda's Bank of Uganda said it raised the CBR to 12.0% from 9.75% at its
  14 October meeting ([BoU publications](https://www.bou.or.ug/publications)).
- Uganda's annual CPI inflation for the twelve months to September 2026 was
  4.6% ([UBOS September CPI release](https://www.ubos.org/2026/09/30/consumer-price-index-september-2026/)).
- Kenya's CBR was 8.75% from 7 October 2026; CBK's page also reported a daily
  USD reference of KES 129.95 posted 28 October and September inflation of
  6.8% ([CBK rates](https://www.centralbank.go.ke/rates/central-bank-rate/),
  [CBK monetary-policy page](https://www.centralbank.go.ke/monetary-policy/)).
- Tanzania's Bank of Tanzania displayed CBR 6.25% for Q4 2026 and annual
  inflation 4.3% for September 2026 ([BoT indicators](https://www.bot.go.tz/?lang=en)).
- The exact daily Uganda and Tanzania FX values, tax rates for all three
  countries, and current URSB/URA/sector licensing steps remain
  **NOT_ASSESSED** in the preparation. No such value is used in the synthetic
  financial case. Tax/accounting treatment remains with the accounting
  doctrine; current macro/market evidence remains with Digital Research.

The local [`country-market-data.json`](../../source-registers/country-market-data.json)
register contains 23 entries and was dated 2026-09-25; the baseline command
`python -B tools/evidence-register/refresh_evidence_register.py --check`
reports 10 overdue rows that still display `verified-current`. The
`--check-urls` probe reports retrieval failures for UBOS and KNBS TLS checks
and an HTTP 403 from UNBS. These are access/gate outcomes, not proof
that those issuers' content is false. The preparation source review lists the
affected row IDs and each status; no overdue row is renewed by this baseline
observation. The same-source official links above support only their stated
indicators.

The OpenAI changelog records GPT-6.1 Terra released on 26 October 2026
([official changelog](https://developers.openai.com/api/docs/changelog)); the
catalogue contains the GPT-6 model family ([official catalogue](https://developers.openai.com/api/docs/models)).
The local Codex cache at access time listed `gpt-6-luna` with `high` among its
supported reasoning levels, and the engine's Codex policy check passes. The
authorised Luna/high pin is retained; comparative quality, latency, cost, and
account entitlement remain **NOT_ASSESSED**. No paid call was made.

## Additional baseline defects and scope

1. **P0 — formula reconciliation false negative:** the synthetic mismatch
   passed because the formula-map observes workbook structure and cached
   values, not formula execution or a declared check result. Fixing this
   requires a deterministic reconciliation contract and matched/mismatched
   fixtures; a structural PASS must not be presented as recalculation.
2. **P1 — stale source state:** 10 overdue country-source records retain
   `verified-current`; a status lifecycle check is absent or incomplete.
3. **P1 — damaged retail-reference text:** a single non-tab control byte
   `0x01` interrupts the sentence in
   `skills/industry-guides/retail/references/retail-breakeven-benchmarks.md`
   at the text `The table below<control-byte>consolidates`. The intended
   reading is unambiguous from the surrounding sentence; only the control byte
   is eligible for repair.
4. **P2 — runtime catalogue truncation:** root-provided offline checks report
   a default Luna/high path list of 117/134, while the explicit
   `skills.max_context_tokens=10000` invocation lists 134/134. This is a
   tested runtime-configuration limitation, not an installation failure or a
   claim about every host.

The baseline code task outputs, run commands, counts, and limitations are
recorded in `00-practitioner-tasks.md`; the frozen numeric assessment is in
`01-baseline-scorecard.md`. Baseline measurements are from the unchanged
checkout and prepared logs, not post-change results.

# Local output-readiness review — 2026-09-06

The native checks pass for repository structure; the four fictional audience packs
remain **blocked for release**. Workbook calculation, native document/deck rendering,
professional acceptance and release authority are not established by those passes.
No readiness score or financial opinion is assigned.

Scope: this repository only, working-tree inspection against HEAD
`867b30f3a6af61923b42d1247a544e08ca79a309`. Local access/check date: 2026-09-06.
Evidence expires on relevant file changes. Main owns release-validator defensive
validation/tests and stale Digital Research paths; neither was repaired or retested
adversarially here. No network/source-currentness verification, other-engine work,
workbook writes, commits or publication occurred. This audit is the sole sidecar write.
The [local Kaizen skill](../../skills/meta-strategy/kaizen-improvement-system/SKILL.md)
and [adoption plan](../continuous-improvement/kaizen-adoption-2026-08.md) guided the
evidence/gap distinction; the explicit assignment excludes numerical grading.

## Native gate results

Commands ran from the repository root with `python -B -X utf8`; `-B` prevents
bytecode writes. No output-file or URL-probe options were used.

| Script and arguments | Observed result | Exit | What the pass establishes |
|---|---|---:|---|
| `scripts/source_ingestion_guardrail.py` | 0 findings | 0 | No match to the configured ebook, raw-path, size and full-text-marker rules; not a complete provenance/rights review. |
| `tools/evidence-register/refresh_evidence_register.py --check` | 10 entries; active jurisdictions covered | 0 | Required fields, dates, source IDs and jurisdiction links; no remote source or claim-support verification. |
| `tools/sector-gates/validate_sector_gates.py` | 12 sector families; 24 gates | 0 | Required gate fields and source-ID references; no competent-authority clearance. |
| `tools/exemplar-packs/validate_exemplar_packs.py` | 4 packs; 32 required artefacts | 0 | File/header/manifest structure, referenced base/report existence, committee status and blocked release declaration. |
| `scripts/build-financial-models/verify_workbooks.py` | 7/7 workbooks verified | 0 | ZIP readability, minimum size and expected sheet names/counts. |
| `tools/workbook-audit/formula_map.py` with all seven XLSX paths from `rg --files -g '*.xlsx'` | 7 pass; 0 findings each | 0 | Formula-text, sheet-reference and cached-error checks; no calculation engine. |
| Same formula-map command on `skills/pipeline/10-financial-projections/templates/saas-financial-projection-3yr-5yr.xlsx --require-scenarios --require-balance-checks` | Pass; 0 findings | 0 | Scenario/check text detected; no scenario execution or reconciliation-value assertion. |
| `tools/release-gate/validate_release_bundle.py examples/full-plan-packages/<pack>/release-bundle.json`, separately for all four packs | Each: `structurally valid; decision=blocked` | 0 each | A valid blocked record, not permission to release. |

The four pack names are `dfi-loan-uganda`, `grant-east-africa`,
`owner-manager-uganda` and `vc-east-africa`. These fresh checks supersede historical
gate counts for this review, without revising earlier audit records.

## Findings and next acceptance

| Finding and local evidence | Gap / next acceptance | Owner |
|---|---|---|
| **Preserve the release distinction.** [README capability map](../../README.md#capability-map), [pack instructions](../../examples/full-plan-packages/README.md) and all four release bundles distinguish scripts/templates from released outputs. Every committee result has `status=pass` with `recommendation=defer`; every render, design, document and authority state is `not-assessed`. Security is unassessed in three packs and explicitly not applicable in the owner-manager teaching pack. | Treat committee status as a simulation record. Retain blockers until final artefact identity, applicable receiver acceptance, render review and actual authority evidence satisfy the [release instructions](../quality-gates/business-plan-release-gate.md). | Pack/release owner |
| **Workbook passes are structural.** The seven-file read-only `audit_workbook` inventory found 4,385 formula cells; all cached values were `0`. The [retained projection report](../workbook-audits/saas-financial-projection-3yr-5yr.formula-map.json) records `Inputs!B6` as `IF(B5="Bull",1.25,IF(B5="Bear",0.75,1))` with cache `0`, although none of its branches returns zero. | Recalculate a controlled copy in the target spreadsheet application, retain application/version and file identity, reopen it, and check scenario outputs against independent expected results. This is a calculation-evidence gap, not a financial assessment. | Spreadsheet owner; financial judgement stays with the authorised reviewer |
| **Audience coverage exceeds demonstrated model execution.** All four `model-overlay.json` files reference one shared projection XLSX and one formula-map report. The exemplar validator checks overlay scenario/check counts and report existence; it does not apply the inputs or execute their required checks. Spreadsheet handoffs nevertheless say `pass` with empty caveats. | Keep that pass explicitly scoped to structure. Retain an overlay-to-input-cell map, applied scenario identity, recalculated outputs and review evidence for each relied-upon audience model. | Exemplar/spreadsheet owner |
| **Evidence links need more precision.** The [DFI committee record](../../examples/full-plan-packages/dfi-loan-uganda/committee-result.json) uses `formula-map.json:status=pass` for model integrity; its [manifest](../../examples/full-plan-packages/dfi-loan-uganda/committee-manifest.json) separately points to the real shared report. | Link criterion evidence directly to the actual report and workbook identity, with structural versus executed scope. The fictional score is not adopted by this audit. | Exemplar owner |
| **Source gates have bounded reach.** [Source ingestion](../../scripts/source_ingestion_guardrail.py) uses path/extension/size/marker heuristics; the evidence checker does not probe URLs without `--check-urls`, and the sector checker validates structure and source IDs. | Retain the clean ingestion result. Before an external claim or regulated conclusion is used, obtain separate claim-level verification and applicable authority evidence; neither is assessed here. | Source/sector owner in a separately authorised workflow |
| **Documented formula-map invocation differs from the CLI.** README/AGENTS show `--output`; the [existing parser](../../tools/workbook-audit/formula_map.py) supports `--json-out` and `--markdown-out`. | Reconcile the invocation in a later documentation change and verify `--help`; this sidecar used stdout only and changed no tooling. | Maintainer |

## README output-family coverage

This covers the [capability map and routing table](../../README.md), including their
planning variants. It records inspected exemplars and gaps, not exhaustive skill-body
grading. Filename inventory of tracked native outputs found seven XLSX files and no
DOCX, PDF or PPTX; repository searches likewise found no native document/deck outputs.

| Output family / route | Inspected evidence and next acceptance |
|---|---|
| Full plans, decision packs, lender/investor/owner cases | Four ten-section LakeLink plans, four deck scripts and manifests; retain a complete versioned engagement pack with accepted evidence. |
| Feasibility / business cases | Owner-manager plan compares hire, contractor and hold choices; standalone feasibility acceptance and independently tested alternatives are not demonstrated. |
| Market analysis / validation | DFI section 3 and VC sections 3–4 specify customer/cohort evidence and a sizing method; actual interviews, observations and claim support remain absent from these fictional packs. |
| Build-Measure-Learn / living plans | Grant sections 5 and 9 describe learning and adaptive decisions; retain a completed experiment, observed result, decision change and subsequent review. |
| Nonprofit strategy / grant planning | Grant plan includes beneficiaries, theory of change, MEL and safeguards; retain stakeholder/governance acceptance and an observed baseline-to-review cycle. |
| Facility moves / major operating change | README defines the route; no dedicated completed move/cutover evidence was identified in the exemplar inventory. Retain readiness, go/no-go, fallback and stabilisation records. |
| M&E / quarterly execution / dashboards | Grant MEL prose, owner-manager cadence and a native KPI workbook exist; retain populated definitions, data-quality checks, review decisions and follow-up evidence. |
| Financial projections / planning workbooks | Seven structural passes; calculation, model reconciliation and professional fitness remain outside the proven scope. See workbook findings above. |
| SaaS / recurring-revenue planning | Shared SaaS templates and VC cohort requirements exist; retain versioned inputs and executed cohort/scenario evidence. |
| AI-enabled business planning | AI cost and agent workbook templates exist; no completed AI business-case evaluation, oversight or drift record appears in the four packs. |
| Digital transformation | README supplies the route; LakeLink describes digital services, not a completed client transformation. Retain maturity baseline, adoption and benefits-review evidence. |
| Pitch / presentation | Four Markdown scripts; native PPTX generation, opening, rendering and visual QA remain NOT ASSESSED. |
| DOCX / PDF delivery | No tracked native artefact; retain final editable/export files, readback, pagination/accessibility and rendered-page review. |
| Proposal / tender / EOI / RFP | README explicitly hands off to Proposal Skills. The grant teaching pack does not demonstrate that receiver's acceptance; retain a scoped accepted handoff when applicable. |
| External release | Four correctly blocked bundles. Reassess only after mandatory evidence and authority are supplied under the [cross-engine contract](../../references/cross-engine-delivery-contract.md). |

Re-audit after main integrates its validator/path changes, and before any output
family is promoted beyond these evidence states. Manual editorial review: no
blocking unsupported claim found in this audit; counts are command-backed and
gaps are explicit. Automated genericness scoring, live agent behaviour, visual QA,
client outcomes and professional/authority acceptance remain NOT ASSESSED.

## CLI mismatch disposition — 2026-09-06

Closed the demonstrated `--output` mismatch in a separately authorised repair.
`tools/workbook-audit/formula_map.py` now accepts `--output` as an alias for
`--json-out`, using the same `json_out` destination. Existing options and audit
logic remain unchanged; no financial calculation or host recalculation was added.

`tests/test_formula_map.py` reuses the existing temporary broken-workbook fixture
through a shared helper. Its subprocess regression compares both JSON flags with
the expected report, checks simultaneous `--markdown-out` output, preserves the
expected audit-failure exit, and verifies that the input bytes remain unchanged.
All generated fixture/report files stay inside `TemporaryDirectory`.

Before the parser repair, the new regression failed because `--output` returned
argument-error exit 2. Afterward, `python -B -X utf8 -m unittest
tests.test_formula_map` passed all three tests (exit 0); both fixture CLI runs
returned the expected audit-failure exit 1 and wrote matching reports. CLI
`--help` lists both JSON flags and the existing options. Scoped `git diff --check`
passed. All seven production XLSX SHA-256 hashes and modification times matched
the pre-test snapshot. Only the script, its test module and this disposition were
changed by this repair. All other readiness findings remain open as recorded.

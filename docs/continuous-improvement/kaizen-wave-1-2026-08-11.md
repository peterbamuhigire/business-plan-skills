# Business Plan Skills: Kaizen Wave 1 Report

Assessment date: 2026-08-11
Repository: `C:\wamp64\www\business-plan-skills`
Owner: Peter Bamuhigire / Codex Wave 1 worker
Scope: P0 route and output-truth repairs plus one bounded P1 contract and ingestion-evidence improvement
Re-audit date: 2026-08-18 for Wave 1 reliability; 2026-08-25 for the next behavioural review

## Result in one paragraph

The repository started from a clean `main` worktree aligned with
`origin/main`. Wave 1 repaired stale high-use route references in the living
plan, AI-integration, bankability, root operating-model, and AGENTS surfaces;
added a deterministic route/link check; qualified README output claims by
evidence state; removed the duplicated contract surface from the single
selected high-use AI skill; and added tests for route resolution, contract
heading uniqueness, and raw extraction detection. Structural validation,
routing, workbook, exemplar, evidence-register, sector-gate, targeted skill
validation, unit tests, and diff checks pass. The strengthened source-ingestion
guardrail exits non-zero because it now detects three pre-existing raw
extraction files. That is an intentional safety finding, not a pass and not a
finding to hide in this wave.

## Baseline inventory, score, and maturity

The assignment baseline records 126 active skills, 126/126 contract checks,
38/38 routing fixtures, 14 unit tests, and 7 workbook checks; it records a
56.94 raw diagnostic score, a published Wave 1 ceiling of 55, and maturity L3
(`defined`, with important outcome proof incomplete). These values are taken
from the supplied initial assessment and the repository baseline file; the
assignment cap is not written into the repository's permanent 65-point policy.

- Baseline assessment: `C:\wamp64\www\KAIZEN-INITIAL-ASSESSMENT.md`
- Machine count and zero-debt baseline: [`docs/quality/skill-quality-baseline.json`](../quality/skill-quality-baseline.json)
- Permanent repository cap: [`README.md`](../../README.md#the-kaizen-operating-contract)
- Baseline source-ingestion result: `scripts/source_ingestion_guardrail.py`, 0 findings before this change

The initial assessment records 76 of 126 skills with duplicated H2 contract
headings. Wave 1 deliberately does not bulk-edit that catalogue. The selected
normalisation target is `skills/pipeline/14-ai-integration/SKILL.md`, where the
five duplicated contract headings were removed and the portable contract was
kept as the single canonical surface.

## Changes implemented

### P0-08: repair high-use routes and qualify output evidence

| Required field | Wave 1 record |
|---|---|
| Gap | High-use living-plan, AI-integration, and bankability references pointed at pre-`pipeline` or pre-category paths. README wording presented broad output capability without separating generated, validated, rendered, and release evidence. Evidence: stale paths in the affected files and the baseline assessment's P0-08 finding. |
| Root cause | Directory reorganisation changed the filesystem, but route prose and output claims were not checked against filesystem truth. Structural presence was treated as stronger proof than artefact evidence. |
| Exact change | Updated route references in [`meta-living-plan-governance/SKILL.md`](../../skills/meta-strategy/meta-living-plan-governance/SKILL.md), [`14-ai-integration/SKILL.md`](../../skills/pipeline/14-ai-integration/SKILL.md), [`meta-bankability-scoring/SKILL.md`](../../skills/meta-finance/meta-bankability-scoring/SKILL.md), [`living-business-plan-operating-model.md`](../../living-business-plan-operating-model.md), and [`AGENTS.md`](../../AGENTS.md). Replaced the README output list with an evidence-state table in [`README.md`](../../README.md). |
| Hypothesis | If route references resolve from the current filesystem and output claims name their proof state, a fresh agent will reach the intended route and will not infer render, accessibility, client, or release proof from a Markdown or template file. |
| Owner | Repository maintainer / business-plan engine owner. |
| Measure | Route-link failures; top-three routing precision; structural and targeted skill validation; explicit README states. |
| Risk | Correcting paths may expose intended future routes that were never implemented. Qualifying output claims may appear narrower to users until native artefact evidence exists. Cross-engine handoff names can drift again after directory changes. |
| Rollback | Revert only the route-reference and README hunks if a route fixture regresses; retain the route checker and restore the previous wording only after its evidence is re-established. |
| Acceptance evidence | [`scripts/routing_link_check.py`](../../scripts/routing_link_check.py) reports 0 failures across 7 configured surfaces after the report file exists; [`scripts/routing_smoke_test.py`](../../scripts/routing_smoke_test.py) reports 40/40 top-three matches; the structural validator reports 126/126 compliant. |
| Standardisation | The route checker is a repository script and unit test, with the high-use surface list kept explicit. README claims now use `Generated`, `Validated`, `NOT ASSESSED`, and `BLOCKED` states. |
| Re-audit | 2026-08-18, then after any directory relocation. |

### P1-07: bounded contract normalisation

| Required field | Wave 1 record |
|---|---|
| Gap | The selected high-use `14-ai-integration` skill repeated `Required Inputs`, `Workflow`, `Anti-Patterns`, `Outputs`, and `References` H2 headings, creating two competing contract surfaces. The initial assessment records 76/126 affected skills; Wave 1 is intentionally limited to this routed cluster. |
| Root cause | A legacy domain body and a later portable contract were appended instead of being merged into one ordered skill surface. |
| Exact change | Removed the duplicated legacy contract blocks from [`skills/pipeline/14-ai-integration/SKILL.md`](../../skills/pipeline/14-ai-integration/SKILL.md), retained its domain workflow and references, kept one portable contract block, and renamed the capability heading to `Capability Contract` for the repository's canonical validator. |
| Hypothesis | If one routed skill has one contract heading for each required contract, retrieval ambiguity will fall without changing the domain route or its substantive AI planning guidance. |
| Owner | Repository maintainer / business-plan engine owner. |
| Measure | Selected heading count before/after; quick validation; full contract validator; routing smoke fixtures. |
| Risk | Removing duplicated prose could remove a domain rule if the two blocks were not equivalent. The patch was limited to the legacy contract blocks; the long domain content and detailed references remain. |
| Rollback | Restore only the removed blocks if a targeted prompt or validation check shows lost domain behaviour; do not expand the edit to the remaining 75 recorded skills in this wave. |
| Acceptance evidence | The targeted test asserts one each of the five contract headings plus one `Capability Contract`; quick validation passes; the full validator remains 126/126 with zero failure counts; routing remains 40/40. |
| Standardisation | The test in [`tests/test_routing_links.py`](../../tests/test_routing_links.py) makes the bounded normalisation rule executable without declaring the wider catalogue normalised. |
| Re-audit | 2026-08-25 with a fresh retrieval/route review before selecting another cluster. |

### P1 source-ingestion evidence: raw extraction paths

| Required field | Wave 1 record |
|---|---|
| Gap | The source guardrail returned 0 findings while tracked raw material existed below `skills/industry-guides/_extraction/`; its path pattern did not cover `_extraction`. |
| Root cause | Detection depended on file size and a narrow set of directory names. A raw extraction path with a smaller Markdown file could pass unnoticed. |
| Exact change | Added `RAW_EXTRACTION_PATH_RE` and a `raw-extraction-path` finding to [`scripts/source_ingestion_guardrail.py`](../../scripts/source_ingestion_guardrail.py). Added temporary, test-labelled fixtures for `_extraction`, a concise `book-extractions` synthesis path, and a raw ebook extension in [`tests/test_source_ingestion_guardrail.py`](../../tests/test_source_ingestion_guardrail.py). |
| Hypothesis | If raw extraction directories are rejected by path before size or marker heuristics, the guardrail will fail closed for the known raw route and will not confuse a small test fixture with an approved synthesis. |
| Owner | Repository maintainer, with source-rights review by the domain owner. |
| Measure | Temporary-fixture detection and root scan findings; the root scan must be treated as a release blocker while findings remain. |
| Risk | Existing raw source files are now visible as blockers. Suppressing or allowlisting them would weaken the source-ingestion policy and could retain reconstructive source content. |
| Rollback | Revert the new path rule only if it produces a demonstrated false positive against a concise, attributed synthesis path; keep the temporary tests and add a narrower reviewed pattern. Do not delete or rewrite the three existing source files without a separate provenance and distillation decision. |
| Acceptance evidence | Targeted source-ingestion tests pass. The full root scan reports exactly three findings: `skills/industry-guides/_extraction/agriculture-raw.md`, `skills/industry-guides/_extraction/services-other-raw.md`, and `skills/industry-guides/_extraction/trade-manufacturing-raw.md`; exit state is 1. This is detection evidence, not a release pass. |
| Standardisation | The path rule and tests are now discoverable in the source guardrail and its test module. The three findings remain an owned remediation item rather than being converted into a false green result. |
| Re-audit | 2026-08-25 after a documented distillation/removal decision. |

## Before and after measures

| Measure | Before | After Wave 1 | Interpretation |
|---|---:|---:|---|
| Active skills / contract validator | 126 / 126, zero failure counts | 126 / 126, zero failure counts | No structural regression. Source: [`validate_skill_engine.py`](../../scripts/validate_skill_engine.py) and [`skill-quality-baseline.json`](../quality/skill-quality-baseline.json). |
| Routing fixtures | 38/38 top-three matches | 40/40 top-three matches | Two positive fixtures now exercise living-plan and AI-integration routes; source: [`tests/routing-fixtures.json`](../../tests/routing-fixtures.json). |
| High-use route/link surfaces | No deterministic route-link gate | 7 surfaces, 0 failures | Stale route references are now checked by [`routing_link_check.py`](../../scripts/routing_link_check.py). |
| Selected AI contract headings | 5 duplicated H2 headings in one selected skill | 0 duplicated headings; one each retained | Bounded P1 normalisation only; the wider 76/126 catalogue finding remains open. |
| Source-ingestion path coverage | 0 findings, with `_extraction` missed | 3 raw-extraction findings, exit 1 | Detection improved; repository safety remains blocked until the existing raw files are resolved. |
| Unit tests | 14 tests | 19 tests, all passing | Five deterministic tests were added for route links, heading uniqueness, raw extraction paths, synthesis-path handling, and raw ebook rejection. Source: [`tests/`](../../tests/). |
| Workbook checks | 7 workbook validations | 7 workbook validations pass | No workbook content changed; source: [`verify_workbooks.py`](../../scripts/build-financial-models/verify_workbooks.py). |

## Validation commands and retained results

Commands were run from `C:\wamp64\www\business-plan-skills` in PowerShell.
Exit states are retained here; no unavailable check is represented as passed.

| Command | Result | Exit |
|---|---|---:|
| `python -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` | 126 active, 3 templates, 126 fully compliant, zero failure counts | 0 |
| `python -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py skills/pipeline/14-ai-integration` | Skill is valid | 0 |
| `python -X utf8 scripts/routing_link_check.py` | 7 surfaces; 0 failures | 0 |
| `python -X utf8 scripts/routing_smoke_test.py --threshold 1.0` | 40/40 top-three matches; 100.0% | 0 |
| `python -X utf8 -m unittest tests.test_routing_links tests.test_source_ingestion_guardrail` | 5 targeted tests passed | 0 |
| `python -X utf8 -m unittest discover -s tests -p "test_*.py"` | 19 tests passed | 0 |
| `python -X utf8 tools/evidence-register/refresh_evidence_register.py --check` | 10 evidence-register entries; active jurisdictions covered | 0 |
| `python -X utf8 tools/sector-gates/validate_sector_gates.py` | 12 sector families and 24 regulatory gates | 0 |
| `python -X utf8 tools/exemplar-packs/validate_exemplar_packs.py` | 4 fictional audience packs; 32 required artefacts | 0 |
| `python -X utf8 scripts/build-financial-models/verify_workbooks.py` | All 7 tracked workbooks verified | 0 |
| `python -X utf8 scripts/source_ingestion_guardrail.py` | 3 pre-existing raw extraction findings listed above | 1 |
| `git diff --check` | No whitespace errors | 0 |

The source-ingestion exit 1 is the only intentional post-change failing gate.
It exposes pre-existing content that the baseline scan did not recognise. No
validator, fixture, or test was weakened, skipped, or deleted to create a pass.

## Remaining backlog

### P0

- Resolve the three raw extraction files through a separately approved source
  distillation/removal action with provenance and rights review. Until then,
  keep the source-ingestion gate blocked.
- Do not claim native PPTX, DOCX, PDF, render, accessibility, or external
  release evidence. The README now records these states as `NOT ASSESSED` or
  `BLOCKED`.

### P1

- Extend contract normalisation only after the 2026-08-25 re-audit demonstrates
  that the selected AI edit improved retrieval without changing domain output.
- Add a semantic claim-support fixture for business-plan evidence; the current
  route and structural gates do not prove that a cited source supports every
  assembled claim.
- Add a small fictional plan-behaviour fixture for missing inputs, an
  unassessed handoff, and a blocked release decision.

### P2

- Replace manually repeated catalogue counts with a single generated report
  where useful; the baseline file remains the current count source.
- Measure native document and render evidence only when the required tooling and
  real artefacts are supplied.
- Review remaining duplicated contract headings by route risk, not by file-count
  target, and stop if extra splitting or editing increases retrieval cost.

## NOT ASSESSED and evidence boundaries

- Native PPTX, DOCX, and PDF generation, reopenability, rendering, accessibility,
  pagination, font behaviour, and visual inspection: **NOT ASSESSED**; no tracked
  native artefact was present in the repository baseline.
- Client-specific market, country, funding, regulatory, tax, legal, accounting,
  reviewer, or release-authority evidence: **NOT ASSESSED**; the repository's
  fictional exemplar data cannot certify a client engagement.
- Production performance, field outcomes, and bank or investor acceptance:
  **NOT ASSESSED**.
- Semantic support of every current external claim: **NOT ASSESSED** beyond the
  changed route and source-ingestion checks.
- Actual Claude, Codex, or generic-agent runtime instruction loading:
  **NOT ASSESSED**. The repository files provide the portable contract, but a
  vendor runtime smoke test was not executed in this Wave 1 worker.

## Compatibility

Canonical reusable logic remains in `SKILL.md`; the edited AI skill declares
portable compatibility with `claude-code` and `codex`. `AGENTS.md` remains the
model-neutral repository guide, and `CLAUDE.md` remains the repository's Claude
controller. No model-specific skill logic was copied into the canonical skill.
For a generic agent without automatic instruction discovery, the documented
fallback is to read `AGENTS.md`, `README.md`, and the selected `SKILL.md`
directly. Actual vendor discovery and generic-agent behaviour remain
**NOT ASSESSED** as stated above.

## Unrelated or pre-existing changes

The baseline worktree was clean before editing. All worktree changes listed in
this report belong to this Wave 1 patch. No sibling repository, workspace-level
report, commit, push, fetch, pull, reset, or broad deletion was performed.

## Next-wave recommendations

1. Resolve the three raw extraction findings with an explicit source-rights and
   distillation record before changing the guardrail back to a passing state.
2. Re-run the route/link and 40-fixture routing checks from a fresh context after
   the directory tree changes next.
3. Use a single fictional behavioural benchmark that exercises missing inputs,
   evidence labels, financial handoff, and blocked release without claiming
   client or production proof.
4. Select the next contract-normalisation batch only from routing and retrieval
   evidence. Do not edit the remaining duplicated headings in bulk.
5. When native artefacts and tools are available, add separate generated,
   validated, reopened, rendered, accessibility-reviewed, and release-authorised
   states rather than collapsing them into one checklist.

## Required files and execution availability

All nine mandatory input files named in the assignment were available and read:
the master prompt, initial assessment, standards register, repository
controllers, and the five required skill guidance files. No required file was
unavailable. The Linux-only or native Office render environment was not needed
for this bounded patch and remains **NOT ASSESSED**.

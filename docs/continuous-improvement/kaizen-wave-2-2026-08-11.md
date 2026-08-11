# Business Plan Skills: Kaizen Wave 2 Report

Assessment date: 2026-08-11
Repository: `C:\wamp64\www\business-plan-skills`
Owner: Repository maintainer / Codex Wave 2 auditor
Scope: Wave 2 P0 source-ingestion closure, guardrail challenge, and route-boundary review
Re-audit date: 2026-08-25
Status: P0 source-ingestion findings cleared; native rendering remains **NOT ASSESSED**

## Result

The three Wave 1 source-ingestion blockers are closed without weakening the
guardrail. Each tracked raw extraction was inspected before removal. Existing
sector references retained the useful guidance for the mapped profiles. Four
narrow gaps were not represented by a current reference, so four concise,
independently written, attributed syntheses were added in the owning sector
directories. The raw tables and reconstructed source text were not relocated.

The final repository scan reports zero source-ingestion findings and exits 0.
The pre-remediation scan is retained as explicit evidence: it reported the
three raw paths and exited 1. The earlier Wave 1 structural and behavioural
gates still pass, and the new adversarial controls reject a case-variant raw
path, a renamed large full-text file, and a local route that escapes the
repository root.

No claim is made about native PPTX, DOCX, or PDF generation, reopening,
rendering, pagination, accessibility, or production release. Those stages are
still **NOT ASSESSED**.

## Fresh re-audit findings

### Wave 1 challenge and result

Wave 1 correctly treated the source-ingestion exit 1 as a blocker rather than
allowlisting the three files. A fresh run before this edit reproduced exactly
those three findings in:

- `skills/industry-guides/_extraction/agriculture-raw.md`
- `skills/industry-guides/_extraction/services-other-raw.md`
- `skills/industry-guides/_extraction/trade-manufacturing-raw.md`

The first Wave 1 run therefore remains valid detection evidence, not a failed
implementation to hide. The independent content review found that the files
were extracted source material containing profile tables, incomplete fields,
historical assumptions, and source text. Their useful planning themes were
checked against the existing industry-reference catalogue.

The fresh review also challenged the Wave 1 route checker. Its resolver tested
whether a referenced path existed, but did not reject a relative link that
resolved outside the repository root. That was a real boundary defect. The
checker now fails such a link, while HTTP(S), mail, and fragment links remain
outside the local-file check.

### Source-to-guidance disposition

| Inspected source | Disposition before removal | Wave 2 representation | Evidence boundary |
| --- | --- | --- | --- |
| Agriculture extraction | Existing livestock, food-processing, textiles, construction, agriculture, and retail references represented the mapped operating themes. Grain grocery and dried oyster mushrooms were distinct gaps. | [`grain-grocery.md`](../../skills/industry-guides/retail/references/grain-grocery.md) and [`oyster-mushroom-drying.md`](../../skills/industry-guides/agriculture/references/oyster-mushroom-drying.md) | Historical source tables are not current market or financial evidence. |
| Services and other sectors extraction | Existing service, hospitality-tourism, education-social, construction, and chemicals references represented the operating themes found during review. No additional distinct synthesis was needed. | No new file; existing references remain the source-of-truth guidance. | Profile-level source figures remain historical and are not promoted by this removal. |
| Trade and manufacturing extraction | Existing manufacturing, textiles, chemicals, construction, mining, hospitality, and services references represented the mapped operating themes. Water distillation and PTFE-coated cookware were distinct gaps. | [`water-distillation.md`](../../skills/industry-guides/food-processing/references/water-distillation.md) and [`ptfe-coated-cookware.md`](../../skills/industry-guides/manufacturing-light/references/ptfe-coated-cookware.md) | Current quality, safety, market, and regulatory requirements remain gaps until verified for the intended use and jurisdiction. |

The four new references state their source attribution, independent-synthesis
boundary, existing adjacent guidance, and missing current evidence. They omit
the source financial tables because the inspected source does not by itself
establish present-day viability.

### Removed-content recovery

The removed paths were tracked at the Wave 2 starting point. Their Git object
identifiers were checked before handoff:

| Removed path | `HEAD` blob checked | Current path |
| --- | --- | --- |
| `skills/industry-guides/_extraction/agriculture-raw.md` | `0017a6ea1ccb59b4aac0a82280beefd99692aaee` | absent |
| `skills/industry-guides/_extraction/services-other-raw.md` | `49b94ed70b38fd86cab594e44ffabb1a01485e89` | absent |
| `skills/industry-guides/_extraction/trade-manufacturing-raw.md` | `9e347ed70b38fd86d7954a28eb1465d2555834a` | absent |

The removed tracked content remains recoverable from Git history with
`git show HEAD:<path>` or a repository history review. It is not copied under
another name in this repository.

## Exact Wave 2 files

Wave 1 files were preserved. Wave 2 changed only these repository-local paths:

- `scripts/source_ingestion_guardrail.py`
- `scripts/routing_link_check.py`
- `tests/test_source_ingestion_guardrail.py`
- `tests/test_routing_links.py`
- `skills/industry-guides/_extraction/agriculture-raw.md` (deleted)
- `skills/industry-guides/_extraction/services-other-raw.md` (deleted)
- `skills/industry-guides/_extraction/trade-manufacturing-raw.md` (deleted)
- `skills/industry-guides/agriculture/references/oyster-mushroom-drying.md`
- `skills/industry-guides/food-processing/references/water-distillation.md`
- `skills/industry-guides/manufacturing-light/references/ptfe-coated-cookware.md`
- `skills/industry-guides/retail/references/grain-grocery.md`
- `docs/continuous-improvement/kaizen-wave-2-2026-08-11.md`

No workspace-level report, sibling repository, commit, push, fetch, pull,
reset, or publish operation was performed.

## Wave 2 action records

### W2-P0-01 — Distil useful guidance and remove tracked raw paths

| Required field | Wave 2 record |
| --- | --- |
| Gap | Source-ingestion detection found three tracked raw extractions. Useful guidance could be lost if removal happened without profile mapping. Evidence: the pre-remediation guardrail exit 1 and the three inspected `HEAD` blobs above. |
| Root cause | Source extraction, source tables, and reusable sector guidance were stored together; the first-wave guardrail exposed the path but did not yet perform the distillation decision. |
| Change | Removed the three `_extraction` files. Added four concise references at the exact paths listed above. Existing references were retained for the mapped services and other profiles. |
| Hypothesis | If useful operational logic is retained only in concise, attributed, sector-owned references, the guardrail can stay fail-closed without losing discoverable planning guidance or preserving reconstructive source text. |
| Owner | Business-plan engine maintainer; domain owner reviews source attribution and current applicability before client use. |
| Measure | Final source-ingestion findings 0, final exit 0; four synthesis files exist and contain attribution plus an explicit raw-content boundary; no `_extraction` path remains. |
| Risk | A profile may contain a useful detail that the catalogue mapping missed. The new references may also be mistaken for current market, financial, or regulatory authority. |
| Rollback | Recover an individual removed blob from Git history, inspect the specific omission, and write a narrower attributed synthesis. Do not restore raw source into the working tree or rename it to bypass the guardrail. |
| Acceptance evidence | `scripts/source_ingestion_guardrail.py` reports `findings: 0` and exits 0; the provenance test passes; the four references are independently written and gap-labelled; the old blobs are recoverable by `git show`. |
| Standardisation | The source guardrail, provenance test, and reference-file boundary now make source distillation a release step. Future source additions must enter as concise, attributed synthesis in the owning reference directory. |
| Re-audit | 2026-08-25, then before any new source extraction is retained. |

### W2-P0-02 — Attack and harden source-ingestion matching

| Required field | Wave 2 record |
| --- | --- |
| Gap | The known `_extraction` path was blocked, but the Wave 1 test did not exercise the plural or case-variant `_EXTRACTIONS` form, and a renamed large full-text file needed an independent negative control. |
| Root cause | The path matcher encoded the observed singular directory but its variant coverage and content-marker fallback were not tested adversarially. |
| Change | Extended `RAW_EXTRACTION_PATH_RE` to cover `_extraction` and `_extractions` case-insensitively. Added tests for the variant path, a large full-text file moved to an apparently approved path, and concise synthesis allowance under `book-extractions`. |
| Hypothesis | If both path variants and the content-marker fallback are exercised, simple renaming and case changes will not turn reconstructive source material into a false green result, while concise synthesis remains usable. |
| Owner | Business-plan engine maintainer. |
| Measure | Targeted guardrail tests pass; the full repository guardrail remains zero; expected negative cases remain blocking assertions rather than skipped tests. |
| Risk | A broad path pattern could reject a legitimate concise reference. The `book-extractions` concise-synthesis test is retained as the false-positive control. |
| Rollback | Revert only the regex widening if a demonstrated legitimate path is rejected, then add the smallest reviewed pattern and a regression fixture. Never remove the raw-content fallback. |
| Acceptance evidence | `python -X utf8 -m unittest tests.test_source_ingestion_guardrail tests.test_routing_links` exits 0; the test suite records raw-path and full-text rejection; final guardrail scan exits 0. |
| Standardisation | Keep path, extension, size, and marker checks as separate layers. Every future bypass report must become a deterministic fixture with an explicit expected block or allow outcome. |
| Re-audit | 2026-08-25, with any new extraction naming convention. |

### W2-P0-03 — Prevent route references escaping the repository

| Required field | Wave 2 record |
| --- | --- |
| Gap | The Wave 1 route checker could accept a local relative link when the target existed outside the repository root. This allowed a route surface to appear resolved without proving repository-local ownership. |
| Root cause | `_resolve` normalised the path and checked existence, but `scan` did not check containment against the resolved repository root. |
| Change | `scripts/routing_link_check.py` now reports `resolves outside repository` for resolved local targets outside the scan root. `tests/test_routing_links.py` adds an explicit traversal fixture. |
| Hypothesis | If route validation checks both existence and containment, path traversal or sibling-workspace references cannot masquerade as portable repository routes. |
| Owner | Business-plan engine maintainer. |
| Measure | Default high-use scan has 0 failures; the escape-path fixture produces one expected failure inside the test; the 40-fixture top-three routing smoke remains green. |
| Risk | An intentional local handoff to a separately owned repository would now be rejected by this repository-local check. Such a handoff must use an explicit cross-engine contract, not an implicit relative path. |
| Rollback | Revert only the containment branch if an approved local route is proven necessary, and replace it with an explicit cross-engine route contract and ownership record. |
| Acceptance evidence | `python -X utf8 scripts/routing_link_check.py` exits 0 on repository surfaces; the traversal test passes; `python -X utf8 scripts/routing_smoke_test.py --threshold 1.0` remains 40/40 with exit 0. |
| Standardisation | Route checks now prove filesystem existence and repository ownership separately from routing relevance. The normalisation test for the selected AI skill remains in the suite. |
| Re-audit | 2026-08-25 and after future route or directory changes. |

## Before, Wave 1, and Wave 2 measures

| Measure | Before Wave 1 | After Wave 1 | After Wave 2 | Evidence |
| --- | --- | --- | --- | --- |
| Source-ingestion root scan | 0 findings, exit 0, but `_extraction` was missed | 3 findings, exit 1 | 0 findings, exit 0 | Wave 1 report; `scripts/source_ingestion_guardrail.py`; retained pre-remediation exit 1 |
| Tracked raw extraction paths | 3 present | 3 present and visible blockers | 0 present | `git cat-file -e HEAD:<path>` and current-path checks |
| Active skills / structural contract | 126 / 126 | 126 / 126 | 126 / 126 | `scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json`, exit 0 |
| Routing fixtures | 38/38 top-three matches | 40/40 top-three matches | 40/40 top-three matches | `scripts/routing_smoke_test.py --threshold 1.0`, exit 0 |
| Unit tests | 14 | 19 | 23 | `python -X utf8 -m unittest discover -s tests -p "test_*.py"`, exit 0 |
| Source-gap syntheses for the four newly identified gaps | Not assessed | No retained source-gap synthesis | 4 attributed references | `tests/test_source_ingestion_guardrail.py`, provenance test, exit 0 |
| Repository-root route containment | Not assessed | Not assessed | Traversal negative control rejects outside target | `tests/test_routing_links.py`, targeted suite exit 0 |

The supplied Wave 1 reports retain the baseline raw diagnostic score of 56.94
and Wave 1 diagnostic raw score of 63.0, with the exercise-published score
capped at 55. This bounded Wave 2 audit does not invent a replacement weighted
score from test counts. The 95 target remains unawarded; native artefact,
semantic claim-support, human review, system, production, and longitudinal
outcome evidence are not established here.

## Commands and exits

The following results were run from the repository root. Exit states are
retained; a negative control is not silently converted into a pass.

| Command | Result | Exit |
| --- | --- | ---: |
| `python -X utf8 scripts/source_ingestion_guardrail.py` before removal | Three known raw-extraction findings; expected Wave 1 blocker | 1 |
| `python -X utf8 -m unittest tests.test_source_ingestion_guardrail tests.test_routing_links` | Source, route, provenance, and traversal controls passed | 0 |
| `python -X utf8 -m unittest discover -s tests -p "test_*.py"` | 23 tests passed | 0 |
| `python -X utf8 scripts/source_ingestion_guardrail.py` after removal | `findings: 0` | 0 |
| `python -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` | 126 active; 126 fully compliant; zero failure counts | 0 |
| `python -X utf8 scripts/routing_link_check.py` | 7 surfaces; 0 failures | 0 |
| `python -X utf8 scripts/routing_smoke_test.py --threshold 1.0` | 40/40 top-three matches | 0 |
| `python -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py skills/pipeline/14-ai-integration` | Skill valid; Wave 1 normalisation preserved | 0 |
| `python -X utf8 tools/evidence-register/refresh_evidence_register.py --check` | 10 evidence-register entries; active jurisdictions covered | 0 |
| `python -X utf8 tools/sector-gates/validate_sector_gates.py` | 12 sector families; 24 regulatory gates | 0 |
| `python -X utf8 tools/exemplar-packs/validate_exemplar_packs.py` | 4 complete fictional audience packs; 32 required artefacts | 0 |
| `python -X utf8 scripts/build-financial-models/verify_workbooks.py` | All 7 tracked workbooks verified | 0 |
| `git diff --check` | No whitespace errors | 0 |

The four new references are not active `SKILL.md` files, so the active-skill
count does not change. No existing test was weakened, skipped, deleted, or
removed to obtain these results.

## Safety audit

Safety status: **Safe for the changed Wave 2 surfaces**, with explicit evidence
boundaries.

Inspected surfaces: the changed Python scripts, their tests, all four new
references, the three deleted raw blobs at `HEAD`, the repository controllers,
and the final source-ingestion scan.

Findings:

- No new installer, package, remote script, credential request, secret
  collection, upload, exfiltration, reverse shell, or hidden system action was
  added.
- The marker text in the renamed-full-text test is deliberate fixture data for
  the guardrail and does not execute or leave a source file in the repository.
- The three raw extracts were removed rather than renamed or moved.
- The four references are concise, attributed, independently written, and do
  not reproduce the source tables.
- Current quality, market, safety, regulatory, and financial claims that the
  inspected source cannot establish are labelled **gaps**.

Required action: retain the source guardrail and review any future source
distillation through the same provenance and rights boundary. No safety finding
requires a code change in this wave.

## Anti-slop review

Manual anti-slop status: **no blocking finding in the changed artefacts**.

- No new statistic, market size, forecast, credential, organisation, URL, or
  direct quote was invented.
- Source titles and profile locations in the four references are attribution
  points, not claims that the historical source is current authority.
- Historical financial tables were intentionally omitted instead of being
  reused as filler or presented as current evidence.
- Each new reference contains a concrete operating workflow, a boundary, and
  a named evidence gap.
- The changed scripts and tests contain executable negative controls rather than
  prose-only assurance.

The automated `ai-slop-audit` skill was not executed in this repository-local
Wave 2 patch; its runtime verdict is **NOT ASSESSED**. The manual review does
not substitute for that unavailable execution.

## Portability status

| Agent surface | Status | Evidence and limit |
| --- | --- | --- |
| Claude | Structural/manual only | `CLAUDE.md` remains the repository controller and canonical skill content remains provider-neutral. Actual Claude runtime discovery was not executed. |
| Codex | Structural/manual only | `AGENTS.md` and `SKILL.md` remain the model-neutral contract surfaces. Actual Codex runtime discovery was not executed. |
| Generic agent | Manual fallback available | A generic runner can read `AGENTS.md`, `README.md`, the selected `SKILL.md`, and the linked reference. There is no universal automatic instruction-file mechanism; runtime behaviour is **NOT ASSESSED**. |

No vendor-specific logic was added to the four references or the Python
guardrails. The route and source checks are repository-local and portable to an
agent that can read files and run Python.

## Residual P0, P1, P2, and NOT ASSESSED states

### P0

- **Closed:** three raw source-ingestion findings; final guardrail findings are
  zero and the raw paths are absent.
- **Open evidence boundary:** native PPTX/DOCX/PDF generation, reopening,
  rendering, accessibility, pagination, font behaviour, and visual inspection
  remain **NOT ASSESSED**. No README or report claim was promoted because of
  this source-ingestion fix.

### P1

- The wider duplicated-contract-heading finding remains open; Wave 2 did not
  perform a catalogue-wide normalisation.
- Semantic support of every cited business-plan claim remains **NOT ASSESSED**;
  the new references do not prove current source support.
- A fictional end-to-end business-plan behaviour fixture for missing inputs,
  evidence labels, finance handoff, and blocked release remains open.
- Actual client, lender, investor, bank, grant, reviewer, and release-authority
  acceptance remains **NOT ASSESSED**.

### P2

- Continue source-register currency review for mutable market, standards,
  regulatory, and platform claims through the Digital Research Engine.
- Re-audit cross-model instruction discovery on a dated compatibility matrix.
- Review further profile normalisation only by route risk and retrieval benefit,
  not by file-count target.

### Other unassessed states

- Production performance, field outcomes, and live external-system behaviour:
  **NOT ASSESSED**.
- Native document and presentation render evidence: **NOT ASSESSED**.
- Current jurisdiction-specific approvals for water treatment, cookware,
  food-processing, manufacturing, and agricultural products: **NOT ASSESSED**;
  the new references deliberately stop before making those claims.

## Standardisation and next review

The durable lesson is narrow: a raw-source finding is cleared by verified
distillation or removal, not by a path exemption. The guardrail and provenance
test teach that rule to the next maintainer; the route test separately teaches
that existence is not enough when a local path crosses repository ownership.

Re-audit on 2026-08-25. Re-run the source guardrail, route/link checks, full
tests, and the structural validator from a fresh context. If a future agent
needs a removed detail, recover the historical blob for inspection outside the
working tree and add only a concise, attributed, independently written
reference after current applicability and rights review.

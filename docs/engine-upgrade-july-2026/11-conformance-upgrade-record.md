# July 2026 conformance upgrade record

Date: 2026-07-13
Engine: `C:\wamp64\www\business-plan-skills`
Benchmark: canonical `skills-web-dev` July 2026 skill-writing, composition, engine-audit, and anti-slop contracts.

## Scope and starting measurement

Active roots were discovered from the filesystem: `skills/` contained 120 active skills and `country-context/` contained 3. The engine had 123 active skills and 2 template resources. No inactive alias was counted as active.

The canonical scanner reported 0/123 compliant skills before changes. Aggregated findings were:

| Finding | Before | After |
| --- | ---: | ---: |
| Portable metadata | 123 | 0 |
| Portable sections | 123 | 0 |
| Decision rules | 123 | 0 |
| Trigger description | 121 | 0 |
| Input contract | 118 | 0 |
| Degraded mode | 113 | 0 |
| Capability contract | 79 | 0 |
| Fewer than five anti-patterns | 57 | 0 |
| Identity mismatch | 26 | 0 |
| Empty contract section | 10 | 0 |
| Line limit | 5 | 0 |
| Invalid YAML frontmatter | 3 | 0 |

Root causes were legacy two-field frontmatter, inconsistent section names, missing evidence and permission contracts, long entrypoints, and generic routing language. The existing July audit measured capability breadth; it did not establish structural conformance.

## Implemented cohorts

| Cohort | Active skills | Result |
| --- | ---: | --- |
| Pipeline | 49 | Canonical and local validation pass. |
| Meta, SaaS, and writing | 47 | Canonical and local validation pass. |
| Country, advisory, ICT, industry, language, and marketing | 21 | Canonical and local validation pass. |
| Shared meta-utility and authoring controls | 6 | Canonical and local validation pass. |

The upgrade added portable metadata; neighbour-aware triggers; input, output, and evidence tables; capability boundaries; read-only audit defaults; degraded mode; decision rules; stop and recovery behaviour; paired anti-pattern corrections; worked examples; and linked references. Long presentation, article, and proposal workflows were extracted to backlinked references.

## Regression controls and final evidence

- Local zero-debt validator: 123/123 compliant; `failure_counts` empty.
- Canonical scanner: 120/120 under `skills/` and 3/3 under `country-context/`; no findings.
- Canonical per-skill quick validator: 123 passed, 0 failed.
- Routing: 30/30 fixtures passed; expected skill in the top three for 100% of positive, negative, collision, limited-capability, and failure-path cases.
- Entry-point limit: no active `SKILL.md` exceeds 500 lines.
- CI: `.github/workflows/skill-quality.yml` runs the zero-debt validator, routing smoke test, and Python syntax checks on pushes to `main` and pull requests.
- Finance doctrine: gate recorded in `12-release-manifest.yml`; no current rate or professional-assurance claim was introduced.

The machine-readable baseline is `docs/quality/skill-quality-baseline.json`. Its empty failure map is a regression lock, not a waiver.

## Capability expansion completed

The five items previously recorded outside conformance were completed on 2026-07-13: a dated evidence-register refresh gate, standard-library workbook formula-map tooling, four complete audience exemplar packs, 24 gates across 12 sector families, and a blocker-first investment-committee simulation skill and CLI. The added skill increases the active catalogue to 124. See `14-capability-expansion-release.md` for machine evidence; the original 123-skill before/after counts above remain the historical conformance measurement.

## Full required-feature closure — 2026-07-14

The audit's broader required-feature list is now implemented, not merely documented. `business-plan-orchestrator` adds eight mandatory stages from intake through finalisation; `references/cross-engine-delivery-contract.md` defines research, finance, spreadsheet, design, document and security handoffs; and the release-bundle validator enforces blocker precedence, evidence-path existence, honest non-applicability, render review, reviewer notes, audit log, checklist and release authority.

Current machine state: 125/125 active skills conform, 3 template resources are counted separately, 38/38 routing fixtures meet the 100% top-three threshold, and 14 capability tests pass. The four audience packs now contain 32 required artefacts, including release bundles that correctly remain blocked because teaching artefacts are not rendered client submissions and have no client authority. The 123-skill and 124-skill figures above remain dated historical measurements rather than being rewritten.

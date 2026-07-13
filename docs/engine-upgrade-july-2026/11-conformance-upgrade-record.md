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

## Capability work outside conformance

The evidence-register refresh workflow, workbook formula-map tooling, complete DFI/grant/VC/owner-manager exemplar packs, sector regulatory gates, and investment-committee simulation remain product-capability expansion. They are not conformance debt and do not reduce the zero-debt result.

# Scorecard

Raw weighted total: 71/100. Capped audit total: 60/100. The cap is applied because this audit intentionally exposes the path from current state to 95+ rather than awarding production-certification scores.

| Dimension | Raw score | Points |
| --- | --- | --- |
| Richness | 17/20 | 17 |
| Robustness | 15/20 | 15 |
| World-Class Output Capability | 15/20 | 15 |
| Architecture & Discoverability | 9/15 | 9 |
| Composability & Reuse | 9/15 | 9 |
| Currency & Compliance | 6/10 | 6 |

## Richness

Raw score: 17/20.

The engine has 123 SKILL.md files, 653 reference-file hits, 8 template-file hits, and 0 example-file hits. This gives it substantial domain coverage, but the richness score is held back where references are not converted into reusable examples, current-source registers, or complete model outputs.

Top deficiencies:

- Country and market data can age quickly and needs a dated source refresh mechanism for every market claim.
- Financial workbooks exist, but model audit trails, formula maps, and cross-check tests need to be more explicit.
- The engine needs more complete finished business-plan packs for different funder types and sectors.

## Robustness

Raw score: 15/20.

Robustness is supported by routers/governance files (396 read), scripts/tests where present (14 script or script-like files), and explicit anti-slop or quality gates in the repository. It is limited by missing live validation, missing negative fixtures, weak automated checks, or incomplete failure-mode coverage depending on the engine.

Top deficiencies:

- Country and market data can age quickly and needs a dated source refresh mechanism for every market claim.
- Financial workbooks exist, but model audit trails, formula maps, and cross-check tests need to be more explicit.
- The engine needs more complete finished business-plan packs for different funder types and sectors.

## World-Class Output Capability

Raw score: 15/20.

The engine can produce credible specialist output in its domain, but the audit asks whether the output is indistinguishable from a top-tier firm. The current blocker is usually the same pattern: not enough finished exemplars, proof packs, rendered outputs, evaluator simulations, or audited workbooks to demonstrate repeatable excellence.

Top deficiencies:

- Country and market data can age quickly and needs a dated source refresh mechanism for every market claim.
- Financial workbooks exist, but model audit trails, formula maps, and cross-check tests need to be more explicit.
- The engine needs more complete finished business-plan packs for different funder types and sectors.

## Architecture & Discoverability

Raw score: 9/15.

The structure is discoverable enough to route by filesystem and frontmatter, but there are 0 skills missing name frontmatter and 0 missing description frontmatter. Empty directories (1) and large local project/example surfaces can also reduce routing clarity.

Top deficiencies:

- Country and market data can age quickly and needs a dated source refresh mechanism for every market claim.
- Financial workbooks exist, but model audit trails, formula maps, and cross-check tests need to be more explicit.
- The engine needs more complete finished business-plan packs for different funder types and sectors.

## Composability & Reuse

Raw score: 9/15.

Reuse is visible through references, templates, scripts, examples, cross-engine trigger blocks, and local governance. The gap is less about having reusable pieces and more about proving they compose into complete delivery workflows with stable contracts and acceptance criteria.

Top deficiencies:

- Country and market data can age quickly and needs a dated source refresh mechanism for every market claim.
- Financial workbooks exist, but model audit trails, formula maps, and cross-check tests need to be more explicit.
- The engine needs more complete finished business-plan packs for different funder types and sectors.

## Currency & Compliance

Raw score: 6/10.

Currency and compliance depend on dated source registers, official standards, live-rate or platform refresh protocols, and release gates. The score is constrained when standards are named but not tied to dated verification, reviewer sign-off, or automated freshness checks.

Top deficiencies:

- Country and market data can age quickly and needs a dated source refresh mechanism for every market claim.
- Financial workbooks exist, but model audit trails, formula maps, and cross-check tests need to be more explicit.
- The engine needs more complete finished business-plan packs for different funder types and sectors.

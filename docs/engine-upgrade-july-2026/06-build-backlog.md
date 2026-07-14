# Concrete Build Backlog

Conformance debt was cleared on 2026-07-13. The capability items below were completed on the same date and are now protected by CI; this table is retained as the implementation record.

| # | Filename/path | Purpose | Acceptance criteria | Effort |
| --- | --- | --- | --- | --- |
| 1 | `docs/source-registers/country-market-data.{json,md}` | Dated country and market evidence register. | **Complete:** 10 owner-assigned entries; all 3 active country skills link the register; overdue state fails tests. | M |
| 2 | `tools/workbook-audit/formula_map.py` | Generate formula map and cross-check report for Excel models. | **Complete:** formulae, broken/missing/external links, assumptions, scenarios and reconciliation checks are audited with standard-library OOXML parsing. | M |
| 3 | `examples/full-plan-packages/` | Complete DFI, grant, VC and owner-manager reference packs. | **Complete:** 4 packs contain plan, deck, model overlay, evidence, annex and committee input/result records; validator passes. | L |
| 4 | `skills/meta-finance/meta-investment-committee-red-team/SKILL.md` | Simulate audience-specific committee review. | **Complete:** blocker-first skill, deterministic CLI, dissent/condition records and positive/failure tests. | M |
| 5 | `references/sector-regulatory-gates.{json,md}` | Centralise sector permits, compliance and operating constraints. | **Complete:** 12 sector families, 24 gates, source-key validation and model/timeline stop conditions. | M |
| 6 | `skills/meta-strategy/business-plan-orchestrator/`, `references/cross-engine-delivery-contract.md`, `tools/release-gate/` | Enforce the complete workflow, handoffs and professional finalisation path. | **Complete:** eight stage gates, six cross-engine handoffs, blocker-first release schema, four honest exemplar bundles and render/handoff negative tests. | L |

# Capability expansion release

Dates: 2026-07-13 to 2026-07-14
Scope: the five original priorities plus the remaining required-feature set.

## Before and after

| Capability | Before | After and evidence |
| --- | --- | --- |
| Country/market evidence | No central dated refresh gate | 10 machine-readable entries, 3 active jurisdictions linked, owners and recheck dates enforced |
| Workbook formula audit | Stale path-only workbook verifier | 7 workbooks verified; OOXML formula map detects broken/missing/external links, cached errors, assumptions, scenarios and reconciliation checks |
| Audience exemplars | No complete audience package | 4 fictional packs and 32 required artefacts covering DFI, grant, VC and owner-board decisions, including honest release states |
| Sector regulation | Distributed narrative guidance | 12 sector families and 24 applicability/evidence/model/stop gates linked to source IDs |
| Committee rehearsal | No dedicated route | 1 read-only skill, 3 references, deterministic CLI, 4 routing fixtures and blocker-precedence tests |
| End-to-end orchestration | No mandatory full-plan controller | 8-stage `business-plan-orchestrator` from intake and evidence design through assembly, finalisation and release |
| Cross-engine delivery | No stable acceptance envelope | 6 handoffs for research, finance, spreadsheet, design, document and security work |
| Professional finalisation | Render/reviewer/audit/checklist path absent | Release schema and validator require render state, reviewer notes, audit log, checklist and explicit authority |

## Release evidence

- Local skill validator: 125/125, empty failure map.
- Routing: 38/38 expected skills within the top three at the 100% threshold.
- Capability tests: 14/14 pass, including deliberately broken workbook, overdue source,
  unknown sector, missing committee evidence, blocker precedence, missing render evidence and invalid handoff exemption paths.
- Shared financial workbook: formula audit passes with scenarios and reconciliation checks; retained
  reports are in `docs/workbook-audits/`.
- Evidence register, sector gate, workbook verifier and exemplar-pack validators pass independently.
- The CI workflow runs every local gate on pushes to `main` and pull requests.
- All four teaching release bundles validate structurally and remain `blocked`, which is the correct state for unrendered, unauthorised exemplars.
- Optional direct URL probing assessed 7/10 endpoints; the local Python trust store could not
  establish three certificate chains. Those three official pages were independently retrieved in
  the source review, and the probe limitation was not converted into a pass.

## Boundaries retained

The evidence register validates source routes and refresh metadata, not every claim copied from a
source. Sector gates are screening questions, not legal opinions. Exemplar numbers are fictional
and must be replaced. Committee simulation rehearses a decision and cannot approve funding. A
client-specific rendered pack, professional sign-off and observed funder feedback remain delivery
work, not unresolved engine conformance or measured capability debt.

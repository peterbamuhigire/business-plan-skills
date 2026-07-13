# Capability expansion release

Date: 2026-07-13
Scope: the five items formerly listed as capability work outside conformance.

## Before and after

| Capability | Before | After and evidence |
| --- | --- | --- |
| Country/market evidence | No central dated refresh gate | 10 machine-readable entries, 3 active jurisdictions linked, owners and recheck dates enforced |
| Workbook formula audit | Stale path-only workbook verifier | 7 workbooks verified; OOXML formula map detects broken/missing/external links, cached errors, assumptions, scenarios and reconciliation checks |
| Audience exemplars | No complete audience package | 4 fictional packs and 28 required artefacts covering DFI, grant, VC and owner-board decisions |
| Sector regulation | Distributed narrative guidance | 12 sector families and 24 applicability/evidence/model/stop gates linked to source IDs |
| Committee rehearsal | No dedicated route | 1 read-only skill, 3 references, deterministic CLI, 4 routing fixtures and blocker-precedence tests |

## Release evidence

- Local skill validator: 124/124, empty failure map.
- Routing: 34/34 expected skills within the top three at the 100% threshold.
- Capability tests: 10/10 pass, including deliberately broken workbook, overdue source,
  unknown sector, missing committee evidence and blocker-precedence paths.
- Shared financial workbook: formula audit passes with scenarios and reconciliation checks; retained
  reports are in `docs/workbook-audits/`.
- Evidence register, sector gate, workbook verifier and exemplar-pack validators pass independently.
- The CI workflow runs every local gate on pushes to `main` and pull requests.
- Optional direct URL probing assessed 7/10 endpoints; the local Python trust store could not
  establish three certificate chains. Those three official pages were independently retrieved in
  the source review, and the probe limitation was not converted into a pass.

## Boundaries retained

The evidence register validates source routes and refresh metadata, not every claim copied from a
source. Sector gates are screening questions, not legal opinions. Exemplar numbers are fictional
and must be replaced. Committee simulation rehearses a decision and cannot approve funding. A
client-specific rendered pack, professional sign-off and observed funder feedback remain delivery
work, not unresolved engine conformance or measured capability debt.

# Business-plan release gate

This is the final blocker-first gate for a complete business-plan engagement. It complements, and never replaces, the specialist research, finance, regulatory, workbook, design, security, document, and professional-review gates.

## Decisions

| State | Meaning |
|---|---|
| `release` | Every mandatory stage and handoff passes, evidence paths exist, finalisation is verified, and release authority is recorded. |
| `blocked` | A mandatory check failed, is unavailable, lacks evidence, or release authority is absent. |

There is no score-based override. One knockout keeps the package blocked.

## Automatic blockers

- Decision, audience, jurisdiction, version, or release owner is missing.
- A load-bearing claim is unsupported, incorrectly cited, stale beyond its required review date, or materially contradicted without disposition.
- Narrative, workbook, funding ask, use of funds, milestone timing, or downside case does not reconcile.
- Finance doctrine, sector regulation, due diligence, bankability/valuation, or audience gate has a blocking finding.
- A relied-upon XLSX lacks a passing formula map, required scenarios, or reconciliation evidence.
- An applicable research, finance, spreadsheet, design, document, or security handoff is failed or not assessed.
- A promised native document has not been written and opened, or a layout-sensitive artefact has not been rendered and visually reviewed.
- Reviewer notes, audit log, release checklist, or explicit release authority is absent.
- Anti-slop audit is grade F or reports a fabricated claim, citation, source, package, or capability.

## Required release evidence

Use `templates/release-evidence-bundle.json`. All evidence paths must resolve inside the repository or authorised engagement workspace.

1. Stage register from intake through release.
2. Cross-engine handoff records with applicability and receiver state.
3. Claim/evidence register and source-verification trail.
4. Finance gate, model formula map, reconciliations, and scenarios where applicable.
5. Regulatory/sector screen and professional-review status where applicable.
6. Assembly/version record, render record, reviewer notes, audit log, and release checklist.
7. Named release authority and timestamp for external publication or submission.

## Gate execution

Run:

```powershell
python -X utf8 tools\release-gate\validate_release_bundle.py <release-bundle.json>
```

The validator checks structure, path existence, state consistency, blocker precedence, and finalisation evidence. It cannot determine whether a source truly supports a claim, whether a financial judgement is correct, or whether a visual artefact is good. Those remain specialist and human review responsibilities.

## Recovery

For each finding record the owner, affected artefacts, requested evidence or correction, and the earliest stage to rerun. Do not edit a failed state to `pass`; retain the audit entry and add the new evidence and result.

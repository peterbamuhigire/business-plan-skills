# Next cycle plan

Proposed next cycle is intentionally small. No change here authorizes external
submission, client data processing, or paid model calls.

| Priority | Work item | Acceptance evidence | Owner role / status |
|---|---|---|---|
| P0 | Complete source-by-source review of the ten overdue country-register rows; update individual claims only when official issuer material and claim scope are checked. | Dated source URL, exact relevant claim/period, source copy or locator, reviewer and due date; register `--check` passes without changing dates to manufacture freshness. | Country-context and finance gate owners; open. |
| P1 | Validate representative projection scenarios in a spreadsheet application, including formula-driven sources and formula outputs. | Workbook SHA-256, application/version, scenario inputs, recalculated outputs, independent expected values and named reviewer; test all audience-relevant overlays. | Spreadsheet reviewer; open. |
| P1 | Produce one complete synthetic plan package with narrative/model tie-outs, rendering and accessibility review. | Evidence-backed bundle, checked HTML/PDF rendering, accessibility findings and release-gate record. | Plan maintainer and independent reviewers; open. |
| P2 | Resolve Claude plugin warnings if public directory submission becomes requested; establish actual eligibility before modifying assets or root context behavior. | Separate local validation and public portal result; no claim of acceptance without submission evidence. | Plugin maintainer; conditional. |
| P2 | Revisit the Luna/high policy only with measured task-quality, latency and cost evidence, and verify current account/runtime availability. | Dated official release/catalogue sources plus controlled same-task evaluation; retain pin unless evidence supports a change. | Codex policy owner; due per existing review trigger. |

## Carry-forward gates

- Keep `NOT_ASSESSED` for anything not actually evaluated. A working local
  marketplace install does not establish public distribution or account
  availability.
- Keep source currency claim-level. URL retrieval success alone cannot renew
  tax, FX, market, licensing or regulatory claims.
- Keep workbook structure and arithmetic evidence separate. The new numeric
  contract is deliberately limited to literal values and subtraction; it is
  not a spreadsheet engine.
- Preserve the synthetic fixture and hard-cap negative tests. Do not remove
  content to meet the file ceiling.
- Reassess against the frozen and recalibrated baseline values documented in
  [`01-baseline-scorecard.md`](01-baseline-scorecard.md); show raw score, the
  Portfolio Standard cap of 65, and the separate user-requested initial cap of
  45.

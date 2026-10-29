# Improvement backlog and Five Whys

Assessment date: 2026-10-29. Root causes below are hypotheses based on
repository code, the retained fixtures, and command results; they are not
claims about uninspected users or production incidents.

## P0 — mismatch workbook passed a structural check

**Observed:** the retained synthetic workbook declares literal numeric inputs
of 100 and 80, with a subtraction formula and blank cached result. The original
structural scan returned PASS. The post-change scan now reports an input
difference and missing cache in
[`labs/synthetic-mismatch-final-audit.json`](labs/synthetic-mismatch-final-audit.json).

1. **Why did the mismatched file pass?** The check looked for formula and
   balance/check text evidence; it did not compare declared numeric values.
2. **Why did text/formula presence count as adequate?** The tool's contract was
   an OOXML structure scan, with no numeric oracle parameter.
3. **Why was no numeric oracle supplied?** There was no small, explicit
   contract naming the cells and tolerance for a critical tie-out.
4. **Why could the release handoff still say pass?** The release validator
   checked paths and states but not whether a passing XLSX handoff carried
   numeric reconciliation evidence tied to that file.
5. **Why was this not caught earlier?** Tests covered broken references and
   structural validity, not an arithmetically mismatched workbook with a blank
   or stale cached result.

**Root-cause hypothesis (inference):** structural presence checks were treated
as if they established arithmetic integrity, and the release handoff schema
did not separate those claims. Repair uses a narrow literal-input comparison
plus cached-result check and hash binding. It does not recalculate arbitrary
spreadsheet formula graphs, assess accounting treatment, or approve business
assumptions.

## P1 — overdue sources kept a current status

**Observed:** the baseline register had ten rows whose recheck dates were
before 2026-10-29 while status remained `verified-current` (baseline evidence
in [`01-baseline-scorecard.md`](01-baseline-scorecard.md)). The current file
marks those overdue rows `stale` without changing their original check dates
or asserting renewed source review.

1. **Why could an overdue row remain current?** Validation reported lateness
   but did not flag the status/date contradiction.
2. **Why did the contradiction persist?** The register requires a status value
   but has no automated lifecycle rule that invalidates `verified-current`
   after its recheck date.
3. **Why is status not auto-renewed?** Renewal should require checking the
   relevant source and claim; a URL request alone cannot renew a claim.
4. **Why was the distinction unclear?** The schema and tests focused on
   required fields and overdue reporting, not status semantics.
5. **Why is a stale disposition still useful?** It prevents downstream readers
   from treating elapsed recheck periods as current without pretending the
   underlying issuer material is false.

**Root-cause hypothesis (inference):** the lifecycle validator lacked a rule
that overdue evidence cannot remain `verified-current`. The repair adds that
negative check and marks the observed overdue entries stale; the refresh gate
still fails for overdue entries until a reviewer performs source-level renewal.

## P1 — corrupted retail reference text

**Observed:** one `0x01` byte occurred between “below” and “consolidates” in
the [retail break-even reference](../../../skills/industry-guides/retail/references/retail-breakeven-benchmarks.md).
It was removed, and a focused regression test now rejects unexpected C0
control bytes in that file.

1. **Why was prose damaged?** A non-text control byte was present in the saved
   Markdown.
2. **Why did it persist?** The skill-contract validator did not check text
   reference bytes.
3. **Why was there no focused guard?** Existing tests covered business logic
   and reference structures, not invalid control characters in this document.
4. **Why was cleanup bounded?** The nearby text made the exact byte location
   unambiguous; no wording or benchmark content was rewritten.
5. **Why can it recur?** A future copy/edit could reintroduce a control byte
   without changing frontmatter or skill structure.

**Root-cause hypothesis (inference):** this file had no text-integrity
regression check. The focused assertion guards the repaired file only; a
repository-wide content sanitizer is outside this cycle.

## P2 — package file-count ceiling had no local guard

**Observed:** checkout and package-oriented counts were measured in the
preparation snapshot, but the repository had no fixed-cap checker. A checker
now counts both trees and rejects either above the fixed 5,000-entry cap.
OpenAI documents a 5,000-entry ZIP limit in its
[submission-error reference](https://developers.openai.com/plugins/deploy/submission-errors)
(accessed 2026-10-29).

1. **Why could a package exceed the limit unnoticed?** No repository command
   counted package entries against the documented ceiling.
2. **Why was no guard part of local validation?** Package readiness focused on
   skill manifests and runtime validation.
3. **Why check both trees?** Full checkout growth and package content are
   different measurements; neither alone proves the final archive count.
4. **Why is the ceiling not a user option?** Allowing an override above the
   documented limit would make the check misleading.
5. **Why keep the count labelled package-oriented?** It excludes a small
   explicit set of local development directories and is not a built ZIP.

**Root-cause hypothesis (inference):** local quality checks lacked a fixed
package-size acceptance control. The new guard reports its exclusions and
does not delete any checkout content.
## Prioritised improvement backlog

Limit: four cycle items (within the Portfolio Standard's ten-item maximum).
Owners are roles; no production or client work was supplied.

| Priority | Finding | Five-Whys root cause | Bounded action | Acceptance evidence | Owner / disposition |
|---|---|---|---|---|---|
| P0 | Formula-map and release handoff did not detect the retained mismatch | Structural checks were relied on without a cell-level numeric oracle or release evidence binding | Add an opt-in required reconciliation contract for same-sheet literal numeric inputs; verify declared subtraction, tolerance and cache; recompute from workbook+contract during release validation rather than trusting an attached report | Matched/mismatched/blank/stale-cache fixtures; forged-report rejection; missing contract/report rejection; four exemplar bundles remain blocked and mark spreadsheet numerical assessment not-assessed | Completed in this cycle; arbitrary formulas, formula-source recalculation and spreadsheet application behavior remain out of scope |
| P1 | Ten recheck-overdue rows showed `verified-current` at baseline | Date validator lacked a status/date consistency rule | Reject overdue `verified-current`; set observed overdue records to `stale` without changing check dates or pretending to renew sources | Focused lifecycle test; `--check` still reports overdue records, showing no false renewal | Partly completed: status integrity fixed, source-level refresh still open for designated owners |
| P1 | One C0 control byte corrupted retail reference text | No focused byte-integrity assertion for that reference | Remove the single confirmed byte and add a targeted regression test | Byte scan reports none in the repaired file; focused test passes | Completed |
| P2 | No package-size ceiling guard | Local package checks did not compare either tree to the documented ZIP ceiling | Add a fixed 5,000 hard-cap check for the full checkout and package-oriented tree; reject CLI override attempts | Boundary test accepts 5,000/rejects 5,001 for both counts; CLI rejects an override; inventory prints both counts | Completed; count does not represent a built archive |

## Deferred work and explicit gaps

- Renew overdue country sources only after source-by-source, claim-specific
  review. URL availability alone does not establish data freshness or legal
  applicability. Exact current tax rates, FX values and registration/licensing
  processes remain **NOT_ASSESSED** in the synthetic plan.
- Full workbook calculation, formula-driven source dependency evaluation,
  recalculation in Excel/LibreOffice, accounting treatment, and lender-specific
  debt-service review remain **NOT_ASSESSED**.
- Public submission acceptance is **NOT_ASSESSED**. Local Claude validation
  and isolated native Codex/Claude installs were exercised; they do not prove
  public-directory eligibility or account-wide availability.
- Model selection remains Luna/high under the authorized policy. Comparative
  quality, cost, latency and account entitlement are **NOT_ASSESSED**; official
  provider release/current-catalogue snapshot is recorded in
  [`00-scope-and-evidence.md`](00-scope-and-evidence.md).

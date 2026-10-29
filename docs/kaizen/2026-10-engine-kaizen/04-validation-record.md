# Validation record

Validation date: 2026-10-29. Tests ran in an externally prepared Python
environment; no dependencies were added to the checkout. No host configuration
or plugin catalogue was changed by the native checks.

## Implementation and scope

- Added an opt-in reconciliation contract for finite literal numeric values on
  one worksheet, an exact declared subtraction formula, finite non-negative
  tolerance, and a numeric cached result consistent with the inputs. Audit
  hashes apply to the exact workbook bytes that were parsed.
- A passing XLSX spreadsheet handoff must provide its report and contract. The
  release validator recomputes the check from workbook plus contract and
  compares report data with the recomputed result; a fabricated PASS report
  cannot override mismatched workbook values.
- Existing example handoffs now say numerical reconciliation is
  `not-assessed`; all four bundles remain blocked.
- The ten expired register entries were changed to `stale`, preserving their
  original checked/due dates. The validator now also rejects an overdue row
  that still claims `verified-current`. The source gate still fails until
  claim-level source review occurs.
- Removed the confirmed control byte from the retail reference and added a
  focused regression test.
- Added a fixed hard-cap helper for full checkout and package-oriented file
  counts. It does not allow a user-supplied higher cap and does not delete
  files.
- Added a Codex compatibility manifest and local repo marketplace. Added
  Claude manifest description and author metadata. Existing hook configuration
  remains unchanged.
- Updated the finance projection skill to distinguish structural formula scan
  from calculation evidence.

No canonical accounting doctrine, other engine, tax value, user-supplied
business content, or source claim was rewritten.

## Executed checks

| Command / gate | Result | Boundary |
|---|---|---|
| Prepared pytest environment: `python -m pytest -q tests` | 78 passed, 56 subtests passed | Full repo Python suite. An initial fixture setup failure was corrected; subsequent full runs passed. |
| `scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` | 137 active skills, 3 templates, 137 compliant, zero findings | Structural contract only. |
| `scripts/routing_smoke_test.py --threshold 1.0` | 61/61 top-three matches | Not precision@1 or live-agent routing. |
| `scripts/routing_link_check.py` | 7 surfaces; zero failures | Enumerated links only. |
| `tools/sector-gates/validate_sector_gates.py` | 12 sector families, 24 regulatory gates; pass | Structural coverage, not competent-authority approval. |
| `tools/exemplar-packs/validate_exemplar_packs.py` and release bundle checks | 4 packs, 32 artefacts; valid and blocked | Spreadsheet numerical state is not assessed. |
| `scripts/build-financial-models/verify_workbooks.py` | All 7 workbooks verified | ZIP structure and expected sheet names only. |
| Formula map over all 7 XLSX templates | 7 structural passes; reconciliation `not-assessed` | No arbitrary formula recalculation. |
| Required contract on retained mismatch workbook | Exit 1; 2 findings | Synthetic negative fixture. |
| `tools/evidence-register/refresh_evidence_register.py --check` | Exit 1; 10 overdue entries | Deliberately not reported as a pass; states now indicate stale. |
| `.codex/ensure_model_policy.py --runtime codex --check` | Pass | Authorized Luna/high policy is retained. |
| `claude plugin validate .claude-plugin/marketplace.json` | Pass | The plugin directory validator reports warnings for root `CLAUDE.md` context and missing icon; strict mode treats these warnings as failure. |
| Isolated Claude native marketplace install/list | Marketplace add and plugin install succeed; plugin enabled | Offline disposable container; repository mounted read-only; no host config or account-wide claim. |
| Isolated Codex native marketplace add/install/list | Marketplace and plugin listed as installed/enabled | Offline disposable container; repository mounted read-only; local repo marketplace only. |
| `scripts/check_package_file_budget.py` | 1,294 checkout entries; 1,143 package-oriented entries | Pre-document-commit worktree snapshot. Both are below the documented 5,000-entry ZIP limit ([OpenAI submission errors](https://developers.openai.com/plugins/deploy/submission-errors), accessed 2026-10-29). The package-oriented count excludes `.git`, `.cache`, `cache`, `__pycache__`, `node_modules`, `.venv`, and `venv`; counts files and symlink entries; does not follow symlinks. Not a built archive count. |
| `git diff --check` | Pass | Whitespace validation only. |

## Native package warnings and unassessed acceptance

Claude's plugin manifest and marketplace pass the ordinary local manifest
checks. Directory checks warn that root `CLAUDE.md` is not loaded as plugin
context and that no icon is present. Strict validation fails on warnings.
These are recorded, not presented as public acceptance. Codex's local repo
marketplace and plugin were successfully discovered and installed in the
offline test. Public-directory submission and account-level availability are
**NOT_ASSESSED**.

## Current source and model evidence

The source-currentness snapshot checked official Bank of Uganda, Uganda
Bureau of Statistics, Central Bank of Kenya and Bank of Tanzania pages on
2026-10-29; values and precise scope are linked in
[`00-scope-and-evidence.md`](00-scope-and-evidence.md). These are dated context
snapshots, not synthetic-plan inputs. The ten overdue country-register items
remain **NOT_ASSESSED** for claim-level renewal; URL retrieval alone is not
enough.

The OpenAI changelog, model catalogue and selection guidance were checked on
2026-10-29 ([changelog](https://developers.openai.com/api/docs/changelog),
[catalogue](https://developers.openai.com/api/docs/models),
[selection guidance](https://developers.openai.com/api/docs/guides/model-selection)).
The authorised Luna/high pin is retained. Comparative quality, cost, latency,
and account entitlement remain **NOT_ASSESSED**.

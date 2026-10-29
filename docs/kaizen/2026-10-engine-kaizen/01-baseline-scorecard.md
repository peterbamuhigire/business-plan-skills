# Frozen baseline scorecard

- **Baseline commit:** `d3d5013744b8a668e21647e45161c1c7f80fdc3d`
- **Assessment date:** 2026-10-29
**Scale:** scores are practitioner judgements (inference), recorded on a 0–100
scale by multiplying the preparation's 0–10 ratings by 10. They are not
validator pass rates. The raw score is the arithmetic mean of all ten
dimensions.

| Dimension | Raw /100 | Named baseline evidence | Deficiency |
|---|---:|---|---|
| Doctrine | 70 | FP&A assumption-trace and release/orchestrator rules were read; practitioner tasks preserve gaps and separate synthetic assumptions | No released bankable SaaS case demonstrates the end-to-end contract. |
| Taxonomy and routing | 70 | Router plus 137 active skills; routing smoke test matched 61/61 examples in top three | This is top-three lexical coverage, not precision@1; runtime context omits paths by default. |
| Skill depth | 70 | Orchestrator, finance/projection route, source, release and workbook-audit workflows inspected | Compliance does not prove practitioner behavior; duplicate headings and full semantic coverage remain open. |
| Applied proof | 40 | Three practitioner tasks; 66 tests pass; synthetic mismatch workbook passes formula-map with blank cached value | No reconciled, independently reviewed bankable/investor output; critical mismatch false negative. |
| Standards currency | 30 | Official macro checks and source-register validator; country register check reports 10 overdue rows | Several country tables are stale/corrupt; taxes, FX gaps, registration/licensing and source claims remain unverified. |
| Output readiness | 70 | Release-bundle schema and blocked example packages inspected | Structural validation does not establish workbook reconciliation, rendered quality, or authority. |
| Accessibility and inclusion | 50 | Existing language and country-context routes inspected | No rendered complete plan or assistive/accessibility review was performed. |
| Production and handoff | 70 | Release workflow names stages, handoffs, owners, and blockers | No end-to-end reviewed/rendered handoff; formula-map does not inspect calculation results. |
| Hygiene | 70 | Skill validator reports 137 active skills compliant; one C0 byte in the retail reference; expired source records present | A clean skill contract check misses prose corruption and source-currentness state drift. |
| Safety and integrity | 60 | FP&A trace and release rules preserve evidence states; tenant/finance handoffs named | Structural workbook PASS can hide a mismatch; overdue records and malformed text can flow downstream. |

- **Raw mean:** `(70 + 70 + 70 + 40 + 30 + 70 + 50 + 70 + 70 + 60) / 10 = 60.0/100`.
- **Portfolio Standard score:** `min(60.0, 65) = 60.0/100`.
- **User-requested initial-cycle cap:** `min(60.0, 45) = 45/100`.

The Standard cap and the initial user cap are separate reporting ceilings; the
45-point value is not a changed raw score. A critical safety, financial,
privacy, legal, or release blocker remains a blocker regardless of mean score.
The 95/100 figure is a target, not an achieved result.

## Baseline measures

| Measure | Frozen result | Boundary |
|---|---|---|
| Skill contract | 137 active skills, 3 templates, 137 compliant, no findings; `scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` exit 0 | Contract structure only. |
| Routing | 61/61 top-three matches (100.0%); `scripts/routing_smoke_test.py --threshold 1.0` exit 0 | Not precision@1 or live-agent routing. |
| Test suite | 66 passed; `python -m pytest tests` in the prepared external test environment | No repository dependency installation. |
| Country source register | 10 overdue entries; `python -B tools/evidence-register/refresh_evidence_register.py --check` exit 1 | No claim-level renewal by the baseline. |
| URL probe | TLS retrieval errors for UBOS and KNBS; UNBS HTTP 403; URL check exit 1 | Retrieval failures do not establish source invalidity. |
| Sector gate | 12 families, 24 gates; exit 0 | Structural completeness, not competent-authority clearance. |
| Exemplar packs | 4 packs, 32 artefacts; each schema-valid but decision `blocked` | Not a release pass. |
| Workbook verification | 7/7 workbooks readable and expected sheet names present | Does not calculate or reconcile formulas. |
| Mismatch specimen | Cash flow 100 vs balance-sheet cash 80; formula `=B1-B2`, blank cached result; formula-map exit 0, zero findings | Reproduced in `00-practitioner-tasks.md` and retained workbook/audit files. |
| Checkout capacity | 1,163 file entries full checkout / 1,125 package-oriented at the unchanged preparation snapshot | Count method: `os.walk`, files and symlink entries, no symlink-directory traversal; package excludes `.git`, caches, venvs and `node_modules`. This is not a built archive count. |
| Native runtime | Root-provided offline debug summary: default 117/134 paths, configured 134/134 | Tested runtime invocation only; no account-wide guarantee. |
| Owned negatives and coverage | Full per-skill owned-negative and 3-positive/2-negative coverage census **NOT_ASSESSED** | Do not infer from routing top-three result. |
| Links, examples, source records | Full broken/machine-specific link, duplicate-heading, example-depth, and dangling-cross-engine census **NOT_ASSESSED** | Not represented as zero. |

### Cited currentness snapshots

Dynamic source claims in the baseline scope are linked at the point of use in
[00-scope-and-evidence.md](00-scope-and-evidence.md). The source-country and
tax pages were not copied into this scorecard as current law or assumptions.
The model policy remains Luna/high because official release recency and the
local runtime list do not provide comparative task-quality evidence.

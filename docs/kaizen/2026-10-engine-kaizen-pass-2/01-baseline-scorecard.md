# Frozen baseline scorecard (pass 2)

- **Baseline commit:** `50d50f937e58ef2cd476c8a0c15b4b1d0305f3e9` (`main`, clean working tree)
- **Assessment date:** 2026-10-31
- **Frozen:** committed before any engine content, tool or test was changed. Later edits to this file may only append a dated note below the freeze line.

**Scale.** Scores are practitioner judgements (inference) on a 0 to 100 scale, not validator pass rates. The raw score is the arithmetic mean of the ten Portfolio Standard dimensions. The published score is `min(raw, 65)`. Any safety, legal, financial, privacy or release failure is a blocker whatever the number.

## Scores

The 29 October final column is taken from [`../2026-10-engine-kaizen/05-final-report.md`](../2026-10-engine-kaizen/05-final-report.md). This fresh baseline is lower on five dimensions because it measured things that cycle left `NOT_ASSESSED` (text integrity, workbook recalculation, routing precision@1, fixture coverage, register-to-table agreement). It is a wider measurement, not a regression of the engine since 29 October: no engine content changed between the two dates.

| Dimension | 29 Oct final | Fresh baseline | Named evidence | One-line deficiency |
|---|---:|---:|---|---|
| Doctrine | 50 | 50 | Router, orchestrator, stage gates, release gate read; blocker precedence is explicit | No independently reviewed real engagement; doctrine and shipped template contradict each other (balance sheet and DSCR required, absent) |
| Taxonomy and routing | 55 | 50 | 137 active skills; 61/61 top-three; precision@1 48/61 (78.7%); 43 of 137 skills have any fixture | Top-three lexical match overstates routing; no skill has three positives and two owned negatives |
| Skill depth | 50 | 50 | Orchestrator and projection skill inspected; 137/137 contract-compliant | 75 of 137 skills carry duplicate contract headings; contract compliance is structure, not behaviour |
| Applied proof | 45 | 40 | Mismatch contract works on literal inputs; template run end to end in LibreOffice | The shipped bank-loan model cannot model a loan, has no balance sheet, and 10 inputs drive nothing; a formula-driven model cannot pass the gate |
| Standards currency | 35 | 30 | Register check exit 1 with 10 overdue rows; macro snapshot of 29 Oct | Human register table still reads `verified-current` for the 10 stale rows; Uganda context labels a 2025 rate "current" and gives a policy rate the Bank of Uganda has since moved |
| Output readiness | 60 | 55 | 4 blocked exemplar bundles; template recalculated | Template yields Year 3 EBITDA of +102,300 against operating income of (10,715); no complete plan produced or rendered |
| Accessibility and inclusion | 25 | 25 | Language and country routes inspected | No rendered plan, no assistive review |
| Production and handoff | 55 | 50 | Release bundle schema, plugin installs from 29 Oct | Formula caches in all 7 shipped workbooks are stale placeholders; no recalculation evidence exists anywhere in the handoff |
| Hygiene | 60 | 40 | Zero broken relative links (586 checked); no control bytes found | 1,636 lines still carry the April 2026 non-ASCII loss (170 corrupt numeric ranges); Windows paths in the router; register table out of step with its JSON |
| Safety and integrity | 55 | 50 | Fail-closed literal mismatch check; stale-status rule | Numeric corruption in country context (for example inflation "35%") and an EBITDA add-back error can flow into lender and investor material |

- **Raw mean:** `(50 + 50 + 50 + 40 + 30 + 55 + 25 + 50 + 40 + 50) / 10 = 44.0/100`
- **Published (Portfolio Standard) score:** `min(44.0, 65) = 44.0/100`
- **29 October final for comparison:** raw 49.0, published 49.0. The 95/100 figure is a target and is not claimed.

**Blockers present at baseline (independent of the score):** D1, D2 and D11 in [`00-scope-and-evidence.md`](00-scope-and-evidence.md). Each can put a wrong number in front of a lender or investor.

## Measured inputs (all taken at the frozen commit)

| Measure | Result | Boundary |
|---|---|---|
| Skill contract validator | 137 active, 3 templates, 137 compliant, exit 0 | Structure only |
| Routing, top three | 61/61 (100.0%), exit 0 | Lexical scorer in `scripts/routing_smoke_test.py` |
| Routing precision@1 | 48/61 = 78.7% | Same scorer; first time measured |
| Owned negatives | 14 fixtures name an excluded skill; those 14 skills each own 1; 0 skills own 2 | An "owned negative" is a fixture whose `excluded` list names the skill |
| Fixture coverage (3 positives and 2 owned negatives) | 0 of 137 skills; 43 of 137 have at least 1 positive; 4 have 3 or more | Counted from `tests/routing-fixtures.json` |
| Worked-example depth | Not scored per skill; 4 exemplar packs (32 artefacts) all `blocked`; 0 complete rendered plans | Counting every worked example is `NOT_ASSESSED` |
| Broken relative markdown links | 0 of 586 checked (1,020 `.md` files, `docs/kaizen/` excluded); the 2 absolute-looking link strings are quoted counter-examples in `blog-writer/references/editorial-standards.md:255-256` | Link targets only; anchors not checked |
| Machine-specific paths in engine content | 12 lines in 5 files (`AGENTS.md` 8, `.gitignore` 1, `templates/README-financial-models.md` 1, `skills/meta-utility/skill-writing/SKILL.md` 1, and 1 comment in `scripts/validate_skill_engine.py` that documents the link rule and is legitimate); 14 lines in 11 historical `docs/` records; 12 lines in 2 test or hook fixtures | `git grep` for drive letters, `wamp64`, `/home/`, `/Users/` |
| Dangling cross-engine references | 1 confirmed (`procurement-policy-and-manual/SKILL.md:52`); the path-form references to the proposal, accounting and SDLC engines otherwise resolved against the local sibling checkouts (read-only); the research-engine reference and a name-level census of backticked skill names are `NOT_ASSESSED` | Path references only |
| Expired source records | 10 of 23 overdue at 2026-10-31 (all marked `stale` in JSON; all still `verified-current` in the Markdown table) | `refresh_evidence_register.py --check` |
| Text damage from non-ASCII loss | 1,636 lines in HEAD (170 numeric-range lines) in 47 files | `labs/baseline-text-damage-census.txt` |
| Workbook formula caches | 4,046 of 4,385 formula cells (92%) differ from a LibreOffice recalculation; 0 error cells after recalculation | `labs/baseline-workbook-cache-census.txt` |
| Dead inputs in the projection template | 10 of 104 literal numeric input cells unreferenced | Scan includes ranges and defined names |
| Duplicate H2 headings in `SKILL.md` | 75 of 137 files | Counted by the command below |
| Unit tests | 80 passed, `unittest`, exit 0 | `pytest` is not installed |
| Package file budget | 1,343 / 1,142 entries against a 5,000 cap | Not a built archive |
| Model currentness | `NOT_ASSESSED` | Claude runtime; no model-policy change proposed |

Duplicate heading census (read-only, repeatable):

```
python3 -I - <<'PY'
import collections, subprocess
from pathlib import Path
paths = subprocess.run(["git", "ls-files", "skills/**/SKILL.md", "country-context/**/SKILL.md"],
                       capture_output=True, text=True).stdout.split()
dup = [p for p in paths
       if any(n > 1 for n in collections.Counter(
           l.strip() for l in Path(p).read_text(encoding="utf-8").splitlines()
           if l.startswith("## ")).values())]
print(len(paths), len(dup))
PY
```

Result at baseline: `137 75` (137 tracked `SKILL.md` files, 75 with at least one repeated H2 heading).

## Freeze line

Everything above is frozen at `50d50f9`. Appended notes follow below only.

# README kaizen record, 31 October 2026

A scoped micro-cycle on the root `README.md` of the business-plan engine. It follows the Portfolio Kaizen steps (Observe, Baseline, Select, Experiment, Check, Standardise, Teach, Re-measure). It changes no skill body, script or test. **It publishes no score.** The latest published score stays 50.0 out of 100 from pass 2.

Branch `kaizen/2026-10-readme-kaizen`, created from `main` at `4512534` (clean tree, 0 `git status --porcelain` lines). The measurement scripts (`readme-metrics.py`, `readme-preserve-check.py`) come from the README kaizen brief and are not stored in this repository.

## Observe

Baseline, measured before the first edit:

| Metric | Before | What it says |
|---|---:|---|
| `words` | 11,588 | Far longer than a front door can carry |
| `h2` | 5 | Five sections held everything |
| `toc` | 0 | No contents list |
| `first_cmd` | 13 | First command at line 13 |
| `longest_sec` | 4,242 | The References section |
| `long_lines` | 44 | Lines over 300 characters |
| `max_line` | 1,276 | Characters in the longest line |
| `sent_len` | 19.8 | Words per sentence in prose paragraphs |
| `fre` | 39 | Flesch reading ease: difficult |
| bullets, table rows | 277, 199 | Mostly the catalogue and the reference lists |

What the baseline hid, by section (words): References 4,242 (Books 2,164, Standards 1,111, Websites 678, Repositories 245); Capabilities 2,658, of which about 2,000 was a 137-row skill table; Installation 1,286; the kaizen section 2,169.

Other observations:

- The README had no task-to-skill table, no contents list and no contributing, author or licence section.
- Two dated records linked README anchors that did not exist: `#capability-map` in `docs/audits/2026-09-06-kaizen-readiness.md` and `#the-kaizen-operating-contract` in `docs/continuous-improvement/kaizen-wave-1-2026-08-11.md`. They were already broken at `main`.
- What reads the README:
  - `scripts/validate_skill_engine.py` (line 59) only requires that the file exists.
  - `scripts/routing_link_check.py` scans it as a surface: every `skills/...` path token and Markdown link must resolve.
  - `tests/test_runtime_orchestration_guidance.py` requires the text `runtime-agnostic-orchestration-2026-09-07.md` in it.
  - `scripts/check_text_integrity.py` scans it, because it scans Markdown outside `docs/`.
  - `AGENTS.md` and `CONTRIBUTING.md` point readers at "the README's Checks paragraph". `docs/README.md` links `README.md#what-the-october-2026-kaizen-improved`.
  - The registered validators for this engine in the portfolio catalogue are `validate_skill_engine.py` and `routing_smoke_test.py`.
- No script, test, manifest or router reads the catalogue table or the References section as content.

## Select

| Item | Decision | Reason |
|---|---|---|
| R1 Front door | Applied | Purpose, audience, six measured facts and three numbered steps inside the first 40 lines. The plain statement that the shipped workbooks are not lender models is the last "At a glance" fact and has its own subsection under "What is inside" |
| R2 Contents | Applied | An 11-item list, with the four kaizen sections nested; all 16 in-page anchors resolve |
| R3 Structure | Applied | 17 H2 sections. The largest H2 is Validate at 906 words, made of six H3 sections of 263 words or fewer. The largest H3 or themed H2 is 659 words, above the 600 aim and below the 1,200 limit |
| R4 Find the right skill | Applied | 12 rows (14 skill links). Each task comes from `tests/routing-fixtures.json`. Every linked `SKILL.md` exists |
| R5 No walls of text | Applied | Longest paragraph or list item 71 words. No table cell over 35 words. Lines over 300 characters 44 to 0 |
| R6 Plain English | Applied | Short active sentences; terms defined at first use; exact commands, numbers and hashes kept |
| R7 Say it once | Applied | The 44.0 baseline, the install-command fix and the lender-model statement are no longer repeated in the same section. The reverted-attempts narrative is two bullets, with the detail in the pass 2 experiment log. The October 2026 kaizen section is kept (Peter asked for it), tightened and split into one introduction and four themed sections |
| R8 Relocate bulk | Applied to two items | The 137-row catalogue went to `docs/skill-catalogue.md` and the 200-book, repository, standards and website lists to `docs/cited-sources.md`. The README keeps the category counts, a summary and a link for each |
| Move the Checks paragraph | Skipped | Validators and `AGENTS.md` point at it |
| Move "What is still open" and the date-gates table | Skipped | 538 words together, and the part a reader acts on |
| `CHANGELOG.md` entry | Skipped | This engine keeps no changelog |

## Experiment

| Commit | Theme | What it changed |
|---|---|---|
| `59896c0` | Relocation | Moved the catalogue and cited sources verbatim to two docs pages, with relative links corrected. `words` 11,588 to 5,006 and `longest_sec` 4,242 to 2,924 in this step |
| `52e857b` | Structure and front door | New opening, At a glance, Start here, Contents, When to use it, Find the right skill; Installation split into Install and update and Validate; Capabilities and Operating contracts became What is inside and How it works; contributing section added. `words` rise to 5,811 as the front door is added |
| `306bd35` | Plain English | Rewrote the prose of every section; long bullets became a one-line problem with Fix, Re-measured and Limit sub-bullets; the kaizen section split into themed sections; routing figures put in one table; lines over 300 characters 44 to 0. Its commit message wrongly says four routing figures appeared "twice in prose"; they appeared once, as a prose run, and are now a table. History was not rewritten |
| `58a41ab` | Docs index and links | `docs/README.md` lists the new pages and names the new README sections; two dead anchors in dated records repointed; checkout file count corrected; README points to the documentation index |
| this commit | Record | This file |

Deliberate corrections to facts, each re-measured on 31 October 2026:

1. Two dead anchors repointed (`#capability-map` to `#what-is-inside`; `#the-kaizen-operating-contract` to `#quality-and-improvement`). The permanent 65-point cap is described under Quality and improvement.
2. "wrote 903 files (137 `SKILL.md` files, the hooks and the rules)" became "wrote 903 files. They include 137 `SKILL.md` files, the hooks and the rules". The number is unchanged: a fresh project-scope install into an empty scratch directory wrote 903 files, `doctor` reported 0 missing and 0 locally modified, and a second install into the same directory gave the same result. The 903 also hold the `references/` folders, so "the hooks and the rules" was an incomplete list.
3. Checkout file count 1,669 became 1,681, with a note that the count includes `.git`. The cap script counted 1,681 and 1,169 at the start of this cycle. The package-oriented figure was not touched.
4. An "Update" subsection was added. It states only what was run: a second installer run succeeded on an unchanged checkout. It says that a changed tree and the plugin update path were not tested.
5. The "At a glance" fact "13 of the 14 checks exit 0" is new. It was counted from the validator run below.

## Check

### Validators (before and after)

Run from the repository root with `python3 -B -X utf8` and `PYTHONDONTWRITEBYTECODE=1`. The "after" run is on branch commit `58a41ab` plus this record. The full outputs, with timings and temporary paths removed, were compared line by line: they are identical except the file-entry counts printed by the budget checker.

| Command | Before | After |
|---|---:|---:|
| `validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` | 0 | 0 |
| `routing_smoke_test.py --threshold 1.0 --report --min-precision-at-1 0.80` | 0 | 0 |
| `routing_link_check.py` (default surfaces) | 0 | 0 |
| `check_text_integrity.py` | 0 | 0 |
| `check_package_file_budget.py` | 0 | 0 |
| `source_ingestion_guardrail.py` | 0 | 0 |
| `refresh_evidence_register.py --check` | 1 | 1 |
| `validate_sector_gates.py` | 0 | 0 |
| `validate_exemplar_packs.py` | 0 | 0 |
| `verify_workbooks.py` | 0 | 0 |
| `validate_release_bundle.py` on each of the four example packs | 0 each | 0 each |
| `python3 -m unittest discover -s tests -p "test_*.py"` (130 tests) | 0 | 0 |
| `quick_validate.py` on every skill directory (137) | 0 failures | 0 failures |
| `node hooks/test-destructive-bash-gate.js` | 0 | 0 |
| `node hooks/test-plugin-hook-config.js` | 0 | 0 |
| `node scripts/generate-plugin-manifest.js --engine . --root . --check` | not run | 0 (137 skills) |

- The evidence-register check exits 1 before and after, for the four overdue rows that the README already states. This cycle did not touch it.
- The file-entry counts differ: package-oriented 1,169 to 1,172 (the two new docs pages and this record), full checkout 1,681 to 1,705 (the same three files plus git objects for four commits).
- The registered validators in the portfolio catalogue are the first two rows. Both exit 0.

### Preservation check

`readme-preserve-check.py <repo> main kaizen/2026-10-readme-kaizen` (the checker that resolves relative links against each file's location):

```text
links: old README 234 targets; new README 68; moved to docs 171; LOST 0
commands: old README 36; kept in README 36; moved to docs 0; LOST 0
anchors: 6 README.md#anchor links in tracked files; BROKEN 0
in-page links: 16 anchors used; BROKEN 0
RESULT: OK
```

An earlier run, made before the checker resolved relative links, flagged 125 skill links as LOST. Each was a `skills/...` or `country-context/...` link that moved to `docs/skill-catalogue.md` with a `../` prefix. A separate script that resolves every link to a repository path first agreed: 0 lost, 171 moved, 0 dangling relative links in the new README and the changed docs.

### Checks made on the moved pages

No script covers the two new pages, so each was checked once by hand:

- `routing_link_check.py README.md docs/skill-catalogue.md docs/cited-sources.md docs/README.md`: 4 surfaces, 0 failures.
- `check_text_integrity.py` run with `--root` on a scratch copy of the two pages, with the repository's hash fixture: exit 0. It is not vacuous: the same run on a copy with a glued year range and a glued decimal range appended exits 1 with two findings. `routing_link_check.py` on a built-to-fail link exits 1.
- The catalogue lists 137 rows with 137 unique paths. `find skills country-context -name SKILL.md` finds the same 137, and every row's name matches its directory name.
- The README category table matches `find` for all 16 categories (49, 22, 12, 11, 4, 4, 3, 3, 7, 2, 3, 5, 6, 1, 2, 3).
- The cited-sources counts (200 books, 11 repositories, 14 standards groups, 26 websites) match a count of list items in the original README. The Books list holds 201 items, one of which is the "Cited by title only" line.

### Metrics after

| Metric | Before | After | Target | Result |
|---|---:|---:|---|---|
| `words` | 11,588 | 5,835 | at most 12,167 (aim 10,429) | Met: minus 49.6% |
| `h2` | 5 | 17 | none | Four of the 17 come from splitting the kaizen section |
| `toc` | 0 | 1 | 1 | Met |
| `first_cmd` | 13 | 20 | 40 or less | Met. It rose from 13 because six facts now come first |
| `longest_sec` | 4,242 | 906 | 1,500 or less (1,200 preferred) | Met |
| `long_lines` | 44 | 0 | 22 or fewer | Met |
| `max_line` | 1,276 | 296 | 700 or less | Met |
| `sent_len` | 19.8 | 12.6 | 16.5 or less | Met |
| `fre` | 39 | 56 | at least 39 (aim 44) | Met: plus 17 |
| bullets, table rows | 277, 199 | 143, 80 | information | Fewer, mainly because of the relocation |

Limits of these numbers:

- `sent_len` and `fre` read prose paragraphs only, not bullets or table cells. The 56 and the 12.6 are therefore not a reading-ease score for the whole page. Bullets in the kaizen sections still carry long sentences with commit hashes and figures.
- `words` fell mainly because two lists moved out, not because the prose shrank. The two docs pages hold 2,555 and 4,240 words.
- Splitting the kaizen section into H2s lowers `longest_sec`. As H3s under one H2, that section would be about 2,005 words.

### Not assessed

- `python3 -m pytest` (no `pytest` on this host); `unittest` ran instead.
- The plugin commands (`/plugin marketplace add`, `/plugin install`), the `codex plugin` commands, the PowerShell installer form and the `git clone` lines. None can run here without network access, a model runtime or Windows, and none was changed in meaning.
- Whether the Start here prompt example ("Run the client intake and list the missing assumptions.") reaches `00-client-intake` in a live agent. The routing fixtures show the lexical scorer finds it; no model call was made.
- CI on a runner.
- Whether a reader finds the new README easier. No reader test was run; the metrics are proxies.

## Standardise

README conventions for this engine, for the next editor:

1. **Skeleton.** Title and purpose; At a glance; Start here (with the contents list); When to use it; Find the right skill; How it works; What is inside; Install and update; Validate; Quality and improvement; the October 2026 kaizen sections; What is still open; Cited sources; Contributing, author and licence.
2. **Limits.** First fenced command by line 40. No paragraph over 90 words and no table cell over 35 words. No line over 300 characters. No H2 over 1,200 words. Mean sentence length 16 words or fewer.
3. **Interfaces to keep.**
   - The anchor `#what-the-october-2026-kaizen-improved` (linked from `docs/README.md`).
   - A `Checks` heading with the command block, and the "What each check needs" table (`AGENTS.md` and `CONTRIBUTING.md` point at it).
   - The text `runtime-agnostic-orchestration-2026-09-07.md` (required by a unit test).
   - Every `skills/...` path in the README must exist (`routing_link_check.py`).
   - No host paths and no glued numeric ranges (`check_text_integrity.py`).
4. **Long lists live in `docs/`.** The README holds counts and a link. `docs/skill-catalogue.md` is a convenience copy; the `SKILL.md` files stay the source of truth, as `CONTRIBUTING.md` says.
5. **Numbers.** Re-measure any number you touch. A date next to a result means the command was run on that date.
6. **Before you commit.** Run `readme-metrics.py` and `readme-preserve-check.py`, and the commands in the Validate section.

## Teach

- Write the first 40 lines for a stranger: what it is, who for, six measured facts, three commands. Everything else can wait below a contents list.
- When a table has more than about 50 rows, move it to `docs/` and keep the counts. Check the moved page once with the link and text-integrity scripts, because they do not scan it by default.
- Keep one statement of each fact. Link to the record that holds the detail instead of repeating the story.

## Re-measure and next cycle

Re-run `readme-metrics.py` after the next README edit. Compare with the "After" column above.

Open items for a later cycle (none of them is a README defect):

1. Add `docs/skill-catalogue.md` to `DEFAULT_SURFACES` in `scripts/routing_link_check.py`, and add a test that compares the catalogue rows with the `SKILL.md` set. Today no script notices drift in the catalogue page. Scripts were out of scope here.
2. `scripts/check_text_integrity.py` skips `docs/`, so `docs/cited-sources.md` and `docs/skill-catalogue.md` sit outside it. Decide whether the two pages should be scanned.
3. `AGENTS.md` and `CONTRIBUTING.md` say "the README's Checks paragraph". The content is now the `Checks` and "What each check needs" subsections of Validate. Change the wording in the next documentation pass.
4. `docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md` says "Three attempts ... were tried before the kept one". The experiment log (`03-experiment-log.md`) lists three attempts in all, with the third kept, so two were reverted. The README follows the log. This is a dated record and was not edited.
5. The recalculation, workbook and evidence items in "What is still open" are unchanged by this cycle.

No cross-engine mismatch was found in this cycle. No other repository was edited.

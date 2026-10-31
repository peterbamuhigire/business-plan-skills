# Documentation follow-ups (31 October 2026)

Written by the documentation wave that followed pass 2, on branch `kaizen/2026-10-docs`. The wave changed documents only. Everything below needs a change to a skill, a configuration file, a script or the CI workflow, which that wave was not allowed to make, or a check that could not be run. Each item names the exact file and what closes it.

## Configuration and scripts

| Item | Evidence | What closes it |
|---|---|---|
| `.skills-engine/engine-manifest.yaml` carries a stale `plugin_exclusions` entry for `country-context/*` (lines 40 to 42). Its reason says the files are "not standalone plugin skills" and that "the generator scans skills/ only" | `.claude-plugin/plugin.json` lists all three country-context skills. `node scripts/generate-plugin-manifest.js --engine . --root . --check` exits 0 ("plugin.json is current", 137 skills). With the default `--root skills` it exits 1 (134 on disk). The portfolio renderer (`scripts/render_host_files.py` lines 392 to 404 in the coordination package) requires every `SKILL.md` to be in `plugin.json` or in `plugin_exclusions`; these three are in `plugin.json`, so the exclusion is redundant and its reason is wrong | Delete the entry, then run the coordination package's `render_host_files.py --check`. The wave did not edit the manifest because it is configuration |
| `install.sh` is committed without its executable bit (`git ls-files -s install.sh` shows mode 100644) | `./install.sh` fails with "Permission denied" on Linux; `bash install.sh` works. The README now says `bash install.sh` | `git update-index --chmod=+x install.sh`, then commit |
| The manifest's `validation` list holds one command (the catalogue gate) and starts it with bare `python` | `.skills-engine/engine-manifest.yaml` lines 10 to 18. Routing, link, evidence, sector, exemplar, release-bundle, workbook and unit-test checks, which `CONTRIBUTING.md` calls required, are not declared | Add the checks with `python3` where the platform list includes Linux, and re-run `tests/agent-integration/test_business_plan_agent_contract.py` |
| `scripts/generate-plugin-manifest.js` comments (lines 12, 13 and 28) use former engine names (`digital-research-engine`, `skills-web-dev`) | Text search | The script is the portfolio's shared copy; change it upstream and re-mirror, not here |

## CI

`.github/workflows/skill-quality.yml` installs only `PyYAML==6.0.2`. It does not install LibreOffice, so the 7 engine tests in `tests/test_recalc_check.py` run or skip depending on the runner image, and a skip must be recorded `NOT_ASSESSED`. It does not run `routing_link_check.py`, `quick_validate.py` or the two hook tests. Its evidence step runs the same command that exits 1 locally (4 of 24 rows overdue), so the workflow fails at that step until the rows are renewed. No runner was used in this wave, so none of this was observed on GitHub.

## Skill and reference text that names former engines or restates dated figures

| File | Line | Issue |
|---|---|---|
| `skills/meta-strategy/kaizen-improvement-system/SKILL.md` | 99, 108 | Names `digital-research-engine`; the repository is `digital-research-skills` (the engine's display name is still "Digital Research Engine"). The instruction to resolve it through the global routing table is correct |
| `skills/language/writing-quality/references/english-collocations-and-lexical-precision-2026-09-02.md` | 3 | Path begins `digital-research-engine/docs/continuous-improvement/`; the target exists in the research checkout |
| `skills/industry-guides/retail/references/retail-operating-model-and-engine-plan.md` | 96 | Names the "internal digital-research-engine project" |
| `country-context/INDEX.md` | 26 to 28, 15, 38 | Gives bare planning rates (UGX 3,700, KES 135, TZS 2,700 per USD) with no date and marks all three countries "Complete". `country-context/uganda/SKILL.md` now labels its rate a 2025 assumption to be confirmed (open decision 3 in `06-next-cycle.md`). It also says core skills are `01` to `15` when the pipeline runs to `16-sustainability-strategy`, and tells authors to update `CLAUDE.md`, which holds no country list |
| `references/` and skills restating tax rates | see `06-next-cycle.md`, cross-engine table | Unchanged by this wave; the accounting register entries are still draft |

## Documents deliberately left as they were

- Dated records under `docs/` keep the paths and engine names of their day. A search for a Windows drive path or the Windows web-server folder name found 14 lines in 11 dated records (the July 2026 upgrade pack, the September 2026 audits and kaizen waves, the pass 2 baseline scorecard and `docs/prompt-for-socials.md`); the search excludes URLs, which a looser pattern matched in two contract documents. None were edited.
- `docs/workbook-audits/saas-financial-projection-3yr-5yr.formula-map.md` is a structural report generated on 29 October 2026. The new `docs/README.md` states that its PASS is structural only. Regenerate it when the workbook is rebuilt.
- No `CHANGELOG.md` exists and none was created: the engine records change in git history and in the dated folders under `docs/kaizen/`. The pass 2 changes by theme, with commit hashes, are in `05-final-report.md` in this folder. If a changelog is wanted, that table is its first entry.

## Not assessed in the documentation wave

| Item | Reason |
|---|---|
| `/plugin marketplace add`, `/plugin install`, `codex plugin marketplace add .` and `codex plugin add` lines in the README | Neither the Claude plugin command nor the `codex` binary was run; the README already says local installation checks do not establish public-directory acceptance |
| Node.js 18 as the installer minimum | The installer's own error message states it; the installer and both hook tests ran on Node.js 22 only |
| Isolated native Codex discovery test quoted in the README footer (`-m gpt-6-luna ...`) | Carried from an earlier cycle; no Codex run here |
| Windows PowerShell form of the commands (`python` for `python3`, `install.ps1`) | No PowerShell is installed on the workstation |
| A Linux GitHub runner | Nothing was pushed |
| The wording of each workbook's own sheet-by-sheet description in `templates/README-financial-models.md` | Paths, commands, the lender-use claim and the verification block were checked; the per-sheet feature lists were not compared with each workbook |

## Portfolio-managed router blocks

The shared renderer (`scripts/render_host_files.py --render-router-blocks --engine <this checkout>`, run from a frozen snapshot of the coordination package) reported `{"changed": [], "dry_run": true}` before any edit and the same after the last edit: this engine's `AGENTS.md` already carries the path-free wording for the three managed sentences, and no managed sentence was edited by hand.

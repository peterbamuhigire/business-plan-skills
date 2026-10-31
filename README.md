# Business Plan Skills

Business Plan Skills is a set of 137 skills that help Claude Code or Codex write, test and release business plans. It covers bankable plans for lenders, investor-grade plans, standalone marketing plans, pitch decks, and the strategy, finance and policy documents around them.

It is for founders, consultants, boards, lenders and investors, mainly in East and Central Africa. Use it when a plan must keep assumptions apart from evidence, tie its narrative to its model, and claim no more than the evidence reviewed.

## At a glance

- **137 active skills** in 16 categories: 134 under `skills/` and 3 country-context skills for Uganda (the default), Kenya and Tanzania.
- **Routing:** on 31 October 2026, 80 of 80 test prompts reached the right skill in the top three, and 64 of 80 (80.0%) reached it first.
- **Checks:** 13 of the 14 checks listed under [Validate](#validate) exit 0. The evidence-register check exits 1 because 4 of 24 source rows are overdue.
- **Install:** a project-scope install writes 903 files, including 137 `SKILL.md` files, and `doctor` reports 0 missing.
- **Audit score:** 50.0 out of 100 on 31 October 2026, against a target of 95.
- **Not a lender model:** the seven shipped Excel workbooks are starting structures. The SaaS projection workbook has no balance sheet and no debt schedule.

## Start here

1. Install in Claude Code:

   ```text
   /plugin marketplace add https://github.com/peterbamuhigire/business-plan-skills
   /plugin install business-plan@chwezi-business-plan
   ```

   The installer script, Codex and manual routes are under [Install and update](#install-and-update).
2. Check the engine from a clone. This needs Python 3.11 or later and PyYAML:

   ```sh
   git clone https://github.com/peterbamuhigire/business-plan-skills
   cd business-plan-skills
   python3 -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json
   ```

   Expect `active skills: 137` and `fully compliant: 137`, with exit 0.
3. Ask for work in plain words, for example "Run the client intake and list the missing assumptions." The [business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md) runs a whole engagement, and [Find the right skill](#find-the-right-skill) lists other starting points.

**Contents**

- [When to use it](#when-to-use-it)
- [Find the right skill](#find-the-right-skill)
- [How it works](#how-it-works)
- [What is inside](#what-is-inside)
- [Install and update](#install-and-update)
- [Validate](#validate)
- [Quality and improvement](#quality-and-improvement)
- [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved)
  - [Wrong numbers and spreadsheet checks](#kept-changes-wrong-numbers-and-spreadsheet-checks)
  - [Evidence, country context and packaging](#kept-changes-evidence-country-context-and-packaging)
  - [Routing and documentation](#kept-changes-routing-and-documentation)
  - [How it was measured, and what was reverted](#how-the-kaizen-was-measured-and-what-was-reverted)
- [What is still open](#what-is-still-open)
- [Cited sources](#cited-sources)
- [Contributing, author and licence](#contributing-author-and-licence)

## When to use it

Use this engine when the work is a business plan, or a document that feeds or tests one:

- a full plan, from client intake and evidence design to assembly and release;
- a bankable plan for a bank or development-finance institution, or an investor memorandum and pitch deck;
- a financial model, bankability score, stress test, valuation or investment-committee rehearsal;
- a standalone marketing plan, a grant proposal or a quarterly execution plan;
- a finance, procurement, HR, governance, grants, controls or monitoring-and-evaluation manual.

Other Chwezi engines are consulted alongside this one, never instead of it:

- the Chwezi Accounting Doctrine engine (`chwezi-accounting-doctrine`) for IFRS and IAS, tax and controls;
- `chwezi-design-engine` for the look of any deliverable;
- the Digital Research Engine (GitHub repository `chwezi-research-engine`; catalogue id `digital-research-skills`) for current facts;
- `proposal-skills` for tenders and PPDA submissions.

Resolve each through your engine-routing table. No path to a sibling engine is stored here.

## Find the right skill

Each row is a task that the routing fixtures in `tests/routing-fixtures.json` already use. The [skill catalogue](docs/skill-catalogue.md) lists all 137 skills.

| If you need to | Use | What you get |
|---|---|---|
| Run a whole plan from intake to release | [`business-plan-orchestrator`](skills/meta-strategy/business-plan-orchestrator/SKILL.md) | Staged engagement with evidence checkpoints and a release decision |
| Capture scope, facts and missing assumptions | [`00-client-intake`](skills/pipeline/00-client-intake/SKILL.md) | Draft project brief, evidence gaps and an assumptions register |
| Write the financial projections section | [`10-financial-projections`](skills/pipeline/10-financial-projections/SKILL.md) | Three statements, assumptions and a workbook model |
| Score a plan against lender criteria | [`meta-bankability-scoring`](skills/meta-finance/meta-bankability-scoring/SKILL.md) | Debt-service capacity, security, repayment logic and blockers |
| Stress-test revenue, margin and debt service | [`meta-financial-stress-test`](skills/meta-finance/meta-financial-stress-test/SKILL.md) | Downside cases for revenue, working capital, break-even and runway |
| Value a company | [`meta-valuation`](skills/meta-finance/meta-valuation/SKILL.md) | DCF, multiples and venture methods, with sensitivity and dilution |
| Rehearse a lender, DFI or grant committee | [`meta-investment-committee-red-team`](skills/meta-finance/meta-investment-committee-red-team/SKILL.md) | Role rounds, a vote, dissent and conditions |
| Build a standalone marketing plan | [`marketing-plan-orchestrator`](skills/marketing-sales/marketing-plan-orchestrator/SKILL.md) | Situation analysis through budget, KPIs and control |
| Write a grant proposal | [`11b-grant-proposal`](skills/pipeline/11b-grant-proposal/SKILL.md) | Donor outcomes, logframe, budget narrative and sustainability case |
| Draft a procurement policy and manual | [`procurement-policy-and-manual`](skills/advisory-deliverables/procurement-policy-and-manual/SKILL.md) | Thresholds, methods, approval limits and a contracts committee |
| Localise a plan for one country | [`uganda`](country-context/uganda/SKILL.md), [`kenya`](country-context/kenya/SKILL.md) or [`tanzania`](country-context/tanzania/SKILL.md) | Currency, tax, regulation, labour, banking and risk context to verify |
| Check a finished plan for filler | [`ai-slop-audit`](skills/meta-utility/ai-slop-audit/SKILL.md) | Findings on generic prose and unsupported statistics, without a rewrite |

## How it works

[`AGENTS.md`](AGENTS.md) is the router. It works with any runner. [`CLAUDE.md`](CLAUDE.md) imports it for Claude Code. Always-on principles live in [`rules/`](rules/).

A skill is a directory that holds a `SKILL.md` file and, for deeper material, a `references/` folder. The router names the right `SKILL.md`, and the assistant reads it from disk.

Full plans start at the [business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md). It runs an engagement through these stages:

- client intake and evidence design;
- sixteen numbered plan sections, with a grant-proposal variant;
- the financial model and the investment-committee challenge;
- assembly and release.

Standalone marketing plans start at the [marketing-plan orchestrator](skills/marketing-sales/marketing-plan-orchestrator/SKILL.md).

Three rules hold across every skill:

- Assumptions and evidence are kept apart.
- The narrative and the model must reconcile.
- A release claim goes no further than the evidence actually reviewed.

Multi-phase work follows the [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md). It sets scoped work packages, evidence checkpoints, context hygiene, least agency, and sanitised handling of external content.

Country context for Uganda (the default), Kenya and Tanzania supplies currency, tax, regulatory, labour and banking facts. Verify each one at the time of writing.

The engine works to standards that it cites directly:

- IFRS 15, IAS 20, IAS 21, IFRS 13 and IFRS for SMEs for revenue, grants, foreign currency and fair value in projections. Accounting doctrine itself is deferred to the Chwezi Accounting Doctrine engine.
- COSO and ISO 31000 for internal control and risk.
- The IFC Performance Standards (2012) for environmental and social management in development-finance submissions.
- ISO/IEC 27001 and ISO/IEC 42001 for security and AI governance in SaaS due diligence.
- The ICC/ESOMAR International Code for market research.
- The PPDA framework for public procurement in Uganda.

## What is inside

The engine has 137 active skills: 134 under [`skills/`](skills/) and 3 under [`country-context/`](country-context/). Templates in [`templates/`](templates/) are not counted, and neither are sector guide files that are references rather than skills.

| Category | Folder | Skills |
|---|---|---:|
| Plan pipeline | [`skills/pipeline/`](skills/pipeline/) | 49 |
| Strategy and validation | [`skills/meta-strategy/`](skills/meta-strategy/) | 22 |
| Finance and investor readiness | [`skills/meta-finance/`](skills/meta-finance/) | 12 |
| SaaS | [`skills/saas/`](skills/saas/) | 11 |
| ICT and e-commerce | [`skills/ict/`](skills/ict/) | 4 |
| Marketing and sales | [`skills/marketing-sales/`](skills/marketing-sales/) | 4 |
| Pricing and go-to-market | [`skills/meta-pricing-gtm/`](skills/meta-pricing-gtm/) | 3 |
| Pitch | [`skills/meta-pitch/`](skills/meta-pitch/) | 3 |
| Advisory deliverables | [`skills/advisory-deliverables/`](skills/advisory-deliverables/) | 7 |
| Board and investor reporting | [`skills/meta-reporting/`](skills/meta-reporting/) | 2 |
| Language | [`skills/language/`](skills/language/) | 3 |
| Writing and content | [`skills/writing-content/`](skills/writing-content/) | 5 |
| Utility and quality | [`skills/meta-utility/`](skills/meta-utility/) | 6 |
| Sustainability | [`skills/meta-sustainability/`](skills/meta-sustainability/) | 1 |
| Industry guides | [`skills/industry-guides/`](skills/industry-guides/) | 2 |
| Country context | [`country-context/`](country-context/) | 3 |
| **Total** | | **137** |

The full list, with a one-line statement of what each skill does, is in the [skill catalogue](docs/skill-catalogue.md).

Beyond the plan pipeline, the skills cover:

- business-model design, market validation and competitive intelligence;
- pricing, valuation, bankability scoring, stress testing and due diligence;
- SaaS, AI and agent-product economics, ICT and e-commerce businesses, and hospitality;
- pitch preparation and organisational policy manuals.

The engine produces:

- complete business plans and plan sections, bankable plans for banks and development-finance institutions, investor memoranda and pitch decks;
- Excel financial models, built by the scripts in [`scripts/build-financial-models/`](scripts/build-financial-models/);
- bankability scores, stress tests and valuations;
- marketing plans, competitive-intelligence reports, grant proposals and quarterly execution plans;
- finance, procurement, HR, governance, grants, controls and monitoring-and-evaluation manuals.

### The shipped workbooks are not lender models

The seven shipped Excel workbooks are starting structures, not finished lender models. The SaaS projection workbook has no balance sheet and no debt schedule. Its Adjusted EBITDA adds back depreciation and share-based pay that its operating expenses never charge.

[Section 0 of its reference](skills/pipeline/10-financial-projections/references/saas-financial-projection-template-3yr-5yr.md) lists each gap with cell references and gives the procedure for a lender case. The open fix is recorded under [What is still open](#what-is-still-open).

## Install and update

### Prerequisites

- [Claude Code](https://claude.com/claude-code) or Codex.
- Node.js 18 or later, for the installer scripts and the hook tests. The installer and both hook test files ran on Node.js 22 on 31 October 2026. Version 18 is the minimum the installer states, and it was not tested.
- Python 3.11 or later, for the validators. CI uses Python 3.12 with `PyYAML==6.0.2`. The 31 October 2026 run used Python 3.14.8 with PyYAML 6.0.3. The validators and the test suite need only PyYAML.
- Optional: LibreOffice for workbook recalculation, `xlsxwriter` for the model builders, and the packages in [`tools/requirements.txt`](tools/requirements.txt) for `tools/scrape_metrics.py`. [What each check needs](#what-each-check-needs) says which check uses which.

### Claude Code plugin

The repository ships a marketplace in [`.claude-plugin/`](.claude-plugin/marketplace.json):

```text
/plugin marketplace add https://github.com/peterbamuhigire/business-plan-skills
/plugin install business-plan@chwezi-business-plan
```

### Installer scripts

[`install.sh`](install.sh) and [`install.ps1`](install.ps1) call `scripts/install-engine.js`. It copies the engine into `~/.claude` (`--scope user`, the default) or into `.claude` under the current directory (`--scope project`).
Add `--dry-run` to see the plan without writing anything, or `--json` for machine-readable output.

```sh
git clone https://github.com/peterbamuhigire/business-plan-skills
cd business-plan-skills
bash install.sh --scope project --dry-run
bash install.sh --scope project
```

Run the script with `bash`. `install.sh` is committed without its executable bit, so `./install.sh` fails with "Permission denied" on Linux and macOS. On Windows PowerShell, use `.\install.ps1 --scope project`.

A project-scope install into an empty directory on 31 October 2026 wrote 903 files. They include 137 `SKILL.md` files, the hooks and the rules. Then `node scripts/install-engine.js doctor --scope project` reported 0 missing and 0 locally modified.

### Update

For an installer-script install, pull the repository and run the installer again with the same scope. On 31 October 2026 a second run into the same directory succeeded, and `doctor` still reported 0 missing and 0 locally modified. That test used an unchanged checkout.
It shows that the command runs, not that a changed tree upgrades cleanly. A plugin install updates through Claude Code's plugin manager, which was not tested.

### Codex

Codex reads [`AGENTS.md`](AGENTS.md) as the router. Before substantive work, run the model-policy check described in [`.codex/README.md`](.codex/README.md): `python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`. Claude skips that section.

The shared [compatible plugin manifest](.claude-plugin/plugin.json) and the [repo-local marketplace](.agents/plugins/marketplace.json) expose the skills through Codex's local marketplace path. From a supported Codex CLI or client, add the repository marketplace and install the plugin:

```sh
codex plugin marketplace add .
codex plugin add business-plan@business-plan-local
```

These local installation checks do not establish public-directory acceptance. The Claude marketplace and the Codex repo marketplace are distinct catalogues.

### Manual use

Clone the repository, read [`CLAUDE.md`](CLAUDE.md) (Claude Code) or [`AGENTS.md`](AGENTS.md) (any runner), then open the `SKILL.md` that the router names. Skills are read directly from disk. No registration is required.

## Validate

### Checks

Run these from the repository root. The commands use `python3` (use `python` on Windows) and change no tracked file. Python bytecode caches are git-ignored, and `-B` avoids them. [What each check needs](#what-each-check-needs) says which check uses PyYAML, Node.js, LibreOffice or `xlsxwriter`.

```sh
python3 -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json
python3 -X utf8 scripts/routing_smoke_test.py --threshold 1.0 --report --min-precision-at-1 0.80
python3 -X utf8 scripts/routing_link_check.py
python3 -X utf8 scripts/check_text_integrity.py
python3 -X utf8 scripts/check_package_file_budget.py
python3 -X utf8 scripts/source_ingestion_guardrail.py
python3 -X utf8 tools/evidence-register/refresh_evidence_register.py --check
python3 -X utf8 tools/sector-gates/validate_sector_gates.py
python3 -X utf8 tools/exemplar-packs/validate_exemplar_packs.py
python3 -X utf8 scripts/build-financial-models/verify_workbooks.py
for bundle in examples/full-plan-packages/*/release-bundle.json; do
  python3 -X utf8 tools/release-gate/validate_release_bundle.py "$bundle"
done
python3 -X utf8 -m unittest discover -s tests -p "test_*.py"
python3 -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py <skill-directory>
node hooks/test-destructive-bash-gate.js
node hooks/test-plugin-hook-config.js
```

CI runs the catalogue, routing, evidence, sector-gate, workbook, exemplar-pack, release-bundle and unit-test checks, plus a `compileall`. The workflow is [`skill-quality.yml`](.github/workflows/skill-quality.yml).

[`source-ingestion-guardrail.yml`](.github/workflows/source-ingestion-guardrail.yml) runs the guardrail. The text-integrity and file-budget checks also run inside `validate_skill_engine.py`. `routing_link_check.py`, `quick_validate.py` and the hook tests are not in CI.

### Results on 31 October 2026

These runs used Python 3.14.8 and Node.js 22.

| Check | Exit | Result |
|---|---:|---|
| `validate_skill_engine.py` | 0 | 137 active skills, 137 compliant, no failure counts |
| `routing_smoke_test.py` | 0 | 80 of 80 top-three matches; precision@1 64 of 80 (80.0%); 46 of 137 skills have a fixture |
| `routing_link_check.py` | 0 | 7 surfaces, 0 failures |
| `check_text_integrity.py` | 0 | No control characters, glued numeric ranges, host paths or known stripped lines |
| `check_package_file_budget.py` | 0 | Both counts under the 5,000-entry cap |
| `source_ingestion_guardrail.py` | 0 | 0 findings, 0 content warnings |
| `refresh_evidence_register.py --check` | **1** | 4 of 24 register rows overdue; it fails until they are renewed, see [Quality and improvement](#quality-and-improvement) |
| `validate_sector_gates.py` | 0 | 12 sector families, 24 gates (structure only) |
| `validate_exemplar_packs.py` | 0 | 4 packs, 32 artefacts |
| `verify_workbooks.py` | 0 | 7 workbooks; reads ZIP entries and sheet names only, not formulas or values |
| `validate_release_bundle.py` on each example pack | 0 each | Structurally valid; all four report `decision=blocked` |
| unit tests | 0 | 130 tests |
| `quick_validate.py` on every skill directory | 0 | 137 directories, 0 failures |
| hook tests | 0 | 61 of 61 and 7 of 7 |

### What each check needs

The table comes from the imports in the code and from running the checks with and without each tool. The PyYAML row comes from the `import yaml` lines only, because no check was run without PyYAML.

| Needs | Checks |
|---|---|
| Python standard library only | `routing_link_check`, `check_text_integrity`, `check_package_file_budget`, `source_ingestion_guardrail`, `refresh_evidence_register`, `validate_sector_gates`, `validate_exemplar_packs`, `validate_release_bundle`, `verify_workbooks`, `formula_map` |
| PyYAML | `validate_skill_engine`, `routing_smoke_test`, `quick_validate`, the agent-contract test in the unit-test suite |
| Node.js | The installer and the two hook tests. The hook tests also run `git init` in a temporary directory |
| LibreOffice (`soffice` or `libreoffice` on the path) | `tools/workbook-audit/recalc_check.py`, and 7 of the 19 tests in `tests/test_recalc_check.py` |
| `xlsxwriter` | The seven model builders in `scripts/build-financial-models/` only |
| `openpyxl`, `requests`, `pandas`, `beautifulsoup4`, `xlrd` | `tools/scrape_metrics.py` only (the list in `tools/requirements.txt`) |
| `pytest` | Optional. pytest 9.0.3 passed all 130 tests and 75 subtests in a copy of the repository |
| PowerShell, Pandoc, Mermaid, a browser, a container | None. No check calls them (searched `scripts/`, `tools/`, `tests/` and `.github/`) |

Notes on the table:

- Without LibreOffice, `recalc_check.py` exits 2 (`NOT_ASSESSED`) and the 7 tests are skipped, not passed.
- On a Python without `xlsxwriter`, each model builder stops with `ModuleNotFoundError`. The checks and the unit tests do not import it.
- No check imports `openpyxl`. It was absent from both interpreters used, and every check above still passed.
- The pytest run used `python3 -m pytest -p no:cacheprovider tests`.

### Workbook checks

For a delivered XLSX model, run both workbook tools and keep both reports. `formula_map.py` reads the file's structure and stored values. `recalc_check.py` recalculates a copy in LibreOffice and tests tie-outs on the recalculated values, so two formula-driven sides can be compared.

```sh
python3 -X utf8 tools/workbook-audit/formula_map.py <workbook.xlsx> --require-scenarios --require-balance-checks --require-wired-inputs --json-out <formula-map.json>
python3 -X utf8 tools/workbook-audit/recalc_check.py <workbook.xlsx> --checks <contract.json> --require-checks --require-fresh-cache --json-out <recalc.json>
```

The model builders overwrite the shipped `.xlsx` templates in place. Run them in a copy of the repository, never in the checkout you intend to commit.

All seven builders ran in a copy on 31 October 2026, inside a scratch virtual environment with `xlsxwriter` 3.3.1. `verify_workbooks.py` then passed all seven workbooks. The system Python on that workstation has no `xlsxwriter`, so there each builder stops with `ModuleNotFoundError`.

### Text integrity

`scripts/check_text_integrity.py` scans Markdown outside `docs/` for damage that a structural validator cannot see:

- control or replacement characters;
- glued numeric ranges (`35%` where the source said 3–5%, or two decimals fused into one number), glued year ranges and glued thousands groups;
- host-specific paths (drive letters, a Windows web-server folder, home directories);
- any line whose hash matches one of the 298 stripped copies in `tests/fixtures/stripped-operator-line-hashes.txt`.

It exists because a bulk rewrite in April 2026 removed non-ASCII characters from 47 files and turned numeric ranges into wrong numbers. The Uganda inflation row read `35%` until the original 3–5% was restored on 31 October 2026.

Run against the tree as it stood before the fix (commit `0d1eb51`, with the hash file supplied by `--hashes`), it reported 306 findings and exited 1. Run against the current tree, it exits 0. It also runs inside `validate_skill_engine.py`.
Do not weaken the check or its fixture to make an edit pass. Keep the dash in a numeric range.

### File budget

The file-budget checker applies a fixed 5,000-entry ceiling to both the full checkout and a package-oriented count. It guards against the ZIP entry limit documented for OpenAI plugin submissions ([submission errors](https://developers.openai.com/plugins/deploy/submission-errors)).
The counts are not a built-archive measurement.

## Quality and improvement

Kaizen evidence is kept in dated folders. Each holds the same seven files: scope and evidence, baseline scorecard, backlog, experiment log, validation record, final report and next cycle.
The [documentation index](docs/README.md) lists the audits, kaizen records, source registers and quality gates under `docs/`.

- [`docs/kaizen/2026-10-engine-kaizen/`](docs/kaizen/2026-10-engine-kaizen/05-final-report.md): the 29 October 2026 cycle.
- [`docs/kaizen/2026-10-engine-kaizen-pass-2/`](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md): pass 2, 31 October 2026,
  with the [open work and decisions](docs/kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md) and the [documentation follow-ups](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md).
- [`docs/kaizen/2026-10-readme-kaizen/`](docs/kaizen/2026-10-readme-kaizen/readme-kaizen-record.md): the 31 October 2026 rewrite of this README. It is a scoped cycle and publishes no score.

**Latest published score: 50.0 out of 100** (pass 2, 31 October 2026). The raw mean and the published value, `min(raw, 65)`, are both 50.0, because the cap of 65 does not bind. The target of 95 is not met, and no dimension reaches 65.
The lowest are accessibility and inclusion at 25 (not worked on) and standards currency at 40. The scores are practitioner judgements, not validator pass rates.

| Point in time | Raw mean | Published, `min(raw, 65)` |
|---|---:|---:|
| 29 October, reassessed baseline | 42.5 | 42.5 |
| 29 October, final | 49.0 | 49.0 |
| 31 October, pass 2 fresh baseline | 44.0 | 44.0 |
| 31 October, pass 2 final (current) | 50.0 | 50.0 |

- The 29 October cycle first froze a baseline of 60.0, then recalibrated it to 42.5 because the original ratings overstated structural evidence. Its final report keeps both, and 42.5 is the comparable starting point.
- Pass 2 measured a fresh baseline of 44.0 before it changed anything. That is lower than the 29 October final because pass 2 assessed things that cycle left not assessed. Engine content did not change between the two dates.
- In pass 2, hygiene rose from 40 to 60, applied proof from 40 to 50, and standards currency from 30 to 40. Doctrine, routing, production and handoff, and safety and integrity each rose from 50 to 55.
- Skill depth (50), output readiness (55) and accessibility and inclusion (25) did not move.
- All scores are taken from the evidence files. None was re-measured.

## What the October 2026 kaizen improved

Two cycles ran in October 2026.

- The 29 October cycle: [final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md), [experiment log](docs/kaizen/2026-10-engine-kaizen/03-experiment-log.md) and [validation record](docs/kaizen/2026-10-engine-kaizen/04-validation-record.md).
- Pass 2, on 31 October: [final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md),
  [backlog](docs/kaizen/2026-10-engine-kaizen-pass-2/02-improvement-backlog.md), [experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md) and [validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md).

A documentation wave followed pass 2 on the same day. This section and the four that follow list only changes that were committed and kept. Each short hash was checked with `git show --stat` and is an ancestor of `main`. Real defects come first, ordered by severity.

"Re-measured" means the command was run again on 31 October 2026, on the tree from before the change (extracted from git into a scratch directory) and on the current tree. "From the evidence" means the figure is copied from the file named and was not re-run.
Everything that needs LibreOffice ran with LibreOffice 26.2.6.3. None of the re-measurements ran on Windows, on a CI runner or with a paid model call.

## Kept changes: wrong numbers and spreadsheet checks

- **Wrong numbers in plan content.** A bulk rewrite in April 2026 (`e1a9aa1`) deleted every non-ASCII character from 47 files, so numeric ranges became other numbers. The Uganda inflation row read "35% (2025)" where the source said 3–5%.
  The bankability checklist read "DSCR  1.25x" with the ≥ sign gone.
  - Fix: pass 2 restored the numeric operators on 256 lines in 33 files, each proven to be an exact strip of a pre-damage line (`e762dbc`). It added `scripts/check_text_integrity.py` with 298 known-line hashes, run inside `validate_skill_engine.py` (`423214c`).
  - Re-measured: the current check run on the pre-fix tree reports 306 findings and exits 1 (254 known stripped lines, 25 glued thousands groups, 13 glued year ranges, 4 glued decimal ranges, 10 host paths). On the current tree it exits 0.
  - Not restored: 1,370 lines that lost an em dash, arrow, section sign or box-drawing character. This is an open decision, below.
- **A mismatched workbook passed the spreadsheet check.** A synthetic workbook with cash 100 against balance-sheet cash 80 passed `formula_map.py` with zero findings.
  - Fix (`4b2def5`, 29 October): an opt-in reconciliation contract (literal inputs, a declared subtraction, a tolerance, a numeric stored result) now fails it. `validate_release_bundle.py` recomputes the check from the workbook bytes instead of trusting a supplied PASS report.
  - Re-measured: the check as it stood before the change exits 0 with no findings on that workbook. The current tool with the contract exits 1 with 2 findings.
  - The forged-report and altered-hash cases are unit tests in `tests/test_release_bundle.py`.
  - Limit: verified against synthetic fixtures only. No real client model was reviewed, and the four example release bundles still report `decision=blocked` (re-measured).
- **A formula-driven model could never pass the gate.** In a real three-statement model both sides of a tie-out are formulas, which the contract above rejects. The workbook generators also write formulas without a stored value, so the file stores 0.
  - Fix (`1350d4a`): `tools/workbook-audit/recalc_check.py` recalculates a copy in LibreOffice (throwaway profile, original untouched). It reports stale stored values and error cells, and tests tie-outs on recalculated values. With no engine it exits 2 (`NOT_ASSESSED`), never a pass.
  - Re-measured on the built-to-fail fixtures in the [pass 2 `labs/`](docs/kaizen/2026-10-engine-kaizen-pass-2/labs/): the earlier structural check returns `reconciliation-source-not-literal` for the mismatched and the matched workbook alike.
    `recalc_check.py` fails the mismatch (sides differ by 25.0) and passes the matched one.
  - On the shipped projection workbook it reports 1,772 of 1,852 formula cells whose stored value differs from a recalculation.
  - Limits: seven of its 19 tests need LibreOffice and are skipped without it. The release gate does not yet require it.
- **Dead inputs and prose-satisfied balance checks.** `--require-balance-checks` passed the projection workbook because the words "Ending ARR" matched, although the workbook has no balance sheet. Also, 10 of its 104 numeric inputs fed no formula.
  - Fix (`9c044f2`): `formula_map.py` now reports unreferenced inputs (`--require-wired-inputs`) and requires balance evidence on a formula row. 7 new tests.
  - Re-measured: on the shipped projection workbook `--require-wired-inputs` exits 1 with 10 findings. An independent hand scan in pass 2 found the same count (from the evidence: [`00-scope-and-evidence.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/00-scope-and-evidence.md)).
## Kept changes: evidence, country context and packaging

- **Overdue evidence rows read as current.** Ten of 23 register rows were past their recheck date while marked `verified-current`. The Markdown table still said so after the JSON said `stale`.
  - Fix, 29 October (`c2adec7`): an overdue `verified-current` row is now a validation error, and the ten rows were marked `stale`.
  - Fix, pass 2 (`d4f9943`): each issuer page was read for the claim it supports. Six rows were renewed with narrowed claims. Four stayed stale because the page could not be read (certificate error, HTTP 403, no body text). A primary-source Bank of Uganda row was added.
    The Markdown table is now generated from the JSON and checked for drift.
  - Re-measured: overdue rows 10 of 23 to 4 of 24. An agent did the review, not a human reviewer, and `--check` still exits 1.
- **Country context stated undated or unverified figures as current.** A 2025 exchange rate was labelled current, and the policy rate was a superseded 2025 range. All three country skills restated tax rates as plain facts, while the accounting engine's register holds them as draft.
  - Fix: the Uganda rows are now dated. The Central Bank Rate reads 12.0% from 14 October 2026 with its Bank of Uganda source, and the planning rate is labelled a 2025 assumption (`c392a40`). Each taxation section carries a dated callout that no rate is verified (`24bd64b`).
  - Limits: no tax rate was changed or verified. The Bank of Uganda statement was read on 31 October 2026, first two PDF pages only.
    The register lookups behind the callout are from the evidence ([`04-validation-record.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md)). Kenya and Tanzania rates were not refreshed.
- **The financial-projection reference promised more than the workbook models.** It called the workbook mandatory and listed a balance sheet and debt flows that the workbook lacks. The workbook's Adjusted EBITDA adds back depreciation and share-based pay that its cost lines never deducted.
  - Documented, not fixed (`01997bd`): a scope table in the reference, a decision row and an anti-pattern in the financial-projections skill, an instruction to quote operating income, and recalculation routed from the orchestrator, delivery contract and router.
  - Skill validators and the unit tests passed at that commit (from the evidence). Both pass on the current tree (re-measured). The workbook is still not a lender model.
- **The plugin manifest exposed 134 of 137 skills.** The three country-context skills were missing from the Claude-compatible manifest, and no registered validator checked the package-size limit.
  - Fix: `22a99c6` added the three paths and ran a fixed 5,000-entry cap inside `validate_skill_engine.py` (checker added in `eb8d462`, test runner order fixed in `58817d0`).
  - Re-measured: `plugin.json` lists 134 skill paths before `22a99c6` and 137 after. `node scripts/generate-plugin-manifest.js --engine . --root . --check` exits 0 on the current tree.
    On 31 October 2026 the cap counted 1,681 files in the checkout and 1,169 in a package-oriented subset, not a built archive.
    The checkout count includes `.git`, so it rises with every commit.
  - Isolated Claude and Codex marketplace installs in containers ran on 29 October (from the evidence) and were not repeated. Public-directory acceptance is not assessed.
- **Paths and bytes that resolved nowhere.** The router (8 lines), one skill and the model README named Windows host paths (10 lines in Markdown, plus one in `.gitignore`). All seven workbook generators wrote to folders that no longer exist after the skills moved under `skills/pipeline/`.
  One skill pointed at a wrong sibling-engine path. One retail reference held a stray control byte.
  - Fix: host paths were removed and a host-path signature was added to the text check. The generator paths were repointed and a static test added (`5fc69b9`). The sibling path was corrected (`02395c1`). The byte was removed with a focused test (`970d5ad`).
  - Re-measured: host-path findings 10 to 0. `tests/test_generator_paths.py` on the pre-fix tree fails for all 7 generators and passes on the current tree. Control bytes in the retail file 1 to 0.
  - Limit: the generator test reads target paths and does not run the builders, which need `xlsxwriter`.

## Kept changes: routing and documentation

### Routing and discoverability

**Routing is measured at first place, and an unreadable skill can no longer be skipped silently.** Only top-three recall was measured. A skill whose frontmatter failed to parse was dropped without a message.
This was found when a description containing a colon and a space broke the YAML and the score fell to 78 of 80.

- Fix: `routing_smoke_test.py --report` now prints precision@1, fixture coverage and owned negatives. An unreadable skill fails and names the file. Two descriptions were made specific (`00-plan-assembly`, `10-financial-projections`). 19 fixtures were added (`c7d956a`, `33617d4`).
  The CI workflow passes a precision@1 floor of 0.80 (`015c68b`; not observed on a runner).
- Re-measured, before (at `50d50f9`) and now:

| Measure | At `50d50f9` | Now |
|---|---:|---:|
| Top-three matches | 61 of 61 | 80 of 80 |
| First-place matches | 48 of 61 (78.7%) | 64 of 80 (80.0%) |
| Skills with a fixture | 43 of 137 | 46 of 137 |
| Skills with three positives and two owned negatives | 0 | 5 |

- The 1.3-point rise is not a like-for-like gain: the 61 original fixtures run against the current skills still score 48 of 61.
- The measure is a lexical scorer, not live-agent routing. The floor equals the measured value, so there is no headroom. 46 of 137 skills still share a template description.

### Documentation and portability

- **The documented install command failed and the check list was incomplete.** The README told Linux users to run `./install.sh`, which fails with "Permission denied" because the file is committed without its executable bit (mode 100644, re-measured). It listed four checks.
  - Fix (`8ac52d2`, `ee81598`): the README now uses `bash install.sh`. It lists every check with its 31 October result and the dependency it needs (PyYAML, LibreOffice, `xlsxwriter`, Node.js).
    `AGENTS.md` now uses `python3` in place of `python`, states the CI routing floor, adds the link and text-integrity checks, and carries a known-limits note for the projection workbook and the overdue rows.
  - Re-run for this section: every command in the Checks block exits 0 except the evidence-register check, which exits 1 (four rows overdue). The PowerShell form and the plugin install commands were not run.
- **Contributor and template documents had stale commands and paths.** `CONTRIBUTING.md` had 8 lines with backslash paths or PowerShell cmdlets, and the release-gate document had 1. Both now have none (re-measured by pattern search).
  - The model README listed 17 repository paths in backticks, of which 9 did not exist. It now lists 18 and all exist (ad hoc check, not a registered validator).
  - Its claim that the workbooks were usable for lender presentations was replaced by a pointer to the scope table and the Adjusted EBITDA defect (`e69cff2`, `9756062`).
- **No index of the records under `docs/`.** [`docs/README.md`](docs/README.md) now lists the kaizen records, registers, contracts and dated history. It says that the formula-map PASS is structural only (`8c446ee`).
  [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md) records the configuration, CI and skill-text items that the documentation wave found but did not change (`0a2360e`).

## How the kaizen was measured, and what was reverted

- Each cycle froze its baseline before changing anything (`1b5fb14`, `0d1eb51`) and recorded Five Whys for each critical defect (`9a4730a`, `00afcec`, `f05f1b3`).
  Each new check was shown to fail on a built-to-fail input before it was kept (the table in the [pass 2 validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md)).
- Unit tests: 66 at `d3d5013` (before the 29 October cycle), 80 at `50d50f9`, 130 now. All were re-measured with `python3 -m unittest discover`.
- Two attempts at the `00-plan-assembly` description were reverted before commit. The first lost the words "plan assembly" and regressed a fixture. The second broke the YAML, which exposed the silent-skip defect above.
- A Codex-specific plugin override added in `eb8d462` was removed in `22a99c6`, because it still exposed 134 skills. The shared Claude-compatible manifest exposes all 137.

## What is still open

### Open findings that affect use

- **The shipped SaaS projection workbook is defective for lender use (P0).** It has no balance sheet and no debt schedule. Its Adjusted EBITDA adds back items that were never deducted.
  - Measured on 31 October 2026: `formula_map.py --require-wired-inputs` reports 10 of 104 numeric inputs that no formula uses. `recalc_check.py --require-fresh-cache` finds that 1,772 of 1,852 formula cells store a value that differs from a recalculation.
  - The fix is to rebuild `scripts/build-financial-models/build_financial_projection.py`, with an accounting review of tax, depreciation and share-based pay. It waits on a maintainer decision to install `xlsxwriter` and on that review.
  - Until then, quote operating income rather than Adjusted EBITDA, and follow the lender-case procedure in the workbook's reference.
- **The release gate does not yet require the recalculation report (P0).** `validate_release_bundle.py` can mark a spreadsheet handoff passing on the literal-input contract alone. The four example packs stay blocked.
- **Four register rows are stale.** They are UBOS, KNBS, UNBS and the Bank of Uganda supervision page, whose issuer pages could not be read. So `refresh_evidence_register.py --check` exits 1. Kenya and Tanzania policy and exchange rates were not refreshed.
  - No tax rate is verified. The accounting engine's register holds the Uganda and Kenya VAT, PAYE, income-tax and withholding entries as draft or skeleton entries, and has none for Tanzania.
  - Treat every rate in `country-context/` as a dated figure to confirm before use.
- **Routing is coarse for 46 of 137 skills.** They share one template description, so routing between them rests on the skill name. Precision@1 is 80.0%, and a CI ratchet holds it there. 75 `SKILL.md` files repeat a heading.
- **No complete plan has been rendered**, reviewed for accessibility, or reviewed by a person other than the author.

### Decisions for the maintainer

Three decisions wait on the maintainer:

1. Whether `xlsxwriter` may be installed.
2. Whether the em dashes and symbols stripped in April 2026 should be restored.
3. Whether the Uganda context keeps a fixed UGX planning rate.

### Date-triggered gates

`tools/evidence-register/refresh_evidence_register.py --check` fails when a register row's `recheck_due` date is earlier than today. It already exits 1, and it fails on more rows on the dates below.

The script has no `--as-of` option. The counts were produced by calling its `validate()` function with each future date as `today`, which is the logic the command runs. A row is renewed by reading the issuer page and recording what it shows. Retrieving a URL renews nothing.

| First failing date | Rows that become overdue | Total overdue |
|---|---|---:|
| 31 October 2026 | `UG-UBOS-STATISTICAL-PUBLICATIONS`, `KE-KNBS-STATISTICAL-ABSTRACT`, `UG-UNBS-STANDARDS`, `UG-BOU-SUPERVISION` | 4 |
| 1 December 2026 | `UG-BOU-MPS-OCT-2026` (the October 2026 policy-rate row), `UG-DATAREPORTAL-DIGITAL-2026` | 6 |
| 26 December 2026 | `TZ-ONLINE-CONTENT-REGULATIONS-2020-2022`, `KE-MOBILE-SPEED-SECONDARY-2025` | 8 |
| 26 January 2027 | `UG-UCC-QOS-2024` | 9 |
| 30 January 2027 | The six rows renewed on 31 October 2026 (listed below) | 15 |
| 24 March 2027 | `UG-DPPA-2019-AND-REGULATIONS-2021`, `KE-ODPC-DATA-PROTECTION-REGULATIONS-2021` | 17 |
| 26 March 2027 | The seven remaining rows | 24 |

The six rows renewed on 31 October 2026 are `TZ-NBS-STATISTICAL-ABSTRACT`, `UG-URA-TAX-GUIDANCE`, `UG-URSB-BUSINESS-REGISTRATION`, `UG-NEMA-REGULATIONS`, `UG-UCC-LICENSING` and `GLOBAL-WORLD-BANK-DATA`.

The planned re-audit is 30 November 2026, the day the Bank of Uganda policy-rate row falls due. No other check in the repository reads the date (searched `scripts/`, `tools/`, `tests/` and `.github/`). `tools/scrape_metrics.py` only stamps its output.

## Cited sources

The sources this repository cites as the basis for its skills are listed in [`docs/cited-sources.md`](docs/cited-sources.md). The list holds 200 books, 11 repositories, 14 groups of standards and official sources, and 26 website and article entries.

Books that appear only in reading or wish lists (for example [`05-reading-list.md`](docs/engine-upgrade-july-2026/05-reading-list.md)), and titles supplied without content, are not listed. These are citations only. No book content is reproduced.

## Contributing, author and licence

- **Contributing:** read [`CONTRIBUTING.md`](CONTRIBUTING.md) before you add or change a skill. It covers authoring a skill and validating a change.
- **Author:** Peter Bamuhigire.
- **Licence:** MIT. See [`LICENSE`](LICENSE).

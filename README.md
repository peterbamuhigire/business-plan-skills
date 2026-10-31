# Business Plan Skills

Business Plan Skills is a routed engine of 137 skills for writing, testing and releasing business plans, bankable and investor-grade plans, standalone marketing plans, and the strategy, finance and advisory documents that sit around them. The [business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md) runs an engagement from client intake and evidence design through sixteen numbered plan sections (with a grant-proposal variant), the financial model, investment-committee challenge, assembly and release; specialist skills cover business-model design, market validation, competitive intelligence, pricing, valuation, bankability scoring, stress testing, due diligence, SaaS, AI and agent-product economics, ICT and e-commerce businesses, hospitality, pitch preparation and organisational policy manuals. Country context for Uganda (the default), Kenya and Tanzania supplies currency, tax, regulatory, labour and banking facts, each of which must be verified at the time of writing. The engine keeps assumptions and evidence apart, requires the narrative and the model to reconcile, and limits every release claim to the evidence actually reviewed.

The engine works to standards it cites directly: IFRS 15, IAS 20, IAS 21, IFRS 13 and IFRS for SMEs for revenue, grants, foreign currency and fair value in projections (with accounting doctrine deferred to the Chwezi Accounting Doctrine engine); COSO and ISO 31000 for internal control and risk; the IFC Performance Standards (2012) for environmental and social management in development-finance submissions; ISO/IEC 27001 and ISO/IEC 42001 for security and AI governance in SaaS due diligence; the ICC/ESOMAR International Code for market research; and the PPDA framework for public procurement in Uganda. Its products are complete business plans and plan sections, bankable plans for banks and development-finance institutions, investor memoranda and pitch decks, Excel financial models built by the scripts in [`scripts/build-financial-models/`](scripts/build-financial-models/), bankability scores, stress tests, valuations, marketing plans, competitive-intelligence reports, grant proposals, quarterly execution plans, and finance, procurement, HR, governance, grants, controls and M&E manuals. It serves founders and owner-managers, consultants and programme teams, boards, lenders, development-finance institutions and investors, principally in East and Central Africa.

## Installation

Prerequisites: [Claude Code](https://claude.com/claude-code) or Codex; Node.js 18 or later for the installer scripts and the hook tests (the installer and both hook test files were run on Node.js 22 on 31 October 2026; 18 is the minimum the installer states and was not tested); Python 3.11 or later for the validators (CI uses Python 3.12 with `PyYAML==6.0.2`; the 31 October 2026 run used Python 3.14.8 with PyYAML 6.0.3). The validators and the test suite need only PyYAML. Optional extras are LibreOffice for workbook recalculation, `xlsxwriter` for the model builders, and the packages in [`tools/requirements.txt`](tools/requirements.txt) for `tools/scrape_metrics.py`; the Checks paragraph below says which check needs which.

**Claude Code plugin.** The repository ships a marketplace in [`.claude-plugin/`](.claude-plugin/marketplace.json):

```text
/plugin marketplace add https://github.com/peterbamuhigire/business-plan-skills
/plugin install business-plan@chwezi-business-plan
```

**Installer scripts.** [`install.sh`](install.sh) and [`install.ps1`](install.ps1) call `scripts/install-engine.js`, which copies the engine into `~/.claude` (`--scope user`, the default) or into `.claude` under the current directory (`--scope project`). Add `--dry-run` to see the plan without writing anything, or `--json` for machine-readable output.

```sh
git clone https://github.com/peterbamuhigire/business-plan-skills
cd business-plan-skills
bash install.sh --scope project --dry-run
bash install.sh --scope project
```

Run the script with `bash`: `install.sh` is committed without its executable bit, so `./install.sh` fails with "Permission denied" on Linux and macOS. On Windows PowerShell: `.\install.ps1 --scope project`. A project-scope install into an empty directory on 31 October 2026 wrote 903 files (137 `SKILL.md` files, the hooks and the rules), and `node scripts/install-engine.js doctor --scope project` reported 0 missing and 0 locally modified.

**Codex.** Codex reads [`AGENTS.md`](AGENTS.md) as the router. Before substantive work, run the model-policy check described in [`.codex/README.md`](.codex/README.md): `python <engine-root>/.codex/ensure_model_policy.py --runtime codex --check`. Claude skips that section.

The shared [compatible plugin manifest](.claude-plugin/plugin.json) and
[repo-local marketplace](.agents/plugins/marketplace.json) expose the skills
through Codex's local marketplace path. From a supported Codex CLI/client, add
the repository marketplace and install the plugin with:

```sh
codex plugin marketplace add .
codex plugin add business-plan@business-plan-local
```

These local installation checks do not establish public-directory acceptance.
The Claude marketplace and Codex repo marketplace are distinct catalogues.

**Manual use.** Clone the repository, read [`CLAUDE.md`](CLAUDE.md) (Claude Code) or [`AGENTS.md`](AGENTS.md) (any runner), then open the `SKILL.md` that the router names. Skills are read directly from disk; no registration is required.

**Checks.** From the repository root. The commands use `python3` (use `python` on Windows) and change no tracked file; Python bytecode caches are git-ignored, and `-B` avoids them.

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

CI ([`skill-quality.yml`](.github/workflows/skill-quality.yml)) runs the catalogue, routing, evidence, sector-gate, workbook, exemplar-pack, release-bundle and unit-test checks plus a `compileall`; [`source-ingestion-guardrail.yml`](.github/workflows/source-ingestion-guardrail.yml) runs the guardrail. The text-integrity and file-budget checks also run inside `validate_skill_engine.py`. `routing_link_check.py`, `quick_validate.py` and the hook tests are not in CI.

Result of each command on 31 October 2026 (Python 3.14.8, Node.js 22):

| Check | Exit | Result |
|---|---:|---|
| `validate_skill_engine.py` | 0 | 137 active skills, 137 compliant, no failure counts |
| `routing_smoke_test.py` | 0 | 80 of 80 top-three matches; precision@1 64 of 80 (80.0%); 46 of 137 skills have a fixture |
| `routing_link_check.py` | 0 | 7 surfaces, 0 failures |
| `check_text_integrity.py` | 0 | no control characters, glued numeric ranges, host paths or known stripped lines |
| `check_package_file_budget.py` | 0 | both counts under the 5,000-entry cap |
| `source_ingestion_guardrail.py` | 0 | 0 findings, 0 content warnings |
| `refresh_evidence_register.py --check` | **1** | 4 of 24 register rows overdue; it fails until they are renewed, see [Quality and improvement](#quality-and-improvement) |
| `validate_sector_gates.py` | 0 | 12 sector families, 24 gates (structure only) |
| `validate_exemplar_packs.py` | 0 | 4 packs, 32 artefacts |
| `verify_workbooks.py` | 0 | 7 workbooks; reads ZIP entries and sheet names only, not formulas or values |
| `validate_release_bundle.py` on each example pack | 0 each | structurally valid; all four report `decision=blocked` |
| unit tests | 0 | 130 tests |
| `quick_validate.py` on every skill directory | 0 | 137 directories, 0 failures |
| hook tests | 0 | 61 of 61 and 7 of 7 |

What each check needs. The table comes from the imports in the code and from running the checks with and without each tool; the PyYAML row comes from the `import yaml` lines only, because no check was run without PyYAML:

| Needs | Checks |
|---|---|
| Python standard library only | `routing_link_check`, `check_text_integrity`, `check_package_file_budget`, `source_ingestion_guardrail`, `refresh_evidence_register`, `validate_sector_gates`, `validate_exemplar_packs`, `validate_release_bundle`, `verify_workbooks`, `formula_map` |
| PyYAML | `validate_skill_engine`, `routing_smoke_test`, `quick_validate`, the agent-contract test in the unit-test suite |
| Node.js | the installer and the two hook tests; the hook tests also run `git init` in a temporary directory |
| LibreOffice (`soffice` or `libreoffice` on the path) | `tools/workbook-audit/recalc_check.py` and 7 of the 19 tests in `tests/test_recalc_check.py`. Without it `recalc_check.py` exits 2 (`NOT_ASSESSED`) and the 7 tests are skipped, not passed |
| `xlsxwriter` | the seven model builders in `scripts/build-financial-models/` only; on a Python without it each stops with `ModuleNotFoundError`. The checks and the unit tests do not import it |
| `openpyxl`, `requests`, `pandas`, `beautifulsoup4`, `xlrd` | `tools/scrape_metrics.py` only (the list in `tools/requirements.txt`). No check imports `openpyxl`; it was absent from both interpreters used and every check above still passed |
| `pytest` | optional. pytest 9.0.3 collected the same 130 tests: 130 passed, 75 subtests passed, on a copy of the repository with `python3 -m pytest -p no:cacheprovider tests` |
| PowerShell, Pandoc, Mermaid, a browser, a container | none; no check calls them (searched `scripts/`, `tools/`, `tests/` and `.github/`) |

For a delivered XLSX model, run the two workbook tools and keep both reports. `formula_map.py` reads the file's structure and stored values; `recalc_check.py` recalculates a copy in LibreOffice and tests tie-outs on the recalculated values, so two formula-driven sides can be compared.

```sh
python3 -X utf8 tools/workbook-audit/formula_map.py <workbook.xlsx> --require-scenarios --require-balance-checks --require-wired-inputs --json-out <formula-map.json>
python3 -X utf8 tools/workbook-audit/recalc_check.py <workbook.xlsx> --checks <contract.json> --require-checks --require-fresh-cache --json-out <recalc.json>
```

The model builders overwrite the shipped `.xlsx` templates in place. Run them in a copy of the repository, never in the checkout you intend to commit. All seven ran in a copy, inside a scratch virtual environment with `xlsxwriter` 3.3.1, on 31 October 2026, and `verify_workbooks.py` then passed all seven workbooks. The system Python on that workstation has no `xlsxwriter`, so there each builder stops with `ModuleNotFoundError`.

**Text integrity.** `scripts/check_text_integrity.py` scans Markdown outside `docs/` for the damage a structural validator cannot see: control or replacement characters, glued numeric ranges (`35%` where the source said 3–5%, or two decimals fused into one number), glued year ranges and thousands groups, host-specific paths (drive letters, a Windows web-server folder, home directories), and any line whose hash matches one of the 298 stripped copies recorded in `tests/fixtures/stripped-operator-line-hashes.txt`. It exists because a bulk rewrite in April 2026 removed non-ASCII characters from 47 files and turned numeric ranges into wrong numbers; the Uganda inflation row read `35%` until the original 3–5% was restored on 31 October 2026. Run against the tree as it stood before the fix (commit `0d1eb51`, with the hash file supplied by `--hashes`), it reported 306 findings and exited 1; run against the current tree it exits 0. It also runs inside `validate_skill_engine.py`. Do not weaken the check or its fixture to make an edit pass; keep the dash in a numeric range.

The file-budget checker applies a fixed 5,000-entry ceiling to both the full
checkout and a package-oriented count. This is a guard against the ZIP entry
limit documented for OpenAI plugin submissions; counts are not a built-archive
measurement ([submission errors](https://developers.openai.com/plugins/deploy/submission-errors)).

## Capabilities

137 active skills: 134 under [`skills/`](skills/) and 3 under [`country-context/`](country-context/). Templates in [`templates/`](templates/) and sector guide files that are references rather than skills are not counted.

The seven shipped Excel workbooks are starting structures, not finished lender models. The SaaS projection workbook has no balance sheet and no debt schedule, and its Adjusted EBITDA adds back depreciation and share-based pay that its operating expenses never charge. [Section 0 of its reference](skills/pipeline/10-financial-projections/references/saas-financial-projection-template-3yr-5yr.md) lists each gap with cell references and the procedure for a lender case; the open fix is recorded under [Quality and improvement](#quality-and-improvement).

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

| Category | Skill | What it does |
|---|---|---|
| Plan pipeline | [`00-client-intake`](skills/pipeline/00-client-intake/SKILL.md) | Client intake: scope, facts, evidence gaps and assumptions register. |
| Plan pipeline | [`00-plan-assembly`](skills/pipeline/00-plan-assembly/SKILL.md) | Assembles, reconciles and renders the finished plan, including plan figures. |
| Plan pipeline | [`01-executive-summary`](skills/pipeline/01-executive-summary/SKILL.md) | Executive summary written last from reconciled sections. |
| Plan pipeline | [`02-company-overview`](skills/pipeline/02-company-overview/SKILL.md) | Company overview: legal form, ownership, history, mission and structure. |
| Plan pipeline | [`saas-agent-product-strategy-and-roadmap`](skills/pipeline/03-products-services/saas-agent-product-strategy-and-roadmap/SKILL.md) | Product strategy and roadmap overlay for agent products. |
| Plan pipeline | [`saas-ai-product-strategy-and-roadmap`](skills/pipeline/03-products-services/saas-ai-product-strategy-and-roadmap/SKILL.md) | Product strategy and roadmap overlay for AI-led SaaS. |
| Plan pipeline | [`03-products-services`](skills/pipeline/03-products-services/SKILL.md) | Products and services section. |
| Plan pipeline | [`saas-ai-market-and-tam`](skills/pipeline/04-market-analysis/saas-ai-market-and-tam/SKILL.md) | Market and TAM overlay for AI-led SaaS. |
| Plan pipeline | [`04-market-analysis`](skills/pipeline/04-market-analysis/SKILL.md) | Market analysis and sizing section. |
| Plan pipeline | [`05-target-market`](skills/pipeline/05-target-market/SKILL.md) | Target market and customer segmentation section. |
| Plan pipeline | [`saas-agent-moat-and-wrapper-risk`](skills/pipeline/06-competitive-analysis/saas-agent-moat-and-wrapper-risk/SKILL.md) | Moat and wrapper-risk overlay for agent products. |
| Plan pipeline | [`saas-ai-moat-and-defensibility`](skills/pipeline/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md) | Moat and defensibility overlay for AI-led SaaS. |
| Plan pipeline | [`06-competitive-analysis`](skills/pipeline/06-competitive-analysis/SKILL.md) | Competitive analysis section. |
| Plan pipeline | [`saas-agent-commercial-packaging-economics`](skills/pipeline/07-marketing-sales-strategy/saas-agent-commercial-packaging-economics/SKILL.md) | Commercial packaging economics for agent products. |
| Plan pipeline | [`saas-agent-outcome-pricing-business-case`](skills/pipeline/07-marketing-sales-strategy/saas-agent-outcome-pricing-business-case/SKILL.md) | Business case for outcome-based pricing of agent products. |
| Plan pipeline | [`saas-agent-pricing-strategy`](skills/pipeline/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md) | Pricing strategy overlay for agent products. |
| Plan pipeline | [`saas-ai-pricing-strategy`](skills/pipeline/07-marketing-sales-strategy/saas-ai-pricing-strategy/SKILL.md) | Pricing strategy overlay for AI-led SaaS. |
| Plan pipeline | [`07-marketing-sales-strategy`](skills/pipeline/07-marketing-sales-strategy/SKILL.md) | Marketing and sales section with SMART objectives, channels and a budget reconciled to the P&L. |
| Plan pipeline | [`08-operations-plan`](skills/pipeline/08-operations-plan/SKILL.md) | Operations plan: processes, facilities, suppliers and controls. |
| Plan pipeline | [`coaching-performance-management`](skills/pipeline/09-management-team/coaching-performance-management/SKILL.md) | Coaching and performance-management design for the team section. |
| Plan pipeline | [`saas-agent-talent-strategy`](skills/pipeline/09-management-team/saas-agent-talent-strategy/SKILL.md) | Talent strategy overlay for agent businesses. |
| Plan pipeline | [`saas-ai-talent-strategy`](skills/pipeline/09-management-team/saas-ai-talent-strategy/SKILL.md) | Talent strategy overlay for AI-led SaaS. |
| Plan pipeline | [`09-management-team`](skills/pipeline/09-management-team/SKILL.md) | Management team, governance and staffing section. |
| Plan pipeline | [`saas-agent-deferred-revenue-and-credit-reserves`](skills/pipeline/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md) | Deferred revenue and credit-reserve treatment for agent businesses. |
| Plan pipeline | [`saas-agent-revenue-recognition`](skills/pipeline/10-financial-projections/saas-agent-revenue-recognition/SKILL.md) | Revenue-recognition treatment in agent-business projections. |
| Plan pipeline | [`saas-agent-sla-cogs-treatment`](skills/pipeline/10-financial-projections/saas-agent-sla-cogs-treatment/SKILL.md) | SLA cost-of-revenue treatment for agent businesses. |
| Plan pipeline | [`saas-agent-sla-economics-in-projection`](skills/pipeline/10-financial-projections/saas-agent-sla-economics-in-projection/SKILL.md) | SLA economics carried into the projection model. |
| Plan pipeline | [`saas-agent-unit-economics-and-cogs`](skills/pipeline/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md) | Unit economics and cost of revenue for agent products. |
| Plan pipeline | [`saas-ai-cost-of-tenant-calculator`](skills/pipeline/10-financial-projections/saas-ai-cost-of-tenant-calculator/SKILL.md) | Per-tenant AI cost calculator for SaaS projections. |
| Plan pipeline | [`saas-ai-unit-economics-and-cogs`](skills/pipeline/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md) | Unit economics and cost of revenue for AI-led SaaS. |
| Plan pipeline | [`10-financial-projections`](skills/pipeline/10-financial-projections/SKILL.md) | Financial projections: three statements, assumptions and workbook model. |
| Plan pipeline | [`saas-agent-funding-stage-playbook`](skills/pipeline/11-funding-request/saas-agent-funding-stage-playbook/SKILL.md) | Funding-stage playbook for agent businesses. |
| Plan pipeline | [`saas-agent-investor-narrative-on-sla`](skills/pipeline/11-funding-request/saas-agent-investor-narrative-on-sla/SKILL.md) | Investor narrative for SLA commitments in agent businesses. |
| Plan pipeline | [`saas-ai-funding-stage-playbook`](skills/pipeline/11-funding-request/saas-ai-funding-stage-playbook/SKILL.md) | Funding-stage playbook for AI-led SaaS. |
| Plan pipeline | [`11-funding-request`](skills/pipeline/11-funding-request/SKILL.md) | Funding request: amount, use of funds, instrument and terms. |
| Plan pipeline | [`saas-ai-for-good-grant-proposal`](skills/pipeline/11b-grant-proposal/saas-ai-for-good-grant-proposal/SKILL.md) | AI-for-good grant proposal overlay. |
| Plan pipeline | [`11b-grant-proposal`](skills/pipeline/11b-grant-proposal/SKILL.md) | Grant proposal variant of the funding section. |
| Plan pipeline | [`saas-agent-risk-and-stress-test`](skills/pipeline/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md) | Risk and stress-test overlay for agent businesses. |
| Plan pipeline | [`saas-agent-sla-risk`](skills/pipeline/12-risk-analysis/saas-agent-sla-risk/SKILL.md) | SLA risk overlay for agent businesses. |
| Plan pipeline | [`saas-ai-risk-and-stress-test`](skills/pipeline/12-risk-analysis/saas-ai-risk-and-stress-test/SKILL.md) | Risk and stress-test overlay for AI-led SaaS. |
| Plan pipeline | [`12-risk-analysis`](skills/pipeline/12-risk-analysis/SKILL.md) | Risk analysis: register, mitigation and scenario links. |
| Plan pipeline | [`saas-agent-implementation-timeline`](skills/pipeline/13-implementation-timeline/saas-agent-implementation-timeline/SKILL.md) | Implementation timeline overlay for agent products. |
| Plan pipeline | [`13-implementation-timeline`](skills/pipeline/13-implementation-timeline/SKILL.md) | Implementation timeline with approval gates, critical path and Gantt. |
| Plan pipeline | [`saas-agent-integration-deep`](skills/pipeline/14-ai-integration/saas-agent-integration-deep/SKILL.md) | Deep integration overlay for agent products. |
| Plan pipeline | [`14-ai-integration`](skills/pipeline/14-ai-integration/SKILL.md) | AI integration section, including staged data-foundation investment cases. |
| Plan pipeline | [`15-appendices`](skills/pipeline/15-appendices/SKILL.md) | Appendices: evidence, workings and supporting documents. |
| Plan pipeline | [`saas-agent-sustainability-and-ethics`](skills/pipeline/16-sustainability-strategy/saas-agent-sustainability-and-ethics/SKILL.md) | Sustainability and ethics overlay for agent products. |
| Plan pipeline | [`saas-ai-sustainability-and-ethics`](skills/pipeline/16-sustainability-strategy/saas-ai-sustainability-and-ethics/SKILL.md) | Sustainability and ethics overlay for AI-led SaaS. |
| Plan pipeline | [`16-sustainability-strategy`](skills/pipeline/16-sustainability-strategy/SKILL.md) | Sustainability strategy section. |
| Strategy and validation | [`benchmark-methodology`](skills/meta-strategy/benchmark-methodology/SKILL.md) | Scores a tiered competitor set against a defined benchmark method. |
| Strategy and validation | [`business-plan-orchestrator`](skills/meta-strategy/business-plan-orchestrator/SKILL.md) | Runs a full business-plan engagement from intake and evidence design to assembly and release. |
| Strategy and validation | [`competitive-platform-analysis`](skills/meta-strategy/competitive-platform-analysis/SKILL.md) | Scopes a sourced, tiered competitor set for a competitive-intelligence report. |
| Strategy and validation | [`competitive-report-structure`](skills/meta-strategy/competitive-report-structure/SKILL.md) | Assembles scored competitor profiles into a competitive-intelligence report. |
| Strategy and validation | [`idea-testing`](skills/meta-strategy/idea-testing/SKILL.md) | Tests a business idea, offer or market hypothesis before commitment. |
| Strategy and validation | [`kaizen-improvement-system`](skills/meta-strategy/kaizen-improvement-system/SKILL.md) | Audits and improves this engine or any plan, model or pitch it produces. |
| Strategy and validation | [`meta-business-model-design`](skills/meta-strategy/meta-business-model-design/SKILL.md) | Designs and scores alternative business models before sections are drafted. |
| Strategy and validation | [`meta-consulting-synthesis`](skills/meta-strategy/meta-consulting-synthesis/SKILL.md) | Synthesises analytical sections into a consulting-grade storyline before assembly. |
| Strategy and validation | [`meta-critical-thinking-business-logic`](skills/meta-strategy/meta-critical-thinking-business-logic/SKILL.md) | Tests the business logic of model, market, operations, financials and funding ask. |
| Strategy and validation | [`meta-digital-transformation`](skills/meta-strategy/meta-digital-transformation/SKILL.md) | Digitally enabled growth strategy, operating model or business-model redesign. |
| Strategy and validation | [`meta-due-diligence`](skills/meta-strategy/meta-due-diligence/SKILL.md) | Commercial, operational, legal and financial due diligence. |
| Strategy and validation | [`meta-international-market-entry`](skills/meta-strategy/meta-international-market-entry/SKILL.md) | Chooses a foreign or regional market and entry mode (Porter's Diamond, CAGE, institutional voids). |
| Strategy and validation | [`meta-living-plan-governance`](skills/meta-strategy/meta-living-plan-governance/SKILL.md) | Specifies how a finished plan is maintained, reviewed and updated. |
| Strategy and validation | [`meta-market-validation`](skills/meta-strategy/meta-market-validation/SKILL.md) | Field validation of market assumptions before writing. |
| Strategy and validation | [`meta-monitoring-evaluation`](skills/meta-strategy/meta-monitoring-evaluation/SKILL.md) | Translates a completed plan into execution monitoring. |
| Strategy and validation | [`meta-operational-readiness-due-diligence`](skills/meta-strategy/meta-operational-readiness-due-diligence/SKILL.md) | Tests local executability: banking, tax, licensing, payroll, FX, logistics and compliance. |
| Strategy and validation | [`meta-quarterly-gameplan`](skills/meta-strategy/meta-quarterly-gameplan/SKILL.md) | Converts a completed plan into quarterly execution sprints. |
| Strategy and validation | [`meta-statistics`](skills/meta-strategy/meta-statistics/SKILL.md) | Statistical rigour for market sizing, surveys, forecasts and comparative metrics. |
| Strategy and validation | [`meta-strategic-audit`](skills/meta-strategy/meta-strategic-audit/SKILL.md) | Read-only strategic audit of an existing SME, NGO or growth firm. |
| Strategy and validation | [`meta-strategic-factor-analysis`](skills/meta-strategy/meta-strategic-factor-analysis/SKILL.md) | Turns PESTEL and five-forces scans into EFAS, IFAS, SFAS tables and a TOWS matrix. |
| Strategy and validation | [`meta-strategic-optionality`](skills/meta-strategy/meta-strategic-optionality/SKILL.md) | Exit thesis, exit readiness, sale memorandum and succession options. |
| Strategy and validation | [`meta-strategic-options-evaluation`](skills/meta-strategy/meta-strategic-options-evaluation/SKILL.md) | Generates and chooses strategic options (TOWS, Ansoff, strategy clock, SAFe tests). |
| Finance and investor readiness | [`meta-accounting-finance-review`](skills/meta-finance/meta-accounting-finance-review/SKILL.md) | Reviews projections, funding requests, valuation, budgets and controls in a plan. |
| Finance and investor readiness | [`meta-agent-bankability-and-investor-readiness`](skills/meta-finance/meta-agent-bankability-and-investor-readiness/SKILL.md) | Bankability and investor-readiness gate for agent-product plans. |
| Finance and investor readiness | [`meta-agent-revenue-recognition-policy`](skills/meta-finance/meta-agent-revenue-recognition-policy/SKILL.md) | Revenue-recognition policy for agent businesses facing audit or institutional due diligence. |
| Finance and investor readiness | [`meta-agent-sla-financial-controls`](skills/meta-finance/meta-agent-sla-financial-controls/SKILL.md) | Financial controls for SLA credits, refunds, prepaid credits and outcome pricing. |
| Finance and investor readiness | [`meta-agent-valuation-adjustments`](skills/meta-finance/meta-agent-valuation-adjustments/SKILL.md) | Valuation adjustments specific to agent-product businesses. |
| Finance and investor readiness | [`meta-agent-valuation-overlay-for-sla`](skills/meta-finance/meta-agent-valuation-overlay-for-sla/SKILL.md) | Valuation overlay for agent businesses carrying SLA commitments. |
| Finance and investor readiness | [`meta-ai-bankability-and-investor-readiness`](skills/meta-finance/meta-ai-bankability-and-investor-readiness/SKILL.md) | Readiness gate for AI-led SaaS plans going to fundraise, DFI or grant review. |
| Finance and investor readiness | [`meta-ai-valuation-adjustments`](skills/meta-finance/meta-ai-valuation-adjustments/SKILL.md) | Valuation adjustments for AI-led SaaS in priced rounds, secondaries or acquisitions. |
| Finance and investor readiness | [`meta-bankability-scoring`](skills/meta-finance/meta-bankability-scoring/SKILL.md) | Scores debt-service capacity, security, repayment logic and bankability blockers. |
| Finance and investor readiness | [`meta-financial-stress-test`](skills/meta-finance/meta-financial-stress-test/SKILL.md) | Stress-tests revenue, margins, working capital, break-even, runway and debt service. |
| Finance and investor readiness | [`meta-investment-committee-red-team`](skills/meta-finance/meta-investment-committee-red-team/SKILL.md) | Simulates a lender, DFI, VC, grant or board investment committee against the full plan. |
| Finance and investor readiness | [`meta-valuation`](skills/meta-finance/meta-valuation/SKILL.md) | Values a company by DCF, multiples and venture methods, with sensitivity and dilution. |
| SaaS | [`saas-bankability-and-investor-readiness`](skills/saas/saas-bankability-and-investor-readiness/SKILL.md) | Readiness gate for SaaS equity rounds from pre-seed to growth and DFI equity. |
| SaaS | [`saas-customer-success-operating-model`](skills/saas/saas-customer-success-operating-model/SKILL.md) | Customer-success operating model for SaaS operations and sales sections. |
| SaaS | [`saas-gtm-motion-design`](skills/saas/saas-gtm-motion-design/SKILL.md) | Chooses the SaaS go-to-market motion before the sales section is detailed. |
| SaaS | [`saas-lifecycle-email-and-retention`](skills/saas/saas-lifecycle-email-and-retention/SKILL.md) | Lifecycle email and retention programme for SaaS. |
| SaaS | [`saas-marketing-channel-economics`](skills/saas/saas-marketing-channel-economics/SKILL.md) | Channel economics for SaaS marketing. |
| SaaS | [`saas-mvp-and-product-market-fit-strategy`](skills/saas/saas-mvp-and-product-market-fit-strategy/SKILL.md) | MVP and product-market-fit strategy for pre-PMF SaaS or ICT plans. |
| SaaS | [`saas-pricing-and-packaging-strategy`](skills/saas/saas-pricing-and-packaging-strategy/SKILL.md) | Tiering, packaging and expansion pricing for SaaS. |
| SaaS | [`saas-sales-org-design-and-capacity-planning`](skills/saas/saas-sales-org-design-and-capacity-planning/SKILL.md) | Sales organisation design and capacity planning for SaaS above $1M ARR. |
| SaaS | [`saas-unit-economics-and-cohort-model`](skills/saas/saas-unit-economics-and-cohort-model/SKILL.md) | SaaS unit economics and cohort model for the projections section. |
| SaaS | [`saas-valuation-and-fundraising-strategy`](skills/saas/saas-valuation-and-fundraising-strategy/SKILL.md) | SaaS valuation and fundraising strategy. |
| SaaS | [`saas-vertical-niche-selection`](skills/saas/saas-vertical-niche-selection/SKILL.md) | Selects a vertical niche before a new SaaS or ICT plan is drafted. |
| ICT and e-commerce | [`ecommerce-business-model-diagnostic`](skills/ict/ecommerce-business-model-diagnostic/SKILL.md) | Scores an operating e-commerce business for viability and cross-border readiness, with a 90-day improvement plan. |
| ICT and e-commerce | [`ecommerce-unit-economics-and-cross-border-margin-model`](skills/ict/ecommerce-unit-economics-and-cross-border-margin-model/SKILL.md) | Models landed cost, contribution margin, CAC, LTV and cross-border viability for e-commerce. |
| ICT and e-commerce | [`ict-product-company-business-plan`](skills/ict/ict-product-company-business-plan/SKILL.md) | Business plan for a non-SaaS ICT product company (licensed, embedded or on-premise software). |
| ICT and e-commerce | [`ict-services-firm-business-plan`](skills/ict/ict-services-firm-business-plan/SKILL.md) | Business plan for an ICT services firm, agency or integrator: utilisation, bench, pipeline and productisation. |
| Marketing and sales | [`demand-forecasting`](skills/marketing-sales/demand-forecasting/SKILL.md) | Demand forecasts, stock-out timing, reorder logic and branch or product sales aggregation. |
| Marketing and sales | [`digital-marketing-strategy`](skills/marketing-sales/digital-marketing-strategy/SKILL.md) | Evidence-based digital marketing section: channels, content, campaigns, measurement and budget. |
| Marketing and sales | [`entrepreneurial-demand-generation`](skills/marketing-sales/entrepreneurial-demand-generation/SKILL.md) | Shows how customers move from awareness to conversion, retention and referral. |
| Marketing and sales | [`marketing-plan-orchestrator`](skills/marketing-sales/marketing-plan-orchestrator/SKILL.md) | Builds or audits a standalone marketing plan from situation analysis to budget, KPIs and control. |
| Pricing and go-to-market | [`meta-premium-go-to-market`](skills/meta-pricing-gtm/meta-premium-go-to-market/SKILL.md) | Go-to-market for premium, executive, enterprise and high-ticket buyers. |
| Pricing and go-to-market | [`meta-pricing-strategy`](skills/meta-pricing-gtm/meta-pricing-strategy/SKILL.md) | Tests and defends pricing that matches or undercuts competitors. |
| Pricing and go-to-market | [`meta-website-investment-planning`](skills/meta-pricing-gtm/meta-website-investment-planning/SKILL.md) | Plans and justifies website, online store, portal or SEO investment within a plan. |
| Pitch | [`meta-pitch-preparation`](skills/meta-pitch/meta-pitch-preparation/SKILL.md) | Prepares founders for investor, lender, donor, client or board pitches. |
| Pitch | [`meta-presentation-design`](skills/meta-pitch/meta-presentation-design/SKILL.md) | Designs or audits a presentation deck tied to a plan or proposal. |
| Pitch | [`pitch-deck`](skills/meta-pitch/pitch-deck/SKILL.md) | Builds investor, bank or proposal pitch decks. |
| Advisory deliverables | [`finance-policy-and-manual`](skills/advisory-deliverables/finance-policy-and-manual/SKILL.md) | Drafts a financial management policy or finance and accounting manual. |
| Advisory deliverables | [`governance-and-board-charter`](skills/advisory-deliverables/governance-and-board-charter/SKILL.md) | Drafts a governance framework, board or committee charter and delegation-of-authority matrix. |
| Advisory deliverables | [`grants-management-manual`](skills/advisory-deliverables/grants-management-manual/SKILL.md) | Drafts a grants or donor-funds management manual for a grant recipient. |
| Advisory deliverables | [`hr-policy-manual`](skills/advisory-deliverables/hr-policy-manual/SKILL.md) | Drafts an HR policy manual for an NGO, SME, SACCO, project or public-adjacent body. |
| Advisory deliverables | [`internal-controls-and-risk-framework`](skills/advisory-deliverables/internal-controls-and-risk-framework/SKILL.md) | Drafts an internal-control policy, risk framework, control matrix and risk register. |
| Advisory deliverables | [`me-framework-document`](skills/advisory-deliverables/me-framework-document/SKILL.md) | Drafts a standalone monitoring, evaluation and learning framework. |
| Advisory deliverables | [`procurement-policy-and-manual`](skills/advisory-deliverables/procurement-policy-and-manual/SKILL.md) | Drafts a procurement policy or procurement and disposal manual. |
| Board and investor reporting | [`meta-agent-board-and-investor-reporting`](skills/meta-reporting/meta-agent-board-and-investor-reporting/SKILL.md) | Monthly investor updates for agent businesses. |
| Board and investor reporting | [`meta-board-and-investor-reporting`](skills/meta-reporting/meta-board-and-investor-reporting/SKILL.md) | Board and investor reporting for SaaS companies with external investors. |
| Language | [`east-african-english`](skills/language/east-african-english/SKILL.md) | Professional English for Uganda, Kenya and Tanzania: British spelling, register, courtesy and country tone. |
| Language | [`language-standards`](skills/language/language-standards/SKILL.md) | Grammar, register, terminology and localisation controls for English, French and Kiswahili content. |
| Language | [`writing-quality`](skills/language/writing-quality/SKILL.md) | Edits plans, proposals and pitches for clarity, argument, persuasion and a human voice. |
| Writing and content | [`ai-prompt-writer`](skills/writing-content/ai-prompt-writer/SKILL.md) | Writes prompts for external AI tools (text, image and video). |
| Writing and content | [`blog-idea-generator`](skills/writing-content/blog-idea-generator/SKILL.md) | Generates blog topics, editorial angles and content pipelines. |
| Writing and content | [`blog-writer`](skills/writing-content/blog-writer/SKILL.md) | Writes blog articles and long-form website content. |
| Writing and content | [`content-writing`](skills/writing-content/content-writing/SKILL.md) | Drafts and edits website copy. |
| Writing and content | [`premium-commercial-writing`](skills/writing-content/premium-commercial-writing/SKILL.md) | Persuasive writing for buyers, lenders, investors, boards and grant committees. |
| Utility and quality | [`ai-slop-audit`](skills/meta-utility/ai-slop-audit/SKILL.md) | Audits a finished artefact for AI-generated filler before release. |
| Utility and quality | [`anti-ai-slop`](skills/meta-utility/anti-ai-slop/SKILL.md) | Prevents AI-generated filler while drafting any human-facing artefact. |
| Utility and quality | [`proposal-architect`](skills/meta-utility/proposal-architect/SKILL.md) | Coordinates a proposal, bid, tender, EOI or RFP response to a compliant draft. |
| Utility and quality | [`skill-safety-audit`](skills/meta-utility/skill-safety-audit/SKILL.md) | Read-only safety review of new or changed skills. |
| Utility and quality | [`skill-writing`](skills/meta-utility/skill-writing/SKILL.md) | Creates and reviews skills under the canonical chwezi-dev-engine standard. |
| Utility and quality | [`update-claude-documentation`](skills/meta-utility/update-claude-documentation/SKILL.md) | Synchronises README, AGENTS, CLAUDE and status documents after authorised changes. |
| Sustainability | [`meta-sustainability`](skills/meta-sustainability/SKILL.md) | Identifies sustainability design requirements at the start of an engagement. |
| Industry guides | [`hospitality-hotel-restaurant`](skills/industry-guides/hospitality-hotel-restaurant/SKILL.md) | Bankable plans, feasibility studies and operating plans for hotels, lodges, restaurants and food service. |
| Industry guides | [`industry-guides`](skills/industry-guides/SKILL.md) | Entry point to the sector guide catalogue: operating models, benchmarks, regulation, costs and risks. |
| Country context | [`kenya`](country-context/kenya/SKILL.md) | Kenya currency, tax, regulatory, labour, banking, market and risk context for plans and investment cases. |
| Country context | [`tanzania`](country-context/tanzania/SKILL.md) | Tanzania currency, tax, regulatory, labour, banking, development-plan and risk context. |
| Country context | [`uganda`](country-context/uganda/SKILL.md) | Uganda context (the repository default): currency, tax, regulation, labour, banking, market and risk. |

## Operating contracts

- [`AGENTS.md`](AGENTS.md) is the runner-agnostic router; [`CLAUDE.md`](CLAUDE.md) imports it for Claude Code. Always-on principles live in [`rules/`](rules/).
- Multi-phase work follows the [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md): scoped work packages, evidence checkpoints, context hygiene, least agency, and sanitised handling of external content.
- Full plans start at the [business-plan orchestrator](skills/meta-strategy/business-plan-orchestrator/SKILL.md); standalone marketing plans start at the [marketing-plan orchestrator](skills/marketing-sales/marketing-plan-orchestrator/SKILL.md).
- Sister engines are consulted alongside, never instead: Chwezi Accounting Doctrine (`chwezi-accounting-doctrine`) for IFRS/IAS, tax and controls; `chwezi-design-engine` for the look of any deliverable; the Digital Research Engine (`digital-research-skills`, formerly checked out as `chwezi-research-engine`) for current facts; `proposal-skills` for tenders and PPDA submissions. Resolve each through your engine-routing table; no path to a sibling is stored here.
- The [documentation index](docs/README.md) lists the audits, kaizen records, source registers and quality gates under `docs/`.

## Quality and improvement

Kaizen evidence is kept in dated folders. Each holds the same seven files: scope and evidence, baseline scorecard, backlog, experiment log, validation record, final report and next cycle.

- [`docs/kaizen/2026-10-engine-kaizen/`](docs/kaizen/2026-10-engine-kaizen/05-final-report.md): the 29 October 2026 cycle.
- [`docs/kaizen/2026-10-engine-kaizen-pass-2/`](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md): pass 2, 31 October 2026, with the [open work and decisions](docs/kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md) and the [documentation follow-ups](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md).

What those cycles changed, with commit hashes and before-and-after figures, is under [What the October 2026 kaizen improved](#what-the-october-2026-kaizen-improved); what remains open is under [What is still open](#what-is-still-open).

**Latest published score: 50.0 out of 100** (pass 2, 31 October 2026). The raw mean and the published value, `min(raw, 65)`, are both 50.0, because the cap of 65 does not bind. Pass 2 measured a fresh baseline of 44.0 before it changed anything; the 29 October final was 49.0. The target of 95 is not met and no dimension reaches 65: the lowest are accessibility and inclusion at 25 (not worked on) and standards currency at 40. The scores are practitioner judgements, not validator pass rates. The fresh baseline is lower than the 29 October final because pass 2 measured things that cycle left not assessed; engine content did not change between the two dates.

### What the October 2026 kaizen improved

Two cycles ran in October 2026: the 29 October cycle ([final report](docs/kaizen/2026-10-engine-kaizen/05-final-report.md), [experiment log](docs/kaizen/2026-10-engine-kaizen/03-experiment-log.md), [validation record](docs/kaizen/2026-10-engine-kaizen/04-validation-record.md)) and pass 2 on 31 October ([final report](docs/kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md), [backlog](docs/kaizen/2026-10-engine-kaizen-pass-2/02-improvement-backlog.md), [experiment log](docs/kaizen/2026-10-engine-kaizen-pass-2/03-experiment-log.md), [validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md)). A documentation wave followed pass 2 on the same day. This section lists only changes that were committed and kept. Each short hash was checked with `git show --stat` and is an ancestor of `main`. Real defects come first, ordered by severity.

"Re-measured" below means the command was run again on 31 October 2026 on the tree from before the change (extracted from git into a scratch directory) and on the current tree. "From the evidence" means the figure is copied from the file named and was not re-run. Everything that needs LibreOffice was run with LibreOffice 26.2.6.3. None of the re-measurements ran on Windows, on a CI runner or with a paid model call.

| Point in time | Raw mean | Published, `min(raw, 65)` |
|---|---:|---:|
| 29 October, reassessed baseline | 42.5 | 42.5 |
| 29 October, final | 49.0 | 49.0 |
| 31 October, pass 2 fresh baseline | 44.0 | 44.0 |
| 31 October, pass 2 final (current) | 50.0 | 50.0 |

The 29 October cycle first froze a baseline of 60.0, then recalibrated it to 42.5 because the original ratings overstated structural evidence; its final report keeps both, and 42.5 is the comparable starting point. Pass 2 measured 44.0 afresh because it assessed things the earlier cycle left unassessed; engine content did not change between the two dates. All scores are practitioner judgements taken from the evidence files, not re-measured. In pass 2, hygiene rose from 40 to 60, applied proof from 40 to 50, standards currency from 30 to 40, and doctrine, routing, production and handoff, and safety and integrity from 50 to 55. Skill depth (50), output readiness (55) and accessibility and inclusion (25) did not move.

**Correctness: wrong or misleading content**

- **Wrong numbers in plan content.** A bulk rewrite in April 2026 (`e1a9aa1`) deleted every non-ASCII character from 47 files, so numeric ranges became other numbers: the Uganda inflation row read "35% (2025)" where the source said 3–5%, and the bankability checklist read "DSCR  1.25x" with the ≥ sign gone. Pass 2 restored the numeric operators on 256 lines in 33 files, each proven to be an exact strip of a pre-damage line (`e762dbc`), and added `scripts/check_text_integrity.py` with 298 known-line hashes, run inside `validate_skill_engine.py` (`423214c`). Re-measured: the current check run on the pre-fix tree reports 306 findings and exits 1 (254 known stripped lines, 25 glued thousands groups, 13 glued year ranges, 4 glued decimal ranges, 10 host paths); on the current tree it exits 0. Not restored: 1,370 lines that lost an em dash, arrow, section sign or box-drawing character (open decision, below).
- **A mismatched workbook passed the spreadsheet check.** A synthetic workbook with cash 100 against balance-sheet cash 80 passed `formula_map.py` with zero findings. An opt-in reconciliation contract (literal inputs, a declared subtraction, a tolerance, a numeric stored result) now fails it, and `validate_release_bundle.py` recomputes the check from the workbook bytes instead of trusting a supplied PASS report (`4b2def5`, 29 October). Re-measured: the check as it stood before the change exits 0 with no findings on that workbook; the current tool with the contract exits 1 with 2 findings. The forged-report and altered-hash cases are unit tests in `tests/test_release_bundle.py`. Verified against synthetic fixtures only; no real client model was reviewed, and the four example release bundles still report `decision=blocked` (re-measured).
- **A formula-driven model could never pass the gate.** In a real three-statement model both sides of a tie-out are formulas, which the contract above rejects, and the workbook generators write formulas without a stored value, so the file stores 0. `tools/workbook-audit/recalc_check.py` recalculates a copy in LibreOffice (throwaway profile, original untouched), reports stale stored values and error cells, and tests tie-outs on recalculated values; with no engine it exits 2 (`NOT_ASSESSED`), never a pass (`1350d4a`). Re-measured on the built-to-fail fixtures in the [pass 2 `labs/`](docs/kaizen/2026-10-engine-kaizen-pass-2/labs/): the earlier structural check returns `reconciliation-source-not-literal` for the mismatched and the matched workbook alike; `recalc_check.py` fails the mismatch (sides differ by 25.0) and passes the matched one. On the shipped projection workbook it reports 1,772 of 1,852 formula cells whose stored value differs from a recalculation. Seven of its 19 tests need LibreOffice and are skipped without it. It is not yet required by the release gate.
- **Dead inputs and prose-satisfied balance checks.** `--require-balance-checks` passed the projection workbook because the words "Ending ARR" matched, although the workbook has no balance sheet, and 10 of its 104 numeric inputs fed no formula. `formula_map.py` now reports unreferenced inputs (`--require-wired-inputs`) and requires balance evidence on a formula row (`9c044f2`). Re-measured: on the shipped projection workbook `--require-wired-inputs` exits 1 with 10 findings, the same count an independent hand scan found in pass 2 (from the evidence: [`00-scope-and-evidence.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/00-scope-and-evidence.md)). 7 new tests.
- **Overdue evidence rows read as current.** Ten of 23 register rows were past their recheck date while marked `verified-current`, and the Markdown table still said so after the JSON said `stale`. The 29 October cycle made an overdue `verified-current` row a validation error and marked the ten rows `stale` (`c2adec7`). Pass 2 read each issuer page for the claim it supports: six rows were renewed with narrowed claims, four stayed stale because the page could not be read (certificate error, HTTP 403, no body text), a primary-source Bank of Uganda row was added, and the Markdown table is now generated from the JSON and checked for drift (`d4f9943`). Re-measured: overdue rows 10 of 23 to 4 of 24. The review was done by an agent, not a human reviewer, and `--check` still exits 1.
- **Country context stated undated or unverified figures as current.** A 2025 exchange rate was labelled current, the policy rate was a superseded 2025 range, and all three country skills restated tax rates as plain facts while the accounting engine's register holds them as draft. The Uganda rows are now dated, the Central Bank Rate reads 12.0% from 14 October 2026 with its Bank of Uganda source, the planning rate is labelled a 2025 assumption (`c392a40`), and each taxation section carries a dated callout that no rate is verified (`24bd64b`). No tax rate was changed or verified. The Bank of Uganda statement was read on 31 October 2026, first two PDF pages only; the register lookups behind the callout are from the evidence ([`04-validation-record.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md)). Kenya and Tanzania rates were not refreshed.
- **The financial-projection reference promised more than the workbook models.** It called the workbook mandatory and listed a balance sheet and debt flows the workbook lacks, and the workbook's Adjusted EBITDA adds back depreciation and share-based pay that its cost lines never deducted. Documented, not fixed: a scope table in the reference, a decision row and an anti-pattern in the financial-projections skill, an instruction to quote operating income, and recalculation routed from the orchestrator, delivery contract and router (`01997bd`). Skill validators and the unit tests passed at that commit (from the evidence); both pass on the current tree (re-measured). The workbook is still not a lender model.
- **The plugin manifest exposed 134 of 137 skills.** The three country-context skills were missing from the Claude-compatible manifest, and the package-size limit was checked by no registered validator. `22a99c6` added the three paths and ran a fixed 5,000-entry cap inside `validate_skill_engine.py` (checker added in `eb8d462`, test runner order fixed in `58817d0`). Re-measured: `plugin.json` lists 134 skill paths before `22a99c6` and 137 after, and `node scripts/generate-plugin-manifest.js --engine . --root . --check` exits 0 on the current tree. On 31 October 2026 the cap counted 1,669 files in the checkout and 1,169 in a package-oriented subset, not a built archive. Isolated Claude and Codex marketplace installs in containers were run on 29 October (from the evidence) and were not repeated; public-directory acceptance is not assessed.
- **Paths and bytes that resolved nowhere.** The router (8 lines), one skill and the model README named Windows host paths (10 lines in Markdown, plus one in `.gitignore`); all seven workbook generators wrote to folders that no longer exist after the skills moved under `skills/pipeline/`; one skill pointed at a wrong sibling-engine path; one retail reference held a stray control byte. Host paths were removed and a host-path signature added to the text check, the generator paths were repointed and a static test added (`5fc69b9`), the sibling path was corrected (`02395c1`), and the byte was removed with a focused test (`970d5ad`). Re-measured: host-path findings 10 to 0; `tests/test_generator_paths.py` on the pre-fix tree fails for all 7 generators and passes on the current tree; control bytes in the retail file 1 to 0. The generator test reads target paths and does not run the builders, which need `xlsxwriter`.

**Routing and discoverability**

- **Routing is measured at first place, and an unreadable skill can no longer be skipped silently.** Only top-three recall was measured, and a skill whose frontmatter failed to parse was dropped without a message (found when a description containing a colon and a space broke the YAML and the score fell to 78 of 80). `routing_smoke_test.py --report` now prints precision@1, fixture coverage and owned negatives, an unreadable skill fails and names the file, two descriptions were made specific (`00-plan-assembly`, `10-financial-projections`), 19 fixtures were added (`c7d956a`, `33617d4`), and the CI workflow passes a precision@1 floor of 0.80 (`015c68b`; not observed on a runner). Re-measured: 61 of 61 top-three, 48 of 61 first place (78.7%), 43 of 137 skills with a fixture and none with three positives and two owned negatives at `50d50f9`; 80 of 80, 64 of 80 (80.0%), 46 of 137 and 5 now. The 1.3-point rise is not a like-for-like gain: the 61 original fixtures run against the current skills still score 48 of 61. The measure is a lexical scorer, not live-agent routing, and the floor equals the measured value, so there is no headroom. 46 of 137 skills still share a template description.

**Documentation and portability**

- **The documented install command failed and the check list was incomplete.** `README.md` told Linux users to run `./install.sh`, which fails with "Permission denied" because the file is committed without its executable bit (mode 100644, re-measured), and listed four checks. It now uses `bash install.sh`, lists every check with its 31 October result and the dependency it needs (PyYAML, LibreOffice, `xlsxwriter`, Node.js), and records the Quality and improvement status. `AGENTS.md` now uses `python3` in place of `python`, states the CI routing floor, adds the link and text-integrity checks, and carries a known-limits note for the projection workbook and the overdue rows (`8ac52d2`, `ee81598`). Re-run for this section: every command in the Checks block exits 0 except the evidence-register check, which exits 1 (four rows overdue). The PowerShell form and the plugin install commands were not run.
- **Contributor and template documents had stale commands and paths.** `CONTRIBUTING.md` had 8 lines with backslash paths or PowerShell cmdlets and the release-gate document 1; both now have none (re-measured by pattern search). The model README listed 17 repository paths in backticks of which 9 did not exist; it now lists 18 and all exist (ad hoc check, not a registered validator). Its claim that the workbooks were usable for lender presentations was replaced by a pointer to the scope table and the Adjusted EBITDA defect (`e69cff2`, `9756062`).
- **No index of the records under `docs/`.** [`docs/README.md`](docs/README.md) now lists the kaizen records, registers, contracts and dated history and says that the formula-map PASS is structural only (`8c446ee`). [`07-docs-followups.md`](docs/kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md) records the configuration, CI and skill-text items the documentation wave found but did not change (`0a2360e`).

**Measurement discipline.** Each cycle froze its baseline before changing anything (`1b5fb14`, `0d1eb51`), recorded Five Whys for each critical defect (`9a4730a`, `00afcec`, `f05f1b3`), and showed each new check to fail on a built-to-fail input before keeping it (the table in the [pass 2 validation record](docs/kaizen/2026-10-engine-kaizen-pass-2/04-validation-record.md)). Unit tests: 66 at `d3d5013` (before the 29 October cycle), 80 at `50d50f9`, 130 now, all re-measured with `python3 -m unittest discover`.

**Tried and reverted.** Two attempts at the `00-plan-assembly` description were reverted before commit: the first lost the words "plan assembly" and regressed a fixture; the second broke the YAML, which exposed the silent-skip defect above. A Codex-specific plugin override added in `eb8d462` was removed in `22a99c6` because it still exposed 134 skills; the shared Claude-compatible manifest exposes all 137.

### What is still open

**Open findings that affect use**

- **The shipped SaaS projection workbook is defective for lender use (P0).** It has no balance sheet and no debt schedule, and its Adjusted EBITDA adds back items that were never deducted. Measured on 31 October 2026: `formula_map.py --require-wired-inputs` reports 10 of 104 numeric inputs that no formula uses, and `recalc_check.py --require-fresh-cache` finds that 1,772 of 1,852 formula cells store a value that differs from a recalculation. The fix is to rebuild `scripts/build-financial-models/build_financial_projection.py`, with an accounting review of tax, depreciation and share-based pay. It waits on a maintainer decision to install `xlsxwriter` and on that review. Until then, quote operating income rather than Adjusted EBITDA and follow the lender-case procedure in the workbook's reference.
- **The release gate does not yet require the recalculation report (P0).** `validate_release_bundle.py` can mark a spreadsheet handoff passing on the literal-input contract alone. The four example packs stay blocked.
- **Four register rows are stale** (UBOS, KNBS, UNBS and the Bank of Uganda supervision page, whose issuer pages could not be read), so `refresh_evidence_register.py --check` exits 1. Kenya and Tanzania policy and exchange rates were not refreshed. No tax rate is verified: the accounting engine's register holds the Uganda and Kenya VAT, PAYE, income-tax and withholding entries as draft or skeleton entries, and has none for Tanzania. Treat every rate in `country-context/` as a dated figure to confirm before use.
- **Routing is coarse for 46 of 137 skills.** They share one template description, so routing between them rests on the skill name. Precision@1 is 80.0% and a CI ratchet holds it there. 75 `SKILL.md` files repeat a heading.
- **No complete plan has been rendered**, reviewed for accessibility, or reviewed by a person other than the author.

Three decisions wait on the maintainer: whether `xlsxwriter` may be installed, whether the em dashes and symbols stripped in April 2026 should be restored, and whether the Uganda context keeps a fixed UGX planning rate.

**Date-triggered gates.** `tools/evidence-register/refresh_evidence_register.py --check` fails when a register row's `recheck_due` date is earlier than today. It already exits 1 and fails on more rows on the dates below. The script has no `--as-of` option, so the counts were produced by calling its `validate()` function with each future date as `today`, which is the logic the command runs. A row is renewed by reading the issuer page and recording what it shows; retrieving a URL renews nothing.

| First failing date | Rows that become overdue | Total overdue |
|---|---|---:|
| 31 October 2026 | `UG-UBOS-STATISTICAL-PUBLICATIONS`, `KE-KNBS-STATISTICAL-ABSTRACT`, `UG-UNBS-STANDARDS`, `UG-BOU-SUPERVISION` | 4 |
| 1 December 2026 | `UG-BOU-MPS-OCT-2026` (the October 2026 policy-rate row), `UG-DATAREPORTAL-DIGITAL-2026` | 6 |
| 26 December 2026 | `TZ-ONLINE-CONTENT-REGULATIONS-2020-2022`, `KE-MOBILE-SPEED-SECONDARY-2025` | 8 |
| 26 January 2027 | `UG-UCC-QOS-2024` | 9 |
| 30 January 2027 | the six rows renewed on 31 October 2026: `TZ-NBS-STATISTICAL-ABSTRACT`, `UG-URA-TAX-GUIDANCE`, `UG-URSB-BUSINESS-REGISTRATION`, `UG-NEMA-REGULATIONS`, `UG-UCC-LICENSING`, `GLOBAL-WORLD-BANK-DATA` | 15 |
| 24 March 2027 | `UG-DPPA-2019-AND-REGULATIONS-2021`, `KE-ODPC-DATA-PROTECTION-REGULATIONS-2021` | 17 |
| 26 March 2027 | the seven remaining rows | 24 |

The planned re-audit is 30 November 2026, the day the Bank of Uganda policy-rate row falls due. No other check in the repository reads the date (searched `scripts/`, `tools/`, `tests/` and `.github/`; `tools/scrape_metrics.py` only stamps its output).

## References

Sources the repository itself cites as the basis for its skills. Books that appear only in reading or wish lists (for example [`05-reading-list.md`](docs/engine-upgrade-july-2026/05-reading-list.md)), and titles supplied without content, are not listed. Citations only; no book content is reproduced here.

### Books

- Abrams, R. M. (1993) *The Successful Business Plan: Secrets & Strategies*, 2nd edn, The Oasis Press
- Agrawal, A., Gans, J. and Goldfarb, A. (2018; updated 2022) *Prediction Machines: The Simple Economics of Artificial Intelligence*, Harvard Business Review Press
- Alam, M. M. *Transforming an Idea Into a Business with Design Thinking*, Springer
- Alonzo, R. S. (2007) *The Upstart Guide to Owning and Managing a Restaurant*, 2nd edn, Kaplan
- Amitabh, U. (2022) *Passion Economy and the Side Hustle Revolution*, SAGE
- Anderson, D. R., Sweeney, D. J., Williams, T. A., Camm, J. D. and Cochran, J. J. (2013) *Essentials of Statistics for Business and Economics*, 7th edn, Cengage
- Anthony, R. and Boyd, B. (2014) *Innovative Presentations For Dummies*, Wiley
- ASCM (2022) *Certified in Logistics, Transportation and Distribution (CLTD) Learning System*
- Ashley, A. (2003) *Oxford Handbook of Commercial Correspondence*, Oxford University Press
- Atkinson, C. (2008) *Beyond Bullet Points*, Microsoft Press
- Barnard, F., Akridge, J., Dooley, F. and Foltz, J. (2012) *Agribusiness Management*, 4th edn, Routledge
- Barrow, C. (2009) *Get Backed, Get Big, Get Bought*, Capstone
- Bates (2024) *Valuepreneurs*
- Berger, L. and Berger, D. (eds) (2004) *The Talent Management Handbook*, McGraw-Hill
- Berkman, J. W. (2013) *Due Diligence and the Business Transaction: Getting a Deal Done*, Apress
- Berlin, I. (1953) *The Hedgehog and the Fox*
- Berman, B. and Evans, J. (2013) *Retail Management*
- Berns, G. (2005) *Satisfaction*
- Beveridge, A. and Oberschall, A. (1979) *African Businessmen and Development in Zambia*, Princeton University Press
- Bland, D. and Osterwalder, A. (2020) *Testing Business Ideas*, Wiley
- Blank, S. and Dorf, B. (2012) *The Startup Owner's Manual*, K&S Ranch
- Bly, R. *How to Write and Sell Simple Information*
- Bodnar, K. and Cohen, J. L. (2012) *The B2B Social Media Book*, Wiley
- Bragg, S. (2003) *Essentials of Payroll: Management and Accounting*, Wiley
- Brandenburger, A. and Nalebuff, B. (1996) *Co-opetition*
- Brito, M. (2013) *Your Brand, The Next Media Company*, Que Biz-Tech/Pearson
- Brunson, R. (n.d.) *Proven Secrets to Double Your Traffic, Conversion & Sales for Any Product or Service Online*, SuccessEtc LLC
- Bush, W. *ProductLed Growth*
- Byczynski, L. (2013) *Market Farming Success*, rev. edn, Chelsea Green
- Cadle, J., Paul, D. and Turner, P. (2010) *Business Analysis Techniques: 72 Essential Tools for Success*, BCS
- Cassani, A. *Code Revealed*
- Chaffey, D. and Ellis-Chadwick, F. (2022) *Digital Marketing*, 8th edn
- Cialdini, R. (2021) *Influence*, Harper Business
- Collins, J. (2001) *Good to Great*
- Cooper, B. and Vlaskovits, P. (2010) *The Entrepreneur's Guide to Customer Development*, Cooper-Vlaskovits
- Cotton, B. / FLG Partners (2019) *How to Run a SaaS Business*
- Croll, A. and Yoskovitz, B. (2013) *Lean Analytics*, O'Reilly Media
- Cunningham, L. (2014) *Berkshire Beyond Buffett: The Enduring Value of Values*
- Damerow, G. (2010) *Storey's Guide to Raising Chickens*, 3rd edn, Storey Publishing
- Damodaran, A. (2011) *The Little Book of Valuation*, Wiley
- Dardick, E. (2011) *Get Catering and Grow Sales!*
- Debelak, D. (2006) *Business Models Made Easy*, Entrepreneur Press
- Debelak, D. (2006) *Perfect Phrases for Business Proposals and Business Plans*, McGraw-Hill
- Dennis, A., Wixom, B. H. and Tegarden, D. (2021) *Systems Analysis and Design: An Object-Oriented Approach with UML*, 6th edn, Wiley
- Dietz, T. (2023) *Decisions for Sustainability*, Cambridge University Press
- Digital Business Academy (2021) *Social Media Marketing 2021-22: Beginners Guide to Making Money Online*, self-published
- Dittmer, P. R. and Keefe, J. D. (2009) *Principles of Food, Beverage, and Labor Cost Controls*, 9th edn
- Donnelly and Foley (2003) *Budgeting for Better Performance*, 4th edn, ILM/Elsevier/Pergamon
- Duarte, N. (2010) *Resonate*, Wiley
- Duarte, N. (2012) *HBR Guide to Persuasive Presentations*, Harvard Business Review Press
- Duguin, S. *Cybersecurity for NGOs: Attack Prevention and Threat Response*
- Dumas, M., La Rosa, M., Mendling, J. and Reijers, H. A. (2013) *Fundamentals of Business Process Management*, Springer
- Edwards, J. (ed.) (2007) *Presentation Skill*, Global Media
- Edwards, P., Edwards, S. and Douglas, L. C. (1991) *Getting Business to Come to You*, Jeremy P. Tarcher/Perigee
- Entrepreneur Press (2012) *Start Your Own Restaurant and More*, 4th edn
- Evans, V. (2018) *Strategy Plain and Simple*, Pearson
- Fahey, L. and Randall, R. (eds) (2000) *The Portable MBA in Strategy*, 2nd edn, Wiley
- Feld, B. and Mendelson, J. (2019) *Venture Deals*, 4th edn, Wiley
- Fisher, R. and Ury, W. *Getting to Yes*
- Fleisher, C. and Bensoussan, B. (2007) *Business and Competitive Analysis*, FT Press
- Fortier, J.-M. (2014) *The Market Gardener*, New Society Publishers
- Gallo, C. (2010) *The Presentation Secrets of Steve Jobs*, McGraw-Hill
- Garbugli, É. (2020) *The SaaS Email Marketing Playbook*
- Geddes, B. (2014) *Advanced Google AdWords*, 3rd edn, Wiley/Sybex
- Geffner, A. (1998) *Business English*, 3rd edn, Barron's
- Gerber, M. E. (1995) *The E-Myth Revisited*
- Gerber, M. E. (2008) *Awakening the Entrepreneur Within*, HarperCollins
- Godin, S. (2012) *Startup School* (audio programme)
- Goh, F. (2025) *Innovate to Elevate!*
- Goldratt, E. *The Goal*
- Golding, T. (2024) *Building Multi-Tenant SaaS Architectures*, O'Reilly Media
- Goliger (2023) *The Zero to 100 Million Sales Blueprint*
- Graves *Writing for Profit*
- Grove, A. (1983) *High Output Management*
- Guillebeau, C. (2017) *Side Hustle: From Idea to Income in 27 Days*, Crown Business
- Gupta, N. (2019) *Black Book of English Vocabulary*
- Hahn, F. and Mangun, K. (2003) *Do It Yourself Advertising and Promotion*, 3rd edn
- Haines, S. (2022) *How to Create a Business Case*
- Hair, J. F. Jr., Ortinau, D. J. and Harrison, D. E. (2023) *Essentials of Marketing Research*, 6th edn, McGraw-Hill Education
- Hak, T., Moldan, B. and Dahl, A. L. (eds) (2007) *Sustainability Indicators: A Scientific Assessment*, SCOPE Report 67, Island Press
- Hammer, M. and Champy, J. (1993) *Reengineering the Corporation*
- Hansen *Deploy Empathy*
- Hargis, G. et al. *Developing Quality Technical Information*
- Harris and Lenox (2013) *The Strategist's Toolkit*, Darden
- Harvard Business Review (2014) *Presentations* (20-Minute Manager series), Harvard Business Review Press
- Harvard Business Review (2020) *10 Must Reads on Managing People*, Vol. 2
- Hattori, S. *The McKinsey Edge*
- Hetherington, C. (2024) *OSINT: The Authoritative Guide to Due Diligence*, 3rd edn, Hetherington Group
- Hill, R. (2013) *Pricing for Profit*, Kogan Page
- Holmes, C. *The Ultimate Sales Machine*
- Holt, J. and Farenga, P. (2003) *Teach Your Own*
- Hood (2013) *Words at Work*, WordCraft Global
- Horowitz, B. (2014) *The Hard Thing About Hard Things*, HarperBusiness
- Howson, P. (2003) *Due Diligence: The Critical Stage in Mergers and Acquisitions*, Gower
- Hunter, V. L. with Tietyen, D. (1997) *Business to Business Marketing*, NTC Business Books
- ILM/Elsevier (2003) *Finance for Non-Financial Managers*
- Jia, R. (2025) *Growth Marketing Strategy*
- John, I. (2023) *The Art of Asking ChatGPT for High-Quality Answers*
- Johnson, G., Whittington, R., Scholes, K., Angwin, D. and Regnér, P. (2017) *Exploring Strategy*, 11th edn, Pearson
- Kagan, N. (2024) *Million Dollar Weekend*, Portfolio/Penguin
- Kane, A. (2021) *Social Media Marketing and Online Business 2021*, self-published
- Kawasaki, G. (1989) *The Macintosh Way*
- Kawasaki, G. (2004) *The Art of the Start*
- Kaza, S. (2025) *Unconvention: A Small Business Strategy Guide*, Ideapress Publishing
- Kazanjy, P. (2020) *Founding Sales*
- Keeley, L. et al. (2013) *Ten Types of Innovation*
- Keenan, J. (2019) *Gap Selling*
- Keegan, B. P. (2024) *Dare to Disrupt*
- Keller, G. (2011) *Statistics for Management and Economics, Abbreviated*, 9th edn, Cengage
- Kelley, L. D. and Sheehan, K. B. (c. 2021) *Advertising Management in a Digital Environment*, Routledge
- Kennedy, D. S. (2000) *The Ultimate Sales Letter*, 2nd edn, Adams Media
- Kennedy, D. S. (2004) *No B.S. Sales Success*, 3rd edn, Entrepreneur Press
- Kennedy, D. S. and Marrs, J. (2011) *No B.S. Price Strategy*, Entrepreneur Press
- Kennedy, D. S. and Walsh-Phillips, K. (2018) *Magnetic Marketing*, ForbesBooks
- Keshwani, A. (2023) *55 Digital Marketing Masterpieces*
- Kim, G. et al. *The DevOps Handbook*, 2nd edn, IT Revolution
- Kim, W. C. and Mauborgne, R. (2005) *Blue Ocean Strategy*
- King, J. B. *Business Plans to Game Plans*
- Klaff, O. (2011) *Pitch Anything*, McGraw-Hill
- Knaflic, C. N. *Storytelling with Data*
- Kotler, P., Kartajaya, H. and Setiawan, I. (2023) *Marketing 6.0: The Future Is Immersive*, Wiley
- Kumar, R. et al. (2025) *Technopreneurship and Sustainability*, CRC Press
- Kupsh, J. and Graves, P. R. (1993) *How to Create High-Impact Business Presentations*, NTC Business Books
- Lafley, A. G. and Martin, R. (2013) *Playing to Win: How Strategy Really Works*, Harvard Business Review Press
- Lamplugh, M. (2024) *The AI Marketing Playbook*, 2nd edn, Mercury Learning and Information
- Leleux, B. and van der Kaaij, J. (2019) *Winning Sustainability Strategies*, Palgrave Macmillan
- Levinson, J. C. *Guerrilla Marketing*
- Lima *Fundamentals of Writing*
- Lin, L. C. (2013) *Decode and Conquer*, 2nd edn, Impact Interview
- Maister, D., Green, C. and Galford, R. *The Trusted Advisor*
- Marcos, J., Guesalaga, R., Hough, A. and Vincent, R. (c. 2025) *The High-Performing Key Account Manager*, Kogan Page
- Marshall, P. and Yu, D. (2022) *The Definitive Guide to TikTok Advertising*, Perry Marshall & Associates
- Mathew, J. (2021) *YouTube Marketing 2021*, self-published
- Maxwell *7 Steps to Better Writing*
- Mayer, R. (2009) *Multimedia Learning*, Cambridge University Press
- McDonald, M., Wilson, H. and Chaffey, D. (2024) *Marketing Plans: Profitable Strategies in the Digital Age*, 9th edn, Wiley
- McGowan, B. (2014) *Pitch Perfect*, HarperBusiness
- McNeill, J. (2026) *The Algorithm*
- Mersch, E. (2023) *Hacking SaaS*
- Miller, D. (2017) *Building a StoryBrand*, HarperCollins
- Minto, B. (1987; 2002; Minto International 2010) *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving*
- Mirieri, T. (c. 2015-2016) *SACCO and Chama Business Explained*, self-published
- Mohan, S. *Designing the AI-Driven Data Foundations: Architecture, Principles, and Practice*
- Molenaar, C. *Demand-Driven Business Strategy: Digital Transformation and Business Model Innovation*
- Moore, G. (1991/1999) *Crossing the Chasm*
- Morlidge, S. and Player, S. (2010) *Future Ready: How to Master Business Forecasting*, Wiley
- Murray-Webster, R. and Pullan, P. *Making Risk Management Work*, 2nd edn, Routledge
- Nager, M. et al. (2011) *Startup Weekend*
- National Restaurant Association (1996) *Uniform System of Accounts for Restaurants*, 7th edn
- Ohmae, K. (1982) *The Mind of the Strategist*, McGraw-Hill
- Olson, D. and Wu, D. (2017) *Enterprise Risk Management Models*, 2nd edn, Springer
- Orlicky, J. *Material Requirements Planning*, McGraw-Hill
- Page, S. (2015) *The Power of Business Process Improvement*, 2nd edn, AMACOM
- Palfreyman, J. (2020) *Digital Transformation Handbook: An Agile Approach to Maximise Value*
- Penrith, D. (2009) *Start and Run a Shop*, How To Books
- Pinskey, R. (1997) *101 Ways to Promote Yourself*, Avon Books
- Porter, M. E. (1980) *Competitive Strategy: Techniques for Analyzing Industries and Competitors*, Free Press
- Porter, M. E. (1985) *Competitive Advantage: Creating and Sustaining Superior Performance*, Free Press
- Rasiel, E. (1999) *The McKinsey Way*, McGraw-Hill
- Rasiel, E. and Friga, P. *The McKinsey Mind*
- Raydugin, Y. (2013) *Project Risk Management: Essential Methods for Project Teams and Decision Makers*, Wiley
- Reynolds, G. (2008) *Presentation Zen*, New Riders
- Robinson, D. (2023) *The Digital Marketing Playbook for 2023*, self-published
- Rogers, D. L. (2016) *The Digital Transformation Playbook*, Columbia University Press
- Rogers, E. (1962) *Diffusion of Innovations*
- Rogoff, E. *Bankable Business Plans*
- Rouhiainen, L. (2021) *101 Facebook Marketing Tips and Strategies for Small Businesses*
- Rowse, D. *ProBlogger*
- Rubie, P. and Provost, G. (1997) *How to Tell a Story*, Writer's Digest Books
- Rubinelli, S. *Institutional Health Communication in the Information Age*
- Rumelt, R. (2011) *Good Strategy/Bad Strategy*
- Sardanis, A. (2007) *A Venture in Africa*, I.B. Tauris
- Scharfman, J. (2012) *Private Equity Operational Due Diligence*, Wiley
- Schmidgall, R. S., Hayes, D. K. and Ninemeier, J. D. (2002) *Restaurant Financial Basics*, Wiley
- Shiach, D. (2009) *How to Write Essays*, How To Books
- Silberman, M. (ed.) (2003) *The Active Manager's Tool Kit*, McGraw-Hill
- Simon, A. R. (2022) *Side Hustles For Dummies*, Wiley
- Sinek, S. (2009) *Start With Why*, Portfolio/Penguin
- Smith, S. and Mazin, R. (2004) *The HR Answer Book*, AMACOM
- Stephenson, G. (2019) *Whole Farm Management*, Storey Publishing
- Stockwell, J. and Shaw, H. M. (1994) *Direct Marketing Checklists*, NTC Business Books
- Stutts, P. (2021) *The Undefeated Marketing System*
- Thankaraju (2018) *Startup 500 Business Ideas*
- Tidd, J. and Bessant, J. (2013) *Managing Innovation*, 5th edn, Wiley
- Tiwari, R. (2008) *Retailing*
- Tracy, B. and Partridge, H. (2026) *Make Phenomenal Profits*
- Upadhyay (2024) *Generative AI for Marketing*
- van der Kooij, J. et al. (2018) *The SaaS Sales Method for Account Executives* and *The SaaS Sales Method Fundamentals*, Winning by Design
- Vandeput, N. (2023) *Demand Forecasting Best Practices*, Manning
- Verwijs, C., Overeem, B. and Lennartz, R. (2023) *Practical Product Management for Product Owners*, Scrum.org
- Waite, M. (2023) *Sustainability at Work*, 2nd edn, Routledge
- Walling, R. (2023) *The SaaS Playbook*
- Webb *What Customers Crave*
- Weinberg, G. and Mares, J. (2014) *Traction*, S-curves Publishing
- Wheelen, T. L., Hunger, J. D., Hoffman, A. N. and Bamford, C. E. (2018) *Concepts in Strategic Management and Business Policy*, 15th edn, Pearson
- Whitmell *Business Writing Essentials*
- Willis, T. (2024) *Social Media Marketing in 2024*, self-published
- Wiswall, R. (2009) *The Organic Farmer's Business Handbook*, Chelsea Green
- Wood, M. B. (2003) *The Marketing Plan Handbook*
- *The Chicago Manual of Style*, 17th edn
- Cited by title only in the repository: *Valuation*; *Master Data Storytelling*; *Strategic Storytelling*; *The Bezos Letters*; *Yes!*; *Buyology*; *The Adweek Copywriting Handbook*; *Digital Business Strategy* (2024); *Business Models for E-Commerce*; *Growth Engineering*; *Remarkable Business Growth*; *Think Deeper*; *Small Business 911*; *Strategic DevOps*; *DevOps for PHP Developers*; *Modern DevOps Practices*; *Mastering Project Management Integration and Scope*; *Mathematical Foundations of Big Data Analytics*; *AI-Based Data Analytics: Applications for Business Management*; *The Data Analytics Advantage*; *Data Analytics using Python*; *Introduction to Data Analytics*; *The Nonprofit Guide to Strategic Planning*; *Facility Move Playbook*; *Paid for Your Perspective*

### Repositories

- Archify — https://github.com/tt-a1i/archify — MIT — diagram IR and render-evidence pattern for plan figures (Gantt, process flow, pitch diagrams), paraphrased at commit `0e4949f910a8e390bd3b4933883a4dcabad571be` via the chwezi-sdlc-documentation renderer ([`plan-figures.md`](skills/pipeline/00-plan-assembly/references/plan-figures.md))
- ECC (affaan-m) — https://github.com/affaan-m/ECC — shortform, longform and security guides behind the [runtime-agnostic orchestration contract](docs/operations/runtime-agnostic-orchestration-2026-09-07.md); the Git Bash path fix in `install.sh`
- codex-astra-luna-orchestrator — https://github.com/donvito/codex-astra-luna-orchestrator — concept reference for the Codex model-policy helper, inspected at commit `21f4561656a1b8f2813828520357e3cd1785d50f`; independently implemented ([`.codex/README.md`](.codex/README.md))
- chwezi-dev-engine — https://github.com/peterbamuhigire/chwezi-dev-engine — canonical `skill-writing` standard and byte-mirrored validator scripts
- Business Plan Skills — https://github.com/peterbamuhigire/business-plan-skills — this repository

Repositories studied in the 29 September 2026 ten-repository Kaizen from which this engine adopted something:

- Archify — https://github.com/tt-a1i/archify — MIT — plan-figure pipeline (M10-13, above)
- Impeccable — https://github.com/pbakaus/impeccable — Apache-2.0 — project-context contract: the router reads a `PROJECT.md` with `project_schema: 1` before planning (M10-12, IM-11)
- Ponytail — https://github.com/DietrichGebert/ponytail — MIT — host-file single source and drift control: thin `CLAUDE.md` bridge over `AGENTS.md` (M10-02)
- Superpowers — https://github.com/obra/superpowers — MIT — skill-authoring convergence that turned local `skill-writing` into a pointer to the canonical standard (M10-04)
- Addy Osmani agent-skills — https://github.com/addyosmani/agent-skills — MIT — routing-evaluation work that re-mirrored the canonical `quick_validate.py` (M10-03)
- Graphify — https://github.com/Graphify-Labs/graphify — Apache-2.0 — skill-graph pass that found 151 dangling numbered-skill paths, repointed on 29 September (M10-12)

### Standards and official sources

- Accounting and assurance: IFRS 15 (with ASC 606); IAS 21 (with ASC 830); IAS 20; IFRS 9; IFRS 13; IFRS for SMEs; IPSAS; IPEV Valuation Guidelines; COSO Internal Control and COSO ERM (2017); ISO 31000
- Environmental, social and development finance: IFC (2012) *Performance Standards on Environmental and Social Sustainability*; AfDB Operational Safeguards; Uganda Development Bank (2021) *Environmental and Social Policy*; IIRC (2021) *International Integrated Reporting Framework*; GRI Standards; TCFD; UN Sustainable Development Goals; EU Deforestation Regulation 2023/1115; published ESMPs of AfDB (Zambia Grid Resilience, 2025), FAO/World Bank (Yemen FSRRP, 2025), UNDP (Vietnam Climate Smart Coastal Communities, 2025) and World Bank (Rail Logistics Improvement Project, P170532)
- Security, AI and data protection: ISO/IEC 27001; SOC 2; ISO/IEC 42001; NIST AI RMF; OWASP; GDPR
- Trade, quality and research codes: ISO 9001; ISO 4217; Incoterms (2000/2020); HACCP; ICC/ESOMAR International Code 2025 (https://standards.esomar.org/assets/documents/icc-esomar-code-2025.pdf); FATF; UNBS specifications US 107, US 191, US 386, US 792 and US/IEC 60227
- Donor and procurement rules: EU PRAG Annex III; USAID ADS 303; GIZ procurement standards; Government of Uganda IPPS rates; UNDP Uganda procurement guidelines; PPDA Act 2003 and PPDA Regulations 2023
- Uganda statutes: Income Tax Act Cap. 340; Value Added Tax Act Cap. 349; Excise Duty Act 2014; Stamp Duty Act 2014; Income Tax (Transfer Pricing) Regulations 2011; Employment Act 2006; NSSF Act; Workers' Compensation Act; Occupational Safety and Health Act; Whistleblowers Protection Act 2010; Local Governments (Financial and Accounting) Regulations 2007; Trade Licensing Act Cap. 101; Companies Act 2012; Industrial Property Act Cap. 224 and Regulations 2017; Trademarks Act Cap. 225 and Regulations 2023; Children Act Cap. 59; NEMA Act Cap. 153; Data Protection and Privacy Act 2019 (https://media.ulii.org/files/legislation/akn-ug-act-2019-9-eng-2019-05-03.pdf) and Regulations 2021; Tier 4 Microfinance Institutions and Money Lenders Act 2016; Financial Institutions (Revision of Minimum Capital Requirements) Instrument 2022
- Uganda regulators and official publications: KPMG (2025) *Tax (Amendment) Bills, 2025*; Ministry of Justice and Constitutional Affairs / WIPO (2019) *National Intellectual Property Policy*; URSB (2025) *Intellectual Property Examination Guidelines*; UMRA (2024) *Tier 4 Digital Lending Guidelines*; CMA Uganda (2020) *Handbook*; USE (2021) *Listing Rules*; TASLAF Advocates (2023) *A Legal Guide to Uganda's Financial Sector*; Uganda Bankers' Association *Banking Sector Report 2023*; Norfund / DFCU Bank (2017) *Increasing Access to Finance in Uganda*; Stanbic Bank Uganda (2019) loan terms; Uganda Development Bank lending guidelines; Uganda Credit Guarantee Scheme manual; PSFU SME lending data 2024; BoU CBR data 2025; MSME Financing Gateway for East Africa; UNCDF; aBi Trust; MoICT&NG (2025) *Uganda ICT IP Guidelines*; NRC et al. (2025) *Self-Employment and Small Business Guide for Uganda*; RSM Eastern Africa (2026) *Doing Business in Uganda 2025/26*; Baker Tilly Hem *Business in Uganda*; Uganda Green Growth Development Strategy; NEMA Environmental Sensitivity Atlas
- Uganda statistics: UBOS *Key Economic Indicators* (139th issue), CPI (February 2026), UNHS 2023/24, National Labour Force Survey 2021, Annual Agricultural Survey 2021/22, NPHC 2024, National Livestock Census 2021 (https://www.ubos.org/publications/statistical/)
- Uganda agriculture: MAAIF dairy-farm planning guidelines; MAAIF/UNDP (2014) *NAMA on Climate-Smart Dairy Livestock Value Chains*; MAAIF (2020) goat and sheep guidance; NAGRC&DB guidance; NARO/MAAIF (2015) *Cassava Seed Business Training Manual*; NAARI/MAAIF *Cassava Development in Uganda*; AgriTT/DFID/MAAIF *Building Uganda's Cassava Production Base*; ASHC/IITA/CABI (2014) *Cassava System Cropping Guide*; TAAT/IITA (2022) *Cassava Processing Technology Toolkit Catalogue*; IITA (2005) *Cassava Production, Processing and Marketing in Nigeria*; Abass et al. (2014) *Quality Assurance Manual for Cassava Processing*, ASERECA; UCDA guidance
- Regional and multilateral: UNDP Uganda *Compendium of Investment & Business Opportunities*, Vol. 2; World Bank *Uganda Economic Update* (21st edn, 2023; 26th edn, 2025); World Bank / Government of Uganda (2025) *Uganda Human Capital Development and Growth Review*; IFC/World Bank (2022) *Creating Markets in Uganda*; World Bank/IFC (2022) *Unlocking the Potential of Women Entrepreneurs in Uganda*; World Bank (2019) *Profiting from Parity*; World Bank Worldwide Governance Indicators and *Doing Business 2020*; World Bank World Development Indicators (https://databank.worldbank.org/source/world-development-indicators); AfDB (2025) *African Economic Outlook*; Afreximbank (2025) *African Trade and Economic Outlook* and *African Trade Report*; EAA (2025) *East Africa Macroeconomic Outlook*; AUC/OECD (2025) *Africa's Development Dynamics*; AFRODAD (2021) *Mineral Resource Governance in East Africa*; UNCTAD *Economic Development in Africa Report* (2020) and AfCFTA assessment (2023); EAC (2009) *Common Market Protocol*; IOM/BRMM (2022) labour-mobility report; UNECA (2025) *Eastern Africa's Trade Performance in 2024–2025*; Majune, S. K. (2024) *Export Trade Potential of the EAC under AfCFTA*, EAC/TradeMark Africa; WTO *Global Trade Report 2025*
- Kenya: KNBS *Kenya Facts and Figures 2025*, *Economic Survey 2025* and *2025 Statistical Abstract* (https://www.knbs.or.ke/reports/2025-statistical-abstract/); US Department of State *2025 Kenya Investment Climate Statement*; SECO *Economic Report 2025 — Kenya*; CBK *Monthly Economic Indicators*, average interest rates (2025) and *Revised Risk-Based Credit Pricing Model* (2025); IMF *Article IV Kenya 2024*; Ministry of Mining *Kenya Mining Investment Handbook*; Data Protection Act 2019 (https://new.kenyalaw.org/akn/ke/act/2019/24/eng@2022-12-31); Data Protection (General) Regulations 2021 (https://www.odpc.go.ke/wp-content/uploads/2024/03/THE-DATA-PROTECTION-GENERAL-REGULATIONS-2021-1.pdf); Consumer Protection Act 2012 (https://www.parliament.go.ke/sites/default/files/2017-05/ConsumerProtectionActNo46of2012.pdf); Media Council Code 2025 (https://new.kenyalaw.org/akn/ke/act/ln/2025/88/eng@2025-08-01); Companies (Amendment) Act 2017; Pharmacy and Poisons Act; portals https://itax.kra.go.ke/, https://eprocedures.investkenya.go.ke/, https://lands.go.ke/, http://www.nema.go.ke/
- Tanzania: *FYDP III 2021/22–2025/26*; Tanzania Investment Act No. 10 of 2022; Ministry of Finance *Budget Execution Report FY2025-26 Q1*; Afreximbank *Tanzania Country Brief* (2025); AfDB *Tanzania CSP 2021–2025 Completion Report*; IMF Country Report No. 25/164; Norad (2025); TIC *Quarterly Bulletin* (2025); NBS *Statistical Abstract* (https://www.nbs.go.tz/index.php/statistics/topic/statistical-abstract?page=1); TCRA Online Content Regulations 2020; Fair Competition Act 2003 (https://www.viwanda.go.tz/uploads/documents/sw-1618818548-fca_no_8-2003.pdf); Personal Data Protection Act 2022
- Other African data-protection law: Nigeria NDPR 2019 and DPA 2023; Rwanda Data Protection Law 2021; Ghana DPA 2012; Egypt Data Protection Law 2020
- Uganda regulator portals: https://ura.go.ug/en/dt-faqs/, https://ursb.go.ug/services/business-registration, https://obrs.ursb.go.ug, https://ubiz.go.ug, https://bou.or.ug/supervision, https://www.nema.go.ug/en/regulations/, https://www.unbs.go.ug/content.php?pg=content&src=information-resource-center, https://www.ucc.co.ug/telecommunication-licensing/, UCC QoS report (https://www.ucc.co.ug/wp-content/uploads/2024/12/QOS-August-to-September-2024.pdf), and the NSSF, NGO Bureau, business licensing, NIRA, KCCA, UMRA, UIA, UTB, UNCHE, NDA, NARO, ERB, ERA, Ministry of Education and MAAIF sites listed in [`regulatory-compliance-matrix.md`](skills/pipeline/02-company-overview/references/regulatory-compliance-matrix.md)

### Websites and articles

- Teece, D. (2007) "Explicating dynamic capabilities", *Strategic Management Journal*; Teece, D. (2010) "Business models, business strategy and innovation", *Long Range Planning* 43(2-3)
- Mangematin, V., Ravarini, A. and Sharkey Scott, P. (eds) (2017) special issue on business model innovation, *Journal of Business Strategy* 38(2), Emerald
- Zajonc, R. (1980) "Feeling and thinking", *American Psychologist*; Miller, G. (1956) "The magical number seven", *Psychological Review*; Rogers, T. and Norton, M. (2011), Harvard Business School research on topic changes and trust
- HBR articles cited in the HBR presentations guide: Denning (2004), Guber (2007), Tannen (1995), Morgan (2008)
- Barney (1991) on VRIO; Prahalad and Hamel (1990) on core competence; McClelland (1973) on competencies; Redlich (1955); Reichheld (1994)
- Gabriel, A. I. and Sheya, N. (2023) "Regulatory Framework of the Capital Market in Uganda", *KIULJ* 5(I), https://doi.org/10.59568/KIULJ-2023-5-1-08; Seijjaaka, S. (n.d.) "Challenges to the Growth of Capital Markets in Underdeveloped Economies", TrustAfrica
- Okello, T. J. O. (2011) Centenary Bank loan-recovery research report; Area, A. (2016) UDB loan-performance EMBA proposal; Alton and Hazen (2001); Nsereko (1995)
- Staal, S. and Kaguongo, W. (2003) *The Ugandan Dairy Sub-Sector*, ILRI/IFPRI/USAID; Baltenweck, I. et al. (2007) *Dairy Farming in Uganda*, ILRI Research Report 1; Kabirizi, J. M. et al. (2025) climate-smart dairy study; Balikowa (2011)
- de Melo, J. and Twum, A. (2020) *Supply Chain Trade in East Africa*, FERDI WP 263; Borin and Mancini (2019); Daly, Abdulsam and Gereffi (2016) *Regional Value Chains in East Africa*, IGC; Fritz et al. (2018)
- Infrastructure-finance studies: Dappe and Lebrand (2021); Rozenberg and Fay (2019); Fontagné et al. (2022); Collins et al. (2025); Mensah (2024); Amendolagine, Presbitero and Rabellotti (2024); CRDI (2023)
- *Sustainability Today* (Summer 2022); World Business Journal (2025), WBJAC International
- Crack A Business Kenya sector guides (2012–2018), about forty titles cited across the industry guides
- Umbrex Consulting (2025) *Market Sizing Playbook* and *Customer Retention Playbook*; McKinsey writing on the seven degrees of growth
- SaaS benchmarks: Bessemer Cloud Index and *State of the Cloud*; OpenView SaaS Benchmarks; KeyBanc SaaS Survey; ICONIQ Growth; SaaS Capital Index; NVCA Yearbook; Briter Bridges; ProfitWell pricing research; Tomasz Tunguz; David Skok (forentrepreneurs.com)
- Africa technology markets: GSMA *Mobile Economy*; Disrupt Africa; Partech Africa funding reports; GSMA Intelligence terms of use (https://www.gsmaintelligence.com/gsma-intelligence-terms-of-use/)
- Dave Chaffey, Smart Insights (RACE framework)
- Bivatec blog (beekeeping articles), bivatec.com
- DataReportal *Digital 2026: Uganda* — https://datareportal.com/reports/digital-2026-uganda
- Pew Research Center (22 March 2024) on WhatsApp and Facebook in middle-income nations — https://www.pewresearch.org/short-reads/2024/03/22/whatsapp-and-facebook-dominate-the-social-media-landscape-in-middle-income-nations/
- StatRanker mobile download speeds 2025 — https://statranker.org/digital-innovation/top-100-countries-by-mobile-internet-download-speed-median-2025/
- US Small Business Administration planning guidance — https://www.sba.gov/counseling/plan-your-business/
- Bain strategy practice — https://www.bain.com/consulting-services/strategy/; McKinsey growth, marketing and sales practice — https://www.mckinsey.com/capabilities/growth-marketing-and-sales/how-we-help-clients
- McKinsey and The Business of Fashion (2025) *State of Luxury 2025* — https://www.mckinsey.com/industries/retail/our-insights/state-of-luxury-2025
- Eleken articles on product-idea validation, UX ideas, SaaS launch, startup scaling, design-system checklists and mobile onboarding — https://www.eleken.co/blog-posts/how-to-validate-product-ideas and sibling pages
- GOV.UK Service Manual, *Plan user research for your service* — https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service
- OpenAI image prompting and image generation guides — https://developers.openai.com/api/docs/guides/image-prompting, https://developers.openai.com/api/docs/guides/image-generation

The registered skill gate checks all **137** active skill paths, including the
three country-context skills, against plugin metadata and the fixed full-checkout
and package cap. The isolated native Codex discovery test uses
`-m gpt-6-luna -c model_reasoning_effort="high" -c skills.max_context_tokens=10000`;
the larger skills budget is explicit and does not change the user configuration.
For manifest regeneration, include both canonical roots (the generator supports
`--root .`); a skills-only manifest fails the registered parity gate. To check
the manifest without writing it, run
`node scripts/generate-plugin-manifest.js --engine . --root . --check`. On
31 October 2026 it exited 0 and reported that `plugin.json` is current with 137
skills; with the default `--root skills` it exited 1 and reported 134 skills on
disk, because the manifest also lists the three country-context skills.

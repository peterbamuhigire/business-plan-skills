# Documentation index

What is under `docs/`, newest evidence first. Dated records describe the repository on the day they were written; they keep that day's paths, counts and engine names, and are not edited afterwards. For the current state of the engine read the root [`README.md`](../README.md), the router [`AGENTS.md`](../AGENTS.md) and [`CONTRIBUTING.md`](../CONTRIBUTING.md).

## Kaizen and quality records

| Path | What it holds |
|---|---|
| [`kaizen/2026-10-engine-kaizen-pass-2/`](kaizen/2026-10-engine-kaizen-pass-2/05-final-report.md) | Pass 2, 31 October 2026: published score 50.0 against a fresh baseline of 44.0, the kept changes with commit hashes, [open work and decisions](kaizen/2026-10-engine-kaizen-pass-2/06-next-cycle.md), and [documentation follow-ups](kaizen/2026-10-engine-kaizen-pass-2/07-docs-followups.md). `labs/` holds the built-to-fail workbooks and the one-off restoration script |
| [`kaizen/2026-10-engine-kaizen/`](kaizen/2026-10-engine-kaizen/05-final-report.md) | The 29 October 2026 cycle (final 49.0) with its own `labs/` |
| [`kaizen/fpa-assumption-trace.md`](kaizen/fpa-assumption-trace.md) | The planning-assumption trace contract that links a financial narrative to its evidence |
| [`audits/`](audits/) | The 6 September 2026 kaizen audit and the local output-readiness review |
| [`continuous-improvement/`](continuous-improvement/) | Earlier dated kaizen waves and reviews (August to September 2026), including the model-currentness review of 25 September 2026 |
| [`quality/`](quality/) | `skill-quality-baseline.json` (the zero-debt regression lock read by `validate_skill_engine.py`) and the UNDP compendium allowlist read by `source_ingestion_guardrail.py` |
| [`quality-gates/business-plan-release-gate.md`](quality-gates/business-plan-release-gate.md) | The blocker-first release gate and how to run it |

Latest published score: 50.0 raw and 50.0 capped (`min(raw, 65)`), against a target of 95. Scores are practitioner judgements, not validator pass rates.

## Evidence and source registers

| Path | What it holds |
|---|---|
| [`source-registers/country-market-data.json`](source-registers/country-market-data.json) | The country and market evidence register: 24 rows, each with status, `checked_on` and `recheck_due`. The checker is `tools/evidence-register/refresh_evidence_register.py` |
| [`source-registers/country-market-data.md`](source-registers/country-market-data.md) | The same register as a table. The table between its markers is generated from the JSON (`--write-markdown`) and checked by `--check` |
| [`workbook-audits/`](workbook-audits/) | A structural formula map of the SaaS projection workbook. Its PASS is structural only: the same workbook reports 10 unwired inputs under `formula_map.py --require-wired-inputs` and has no balance sheet, so do not read it as proof that the model calculates correctly |

## Contracts and operating notes

| Path | What it holds |
|---|---|
| [`operations/`](operations/runtime-agnostic-orchestration-2026-09-07.md) | The runtime-agnostic orchestration contract: scoped work packages, evidence checkpoints, least agency |
| [`ai-prompting/`](ai-prompting/domain-prompt-compilation-contract.md) | The local copy of the domain prompt compilation contract, kept so a fork of this engine alone can still generate prompts |
| [`approval-enforcement.md`](approval-enforcement.md) and [`approval-adapter.json`](approval-adapter.json) | Which business-plan actions need approval and who may give it |
| [`control-plane-adoption.md`](control-plane-adoption.md) | How the engine exposes itself to the optional coordination package through `.skills-engine/engine-manifest.yaml` |

## Upgrade, analysis and planning history

| Path | What it holds |
|---|---|
| [`engine-upgrade-july-2026/`](engine-upgrade-july-2026/00-executive-summary.md) | The July 2026 audit, build backlog, conformance upgrade record and release manifest |
| [`evaluation/2026-04-12/`](evaluation/2026-04-12/) | The April 2026 evaluation and recommendations |
| [`implementation/review-12-Mar-2026/`](implementation/review-12-Mar-2026/) | The March 2026 coverage and gap review |
| [`march-9-analysis/`](march-9-analysis/README.md), [`march-12-analysis/`](march-12-analysis/README.md) | The March 2026 gap analyses |
| [`plans/`](plans/) | Design plans from March 2026 and the nine-part engine-completion roadmap in `plans/engine-completion/` |
| [`updates/`](updates/) | A note on skills added outside a kaizen cycle (June 2026) |
| [`prompt-for-socials.md`](prompt-for-socials.md) | A historical kickstart prompt written for a separate social-media skills repository; it does not describe this engine |

## Running the checks

The commands, what each needs (PyYAML, Node.js, LibreOffice, `xlsxwriter`) and the date-triggered evidence gate are in the root [`README.md`](../README.md) under Installation and under Quality and improvement.

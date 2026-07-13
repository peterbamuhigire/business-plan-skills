---
name: meta-board-and-investor-reporting
description: Use when a SaaS company has external investors (priced round, SAFE notes outstanding, DFI partners). Use monitoring and evaluation for internal operating KPI systems.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Board & Investor Reporting Skill

## Overview

Funded SaaS companies that fail to maintain investor confidence often had great plans and weak reporting. The board pack is the operating artefact of the living plan — it embodies what's working, what's broken, and what the company is asking the board to help with. This skill installs the canonical monthly investor update + quarterly board pack rhythm.

## Use When

- A SaaS company has external investors (priced round, SAFE notes outstanding, DFI partners)
- A company is preparing for a fundraise (boards expect this artefact)
- An existing board pack is ad hoc, late, or causing surprise
- Investors are asking for more transparent reporting

## Do Not Use When

- The request belongs to the neighbouring route. Use monitoring and evaluation for operating KPI systems; use this family for board and investor reporting.
- The available evidence cannot support a responsible board and investor reporting conclusion; return the evidence gap instead of inventing one.

## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Board And Investor Reporting brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Plan and operating metrics (from `saas-unit-economics-and-cohort-model`)
- MSPOT for the year (from `meta-living-plan-governance`)
- Decision log
- Board composition and term lengths
- Investor letter cadence expectations

## Workflow

1. **Set the monthly investor-update structure:**
   - One-line headline (top metric movement)
   - KPI snapshot (5-8 numbers)
   - Wins (3-5)
   - Losses / risks (2-4, honest)
   - Asks (where investors can help)
   - Cash position + runway
2. **Set the quarterly board-pack structure** (see references):
   - Cover + agenda
   - CEO letter (narrative)
   - Financial dashboard (P&L, cash, ARR waterfall, unit economics)
   - Operating dashboard (KPIs, cohorts, NPS, NRR)
   - Strategic discussion (1-3 decisions board needs to weigh)
   - HR / people / culture
   - Risk register update
   - Forward look (next quarter targets)
   - Appendix (deeper financials, customer wins, product roadmap)
3. **Install the cadence**:
   - Monthly investor update — within 7 business days of month-close, every month
   - Quarterly board pack — sent 5 business days before board meeting
   - Board meeting — 90-120 minutes, focused on strategy, not status (status was the pre-read)
4. **Define decision-ask discipline** — every board meeting should have 1-3 explicit decisions the board is asked to weigh in on; never use the board as a status audience.
5. **Tie to MSPOT** — the board pack mirrors MSPOT structure (Mission unchanged, Strategy progress, Projects status, Omissions confirmed, Tracking).
6. **Use the decision log** — major decisions log entries are board-pack content.
7. **Set up the data room** in parallel — keeps DD-readiness continuous, not just at fundraise time.
8. **Train the team** on board-pack content production — Finance produces financials, Heads produce operating dashboards, CEO writes the narrative.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the board and investor reporting pack and that the decision concerns which performance changes require a board decision.
- **Stop condition:** halt the affected conclusion if required evidence is missing (reconciled KPI definitions, board calendar, and decision log) or if the work could lead to this identified risk: turning governance reporting into unactionable metric theatre.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- Monthly update delivered within 7 days every month — no exceptions
- Quarterly board pack delivered ≥5 days before board meeting
- KPI dashboard consistent month-over-month (no metric-substitution)
- Asks explicit; status implicit (no surprises)
- Honest about losses and risks (board will discover anyway)
- Decision log surfaces in the pack

## Anti-Patterns

- Slide deck only — no written narrative
- Highlights only — no losses / risks
- Different metrics each month (cherry-picking)
- Board meeting as status presentation, not decision forum
- Missing month-close discipline (Day 5 close discipline matters)
- Asks vague ("we'd appreciate any advice")


- Applying the wrong neighbouring route to meta board and investor reporting. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Board And Investor Reporting deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Monthly investor-update template (filled or fillable)
- Quarterly board-pack template
- KPI dashboard standard
- Cadence calendar
- Decision-ask discipline
- Data-room structure

## AI Section (mandatory for AI-feature-led companies)

When AI is material to revenue or product, every quarterly board pack must include an AI section per `references/saas-ai-board-pack-section.md`. Every monthly investor update must include the AI block per `skills/11-funding-request/references/saas-ai-investor-update-block.md`. The AI section includes:
- AI KPI dashboard (AI-ARR, AI GM, AI-cost-%-of-ARR, eval coverage, hallucination rate, cache-hit, per-tenant cost, vendor spend, incidents)
- AI strategic decisions for board (1-3 explicit asks)
- AI risk register update
- AI roadmap progress with cost-gate decisions
- AI compliance and governance update
- Forward look (AI KPI targets + roadmap targets + top AI risk)

This sits alongside the financial dashboard and is treated as a first-class section, not as an appendix.

## Agent Section (mandatory for agent-product companies)

When the company ships an agent or multi-agent product, every quarterly board pack must include the **Agent Section** per `skills/meta-agent-board-and-investor-reporting/references/saas-agent-board-pack-section.md`. Every monthly investor update must include the **Agent block** per `skills/meta-agent-board-and-investor-reporting/references/saas-agent-investor-update-block.md`. The Agent section includes:

- Full agent KPI trends (13-week): resolved tasks, cost per resolved task, intervention rate, task success, agent GM, agent ARR attribution, cache, HITL / tool / retry shares, branch / loop breaches
- Moat-vs-wrapper reassessment (quarterly)
- Autonomy expansion review (any new actions promoted to higher class)
- Drill cadence audit (monthly safety drill + quarterly tabletop)
- Audit-log review summary
- Regulator engagement log
- Stress-test refresh
- Reserves balances (irreversibility / migration / regulator)
- Talent retention signals (AI Safety Lead, Eval Engineer, Agent Architect)
- Foundation-model platform risk
- Bankability rescore
- Valuation context
- Decisions taken + decisions due
- Next-quarter agent priorities

Sev-1 incidents must be communicated to investors within 48 hours of confirmation, not at the next board meeting. The Agent section sits **on top of** the AI section, not in place of it.

This is operationalised through `skills/meta-agent-board-and-investor-reporting/SKILL.md` (workflow).

## References

- `references/saas-board-pack-template.md` — full template + worked example
- `references/saas-ai-board-pack-section.md` — AI section template for AI-feature-led companies
- `skills/meta-agent-board-and-investor-reporting/SKILL.md` — Agent reporting workflow (for agent-product companies)
- `skills/meta-agent-board-and-investor-reporting/references/saas-agent-board-pack-section.md` — Agent section template
- `skills/meta-agent-board-and-investor-reporting/references/saas-agent-investor-update-block.md` — Agent investor-update block
- `book-extractions/cotton-run-a-saas-business-extraction.md` — MSPOT and cadence
- `book-extractions/mersch-hacking-saas-extraction.md` — financial reporting standards
- `skills/meta-living-plan-governance/SKILL.md` — sister skill (this skill operationalises the living plan via investor reporting)
- `skills/meta-quarterly-gameplan/SKILL.md` — sister skill (quarterly operating rhythm)

## Africa / Uganda Application Notes

- DFI investors (IFC, FMO, BII, AfDB, Norfund, Proparco) require specific reporting formats — adopt theirs as the master template if DFI is on cap table.
- Many African boards are part-international, part-local — boards may be in 2-3 time zones. WhatsApp / Slack-asynchronous board engagement between meetings is normal.
- ESG / impact reporting is often required — embed in the quarterly pack rather than producing a separate report.
- FX volatility: include USD and local-currency views; explain FX impact separately from operational performance.
- Public-sector / NGO customer reporting: when these are >20% of ARR, include separate customer-concentration analysis.
- Board governance compliance: Ugandan Companies Act, Kenya Companies Act, South Africa Companies Act 2008 have specific board-resolution and minute-keeping requirements; embed in the cadence.

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Board and investor reporting pack decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to turning governance reporting into unactionable metric theatre. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the board and investor reporting pack; drafting the monthly update or quarterly pack is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If reconciled KPI definitions, board calendar, and decision log cannot be obtained, return a qualified board and investor reporting pack covering only the checks that remain supportable. Leave this decision unresolved: which performance changes require a board decision. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which performance changes require a board decision | Record the conclusion, source trail, owner, and review trigger in the board and investor reporting pack. | Risk of turning governance reporting into unactionable metric theatre |
| Material evidence conflicts or remains uncertain | Present the metric under both definitions with the resulting board decision, then standardise the approved definition from the next period. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: reconciled KPI definitions, board calendar, and decision log | Mark the decision on which performance changes require a board decision `not assessed` in the board and investor reporting pack, and send it to the CFO and board chair. | Otherwise, the work risks turning governance reporting into unactionable metric theatre |

## Quality Standards


Accept the board and investor reporting pack only when evidence is sufficient for this decision: which performance changes require a board decision. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of turning governance reporting into unactionable metric theatre.

## Worked Example


ARR grows, but finance and sales use different churn definitions. Show the reconciliation, adopt one board definition, restate the comparison period, and ask the board to decide the corrective retention action.

<!-- dual-compat-end -->

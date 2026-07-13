---
name: meta-agent-board-and-investor-reporting
description: Use when drafting the monthly investor update for an agent business. Use monitoring and evaluation for internal operating KPI systems.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

<!-- dual-compat-start -->
# Meta — Agent Board & Investor Reporting Skill

## Overview

Standard board / investor reporting (handled by `meta-board-and-investor-reporting`) covers GTM, financial, product, risk. AI reporting layers AI metrics (covered by `meta-board-and-investor-reporting/references/saas-ai-board-pack-section.md`). **Agent reporting** must add the autonomy / incident / drill / regulator dimensions that an agent business cannot defer to next quarter without losing investor trust.

The agent reporting block is mandatory in every monthly investor update and every quarterly board pack of an agent business.

## Use When

- Drafting the monthly investor update for an agent business
- Drafting the quarterly board pack for an agent business
- Setting up the reporting cadence for a newly-funded agent business
- Refreshing the investor relations template
- Cross-loaded with `meta-board-and-investor-reporting`

## Do Not Use When

- The product is not an agent — use AI / SaaS reporting only
- A one-off investor update (use ad-hoc; do not over-engineer)


- Route to `meta-monitoring-evaluation` instead for an internal operating KPI system.
## Required Inputs


| Input | Source / provider | Required? | If absent |
|---|---|---:|---|
| Board And Investor Reporting brief and decision audience | Client, plan owner, or approved project files | Yes | Stop before making a recommendation; state the missing decision context. |
| Claims, assumptions, and supporting evidence | Source register, model, research notes, interviews, or operating records | Yes | Separate known facts from assumptions and return a qualified gap list. |
| Authority and delivery constraints | Requesting owner and repository instructions | Yes | Remain read-only and produce a draft or review only. |
- Agent KPI dashboard (cost per resolved, intervention rate, task success, etc.)
- Irreversibility-incident log (last 90 days minimum)
- Drill calendar and attendance records
- Audit-log review records
- Regulator-engagement log
- Agent revenue attribution
- Eval-suite scores trend
- Foundation-model deprecation watch
- Reserve balances (irreversibility / migration / regulator)

## Workflow

1. **Monthly investor update agent block** per `references/saas-agent-investor-update-block.md`:
   - Headline agent KPIs (cost per resolved task; intervention rate; task success; agent gross margin; agent ARR attribution)
   - Eval-suite scores trend (4-week)
   - Top 3 agent risks this month
   - Foundation-model / provider changes
   - Incidents (sev-1 / sev-2; or "none this month")
   - Reserve balances
   - Next month focus on agent
2. **Quarterly board pack agent section** per `references/saas-agent-board-pack-section.md`:
   - Full agent KPI trends (13-week)
   - Moat-vs-wrapper reassessment (quarterly)
   - Autonomy expansion review (any new actions promoted to higher class)
   - Drill cadence audit
   - Audit-log review summary
   - Regulator engagement log
   - Stress-test refresh
   - Bankability rescore (cross-reference)
   - Talent retention signals (AI Safety Lead, Eval Engineer)
   - Foundation-model platform risk
   - Next-quarter agent priorities
3. **Variance discipline** — for any KPI off plan, state diagnosis (execution vs environment) + remediation + owner + deadline. Per the living-plan governance.
4. **Decision-log integration** — every material agent decision (autonomy expansion, new tool integration, provider switch, pricing change, incident response) logged with date / decision / alternatives / evidence / owner / review-date.
5. **Wire to the next bankability rescore** — board pack outputs feed quarterly bankability rescore.
6. **Anti-surprise discipline** — sev-1 incidents communicated to investors within 48 hours of confirmation, not at next board meeting.

### Decision, stop, and recovery controls


- **Decision point:** confirm that the requested output is the agent board-reporting module and that the decision concerns which agent risks and decisions enter the board pack.
- **Stop condition:** halt the affected conclusion if required evidence is missing (task success, intervention, incident, cost, and attribution data) or if the work could lead to this identified risk: showing activity while hiding irreversibility or unit-cost deterioration.
- **Recovery:** obtain the missing record or reviewer, repeat the affected check, and update the exception record before release.

## Quality Bar

- All headline agent KPIs reported every month
- Eval-suite trend present
- Incident log present (or explicit "none this month")
- Reserve balances current
- Quarterly: moat reassessment, autonomy review, drill audit, audit-log summary, regulator log
- Variance discipline applied (diagnosis + remediation + owner)
- Decision log maintained
- Sev-1 reporting within 48h
- Format consistent month-on-month (investors compare across periods)

## Anti-Patterns

- Skipping months ("nothing material")
- Only reporting good metrics
- Burying incidents in appendix
- Reporting agent revenue without attribution method
- Quarterly moat reassessment skipped
- Eval-suite trend absent
- Reserve balances absent
- Trigger-replan events not communicated


- Applying the wrong neighbouring route to meta agent board and investor reporting. **Correction:** confirm the decision and route to the named neighbour before analysis.
- Treating an assumption as verified evidence. **Correction:** label it, cite its source or owner, and assign a verification action.
- Recommending action without a decision threshold. **Correction:** state the measurable acceptance condition and review trigger.
- Recording an unavailable check as passed. **Correction:** mark it `not assessed` and state the consequence for the decision.
- Mutating or publishing during an analysis-only task. **Correction:** remain read-only until the owner gives explicit authority.
## Outputs


| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Board And Investor Reporting deliverable | Named decision-maker or plan author | The recommended choice, assumptions, countercase, and next action are explicit. |
| Evidence and exception register | Reviewer, funder, board, or implementation owner | Every load-bearing claim is sourced or labelled as an assumption; missing checks are not shown as passes. |
- Monthly investor update agent block
- Quarterly board pack agent section
- Decision log entries for the period
- Variance diagnoses for off-plan KPIs
- Sev-1 incident communications (if any)

## Living-Plan Cadence Defaults

| Element | Cadence | Owner |
|---|---|---|
| Monthly investor update agent block | monthly | CEO + CFO + AI Safety Lead |
| Quarterly board pack agent section | quarterly | CEO + CFO + AI Safety Lead + Compliance |
| Decision log | continuous | CEO; reviewed monthly |
| Variance diagnosis | monthly | CFO + section owners |
| Sev-1 incident communication | within 48h | AI Safety Lead + CEO |

## References

- `references/saas-agent-investor-update-block.md` — monthly agent block template
- `references/saas-agent-board-pack-section.md` — quarterly board agent section template
- `skills/meta-board-and-investor-reporting/SKILL.md` — parent
- `skills/meta-board-and-investor-reporting/references/saas-ai-board-pack-section.md` — AI block parent
- `skills/meta-agent-bankability-and-investor-readiness/SKILL.md` — bankability rescore
- `skills/meta-living-plan-governance/SKILL.md` — cadence parent

## Africa / Uganda Application Notes

- **DFI / multilateral investors** (IFC, AfDB, FMO, BII, Proparco, FCDO, USAID, IDRC, GIZ) require quarterly board packs in their templates; ensure the agent section maps to their fields
- **Local board members** in African plans may include strategic / political / regulator-aligned directors; agent reporting must be readable to non-technical board members; include a one-paragraph plain-English summary of agent state each quarter
- **Sov-AI procurement investors** want explicit reporting on residency, local-citizen headcount, regulator engagement
- **Currency** — report in USD for institutional investors; local-currency-equivalent for DFI / strategic
- **Press / political exposure** — agent businesses in regulated African sectors should report public sentiment / regulatory-watch as a board item
- **Jobs-impact disclosure** — for public-sector agent deployments, jobs-impact tracking is increasingly required by donors / multilaterals

## Evidence Produced



| Evidence | Format | Acceptance condition |
|---|---|---|
| Agent board-reporting module decision trace | Sources, calculations, assumptions, countercase, and selected action | A reviewer can trace the selected action and rejected alternatives to the cited inputs. |
| Exception record | Failed and not-assessed checks with owner and due action | The register exposes every unresolved exception that could lead to showing activity while hiding irreversibility or unit-cost deterioration. |

## Capability and Permission Boundaries


Read supplied records and use non-mutating checks to produce the agent board-reporting module; adding the agent KPI section to an authorised draft pack is permitted when requested. Do not publish, contact third parties, alter live systems, commit funds, or claim legal, tax, audit, valuation, ESG, or investment assurance without the owner's explicit authorisation and the appropriate reviewer.

## Degraded Mode


If task success, intervention, incident, cost, and attribution data cannot be obtained, return a qualified agent board-reporting module covering only the checks that remain supportable. Leave this decision unresolved: which agent risks and decisions enter the board pack. Record the evidence owner and next check; an inaccessible source, tool, or reviewer is never a pass.

## Decision Rules



| Decision condition | Action | Failure or risk avoided |
|---|---|---|
| Evidence is sufficient to decide: which agent risks and decisions enter the board pack | Record the conclusion, source trail, owner, and review trigger in the agent board-reporting module. | Risk of showing activity while hiding irreversibility or unit-cost deterioration |
| Material evidence conflicts or remains uncertain | Reconcile the disputed agent metric to event and finance records, showing both definitions until the board approves one. | Selecting an option without resolving the decision-relevant uncertainty |
| Required evidence is missing: task success, intervention, incident, cost, and attribution data | Mark the decision on which agent risks and decisions enter the board pack `not assessed` in the agent board-reporting module, and send it to the CFO and board chair. | Otherwise, the work risks showing activity while hiding irreversibility or unit-cost deterioration |

## Quality Standards


Accept the agent board-reporting module only when evidence is sufficient for this decision: which agent risks and decisions enter the board pack. Assumptions and countercases remain visible, calculations and cross-references reconcile, and the reviewer can see how the recommendation addresses the risk of showing activity while hiding irreversibility or unit-cost deterioration.

## Worked Example


Task success rises while human intervention and irreversible incidents also rise. Put all three trends and the required governance decision in the board module rather than presenting success alone.

<!-- dual-compat-end -->

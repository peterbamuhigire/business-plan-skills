---
name: saas-agent-risk-and-stress-test
description: Use when producing or reviewing the saas agent risk and stress test component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS Agent Risk & Stress-Test Skill

## Overview

AI risk registers (handled by `saas-ai-risk-and-stress-test`) cover cost spike, model deprecation, hallucination event, data-rights conflict, vendor concentration, regulatory exposure. **Agent risk** must add two categories that do not exist in AI-feature plans:

1. **Autonomy incidents** — the agent takes an action the customer / regulator considers wrong, beyond authority, or harmful
2. **Irreversibility incidents** — the agent takes an action that **cannot be undone** (financial transfer; record committed to ledger; communication sent; legal document filed; permit issued; medication ordered)

Plus agent-specific failure modes: multi-agent collusion / loop, tool-vendor outage breaking the action layer, prompt-injection escalation that bypasses safety, action-authentication bypass, AI Safety Lead flight, foundation-model deprecation that breaks specific tool-call signatures.

Generic risk skills miss all of these.

## Use When

- A SaaS plan ships an agent or multi-agent product
- Section 12 is being built for an agent-product plan
- The plan claims agent autonomy in irreversibility-class actions (financial, medical, legal, public-sector)
- A regulator is involved or expected
- A board / investor / DFI has asked for the agent risk register specifically
- An incident has occurred and the register needs to be refreshed
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- AI is internal-efficiency only (no customer-facing agent action) — use generic `12-risk-analysis` plus `saas-ai-risk-and-stress-test`
- The agent is read-only (recommendations only, no actions) — most agent risks attenuate; use generic AI risk register

## Required Inputs

- Agent architecture and action taxonomy
- **Irreversibility classification** of agent actions:
  - Class A — reversible information output (e.g. recommendation, draft, summary)
  - Class B — reversible transactional action (e.g. open ticket, schedule appointment that can be moved)
  - Class C — soft-irreversible (e.g. message sent that cannot be unsent but can be retracted)
  - Class D — hard-irreversible (e.g. financial transfer; legal document filed; medication ordered; permit issued; ledger committed)
- HITL / human-final policy per class
- Kill-switch / pause-switch design
- Audit-log design (immutability, retention, queryability, regulator-acceptable)
- Tool registry inventory + per-tool failure modes
- Foundation-model dependency map (which models, which providers, which deprecation horizons)
- Eval-coverage by action class
- Red-team / safety drill cadence
- Customer-credit and indemnity exposure
- Regulatory map (KE ODPC / NG NDPC / UG NITA-U / ZA Info Reg / sectoral)
- Insurance coverage (AI E&O, cyber, product liability)

## Workflow

1. **Build the action taxonomy** — every action the agent can take, classified A/B/C/D for irreversibility, with HITL / human-final policy stated per class.
2. **Build the agent risk register** per `references/saas-agent-risk-register-template.md`:
   - Cost / margin risks (LLM cost spike; tool cost spike; intervention cost spike; FX)
   - Model risks (deprecation; version drift; quality regression; foundation-model commoditisation absorbing the orchestration)
   - Autonomy risks (action beyond authority; wrong action; misinterpreted goal)
   - Irreversibility risks (Class D actions taken incorrectly; sev-1 customer loss)
   - Safety / red-team risks (prompt injection; jailbreak; tool-call exfiltration; action-auth bypass)
   - Multi-agent risks (collusion; loop; planner gaming critic)
   - Tool / vendor risks (tool outage; tool API change; tool deprecation; vendor lock-in)
   - Data risks (training-data lawsuit; customer-data leakage; data-rights conflict; data-residency breach)
   - Talent risks (AI Safety Lead flight; Eval Engineer flight; Agent Architect flight)
   - Regulatory risks (sector regulator action; data-protection enforcement; AI Act / equivalent enforcement; sovereign-AI procurement disqualification)
   - Customer risks (customer-misuse of the agent; downstream-harm allegation; jobs-impact backlash)
   - Operational risks (eval-coverage gap; audit-log gap; kill-switch failure; drill skipped)
3. **For each risk:** name, severity (1-5), likelihood (1-5), composite score, owner, mitigation, leading indicator, trigger-replan condition.
4. **Apply the irreversibility / autonomy class matrix:**
   - Class D actions: human-final mandatory; no full autonomy; explicit pre-action confirmation; double-signing; immutable audit
   - Class C actions: HITL approval required above policy threshold; agent may execute below threshold with audit
   - Class B actions: agent autonomous within policy; HITL on escalation
   - Class A actions: agent autonomous; audit only
5. **Build agent stress-test scenarios** per `references/saas-agent-stress-test-scenarios.md`:
   - Provider 2x and 5x pricing
   - Tool-vendor outage 1 week
   - Intervention rate 2x
   - Irreversibility incident at scale (sev-1 affecting >1% of customers)
   - Foundation-model deprecation forcing migration
   - FX 20% local-currency depreciation
   - Regulator action freezing agent deployment in a market
   - Branch explosion / multi-agent loop
   - AI Safety Lead departure mid-roadmap
   - Prompt-injection mass exploitation
6. **Quantify impact** per scenario: agent GM impact, runway impact, customer-churn impact, reserve drawdown, time-to-mitigate.
7. **Wire reserves** to `saas-agent-unit-economics-and-cogs` (irreversibility reserve, migration reserve, regulator-engagement reserve).
8. **Set the drill cadence** — monthly safety drill; quarterly tabletop incident exercise; annual full simulation.
9. **Connect to insurance** — confirm AI E&O coverage scope; document any exclusions (autonomous agent action sometimes excluded); price coverage gap.
10. **Wire to living-plan governance** — assign cadence, owners, variance thresholds per Agent Risk Cadence below.

## SLA-Extended Stress Scenarios

When the agent product carries SLA commitments, the stress-test set must be extended with SLA-specific scenarios (the agent-risk scenarios above remain; these add). The full discipline lives in `saas-agent-sla-risk/SKILL.md` and `meta-financial-stress-test/references/saas-agent-sla-stress-test-scenarios.md`; the extension scenarios are:

- **Catastrophic SLA breach (sev-1 mass-credit)** — single incident affecting >5% of customers triggers SLA-credit accrual 5-15x trailing baseline in one month; reserve depletes 60-120%
- **Foundation-model cost shock making SLA-tier pricing unviable** — provider 2x repricing where contracts lack vendor-cost pass-through clause; SLA-tier becomes loss-making until repricing cycle completes
- **Customer-side SLA gaming** — staff inflate intervention reports / reject outcomes; revenue leakage 5-15% across affected cohort; refund reserve absorbs initial but gaming-detection control must fire
- **Regulator-mandated SLA tightening** — sector regulator (FCA / OCC / SEC / SARB / CBK / CMA / CBN / FSCA / BoU / NDPC) publishes standard exceeding current commitments; cost-of-quality upgrade required; non-compliance penalty risk
- **SLA-credit accrual exceeding reserve** — actuals >120% of reserve drawn; P&L surprise; auditor concern; methodology re-cut; investor-narrative damage
- **Outcome-pricing refund cascade** — systematic downstream rejection of outcomes drains refund reserve; revenue restatement risk
- **Insurance carrier exclusion expansion** — carrier removes SLA-credit / refund coverage at renewal; self-insurance reserve absorbs
- **Sovereign-AI provider SLA pass-through breach** — mandated in-region provider outage triggers vendor SLA breach by pass-through

Each scenario is sized for revenue impact, reserve impact, valuation hit, and recovery horizon in `saas-agent-sla-stress-test-scenarios.md`. Top-3 scenarios for the specific business feed into the 3yr / 5yr stress case and the investor-narrative FAQ rebuttal library.

## Quality Bar

- Action taxonomy with explicit irreversibility classes A/B/C/D
- HITL / human-final policy stated per class
- Risk register populated across all 12 categories
- Each risk has severity x likelihood, owner, mitigation, leading indicator, trigger-replan
- Stress scenarios cover all 10 mandatory scenarios
- Quantified impact per scenario (GM, runway, churn, reserve)
- Reserves are right-sized (12+ months coverage at expected rate)
- Drill cadence assigned with owners
- Insurance scope reviewed and gaps identified
- A sceptical board chair or DFI risk officer would not call the register "performative"

## Anti-Patterns

- "AI risks" stated generically without separating autonomy from irreversibility
- No irreversibility classification — therefore no human-final logic — therefore catastrophic incident is a matter of time
- Kill-switch claimed but never drilled
- Audit log claimed but not regulator-acceptable
- "We have HITL" without policy thresholds per class
- No drill cadence (drills uncover gaps that postmortems would otherwise expose)
- No reserve for irreversibility-incident customer-credits and legal
- Insurance assumed to cover autonomous agent action (often excluded)
- Multi-agent product without branch / loop caps and kill-switch
- AI Safety Lead role unfilled or treated as optional
- "Foundation model risk is low because we can switch" — switching mid-production is a quarter of work and likely a revenue dip

## Outputs

- Action taxonomy with irreversibility classes
- Populated risk register (12 categories)
- Stress-test scenarios with quantified impact
- Reserve sizing (irreversibility, migration, regulator)
- Drill cadence calendar
- Insurance gap analysis
- Living-plan cadence assignment

## Living-Plan Agent Risk Cadence

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Irreversibility-class incidents | continuous + monthly review | AI Safety Lead | any sev-1 = immediate |
| Autonomy incidents (action beyond authority) | continuous + monthly | AI Safety Lead | any sev-1 |
| Red-team / safety drill | monthly | AI Safety Lead | missed drill |
| Tabletop incident exercise | quarterly | AI Safety Lead + CEO | missed exercise |
| Eval-coverage by action class | monthly | Eval Engineer | coverage gap on Class C/D |
| Audit-log review | monthly | Compliance | findings |
| Kill-switch drill | monthly | Tool Engineer + AI Safety Lead | drill failure |
| Tool-invocation reliability | weekly | Tool Engineer | error rate >2% |
| Multi-agent loop / branch breach | continuous | Eval Engineer | any breach |
| Prompt-injection scan | weekly | AI Safety Lead | new vector |
| Foundation-model deprecation watch | monthly | CTO / Head of AI | provider notice |
| Regulator engagement | quarterly | Compliance | new rule |
| AI Safety Lead retention signal | monthly | Head of People | flight signal |
| Insurance coverage review | semi-annual | CFO | exclusion identified |
| Reserve adequacy review | quarterly | CFO + AI Safety Lead | <12 months coverage |

## References

- `references/saas-agent-risk-register-template.md` — populated risk register
- `references/saas-agent-stress-test-scenarios.md` — quantified stress scenarios
- `references/agent-operations-runbook-summary.md` — kill-switch, audit, drill summary (also lives at `08-operations-plan/references/`)
- `skills/12-risk-analysis/saas-ai-risk-and-stress-test/SKILL.md` — AI risk parent
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — reserves consumer
- `skills/meta-financial-stress-test/SKILL.md` — financial stress-test discipline
- `skills/meta-agent-bankability-and-investor-readiness/SKILL.md` — bankability scorecard consumer
- `skills/12-risk-analysis/saas-agent-sla-risk/SKILL.md` — SLA-specific risk register
- `skills/12-risk-analysis/saas-agent-sla-risk/references/saas-agent-sla-risk-register.md` — populated SLA risk register
- `skills/meta-financial-stress-test/references/saas-agent-sla-stress-test-scenarios.md` — 8 standardised SLA stress scenarios with financial impact
- `skills/meta-agent-sla-financial-controls/SKILL.md` — controls evidence
- `skills/10-financial-projections/saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` — SLA-credit and refund reserve methodology
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent audit
- `book-extractions/agent-sla-commercial-business-plan-audit-2026.md` — SLA + commercial audit

## Africa / Uganda Application Notes

- **Mobile-money irreversibility** — M-Pesa, MoMo, Airtel Money, Wave, Orange Money transactions are functionally irreversible once authorised; Class D classification mandatory for any agent action touching mobile-money rails.
- **Regulatory environment** — KE ODPC, NG NDPC, UG NITA-U / PDPO, ZA Information Regulator, RW NCSA, TZ PDPC are evolving AI-action accountability and audit-log expectations; agent vendors should engage proactively. Sectoral regulators (BoU / CBK / CBN / SARB; HPCSA / UMDPC equivalents; LSK / SCUEA legal regulators) increasingly ask for documented HITL policy on Class C/D actions.
- **Customer-data residency** — agents processing customer data for KE / NG / ZA / RW must respect residency rules; cross-border processing may require approvals.
- **Jobs-impact risk** — public-sector agent deployments in countries with high formal-sector unemployment (especially ZA, KE, NG) carry political risk; jobs-impact disclosure and re-skilling commitment are increasingly funding conditions for DFI / multilateral support.
- **AI Safety Lead scarcity** — the role is almost non-existent in-region; consider fractional / remote / external-advisor models; African talent map in `saas-agent-talent-strategy`.
- **FX risk** — USD-denominated LLM + tool spend with local revenue; +/- 20% corridor stress mandatory; pricing pass-through clause mandatory for contracts >12 months.
- **Insurance availability** — AI E&O cover in African markets is thin; brokers active in 2025-2026 include AON, Marsh, Liberty Mutual via reinsurance; expect exclusions on autonomous agent action and irreversibility events; price the gap.
- **Public-sector agent risk** — sovereign-AI procurement can be cancelled with political change; mitigation: diversify customer mix; avoid single-tender concentration >20-25% of ARR.
- **Drill cadence in African operations** — drills are often skipped due to team capacity; treat as non-negotiable; document attendance to evidence governance maturity to DFIs.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Business model, assumptions, contracts, operating controls, risk evidence, scenario variables, and risk appetite for saas agent risk and stress test | All pipeline sections, client records, current research, and governance owners | Yes | If absent, probability, impact, control effectiveness, or scenario data is unavailable, mark the risk unassessed and use a bounded sensitivity rather than a false score. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent risk and stress test exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent risk and stress test release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Risk-source trace, scenario calculation, control-owner confirmation, and residual-risk decision | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent risk and stress test decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent risk and stress test review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent risk and stress test, the controlling focus is agent failure economics, unsafe-action exposure, provider dependency, human fallback, and cash stress. This skill may inspect evidence and challenge assumptions in read-only mode; it may not change controls, accept risk for management, trigger contingency spending, or certify compliance. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent risk and stress test, loss of evidence about agent failure economics, unsafe-action exposure, provider dependency, human fallback, and cash stress activates degraded mode. If the controlling saas agent risk and stress test evidence is unavailable, the same boundary applies. When probability, impact, control effectiveness, or scenario data is unavailable, mark the risk unassessed and use a bounded sensitivity rather than a false score. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent risk and stress test, a mitigation has no owner, trigger, budget, or evidence of effectiveness| treat it as planned rather than operating, raise residual risk, and define the test or owner needed | Decorative risk registers understate exposure and create false assurance |
| For saas agent risk and stress test, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent risk and stress test decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent risk and stress test, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent risk and stress test decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect business model, assumptions, contracts, operating controls, risk evidence, scenario variables, and risk appetite and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Risk-source trace, scenario calculation, control-owner confirmation, and residual-risk decision must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent risk and stress test, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent risk and stress test, treating an unavailable business model, assumptions, contracts, operating controls, risk evidence, scenario variables, and risk appetite as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing decision-ranked risk register, stress tests, mitigations, triggers, and contingency actions that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

A tool-using agent can issue refunds and its provider doubles prices during peak season. Stress unsafe actions and vendor cost together, then cap permissions and define the manual continuity path.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent risk and stress test; no local deep-dive reference is declared.
- For saas agent risk and stress test claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->

---
name: meta-agent-bankability-and-investor-readiness
description: Agent-specific bankability scorecard layered on top of SaaS bankability and AI bankability. Tests unit-economic discipline (cost per resolved task), moat-vs-wrapper, governance maturity (kill-switch, audit, drill cadence), safety / red-team practice, regulatory readiness, talent depth (AI Safety Lead in seat?), KPI maturity (intervention rate measured?). Use as the final gate before declaring an agent plan investor-ready.
---

# Meta — Agent Bankability & Investor Readiness Skill

## Overview

A SaaS plan must pass SaaS bankability (handled by `meta-bankability-scoring` + `saas-bankability-and-investor-readiness`). An AI-SaaS plan must additionally pass AI bankability (`meta-ai-bankability-and-investor-readiness`). An agent-product plan must additionally pass **agent bankability** — the gate that asks whether the agent business is investor-ready, not just AI-investor-ready.

The agent bankability scorecard sits **on top** of the prior two and adds the dimensions that agent-fund partners and DFI risk officers specifically diligence in 2026:

1. **Unit-economic discipline** — cost-per-resolved-task computed; agent GM credible; sensitivity / stress run
2. **Moat-vs-wrapper** — defensibility score honestly computed; not a wrapper
3. **Governance maturity** — kill-switch designed and drilled; audit-log regulator-acceptable; drill cadence in place
4. **Safety / red-team practice** — AI Safety Lead in seat; eval coverage on Class C/D actions; injection / jailbreak / auth-bypass coverage
5. **Regulatory readiness** — regulator engagement evidence; sectoral approval where required; documented HITL policy
6. **Talent depth** — mandatory roles filled; succession on AI Safety
7. **KPI maturity** — intervention rate measured; cost per resolved task measured; irreversibility-incident log maintained; living-plan cadence in place

## Use When

- An agent-product plan is being finalised
- Before declaring the plan investor-ready or DFI-ready
- Before a Series A or growth-round raise
- Before submitting to an agent-specialist fund
- When a board / DFI requires a bankability sign-off
- When integrating with `meta-bankability-scoring` for the full bankability gate

## Do Not Use When

- The plan does not include an agent product — use SaaS / AI bankability only
- The plan is pre-PMF and the agent is aspirational — use as forward-looking gap analysis, not a pass / fail

## Required Inputs

- Completed agent unit economics (`saas-agent-unit-economics-and-cogs`)
- Completed moat-vs-wrapper analysis (`saas-agent-moat-and-wrapper-risk`)
- Completed agent risk register (`saas-agent-risk-and-stress-test`)
- Completed agent talent strategy (`saas-agent-talent-strategy`)
- Completed agent pricing strategy (`saas-agent-pricing-strategy`)
- Agent operating evidence: KPI dashboard, eval reports, drill records, audit-log review records, incident log
- Regulator-engagement record

## Workflow

1. **Run the SaaS bankability scorecard** (`meta-bankability-scoring`) — prerequisite.
2. **Run the AI bankability scorecard** (`meta-ai-bankability-and-investor-readiness`) — prerequisite.
3. **Run the agent bankability scorecard** per `references/saas-agent-bankability-checklist.md` across 7 dimensions:
   - Unit-economic discipline (0-15)
   - Moat-vs-wrapper (0-15)
   - Governance maturity (0-15)
   - Safety / red-team practice (0-15)
   - Regulatory readiness (0-10)
   - Talent depth (0-15)
   - KPI maturity (0-15)
   - **Maximum 100**
4. **Interpret the score:**
   - 0-39: not bankable at agent-fund standard; do not raise; gap-fill required
   - 40-59: bankable for grant / DFI / strategic; not for institutional agent fund
   - 60-79: bankable for Series A / institutional agent fund
   - 80-94: top-quartile investor-ready
   - 95-100: rare; growth-round ready
5. **Identify the 2-3 binding gaps** — the dimensions most reducing the score; concrete action plan per gap.
6. **Wire to the investor deck / data room** — what evidence supports each scorecard item; cross-reference to data room.
7. **Schedule the next review** — agent bankability is not static; refresh quarterly.

## Quality Bar

- All three layers (SaaS / AI / Agent) scored separately and aggregated honestly
- Each scorecard item has evidence cited (not assertion)
- Gaps named; remediation plan time-boxed
- Score not gamed
- Data-room evidence linked
- A sceptical agent-fund partner would accept the scoring as fair

## Anti-Patterns

- Skipping SaaS or AI bankability and going straight to agent — gaps will surface in DD
- "We score 90" without evidence per item
- Gaming the rubric (claiming evidence that does not exist)
- Treating it as one-time; not refreshing quarterly
- No remediation plan for gaps
- Treating the AI Safety Lead in-seat check as optional

## Outputs

- Agent bankability score (0-100) with subscores
- Evidence inventory per scorecard item
- 2-3 binding gaps and remediation plan
- Cross-reference to investor deck and data room
- Quarterly review schedule

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Full agent bankability rescore | quarterly | CEO + CFO + AI Safety Lead | -5 points QoQ |
| Cost per resolved task tracker | weekly | CFO + Head of Agent | (per unit-economics skill) |
| Intervention rate tracker | weekly | HITL Designer + Head of Agent | (per unit-economics skill) |
| Irreversibility incident log | continuous + monthly review | AI Safety Lead | any sev-1 |
| Drill cadence audit | monthly | AI Safety Lead + Internal Audit | any missed drill |
| Regulator engagement evidence | quarterly | Compliance | any lapse |
| AI Safety Lead retention signal | monthly | Head of People | flight signal |

## References

- `references/saas-agent-bankability-checklist.md` — the 7-dimension scorecard
- `skills/meta-bankability-scoring/SKILL.md` — SaaS bankability parent
- `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` — AI bankability parent
- `skills/saas-bankability-and-investor-readiness/SKILL.md` — SaaS readiness
- `skills/10-financial-projections/saas-agent-unit-economics-and-cogs/SKILL.md` — unit economics
- `skills/06-competitive-analysis/saas-agent-moat-and-wrapper-risk/SKILL.md` — moat-vs-wrapper
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — risk register
- `skills/09-management-team/saas-agent-talent-strategy/SKILL.md` — talent
- `skills/07-marketing-sales-strategy/saas-agent-pricing-strategy/SKILL.md` — pricing
- `skills/meta-due-diligence/SKILL.md` — DD readiness
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent audit

## Africa / Uganda Application Notes

- **DFI / multilateral diligence** (IFC, AfDB, FMO, BII, Proparco, FCDO, USAID, IDRC, GIZ) increasingly checks agent items explicitly: cost-per-resolved-task, kill-switch drill cadence, audit-log retention, AI Safety Lead in seat, regulator engagement, jobs-impact disclosure
- **African agent fund landscape (2025-2026)** — TLcom Capital (Pan-Africa), Norrsken22, Ventures Platform (Nigeria), 4Di Capital (SA), Knife Capital (SA), Partech Africa, Equator Ventures, Catalyst Fund (climate / agritech / fintech overlap with agents), Future Africa, Renew Capital, Ingressive Capital — most generalist with agent appetite; agent-specialist funds in Africa not yet meaningful at scale; institutional agent investment often via SF / EU co-investors with African lead
- **Sovereign-AI procurement readiness** — for plans targeting public sector (KE Huduma, NG NIMC, RW Irembo, UG NITA-U, ZA Home Affairs / SARS), pre-clearance with regulator and local-entity / local-citizen-headcount evidence are bankability items
- **Local-language coverage** as a bankability evidence point in vertical agents serving African end-users
- **Insurance / indemnity** — AI E&O cover thin in Africa; document insurance approach and self-insurance reserve transparently in DD pack

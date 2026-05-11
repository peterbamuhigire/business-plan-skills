---
name: meta-living-plan-governance
description: Operate the business plan as a living document over the lifetime of the business — weekly metrics, monthly business review, quarterly re-plan, annual strategy refresh, decision log, plan-vs-actual variance protocol, trigger-replan rules, and sunsetting policy. Use whenever a plan is being finalised, or when a funded company is establishing its operating cadence after the plan is approved.
---

# Living Plan Governance Skill

## Overview

A business plan is not a one-off artefact for a funding committee. It is a living document that should evolve with the business across its entire lifetime. This skill installs the operating cadence by which the plan stays alive: what metrics feed it, how often each section is reviewed, who owns each section, where decisions get logged, what variance triggers re-planning, and when content is archived.

This skill is mandatory for SaaS / ICT plans because their assumptions decay faster than traditional industries: pricing experiments resolve in weeks, channel performance shifts quarterly, AI cost economics change every 6 months, and competitor moves can invalidate strategy overnight.

## Use When

- A business plan is being finalised for submission or internal use, and the engine must specify how the plan will be maintained
- A funded company is setting up its operating rhythm post-investment
- An existing company has a static plan that has not been updated in 6+ months and is now misaligned with reality
- An investor or board is asking how the plan-vs-actual variance will be governed
- A digital-first or SaaS-first business needs explicit cadences because its market changes faster than annual planning can absorb

## Do Not Use When

- The plan is a one-off proposal document for an external party (use `proposal-architect` instead)
- The business is in deep crisis where survival decisions override planning rhythm (stabilise first)
- The user wants a generic project plan — this is specifically the business-plan-as-living-document discipline

## Required Inputs

- The finalised or near-finalised business plan
- The list of plan assumptions (from each section) that are material to outcomes
- The current team and proposed roles (to assign ownership)
- The KPI dashboard or metrics available (or the gap, if nothing exists)
- The board / investor cadence expectations
- The country / regulatory reporting calendar (annual returns, tax filings, regulatory submissions)

## Workflow

1. **Inventory the plan's assumptions** — for each section (00 through 16), extract the load-bearing assumptions. For SaaS plans, these typically include: ARR growth, churn, NRR, CAC, conversion rates, gross margin, payment-rail availability, FX rate, AI cost per tenant, key-customer concentration, regulatory status.
2. **Map each assumption to a metric / signal** — every assumption needs a measurable proxy. If a metric does not yet exist, note the instrumentation requirement.
3. **Assign cadence** to each section — weekly / monthly / quarterly / annual / trigger-only. See the cadence table below.
4. **Assign owner** to each section — CEO / CFO / Head of Product / Head of GTM / Head of CS / Founder / Board chair. Avoid "everyone owns it" — that means no one does.
5. **Define variance thresholds** — at what plan-vs-actual gap does the section trigger a re-plan? Default: ±15% on revenue metrics, ±25% on cost metrics, ±5pp on churn, ±10pp on NRR.
6. **Set up the decision log** — a single canonical location (Notion / Coda / Confluence / shared doc) where every material decision is recorded with: date, decision, alternatives considered, evidence, decision-maker, expected outcome, review date.
7. **Define trigger-replan events** — explicit events that force an immediate re-plan regardless of cadence: founder departure, key-customer churn, regulatory shock, FX shock >10%, technology shock (AI-cost spike, platform deprecation), funding round closure, major hire / fire.
8. **Define sunset policy** — when does a section's content get archived? Default: when the section's assumptions have been replaced by ≥2 quarterly updates, and the original content no longer reflects current strategy.
9. **Configure the Mission/Strategy/Projects/Omissions/Tracking (MSPOT) artefact** — adopt HubSpot's MSPOT (Cotton) as the annual artefact that summarises the living plan. Mission rarely changes; Strategy changes annually; Projects are the 4–5 big initiatives; Omissions are the explicit "not this year" list; Tracking is the KPI dashboard.
10. **Document the cadence calendar** — produce a 12-month rolling cadence calendar (weekly stand-up, monthly business review, quarterly board pack, annual strategy refresh).

## Cadence Table by Section

| Section | Weekly | Monthly | Quarterly | Annual | Trigger |
|---|---|---|---|---|---|
| 01 Exec Summary | | | | refresh | acquisition / pivot |
| 02 Company Overview | | | | refresh | legal change |
| 03 Products | | KPI review | roadmap re-plan | | major launch / sunset |
| 04 Market | | | competitor scan | TAM refresh | major entrant / regulation |
| 05 Target Market | | | ICP refresh | persona refresh | win/loss data shift |
| 06 Competitive | | | scan | full re-analysis | major M&A |
| 07 Marketing/Sales | metrics | MBR | full strategy review | full re-plan | channel collapse / 2× growth |
| 08 Operations | | SLA review | process audit | annual review | outage / SLA breach |
| 09 Management/Team | | hiring update | org review | annual offsite | senior departure |
| 10 Financial Projections | actuals vs plan | full review | re-forecast | new 3yr plan | variance >15% |
| 11 Funding Request | | runway check | | | round opens / closes |
| 12 Risk | | risk-flag review | full re-analysis | | new top-3 risk |
| 13 Implementation | sprint planning | milestone review | gate review | | milestone slip >30 days |
| 14 AI Integration | tool stack | | full review | | new model / cost shock |
| 16 Sustainability | | | impact KPI | full review | regulatory change |

## AI Living-Plan Cadence (mandatory for AI-feature-led plans)

When AI is material to the plan (typically >2% of ARR or load-bearing to product), add the following AI-specific cadence on top of the section-by-section cadence above. Each element has explicit owner and variance threshold.

| AI element | Cadence | Owner | Variance threshold | Trigger-replan condition |
|---|---|---|---|---|
| Eval suite scores (accuracy / hallucination / refusal / latency) | weekly | Head of AI | -5pp on any metric | -10pp in single week |
| Per-tenant AI cost (median + top decile) | monthly | CFO + Head of AI | +20% MoM | sustained +30% over 2 months |
| AI Gross Margin | monthly | CFO | -3pp MoM | -5pp QoQ |
| AI-cost-as-%-of-ARR | monthly | CFO | >15% alarm | >20% absolute |
| Hallucination rate (production sampling) | monthly | Head of AI + Head of QA | +1pp absolute | sev-1 hallucination event = immediate |
| Cache-hit ratio | weekly | Head of AI | -10pp from baseline | -20pp |
| Token usage per query | weekly | Head of AI | +25% WoW | +50% WoW |
| Retraining trigger watch | monthly | Head of AI | drift >threshold | concept drift confirmed |
| Model-deprecation watch | monthly | Head of AI / CTO | provider notice | deprecation announced |
| Provider pricing watch | weekly + per-change | Head of AI / CTO | any change | major change (>30%) |
| AI moat reassessment | quarterly | CEO + Head of Strategy | -3 points on rubric | competitor parity claim |
| Regulatory AI watch | quarterly | Head of Legal / Compliance | new rule | active enforcement against analogue |
| AI-incident log | continuous + monthly review | Head of AI | any sev-1 | sev-1 customer-impact event |
| AI vendor concentration | quarterly | CFO + CTO | >80% on single provider | provider EULA / pricing shock |
| AI talent retention | quarterly | Head of People + CTO | >20% AI-team attrition | departure of AI lead |
| AI governance committee | monthly | Committee chair | missed meeting | governance failure |
| Training-data provenance audit | quarterly | Head of AI / Data | new data source | data-rights challenge |
| AI sustainability KPIs | quarterly | Sustainability lead + CTO | regression from baseline | structural shift |

The AI cadence is operationalised through:
- `skills/10-financial-projections/saas-ai-unit-economics-and-cogs/SKILL.md` — economics + cost
- `skills/10-financial-projections/saas-ai-cost-of-tenant-calculator/SKILL.md` — per-tenant cost
- `skills/12-risk-analysis/saas-ai-risk-and-stress-test/SKILL.md` — risk register + stress
- `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md` — moat reassessment
- `skills/meta-ai-bankability-and-investor-readiness/SKILL.md` — scorecard refresh
- `skills/08-operations-plan/references/ai-cost-and-vendor-management-ops.md` — operations
- `skills/16-sustainability-strategy/saas-ai-sustainability-and-ethics/SKILL.md` — ethics + sustainability
- `skills/meta-board-and-investor-reporting/references/saas-ai-board-pack-section.md` — reporting

## The MSPOT Annual Artefact

Cotton (HubSpot) MSPOT structure:

- **M**ission — the unchanging "why we exist" (refreshed only with company-defining events)
- **S**trategy — the "how we win this year" (annual refresh; quarterly review)
- **P**rojects — the 4–5 big initiatives this year; everything else is BAU or omitted
- **O**missions — the explicit list of things we are NOT funding this year (the "no" list)
- **T**racking — the KPI dashboard with explicit targets and review cadence

The Omissions section is the highest-leverage discipline; it's how the organisation limits the CEO's appetite and prevents indigestion.

## The Decision Log Standard

Every material decision recorded with:
- Date
- Decision title and one-line description
- Alternatives considered (do-nothing always one of them — Haines discipline)
- Evidence considered (data, customer interviews, market signals)
- Assumptions made
- Decision-maker(s)
- Expected outcome / success criteria
- Review date (when do we check if this worked)
- Outcome (filled in at review date — Haines post-implementation audit discipline)

## The Plan-vs-Actual Variance Protocol

When variance exceeds threshold:
1. **Diagnose** — is the variance from execution failure (we missed the plan) or from environmental shift (plan assumption was wrong)?
2. **Reconcile** — does this variance invalidate downstream sections? (A churn miss propagates to LTV → unit economics → runway → funding ask.)
3. **Re-plan** — produce a delta to the affected sections; do not rewrite untouched sections.
4. **Log** — the variance, the diagnosis, the change, the decision-maker in the decision log.
5. **Communicate** — notify the board / investors with the diagnosis and remediation; do not surprise them at the next board meeting.

## Trigger-Replan Events (force immediate re-plan regardless of cadence)

- Founder or C-suite departure
- Loss of customer representing >10% of ARR
- Currency depreciation >10% in 30 days
- Regulatory event invalidating a material assumption (e.g. payment-rail ban, data-residency law)
- Technology shock (key API deprecated, AI cost shift, security breach)
- Funding round closure (new capital changes the runway plan)
- M&A activity (own acquisition, key competitor acquired)
- Major key-supplier failure (AWS region outage extending >24h, key payment-gateway suspension)

## Quality Bar

- Every load-bearing assumption in the plan has an owner, a metric, and a cadence
- Every section has a defined review cadence
- A canonical decision log exists and is being maintained
- Variance thresholds are explicit, not implicit
- Trigger-replan events are enumerated, not vague
- MSPOT (or equivalent) is produced annually and visible to the team
- Plans more than 6 months old without quarterly updates should be flagged as stale

## Anti-Patterns

- Treating the business plan as a fundraising artefact that gets archived after the round closes
- "We'll update it when we have time" — no, you won't; install the cadence
- KPI dashboards that are not tied to plan assumptions
- Decisions made informally without logging — institutional memory dies with founder turnover
- Sections that haven't been touched in 12+ months but are still treated as canonical
- Mission / Strategy / Vision in one document with no Omissions list

## Outputs

- A cadence calendar for the next 12 months
- A per-section ownership and variance-threshold matrix
- A populated decision-log template
- An MSPOT artefact for the current year
- A trigger-replan event list customised to the business
- A handoff document to the operating team explaining how to maintain the plan

## References

- `references/living-business-plan-operating-model.md` — full operating-model reference
- `book-extractions/cotton-run-a-saas-business-extraction.md` — MSPOT discipline (section 10)
- `book-extractions/haines-how-to-create-a-business-case-extraction.md` — post-implementation audit, decision-log discipline
- `book-extractions/walling-saas-playbook-extraction.md` — customer-conversation cadence as living-strategy input
- `skills/meta-quarterly-gameplan/SKILL.md` — quarterly operational rhythm (sister skill)
- `skills/meta-monitoring-evaluation/SKILL.md` — KPI dashboard discipline (sister skill)

## Africa / Uganda Context

- Annual planning cycles often align with funding-cycle calendars (Q4 USAID / FCDO budgets, Q1 corporate budgets, Q3 multilateral grants). Sync the cadence calendar with the funder calendar.
- Quarterly board packs are often required by DFIs (UDB, AfDB, IFC) — adopt their format early to avoid re-work.
- Trigger-replan events in Africa include: FX shock (KES, UGX, NGN can move 10–30% in a quarter), payment-rail policy change (Central Bank circulars affecting M-Pesa, MoMo, fintech), regulatory shock (data-localisation laws, sector-specific licensing).
- Decision log should also record political / stakeholder context — many decisions in African enterprise are co-determined by political-economy factors that pure financial logic misses; the log preserves this knowledge.

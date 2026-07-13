---
name: saas-agent-sustainability-and-ethics
description: Use when producing or reviewing the saas agent sustainability and ethics component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS Agent Sustainability & Ethics Skill

## Overview

AI ethics (handled by `saas-ai-sustainability-and-ethics`) covers fairness, transparency, consent, provenance, redress, downstream-misuse. **Agent ethics** must additionally address:

1. **Action accountability** — when the agent acts, who is accountable for the consequence?
2. **Human-final on irreversibility** — Class D actions require human-final; this is an ethical commitment, not just a risk control
3. **Audit-log retention and queryability** — the agent must be auditable end-to-end for every action
4. **Contestability / redress** — affected parties must have a way to challenge agent action and receive remediation
5. **Jobs-impact disclosure** — in markets with high formal-sector unemployment or in regulated contexts, jobs-impact disclosure is increasingly an ethical and funding requirement
6. **Multi-step compute sustainability** — agents inflate compute per task; energy footprint scales accordingly

## Use When

- Section 16 is being built for an agent-product plan
- ESG / IFC Performance Standards alignment required
- DFI / multilateral funding with social / environmental requirements
- Public-sector deployment in regulated markets
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- The product is AI-feature only without agentic action — use `saas-ai-sustainability-and-ethics`
- The agent is internal-efficiency only with no customer-facing action — generic Section 16 plus AI ethics is sufficient
- The plan is too early (pre-PMF) for full ethics-and-sustainability commitment — note the direction and the gating thresholds for adopting full discipline

## Required Inputs

- Agent action taxonomy (A/B/C/D)
- Customer-facing impact
- Jobs-impact estimate (if applicable)
- Energy per task estimate
- Channel mix
- Local-language coverage
- Affected-party demographics
- Insurance / indemnity coverage

## Workflow

1. **Action-accountability declaration** — for each action class, who is the accountable party? Vendor (you), customer (your customer), end-user, or shared? Document in customer contract, in regulator submissions, in audit-log schema.
2. **Human-final commitment on Class D** — declare explicitly. Document the human-final UX, the double-signing, the audit. Non-negotiable.
3. **Audit-log retention and queryability** — declare retention period (typically 3-7+ years for regulated; longer if sectoral), queryability standard (regulator-on-demand), immutability mechanism.
4. **Contestability / redress workflow** — affected party submits request; SLA for response; remediation options; escalation path. Document the workflow and the workforce.
5. **Jobs-impact disclosure** — if agent displaces or substantially modifies roles, disclose transparently. Re-skilling / redeployment commitment where applicable. Engage labour representatives in regulated sectors.
6. **Sustainability KPIs:**
   - Energy per resolved task (kWh or equivalent)
   - Water for cooling (where in-region inference)
   - Embodied carbon contribution
   - Multi-step compute inflation vs single-shot LLM baseline
   - Cache-hit ratio (sustainability win)
   - Model-mix downshift (sustainability win)
   - In-region inference vs cross-region (latency + footprint trade-off)
7. **Local-language and channel-access ethics** — agents should serve the languages and channels their users actually use; English-only chat-only is an accessibility failure in African markets.
8. **Provenance** — training-data provenance audited; customer-data not used for cross-customer training without explicit consent.
9. **Downstream-misuse risk** — acceptable-use policy; abuse detection; rate-limit; kill-switch.
10. **Insurance + indemnity alignment** — ethical commitments backed by insurance / reserve where applicable.
11. **External review / certification** — consider third-party AI ethics review for vertical / regulated agents.
12. **Wire to bankability** — `meta-agent-bankability-and-investor-readiness` consumes ethics evidence.

## Quality Bar

- Action-accountability declared per class
- Human-final on Class D non-negotiable and documented
- Audit-log retention + queryability declared
- Contestability / redress workflow operational
- Jobs-impact disclosed where applicable
- Sustainability KPIs measured and reported
- Local-language and channel coverage stated as ethics commitment
- Training-data provenance audited
- Downstream-misuse controls operational
- Cross-referenced to bankability, board reporting, risk

## Anti-Patterns

- "Customer is responsible for the action" without contract clarity
- Class D agentic without human-final
- Audit-log only for engineering debugging; not regulator-acceptable
- No contestability workflow
- Jobs-impact ignored in public-sector deployments
- Sustainability KPIs absent
- English-only agent in multi-lingual market positioned as "AI for everyone"
- Customer-data quietly used for cross-customer training
- Downstream-misuse not monitored

## Outputs

- Action-accountability matrix (per class)
- Human-final policy on Class D
- Audit-log retention + queryability spec
- Contestability / redress workflow
- Jobs-impact disclosure (where applicable)
- Sustainability KPI set with baselines and targets
- Local-language and channel ethics commitment
- Training-data provenance audit
- Downstream-misuse controls
- Insurance + indemnity alignment
- External-review / certification posture

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Audit-log review | monthly | Compliance + AI Safety | findings |
| Contestability request response | continuous | Compliance | SLA breach |
| Jobs-impact tracking | quarterly | CEO + HR | shift in impact |
| Sustainability KPIs | quarterly | Sustainability lead + CTO | regression |
| Training-data provenance audit | quarterly | Head of AI | new data source |
| Misuse detection report | monthly | AI Safety + Compliance | trend up |
| External review cadence | annual | CEO + Compliance | finding |

## References

- `references/agent-ethics-and-sustainability-block.md` — Section 16 block template (also lives at `16-sustainability-strategy/references/`)
- `skills/16-sustainability-strategy/saas-ai-sustainability-and-ethics/SKILL.md` — AI parent
- `skills/16-sustainability-strategy/SKILL.md` — generic
- `skills/12-risk-analysis/saas-agent-risk-and-stress-test/SKILL.md` — risk
- `skills/meta-agent-bankability-and-investor-readiness/SKILL.md` — bankability
- `book-extractions/agent-products-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **Jobs-impact in African public-sector deployments** is politically and reputationally consequential; transparent disclosure and re-skilling commitment increasingly required by donors / multilaterals / regulators
- **Local-language coverage as ethics** — agents serving African end-users that don't cover Swahili / Hausa / Yoruba / Amharic / Luganda / Zulu / Xhosa / Wolof / Tigrinya / Lingala have accessibility gaps; commit to coverage roadmap
- **Channel ethics** — chat-only excludes non-smartphone / unbanked users; commit to USSD / SMS / IVR coverage in mass-market deployments
- **Contestability in low-literacy or low-access contexts** — design redress workflows that work in vernacular, via voice, via in-person mediation when needed
- **Training-data provenance** — African-language data must be sourced with consent and proper licensing (Lacuna Fund standards, Masakhane practices); commercial use of community-built data requires explicit terms
- **Sovereign-AI / residency** — for sustainability, in-region inference reduces network footprint and supports local data-centre demand; consider as positive sustainability story (paired with grid-energy considerations)
- **Insurance / indemnity** — thin in African markets; ethical commitments must be backed by reserve when insurance is not available
- **External review** — Africa AI Safety Consortium, Lelapa AI partners, Mozilla African Innovation Mradi, university ethics boards are options for third-party review
- **Sectoral ethics** — health (UMDPC / KMPDC / HPCSA / Pharmacy Councils), finance (BoU / CBK / CBN / SARB / FSCA / BNR), legal (LSK / SCUEA / Law Society SA / NBA) have sector-specific ethics expectations

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Materiality evidence, impact baseline, stakeholder requirements, climate or ethics risks, governance roles, and costed initiatives for saas agent sustainability and ethics | Operations, stakeholder evidence, verified sustainability sources, and approved financial model | Yes | If absent, a baseline, materiality source, methodology, or responsible owner is unavailable, describe the gap and withhold the target or assurance claim. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Material sustainability and ethics strategy with targets, owners, costs, and assurance limits | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas agent sustainability and ethics exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas agent sustainability and ethics release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Materiality decision record, baseline/source register, target calculation, governance owner, and adverse-impact review | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas agent sustainability and ethics decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas agent sustainability and ethics review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas agent sustainability and ethics, the controlling focus is agent energy and tool-use footprint, autonomous-action ethics, labour effects, oversight, and incident accountability. This skill may analyse impacts and draft commitments; it may not certify ESG performance, purchase offsets, make public claims, or approve environmental or ethical commitments without authority and verification. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas agent sustainability and ethics, loss of evidence about agent energy and tool-use footprint, autonomous-action ethics, labour effects, oversight, and incident accountability activates degraded mode. If the controlling saas agent sustainability and ethics evidence is unavailable, the same boundary applies. When a baseline, materiality source, methodology, or responsible owner is unavailable, describe the gap and withhold the target or assurance claim. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas agent sustainability and ethics, a proposed sustainability or AI-ethics claim lacks a measurable baseline, operating owner, or credible mitigation| remove the public claim, define the measurement and governance step, and retain it as an internal objective | Greenwashing or ethics-washing creates legal, reputational, and investor risk |
| For saas agent sustainability and ethics, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas agent sustainability and ethics decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas agent sustainability and ethics, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete material sustainability and ethics strategy with targets, owners, costs, and assurance limits, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas agent sustainability and ethics decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect materiality evidence, impact baseline, stakeholder requirements, climate or ethics risks, governance roles, and costed initiatives and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce material sustainability and ethics strategy with targets, owners, costs, and assurance limits with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Material sustainability and ethics strategy with targets, owners, costs, and assurance limits must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Materiality decision record, baseline/source register, target calculation, governance owner, and adverse-impact review must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to saas agent sustainability and ethics, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas agent sustainability and ethics, treating an unavailable materiality evidence, impact baseline, stakeholder requirements, climate or ethics risks, governance roles, and costed initiatives as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing material sustainability and ethics strategy with targets, owners, costs, and assurance limits that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

An autonomous recruitment agent reduces recruiter time but may exclude candidates without a clear appeal path. Limit decision authority, log interventions, and assign incident and appeal ownership.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas agent sustainability and ethics; no local deep-dive reference is declared.
- For saas agent sustainability and ethics claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->

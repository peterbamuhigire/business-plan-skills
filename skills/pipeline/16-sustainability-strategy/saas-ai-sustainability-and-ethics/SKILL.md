---
name: saas-ai-sustainability-and-ethics
description: Use when producing or reviewing the saas ai sustainability and ethics component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# SaaS AI Sustainability & Ethics Skill

## Overview

ESG and IFC Performance Standards now include AI dimensions. AI training and inference are real energy / water / carbon line items. AI fairness, transparency, and misuse risk are real ethical exposures. This skill installs the discipline to address both in Section 16 in a way that survives DFI diligence and ESG audit.

## Use When

- Section 16 of an AI-feature-led plan is being built
- DFI / ESG diligence is upcoming
- AI-for-good grant proposal requires sustainability + ethics articulation
- Plan operates in a jurisdiction with active AI ethics regulation (EU AI Act, KE / NG / ZA AI policy)
- Sovereign-AI tender requires ethics + sustainability evidence

## Do Not Use When

- AI is internal-efficiency only — use `16-sustainability-strategy` standard
- Plan has no AI dependency

## Required Inputs

- AI architecture (which models, providers, hosting locations)
- Estimated inference volume (queries × tokens × month)
- Training cycles per year (or none)
- Vertical / use case
- Data sensitivity profile
- Jurisdiction(s)

## Workflow

1. **Estimate AI energy / carbon / water** per `references/ai-ethics-and-sustainability-block.md`:
   - **Inference energy**: tokens × kWh-per-token (provider-published or Hugging Face estimator); convert to kgCO2e using grid mix of hosting region
   - **Training energy**: training compute × hours × GPU power × cooling factor; embodied carbon of GPUs amortised
   - **Water** — data-centre water-for-cooling: highly region-dependent; Cape Town has water stress; Johannesburg medium; Lagos low; Cairo high
   - **Embodied carbon** of GPU manufacture amortised over GPU lifetime
2. **Set AI sustainability KPIs** for the plan:
   - kgCO2e per million tokens served
   - kgCO2e per active tenant per month
   - % of inference on renewable-powered regions
   - Cache-hit ratio (cache is sustainability lever)
   - Model-mix efficiency (smaller models = less energy)
3. **Build the AI ethics framework**:
   - **Fairness** — bias audit cadence, fairness metrics by demographic dimension, mitigation playbook
   - **Transparency** — model cards, datasheets for training data, user-facing AI-decision disclosure
   - **Redress** — user mechanism to challenge AI decisions, escalation to human review
   - **Consent** — training-data consent, inference-data consent, opt-out mechanisms
   - **Training-data provenance** — sourcing, licensing, consent, compensation, curation
   - **Downstream-misuse risk** — what bad uses are possible? what's the EULA / TOS posture?
4. **Map to applicable frameworks**:
   - **EU AI Act** — risk category (unacceptable / high / limited / minimal); compliance posture
   - **NIST AI Risk Management Framework** — Govern / Map / Measure / Manage cycle
   - **OECD AI Principles**
   - **AU Continental AI Strategy** ethics provisions
   - **National AI policies** (KE / NG / ZA / RW / UG)
   - **IFC Performance Standards** (PS1 management, PS2 labour, PS5 land if data-centre, PS6 if relevant)
   - **GRI standards** AI-disclosure additions
   - **TCFD** climate disclosures (Scope 2 from compute; Scope 3 from cloud providers)
5. **Establish the AI governance committee** — composition, RACI, decision authority for model changes, data uses, incident response.
6. **Build the AI-incident protocol** — sev-1 / sev-2 / sev-3 classification, customer comms, regulator notification, remediation, reserve drawdown.
7. **Build the local-language / inclusion commitments** — which languages are covered, fairness across language groups, accessibility (screen-reader, low-bandwidth, mobile-first), socio-economic inclusion.
8. **Build the disclosure plan** — what gets reported to whom on what cadence (board, investors, regulators, customers, public).
9. **Wire to risk register** — ethics / sustainability risks cross-reference `saas-ai-risk-and-stress-test`.
10. **Wire to living plan** — sustainability KPIs quarterly, ethics committee monthly, incident-log continuous.

## Quality Bar

- Energy / carbon / water estimated with explicit methodology
- AI sustainability KPIs stated with baselines and targets
- Ethics framework specific, not generic
- Training-data provenance documented honestly
- Applicable regulatory frameworks mapped; compliance posture stated
- Governance committee composition + RACI defined
- AI-incident protocol exists
- Local-language / inclusion commitments specific
- Disclosure cadence defined

## Anti-Patterns

- "We're carbon-neutral via offsets" with no measurement methodology
- Ethics framework that is generic principles without operational commitment
- Training-data provenance left vague
- "We comply with regulations" without naming them
- Governance committee aspirational, not operating
- No incident protocol
- AI-fairness claimed without metric

## Outputs

- AI energy / carbon / water estimates with methodology
- AI sustainability KPI dashboard
- AI ethics framework
- Training-data provenance statement
- Regulatory mapping + compliance posture
- AI governance committee composition + RACI
- AI-incident protocol
- Local-language / inclusion commitments
- Disclosure plan
- Cross-references to risk, ops, talent, board reporting

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| AI sustainability KPIs | quarterly | Sustainability lead + CTO | regression from baseline |
| AI ethics committee | monthly | Committee chair | missed meeting |
| AI incident log | continuous + monthly review | Head of AI | sev-1 incident |
| Training-data provenance audit | quarterly | Head of AI / Data | new data source |
| Bias audit | semi-annual | Head of AI / QA | regression |
| Regulatory watch | quarterly | Head of Legal | new regulation |
| Disclosure cadence | per reporting plan | CEO + CFO | missed disclosure |

## References

- `references/ai-ethics-and-sustainability-block.md` — full ethics + sustainability framework with worked examples
- `skills/16-sustainability-strategy/SKILL.md` — generic sustainability flow
- `skills/12-risk-analysis/saas-ai-risk-and-stress-test/SKILL.md` — risk cross-reference
- `skills/meta-sustainability/SKILL.md` — IFC PS framework
- `skills/14-ai-integration/references/ai-sustainability-tools.md` — sustainability tools reference
- `book-extractions/cotton-run-a-saas-business-extraction.md` — SaaS sustainability angle

## Africa / Uganda Application Notes

- **Energy mix** matters: SA grid is coal-heavy (high kgCO2e per kWh); Kenya / Ethiopia / Uganda increasingly hydro / geothermal (lower); Nigeria mixed. Hosting choice has material sustainability impact.
- **Water stress**: Cape Town / Johannesburg data centres face water cost pressure; this affects sovereign-AI tender pricing.
- **Local-language coverage** is itself an inclusion commitment with measurable progress (Swahili, Hausa, Yoruba, Amharic, Luganda, Igbo, Zulu, Xhosa, Wolof, Tigrinya).
- **Gender disaggregation** required by most DFIs and AI-for-good grants.
- **Data sovereignty + ethics** intersect: KE, NG, ZA, UG, RW data protection laws each have AI provisions or related case law evolving.
- **Algorithmic-fairness audits in regulated African verticals** (lending, hiring, insurance) increasingly expected by regulators; build the discipline early.
- **AI-incident regulator notification** — KE DPC, NG NDPC, ZA Information Regulator each have notification expectations evolving; track requirements.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Materiality evidence, impact baseline, stakeholder requirements, climate or ethics risks, governance roles, and costed initiatives for saas ai sustainability and ethics | Operations, stakeholder evidence, verified sustainability sources, and approved financial model | Yes | If absent, a baseline, materiality source, methodology, or responsible owner is unavailable, describe the gap and withhold the target or assurance claim. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Material sustainability and ethics strategy with targets, owners, costs, and assurance limits | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| saas ai sustainability and ethics exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| saas ai sustainability and ethics release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Materiality decision record, baseline/source register, target calculation, governance owner, and adverse-impact review | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| saas ai sustainability and ethics decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| saas ai sustainability and ethics review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For saas ai sustainability and ethics, the controlling focus is AI compute footprint, data ethics, bias, affected stakeholders, human oversight, and claims assurance. This skill may analyse impacts and draft commitments; it may not certify ESG performance, purchase offsets, make public claims, or approve environmental or ethical commitments without authority and verification. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For saas ai sustainability and ethics, loss of evidence about AI compute footprint, data ethics, bias, affected stakeholders, human oversight, and claims assurance activates degraded mode. If the controlling saas ai sustainability and ethics evidence is unavailable, the same boundary applies. When a baseline, materiality source, methodology, or responsible owner is unavailable, describe the gap and withhold the target or assurance claim. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For saas ai sustainability and ethics, a proposed sustainability or AI-ethics claim lacks a measurable baseline, operating owner, or credible mitigation| remove the public claim, define the measurement and governance step, and retain it as an internal objective | Greenwashing or ethics-washing creates legal, reputational, and investor risk |
| For saas ai sustainability and ethics, A current legal, regulatory, tax, accounting, market, or platform claim controls the saas ai sustainability and ethics decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For saas ai sustainability and ethics, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete material sustainability and ethics strategy with targets, owners, costs, and assurance limits, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact saas ai sustainability and ethics decision, intended reader, jurisdiction, business stage, and permission boundary.
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
- Language remains specific to saas ai sustainability and ethics, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In saas ai sustainability and ethics, treating an unavailable materiality evidence, impact baseline, stakeholder requirements, climate or ethics risks, governance roles, and costed initiatives as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing material sustainability and ethics strategy with targets, owners, costs, and assurance limits that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

An AI feature uses a large model for every request although a smaller model passes most tasks. Measure quality and energy-cost trade-offs, route simple tasks to the smaller model, and report the boundary honestly.

## References

- Use the verified project evidence register and the owning upstream pipeline section for saas ai sustainability and ethics; no local deep-dive reference is declared.
- For saas ai sustainability and ethics claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->

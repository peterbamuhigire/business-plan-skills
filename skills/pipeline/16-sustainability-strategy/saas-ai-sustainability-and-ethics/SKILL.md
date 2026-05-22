---
name: saas-ai-sustainability-and-ethics
description: AI sustainability (compute energy intensity, water for cooling, embodied carbon of GPU manufacture) and AI ethics (fairness, transparency, redress, consent, training-data provenance, downstream-misuse risk) for a SaaS plan. Practical KPIs aligned with IFC Performance Standards, Stanford AI Index, IEA AI-and-energy, GRI / TCFD. Use when Section 16 of an AI-feature-led plan is being built or DFI / ESG diligence is upcoming.
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

---
source: Mozilla African Innovation Mradi, GSMA AI for Impact, IDRC AI4D, Lacuna Fund, Google.org, Microsoft AI for Good, McGovern Foundation, Gates AI envelopes — call requirements 2023-2026; engine synthesis
frameworks: [Theory-of-change for AI; Training-data provenance; Community-benefit; Ethics + explainability; Local-capacity-building; Impact KPI framework; Sustainability beyond grant]
skill: saas-ai-for-good-grant-proposal
cross-reference: [saas-ai-funding-stage-playbook, meta-sustainability, meta-monitoring-evaluation, ai-ethics-and-sustainability-block]
---

# SaaS AI-for-Good Grant Proposal Template

## 1. The 11-section proposal architecture

Most AI-for-good grantmakers expect this structure (with section-name variations):

1. **Executive summary** (1 page)
2. **Problem statement** (with quantified evidence)
3. **Theory-of-change**
4. **Intervention — the AI capability**
5. **Training-data provenance + ethics + governance**
6. **Local-capacity-building**
7. **Impact KPIs + M&E plan**
8. **Budget**
9. **Team + partners**
10. **Sustainability beyond grant period**
11. **Risks + mitigations**

## 2. Theory-of-change (the centrepiece)

| Component | Definition | Example (dairy AI) |
|---|---|---|
| **Problem** | Quantified problem statement | "Smallholder dairy farmers (1.2M in East Africa) lose 18-25% of milk income to cooperative-management inefficiencies and information asymmetry; Luganda-language operational guidance unavailable from any digital channel" |
| **Inputs** | Data, compute, talent, partnerships | "Luganda training data partnership with Lelapa; eval-curator network of veterinary officers; Liquid Cape Town GPU; 3 ML engineers" |
| **Activities** | What we do | "Build Luganda LLM fine-tune; deploy to 200 cooperatives; train 40 extension officers as AI-aware coaches; build eval suite with vet-officer curation" |
| **Outputs** | Direct deliverables | "Luganda fine-tuned model deployed; 200 cooperatives onboarded; 60,000 farmers reached; eval suite with 240 cases; 40 trained AI-aware extension officers" |
| **Outcomes** | Behavioural / institutional change | "Cooperative payment dispute resolution time reduced from 14 days to 3 days; member satisfaction up from 62% to 78%; cooperative governance training participation up 45%" |
| **Impact** | Long-term societal change | "Smallholder dairy income up 8-12% across 60,000 farmers; women farmer participation in cooperative leadership up 25%; replicable model for other African verticals" |

Each component must be quantified and verifiable.

## 3. Training-data provenance (the #1 question for Lacuna / Mozilla / IDRC)

State explicitly:

- **Sources** — exact origin of training data
- **Consent** — basis (consent / contract / legitimate interest); document
- **Compensation** — for human-curated data; rates; structure
- **Curation** — bias-mitigation, quality control, representativeness
- **Licensing** — what licence does the data carry; do you have rights for AI training
- **Audit trail** — provenance log with timestamps and decision rationale
- **Data sovereignty** — where data is stored; jurisdiction; deletion process

## 4. Community benefit articulation

- **Who benefits** — specific populations (with intersectional disaggregation)
- **How is benefit measured** — KPIs with baseline / endline
- **Community consultation** — how communities shaped the intervention design
- **Data sovereignty** — community right to data about them; opt-out; deletion
- **Local ownership** — local talent built, local language served, local context understood
- **Distributed benefit** — equity dimension (gender, age, region, income, disability)

## 5. Ethics + explainability commitments (operational, not aspirational)

- **Fairness metrics** — what's measured; cadence; mitigation when bias found
- **Transparency** — model cards; datasheets; user-facing AI-decision disclosure
- **Redress** — user mechanism to challenge; escalation; SLA
- **Consent** — training-data consent; inference-data consent; opt-out
- **Bias audit** — schedule; methodology; external reviewer
- **Downstream-misuse** — TOS; detection mechanisms; revocation

## 6. Local-capacity-building (DFI / grant priority)

- **Engineers trained** — count; programme; verification
- **University partnerships** — named institutions, programme details
- **Open-source contributions** — what's released; licence; community engagement
- **Local-language coverage** — languages added; quality metrics
- **Knowledge transfer** — workshops, documentation, train-the-trainer

## 7. Impact KPI framework

| Layer | KPI | Baseline | Target | Source | Disaggregation |
|---|---|---|---|---|---|
| **Reach** | Users served (count) | 0 | 60,000 | App analytics | Gender, age, region, language |
| **Reach** | Languages covered | 2 | 5 | Product | n/a |
| **Outcome** | Payment dispute resolution time | 14 days | 3 days | App + survey | Cooperative size |
| **Outcome** | Member satisfaction | 62% | 78% | Annual survey | Gender |
| **Impact** | Smallholder dairy income change | baseline survey | +8-12% | Annual income survey | Gender, region |
| **Impact** | Women in cooperative leadership | 12% | 15% | Survey | Region |
| **Equity** | % users female | n/a | ≥45% | App analytics | n/a |
| **Equity** | % users in remote areas | n/a | ≥30% | App analytics + region | n/a |

## 8. Budget (line-item; grant-format)

Typical grant-format budget lines (adjust per grantmaker):

| Line | Y1 | Y2 | Y3 | Total |
|---|---|---|---|---|
| Personnel (named) | | | | |
| AI infrastructure (compute, API, hosting) | | | | |
| Training-data acquisition + labelling | | | | |
| Eval pipeline build | | | | |
| Local-capacity-building (training, workshops, university partnerships) | | | | |
| Community consultation + outreach | | | | |
| M&E (baseline, midline, endline) | | | | |
| Travel + per diem | | | | |
| Equipment | | | | |
| Indirect cost (per grantmaker cap; often 12-18%) | | | | |

Match the grantmaker's required line items exactly.

## 9. Team + partners

- **Core team** — named with relevant credentials
- **Domain advisors** — named with affiliations
- **Implementation partners** — named with MoUs
- **Local partner organisations** — community-based, university, government
- **Technical partners** — AI / data partners (Lelapa, Masakhane, AIMS, etc.)
- **M&E partner** (often required for research grants)

## 10. Sustainability beyond grant period

This is where most grant proposals fail. State explicitly:

- **Commercial revenue path** — paying tiers, ARR trajectory after grant
- **Institutional adoption** — public-sector procurement; line-item budget commitment
- **Open-source community** — sustainable contribution after grant period
- **Follow-on funding** — anticipated commercial round; other grant pathways
- **Cost trajectory** — declining unit cost via scale + cost engineering
- **Avoid** "we'll raise a Series A" as sole sustainability path (circular logic)

## 11. Risks + mitigations

Honest risk register:
- Technical (model performance, eval coverage)
- Operational (deployment, adoption, training)
- Community (cultural fit, language quality, trust)
- Regulatory (data protection, AI ethics evolution)
- Financial (FX, cost spike, capacity scarcity)
- Sustainability (commercial path, follow-on funding)

For each: probability, impact, mitigation, owner.

## 12. Grantmaker-specific tailoring

| Grantmaker | What to emphasise |
|---|---|
| **Mozilla African Innovation Mradi** | Community-benefit + local ownership; open-source contribution |
| **GSMA AI for Impact** | Mobile / WhatsApp / USSD AI channel; SDG alignment |
| **IDRC AI4D Africa** | Research-and-policy angle; capacity-building; replicability |
| **Google.org AI for Social Good** | Scale + measurable impact; technical rigor |
| **Microsoft AI for Good** | Azure-aligned; partnership willingness |
| **Lacuna Fund** | Training-data quality + provenance; low-resource languages; openness |
| **McGovern Foundation** | Responsible AI; governance + ethics depth |
| **Gates AI envelopes** | SDG-3 (health) or SDG-2 (agriculture) or SDG-5 (gender); evidence; scale |
| **Wellcome** | Health AI in LMICs; research rigour; ethics |
| **Hewlett / Ford / Omidyar** | Democracy / equity / responsible-tech angle |

## 13. Anti-patterns

- "AI will improve outcomes" without theory-of-change
- Training-data provenance vague
- Ethics commitments as principles without operational mechanism
- Impact KPIs all reach (no outcome / impact)
- Budget mismatched to grantmaker format
- Sustainability via "Series A" only
- Generic proposal copy-pasted across funders
- Local-capacity-building as line item without mechanism
- Reach without disaggregation

## 14. Living-plan link

| Element | Cadence | Owner |
|---|---|---|
| Grant pipeline | monthly | Grants lead + CEO |
| Active-grant M&E reporting | per grant cycle | Programme manager |
| Impact KPI baseline / midline / endline | per grant plan | M&E lead |
| Training-data provenance audit | quarterly | Head of AI / Data |
| Capacity-building outputs | quarterly | Programme manager |
| Sustainability check-in | quarterly | CEO + CFO + Grants |

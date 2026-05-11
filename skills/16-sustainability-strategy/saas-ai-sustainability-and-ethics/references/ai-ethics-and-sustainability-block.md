---
source: Stanford AI Index 2024; Hugging Face energy estimator; IEA AI-and-energy report; IFC PS2-PS6; EU AI Act; NIST AI RMF; AU Continental AI Strategy; engine synthesis
frameworks: [AI energy / carbon / water estimation; AI ethics framework; Local-language inclusion; AI compliance map; Disclosure plan]
section: 16-sustainability-strategy
cross-reference: [saas-ai-sustainability-and-ethics, saas-ai-risk-and-stress-test, meta-sustainability]
---

# AI Ethics & Sustainability Block — Reference

The block that should sit in Section 16 (and the data room) of any AI-feature-led SaaS plan. Provides the methodology investors, DFIs, and regulators expect.

## 1. AI energy / carbon / water estimation methodology

### Inference energy

```
inference energy (kWh) = total tokens served × energy-per-token (model-specific)
```

Energy-per-token typical 2025 estimates (varies by provider, region, hardware):
- GPT-4 class: ~0.0003 kWh / 1k tokens
- GPT-4o-mini class: ~0.00005 kWh / 1k tokens
- Claude Sonnet class: ~0.0003 kWh / 1k tokens
- Claude Haiku class: ~0.00006 kWh / 1k tokens
- Llama 3 70B self-hosted: ~0.0004 kWh / 1k tokens (varies by hardware utilisation)
- Embeddings: ~0.000001 kWh / 1k tokens

```
kgCO2e (inference) = inference energy × grid-emissions-factor (region-specific)
```

Grid emissions factors (kg CO2 / kWh):
- SA (Eskom): ~0.95
- KE: ~0.20-0.30 (hydro + geothermal)
- ET, UG, RW: ~0.05-0.15 (hydro)
- NG: ~0.40
- EG: ~0.40
- US (national avg): ~0.40
- EU (avg): ~0.25
- France: ~0.06 (nuclear)
- Sweden: ~0.04 (hydro + nuclear)

### Training energy

```
training energy (kWh) = GPU-hours × GPU-power × cooling-factor
```

For fine-tuning (typical):
- Small fine-tune (1M tokens): ~10 GPU-hours × 0.7 kW × 1.3 cooling = ~9 kWh
- Medium fine-tune (100M tokens): ~500 GPU-hours × 0.7 kW × 1.3 = ~450 kWh
- Large fine-tune (1B tokens): ~5,000+ GPU-hours; ~4,500+ kWh

### Embodied carbon (GPU manufacture)

Amortise over GPU lifetime (typical 4-5 years):
- H100: ~3,000-5,000 kg CO2e embodied; divided by lifetime hours
- A100: ~2,000-3,500 kg CO2e embodied; divided by lifetime hours

For most SaaS plans, embodied carbon is a smaller line than inference + training; report if material.

### Water for data-centre cooling

```
data-centre water (L) = data-centre power (kWh) × Water Usage Effectiveness (WUE)
```

WUE varies by data centre:
- AWS, Azure, GCP modern hyperscale: 0.15-0.50 L/kWh
- Older data centres: 1.0-3.0 L/kWh
- Cape Town water-stressed: factor in pricing

## 2. AI sustainability KPIs (for the plan)

| KPI | Target | Cadence |
|---|---|---|
| kgCO2e per million tokens served | <50 (premium model) / <10 (cheap model) / <2 (embedding) | Quarterly |
| kgCO2e per active tenant per month | <5 typical SaaS / <20 AI-heavy | Monthly |
| % of inference on renewable-powered regions | rising; target >50% by Y3 | Quarterly |
| Cache-hit ratio | rising; sustainability lever | Weekly |
| Model-mix efficiency (smaller-model share for routine queries) | rising | Monthly |
| Local-language coverage (count of supported African languages) | rising | Quarterly |
| Bias-audit completion rate | 100% per cycle | Per audit |
| Eval coverage % | rising | Monthly |
| AI-incident count (sev-1, sev-2) | trending to zero | Per incident + monthly |
| Customer redress requests resolved % | 100% | Per request + monthly |
| Gender ratio in AI team | per DFI / grant requirement | Quarterly |

## 3. AI ethics framework (the operational commitments)

### Fairness

- **Bias audit cadence**: semi-annual minimum; annual for high-stakes products
- **Fairness metrics**: tracked by gender, geography, income, disability, language where data permits
- **Mitigation playbook**: prompts, data balancing, post-hoc adjustment, model selection
- **Disclosure**: bias audit summary to customers / regulators

### Transparency

- **Model cards** for any model trained or fine-tuned (Hugging Face format)
- **Datasheets** for training data (Gebru et al. format)
- **AI-decision disclosure** to users at point of AI-influenced decision
- **AI explainer** in product documentation
- **Customer-facing AI policy**

### Redress

- **User mechanism** to challenge AI decisions (UI affordance + back-end process)
- **Escalation to human review** for material decisions
- **SLA for redress response** (e.g. 5 business days)
- **Tracking of redress requests** and outcomes

### Consent

- **Training-data consent**: explicit where required; documented sourcing
- **Inference-data consent**: terms of service clarity on data handling
- **Opt-out mechanisms** where applicable
- **Data retention policy** + right-to-be-forgotten implementation

### Training-data provenance

- **Sourcing log**: every dataset's source, licence, consent basis
- **Compensation policy** for human-curated data
- **Bias-mitigation curation**: documented steps
- **EULA-exposure tracking** — model-provider EULA implications for customer data

### Downstream-misuse risk

- **EULA / TOS** restricting bad uses (e.g. mass surveillance, harmful content)
- **Detection mechanisms** for misuse patterns
- **Customer revocation** process for confirmed misuse
- **Red-team review** for new high-risk capabilities

## 4. AI compliance map

For each operating jurisdiction:

| Jurisdiction | Framework | Status / posture |
|---|---|---|
| EU (any EU customer) | EU AI Act | Risk category; conformity assessment status |
| US (enterprise customer) | NIST AI RMF | Mapping documented; voluntary |
| Kenya | KE National AI Strategy + DPA | Posture statement; DPC registration |
| Nigeria | NG NITDA NAIS + NDPA | Posture; NDPC registration |
| South Africa | ZA AI Policy Framework + POPIA | Posture; Info Regulator |
| Rwanda | RW National AI Policy + Data Protection Law | Posture; NCSA registration |
| Egypt | EG National AI Strategy + Data Protection Law | Posture; Egyptian DPC |
| Uganda | UG ICT Policy + DPPA + NITA-U AI guidelines | Posture; NITA-U registration |
| Other | AU Continental AI Strategy (member-state alignment) | Posture |

## 5. Local-language / inclusion commitments

For African plans:
- **Languages covered** today + roadmap
- **Quality metrics** per language (eval scores)
- **Equity of access** — pricing across languages (no premium just for non-English)
- **Local-context expertise** — domain experts who validate local-relevance
- **Accessibility** — screen-reader, low-bandwidth, USSD / SMS / WhatsApp channels for digital-divide
- **Gender equity** in product use + team composition
- **Disability access** — voice-input alternatives, plain-language outputs

## 6. AI governance committee structure (RACI)

| Function | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| AI policy approval | Committee | CEO | Legal, CFO, Head of AI, ethics advisor | Board, customers |
| Model change | Head of AI | CTO | Committee | Customers (if material) |
| New data source | Head of AI / Data | Head of AI | Committee, Legal | Board (if major) |
| Risk acceptance | Committee | CEO | Legal, CFO, Head of AI | Board |
| Incident response | Head of AI | CEO | Legal, Comms, Committee | Customers, Regulator |
| Bias audit | Head of AI / QA | Committee | External advisor | Board |
| External audit | CTO | CEO | Committee | Board |

Committee meets monthly; minimum quorum 3; minutes maintained.

## 7. Disclosure plan

| Audience | What | Cadence |
|---|---|---|
| Board | AI governance summary + risk register | Quarterly |
| Investors | AI section in monthly update | Monthly |
| Customers | AI policy; AI-decision disclosure in product | Continuous + on update |
| Regulator | Incident notification per jurisdiction; compliance filings | Per requirement |
| Public | Annual AI transparency report; sustainability report | Annual |

## 8. Anti-patterns

- "Carbon-neutral via offsets" with no measurement
- Ethics framework as principles without operational commitments
- Bias claim without metrics
- Training-data provenance "we use public data" without documentation
- AI committee aspirational
- No incident protocol
- "We comply with regulations" without naming them
- Local-language as marketing claim without quality metric

## 9. Living-plan link

| Element | Cadence | Owner |
|---|---|---|
| AI sustainability KPIs | quarterly | Sustainability lead + CTO |
| AI ethics committee meetings | monthly | Committee chair |
| Bias audits | semi-annual | Head of AI / QA |
| AI-incident log | continuous + monthly review | Head of AI |
| Training-data provenance audit | quarterly | Head of AI / Data |
| Regulatory watch | quarterly | Head of Legal |
| Annual transparency report | annual | Sustainability lead + Head of AI |

## 10. Africa specifics

- Renewable-grid hosting (KE, ET, UG, RW) is a real sustainability story
- Water-stress regions (Cape Town, Cairo) raise data-centre water cost over time
- Local-language coverage is a measurable inclusion KPI
- Gender disaggregation required by most DFIs and AI-for-good grants
- Algorithmic fairness in regulated African verticals (lending, insurance, hiring) increasingly regulator-expected
- AU Continental AI Strategy ethics alignment will become a procurement requirement in member states

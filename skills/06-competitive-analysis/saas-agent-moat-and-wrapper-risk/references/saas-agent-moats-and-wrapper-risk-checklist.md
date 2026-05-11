---
source: Agent-products business-plan audit (2026); 2024-2026 agent-VC diligence; Walling moats; Wardley Mapping
frameworks: [8-question agent moat test; Wrapper-risk catalogue; Foundation-model commoditisation analysis; Wardley placement for agents; Moat-or-wrapper scorecard 0-24]
skill: saas-agent-moat-and-wrapper-risk
cross-reference: [meta-agent-valuation-adjustments, saas-agent-product-strategy-and-roadmap, saas-agent-risk-and-stress-test]
---

# Agent Moats & Wrapper-Risk — Checklist

## 1. The 8-Question Agent Moat Test

Score each 0-3 (0 = absent; 1 = early signal; 2 = real but improvable; 3 = strong + compounding). Maximum = 24.

### Q1 — Proprietary tools
Tools = the action layer the agent invokes (APIs, integrations, data sources, function-calls).
- Are your tools proprietary or commoditisable?
- Are tool integrations difficult / expensive for competitors to recreate?
- Do your tools embody domain knowledge or regulatory clearance?

Score:
- 0: All tools public APIs (Stripe, Twilio, generic CRM)
- 1: Some proprietary internal tools; not yet a barrier
- 2: Multiple proprietary tools that took quarters to build / integrate
- 3: Tool registry is a substantial barrier; took years; covers regulatory / vertical specifics

### Q2 — Proprietary action data
Each customer interaction generates action data: prompts, plans, tool sequences, outcomes, interventions, human-correction signals.
- Does the data accrue per customer / per interaction in a way that improves YOUR agent specifically?
- Is the data licensed to be used for agent improvement (training, eval, prompt-tuning)?
- Is there a flywheel: more customers -> more action data -> better agent -> more wins?

Score:
- 0: No accrual loop; generic public training data only
- 1: Accrual loop in place but small volume
- 2: Real flywheel with measurable agent improvement from your data
- 3: Strong flywheel; demonstrable accuracy / cost / intervention-rate improvements traceable to action data; data exclusive

### Q3 — Integration depth
- How deeply is the agent integrated into customer system-of-record (ERP, CRM, core banking, EHR, ESS, ITSM)?
- Identity integration? SSO + role-based agent-action permissions?
- Audit-log integration (immutable, queryable, regulator-acceptable)?
- Billing integration (per-resolution metered into customer FinOps)?

Score:
- 0: Side-of-desk; copy-paste; no integration
- 1: Light integration; one system
- 2: Multi-system integration; identity + audit
- 3: Deep integration across multiple systems-of-record with audit + identity + billing

### Q4 — Eval-loop
Eval-loop = your ability to know when the agent works, when it doesn't, and to improve.
- Do you have offline eval suites + online eval sampling?
- Do you have human-correction signals from production?
- Do eval scores improve over time with evidence?
- Is the eval suite proprietary (built on customer data) or public (commodity)?

Score:
- 0: No eval discipline
- 1: Offline evals only; no online sampling
- 2: Online sampling + offline; human correction loop
- 3: Proprietary eval suite on customer data; demonstrable improvement trajectory; eval-suite itself is a moat

### Q5 — Customer-trust / brand
- Are you the trusted agent vendor in your vertical / region?
- Do you have named references that competitors cannot easily list?
- Do you have public-sector / regulated-sector references?

Score:
- 0: No referenceable customers
- 1: A few private references
- 2: Public references in target vertical
- 3: Marquee / lighthouse references; public-sector / regulator references

### Q6 — Regulatory clearance
- Do you have explicit regulator engagement (KE ODPC, NG NDPC, UG NITA-U, ZA Info Reg, sectoral regulators)?
- Has your audit log been accepted by a regulator or external auditor?
- Do you have sectoral approval (e.g. financial services / health / public sector)?
- Is there a documented path to regulatory clearance for competitors that is materially harder than yours?

Score:
- 0: No regulator engagement
- 1: Initial engagement; nothing accepted
- 2: Documented engagement + at least one acceptance
- 3: Multiple regulator engagements; accepted audit log; sectoral approval; competitors face material time-to-clearance

### Q7 — Switching cost
- Data migration friction: customer's action data and configurations would need to be replicated
- Integration switching: deep integrations would need to be rebuilt
- Retraining cost: customer-specific eval + prompt tuning would need to be redone
- Contractual lock-in alone is weak — only counts in combination with real switching cost

Score:
- 0: Easy to switch (no data, no integration, monthly contract)
- 1: Some friction (modest data, light integration)
- 2: Real friction (substantial action data, deep integration, multi-quarter retraining)
- 3: High friction (years of accrued data, deep multi-system integration, regulator-attached audit log, vertical configuration)

### Q8 — Distribution
- Channel partnerships, embedded distribution (inside a larger platform), exclusive distribution
- Channel reach competitors cannot easily replicate
- Distribution that scales with the channel partner's own growth

Score:
- 0: No distribution advantage
- 1: Building distribution; not meaningful
- 2: Real distribution advantage in vertical / region
- 3: Dominant distribution; embedded in larger platform; competitors must build from scratch

**Maximum: 24**

## 2. Moat-or-Wrapper Score Interpretation

| Score | Category | Implication |
|---|---|---|
| 0-8 | Wrapper | Reposition or repackage; valuation discount; expect investor pushback |
| 9-14 | Real but incomplete | Neutral valuation; identify 2-3 dimensions to deepen |
| 15-19 | Strong moat | Agent premium territory |
| 20-24 | Rare strong defensibility | Premium across multiple dimensions |

## 3. Wrapper-Risk Catalogue (the failure modes)

| Pattern | Description | Verdict |
|---|---|---|
| Pure prompt cleverness | Clever system prompt over GPT-4o/5 + retrieval | Wrapper |
| Public-tool only | Agent uses only public APIs (Stripe, Twilio, Sendgrid, Google) | Wrapper |
| Generic orchestration | Wraps LangChain / CrewAI / AutoGen with no proprietary layer | Wrapper |
| Foundation-model partnership | "We partner with OpenAI / Anthropic" | Wrapper (everyone has API access) |
| Demo without deployment | Impressive demos; no production customers | Unproven; flag as risk |
| Single-customer custom build | One-customer custom integration looks like a product | Services, not product |
| No eval-loop | Agent ships and never improves with customer data | Wrapper |
| Vertical positioning without vertical depth | "We're a vertical X agent" with no proprietary tools / data / integration / eval / regulatory | Wrapper with vertical paint |
| One-time fine-tune | Fine-tuned once; no ongoing data accrual | Not a moat (single-shot effort) |
| Open-source-model claim | "We use Llama / Mistral / Gemma" without engineering or data edge | Wrapper of open-source |
| Plug-in / extension | Lives inside another platform (ChatGPT plug-in, Salesforce app, Slack app) without independent defensibility | Platform-dependent; not standalone moat |
| Agent marketplace listing | Agent listed in AWS / Azure / GCP marketplace alone | Distribution channel, not moat |

## 4. Foundation-Model Commoditisation Analysis

Run this thought experiment explicitly:

> If OpenAI / Anthropic / Google ships an agent in our exact category with their model + their tools + their marketplace next quarter, what survives of our business?

For each "what survives" claim, document evidence:

| Survives because... | Evidence required |
|---|---|
| Customer data and configurations | Volume of accrued action data; customer count; retention |
| Proprietary tools and integrations | Tool registry inventory; integration depth audit |
| Regulator-accepted audit log | Regulator engagement record; audit acceptance |
| Vertical workflow embedding | Multi-system workflow with proprietary steps |
| Customer-trust / vertical reputation | Reference list; brand evidence; switching survey |
| Distribution channel | Partner contracts; embedded relationships |
| Local-language / sovereign-AI | Local data exclusivity; in-region hosting; sovereign accreditation |

If "what survives" is empty, the moat-or-wrapper score is dishonestly inflated.

## 5. Wardley-Map Placement for Agent Components

Place each component on the evolution axis (Genesis -> Custom -> Product -> Commodity):

| Component | Typical placement (2026) | Implication for moat |
|---|---|---|
| Foundation model (LLM) | Commodity / Product | Cannot be your moat |
| Embedding model | Commodity | Cannot be your moat |
| Vector DB / RAG layer | Product | Cannot be your moat |
| Orchestration framework (LangChain / CrewAI / AutoGen / LangGraph / Semantic Kernel) | Product moving to Commodity | Cannot be your moat |
| Generic observability (LangSmith / LangFuse / Helicone) | Product | Cannot be your moat |
| Generic eval framework | Custom moving to Product | Marginal moat |
| Proprietary tool registry | Custom | Real moat |
| Proprietary action-data flywheel | Genesis / Custom | Strong moat |
| Proprietary eval suite on customer data | Custom | Strong moat |
| Customer-specific integrations | Custom | Real moat (depth-dependent) |
| Domain / regulatory clearance | Custom | Strong moat |
| Local-language data + models | Genesis / Custom | Strong moat (in African / non-English markets) |

A moat in Commodity layers is not a moat. Your moat must live in Custom / Genesis layers with explicit "stay defensible" logic.

## 6. The Moat-or-Wrapper Thesis Paragraph

One paragraph an experienced operator would not call marketing language. Must answer:

- What is proprietary (tools, data, integration, eval, clearance, distribution)?
- What accrues (action data flywheel; customer switching cost)?
- What would survive a foundation-model commoditisation event?
- What is the customer-switching cost in concrete terms?

If you cannot write this paragraph without marketing language, the moat is not yet real.

## 7. Cross-References

- Risk register: `saas-agent-risk-and-stress-test` consumes the foundation-model commoditisation risk
- Valuation: `meta-agent-valuation-adjustments` consumes the moat-or-wrapper score
- Executive summary: `saas-agent-executive-summary-block.md` quotes the thesis paragraph
- Product strategy: `saas-agent-product-strategy-and-roadmap` informs the moat-deepening roadmap

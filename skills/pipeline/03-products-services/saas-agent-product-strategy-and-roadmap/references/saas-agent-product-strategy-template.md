---
source: Agent-products business-plan audit (2026); Wardley Mapping; engine synthesis
frameworks: [Autonomy ladder; Gates; Tool registry strategy; Build / buy / host; Roadmap by ARR; Model-router]
skill: saas-agent-product-strategy-and-roadmap
cross-reference: [saas-agent-moat-and-wrapper-risk, saas-agent-unit-economics-and-cogs, saas-agent-risk-and-stress-test, saas-agent-implementation-timeline]
---

# Agent Product Strategy Template

## 1. Autonomy Ladder Rungs

| Rung | Description | Human role | Class fit |
|---|---|---|---|
| Assist | Agent provides info | Human acts | A |
| Suggest | Agent proposes action | Human approves and acts | A / B |
| Supervise | Agent acts; human reviews each action | Human reviews + can reverse | B / C |
| Agentic | Agent acts within policy | Human reviews exceptionally; human-final on Class D | B / C / D |

## 2. Gates Between Rungs

To promote a customer job from rung N to rung N+1:

- Eval coverage on the action class >=95%
- Sample size in current rung >= threshold (typically 5,000-20,000 actions)
- Incident-free in current rung for >=90 days
- AI Safety Lead sign-off
- Customer notification / consent (Class C/D especially)
- Drill on the kill-switch and audit-log for the action class
- Reserve adequacy confirmed
- Regulator engagement if sectorally required

## 3. Tool Registry Strategy

| Tool category | Strategy |
|---|---|
| Customer system-of-record (CRM, ERP, core banking, EHR) | Proprietary integration; deep moat layer |
| Identity / SSO | Buy + integrate |
| Payment rails (Stripe, mobile-money APIs, M-Pesa, MoMo, Wave) | Buy + abstraction layer |
| Channel (WhatsApp BSP, SMS, USSD, IVR aggregator) | Buy + abstraction |
| Search / retrieval | Buy index + proprietary embeddings on customer corpus |
| KYC / KYB | Buy + multi-vendor abstraction |
| Mapping / geo | Buy |
| Document OCR | Buy + customise (proprietary post-processing) |
| Domain-specific (legal corpus, medical codes, agronomic data) | Build proprietary or license |
| Audit-log | Build proprietary (this is regulator-facing) |

## 4. Build / Buy / Host Decisions

| Capability | Build | Buy | Host |
|---|---|---|---|
| Orchestration framework | No (unless platform thesis) | LangGraph / CrewAI / Semantic Kernel / AutoGen | Cloud |
| Foundation models | No | OpenAI / Anthropic / Google / Mistral / Meta / Cohere | API |
| Specialist models | Maybe (fine-tune) | Hugging Face / Together / Fireworks / providers | API or self-host |
| Local-language models | Maybe (fine-tune) | Lelapa AI / Masakhane / Awarri | API or in-region GPU |
| Eval platform | Customise | LangSmith / LangFuse / Arize / W&B / Helicone | SaaS or self-host |
| Observability | Buy | LangSmith / LangFuse / Helicone / Datadog | SaaS |
| Vector DB | Buy | Pinecone / Weaviate / pgvector / Chroma / Qdrant | SaaS or self-host |
| HITL workbench | Build (mostly) | Some buy from Scale / Snorkel / Surge for labelling | Self-host |
| Tool registry | Build (proprietary moat) | n/a | Self-host |
| Audit-log store | Build | Append-only DB / cloud-managed | Self-host |
| In-region inference | Host | n/a | af-south-1 / Cassava / Liquid / Ethiopian AI Inst |

## 5. Roadmap by ARR Milestone

| Stage | Roadmap focus |
|---|---|
| Pre-PMF | One Class B agent; one customer job; supervised mode; eval suite v1 |
| Seed (USD 0.2-1M ARR) | One Class C agent; multiple customers; agentic in low-stake actions; eval suite v2 + drill cadence |
| Series A (USD 1-5M ARR) | Multiple Class C/D agents; vertical agent library v1; multi-channel; multi-language if relevant |
| Series B (USD 5-20M ARR) | Vertical library v2; platform plays if applicable; multi-country; sovereign-AI ready |
| Growth (USD 20M+ ARR) | Platform layer; tool registry licensed; agent marketplace; multi-vertical |

## 6. Model-Router Architecture

- Routing decision: query complexity x action class x cost target x latency target
- Models: 1 frontier (planner / critic on high-stake) + 1-2 cheap-router (worker on routine) + N specialist (vertical / local-language)
- Eval per model and per route
- Canary rollout on model changes
- Versioned eval suite
- Migration reserve

## 7. Eval-Driven Roadmap

Every roadmap item must have:
- Target eval coverage (offline + online)
- Sample-size requirement before promotion
- Target cost-per-resolved-task
- Target intervention rate
- Target task success rate
- Drill plan
- Kill-switch criteria
- Roll-back plan

## 8. Cost-Gated Launches

Every roadmap item has a target cost-per-resolved-task. The launch is held until:
- Target cost-per-resolved is held in shadow / staging
- 14-day stable under load
- Sensitivity to expected stress is acceptable
- Agent GM target achievable at expected pricing

## 9. Vertical Agent Library (if vertical thesis)

- Reusable planner / worker / critic templates per vertical
- Reusable tool adapters per vertical
- Reusable eval-sets per vertical
- Reusable HITL workbench per vertical
- Reusable audit-log schema per vertical
- Reusable regulator-engagement artefacts per vertical
- Reuse rate metric: % of new-customer deployment built from library

## 10. Customer Notification / Consent Practice

- Class A: no notification required
- Class B: notification on autonomy
- Class C: notification + opt-in
- Class D: notification + opt-in + signed consent with action-class explanation; human-final mandatory

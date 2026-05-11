---
source: Mersch ch. 11; Cotton MSPOT; 2024-2026 AI-investor board-pack practice
frameworks: [Quarterly AI board-pack section; AI strategic discussion; AI risk register summary; AI roadmap progress; AI compliance posture]
skill: meta-board-and-investor-reporting
cross-reference: [meta-board-and-investor-reporting, saas-ai-investor-update-block, saas-ai-risk-and-stress-test, meta-ai-bankability-and-investor-readiness]
---

# SaaS AI Board Pack Section

The AI section that should appear in every quarterly board pack for an AI-feature-led SaaS company. 3-5 pages typical. Read in parallel with the financial dashboard.

## 1. Section structure

### 1.1 AI KPI dashboard (1 page)

Quarterly versions of monthly KPIs plus quarterly-only metrics:

- AI-attributable ARR (quarter-end, QoQ trend, YoY trend)
- AI Gross Margin (quarter average, trajectory)
- AI Contribution Margin per tier
- AI-cost-as-%-of-ARR (quarter average, trajectory)
- Per-tenant AI cost (median + top decile by tier)
- Eval coverage (quarter-end + 90-day trend)
- Hallucination rate (production sampling — quarter average)
- Cache-hit ratio (quarter average)
- Model-mix share (quarter average)
- AI talent: hires this quarter / attrition / open roles
- AI vendor spend by provider (quarter total)
- AI incidents (count by severity; resolution time average)

### 1.2 AI strategic discussion (1-2 pages)

The 1-3 decisions the board is asked to weigh in on:

- Should we switch primary foundation-model provider given Q price + capability change?
- Should we approve the local-model self-hosting investment ($X capex; $Y opex)?
- Should we accept the proposed pricing change given AI-cost trajectory?
- Should we proceed with sovereign-AI tender bid given resource implications?
- Should we acquire/partner with [local-language AI specialist]?

For each: framing, options, recommended path, evidence, ask of board.

### 1.3 AI risk register update (0.5-1 page)

- Top 5 AI risks (likelihood × impact)
- Mitigation status update on each
- New risks added this quarter
- Risks downgraded / resolved
- Hallucination-liability reserve adequacy
- Foundation-model platform-risk status

### 1.4 AI roadmap progress (0.5-1 page)

- Roadmap items shipped this quarter (with eval evidence)
- Roadmap items in flight
- Slipped items + reason + recovery plan
- Cost-gate decisions made this quarter (features gated; features approved)
- AI feature adoption metrics (per-tier, per-feature)
- Customer-AI-success case studies (1-2 named)

### 1.5 AI compliance & governance update (0.5 page)

- Regulatory developments in operating jurisdictions
- Eval governance committee minutes summary (decisions made)
- AI policy version changes
- External audit / certification progress (ISO 42001, SOC 2 AI add-on)
- Customer data-residency posture changes

### 1.6 Forward look (0.25 page)

- AI KPI targets next quarter
- Roadmap targets next quarter
- Top AI risk to monitor
- Pricing experiment outcomes expected

## 2. Worked example — Q3 board pack section (dairy AI platform)

> **AI KPI dashboard (Q3):**
> AI-ARR $1.05M (Q3) vs $912k (Q2) +15% QoQ; AI-ARR $1.05M vs $580k Y/Y +81%. AI GM 72% (Q3 avg) vs 68% (Q2 avg) +4pp. AI Contribution Margin: Standard tier 78%, Pro tier 89% (both improved). AI-cost-%-of-ARR 9.8% (Q3 avg). Per-tenant cost: Standard median $6.40 / top-decile $17.20; Pro median $34 / top-decile $89. Eval coverage 63% (Q3 end) up from 58% (Q2 end). Hallucination 0.35% (Q3 avg). Cache-hit 49% (Q3 avg). Model-mix: 67% cheap / 28% premium / 5% local (self-hosted Mistral). AI hires: 2 in Q3 (1 ML engineer, 1 eval lead); 0 attrition; 3 open roles. AI vendor spend Q3: $42k (Anthropic $18k, OpenAI $11k, Cohere $9k, Pinecone $2k, Langfuse $2k). Incidents: 1 sev-2 (cache poisoning by malformed input; resolved 4h); 0 sev-1.
>
> **Strategic decisions for board:**
> 1. **Approve $180k local Mistral self-hosting capex on Liquid Cape Town infra**: expected payback 8 months; reduces FX exposure on routine-query cost by 65%; mitigates Cohere migration risk. Board ask: approve capex + 6-month KPI checkpoint.
> 2. **Approve bid on KE Ministry of Agriculture extension-officer AI tender** ($800k ACV; 2-year term): would represent 15% of projected ARR; requires KE in-country deployment ($120k one-time); 3-month bid timeline. Board ask: approve bid + resource allocation.
>
> **AI risk register update:**
> Top 5 risks: (1) Cohere Command R+ deprecation (mitigation in progress; migration on track); (2) UGX FX volatility (+5% headroom in pricing; quarterly review); (3) NITA-U emerging AI guidelines (compliance roadmap drafted; legal review November); (4) AI talent retention vs international remote competitors (Q4 retention plan submitted); (5) Hallucination-liability in milk-payment-summarisation flow (mitigation: human-in-loop for all payment-impacting summaries). Reserve $35k (4% of AI ARR) — adequate per current methodology. Platform risk: Anthropic / OpenAI vertical-extension watch — no direct dairy/coop AI release Q3.
>
> **AI roadmap (Q3):**
> Shipped: Luganda voice-note transcription (eval 0.78 → 0.85 over Q3); anomaly-detection v2 (Claude → GPT-4o-mini migration; -$1,800/month cost). In flight: extension-officer summarisation v2 (delayed 4 weeks; eval gap on long-prompt flow). Cost-gated this quarter: 2 features approved (Luganda voice-note, anomaly v2); 1 feature deferred (predictive milk-yield model — eval not ready). Adoption: Standard tier Luganda chatbot 76% MAU; Pro tier anomaly 84% MAU. Customer case study: Nyabushozi Cooperative — 22% reduction in payment-dispute volume attributed to Luganda chatbot.
>
> **AI compliance & governance:**
> NITA-U AI guidelines draft published Oct; legal review in progress; gap to compliance estimated <60 days. EU AI Act not applicable (no EU customers). AI policy v1.2 approved (added incident response detail). AI committee met 3 times in Q3; key decisions: (a) approved Mistral self-hosting (subject to board); (b) approved customer data-residency tier for Pro+ ; (c) approved redress process for AI-decision challenges. ISO 42001 readiness audit scheduled Q1 next year.
>
> **Forward look (Q4):**
> AI-ARR target $1.3M. Eval coverage target 70%. Cache-hit target 55%. Roadmap: Mistral deployment; extension-officer summarisation v2; KE tender (if approved); SOC 2 Type II readiness. Top AI risk to watch: KE tender outcome + budget allocation if won. Pricing experiment outcome expected Q4 mid: Standard tier allowance 200 → 150 queries.

## 3. Anti-patterns

- Same KPIs every quarter (no quarter-only metrics)
- Strategic discussion with no decision-asks (board as audience, not forum)
- Risk register all-stable (no honest movement)
- Roadmap all-shipped, no slips (suspect)
- Compliance posture "we comply" (vague)
- Forward look absent or generic

## 4. Living-plan link

Quarterly board pack section assembled 5 days before board meeting. Drafted by CEO + CFO + Head of AI. Reviewed by AI committee chair. Cross-references the monthly investor updates ([Month 7 / 8 / 9] data feeds the Q3 view).

## 5. Africa context

- DFI-on-board: include impact KPIs (gender-disaggregated reach, local-language coverage, public-sector accessibility)
- Sovereign-AI tender posture relevant to many African board packs
- FX impact on AI economics explicitly explained
- Local data residency compliance posture against the operating country's data protection law
- Local talent pipeline metrics (AIMS / CMU Africa / ALU partnerships; Deep Learning Indaba engagement)

---
name: saas-agent-moat-and-wrapper-risk
description: Test agent-product moat claims with an 8-question rubric (proprietary tools, proprietary action data, integration depth, eval-loop, customer-trust, regulatory clearance, switching-cost, distribution) against the dominant agent failure mode — wrapper risk from the foundation model provider. Produces a defensibility-vs-wrapper score and a moat-or-wrapper thesis paragraph. Use whenever a SaaS plan claims an agent product is competitively defensible.
---

# SaaS Agent Moat & Wrapper Risk Skill

## Overview

In 2025-2026, **most "agent companies" are GPT wrappers in trench coats**. The single most consequential question an agent-fund investor asks is: *"If OpenAI / Anthropic / Google ships this capability directly next quarter, what's left of your business?"* If the answer is "we'd be in trouble", the company is a wrapper and the valuation collapses to a fraction of the headline ARR multiple. If the answer is "we'd still win because of X, Y, Z" with evidence, the company is a defensible agent business and earns the agent premium.

This skill installs the moat-vs-wrapper discipline. Builds on `saas-ai-moat-and-defensibility` (which runs the 7-question AI moat test) and adds the agent-specific dimensions and the **wrapper-risk-from-foundation-provider** vector as its own first-class test.

## Use When

- A SaaS plan claims an agent or multi-agent product is defensible
- Section 06 is being built for an agent-product plan
- A foundation-model provider has shipped a capability that overlaps the agent business
- An investor's technical diligence on agent defensibility is upcoming
- A founder is choosing between agent positioning ("we're an agent platform") and vertical positioning ("we're a vertical X agent")
- The plan asks for an agent valuation premium that implicitly assumes moat
- The plan must pass `meta-agent-bankability-and-investor-readiness`

## Do Not Use When

- The product is an AI feature inside SaaS without agentic action — use `saas-ai-moat-and-defensibility`
- The agent is internal-efficiency only with no customer-facing defensibility to test
- The plan is pre-PMF — moat claims are forward-looking, but discipline still applies; flag claims as "in development"

## Required Inputs

- Agent architecture (planner / worker / critic; tool registry; data flows)
- Tool inventory — which tools are proprietary, which are third-party, which are commoditisable
- Action-data inventory — what action data accrues per customer (prompts, completions, tool invocations, outcomes, interventions, human-correction signals)
- Integration depth per customer — system-of-record integration, identity integration, audit-log integration, billing integration
- Eval-loop maturity — offline + online evals; production sampling; human-correction loops; eval-set proprietary or public
- Customer-trust evidence — references, regulatory clearance, audit acceptance, public-sector references
- Switching-cost evidence — data migration friction, integration switching, retraining cost, contractual lock-in
- Distribution channels — direct, partner, marketplace, embedded
- Foundation-model provider trajectory — is OpenAI / Anthropic / Google shipping in your category? GA / preview / rumoured?
- Competitor moat claims

## Workflow

1. **List the moat claims** in the plan — every place the agent is presented as competitive differentiation.
2. **Run the 8-question agent moat test** per `references/saas-agent-moats-and-wrapper-risk-checklist.md`:
   - Q1 — **Proprietary tools** — are the tools the agent uses proprietary (your APIs, your integrations, your data sources) or commoditisable?
   - Q2 — **Proprietary action data** — does each customer interaction generate action data that improves the agent uniquely for you?
   - Q3 — **Integration depth** — how deeply embedded is the agent in customer system-of-record, identity, audit, billing?
   - Q4 — **Eval-loop** — do you have a real eval suite running in production with human-correction signals improving the agent over time?
   - Q5 — **Customer-trust / brand** — are you the trusted agent vendor in this vertical / region?
   - Q6 — **Regulatory clearance** — do you have explicit regulator engagement, audit acceptance, sectoral approval that competitors lack?
   - Q7 — **Switching-cost** — data, integration, training that locks customer in (or, conversely, contractual lock-in alone — weak)?
   - Q8 — **Distribution** — channel, partnership, embedded-in-larger-platform reach that competitors cannot match?
3. **Score 0-3 per dimension; max 24.** Scoring guide in checklist.
4. **Apply the wrapper-risk detector** per `references/agent-moats-vs-wrapper-risk.md`:
   - **Pure prompt cleverness** — clever system prompt over GPT-4o/5 with no tools / data / integration / eval moat = wrapper
   - **Public-tool only** — agent uses only public APIs and public data = wrapper
   - **Generic orchestration** — wraps LangChain / CrewAI / AutoGen with no proprietary layer = wrapper
   - **Foundation-model partnership claim** — "we partner with OpenAI / Anthropic" = wrapper (everyone has API access)
   - **Demo without deployment** — agent runs in demos but no production customers = unproven; flag as risk
   - **Single-customer custom build** — looks like a services business, not an agent product = services, not product
   - **No eval-loop** — agent ships and never improves with customer data = wrapper
5. **Foundation-model platform risk** — explicitly map: *if OpenAI / Anthropic / Google / Meta / Amazon ship in our category next quarter, what survives?* For each surviving piece, document why.
6. **Wardley-map the agent components** — place planner / workers / critic / tools / eval-loop / observability / action-data on Genesis -> Custom -> Product -> Commodity. Components in Commodity cannot be your moat. Your moat must be in Custom / Product layers with explicit "stay defensible" logic.
7. **Compute the moat-vs-wrapper score** — 0-24 from the rubric:
   - 0-8: wrapper; valuation discount applies; recommend repositioning or repackaging
   - 9-14: real but incomplete moat; valuation neutral; needs deliberate deepening
   - 15-19: strong moat; agent premium territory
   - 20-24: rare; strong defensibility across multiple dimensions
8. **Write the moat-or-wrapper thesis paragraph** — one paragraph an experienced operator would not call marketing language. Must answer: what is proprietary, what accrues, what would survive a foundation-model commoditisation event, what is the customer-switching cost.
9. **Wire to valuation** (`meta-agent-valuation-adjustments`), to risk (`saas-agent-risk-and-stress-test`), and to executive summary (`saas-agent-executive-summary-block.md`).

## Quality Bar

- Every agent-moat claim tested through the 8-question rubric
- Wrapper-risk detector applied; weak claims explicitly downgraded or retracted
- Foundation-model platform risk **explicitly named** with surviving-pieces inventory
- Wardley-map placement done for each agent component
- Moat-or-wrapper score computed; not gamed
- Thesis paragraph free of marketing language; evidence-based
- Cross-referenced to valuation, risk register, executive summary
- A sceptical agent-fund investor would not call the moat thesis "promotional"

## Anti-Patterns

- "We're not a wrapper because we're vertical" — vertical alone is not a moat unless paired with proprietary tools / data / integration / eval / regulatory
- "We have a proprietary system prompt" — system prompts are not defensible (extractable, replicable)
- "We use a fine-tuned model" — one-time fine-tune without ongoing data accrual is not a moat
- "We partner with OpenAI / Anthropic" — API access is not a moat
- "LangChain / CrewAI / AutoGen is our framework" — wrapping commoditised orchestration is not a moat
- Mentioning eval without showing an eval suite + scores + improvement trajectory
- Skipping the foundation-model commoditisation question
- Wardley-mapping with all components in Custom (handwaving the actually-commoditised pieces)
- "Switching cost is high because customers signed annual contracts" — contractual lock-in alone is weak

## Outputs

- Moat-claim inventory
- 8-question rubric score (0-24)
- Wrapper-risk detection list (claims rejected or downgraded)
- Foundation-model commoditisation analysis (what survives if provider ships)
- Wardley-map placement of agent components
- Moat-or-wrapper score and thesis paragraph
- Cross-reference to valuation premium / wrapper discount

## Living-Plan Cadence Defaults

| Element | Cadence | Owner | Variance threshold |
|---|---|---|---|
| Foundation-model commoditisation watch | monthly | Head of AI / CTO | provider ships competing capability |
| Competitor agent claim scan | monthly | Head of Strategy | new entrant with similar claim |
| Action-data accrual evidence | monthly | Head of Product | accrual rate <plan |
| Eval-loop trajectory | monthly | Eval Engineer | eval improvement stalled 60 days |
| Tool-registry proprietary share | quarterly | Tool Engineer | proprietary share falling |
| Integration depth per customer | quarterly | Head of CS | shallow integrations on >30% customers |
| Moat-vs-wrapper score reassessment | quarterly | CEO + Head of Strategy | -3 points |
| Wardley-map refresh | annual | Head of Strategy | structural shift |
| Regulatory clearance maintenance | quarterly | Compliance + Legal | clearance lapse risk |

## References

- `references/saas-agent-moats-and-wrapper-risk-checklist.md` — 8-question rubric + wrapper-risk catalogue + Wardley placement
- `references/agent-moats-vs-wrapper-risk.md` — compact rubric (lives at `06-competitive-analysis/references/`)
- `skills/06-competitive-analysis/saas-ai-moat-and-defensibility/SKILL.md` — AI moat parent
- `skills/06-competitive-analysis/SKILL.md` — generic competitive analysis
- `skills/meta-agent-valuation-adjustments/SKILL.md` — consumes the moat score
- `book-extractions/walling-saas-playbook-extraction.md` — moat discipline
- `book-extractions/agent-products-business-plan-audit-2026.md` — agent audit

## Africa / Uganda Application Notes

- **Local-language agent moat** is genuinely available in African markets — agents that work in Swahili, Hausa, Yoruba, Amharic, Igbo, Zulu, Luganda, Lingala, Wolof, Tigrinya at production quality are scarce and defensible. Pair with local TTS / STT (voice-IVR / WhatsApp-voice).
- **Sovereign-AI / data-residency moat** — agents that can demonstrably run on in-country compute with in-country data are procurement-favoured in KE, NG, ZA, RW, EG, UG public-sector and regulated sectors.
- **Integration depth in African workflows** — mobile-money rails (M-Pesa, MoMo, Airtel Money, Wave, Orange Money), USSD aggregators, WhatsApp Business API channel, identity systems (NIN / Huduma / Hudumba / Aadhaar-equivalents) are real integration moats; OpenAI / Anthropic / Google direct-ship cannot replicate the integration layer quickly.
- **Regulatory clearance moat** in African sectors — KE CMA fintech sandbox, KE ODPC, NG SEC / CBN / NITDA / NDPC, ZA FSCA / Information Regulator, RW BNR / NCSA, UG BoU / NITA-U / PDPO — agent vendors with explicit engagement and accepted-audit-log status have a real moat against foreign agents.
- **Customer-trust moat** — public-sector and regulated-sector procurement in Africa often disqualifies foreign agent vendors; local accountability matters disproportionately.
- **Distribution moat in African verticals** — 50 deployed SACCOs, 200 deployed clinics, 30 deployed schools, 5 deployed government agencies are real moats that foreign agents cannot replicate quickly.
- **Wrapper risk in Africa** — many "AI agent" startups in 2025-2026 are pure wrappers; the moat-vs-wrapper rubric must be applied strictly to avoid funding-stage embarrassment when DFI / IFC / AfDB technical diligence runs.

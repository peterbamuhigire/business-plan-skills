---
source: Agent-products business-plan audit (2026); Cotton TAM discipline; engine synthesis
frameworks: [Agent TAM unit; Actions-served vs queries-served; Vertical agent TAM; Sovereign-AI agent TAM]
skill: 04-market-analysis
cross-reference: [saas-ai-market-and-tam, saas-agent-product-strategy-and-roadmap, saas-agent-pricing-strategy]
---

# Agent TAM Discipline — Reference

## 1. The Unit Problem

Generic AI TAM uses **queries** (or model calls) as the unit. Agent TAM must use **actions** or **outcomes** as the unit:

- One user request -> 1 LLM query (AI-feature TAM)
- One user request -> 1 resolved task = N steps + M tool calls (agent TAM)

If you size your agent market in LLM queries, you overstate the addressable revenue (because one resolved task replaces many queries and many human minutes) and understate the value-capture (because the willingness-to-pay is per-resolved-task, not per-query).

The correct unit:
- For CX agents: resolved tickets / month / customer
- For ops agents: completed tasks / month / customer
- For multi-agent orchestrated: outcomes / month / customer
- For vertical agents: domain-specific outcomes (cases, claims, codes, recoveries)
- For agent platforms: active agents / steps / tool invocations

## 2. TAM Layers

For each segment:

- **Activity volume** — how many of the unit (resolved tasks, outcomes) happen per period in the segment, today
- **Addressable-by-agent fraction** — what % of that volume is realistically agent-addressable in the 3-5 year horizon? (rarely 100%; typically 20-60% depending on action class and irreversibility)
- **Capture-per-unit** — your price per resolved task / outcome / step
- **Addressable revenue** — activity x addressable-by-agent fraction x capture-per-unit

## 3. Honest Attribution

Avoid:
- Double-counting LLM TAM as agent TAM
- Assuming 100% agent capture in a segment
- Using "AI TAM" projections that don't break down to actions
- Ignoring irreversibility ceiling (Class D actions take longer to mature)

Discipline:
- Bottom-up build from segment activity volumes
- Top-down sanity check against macro AI / SaaS / vertical reports
- Discount Class C / D shares more heavily (longer adoption curve)

## 4. Vertical Agent TAM

Build TAM by vertical:

- **CX / customer service** — tickets resolved / agent / month x agents in market x % agent-addressable x price
- **Collections / fintech** — accounts in arrears x % recoverable x agent-addressable share x recovery commission
- **Healthtech triage** — patient touchpoints x triage-addressable share x value per triage
- **Edutech tutoring** — students x sessions / month x agent-addressable share x value per session
- **Legal-aid** — consultations or document-events x agent-addressable share x value per outcome
- **Agri-extension** — farmers x advisory touchpoints x value per touchpoint
- **Public-sector citizen-service** — service interactions x agent-addressable share x government-procurement budget per interaction
- **Back-office / ops** — task volumes (invoices, reconciliations, KYC, claims) x automatable share x value per task

## 5. Sovereign-AI Agent TAM

A distinct TAM layer for African (and other emerging) markets:
- Public-sector procurement budgets for citizen-service automation
- Regulated-sector procurement requiring residency / local accountability
- Sovereign-AI envelopes (RW innovation; KE Talanta; NG NITDA implementation; ZA Presidential 4IR; EG infrastructure)

This is typically a separate go-to-market from commercial; do not blend the TAMs.

## 6. Conservative vs Aggressive TAM

State both with assumption deltas:

- **Aggressive** — addressable-by-agent 50%+; Class D adoption within 3 years; sovereign-AI captures 30% of regulated segment
- **Conservative** — addressable-by-agent 20-30%; Class D adoption 5-7 years; sovereign-AI captures 10-15%

Investors will discount aggressive; show your reasoning for the conservative case.

## 7. TAM by Geography

For African plans:
- Lead country (where you start)
- Adjacent country (typically 2-3 years out)
- Pan-Africa addressable
- Global addressable (only relevant if platform play)

## 8. Anti-Patterns

- Quoting "AI TAM USD 1.3 trillion" without breaking down to your action unit
- Assuming 100% agent capture
- Mixing commercial and sovereign-AI TAMs
- Using global TAM when you serve 1-2 countries
- TAM growth assumed at hype-cycle rates
- No conservative scenario
- Class D activity sized as if Class A adoption rates apply

## 9. Cross-References

- AI TAM parent: `saas-ai-market-and-tam`
- Product strategy: `saas-agent-product-strategy-and-roadmap` (autonomy ladder informs addressable %)
- Pricing: `saas-agent-pricing-strategy` (capture per unit)
- Africa context: `africa-agent-context-extension.md`

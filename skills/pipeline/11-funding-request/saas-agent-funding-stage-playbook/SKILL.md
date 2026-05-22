---
name: saas-agent-funding-stage-playbook
description: Agent-business funding playbook across pre-seed, seed, A, B, and growth. Investor archetypes for agents (agent-specialist funds, vertical AI funds, generalist SaaS, sovereign-AI envelopes, DFI). Use-of-proceeds patterns specific to agents (heavy on Tool / Eval / Safety vs heavy on GTM in normal SaaS). Milestone breakpoints (first supervised production; first autonomous production; first cost-per-resolved under target; first audit clearance).
---

# SaaS Agent Funding Stage Playbook Skill

## Overview

AI funding (handled by `saas-ai-funding-stage-playbook`) maps AI startups to AI-VC / sovereign-AI / DFI envelopes. **Agent funding** has its own investor archetypes (agent-specialist funds, vertical AI funds) and its own use-of-proceeds shape (heavier on Tool / Eval / Safety than on GTM). Milestones are agent-specific.

## Use When

- Section 11 is being built for an agent-product plan
- A round is being planned (pre-seed -> growth)
- Investor-targeting list is being assembled
- Use-of-proceeds is being argued
- Milestone breakpoints for the next round are being declared

## Do Not Use When

- The product is AI-feature only without agentic action — use `saas-ai-funding-stage-playbook`
- A grant-only path is the funding strategy — use `11b-grant-proposal` instead
- The plan is too early (pre-PMF, pre-customer) — focus on building first customers before funding-stage discipline

## Required Inputs

- Current stage and ARR
- Cost-per-resolved-task trajectory
- Moat-vs-wrapper score
- Bankability score
- Customer mix (regulated / public / SMB / enterprise)
- Geographic footprint

## Workflow

1. **Match stage to investor archetype** per `references/saas-agent-funding-stage-playbook.md`:
   - **Pre-seed (USD 250k-1.5M)** — angels, agent-specialist seed funds, accelerator (YC / Techstars / Founder Institute / MEST / Antler / Future Africa / 500 / Norrsken / Catalyst Fund), DFI early-stage envelopes
   - **Seed (USD 1.5-5M)** — agent-specialist seed funds, AI-specialist seed (a16z AI, Bessemer AI), African / EM seed (TLcom, Norrsken22, Partech Africa, Ventures Platform, Future Africa, Equator, Knife, 4Di), DFI seed envelopes
   - **Series A (USD 5-20M)** — agent-specialist A funds, vertical AI funds, generalist SaaS funds with AI thesis, sovereign-AI strategic, DFI A envelopes
   - **Series B (USD 20-60M)** — agent-specialist growth, vertical AI growth, generalist growth, sovereign-AI strategic at scale, DFI patient capital
   - **Growth (USD 60M+)** — generalist growth + strategic + sovereign at scale; potential pre-IPO; cross-border listings (JSE / NSE / NGX / EGX)

2. **Specify use of proceeds** for agents specifically:
   - **Tool Engineering** (proprietary tools / integrations) — typically 25-40% of seed / A
   - **Eval infrastructure** — typically 10-20%
   - **AI Safety + governance + regulator engagement** — typically 10-15%
   - **Agent Architect + senior engineering** — typically 15-25%
   - **HITL Designer + operations** — typically 5-10%
   - **GTM** (lower than normal SaaS at early stages because product-led + vertical-anchored) — typically 15-25% at seed/A; rises at B
   - **Forward Deployed Engineering** if vertical thesis — 5-15%
   - **Reserve (irreversibility / migration / regulator)** — 5-10%
   - **Compute / infra (LLM + tools + in-region GPU)** — typically 8-15%

3. **Set milestone breakpoints** per stage:
   - **Pre-seed -> seed:** first Class B agent live in production with 5+ customers; eval suite v1; cost-per-resolved-task baselined; AI Safety Lead engaged (fractional acceptable)
   - **Seed -> A:** first Class C agent live in supervised mode; eval coverage >85%; cost-per-resolved under target; 20+ customers; agent GM >50%; AI Safety Lead full-time
   - **A -> B:** first Class D agent live with human-final; eval coverage >95% on Class C/D; cost-per-resolved-task well under competitive anchor; agent GM >60%; 100+ customers or regulated / public-sector anchors; first audit clearance
   - **B -> Growth:** multi-country deployment; multi-vertical or platform play; agent GM >70%; sovereign-AI procurement won; regulator-accepted audit-log in production
   - **Growth -> exit:** category-defining vertical or platform position; multiple sovereign-AI tenders; strategic-acquisition value or IPO path

4. **Diligence preparation** — the bankability scorecard (`meta-agent-bankability-and-investor-readiness`) and data room (`meta-due-diligence` agent contents) prepared 60-90 days before round opens

5. **Investor narrative discipline:**
   - Open with the agent thesis (one paragraph; archetype declared)
   - Cost-per-resolved-task as headline economic metric
   - Moat-or-wrapper thesis paragraph
   - Autonomy ladder progress with gates
   - Regulator-engagement evidence
   - AI Safety Lead in seat
   - Stress-tested

## Quality Bar

- Stage-to-investor match explicit
- Use of proceeds reasoned (% by line)
- Milestone breakpoints for next round declared
- Diligence preparation in train
- Investor narrative draft
- Cross-reference to bankability and valuation

## Anti-Patterns

- "AI fund" with no distinction between AI-feature and agent funds
- Use of proceeds same as normal SaaS (too heavy on GTM, too light on Tool / Eval / Safety)
- Milestones in MRR / ARR only without agent-specific (cost-per-resolved, intervention rate, autonomy ladder, regulator)
- Round opens before bankability evidence assembled
- No AI Safety Lead at A or later
- Pricing in local currency to USD investors

## Outputs

- Investor target list with archetype labels
- Use-of-proceeds breakdown
- Milestone breakpoints for current and next round
- Investor narrative draft
- Cross-reference to bankability + data room
- Stress on funding ask under tail risks

## Living-Plan Cadence Defaults

| Element | Cadence | Owner |
|---|---|---|
| Investor target list refresh | quarterly | CEO + Head of Strategy |
| Milestone progress | monthly | CEO + CFO |
| Bankability rescore | quarterly | (per bankability skill) |
| Use-of-proceeds variance | monthly | CFO |
| Round opens | per-round | CEO + Board |

## References

- `references/saas-agent-funding-stage-playbook.md` — stage-by-stage detail; investor archetypes; use-of-proceeds patterns
- `skills/11-funding-request/saas-ai-funding-stage-playbook/SKILL.md` — AI parent
- `skills/meta-agent-bankability-and-investor-readiness/SKILL.md` — bankability gate
- `skills/meta-agent-valuation-adjustments/SKILL.md` — valuation
- `skills/meta-due-diligence/SKILL.md` — DD
- `book-extractions/agent-products-business-plan-audit-2026.md` — audit

## Africa / Uganda Application Notes

- **African agent-fund landscape in 2025-2026** — agent-specialist funds rare; institutional agent investment typically via SF / EU co-investors with African lead (TLcom, Norrsken22, Partech, Ventures Platform, 4Di, Knife, Future Africa, Equator, Catalyst Fund, Renew, Ingressive)
- **DFI / multilateral envelopes** — IFC, AfDB, FMO, BII, Proparco, FCDO, USAID DIV, IDRC, GIZ — increasingly carve out AI / agent allocations
- **Sovereign-AI envelopes** — RW innovation envelope, KE Talanta AI, NG NITDA implementation, ZA Presidential 4IR, EG infrastructure — supportive but slow; use as supplementary not primary
- **Patient capital available** through DFIs; lowers required multiple but slower DD
- **Pricing** — institutional rounds in USD; DFI / strategic in local-currency-equivalent
- **Diligence reality** — DFI DD is rigorous (audit-log, jobs-impact, governance, environmental & social) and takes 6-9 months; build buffer
- **Regulatory clearance evidence** — strongly DD-valued for African plans
- **Co-investment patterns** — typically lead + 2-4 co-investors; sometimes DFI-anchored
- **Currency hedging** — institutional rounds often require USD-equivalent runway projections

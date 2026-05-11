---
source: Agent-products business-plan audit (2026); 2024-2026 agent-VC and enterprise procurement practice; Kennedy/Marrs pricing discipline; engine synthesis
frameworks: [Agent pricing primitives; Intervention credit; SLA-tied price; Vendor-cost pass-through; Price corridor; Stress matrix]
skill: saas-agent-pricing-strategy
cross-reference: [saas-agent-unit-economics-and-cogs, saas-agent-moat-and-wrapper-risk, meta-agent-valuation-adjustments, meta-pricing-strategy]
---

# Agent Pricing Architecture — Reference

The canonical pricing primitives, decision rubric, intervention-credit and SLA design, vendor-cost pass-through clause, and price-corridor analysis for agent products in this engine.

## 1. The Five Primitives

### Per-resolution
Customer pays per **resolved** task. Resolved = completed by the agent without HITL takeover (or with HITL within agreed limits).
- **Best fit:** CX agents, collections agents, claim-triage agents, ticket-resolution agents, agri-extension queries
- **Pros:** Strongest incentive alignment; customer pays for value; predictable margin if cost-floor known
- **Cons:** Revenue volatility tied to agent quality; requires rigorous "resolved" definition; intervention-credit policy mandatory

### Per-outcome
Customer pays per **outcome event** (recovered payment, signed contract, scheduled appointment, completed compliance check). Distinct from per-resolution in that the outcome includes downstream business effect, not just agent action.
- **Best fit:** collections, scheduling, sales-development agents, compliance agents, vertical agentic SaaS
- **Pros:** Outcome alignment is the strongest value-capture; pricing power is highest
- **Cons:** Outcome definition is legally and operationally complex; attribution disputes likely; longer sales cycles

### Per-step
Customer pays per **agent step** (LLM step, tool invocation, branch). Used in agent-platform / infrastructure businesses where you sell to other agent builders.
- **Best fit:** agent platform, tool registry, orchestration framework, eval-loop platform
- **Pros:** Tracks usage closely; simple to meter
- **Cons:** Step-counting can grow unpopular; customers optimise step usage in ways that hurt revenue; commoditisable

### Per-agent / per-seat
Customer pays per **deployed agent** or per **user with agent access**. Most familiar to SaaS buyers.
- **Best fit:** agent-as-internal-employee positioning; sales / SDR agents; analyst agents where the user binds to the agent
- **Pros:** Predictable revenue; familiar to procurement
- **Cons:** Decouples price from value; weak margin if cost varies; investors discount as "renamed SaaS"

### Hybrid
Combinations: platform fee + per-resolution overage; tier with included resolutions + per-resolution overage; per-agent + per-step variable.
- **Best fit:** mid-market and enterprise where procurement wants a predictable base and finance wants usage variability
- **Pros:** Balances predictability + alignment
- **Cons:** Complex to design; complex to invoice; commission complexity for the sales team

## 2. Decision Rubric — Choosing the Primitive

Answer in order:

1. **Is the agent's value measurable per discrete outcome?** (e.g. "resolved ticket", "scheduled appointment", "collected payment", "completed coding")
   - Yes -> per-resolution or per-outcome
   - No -> per-agent or per-step

2. **Is the customer's current cost-replacement anchor per-task or per-seat?**
   - Per-task (e.g. they currently pay a BPO USD 1.50 / ticket) -> per-resolution / per-outcome
   - Per-seat (e.g. they pay an analyst's salary) -> per-agent

3. **Is the agent platform sold to other agent builders?**
   - Yes -> per-step (with per-tool overlay) and / or per-agent
   - No -> stay with above

4. **Does procurement need predictability?**
   - Yes (enterprise / public sector) -> hybrid with capped variable
   - No (SMB) -> primitive can be pure

5. **What is the irreversibility class?**
   - High (financial, medical, legal) -> per-outcome with strict definition and explicit human-final clause; never per-step (signals commoditisation)
   - Low (information, recommendation) -> per-resolution viable; per-step viable for platform play

## 3. Intervention-Credit Design

When HITL or human-final takes over, what does the customer pay?

| Design | Customer pays | Vendor revenue | Vendor incentive | Customer fairness | Operational complexity |
|---|---|---|---|---|---|
| Full credit | 0% on HITL takeover | volatile | maximise true autonomy | high | low (easy to communicate) |
| Partial credit (30-50%) | 30-50% on HITL | moderate | balance autonomy + revenue | moderate | low |
| No credit, intervention budget cap | 100%; bounded total | high | maximise attempts within cap | moderate (cap protects) | moderate |
| Tiered by reason | model-failure -> credit; customer-ambiguity -> no credit | balanced | improve only what you control | high | high (root-cause tagging required) |
| No intervention concept | 100% always | high | none | low | low (and angry customers) |

**Recommended default for agent businesses targeting bankability:** partial credit (30-50%) or tiered-by-reason. Full credit creates revenue volatility that scares investors and DFIs.

## 4. SLA-Tied Pricing

Standard SLA tiers and credit schedule:

| SLA | Metric | Typical bar | Credit on breach |
|---|---|---|---|
| Response time | Time from request to agent first action | <5s p95 (chat) / <60s p95 (back-office) | 5% of period fee per breach class |
| Resolution time | Time from request to resolved | <2 min p95 (CX) / <24 h p95 (back-office) | 10% per breach class |
| Quality bar | % outputs passing eval (deterministic + LLM-judge) | >=92-97% depending on stake | 10-20% per breach class |
| Escalation timeliness | HITL handover before SLA threshold | 100% in irreversibility class | 25% per breach |
| Audit-log completeness | Audit-log retention and queryability | 100% on demand | 25% per breach (regulator exposure) |
| Kill-switch availability | Customer can pause agent within <60s | 99.99% | 25% per breach |

Cap monthly credits at 30-50% of period fee to bound vendor downside.

## 5. Vendor-Cost Pass-Through Clause (template)

For contracts >12 months, include language equivalent to:

> If, during the Term, Vendor's blended provider cost (LLM token cost + tool invocation cost) for the Customer's workload rises more than 25% on a trailing-90-day basis versus the baseline computed at contract execution, Vendor may, on 60 days' written notice, adjust the per-resolution / per-outcome / per-step price by up to the percentage cost increase above 25%. Customer's right of remedy: re-negotiation in good faith; failing agreement within 30 days, either party may terminate without penalty.

This clause is acceptable to most enterprise procurement, IFC-style DFI procurement, and African public-sector procurement when paired with: cost transparency (provider invoices on request), reasonable notice, and a customer termination right. Without it, the first provider price spike kills the contract margin.

## 6. The Price Corridor

For each candidate price point, plot:

1. **Min-margin price** = cost-per-resolved-task / (1 - target_gm)
   Example: USD 0.19 cost-per-resolved at 65% GM target -> min price = USD 0.19 / 0.35 = USD 0.54
2. **Competitive-anchor price** = the alternative the customer would pay (human FTE rate per task; competing software per task; do-nothing cost)
3. **Value-ceiling price** = customer's willingness-to-pay maximum (typically a fraction of the alternative)

**Viable corridor:** above min-margin AND above competitive-anchor AND below value-ceiling.

**Chosen price:** typically 60-75% of value-ceiling for premium positioning; 40-55% of value-ceiling for penetration positioning. Never below competitive-anchor unless your moat thesis requires it (and your investors agree).

## 7. Worked Example — Vertical Collections Agent (East Africa)

From the unit-economics worked example (cost per resolved case USD 0.19):

| Element | Value | Notes |
|---|---|---|
| Cost per resolved case | USD 0.19 | from agent UE |
| Target agent GM | 65% | viable for bankability |
| Min-margin price | USD 0.54 | 0.19 / 0.35 |
| Competitive anchor (human collections agent FTE per recovered case) | USD 2.50-4.00 | based on local FTE math |
| Value ceiling | USD 5.00 per recovered case | client typically gets 5-12% commission on UGX 200k+ recovery |
| Chosen price | USD 1.20 per resolved case | 24% of value ceiling -> penetration play with strong margin |
| Result agent GM at chosen price | 84% | well above target |
| Intervention credit | 40% on HITL takeover | partial credit |
| SLA: quality bar | >=94% | 10% credit per breach class |
| SLA: kill-switch | 99.99% | 25% credit per breach |
| Vendor-cost pass-through | applies | 25% provider-cost threshold |
| FX corridor | priced USD; UGX equivalent floats | UGX 3,500-3,900 / USD acceptable |

## 8. Stress Matrix on Pricing

| Stress | Cost-per-resolved | Effective price (after credits) | Agent GM | Action |
|---|---|---|---|---|
| Provider 2x | USD 0.30 | USD 1.20 | 75% | Hold price; cost-engineer; activate pass-through after 3-month sustained |
| Provider 5x | USD 0.70 | USD 1.20 | 42% | Activate pass-through; raise price; provider switch |
| Intervention rate 2x (12% -> 24%) | USD 0.24 | USD 1.20 x (1 - 40% x 12pp) = USD 1.15 | 79% | Improve triage; tune planner |
| FX -20% local | unchanged USD | unchanged USD; +20% in local | 84% | Customer sees price rise in local; renegotiate or absorb |
| SLA breach month (worst) | USD 0.19 | USD 1.20 x 70% = USD 0.84 | 77% | Root-cause; fix; resume normal |
| Failure rate 2x | USD 0.30 | USD 1.20 | 75% | Tighten eval; reduce overconfident attempts |

The pricing is robust except at provider 5x (mitigated by pass-through clause).

## 9. Composition with Platform / Tier Pricing

When agent revenue sits inside a broader contract:

- **Platform fee** (per month, predictable) + **per-resolution variable** (uncapped or capped)
- **Tier** with **included resolutions / month** + **overage at per-resolution rate**
- **Per-agent base** + **per-step variable** (for agent platform)

Investors expect agent revenue to be **separately attributed** in ARR, NRR, and ACV; bundle pricing must permit attribution.

## 10. Anti-Patterns (recap)

- Per-seat pricing on agent product -> destroys value capture
- Per-query pricing on agent product -> commoditises and invites cost-pass-through fight
- No intervention-credit policy -> churn risk
- No vendor-cost pass-through -> first provider hike kills contract margin
- Pricing in local currency with USD costs and no FX clause -> first 15% depreciation eats margin
- Outcome pricing with undefined outcomes -> legal exposure
- Bundling that hides agent revenue -> investor multiple compressed
- Setting price without cost-floor analysis -> silent margin loss
- Setting price above value-ceiling -> adoption collapses
- Setting price below competitive-anchor without moat thesis -> giving away margin

## 11. Living-Plan Cadence

Mirrors `saas-agent-pricing-strategy/SKILL.md` cadence table.

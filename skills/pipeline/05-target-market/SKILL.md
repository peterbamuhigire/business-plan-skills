---
name: 05-target-market
description: Use when producing or reviewing the 05 target market component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Target Market & Customer Analysis Skill

## Overview

Generate Section 05 of the business plan: the target market section. Use this skill to identify the highest-priority customer segments, show why they matter, and translate customer understanding into commercially useful profiles.

## Use When

- Use when drafting or improving the target market section for a business plan or proposal.
- Use when the business needs specific customer segments, personas, buying logic, and segment priorities.
- Use when customer selection will affect channels, pricing, product choices, or financial assumptions.

## Do Not Use When

- Do not use to perform full market sizing or industry trend analysis without the market-analysis skill.
- Do not create personas that are decorative but commercially useless.
- Do not claim certainty where the business only has hypotheses; label assumptions clearly.

## Required Inputs

- Product or service definition, business model, and customer problem
- Available research, sales evidence, interviews, or assumptions about buyers
- Geographic and country context for demographics, behaviour, and purchasing power
- Any adjacent section outputs that influence customer profitability or route to market

## Workflow

1. Define the primary customer problem and the buyer most likely to pay for relief.
2. Segment the market using multiple dimensions and prioritise the most bankable segments.
3. Build personas that capture behaviour, purchase drivers, pain points, and economics.
4. Estimate acquisition and lifetime value logic where the data supports it.
5. Reconcile segment choices with market size, pricing, channels, and sales strategy.
6. Flag unsupported assumptions or validation gaps that need testing.

## Quality Bar

- Segments are specific enough to target, price, and sell to.
- Personas reflect buying behaviour and commercial value, not demographic theatre.
- Profitability and acquisition logic are transparent where estimates are used.
- Customer choices align with the rest of the plan.

## Anti-Patterns

- "Everyone is a customer" segmentation.
- Personas with no purchasing authority, need, or ability to pay.
- Copying generic demographics without tying them to demand or revenue.
- Customer assumptions that contradict the offer, channel, or pricing model.

## Outputs

- A finished or revised Section 05 target market draft
- Prioritised customer segments and personas
- Explicit assumptions and open questions for validation, marketing, and sales



Generate detailed customer profiles that prove the business understands exactly who will buy and why.

## Required Elements

1. **Primary target segment**  The core customer group with quantified size
2. **Secondary segments**  Additional markets to pursue in priority order
3. **Customer personas** (2-4)  Detailed buyer profiles using template below
4. **Segmentation criteria**  Multi-dimensional market division (minimum 3 dimensions)
5. **Buyer behaviour**  How customers discover, evaluate, and purchase
6. **Customer pain points**  Specific, validated problems they need solved
7. **Purchase drivers**  What triggers a buying decision
8. **Generational profile**  Where target customers sit on Kotler's generational spectrum
9. **Customer acquisition cost (CAC)**  Estimated cost per channel
10. **Customer lifetime value (CLV)**  Projected revenue per customer over time
11. **CLV:CAC ratio**  Must exceed 3:1 for bankability
12. **Customer profitability analysis**  Segment-level profitability ranking

## Customer Persona Template

For each persona:

```text
Name: [Representative name]
Demographics: [Age, gender, income, location, education]
Generation: [Baby Boomer / Gen X / Millennial / Gen Z / Gen Alpha]
Role/Title: [If B2B]
Goals: [What they want to achieve  be specific]
Pain points: [Frustrations with current solutions  quantify impact]
Buying behaviour: [How they research and purchase]
Digital maturity: [Analogue / Digitising / Digital-first / AI-augmented]
Decision criteria: [Ranked: price, quality, speed, trust, values alignment]
Preferred channels: [Where they spend time, how to reach them]
Objections: [Why they might NOT buy  and how to address each]
Estimated CLV: [Projected lifetime revenue from this persona]
```

## Segmentation Framework

Apply minimum three dimensions from:

- **Demographic**  Age, income, education, family size
- **Geographic**  Region, urban/rural, climate, market access
- **Psychographic**  Lifestyle, values, attitudes, personality
- **Behavioural**  Usage rate, loyalty status, purchase occasion, benefits sought
- **Firmographic** (B2B)  Industry, company size, revenue, decision-making structure
- **Technographic**  Technology adoption level, digital channel preference, device usage

### Generational Targeting (Kotler 6.0)

If target market includes Gen Z (born 1997-2012) or Gen Alpha (born 2013+), the plan must address:
- Social media as primary discovery channel
- Content authenticity over polished corporate messaging
- Personalisation capabilities in product and experience
- Values alignment (sustainability, diversity, ethics)
- Mobile-first and potentially immersive (AR/VR) experiences

## Customer Economics

### CLV Calculation

```text
Simple CLV = Average purchase value x Purchase frequency x Customer lifespan

Full CLV = (Average revenue per customer per period x Gross margin %)
           / Customer churn rate

CLV with discount rate = Sum of [Margin x Retention rate^t / (1 + Discount rate)^t]
                         for t = 1 to expected lifespan
```

### CAC Calculation

```text
CAC = Total sales and marketing spend / Number of new customers acquired

Channel-specific CAC:
  Paid ads CAC = Ad spend on channel / Customers acquired from channel
  Content CAC = Content production cost / Customers attributed to content
  Referral CAC = Referral incentive cost / Referred customers converted
```

### CLV:CAC Benchmarks

| Ratio | Interpretation | Action |
|---|---|---|
| < 1:1 | Losing money on every customer | Unsustainable  fix immediately |
| 1:1 - 3:1 | Marginal economics | Optimise acquisition or increase retention |
| 3:1 - 5:1 | Healthy unit economics | Bankable  investors expect this range |
| > 5:1 | Strong but potentially under-investing | Consider increasing acquisition spend |

### Customer Profitability Metrics (Farris)

Rank customer segments by profitability:

```text
Customer Profit = Revenue from customer - Cost to serve customer

Customer Profitability % = Customer Profit / Revenue from customer x 100
```

Apply the 80/20 rule: identify whether top 20% of customers generate 80% of profit. Flag segments where cost-to-serve exceeds revenue.

## Generation Process

1. Ask for: product/service type, B2B or B2C, geography, price point
2. Define primary and secondary segments using 3+ dimensions
3. Identify generational profile and digital maturity of target customers
4. Build 2-4 detailed personas with specific CLV estimates
5. Map the buyer journey from awareness to purchase to advocacy
6. Calculate CAC per channel with explicit assumptions
7. Calculate CLV using appropriate formula for the business model
8. Validate CLV:CAC ratio against benchmarks
9. Rank segments by customer profitability

## Quality Criteria

- Personas feel like real people, not demographic averages
- Segmentation uses minimum three criteria (not just demographics)
- CAC and CLV are calculated with stated assumptions
- CLV:CAC ratio exceeds 3:1 or explains the path to achieving it
- Generational characteristics are addressed if targeting Gen Z/Alpha
- Customer profitability analysis identifies most and least profitable segments
- Buyer journey maps specific touchpoints, not generic funnels

### Problem Recognition Scale

Segment target customers by pain level to prioritise acquisition efforts (Blank & Dorf, 2012):

| Level | Customer State | Segment Value |
|---|---|---|
| **Latent** | Have the problem, don't know it | Low  must educate first |
| **Passive** | Know the problem, not motivated | Medium  need a trigger event |
| **Active** | Searching for a solution | High  ready to evaluate |
| **Vision** | Built a workaround, will pay for better | Highest  earlyvangelists |

Focus initial targeting on Active and Vision-level customers. See `references/customer-discovery-archetypes.md`.

### B2B Customer Types

In business-to-business contexts, map all six types within the buying organisation (Blank & Dorf, 2012): End Users, Influencers, Recommenders, Economic Buyers, Decision-Makers, and Saboteurs. Each requires a different engagement approach. See `references/customer-discovery-archetypes.md`.

## References

- **The Underdog Principles  small business competitive advantage**: See `references/underdog-principles-kaza.md` for the Positioning/Proximity/Purpose framework (why focused markets beat mass markets), consultative business case framework (5-question investment test), the 1015% borrowing rule, purpose drift warning signs, and the technology trap (automation destroying human connection)  from Kaza (*Unconvention*, Ideapress, 2025). **Read when defining the target niche, justifying premium pricing to a focused segment, or advising a founder on purpose alignment.**
- **Customer profitability metrics**: See `references/customer-metrics.md` for CLV models, CAC calculations, retention economics, and customer profitability formulas from Farris and growth marketing frameworks
- **Buyer behaviour and personas**: See `references/buyer-behaviour.md` for generational buying patterns, digital maturity assessment, education-based marketing triggers, and the AARRR funnel applied to customer acquisition
- **Customer discovery archetypes**: See `references/customer-discovery-archetypes.md` for Customer Archetype framework with Day-in-the-Life analysis, Problem Recognition Scale for segmentation, six B2B customer types, three-tier stakeholder mapping, empathy-based interview methodology (8-category guide), Empathy Map synthesis, persona template, and current journey mapping  from Blank & Dorf (2012), Cooper & Vlaskovits (2010), and Alam
- **ICP, segmentation, and retention economics (Umbrex, 2025)**: See `../07-marketing-sales-strategy/references/customer-retention-playbook.md` for the 5-tier retention segmentation framework (structural/economic/behavioural/relationship/strategic), Ideal Customer Profile (ICP) 5-pillar validation checklist, High-Value Account (HVA) scoring template, 22 prioritisation matrix, and retention economics metrics (GRR, NRR, LTV/CAC, CAC payback). **Read when segmenting customers beyond firmographics, scoring ICP fit, or calculating CLV/CAC with investor-grade metric definitions.**
- **Advanced TAM/SAM/SOM methodology (Umbrex, 2025)**: See `../04-market-analysis/references/market-sizing-methodology.md` for precise TAM/SAM/SOM definitions and funnel logic, 8 market boundary principles, bottom-up penetration modelling, SOM reasonableness rules, Rogers' diffusion model for adoption S-curves, and a Uganda TAM/SAM/SOM template in UGX. **Read when building customer market size estimates or cross-checking SOM figures from a customer-base perspective.**
- **Uganda consumer demographics (World Bank, 2025)**: See `references/uganda-consumer-demographics-2025.md` for Uganda-specific consumer market data  population 46M (>50% under-18, growing >3%/year, 104M projected by 2060); generational segments (Gen Z ~1012M, Millennials ~810M); NEET youth 5.25M (the "aspiring but income-constrained" segment); income quintile profiles (Q1Q5) with access patterns for health, education, financial services, and FMCG; urban/rural split (Kampala 1.797M; rural pop +54% by 2030); education literacy gap (57% of P6 pupils below literacy minimum  design for low-literacy consumers); NCD-driven health product demand (NCDs rising to 37.3% of DALYs); social protection transfer recipients (2.43M) as emerging consumers; aspiration-versus-reality gap (youth want professional careers but 88% lack qualifications  "affordable aspiration" brand positioning); regional market characteristics (Central/Western/Eastern/Northern/Karamoja); key market sizing numbers (working for pay 10M; annual new labour force 1.11.2M; multidimensional poverty 41.2%). Sources: World Bank UHCDGR 2025, UNPHC 2024, UBOS UNHS 2019/20, NAPE 2023. **Read when building consumer personas, sizing the Uganda consumer market, determining price-point strategy, or selecting customer channels for any Uganda-based consumer or B2B business plan.**

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Segment evidence, buyer roles, customer economics, discovery records, and serviceability constraints for 05 target market | Customer interviews, sales records, market analysis, and operating model | Yes | If absent, customer evidence is unavailable for a proposed segment, label it a hypothesis and return a discovery plan instead of a finished ICP. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Prioritised target segments, ICPs, personas, and segment economics | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 05 target market exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 05 target market release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Segment scorecard, interview trace, CAC/CLV assumption log, and exclusion rationale | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 05 target market decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 05 target market review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 05 target market, the controlling focus is segment urgency, reachable buyer, willingness to pay, serviceability, acquisition economics, and beachhead choice. This skill may segment and prioritise supplied customer evidence; it may not infer protected traits, invent personas, or approve targeting that breaches consent or data-use limits. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 05 target market, loss of evidence about segment urgency, reachable buyer, willingness to pay, serviceability, acquisition economics, and beachhead choice activates degraded mode. If the controlling 05 target market evidence is unavailable, the same boundary applies. When customer evidence is unavailable for a proposed segment, label it a hypothesis and return a discovery plan instead of a finished ICP. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 05 target market, a large segment has weak urgency, access, margin, or product fit| deprioritise it and document the smaller segment whose buying trigger and serviceability are evidenced | Broad targeting wastes acquisition spend and obscures the real buyer |
| For 05 target market, A current legal, regulatory, tax, accounting, market, or platform claim controls the 05 target market decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 05 target market, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete prioritised target segments, icps, personas, and segment economics, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 05 target market decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect segment evidence, buyer roles, customer economics, discovery records, and serviceability constraints and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
4. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
5. Produce prioritised target segments, icps, personas, and segment economics with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
6. Run the section quality checks, applicable finance or professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Prioritised target segments, ICPs, personas, and segment economics must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Segment scorecard, interview trace, CAC/CLV assumption log, and exclusion rationale must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 05 target market, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 05 target market, treating an unavailable segment evidence, buyer roles, customer economics, discovery records, and serviceability constraints as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing prioritised target segments, icps, personas, and segment economics that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

Small retailers appear numerous, but interviews show pharmacies have the urgent stock-out problem and a named buyer. Select pharmacies as the beachhead.

## References

- Use the verified project evidence register and the owning upstream pipeline section for 05 target market; no local deep-dive reference is declared.
- For 05 target market claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->

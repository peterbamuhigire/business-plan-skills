---
name: target-market
description: Generate the target market section with customer personas, market segmentation, buyer behaviour analysis, customer acquisition cost estimates, and lifetime value projections. Defines exactly who the customer is and how they buy. Use when building or reviewing target market sections, creating customer personas, calculating CLV/CAC ratios, or validating customer segment choices. Incorporates Farris's customer profitability metrics, Kotler's generational analysis, and growth marketing acquisition frameworks.
---

# Target Market & Customer Analysis Skill

Generate detailed customer profiles that prove the business understands exactly who will buy and why.

## Required Elements

1. **Primary target segment** — The core customer group with quantified size
2. **Secondary segments** — Additional markets to pursue in priority order
3. **Customer personas** (2-4) — Detailed buyer profiles using template below
4. **Segmentation criteria** — Multi-dimensional market division (minimum 3 dimensions)
5. **Buyer behaviour** — How customers discover, evaluate, and purchase
6. **Customer pain points** — Specific, validated problems they need solved
7. **Purchase drivers** — What triggers a buying decision
8. **Generational profile** — Where target customers sit on Kotler's generational spectrum
9. **Customer acquisition cost (CAC)** — Estimated cost per channel
10. **Customer lifetime value (CLV)** — Projected revenue per customer over time
11. **CLV:CAC ratio** — Must exceed 3:1 for bankability
12. **Customer profitability analysis** — Segment-level profitability ranking

## Customer Persona Template

For each persona:

```
Name: [Representative name]
Demographics: [Age, gender, income, location, education]
Generation: [Baby Boomer / Gen X / Millennial / Gen Z / Gen Alpha]
Role/Title: [If B2B]
Goals: [What they want to achieve — be specific]
Pain points: [Frustrations with current solutions — quantify impact]
Buying behaviour: [How they research and purchase]
Digital maturity: [Analogue / Digitising / Digital-first / AI-augmented]
Decision criteria: [Ranked: price, quality, speed, trust, values alignment]
Preferred channels: [Where they spend time, how to reach them]
Objections: [Why they might NOT buy — and how to address each]
Estimated CLV: [Projected lifetime revenue from this persona]
```

## Segmentation Framework

Apply minimum three dimensions from:

- **Demographic** — Age, income, education, family size
- **Geographic** — Region, urban/rural, climate, market access
- **Psychographic** — Lifestyle, values, attitudes, personality
- **Behavioural** — Usage rate, loyalty status, purchase occasion, benefits sought
- **Firmographic** (B2B) — Industry, company size, revenue, decision-making structure
- **Technographic** — Technology adoption level, digital channel preference, device usage

### Generational Targeting (Kotler 6.0)

If target market includes Gen Z (born 1997-2012) or Gen Alpha (born 2013+), the plan must address:
- Social media as primary discovery channel
- Content authenticity over polished corporate messaging
- Personalisation capabilities in product and experience
- Values alignment (sustainability, diversity, ethics)
- Mobile-first and potentially immersive (AR/VR) experiences

## Customer Economics

### CLV Calculation

```
Simple CLV = Average purchase value x Purchase frequency x Customer lifespan

Full CLV = (Average revenue per customer per period x Gross margin %)
           / Customer churn rate

CLV with discount rate = Sum of [Margin x Retention rate^t / (1 + Discount rate)^t]
                         for t = 1 to expected lifespan
```

### CAC Calculation

```
CAC = Total sales and marketing spend / Number of new customers acquired

Channel-specific CAC:
  Paid ads CAC = Ad spend on channel / Customers acquired from channel
  Content CAC = Content production cost / Customers attributed to content
  Referral CAC = Referral incentive cost / Referred customers converted
```

### CLV:CAC Benchmarks

| Ratio | Interpretation | Action |
|---|---|---|
| < 1:1 | Losing money on every customer | Unsustainable — fix immediately |
| 1:1 - 3:1 | Marginal economics | Optimise acquisition or increase retention |
| 3:1 - 5:1 | Healthy unit economics | Bankable — investors expect this range |
| > 5:1 | Strong but potentially under-investing | Consider increasing acquisition spend |

### Customer Profitability Metrics (Farris)

Rank customer segments by profitability:

```
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
| **Latent** | Have the problem, don't know it | Low — must educate first |
| **Passive** | Know the problem, not motivated | Medium — need a trigger event |
| **Active** | Searching for a solution | High — ready to evaluate |
| **Vision** | Built a workaround, will pay for better | Highest — earlyvangelists |

Focus initial targeting on Active and Vision-level customers. See `references/customer-discovery-archetypes.md`.

### B2B Customer Types

In business-to-business contexts, map all six types within the buying organisation (Blank & Dorf, 2012): End Users, Influencers, Recommenders, Economic Buyers, Decision-Makers, and Saboteurs. Each requires a different engagement approach. See `references/customer-discovery-archetypes.md`.

## References

- **The Underdog Principles — small business competitive advantage**: See `references/underdog-principles-kaza.md` for the Positioning/Proximity/Purpose framework (why focused markets beat mass markets), consultative business case framework (5-question investment test), the 10–15% borrowing rule, purpose drift warning signs, and the technology trap (automation destroying human connection) — from Kaza (*Unconvention*, Ideapress, 2025). **Read when defining the target niche, justifying premium pricing to a focused segment, or advising a founder on purpose alignment.**
- **Customer profitability metrics**: See `references/customer-metrics.md` for CLV models, CAC calculations, retention economics, and customer profitability formulas from Farris and growth marketing frameworks
- **Buyer behaviour and personas**: See `references/buyer-behaviour.md` for generational buying patterns, digital maturity assessment, education-based marketing triggers, and the AARRR funnel applied to customer acquisition
- **Customer discovery archetypes**: See `references/customer-discovery-archetypes.md` for Customer Archetype framework with Day-in-the-Life analysis, Problem Recognition Scale for segmentation, six B2B customer types, three-tier stakeholder mapping, empathy-based interview methodology (8-category guide), Empathy Map synthesis, persona template, and current journey mapping — from Blank & Dorf (2012), Cooper & Vlaskovits (2010), and Alam
- **Uganda consumer demographics (World Bank, 2025)**: See `references/uganda-consumer-demographics-2025.md` for Uganda-specific consumer market data — population 46M (>50% under-18, growing >3%/year, 104M projected by 2060); generational segments (Gen Z ~10–12M, Millennials ~8–10M); NEET youth 5.25M (the "aspiring but income-constrained" segment); income quintile profiles (Q1–Q5) with access patterns for health, education, financial services, and FMCG; urban/rural split (Kampala 1.797M; rural pop +54% by 2030); education literacy gap (57% of P6 pupils below literacy minimum — design for low-literacy consumers); NCD-driven health product demand (NCDs rising to 37.3% of DALYs); social protection transfer recipients (2.4–3M) as emerging consumers; aspiration-versus-reality gap (youth want professional careers but 88% lack qualifications — "affordable aspiration" brand positioning); regional market characteristics (Central/Western/Eastern/Northern/Karamoja); key market sizing numbers (working for pay 10M; annual new labour force 1.1–1.2M; multidimensional poverty 41.2%). Sources: World Bank UHCDGR 2025, UNPHC 2024, UBOS UNHS 2019/20, NAPE 2023. **Read when building consumer personas, sizing the Uganda consumer market, determining price-point strategy, or selecting customer channels for any Uganda-based consumer or B2B business plan.**

---
name: market-analysis
description: Generate the market analysis section with industry overview, market size (TAM/SAM/SOM), growth trends, market drivers, regulatory environment, and data sources. Proves the market opportunity is real and large enough to justify investment. Use when building or reviewing market analysis sections, sizing markets, or validating market opportunity claims. Incorporates Farris's market metrics, Kotler's marketing evolution model, and bottom-up sizing methodology.
---

# Market Analysis Skill

Generate a data-driven market analysis that proves the business operates in a viable, growing market worth investing in.

## Required Elements

1. **Industry overview** — Current state, structure, dynamics, and marketing evolution stage
2. **Market size** — TAM, SAM, SOM with dual methodology
3. **Growth rate and trends** — Historical and projected CAGR
4. **Market drivers** — Forces fuelling growth (technology, regulation, demographics, AI adoption)
5. **Market barriers** — Entry barriers, switching costs, regulatory hurdles
6. **Regulatory environment** — Laws, licences, compliance requirements
7. **Industry lifecycle stage** — Emerging, growing, mature, or declining
8. **Key industry players** — Major companies and estimated market share
9. **Market share metrics** — How share is measured in this industry (Farris)
10. **Data sources** — Citation for every claim

## Market Sizing Methodology

Use **both** approaches and reconcile (investors flag plans using only top-down):

**Bottom-up (preferred):**
```
Number of potential customers
  x Average revenue per customer
  x Realistic conversion rate
  = SOM (Serviceable Obtainable Market)
```

**Top-down:**
```
Total industry revenue
  x Relevant segment percentage
  x Obtainable share percentage
  = SOM cross-check
```

### SOM Reasonableness Rules

- Startups: SOM typically 1-5% of SAM in years 1-3
- Established businesses entering new markets: 5-15% of SAM
- If SOM exceeds 20% of SAM, provide extraordinary justification
- TAM → SAM narrowing must show clear filtering criteria

## Market Share Metrics (Farris)

Define how market share is measured in this industry:

| Metric | Formula | Use |
|---|---|---|
| **Unit market share** | Units sold / Total units sold in market | Product businesses |
| **Revenue market share** | Revenue / Total market revenue | All businesses |
| **Relative market share** | Brand share / Largest competitor share | Competitive positioning |
| **Market concentration** | Combined share of top 3-4 players | Industry structure |
| **Share of wallet** | Spend with us / Customer's total category spend | Customer penetration |

## Marketing Evolution Context (Kotler 6.0)

Position the industry within Kotler's marketing evolution framework:

| Era | Focus | Relevance |
|---|---|---|
| Marketing 1.0 | Product-centric | Traditional manufacturing |
| Marketing 2.0 | Customer-centric | Service industries |
| Marketing 3.0 | Human-centric, values | Social enterprise, sustainability |
| Marketing 4.0 | Digital transition | E-commerce, digital-first |
| Marketing 5.0 | Technology for humanity | AI, IoT, big data integration |
| Marketing 6.0 | Immersive, phygital | Metaverse, AR/VR, phygital experiences |

Identify where the target industry sits and where it is heading — this signals market trajectory to investors.

## Generation Process

1. Ask for: industry, geography, target segment, business model
2. Research or estimate market size using both methodologies
3. Identify 3-5 key trends shaping the industry
4. Document regulatory landscape
5. Map competitive ecosystem (detailed in section 06)
6. Position industry on Kotler's evolution curve
7. Define how market share is measured in this industry
8. Cite all data sources — flag estimates clearly as "estimated"

## Quality Criteria

- Market size uses bottom-up methodology, not just top-down
- Both methods reconcile within 30% of each other
- Growth claims cite sources or are flagged as estimates
- TAM/SAM/SOM shows logical narrowing with clear filters
- SOM passes the reasonableness rules above
- Trends are specific to this industry, not generic macro trends
- Regulatory risks are acknowledged honestly
- Market share metrics are defined for this specific industry

## References

- **Market metrics and formulas**: See `references/market-metrics.md` for comprehensive market measurement formulas, market share calculations, and industry analysis metrics from Farris
- **Industry trend analysis**: See `references/industry-trends.md` for trend identification frameworks, digital transformation indicators, and phygital marketing evolution from Kotler 6.0
- **Marketing research methodology**: See `references/marketing-research-methodology.md` for the complete marketing research process, secondary data evaluation criteria, research design selection (exploratory/descriptive/causal), sampling methods with sample size formulas, statistical analysis techniques for market analysis, and research report formatting from Hair, Ortinau & Harrison

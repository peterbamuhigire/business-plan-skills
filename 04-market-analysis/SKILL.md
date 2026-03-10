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

### Market Type Classification

Before sizing the market, classify its type — this changes everything about strategy, spending, and timeline (Blank & Dorf, 2012):

| Type | Definition | Revenue Curve |
|---|---|---|
| **Existing market** | Known customers, known competitors | Predictable growth via share capture |
| **New market** | No existing category | Slow adoption, 3-7 years to scale |
| **Re-segmented** | Niche or low-cost in existing market | Moderate, segment-dependent |
| **Clone market** | Proven model from another country | Depends on local adaptation |

Use the cost-of-entry thresholds to assess competitive feasibility: 74%+ = monopoly (avoid head-on), 41%+ = market leader (re-segment instead), <26% = fragmented (easiest entry). See `references/market-type-entry-analysis.md`.

## References

- **Market metrics and formulas**: See `references/market-metrics.md` for comprehensive market measurement formulas, market share calculations, and industry analysis metrics from Farris
- **Industry trend analysis**: See `references/industry-trends.md` for trend identification frameworks, digital transformation indicators, and phygital marketing evolution from Kotler 6.0
- **Marketing research methodology**: See `references/marketing-research-methodology.md` for the complete marketing research process, secondary data evaluation criteria, research design selection (exploratory/descriptive/causal), sampling methods with sample size formulas, statistical analysis techniques for market analysis, and research report formatting from Hair, Ortinau & Harrison
- **Market strategy frameworks**: See `references/market-strategy-frameworks.md` for market sizing methods (6 methods including marketcrafting), HOOF demand forecasting, Porter's Five Forces with rating methodology, Value Net framework (complementors and cooperative dynamics), PESTEL environmental analysis, industry life cycle (S-curve phases), customer buying criteria (E2-P2-R2), and key success factor derivation from Evans, Harris & Lenox, and Fahey & Randall
- **Market type and entry analysis**: See `references/market-type-entry-analysis.md` for four market types (existing/new/re-segmented/clone), cost-of-entry thresholds from military OR (74%/41%/26% rules), revenue growth curves by market type, bottom-up vs. top-down estimation, Business Context Map (6-sector environmental scan), and market segmentation criteria — from Blank & Dorf (2012), Cooper & Vlaskovits (2010), and Alam
- **Uganda macroeconomic context (2025–26)**: See `references/uganda-macro-context-2025.md` for current Uganda GDP, exchange rates, inflation by category, population data, labour market statistics, poverty rates by region, household expenditure patterns, and financial access data — from UBOS (CPI Feb 2026, UNHS 2023/24, NLFS 2021, KEI Q1 2025/26) and World Bank (Uganda Economic Update 2023). **Read this file whenever sizing a Uganda market, citing inflation assumptions, or estimating consumer purchasing power.**
- **Uganda economic outlook — World Bank & AfDB (2025)**: See `references/uganda-economic-outlook-worldbank-afdb.md` for comprehensive quantitative data across 10 domains: GDP growth trajectory (FY22–FY27 including oil-boom FY27 projection of 9.8%), sectoral performance, interest rates and lending rates, exchange rate history, public debt, fiscal operations, export data (coffee, gold, tourism), FDI, poverty headcount (old and new IPL), agriculture productivity gaps vs. Kenya/Tanzania/Rwanda, oil pipeline (EACOP) timeline, climate shock projections, Africa-wide context from AfDB AEO 2025, and stress test reference data. Sources: World Bank UEU-21 (June 2023), World Bank UEU-26 (December 2025), AfDB AEO 2025. **Use this file for macroeconomic framing, sector benchmarking, risk sections, and any forward-looking projections beyond FY25.**
- **Uganda private sector markets — IFC/World Bank CPSD (2022)**: See `references/uganda-private-sector-markets.md` for private sector structure data, investment climate indicators, financial sector benchmarks (credit to private sector 14.2% GDP; SME loan access 6% vs Kenya 44%; lending rates 19.26%), and detailed sector opportunity assessments for agribusiness (fish, dairy, maize), energy (installed capacity 1,252 MW; SHS market 428,100 units), and housing (2 million unit shortfall; 180,000 units/year needed; 76% of households low income). Also covers cross-cutting constraints (infrastructure, trade, skills, land) and digital economy opportunity. Source: IFC/World Bank Country Private Sector Diagnostic, February 2022. **Read when sizing Uganda markets, assessing investment climate risk, or benchmarking against regional peers (Kenya, Rwanda, Tanzania).**

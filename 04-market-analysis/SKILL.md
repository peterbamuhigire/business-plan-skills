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

## Industry Structure Analysis (Porter)

Beyond market sizing, assess the **structural attractiveness** of the industry using Porter's analytical frameworks:

### Industry Lifecycle Stage (Porter's critique of the Product Life Cycle)
Rather than mechanically applying the standard introduction → growth → maturity → decline model (which Porter shows is unreliable), identify the **driving forces** that are actively changing industry structure:

| Driving Force | How to Assess It |
|--------------|-----------------|
| Long-run growth rate change | Is the market growing, plateauing, or declining? What is causing it? |
| Changes in buyer segments | Are new buyer types entering? Are existing buyers becoming more sophisticated? |
| Product or process innovation | Is technology changing what buyers expect or how firms can serve them? |
| Entry or exit of major firms | Are new entrants or large firms reshaping the competitive landscape? |
| Input cost changes | Are input costs shifting in ways that favour some competitors over others? |
| Regulatory change | Is regulation creating or removing entry barriers? |

### Strategic Group Mapping
Cluster competitors into **strategic groups** — firms following similar strategies along key dimensions (price position, quality, geographic coverage, vertical integration, brand investment). This reveals:
- Which firms are *direct* competitors (same strategic group) vs. indirect (different group)
- Whether any strategic position is unoccupied — and whether this is an opportunity or a structural impossibility
- Which group is in the most structurally attractive position (faces weakest Five Forces)

**Cross-reference:** `references/industry-structure-porter.md` for the complete framework including strategic dimensions, mobility barriers, industry evolution driving forces, and Uganda/EA application notes.

## References

- **Industry structure, strategic groups, and industry evolution**: See `references/industry-structure-porter.md` for strategic group mapping methodology, dimensions of competitive strategy, mobility barriers, industry evolution driving forces, product life cycle critique, and Uganda/EA application notes — from Porter (1980)
- **Market metrics and formulas**: See `references/market-metrics.md` for comprehensive market measurement formulas, market share calculations, and industry analysis metrics from Farris
- **Industry trend analysis**: See `references/industry-trends.md` for trend identification frameworks, digital transformation indicators, and phygital marketing evolution from Kotler 6.0
- **Marketing research methodology**: See `references/marketing-research-methodology.md` for the complete marketing research process, secondary data evaluation criteria, research design selection (exploratory/descriptive/causal), sampling methods with sample size formulas, statistical analysis techniques for market analysis, and research report formatting from Hair, Ortinau & Harrison
- **Market strategy frameworks**: See `references/market-strategy-frameworks.md` for market sizing methods (6 methods including marketcrafting), HOOF demand forecasting, Porter's Five Forces with rating methodology, Value Net framework (complementors and cooperative dynamics), PESTEL environmental analysis, industry life cycle (S-curve phases), customer buying criteria (E2-P2-R2), and key success factor derivation from Evans, Harris & Lenox, and Fahey & Randall
- **Market type and entry analysis**: See `references/market-type-entry-analysis.md` for four market types (existing/new/re-segmented/clone), cost-of-entry thresholds from military OR (74%/41%/26% rules), revenue growth curves by market type, bottom-up vs. top-down estimation, Business Context Map (6-sector environmental scan), and market segmentation criteria — from Blank & Dorf (2012), Cooper & Vlaskovits (2010), and Alam
- **Uganda macroeconomic context (2025–26)**: See `references/uganda-macro-context-2025.md` for current Uganda GDP, exchange rates, inflation by category, population data, labour market statistics, poverty rates by region, household expenditure patterns, and financial access data — from UBOS (CPI Feb 2026, UNHS 2023/24, NLFS 2021, KEI Q1 2025/26) and World Bank (Uganda Economic Update 2023). **Read this file whenever sizing a Uganda market, citing inflation assumptions, or estimating consumer purchasing power.**
- **Uganda economic outlook — World Bank & AfDB (2025)**: See `references/uganda-economic-outlook-worldbank-afdb.md` for comprehensive quantitative data across 10 domains: GDP growth trajectory (FY22–FY27 including oil-boom FY27 projection of 9.8%), sectoral performance, interest rates and lending rates, exchange rate history, public debt, fiscal operations, export data (coffee, gold, tourism), FDI, poverty headcount (old and new IPL), agriculture productivity gaps vs. Kenya/Tanzania/Rwanda, oil pipeline (EACOP) timeline, climate shock projections, Africa-wide context from AfDB AEO 2025, and stress test reference data. Sources: World Bank UEU-21 (June 2023), World Bank UEU-26 (December 2025), AfDB AEO 2025. **Use this file for macroeconomic framing, sector benchmarking, risk sections, and any forward-looking projections beyond FY25.**
- **Uganda private sector markets — IFC/World Bank CPSD (2022)**: See `references/uganda-private-sector-markets.md` for private sector structure data, investment climate indicators, financial sector benchmarks (credit to private sector 14.2% GDP; SME loan access 6% vs Kenya 44%; lending rates 19.26%), and detailed sector opportunity assessments for agribusiness (fish, dairy, maize), energy (installed capacity 1,252 MW; SHS market 428,100 units), and housing (2 million unit shortfall; 180,000 units/year needed; 76% of households low income). Also covers cross-cutting constraints (infrastructure, trade, skills, land) and digital economy opportunity. Source: IFC/World Bank Country Private Sector Diagnostic, February 2022. **Read when sizing Uganda markets, assessing investment climate risk, or benchmarking against regional peers (Kenya, Rwanda, Tanzania).**
- **AfCFTA and East Africa trade framework**: See `references/afcfta-ea-trade-framework.md` for Uganda's participation in AfCFTA (54 countries, $3.4T GDP market), EAC Common External Tariff structure (0%/10%/25%), Rules of Origin (35% local value-added for zero tariff), Uganda's six trade agreements (EAC, COMESA, AfCFTA, EBA, AGOA, UK DCTS), May 2025 export destination data (Middle East 34.4%, EAC 25%, EU 19.1%), top exports (gold $3.16B, coffee $990M), PAPSS for local currency cross-border payments, EUDR compliance requirements (effective 31 Dec 2025, applies to coffee/cocoa/timber), and practical implications for plan authors. Cross-reference `references/eac-trade-data-2024.md` for 2024–25 statistics. **Read when the business has export potential, imports from outside EAC, or needs to size the regional market beyond Uganda.**
- **EAC trade data 2024–2025**: See `references/eac-trade-data-2024.md` for current quantitative trade benchmarks — Uganda export growth 22% in 2024 and 50% in Jan–May 2025; Uganda AfCFTA export potential US$178.2M (dairy $178M, coffee $101M, sugar $86M, wood $84M, ferrous metals $112M); EAC total trade US$11B 2024; NTB count rising (10→48 between Nov 2024 and May 2025); OSBP impact (79% border time reduction); EAC regional value chain participation only 1.7% of gross exports. Sources: UNECA Sep 2025, de Melo/Twum FERDI 2020, EAC/TradeMark Africa Apr 2024. **Use for current market sizing figures when the business targets exports or competes with imported goods.**
- **EAC Common Market Framework**: See `references/eac-common-market-framework.md` for EAC Common Market Protocol seven freedoms (goods, persons, labour, establishment, residence, services, capital); free movement of workers and no work permit fees for EAC nationals (Art. 10); mutual recognition of qualifications (EAQFHE 2015); right of establishment for EAC companies; regional value chain opportunities (dairy, maize, tourism) with Uganda's structural position; Uganda SME export pathways; cross-border hiring implications; overlapping EAC/IGAD frameworks. Sources: EAC Common Market Protocol 2009, Daly et al./IGC 2016, IOM/BRMM 2022. **Read when the business has regional expansion plans, is hiring EAC nationals, or needs to understand market access rights within the EAC bloc.**
- **Uganda human capital development (World Bank, 2025)**: See `references/uganda-human-capital-2025.md` for the World Bank's full analysis of Uganda's human capital trajectory — HCI score 0.39 (2022), Vision 2040 GDP targets (US$50B → US$500B, per capita US$1,046 → US$7,000), demographic dividend framing (46M population, >50% under-18, 104M projected by 2060, 1.1–1.2M new workers/year), education statistics (LAYS 4.3, 57% of P6 pupils below literacy minimum, education spend only 2.7% of GDP), health outcomes table (life expectancy 68.5 years, maternal mortality 189 per 100,000), WASH gaps (12M without basic water, 38M without safe sanitation), social protection coverage (3% of population), and public investment requirements to hit Vision 2040. **Read when framing demographic market drivers, sizing growth in consumer or social-sector markets, or establishing Uganda's development context in the opening of any market analysis section.**
- **Uganda agriculture sector data (2021/22)**: See `references/uganda-agriculture-survey-2022.md` for crop production benchmarks (maize 1.5 MT/ha, coffee 265,000 MT total, banana 10M MT), livestock prevalence by species and region, input adoption rates (fertiliser 5–8 kg/ha nationally, irrigation 0.7% of HHs, improved seed 4%), farm size distribution (avg 1.3 Ha), market access data (avg 7.1 km to market), agro-processing sector (65% of manufacturing, USD 13.24B value), and regional benchmarks for all 14 sub-regions. Source: UBOS AAS 2021/22; WB UEU-26 2025. **Read when sizing agricultural markets, planning agribusiness models, benchmarking crop yields, or analysing agro-input business potential.**
- **Uganda tourism sector**: See `references/uganda-tourism-sector.md`
- **AfDB African Economic Outlook 2025**: See `references/africa-economic-outlook-2025.md` for Africa-wide GDP projections (3.9% 2025, 4.0% 2026), East Africa regional performance (5.9% 2025–26 — fastest growing), country profiles (Uganda 6.8%/4.1% inflation; Tanzania 5.9%/3.3% lowest inflation; Rwanda 7.7%; Kenya 4.9%), USD 1.43T domestic capital mobilisation potential across five forms (fiscal/natural/financial/business/human), downside risk tiers (US tariffs, aid cuts, climate, debt distress), and strategic opportunities (AfCFTA, beneficiation, diaspora). **Read when framing continental macro context, projecting East Africa growth, or assessing risk factors for 2025–2026 business plans.**
- **East Africa mineral resource governance**: See `references/ea-mineral-governance.md` for country-by-country mineral production data (Tanzania/Kenya/Uganda/Rwanda/Burundi), royalty rates by country (Tanzania 4–5% metals, 1% clearing fee), World Bank governance indicators for all five EAC states, IFF risk (USD 30–52B/year, >50% from extractives, Acacia Mining precedent), ASM employment data (Uganda 300K direct/5M dependent), local content compliance cost estimates (Tanzania 15–25%, Uganda/Kenya 10–15%), EITI participation status, and jurisdiction selection tier guide. **Read when writing market analysis or risk sections for mining/extractive ventures in East Africa.**
- **Africa-wide trade and economic outlook (2025)**: See `references/africa-trade-outlook-2025.md` for Africa GDP growth trajectory (3.4% continental avg; Eastern Africa 4.4%), East Africa country projections (Uganda 6.8% 2025, Kenya 5.3%, Tanzania 6.0%, Rwanda 7.2%), Africa total goods trade US$1,401B (+5.8%), intra-African trade US$208B (+7.7% AfCFTA effect), Uganda credit rating downgrade (B3 Moody's), commodity price gains (coffee +46%, gold +23%), fiscal balance trajectories, and Africa debt/inflation context. Source: Afreximbank ATO 2025. **Read when framing continental/regional macro context, benchmarking Uganda against EA peers, or assessing trade-related market opportunities.** for pre-COVID sector size (6% of GDP, USD 1.4B receipts, 1.5M arrivals), employment (670,000 direct; 1.56M indirect), post-pandemic recovery trajectory (513,000 arrivals 2022), Uganda's competitive position (54% of world's mountain gorillas, most bird species in Africa), infrastructure gaps, 25 regulatory licences, World Bank recommendations, and investment opportunities in accommodation, concessions, and product diversification. Source: WB Uganda Economic Update June 2023. **Read for tourism business plans, lodge/hospitality investment proposals, or tour operator market analysis.**
- **Advanced market sizing methodology (Umbrex, 2025)**: See `references/market-sizing-methodology.md` for the complete Umbrex Market Sizing Playbook — TAM/SAM/SOM definitions and funnel logic; 8 market boundary principles; 12 failure modes with mitigations; top-down step-by-step build; bottom-up penetration modelling; supply-side/value-chain sizing; Three-Lens Triangulation Framework (top-down + bottom-up + expert); order-of-magnitude sanity checks with universal constants; driver trees and Monte Carlo sensitivity stress-testing; adoption S-curve and Rogers diffusion model; communicating market sizing to investors (Pyramid Principle, three investor questions); and a Uganda/East Africa application section with reference numbers, common sizing approaches by market type, and a TAM/SAM/SOM template in UGX. **Read when building or stress-testing any TAM/SAM/SOM model, preparing for investor scrutiny, or working with limited data in East African markets.**
- **Statistical rigour for market analysis**: Use `meta-statistics` skill when computing or presenting any market sizing figures, growth rates, survey results, or comparative statistics. Key rules: use geometric mean (not arithmetic) for CAGR; use confidence intervals on all primary survey claims; use coefficient of variation to compare volatility across segments; follow Section 2.5 data visualisation standards (no 3D charts; axis from zero; label units). See `meta-statistics/references/statistics-for-business-plans.md §Market Sizing` for TAM/SAM/SOM statistical methodology and citation templates.

---
name: market-sizing-methodology
description: Advanced market sizing methodology covering TAM/SAM/SOM definitions, market boundary principles, 12 failure modes, top-down and bottom-up methodologies, data collection (secondary sources, primary research, proxy indicators), three-lens triangulation framework, driver trees, sensitivity stress-testing, OOM sanity checks, and communicating market sizing to investors. Source: Umbrex Consulting LLC Market Sizing Playbook (2025).
type: reference
---

# Market Sizing Playbook
**Source:** Umbrex Consulting LLC, *Market Sizing Playbook* (Umbrex, 2025, ISBN 978-1-968040-37-6). 193 pages. Practitioner playbook building on hundreds of McKinsey and independent consulting engagements.

---

## Chapter 1 — Foundations of Market Sizing

### Why Market Sizing Matters
Market sizing translates vision into evidence. It tells investors whether the opportunity is worth the capital, tells management where to prioritise, and tells founders whether the business can ever achieve meaningful scale. Three contexts demand rigorous sizing:
- **Investment/M&A:** Confirming the prize justifies capital commitment
- **Strategic planning:** Allocating R&D, sales, and marketing resources across opportunities
- **Operational planning:** Forecasting revenue potential and setting realistic targets

### Essential Definitions

**Market** — The set of economic transactions in which a defined customer group buys a defined solution to satisfy a defined need. Three guardrails: product/service scope (what is in vs. adjacent), customer scope (who buys or could buy), and substitutability (if buyers can weigh two offerings against the same need, both belong in the market).

| Layer | Definition | Key Question | Practical Use |
|-------|-----------|-------------|---------------|
| **TAM** (Total Addressable Market) | Revenue if every potential buyer adopted at today's average economics — perfect penetration, no competition | "How big is the theoretical ceiling?" | Benchmark ambition; size the prize |
| **SAM** (Serviceable Available Market) | TAM filtered through your business model — products you can make, geographies you can reach, segments you can credibly serve | "What portion could we structurally compete for?" | Entry prioritisation; resource allocation |
| **SOM** (Serviceable Obtainable Market) | Realistic share of SAM captureable within strategic planning horizon given competition and capacity | "What can we actually win?" | Revenue targets; investor forecasts |
| **Share** | Current position in % terms against TAM, SAM, or SOM (always declare the denominator) | "Where are we today?" | Competitive benchmarking |

**The funnel:** TAM (theoretical boundary) → SAM (structurally eligible territory) → SOM (realistically winnable prize) → Share (what you hold today).

**State the hierarchy clearly:** A 20% SAM share may equal only 5% of TAM. Clarity prevents the "denominator game" where ambitions look impressive because the wrong pool is cited.

**TAM tips:**
- State whether TAM is revenue-based (dollars spent) or volume-based (units, tons, gigabytes)
- Anchor to an explicit time stamp (e.g., "TAM 2025F")
- If combining multiple geographies, disclose exchange-rate assumptions

**SAM scoping checklist:** Regulatory constraints (licences, tariffs), channel reach (inside sales vs. distributors), technology readiness (product roadmap vs. customer requirements).

**SOM quantification:** Bottom-up capacity or sales-coverage modelling; win-loss conversion rates applied to SAM pipeline; sensitivity to price elasticity and competitive moves.

### Principles of Sound Market Boundary Definition (8 Principles)
Drawing the market boundary is the single biggest swing factor in accuracy — too wide inflates the prize, too narrow overlooks adjacencies.

1. **Begin with the strategic decision.** A boundary informs a choice. State the decision first (e.g., "whether to enter on-demand drone delivery") — this disciplines the scoping conversation.

2. **Anchor on the customer's needs, not the technology.** Define as "last-mile delivery of sub-5-pound parcels within 2 hours" not "drone logistics sector" — futures-proofing against technology shifts.

3. **Apply the substitutability test.** If a buyer can weigh two offerings against each other for the same need, both belong inside the market. Electric heat pumps and gas boilers compete for residential heating; solar panels and rooftop wind turbines rarely do.

4. **Segment where economics differ materially.** Include sub-segments only when demand drivers, price elasticity, or regulation differ enough to change the sizing math.

5. **Respect geographic granularity when it alters growth curves.** National borders matter when regulation, infrastructure, or consumer behaviour diverge. In homogeneous regions, aggregate.

6. **Match boundary definition to data availability.** The perfect conceptual boundary is useless if you cannot populate it with numbers. Probe data sources early (trade codes, HS codes, point-of-sale panels).

7. **Stress-test for scope creep and omission.** Run a weekly "ring-fence review": what is explicitly in, what is explicitly out. Also search for blind spots — niches omitted because outside the team's comfort zone.

8. **Keep the boundary dynamic.** Build a trigger list — regulatory decisions, cost milestones, adoption-rate inflections — that would force you to redraw the boundary.

**Quick diagnostic checklist:**
- Can we state the market in one sentence using need, customer, and solution?
- Have we tested substitutability from the end-user's perspective?
- Does every included segment move the valuation needle if its growth diverges?
- Do we have at least two independent data sources for each segment?
- Have we documented explicit exclusions and the rationale?
- What events would make this boundary obsolete?

### Twelve Common Failure Modes and Mitigations

| # | Failure Mode | Description | Mitigation |
|---|--------------|-------------|-----------|
| 1 | **Boundary bloat** | Generous definitions inflate prize | Weekly ring-fence review; standing "devil's advocate" |
| 2 | **Double counting** | Overlapping datasets tallied twice | Map inputs to mutually exclusive hierarchy; pivot check |
| 3 | **Single-source syndrome** | Relying on one syndicated report | Triangulate ≥3 independent lenses |
| 4 | **Price-basis mismatch** | Wholesale vs. retail vs. pre-rebate figures mixed | Enforce common price basis at ingest stage |
| 5 | **Extrapolation compounds error** | Past growth rates projected forward ignoring S-curves | Driver-based forecasting; scenario analysis |
| 6 | **Static elasticity** | Price sensitivity treated as constant | Layer elasticity curves by segment; re-estimate as penetration climbs |
| 7 | **Demand–supply confusion** | Capacity-based sizing misread as demand | Cross-check supply-side with purchase-order data or surveys |
| 8 | **Adoption-friction blindness** | Linear path from awareness to purchase assumed | Build "time-to-adopt" lags; validate with customer journey interviews |
| 9 | **Primary-research bias** | Surveys skew to enthusiasts; expert panels favour incumbents | Balance: telemetry + surveys + diverse expert pools including sceptics |
| 10 | **Currency and inflation oversights** | Nominal vs. real figures mixed; FX frozen | Convert to constant-currency real terms; state forward FX and inflation assumptions |
| 11 | **Snapshot trap** | Single-year TAM snapshot hides secular shifts | Show 5-year history + 5-year forward series |
| 12 | **Cannibalisaton neglect** | New product displacing legacy offerings not modelled | Forecast new category growth AND corresponding legacy decline |

---

## Chapter 2 — Scoping and Framing

### Clarifying the Business Question
Every sizing exercise exists to inform a choice. Distil the single decisive question whose answer unlocks action before building any model.

**Eight-question kickoff drill:**
1. What exact decision will this sizing inform?
2. By when must that decision be made?
3. What financial exposure and irreversibility are attached?
4. What magnitude difference changes the choice? (venture fund ±50% tolerance vs. utility committing $2B grid-scale batteries needing ±5%)
5. What hypotheses carry the most uncertainty and impact?
6. Which 3–5 value drivers should anchor the model?
7. What precision, currency, and time frame satisfy stakeholders?
8. Who holds veto power, and are they in the room?

**Map decision horizon and risk tolerance:** Plot the decision on a two-axis matrix — financial exposure vs. irreversibility — to calibrate depth of analysis required.

**Define success criteria in four buckets:**
- Analytical rigour — model audit trail passes internal control checks
- Stakeholder buy-in — all signatories initial the Assumption Register
- Timeliness — insights delivered before the investment committee date
- Actionability — outputs feed directly into valuation or capital-allocation model without reformatting

### Setting Market Granularity and Geographic Scope
Objective: "minimum viable granularity" — the fewest segments and regions that still move the decision needle.

**Practical rule of thumb:** Segment or localise only when a sub-slice changes the aggregate forecast by ≥10%, or exhibits a growth rate 2× above or below the mean.

**Customer-driven segmentation hierarchy:** Start with how buyers make choices (not how data sources classify products). If purchase criteria differ more by enterprise size than by industry, lead with firmographic tiers.

**Geographic clustering approach ("cluster and peel"):** Start broad; peel off outliers whose drivers break from cluster average. Countries sharing regulatory regimes (e.g., EU CE-marked medical devices) or consumer culture can be treated as one unit.

**Exchange-rate and PPP harmonisation:** Convert historical figures to real terms in a common base year. For purchasing-power-sensitive products, apply PPP adjustments (a $299 smartphone targets separate income tertiles in Uganda vs. Germany).

**When to revisit granularity:** When a new region exceeds 5% of global demand, or when a sub-segment's CAGR outpaces the parent by 3× for two consecutive years.

### Stakeholder Alignment on Assumptions

**Assumption Register:** Host a half-day workshop with all primary stakeholders. Capture explicit statements ("Average selling price declines 5% per year"; "Regulatory clearance by Q4 2026") in an Assumption Register with source, owner, and last validation date.

**Classify by impact × certainty (2×2 matrix):** High-impact, high-uncertainty assumptions become dedicated workstreams. Low-impact, low-uncertainty items ride on secondary data.

**RACI for assumptions:** Finance VP accountable for discount rate; strategy lead responsible for market growth rates; legal counsel consulted on regulatory timing.

**Red teams:** Assign 2 outsiders to challenge core assumptions, hunt blind spots, propose alternative scenarios. Document how each challenge was addressed — this bolsters credibility with investors.

### Drafting the Initial Hypothesis and Workplan
Start with a falsifiable statement: "The U.S. DC-fast charging market will exceed $4 billion in revenue by 2030, driven primarily by fleet electrification." — not "EV charging is a big opportunity."

**Driver tree construction:**
- Decompose hypothesis into first-principle levers: number of addressable vehicles × annual charge events × kWh per event × price per kWh
- Continue branching until further splits no longer change the decision
- Only expand branches that cross the materiality threshold

**Hypothesis workplan discipline:**
- Convert each high-impact, high-uncertainty node into a time-boxed workstream with owner and timeline
- Structure in one-week sprints ending with a hypothesis checkpoint
- Embed verification milestones (go/no-go gates with independent reviewers)
- Define exit criteria: hypothesis "closed" when confidence exceeds pre-agreed threshold (e.g., ±15% at 80% certainty)

---

## Chapter 3 — Data Collection Playbook

### Secondary-Source Mining

**Three-pillar source universe:**
1. **Industry reports** — Gartner, IDC, Euromonitor, Wood Mackenzie, niche boutiques (scale comparisons, segmentation, CAGR estimates)
2. **Government and multilateral data** — Statistical agencies (UBOS for Uganda, KNBS for Kenya, NBS for Tanzania), UN Comtrade, EIA, FAO, central-bank surveys (free, transparent, longitudinal — but lag 12–24 months)
3. **Trade associations** — Sector-specific shipment figures, but may under-report disruptor segments

**4T quality screen (apply to every source):**
| Criterion | Question |
|-----------|---------|
| **Transparency** | Does the publisher disclose definitions and methodology? |
| **Timeliness** | How recently was the data collected? (Fast-moving sectors: >12 months = unreliable) |
| **Taxonomy** | Are product and customer categories aligned with your market boundary? |
| **Triangulation** | Can at least one independent source corroborate the figure? |

**Normalise and reconcile:** Translate all data to a common basis — constant-currency, real terms; consistent unit measures; identical price levels. Store conversion factors in the workbook.

**Source Log:** One line per unique figure — publication name, page/table reference, download location, transformations applied. Link cells to the log via comments. This audit trail speeds red-team reviews and protects you under investor scrutiny.

**Creative data sourcing for scarce categories:**
- Satellite imagery (tracking solar farm build-outs via panel counts)
- Web-scraped product listings (estimating SKU proliferation on e-commerce sites)
- Patent databases (proxying R&D pipeline depth by geography)
- Shipping-manifest analytics (flagging volume shifts before official trade statistics)

**Uganda/EA secondary sources (apply 4T screen):**
- UBOS Statistical Abstract, National Household Survey, National Population Census 2024
- Bank of Uganda Monetary Policy Reports, Quarterly Financial Stability Report
- Uganda Revenue Authority tax compliance reports
- Uganda Investment Authority (UIA), Private Sector Foundation Uganda (PSFU) reports
- East African Community statistics, AfDB African Economic Outlook
- IFC, World Bank Uganda CPSD and sector studies

### Primary Research

**Expert interviews:**
- Build a knowledge grid: list critical unknowns vs. archetypes best positioned to answer each (former regulators, supply-chain heads, procurement VPs)
- Cast a balanced net: insiders from incumbents, disruptors, service providers, and adjacent sectors
- Use ranges ("<10%, 10–30%, >30%") to coax numbers from reluctant experts
- Offer blind-quote reassurance; cross-check each insight with at least two other perspectives
- Log transcript timestamps linked to the driver-tree node they inform

**Surveys:**
- Precisely define target population; calculate sample size from precision requirement (±5pp at 95% confidence in 50,000 population → ~380 responses)
- Question design rules: one construct per question; behaviour over intent (ask for last-period spend, not future plans); anchored scales
- Pre-test with 10 respondents; weight results back to population proportions
- Clean data rigorously: remove speeders, straight-liners, and improbable outliers

**Mystery shopping:** Use to reveal ground truth when price transparency is low (simulate buyer personas, record full price-discount ladder). Integrate price dispersion outputs into model's pricing module.

### Proxy Indicators and Adjacency Benchmarks

**Five proxy indicator families:**
| Family | Examples | Best For |
|--------|---------|---------|
| **Digital exhaust** | Search query volumes, app-store downloads, social media mentions | Consumer interest tracking |
| **Factor inputs** | Import/export volumes, critical raw materials, component order books | Hardware-centric industries |
| **Regulatory artifacts** | Licence applications, environmental filings, subsidy grant lists | Markets with 12–24 month policy lead time |
| **Labour market signals** | Job postings with specialist keywords, LinkedIn employee counts | Software platforms and frontier tech |
| **Capital flows** | Venture funding rounds, infrastructure bond issuances, equipment leasing | Pre-revenue market signalling |

**Designing a proxy framework:**
1. Define the latent variable (specific driver-tree node)
2. Hypothesise candidate signals (measurable phenomena plausibly correlated)
3. Back-test correlations (R² >0.6 at meaningful lags justifies operational use)
4. Calibrate scaling factors (translate proxy units to market units)
5. Stress-test robustness (check sensitivity to outliers, seasonality, structural breaks)

**Adjacency benchmarks (learning from analog markets):**
- Technology adoption S-curves (smartphones inform smart-watch diffusion)
- Cost-performance learning curves (Wright's Law: cost decline as function of cumulative production)
- Channel evolution (e-commerce penetration in apparel foreshadowed furniture patterns)
- Business-model migration (perpetual license → SaaS mirrors hardware firewalls → security-as-a-service)

**Guardrails:** Always pair quantitative analogs with qualitative sanity checks. Distinguish leading vs. lagging proxies before deploying.

### Data Reliability and Triangulation

**Source Quality Matrix (5 dimensions, 1–5 scale):**
- Transparency, Timeliness, Taxonomy fit, Triangulability, Track record
- Inputs scoring ≤3 trigger mandatory triangulation or replacement

**Weighted-average modelling:** Convert reliability scores into weights (inverse-variance or proportional weighting). Document the formula; avoid unilateral source picks unless one source scores ≥2 points above others.

**Triangulation by orthogonality:** Sources must differ along at least one structural dimension — method (supply vs. demand), data type (quant vs. qual), or vantage point (geography, value-chain stage). Convergence suggests robustness; divergence flags deeper investigation.

**Gap management:**
1. Gap log: list every driver-tree node lacking data or scoring ≤3
2. Materiality screen: multiply node's sensitivity weight by its size share; fill high-materiality gaps first
3. Scenario ranges for irreducible uncertainty: pessimistic floor (historical precedent), reference case (expert consensus), optimistic ceiling (technology-learning extrapolation)

---

## Chapter 4 — Top-Down Market Sizing

### Conceptual Overview
Top-down starts at 30,000 feet with a macroeconomic or industry-wide figure, then applies a sequence of filters to isolate the target opportunity.

**Strengths:** Data leverage (macroeconomic databases are vetted by large statistical teams), speed and replicability, early strategic signalling.

**Best used when:** Reliable high-level statistics exist; boundary nests cleanly inside existing statistical categories; decision tolerates ±20% accuracy for initial gating decisions.

**Caution flags:** Rapid technology shifts (statistics lag); fragmented/informal sectors (under-registration in official data); more than four sequential filters (consider bottom-up instead).

### Four Core Components
1. **Base metric** — Choose a top-level figure tightly correlated with the target market (e.g., global smartphone sales for mobile accessories)
2. **Filter ratios** — Apply successive percentages along relevant dimensions (geography, customer segment, product subset, usage intensity) — each ratio must be evidence-based and independently triangulated
3. **Price or value translation** — Multiply resulting unit quantity by average selling price (ASP) or revenue yield to convert volume to dollars
4. **Time-series extension** — Layer growth drivers (GDP forecasts, penetration curves, regulatory milestones) to project forward

### Step-by-Step Top-Down Build
1. Select macro base (verify in ≥2 independent sources)
2. Apply geographic filter (country/region share of global)
3. Apply segment filter (% of addressable population or spend)
4. Apply product/service specificity filter (% of segment relevant to exact offering)
5. Apply usage/penetration filter (% who will actually buy)
6. Multiply by ASP to get revenue TAM
7. Apply SAM and SOM filters
8. Cross-check result with order-of-magnitude sanity test

### Handling Data Gaps in Top-Down Models
- Use proxy indicators for missing ratios (§3.3 above)
- When a single ratio dominates outcome, make it a scenario variable (optimistic/base/pessimistic)
- Document assumptions explicitly — investors focus scrutiny on the filters, not the base metric

---

## Chapter 5 — Bottom-Up Market Sizing

### Conceptual Overview
Bottom-up builds from first principles: count potential buyers, multiply by average revenue, adjust for adoption rates. It is more granular and defensible than top-down but requires more data and analytical effort.

**Best used when:** You can enumerate or estimate the customer population directly; sales-team capacity constrains the achievable market; unit economics are known from early customers.

**Core formula:**
```
Number of addressable customers
× Win rate (conversion assumption)
× Average contract value / revenue per customer
= SOM
```

### Step-by-Step Bottom-Up Build
1. Define target customer population (who qualifies by ICP criteria)
2. Estimate population size (census data, trade directories, market research, LinkedIn, web scraping)
3. Segment population by tier (enterprise, mid-market, SME) with different conversion assumptions
4. Estimate average contract value per tier (from early customer data or comparable market pricing)
5. Apply realistic conversion rate per tier (informed by sales pipeline data or industry benchmarks)
6. Stress-test with capacity constraint (can the team actually service this many customers?)
7. Sum tiers to get SOM; infer SAM by grossing up with market penetration assumption

### Penetration Rates and Unit Economics
- Start with a defensible first-year penetration rate (typically 0.1–2% of SAM for early-stage businesses)
- Model penetration S-curve for years 2–5
- Tie penetration rate to sales capacity (number of reps × activity rate × conversion rate)
- Unit economics sanity check: if CAC payback exceeds contract length, the SOM is unsustainable

### SOM Reasonableness Rules (from SKILL.md best practice)
| Business Stage | SOM as % of SAM (Years 1–3) | Justification Required |
|---------------|----------------------------|------------------------|
| Startup, no traction | 1–3% | Strong if achievable |
| Early revenue, some traction | 3–8% | Needs capacity proof |
| Established brand, new market | 8–15% | Needs competitive analysis |
| SOM >20% of SAM | >20% | Extraordinary justification required |

---

## Chapter 6 — Value-Chain and Supply-Side Approaches

### When to Use Supply-Side Sizing
Supply-side approaches size the market from the production/distribution capacity perspective rather than demand. Useful when: demand-side data is unavailable or unreliable; the market is supply-constrained; you want to cross-check demand estimates.

**Method:** Map the value chain → audit production capacity → adjust for utilisation rates, yield losses, and ramp curves → translate to revenue.

### Capacity-Based Sizing Steps
1. Map the value chain (materials, components, manufacturing, distribution, final product)
2. Build a plant-level capacity roster by region
3. Apply derating factors (construction slippage, ramp-up curves, maintenance downtime)
4. Forecast utilisation vs. demand
5. Translate shipments to revenue via ASP and learning-curve adjustments
6. Run input-output and bill-of-materials (BOM) reconciliation (identify material bottlenecks)
7. Produce scenario and sensitivity bands

**Bill of Materials (BOM) considerations:**
- Identify critical material constraints (can a single input limit production growth?)
- Apply scrap and reject rates (typically 8–10% for high-tech manufacturing)
- Cross-check supply adequacy against sourcing plans

---

## Chapter 7 — Hybrid, Triangulation, and Sanity Checks

### Three-Lens Triangulation Framework

| Lens | Orientation | Strengths | Primary Bias | Key Outputs |
|------|------------|----------|-------------|-------------|
| **Top-Down** | Macro aggregates → ratios → target | Speed; consistency across geographies | Over-generalisation; ratio stacking error | TAM range, CAGR, high-level segment splits |
| **Bottom-Up** | Unit census → adoption → economics | Granularity; actionability | Data gaps; over-precision illusion | SAM, SOM, account lists, sales targets |
| **Expert/Judgment** | Tacit knowledge → forward-looking insight | Context; disruptor early signals | Subjectivity; recency bias | Mode estimates, probability ranges |

**Framework workflow:**
1. **Parallel builds** — Start all three lenses in week 1 (they inform each other)
2. **Independent ownership** — Assign separate owners to prevent unconscious convergence
3. **First reconciliation gate** — If any estimate sits >30% from the median, trigger root-cause deep dive
4. **Driver coherence table** — Even when totals align, verify underlying drivers converge across lenses
5. **Weighted synthesis** — Convert each lens to probability distribution (P10/P50/P90); blend using reliability weights
6. **Scenario anchoring** — Blended P50 = base case; expert P10 = downside; maximum of lenses = upside
7. **Documentation** — Store reconciled driver tables and weighting logic in a "Triangulation" tab

**Guardrails:**
- Maintain orthogonality (if two lenses share the same dataset, they are not independent)
- Schedule blind initial estimates before team discussions (combat anchoring)
- Update all three lenses simultaneously when new data arrives

### Order-of-Magnitude (OOM) Checks — Heuristics

**Universal constants for quick checks:**
- World population: 8 billion
- Hours per year: 8,760
- Global GDP 2024: ~$105 trillion (1% ≈ $1 trillion)
- Standard 40-foot container: ~67 m³, ~28 pallets, 14t payload
- Standard EV battery pack: ~60 kWh
- Smartphone penetration ceiling: ~85–90% of adults in any large market

**Core heuristics:**
1. **GDP/consumption ratios** — Most mature B2C categories hover within predictable multiples of GDP per capita (packaged food ≈9% of household outlays in OECD; personal care ≈1%)
2. **Penetration ceiling rules** — Physical constraints cap uptake (passenger vehicles per licensed driver rarely exceed 1.3; smartphone penetration stalls ~85–90%)
3. **Capacity factor bounds** — Power plants cannot run above 100% capacity; electro-mechanical systems rarely average >90%
4. **"Rule of 1% of the fleet"** — Annual replacement volumes for aftermarket opportunities rarely exceed 1% of total fleet absent regulation
5. **Power-law / 80-20 signs** — Top 20% of SKUs typically deliver 80% of volume; if a model counts on bottom decile for half the revenue, revisit consumer behaviour evidence
6. **Currency basis consistency** — Cross-check euro-to-dollar conversions immediately; FX errors commonly embed in models

**10-minute OOM audit workflow:**
1. State the claim in one sentence ("The 2030 EV battery market is $244 billion")
2. Pick a dominant driver (e.g., 75 million global vehicle sales × 40% EV share × 60 kWh/vehicle × $60/kWh ≈ $108 billion — far below $244B, deeper scrutiny required)
3. Cross-reference with an alternative anchor (e.g., cobalt supply: global mined ~200kt; at 6kg/EV, 30M EVs consume the entire supply — so 50M EVs is unrealistic without substitution)

### Driver Trees and Sensitivity Stress-Testing

**Building a driver tree:**
- Decision variable (TAM/SAM/revenue) in a box at the right-hand edge
- Work leftward, decomposing into MECE drivers
- Stop branching when further splits no longer change the decision (typically 3–4 layers)
- Principles: economic causality over data convenience; segment symmetry; linked granularity (leaf-node level should match available data)

**Sensitivity testing — three escalating stages:**
1. **One-way deltas (tornado chart):** Vary each driver ±10–25% while holding others constant. Sort results largest to smallest — top 3 usually explain >70% of variance. Focus refinement here.
2. **Two-way data tables:** Pair top two drivers and step through plausible ranges to reveal non-linear interactions
3. **Monte Carlo simulation:** Assign probability distributions to top drivers (triangular, beta, log-normal); run 5,000–10,000 iterations to generate full outcome distribution (P10/P50/P90)

**Stress-test triggers:**
- Regulatory shifts: model as step-changes, not smooth trends
- Supply constraints: cap volume drivers when input availability limits growth
- Competitive shocks: embed discrete market-share losses triggered at price thresholds

**Reading results:** A tornado chart showing 80% of variance tied to one driver reframes the story — the market question is really a bet on that specific variable. Communicate this insight alongside the charts; numbers alone rarely persuade.

**Common failure modes:**
- Too many drivers (limit tornado charts to 12 bars max)
- Uniform distributions for everything (use asymmetric shapes: beta for penetration ceilings; log-normal for commodity prices)
- Unlinked scenario toggles that permit economically impossible worlds

---

## Chapter 8 — Advanced Analytical Techniques

### Scenario Planning
- Use scenario planning when a single point forecast is misleading due to high strategic uncertainty
- Define 3–4 scenarios along two key uncertainties (not all variables)
- Each scenario must be internally consistent — link regulatory assumptions, technology assumptions, and competitive assumptions
- Quantify probability of each scenario; present P50 as base and range for investment decisions

### Monte Carlo Simulations
- Input distributions for key drivers (triangular distributions: min-mode-max from expert interviews)
- Run ≥5,000 iterations
- Report P10/P50/P90 — not just mean
- Use to stress-test whether investment thesis survives downside scenarios

### Geospatial / Zip-Code-Level Opportunity Mapping
Useful for businesses with physical presence constraints (retail, distribution, last-mile services). Match demographic and economic data to geographic units. Prioritise expansion locations by market density score.

### Adoption-Curve and Diffusion Models
**Rogers' Diffusion of Innovations — adoption segments:**
| Segment | % of Market | Behaviour |
|---------|------------|----------|
| Innovators | 2.5% | Risk-tolerant; accept imperfect early products |
| Early Adopters | 13.5% | Opinion leaders; need clear value story |
| Early Majority | 34% | Pragmatic; need social proof and reduced risk |
| Late Majority | 34% | Sceptical; price-sensitive; need mainstream adoption |
| Laggards | 16% | Tradition-bound; adopt last |

**Implication for market sizing:** SOM typically confined to Innovators + Early Adopters initially (16% of SAM maximum without crossing the "chasm"). Year-3–5 targets can include Early Majority only if clear crossing strategy exists.

**Matching S-curve analogs:** Match on cost-to-income ratios and regulatory context before importing curve parameters from analogous markets.

---

## Chapter 9 — Sizing Emerging and Unstructured Markets

### Framework for Markets with Undefined Value Chains
When traditional data is unavailable:
1. Define the job-to-be-done (what customer problem does this market solve?)
2. Map incumbent solutions (the "good enough" alternatives customers currently use)
3. Estimate incumbent market size (this becomes the SOM displacement target)
4. Model substitution rate (what fraction switches, at what pace?)
5. Add net-new demand enabled by the new solution

### Regulatory and Technology-Trigger Considerations
- Identify the regulatory event or technology threshold that unlocks mainstream adoption
- Size the market conditional on the trigger occurring (scenario-weighted)
- Track trigger probability explicitly; update quarterly as leading indicators emerge

**Uganda/East Africa emerging market considerations:**
- Data scarcity is common — apply proxy indicator frameworks extensively
- Mobile money transaction data (MTN MoMo, Airtel Money) is an excellent proxy for financial market sizing
- UBOS household surveys (UNHS 2019/20) provide income quintile and expenditure data for consumer markets
- Agricultural markets: use MAAIF/UBOS Agricultural Census 2022 for crop production volumes; convert to market value using farm-gate price data
- Construction/property: KCCA building permits + population growth rate + housing deficit estimate
- Informal sector adjustment: typically add 25–40% to formal sector estimates for Uganda economy-wide (URA estimates 60%+ of GDP in informal sector)

---

## Chapter 11 — Communicating Market Sizing Insights

### Visualisation Standards
- **Bar charts** for segment comparisons (use sorted order; largest segment left or at top)
- **Waterfall charts** for TAM → SAM → SOM funnel (show exactly where each filter reduces the market)
- **Area charts or line charts** for CAGR and market growth over time
- **Tornado charts** for sensitivity analysis
- **Stacked bar charts** for market share comparisons across time periods
- Avoid 3D charts (distort perceptions); always label data points; declare currency, year, and price basis on every chart

### Executive-Level Storylining (Pyramid Principle)
Lead with the conclusion (SCQA structure — see `01-executive-summary/references/pyramid-principle.md`):
- **Situation:** "The [market] is a $X billion opportunity growing at Y% per annum"
- **Complication:** "However, current approaches/players do not adequately serve [specific segment]"
- **Question:** "How large is the addressable gap, and can we capture it?"
- **Answer:** "Our analysis shows a $Z million SOM achievable by Year 3, representing Z% of SAM"

**Three questions an investor will ask:**
1. Is this a real and growing market? (TAM with CAGR, sources)
2. Can you credibly compete for a meaningful slice? (SAM filters + SOM justification)
3. What assumptions would have to be true for this to work? (sensitivity and scenario analysis)

### Embedding Market Sizing into Business Plans and Investment Cases
- TAM/SAM/SOM should appear in Section 04 (Market Analysis) with full methodology
- SOM should feed directly into the financial model's revenue assumptions (Section 10)
- Sensitivity of SOM to key assumptions should be visible (at minimum: upside, base, downside cases)
- Every TAM/SAM figure should cite a source — uncited figures invite investor scepticism
- Use dual methodology (top-down + bottom-up) as required by most sophisticated investors; reconcile the two estimates

---

## Chapter 12 — Toolkits and Templates

### Market Sizing Readiness Self-Assessment Checklist
- Is the market boundary defined with explicit in/out criteria?
- Are TAM, SAM, and SOM clearly distinguished with appropriate denominators declared?
- Have at least two independent sizing methodologies been applied?
- Are all key assumptions documented in an Assumption Register with owners?
- Has at least one red-team challenge been conducted and responses logged?
- Are data sources cited with 4T quality scores?
- Is the model's sensitivity to top 3 drivers quantified?
- Are scenarios (pessimistic/base/optimistic) linked to specific driver assumptions?
- Is the output in a format decision-makers can act on (chart + narrative + action recommendation)?

---

## Application to Uganda/East Africa Business Plans

### Uganda Market Sizing Reference Numbers (Use as Anchors)
- Total population: 45.9 million (NPHC 2024); 54% urban growth projection by 2030
- Working-age population: 23.5 million; formal wage employment: ~2.5–3 million
- Kampala population: 1.797 million (GKMA ~3.5 million)
- Mobile money active accounts: ~20 million (BoU, 2024)
- Internet penetration: ~26% (UCC, 2024)
- Banked population: ~57% (financial inclusion definition, FinScope 2023)
- Annual new market entrants (labour force): 1.1–1.2 million youth per year

### Common Uganda Market Sizing Approaches
| Market Type | Recommended Approach | Primary Data Source |
|-------------|---------------------|---------------------|
| Consumer FMCG | Top-down from household expenditure | UBOS UNHS 2019/20; UNPHC 2024 |
| B2B services | Bottom-up from target company census | UIA business directory; PSFU database |
| Agricultural inputs | Supply-side from crop production data | UBOS Agricultural Census 2022; MAAIF |
| Financial services | Proxy from mobile money penetration | BoU Annual Financial Stability Report |
| Healthcare | Top-down from disease burden + OOP spend | MOH; UBOS Health Survey |
| Real estate | Bottom-up from housing deficit estimates | UN-Habitat Uganda; KCCA building permits |

### TAM/SAM/SOM Template — Uganda Consumer Business
```
TAM: Total Uganda population spending on [category] = Population × Penetration rate × Average annual spend
     Example: 45.9M × 35% penetration × UGX 120,000/year = UGX 1.93 trillion

SAM: Urban Uganda + C2/C1 income bands with disposable income for [category]
     Example: Urban population 12M × 40% in accessible income band × UGX 150,000 = UGX 720B

SOM (Year 1–3): Reachable via planned distribution × realistic conversion rate × average order value
     Example: 50,000 reachable customers × 8% conversion × UGX 85,000 ACV = UGX 340M ARR
```

*All figures should use UGX at UGX 3,700/$1 conservative planning rate (see CLAUDE.md)*

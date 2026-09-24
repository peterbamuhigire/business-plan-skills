---
name: market-sizing-methodology
description: Task reference for sizing a market in a business plan - TAM, SAM and SOM definitions, market-boundary rules, common failure modes, top-down, bottom-up and supply-side methods, data collection and proxies, three-lens triangulation, driver trees, sensitivity and scenario testing, order-of-magnitude checks, emerging-market sizing, and how to present the result to investors.
type: reference
---

# Market Sizing Method for Business Plans

Use this reference to size a market defensibly and present it. Sizing translates vision into evidence: it tells investors whether the prize justifies the capital, management where to prioritise, and founders whether the business can reach meaningful scale. Three contexts demand rigour: investment or acquisition, strategic planning (allocating research, sales and marketing effort) and operational planning (revenue potential and targets). The structure below is the engine's own; concepts such as TAM, SAM, SOM, driver trees, tornado charts, Monte Carlo simulation, S-curves and the Pyramid Principle are standard practice. See also estimation-trees-and-sanity-checks.md in this folder.

All local statistics quoted in section 12 are anchors that must be re-verified with a dated source.

## 1. Definitions

A market is the set of transactions in which a defined customer group buys a defined solution for a defined need. Three guardrails: product or service scope (what is in versus adjacent), customer scope (who buys or could buy), substitutability (if buyers can weigh two offers against the same need, both belong in the market).

| Layer | Definition | Question | Use |
|---|---|---|---|
| TAM (total addressable market) | Revenue if every potential buyer adopted at today's average economics: no competition, perfect penetration | How large is the theoretical ceiling? | Benchmark ambition |
| SAM (serviceable available market) | TAM filtered by what your model can serve: products you can make, places you can reach, segments you can credibly serve | What could we structurally compete for? | Entry priority, resource allocation |
| SOM (serviceable obtainable market) | Realistic capture of SAM within the planning horizon given competition and capacity | What can we actually win? | Revenue targets, investor forecasts |
| Share | Current position against TAM, SAM or SOM (always name the denominator) | Where are we today? | Benchmarking |

Funnel: TAM, then SAM, then SOM, then share. State the hierarchy: a 20 percent share of SAM may be only 5 percent of TAM; naming the denominator prevents flattering comparisons.
TAM tips: say whether it is value (currency spent) or volume (units, tonnes); time-stamp it (for example "TAM 2025F"); disclose exchange-rate assumptions when combining geographies.
SAM scoping: regulatory limits (licences, tariffs), channel reach (direct sales versus distributors), technology readiness.
SOM quantification: bottom-up capacity or sales-coverage modelling, win-loss rates applied to the SAM pipeline, sensitivity to price elasticity and competitor moves.

## 2. Setting the market boundary

The boundary is the largest swing factor: too wide inflates the prize, too narrow misses adjacencies. Rules:
1. Begin with the strategic decision the sizing informs.
2. Anchor on customer needs, not technology (define "delivery of small parcels within two hours", not "drone logistics").
3. Apply the substitutability test from the buyer's point of view.
4. Segment only where economics differ materially (demand drivers, price elasticity or regulation).
5. Respect geographic detail where growth curves differ; aggregate homogeneous regions.
6. Match the boundary to available data (trade codes, panels); probe sources early.
7. Stress-test for scope creep and omission with a regular ring-fence review (what is explicitly in and out, plus blind spots).
8. Keep it dynamic: list triggers (regulatory decisions, cost milestones, adoption inflections) that would force a redraw.

Diagnostic: can the market be stated in one sentence with need, customer and solution? Has substitutability been tested from the end-user's view? Does each segment move the valuation if its growth diverges? Are there two independent sources per segment? Are exclusions and reasons documented? What would make the boundary obsolete?

## 3. Twelve failure modes

| Failure | Description | Mitigation |
|---|---|---|
| Boundary bloat | Generous definitions inflate the prize | Regular ring-fence review; a devil's advocate |
| Double counting | Overlapping datasets counted twice | Mutually exclusive hierarchy; pivot check |
| Single-source dependence | One syndicated report | Triangulate at least three independent lenses |
| Price-basis mismatch | Wholesale, retail or pre-rebate mixed | One price basis at ingestion |
| Extrapolating history | Past growth projected, ignoring S-curves | Driver-based forecasts, scenarios |
| Static elasticity | Constant price sensitivity | Elasticity curves by segment, re-estimated as penetration rises |
| Demand-supply confusion | Capacity read as demand | Cross-check with purchase orders or surveys |
| Adoption-friction blindness | Straight line from awareness to purchase | Build adoption lags; test with journey interviews |
| Primary-research bias | Surveys skew to enthusiasts; experts favour incumbents | Combine usage data, surveys and diverse experts including sceptics |
| Currency and inflation errors | Nominal and real mixed; FX frozen | Constant-currency real terms; state FX and inflation assumptions |
| Snapshot trap | One-year TAM hides trends | Show five years of history and five forward |
| Cannibalisation neglect | New product displaces legacy sales | Model new-category growth and legacy decline together |

## 4. Scoping the exercise

Kick-off questions: what decision will this inform; by when; what exposure and irreversibility attach; what size of error changes the choice (a venture screening decision tolerates a wide band, a utility infrastructure commitment a narrow one); which hypotheses carry the most uncertainty and impact; which three to five drivers anchor the model; what precision, currency and time frame satisfy stakeholders; who holds a veto and are they involved. Plot the decision on exposure versus irreversibility to set analytical depth.

Success criteria: analytical rigour (audit trail), stakeholder buy-in (assumption register initialled), timeliness (before the decision date), actionability (outputs feed the valuation or capital model without reformatting).

Granularity: use the minimum viable detail. Segment or localise only when a sub-slice changes the aggregate by about 10 percent or more, or grows at double or half the mean. Segment by how buyers choose, not how data providers classify. Cluster geographies that share regulation or culture and peel off outliers. Convert history to real terms in a common base year and apply purchasing-power adjustment where income differs greatly. Revisit granularity when a region passes about 5 percent of demand or a sub-segment's growth outpaces its parent for two years.

Assumption register: a workshop capturing each explicit assumption with source, owner and last validation date; classify by impact and certainty (high-impact, high-uncertainty items become workstreams); assign accountability (for example finance for the discount rate, strategy for growth, legal for regulatory timing); appoint outsiders as a red team and log how each challenge was answered.

Hypothesis and driver tree: start from a falsifiable statement, decompose into first-principle levers (for example addressable vehicles x charging events x energy per event x price), stop branching when splits stop changing the decision, and turn high-impact uncertain nodes into time-boxed workstreams with owners, checkpoints, independent go or no-go gates and exit criteria (for example an agreed error band at a stated confidence).

## 5. Data collection

### Secondary sources
Three families: industry reports (scale, segmentation, growth estimates); government and multilateral data (statistical offices, trade databases, food and agriculture bodies, central-bank surveys: free and longitudinal but often 12 to 24 months behind); trade associations (shipment data, may miss disruptors).
Four-T screen for every source: Transparency (definitions and method disclosed), Timeliness (in fast sectors, data over a year old is unreliable), Taxonomy (categories match your boundary), Triangulation (an independent source corroborates).
Normalise to constant currency, consistent units and price levels; keep conversion factors in the workbook. Keep a source log (publication, page or table, location, transformations) linked to cells.
Creative sources for scarce categories: satellite imagery, scraped product listings, patent databases, shipping-manifest analytics.
Local sources to screen: national statistics office abstracts, household surveys and census; central-bank reports; revenue-authority reports; investment authority and private-sector foundation reports; regional community statistics; development-bank outlooks; international finance and development institution country studies.

### Primary research
- Expert interviews: build a knowledge grid of unknowns against archetypes able to answer (former regulators, supply-chain heads, procurement leads); include incumbents, disruptors, service providers and adjacent sectors; offer ranges ("under 10 percent, 10 to 30, over 30") to draw out numbers; offer anonymity; corroborate each insight with two other views; log timestamps against the driver-tree node.
- Surveys: define the population; size the sample from the precision needed (about 380 responses gives roughly plus or minus 5 points at 95 percent confidence in a large population); one construct per question; ask behaviour (last period's spend) rather than intent; anchored scales; pre-test on about ten respondents; weight to population proportions; remove speeders, straight-liners and improbable outliers.
- Mystery shopping where price transparency is low: simulate buyer personas and record the full discount ladder; feed dispersion into the pricing module.

### Proxy indicators

| Family | Examples | Best for |
|---|---|---|
| Digital exhaust | Search volumes, app downloads, social mentions | Consumer interest |
| Factor inputs | Import and export volumes, raw materials, component order books | Hardware-centred industries |
| Regulatory artefacts | Licence applications, environmental filings, subsidy lists | Markets with a 12 to 24-month policy lead |
| Labour signals | Job postings, employee counts | Software and frontier technology |
| Capital flows | Funding rounds, bond issues, equipment leasing | Pre-revenue signals |

Proxy procedure: define the latent variable (a driver-tree node); hypothesise candidate signals; back-test correlation (an R-squared above about 0.6 at useful lags justifies use); calibrate scaling to market units; stress-test for outliers, seasonality and structural breaks. Separate leading from lagging proxies and pair quantitative analogues with a qualitative sanity check.
Analogue benchmarks: technology adoption S-curves, cost-performance learning curves (cost falls with cumulative production), channel evolution across categories, business-model migration.

### Reliability and triangulation
Score sources 1 to 5 on transparency, timeliness, taxonomy fit, triangulability and track record; inputs scoring 3 or less need triangulation or replacement. Convert reliability to weights (inverse-variance or proportional) and document the formula; do not pick a source unilaterally unless it leads by at least two points. Triangulate by orthogonality: sources differ by method (supply versus demand), data type or vantage point; if two lenses share a dataset they are not independent. Gap management: log nodes lacking data; rank by sensitivity x size share; fill high-materiality gaps first; for irreducible uncertainty use a pessimistic floor (historical precedent), reference case (expert consensus) and optimistic ceiling (technology-learning extrapolation).

## 6. Top-down sizing

Start with a macro or industry figure and apply filters. Strengths: vetted data, speed, early signal. Use when reliable high-level statistics exist, the boundary nests inside statistical categories and about plus or minus 20 percent accuracy suffices for a first gate. Cautions: fast technology change (statistics lag), fragmented or informal sectors (under-registration), more than about four sequential filters (prefer bottom-up).
Components: base metric closely correlated with the target market; evidence-based filter ratios, each triangulated; translation to value (units x average selling price); time-series extension (growth drivers).
Steps: (1) choose the base, verified in two sources; (2) geographic filter; (3) segment filter; (4) product specificity filter; (5) usage or penetration filter; (6) multiply by price for revenue TAM; (7) apply SAM and SOM filters; (8) order-of-magnitude check.
Data gaps: proxies for missing ratios; make a dominant ratio a scenario variable; document assumptions, since investors scrutinise the filters, not the base.

## 7. Bottom-up sizing

Count buyers, multiply by revenue per buyer, adjust for adoption. More granular and defensible, needs more data. Best when the customer population can be enumerated, sales capacity constrains the market or unit economics are known from early customers.
Formula: addressable customers x win rate x average contract or revenue value = SOM.
Steps: (1) define the population by ideal-customer criteria; (2) estimate size from census, trade directories, research, professional networks or web scraping; (3) segment by tier with separate conversion rates; (4) estimate revenue per tier from early customers or comparable prices; (5) apply realistic conversion from pipeline data or benchmarks; (6) stress-test against capacity to serve; (7) sum tiers to SOM and gross up to SAM with a penetration assumption.
Penetration: use a defensible first-year rate (often a small fraction of SAM to low single digits for early-stage firms), an S-curve for years two to five, tie it to sales capacity (reps x activity x conversion), and check unit economics (if payback exceeds contract length, SOM is unsustainable).

SOM reasonableness (rule-of-thumb, years one to three):

| Stage | SOM as share of SAM | Justification |
|---|---|---|
| Start-up, no traction | About 1 to 3 percent | Strong support if reached |
| Early revenue, some traction | About 3 to 8 percent | Capacity proof |
| Established brand, new market | About 8 to 15 percent | Competitive analysis |
| Above 20 percent | Extraordinary claim | Exceptional justification |

## 8. Supply-side sizing

Use when demand data is unreliable or the market is supply-constrained, or to cross-check demand. Steps: map the value chain; build a plant-level capacity roster; apply derating (construction slippage, ramp-up, downtime); forecast utilisation against demand; translate shipments to revenue with price and learning-curve adjustments; reconcile with input-output and bills of materials to find material bottlenecks (can a single input cap growth?); apply scrap and reject rates (high-tech manufacturing often runs at several percent to about ten percent; verify); produce scenario bands.

## 9. Hybrid triangulation and sanity checks

| Lens | Orientation | Strength | Bias | Output |
|---|---|---|---|---|
| Top-down | Aggregates, ratios | Speed, cross-geography consistency | Over-generalisation, ratio stacking | TAM range, growth, segment splits |
| Bottom-up | Unit census, adoption | Granularity, actionability | Data gaps, false precision | SAM, SOM, account lists, targets |
| Expert judgement | Tacit knowledge | Context, early signals | Subjectivity, recency | Modal estimates, probability ranges |

Workflow: (1) start all three in week one; (2) separate owners; (3) if any estimate sits more than about 30 percent from the median, find the root cause; (4) check driver coherence, not just totals; (5) convert each lens to P10, P50 and P90 and blend by reliability weights; (6) anchor scenarios (blended P50 base, expert P10 downside, the maximum of lenses as upside); (7) record reconciled drivers and weights in a triangulation tab. Guardrails: keep independence, take blind initial estimates before discussion (anchoring), update all lenses together.

Order-of-magnitude checks:
- Constants: world population, hours per year (8,760), global output (1 percent is roughly a trillion currency units at current scale; verify), container capacity, typical battery-pack size, smartphone penetration ceilings.
- Heuristics: consumption ratios to income per head (share of household outlays by category); penetration ceilings (vehicles per licensed driver, smartphones per adult); capacity factors below 100 percent; replacement volumes rarely above about 1 percent of the installed base absent regulation; the 80-20 pattern (if half of revenue depends on the bottom decile of products, re-examine behaviour evidence); consistent currency basis.
- Ten-minute audit: state the claim in a sentence; rebuild it from one dominant driver; cross-check with an independent anchor (for example a scarce raw-material supply that limits the claimed volume). If the two differ by a large multiple, investigate.

## 10. Driver trees, sensitivity and scenarios

Driver tree: decision variable (TAM, SAM or revenue) at the right; decompose leftwards into mutually exclusive, collectively exhaustive drivers; stop when splits no longer change the decision (usually three to four layers). Principles: economic causality over data convenience, segment symmetry, leaf granularity matching data.

Sensitivity in three stages:
1. One-way deltas (tornado chart): vary each driver about 10 to 25 percent; the top three usually explain most variance.
2. Two-way data tables for the top two drivers to reveal interactions.
3. Monte Carlo simulation: probability distributions (triangular from expert min, mode and max; beta for ceilings; log-normal for commodity prices); at least several thousand runs; report P10, P50 and P90, not just the mean.
Stress triggers: regulatory shifts as step changes; supply constraints capping volume; competitor shocks at price thresholds. If one driver explains most variance, the market question is really a bet on it; say so. Failure modes: too many drivers (about a dozen bars at most), uniform distributions for everything, unlinked scenario toggles that permit impossible worlds.

Scenario planning: use when a point forecast misleads; define three or four scenarios along two key uncertainties, internally consistent, with probabilities; present P50 as base with the range.
Geospatial mapping: for physical presence businesses (retail, distribution, last mile), match demographic and economic data to geographic units and rank expansion sites by market density.
Adoption curve (Rogers): innovators about 2.5 percent, early adopters about 13.5, early majority about 34, late majority about 34, laggards about 16. Confine early SOM to innovators plus early adopters (about 16 percent of SAM at most) unless there is a credible strategy for crossing to the majority. Match S-curve analogues on cost-to-income ratios and regulatory context before importing parameters.

## 11. Emerging or unstructured markets

1. Define the job to be done.
2. Map incumbent "good enough" solutions.
3. Estimate the incumbent market (the displacement target).
4. Model the substitution rate and pace.
5. Add net-new demand the solution enables.
Identify the regulatory event or technology threshold that unlocks mainstream adoption, size the market conditional on it (scenario-weighted), track trigger probability and update quarterly.

## 12. Local sizing in East Africa

- Data scarcity is common; use proxies extensively.
- Mobile-money transaction data is an excellent proxy for financial-market size.
- Household surveys give income-quintile and expenditure data for consumer markets; agricultural censuses give production volumes to convert to value with farm-gate prices; building permits plus population growth plus a housing-deficit estimate suit property.
- Informal-sector adjustment: informal activity is a large share of the economy; adding a sizeable uplift (an older rule of thumb is roughly a quarter to two fifths) to formal-sector estimates is common; verify with current national statistics.
- Anchors to refresh before use (national population and census, urban share, working-age population, capital-city population, mobile-money accounts, internet penetration, banked share, annual labour-force entrants): take from the latest census, regulator and financial-inclusion survey and date them.

| Market | Approach | Primary data |
|---|---|---|
| Consumer goods | Top-down from household expenditure | Household survey, census |
| Business services | Bottom-up from a company census | Investment authority and private-sector directories |
| Agricultural inputs | Supply-side from crop production | Agricultural census, ministry data |
| Financial services | Proxy from mobile-money penetration | Central-bank stability report |
| Healthcare | Disease burden and out-of-pocket spend | Health ministry, health survey |
| Real estate | Bottom-up from housing deficit | Housing agency, permits |

Consumer template (illustrative structure; all inputs to be sourced):
- TAM = population x penetration x average annual spend.
- SAM = urban or accessible-income population x share in the accessible band x spend.
- SOM (years one to three) = reachable customers x conversion rate x average order value.
Use a conservative, stated exchange rate for currency conversion (see the engine's planning-rate convention in its controller file) and tax treatment via the Chwezi finance engine.

## 13. Communicating the result

- Charts: sorted bars for segments; waterfall for the TAM to SAM to SOM funnel (show where each filter cuts); line or area charts for growth; tornado for sensitivity; stacked bars for share over time. Avoid 3D; label points; state currency, year and price basis on every chart.
- Storyline (Pyramid Principle by Minto; situation, complication, question, answer; see 01-executive-summary/references/pyramid-principle.md): situation (the market size and growth), complication (current players under-serve a segment), question (how large is the gap and can we capture it), answer (the SOM by year three as a share of SAM).
- Investor questions: is the market real and growing (TAM, growth, sources)? Can you credibly compete for a meaningful slice (SAM filters, SOM justification)? What must be true for it to work (sensitivity, scenarios)?
- In the plan: TAM, SAM and SOM in the market-analysis section with method; SOM feeding the financial model's revenue assumptions; upside, base and downside visible; every figure sourced; dual method (top-down and bottom-up) reconciled.

## 14. Readiness checklist

Boundary with explicit in and out criteria; TAM, SAM and SOM distinguished with denominators; at least two independent methods; assumption register with owners; at least one red-team challenge logged; sources cited with four-T scores; sensitivity to the top three drivers quantified; scenarios linked to driver assumptions; output in a decision-ready form (chart, narrative, recommended action).

Sources consulted: Umbrex Consulting, Market Sizing Playbook (2025); Rogers, Diffusion of Innovations; Minto, The Pyramid Principle; general consulting and statistics practice.

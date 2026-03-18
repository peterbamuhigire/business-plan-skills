# Pillar 5 — Customer and Market Analytics
**Score: 6.0 / 10**

This pillar has the widest gap relative to McKinsey/Bain standards. The qualitative customer frameworks are strong — personas, AARRR, Kotler, CLV:CAC benchmark. But the quantitative analytics that underpin revenue confidence — RFM segmentation, cohort retention curves, churn modelling, price elasticity — are essentially absent. This matters most for services, subscription, and retail businesses where these are the primary proof of revenue quality.

---

## 5.1 What Is Present (Positives)

| Component | Location | Assessment |
|-----------|----------|------------|
| Customer archetype / persona framework | 05-target-market | Strong — Day-in-the-Life, Pain Points, Problem Recognition Scale |
| CLV:CAC >3:1 benchmark | 05-target-market | Benchmark correct; not dynamically modelled |
| TAM/SAM/SOM dual methodology | 04-market-analysis | Both top-down and bottom-up; explicitly required |
| Kotler generational targeting | 05-target-market | Gen Z/Millennial/Gen X/Boomer profiles for EA |
| Uganda Consumer Demographics (WB 2025) | 05-target-market | Income quintiles, NEET proportions, literacy gaps — excellent secondary data |
| AARRR funnel (Acquisition-Activation-Retention-Referral-Revenue) | 07-marketing-sales-strategy | Full funnel with Uganda channel examples |
| Customer discovery interview methodology | meta-market-validation | Blank & Dorf, Alam empathy-based interviews |
| Kaza Underdog Principles | 05-target-market | Positioning/Proximity/Purpose for challenger brands |
| Decision-Making Unit mapping | 05-target-market | Described structurally |
| Social protection recipients as emerging consumers | Uganda Consumer Demographics | Genuinely innovative market angle for EA |

---

## 5.2 Critical Analytics Gaps

### Gap 1 — RFM Customer Segmentation (HIGH IMPACT for Retail/Services/Hospitality)

**What it is:** Recency/Frequency/Monetary analysis — classifying existing or projected customers by how recently they bought, how often they buy, and how much they spend. Produces actionable segments: Champions, Loyal Customers, At-Risk Customers, Lost Customers.

**Why it matters:** Any business with repeat customers (restaurant, retail, services, subscription) needs RFM to demonstrate that revenue is not evenly distributed. Typically: top 20% of customers generate 80% of revenue. Investors and lenders want to see this known and managed.

**Current state:** The 80/20 rule is cited in `meta-market-validation` (Rasiel/McKinsey). But no operational RFM framework exists to apply it to customer segments in the plan.

**Recommendation:** Add RFM framework to `05-target-market/SKILL.md` and create `05-target-market/references/customer-analytics.md` covering:
- RFM scoring methodology (1-5 scale per dimension)
- RFM segment definitions (Champions, Loyal, Promising, At-Risk, Lost)
- Revenue concentration analysis (Pareto: top customer revenue share)
- Practical application for new businesses (use projected rather than actual customer data)
- Uganda/EA examples: mobile money transaction frequency as Recency/Frequency proxy

### Gap 2 — Cohort Retention Curves (HIGH IMPACT for Subscription/Services/B2B)

**What it is:** Plotting the revenue retention of each monthly cohort of customers over time. Shows whether the business is getting better or worse at retaining customers.

**Why it matters:** Aggregate revenue growth can mask deteriorating unit economics (new customers acquired faster than old ones churn). Sophisticated investors always ask for cohort data. Without it, LTV:CAC calculations are unreliable.

**Current state:** LTV:CAC >3:1 benchmark cited. No cohort modelling framework.

**Recommendation:** Add to `10-financial-projections/SKILL.md`:
- Cohort retention table structure (Month 0 = 100%, Month 1 = X%, Month 6 = Y%, Month 12 = Z%)
- Industry benchmark retention rates by business type:
  - SaaS/subscription: Month 12 retention typically 60-85%
  - Retail: Monthly repurchase 20-40%
  - Professional services: Annual retention 70-85%
  - Food service: Weekly retention 15-30% (regular customers)
- LTV calculation from cohort curves: Sum of monthly revenue × retention rates discounted at cost of capital
- Payback period: Months until cumulative cohort revenue exceeds CAC

### Gap 3 — Churn Modelling (HIGH IMPACT for any Recurring Revenue Business)

**What it is:** Monthly/annual customer churn rate — the percentage of active customers who stop buying in each period. Directly determines LTV.

**Why it matters:** A 5% monthly churn gives LTV of 20 months × ARPU. A 10% monthly churn gives LTV of 10 months. This is the difference between a healthy and a failing subscription business. Without modelling it explicitly, financial projections are guesswork.

**Current state:** Entirely absent as a methodology. LTV:CAC benchmark cited without methodology for calculating LTV from churn data.

**Recommendation:** Add to `10-financial-projections/references/working-capital-modelling.md` (or create `cohort-unit-economics.md`):
- Monthly vs. annual churn calculation
- Churn rate impact on LTV (table: monthly churn 2%/5%/10%/20% → LTV multipliers)
- Leading indicators of churn (NPS, usage frequency, support tickets)
- Churn reduction levers for EA context (WhatsApp re-engagement, mobile money loyalty, personal follow-up)
- Uganda baseline churn benchmarks by sector (estimate from analogues where available)

### Gap 4 — Price Elasticity Modelling (MEDIUM IMPACT)

**What it is:** How much does demand change when price changes? Price elasticity = % change in quantity / % change in price.

**Why it matters:** Pricing strategy sections (07-marketing-sales-strategy, 05-target-market) recommend price positioning but do not quantify the revenue risk of pricing too high or the margin sacrifice of pricing too low.

**Current state:** Value-based pricing 5-step framework (Kaza) exists. No quantitative elasticity framework.

**Recommendation:** Add to `05-target-market/SKILL.md`:
1. **Van Westendorp Price Sensitivity Meter** — 4-question survey technique to find acceptable price range. Questions: (a) At what price is this too cheap (quality concern)? (b) Too expensive (won't buy)? (c) Expensive but would consider? (d) Cheap bargain? Intersection of (a-b) curves gives acceptable range.
2. **Conjoint-lite approach** for EA context — present 3 price/feature combinations to 10-20 potential customers; count preferences. Simpler than full conjoint but actionable.
3. **Competitive price positioning matrix** — place your price vs. competitors on a 2×2 (price/quality) and assess whitespace.
4. **Price-volume trade-off table** — at each price point, what unit volume is needed to achieve the same revenue? Helps identify whether volume assumptions are realistic.

### Gap 5 — Customer Acquisition Cost by Channel (MEDIUM IMPACT)

**What it is:** The actual cost to acquire one customer through each marketing channel — digital ads, referrals, sales team, events, etc.

**Current state:** CAC benchmark (>3:1 CLV:CAC) exists. AARRR funnel exists. But there is no framework for calculating channel-level CAC, which determines where marketing budget should be allocated.

**Recommendation:** Add to `07-marketing-sales-strategy/SKILL.md`:
- CAC formula by channel: (Channel spend in period) ÷ (New customers from that channel in period)
- Channel mix optimisation: allocate budget to channels with lowest CAC until diminishing returns
- Uganda channel CAC benchmarks (estimate):
  - WhatsApp Business (organic): UGX 0 CAC, high retention
  - Facebook ads (Uganda SME): UGX 5,000–25,000 per lead; conversion rate 5-15%
  - Referral programmes: typically lowest CAC; Uganda social trust networks highly effective
  - Sales team (B2B): UGX 50,000–500,000+ per customer; long cycle
  - Radio advertising: high reach, low CAC per impression, low conversion trackability
- Payback period by channel: CAC ÷ Monthly ARPU = months to recover acquisition cost

### Gap 6 — Net Promoter Score Framework (LOW-MEDIUM IMPACT)

**What it is:** Single-question survey (0-10 scale: "How likely are you to recommend us?"). Promoters (9-10) minus Detractors (0-6) = NPS. Industry benchmarks: NPS >50 excellent; NPS 30-50 good; NPS <0 alarming.

**Why it matters:** Every Bain revenue growth study uses NPS as the primary customer advocacy metric. It is a leading indicator of growth (high NPS → organic referrals → lower CAC). Investors from Bain Capital and similar firms specifically ask for NPS data.

**Current state:** Not present. Referral in AARRR is conceptually related but NPS as a quantified measurement is absent.

**Recommendation:** Add NPS to `05-target-market/SKILL.md` as a tracking metric:
- Measurement protocol (how to administer a clean NPS survey)
- NPS benchmarks by EA industry sector (food service, retail, professional services, education)
- NPS → Revenue linkage model (Bain research: NPS leaders grow 2× faster than industry average)
- For new businesses: target NPS of ≥40 in Year 1 as investor-grade signal

---

## 5.3 Market Sizing Rigour

### Current Standard (Strong)
The TAM/SAM/SOM dual methodology is correctly specified — both top-down (start from total market, apply filters) and bottom-up (build from unit economics). This is the McKinsey standard.

### Enhancement: Explicitly State Confidence Level

McKinsey analysts always attach confidence levels to market size estimates:
- **TAM:** Usually high confidence (based on official statistics)
- **SAM:** Medium confidence (requires geographic/demographic filters)
- **SOM:** Low confidence (depends on unproven competitive position)

**Recommendation:** Add to `04-market-analysis/SKILL.md` a required statement:
> "State the confidence level (High/Medium/Low) and the primary assumption driving each level of the market funnel. Flag where primary research is needed to validate the assumption."

### Enhancement: Market Penetration Rate Reality Check

A common error in EA business plans: SOM implies a market penetration rate that is unrealistic in Years 1-3.

**Example:** TAM = UGX 50B, SOM = UGX 2.5B (5% penetration). If the business has zero brand recognition and one sales person, 5% penetration in Year 1 is implausible regardless of how the market is sized.

**Recommendation:** Add a Market Penetration Sanity Check to `04-market-analysis/SKILL.md`:
- State the implied penetration rate at Year 1, Year 3, Year 5 revenue projections
- Benchmark against comparable businesses in similar markets
- If Year 1 penetration >2% of SAM for a new entrant with no brand, require explicit justification

---

## 5.4 Recommended New Reference File

**`05-target-market/references/customer-analytics.md`** (create new)

Contents:
1. RFM segmentation methodology and scoring guide
2. Cohort retention table template with EA benchmarks
3. Churn rate modelling — monthly vs. annual, LTV calculation
4. Van Westendorp Price Sensitivity Meter protocol
5. NPS measurement protocol and EA industry benchmarks
6. CAC by channel — calculation and Uganda benchmark estimates
7. Customer Concentration Risk analysis (revenue % from top 5 customers)
8. Customer lifetime stages (new → active → loyal → champion → at-risk → churned)

---
name: financial-projections
description: Generate the financial projections section with income statement, cash flow statement, balance sheet, break-even analysis, key assumptions, and financial ratios. The most scrutinised section by investors and lenders. Based on Rogoff's bankability standards.
---

# Financial Projections Skill

Generate rigorous, transparent financial projections that withstand investor scrutiny. This is where bankability is won or lost.

## What to Generate

### Required Financial Statements (3-5 year projections)

1. **Income statement (P&L)** — Revenue, COGS, gross margin, operating expenses, net income
2. **Cash flow statement** — Operating, investing, and financing cash flows
3. **Balance sheet** — Assets, liabilities, equity (annual snapshots)
4. **Break-even analysis** — When the business becomes profitable
5. **Key assumptions document** — Every number must trace to an assumption

### Required Analyses

6. **Revenue model** — How revenue is generated, pricing x volume
7. **Cost structure** — Fixed vs. variable costs breakdown
8. **Unit economics** — Revenue per unit, cost per unit, contribution margin
9. **Financial ratios** — Gross margin %, net margin %, burn rate, runway
10. **Sensitivity analysis** — How projections change with key variable shifts (detailed in meta-financial-stress-test)

### Financial Projection Framework

**Year 1:** Monthly projections (12 months)
**Years 2-3:** Quarterly projections
**Years 4-5:** Annual projections

### Key Assumptions to Document

Every projection must state its assumption:

- Revenue growth rate and basis
- Customer acquisition rate and churn
- Pricing changes over time
- Cost inflation assumptions
- Hiring timeline and salary costs
- Capital expenditure schedule
- Working capital requirements
- Tax rates and obligations

### Process Costing for Operational Budgets

When projecting staffing and operational costs, use process-based costing (Page, 2015):

1. **FTE calculation**: Adjusted Annual Hours = 2,080 − Vacation − Sick − Holidays; FTE = Total Annual Process Hours ÷ Adjusted Hours
2. **People cost**: (Annual Salary × FTE) × (1 + Employee Benefit Rate)
3. **Tool cost**: Software/licence costs apportioned by FTE usage
4. **Overhead cost**: People Cost × Overhead Rate
5. **Cost per transaction**: Total Process Cost ÷ Annual Volume

For technology investments, apply the three-dimensional feasibility framework (Dennis et al., 2021):
- **Technical feasibility** — Can we build/deploy it? (familiarity, size, compatibility risks)
- **Economic feasibility** — Should we invest? (NPV, ROI, break-even analysis over 3–5 years)
- **Organisational feasibility** — Will the team adopt it? (strategic alignment, champion, user readiness)

### Budgeting Fundamentals

**The limiting budget factor** determines what gets built first (ILM):
- New/cash-constrained business → **cash budget first**
- Established business → **sales budget first** (everything else follows from revenue)
- Production-constrained → **production budget first**

**Variance analysis:** Compare actuals to budget monthly. Label variances as Favourable (F) or Adverse (A). Investigate both — adverse variances need corrective action; favourable variances may indicate short cuts or lessons to capture.

**Flexible budgets:** Separate fixed and variable costs so monthly reviews compare "what should we have spent at this actual volume" not "what did we budget at planned volume." See `references/budgeting-forecasting.md`.

### Forecast vs. Target vs. Plan

Keep these distinct in the assumptions document (Morlidge):
- **Forecast** = what you think will happen (inform decisions; update as conditions change)
- **Target** = what you want to happen (set ambition; fixed)
- **Plan** = actions to bridge target and forecast (execution roadmap)

Revenue projections contain both: treat costs as engineering estimates (forecasts), treat revenue as targets-with-a-plan. Never anchor cost assumptions to revenue targets.

**Driver-based modelling:** Identify 5–10 key drivers (transactions, customers, utilisation rate, price per unit) and derive all other line items from them. This makes assumptions explicit, enables instant scenario analysis, and prevents inconsistencies across statements.

### Revenue Model Templates

- **Product sales:** Units x Price = Revenue
- **Subscription/SaaS:** Customers x Monthly fee x (1 - Churn) = MRR
- **Service/consulting:** Billable hours x Hourly rate x Utilisation = Revenue
- **Marketplace:** GMV x Commission rate = Revenue
- **Advertising:** Impressions x CPM / 1000 = Revenue

## Generation Process

1. Ask for: business model, pricing, expected customer count, major costs, funding stage
2. Build revenue model with explicit unit economics
3. Project costs (COGS, OpEx, CapEx) month by month for year 1
4. Generate income statement, cash flow, and balance sheet
5. Calculate break-even point
6. Document every assumption
7. Compute key financial ratios
8. Flag areas requiring sensitivity analysis

## Quality Criteria (Rogoff's Bankability Standards)

- Every number traces to a documented assumption
- Revenue projections are bottom-up (not "we'll capture X% of the market")
- Cash flow is projected separately from profit (profitable companies can run out of cash)
- Break-even timeline is realistic
- Projections show a credible path to profitability
- No hockey-stick growth without clear justification
- Assumptions are conservative-to-moderate, not optimistic

### Startup-Specific Financial Metrics

For early-stage ventures, supplement traditional financial statements with startup metrics (Blank & Dorf, 2012):

- **Cash burn rate** and months of cash remaining (the master metric)
- **Customer acquisition cost (CAC)** and customer lifetime value (LTV)
- **LTV:CAC ratio** (target >3:1)
- **Conversion rates** through the sales funnel
- **Revenue growth rate** (month-over-month)

Use the **One-Minute Business Model** as a quick feasibility check: Revenue per unit − Cost per unit = Profit per unit; Target revenue ÷ Profit per unit = Units needed (Kagan, 2024). If the monthly unit target seems achievable, build the detailed projections.

When projections don't work, adjust the **Six Revenue Dials**: average order value, frequency, price point, customer type, product line, and add-on services (Kagan, 2024). See `references/startup-financial-metrics.md`.

## References

- **Budgeting and forecasting best practices**: See `references/budgeting-forecasting.md` for the budget definition and types (sales/cash/production), limiting budget factor, budgetary control and variance analysis (favourable/adverse), flexible budgets (adjusting for activity level), standard costing, performance measurement framework, financial and non-financial KPIs, benchmarking types; PLUS forecast vs. prediction vs. target vs. plan distinctions, TARAC/CARAT qualities of a good forecast, 7 symptoms of forecasting disease, rolling forecasts vs. annual budgets, driver-based modelling, demand vs. sales distinction, judgmental bias types, and a cash budget template — from ILM/Elsevier (2003), Morlidge & Player (Wiley, 2010), and Vandeput (Manning, 2023). **Read when building budget structure, variance tables, or reviewing forecasting assumptions.**
- **Process costing and feasibility analysis**: See `references/process-costing-feasibility.md` for FTE calculation formulas, three-component process costing (people/tools/overhead), cost per transaction, hard vs soft savings, three-dimensional feasibility analysis (technical/economic/organisational), NPV/ROI/break-even methodology, and cost-benefit spreadsheet structure — from Page (AMACOM, 2015) and Dennis, Wixom & Tegarden (Wiley, 2021)
- **Startup financial metrics**: See `references/startup-financial-metrics.md` for Metrics That Matter framework (3 worked examples by channel type), One-Minute Business Model, Six Revenue Dials, Freedom Number, burn rate guidelines by stage, and revenue curves by market type — from Blank & Dorf (2012) and Kagan (2024)
- **Uganda wage and cost benchmarks (2025–26)**: See `references/uganda-wage-cost-benchmarks.md` for median monthly earnings (UGX 200,000 cash; UGX 260,000 cash+in-kind), inflation rates by expenditure category, key commodity/energy price changes, household spending patterns, poverty line thresholds, and a default assumptions template (exchange rates, tax rates, NSSF, lending rates) — from UBOS (NLFS 2021, UNHS 2023/24, CPI Feb 2026, KEI Q1 2025/26). **Read this file whenever setting salary assumptions, input cost escalation rates, or building the assumptions document for Uganda financial projections.**

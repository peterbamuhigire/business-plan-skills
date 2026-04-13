---
name: financial-projections
description: Generate the financial projections section with income statement, cash flow statement, balance sheet, break-even analysis, key assumptions, and financial ratios. The most scrutinised section by investors and lenders. Based on Rogoff's bankability standards.
---

# Financial Projections Skill

## Use When

- Use when building or reviewing the core financial model for a plan or proposal.
- Use when lenders, investors, or committees need to see projected profitability, cash flow, and funding resilience.
- Use whenever a business case needs explicit assumptions and bankability logic.

## Do Not Use When

- Do not use before the business model, pricing logic, and implementation path are at least directionally clear.
- Do not use to invent precision where the assumptions are unknown.
- Do not confuse this skill with stress testing, valuation, or funding structure; those are adjacent but distinct workflows.

## Required Inputs

- Business model, pricing, customer or volume assumptions, and growth path
- Cost structure, staffing plan, implementation timing, and capex needs
- Tax, salary, inflation, and country context
- Target funder context: debt, equity, blended finance, internal planning

## Workflow

1. Identify the revenue drivers and key modelling assumptions.
2. Build Year 1 monthly and outer-year periodic projections.
3. Produce the P&L, cash flow, balance sheet, break-even, and ratio outputs.
4. Separate profit logic from cash logic and make working-capital assumptions explicit.
5. Reconcile the model with market, operations, hiring, and funding sections.
6. Prepare any handoff inputs needed for stress testing or valuation.

## Quality Bar

- Every major line item traces to an explicit assumption.
- The model is bottom-up and credible, not aspirational spreadsheet theatre.
- Cash, debt service, and funding implications are visible.
- The model can survive scrutiny from a banker or investor.

## Anti-Patterns

- Revenue hockey sticks without operational proof.
- Treating accounting profit as if it were cash available for debt service.
- Using balancing figures to hide weak working-capital logic.
- Disconnecting the financial model from implementation timing and market assumptions.

## Outputs

- Financial projections section
- Assumptions document
- Core financial statements and key ratios
- Break-even and sensitivity handoff points
- Valuation bridge inputs where equity or blended capital is involved



Generate rigorous, transparent financial projections that withstand investor scrutiny. This is where bankability is won or lost.

## What to Generate

### Required Financial Statements (3-5 year projections)

1. **Income statement (P&L)**  Revenue, COGS, gross margin, operating expenses, net income
2. **Cash flow statement**  Operating, investing, and financing cash flows
3. **Balance sheet**  Assets, liabilities, equity (annual snapshots)
4. **Break-even analysis**  When the business becomes profitable
5. **Key assumptions document**  Every number must trace to an assumption

### Required Analyses

6. **Revenue model**  How revenue is generated, pricing x volume
7. **Cost structure**  Fixed vs. variable costs breakdown
8. **Unit economics**  Revenue per unit, cost per unit, contribution margin
9. **Financial ratios** - Gross margin %, net margin %, burn rate, runway, current ratio, quick ratio, interest cover, debt-to-equity where relevant
10. **Sensitivity analysis** - How projections change with key variable shifts (detailed in meta-financial-stress-test)
11. **Valuation bridge** - For equity, blended-finance, or strategic-partnership cases, identify the inputs that `meta-valuation` will use: free cash flow, growth, margins, reinvestment, and terminal assumptions

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
- Cost of capital or return hurdle when equity valuation will be required

### Process Costing for Operational Budgets

When projecting staffing and operational costs, use process-based costing (Page, 2015):

1. **FTE calculation**: Adjusted Annual Hours = 2,080  Vacation  Sick  Holidays; FTE = Total Annual Process Hours  Adjusted Hours
2. **People cost**: (Annual Salary  FTE)  (1 + Employee Benefit Rate)
3. **Tool cost**: Software/licence costs apportioned by FTE usage
4. **Overhead cost**: People Cost  Overhead Rate
5. **Cost per transaction**: Total Process Cost  Annual Volume

For technology investments, apply the three-dimensional feasibility framework (Dennis et al., 2021):
- **Technical feasibility**  Can we build/deploy itSection  (familiarity, size, compatibility risks)
- **Economic feasibility**  Should we investSection  (NPV, ROI, break-even analysis over 35 years)
- **Organisational feasibility**  Will the team adopt itSection  (strategic alignment, champion, user readiness)

### Budgeting Fundamentals

**The limiting budget factor** determines what gets built first (ILM):
- New/cash-constrained business  **cash budget first**
- Established business  **sales budget first** (everything else follows from revenue)
- Production-constrained  **production budget first**

**Variance analysis:** Compare actuals to budget monthly. Label variances as Favourable (F) or Adverse (A). Investigate both  adverse variances need corrective action; favourable variances may indicate short cuts or lessons to capture.

**Flexible budgets:** Separate fixed and variable costs so monthly reviews compare "what should we have spent at this actual volume" not "what did we budget at planned volume." See `references/budgeting-forecasting.md`.

### Forecast vs. Target vs. Plan

Keep these distinct in the assumptions document (Morlidge):
- **Forecast** = what you think will happen (inform decisions; update as conditions change)
- **Target** = what you want to happen (set ambition; fixed)
- **Plan** = actions to bridge target and forecast (execution roadmap)

Revenue projections contain both: treat costs as engineering estimates (forecasts), treat revenue as targets-with-a-plan. Never anchor cost assumptions to revenue targets.

**Driver-based modelling:** Identify 510 key drivers (transactions, customers, utilisation rate, price per unit) and derive all other line items from them. This makes assumptions explicit, enables instant scenario analysis, and prevents inconsistencies across statements.

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
7. Compute key financial ratios and covenant-style checks
8. Build the valuation bridge when Section 11 involves equity or blended capital
9. Flag areas requiring sensitivity analysis

## Quality Criteria (Rogoff's Bankability Standards)

- Every number traces to a documented assumption
- Revenue projections are bottom-up (not "we'll capture X% of the market")
- Cash flow is projected separately from profit (profitable companies can run out of cash)
- Break-even timeline is realistic
- Projections show a credible path to profitability
- No hockey-stick growth without clear justification
- Assumptions are conservative-to-moderate, not optimistic
- Working-capital assumptions are explicit, not buried in balancing figures
- When equity is involved, the model is ready for `meta-valuation` rather than forcing valuation to be guessed later

### Startup-Specific Financial Metrics

For early-stage ventures, supplement traditional financial statements with startup metrics (Blank & Dorf, 2012):

- **Cash burn rate** and months of cash remaining (the master metric)
- **Customer acquisition cost (CAC)** and customer lifetime value (LTV)
- **LTV:CAC ratio** (target >3:1)
- **Conversion rates** through the sales funnel
- **Revenue growth rate** (month-over-month)

Use the **One-Minute Business Model** as a quick feasibility check: Revenue per unit  Cost per unit = Profit per unit; Target revenue  Profit per unit = Units needed (Kagan, 2024). If the monthly unit target seems achievable, build the detailed projections.

When projections don't work, adjust the **Six Revenue Dials**: average order value, frequency, price point, customer type, product line, and add-on services (Kagan, 2024). See `references/startup-financial-metrics.md`.

## References

- **Budgeting and forecasting best practices**: See `references/budgeting-forecasting.md` for the budget definition and types (sales/cash/production), limiting budget factor, budgetary control and variance analysis (favourable/adverse), flexible budgets (adjusting for activity level), standard costing, performance measurement framework, financial and non-financial KPIs, benchmarking types; PLUS forecast vs. prediction vs. target vs. plan distinctions, TARAC/CARAT qualities of a good forecast, 7 symptoms of forecasting disease, rolling forecasts vs. annual budgets, driver-based modelling, demand vs. sales distinction, judgmental bias types, and a cash budget template  from ILM/Elsevier (2003), Morlidge & Player (Wiley, 2010), and Vandeput (Manning, 2023). **Read when building budget structure, variance tables, or reviewing forecasting assumptions.**
- **Process costing and feasibility analysis**: See `references/process-costing-feasibility.md` for FTE calculation formulas, three-component process costing (people/tools/overhead), cost per transaction, hard vs soft savings, three-dimensional feasibility analysis (technical/economic/organisational), NPV/ROI/break-even methodology, and cost-benefit spreadsheet structure  from Page (AMACOM, 2015) and Dennis, Wixom & Tegarden (Wiley, 2021)
- **Startup financial metrics**: See `references/startup-financial-metrics.md` for Metrics That Matter framework (3 worked examples by channel type), One-Minute Business Model, Six Revenue Dials, Freedom Number, burn rate guidelines by stage, and revenue curves by market type  from Blank & Dorf (2012) and Kagan (2024)
- **Uganda wage and cost benchmarks (202526)**: See `references/uganda-wage-cost-benchmarks.md` for median monthly earnings (UGX 200,000 cash; UGX 260,000 cash+in-kind), inflation rates by expenditure category, key commodity/energy price changes, household spending patterns, poverty line thresholds, and a default assumptions template (exchange rates, tax rates, NSSF, lending rates)  from UBOS (NLFS 2021, UNHS 2023/24, CPI Feb 2026, KEI Q1 2025/26). **Read this file whenever setting salary assumptions, input cost escalation rates, or building the assumptions document for Uganda financial projections.**
- **Uganda tax framework (ITA Cap.340 + 2025 amendments)**: See `references/uganda-tax-framework.md` for the complete Uganda tax system  corporate income tax (30%, with worked P&L example), PAYE bands and monthly computation example, VAT (18%, UGX 150M threshold, EFRIS compliance), WHT rates by payment type (6 Sched., 7 types), presumptive tax for turnovers <UGX 150M, rental income tax, NSSF (15% total), import duties and 2025 levies (1.5%+1.0% on CIF), the six 2025 amendments checklist, and tax schedule templates for all three financial statements. Also covers KPMG 2025 excise/stamp duty changes, export levies, and penalty waiver window. **Read for every Uganda financial projection  use the PAYE bands, corporate tax rate, and EFRIS compliance requirements. Do not estimate tax rates from memory.**
- **Informal business records  reconstruction and lending**: See `references/informal-business-records.md` for mobile money statement analysis method (MTN/Airtel), bank statement analysis, customer order book reconstruction, supplier COGS imputation, reconstructed income statement template, lender acceptance table by institution type (Stanbic/ABSA require 2yr audited; Centenary/Equity accept 12mo statements; microfinance accept 6mo), cash-flow lending narrative template, transition plan from informal to formal records, and SACCO/microfinance lending pathway. **Read when the business has no formal audited accounts  covers how to reconstruct financial history from available records and present it credibly to lenders.**
- **Financial model templates**: See `references/financial-model-templates.md` for ready-to-use Uganda financial statement templates  monthly income statement (with NSSF, VAT, provisional tax rows), annual summary (Years 13), monthly cash flow (with Uganda VAT/PAYE/NSSF timing rules), balance sheet (with ITA Sixth Schedule depreciation rates: plant 40%, vehicles 35%, computers 40%, furniture 20%, buildings 5%), key ratios dashboard (DSCR, current ratio, gross margin with bank compliance check), break-even analysis template, and a complete financial assumptions document template. **Use this as the structural skeleton for all Section 10 financial statements  do not invent your own row structure.**
- **Uganda IP framework**: See `references/uganda-ip-framework.md` for the IP protection process relevant to financial planning  IP as a balance sheet asset and loan collateral, trademark registration (URSB, 7+10yr, Nice Classification, UGX 175,000 total fee), patent (20yr), utility model (10yr), industrial design (15yr), copyright (automatic, life+50yr), ARIPO regional protection (19 African countries), trade secret via NDA. **Read when assessing whether IP should appear on the balance sheet or be disclosed as a business asset to lenders.**
- **Statistical rigour for financial projections**: Use `meta-statistics` skill when computing or presenting growth rates, revenue forecasts, or comparative financial metrics. Key rules: use geometric mean (CAGR formula) for all multi-year growth rates; use coefficient of variation to compare revenue-line volatility; use regression if  3 years historical data exist; report adjusted R2 and significance (p-value) for any regression-based forecast. See `meta-statistics/references/statistics-for-business-plans.md Regression` and `Growth Rates` for worked Uganda examples and citation templates.

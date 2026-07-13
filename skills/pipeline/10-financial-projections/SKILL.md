---
name: 10-financial-projections
description: Use when producing or reviewing the 10 financial projections component of a business plan; applies its specialist evidence, decisions, and acceptance tests instead of neighbouring pipeline skills.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
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
12. **Initiative-level business case** - For any major technology, expansion, or process investment, state the incremental cost, benefit, timing, and downside if it underdelivers

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
- Accounting basis, bookkeeping cadence, source-document discipline, reconciliation routines, and financial-control assumptions where these affect lender or investor trust
- IFRS/IFRS for SMEs statement format, accounting-policy assumptions, and whether the operating system will use an embedded posting engine so projected and actual gross margin, contribution margin, working capital, and cash flow remain comparable
- Inventory buildup by raw materials, work in process, finished goods, packaging, and spares where applicable
- Production yield, scrap, rework, setup/changeover, and practical capacity assumptions for manufacturing or processing businesses
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
- **Technical feasibility** — Can we build/deploy it? (familiarity, size, compatibility risks)
- **Economic feasibility**  Should we invest? (NPV, ROI, break-even analysis over 35 years)
- **Organisational feasibility** — Will the team adopt it? (strategic alignment, champion, user readiness)

### Accounting Upgrade References

When the plan involves SaaS, ERP, POS, inventory, payroll, schools, clinics, NGOs, agribusiness, or any system that will produce its own books, use:

- `references/accounting-upgrade/ifrs-statement-templates.md` for IFRS-aligned projected statements.
- `references/accounting-upgrade/posting-model-unit-economics.md` to align projected unit economics with the live posting model.
- `references/accounting-upgrade/cvp-working-capital.md` for CVP, break-even, AR/AP/inventory days, and cash-conversion-cycle analysis.

Hard rules:

- Do not default to US GAAP classifications for East/Central African markets.
- Do not use LIFO under IFRS or IFRS for SMEs.
- Do not double-count depreciation as both operating expense and below-EBITDA deduction.
- Separate employee payroll deductions from employer payroll costs.

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

### Industrial and Inventory-Heavy Financial Modelling

For manufacturing, food processing, fabrication, wholesale, logistics, and distribution businesses, add an operations-linked cost schedule:

1. **Material plan:** units sold -> units produced -> gross material requirement -> net purchase requirement after usable stock and supplier lead times.
2. **Inventory days:** model separate days-on-hand for raw materials, packaging, WIP, finished goods, spares, and slow-moving stock.
3. **Yield and scrap:** convert input quantities into saleable output using expected yield; show scrap, rework, and quality rejection as cost lines, not hidden margin leakage.
4. **Capacity cost:** tie labour, overtime, maintenance, utilities, and equipment leases to practical capacity, setup/changeover, and planned utilisation.
5. **Warehouse and logistics cost:** include storage rent, handling labour, racking, cold chain, pick/pack, distribution staging, freight, and returns handling.
6. **Green production economics:** model energy per unit, water per unit, waste disposal, by-product recovery, and resource-efficiency capex where relevant.

If a projected sales volume exceeds practical production or warehouse capacity, either add capex/hiring/timeline assumptions or reduce the forecast.

## Generation Process

1. Ask for: business model, pricing, expected customer count, major costs, funding stage
2. Build revenue model with explicit unit economics
3. Project costs (COGS, OpEx, CapEx) month by month for year 1
4. Generate income statement, cash flow, and balance sheet
5. Calculate break-even point
6. Document every assumption
7. Compute key financial ratios and covenant-style checks
8. Run `meta-accounting-finance-review` when the plan has material accounting, controls, tax, inventory, payroll, POS, ERP, grant, debt, valuation, or investor-readiness implications.
9. Build the valuation bridge when Section 11 involves equity or blended capital
10. Flag areas requiring sensitivity analysis
11. For material initiatives, compare base case, preferred option, and do-nothing or low-investment alternative
12. For industrial businesses, reconcile production volume, material purchases, inventory buildup, capacity, yield, and working capital before calculating DSCR or funding need.
13. For businesses that will rely on ERP, POS, Excel, mobile money, school fees, patient billing, inventory, payroll, or project accounting, state how source transactions become reliable books: chart of accounts, subledgers, control accounts, accruals/prepayments, depreciation, tax, reconciliations, period close, and management reporting.

## Quality Criteria (Rogoff's Bankability Standards)

- Every number traces to a documented assumption
- Revenue projections are bottom-up (not "we'll capture X% of the market")
- Cash flow is projected separately from profit (profitable companies can run out of cash)
- Break-even timeline is realistic
- Projections show a credible path to profitability
- No hockey-stick growth without clear justification
- Assumptions are conservative-to-moderate, not optimistic
- Working-capital assumptions are explicit, not buried in balancing figures
- Bookkeeping, reconciliation, tax, inventory, payroll, and source-document assumptions are credible enough that projected results could be produced after launch
- When equity is involved, the model is ready for `meta-valuation` rather than forcing valuation to be guessed later
- Major capex, systems, or digitisation bets show incremental economics rather than being buried in a lump-sum use-of-funds line
- Website, ecommerce, landing page, portal, web app, SEO/content engine, and website-design-service assumptions show one-time build costs, recurring operating costs, content/SEO costs, maintenance, support, subscriptions, payment fees, and realistic conversion assumptions.

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
- **Business-case discipline for major investments**: See `../book-extractions/haines-how-to-create-a-business-case-extraction.md` for incremental benefit logic, option comparison, do-nothing case, payback/NPV framing, and one-variable sensitivity analysis. **Read when the financial model includes major digitisation, automation, market-entry, or capacity-expansion spend.**
- **Startup financial metrics**: See `references/startup-financial-metrics.md` for Metrics That Matter framework (3 worked examples by channel type), One-Minute Business Model, Six Revenue Dials, Freedom Number, burn rate guidelines by stage, and revenue curves by market type  from Blank & Dorf (2012) and Kagan (2024)
- **Uganda wage and cost benchmarks (202526)**: See `references/uganda-wage-cost-benchmarks.md` for median monthly earnings (UGX 200,000 cash; UGX 260,000 cash+in-kind), inflation rates by expenditure category, key commodity/energy price changes, household spending patterns, poverty line thresholds, and a default assumptions template (exchange rates, tax rates, NSSF, lending rates)  from UBOS (NLFS 2021, UNHS 2023/24, CPI Feb 2026, KEI Q1 2025/26). **Read this file whenever setting salary assumptions, input cost escalation rates, or building the assumptions document for Uganda financial projections.**
- **Uganda tax framework (ITA Cap.340 + 2025 amendments)**: See `references/uganda-tax-framework.md` for the complete Uganda tax system  corporate income tax (30%, with worked P&L example), PAYE bands and monthly computation example, VAT (18%, UGX 150M threshold, EFRIS compliance), WHT rates by payment type (6 Sched., 7 types), presumptive tax for turnovers <UGX 150M, rental income tax, NSSF (15% total), import duties and 2025 levies (1.5%+1.0% on CIF), the six 2025 amendments checklist, and tax schedule templates for all three financial statements. Also covers KPMG 2025 excise/stamp duty changes, export levies, and penalty waiver window. **Read for every Uganda financial projection  use the PAYE bands, corporate tax rate, and EFRIS compliance requirements. Do not estimate tax rates from memory.**
- **Informal business records  reconstruction and lending**: See `references/informal-business-records.md` for mobile money statement analysis method (MTN/Airtel), bank statement analysis, customer order book reconstruction, supplier COGS imputation, reconstructed income statement template, lender acceptance table by institution type (Stanbic/ABSA require 2yr audited; Centenary/Equity accept 12mo statements; microfinance accept 6mo), cash-flow lending narrative template, transition plan from informal to formal records, and SACCO/microfinance lending pathway. **Read when the business has no formal audited accounts  covers how to reconstruct financial history from available records and present it credibly to lenders.**
- **Financial model templates**: See `references/financial-model-templates.md` for ready-to-use Uganda financial statement templates  monthly income statement (with NSSF, VAT, provisional tax rows), annual summary (Years 13), monthly cash flow (with Uganda VAT/PAYE/NSSF timing rules), balance sheet (with ITA Sixth Schedule depreciation rates: plant 40%, vehicles 35%, computers 40%, furniture 20%, buildings 5%), key ratios dashboard (DSCR, current ratio, gross margin with bank compliance check), break-even analysis template, and a complete financial assumptions document template. **Use this as the structural skeleton for all Section 10 financial statements  do not invent your own row structure.**
- **Uganda IP framework**: See `references/uganda-ip-framework.md` for the IP protection process relevant to financial planning  IP as a balance sheet asset and loan collateral, trademark registration (URSB, 7+10yr, Nice Classification, UGX 175,000 total fee), patent (20yr), utility model (10yr), industrial design (15yr), copyright (automatic, life+50yr), ARIPO regional protection (19 African countries), trade secret via NDA. **Read when assessing whether IP should appear on the balance sheet or be disclosed as a business asset to lenders.**
- **Statistical rigour for financial projections**: Use `meta-statistics` skill when computing or presenting growth rates, revenue forecasts, or comparative financial metrics. Key rules: use geometric mean (CAGR formula) for all multi-year growth rates; use coefficient of variation to compare revenue-line volatility; use regression if  3 years historical data exist; report adjusted R2 and significance (p-value) for any regression-based forecast. See `meta-statistics/references/statistics-for-business-plans.md Regression` and `Growth Rates` for worked Uganda examples and citation templates.
- **Website investment and costing**: Use `../meta-website-investment-planning/SKILL.md` and `../meta-website-investment-planning/references/website-investment-costing-gate.md` when projections include a website, ecommerce, content/SEO engine, portal, web app, or website-design service business. Model one-time build costs, recurring costs, maintenance, content/SEO, payment fees, conversion assumptions, and delivery capacity explicitly.
- **Data analytics for planning and management dashboards**: See `../../book-extractions/data-analytics-business-planning-extraction.md` when projections depend on historical sales, operational datasets, forecasts, AI analytics, scenario analysis, KPI dashboards, or variance logic. Use the descriptive/diagnostic/predictive/prescriptive ladder to keep forecasts, targets, and recommendations properly separated.
- **Industrial production and inventory model link**: See `../../book-extractions/industrial-production-inventory-planning-extraction.md` when modelling manufacturing, food processing, warehousing, logistics, wholesale, or any business with material stock risk. Use it to structure raw-material consumption, MRP-style purchasing, safety stock, WIP, yield/scrap, capacity, warehousing, and resource-efficiency assumptions.
- **Accounting, bookkeeping, ERP finance controls, cost accounting, and finance workbook discipline**: See `../../book-extractions/accounting-bookkeeping-finance-controls-extraction.md` when the plan involves ERP/POS, school fees, patient billing, inventory, payroll, tax, mobile money, credit sales, supplier credit, cost centres, management accounts, Excel models, or weak/informal records. Use it to strengthen accounting basis, reconciliations, source documents, control accounts, close cadence, cost accounting, variance analysis, and model checks.
- **Accounting and finance review gate**: Run `../meta-accounting-finance-review/SKILL.md` and read `../meta-accounting-finance-review/references/accounting-finance-quality-gate.md` before bankability scoring, stress testing, valuation, due diligence, or final assembly whenever the numbers must withstand accountant, investor, lender, CEO, or board scrutiny.
- **SaaS unit economics**: Use `../saas-unit-economics-and-cohort-model/SKILL.md` whenever the business is SaaS / subscription / recurring revenue — replaces the generic financial-projection workflow for the unit-economics layer (LTV, CAC, NRR, Rule of 40, ARR waterfall, cohort retention).
- **AI unit economics (for AI-feature-led SaaS plans)**: Use `saas-ai-unit-economics-and-cogs/SKILL.md` whenever AI is a material customer-facing cost in the plan (typically >2% of ARR or load-bearing). Decomposes AI COGS into a CFO-grade waterfall (token, embedding, fine-tune amortisation, vector store, GPU reservation, eval, hallucination reserve, retraining, AI overhead) and computes AI Gross Margin, AI Contribution Margin per tier, blended-GM impact, and AI-cost-as-%-of-ARR — the diagnostics AI-aware investors look for.
- **AI cost-of-tenant calculator**: Use `saas-ai-cost-of-tenant-calculator/SKILL.md` to build the per-tenant AI cost spec (per-query formula, per-tenant monthly formula, sensitivity matrix on usage / model-mix / cache / FX, break-even tenant, top-decile tenant, mitigation lever library, worked African vertical-SaaS example) before making any AI tier-design or pricing decision.
- **Agent revenue recognition (ASC 606 / IFRS 15)**: Use `saas-agent-revenue-recognition/SKILL.md` whenever the plan ships an agent product priced per-resolution, per-outcome, subscription + success fee, prepaid task credits, or hybrid — each primitive has its own performance obligation, recognition trigger, and variable-consideration treatment. Generic SaaS rev-rec assumes ratable subscription; agent rev-rec does not.
- **Agent deferred revenue and credit reserves**: Use `saas-agent-deferred-revenue-and-credit-reserves/SKILL.md` for prepaid agent task credits (deferred revenue + breakage), SLA-credit accrued liability (sized off trailing credits issued ÷ trailing agent revenue), refund-reserve methodology, true-up cadence, and balance-sheet presentation. Auditors and DD teams quote these reserves.
- **Agent SLA COGS treatment**: Use `saas-agent-sla-cogs-treatment/SKILL.md` to classify SLA-related cost lines correctly — which are COGS (HITL for SLA defence, retraining amortisation, SLA-monitoring infra, SLA-relevant evals), which are contra-revenue (SLA credits issued, outcome refunds), which are S&M (CS for SLA management), which are G&A (legal defending SLA disputes). Getting this wrong overstates revenue and understates COGS.
- **Agent SLA economics in projection**: Use `saas-agent-sla-economics-in-projection/SKILL.md` to integrate SLA performance into the 3yr / 5yr plan as a driver (SLA breach feeds revenue / risk / churn / funding need), not a footnote. SLA-tier mix evolution, cost-of-quality assumption, churn-correlation modelling. See `saas-agent-sla-economics-in-projection/references/africa-agent-sla-context.md` for Africa-specific FX / mobile-money / sovereign-AI / DFI overlay.

## July 2026 Portable Contract

<!-- dual-compat-start -->

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when absent |
|---|---|---:|---|
| Approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon for 10 financial projections | Client records, approved operating model, finance owner, and accounting doctrine | Yes | If absent, contract terms, usage evidence, framework, or cost drivers are unavailable, isolate the affected schedule, label it unassessed, and do not force the model to balance with a plug. |
| Finalised business brief, target reader, country, and stage | Client intake and engagement owner | Yes | Stop section decisions and route the missing context to client intake. |
| Reconciled upstream assumptions that this section consumes | Named pipeline owners | Conditional | Record the dependency, affected claim, owner, and recovery step; do not substitute an invented value. |

## Outputs

| Artefact | Consumer | Observable acceptance condition |
|---|---|---|
| Integrated projections with SLA and scenario effects | Plan author and target decision-maker | The artefact answers the section decision and traces each material conclusion to the supplied evidence. |
| 10 financial projections exception and handoff note | Downstream section owners | Every blocked or conditional item names its consequence, owner, evidence request, and restart condition. |
| 10 financial projections release record | Reviewer or plan assembler | Records the checks completed, failures, unassessed items, professional review required, and release state. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Formula trace, source/assumption register, three-statement or schedule reconciliation, and finance-gate record | Source-linked table, calculation, or annotated prose | The evidence is reproducible from named inputs and distinguishes verified fact, management assumption, and inference. |
| 10 financial projections decision record | Decision note | States the selected action, rejected credible alternative, countercase, rationale, and risk accepted or avoided. |
| 10 financial projections review trace | Gate entry | Identifies the date, input versions, reviewer role, failed checks, recovery owner, and any check that remains not assessed. |

## Capability and Permission Boundaries

For 10 financial projections, the controlling focus is integrated income statement, cash flow, balance sheet, assumptions, sensitivities, and funding reconciliation. This skill may inspect records and calculate planning scenarios in read-only mode; it may not post entries, change ledgers, set accounting policy, certify IFRS treatment, or release statutory values without authorised professional review. Its normal mode is read-only analysis and drafting. Any mutation, external communication, spending, certification, or professional conclusion outside that boundary requires explicit authority and must remain traceable to the approving role.

## Degraded Mode

For 10 financial projections, loss of evidence about integrated income statement, cash flow, balance sheet, assumptions, sensitivities, and funding reconciliation activates degraded mode. If the controlling 10 financial projections evidence is unavailable, the same boundary applies. When contract terms, usage evidence, framework, or cost drivers are unavailable, isolate the affected schedule, label it unassessed, and do not force the model to balance with a plug. Return the verified subset, label the affected decision qualified or not assessed, explain the downstream consequence, and state the smallest evidence request or authorised action that permits recovery. Do not convert the missing check into a pass.

## Decision Rules

| Choice or condition | Action | Failure or risk avoided |
|---|---|---|
| For 10 financial projections, commercial billing, cash receipt, service delivery, and accounting recognition occur in different periods| model each event separately, reconcile the bridge, and route judgemental treatment to the finance reviewer | Cash, revenue, liability, and margin can be conflated into a misleading forecast |
| For 10 financial projections, A current legal, regulatory, tax, accounting, market, or platform claim controls the 10 financial projections decision| Verify the controlling source, effective date, jurisdiction, and reviewer status before release | Stale external facts become permanent plan assumptions |
| For 10 financial projections, The evidence reconciles with neighbouring sections and the countercase does not overturn the choice| Complete integrated projections with sla and scenario effects, attach the evidence and release record, and hand off named dependencies | Premature release and repeated downstream rework |

## Workflow

1. Define the exact 10 financial projections decision, intended reader, jurisdiction, business stage, and permission boundary.
2. Collect approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon and map each material conclusion to its source; stop the affected conclusion when an input could change it.
3. Apply `../../../references/sector-regulatory-gates.md`; place every evidenced licence, control, certification, mitigation and delay effect in the owning schedule, and leave unresolved gates visibly unassessed rather than using a plug.
4. Apply the specialist methods and directly linked references already contained in this skill, retaining its domain thresholds, calculations, and Uganda or East Africa context where applicable.
5. Compare the credible alternatives, test the countercase and failure path, and apply the decision table rather than selecting a template default.
6. Produce integrated projections with SLA and scenario effects with the evidence, exception, and handoff records; reconcile every shared assumption with its owning section.
7. Run the workbook formula map, section quality checks, finance gate, applicable professional review, and anti-slop gate. If a gate fails, correct the evidence or decision and return to the responsible step.

## Quality Standards

- Integrated projections with SLA and scenario effects must answer a real decision for the named bank, investor, DFI, grant, board, or strategic-partner reader.
- Formula trace, source/assumption register, three-statement or schedule reconciliation, and finance-gate record must be source-linked, dated where facts can change, and sufficient for another reviewer to reproduce the conclusion.
- The section exposes its countercase, stop condition, recovery action, and effect on neighbouring sections.
- No unavailable source, calculation, tool, or professional review is reported as passed; finance and statutory judgements follow the governing doctrine.
- Language remains specific to 10 financial projections, uses British English naturally, and passes the repository anti-slop gate without promotional filler.

## Anti-Patterns

- In 10 financial projections, treating an unavailable approved commercial assumptions, contracts, usage/cost evidence, accounting framework, opening position, and projection horizon as confirmed. Correction: qualify the affected conclusion and issue the named evidence request.
- Producing integrated projections with sla and scenario effects that restates the brief but makes no choice. Correction: record the choice, rejected alternative, rationale, countercase, and implication.
- Ignoring a conflicting upstream assumption. Correction: return it to its owning section and resume only from a reconciled version.
- Reporting an unavailable check as passed. Correction: mark it not assessed and narrow the release state.
- Claiming compliance, assurance, bankability, or investor readiness from narrative quality. Correction: run the applicable gate and retain its evidence.
- Copying the worked example into a client plan. Correction: use the method only and replace every fact with verified engagement evidence.

## Worked Example

The base case meets profit targets only because SLA credits are omitted. Add the expected credit cost and downside case, then reconcile EBITDA, cash, and funding need.

## References

- Audit XLSX formulae, assumptions, external links, scenarios and balance checks with `../../../tools/workbook-audit/formula_map.py`; a structural failure blocks release.
- Use the verified project evidence register and the owning upstream pipeline section for 10 financial projections; no local deep-dive reference is declared.
- For 10 financial projections claims involving money, tax, grants, reserves, revenue, cost, valuation, or financial statements, apply the Chwezi finance doctrine and record the required professional-review state; illustrative figures never become client facts.

<!-- dual-compat-end -->

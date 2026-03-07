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

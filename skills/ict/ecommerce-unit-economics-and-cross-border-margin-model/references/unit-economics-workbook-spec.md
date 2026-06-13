# Unit Economics Workbook Specification

## Required Tabs

1. `README`: purpose, company, markets, version, preparer, review date.
2. `Inputs`: all assumptions with links to the assumptions register.
3. `Products`: SKU/category, COGS, price, weight/volume, return eligibility.
4. `Routes`: origin, destination, logistics providers, customs/duties, last-mile cost.
5. `Channels`: owned site, marketplace, WhatsApp/social, distributor, agent.
6. `Payment`: provider fees, settlement delay, FX, chargebacks/refunds.
7. `Marketing`: spend, orders, CAC, conversion, retention, LTV inputs.
8. `Model`: gross margin, contribution margin, payback, LTV:CAC, cash-cycle impact.
9. `Sensitivity`: returns, freight, CAC, discount, FX, commission, AOV.
10. `Verdict`: go, conditional, no-go by market/channel.

## Core Formula Logic

- Gross margin = revenue - COGS.
- Contribution margin = revenue - COGS - variable fulfilment - payment/FX - commissions - returns/refunds - CAC.
- Contribution margin percent = contribution margin / revenue.
- Payback period = CAC / contribution margin per active customer period, where data exists.
- LTV:CAC = contribution-based LTV / CAC. Treat 3:1 as a global health reference, not an EAC fact.

## Integrity Checks

- No blank source field for material assumptions.
- No negative costs unless explicitly marked as subsidy/credit.
- VAT/tax treatment stated and separated from net operating economics.
- Formula cells protected or visibly separated from input cells.
- Scenario outputs reconcile to base model.

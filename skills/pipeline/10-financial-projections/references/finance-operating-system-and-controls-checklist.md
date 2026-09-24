Parent: [Financial Projections Skill](../SKILL.md)

When to read: when financial credibility depends on how the business will keep records, control money, reconcile balances, cost its output, and review performance — for example ERP or POS use, school fees, patient billing, inventory, payroll, tax, mobile money, credit sales, supplier credit, cost centres, or management accounts. Also used by the agent revenue-recognition, SLA controls, and reserve skills.

# Finance Operating System and Controls Checklist

A bankable plan shows the financial operating system that will produce trustworthy results after launch, not only projected statements. This checklist paraphrases practice from management accounting, bookkeeping, financial accounting, ERP finance configuration, and spreadsheet-modelling texts supplied to the engine (titles not recorded individually at ingestion). Accounting treatment, tax rules, and statutory deductions must be confirmed through the Chwezi Accounting Doctrine engine (`chwezi-accounting-doctrine`) per the Finance and Accounting Trigger; this checklist does not replace it.

## 1. Bookkeeping foundations

- [ ] The accounting equation (assets = liabilities + equity) is the integrity check for the projected balance sheet.
- [ ] Basis stated: cash, accrual, or a staged move to accrual. Accrual is the credible target for any business with invoices, credit sales, supplier bills, payroll, inventory, taxes, loans, or fixed assets.
- [ ] Books and schedules named: sales, purchases, cash book, payroll, inventory, fixed assets, tax, receivables, payables, general ledger.
- [ ] Source-document retention described: invoices, receipts, bills, payment confirmations, delivery notes, payroll records, bank statements, tax returns, contracts.
- [ ] Profit and cash separated: credit sales, stock purchases, loan repayments, tax timing, capex, and supplier terms shown in the cash-flow timing.
- [ ] Reconciliations scheduled: bank, mobile money, receivables, payables, inventory, tax, payroll, fixed assets.

## 2. ERP and system controls

- [ ] For ERP-reliant businesses, the finance module covers chart of accounts, subledgers, posting rules, fiscal periods, audit trail, approvals, reversals, period close, and management reporting.
- [ ] Control accounts used for receivables, payables, inventory, tax, payroll, fixed assets, and bank or cash.
- [ ] No direct posting to control accounts except controlled adjustments with a reason and approval.
- [ ] Dimensions recorded where management needs them: company, branch, cost centre, profit centre, project, location.
- [ ] Maker-checker approval for high-risk actions: payments, write-offs, stock adjustments, manual journals, payroll approval, supplier bank-detail changes, closed-period changes.
- [ ] Period close run from a written checklist.

## 3. Management and cost accounting

- [ ] Costs classified: fixed or variable, direct or indirect, controllable or not, product or period, one-off or recurring.
- [ ] Contribution margin used for break-even, pricing, capacity, and mix decisions.
- [ ] Cost centres and profit centres defined where departments, branches, clinics, campuses, lines, or projects need accountability.
- [ ] For manufacturing, processing, construction, services, and clinics: direct labour, materials, overhead, wastage, rework, and capacity costed.
- [ ] For repeatable output: standard costs and variance analysis (price or rate, usage or efficiency, volume, yield or mix, overhead).
- [ ] Flexible budgets compare actual spend with the cost expected at the actual activity level.

## 4. Workbook discipline

- [ ] Separate sheets for inputs, data, calculations, checks, reports, and dashboard.
- [ ] Checks for trial balance, balance sheet, cash roll-forward, receivables and payables control, inventory control, fixed assets, and formula errors.
- [ ] Driver-based assumptions: customers, volume, price, utilisation, cost-of-sales rate, staff, inventory days, receivable days, payable days, capex, tax timing.
- [ ] Scenarios and sensitivities for the few assumptions that move funding need, DSCR, runway, or profit.
- [ ] Variance dashboard: actual against budget by month, year to date, and rolling forecast.
- [ ] Run `tools/workbook-audit/formula_map.py` on the delivered workbook.

## 5. Section links

- **Operations:** how transactions are captured at source — POS, invoices, purchase orders, stock movements, payroll, patient or fee billing, production orders, delivery notes, payments.
- **Financial projections:** working capital, stock, receivables, payables, tax, depreciation, loan repayment, capex, and closing cash explicit; control assumptions stated where the reader must trust the numbers.
- **Risk:** weak bookkeeping, late reconciliations, cash leakage, tax non-compliance, inventory misstatement, debtor collection failure, supplier payment errors, payroll errors, fraud, spreadsheet errors.
- **Implementation:** finance rhythm — daily cash-up; weekly bank and mobile-money reconciliation; monthly receivables and payables review; monthly stock or cycle count; monthly management accounts; quarterly tax review; annual close.

## 6. Red flags

- Strong profit with no cash-flow timing.
- Inventory-heavy business with no valuation method or stock-count process.
- Credit sales with no receivable days or bad-debt allowance.
- Supplier credit assumed without payable terms or payment discipline.
- Payroll costed without statutory deductions or an approval workflow.
- ERP or software mentioned without chart of accounts, posting rules, audit trail, or period close.
- Spreadsheet model without checks, assumptions, or reconciliation to the statements.

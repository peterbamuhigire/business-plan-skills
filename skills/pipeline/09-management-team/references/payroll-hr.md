# Payroll Design, Controls and Costing for the Management Plan (Uganda and East Africa)

Use this reference when the plan must cost payroll, describe how pay is processed and controlled, and show statutory compliance. It gives the payroll method, control design, accounting entries, employment-type rules and costing templates. Statutory rates, brackets, thresholds, dates and penalties change; the figures shown are planning assumptions that must be re-verified against a dated official source (Uganda Revenue Authority, National Social Security Fund, Ministry of Gender, Labour and Social Development) and with the Chwezi finance engine (payroll, tax and accounting treatment). Where earlier documents in this folder show different statutory figures, use the verified current source, not either file. See `hr-fundamentals.md` for the wider HR framework.

## 1. Payroll fundamentals

Payroll is the whole process of calculating pay, applying statutory deductions, remitting them and paying net wages on time, done the same way every time.
Why the plan needs it: legal compliance (late remittance attracts penalties); cost accuracy (true employment cost exceeds gross salary); employee trust (errors erode it); audit readiness (banks, investors and tax auditors review payroll records).

Pay cycle: monthly is standard for permanent staff and minimises processing effort; statutory returns are monthly, so it fits compliance. Weekly or fortnightly cycles suit casual labour and some donor-funded bodies.

Definitions and formula:
- Gross pay: basic salary plus all taxable allowances.
- Statutory deductions: employee income tax withheld at source plus the employee social-security contribution.
- Voluntary deductions: loan repayments, savings scheme contributions, union dues.
- Net pay = gross pay less income tax withheld less employee social-security contribution less voluntary deductions.
Show every column in the register and give each employee an itemised payslip.

Typical compensation components and tax questions (verify treatment):
| Component | Point to check |
|---|---|
| Basic salary | Taxable; usual basis for social-security calculation |
| Cash housing, transport, communication, medical allowances | Cash is generally taxable |
| Meals and accommodation on business premises | Possible exemption if provided in kind for the employer's convenience |
| Overtime, bonuses, commissions | Treated as wages |
| Per diem | Exempt within authority-approved limits; excess taxable |
| Employer social-security contribution | Employer cost, not employee income |
| End-of-contract gratuity | Generally taxable when paid |
| Leave allowance | Taxable |

## 2. Income tax withheld at source (PAYE)

Method:
1. Compute monthly chargeable income (gross pay including taxable allowances and imputed benefits).
2. Apply the current progressive monthly bands from the revenue authority: a nil band, then successive bands with rising rates, with a higher rate above a top threshold. Do not hard-code bands in the plan; keep them in a dated parameter table.
3. Withhold, remit and file monthly (assumed due by the 15th of the following month through the revenue authority's online system using a payment registration number).
4. Reconcile at year end and file the employer annual return; issue each employee a tax certificate of total gross pay and tax deducted.
Worked-calculation pattern (use the current bands): tax = sum over bands of (income falling in band x band rate). Check three cases in any model: a low-income employee, a mid-level manager and a senior employee above the top band.
Employer duties: register as an employer; ensure every employee has a tax identification number; keep payroll records for the statutory period (assumed at least five years).
Penalty types to note: late filing, late payment (percentage plus monthly interest), failure to deduct (employer liable for the tax), understating wages (fraud exposure). Employees with a single employment source generally rely on withholding; those with other income file their own returns.

## 3. Social-security contributions

Assumptions to verify: registration required above a small employee threshold (assumed five); employer 10% and employee 5% of gross monthly wage; both remitted by the employer together by the 15th of the following month via the fund's portal with a schedule of names, membership numbers and amounts; new employees registered within about 30 days; existing membership numbers reused; penalties for failure to register, late remittance (percentage per month plus interest) and wilful non-remittance (prosecution, possible director liability).
Formulae: employee contribution = 5% x gross (deducted); employer contribution = 10% x gross (additional cost); remittance = sum of both.

## 4. Allowances and benefits in kind

Principle: all cash payments to employees are taxable unless specifically exempted. Typical exemptions to test: employer contributions to approved pension funds; meals and accommodation on premises; medical costs paid directly to a provider under a group scheme; per diem within approved limits; certain terminal benefits on death or incapacity.
Benefits in kind must be valued and added to income: private use of a company vehicle, employer housing, school fees paid, club memberships, share options (market value at exercise less amount paid). General rule: add the fair market value of the benefit less any amount the employee pays.
Per diem: use the authority's published rates by grade and location; in the plan, state a per-day assumption for domestic day trips and up-country overnight travel and mark it for re-verification. For allowance budgets, benchmark each allowance (transport, housing, airtime, medical, hardship, leave) against current local market data, not this file.

## 5. Payroll register, payslips and records

Register columns: employee number, name, national ID number, social-security number, department or cost centre, basic salary, each taxable allowance, gross pay, employee social-security deduction, taxable income, PAYE, other deductions (loans, savings scheme, union dues), total deductions, net pay, bank account, employer social-security contribution.
Payslip minimum: employer name and address; employee name and number; pay period; gross pay; each deduction itemised; net pay; date paid. Employment law requires a written statement of wages (verify section).
Records: payroll registers, payslip copies, tax remittance receipts, social-security schedules, contracts and deduction authorisations, kept for the statutory period (assumed at least five years). Personnel and pay data are confidential personal data; restrict access and comply with the data-protection law.

## 6. Payroll accounting

Monthly entries (variables, not fixed amounts):
1. Record expense and liabilities: debit salary expense (gross) and employer social-security expense; credit PAYE payable, social-security payable (employee plus employer), and net wages payable.
2. Pay employees: debit net wages payable; credit bank.
3. Remit PAYE by the due date: debit PAYE payable; credit bank.
4. Remit social security by the due date: debit social-security payable; credit bank.
Accrual: when a reporting date falls mid-payroll, debit salary expense and credit accrued salaries for the proportion earned, and reverse at the start of the next period.
Presentation: the employer social-security contribution is a staff cost; total payroll cost = gross salaries + employer contribution + other employer-side costs. Verify presentation and any IFRS treatment (for example short-term employee benefits, leave accruals) with the Chwezi finance engine.
Bank control: keep a separate payroll bank account where possible, transfer exactly the net-wages total on pay day, reconcile monthly against the register, and investigate any unprocessed or returned payment at once (possible ghost employee or wrong details).

## 7. Payroll controls and audit

Objective: prevent innocent error and fraud.
Segregation of duties:
| Function | Performed by |
|---|---|
| Preparing payroll | Payroll or accounts clerk |
| Approving pay changes | HR manager or owner |
| Approving the payroll run | Finance manager or owner, not the preparer |
| Authorising bank transfers | Director or senior manager, not the preparer |
| Bank reconciliation | Accounts person, not the preparer |
In micro-businesses, the owner approves each run and reviews the register before payment.
Pay-rate control: keep approved rates in signed contracts and compare the register with contracts quarterly; require a signed, authorised form from a senior manager for every pay change.
Time control: supervisor approval of hours for hourly or daily workers; investigate consistently high overtime; signed attendance register for salaried staff.
Ghost-employee prevention: periodic payslip or payment hand-out against national ID; monthly roster check by department managers; investigate shared bank accounts; remove leavers on their last day with a signed termination form before the final run; require an appointment letter and confirmed start date before adding anyone; review monthly exception reports (new, deleted, rate changes, negative deductions).

Annual (or quarterly, for larger firms) audit checklist:
1. Compare the register to the HR master list; each name has a contract.
2. Trace 5 to 10 random employees' pay to contracts.
3. Recompute PAYE for the sample using current bands.
4. Recompute social-security contributions for the sample.
5. Compare tax remittance receipts with register totals for the year.
6. Compare social-security receipts with register totals.
7. Review the payroll bank account (credits from main account, debits to employees).
8. Investigate any employee without a social-security number.
9. Confirm leavers were removed in the right month.
10. Confirm deduction authorisation forms are on file.

Fraud schemes and defences:
| Scheme | Defence |
|---|---|
| Ghost employees | ID verification, manager roster checks |
| Salary inflation | Segregation of duties, signed change forms |
| Payments after termination | Same-day removal, manager approval |
| False overtime | Two-level approval, exception reports |
| Duplicate payments | System duplicate detection, bank reconciliation |
| Fictitious negative deductions | Approval for every negative deduction |

## 8. Payroll tools

| Option | Fits | Watch |
|---|---|---|
| Spreadsheet template | Under about 15 staff; free, flexible | No audit trail, silent formula errors, hard to scale, no automatic filing |
| General accounting package with payroll set-up | Small firms with an accountant | Manual set-up of local tax tables |
| Established payroll package | Medium to large firms; built-in local tables, payslips, schedules, ledger link | Licence cost; verify current pricing |
| Cloud payroll platforms (East African vendors) | Multi-country teams; automatic statutory updates | Per-employee monthly fee; verify current pricing |
Selection criteria: statutory tables updated automatically; register export to spreadsheet; branded emailed payslips; audit trail of changes with user and timestamp; bank-file export for bulk payment to local banks and mobile money; export in the revenue authority's return format. Compare quotes at the time of the plan.

## 9. Employment types

- Permanent: full statutory treatment (tax withholding, social security, leave, notice).
- Casual (day-to-day or under a month; verify definition): settle pay at day or week end; tax withheld if pay, annualised, exceeds the nil band; social-security applicability depends on current rules (verify); continuous retention beyond a month converts to regular status; keep a casual labour register (dates, rate, amount) for the statutory period.
- Consultants and contractors: not on payroll; they invoice; withholding tax on local individual consultants (assumed 6%; verify) is deducted and remitted with a certificate. Test for employment: does the business control how the work is done, and does the person work mainly for one client? Misclassifying employees as consultants to avoid contributions is unlawful and closely watched.
- Part-time: pro-rated salary and leave; tax and contributions on actual earnings.
- Expatriates: tax on locally sourced income (including salary paid offshore for services rendered locally); work permit before engagement; tax treaties may reduce withholding on some payments but not employment income earned locally; social-security inclusion unless exempt under a reciprocal agreement; value accommodation and vehicles as benefits in kind.

## 10. Year-end processes

- Reconcile total PAYE remitted for the year with the sum of employees' computed tax; file the employer annual return by the current deadline (verify; the tax year is assumed to run 1 July to 30 June).
- Issue employee tax certificates showing gross pay, tax deducted and employee social-security deducted, by the current deadline.
- Keep all monthly payment registration receipts and reconcile the cumulative tax on the online system to the register each quarter.
- Social-security annual statements show contributions and balance; remind staff that balances are portable and are paid out on defined grounds such as retirement age.

## 11. Statutory leave payments

- Maternity: assumed 60 working days, full pay, tax and social security continue, once per 24 months (verify), notice about one month; dismissal for pregnancy or maternity is prohibited. Provision for costing: build maternity cost into HR budgets for businesses with many women of child-bearing age; derive the provision from own headcount and cover costs, not from a fixed percentage.
- Paternity: assumed four working days at full pay.
- Sick leave: assumed one month full pay and a second month half pay; a medical certificate may be required beyond a few days; protection from dismissal for illness during an initial period (verify).

## 12. Costing payroll in the plan

Step 1: list positions, headcount and gross monthly pay; compute monthly and annual gross totals.
Step 2: add employer social-security contribution (10% assumed).
Step 3: add other employer-side costs: workers' compensation insurance (rate varies by industry risk; obtain a quote), amortised recruitment, uniforms and protective equipment, training, leave provision (annual leave days divided by working days, times salary).
Step 4: compute total employment cost per month and per year.
Rule of thumb for planning only: true cost = gross x a loading factor. A loading of about 1.10 covers employer social security; additional loadings for insurance, leave, recruitment and training raise it (higher in high-injury sectors). Compute the factor from the plan's own components and state it as an assumption.
Worked pattern: an employee on gross G costs G + 0.10G + insurance rate x G + leave provision (about 21/260 x G under the assumed 21-day entitlement) + recruitment and training amortisation.

Budget template:
```
ANNUAL PAYROLL BUDGET - [Business name], Year
Staffing: position | FTE | monthly gross | annual gross
Statutory costs: employer social security; workers' compensation
Other employment costs: leave provision; amortised recruitment; training
TOTAL ANNUAL EMPLOYMENT COST
Payroll calendar (12 months): gross | PAYE | employee social security | net pay | employer social security | total cost
```
Ratios: payroll-to-revenue (total employment cost divided by revenue; benchmark from sector data, since service businesses run higher than manufacturers); revenue per employee; PAYE compliance rate (remitted divided by due, target 100%); social-security compliance rate (target 100%).

## 13. Compliance calendar (assumed dates; verify)

| When | Action |
|---|---|
| Before month end | Process payroll; distribute payslips |
| 15th of following month | File and pay PAYE; file and pay social-security contributions |
| Within about 30 days of hire | Register new employee for social security |
| Tax year end | Reconcile PAYE; prepare employer annual return |
| After year end | Issue employee tax certificates; file annual return |
| Annually | Renew workers' compensation cover; review approved per diem rates |

Sources consulted: Bragg, Essentials of Payroll: Management and Accounting, Wiley, 2003 (US practice adapted); Ugandan Income Tax Act, NSSF Act, Employment Act 2006 and Workers' Compensation Act as understood at drafting (verify current text and rates).

# HR Policy Manual — Document Blueprint

The reusable architecture for a standalone Human Resources Policy Manual, synthesised from real Ugandan NGO HR manuals and the Employment Act 2006 framework. Most chapters are HR-owned and grounded directly in Uganda labour law; the money-touching chapters (compensation & payroll, allowances, staff advances) defer their substance to the finance engine via the chapter→skill map below — never improvise accounting treatment.

This blueprint states policy architecture, not legal advice. Every employment-law minimum (leave, notice, probation ceiling, minimum wage, maternity/paternity entitlement) must be verified against **current Uganda law** at issue and recorded in the dated Statutory Schedule.

Finance-engine root: `C:\wamp64\www\chwezi-accounting-doctrine` (paths below are relative to it).

## Uganda legal framework (cite in the body; keep the numbers in the Statutory Schedule)

- **Employment Act 2006** — contracts, probation, hours, leave, termination, notice, redundancy.
- **NSSF Act** — mandatory social-security contributions (employee + employer).
- **Income Tax Act (PAYE)** — payroll tax on emoluments.
- **Local Service Tax** — payroll-deducted local tax.
- **Workers' Compensation Act** — injury/occupational-disease compensation.
- **Employment (Sexual Harassment) Regulations 2012** — anti-harassment policy and complaints procedure.
- **Occupational Safety and Health Act** — workplace safety duties.
- **Data Protection and Privacy Act 2019 (DPPA)** — handling of employee personal data.
- **Whistleblowers Protection Act 2010** — protected disclosures.

Cite the Act in the relevant chapter; place the actual rate/threshold/minimum in the Statutory Schedule appendix only.

## Manual chapter map (HR-owned vs finance-deferred)

| # | Chapter | Owner | Substance source |
|---|---|---|---|
| 1 | Introduction, scope, definitions, employment categories, guiding principles | HR-owned | this blueprint; `country-context/uganda` |
| 2 | Recruitment & selection (workforce planning, advertising, shortlisting, interview, reference & background checks, equal opportunity) | HR-owned | Employment Act 2006; this blueprint |
| 3 | Employment contracts & probation (offer, contract types, probation within the legal ceiling, confirmation) | HR-owned | Employment Act 2006 (probation/notice minimums → Statutory Schedule) |
| 4 | Job grading & descriptions (grade structure, job descriptions, salary bands) | HR-owned (band figures are parameters) | this blueprint; band amounts client-set |
| 5 | Working hours & attendance (hours, overtime, public holidays, timekeeping, remote/flexi) | HR-owned | Employment Act 2006 (hours/overtime → Statutory Schedule) |
| 6 | Leave (annual, sick, maternity, paternity, compassionate, study, unpaid) | HR-owned (days above statutory minimum are parameters) | Employment Act 2006 (statutory minimums → Statutory Schedule) |
| 7 | **Compensation & payroll** (salary structure, monthly payroll, statutory deductions PAYE/NSSF/LST, pay slips, pay day) | **Finance-deferred** | `04-subledgers-and-operations/payroll-and-statutory-postings-east-africa`; rates via Statutory Schedule |
| 8 | **Allowances & per diem** (travel/per diem, board sitting allowances, vehicle & driver rules, claims) | **Finance-deferred** | `04-subledgers-and-operations/expense-management-and-staff-claims`; `doctrine/references/uganda-ngo-financial-management-patterns.md` (allowance patterns) |
| 9 | **Staff advances** (salary advances capped & recovered over set months, housing advances, accountability) | **Finance-deferred** | `04-subledgers-and-operations/expense-management-and-staff-claims`; NGO patterns (advance patterns) |
| 10 | Performance management (appraisal cycle, objectives, ratings, performance improvement) | HR-owned | this blueprint |
| 11 | Learning & development (training needs, study support, bonding) | HR-owned | this blueprint |
| 12 | Code of conduct & ethics (conduct, conflict of interest, gifts, confidentiality, whistleblowing) | HR-owned (whistleblowing cross-ref) | `10-controls-governance-and-fraud/whistleblowing-and-finance-ethics` |
| 13 | Discipline & grievance (offences, staged warnings, hearing, appeal; grievance route) | HR-owned | Employment Act 2006 (fair-procedure principles) |
| 14 | Anti-harassment & safeguarding (sexual harassment, child/beneficiary safeguarding, PSEA) | HR-owned | Employment (Sexual Harassment) Regulations 2012 |
| 15 | Occupational safety & health (duties, first aid, incident reporting, workers' compensation) | HR-owned | Occupational Safety and Health Act; Workers' Compensation Act |
| 16 | Separation & clearance (resignation, termination, redundancy, retirement, exit interview, clearance, final dues) | HR-owned (notice/redundancy minimums → Statutory Schedule; final-dues mechanics cross-ref finance) | Employment Act 2006; finance manual for final-pay computation |
| 17 | Employee-data protection & records retention | HR-owned | `15-security-privacy-and-continuity/finance-data-privacy-and-retention`; DPPA 2019 |
| 18 | Appendices: HR forms pack, Statutory Schedule, version control | HR-owned | this blueprint + `doctrine/references/uganda-compliance-caveats.md` |

Chapters 7–9 state the HR-facing rule (who is entitled to what, on what conditions) and cross-reference the finance manual for the accounting, posting, and control treatment. They must not restate payroll/allowance/advance accounting — that lives in the finance engine and the finance manual.

## Statutory Schedule appendix (dated, live-verified)

A single dated table holding every employment-law minimum and tax/social-security rate, separated from the policy body so the manual does not go stale:

- **Employment-law minimums** — minimum annual leave, sick-leave entitlement, maternity and paternity leave, maximum probation period, minimum notice periods by length of service, overtime/hours limits, redundancy/severance entitlement, minimum wage (if applicable). Source: Employment Act 2006 and subsidiary regulations.
- **Tax & social security** — PAYE bands/rates, NSSF employee and employer contribution rates, Local Service Tax bands. Source: Income Tax Act, NSSF Act, Local Service Tax framework; verify via `doctrine/references/uganda-compliance-caveats.md`.

Each entry carries the figure, the source citation, the verification date, and the next review date. The manual body references "the current rate/minimum per the Statutory Schedule", never a number. **Verify every entry against current Uganda law at issue — this skill does not give legal advice.**

## Parameterisation rule

Everything the entity must choose is a **parameter with an owner and a review date**, presented as a default-to-be-approved, not a hardcoded fact:

> "Annual leave: **[____] working days** (statutory minimum per the Statutory Schedule; recommended entity default 21 working days) — set by the Board/Management, reviewed annually."
>
> "Salary advance: capped at **[____]** of monthly gross (recommended one month), recovered over **[____] months** (recommended up to 3), one advance at a time — set by Management per the finance manual."

Statutory minimums and rates are NOT parameters — they live in the dated **Statutory Schedule** and are verified against the live source register at issue. A parameter may sit *at or above* a statutory minimum, never below it; flag any choice that approaches the legal floor.

## Standard HR forms / templates pack (appendix)

Employment contract (by category); job description template; job-requisition/recruitment-approval form; interview-assessment & reference-check form; leave application & leave record card; payroll sheet & pay slip (cross-ref finance manual); staff salary/housing-advance request & accountability form (cross-ref finance manual); per-diem/travel & board-sitting-allowance claim form (cross-ref finance manual); performance-appraisal form; performance-improvement plan; training request & bonding agreement; disciplinary notice / warning letter & disciplinary-hearing record; grievance form; incident/accident report; exit interview & staff clearance form; final-dues computation sheet (cross-ref finance manual); code-of-conduct attestation; anti-harassment/safeguarding acknowledgement. Tailor the list to the entity's actual employment categories and processes — do not ship forms for processes it does not run.

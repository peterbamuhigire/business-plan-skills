---
name: hr-policy-manual
description: Use when authoring an HR policy manual for an East African NGO, SME, SACCO, project, or public-adjacent body; use `governance-and-board-charter` for board authority, verify current employment law, and defer payroll, allowances, advances, and staff costs to Chwezi Accounting Doctrine.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# HR Policy Manual

A consulting-deliverable skill: it produces a standalone Human Resources Policy Manual, not a business-plan section. It owns the document's structure, the consulting workflow, the parameter-setting, and the East African labour-law framing — and, for the money-touching chapters (compensation, payroll, allowances, staff advances), it pulls the substance from the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine` rather than improvising. The rest is standard HR grounded in Uganda labour law.

## Use When

- A client needs an **HR Policy Manual**, **Human Resources Policies & Procedures Manual**, **staff handbook / conditions of service**, **code of conduct**, or a **discipline-and-grievance / safeguarding framework**.
- Responding to an RFP/EOI for "development of a human resources policy manual / staff handbook."
- Reviewing, gap-auditing, or updating an existing HR manual against current practice and Uganda labour law.

## Do Not Use When

- The deliverable is a finance manual — use `advisory-deliverables/finance-policy-and-manual` (payroll is one chapter there; this skill is the full standalone HR manual).
- Writing a business-plan team/management section — use the relevant `pipeline` skill.
- The request is a pure finance, IT, or procurement manual with no people-management content — use the matching advisory-deliverable skill.
- Giving legal advice on a specific employment dispute — this skill states policy, not legal opinion; refer to counsel.

## Required Inputs

Entity type (NGO/CSO, SME, SACCO/cooperative, donor-funded project, public/LG-adjacent body); legal form, registration (URSB/NGO Bureau), and funding model (donor-restricted, own revenue, mixed); headcount, employment categories (permanent, contract, casual, volunteer, consultant), and any existing grading structure; whether a recognised union or staff association exists; any existing HR policies, staff handbook, or conditions of service; board/committee structure and the HR/management approver; payroll software and the finance manual it sits under; jurisdiction (default Uganda); named approver/owner. Never fabricate these — ask.

## Workflow

1. **Intake & scope.** Fix entity type, the document(s) wanted, headcount and employment categories, jurisdiction, and whether a union/CBA applies. If a manual exists, run a gap audit against the blueprint before drafting.
2. **Select the blueprint.** Load `references/document-blueprint.md` for the chapter map, the HR-owned vs finance-deferred split, and the forms list.
3. **Draft the HR-owned chapters from Uganda labour law — cite, do not hardcode.** Recruitment, contracts & probation, grading, hours & attendance, leave, performance, learning, code of conduct, discipline & grievance, anti-harassment & safeguarding, occupational safety & health, separation & clearance, and employee-data protection. Cite the governing Act (Employment Act 2006, OSH Act, DPPA 2019, etc.); put every minimum (leave, notice) in the Statutory Schedule, not the body.
4. **Pull the money-touching chapters from the finance engine — do not improvise.** For compensation & payroll, statutory deductions, pay slips, allowances/per diem, board sitting allowances, and staff/housing advances, read the mapped finance-engine `SKILL.md` plus `doctrine/references/uganda-ngo-financial-management-patterns.md`. The blueprint carries the chapter→skill map. These chapters state the HR rule and cross-reference the finance manual; they do not restate accounting treatment.
5. **Set every entity choice as a named client parameter.** Grades and salary bands, leave days above the statutory minimum, allowance amounts, advance caps and recovery months, probation length within the legal ceiling, notice periods at or above statute — each a default-to-be-approved with an owner and a review date. Never copy another entity's figures verbatim.
6. **Keep statutory rates and minimums OUT of the body.** PAYE, NSSF (employee + employer), Local Service Tax, minimum statutory leave, and minimum notice go into a dated, verified **Statutory Schedule appendix** that points to the live source register — so the manual does not go stale. The body references "the current rate/minimum per the Statutory Schedule."
7. **Add governance, ethics, and safeguarding.** Code of conduct and conflict-of-interest; whistleblowing (cross-referenced to the finance-ethics skill); anti-harassment and child/beneficiary safeguarding; the disciplinary and grievance procedures with their committees and appeal route.
8. **Add forms and version control.** The standard HR forms appendix and a review-and-amendment page with effective date and approver.
9. **Run the quality gates.** `meta-utility/anti-ai-slop` (live), `meta-strategy/meta-critical-thinking-business-logic`, and the finance engine's conformance scan where payroll/allowance/advance content appears. Record each gate run in the artefact manifest.
10. **Produce the deliverable.** Client-ready DOCX/PDF (use the document engines), plus an adoption checklist: board/management approval, effective date, and staff orientation plan.

## Quality Bar

Every policy statement is specific and enforceable (no "staff will behave professionally"); every entity choice is a named parameter with an owner and a review date; statutory minimums and tax/NSSF rates are never hardcoded in the body but live in the dated Statutory Schedule; each HR-owned chapter cites the governing Uganda Act; the money-touching chapters defer to the finance manual rather than restating it; discipline and grievance follow a fair, staged, documented process with a defined appeal; safeguarding and anti-harassment are present even for a small team; and the document passes anti-ai-slop. British English throughout. The manual states policy, not legal advice, and flags that employment-law minimums must be verified against current Uganda law at issue.

## Anti-Patterns

- Hardcoding leave days, notice periods, PAYE/NSSF/LST rates, or the minimum wage in the manual body instead of the dated, verified Statutory Schedule.
- Copying one organisation's grades, salary bands, allowance amounts, or advance caps verbatim into another.
- Restating payroll, allowance, or staff-advance accounting in the HR manual instead of deferring to the finance engine and cross-referencing the finance manual.
- Shipping a generic staff handbook full of `[bracketed placeholders]` instead of client-parameterised policy.
- Setting probation, notice, or leave below the statutory minimum, or a disciplinary process with no warnings, hearing, or appeal.
- Dropping safeguarding, anti-harassment, or grievance sections because the entity is "too small".
- Presenting policy as legal advice, or asserting a statutory minimum as current without verifying it against the live source.

## Outputs

HR Policy Manual / staff handbook; job-grading and salary-band structure (parameters); leave framework; code of conduct and conflict-of-interest policy; discipline and grievance procedures; anti-harassment and safeguarding policy; OSH policy; separation and clearance procedure; employee-data-protection policy; HR forms pack; dated Statutory Schedule appendix; adoption and version-control page; quality-gate manifest.

## References

- `references/document-blueprint.md` — chapter map (HR-owned vs finance-deferred), the chapter→doctrine-skill mapping for the money-touching chapters, the Statutory Schedule concept, the parameterisation rule, and the standard forms list.
- Finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`): `skills/04-subledgers-and-operations/payroll-and-statutory-postings-east-africa`, `skills/04-subledgers-and-operations/expense-management-and-staff-claims`, `skills/10-controls-governance-and-fraud/whistleblowing-and-finance-ethics`, `skills/15-security-privacy-and-continuity/finance-data-privacy-and-retention`, and `doctrine/references/uganda-compliance-caveats.md` / `uganda-ngo-financial-management-patterns.md`.
- `country-context/uganda/SKILL.md` for institutions, regulatory bodies, and labour market; `language/east-african-english` for style.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Existing HR policies, contracts, organogram, grading, benefits, cases, and staff feedback | Client HR and governance records | Required | Produce a gap and evidence request; do not invent current terms |
| Entity type, workforce categories, locations, collective terms, and funding restrictions | Client and verified authorities | Required | Keep affected clauses parameterised and provisional |
| Current labour, payroll, benefits, tax, and privacy requirements | Verified legal sources and Chwezi Accounting Doctrine | Required for affected chapters | Stop those chapters pending current-source and professional review |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| HR Policy Manual | Board, management, HR, supervisors, staff, and assurance reviewers | Employment lifecycle, authority, fair process, records, exceptions, and appeal routes are explicit |
| Statutory and policy parameter schedule | HR and finance owners | Every changing rate, entitlement, threshold, or form has a source, effective date, owner, and review date |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Clause traceability register | Clause-to-source-to-owner matrix | Legal, contractual, donor, and finance-dependent clauses are sourced and reviewable |
| Finance and professional-review record | Chapter gate log | Payroll, allowances, advances, benefits, deductions, and staff costs pass current Chwezi doctrine and qualified review |

## Capability Contract

Default to read-only inspection of confidential HR records and minimise personal data. Edit only the authorised manual. Do not decide an individual case, change employment terms, run payroll, access unnecessary personnel data, or certify legal compliance without explicit authority and qualified review.

## Degraded Mode

If current law, client evidence, confidential-case access, or finance doctrine is unavailable, return a core policy architecture, parameter schedule, and evidence request. Mark legal and payroll conclusions `not assessed`; never infer entitlement or misconduct.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Law or contract grants a higher minimum than draft policy | Apply the higher binding requirement | Unlawful under-provision |
| A rule depends on worker category or location | Separate the applicable schedules | Applying the wrong terms |
| A case needs investigation or hearing | Preserve due process and impartial authority | Predetermined discipline |
| Clause affects payroll, allowance, advance, benefit, or deduction | Apply Chwezi doctrine and professional review | Payroll or tax misstatement |

## Workflow

1. Confirm entity, workforce, locations, audience, confidentiality boundary, and approval route.
2. Inventory existing terms, cases, systems, roles, benefits, findings, and staff concerns.
3. Map the employment lifecycle and binding legal, contractual, donor, privacy, and finance sources; stop where a load-bearing rule cannot be verified.
4. Agree the manual architecture and controlled parameter schedule before drafting changing values.
5. Draft fair procedures with roles, notice, evidence, decision, appeal, records, and exceptions.
6. Reconcile payroll and money-touching chapters against current Chwezi doctrine and qualified professional review.
7. Test recruitment, leave, grievance, discipline, exit, and payroll-change cases; repair gaps before release.
8. Issue only with approval status, review dates, privacy controls, and unresolved legal questions visible.

## Quality Standards

The manual must be lawful, fair, usable by supervisors, respectful of privacy, and consistent across contracts, payroll, and governance. Time-sensitive legal and finance content must be sourced, dated, and professionally reviewed.

## Anti-Patterns

- Copying a generic leave table. Fix: verify jurisdiction, worker category, contract, and effective date.
- Treating discipline as an automatic penalty list. Fix: require allegation, evidence, response, impartial decision, and appeal.
- Mixing policy rules with changing rates. Fix: keep rates and thresholds in a controlled schedule.
- Collecting more personal data than the process needs. Fix: state purpose, access, retention, and deletion controls.
- Drafting payroll clauses without finance review. Fix: route pay, deductions, benefits, advances, and postings to Chwezi doctrine.
- Calling the manual legal advice or approved before sign-off. Fix: state status and required professional and competent-body review.

## Worked Example

For an employee working across two countries, do not apply the default Uganda leave schedule automatically. Identify the governing contract and work location, verify mandatory minima, record the applicable schedule, and seek legal and payroll review before issue.
<!-- dual-compat-end -->

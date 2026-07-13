---
name: grants-management-manual
description: Use when authoring a grants or donor-funds management manual for a grant recipient in East Africa; use `11b-grant-proposal` to apply for funding, and defer restricted-fund accounting, foreign exchange, reporting, and close rules to Chwezi Accounting Doctrine.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Grants Management Manual

A consulting-deliverable skill: it produces a standalone Grants / Donor-Funds Management Manual, not a business-plan section and not a grant proposal. It owns the document's structure, the grant-lifecycle workflow, the parameter-setting, the multi-currency flexing logic, and the East African framing — and it pulls every accounting treatment, eligibility rule, and compliance touchpoint from the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.

## Use When

- A client needs a **Grants Management Manual**, **Donor-Funds Management Manual**, **Grant Accounting & Compliance Manual**, **sub-granting policy**, or a **fund-accounting / donor-reporting procedures** document.
- Responding to an RFP/EOI for "development of a grants / donor-funds management manual."
- Reviewing, gap-auditing, or updating an existing grants manual against current standards and donor terms.

## Do Not Use When

- **Writing a grant proposal or concept note — use `pipeline/11b-grant-proposal`.** That skill *wins* funding; this manual governs how received funds are *managed*.
- The grants chapter is one part of a broader finance manual — use `advisory-deliverables/finance-policy-and-manual` (grants is one chapter there; this skill is the full standalone manual).
- Answering a single grant-accounting question — go straight to the relevant finance-engine `SKILL.md`.

## Required Inputs

Entity type (NGO/CSO, donor-funded project, grant-receiving public body); legal form, registration (URSB/NGO Bureau), and funding model (single-donor, multi-donor, sub-granting up- or down-stream); the donor portfolio and each donor's binding rules (World Bank, USAID ADS, EU/GIZ, AfDB, UN/UNDP, bilateral); reporting framework (IFRS for SMEs or full IFRS / IAS 20); functional currency and grant currencies; whether sub-granting is in scope; existing manual/policies; board and committee structure; accounting software and chart of accounts in use; jurisdiction (default Uganda); named approver/owner. Never fabricate these — ask.

## Workflow

1. **Intake & scope.** Fix entity type, the donor portfolio, functional/grant currencies, whether sub-granting applies, framework, and software. If a manual exists, run a gap audit against the blueprint before drafting.
2. **Select the blueprint.** Load `references/document-blueprint.md` for the grant-lifecycle spine, the multi-currency flexing logic, the parameterisation rule, and the forms list.
3. **Pull accounting substance from the doctrine — do not improvise.** For each chapter read the mapped finance-engine `SKILL.md` plus `doctrine/references/uganda-ngo-financial-management-patterns.md`. The blueprint carries the chapter→skill map. Grant recognition is **deferred-income** (IAS 20 / Section 24), not the capital approach.
4. **Layer donor rules on top, stricter rule wins.** Read the relevant `proposal-skills` donor packs (`sectors/world-bank`, `sectors/undp`, `sectors/afdb`, `domain-delivery/giz-eu-local-procurement-response`). The manual states the organisation's baseline; each donor's stricter terms override per grant.
5. **Set every figure as a named client parameter.** Retirement days, advance caps, capitalisation threshold, retention period, surprise-count frequency — each is a default-to-be-approved with an owner and a review date. Never copy another entity's figures verbatim.
6. **Keep statutory rates OUT of the body.** WHT-at-source on grant payments, VAT treatment, PAYE on grant-funded staff go into a dated, verified **Statutory Schedule appendix** that cites the live source register — so the manual does not go stale.
7. **Build the fund-control core.** Restricted vs unrestricted; unspent restricted grants as **deferred income (a liability)**; a separate bank account and cost centre per donor; a chart of accounts that **mirrors each grant budget line**; the multi-currency flexing logic.
8. **Add sub-granting, audit & close-out, governance, and forms.** Sub-grant agreement and retirement rules; donor-audit and ineligible-cost-recovery clauses; grant close-out and asset disposition; the forms appendix; and a review/version-control page.
9. **Run the quality gates.** `meta-utility/anti-ai-slop` (live), `meta-strategy/meta-critical-thinking-business-logic`, and the finance engine's `finance-doctrine-conformance-scanner` / `finance-module-audit`. Record each gate run in the artefact manifest.
10. **Produce the deliverable.** Client-ready DOCX/PDF (use the document engines), plus an adoption checklist: board resolution, effective date, and staff training plan.

## Quality Bar

Restricted and unrestricted funds are never commingled; unspent restricted grants are carried as deferred income, not revenue; every donor has a separate bank account, cost centre, and budget-mirrored coding; the chart of accounts maps line-for-line to each grant budget; multi-currency flexing uses the weighted-average rate from actual disbursements and variance is measured against the flexed budget; cost eligibility is tested as Reasonable / Allocable / Allowable with an unallowable-cost list; every figure is a named parameter with an owner and review date; statutory rates are never hardcoded in the body; donor rules are layered with "stricter rule wins"; and it passes anti-ai-slop and the doctrine conformance scan. British English throughout.

## Anti-Patterns

- Confusing this manual with a grant proposal — `pipeline/11b-grant-proposal` writes proposals; this governs received funds.
- Recognising a restricted grant as income on receipt instead of carrying the unspent balance as **deferred income**.
- Commingling donor funds in one bank account or one cost centre, or coding to a chart that does not mirror the grant budget.
- Measuring variance against the original budget after a currency move, instead of against the **flexed budget** at the weighted-average rate.
- Embedding WHT/VAT/PAYE rates in the manual body instead of the live-verified Statutory Schedule.
- Advancing to a sub-grantee with no board-approved sub-grant agreement, or letting retirements drift past the month-end deadline.
- Asserting an IAS 20 / Section 24 treatment without reading the mapped finance-engine skill.
- Treating a donor's financial rules and the entity's manual as interchangeable — layer both, stricter wins.

## Outputs

Grants / Donor-Funds Management Manual; donor register and acknowledgement procedure; fund-accounting and deferred-income procedures; dual-currency budgeting and flexing procedure; cost-eligibility framework + unallowable-cost list; sub-granting policy and forms; donor-reporting (budget-vs-actual-vs-variance) templates; audit and close-out procedures; forms-and-templates pack; dated Statutory Schedule appendix; adoption and version-control page; quality-gate manifest.

## References

- `references/document-blueprint.md` — grant-lifecycle spine, chapter→doctrine-skill map, multi-currency flexing logic, parameterisation rule, and standard forms list.
- Finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`): `skills/11-sector-and-fund-accounting/ngo-and-fund-accounting`, `skills/03-ifrs-specialised-standards/ias-government-grants`, `skills/12-public-sector-and-ipsas/donor-funded-project-fiscal-compliance`, and `doctrine/references/uganda-ngo-financial-management-patterns.md`, plus the skills named in the blueprint map.
- `proposal-skills` (`C:\wamp64\www\proposal-skills`): donor packs `sectors/world-bank`, `sectors/undp`, `sectors/afdb`, `domain-delivery/giz-eu-local-procurement-response`.
- `country-context/uganda/SKILL.md` for institutions/regulatory bodies; `language/east-african-english` for style.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Award agreements, budgets, amendments, donor rules, and reporting calendars | Grantor and recipient records | Required | Build an award-data request and do not invent obligations |
| Programme, procurement, safeguarding, subaward, and close-out workflows | Recipient teams and existing manuals | Required | Mark interfaces unresolved and keep procedures provisional |
| Restricted-fund, foreign-exchange, revenue, and reporting doctrine | Chwezi Accounting Doctrine and verified grantor rules | Required | Stop financial chapters until doctrine and professional review are available |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Grants Management Manual | Programme, finance, procurement, partners, management, auditors, and donors | The award lifecycle, roles, controls, evidence, reporting, amendments, subawards, and close-out are executable |
| Award compliance and parameter register | Grant manager and assurance reviewers | Each award-specific rule has a source, owner, effective dates, threshold, and evidence requirement |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Award obligation traceability | Clause-to-process-to-evidence matrix | Every load-bearing donor obligation maps to a procedure and retained record |
| Finance doctrine gate | Chapter mapping and review status | Restricted-fund, FX, revenue, budget, and close treatments are reviewed under current Chwezi doctrine |

## Capability Contract

Read access to award records and doctrine is required. Edit only the authorised manual. Do not amend an award, move restricted funds, approve expenditure, certify a donor report, or conclude compliance without delegated authority and qualified finance, legal, or donor review.

## Degraded Mode

Fallback:

Without complete award terms, systems evidence, doctrine, or current donor sources, return a core lifecycle framework plus an award-specific parameter and evidence request. Label financial and compliance conclusions `not assessed`; never treat a missing donor rule as permission.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Award term is stricter than general policy | Apply and record the award overlay | Ineligible expenditure |
| Award and law or accounting doctrine conflict | Stop and obtain authoritative advice or donor clarification | Breach or misstatement |
| Cost, output, or timing change exceeds approved flexibility | Route a formal amendment before commitment | Unauthorised rebudgeting |
| Financial treatment touches restricted funds, FX, revenue, or close | Apply Chwezi doctrine and professional review | Misstated grant balances or reports |

## Workflow

1. Confirm recipient type, grant portfolio, jurisdictions, users, and approval route.
2. Inventory award terms, budgets, systems, findings, partner arrangements, and reporting obligations.
3. Map the full award lifecycle and interfaces with finance, procurement, HR, safeguarding, and programme delivery.
4. Build the award compliance register; stop where a binding obligation lacks source evidence.
5. Draft procedures, roles, evidence, exceptions, amendment routes, subaward controls, and close-out checks.
6. Reconcile money-touching rules against current Chwezi doctrine and qualified professional review.
7. Test one new award, one rebudgeting case, one partner advance, and one close-out; repair failures at the register or procedure level.
8. Release only with donor-specific parameters, unresolved issues, and approval status visible.

## Quality Standards

The manual must separate reusable lifecycle rules from award-specific overlays, trace obligations to evidence, and keep financial treatment consistent with current doctrine. Donor, legal, accounting, and audit claims remain qualified until reviewed.

## Anti-Patterns

- Using one donor's rules for every award. Fix: maintain an award-specific compliance overlay.
- Treating a signed budget as permission to ignore cost categories. Fix: apply flexibility and amendment rules explicitly.
- Omitting partner and subaward controls. Fix: define due diligence, agreement, advance, reporting, monitoring, and close-out evidence.
- Recording grant income by intuition. Fix: route recognition and restricted-fund accounting to Chwezi doctrine.
- Hiding exchange-rate assumptions in a spreadsheet. Fix: document source, date, method, variance, and approval.
- Certifying close-out before assets, advances, records, and reports reconcile. Fix: use a signed close-out checklist and professional review.

## Worked Example

If a donor permits a ten per cent budget-category variance but the proposed move is larger, record the source clause, pause the commitment, prepare the amendment request, and keep the forecast conditional until written donor approval and finance review are obtained.
<!-- dual-compat-end -->

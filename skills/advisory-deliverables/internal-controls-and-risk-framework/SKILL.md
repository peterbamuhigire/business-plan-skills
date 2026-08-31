---
name: internal-controls-and-risk-framework
description: Use when authoring an internal-control policy, risk-management framework, control matrix, or risk register for an East African organisation; use `finance-policy-and-manual` for finance procedures and defer accounting controls, audit evidence, and close doctrine to Chwezi Accounting Doctrine.
metadata:
  portable: true
  compatible_with: [claude-code, codex]
---

# Internal Controls and Risk Framework

A consulting-deliverable skill: it produces a standalone organisational document — an **Internal Control & Risk Management Framework** — not a business-plan section. It owns the document's structure, the consulting workflow, the control and risk parameterisation, and the East African regulatory framing — and it pulls every control design, fraud test, and risk-treatment substance from the finance engine at `C:\wamp64\www\chwezi-accounting-doctrine`.

## Use When

- A client needs an **Internal Control & Risk Management Framework**, **Internal Control Policy**, **segregation-of-duties / authorisation framework**, **ICFR documentation pack** (process narratives, risk-control matrices, walkthroughs), **fraud-risk / anti-fraud policy**, **whistleblowing policy**, or an **enterprise risk register and risk-management policy**.
- Responding to an RFP/EOI for "development of an internal control and risk management framework / risk register."
- Reviewing, gap-auditing, or maturing an existing control environment against COSO ERM / ISO 31000 and the entity's actual cycles.

## Do Not Use When

- Writing the internal-control chapter *inside* a finance manual — use `advisory-deliverables/finance-policy-and-manual` (controls are one chapter there; this skill is the full standalone framework).
- Producing a standalone procurement manual — use `advisory-deliverables/procurement-policy-and-manual`.
- Writing a business-plan risk section — use `pipeline/12-risk-analysis`.
- Answering a single control-design or fraud-test question — go straight to the relevant finance-engine `SKILL.md`.

## Required Inputs

Entity type (NGO/CSO, SME, SACCO/cooperative, donor-funded project, public/LG-adjacent body); legal form, registration (URSB/NGO Bureau), and funding model (donor-restricted, own revenue, mixed); reporting framework and whether ICFR-style assertion documentation is required; existing controls, policies, or risk register; board and committee structure (Audit/Risk committee, internal audit function); operating cycles in scope (cash, procurement, payroll, assets, grants); risk appetite signals from the board; jurisdiction (default Uganda) and whether public-sector surcharge/liability applies; named approver/owner. Never fabricate these — ask.

## Workflow

1. **Intake & scope.** Fix entity type, the document(s) wanted (Framework, Policy, ICFR pack, risk register), the cycles in scope, jurisdiction, and whether a public-sector surcharge overlay applies. If a framework or register exists, run a gap audit against the blueprint before drafting.
2. **Select the blueprint.** Load `references/document-blueprint.md` for the chapter map, the control set rendered as tables, the risk-register method, and the chapter→doctrine-skill map.
3. **Pull control and risk substance from the doctrine — do not improvise.** For each chapter read the mapped finance-engine `SKILL.md` (the blueprint carries the map), anchored on `10-controls-governance-and-fraud/internal-controls-library` and `sox-style-icfr-documentation`, plus `doctrine/references/uganda-ngo-financial-management-patterns.md` (NGO) or `uganda-public-sector-pfm.md` (public).
4. **Draft section by section.** Set every threshold, signatory count, authorisation tier, reconciliation cadence, and review frequency as a **named client parameter**. Propose defaults from the Uganda patterns (clearly flagged "to be board-approved"), never copied verbatim from another entity.
5. **Keep statutory rates and figures OUT of the body.** Any surcharge/pecuniary-liability figures, statutory penalty rates, or tax touchpoints go into a dated, live-verified **Statutory Schedule appendix** that points to the source register — so the framework does not go stale.
6. **Build the control set as tables.** Segregation-of-duties matrix, amount-keyed authorisation matrix, control-activity matrix by cycle (cash/bank, procurement, payroll, assets), and the bank-signatory mandate — from `internal-controls-library` plus the NGO/public patterns. No person occupies two adjacent links of the control chain.
7. **Build the risk-management layer.** Risk register (probability × impact, owner, mitigation, monitoring), risk appetite statement, and control self-assessment — to ISO 31000 / COSO ERM, cross-referencing `srs-skills` `09-governance-compliance/04-risk-assessment` and `pipeline/12-risk-analysis` for method. For public bodies, layer pecuniary-liability / surcharge per the LG (Financial & Accounting) Regulations 2007.
8. **Add fraud, ethics, monitoring, forms, and version control.** Fraud-risk and forensic indicators; whistleblowing per the Whistleblowers Protection Act 2010; conflict-of-interest registers and clearance-on-exit; the internal-audit / monitoring function; the standard forms-and-registers appendix; and a review-and-amendment page with effective date and approver.
9. **Run the quality gates.** `meta-utility/anti-ai-slop` (live), `meta-strategy/meta-critical-thinking-business-logic`, and the finance engine's `finance-doctrine-conformance-scanner` / `finance-module-audit`. Record each gate run in the artefact manifest.
10. **Produce the deliverable.** Client-ready DOCX/PDF (use the document engines), plus an adoption checklist: board/Audit-committee resolution, effective date, control-owner assignment, and staff training plan.

## Quality Bar

Every control statement is specific and testable (no "adequate controls" — name the control, owner, frequency, and evidence); segregation of duties holds even for a three-person team, with no person in two adjacent links and nobody approving in their own favour; every threshold, signatory rule, and cadence is a named parameter with an owner and review date; the risk register carries probability × impact, owner, mitigation, and monitoring against a stated appetite; statutory/surcharge figures are never hardcoded in the body; the framework maps to the entity's actual cycles and to ICFR assertions where required; the public-sector surcharge overlay is applied only where it governs; and it passes anti-ai-slop and the doctrine conformance scan. British English throughout.

## Anti-Patterns

- Vague controls ("controls are in place", "management reviews regularly") instead of named control, owner, frequency, and evidence.
- Dropping the SoD matrix or collapsing the request→approve→disburse→account→review chain because the entity is "too small".
- Letting one person occupy two adjacent links, approve in their own favour, or combine procurer, approver, and inventory-keeper roles.
- Embedding surcharge, penalty, or tax figures in the body instead of the live-verified Statutory Schedule.
- A risk register that lists risks without probability × impact, owner, mitigation, monitoring, or a stated risk appetite.
- Copying one organisation's thresholds, signatory rules, or appetite statements verbatim into another.
- Asserting a control or fraud-test design without reading the mapped finance-engine skill.
- Bolting on the public-sector surcharge overlay for a private NGO, or omitting it for a body it governs.

## Outputs

Internal Control & Risk Management Framework; Internal Control Policy; SoD, authorisation, and control-activity matrices; ICFR documentation pack (process narratives, risk-control matrices, walkthroughs) where required; enterprise risk register + risk-appetite statement; fraud-risk and whistleblowing policy; forms-and-registers pack (risk register, CoI register, control self-assessment checklist, exception/incident log, whistleblowing intake form); dated Statutory Schedule appendix; adoption and version-control page; quality-gate manifest.

## References

- `references/document-blueprint.md` — chapter map, chapter→doctrine-skill mapping, control set as tables, risk-register method, parameterisation rule, and the standard forms/registers list.
- Finance engine (`C:\wamp64\www\chwezi-accounting-doctrine`): `skills/10-controls-governance-and-fraud/` (`internal-controls-library`, `sox-style-icfr-documentation`, `forensic-accounting-and-anti-fraud`, `whistleblowing-and-finance-ethics`, `aml-kyc-and-suspicious-transaction-reporting`, `engagement-quality-and-plain-language-output`); `skills/06-close-consolidation-and-reporting/audit-pbc-and-evidence-management`; `doctrine/references/uganda-ngo-financial-management-patterns.md`, `uganda-public-sector-pfm.md`, `uganda-compliance-caveats.md`.
- Cross-engine risk method: `srs-skills/09-governance-compliance/04-risk-assessment`; `business-plan-skills/skills/pipeline/12-risk-analysis`.
- `country-context/uganda/SKILL.md` for institutions/regulatory bodies; `language/east-african-english` for style.

<!-- dual-compat-start -->
## Inputs

| Artefact | Source or provider | Required? | If absent |
|---|---|---|---|
| Objectives, processes, systems, incidents, audits, and existing controls | Client records, walkthroughs, and interviews | Required | Return a scoped evidence request, not an invented risk assessment |
| Risk appetite, authority, legal, donor, and sector obligations | Board records and verified authorities | Required | Mark appetite and compliance scoring provisional |
| Finance controls and audit-evidence doctrine | Chwezi Accounting Doctrine | Required for money-touching risks | Stop finance-control conclusions pending doctrine and professional review |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Internal Control and Risk Management Framework | Board, management, process owners, assurance, auditors, and funders | Governance, risk method, control design, reporting, incidents, and review are operational |
| Risk register and control matrix | Risk owners and assurance reviewers | Risks link to causes, impacts, appetite, controls, evidence, owner, action, and residual rating |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Risk-control-evidence traceability | Matrix with test and exception fields | Every key control has an owner, frequency, evidence, test, failure route, and remediation date |
| Finance quality-gate record | Doctrine and professional-review log | Money-touching controls map to current Chwezi doctrine and unresolved review blocks certification |

## Capability Contract

Audit and assessment default to read-only. Edit the framework only when authorised. Do not change production controls, access rights, transactions, risk acceptance, whistleblowing records, or audit conclusions without explicit competent authority; never certify control effectiveness without test evidence.

## Degraded Mode

Without walkthroughs, samples, system access, doctrine, or current legal sources, distinguish design review from operating-effectiveness testing and mark inaccessible checks `not assessed`. Return the narrowest risk register and evidence plan that the available facts support.

## Decision Rules

| Choice | Action | Failure or risk avoided |
|---|---|---|
| Risk exceeds appetite and no effective control exists | Escalate and define a dated treatment before acceptance | Unowned material exposure |
| Control exists only in policy | Rate design only; test operation separately | False assurance |
| Segregation is impractical | Add documented compensating review and monitoring | Uncontrolled concentration of duties |
| Risk touches finance, tax, assets, payroll, grants, banking, or reporting | Apply Chwezi doctrine and professional review | Misstated control objective or evidence |

## Workflow

1. Confirm objectives, scope, users, assurance level, risk criteria, and authority.
2. Map processes, assets, obligations, incidents, findings, systems, and dependencies.
3. Identify risks through causes, events, impacts, existing controls, and evidence; stop where a material process cannot be observed.
4. Score inherent risk, assess control design, and separate design from tested operation.
5. Define treatments, owners, dates, indicators, escalation, and residual risk decisions.
6. Apply Chwezi doctrine and qualified review to all money-touching controls and audit evidence.
7. Test representative controls and exception paths; recover by narrowing conclusions or adding evidence work, never by upgrading an untested rating.
8. Release with limitations, risk acceptance, action status, and review cadence visible.

## Quality Standards

Risk ratings must be reasoned, controls testable, evidence retained, and limitations explicit. A control is effective only when both design and operating evidence support that conclusion; finance assertions require the Chwezi gate.

## Anti-Patterns

- Listing generic risks with no cause or impact. Fix: write a specific cause-event-impact statement.
- Calling a policy clause an effective control. Fix: identify execution evidence and test a sample.
- Combining ownership and independent review in one role. Fix: separate or document a compensating control.
- Scoring every risk high to appear cautious. Fix: apply agreed criteria and record rationale.
- Reusing a finance control without doctrine mapping. Fix: verify objective, posting, reconciliation, and evidence under Chwezi doctrine.
- Hiding untested areas in an overall green rating. Fix: mark them `not assessed` and qualify the conclusion.

## Worked Example

Where one staff member creates and pays suppliers, rate the segregation risk, verify whether an independent bank and supplier-master review actually operates, sample its evidence, and keep operating effectiveness unassessed if records are unavailable.
For NGO cyber-resilience investment and control capacity, load [NGO cyber-resilience investment conditions](references/ngo-cyber-resilience-investment-conditions.md).

<!-- dual-compat-end -->

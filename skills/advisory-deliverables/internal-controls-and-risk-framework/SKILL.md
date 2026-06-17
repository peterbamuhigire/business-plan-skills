---
name: internal-controls-and-risk-framework
description: Author a client-ready Internal Control & Risk Management Framework (and matching Internal Control Policy) for NGOs, SMEs, SACCOs, donor-funded projects, and public/LG bodies in Uganda/East Africa. Owns document architecture, the consulting workflow, control parameterisation, the risk-register method, and East African context; defers control and accounting substance to the Chwezi finance engine. Grounded in real Ugandan financial manuals, COSO ERM / ISO 31000, the Whistleblowers Protection Act 2010, and the LG (Financial & Accounting) Regulations 2007.
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

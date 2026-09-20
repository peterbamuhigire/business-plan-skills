---
name: meta-operational-readiness-due-diligence
description: Use when testing whether a business plan's operating model is locally executable across banking, tax, licensing, payroll, FX, compliance, logistics, privacy, government interface, and partnerships; use section skills for prose drafting.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Operational Readiness Due Diligence

<!-- dual-compat-start -->
## Use When

- A plan must demonstrate that its operating model can work in a named country or market.
- Banking, tax, licences, payroll, FX, compliance, logistics, privacy, public-sector interface, or local-partner assumptions affect viability.
- A plan needs one cross-section readiness matrix before operations, financial projections, risk, or investor review is finalised.

## Do Not Use When

- The request is only to draft the operations, financial-projections, or risk section; route to that section skill and add this route when cross-section readiness is material.
- The work contains current legal, tax, payroll, regulatory, privacy, banking, or FX claims but has not been routed to Digital Research and Chwezi Accounting Doctrine where applicable.

## Required Inputs

| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Country, operating sites, business model, transaction flows, currencies, regulated activities, and launch decision | Client intake and approved plan brief | Yes | Stop and return the missing context questions |
| Staffing model, payroll assumptions, vendors, logistics paths, data flows, and technology architecture | Management evidence, discovery, or approved assumptions | Yes | Mark the affected point `NOT_ASSESSED` |
| Tax, licensing, privacy, banking, FX, and compliance evidence | Digital Research source register, Chwezi doctrine, and qualified reviewers | Conditional but required for final claims | Keep the claim qualified and block certification |
| Integrated model, risk register, milestones, and funding/use-of-funds logic | Plan owners and finance model | Yes for release | Return contradictions to the owning section |

## Outputs

| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Ten-point operational-readiness matrix | Plan owner, investor/lender reviewer, and section owners | Each point has status, evidence, owner, next action, timing, and consequence |
| Banking, tax, licensing, payroll, FX, and compliance action register | Operations and finance owners | Current claims are source-linked; planning assumptions have a review date and sensitivity |
| Vendor/data/stakeholder/partnership readiness map | Operations, risk, technology, and governance owners | Dependencies, service expectations, decision rights, and fallback paths are explicit |
| Cross-section reconciliation note | Orchestrator and release reviewer | Operations, model, risk, timeline, funding ask, and assumptions agree or remain blocked |

## Evidence Produced

| Evidence | Format | Acceptance condition |
|---|---|---|
| Readiness matrix and evidence register | Markdown or structured project record | A reviewer can reproduce each status without treating a generic statement as proof |
| Assumption and sensitivity log | Model/workpaper | Currency, payroll loading, payment costs, compliance timing, and logistics effects are visible |
| Blocker and handoff log | Stage register or release bundle | Every missing or failed point has an owner, consequence, recovery action, and restart condition |

## Workflow

1. Freeze the jurisdiction, launch scope, business model, transaction flows, and decision audience. Do not start with a generic country checklist.
2. Translate the ten readiness points into observable tests:
   - banking: account, rails, limits, settlement, multi-currency, integration, reconciliation, and fallback;
   - tax: entity activity, tax classification, indirect-tax treatment, invoicing, filing surface, and reviewer route;
   - licensing: regulated activity, responsible authority, approval dependency, lead time, and launch hold point;
   - payroll: employee/contractor model, fully loaded cost, statutory source dependency, leave/termination exposure, and payment route;
   - FX: billing currency, cost currency, exposure, pricing/reset mechanism, cash buffers, and sensitivity;
   - compliance calendar: registration, filing, renewal, reporting, data, insurance, and contract milestones with owners;
   - logistics: suppliers, last-mile route, service levels, lead times, failure handling, and alternate source;
   - data protection: data classes, residency/transfer, security controls, retention, processor chain, incident route, and reviewer;
   - government interface: policy-monitoring owner, legitimate engagement channels, escalation, and conflict safeguards;
   - local partnerships: role, evidence of standing, due diligence, incentives, deliverables, and exit or substitution path.
3. Classify every item as `verified`, `context-bound`, `planning-assumption`, `partial`, or `NOT_ASSESSED`. A user-provided framework is a hypothesis source, not proof of a current rule.
4. Route current legal, tax, licensing, privacy, payroll, FX, and banking claims to Digital Research source evaluation and verification. Route money-flow, payroll, tax, banking, FX, and reporting treatment to Chwezi Accounting Doctrine and the required professional reviewer. Never hardcode a rate, deadline, exemption, or regulator outcome in this skill.
5. Test the consequence of each gap in the operating model, cash flow, margin, runway, schedule, risk register, and funding ask. Add a downside case where the gap can delay launch, increase cost, or reduce collections.
6. Reconcile the matrix with `08-operations-plan`, `10-financial-projections`, `12-risk-analysis`, implementation timing, and funding/use-of-funds. Return contradictions to the owning skill; do not silently choose the most favourable value.
7. Run a compact red-team: ask what would stop launch, freeze cash, invalidate a proposal, create an employee liability, expose customer data, or make a local partner unusable. Record the smallest evidence or experiment that would retire each blocker.
8. Release only when every material point is evidenced or explicitly accepted as a dated, owned, risk-bearing assumption. Otherwise keep the plan's readiness state blocked or `NOT_ASSESSED`.

## Decision Rules

| Finding | Action | Failure or risk avoided |
|---|---|---|
| A point is described generically, such as “open a corporate account” | Specify the operational requirement, evidence, owner, and fallback | Hidden transaction or settlement bottleneck |
| A current statutory or regulatory claim lacks a usable source entry | Quarantine it, narrow the wording, and assign a reviewer | False compliance or stale planning |
| A gap affects launch, cash, margin, data, or legal exposure | Add a hold point, downside case, owner, and recovery action | Optimistic plan that cannot execute |
| A local partner or vendor is named without role or evidence | Treat it as an unconfirmed dependency and define substitution criteria | Name-dropping and single-counterparty failure |
| Readiness improves but control, cash, privacy, or delivery quality worsens | Reject or revise the experiment and restore the safe baseline | Local optimisation |

## Quality Standards

- The matrix is country- and business-model-specific; it does not substitute for legal, tax, banking, privacy, or professional advice.
- Banking, tax, licensing, payroll, FX, and privacy entries state scope, source status, reviewer, review date, uncertainty, and decision consequence.
- Fully loaded payroll includes employer costs and contract/termination exposure without inventing statutory values.
- FX treatment connects price, settlement, cost currency, cash timing, and sensitivity to the model.
- The compliance calendar names owners and triggers; it is not a list of vague “ongoing” tasks.
- Vendor, data, government, and partnership assumptions have evidence, fallback, and exit logic.
- No plan is called bankable, investor-ready, or achievable while a material readiness blocker is unassessed.

## Capability Contract

Read, search, calculate, and draft within the authorised workspace. This skill is read-only for audit and review by default. It must not open accounts, register taxes, obtain licences, hire staff, sign vendors, lobby officials, certify compliance, submit a plan, or change approved model assumptions without explicit authority and qualified review.

## Degraded Mode

If country, source, model, reviewer, or vendor evidence is unavailable, produce only the supported matrix, return a qualified result, mark the affected item `NOT_ASSESSED`, state the exact evidence needed, and keep release blocked where the point is material. Never convert a missing check into a pass.

## Anti-Patterns

- Generic “local compliance” language. Fix: name the activity, authority, evidence, owner, and hold point.
- Base salary-only budgeting. Fix: show the loaded cost and source-dependent statutory fields.
- One exchange-rate assumption with no exposure logic. Fix: show currencies, observation date/source, reset rule, buffer, and sensitivity.
- Naming a bank, vendor, regulator, or adviser as proof. Fix: record the operational requirement and corroborating evidence.
- Treating a calendar or stakeholder list as control. Fix: add owner, trigger, evidence, escalation, and review cadence.

## Worked Example

For a proposed health-data platform in a new country, the plan may say that banking, privacy approval, a hosting route, and a local implementation partner are required. Until current authority evidence, data-flow review, partner due diligence, and a cash/timeline impact are recorded, each item remains `NOT_ASSESSED`; the model carries a launch hold point and the funding ask does not assume early revenue.

<!-- dual-compat-end -->

## References

- `skills/pipeline/08-operations-plan/SKILL.md`
- `skills/pipeline/10-financial-projections/SKILL.md`
- `skills/pipeline/12-risk-analysis/SKILL.md`
- `skills/meta-strategy/meta-due-diligence/SKILL.md`
- Digital Research Engine: `source-evaluation`, `source-verification`, and `docs/continuous-improvement/kaizen-currentness-gate.md`
- Chwezi Accounting Doctrine: `tax-statutory-source-register-and-country-packs`, `payroll-and-statutory-postings-east-africa`, `fx-management-and-hedging`, and `bank-and-mobile-money-reconciliation`

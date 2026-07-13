---
name: meta-investment-committee-red-team
description: Use when simulating a lender, DFI, VC, grant or owner-board investment committee against a complete plan, model and evidence pack; distinguishes `meta-bankability-scoring`, which scores lender readiness without adversarial committee rounds.
metadata:
  portable: true
  compatible_with:
  - claude-code
  - codex
---

# Investment Committee Red-Team

Test whether a complete funding case survives audience-specific challenge. A simulation produces
decision evidence and repair priorities; it never certifies approval or predicts a real committee.

<!-- dual-compat-start -->
## Use When

- A complete plan, financial model, funding ask and evidence pack need an adversarial pre-submission review.
- The team must rehearse lender, DFI, VC, grant-panel or owner-board questions and decision conditions.

## Do Not Use When

- Use `meta-bankability-scoring` when only a lender-readiness score and fix list are required.
- Use `meta-due-diligence` when verifying records and claims rather than simulating a decision forum.
- Use `meta-valuation` when the controlling task is to calculate enterprise or equity value.
- Do not run a decision round on an early concept with no reconciled model or funding ask.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Versioned plan and funding ask | Plan owner | Yes | Stop the decision verdict; return intake questions only. |
| Formula-audited model and assumptions | Finance owner | Yes | Mark model integrity `not assessed` and block approval. |
| Evidence and exception register | Research lead | Yes | Treat unsupported load-bearing claims as blockers, not neutral items. |
| Audience and decision mandate | Sponsor or funder brief | Yes | Do not substitute another audience's criteria. |
| Sector regulatory gate results | Regulatory gate owner | Conditional | Block affected launch, cash-flow or timing conclusions. |

## Workflow

1. Freeze input versions, audience, requested decision, authority and conflicts; remain read-only.
2. Validate the pack manifest and stop if the plan, ask, model, evidence register or audience is absent.
3. Assign audience roles from the committee framework; record each role's thesis, concern and evidence request.
4. Run independent challenge rounds for commercial logic, execution, finance, evidence, regulation and downside.
5. Apply audience-specific conditions and blockers before calculating a score; no aggregate score overrides a blocker.
6. Issue one result: `decline`, `defer`, `conditional-progress`, or `progress-for-real-review`, with dissent and repairs.
7. Recover only after the owner supplies versioned evidence, then re-run and retain the prior exception trail.

## Quality Standards

- Every challenge cites an input location or records a precise missing artefact.
- The result separates evidence, assumptions, inferences, disagreements and matters not assessed.
- Audience criteria affect the questions and conditions; lender, DFI, VC and grant rounds are not interchangeable.
- Formula, balance, scenario, tax, regulatory and evidence failures remain visible and cannot be averaged away.
- `Progress-for-real-review` means the pack may enter human review, never that funding is approved.

## Anti-Patterns

- Inventing a committee personality or objection. Fix: derive each challenge from the mandate and supplied evidence.
- Letting a high weighted score erase a blocker. Fix: apply blockers before recommendation bands.
- Using lender DSCR questions as a VC decision model. Fix: load the matching audience round.
- Calling an absent workbook check a pass. Fix: mark model integrity `not assessed` and defer.
- Rewriting the plan during an audit. Fix: stay read-only and issue owner-assigned repair actions.
- Claiming that a simulation predicts approval. Fix: state its bounded rehearsal purpose and human-review requirement.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Committee decision memorandum | Sponsor and plan owner | States decision, vote, blockers, conditions, dissent and next gate. |
| Challenge and response register | Section/model owners | Every question has evidence, an owner, a due state and acceptance condition. |
| Repair sequence | Delivery lead | Orders only decision-changing repairs and identifies re-review triggers. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Input version manifest | JSON or table | Identifies every reviewed artefact and formula/evidence gate state. |
| Audience scorecard | Structured record | Shows criterion score, rationale, evidence pointer and blocker status. |
| Dissent and exception log | Decision record | Preserves minority view, unavailable checks and unresolved conditions. |

<!-- dual-compat-end -->
## Capability Contract

The permission boundary requires only read access to the supplied plan, model audit, evidence register and gate
results, plus local execution for deterministic scoring when available. The skill defaults to
read-only. It may not edit source artefacts, contact funders, submit a pack, spend funds, certify
compliance, or represent a real committee decision without explicit authority from the owning role.

## Degraded Mode

Without execution, apply the scorecard manually and label arithmetic unverified. Without a model,
source, sector review or document, return the questions supported by available inputs and mark the
affected criterion `not assessed`; recommendation cannot exceed `defer`. Never infer a pass from
silence, inaccessible files or a polished narrative.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| Any mandatory input or audience blocker fails | `Decline` for fatal incompatibility or `defer` for remediable evidence | Attractive averages conceal an unfinanceable condition |
| No blocker, but material conditions remain | `Conditional-progress` with owners and dated acceptance tests | Vague approval leaves execution risk unowned |
| Evidence, model, gates and audience conditions pass | `Progress-for-real-review`, retaining dissent | Simulation is misrepresented as funding approval |
| Two roles disagree on a load-bearing assumption | Preserve both cases and request the deciding evidence | Consensus language hides unresolved risk |

## Worked Example

A DFI debt pack shows positive cash flow but its formula audit has not tested debt-service coverage
under delay. The finance role marks model integrity unassessed, the environmental role retains the
site-screen condition, and the committee returns `defer` with two acceptance tests. A high market
score does not change that result.

## References

- [Committee review framework](references/committee-review-framework.md) - load roles, rounds and audience-specific questions.
- [Committee scorecard](references/committee-scorecard.md) - load criteria, blocker precedence and recommendation bands.
- [Worked simulations](references/worked-simulations.md) - use to calibrate evidence-linked challenges, not copy conclusions.
- Use `../../../tools/investment-committee/simulate_committee.py` for deterministic manifest validation and scoring.

## Read Next

- `meta-bankability-scoring` - when lender-readiness repair, rather than committee rehearsal, owns the next decision.
- `meta-due-diligence` - when a challenged claim must be verified against records.
- `meta-financial-stress-test` - when the committee requests a new downside or covenant case.

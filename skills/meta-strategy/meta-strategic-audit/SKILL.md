---
name: meta-strategic-audit
description: Use when running a read-only strategic audit of an existing SME, NGO or growth firm across performance, governance, environment, capabilities, strategic factors, choices, implementation and control; distinguishes `meta-due-diligence`, which serves a transaction or investment decision.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Strategic Audit

Diagnose how well an organisation's current strategy fits its environment, capabilities and results, and report findings with evidence and severity. Adapted from the eight-part strategic audit of Wheelen, Hunger, Hoffman and Bamford (2018) *Concepts in Strategic Management and Business Policy*, 15th edn, Pearson, for owner-managed firms, NGOs and growth companies in East Africa. The audit diagnoses; it does not rewrite the strategy.

<!-- dual-compat-start -->
## Use When

- An owner, board, funder or incoming manager wants a diagnostic of where the organisation's strategy stands before a new plan, turnaround, retained advisory engagement or growth round.
- A fixed-fee strategic audit or growth diagnostic is being delivered and its report table of contents must follow a defensible method.
- A plan refresh needs to know whether the stated mission, objectives and strategy are explicit, consistent and actually realised.
- An NGO or social enterprise needs a strategy review ahead of a five-year strategic plan or a donor re-application.

## Do Not Use When

- Use `meta-due-diligence` instead when the review supports an acquisition, investment, lending or partnership transaction and needs an evidence room and red-flag report.
- Use `meta-strategic-factor-analysis` instead when only the weighted EFAS, IFAS, SFAS and TOWS tables are needed.
- Use `meta-critical-thinking-business-logic` instead to test the reasoning of a draft plan rather than the live organisation.
- Use `kaizen-improvement-system` instead to audit this skills engine or one of its outputs.
- Do not edit the client's documents or strategy during the audit; this skill is read-only by default.

## Required Inputs

| Input artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Audit mandate: sponsor, scope, units covered, decision date, read-only authority | Engagement owner | Yes | Stop; an audit without a sponsor and decision date has no standard of judgement. |
| Three years of financial results or management accounts | Client finance function | Yes | Audit Part I on non-financial evidence only; mark financial findings `not assessed`. |
| Stated mission, objectives, strategy, policies and last plan | Client documents, board minutes | Yes | Record "strategy implicit only" as a finding and infer the realised strategy from behaviour. |
| Governance records (board or trustees, owner roles, delegation) | Company secretary, founder | Conditional | Rate governance from interviews and flag the gap. |
| Market, competitor and country evidence | Digital research engine, `country-context/`, `04`, `06` outputs | Conditional | Keep Part III findings as hypotheses with `VERIFY` flags. |
| Interviews with staff, customers and at least one outside party | Auditor | Yes | Narrow Parts IV and VIII conclusions and say so. |

## Workflow

1. Confirm the mandate, the decision date and read-only authority. Research the organisation up to the decision date only. Stop if the sponsor or scope is unclear; recover by returning the mandate questions.
2. Part I, current situation: record performance trends and the strategic posture as stated and as implied by behaviour; note the gap.
3. Part II, governance: assess the board or trustees, the owner-family and succession position, and top management capability.
4. Part III, external environment: run or reuse the PESTEL, five forces and EFAS from `meta-strategic-factor-analysis`.
5. Part IV, internal environment: audit structure, culture and each function with the ten-question pattern in [the audit checklist](references/strategic-audit-checklist-east-africa.md); summarise in the IFAS.
6. Part V, strategic factors: build or check the SFAS; judge whether mission and objectives still fit. Block any finding that introduces a factor not examined in Parts I to IV.
7. Part VI, alternatives: test whether better execution of the current strategy would meet objectives before naming other options; list two or three feasible alternatives but leave choice to `meta-strategic-options-evaluation`.
8. Parts VII and VIII, implementation and control: check programmes, budgets, procedures, owners, KPIs, steering measures and reward alignment.
9. Grade each finding by severity, attach evidence, and write the audit worksheet and report. Return the draft to the sponsor for factual correction only; revise facts, not severity, unless new evidence is supplied.

## Quality Standards

- Every finding carries evidence, source, severity (Critical, High, Medium, Low) and the audit part it belongs to.
- Findings separate the espoused strategy from the realised strategy with at least one piece of customer or operating evidence.
- No recommendation introduces a strategic factor that Parts I to IV did not examine.
- Financial findings present only the ratios that bear on the issues and quantify the cash or margin at stake.
- The report states what was not assessed and why; an unavailable check is never shown as satisfactory.

## Anti-Patterns

- Filling in every checklist question mechanically. Fix: select the questions that bear on the mandate and add sub-questions where the organisation is unusual.
- Accepting the mission statement as a description of the strategy. Fix: compare stated strategy with budgets, pricing, hiring and customer experience.
- Researching events after the decision date. Fix: fix the evidence cut-off at the decision date and note later information separately.
- Rating "strong brand" or "committed staff" as strengths without testing. Fix: apply VRIO against named rivals before recording a strength.
- Turning the audit into a new strategy. Fix: stop at findings and alternatives; route choice to options evaluation and drafting to the section skills.
- Rewriting the client's documents during a review. Fix: stay read-only and deliver findings; edits need separate authority.

## Outputs

| Output artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Strategic audit worksheet (eight parts, plus and minus factors, comments) | Sponsor, audit team | Every part is completed or marked not applicable with a reason. |
| Findings register with evidence and severity | Board, owner, funder | Each finding has evidence, source, severity, owner and the decision it affects. |
| Strategic audit report | Sponsor and decision-makers | Follows the eight-part structure; exhibits numbered; not-assessed items listed. |
| Hand-off note | `meta-strategic-options-evaluation`, `business-plan-orchestrator` | Names the SFAS, the alternatives worth screening and the evidence gaps. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Evidence log | Table: finding ID, document or interview, date, source grade | A reviewer can trace every finding to its evidence. |
| Espoused-versus-realised comparison | Two-column table per strategy element | Each gap cites operating or customer evidence. |
| Not-assessed register | List with reason and consequence | Missing records and refused interviews are visible. |

<!-- dual-compat-end -->
## Capability Contract

Permission boundary: analysis and drafting only unless the engagement owner has authorised more. Read-only by default: read and search supplied records, interview notes and public sources; draft findings and the report. Do not edit client systems or documents, contact customers or regulators without the sponsor's authority, or certify financial statements, legal compliance or governance adequacy. Financial ratios and statements follow the Chwezi finance doctrine; country and regulatory facts come from the Digital research engine and `country-context/` files. Remediation work needs separate explicit authority.

## Degraded Mode

Without financial records, governance documents, interviews or network research, deliver a narrowed audit covering only the parts with evidence, mark the rest `not assessed`, lower confidence, and list the records that would complete it. Do not infer a satisfactory rating from silence.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| Stated strategy and realised behaviour disagree | Record a High finding and describe the realised strategy | Planning from a strategy nobody is executing. |
| Performance gap exists but the strategy still fits the SFAS | Recommend fine-tuning execution before new alternatives | Unnecessary strategic change and wasted capital. |
| Governance rests on one founder with no delegation or successor | Grade Critical for lenders and buyers; route to `09-management-team` | A plan that fails the funder's key-person test. |
| A finding depends on country or regulatory facts | Verify through the Digital research engine before grading | Severity built on an outdated rule. |
| Evidence is contested between interviews | Record both views and the evidence each rests on | False certainty in the report. |

## Worked Example

A Kampala private-school group asks for a strategic audit before a bank facility. Part I shows enrolment up 18% over three years while fee collection fell from 91% to 78% (illustrative). Part II finds the founder signs all spending with no bursar. Part IV's culture review finds a "we are educators, not collectors" paradigm. The SFAS places collection and governance as the two heaviest weaknesses. Findings: F1 Critical, fee-collection decline threatens debt service; F2 High, single-signatory governance. Alternatives listed: fix collections within the current strategy, or pause the fourth campus. Choice is passed to options evaluation; the report lists the missing audited accounts as not assessed.

## References

- [Strategic audit checklist for East African SMEs, NGOs and growth firms](references/strategic-audit-checklist-east-africa.md) - read at steps 2 to 9 for the eight-part questions, the ten-question function pattern, severity scale, worksheet and report outline.
- [Weighted-factor tables](../meta-strategic-factor-analysis/references/weighted-factor-tables-efas-ifas-sfas.md) - read at steps 4 to 6 for EFAS, IFAS and SFAS construction.
- [Country context index](../../../country-context/INDEX.md) - read before judging country-specific external findings.

## Read Next

- `meta-strategic-options-evaluation` - when the audit's alternatives must be screened and a strategy chosen.
- `meta-due-diligence` - when the same organisation is now a transaction target.
- `meta-monitoring-evaluation` - when Part VIII findings require a new control and KPI system.

# End-to-end business-plan stage gates

Back to [Business Plan Orchestrator](../SKILL.md).

## Stage contract

| Stage | Owner | Required evidence | Pass condition | Stop and restart |
|---|---|---|---|---|
| 1. Intake | `00-client-intake` | Decision brief, audience, jurisdiction, permissions, known gaps | Decision and reader are specific enough to choose evidence and funding logic | Stop on missing decision or authority; restart with approved brief |
| 2. Evidence design | Digital research engine plus section owners | Claim register, search plan, source tiers, verification state, gaps | Every load-bearing claim has a source route or an explicit gap | Stop affected claims; restart after verification or scope reduction |
| 3. Business logic | `meta-critical-thinking-business-logic` | Governing thesis, assumptions, warrants, countercases | Customer, revenue, cost, operating, implementation, risk, and funding logic can coexist | Return contradictions to their owners |
| 4. Section production | Pipeline owners | Versioned section outputs and evidence links | Audience-required sections meet their contracts | Redraft only the failed section and its dependants |
| 5. Model and finance | `10-financial-projections`, finance reviewers | Integrated statements, assumption register, formula map, scenarios, reconciliation, doctrine gate | Narrative and model reconcile; no finance or workbook blocker | Return to model owner; rerun dependent funding, valuation, and summary work |
| 6. Challenge | Synthesis, stress, DD, bankability/valuation, sector gates | Findings, dissent, conditions, recovery owners | Knockouts are closed and credible countercase is addressed | Keep status blocked until evidence or decision changes |
| 7. Audience rehearsal | `meta-investment-committee-red-team` or audience equivalent | Complete plan, model evidence, source pack, gate results | Simulation is valid and preserves conditions and dissent | A simulation may defer or reject; it never grants authority |
| 8. Assembly | `00-plan-assembly` | Approved versions, appendix map, final ask, release register | One coherent package with stable cross-references | Return numerical or version conflicts upstream |
| 9. Cross-engine finalisation | Named external engines and reviewers | Handoff records, render, visual QA, workbook QA, security/privacy disposition | Every applicable handoff passes with traceable evidence | `not-assessed` remains blocking when mandatory |
| 10. Release | Authorised release owner | Valid release bundle, reviewer notes, audit log, checklist, authority | Validator returns release and human authority is recorded | Correct named findings and rerun affected gates |

## Audience routes

| Audience | Mandatory overlays | Decision emphasis | Typical knockout |
|---|---|---|---|
| Commercial bank | Bankability, stress test, collateral/security evidence, finance doctrine | Repayment source, DSCR, cash conversion, security, management controls | Downside debt service or unsupported collateral |
| DFI | Bankability, sustainability, safeguards, sector gates, DD | Additionality, impact, governance, long-term viability, safeguards | Unassessed material safeguard or permit |
| VC/equity | Valuation, cohort/unit economics, dilution, moat, DD | Retention, scalable acquisition, defensibility, runway, return path | Illustrative traction presented as evidence |
| Grant | Grant workflow, MEL, restricted-fund finance, safeguarding | Eligibility, outcomes, delivery evidence, budget integrity, sustainability | Missing mandatory form, safeguarding control, or budget tie |
| Owner-manager board | Optionality, cash controls, quarterly plan, living-plan governance | Reversibility, owner constraints, cash, execution capacity | Growth plan outruns working capital or management control |
| Strategic partner | DD, governance, option analysis, integration and dependency risks | Mutual value, rights, execution, exit and concentration | Unclear rights, economics, authority, or termination path |

## Dependency rules

1. The executive summary is written only after the section set, model, risks, and funding logic stabilise.
2. A model change reopens the executive summary, funding request, implementation timing, valuation, stress test, and any cited KPI.
3. A regulatory or sector-gate change reopens operations, risk, implementation, capex/opex, and funding logic.
4. A customer-evidence change reopens market sizing, GTM, revenue assumptions, capacity, and financing need.
5. A release-stage edit that changes meaning returns to the owning stage; document assembly may correct formatting and cross-references only.

## Minimum restart record

Record the failed stage, affected artefacts, finding, severity, owner, evidence request, deadline or trigger, downstream stages invalidated, and the first gate to rerun. A later pass must point to the replacement evidence rather than overwrite the failure history.

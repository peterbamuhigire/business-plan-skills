# Control-plane adoption

This engine adopts the shared ten-engine contract from
`C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md`. Business-plan
skills remain the source of truth for strategy, market logic, modelling, and
decision-ready delivery bundles.

## Local roles and commands

| Role | Responsibility | Required output |
|---|---|---|
| Strategy planner | Establish the decision, scope, options, and operating logic. | Decision frame and owner. |
| Market researcher | Gather and grade country, sector, customer, and competitor evidence. | Claim-level source register. |
| Finance-model reviewer | Test assumptions, formulas, scenarios, and sensitivities. | Reconciled model audit. |
| Red-team reviewer | Challenge feasibility, downside cases, evidence, and readiness claims. | Findings with remediation or residual risk. |

Route thin commands `baseline-plan`, `stress-test`, `scenario-model`, and
`re-audit` to canonical skills. Commands do not duplicate planning doctrine or
create an untracked model.

## Hook and release contract

- `preflight` identifies the decision owner, audience, jurisdiction, currency,
  required research, finance, design, and document companions.
- `context` loads the plan register, source register, assumptions, prior
  decisions, and current model before drafting.
- `before_write` freezes the assumption version and records material changes,
  permissions, and rollback or superseded-output handling.
- `after_write` runs evidence, sector, workbook, and consistency checks and
  appends results to the release bundle.
- `release` blocks investor-, bank-, donor-, or submission-ready claims until
  assumptions, source currency, scenario calculations, decision ownership,
  and cross-engine evidence are present.
- `stop` leaves a handoff with the unresolved decision, missing evidence,
  model state, blockers, and next experiment.

Missing evidence is `NOT ASSESSED`, never a pass. Improvements are promoted
only with an owner, experiment, acceptance evidence, and re-audit date.

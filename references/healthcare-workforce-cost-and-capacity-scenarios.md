# Healthcare workforce cost and capacity scenarios

This reference implements B25-A04 for health-sector business plans. It keeps
pay, benefits, statutory items, estimates, service capacity, inclusion, and
review triggers separate. It is a planning model contract, not a source of
salary, statutory, clinical, or staffing-ratio claims.

## Input contract

| Input | Required fields | Evidence status |
|---|---|---|
| Role and headcount | role, competency, start/end period, employment basis, FTE | Local workforce plan or assumption |
| Pay | currency, period, gross pay, source/locator, effective date | Sourced or management assumption |
| Benefits | component, amount/basis, eligibility, source/locator | Sourced or labelled estimate |
| Statutory items | country, component, period, source-register ID, reviewer | `blocked` until current source review |
| Capacity | productive hours, absence/training allowance, utilisation, service mix | Operational baseline or assumption |
| Inclusion/access | reasonable adjustments, safe access, language, scheduling, supervision | Owner and review trigger |

## Scenario method

1. Separate sourced pay, benefits, statutory placeholders, and estimates. Do
   not embed a country rate or deadline without the current source register.
2. Forecast service capacity by role, competency, productive hours, absence,
   training, utilisation, and service mix. A projected volume above practical
   capacity requires a hiring, process, or timing decision.
3. Build base, constrained/downside, and capacity-supported/upside scenarios.
   State the assumptions that move between scenarios and keep the prior version.
4. Show absence, training, competency, supervision, inclusion, and access risks
   alongside cost. Identify the owner, guardrail, and review trigger.
5. Reconcile people cost to the financial model and route payroll/statutory
   treatment to the finance engine. Preserve unresolved items as exceptions.

## Synthetic formulas

- **People cost** = headcount × period pay + benefits + declared employer-cost
  items. Each component must carry its own source/status.
- **Practical capacity** = FTE × available hours × (1 - absence/training
  allowance) × declared utilisation × competency factor.
- **Service capacity** = practical capacity allocated by service mix; it must
  not exceed the hours or competency available for the role.

These formulas describe a planning contract. They do not establish a clinical
staffing ratio or statutory obligation.

## Stop and review rules

- Every amount has source, period, basis, owner, and reviewer or is labelled an
  assumption/estimate.
- A missing current statutory source blocks final payroll or statutory output.
- A capacity scenario without absence, training, competency, or inclusion risks
  is incomplete.
- Historical foreign ratios, laws, and salary benchmarks remain quarantined
  unless independently current and comparable evidence is supplied.

## Currentness record

| Field | Record |
|---|---|
| Source scope | B25 book-study concept, applied to synthetic workforce cost and capacity scenarios. |
| Publication/version date | Book-study source; no salary benchmark, staffing ratio, tax, or statutory rate is asserted. |
| Access date | 2026-09-19 |
| Freshness class | Durable concept input; pay, statutory, and service-capacity evidence is time-sensitive. |
| Review date | Before external release and whenever the workforce plan, country, or statutory source changes. |
| Support status | Supported as a scenario structure; finance and professional review remain required. |
| Uncertainty | Current compensation, payroll, statutory, clinical, inclusion, and practical-capacity evidence may be `not_assessed`. |

# Approval enforcement adapter

Business-plan actions are declared in [`approval-adapter.json`](approval-adapter.json)
and use the shared contract from `skills-web-dev/docs/approval-contract.md`.

## Required review bundle

Before approval, show the claim and assumption register, source and evidence
map, model and formula diff, sensitivity and downside cases, reconciliations,
regulatory caveats, implementation realism, owner, recipient, expiry, and
rollback/correction path. Facts, estimates, inferences, hypotheses, unknowns,
and management inputs must remain distinct.

## Gated actions

Approving assumptions, changing model logic, declaring a plan bankable or
investor-ready, releasing a funding/valuation recommendation, or sending a
plan to a lender, investor, donor, board, or public audience is L3. Accounting,
tax, costing, controls, reporting, or finance-system claims require review by
the Chwezi Accounting Doctrine and a qualified finance reviewer.

## Stop conditions

AI-generated numbers, citations, customer evidence, or approvals must not
enter a final plan without traceable source or explicit human attribution.
Unreconciled numbers, unsupported claims, unresolved material assumptions, or
missing reviewer identity block release. A generated label such as “bankable”
is never authority.

## Acceptance boundary

The engine may structure a draft and identify inconsistencies. It cannot
approve assumptions, label a plan bankable, issue a funding recommendation, or
release the plan externally until the shared gate records approval.

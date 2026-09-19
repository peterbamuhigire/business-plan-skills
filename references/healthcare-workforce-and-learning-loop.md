# Healthcare workforce and learning loop

This reference implements B25-A02 for health-sector planning. It links role
criteria, staffing evidence, retention learning, and competency re-checks. It
does not certify clinical competence, employment compliance, or safe staffing;
those require the named professional and jurisdictional reviewers.

## Evidence chain

| Stage | Required evidence | Stop condition |
|---|---|---|
| Role design | service pathway, role outcomes, competency criteria, supervision and safety responsibilities | Missing role outcome is `not_assessed`. |
| Selection/onboarding | criterion-to-evidence map, structured decision, onboarding owner, access needs | Selection evidence that does not map to a criterion is rejected. |
| Retention diagnosis | workload, supervision, learning, fairness, safety, and exit/absence observations | Unsupported cause remains an open hypothesis. |
| Learning intervention | observed gap, learning objective, practice/support, owner, time window, guardrail | Completion alone is insufficient. |
| Competency re-check | repeatable observation, assessment or work sample, reviewer, result, follow-up | Missing re-check leaves competence `not_assessed`. |

## Learning-loop procedure

1. Establish the role and service baseline from local records; label missing
   workforce data `not_assessed`.
2. Map selection and onboarding evidence to criteria and assign supervision.
3. Diagnose retention as a set of hypotheses across workload, supervision,
   learning, fairness, and safety rather than assuming pay is the only cause.
4. Run one bounded learning intervention with baseline, guardrail, owner, and
   review date. Keep service continuity and patient-safety consequences visible.
5. Re-check observed competency and service outcome, record what changed, and
   adjust, stop, or roll back the intervention.

## Acceptance rules

- Selection evidence maps to the criterion it is meant to test.
- Retention experiments name baseline, guardrail, owner, and review date.
- Training attendance or completion cannot prove competence.
- An unresolved clinical, safeguarding, or employment question remains
  `not_assessed` and is routed to the appropriate reviewer.

## Currentness record

| Field | Record |
|---|---|
| Source scope | B25 book-study concept, applied to evidence-based workforce learning. |
| Publication/version date | Book-study source; no clinical, employment, or statutory rule is asserted. |
| Access date | 2026-09-19 |
| Freshness class | Durable concept input; local workforce and professional evidence is required. |
| Review date | Before external release and when role, safety, employment, or service conditions change. |
| Support status | Supported as a learning-loop structure; it does not certify competence or safe staffing. |
| Uncertainty | Workforce baseline, retention cause, competency result, and current professional requirements may be `not_assessed`. |

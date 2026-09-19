# Business-agility readiness map

This reference implements B18-A01 for business-plan and transformation work.
It tests whether a proposed change is ready across decisions, processes,
people, tools, and evidence. A platform purchase alone is not a readiness
objective.

## Map schema

| Field | Required question |
|---|---|
| Decision | What decision or customer outcome must improve? |
| As-is | What happens now, including delay, rework, control, and evidence? |
| People | Which roles decide, perform, review, and are affected? |
| Process | Which step, handoff, policy, or exception is changing? |
| Tools/data | Which tool or data is needed, and what rights or quality limits apply? |
| To-be | What observable outcome will be different? |
| Gap | What prevents the to-be state today? |
| Owner/dependency | Who can close the gap and what must be available first? |
| Acceptance | What measurable check shows readiness? |
| Failure consequence | What happens if the slice fails? |
| Next check/rollback | When is it reviewed and how is the prior route restored? |

## Bounded readiness workflow

1. Name the decision, user or customer outcome, and current baseline. If the
   baseline is missing, mark the affected row `not_assessed`.
2. Capture decision rights, process steps, people capability, tools/data, and
   evidence separately. Do not infer readiness from tool availability or
   workshop attendance.
3. Define the smallest reversible slice, owner, dependency, acceptance oracle,
   failure consequence, and rollback route.
4. Run the slice in fixture or shadow mode, compare with the prior route, and
   record false passes, false alarms, and adoption burden.
5. Promote only when the named acceptance check passes and the reviewer accepts
   the residual risk; otherwise return the gap to its owner.

## Readiness states

| State | Meaning | Action |
|---|---|---|
| `ready_for_shadow` | Baseline, owner, data rights, fallback, and oracle exist. | Run one bounded reversible slice. |
| `conditional` | One non-critical dependency is pending. | Keep scope narrow and record the dependency. |
| `blocked` | Missing baseline, authority, evidence, or safe fallback. | Stop the affected conclusion. |
| `not_assessed` | The check was not run or evidence could not be judged. | Preserve the question and next check. |

Every gap needs a source or observation, owner, target state, acceptance check,
and next review date. Record current platform, legal, market, or cost claims as
currentness-gated evidence; this map does not verify them.

## Currentness record

| Field | Record |
|---|---|
| Source scope | B18 book-study concept, applied to a reversible business-planning slice. |
| Publication/version date | Book-study source; current platform or regulatory versions are not asserted. |
| Access date | 2026-09-19 |
| Freshness class | Durable concept input; currentness-gated operational claims remain separate. |
| Review date | Before external release and at each material dependency or tool change. |
| Support status | Supported as a readiness-map structure; no production readiness is certified. |
| Uncertainty | Baseline, rights, capability, cost, and adoption evidence may remain `not_assessed`. |

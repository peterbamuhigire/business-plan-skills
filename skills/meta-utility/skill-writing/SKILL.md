---
name: skill-writing
description: Use when creating, normalising, reviewing, or releasing a reusable business-plan skill; distinguishes skill authoring from `skill-safety-audit`, which inspects safety without redesigning the skill contract.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Skill Writing

Create portable, neighbour-aware skills that produce reviewable business-plan artefacts. Keep domain judgement in the skill, repository-wide routing in `AGENTS.md`, and deeper examples or schemas in directly linked references.

<!-- dual-compat-start -->
## Use When

- Creating a new skill for a repeatable business-planning, advisory, finance, pitch, or execution workflow.
- Normalising a legacy `SKILL.md` to the July 2026 composition contract.
- Reviewing a skill change for routing, capability, evidence, recovery, or acceptance gaps.
- Updating the local template, validator, fixtures, or release baseline.

## Do Not Use When

- Use `skill-safety-audit` instead for a read-only inspection of unsafe permissions, hidden instructions, or exfiltration risk.
- Use the relevant domain skill when the task is to produce a business-plan artefact rather than author its reusable procedure.
- Do not create a new skill when an existing neighbour can own the trigger after a focused update.

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| Reusable problem and intended consumer | Requester or engine roadmap | Yes | Stop; a skill without a repeatable job has no stable contract. |
| Positive, negative, and neighbour-collision prompts | Requester plus active catalogue | Yes | Search neighbouring descriptions; return a routing-gap note if the boundary remains ambiguous. |
| Required inputs, outputs, evidence, and acceptance conditions | Domain owner or governing skill | Yes | Mark unresolved contracts and do not claim the skill is release-ready. |
| Capability and permission boundary | Task authority and runner context | Yes | Default to read-only and exclude mutation until authority is explicit. |

## Workflow

1. Inventory active `SKILL.md` files from `skills/` and `country-context/`; identify the closest neighbours before choosing a new or existing directory.
2. Define the role/procedure boundary, positive and negative triggers, required inputs, outputs, evidence, consumers, and acceptance conditions.
3. Draft from `references/dual-compatible-skill-template.md`; keep the entrypoint below 500 lines and move deep catalogues or case material into linked references.
4. Add a domain decision table, ordered workflow, stop conditions, recovery behaviour, permission boundary, degraded mode, five concrete anti-patterns with corrections, and a worked example when execution could otherwise be ambiguous.
5. Test positive, negative, collision, limited-capability, and failure prompts. Stop and revise when the expected skill is not in the deterministic router's top three.
6. Run the local engine validator, routing smoke test, and canonical quick validator. Recover from a failure by fixing the named contract rather than weakening the baseline.
7. Inspect the diff and release only when the zero-debt baseline remains empty and no useful domain content was lost.

## Quality Standards

- `name` matches the directory; `description` is one line, starts with `Use when`, is at most 350 characters, and distinguishes a neighbour.
- Frontmatter uses only approved keys and declares portable compatibility with Claude Code and Codex.
- Inputs, outputs, evidence, decisions, capabilities, degraded behaviour, and acceptance conditions are observable rather than implied.
- Audit and review procedures default to read-only; edits, publishing, spending, destructive actions, and certification claims require explicit authority.
- Claims, examples, thresholds, and finance treatments are verified, qualified, or assigned to professional review.

## Anti-Patterns

- Creating a near-duplicate skill to improve a catalogue metric. Fix: update the existing neighbour or document a proven independent trigger and output contract.
- Writing `description: Helps with strategy`. Fix: begin with `Use when` and name concrete scenarios plus the closest non-route.
- Listing an input without its source or missing-input behaviour. Fix: use the four-column input table and state the stop, fallback, or qualification.
- Giving a review skill broad edit permissions. Fix: declare read-only as the default and require separate remediation authority.
- Treating a missing check as passed in degraded mode. Fix: mark it `not assessed`, narrow the conclusion, and name the evidence needed.
- Adding a decision table whose third column repeats the action. Fix: name the failure or risk avoided by the chosen branch.
- Copying provider commands into the portable body. Fix: state the required capability and keep runner syntax in an adapter or repository procedure.
- Hiding long examples in the entrypoint. Fix: extract them to a directly linked reference that links back to this skill.

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Normalised skill directory | Domain practitioner and routing engine | Local and canonical validators pass; entrypoint is at most 500 lines. |
| Routing fixture set | Maintainer and CI | Positive, negative, collision, limited-capability, and failure paths place the expected skill in the top three. |
| Validation evidence | Reviewer and release owner | Failure counts are empty against the zero-debt baseline. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Skill validation result | Command output or JSON report | No structural, link, identity, duplicate-name, resource, or encoding failures. |
| Routing result | Fixture summary | All fixtures pass the documented top-three threshold. |
| Change evidence | Reviewed diff and line-count report | No unrelated deletion, runner-specific body instruction, cache, or secret is present. |

<!-- dual-compat-end -->
## Capability Contract

Read and search are required to inspect the active catalogue and neighbours. Editing and execution are permitted only when the authoring task authorises repository changes. Network access is optional and used only for current external claims. Delegation is limited to non-overlapping skill cohorts; shared routers, validators, CI, baselines, and documentation stay with the primary owner.

## Degraded Mode

Without edit access, return a qualified patch plan and mark implementation `not assessed`. Without execution, provide the narrowest useful draft plus the exact validators that remain unrun. Without network access, remove or qualify current external claims; never convert an unavailable verification into a pass.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| Existing neighbour has the same trigger and consumer | Normalise the existing skill | Duplicate routes and contradictory contracts. |
| The proposed workflow has an independent trigger and artefact | Create a focused skill after collision tests | Oversized entrypoints that load irrelevant guidance. |
| Deep material is necessary but not routing-critical | Move it to a directly linked reference | Entry points exceeding 500 lines or obscuring decisions. |
| A requested action exceeds the declared permission boundary | Stop and request explicit authority | Unauthorised edits, publication, spending, or certification. |
| A required capability or input is unavailable | Use degraded mode and qualify the result | An unassessed check being reported as passed. |

## Worked Example

Prompt: "Add a skill for reviewing whether a funding ask is lender-ready." First search `meta-bankability-scoring`, `11-funding-request`, and `meta-accounting-finance-review`. If `meta-bankability-scoring` already produces blocker findings and a lender-readiness score for the same consumer, update its trigger and evidence contract; do not add a duplicate reviewer. Add fixtures that distinguish writing the funding request from scoring its bankability.

## References

- [Dual-compatible skill template](references/dual-compatible-skill-template.md) - required structure and field-level contract.
- [Dual-surface migration rules](references/dual-surface-migration-rules.md) - boundary between portable skills and repository instructions.
- [Output patterns](references/output-patterns.md) - use when a deliverable needs a repeatable schema.
- [Workflow patterns](references/workflows.md) - use for branching, recovery, and stop-condition design.
- [Skill authoring practices](references/skill-authoring-best-practices.md) - use for progressive disclosure and resource selection.

## Read Next

- `skill-safety-audit` for read-only permission and instruction-risk review.
- `anti-ai-slop` while writing any human-facing skill content.
- `ai-slop-audit` after each major cohort and before release.

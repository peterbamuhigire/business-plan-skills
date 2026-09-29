---
name: skill-writing
description: Use when creating, normalising, reviewing, or releasing a reusable business-plan skill under the canonical chwezi-dev-engine skill-writing standard; distinguishes skill authoring from `skill-safety-audit`, which inspects safety without redesigning the skill contract.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---
# Skill Writing

Pointer stub. The canonical standard is `chwezi-dev-engine/skills/sdlc-meta/skill-writing` ([canonical on GitHub](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/skills/sdlc-meta/skill-writing/SKILL.md); local path `C:\wamp64\www\chwezi-dev-engine\skills\sdlc-meta\skill-writing\SKILL.md`). Load it first; this file keeps a portable minimum and this engine's delta.
<!-- dual-compat-start -->
## Use When
- Creating or normalising a skill for a repeatable business-planning, advisory, finance, pitch or execution workflow.
## Do Not Use When
- Use `skill-safety-audit` instead for a read-only safety inspection; use the domain skill when the task is to produce a plan artefact.
## Required Inputs
| Artefact | Source/provider | Required? | If absent |
|---|---|---:|---|
| Reusable problem, trigger prompts and neighbour descriptions | Requester and live catalogue | Yes | Stop; search the catalogue before drafting. |
| Canonical skill-writing standard | chwezi-dev-engine checkout or GitHub | Yes | Apply the portable minimum and mark canonical-only checks `NOT ASSESSED`. |
## Workflow
1. Read the canonical standard, then this engine's delta; inspect the closest neighbours.
2. Write the input, output, evidence, capability, degraded-mode and decision contracts before the procedure.
3. Run `python -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json` and `python -X utf8 scripts/routing_smoke_test.py`, then `python -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py <skill-dir>`.
4. Stop on any finding or routing collision; recover by fixing the named contract and rerun, never by weakening the gate.
## Outputs
| Artefact | Consumer | Acceptance condition |
|---|---|---|
| Skill directory and routing fixtures | Maintainer and router | Validators pass and the expected skill ranks in the top three. |
## Evidence Produced
| Evidence | Artefact and format | Consumer | Acceptance condition |
|---|---|---|---|
| Validation and routing record | Command output | Release owner | Zero findings; unrun checks marked `NOT ASSESSED`. |
<!-- dual-compat-end -->
## Quality Standards
- Portable minimum, applied even when the canonical is unreachable: frontmatter uses only approved keys and `name` matches the folder.
- The description starts `Use when`, stays within 350 characters and names a neighbour, with no workflow steps.
- `SKILL.md` stays within 500 lines; deep detail sits in references one level deep, linked directly.
- Every new or changed skill gets positive, negative and collision routing fixtures.
- Bundled scripts run through their interpreter, for example `python -X utf8 scripts/<name>.py`.
- No book extractions or copied third-party text; paraphrase and attribute.
- British English, the imperative mood, and `NOT ASSESSED` for any check not run.
## Engine-Local Delta
- Draft from the [dual-compatible skill template](references/dual-compatible-skill-template.md) and respect the [dual-surface migration rules](references/dual-surface-migration-rules.md); inventory `skills/` and `country-context/` for neighbours.
- Verify financial figures, thresholds and accounting treatments, or assign them to professional review under the finance engine; apply `anti-ai-slop` while writing and `ai-slop-audit` before release.
## Capability Contract
Read and search are required. Editing files and running validators need explicit permission for the authoring task; publishing, deletion and release changes need separate authorisation.
## Degraded Mode
If the canonical standard is unavailable, apply the portable minimum, return the narrowest qualified result, and mark each canonical-only check `NOT ASSESSED`; never report it as passed.
## Decision Rules
| Condition | Action | Failure or risk avoided |
|---|---|---|
| An existing skill owns the trigger and output | Normalise it in place; put branch-only detail in a linked reference | Duplicate routes and oversized entrypoints |
## Anti-Patterns
- Copying the canonical body into this engine. Fix: link the canonical and keep only the delta here.
- Writing only positive triggers. Fix: name the neighbour and add a collision fixture.
- Treating an unrun validator as a pass. Fix: record `NOT ASSESSED` with the reason.
- Granting edit rights to a review procedure. Fix: default review and audit to read-only.
- Weakening a baseline to clear a finding. Fix: repair the named contract instead.
## Worked Example
Asked for a lender-readiness review skill, first search `meta-bankability-scoring`, `11-funding-request` and `meta-accounting-finance-review`; update the owner that already scores bankability instead of adding a duplicate reviewer.
## References
- [Canonical skill-writing standard](https://github.com/peterbamuhigire/chwezi-dev-engine/blob/main/skills/sdlc-meta/skill-writing/SKILL.md)
- [Dual-compatible skill template](references/dual-compatible-skill-template.md)
- [Dual-surface migration rules](references/dual-surface-migration-rules.md)
- [Skill safety audit](../skill-safety-audit/SKILL.md)

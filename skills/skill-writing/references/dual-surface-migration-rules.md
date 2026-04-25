# Dual-Surface Migration Rules

Use this guide when converting the repository to work cleanly for both Codex and Claude Code.

## Objective

Use a dual-surface model:

- `SKILL.md` as the portable, shared skill unit
- `AGENTS.md` as the repo-wide orchestration and policy layer

## What Goes In `SKILL.md`

Put into `SKILL.md` anything that should travel with the skill regardless of agent:

- when the skill should activate
- required inputs
- workflow and checklist
- decision rules
- anti-patterns
- output standards
- pointers to deeper reference files

## What Goes In `AGENTS.md`

Put into `AGENTS.md` anything that is repo-wide, cross-skill, or operationally global:

- repo purpose
- routing by task type
- baseline skill load order
- hard constraints
- verification expectations
- migration rules
- done-means criteria

## Migration Process

### 1. Preserve the skill as the canonical unit

Do not replace skills with one giant `AGENTS.md`.

### 2. Remove provider-specific assumptions

Delete or rewrite:

- provider-specific command syntax
- slash-command assumptions
- chat UI instructions
- instructions that depend on hidden platform behaviour

### 3. Shorten `SKILL.md`

Keep only:

- scope
- workflow
- decision rules
- outputs

Move:

- long frameworks
- examples
- checklists
- teaching material

into `references/`.

### 4. Normalise structure

Where practical, add these sections:

1. Overview
2. Use When
3. Do Not Use When
4. Required Inputs
5. Workflow
6. Quality Bar
7. Anti-Patterns
8. Outputs
9. References

### 5. Centralise repeated standards

If the same rules appear in many skills, move them into:

- a shared baseline skill
- a shared reference
- or `AGENTS.md` if they are truly repo-wide

## Decision Rule: `SKILL.md` vs `AGENTS.md`

Ask:

- Is this rule portable with the skill? Put it in `SKILL.md`.
- Is this rule about the whole repository or multi-skill workflow? Put it in `AGENTS.md`.

## Anti-Patterns

- giant `SKILL.md` files that duplicate reference content
- repo-wide rules copied into dozens of skills
- platform-specific instructions embedded in portable skills
- overlapping skills that solve the same problem with different wording
- creating a `/skills` directory migration before the logical standards are settled

## Recommended Rollout

1. Add top-level `AGENTS.md`
2. Add universal authoring template
3. Upgrade touched skills to the shared structure
4. Consolidate repeated standards
5. Consider physical directory reorganisation only after content convergence

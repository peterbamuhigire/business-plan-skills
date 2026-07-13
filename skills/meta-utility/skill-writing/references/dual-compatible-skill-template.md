# July 2026 dual-compatible skill template

Parent: [Skill Writing](../SKILL.md)

Use this template for every active skill. Replace every bracketed field with domain content; a filled heading with generic boilerplate is a contract failure.

```markdown
---
name: directory-name
description: Use when [specific trigger]; distinguishes this skill from `[closest-neighbour]`, which [owns excluded case].
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Human-readable title

[One or two sentences stating the procedure's purpose and governing judgement.]

<!-- dual-compat-start -->
## Use When

- [Positive trigger with a concrete task or artefact.]
- [Second trigger that defines the breadth of the route.]

## Do Not Use When

- Use `[neighbour]` instead when [specific excluded case].
- Do not use when [stop or out-of-scope condition].

## Required Inputs

| Artefact | Source/provider | Required? | Behaviour when missing |
| --- | --- | --- | --- |
| [Named input] | [Upstream skill, client, file, or provider] | Yes | [Stop, qualify, gather, or use a named fallback.] |

## Workflow

1. [Inspect and validate inputs.]
2. [Make a named decision using the table below.]
3. [Produce the artefact and its evidence.]
4. [Stop when a blocker is present; recover by gathering, revising, or escalating.]
5. [Run acceptance checks and hand off.]

## Quality Standards

- [Observable domain condition.]
- [Evidence or reconciliation condition.]
- [Release-blocking condition.]

## Anti-Patterns

- [Concrete wrong action.] Fix: [specific correction.]
- [Concrete wrong action.] Fix: [specific correction.]
- [Concrete wrong action.] Fix: [specific correction.]
- [Concrete wrong action.] Fix: [specific correction.]
- [Concrete wrong action.] Fix: [specific correction.]

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| [Named output] | [Role or downstream skill] | [Observable condition proving usability.] |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| [Decision, check, register, or source record] | [Table, file, model, or log] | [What a reviewer can verify.] |

<!-- dual-compat-end -->
## Capability Contract

[State minimum read/search/edit/execute/network capabilities and the safe permission boundary. Analysis, audit, review, critique, and planning default to read-only. Mutation, publishing, destructive action, spending, and certification require explicit authority.]

## Degraded Mode

[State the narrowest useful qualified result when inputs or capabilities are unavailable. Mark inaccessible checks `not assessed`; never report them as passed.]

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| [Decision condition] | [Chosen action] | [Named consequence of the wrong branch] |

## Worked Example

[A short input -> decision -> output -> acceptance example. Omit only for a pure router whose routing table itself is the worked evidence.]

## References

- [Reference title](references/reference-file.md) - [when to load it].

## Read Next

- `[adjacent-skill]` - [when that route wins].
```

## Entry-point rules

- Keep `SKILL.md` at or below 500 lines.
- Keep the description on one line, beginning with `Use when`, and at or below 350 characters.
- Use only `name`, `description`, `license`, `allowed-tools`, and `metadata` in frontmatter.
- Link every reference directly from the entrypoint; start each extracted reference with a link back to its parent skill.
- Keep decisions, safety, degraded behaviour, workflow, outputs, evidence, and acceptance in the entrypoint.
- Move catalogues, long schemas, case studies, and background teaching into `references/`.

# Dual-Compatible SKILL Template

Use this template when creating or refactoring a skill so it works cleanly for both Codex and Claude Code.

## Frontmatter

```yaml
---
name: skill-name
description: One to two sentences stating what the skill does and when to use it.
---
```

Use only:

- `name`
- `description`

Keep the description trigger-oriented, not promotional.

## Body Template

```markdown
# [Skill Title]

## Overview

State the core purpose in 2-3 sentences.

## Use When

- [task or trigger]
- [task or trigger]
- [task or trigger]

## Do Not Use When

- [out-of-scope case]
- [out-of-scope case]

## Required Inputs

- [required input]
- [required input]
- [required input]

## Workflow

1. [step]
2. [step]
3. [step]
4. [step]

## Quality Bar

- [standard]
- [standard]
- [standard]

## Anti-Patterns

- [mistake]
- [mistake]
- [mistake]

## Outputs

- [expected artifact]
- [expected artifact]

## References

- `references/[file].md` - [what to read it for]
```

## Writing Rules

- Write in imperative or declarative procedural language
- Keep the skill portable and provider-agnostic
- Avoid UI-specific instructions
- Avoid embedding large textbook content in `SKILL.md`
- Put deeper frameworks, examples, and checklists into `references/`

## What Belongs In `SKILL.md`

- activation guidance
- required inputs
- workflow
- decision rules
- quality bar
- anti-patterns
- outputs
- links to references

## What Does Not Belong In `SKILL.md`

- repo-wide orchestration rules
- provider-specific command syntax
- chat-interface assumptions
- duplicated global standards repeated across many skills
- long theory dumps that belong in `references/`

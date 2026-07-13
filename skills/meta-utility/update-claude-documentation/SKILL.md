---
name: update-claude-documentation
description: Use when synchronising README, AGENTS, CLAUDE, architecture, API, database, or status documentation after an authorised repository change; use the neighbouring domain skill to decide the implementation itself.
metadata:
  portable: true
  compatible_with:
    - claude-code
    - codex
---

# Update Claude Documentation

<!-- dual-compat-start -->

## Overview

Use this skill to keep repository documentation consistent after meaningful changes. It covers general project docs plus agent-facing instruction surfaces such as `CLAUDE.md` and `AGENTS.md`, so the repo stays coherent for both Claude Code and Codex.

## Use When

- Use when significant code, architecture, workflow, or instruction changes affect repository documentation.
- Use when updating agent-facing docs must stay aligned with user-facing and developer-facing docs.
- Use when multiple documentation files need a coordinated refresh after a change.

## Do Not Use When

- Do not use for trivial typo fixes or isolated wording changes that do not affect system understanding.
- Do not update one doc in isolation when the same change alters the shared narrative elsewhere.
- Do not keep documentation scoped only to one agent surface if the change affects both.

## Required Inputs

- The actual code, workflow, or structure change that occurred
- The set of documentation files potentially affected
- Any breaking changes, migration notes, or new conventions
- Existing docs whose terminology or examples must stay aligned

## Workflow

1. Identify the change and the audiences it affects.
2. Map the change to the documentation files that must be updated.
3. Read the affected files before editing any of them.
4. Update the most specific technical docs first, then the higher-level summaries and instruction files.
5. Check terminology, examples, and workflow guidance for consistency across docs.
6. Flag any remaining documentation debt or unresolved ambiguity.

## Quality Bar

- The same change is reflected consistently across all affected docs.
- Agent-facing docs and user-facing docs describe the same reality.
- Terminology, paths, versions, and examples stay aligned.
- Documentation becomes clearer, not just longer.

## Anti-Patterns

- Updating only one documentation file for a multi-surface change.
- Letting `CLAUDE.md` and `AGENTS.md` drift apart on shared conventions.
- Keeping stale examples after changing APIs, file paths, or workflows.
- Using documentation to paper over unresolved implementation ambiguity.

## Outputs

- Updated documentation set across the affected files
- Explicit notes on any deferred doc work
- Cross-file consistency between general docs and agent instruction surfaces



Update project documentation systematically after significant changes. Keep all files consistent and accurate.

**Core Principle:** Documentation tells one cohesive story. Each file serves a specific audience but must reflect the same reality.

**Modularize Instructions (Token Economy):** Avoid packing everything into a single CLAUDE.md. Prefer multiple focused docs (e.g., docs/setup.md, docs/api.md, docs/workflows.md) and reference them only when needed to reduce context bloat.

## When to Use

 Adding/removing features
 Architecture or design pattern changes
 Dependency or tech stack updates
 API endpoints or database schema changes
 Project directory restructuring
 Development workflow changes

 Typo fixes (do directly)
 Code comments
 WIP features not yet merged

## Documentation Files

| File              | Audience                | Purpose            |
| ----------------- | ----------------------- | ------------------ |
| PROJECT_BRIEF.md  | Stakeholders, new devs  | 30-sec overview    |
| README.md         | Developers              | Setup, usage guide |
| TECH_STACK.md     | Developers, DevOps      | Tech inventory     |
| ARCHITECTURE.md   | Senior devs, architects | System design      |
| docs/API.md       | API consumers           | API reference      |
| docs/DATABASE.md  | Backend devs, DBAs      | Schema docs        |
| CLAUDE.md         | Claude Code             | Dev patterns       |
| docs/setup.md     | Developers              | Setup details      |
| docs/api.md       | API consumers           | API usage guide    |
| docs/workflows.md | Developers              | Workflow rules     |

## Change  File Mapping

**New Feature:**

- README.md (usage)
- docs/API.md (if adds endpoints)
- docs/DATABASE.md (if adds tables)
- ARCHITECTURE.md (if adds components)
- CLAUDE.md (if changes patterns)
- PROJECT_BRIEF.md (if significant)

**Tech Stack Change:**

- TECH_STACK.md (always)
- README.md (setup instructions)
- ARCHITECTURE.md (if affects design)
- CLAUDE.md (if affects workflows)

**Architecture Change:**

- ARCHITECTURE.md (always)
- README.md (overview section)
- CLAUDE.md (patterns)
- PROJECT_BRIEF.md (if major)

**API/Database Change:**

- docs/API.md or docs/DATABASE.md (always)
- ARCHITECTURE.md (if changes contracts)
- CLAUDE.md (if affects patterns)
- README.md (if affects usage)

## Update Workflow

### 1. Understand Change (2-5 min)

Document:

- Type: Feature/Architecture/Tech Stack/API/Database
- What: One sentence description
- Impact: Who/what affected
- Breaking: Yes/No (what breaks)

### 2. Map to Files (1-2 min)

Order: Specific  General

1. Technical Specs (API.md, DATABASE.md)
2. Architecture (ARCHITECTURE.md, TECH_STACK.md)
3. AI Instructions (CLAUDE.md)
4. User Guides (README.md)
5. Overview (PROJECT_BRIEF.md)

### 3. Read Current State (2-3 min)

Read all affected files in parallel.

### 4. Update Systematically (10-20 min)

**Per-file checklist:**

- [ ] Update primary section
- [ ] Update related sections
- [ ] Update examples/code snippets
- [ ] Add migration notes if breaking

### 5. Verify Consistency (2-3 min)

Check across all files:

- [ ] Terminology consistent
- [ ] Version numbers match
- [ ] File paths consistent
- [ ] Component names consistent
- [ ] Features described consistently

### 6. Final Review (1 min)

- [ ] New dev can understand from README
- [ ] CLAUDE.md has context
- [ ] Breaking changes marked
- [ ] Examples work
- [ ] No contradictions

**Total:** 15-30 minutes

## Common Mistakes

 **Updating only one file**

```markdown
# Updated README but forgot CLAUDE.md

# Result: AI doesn't know new pattern
```

 **Inconsistent terminology**

```markdown
# README.md: "Authentication Service"

# ARCHITECTURE.md: "Auth Module"

# CLAUDE.md: "Login System"

# Pick ONE term everywhere
```

 **Forgetting breaking changes**

```markdown
# Renamed API endpoint but README examples still use old path

# Add migration notes EVERYWHERE affected
```

 **General  Specific order**

```markdown
# BAD: Update BRIEF first, then API.md

# GOOD: Update API.md first (precise), then BRIEF (summary)
```

## Quick Reference

**Update Order:**

```text
API/DB Specs  Architecture  CLAUDE  README  BRIEF
```

**Consistency Checks:**

```text
Terminology, Versions, Paths, Names, Features
```

**Time Budget:**

```text
Small change: 5-10 min
Medium change: 15-30 min
Major refactor: 45-60 min
```

## Summary

**Process:** Understand  Map  Read  Update  Verify  Review

**Key Rules:**

1. Update specific docs first, general last
2. Read all affected files before editing
3. Keep terminology consistent
4. Mark breaking changes everywhere
5. Test examples before committing
6. One reality, multiple perspectives

**Remember:** Documentation debt compounds fast. Update immediately when making changes.

## Required Inputs

| Input artefact | Source/provider | Required | Behaviour when missing |
| --- | --- | ---: | --- |
| Authorised repository change and diff | Implementation owner and version control | Yes | Stop factual updates and return an impact map only. |
| Existing owning documents | Repository | Yes | Mark the document gap and create a file only when the task authorises it. |
| Validation evidence and current counts | Repository commands or authoritative source | Conditional | Label the status `not assessed`; do not infer it. |

## Outputs

| Artefact | Consumer | Acceptance condition |
| --- | --- | --- |
| Updated documentation set | Maintainers, users, and agents | Behaviour, commands, paths, counts, and gates match inspected repository evidence. |
| Documentation change map | Reviewer | Every material change is mapped to an updated file or a justified not-applicable decision. |

## Evidence Produced

| Evidence | Format | Acceptance condition |
| --- | --- | --- |
| Documentation change map | Changed behaviour -> affected files -> updated statements | Every material repository change has an owner document or an explicit not-applicable rationale. |
| Consistency check | Link, command, count, and stale-claim results | Commands run, file paths resolve, counts match machine output, and superseded claims are removed or labelled. |

## Capability Contract

Read and search are required. Edit only documentation within the authorised repository change; do not modify application behaviour, publish externally, send messages, or certify accuracy outside the available evidence. Execution is limited to safe link, syntax, count, and repository validation. Network verification is optional and required only for current external facts.

## Degraded Mode

Fallback: without access to the changed implementation or its validation evidence, return a narrow documentation impact map and mark factual updates `not assessed`. Without execution, list the commands and links still unverified. Do not update a version, count, status, or current fact from memory.

## Decision Rules

| Condition | Action | Failure or risk avoided |
| --- | --- | --- |
| A behaviour, interface, dependency, route, or release gate changed | Update its owning document and cross-references | Documentation that contradicts the repository. |
| A historical document remains useful but contains stale status | Add a dated supersession note rather than rewriting history | Loss of audit context. |
| Machine output conflicts with a hand-maintained count | Use machine output and identify the active-root rule | Cached catalogue claims becoming authoritative. |
| Evidence for a current external fact is unavailable | Remove, qualify, or defer the claim | Stale legal, financial, platform, or market guidance. |

## Anti-Patterns

- Updating only README after an authoring-gate change. Correction: also check AGENTS, CLAUDE, CONTRIBUTING, CI, and quality records.
- Copying a cached active-skill count. Correction: discover active `SKILL.md` files from declared roots and record the command.
- Rewriting an old audit to make it appear current. Correction: preserve history and add a dated final-state record or supersession note.
- Describing a validator that was not run. Correction: quote the actual command and measured result or mark it pending.
- Adding a live exchange rate or statutory threshold from memory. Correction: use the governing source register and dated verification.
- Fixing implementation code while assigned documentation only. Correction: stop at the documentation boundary and route the code change to its owner.

## Worked Example

After adding `scripts/validate_skill_engine.py`, update README with the command, AGENTS and CLAUDE with the mandatory gate, CONTRIBUTING with the release sequence, CI with the executable check, and the upgrade record with measured results. Do not claim zero debt until the baseline run exits successfully.

## Workflow

1. Inspect the authorised change, its diff, validation evidence, and owning documentation.
2. Map behaviour, interfaces, commands, routes, and counts to specific files; stop if missing evidence would force a factual guess.
3. Update the most specific documents before summaries and repository instructions.
4. Recover a stale or conflicting statement by using machine output or the governing source, then rerun links, commands, and consistency checks.

## References

- `AGENTS.md` owns repository-wide routing and release rules.
- `skills/meta-utility/skill-writing/SKILL.md` owns the portable skill contract.
- `CONTRIBUTING.md` owns the maintainer procedure.

<!-- dual-compat-end -->

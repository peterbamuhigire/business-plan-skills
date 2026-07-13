# Dual-surface migration rules

Parent: [Skill Writing](../SKILL.md)

Use one canonical portable `SKILL.md` per reusable procedure and keep repository-wide orchestration in `AGENTS.md` or `CLAUDE.md`.

## Ownership boundary

| Content | Owner | Reason |
| --- | --- | --- |
| Trigger, inputs, decisions, workflow, safety, degraded mode, outputs, evidence | `SKILL.md` | Travels with the procedure. |
| Deep examples, schemas, checklists, case material | Directly linked `references/*.md` | Preserves progressive disclosure. |
| Repository routing, active roots, shared gates, release commands | `AGENTS.md` and maintainer documentation | Applies across skills. |
| Runner commands, model selection, UI settings | Thin runner adapter | Must not contaminate portable skill bodies. |

## Migration sequence

1. Inventory active skills from the filesystem and separate templates or inactive aliases.
2. Preserve the existing scope and useful domain content unless collision evidence supports a split or consolidation.
3. Replace invalid metadata and weak descriptions with the approved portable frontmatter.
4. Declare inputs, outputs, evidence, permission boundary, degraded mode, decisions, stop conditions, recovery, and acceptance before rearranging explanatory prose.
5. Extract long material only when the entrypoint would exceed 500 lines or routing-critical instructions are obscured.
6. Add positive, negative, collision, limited-capability, and failure-path fixtures.
7. Run the local validator, routing smoke test, canonical scanner, and canonical per-skill validator.
8. Record before and after measurements; a baseline with failures is not a waiver.

## Stop conditions

- Stop if a pre-existing user change overlaps the intended edit and ownership cannot be reconciled.
- Stop if remote `main` has diverged and safe integration cannot be proved.
- Stop if a proposed split, rename, deletion, or deactivation lacks routing evidence.
- Stop if missing evidence would force invented domain decisions, thresholds, examples, or finance facts.

## Release rule

Release only when the machine-readable baseline has empty failure counts, every routing fixture meets the documented top-three threshold, canonical validation passes, and the final diff contains no cache, secret, or unrelated edit.

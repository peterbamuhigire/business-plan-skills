# Contributing to the business-plan skills engine

The active catalogue is discovered from `skills/**/SKILL.md` and `country-context/**/SKILL.md`. Do not use a README table as the source of truth, and do not count templates or inactive aliases as active skills.

## Author a skill

1. Read `AGENTS.md` and `skills/meta-utility/skill-writing/SKILL.md`.
2. Search neighbouring frontmatter descriptions before adding a directory.
3. Start from `skills/meta-utility/skill-writing/references/dual-compatible-skill-template.md`.
4. Preserve domain knowledge and move only long catalogues, schemas, examples, or background material into directly linked `references/` files.
5. Add or update fixtures in `tests/routing-fixtures.json` for positive, negative, neighbour-collision, limited-capability, and failure paths.

Every active skill requires a directory-matching name; a one-line `Use when` description of at most 350 characters; portable metadata; trigger boundaries; input, output, and evidence contracts; an ordered workflow with stop and recovery behaviour; a domain decision table; capability and permission boundaries; degraded mode; quality standards; five concrete anti-patterns with fixes; and directly linked references. Audit and review skills default to read-only.

## Validate a change

Run from the repository root:

```powershell
python -X utf8 scripts\validate_skill_engine.py --baseline docs\quality\skill-quality-baseline.json
python -X utf8 scripts\routing_smoke_test.py --threshold 1.0
python -X utf8 skills\meta-utility\skill-writing\scripts\quick_validate.py <skill-directory>
git diff --check
```

On Peter's development machine, also run the canonical scanner for both active roots and the canonical quick validator for every changed skill directory. The baseline must keep `failure_counts` empty; it is a regression lock, not a waiver.

## Finance and evidence gates

Any skill touching money, inventory, payroll, tax, grants, banking, POS, mobile money, statutory compliance, or accounting records consumes the external Chwezi Accounting and Finance Doctrine. Do not hardcode current statutory values or imply professional sign-off. Record the finance gate in the release manifest.

Run `writing-quality`, `meta-critical-thinking-business-logic`, and `anti-ai-slop` before release. Run `ai-slop-audit` after each major cohort and at the final gate. A grade F blocks progression.

## Release procedure

1. Fetch `origin` and confirm local `main` is not behind.
2. Run all repository, routing, canonical, link, syntax, and diff checks.
3. Inspect the complete diff for unrelated files, generated caches, secrets, and accidental deletions.
4. Update the active count and evidence in `README.md` and the upgrade record from machine output.
5. Stage intended files, review the staged diff, commit once, and push without force.
6. Verify `HEAD` equals `origin/main` and the worktree is clean.

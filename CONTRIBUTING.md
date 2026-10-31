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

Run from the repository root. The commands use `python3` (use `python` on Windows) and need PyYAML for the catalogue, routing and skill checks; the README's Checks paragraph says which check needs PyYAML, Node.js, LibreOffice or `xlsxwriter`.

```sh
python3 -X utf8 scripts/validate_skill_engine.py --baseline docs/quality/skill-quality-baseline.json
python3 -X utf8 scripts/routing_smoke_test.py --threshold 1.0 --report --min-precision-at-1 0.80
python3 -X utf8 scripts/routing_link_check.py
python3 -X utf8 scripts/check_text_integrity.py
python3 -X utf8 scripts/source_ingestion_guardrail.py
python3 -X utf8 skills/meta-utility/skill-writing/scripts/quick_validate.py <skill-directory>
python3 -X utf8 tools/evidence-register/refresh_evidence_register.py --check
python3 -X utf8 tools/sector-gates/validate_sector_gates.py
python3 -X utf8 tools/exemplar-packs/validate_exemplar_packs.py
for bundle in examples/full-plan-packages/*/release-bundle.json; do
  python3 -X utf8 tools/release-gate/validate_release_bundle.py "$bundle"
done
python3 -X utf8 scripts/build-financial-models/verify_workbooks.py
python3 -X utf8 -m unittest discover -s tests -p "test_*.py"
python3 -m compileall -q scripts tools skills/meta-utility/skill-writing/scripts
node hooks/test-destructive-bash-gate.js
node hooks/test-plugin-hook-config.js
git diff --check
```

On Windows, call `validate_release_bundle.py` once for each `release-bundle.json` under `examples/full-plan-packages/` instead of using the shell loop. `compileall` writes git-ignored `__pycache__` folders.

Two results are expected and recorded rather than failures of your change. `refresh_evidence_register.py --check` exits 1 while register rows are overdue (4 of 24 on 31 October 2026); a change must not add an overdue row, and the dates on which more rows fall due are in the README. `validate_release_bundle.py` reports `decision=blocked` for all four example packs; a structurally valid blocked bundle is the correct result.

The model builders in `scripts/build-financial-models/` need `xlsxwriter` and overwrite the shipped templates in place, so run them in a copy of the repository and commit only the regenerated file you intend to change.

On Peter's development machine, also run the canonical quick validator for every changed skill directory. The research engine's `scripts/skill_contract_validator.py` cannot yet scan this engine by path (with `--root skills` it exits 1, reads 0 skills and reports six `missing_mandatory_resource` findings), so record its result as `not assessed`. The baseline must keep `failure_counts` empty; it is a regression lock, not a waiver.

## Finance and evidence gates

Any skill touching money, inventory, payroll, tax, grants, banking, POS, mobile money, statutory compliance, or accounting records consumes the external Chwezi Accounting and Finance Doctrine. Do not hardcode current statutory values or imply professional sign-off. Record the finance gate in the release manifest.

Current-source portals identify where to verify; they do not prove a copied figure. An active country context must link to the dated evidence register. Regulated activity must pass the applicable central sector screen, and an unavailable professional or authority check remains `not assessed`.

For an XLSX deliverable, run `tools/workbook-audit/formula_map.py` and `tools/workbook-audit/recalc_check.py` and retain both JSON reports; the second recalculates a copy in LibreOffice, so stored placeholder values and formula-sourced tie-outs are tested, and exit 2 means `not-assessed`. `validate_release_bundle.py` does not yet require the recalculation report, so record it in the bundle evidence yourself. Broken references, formula errors, missing required scenarios, missing reconciliation checks or external workbook links block release. Audience exemplars are validated reference packs; replace every illustrative input and re-run finance, evidence, regulatory and committee gates for client work.

For a complete plan, use `business-plan-orchestrator`, apply `references/cross-engine-delivery-contract.md`, and validate a populated release bundle. A native document must be written and opened; a layout-sensitive artefact must also be rendered and visually reviewed. Automated validation does not substitute for claim verification, professional judgement, or release authority.

Run `writing-quality`, `meta-critical-thinking-business-logic`, and `anti-ai-slop` before release. Run `ai-slop-audit` after each major cohort and at the final gate. A grade F blocks progression.

## Release procedure

1. Fetch `origin` and confirm local `main` is not behind.
2. Run all repository, routing, canonical, link, syntax, and diff checks.
3. Inspect the complete diff for unrelated files, generated caches, secrets, and accidental deletions.
4. Update the active count and evidence in `README.md` and the upgrade record from machine output (`validate_skill_engine.py` prints the active skill count).
5. Stage intended files, review the staged diff, commit once, and push without force.
6. Verify `HEAD` equals `origin/main` and the worktree is clean.

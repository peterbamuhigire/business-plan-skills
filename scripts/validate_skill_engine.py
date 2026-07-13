#!/usr/bin/env python3
"""Validate the business-plan skill catalogue against the July 2026 contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

import yaml


ACTIVE_ROOTS = ("skills", "country-context")
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
COMPATIBILITY = ["claude-code", "codex"]
MAX_LINES = 500
FRONTMATTER = re.compile(r"^\ufeff?---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
MOJIBAKE = ("Ãƒ", "Ã‚", "Ã¢", "ðŸ", "â€", "\ufffd")
RUNNER_SPECIFIC = (
    "chat.customAgentInSubagent.enabled",
    "latest VS Code Insiders build",
    ".github/copilot-instructions.md",
)
REQUIRED_HEADING_GROUPS = {
    "use_when": ("Use When",),
    "do_not_use_when": ("Do Not Use When",),
    "required_inputs": ("Required Inputs", "Inputs"),
    "workflow": ("Workflow",),
    "quality_standards": ("Quality Standards", "Quality Bar"),
    "anti_patterns": ("Anti-Patterns", "Domain Anti-Patterns"),
    "outputs": ("Outputs",),
    "evidence_produced": ("Evidence Produced",),
    "capability_contract": ("Capability Contract", "Capability and Permission Boundaries"),
    "degraded_mode": ("Degraded Mode",),
    "decision_rules": ("Decision Rules", "Decision Rules / Stop Conditions"),
    "references": ("References", "Read Next", "Companion Skills"),
}
MANDATORY_FILES = (
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    ".github/workflows/skill-quality.yml",
    "scripts/validate_skill_engine.py",
    "scripts/routing_smoke_test.py",
    "tests/routing-fixtures.json",
    "docs/quality/skill-quality-baseline.json",
    "skills/meta-utility/skill-writing/references/dual-compatible-skill-template.md",
)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--details", action="store_true")
    return parser.parse_args()


def section(body: str, heading: str) -> str:
    matches = re.findall(
        rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s|\Z)",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    return "\n".join(match.strip() for match in matches if match.strip())


def grouped_section(body: str, aliases: tuple[str, ...]) -> str:
    return "\n".join(section(body, alias) for alias in aliases if section(body, alias)).strip()


def has_heading(body: str, heading: str) -> bool:
    return bool(re.search(rf"^##\s+{re.escape(heading)}\s*$", body, re.MULTILINE | re.IGNORECASE))


def parse_skill(path: Path) -> tuple[dict, str, str, list[str]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    match = FRONTMATTER.match(raw)
    if not match:
        return {}, raw, raw, ["frontmatter"]
    try:
        metadata = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}, raw[match.end():], raw, ["frontmatter_yaml"]
    if not isinstance(metadata, dict):
        return {}, raw[match.end():], raw, ["frontmatter_type"]
    return metadata, raw[match.end():], raw, []


def table_contract(text: str, required_terms: tuple[str, ...]) -> bool:
    if "|" not in text:
        return False
    header = next((line.lower() for line in text.splitlines() if line.strip().startswith("|")), "")
    return all(term in header for term in required_terms)


def local_links(skill: Path, body: str, root: Path) -> list[str]:
    failures: list[str] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        target = unquote(target.split("#", 1)[0].strip())
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        resolved = (skill.parent / target).resolve()
        if not resolved.exists():
            failures.append(f"broken_link:{target}")
    return failures


def assess(path: Path, root: Path) -> dict:
    frontmatter, body, raw, failures = parse_skill(path)
    description = frontmatter.get("description", "")
    metadata = frontmatter.get("metadata") if isinstance(frontmatter.get("metadata"), dict) else {}
    unexpected = sorted(set(frontmatter) - ALLOWED_FRONTMATTER)
    if unexpected:
        failures.append("unsupported_frontmatter:" + ",".join(unexpected))
    if frontmatter.get("name") != path.parent.name:
        failures.append("identity")
    if not isinstance(description, str) or not description.strip().lower().startswith("use when") or len(description.strip()) > 350 or "\n" in description.strip():
        failures.append("description_trigger")
    if metadata.get("portable") is not True or metadata.get("compatible_with") != COMPATIBILITY:
        failures.append("portable_metadata")
    if "<!-- dual-compat-start -->" not in body or "<!-- dual-compat-end -->" not in body:
        failures.append("portable_markers")

    for key, aliases in REQUIRED_HEADING_GROUPS.items():
        content = grouped_section(body, aliases)
        if not any(has_heading(body, alias) for alias in aliases):
            failures.append("missing_section:" + key)
        elif not content:
            failures.append("empty_section:" + key)

    use_when = section(body, "Use When")
    do_not = section(body, "Do Not Use When")
    inputs = grouped_section(body, ("Required Inputs", "Inputs"))
    outputs = section(body, "Outputs")
    evidence = section(body, "Evidence Produced")
    workflow = grouped_section(body, ("Workflow",))
    decisions = grouped_section(body, ("Decision Rules", "Decision Rules / Stop Conditions"))
    anti = grouped_section(body, ("Anti-Patterns", "Domain Anti-Patterns"))
    capability = grouped_section(body, ("Capability Contract", "Capability and Permission Boundaries"))
    degraded = section(body, "Degraded Mode")

    if len(re.findall(r"^\s*[-*]\s+", use_when, re.MULTILINE)) < 1:
        failures.append("positive_trigger")
    if len(re.findall(r"^\s*[-*]\s+", do_not, re.MULTILINE)) < 1 or not re.search(r"neighbou?r|instead|route|use `|unlike|while `", do_not + " " + description, re.IGNORECASE):
        failures.append("negative_trigger")
    if not ("|" in inputs and re.search(r"artefact|artifact|input", inputs, re.IGNORECASE) and re.search(r"source|provider|produced by", inputs, re.IGNORECASE) and re.search(r"required", inputs, re.IGNORECASE) and re.search(r"missing|absent|unavailable", inputs, re.IGNORECASE)) and not re.search(r"\bnone\b", inputs, re.IGNORECASE):
        failures.append("input_contract")
    if not ("|" in outputs and re.search(r"artefact|artifact|output", outputs, re.IGNORECASE) and re.search(r"consumer|consumed by", outputs, re.IGNORECASE) and re.search(r"acceptance", outputs, re.IGNORECASE)):
        failures.append("output_contract")
    if not table_contract(evidence, ("evidence", "format", "acceptance")):
        failures.append("evidence_contract")
    if len(re.findall(r"^\s*\d+\.\s+", workflow, re.MULTILINE)) < 3:
        failures.append("ordered_workflow")
    if not re.search(r"stop|block|halt", workflow, re.IGNORECASE):
        failures.append("stop_condition")
    if not re.search(r"recover|retry|revise|return|escalat", workflow, re.IGNORECASE):
        failures.append("recovery")
    if not ("|" in decisions and re.search(r"condition|choice|decision|evidence", decisions, re.IGNORECASE) and re.search(r"action", decisions, re.IGNORECASE) and re.search(r"failure|risk|wrong", decisions, re.IGNORECASE)):
        failures.append("decision_contract")
    if len(re.findall(r"^\s*[-*]\s+|^\s*\d+\.\s+", anti, re.MULTILINE)) < 5:
        failures.append("five_anti_patterns")
    if anti and len(re.findall(r"\b(?:fix|correction)\s*:", anti, re.IGNORECASE)) < 5:
        failures.append("anti_pattern_corrections")
    if not re.search(r"read|search", capability, re.IGNORECASE) or not re.search(r"authori[sz]|permission|boundary", capability, re.IGNORECASE):
        failures.append("capability_contract")
    if not re.search(r"unavailable|cannot|without", degraded, re.IGNORECASE) or not re.search(r"qualified|not assessed|gap|narrow", degraded, re.IGNORECASE):
        failures.append("degraded_mode")
    audit_like = bool(re.search(r"audit|review|critique|assessment|diagnostic", path.parent.name, re.IGNORECASE) or re.match(r"Use when (?:auditing|reviewing|critiquing|assessing|diagnosing)", description, re.IGNORECASE))
    if audit_like and not re.search(r"read-only", capability + " " + do_not, re.IGNORECASE):
        failures.append("audit_read_only_default")
    if len(raw.splitlines()) > MAX_LINES:
        failures.append("line_limit")
    if any(marker in raw for marker in MOJIBAKE):
        failures.append("encoding_noise")
    if any(marker in body for marker in RUNNER_SPECIFIC):
        failures.append("runner_specific_body")
    in_fence = False
    for line in body.splitlines():
        fence = re.match(r"^```([^`]*)$", line.strip())
        if not fence:
            continue
        if in_fence:
            in_fence = False
            continue
        if not fence.group(1).strip():
            failures.append("untagged_code_fence")
            break
        in_fence = True
    failures.extend(local_links(path, body, root))
    return {"path": path.relative_to(root).as_posix(), "name": frontmatter.get("name"), "failures": sorted(set(failures)), "lines": len(raw.splitlines())}


def validate_baseline(payload: dict, baseline_path: Path, root: Path) -> list[str]:
    problems: list[str] = []
    path = baseline_path if baseline_path.is_absolute() else root / baseline_path
    if not path.exists():
        return [f"baseline_missing:{path}"]
    try:
        baseline = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"baseline_invalid:{exc}"]
    if baseline.get("failure_counts") != {}:
        problems.append("baseline_is_not_zero_debt")
    if baseline.get("active_skill_count") != payload["active_skill_count"]:
        problems.append("baseline_active_count_mismatch")
    if baseline.get("template_count") != payload["template_count"]:
        problems.append("baseline_template_count_mismatch")
    if payload["failure_counts"] != baseline.get("failure_counts"):
        problems.append("baseline_regression")
    return problems


def repeated_boilerplate(files: list[Path], root: Path) -> list[dict]:
    occurrences: defaultdict[str, set[str]] = defaultdict(set)
    for path in files:
        raw = path.read_text(encoding="utf-8", errors="replace")
        body = FRONTMATTER.sub("", raw, count=1)
        body = re.sub(r"```[\s\S]*?```", "", body)
        for paragraph in re.split(r"\n\s*\n", body):
            normal = " ".join(paragraph.split())
            if len(normal) < 160 or "|" in normal or normal.startswith("#"):
                continue
            occurrences[normal].add(path.relative_to(root).as_posix())
    return [
        {"text": text, "paths": sorted(paths)}
        for text, paths in sorted(occurrences.items())
        if len(paths) >= 3
    ]


def repeated_contract_rows(files: list[Path], root: Path) -> list[dict]:
    occurrences: defaultdict[str, set[str]] = defaultdict(set)
    aliases = ("Decision Rules", "Decision Rules / Stop Conditions")
    for path in files:
        raw = path.read_text(encoding="utf-8", errors="replace")
        for alias in aliases:
            block = section(raw, alias)
            for line in block.splitlines():
                normal = " ".join(line.split())
                if len(normal) < 80 or not normal.startswith("|"):
                    continue
                if re.fullmatch(r"\|?[\s:|-]+\|?", normal):
                    continue
                lowered = normal.lower()
                if "acceptance condition" in lowered or "failure or risk" in lowered or "behaviour when" in lowered:
                    continue
                if lowered.startswith("| evidence sources conflict | prefer the competent primary source"):
                    continue
                occurrences[normal].add(path.relative_to(root).as_posix())
    return [
        {"text": text, "paths": sorted(paths)}
        for text, paths in sorted(occurrences.items())
        if len(paths) >= 3
    ]


def main() -> int:
    args = arguments()
    root = args.root.resolve()
    files = sorted({p for active in ACTIVE_ROOTS for p in (root / active).rglob("SKILL.md") if p.is_file()})
    results = [assess(path, root) for path in files]
    failures: Counter[str] = Counter()
    names: defaultdict[str, list[str]] = defaultdict(list)
    for result in results:
        failures.update(result["failures"])
        if result["name"]:
            names[str(result["name"])].append(result["path"])
    duplicate_names = {name: paths for name, paths in names.items() if len(paths) > 1}
    if duplicate_names:
        failures["duplicate_names"] = len(duplicate_names)
    mandatory_missing = [item for item in MANDATORY_FILES if not (root / item).exists()]
    if mandatory_missing:
        failures["missing_engine_resource"] = len(mandatory_missing)
    boilerplate = repeated_boilerplate(files, root)
    if boilerplate:
        failures["repeated_boilerplate"] = len(boilerplate)
    repeated_rows = repeated_contract_rows(files, root)
    if repeated_rows:
        failures["repeated_contract_rows"] = len(repeated_rows)
    template_count = sum(1 for p in (root / "templates").rglob("*") if p.is_file()) + sum(1 for p in (root / "skills" / "meta-utility" / "skill-writing" / "references").glob("*template*.md"))
    payload = {
        "engine": "business-plan-skills",
        "active_roots": list(ACTIVE_ROOTS),
        "active_skill_count": len(files),
        "template_count": template_count,
        "fully_compliant": sum(not result["failures"] for result in results),
        "failure_counts": dict(sorted(failures.items())),
        "duplicate_names": duplicate_names,
        "missing_engine_resources": mandatory_missing,
        "repeated_boilerplate": boilerplate,
        "repeated_contract_rows": repeated_rows,
        "results": results if args.details else [],
    }
    baseline_problems = validate_baseline(payload, args.baseline, root) if args.baseline else []
    if baseline_problems:
        payload["baseline_problems"] = baseline_problems
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"skill-engine: {root}")
        print(f"- active skills: {payload['active_skill_count']}")
        print(f"- templates: {payload['template_count']}")
        print(f"- fully compliant: {payload['fully_compliant']}")
        print("- failure counts:")
        for name, count in payload["failure_counts"].items():
            print(f"  - {name}: {count}")
        for item in mandatory_missing:
            print(f"- missing resource: {item}")
        if args.details:
            for result in results:
                if result["failures"]:
                    print(f"- {result['path']}: {', '.join(result['failures'])}")
            for item in boilerplate:
                print(f"- repeated boilerplate ({len(item['paths'])} skills): {item['text'][:160]}")
            for item in repeated_rows:
                print(f"- repeated contract row ({len(item['paths'])} skills): {item['text'][:160]}")
        for problem in baseline_problems:
            print(f"- baseline: {problem}")
    return 1 if failures or baseline_problems else 0


if __name__ == "__main__":
    raise SystemExit(main())

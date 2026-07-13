#!/usr/bin/env python3
"""Validate one skill directory against the repository's July 2026 contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ALLOWED = {"name", "description", "license", "allowed-tools", "metadata"}
REQUIRED = (
    "Use When", "Do Not Use When", "Required Inputs", "Workflow", "Quality Standards",
    "Anti-Patterns", "Outputs", "Evidence Produced", "Capability Contract", "Degraded Mode",
    "Decision Rules", "References",
)


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    path = skill_dir / "SKILL.md"
    if not path.exists():
        return ["SKILL.md not found"]
    raw = path.read_text(encoding="utf-8", errors="replace")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", raw, re.DOTALL)
    if not match:
        return ["invalid or missing YAML frontmatter"]
    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return [f"invalid YAML: {exc}"]
    if not isinstance(frontmatter, dict):
        return ["frontmatter must be a mapping"]
    unexpected = sorted(set(frontmatter) - ALLOWED)
    if unexpected:
        errors.append("unsupported frontmatter keys: " + ", ".join(unexpected))
    if frontmatter.get("name") != skill_dir.name:
        errors.append(f"name must match directory `{skill_dir.name}`")
    description = frontmatter.get("description")
    if not isinstance(description, str) or not description.strip().lower().startswith("use when") or len(description.strip()) > 350 or "\n" in description.strip():
        errors.append("description must be one line, start with `Use when`, and be <=350 characters")
    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict) or metadata.get("portable") is not True or metadata.get("compatible_with") != ["claude-code", "codex"]:
        errors.append("portable metadata must declare compatible_with: [claude-code, codex]")
    body = raw[match.end():]
    if "<!-- dual-compat-start -->" not in body or "<!-- dual-compat-end -->" not in body:
        errors.append("portable contract markers are missing")
    for heading in REQUIRED:
        found = re.search(rf"^##\s+{re.escape(heading)}\s*$([\s\S]*?)(?=^##\s|\Z)", body, re.MULTILINE | re.IGNORECASE)
        if not found or not found.group(1).strip():
            errors.append(f"missing or empty `{heading}` section")
    if len(raw.splitlines()) > 500:
        errors.append(f"SKILL.md exceeds 500 lines ({len(raw.splitlines())})")
    if "\ufffd" in raw:
        errors.append("replacement character found")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        clean = target.split("#", 1)[0].strip()
        if clean and not clean.startswith(("http://", "https://", "mailto:", "#")) and not (path.parent / clean).resolve().exists():
            errors.append(f"broken local link: {target}")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -X utf8 quick_validate.py <skill-directory>")
        return 1
    errors = validate(Path(sys.argv[1]).resolve())
    if not errors:
        print("Skill is valid.")
        return 0
    print("Skill validation failed:")
    for error in errors:
        print("- " + error)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

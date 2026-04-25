#!/usr/bin/env python3
"""Quick validation script for skills."""

import sys
import re
from pathlib import Path

import yaml


REQUIRED_HEADINGS = {
    "use when",
    "do not use when",
    "required inputs",
    "workflow",
    "quality bar",
    "anti-patterns",
    "outputs",
}

WARNING_PLACEHOLDER = "Use when this skill is the primary workflow for the requested task."

def validate_skill(skill_path):
    """Validate a skill and return (ok, message)."""
    skill_path = Path(skill_path)
    warnings = []

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    # Define allowed properties
    allowed_properties = {'name', 'description'}

    # Check for unexpected properties (excluding nested keys under metadata)
    unexpected_keys = set(frontmatter.keys()) - allowed_properties
    if unexpected_keys:
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(allowed_properties))}"
        )

    # Check required fields
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # Extract name for validation
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        # Check naming convention (hyphen-case: lowercase with hyphens)
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        # Check name length (max 64 characters per spec)
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # Extract and validate description
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        # Check for angle brackets
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        # Check description length (max 1024 characters per spec)
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    body = content[match.end():]
    headings = {h.strip().lower() for h in re.findall(r"^##\s+(.+)$", body, re.MULTILINE)}
    missing_headings = sorted(REQUIRED_HEADINGS - headings)
    if missing_headings:
        return False, (
            "Missing required section heading(s): "
            + ", ".join(missing_headings)
        )

    if WARNING_PLACEHOLDER in body:
        warnings.append(
            "placeholder scaffold text still present; replace generic guidance with skill-specific instructions"
        )

    line_count = len(content.splitlines())
    if line_count > 500:
        warnings.append(
            f"SKILL.md is {line_count} lines; preferred maximum is 500 lines"
        )

    if "## Overview" not in body:
        warnings.append("missing Overview section")

    if "## References" not in body and "references/" in body:
        warnings.append("references are mentioned inline but there is no dedicated References section")

    if warnings:
        return True, "Skill is valid with warnings: " + "; ".join(warnings)
    return True, "Skill is valid."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)

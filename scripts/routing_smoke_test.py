#!/usr/bin/env python3
"""Run deterministic top-three routing checks against active skill metadata."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml


STOP = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "i", "in",
    "is", "it", "my", "of", "on", "or", "our", "the", "this", "to", "we", "with",
    "when", "use", "need", "please", "want", "write", "create", "make", "help",
}
FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


def tokens(text: str) -> list[str]:
    return [word for word in re.findall(r"[a-z0-9]+", text.lower()) if word not in STOP and len(word) > 1]


def load_catalogue(root: Path) -> list[dict]:
    skills: list[dict] = []
    for active in ("skills", "country-context"):
        for path in sorted((root / active).rglob("SKILL.md")):
            raw = path.read_text(encoding="utf-8", errors="replace")
            match = FRONTMATTER.match(raw)
            if not match:
                continue
            try:
                frontmatter = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError:
                continue
            name = frontmatter.get("name")
            description = frontmatter.get("description", "")
            if not isinstance(name, str) or not isinstance(description, str):
                continue
            use_match = re.search(r"^##\s+Use When\s*$([\s\S]*?)(?=^##\s|\Z)", raw[match.end():], re.MULTILINE | re.IGNORECASE)
            use_when = use_match.group(1) if use_match else ""
            skills.append({"name": name, "description": description, "use_when": use_when})
    return skills


def score(prompt: str, skill: dict) -> float:
    prompt_tokens = tokens(prompt)
    prompt_set = set(prompt_tokens)
    description_tokens = tokens(skill["description"])
    body_tokens = tokens(skill["use_when"])
    slug_tokens = tokens(skill["name"].replace("-", " "))
    value = 0.0
    value += 4.0 * sum(1 for word in description_tokens if word in prompt_set)
    value += 1.5 * sum(1 for word in body_tokens if word in prompt_set)
    value += 2.5 * sum(1 for word in slug_tokens if word in prompt_set)
    prompt_bigrams = set(zip(prompt_tokens, prompt_tokens[1:]))
    description_bigrams = set(zip(description_tokens, description_tokens[1:]))
    value += 6.0 * len(prompt_bigrams & description_bigrams)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--fixtures", type=Path, default=Path("tests/routing-fixtures.json"))
    parser.add_argument("--threshold", type=float, default=1.0, help="Required top-three precision, 0-1.")
    args = parser.parse_args()
    root = args.root.resolve()
    fixture_path = args.fixtures if args.fixtures.is_absolute() else root / args.fixtures
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    catalogue = load_catalogue(root)
    names = {item["name"] for item in catalogue}
    failures: list[str] = []
    passed = 0
    for fixture in fixtures:
        expected = fixture["expected"]
        if expected not in names:
            failures.append(f"{fixture['id']}: expected skill `{expected}` is not active")
            continue
        ranked = sorted(catalogue, key=lambda item: (-score(fixture["prompt"], item), item["name"]))
        top_three = [item["name"] for item in ranked[:3]]
        excluded = fixture.get("excluded", [])
        ok = expected in top_three and not any(name == top_three[0] for name in excluded)
        if ok:
            passed += 1
        else:
            failures.append(f"{fixture['id']}: expected={expected}; top3={top_three}; excluded={excluded}")
    total = len(fixtures)
    precision = passed / total if total else 0.0
    classes = sorted({fixture.get("class", "unspecified") for fixture in fixtures})
    print(f"routing-smoke: {passed}/{total} top-three matches ({precision:.1%}); threshold={args.threshold:.1%}")
    print("- fixture classes: " + ", ".join(classes))
    for failure in failures:
        print("- " + failure)
    return 0 if precision >= args.threshold and not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())

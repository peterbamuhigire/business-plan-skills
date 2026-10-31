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


SKIPPED: list[str] = []


def load_catalogue(root: Path) -> list[dict]:
    """Read active skill metadata; record in SKIPPED any skill that cannot be read."""
    SKIPPED.clear()
    skills: list[dict] = []
    for active in ("skills", "country-context"):
        for path in sorted((root / active).rglob("SKILL.md")):
            raw = path.read_text(encoding="utf-8", errors="replace")
            relative = path.relative_to(root).as_posix()
            match = FRONTMATTER.match(raw)
            if not match:
                SKIPPED.append(f"{relative}: no frontmatter")
                continue
            try:
                frontmatter = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError as exc:
                SKIPPED.append(f"{relative}: frontmatter does not parse ({type(exc).__name__})")
                continue
            name = frontmatter.get("name")
            description = frontmatter.get("description", "")
            if not isinstance(name, str) or not isinstance(description, str):
                SKIPPED.append(f"{relative}: name or description is not text")
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
    parser.add_argument("--min-precision-at-1", type=float, default=None,
                        help="Optional floor for first-place precision, 0-1; omitted means report only.")
    parser.add_argument("--report", action="store_true",
                        help="Also print precision@1 and per-skill fixture coverage.")
    args = parser.parse_args()
    root = args.root.resolve()
    fixture_path = args.fixtures if args.fixtures.is_absolute() else root / args.fixtures
    fixtures = json.loads(fixture_path.read_text(encoding="utf-8"))
    catalogue = load_catalogue(root)
    names = {item["name"] for item in catalogue}
    failures: list[str] = [f"skill skipped, so it cannot be routed to: {item}" for item in SKIPPED]
    passed = 0
    first_place = 0
    positives: dict[str, int] = {}
    owned_negatives: dict[str, int] = {}
    for fixture in fixtures:
        expected = fixture["expected"]
        if expected not in names:
            failures.append(f"{fixture['id']}: expected skill `{expected}` is not active")
            continue
        ranked = sorted(catalogue, key=lambda item: (-score(fixture["prompt"], item), item["name"]))
        top_three = [item["name"] for item in ranked[:3]]
        excluded = fixture.get("excluded", [])
        first_place += top_three[0] == expected
        positives[expected] = positives.get(expected, 0) + 1
        for owner in excluded:
            owned_negatives[owner] = owned_negatives.get(owner, 0) + 1
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
    first_precision = first_place / total if total else 0.0
    if args.report or args.min_precision_at_1 is not None:
        covered = sum(1 for name in names if positives.get(name, 0) >= 3 and owned_negatives.get(name, 0) >= 2)
        print(f"- precision@1: {first_place}/{total} ({first_precision:.1%})")
        print(f"- skills with at least one fixture: {sum(1 for name in names if positives.get(name, 0))}/{len(names)}")
        print(f"- skills with 3 or more positives: {sum(1 for name in names if positives.get(name, 0) >= 3)}/{len(names)}")
        print(f"- skills with 2 or more owned negatives: {sum(1 for name in names if owned_negatives.get(name, 0) >= 2)}/{len(names)}")
        print(f"- skills with 3 positives and 2 owned negatives: {covered}/{len(names)}")
    floor_ok = args.min_precision_at_1 is None or first_precision >= args.min_precision_at_1
    if not floor_ok:
        print(f"- precision@1 {first_precision:.1%} is below the required {args.min_precision_at_1:.1%}")
    return 0 if precision >= args.threshold and not failures and floor_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

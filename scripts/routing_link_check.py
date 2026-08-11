#!/usr/bin/env python3
"""Check route references in high-use business-plan entry points."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_SURFACES = (
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "living-business-plan-operating-model.md",
    "skills/meta-strategy/meta-living-plan-governance/SKILL.md",
    "skills/pipeline/14-ai-integration/SKILL.md",
    "skills/meta-finance/meta-bankability-scoring/SKILL.md",
)
ROOT_PREFIXES = ("skills/", "country-context/", "book-extractions/", "references/")
PATH_TOKEN = re.compile(
    r"(?<![A-Za-z0-9_.-])(?:skills|country-context|book-extractions|references)/[A-Za-z0-9_./-]+"
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
RELATIVE_TOKEN = re.compile(r"(?<![A-Za-z0-9_.-])(?:\.\.?/)+(?:skills|book-extractions|references)/[A-Za-z0-9_./-]+")


def _clean(value: str) -> str:
    return value.split("#", 1)[0].strip().rstrip(".,;:)]}`")


def _resolve(root: Path, source: Path, value: str) -> Path | None:
    value = _clean(value)
    if not value or value.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if value.startswith(ROOT_PREFIXES[:3]):
        return (root / value).resolve()
    return (source.parent / value).resolve()


def candidates(source: Path, text: str) -> set[str]:
    values = set(PATH_TOKEN.findall(text))
    values.update(RELATIVE_TOKEN.findall(text))
    for target in MARKDOWN_LINK.findall(text):
        target = _clean(target)
        if target:
            values.add(target)
    return values


def scan(root: Path, surfaces: tuple[str, ...] = DEFAULT_SURFACES) -> list[str]:
    root = root.resolve()
    failures: list[str] = []
    for relative in surfaces:
        source = (root / relative).resolve()
        if not source.is_file():
            failures.append(f"{relative}: surface is missing")
            continue
        text = source.read_text(encoding="utf-8", errors="replace")
        for value in sorted(candidates(source, text)):
            target = _resolve(root, source, value)
            if target is None:
                continue
            if root not in target.parents and target != root:
                failures.append(f"{relative}: {value} (resolves outside repository)")
            elif not target.exists():
                failures.append(f"{relative}: {value}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("files", nargs="*", help="Optional repository-relative surfaces to scan.")
    args = parser.parse_args()
    surfaces = tuple(args.files) if args.files else DEFAULT_SURFACES
    failures = scan(args.root, surfaces)
    print(f"routing-link-check: {args.root.resolve()}")
    print(f"surfaces: {len(surfaces)}; failures: {len(failures)}")
    for failure in failures:
        print(f"FAIL: {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

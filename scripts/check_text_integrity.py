#!/usr/bin/env python3
"""Detect text corruption that structural validators cannot see.

A skill can keep every heading and link and still carry a wrong number, or a path
that exists only on one author's machine (drive letters, wamp64, home directories). In April
2026 a bulk rewrite removed every non-ASCII character from 47 files, so "3-5%"
(with an en dash) became "35%" and "9.75-10.5%" became "9.7510.5%". This check
looks for the signatures that kind of loss leaves behind, for host-specific
paths and for control characters, and it rejects any line proven to be a stripped copy of an original.

Scope: Markdown outside docs/ (skills, country context, references, templates,
rules, prompts and root documents). docs/ holds dated historical records.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

SCAN_SUFFIX = ".md"
SKIP_TOP_LEVEL = {"docs", ".git", "node_modules", "__pycache__", ".pytest_cache"}
HASH_FIXTURE = Path("tests") / "fixtures" / "stripped-operator-line-hashes.txt"
MIN_HASHED_LINE = 15

CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f\ufffd]")
SIGNATURES = (
    ("glued-year-range", re.compile(r"\b20\d{2}20\d{2}\b|\(20\d{4}\)|\bFY20\d{4}\b")),
    ("glued-thousands-groups", re.compile(r"\d,\d{4,},\d{3}")),
    ("glued-decimal-range", re.compile(r"\d+\.\d+\.\d+\s?%")),
    ("host-specific-path", re.compile(
        r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]|wamp64|/home/[a-z][a-z0-9_-]*/|/Users/[A-Za-z][A-Za-z0-9_.-]*/")),
)


def digest(line: str) -> str:
    return hashlib.sha256(line.rstrip().encode("utf-8")).hexdigest()[:16]


def load_hashes(path: Path) -> set[str]:
    if not path.is_file():
        return set()
    return {item.strip() for item in path.read_text(encoding="utf-8").splitlines() if item.strip()}


def markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob(f"*{SCAN_SUFFIX}")):
        relative = path.relative_to(root)
        if relative.parts and relative.parts[0] in SKIP_TOP_LEVEL:
            continue
        if any(part in {"node_modules", "__pycache__", ".git"} for part in relative.parts):
            continue
        files.append(path)
    return files


def validate_text_integrity(root: Path, hashes: Path | None = None) -> list[str]:
    """Return one problem string per finding; an empty list means clean."""
    root = root.resolve()
    known = load_hashes(hashes if hashes is not None else root / HASH_FIXTURE)
    problems: list[str] = []
    for path in markdown_files(root):
        name = path.relative_to(root).as_posix()
        try:
            with open(path, encoding="utf-8", newline="") as handle:
                text = handle.read()
        except (OSError, UnicodeDecodeError) as exc:
            problems.append(f"text-integrity: {name} cannot be read as UTF-8: {exc}")
            continue
        for number, line in enumerate(text.split("\n"), start=1):
            body = line.rstrip("\r")
            if number == 1 and body.startswith("﻿"):
                body = body[1:]
            if CONTROL.search(body):
                problems.append(f"text-integrity: {name}:{number} control or replacement character")
            for code, pattern in SIGNATURES:
                match = pattern.search(body)
                if match:
                    problems.append(f"text-integrity: {name}:{number} {code} near {match.group(0)!r}")
            if known and len(body.strip()) >= MIN_HASHED_LINE and digest(body) in known:
                problems.append(f"text-integrity: {name}:{number} line matches a known stripped-operator line")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--hashes", type=Path, help="Override the known-damaged-line hash file")
    args = parser.parse_args()
    problems = validate_text_integrity(args.root, args.hashes)
    for problem in problems:
        print(f"FAIL: {problem}")
    if problems:
        return 1
    print("PASS: no control characters, glued numeric ranges or known stripped lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())

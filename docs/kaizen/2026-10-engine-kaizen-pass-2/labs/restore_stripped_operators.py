#!/usr/bin/env python3
"""Restore numeric-operator characters removed by a historical non-ASCII strip.

Evidence method for backlog item B1 (kaizen pass 2). Read-only unless --apply.

A line is restored only when the damage is provable: in the damaging commit the
new line equals the old line with every non-ASCII character removed. Only the
numeric-operator class is put back (en dash, minus, multiplication, comparison,
plus-minus, division, root, degree, euro). Em dashes, arrows, section signs,
box drawing and emoji are deliberately left as they are.

Phase 1 replaces whole lines that still match the damaged text exactly.
Phase 2 handles lines edited after the damage: it restores a single operator
only when the surrounding ASCII context identifies exactly one place in one file.

With --emit-hashes <path> it also writes the truncated SHA-256 of every damaged
line (one per line, sorted) so a test can prove none of them returns.

Usage: restore_stripped_operators.py --commit <damaging-commit> [--apply] [--emit-hashes <path>]
Run from the repository root.
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
from collections import defaultdict
from pathlib import Path

RESTORE = set("–−×≥≤±÷√°€")
MIN_LINE = 15
CONTEXT = 24
MIN_CONTEXT = 10


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          encoding="utf-8", errors="replace", check=True).stdout


def ascii_only(text: str) -> str:
    return "".join(ch for ch in text if ord(ch) < 128)


def restored(old: str) -> str:
    return "".join(ch for ch in old if ord(ch) < 128 or ch in RESTORE)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--emit-hashes", type=Path)
    args = parser.parse_args()

    changed = git("diff", "--name-only", f"{args.commit}^", args.commit).splitlines()
    pairs: dict[str, str] = {}
    damaged_lines: set[str] = set()
    contexts: list[tuple[str, str, str]] = []
    for name in changed:
        if not name.endswith(".md"):
            continue
        try:
            old = git("show", f"{args.commit}^:{name}")
            new = git("show", f"{args.commit}:{name}")
        except subprocess.CalledProcessError:
            continue
        new_lines = set(new.splitlines())
        for line in old.splitlines():
            if not any(ch in RESTORE for ch in line):
                continue
            damaged = ascii_only(line)
            fixed = restored(line)
            if len(damaged.strip()) >= MIN_LINE and fixed != damaged:
                damaged_lines.add(damaged.rstrip())
            if len(damaged.strip()) >= MIN_LINE and damaged in new_lines and fixed != damaged:
                pairs[damaged] = fixed
            for index, ch in enumerate(line):
                if ch in RESTORE:
                    left = ascii_only(line[:index])[-CONTEXT:]
                    right = ascii_only(line[index + 1:])[:CONTEXT]
                    if len(left.strip()) >= MIN_CONTEXT and len(right.strip()) >= MIN_CONTEXT:
                        contexts.append((left, right, ch))

    targets = [p for p in git("ls-files", "*.md").splitlines() if not p.startswith("docs/")]
    texts = {}
    for p in targets:
        with open(p, encoding="utf-8", newline="") as handle:
            texts[p] = handle.read()
    phase1 = 0
    touched: dict[str, int] = defaultdict(int)
    for path, text in texts.items():
        lines = text.split("\n")
        out = []
        for line in lines:
            body = line.rstrip("\r")
            if body in pairs:
                out.append(pairs[body] + line[len(body):])
                phase1 += 1
                touched[path] += 1
            else:
                out.append(line)
        texts[path] = "\n".join(out)

    phase2 = 0
    ambiguous = 0
    for left, right, ch in contexts:
        joined = left + right
        hits = [(p, t.count(joined)) for p, t in texts.items() if joined in t]
        total = sum(n for _, n in hits)
        if total != 1:
            ambiguous += 1 if total > 1 else 0
            continue
        path = hits[0][0]
        texts[path] = texts[path].replace(joined, left + ch + right, 1)
        phase2 += 1
        touched[path] += 1

    if args.emit_hashes:
        digests = sorted({hashlib.sha256(line.encode("utf-8")).hexdigest()[:16] for line in damaged_lines})
        args.emit_hashes.parent.mkdir(parents=True, exist_ok=True)
        args.emit_hashes.write_text("\n".join(digests) + "\n", encoding="utf-8")
        print(f"hashes written: {len(digests)}")
    print(f"phase 1 whole-line restorations: {phase1}")
    print(f"phase 2 single-operator restorations: {phase2} (ambiguous contexts skipped: {ambiguous})")
    print(f"files touched: {len(touched)}")
    if args.apply:
        for path in touched:
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(texts[path])
        print("applied")
    else:
        print("dry run: nothing written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

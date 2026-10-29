#!/usr/bin/env python3
"""Check checkout and package-oriented file-entry counts against the ZIP cap."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

HARD_CAP = 5000
PACKAGE_EXCLUDES = {".git", ".cache", "cache", "__pycache__", "node_modules", ".venv", "venv"}


def count_entries(root: Path, package_only: bool = False) -> int:
    root = root.resolve()
    count = 0

    def fail(error: OSError) -> None:
        raise error

    for current, dirs, files in os.walk(root, topdown=True, followlinks=False, onerror=fail):
        current_path = Path(current)
        symlink_dirs = [name for name in dirs if (current_path / name).is_symlink()]
        if package_only:
            dirs[:] = [name for name in dirs
                       if name not in PACKAGE_EXCLUDES and not (current_path / name).is_symlink()]
        # os.walk does not descend through symlink directories; count the entry itself.
        counted_symlinks = [name for name in symlink_dirs
                            if not package_only or name not in PACKAGE_EXCLUDES]
        count += len(files) + len(counted_symlinks)
    return count


def validate_counts(counts: dict[str, int]) -> list[str]:
    return [f"{label} count {count} exceeds hard cap {HARD_CAP}"
            for label, count in counts.items() if count > HARD_CAP]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    try:
        counts = {"full checkout": count_entries(args.root),
                  "package-oriented tree": count_entries(args.root, package_only=True)}
    except OSError as exc:
        print(f"FAIL: cannot inventory tree: {exc}", file=sys.stderr)
        return 2
    errors = validate_counts(counts)
    for label, count in counts.items():
        print(f"{label}: {count} file entries (hard cap {HARD_CAP})")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: both counts are within the fixed hard cap")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

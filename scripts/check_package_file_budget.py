#!/usr/bin/env python3
"""Check checkout and package-oriented file-entry counts against the ZIP cap."""

from __future__ import annotations

import argparse
import json
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


def validate_package(root: Path) -> list[str]:
    root = root.resolve()
    try:
        errors = validate_counts({"checkout": count_entries(root), "package": count_entries(root, True)})
        claude = json.loads((root / ".claude-plugin/plugin.json").read_text())
        codex_path = root / ".codex-plugin/plugin.json"
        codex = json.loads(codex_path.read_text()) if codex_path.exists() else claude
        if not claude.get("name") or any(codex.get(k) != claude.get(k) for k in ("name", "version")):
            errors.append("plugin identity/version mismatch")
        expected = {p.relative_to(root).as_posix() for base in ("skills", "country-context") for p in (root / base).rglob("SKILL.md")}
        for label, manifest in (("Claude", claude), ("Codex", codex)):
            configured = manifest.get("skills")
            entries = [configured] if isinstance(configured, str) else configured
            if not isinstance(entries, list) or not entries:
                raise ValueError("missing skill paths")
            paths = []
            for entry in entries:
                if not isinstance(entry, str) or not entry.startswith("./") or ".." in Path(entry).parts or "\\" in entry:
                    raise ValueError("invalid relative skill path")
                base = root / entry
                if not base.resolve().is_relative_to(root) or not base.is_dir():
                    raise ValueError("missing or escaping skill path")
                selected = [base / "SKILL.md"] if (base / "SKILL.md").exists() else list(base.rglob("SKILL.md"))
                for path in selected:
                    if not path.resolve().is_relative_to(root) or any(p.is_symlink() for p in (path, *path.parents) if p != root):
                        raise ValueError("symlinked skill path")
                    paths.append(path.relative_to(root).as_posix())
            if len(paths) != len(set(paths)) or set(paths) != expected:
                errors.append(f"{label} skill path set mismatch")
        for filename in (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json"):
            entries = json.loads((root / filename).read_text())["plugins"]
            if len(entries) != 1 or entries[0].get("name") != claude["name"]:
                errors.append("marketplace identity mismatch")
            source = entries[0].get("source")
            if source != "./" and source != {"source": "local", "path": "./"}:
                errors.append("marketplace local source mismatch")
        return errors
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f"incomplete package evidence: {exc}"]


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
    errors = validate_package(args.root)
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

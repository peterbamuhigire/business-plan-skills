#!/usr/bin/env python3
"""Validate and optionally probe the country/market evidence register."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTER = ROOT / "docs/source-registers/country-market-data.json"
REQUIRED = {"id", "jurisdiction", "publisher", "title", "source_type", "url",
            "claim_families", "checked_on", "recheck_due", "status", "owner", "note"}
ACTIVE_COUNTRIES = {"Uganda": ROOT / "country-context/uganda/SKILL.md",
                    "Kenya": ROOT / "country-context/kenya/SKILL.md",
                    "Tanzania": ROOT / "country-context/tanzania/SKILL.md"}


def validate(path: Path, today: date | None = None) -> list[str]:
    today = today or date.today()
    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    entries = data.get("entries", [])
    seen: set[str] = set()
    jurisdictions: set[str] = set()
    for index, entry in enumerate(entries):
        missing = REQUIRED - set(entry)
        if missing:
            errors.append(f"entry {index}: missing {sorted(missing)}")
            continue
        if entry["id"] in seen:
            errors.append(f"duplicate id: {entry['id']}")
        seen.add(entry["id"])
        jurisdictions.add(entry["jurisdiction"])
        try:
            checked = date.fromisoformat(entry["checked_on"])
            due = date.fromisoformat(entry["recheck_due"])
            if due < checked:
                errors.append(f"{entry['id']}: recheck precedes check")
            if due < today:
                errors.append(f"{entry['id']}: evidence refresh overdue since {due}")
        except ValueError:
            errors.append(f"{entry['id']}: invalid ISO date")
        if entry["status"] not in {"verified-current", "verified-with-caveat", "stale", "no-source-found"}:
            errors.append(f"{entry['id']}: invalid status")
        if not entry["url"].startswith("https://"):
            errors.append(f"{entry['id']}: URL must use HTTPS")
        if not entry["claim_families"]:
            errors.append(f"{entry['id']}: empty claim families")
    for jurisdiction, skill in ACTIVE_COUNTRIES.items():
        if jurisdiction not in jurisdictions:
            errors.append(f"missing active jurisdiction: {jurisdiction}")
        if skill.exists() and "docs/source-registers/country-market-data" not in skill.read_text(encoding="utf-8"):
            errors.append(f"{skill.relative_to(ROOT)}: evidence register is not linked")
    return errors


def check_urls(path: Path) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors = []
    for entry in data["entries"]:
        request = urllib.request.Request(entry["url"], method="HEAD",
                                         headers={"User-Agent": "business-plan-skills-evidence-check/1"})
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                if response.status >= 400:
                    errors.append(f"{entry['id']}: HTTP {response.status}")
        except (urllib.error.URLError, TimeoutError) as exc:
            errors.append(f"{entry['id']}: URL not assessed successfully: {exc}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--register", type=Path, default=DEFAULT_REGISTER)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--check-urls", action="store_true")
    args = parser.parse_args(argv)
    errors = validate(args.register)
    if args.check_urls:
        errors.extend(check_urls(args.register))
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    count = len(json.loads(args.register.read_text(encoding="utf-8"))["entries"])
    print(f"PASS: {count} evidence-register entries; active jurisdictions covered")
    return 0


if __name__ == "__main__":
    sys.exit(main())

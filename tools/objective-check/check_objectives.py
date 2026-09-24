#!/usr/bin/env python3
"""Reject vague marketing objectives using the SMART builder's fail conditions.

Two entry points:
  check_structured(obj)  -> list of failure codes for a dict-shaped objective
  check_sentence(text)   -> list of failure codes for a one-sentence objective

The rules mirror skills/marketing-sales/marketing-plan-orchestrator/references/
smart-objectives-builder.md (section 5, "SMART quality test").
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

VAGUE_PHRASES = (
    "brand awareness",
    "grow sales significantly",
    "grow significantly",
    "leading provider",
    "leading company",
    "go viral",
    "strong social media presence",
    "social media presence",
    "reach more customers",
    "be active on social media",
    "increase engagement",
    "maximise reach",
    "maximize reach",
    "more visibility",
    "raise our profile",
    "market leader",
)
GENERIC_SEGMENTS = {"customers", "everyone", "all customers", "the youth", "smes", "people", "the market", "consumers"}
GENERIC_PLACES = {"uganda", "east africa", "africa", "everywhere", "online", "worldwide", "global", "the region", "the country"}
GENERIC_OWNERS = {"team", "the team", "marketing", "everyone", "management", "we"}
LINE_SOURCES = {"model-maths", "benchmark", "own-trend"}
WIDE_SCOPES = {"national", "cross-border"}
EVIDENCE_CLASSES = {"verified-fact", "estimate", "assumption"}
TIME_WORDS = re.compile(
    r"\b(by|before|within|until)\b[^.]*\b(\d{1,2}\s+)?"
    r"(january|february|march|april|may|june|july|august|september|october|november|december|q[1-4]|20\d\d)\b",
    re.IGNORECASE,
)
NUMBER = re.compile(r"\d")


def _blank(value: object) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def _parse_date(value: object) -> date | None:
    try:
        return date.fromisoformat(str(value))
    except ValueError:
        return None


def check_structured(obj: dict) -> list[str]:
    failures: list[str] = []
    text = " ".join(str(v) for v in obj.values() if isinstance(v, str)).lower()
    if any(phrase in text for phrase in VAGUE_PHRASES) and _blank(obj.get("numerator")):
        failures.append("vague-goal-phrase")
    if any(_blank(obj.get(key)) for key in ("metric", "numerator", "denominator", "window")):
        failures.append("metric-undefined")
    segment = str(obj.get("segment", "")).strip().lower()
    if not segment or segment in GENERIC_SEGMENTS:
        failures.append("segment-generic")
    scope = str(obj.get("scope", "")).strip().lower()
    places = obj.get("places") or []
    named = [p for p in places if str(p).strip().lower() not in GENERIC_PLACES]
    if not named or (len(named) < len(places) and scope not in WIDE_SCOPES):
        failures.append("place-missing-or-too-wide")
    baseline = obj.get("baseline") or {}
    if _blank(baseline.get("value")) or _blank(baseline.get("source")) or _parse_date(baseline.get("date")) is None:
        failures.append("baseline-missing")
    target = obj.get("target") or {}
    if _blank(target.get("value")):
        failures.append("target-missing")
    if target.get("line_source") not in LINE_SOURCES:
        failures.append("line-source-missing")
    deadline = _parse_date(obj.get("deadline"))
    if deadline is None:
        failures.append("deadline-missing")
    elif not obj.get("checkpoints"):
        failures.append("checkpoint-missing")
    owner = str(obj.get("owner", "")).strip().lower()
    if not owner or owner in GENERIC_OWNERS:
        failures.append("owner-missing")
    if _blank(obj.get("tracking_method")):
        failures.append("tracking-missing")
    if obj.get("reconciled") is not True:
        failures.append("arithmetic-not-reconciled")
    if not obj.get("applicability_notes"):
        failures.append("applicability-missing")
    if obj.get("evidence_class") not in EVIDENCE_CLASSES:
        failures.append("evidence-class-missing")
    return failures


def check_sentence(text: str) -> list[str]:
    failures: list[str] = []
    lowered = text.lower()
    if any(phrase in lowered for phrase in VAGUE_PHRASES):
        failures.append("vague-goal-phrase")
    if not NUMBER.search(text):
        failures.append("no-number")
    if not TIME_WORDS.search(text):
        failures.append("no-deadline")
    if not re.search(r"\bfrom\b[^.]*\d", lowered) and "baseline" not in lowered:
        failures.append("no-baseline")
    if not re.search(r"\b(in|among|across|at|with|for)\b\s+([a-z]+\s+)?[A-Z][a-z]+", text):
        failures.append("no-named-place")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="JSON file: a list of objective objects or of {'text': ...}")
    args = parser.parse_args()
    data = json.loads(args.file.read_text(encoding="utf-8"))
    bad = 0
    for index, item in enumerate(data):
        failures = check_sentence(item["text"]) if "text" in item else check_structured(item)
        if failures:
            bad += 1
            print(f"FAIL item {index}: {', '.join(failures)}")
    print(f"objective-check: {len(data)} objectives; {bad} failing")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

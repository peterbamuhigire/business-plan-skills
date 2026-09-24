#!/usr/bin/env python3
"""Reject raw books and likely reconstructive full-text conversions."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


LARGE_BOOK_TEXT_BYTES = 80_000
RAW_BOOK_EXTENSIONS = {".epub", ".mobi", ".azw", ".azw3"}
SOURCE_TEXT_EXTENSIONS = {".md", ".txt", ".rst", ".html", ".htm"}
BOOK_SOURCE_PATH_RE = re.compile(
    r"(?:^|/)(?:book-extractions?|book-dumps?|raw-books?|source-books?)(?:/|$)",
    re.IGNORECASE,
)
RAW_EXTRACTION_PATH_RE = re.compile(
    r"(?:^|/)(?:_extractions?|raw[-_]?extractions?|raw[-_]?books?|book[-_]?dumps?|source[-_]?books?)(?:/|$)",
    re.IGNORECASE,
)
FULL_TEXT_MARKERS = {
    "isbn": re.compile(r"\bISBN(?:-1[03])?\s*:?\s*[\dXx][\dXx\-\s]{8,}"),
    "copyright": re.compile(r"\bcopyright\s+(?:\u00a9|\(c\)|&copy;|[12]\d{3})", re.IGNORECASE),
    "rights-reserved": re.compile(r"\ball rights reserved\b", re.IGNORECASE),
    "reproduction-notice": re.compile(
        r"\bno part of this (?:book|publication|work) may be reproduced\b",
        re.IGNORECASE,
    ),
    "ebook-conversion": re.compile(
        r"(?:\[\]\{#[^}\n]*\.xhtml|calibre\d*|index_split_\d+\.html)",
        re.IGNORECASE,
    ),
}
EXCLUDED_PARTS = {".git", ".venv", "__pycache__", "node_modules"}

# Content-aware check (report-only). A reference file that carries a single-source
# header plus book-like structure (chapter or part sections, or a "Key Quotes"
# section) is probably a digest of one book, which must not be stored here.
# TO MAKE THIS BLOCKING: set CONTENT_CHECK_BLOCKING = True (or run with --strict-content);
# main() then exits 1 when any content warning is found.
CONTENT_CHECK_BLOCKING = False
# The UNDP compendium business profiles live under the sector guides and are exempt.
CONTENT_CHECK_EXCLUDED_PREFIXES = ("skills/industry-guides/",)
SINGLE_SOURCE_HEADER = re.compile(r"(sources?|author|publisher|isbn|books?)\s*[:*|]", re.IGNORECASE)
CHAPTER_HEADING = re.compile(r"^#{1,4}\s*(chapter|part)\s+[0-9ivx]+", re.IGNORECASE | re.MULTILINE)
KEY_QUOTES_HEADING = re.compile(r"^#{1,4}\s*(key quotes?|notable quotes?|memorable quotes?)", re.IGNORECASE | re.MULTILINE)


@dataclass(frozen=True)
class Finding:
    code: str
    path: Path
    message: str

    def format(self) -> str:
        return f"[ERROR] {self.code}: {self.path} {self.message}"


def scan(root: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue

        suffix = path.suffix.lower()
        if suffix in RAW_BOOK_EXTENSIONS:
            findings.append(
                Finding(
                    "raw-book-source",
                    relative,
                    "raw ebook source files are temporary inputs and must not be stored in the repository",
                )
            )
            continue

        in_book_source_path = BOOK_SOURCE_PATH_RE.search(relative.as_posix()) is not None
        in_raw_extraction_path = RAW_EXTRACTION_PATH_RE.search(relative.as_posix()) is not None
        if in_raw_extraction_path:
            findings.append(
                Finding(
                    "raw-extraction-path",
                    relative,
                    "raw extraction paths are temporary inputs; retain a concise, attributed synthesis instead",
                )
            )
            continue

        if in_book_source_path:
            findings.append(
                Finding(
                    "book-extraction-path",
                    relative,
                    "book extractions must never be stored in the repository; fold task-oriented "
                    "guidance into the owning skill's references/",
                )
            )
            continue
        if suffix not in SOURCE_TEXT_EXTENSIONS:
            continue

        size = path.stat().st_size
        if size < 30_000:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        markers = sorted(name for name, pattern in FULL_TEXT_MARKERS.items() if pattern.search(content))
        if len(markers) >= 3:
            findings.append(
                Finding(
                    "source-fulltext-markers",
                    relative,
                    "likely reconstructive book text; matched markers: " + ", ".join(markers),
                )
            )
    return findings


def scan_content(root: Path) -> list[Finding]:
    """Report-only heuristic for book digests kept as skill references."""
    root = root.resolve()
    warnings: list[Finding] = []
    for path in (root / "skills").rglob("*.md") if (root / "skills").is_dir() else []:
        relative = path.relative_to(root).as_posix()
        if "/references/" not in relative or relative.startswith(CONTENT_CHECK_EXCLUDED_PREFIXES):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        header = text[:1500]
        chapters = len(CHAPTER_HEADING.findall(text))
        has_source = SINGLE_SOURCE_HEADER.search(header) is not None
        if has_source and chapters >= 3:
            warnings.append(Finding("single-source-chapter-structure", Path(relative),
                                    f"single-source header with {chapters} chapter or part headings; "
                                    "reorganise by task, not by the book's sequence"))
        elif KEY_QUOTES_HEADING.search(text):
            warnings.append(Finding("key-quotes-section", Path(relative),
                                    "contains a 'Key Quotes' section; remove quotations beyond brief attribution"))
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--strict-content", action="store_true",
                        help="make content-aware warnings blocking (same as CONTENT_CHECK_BLOCKING = True)")
    args = parser.parse_args()
    findings = scan(args.root)
    warnings = scan_content(args.root)
    print(f"source-ingestion-guardrail: {args.root.resolve()}")
    print(f"findings: {len(findings)}")
    for finding in findings:
        print(finding.format())
    print(f"content-warnings: {len(warnings)} (report-only unless --strict-content or CONTENT_CHECK_BLOCKING)")
    for warning in warnings:
        print(f"[WARNING] {warning.code}: {warning.path} {warning.message}")
    blocking = args.strict_content or CONTENT_CHECK_BLOCKING
    return 1 if findings or (blocking and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""OpenBook structural checker for Report markdown.

Usage:
  python scripts/check_report.py path/to/REPORT.md

Exit 0 = pass. Exit 1 = fail.
Never fails for being "too long."
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_H2 = [
    "Cover",
    "The sixty-second version",
    "Narrative",
    "What's next",
    "What we learned",
    "Appendix",
]

DECISION_HEADING_RE = re.compile(
    r"^###\s+(?:\d+\.\s*)?\[\?\]|^###\s+\d+\.",
    re.MULTILINE,
)


def extract_h2(md: str) -> list[str]:
    return [
        m.group(1).strip()
        for m in re.finditer(r"^##\s+(.+?)\s*$", md, re.MULTILINE)
    ]


def section_body(md: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$"
    m = re.search(pattern, md, re.MULTILINE)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"^##\s+", md[start:], re.MULTILINE)
    end = start + nxt.start() if nxt else len(md)
    return md[start:end].strip()


def count_decision_blocks(text: str) -> int:
    """Count ### decision headings (numbered and/or [?])."""
    return len(DECISION_HEADING_RE.findall(text))


BARE_ID_RE = re.compile(
    r"(?<![\w/])#\d{1,6}\b"  # bare issue/PR style: #123
    r"|\bPR ?#?\d{1,6}\b"  # PR 123 / PR #123
    r"|\b[A-Z]{2,6}-\d{2,6}\b"  # tracker style: ABC-123 (2+ digits)
)

# technical tokens that look like tracker IDs but are not references
ID_ALLOWLIST_PREFIXES = ("UTF-", "ISO-", "SHA-", "MD-", "RFC-", "EC-", "AES-")


def paragraphs_of(section: str) -> list[str]:
    blocks: list[str] = []
    for raw in re.split(r"\n\s*\n", section):
        block = raw.strip()
        if not block:
            continue
        first = block.splitlines()[0].lstrip()
        if first.startswith(("#", "-", "*", ">", "|", "```")) or re.match(
            r"^\d+\.\s", first
        ):
            continue
        blocks.append(block)
    return blocks


def check(md: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    h2 = extract_h2(md)

    for req in REQUIRED_H2:
        if req not in h2:
            errors.append(f"Missing required H2: ## {req}")

    positions = []
    for req in REQUIRED_H2:
        if req in h2:
            positions.append(h2.index(req))
    if positions != sorted(positions):
        errors.append(
            "Required H2 sections are out of order. Expected: "
            + " -> ".join(REQUIRED_H2)
        )

    sixty = section_body(md, "The sixty-second version")
    if "The sixty-second version" in h2 and len(sixty) < 40:
        errors.append("## The sixty-second version is empty or too thin")

    nxt = section_body(md, "What's next")
    narrative = section_body(md, "Narrative")
    embedded = count_decision_blocks(narrative)
    cross_cut = count_decision_blocks(nxt)

    if "What's next" in h2:
        n_alt = len(
            re.findall(r"^\d+\.\s+\[\?\]|^\d+\.\s+\*\*", nxt, re.MULTILINE)
        )
        if embedded >= 1:
            # Hybrid: What's next must index chapter decisions (body required).
            # Cross-cut ### blocks are allowed in addition to the index.
            if len(nxt) < 20:
                errors.append(
                    "## What's next must index the embedded decisions "
                    "(one line each) and may add cross-cutting asks"
                )
        elif cross_cut < 1 and n_alt < 1 and len(nxt) < 20:
            errors.append("## What's next has no decision blocks")
        elif cross_cut < 1 and n_alt < 1:
            errors.append(
                "## What's next needs at least one ### N. decision heading "
                "(or embed chapter decisions and write an index here)"
            )

        total = embedded + cross_cut
        if total > 5:
            warnings.append(
                f"{total} decisions (chapter embeds plus cross-cuts); prefer <=5"
            )

    appendix = section_body(md, "Appendix")
    if "Appendix" in h2 and len(appendix) < 1:
        errors.append("## Appendix heading exists but body is empty")

    if "Narrative" in h2 and len(narrative) < 40:
        errors.append("## Narrative is empty or too thin")

    ids = sorted(
        m
        for m in set(BARE_ID_RE.findall(md))
        if not m.startswith(ID_ALLOWLIST_PREFIXES)
    )
    if ids:
        shown = ", ".join(ids[:8]) + ("..." if len(ids) > 8 else "")
        warnings.append(
            f"bare IDs found ({shown}): say what each thing IS in words; "
            "IDs in parentheses at most"
        )

    if narrative:
        walls = [p for p in paragraphs_of(narrative) if len(p.split()) > 130]
        if walls:
            warnings.append(
                f"{len(walls)} paragraph(s) over 130 words in Narrative: "
                "consider lists, bold leads, or a split (one idea per paragraph)"
            )

    # Long report + trailing-only: nudge toward Hybrid
    if narrative and len(narrative.split()) > 2500:
        if embedded < 1 and cross_cut >= 3:
            warnings.append(
                "long narrative with all decisions trailing: prefer Hybrid — "
                "embed chapter-owned asks at chapter end, make What's next an "
                "index plus any cross-cutting asks"
            )

    return errors, warnings


def main() -> None:
    ap = argparse.ArgumentParser(description="Check OpenBook Report structure")
    ap.add_argument("markdown", type=Path)
    args = ap.parse_args()
    path = args.markdown
    if not path.is_file():
        print(f"FAIL: not found: {path}", file=sys.stderr)
        sys.exit(1)

    md = path.read_text(encoding="utf-8")
    errors, warnings = check(md)
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        for e in errors:
            print(f"FAIL: {e}", file=sys.stderr)
        print(f"OpenBook check FAILED: {path}", file=sys.stderr)
        sys.exit(1)
    print(f"OpenBook check PASSED: {path}")
    sys.exit(0)


if __name__ == "__main__":
    main()

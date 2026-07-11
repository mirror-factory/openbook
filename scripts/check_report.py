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


def count_decisions(whats_next: str) -> int:
    # ### 1. or ### 1. [?] or lines starting with ### and a number
    return len(re.findall(r"^###\s+\d+\.", whats_next, re.MULTILINE))


def check(md: str) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []
    h2 = extract_h2(md)

    for req in REQUIRED_H2:
        if req not in h2:
            errors.append(f"Missing required H2: ## {req}")

    # Order among those that exist
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
    if "What's next" in h2:
        n = count_decisions(nxt)
        if n < 1:
            # also accept bold numbered lines without ###
            n_alt = len(re.findall(r"^\d+\.\s+\[\?\]|^\d+\.\s+\*\*", nxt, re.MULTILINE))
            if n_alt < 1 and len(nxt) < 20:
                errors.append("## What's next has no decision blocks")
            elif n < 1 and n_alt < 1:
                errors.append(
                    "## What's next needs at least one ### N. decision heading"
                )
        if n > 5:
            warnings.append(f"What's next has {n} decisions; prefer ≤5")

    appendix = section_body(md, "Appendix")
    if "Appendix" in h2 and len(appendix) < 1:
        errors.append("## Appendix heading exists but body is empty")

    narrative = section_body(md, "Narrative")
    if "Narrative" in h2 and len(narrative) < 40:
        errors.append("## Narrative is empty or too thin")

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

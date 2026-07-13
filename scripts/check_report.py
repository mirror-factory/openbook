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

TWO_MINUTES = "Two Minutes"
LEDE_LEGACY = (
    "Sixty Seconds",
    "The sixty-second version",
)

REQUIRED_H2_BRIEF = [
    "Cover",
    TWO_MINUTES,
    "What's next",
    "What we learned",
    "Appendix",
]

REQUIRED_H2_LONG = [
    "Cover",
    TWO_MINUTES,
    "Narrative",
    "What's next",
    "What we learned",
    "Appendix",
]

# Preferred: ### Decision N · handle
# Legacy: ### N. [?] … or ### N. …
DECISION_HEADING_RE = re.compile(
    r"^###\s+Decision\s+\d+\s*·"
    r"|^###\s+(?:\d+\.\s*)?\[\?\]"
    r"|^###\s+\d+\.",
    re.MULTILINE,
)

LEGACY_DECISION_RE = re.compile(
    r"^###\s+(?:\d+\.\s*)?\[\?\]|^###\s+\d+\.(?!\s*Decision)",
    re.MULTILINE,
)

BARE_ID_RE = re.compile(
    r"(?<![\w/])#\d{1,6}\b"
    r"|\bPR ?#?\d{1,6}\b"
    r"|\b[A-Z]{2,6}-\d{2,6}\b"
    r"|(?<![\w/-])T\d{3}\b"  # task IDs (T023): explain on the same page
)

# Inline enumeration run-ons: "(1) ... (2) ..." packed into prose reads as a
# wall; numbered sequences present vertically as ordered lists (Kyle's ink).
INLINE_ENUM_RE = re.compile(r"\(\d{1,2}\)\s+\S+[^()]{0,400}?\(\d{1,2}\)\s+\S+")

ID_ALLOWLIST_PREFIXES = ("UTF-", "ISO-", "SHA-", "MD-", "RFC-", "EC-", "AES-")

BOLD_LEAD_RE = re.compile(
    r"(?:^|\n\n)\*\*[^*\n]{2,80}\*\*",
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
    return len(DECISION_HEADING_RE.findall(text))


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


def detect_length(md: str) -> str | None:
    m = re.search(
        r"^\*\*Length:\*\*\s*(Brief|Standard|Essay)\s*$",
        md,
        re.MULTILINE | re.IGNORECASE,
    )
    if not m:
        return None
    return m.group(1).title()


def required_h2_for(length: str | None) -> list[str]:
    if length == "Brief":
        return list(REQUIRED_H2_BRIEF)
    return list(REQUIRED_H2_LONG)


def normalize_h2(h2: list[str]) -> list[str]:
    """Map legacy lede headings onto the canonical name for checks."""
    return [TWO_MINUTES if h in LEDE_LEGACY else h for h in h2]


def lede_heading(h2: list[str]) -> str | None:
    if TWO_MINUTES in h2:
        return TWO_MINUTES
    for legacy in LEDE_LEGACY:
        if legacy in h2:
            return legacy
    return None


def check(md: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    h2 = extract_h2(md)
    h2_norm = normalize_h2(h2)
    length = detect_length(md)
    required = required_h2_for(length)

    if length == "Brief" and "Narrative" in h2:
        errors.append(
            "Brief has a Narrative section: either fold it into "
            f"## {TWO_MINUTES} or declare Standard"
        )

    for legacy in LEDE_LEGACY:
        if legacy in h2:
            warnings.append(
                f"legacy H2 ## {legacy}: prefer ## {TWO_MINUTES}"
            )

    for req in required:
        if req not in h2_norm:
            errors.append(f"Missing required H2: ## {req}")

    positions = []
    for req in required:
        if req in h2_norm:
            positions.append(h2_norm.index(req))
    if positions != sorted(positions):
        errors.append(
            "Required H2 sections are out of order. Expected: "
            + " -> ".join(required)
        )

    lede_h = lede_heading(h2)
    sixty = section_body(md, lede_h) if lede_h else ""
    if lede_h and len(sixty) < 40:
        errors.append(f"## {lede_h} is empty or too thin")

    nxt = section_body(md, "What's next")
    narrative = section_body(md, "Narrative")
    embedded = count_decision_blocks(narrative)
    cross_cut = count_decision_blocks(nxt)
    narrative_words = len(narrative.split()) if narrative else 0
    chapter_heads = len(
        re.findall(r"^###\s+Chapter\b", narrative, re.MULTILINE | re.IGNORECASE)
    )

    if LEGACY_DECISION_RE.search(md):
        warnings.append(
            "legacy decision heading ### N. [?] (or ### N.): prefer "
            "### Decision N · short handle"
        )

    if "What's next" in h2:
        n_alt = len(
            re.findall(r"^\d+\.\s+\[\?\]|^\d+\.\s+\*\*", nxt, re.MULTILINE)
        )
        if embedded >= 1:
            if len(nxt) < 20:
                errors.append(
                    "## What's next must index the embedded decisions "
                    "(one line each) and may add cross-cutting asks"
                )
        elif cross_cut < 1 and n_alt < 1 and len(nxt) < 20:
            errors.append("## What's next has no decision blocks")
        elif cross_cut < 1 and n_alt < 1:
            errors.append(
                "## What's next needs at least one ### Decision N · heading "
                "(or embed chapter decisions and write an index here)"
            )

        total = embedded + cross_cut
        if length == "Brief" and total > 3:
            warnings.append(
                f"{total} decisions on a Brief; prefer <=3 for a one-pager"
            )
        elif total > 5:
            warnings.append(
                f"{total} decisions (chapter embeds plus cross-cuts); prefer <=5"
            )

    appendix = section_body(md, "Appendix")
    if "Appendix" in h2 and len(appendix) < 1:
        errors.append("## Appendix heading exists but body is empty")

    if sixty and appendix is not None and "Appendix" in h2:
        claim_nums = set(re.findall(r"\b\d+\b", sixty))
        # Skip tiny numbers that are usually prose (a, one-word counts under
        # scrutiny still matter when they appear; keep all digits but ignore
        # years already in Cover).
        appendix_nums = set(re.findall(r"\b\d+\b", appendix))
        missing = sorted(
            n
            for n in claim_nums
            if n not in appendix_nums and not re.fullmatch(r"20\d{2}", n)
        )
        if missing and len(appendix) >= 1:
            shown = ", ".join(missing[:6]) + ("..." if len(missing) > 6 else "")
            warnings.append(
                f"lede numeric claim(s) not found in Appendix ({shown}): "
                "extract a matching receipt rather than paraphrasing"
            )
        elif claim_nums and len(appendix) < 1:
            warnings.append(
                "two-minute lede has numeric claims but Appendix is empty: "
                "add extracted receipts (see docs/receipts.md)"
            )

    if length != "Brief" and "Narrative" in h2 and len(narrative) < 40:
        errors.append("## Narrative is empty or too thin")

    cover = section_body(md, "Cover")
    if re.search(r"^\*\*Stats:\*\*", cover, re.MULTILINE):
        warnings.append(
            "**Stats:** under Cover: move numbers to "
            "**By the numbers:** in Appendix"
        )

    if length == "Brief" and sixty:
        if re.search(r"^[-*]\s+", sixty, re.MULTILINE):
            warnings.append(
                "Brief two-minute lede contains bullet lines: use continuous prose"
            )
        bold_leads = BOLD_LEAD_RE.findall(sixty)
        if len(bold_leads) > 1:
            warnings.append(
                f"{len(bold_leads)} bold-lead openers in Brief two-minute lede: "
                "prefer zero (writing carries emphasis)"
            )
        elif len(bold_leads) == 1:
            warnings.append(
                "bold lead in Brief two-minute lede: prefer continuous prose "
                "without bold leads"
            )

    ids = sorted(
        m
        for m in set(BARE_ID_RE.findall(md))
        if not m.startswith(ID_ALLOWLIST_PREFIXES)
    )
    if ids:
        shown = ", ".join(ids[:8]) + ("..." if len(ids) > 8 else "")
        warnings.append(
            f"bare IDs found ({shown}): never reference an ID without "
            "explaining it on the same page; say what each thing IS in "
            "words, IDs in parentheses at most"
        )

    enum_runs = INLINE_ENUM_RE.findall(md)
    if enum_runs:
        warnings.append(
            f"{len(enum_runs)} inline enumeration run-on(s) like (1) ... (2) ...: "
            "numbered sequences present vertically as ordered lists (1. 2. 3.)"
        )

    nbsp_count = md.count("&nbsp;") + md.count(" ")
    if nbsp_count:
        warnings.append(
            f"{nbsp_count} non-breaking-space entities: pen room belongs to "
            "decision blocks; the renderer folds entity-only paragraphs into "
            "pen room, but prefer not to author them"
        )

    if narrative:
        walls = [p for p in paragraphs_of(narrative) if len(p.split()) > 130]
        if walls:
            warnings.append(
                f"{len(walls)} paragraph(s) over 130 words in Narrative: "
                "consider lists, bold leads, or a split (one idea per paragraph)"
            )
        only_bullets = bool(narrative.strip()) and not paragraphs_of(narrative)
        has_bullets = bool(re.search(r"^[-*]\s+", narrative, re.MULTILINE))
        if length == "Standard" and only_bullets and has_bullets:
            warnings.append(
                "Standard Narrative is only bullets: write prose-first "
                "(bullets for genuinely parallel facts)"
            )

    if length == "Brief":
        pass  # Narrative presence already errors above
    elif length == "Standard":
        if narrative_words > 1800:
            warnings.append(
                "Length is Standard but Narrative is very long: "
                "consider Essay, or cut toward 2-4 pages"
            )
    elif length == "Essay":
        if narrative_words > 2500 and embedded < 1 and cross_cut >= 3:
            warnings.append(
                "Essay with all decisions trailing: prefer Hybrid — "
                "embed chapter-owned asks at chapter end, make What's next an "
                "index plus any cross-cutting asks"
            )
    elif narrative_words > 2500 and embedded < 1 and cross_cut >= 3:
        warnings.append(
            "long narrative with all decisions trailing: prefer Hybrid — "
            "embed chapter-owned asks at chapter end, make What's next an "
            "index plus any cross-cutting asks"
        )

    # Librarian voice (requirements §10.1): structural, fails the build
    em_dashes = md.count("\u2014")
    if em_dashes:
        errors.append(
            f"librarian: {em_dashes} em dash(es) (U+2014); "
            "use commas, periods, or parentheses"
        )
    # Figures (![caption](path)) and HTML comments are markup, not voice;
    # only bangs that would be READ count against the register.
    prose = re.sub(r"<!--.*?-->", "", md, flags=re.DOTALL)
    prose = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", prose)
    bangs = prose.count("!")
    if bangs:
        errors.append(
            f"librarian: {bangs} exclamation point(s); "
            "name facts plainly without urgency theater"
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

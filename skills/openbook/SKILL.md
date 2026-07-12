---
name: openbook
description: >-
  Write an OpenBook end-of-run handoff report (Brief, Standard, or Essay)
  from the current session. Use when the user invokes /openbook, or asks to
  write the handoff, wrap up this session, or report on what you did.
user-invocable: true
---

# OpenBook handoff

Turn this run into a human-readable report. The kit is Markdown in a folder: no server, no SDK.

## Triggers

- Explicit: `/openbook`, `/openbook brief`, `/openbook standard`, `/openbook essay`
- End-of-run phrases: "write the handoff", "wrap up this session", "report on what you did"

## Length profile

Infer from run size unless the user passed an arg:

| Arg / inference | When |
|-----------------|------|
| **Brief** (default) | Small or medium runs; most coding-agent handoffs |
| **Standard** | Multi-hour work with a real story that will not fit a one-page lede |
| **Essay** | High-substance overnight or morning-report nights |

Set `**Length:** Brief` (or Standard / Essay) in Cover.

## Steps

1. Locate the OpenBook repo root (this skill's parent folders, or a clone the user pointed at).
2. Read `formats/report.md` and `styles/librarian.md` from that root. Follow them exactly.
3. Write `REPORT.md` at the workspace root (or the path the user named).
4. If `scripts/check_report.py` is reachable, run it on the report. Fix any warnings or failures **once**, then stop. Do not invent content to silence the checker.
5. Optionally render with `scripts/render_report.py` when the user wants HTML/PDF. Never browser-print a `file://` tab.

## Truthfulness

- Dead ends are content. Name failures plainly.
- Never invent timestamps, receipts, PR numbers, or test counts.
- Never make the report more optimistic than the transcript.
- Appendix receipts are extracted, never paraphrased into softer wording.
- Librarian voice: no exclamation points, no em dashes.

## Brief shape (public default)

- Continuous prose in `## Two Minutes` (3–6 paragraphs). First sentence is the bottom line. No bold leads, no bullets, no `## Narrative`.
- Decisions as `### Decision N · short handle`, then the question as the first paragraph. Prefer ≤3 asks.
- Put numbers in Appendix as `**By the numbers:** …`, not on Cover.

## Standard / Essay

- Two-minute is an abstract (≤3 paragraphs; bold leads OK).
- `## Narrative` is required and prose-first.
- On Essay: chapter-owned asks at chapter end; `What's next` is an index plus any cross-cutting asks.

Every decision block must be self-contained and plain-language. Never a bare ticket or PR number as the only name for a thing.

# Use OpenBook (paste this)

At the end of this long-horizon run, write `REPORT.md` following:

- `formats/report.md`
- `styles/librarian.md`

**Default length: Brief** (~one page). Set `**Length:** Brief` in Cover. Use **Standard** (~2–4 pages) or **Essay** (long Hybrid chapters) only when the work earns that depth — see length profiles in `formats/report.md`.

**Brief rules (the public default):**

- Continuous prose in `## The sixty-second version` (3–6 paragraphs). First sentence is the bottom line. No bold leads, no bullets, no `## Narrative`.
- Decisions as `### Decision N · short handle`, then the question as the first paragraph.
- Put numbers in Appendix as `**By the numbers:** …`, not on Cover.

**Standard / Essay:** sixty-second is an abstract (≤3 paragraphs; bold leads OK). Narrative is required and prose-first. On Essay, put chapter-owned asks at chapter end; make `What's next` an index plus any cross-cutting asks.

Every decision block must be self-contained and plain-language — never a bare ticket or PR number as the only name for a thing.

Then:

```bash
python scripts/check_report.py REPORT.md
python scripts/render_report.py REPORT.md -o REPORT.pdf
```

Do not hand off until the check passes. For PDF, use `render_report.py` only — never browser Print on a `file://` tab.

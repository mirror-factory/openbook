# Use OpenBook (paste this)

At the end of this long-horizon run, write `REPORT.md` following:

- `formats/report.md`
- `styles/librarian.md`

**Hybrid (when the narrative is long):** put each chapter-owned decision at the end of the chapter that explains it, with pen room. Make `What's next` an index of those asks plus any cross-cutting questions. Every decision block must be self-contained and plain-language — never a bare ticket or PR number as the only name for a thing.

Then:

```bash
python scripts/check_report.py REPORT.md
python scripts/render_report.py REPORT.md -o REPORT.pdf
```

Do not hand off until the check passes. For PDF, use `render_report.py` only — never browser Print on a `file://` tab.

Length is earned by substance. Keep the sixty-second layer even when the narrative is long. Prefer finishing a trustworthy handoff over a thin status dump.

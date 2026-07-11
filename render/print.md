# OpenBook print / PDF

Frameless letter PDF for paper and reMarkable. **Do not** use browser Print on a `file://` tab (Chrome injects date and URL footers).

## Pipeline

```text
REPORT.md → scripts/render_report.py → REPORT.pdf
```

```bash
# once per machine
pip install -r requirements.txt
playwright install chromium

# render
python scripts/render_report.py path/to/REPORT.md -o path/to/REPORT.pdf
```

Optional HTML sidecar:

```bash
python scripts/render_report.py path/to/REPORT.md -o out.pdf --html-only out.html
```

## Design locks

| Item | Value |
|------|--------|
| Typeface | Georgia (system), Times New Roman fallback |
| Body | 11pt, line-height ~1.45 |
| Page | US Letter |
| Margins | ≥2.6cm (set in CSS `@page`) |
| Decisions | `.penroom` ~88pt under each ask |
| Headers/footers | Page number only — **no** URL, **no** print date |
| Figures | Grayscale-safe; captions required |

Layers UI fonts (Archivo, DM Mono) are for the product shell, not morning essays.

## Visual QA checklist

- [ ] No `file://` or `http` string in page margins
- [ ] No browser timestamp in header/footer
- [ ] Body readable at e-ink size; not thin gray
- [ ] Pen rooms visible under each What's next question
- [ ] Chapter H2s do not orphan at page bottoms when avoidable
- [ ] For Mirror Factory mornings with substance: PDF is a real essay (often 15+ pages), not a 2–4 page stub

## reMarkable delivery (Mirror Factory)

1. Render PDF with `render_report.py`
2. Upload to `/Reports/YYYY-MM` (create month folder if needed)
3. Confirm the upload tool succeeded
4. If delivery fails: save PDF locally and put a loud line at the top of `NIGHT-REPORT.md`: `REPORT NOT DELIVERED` plus the path

Filename suggestion: `mf-morning-report-YYYY-MM-DD.pdf`

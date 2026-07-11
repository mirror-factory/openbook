# Claude Code

Paste the block below into a Claude Code session (or add [USE.md](../USE.md) to `CLAUDE.md`).

For Mirror Factory morning reports (e-ink, long essay preference, reMarkable delivery), use the **Morning profile** section at the bottom.

---

## PASTE START

Read and follow OpenBook for the end-of-run handoff.

**Read first** (relative to the OpenBook repo root):

1. `formats/report.md`
2. `styles/librarian.md`
3. `render/print.md`

**At assembly:**

1. Write one OpenBook report Markdown using the exact H2s from `formats/report.md`.
2. **Hybrid (long reports):** chapter-owned `[?]` asks at chapter end; `What's next` = index + any cross-cutting asks. Prefer ≤5 total. Every block self-contained; plain words first (no bare IDs).
3. Voice: librarian (`styles/librarian.md`). No exclamation points, no em dashes.
4. Check, then render PDF with OpenBook tools only (never browser `file://` print):

```bash
python scripts/check_report.py REPORT.md
python scripts/render_report.py REPORT.md -o REPORT.pdf
```

First-time PDF setup: `pip install -r requirements.txt` then `playwright install chromium`.

Acknowledge in one short reply that you have read the OpenBook paths, will use Hybrid for long reports, and will check + render via OpenBook scripts before handoff.

## PASTE END

---

## Morning profile (Mirror Factory)

When the night has substance, prefer a chaptered Bezos-style essay that renders to **15+ pages**. Do not ship a 2–4 page stub. No padding.

**Order:** Cover → Sixty-second → Narrative (chapters with pens where context lives) → What's next (index + cross-cuts) → What we learned → Appendix.

**PDF:** OpenBook `render_report.py` only. **Delivery:** upload to reMarkable `/Reports/YYYY-MM`; on failure, loud `REPORT NOT DELIVERED` plus the local path.

See also: `formats/report.md` length profiles and `render/print.md`.

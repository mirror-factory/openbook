# Claude Code

**Preferred:** load [`skills/openbook/SKILL.md`](../skills/openbook/SKILL.md) and invoke `/openbook` (or `/openbook brief|standard|essay`) at the end of a long run. Phrases such as "write the handoff" also trigger the skill.

**Fallback:** paste the block below into a Claude Code session (or add the short pointer in [USE.md](../USE.md) to `CLAUDE.md`).

For Mirror Factory morning reports (e-ink, long essay preference, reMarkable delivery), use the **Morning profile** section at the bottom.

---

## PASTE START

Read and follow OpenBook for the end-of-run handoff.

**Read first** (relative to the OpenBook repo root):

1. `skills/openbook/SKILL.md` (if present; follow it)
2. `formats/report.md`
3. `styles/librarian.md`
4. `render/print.md`

**At assembly:**

1. Write one OpenBook report Markdown using the exact H2s from `formats/report.md`.
2. **Default to Brief** (~one page). Set `**Length:** Brief` in Cover unless the run clearly earns Standard or Essay.
3. On Essay: chapter-owned `[?]` asks at chapter end; `What's next` = index + any cross-cutting asks. Prefer ≤5 total. Every block self-contained; plain words first (no bare IDs).
4. Voice: librarian (`styles/librarian.md`). No exclamation points, no em dashes.
5. Check, then render PDF with OpenBook tools only (never browser `file://` print):

```bash
python scripts/check_report.py REPORT.md
python scripts/render_report.py REPORT.md -o REPORT.pdf
```

First-time PDF setup: `pip install -r requirements.txt` then `playwright install chromium`.

Acknowledge in one short reply that you have read the OpenBook paths, will default to Brief unless substance warrants more, and will check + render via OpenBook scripts before handoff.

## PASTE END

---

## Morning profile (Mirror Factory)

When the night has substance, prefer **Essay**: a chaptered narrative that renders to **15+ pages** when earned, with Hybrid decisions. Do not ship a 2–4 page stub of a rich night. No padding.

**Order:** Cover → Sixty-second → Narrative (chapters with pens where context lives) → What's next (index + cross-cuts) → What we learned → Appendix.

**PDF:** OpenBook `render_report.py` only. **Delivery:** upload to reMarkable `/Reports/YYYY-MM`; on failure, loud `REPORT NOT DELIVERED` plus the local path.

See also: `formats/report.md` length profiles, `formats/assembly.md` for multi-agent mornings, and `render/print.md`.

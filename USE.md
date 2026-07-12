# Use OpenBook

**Preferred:** install the [`skills/openbook`](./skills/openbook/) skill and invoke `/openbook` (or `/openbook brief|standard|essay`) at the end of a long run. End-of-run phrases such as "write the handoff" also trigger it.

**Fallback** for agents without skill support: paste the block below into `CLAUDE.md`, a Cursor rule, or the session prompt.

---

At the end of this long-horizon run, write `REPORT.md` following `formats/report.md` and `styles/librarian.md`. Default length is Brief. Then run `python scripts/check_report.py REPORT.md` if reachable. Do not invent receipts. For PDF, use `scripts/render_report.py` only, never browser Print on a `file://` tab.

# OpenBook

**Don't trust the agent. Read the OpenBook.**

Writing contracts that make long-horizon agent work readable to humans who don't live in the terminal.

Agents are getting good at *doing* work. They are still bad at leaving a trail a human can trust. OpenBook is a small, stealable kit: opinionated Markdown formats, one voice card, a structural checker, and a frameless letter PDF renderer for paper and e-ink.

It is not an agent framework. It is the document shape between the run and the human.

---

## 60-second install

```bash
git clone https://github.com/mirror-factory/openbook.git
cd openbook
```

1. Point your coding agent at this folder (or paste [USE.md](./USE.md) into `CLAUDE.md`, a Cursor rule, or the session prompt).
2. At the end of a long run, the agent writes `REPORT.md` using [formats/report.md](./formats/report.md).
3. Check structure, then optionally render PDF:

```bash
pip install -r requirements.txt
playwright install chromium

python scripts/check_report.py path/to/REPORT.md
python scripts/render_report.py path/to/REPORT.md -o path/to/REPORT.pdf
```

Never browser-print a `file://` tab. Chrome injects date and URL footers. Use `render_report.py` only.

---

## What you get

| Piece | Job |
|-------|-----|
| [formats/report.md](./formats/report.md) | The Report contract: sixty-second lead, chaptered narrative, decisions where their context lives, receipts |
| [styles/librarian.md](./styles/librarian.md) | Voice card: economical, honest, no hype |
| [scripts/check_report.py](./scripts/check_report.py) | Structural gate (missing sections fail; long essays never fail) |
| [scripts/render_report.py](./scripts/render_report.py) | Markdown → Georgia letter PDF via Playwright |
| [examples/](./examples/) | Before/after of the same night + a shorter coding-agent sample |

Long chaptered essays are valid. OpenBook standardizes **shape and trust**, not shortness. Length is earned; padding is not.

---

## See the difference

Same night. Two shapes.

| | Status dump | OpenBook |
|---|-------------|---------|
| Read | Lists and greens | Sixty-second story, then chapters |
| Decide | Re-enter the terminal | ≤5 plain questions with room for a pen |
| Trust | Asserted | Receipts in the appendix |

Start here: [examples/before-after/](./examples/before-after/). For the long-report pattern
(decisions embedded in their chapters, indexed at the end), see
[examples/embedded-decisions.md](./examples/embedded-decisions.md).

---

## For Claude Code / Cursor

Paste-ready prompt: [USE.md](./USE.md)

Longer Claude Code notes: [integrations/claude-code.md](./integrations/claude-code.md)

---

## Vision

Why this exists, who it is for, and where it goes: [VISION.md](./VISION.md)

---

## From Mirror Factory

OpenBook is extracted from how [Mirror Factory](https://www.mirrorfactory.com) runs overnight agents: narrative morning reports, pen-ready decisions, receipts underneath. We open-sourced the contract so any coding agent can speak clearly to a human.

---

## License

[MIT](./LICENSE)

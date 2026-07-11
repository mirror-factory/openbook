# OpenBook

**Agent work, written for humans.**

OpenBook is a small open-source kit for turning long-horizon agent runs into reports people can actually read: on screen, on paper, or on e-ink.

Agents are getting good at *doing* work. What they leave behind is often a status dump: lists, greens, and jargon that only makes sense in the terminal. OpenBook gives agents a durable report shape so a human can skim what happened, follow the story, and answer the questions that need a pen.

It is not an agent framework. It's a simple handoff layer between the run and the reader.

---

## Try the demo (local)

Open [`docs/index.html`](./docs/index.html) in a browser after cloning (generated assets are included). Drag the slider to compare a dense agent transcript with an OpenBook **Brief**.

For a single shareable file (no other assets needed), open or send [`docs/openbook-demo.html`](./docs/openbook-demo.html) — it works via `file://`.

Rebuild panes anytime:

```bash
python scripts/build_demo.py
```

(Standard and Essay panes are still generated for local inspection; the live demo shows Brief.)

---

## 60-second install

```bash
git clone https://github.com/mirror-factory/openbook.git
cd openbook
```

1. Point your coding agent at this folder (or paste [USE.md](./USE.md) into `CLAUDE.md`, a Cursor rule, or the session prompt).
2. At the end of a long run, the agent writes `REPORT.md` using [formats/report.md](./formats/report.md). **Default length: Brief** (~one page).
3. Check structure, then optionally render PDF:

```bash
pip install -r requirements.txt
playwright install chromium

python scripts/check_report.py path/to/REPORT.md
python scripts/render_report.py path/to/REPORT.md -o path/to/REPORT.pdf
```

Never browser-print a `file://` tab. Chrome injects date and URL footers. Use `render_report.py` only.

---

## Length profiles

| Profile | Target | Role |
|---------|--------|------|
| **Brief** (default) | ~1 page | Prose lede carries the story; no Narrative section |
| **Standard** | ~2–4 pages | Sixty-second abstract + short prose Narrative |
| **Essay** | long, when earned | Chaptered Hybrid (pens where context lives) |

See [formats/report.md](./formats/report.md) for rules. Mirror Factory mornings often prefer Essay; most public handoffs should start at Brief.

---

## What's in the kit

| Piece | Job |
|-------|-----|
| [formats/](./formats/) | Report formats agents load and humans read |
| [styles/](./styles/) | Voice and prose guidance for clearer writing |
| [scripts/](./scripts/) | Structural checks, PDF render, demo build |
| [examples/](./examples/) | Same-night before / Brief / Standard / Essay |
| [render/](./render/) | Report CSS (warm paper screen + Letter print) |
| [docs/](./docs/) | Interactive before/after demo |
| [CHANGELOG.md](./CHANGELOG.md) | Release notes |

---

## See the difference

| | Status dump | OpenBook |
|---|-------------|---------|
| Read | Lists and greens | Sixty-second story at the right depth |
| Decide | Re-enter the terminal | Plain asks with room for a pen |
| Follow-up | Asserted | Receipts in the appendix |

Markdown examples: [examples/before-after/](./examples/before-after/). Interactive: [docs/index.html](./docs/index.html).

---

## For Claude Code / Cursor

Paste-ready prompt: [USE.md](./USE.md)

Longer Claude Code notes: [integrations/claude-code.md](./integrations/claude-code.md)

---

## Vision

Why this exists, who it is for, and where it goes: [VISION.md](./VISION.md)

---

## From Mirror Factory

OpenBook comes from how [Mirror Factory](https://www.mirrorfactory.com) runs overnight agents: narrative morning reports, pen-ready decisions, receipts underneath. We open-sourced the kit so any coding agent can leave work that a human can read.

---

## License

[MIT](./LICENSE)

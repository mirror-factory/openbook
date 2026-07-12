# AGENTS.md, openbook

OpenBook is an open-source kit of Markdown report formats that make long-horizon agent runs readable to humans, rendered as warm-paper HTML and PDF. Read VISION.md for the point and docs/requirements.md for the full spec before changing anything.

## Invariants

- The kit stays Markdown in a folder: no build step, no server, no accounts, no SDK. If a change adds infrastructure, it is wrong.
- formats/report.md is the contract. Exact H2 headings per length profile, decision blocks as `### Decision N · short handle`, self-contained, plain references only. Changing the contract requires updating check_report.py, the examples, and the demo in the same change.
- Truthfulness rules are not negotiable: dead ends are content, no invented timestamps, the editor may cut but never invent. A report may never be more optimistic than its transcript.
- The monitor lives in a separate private repo. No monitor code, no monitor contract docs in this repo.

## Voice

All repo prose follows styles/librarian.md: economical, warm through specificity, no exclamation points, no em dashes, failures named plainly.

## End-of-run handoff

Prefer [`skills/openbook/SKILL.md`](./skills/openbook/SKILL.md) (`/openbook`). Agents without skill support use the short fallback in [`USE.md`](./USE.md).

## Commands

```
python scripts/check_report.py <report.md>    structural checker, the seatbelt
python scripts/render_report.py <report.md>   HTML and PDF, never browser print
python scripts/build_demo.py                  regenerates docs/ demo panes from examples
python evals/run_evals.py                     Layer 1 structural evals (CI)
```

Run the checker on every example and fixture you touch. If check_report.py and formats/report.md disagree, the format doc wins and the checker gets fixed.

## Cursor Cloud specific instructions

This is a Markdown-report kit: pure Python stdlib CLIs plus a static demo site. No app server, no build step, no automated unit-test framework, no code linter. The only runtime dependency is `playwright` (needed by `scripts/render_report.py` for PDF export). The update script installs it and the Chromium browser.

- Use `python3`, not `python`. The `python` binary does not exist on this VM even though the Commands section above spells commands as `python ...`.
- `playwright` is installed with `pip install --user`, so its console script lands in `~/.local/bin` (not on PATH). Invoke it as `python3 -m playwright ...` (e.g. `python3 -m playwright install chromium`).
- Tests / CI: `python3 evals/run_evals.py` is the Layer 1 structural suite that CI runs (`.github/workflows/evals.yml`). `python3 scripts/check_report.py <report.md>` is the structural "linter"/seatbelt for a single report. There is no separate lint or unit-test command.
- PDF/HTML render: `python3 scripts/render_report.py <report.md> -o out.pdf` launches headless Chromium via Playwright. Chromium must already be installed (the update script does this). Add `--html-only out.html` to also dump the intermediate HTML.
- Demo site: `docs/` is static HTML. Preview it with `python3 -m http.server 8099` run from `docs/`, then open `openbook-demo.html` or `index.html`. `python3 scripts/build_demo.py` regenerates the demo panes from `examples/`; it is deterministic, so a clean checkout produces no diff.

## Design

Demo and rendered surfaces use the chosen Dragonglass direction, light mode default. Tokens: paper #F2EEE5 and #E7E4D8, ink #1A1915, night ground #0A0A09, accents Signal Red #F54C26 and Green Pulse #CEF25A first among seven. Type: Helvena display, DM Mono labels, Source Serif 4 for report content, Manrope as web fallback. The design source of truth is the OpenBook Surfaces exploration HTML (kept outside this repo); extract from it, do not invent.

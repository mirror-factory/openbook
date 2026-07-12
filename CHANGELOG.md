# Changelog

Notable changes to OpenBook. Format follows [Keep a Changelog](https://keepachangelog.com/).

## 0.2.0-dev — 2026-07-12

Docs foundation for the next cut. Live demo remains at [mirror-factory.github.io/openbook](https://mirror-factory.github.io/openbook/).

### Added

- **[`AGENTS.md`](./AGENTS.md)** — Cursor and coding-agent invariants for this repo
- **[`docs/requirements.md`](./docs/requirements.md)** — strategy, personas, roadmap, and product requirements (v0.3)
- **[`docs/design-pass-brief.md`](./docs/design-pass-brief.md)** — design-pass kickoff brief for surface exploration
- **[`skills/openbook/`](./skills/openbook/)** — `/openbook` skill for end-of-run handoffs (Brief default; Standard/Essay by arg or inference)
- **[`evals/`](./evals/)** — Layer 1 CI harness, seeded-flaw faithfulness fixture, Layer 2–4 protocols
- **[`docs/receipts.md`](./docs/receipts.md)** — `receipts.jsonl` shape; appendix lines extracted never paraphrased
- **[`styles/senior-engineer.md`](./styles/senior-engineer.md)** / **[`styles/coach.md`](./styles/coach.md)** — alternate voice cards (pager-owner precision; teach-the-next-run)
- **[`formats/assembly.md`](./formats/assembly.md)** — multi-agent night → one morning report (lede writer, decision merge, checker owner)
- **[`examples/parallel-night/`](./examples/parallel-night/)** — synthetic parallel-night transcript + assembled Brief

### Changed

- **[`VISION.md`](./VISION.md)** — rewritten as a one-page manifesto; detail moved to requirements
- **[`USE.md`](./USE.md)** — retired to a skill pointer plus one-paragraph paste fallback
- **README / integrations / AGENTS** — install path points at the skill first
- **[`scripts/check_report.py`](./scripts/check_report.py)** — fails on librarian violations (em dashes, exclamation points); warns when lede numeric claims lack Appendix refs
- **[`formats/report.md`](./formats/report.md)** — Appendix contract: extracted receipts; optional jsonl
- **[`scripts/render_report.py`](./scripts/render_report.py)** — folds sibling `receipts.jsonl` into Appendix on render
- **Demo restyle (Shift)** — [`docs/`](./docs/) before/after page uses Surfaces 2G tokens (paper `#F2EEE5`, ink `#1A1915`, night `#0A0A09`, Signal Red / Green Pulse), Manrope + DM Mono via Google Fonts, light default with a night toggle; wipe interaction unchanged. [`render/report.css`](./render/report.css) paper stack harmonized to the same tokens.
- **OG card** — [`docs/assets/og-card.png`](./docs/assets/og-card.png) (1200×630 from Surfaces 2H / OG Card Spotlight) plus `og:*` / `twitter:*` meta on the demo page. GitHub repo Settings → Social preview still needs a manual upload by Kyle.

## 0.1.0 — 2026-07-11

Public default is **Brief**: a one-page prose handoff, not a short essay wearing long-report furniture. Includes an interactive before/after demo.

### Added

- **Length profiles** — Brief (default), Standard, and Essay in [`formats/report.md`](./formats/report.md)
- **Before/after demo** — live wipe at [mirror-factory.github.io/openbook](https://mirror-factory.github.io/openbook/) (GitHub Pages from `docs/`)
- **Demo builder** — [`scripts/build_demo.py`](./scripts/build_demo.py) regenerates panes from the example pack
- **Example pack** — same July 8 night as transcript + Brief / Standard / Essay reports under [`examples/before-after/`](./examples/before-after/)

### Changed

- **Brief shape** — continuous sixty-second prose carries the story; `## Narrative` is forbidden on Brief (promote to Standard if you need chapters)
- **Cover / Appendix** — drop Cover stats; optional `**By the numbers:**` lives in the Appendix
- **Decisions** — prefer `### Decision N · short handle` (legacy `### N. [?]` still parses with a warning)
- **Rendering** — warm paper, Source Serif 4 stack with Georgia fallbacks, masthead byline + read time, standfirst lede, print-only pen rooms ([`render/report.css`](./render/report.css))
- **Checker** — length-conditional required sections and Brief-specific warnings ([`scripts/check_report.py`](./scripts/check_report.py))
- **Docs** — README, USE.md, and librarian style updated for Brief-first handoffs

### Fixed

- Demo wipe handle no longer loses the drag to iframes
- Pane scroll sync is smoother (less jitter between before and after)
- Print styles stay last in the cascade so screen overrides cannot break PDF/print

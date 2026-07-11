# Changelog

Notable changes to OpenBook. Format follows [Keep a Changelog](https://keepachangelog.com/).

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

# Before / after

Same night (2026-07-12): an agent builds OpenBook, then reports in OpenBook. Four shapes.

| File | What you get |
|------|----------------|
| [before.md](./before.md) | Dense agent-session transcript |
| [after-brief.md](./after-brief.md) | **Default OpenBook** — the page that explains the product |
| [after-standard.md](./after-standard.md) | Same night with short Narrative chapters |
| [after-essay.md](./after-essay.md) | Hybrid essay (chapter pens + closing index) |

**Accuracy:** `before.md` is the same night as the after-* files. It is noisy on purpose; it is not a different story.

**How to compare:** skim the transcript, then read `after-brief.md` (try reading only the bold). Open Standard or Essay when you want more story. Live wipe: [mirror-factory.github.io/openbook](https://mirror-factory.github.io/openbook/).

## Production rules (for future examples)

- Same night for before and all after-* lengths.
- Each after-* must pass `scripts/check_report.py` and render via `scripts/render_report.py`.
- No secrets. Plain-reference always (words first; IDs in parentheses at most).
- Brief: prose lede only; numbers in Appendix `**By the numbers:**`.

Length is a product choice. Trust and finishability matter more than page count.

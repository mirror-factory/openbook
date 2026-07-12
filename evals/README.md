# Evals

Four layers, cheapest first. Standing rule: **a report may never be more optimistic than its transcript.**

| Layer | What | Command |
|-------|------|---------|
| 1 | Structural checks (CI) | `python evals/run_evals.py` |
| 2 | Skill generation benchmarks (10× per fixture) | Manual; see [RESULTS.md](./RESULTS.md) |
| 3 | Faithfulness hooks vs seeded ground truth | `python evals/run_evals.py --layer3 REPORT.md` |
| 4 | Human comprehension | Protocol below |

## Fixtures

| Path | Role |
|------|------|
| [fixtures/broken.md](./fixtures/broken.md) | Must fail `check_report.py` |
| [fixtures/seeded-flaw/](./fixtures/seeded-flaw/) | Transcript + `ground-truth.yaml` for Layer 3 |

Known-good examples under `examples/before-after/after-*.md` must pass Layer 1.

## Layer 4 · two-minute test

A reader gets the report for two minutes, then answers five questions scored against a control who read the raw transcript for ten minutes:

1. What happened?
2. What failed?
3. What needs deciding?
4. Would you ship?
5. What happens next?

Also score decision self-containment: a non-builder answers each decision block without opening anything else.

## Dogfood metrics (field)

- Escape-hatch rate: times the raw transcript is opened after reading the report
- Share of decisions answered within 24 hours
- Minutes of morning review per run

Track these outside CI. They are the product truth Layer 1 cannot see.

## Librarian seatbelt

`scripts/check_report.py` fails on em dashes (U+2014) and exclamation points in report Markdown. Layer 1 runs that checker.

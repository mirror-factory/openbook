# Eval results

Layer 2 protocol and a placeholder scoreboard. Fill rows after skill generation runs.

## Layer 2 protocol (skill generation benchmarks)

For each fixture transcript under `evals/fixtures/` (and the July 8 before.md):

1. Invoke `/openbook` (or the paste fallback) **10 times** with a fresh context each run.
2. Record: checker pass/fail, length profile chosen, token/cost estimate if available.
3. Measure variance: how often the same dead ends and decisions surface.

Do not average away a single run that invents optimism. The standing rule: a report may never be more optimistic than its transcript.

## Scoreboard (placeholder)

| Fixture | Skill rev | Pass/10 | Failure recall (mean) | Decision recall (mean) | Invented timestamps | Notes |
|---------|-----------|---------|-----------------------|------------------------|---------------------|-------|
| before-after/before.md | n/a | n/a | n/a | n/a | n/a | July 8 night |
| seeded-flaw/transcript.md | n/a | n/a | n/a | n/a | n/a | 3 dead ends, 1 masked, 2 forks |
| parallel-night/transcript.md | n/a | n/a | n/a | n/a | n/a | synthetic multi-agent |

Layer 1 CI does not fill this table. Layer 3 hooks: `python evals/run_evals.py --layer3 REPORT.md`.

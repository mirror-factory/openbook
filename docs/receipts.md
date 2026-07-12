# Receipts (v0.5)

Machine-extracted evidence for the Appendix. OpenBook is a legibility layer, not an integrity layer; receipts make the appendix **verifiable** rather than agent-paraphrased.

## Rule

Appendix receipt lines are **extracted, never paraphrased**. Copy the command, the test tally, the PR title, the path. Softening "2 failed" into "a couple of issues" is a truthfulness failure.

Human prose stays in Cover, sixty-second, Narrative, What's next, and What we learned. Receipts live under Appendix (and optionally in `receipts.jsonl` beside the report).

## `receipts.jsonl`

One JSON object per line, UTF-8. Place the file next to `REPORT.md` (same directory, name `receipts.jsonl`). `scripts/render_report.py` folds these records into the Appendix when rendering.

### Record shape

| Field | Required | Meaning |
|-------|----------|---------|
| `kind` | yes | `command` · `test` · `pr` · `commit` · `path` · `source` · `pending-human` · `other` |
| `summary` | yes | Exact extracted line (what a human should see) |
| `ts` | no | ISO-8601 timestamp from the run log; never invent |
| `detail` | no | Extra extracted text (stdout tally, SHA, URL) |
| `ref` | no | Stable id (PR number, commit SHA prefix, path) |

Example:

```jsonl
{"kind":"test","summary":"pnpm exec vitest run packages/billing","detail":"16 passed","ts":"2026-07-09T22:18:00-04:00"}
{"kind":"pr","summary":"feat(billing): rate card JSON + debit after success","ref":"42","detail":"https://github.com/example/ledger-api/pull/42"}
{"kind":"pending-human","summary":"Extend: add to current scope vs mint child scope"}
```

### Folding into Markdown

On render, each record becomes one Appendix bullet:

```markdown
- [test] pnpm exec vitest run packages/billing (16 passed)
- [pr] feat(billing): rate card JSON + debit after success (42)
- [pending-human] Extend: add to current scope vs mint child scope
```

If the report Appendix already contains a `**By the numbers:**` line and hand-written receipts, folded lines append after them (deduped by identical summary text).

## Checker

`scripts/check_report.py` warns when the sixty-second version makes numeric claims that do not appear anywhere in the Appendix. Fix by extracting a matching receipt, not by deleting the fact from the lede.

## Authoring habit

1. During the run, append to `receipts.jsonl` (or keep a scratch list).
2. At handoff, write the story in the body.
3. Copy receipts into Appendix bullets (or leave jsonl for the renderer).
4. Run `check_report.py`. Treat receipt warnings as unfinished work.

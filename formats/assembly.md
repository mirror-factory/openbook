# Multi-agent assembly

How N run reports become one morning report. Load with [report.md](./report.md). Voice default: [librarian](../styles/librarian.md).

## Roles

| Role | Job |
|------|-----|
| **Contributor** | One agent, one workstream. Writes a section contribution or a full mini-report for its lane. |
| **Editor** | Assembles the morning report. Cuts for length and flow. Never invents. Never softens failures. |
| **Checker owner** | Runs `scripts/check_report.py` on the assembled `REPORT.md` before handoff. Usually the editor. |

Contributors do not merge each other's prose. The editor is the single writer of the final Cover, two-minute version, and ranked What's next.

## Inputs

Each contributor leaves, at minimum:

1. A truthful section (Narrative-shaped for Standard/Essay nights, or a short Brief-shaped note for small lanes).
2. Decision blocks that are self-contained (or an explicit "no decisions from this lane").
3. Appendix receipts extracted, not paraphrased ([receipts.md](../docs/receipts.md)).
4. Dead ends named. Missing work named as missing, not implied done.

Optional: `receipts.jsonl` beside a lane report for the renderer to fold later.

## Lede writer

The editor writes **one** two-minute version for the whole night.

- First sentence is the bottom line across all lanes.
- Include every failure that would change a human's morning, even if it lived in only one lane.
- Do not average optimism. If one lane failed, the lede may not read as an all-green night.
- Numeric claims must appear in the assembled Appendix.

## Decision merge

1. Collect every contributor decision block.
2. Drop duplicates (same ask, restated). Keep the clearest plain-language wording.
3. Rank by what blocks the human's next move, not by which agent finished first.
4. Prefer ≤3 on Brief, ≤5 on Standard/Essay total (chapter embeds plus cross-cuts).
5. Re-number as `### Decision N · short handle` in the assembled report.
6. If two lanes disagree on facts, the editor surfaces the conflict as content or as a decision; the editor does not pick a side quietly.

## Who runs the checker

The **editor** runs:

```bash
python scripts/check_report.py REPORT.md
```

Fix structure once. Do not invent receipts to silence warnings. Then render with `scripts/render_report.py` if PDF is needed.

Contributors may run the checker on their section contributions for hygiene; only the assembled document is the handoff gate.

## Length

- Default public handoff: **Brief**.
- Promote to Standard or Essay when the night earned chapters. Padding is an anti-pattern.
- Section contributions that will not fit a Brief lede are a signal to promote, not a signal to delete failures.

## Truthfulness (assembly-specific)

- The editor may cut, reorder, and tighten.
- The editor may not invent timestamps, PRs, test counts, or decisions nobody asked.
- The assembled report may never be more optimistic than the union of contributor transcripts.
- Delivery failures stay loud.

## Example pack

Synthetic parallel night: [examples/parallel-night/](../examples/parallel-night/).

## Cover

**Title:** Three lanes, one morning
**Subtitle:** Contract edge cases, Desk/Catalog mockups, demo pane refresh
**Length:** Brief
**Author:** Dewey (editor) · lanes reed, moss, kiln
**When:** 2026-07-10 · parallel night, assembled 7:10am Eastern

## Sixty Seconds

Three agents ran in parallel; the morning report is one story. The model package now has 70 tests green after acceptance-parse edge cases, with a legacy `done:` migrate deliberately reverted. Design pushed Desk and Catalog mockups and abandoned a third IA called Stacks after one critique. The public demo before-pane copy refreshed; a night-mode CSS spike was started and discarded so tokens stay a human-owned pass.

What needs you is mostly unchanged from earlier design nights, plus one contract fork. Where a Document opens still blocks the shell re-spec. Desk and Catalog as two states of one Library still wants a yes or a named alternative. On the contract side: keep legacy `done:` keys read-only, or schedule a one-shot migrate with your eyes on the seed specs.

## What's next

### Decision 1 · where a Document opens

With the Library in the center and the Journal on the right, where does a Document or Folio open: replace the center, split it, or displace the Journal? This still blocks the shell re-spec.

### Decision 2 · one Library, two states

Do you buy Desk and Catalog as two states of one Library, with Ledger only as a by-time lens? Stacks was tried and dropped; if one concept should win outright, name it.

### Decision 3 · legacy done keys

Keep legacy `done:` keys read-only forever, or schedule a one-shot migrate to acceptance items with human review of hand-edited seed specs?

## What we learned

- Parallel lanes need one editor for the lede; three optimistic summaries would have lied about the discarded CSS and the reverted migrate.
- Abandoned concepts (Stacks) belong in the report when they cost a critique cycle.
- Demo token work stays human-gated; agents should stop early rather than half-commit.

## Appendix

**By the numbers:** 3 lanes · 70 model tests · 2 mockups · 1 demo rebuild · 1 PR · 2 dead ends named

- [test] pnpm exec vitest run packages/model (70 passed)
- [pr] fix(model): acceptance parse edge cases (7)
- [path] design/mockups/desk-v3.png · catalog-v3.png
- [path] design/notes/ledger-as-lens.md
- [command] python scripts/build_demo.py (ok)
- [pending-human] Document open · Desk/Catalog · legacy done keys
- Stacks IA abandoned after critique
- Legacy `done:` migrate reverted (seed specs still hand-edited)
- Night-mode CSS spike discarded (no commit)

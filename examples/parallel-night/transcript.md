# Synthetic parallel night — 2026-07-10

Three agents, one workspace, one editor assemble at morning. Constructed for the assembly guide; not a real run log.

---

## Lane A · contract (agent: reed)

session 2026-07-10T23:05:00-04:00  cwd=/work/atrium  goal=fix-acceptance-parse

> finish acceptance-item parse edge cases; leave decisions for morning.

[read] packages/model/src/frontmatter.ts
$ pnpm exec vitest run packages/model -t acceptance
 Tests  12 passed (12)

[edit] packages/model/src/frontmatter.ts  (+ checkbox trim on Windows CR)
[edit] packages/model/src/frontmatter.test.ts  (+2 cases)

$ pnpm exec vitest run packages/model
 Tests  70 passed (70)

DEAD END: tried to auto-migrate legacy `done:` keys to acceptance items. Touched seed specs the human still edits by hand. Reverted. Left a note in the PR.

$ gh pr create --title "fix(model): acceptance parse edge cases"
https://github.com/example/atrium/pull/7

Lane A decisions:
- Keep legacy `done:` keys read-only forever, or schedule a one-shot migrate with human review?

Lane A receipts: 70 model tests · PR 7 · migrate reverted

---

## Lane B · design (agent: moss)

session 2026-07-10T23:12:00-04:00  cwd=/work/atrium  goal=library-desk-catalog

> push Desk/Catalog mockups; critique Ledger as default.

[write] design/mockups/desk-v3.png
[write] design/mockups/catalog-v3.png
[write] design/notes/ledger-as-lens.md

Critique circle (3 reviewers): Desk greeting is clear; Catalog search affordance still weak; Ledger-as-default loses again.

DEAD END: attempted a third IA called "Stacks." Collapsed into Catalog filters after one critique. Deleted mockup.

Lane B decisions:
- Ship Desk/Catalog as two states of one Library?
- Where does a Document open (center replace vs split vs displace Journal)? Same ask as July 8; still open.

Lane B receipts: 2 mockups · 1 note · Stacks abandoned

---

## Lane C · demo docs (agent: kiln)

session 2026-07-10T23:40:00-04:00  cwd=/work/openbook  goal=demo-pane-refresh

> refresh before pane copy only; do not restyle tokens tonight.

[edit] docs/panes/before.html  (tighten status-dump sample)
$ python scripts/build_demo.py
 ok

DEAD END: started a night-mode CSS spike, then stopped. Token restyle is a separate human-owned pass. Left the branch dirty and discarded.

MASKED RISK avoided: did not commit half-finished night CSS.

Lane C decisions: none. Blocked on design tokens (human).

Lane C receipts: demo build ok · night CSS discarded

---

## Editor assemble (agent: dewey)

Morning. Read three lane notes. Wrote one Brief. Ranked decisions: Document open (blocks shell), Desk/Catalog (design), legacy `done:` keys (contract). Dropped Lane C empty decision slot. Copied receipts into Appendix without softening the Stacks or migrate dead ends.

Checker: `python scripts/check_report.py examples/parallel-night/REPORT.md`

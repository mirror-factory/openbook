## Cover

**Title:** Auth middleware: the night the budget actually stopped
**Subtitle:** Spend events were never written; the hard stop was decorative
**Length:** Brief
**Author:** Example coding agent (OpenBook sample)
**For:** A tech lead who asked for a long-horizon fix and went to sleep
**When:** 2026-07-11 · ~3 hours

## Sixty Seconds

Budgets could not stop anything. The middleware, tables, and admin panel were real and merged, but nothing wrote spend events, so burn stayed zero and the hard stop was decorative. This run closes the loop: every model call debits cents against the scope from a verified rate card; the stop notice carries an Extend control that resumes the paused run.

Review-after-green found a billing skip on reordered messages and a cache-write shape tests missed; both fixed with regressions. The suite is green. Three decisions below need you: merge tier, smoke test tonight or not, and whether unpriced non-Anthropic models stay visible-only until volume needs them.

## What's next

### Decision 1 · merge with a named reviewer

Merge this Tier-2 money PR with a named human reviewer? It touches billing. Green tests are not a substitute for eyes-on.

### Decision 2 · staged smoke tonight

Run the staged $5 smoke test tonight (about 15 minutes)? Steps in the PR: warn at 80%, stop at ceiling, Extend, resume. A failure at any step names the lying layer.

### Decision 3 · leave non-Anthropic unpriced

Leave non-Anthropic models unpriced (tokens visible, cents zero) until volume needs them? Safer than inventing rates. Wrong once real volume routes there.

## What we learned

- **Merged and works drift** when the last wire is never load-tested.
- **Refusing to invent numbers** is a feature in a ledger.
- **Review-after-green** catches seam bugs unit tests miss.

## Appendix

**By the numbers:** 1 PR · 24 tests added · 2 review findings fixed · smoke path staged for human

- Rate card verified for Anthropic; other providers marked unpriced rather than invented
- Middleware debit after every model call; Discord stop notice with Extend
- Billing skip on reordered messages and cache-write shape: fixed with regressions

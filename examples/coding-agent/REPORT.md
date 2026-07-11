## Cover

**Title:** Auth middleware: the night the budget actually stopped
**Length:** Brief
**Author:** Example coding agent (OpenBook sample)
**For:** A tech lead who asked for a long-horizon fix and went to sleep
**When:** 2026-07-11 · ~3 hours
**Stats:** 1 PR · 24 tests added · 2 review findings fixed · smoke path staged for human

## The sixty-second version

**Budgets could not stop anything.** The middleware, tables, and admin panel were real and merged, but nothing wrote spend events, so burn stayed zero and the hard stop was decorative. This run closes the loop: every model call debits cents against the scope from a verified rate card; the stop notice carries an Extend control that resumes the paused run.

**What needs you:** three decisions below (merge tier, smoke test tonight or not, unpriced non-Anthropic models). The PR is green and waiting.

## Narrative

- Task file called this the most important unbuilt feature; acceptance vs code showed spend events were never written, so burn stayed zero.
- Shipped: verified Anthropic rate card; middleware debit after every model call; Discord stop notice with Extend; other providers marked unpriced rather than invented.
- Review-after-green found a billing skip on reordered messages and a cache-write shape tests missed; both fixed with regressions. Suite green.

## What's next

### 1. [?] Merge this Tier-2 money PR with a named human reviewer?

It touches billing. Green tests are not a substitute for a named eyes-on.

### 2. [?] Run the staged $5 smoke test tonight (15 minutes)?

Steps in the PR: warn at 80%, stop at ceiling, Extend, resume. A failure at any step names the lying layer.

### 3. [?] Leave non-Anthropic models unpriced (tokens visible, cents zero) until Rootstock volume needs them?

Safer than inventing rates. Wrong once real volume routes there.

## What we learned

- "Merged" and "works" drift when the last wire is never load-tested.
- Refusing to invent numbers is a feature in a ledger.
- Review-after-green catches seam bugs unit tests miss.

## Appendix

- PR: `feat(billing): record spend and enforce budgets` (branch `feat/budget-writers`)
- Tests: +24, suite green
- Docs: CLAUDE.md note on unmetered subagents
- PENDING-HUMAN: smoke test steps in PR description

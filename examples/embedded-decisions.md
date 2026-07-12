## Cover

**Title:** Embedded Decisions, Demonstrated
**Subtitle:** Hybrid pattern: chapter pens, then index plus one cross-cutting ask
**Length:** Essay
**Author:** An overnight agent (OpenBook example)
**For:** A human reading on paper, with a pen
**When:** The morning after a long run

## Sixty Seconds

**This example shows the Hybrid long-report pattern.** Chapter-owned decisions sit at the end of the chapter that explains them, with pen room there. What's next indexes those asks and holds only cross-cutting questions that span the whole night. Every block is self-contained: no internal IDs, no "see chapter two."

## Narrative

### Chapter 1 · The deploy pipeline slowed down

The nightly deploy went from four minutes to eleven over two weeks. The cause is not one regression but an accumulation:

- The container image grew past two gigabytes
- The test suite doubled
- The artifact cache misses on every run because the cache key includes a timestamp

**The cache key is a one-line fix** and was made during the run. The image size and suite growth are real trade-offs that belong to a human.

The image grew because three teams added system dependencies independently. Splitting the image into a slim runtime and a fat build stage would cut deploy time roughly in half, but it changes how every team adds dependencies from now on.

### Decision 1 · slim-runtime and fat-build stages

Split the deploy image into slim-runtime and fat-build stages? Deploys would drop from eleven minutes toward five. The cost: teams add runtime dependencies through one reviewed file instead of anywhere, which is a process change for all three teams. The alternative is accepting slower deploys as the suite grows.

### Chapter 2 · The flaky checkout test

One end-to-end test failed on roughly one run in nine, always on the payment step, never reproducibly in isolation. The run traced it to a race between the cart total recalculating and the pay button enabling. That is a real product bug wearing a test costume: a fast human could click pay before the total settles. A regression test now pins the fixed ordering.

**The fix shipped during the run.** What remains is a policy question: this is the fourth race found by a flaky test this quarter, and each one was treated as test noise for weeks first.

### Decision 2 · flakes as suspected product bugs

Treat any test that flakes twice as a suspected product bug, with a named owner within a day? The last four flakes were all real races users could hit. The cost is occasional false alarms taking an hour of someone's day. The alternative keeps flakes in the retry pile, where this one sat for three weeks.

## What's next

Chapter decisions (pen rooms above):

1. Slim-runtime and fat-build stages (end of chapter 1)
2. Flakes as suspected product bugs (end of chapter 2)

### Decision 3 · slow-deploy paging rule

Should deploys that exceed eight minutes page the on-call, or only open a ticket? Both chapter fixes reduce deploy time and flake noise, but the night still needs a standing rule for "slow is broken." Paging wakes someone; a ticket can wait until morning. Pick the threshold behavior once for the whole team.

## What we learned

- A trailing-only question list is a memory test; chapter pens remove the test.
- A question a reader can answer without flipping pages is a question that gets answered.
- Cross-cutting asks belong on the closing page, not stuffed into the last chapter.

## Appendix

**By the numbers:** 2 chapter decisions · 1 cross-cutting ask · every question self-contained

- The cache-key fix, the image measurements, and the race trace live in the run's working log alongside this report.
- Nothing in this example refers to a real system; the pattern is the content.

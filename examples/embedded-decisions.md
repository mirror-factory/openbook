## Cover

**Title:** Embedded Decisions, Demonstrated
**Subtitle:** A compact example of decisions living where their context lives
**Author:** An overnight agent (OpenBook example)
**For:** A human reading on paper, with a pen
**When:** The morning after a long run
**Stats:** 2 embedded decisions · 1 trailing index · every question self-contained

## The sixty-second version

**This example shows the long-report pattern.** When a narrative runs long, a trailing question list fights human memory: by the time the reader reaches it, the chapter that explains question three is forgotten. The fix is structural. Each decision block sits at the end of the chapter that gives it context, with its pen room, and What's next becomes a one-line index. Every question is also written to stand alone: no internal IDs, no references to things introduced elsewhere and not restated.

## Narrative

### Chapter 1 · The deploy pipeline slowed down

The nightly deploy went from four minutes to eleven over two weeks. The cause is not one regression but an accumulation: the container image grew past two gigabytes, the test suite doubled, and the artifact cache misses on every run because the cache key includes a timestamp. The cache key is a one-line fix and was made during the run. The image size and suite growth are real trade-offs that belong to a human.

The image grew because three teams added system dependencies independently. Splitting the image into a slim runtime and a fat build stage would cut deploy time roughly in half, but it changes how every team adds dependencies from now on.

### 1. [?] Split the deploy image into slim-runtime and fat-build stages?
Deploys would drop from eleven minutes toward five. The cost: teams add runtime dependencies through one reviewed file instead of anywhere, which is a process change for all three teams. The alternative is accepting slower deploys as the suite grows.

### Chapter 2 · The flaky checkout test

One end-to-end test failed on roughly one run in nine, always on the payment step, never reproducibly in isolation. The run traced it to a race between the cart total recalculating and the pay button enabling. That is a real product bug wearing a test costume: a fast human could click pay before the total settles. A regression test now pins the fixed ordering.

The fix shipped during the run. What remains is a policy question: this is the fourth race found by a flaky test this quarter, and each one was treated as test noise for weeks first.

### 2. [?] Treat any test that flakes twice as a suspected product bug, with a named owner within a day?
The last four flakes were all real races users could hit. The cost is occasional false alarms taking an hour of someone's day. The alternative keeps flakes in the retry pile, where this one sat for three weeks.

## What's next

The decisions live in their chapters, each with pen room there. The index:

1. Split the deploy image (end of chapter 1)
2. Flakes as suspected product bugs (end of chapter 2)

## What we learned

- A trailing question list is a memory test the reader did not sign up for; embedding removes the test.
- A question a reader can answer without flipping pages is a question that gets answered.
- Flaky tests earned a standing rule this run; noise that repeats is signal.

## Appendix

- The cache-key fix, the image measurements, and the race trace live in the run's working log alongside this report.
- Nothing in this example refers to a real system; the pattern is the content.

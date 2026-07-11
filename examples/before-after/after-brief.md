## Cover

**Title:** The Night of July 8th
**Subtitle:** Design ready for pen; markdown contract battle-tested
**Length:** Brief
**Author:** Dewey
**When:** 2026-07-08 · shift 11:24pm–7:00am Eastern

## The sixty-second version

The design direction is ready for your pen, and one layout question blocks the shell re-spec. The Library should be one surface with two states: a Desk that greets you with what changed while you were away, and a Catalog that answers when you ask. The time-led Ledger loses as a default because the Journal already owns the record. Sessions become guided worksheets. Everything obeys one law: information moves between the periphery and the center without demanding attention.

The markdown contract survived an adversarial review. Fifty-four tests were green when a fleet of review agents went looking anyway and found seven data-integrity bugs behind the checkmark, including a Windows byte-order mark that would have silently destroyed frontmatter on save. All seven are fixed and sixty-eight tests now pass. The night's best lesson rode along for free: green is a hypothesis until someone tries to break it.

One find arrived uninvited. Goal intake asks what done looks like tonight, and that answer is already an acceptance line. Sessions could carry the same contract shape Specs do. Nobody decided this; the design wants it, and it is yours to bless or refuse.

Three decisions below want your pen. The first gates the next design pass; an answer before tomorrow evening keeps the shell re-spec off the critical path.

## What's next

### Decision 1 · where a Document opens

With the Library in the center and the Journal on the right, where does a Document or Folio open: replace the center, split it, or displace the Journal? This blocks the shell re-spec, whose acceptance criteria still encode the pre-kickoff layout.

### Decision 2 · one Library, two states

Do you buy Desk and Catalog as two states of one Library (Desk on arrival, Catalog when you ask), with Ledger surviving only as a by-time lens? If one concept should win outright, name it and the next shift consolidates.

### Decision 3 · Sessions with acceptance lines

Should Sessions carry acceptance criteria from goal intake ("what does done look like"), checked at close? It expands what a Session is, and it fell out of the worksheet design uninvited. Bless or refuse.

## What we learned

- Research notes lint the mockups.
- Review-after-green is non-negotiable.
- A known-wrong build can still donate parts (the Ledger did).

## Appendix

**By the numbers:** 6 research notes · 3 Library concepts · 2 pull requests · 68 tests green

- Markdown contract pull request · acceptance 5/5 · 68 tests
- Design research pull request · Library concepts, worksheets, shell composition
- Pending human: shell re-spec; the three decisions above
- This example is redacted from a real night shift.

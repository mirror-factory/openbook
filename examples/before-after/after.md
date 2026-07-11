## Cover

**Title:** The Night of July 8th
**Subtitle:** Design research, three Libraries, five worksheets, and the humbling of a green checkmark
**Author:** Dewey (OpenBook example, redacted from a real night shift)
**For:** A founder reading over coffee, with a pen
**When:** 2026-07-08 · shift 11:24pm–7:00am Eastern
**Stats:** 6 research notes · 10 mockups · 6 critiques · 2 PRs · 17 working commits · 68 tests green · every claim has a file behind it

## The sixty-second version

**The design direction is ready for your pen.** Six research notes, three genuinely distinct Library concepts with honest critiques, session worksheets (four of five mockuped), the three-pane composition in both themes, and a one-page recommendation. In five sentences: the Library center should be one surface with two states (desk on arrival, catalog when you ask); the time-led ledger loses as a default because the Journal already owns the record; Sessions become guided worksheet journeys; semantic zoom stays and gains anchor preservation plus relevance-directed arrival; everything obeys one law: information moves between periphery and center without demanding attention.

**The markdown contract is done and battle-tested.** Parser, serializer, projections, ready-flip, byte-identical round-trips. All acceptance items passed. A 28-agent review fleet then found seven confirmed data-integrity bugs behind a green checkmark, including a Windows BOM that would have silently destroyed real frontmatter on save. All fixed. Sixty-eight tests green. That story is the best argument for review-after-green in the repo.

**The most interesting finding** was not in a mockup. Goal intake asks what done looks like tonight; the answer is an acceptance line. Sessions can carry the same contract shape Specs do. Nobody decided this; the design wants it.

**What needs you:** five ranked questions in What's next. The urgent one: with the Library in the center and the Journal on the right, where does a Document or Folio open?

## Narrative

### Chapter 1 · Setting up the room

I clocked in at 11:24pm and did the reading in the assigned order: kickoff notes, charter, frozen demo, prior register notes, and the July 3 session that is supposed to be the north star. Two things fell out before any research happened.

First, the autopsy of the current Library surface took one look. It is a search box over a flat list, one arrangement, no memory of the last visit, and rows that do nothing when clicked unless they happen to be folios. The kickoff verdict ("I don't like it. But that's a good thing. It's functionally getting something.") is generous; the bones are a list and the feel is a filing cabinet with the drawers welded shut. The microcopy, though, is excellent, and everything built tonight ports it verbatim.

Second, a conflict you should know about: the shell task still encodes the pre-kickoff layout. Its acceptance criteria pin the Journal inside the navigator; Monday's kickoff moved the Journal to the right pane and the Library to the center. Per the brief that task was not touched. It needs your pen before anyone builds it. This is flagged in both PRs and again in What's next.

Operational note for honesty's sake: quality floors (four research notes, three Library concepts, one contract PR) were all met by 11:53pm, twenty-nine minutes in. That is not a boast; it recalibrated the night. The remaining hours went to depth: harder critiques, a self-review of the code, and this report. Chapter 8 covers what pacing a shift like this taught, including the two times the clock embarrassed the author.

The reading also set the emotional register for the night. The July 3 session is not a mood board; it is a contract about how Dewey should sound when interviewing, how corrections should look on a shelf, and what "quiet" means when the product is full of information. Everything below either honors that register or names where it failed.

### Chapter 2 · The research arc, and the night's thesis

Six topics, in priority order: quiet UI, calm density, library and archive interaction patterns, OpenDesign, semantic zoom, and markdown reading. Each has a note with sources, who does it well, and an adopt/reject list. Rather than summarize six summaries, here is the through-line, because the topics converged with almost suspicious cooperation.

The quiet-UI literature (Weiser and Brown's calm technology, Amber Case, iA's typographic invisibility) gives the law: information should move between the periphery and the center of attention without ever demanding it. A quiet interface is not an empty one; a reading room is full of information that waits to be looked at. Tufte and the density writers add the mechanism: density through typography and a fixed grammar, never through widgets; micro/macro reading, where the page reads whole in five seconds and every line is an entry point; and the data-ink discipline that later caught a mockup double-counting a conflict three ways.

Then the librarians delivered the night's thesis. Mitchell Whitelaw's critique of digital collections says the search box "withholds information, and demands a query," a gallery where you cannot walk the floor, only interrogate the attendant. His alternative, the generous interface, shows the collection, offers multiple entry points, and gives every item a rich surrogate rather than a dead row. That sentence is the diagnosis of the current Library, written years before it was built. The archival literature adds the four ways researchers enter an archive (top-down from the overview, bottom-up from an item, interrogative with a question, opportunistic by wandering) and the reminder that the pointer-index model is what archivists have called respect des fonds for two centuries: your stuff stays where your stuff is, and the description records custody.

OpenDesign contributed conventions rather than aesthetics: a nine-section DESIGN.md that makes a design system portable across agents, and a discipline for generative UI returned to in chapter 3. Zoom research (Pad++, Furnas degree-of-interest) and the markdown-reading survey (Typora, Tufte CSS, Butterick) mostly validated what the frozen Document demo already does, while adding two behaviors it does not: anchor preservation and relevance-directed arrival.

What was rejected matters as much as what was adopted. Notification-shaped urgency, gamified streaks, folder trees as the primary mental model, and a third type voice that "explains the UI to the user" all failed the quiet-UI and charter tests. Those rejections later became the anti-pattern list in the DESIGN.md draft.

### Chapter 3 · Three ways to be a Library

You asked for two or three distinct concepts, not variations on one idea. Three were built, each with a one-sentence thesis, each critiqued against the research notes before moving on. The critiques sit beside the mockups; the parts quoted below are where the author lost the argument with himself.

**Concept A, "The Desk."** Thesis: the Library is a place you return to, so it opens on what happened while you were away, then hands you back your desk. The recap leads as settled prose, followed by word-sized event lines, cards for things that need judgment, resume rows, and shelves in a fixed catalog-card grammar. Pointer-index states are visible in the rows: a connected source shows its path; a lost one degrades honestly ("source moved or lost · reconnect · repoint").

The first pass failed its own research note: the recap restated the event list nearly word for word, and one conflict appeared three times (recap prose, needs-you card, shelf row tick). By data-ink standards half the recap was erasable, so it was erased. Version 2 cut prose to judgment only. Version 3, after the third critique, made needs-you cards expand in place with evidence before verbs go live, so approving a conflict from the dashboard means approving with the evidence on the table, not from a headline.

**Concept B, "The Catalog."** Thesis: a great catalog makes ten thousand items feel like one drawer; ask, and the answer comes back ready to act. The ask leads; the answer comes in prose before receipts; every result is a generous surrogate whose composition varies by kind while the grammar (title, why, context, verbs) never varies. A decision note arrives with its gist quoted; a folio arrives with its open acceptance item; a pointed doc arrives with its custody state; an open question arrives with a "Resolve in a Session" verb. Reweighting is real: four weights with plain-language values, a promise that nothing is refiled, a way back to the default arrangement, and "save as my default."

This is also a concrete answer to generative UI: generative composition, deterministic rendering. The model chooses facets and verbs from a fixed vocabulary; the shell renders fixed components. The vocabulary itself is a build-ready table (ten facets, nine verbs, four rules). A hallucinated facet is impossible by construction; the worst failure is a poorly chosen one, which is a correction rather than a betrayal.

The answer line above the results is, on reflection, the most valuable single sentence in any mockup that night. Search that withholds information and demands a query is replaced by search that answers first and shows receipts second.

### Chapter 4 · The useful failure

**Concept C, "The Ledger."** Thesis: the Library is a record of attention over time; what you have is inseparable from when it mattered. Days as headers, filings and decisions as entries, trails growing out of the record, and the best custody treatment of the night: a quiet box reading connected, transcribing, lost, reconnect.

It is recommended against as a default, and it was built anyway, because it teaches. The charter gives "the record" to the Journal. Monday's kickoff moved the Journal to the right pane precisely so the log has a home that is not the dashboard. A Library-as-ledger center pane is a second journal, and two records with one purpose is the exact doc-drift failure mode the charter warns about. So C dies as a default and lives as an organ donor: custody box, trails column (now left navigation), and milestone cards (how decisions could surface in A's recap) were salvaged into everything else. Dead ends are content; this one came with parts.

Building the known-wrong thing on purpose is a process claim as much as a design claim. If the night had only shipped A and B, the custody treatment would have been thinner, and the argument against a time-led Library would have been abstract. C made the argument concrete by failing in public.

### Chapter 5 · The composition, and the hard question it exposed

With priorities met, the whole room was assembled: navigation left (verbs first, then sessions, then the salvaged trails), Library center as A's arrival with B's ask one keystroke away, Journal right as one continuous notebook. Your entries lowercase and messy on purpose; agent entries blocked and marked; quick capture at the bottom with the honest promise that a copy is shelved. Shown open in the mockups; per the kickoff it starts closed and slides.

Building the composition did what mockup polish cannot: it exposed the layout's hard question. Where does a Document or Folio open now? The frozen shell's right pane hosted them; the kickoff gave that pane to the Journal. Replace the center over the Library? Split it? Displace the Journal? Every answer changes the six-state layout contract. That is question 1 below, and the shell task cannot be re-specced without it.

The dark theme pass earned its keep as a linter: hardcoded colors lit up like errors the moment graphite tokens landed. The theme's token values had been trapped inside the large frozen demo file; they now live as extractable tokens. A DESIGN.md draft (nine sections, including the anti-pattern list: no gamification, no notification-shaped design, no folders, no third type voice, no silent boundary crossings) sits in the PR marked proposal, unreviewed.

The composition also clarified what "two states of one Library" means in practice. Arrival is not a separate app; ask is not a modal bolted on. One surface, one grammar, a keystroke between desk and catalog. That recommendation is the spine of DIRECTION.md.

### Chapter 6 · Sessions as worksheets

Guidance should flow from activities, not from the user knowing what to ask. The starter set is five activities, each defined by trigger, inputs, and what happens to the output: goal intake at every door; business model canvas when the territory calls for walls; audience-and-offer for positioning; decision weigh-in at forks; handoff packaging when a spec goes ready. All five are built from one interaction primitive already validated: state, infer once, confirm or correct, shelve verbatim. A worksheet is a sequence of single questions wearing one card, never a form of twelve fields, and nothing an activity produces crosses a boundary without Circulation.

Four of the five have mockups. Goal intake produced the accidental discovery: its second beat asks what done looks like tonight, and the answer becomes the session's acceptance line, checked at close. Sessions quietly acquire the same contract shape Specs have. Question 2 asks whether to keep it.

The correction card is the register's thesis in one surface: the agent's guess steps aside, struck but legible; your words replace it on the shelf, verbatim. The decision weigh-in added a rule worth keeping in the system prompt: the agent's position is held until the human states a lean ("your lean is data I refuse to contaminate"), then it is one sentence long. Options carry provenance; criteria stay in your words; "genuinely torn" is a real answer. The handoff chooser closes the set by asking the Form question in the recipient's clothes: when they open it, do they bless it, interrogate it, or build from it. Narrative, Model, Handoff, without a taxonomy lecture.

What was not mockuped (audience-and-offer, business model canvas in full) is named rather than faked. The interaction primitive is proven; those two activities still need their card sequences before anyone calls the set complete.

### Chapter 7 · The humbling of a green checkmark

The markdown contract asked for parser, serializer, projections, and the ready-flip rule, with byte-identical round-trips for hostile fixtures: a canonical spec, a folio index with different frontmatter, and a legacy narrative the system never wrote, with pre-schema keys. Byte-identity fell out of one design decision: parse keeps the original frontmatter block; serialize re-emits it verbatim while untouched, and switches to canonical emit once anything changes. Fifty-four tests, green on effectively the first run. All acceptance items PASS. PR opened before midnight. Cleverness felt available.

At one in the morning a high-effort review fleet turned on the same diff: finders and adversarial verifiers, twenty-eight agents. Sixteen distinct findings; ten after verification; seven confirmed data-integrity bugs. The worst deserves its own sentence. A UTF-8 BOM, the invisible byte Windows editors love, made the parser treat an entire valid spec as body text, and the next save would have written a second frontmatter block on top of the real one, silently demoting title, status, and acceptance to prose.

Also confirmed: corrective edits that matched the normalized value never reached disk; an invalid form value was destroyed by an unrelated checkbox click; NaN broke byte-identity; unterminated frontmatter duplicated stale text; a file could claim ready with open boxes; CRLF came back mixed; the Full projection quietly dropped preamble content, which for a projection named Full is a philosophical problem as much as a technical one.

All fixable findings were fixed with a regression test each: 68 tests green, typecheck clean, review response posted. The one deliberate non-change (a package-manager version pin) was called out for a conscious merge rather than buried. The lesson outlives the shift: a green first run is a hypothesis, not a verdict. Five hours of latent data loss wore a green checkmark comfortably. The review fleet cost on the order of 843,000 tokens and was worth every one.

### Chapter 8 · Operations notes, told on myself

Three process stories belong in the record because they will recur.

**Timestamps were fabricated, twice.** Early log headings estimated how long the work felt rather than reading the clock. The work runs perhaps twenty times faster than the human-shaped schedule it was planned against. Both instances were corrected with correction notes left visible. A truthfulness bug is a truthfulness bug even when it flatters no one.

**PowerShell 5.1 ate typography.** One shell-based edit turned dashes and middots into mojibake. Rewrote clean; dedicated file tools or explicit UTF-8 IO only. The rule sits beside the headless-Chrome flags that actually work and the package-manager quirks that cost twenty minutes.

**The clock lied mechanically.** A timer armed against a shell `date` that silently ignored timezone fired early (UTC arithmetic on a machine that answers in UTC when TZ is set). Caught by checking a second clock. Re-armed against honest arithmetic. On this machine: trust one clock, and read it every time.

**Pacing an overnight shift is a real design problem.** Floors fell in half an hour; the clock still owned the deadline. The shape that worked: deepen in passes (iterate mockups against their own critiques, review the code, extract the dark theme, write the vocabulary doc), log with real times, stage the report skeleton through the night, true it up against the final state of the world before render. Anything that happened after drafting began is either in the report or in the log.

### Chapter 9 · Why this report is long on purpose

A status dump of the same night would fit on two pages: six notes, three concepts, two PRs, sixty-eight tests. That dump would not force the thinking that made Concept C useful in death, or make the BOM bug memorable, or leave pen room under the questions that actually block tomorrow. The essay is the work product for a human who was asleep while the agents ran. Length here is not padding; it is the cost of being able to decide without re-entering the terminal.

OpenBook's public default still allows short reports when the work is small. Mirror Factory mornings, when the night has substance, prefer this shape: sixty-second first, then chapters, then a short pen page. The anti-pattern is shrinking a rich night into a brief to look efficient. This example is the quality bar for that preference.

## What's next

### 1. [?] With the Library in the center and the Journal on the right, where does a Document or Folio open?

Replace the center, split it, or displace the Journal? This blocks the shell re-spec (whose acceptance criteria still encode the pre-kickoff layout). It also decides whether the six-state shell contract survives or doubles.

### 2. [?] Should Sessions carry acceptance criteria from goal intake ("what does done look like"), checked at close?

It fell out of the worksheet design uninvited. It expands what a Session is. Yours to bless or refuse.

### 3. [?] Is the arrangement-weights vocabulary right: decisions first, recency, trail affinity, kind mix?

Concept B makes reweighting real with these four. If the labels should be plainer for non-technical readers, rename them now.

### 4. [?] Do you buy A and B as two states of one Library surface (arrival and ask), with C as a by-time lens only?

If one concept should win outright, say which and the next shift consolidates.

### 5. [?] Are resume cues ("you were checking the overage math") worth the session-state memory, or is a wrong cue worse than none?

If yes, say so knowing the UI must stay calm; if no, cut them before they ship as noise.

## What we learned

- Critique-then-iterate beats getting it right on the first mockup; research notes are the linter. The duplication bug in Concept A and shouting buttons in Concept B were both caught by rules written two hours earlier.
- A second theme is a free audit; render both themes on every surface, first pass, always.
- Review-after-green is non-negotiable; confidence and latent data loss coexist. See chapter 7.
- Build the wrong thing on purpose when it teaches; Concept C was known-wrong and still donated parts.
- Constrain the generative, keep the judgment; fixed facet vocabularies beat freeform hallucination.
- Next shift: read the clock, stage the report early, run design review fleets the way code review fleets already run.

## Appendix

### Pull requests

- PR #1 · markdown contract · acceptance 5/5 · 68 tests · self-review response posted
- PR #2 · night-shift design research, Library concepts, worksheets, shell composition

### Artifacts

- Research notes: quiet-ui, calm-density, library-archive-patterns, opendesign, semantic-zoom, markdown-reading
- Library concepts: desk (v3), catalog (v2), ledger (organ donor)
- Worksheets: goal-intake, correction-state, decision-weigh-in, handoff-chooser
- Shell and document: shell-composition (light + graphite), document-doi-arrival
- System docs: DESIGN.md draft, graphite-dark tokens, surrogate vocabulary, DIRECTION.md
- Critiques: one per concept plus addenda; every v1 flaw and iteration recorded
- Receipts: screenshots and test output under the night's assets folder

### Pending human

- Shell task re-spec (blocked on question 1)
- DESIGN.md draft review
- Questions 1–5 above
- Earlier outstanding items still open: vendor production Dewey files; locate the non-Kyle interview transcript for the user-research task

### Sources (primary)

Amber Case, Principles of Calm Technology · Weiser & Brown lineage · Reichenstein/iA · Tufte · Strom-Awn on UI density · Whitelaw, Generous Interfaces · finding-aid interaction studies · Breeding on serendipity in virtual libraries · StackView / Blended Shelf · OpenDesign · NN/g Progressive Disclosure · Bederson & Hollan, Pad++ · Furnas fisheye lineage · Baudisch et al., Keeping Things in Context · Typora · Tufte CSS · Butterick, Practical Typography. Full URLs in each research note.

---

*OpenBook example. Redacted and reshaped from a real morning report for format demonstration. Not a live delivery artifact.*

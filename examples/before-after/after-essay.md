## Cover

**Title:** I made you something called OpenBook
**Subtitle:** The night the format, the checker, and the wipe all had to earn their keep
**Length:** Essay
**Author:** Your coding agent
**When:** 2026-07-12 · overnight shift

## Two Minutes

**You are holding the product.** OpenBook is a Markdown report kit for long agent runs: a two-minute lead, decisions a pen can answer, receipts underneath. The wall of terminals from this same night is still one drag to your left.

**The build is real, with one confession.** Format contract, structural checker, warm-paper renderer. *Draft one opened with nine statistics early and said nothing.* The wipe handle stole an hour mid-shift. Dead ends stay visible. **I may cut, but I may never invent.**

**Chapter pens below, then a short index.** Whether this becomes normal for your agents is the real ask. Brief stays the morning default unless you name otherwise. Receipts stay mechanical unless you relax them.

## Narrative

### Chapter 1 · The contract

Long runs were ending as transcript walls. The brief was to leave a format a human could trust: exact headings, self-contained decisions, an appendix for evidence. I wrote `formats/report.md` with three earned lengths (Brief, Standard, Essay), truthfulness rules that treat failures as content, and a ban on invented timestamps.

The checker is the seatbelt. `scripts/check_report.py` fails missing sections, Briefs that smuggle a Narrative, empty decision blocks, librarian voice violations. At 00:41 draft one failed: Cover carried a statistics grid, and the lede made claims without receipt references. Impressive and empty. The grid moved to the Appendix. Draft two passed with soft warnings. Soft warnings are how the contract teaches without blocking a good night.

### Decision 1 · whether this becomes normal

Should your agents end every long run with a page like this? Adopting costs **one pasted paragraph**. If the transcript behind the wipe serves you better, *say so and I will stand down*.

### Chapter 2 · The renderer

Readable on screen is not the same as readable on paper. `render/report.css` sets warm paper (`#F2EEE5`), Source Serif 4 for body, Manrope for chrome, pen rooms that exist only in print so a human can answer beside the ask. The first render warned that pen rooms clipped at the US Letter margin. Screen overrides were winning because print rules were not last in the cascade. Moving them fixed the PDF. A report that cannot be printed is not a morning object.

Byline, read time, standfirst lede: furniture that earns its ink by orienting a reader who was not in the loop. The renderer never invents content; it only shapes what the agent already wrote.

### Decision 2 · how much greets you by default

This page is an **Essay** because the night earned chapter pens. *Brief* is the default for mornings that are short. *Standard* adds short Narrative without embedding asks. **Bless Brief as default, or name your profile.**

### Chapter 3 · The lost hour

The marketing surface is a wipe between the transcript and this report. At 02:14 the handle surrendered drag to the iframe underneath. Pointer events on panes, capture on the handle, both candidates. At 02:41 it still dropped at the pane boundary. At 03:02, `setPointerCapture` on the handle and inert panes during drag. Fixed at 03:19. One hour gone.

That hour is in the before pane on purpose. The product rule is the same as the night's rule: **I may cut, but I may never invent.** Logging a lost hour is how the report stays less optimistic than the transcript.

`build_demo.py` regenerated panes. Scroll sync held. Vitest: three files, forty-one tests. Final checker at 06:12: pass, zero warnings. Commit message named the wedge: format, checker, renderer, demo.

### Decision 3 · what counts as a receipt

Strict rule proposed: every claim in the story traces to a receipt I **extracted mechanically**, never one I paraphrased. *Slower to write, easier to check.* **Confirm or relax.**

## What's next

1. **Decision 1 · whether this becomes normal** - adopt costs **one paste**; stand down if the wall is enough
2. **Decision 2 · how much greets you by default** - **Bless Brief**, or name Standard / Essay
3. **Decision 3 · what counts as a receipt** - mechanical extraction **Confirm or relax**

## What we learned

- **Two minutes is a budget**, not a summary. Whatever does not fit was not the point.
- **A green checkmark is a hypothesis.** The receipt is the evidence.
- **The wall of terminals was never the work.** It was the work's exhaust.
- **Print styles belong last**, or the paper lies.
- **A lost hour named plainly** beats a silent rewrite.

## Appendix

**By the numbers:** 1 format contract · 1 checker · 1 renderer · 3 length profiles · 1 hour lost to a drag handle · 41 tests green · final check 06:12

- **The contract this page obeys:** `formats/report.md` · this file passes `check_report.py` clean
- **The wipe bug, found and fixed:** handle keeps drag from iframes (02:14-03:19)
- **The demoted statistics grid:** first draft, in the transcript at *00:41*
- **Cascade fix:** print styles last so screen cannot break PDF
- **Everything here:** [github.com/mirror-factory/openbook](https://github.com/mirror-factory/openbook) · *steal it tonight*
- *This report describes its own construction. The recursion bottoms out here.*

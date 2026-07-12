## Cover

**Title:** I made you something called OpenBook
**Subtitle:** Same night as the Brief, with the chapters the morning can afford
**Length:** Standard
**Author:** Your coding agent
**When:** 2026-07-12 · overnight shift

## Two Minutes

**I built OpenBook while you were away, and you are reading the product.** Last night's transcript is still behind the wipe. This page is the other option: a report shaped so a long run ends in a story you can skim, decisions you can answer with a pen, and receipts underneath.

**The contract, checker, and renderer shipped.** *My first draft opened with a grid of nine statistics early in the night. Impressive, empty.* Numbers live in the Appendix now. The demo wipe stole an hour while the handle kept surrendering to the page underneath. That hour stays in the transcript, because **I may cut, but I may never invent.**

**Three decisions are yours.** Whether this becomes how your agents report, whether Brief stays the morning default, and whether receipts stay mechanically extracted.

## Narrative

### The contract

I wrote `formats/report.md` as the load-bearing file: three length profiles, decision blocks a human can answer without opening the transcript, truthfulness rules that treat dead ends as content. The checker, `scripts/check_report.py`, fails any report that cheats the shape. Draft one failed for putting a statistics grid on the Cover and for lede claims without receipts. Draft two passed with warnings about byline and pen-room depth. Those warnings were the point. The seatbelt works when it bites.

### The renderer

Warm paper lives in `render/report.css`: Source Serif 4 for the body, pen rooms that stay print-only, a masthead that names author, when, and read time. The first PDF clipped pen rooms at the Letter margin because screen overrides were winning the cascade. Moving print styles last fixed it. A report that looks right on screen and wrong on paper is not finished.

### The lost hour

The before/after wipe demo kept surrendering the drag to the iframe underneath the handle. Pointer events on the panes, capture on the handle, both. From 02:14 to 03:19 the handle dropped at every pane boundary. `setPointerCapture` and inert panes during drag closed it. One hour gone, logged, not rewritten as a victory lap. Then `build_demo.py` regenerated the panes, scroll sync held, and the final checker pass at 06:12 was clean.

## What's next

### Decision 1 · whether this becomes normal

Should your agents end every long run with a page like this? Adopting costs **one pasted paragraph**. If the transcript behind the wipe serves you better, *say so and I will stand down*.

### Decision 2 · how much greets you by default

This page is a **Standard**. *Brief* is the morning default; *Essay* is for nights that earn chapters with pens. **Bless Brief as default, or name your profile.**

### Decision 3 · what counts as a receipt

Strict rule proposed: every claim in the story traces to a receipt I **extracted mechanically**, never one I paraphrased. *Slower to write, easier to check.* **Confirm or relax.**

## What we learned

- **Two minutes is a budget**, not a summary. Whatever does not fit was not the point.
- **A green checkmark is a hypothesis.** The receipt is the evidence.
- **The wall of terminals was never the work.** It was the work's exhaust.
- **Print styles belong last in the cascade**, or the PDF lies about the page.

## Appendix

**By the numbers:** 1 format contract · 1 checker · 1 renderer · 3 length profiles · 1 hour lost to a drag handle · 41 tests green

- **The contract this page obeys:** `formats/report.md` · this file passes `check_report.py` clean
- **The wipe bug, found and fixed:** the handle now keeps the drag from iframes (02:14-03:19)
- **The demoted statistics grid:** first draft, in the transcript at *00:41*
- **Cascade fix:** print styles moved last so screen overrides cannot break PDF
- **Everything here:** [github.com/mirror-factory/openbook](https://github.com/mirror-factory/openbook) · *steal it tonight*

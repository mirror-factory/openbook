# OpenBook Report Format

**Load this file** when writing an end-of-run handoff for a human who was not in the loop.

**One line:** A narrative memo with a sixty-second lead, chaptered story, ranked decisions with room to answer, and receipts underneath.

---

## Required section headings (exact H2 titles)

Use these headings exactly (checker matches them):

1. `## Cover`
2. `## The sixty-second version`
3. `## Narrative`
4. `## What's next`
5. `## What we learned`
6. `## Appendix`

Optional H3 chapters under Narrative (e.g. `### Chapter 1 · …`).

---

## Section order and jobs

### Cover

What this is, who wrote it, for whom, when, and headline stats. Title + one subtitle. No padding.

### The sixty-second version

The whole run in one short read. Most important item first. A reader who stops here should still know what happened and what needs them.

### Narrative

Chaptered prose. Bezos-memo energy: detailed, honest, story-shaped. Include failures and dead ends. Length is **earned**, never padded.

**Formatting is load-bearing, not decoration.** Long-form field-tested rules:

- One idea per paragraph. A paragraph that compresses three parallel items into prose is a list wearing a costume; give it bullets or numbers.
- **Bold the lead** of a paragraph or bullet when a scanning reader should catch it (textbook and workbook practice: the bold layer alone should tell the chapter's story).
- Use ordered lists when order carries meaning, unordered when it does not, and tables only for genuinely tabular facts.
- Italics for emphasis and titles, sparingly; emphasis everywhere is emphasis nowhere.

**Decisions live where their context lives.** In a long report, a decision block (`### N. [?] …` or `### [?] …`) may be embedded at the end of the chapter that explains it — the renderer gives it a pen room wherever it appears. Human memory is the reason: by the time a reader reaches a trailing question list, chapter three is gone. If you embed, What's next becomes a short **index** of the embedded decisions (one line each, with the chapter that holds it), not their home.

### What's next

Ranked decisions for the human — either the decisions themselves (short reports) or a one-line index of decisions embedded in their chapters (long reports). Each full decision block:

- One plain-language question
- One short context line if needed
- **Self-contained**: answerable from the block alone, with no references to things introduced elsewhere and not restated here
- Room to answer (in Markdown: a blank block or `<!-- pen room -->`; in PDF: **generous** pen room under each ask — a human answers in ink, and cramped pen room reads as not really wanting an answer)
- Optional `[?]` marker on open decisions

**Rules:** prefer ≤5 questions; one ask per block; no jargon stacks; no laundry-list "bless or reverse" dumps.

**Plain-reference rule (whole document):** never let an internal ID be the only name for a thing. Ticket numbers, PR numbers, and shorthand codenames mean nothing on paper; say what the thing is in words ("the review workflow change"), with the ID in parentheses at most. A reader with a pen has no terminal to look it up in.

### What we learned

Short. Portable to the next run. Bullets are fine.

### Appendix

Receipts: PRs, commits, tests, paths, ledgers, sources, PENDING-HUMAN. Flat and honest.

---

## Length profiles

| Profile | Guidance |
|---------|----------|
| **Default (public OpenBook)** | Length earned by substance. Short is fine when the work is small. Always keep the sixty-second layer. |
| **Long-essay morning** (Mirror Factory) | When the night has substance, prefer a **chaptered essay of 15+ pages** in PDF. Do **not** collapse a rich night into a 2–4 page stub to look efficient. A Georgia letter essay with pen room is the quality bar. |

There is **no maximum** page count. The anti-pattern is a thin status dump, not a long essay.

---

## Modes

### Full report

One document with all six sections. Default for a single agent or an editor-assembled night.

### Section contribution

A multi-agent contributor may write a Narrative-shaped section in their own voice for an editor to assemble. Still tell the truth; still leave receipts. The editor may cut for length and flow, never rewrite voice or soften failures. Missing sections are named, not invented.

---

## Truthfulness

- Report only what happened.
- Dead ends are content.
- Do not inflate stats or invent timestamps.
- Human-dependent items stay explicitly unresolved.
- Delivery failures (e.g. PDF not uploaded) must be loud, never quiet.
- **Audit before handoff.** A long run's report accretes stats that go stale as the run continues (counts, totals, lists of artifacts). Before delivery, verify every number and referenced artifact against ground truth — ideally with fresh eyes that did not write the report. One stale count erodes trust in every honest sentence around it.

---

## Print / PDF

When rendering for paper or e-ink:

- Use OpenBook `render/` (Georgia essay CSS + frameless template + `scripts/render_report.py`)
- US Letter; margins ≥2.6cm; page numbers; pen room under decisions
- Grayscale-safe figures with captions
- **Never** browser-print a `file://` tab (no Chrome date/URL footers)

---

## Anti-patterns

- Status dump / PR laundry list with no story
- Confident summary with no appendix receipts
- Shrinking a rich night into 2–4 pages to look efficient
- More than five fuzzy decision questions
- Jargon that earns a handwritten "What?"
- Browser-chrome PDFs
- Softening failures in editorial assembly

---

## Minimal skeleton

```markdown
## Cover

**Title:** …
**Author:** …
**For:** …
**When:** …
**Stats:** …

## The sixty-second version

…

## Narrative

### Chapter 1 · …

…

## What's next

### 1. [?] …

…

### 2. [?] …

…

## What we learned

- …

## Appendix

- …
```

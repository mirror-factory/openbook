# OpenBook Report Format

**Load this file** when writing an end-of-run handoff for a human who was not in the loop.

**One line:** A narrative memo with a sixty-second lead, chaptered story, decisions where their context lives, a short closing index with any cross-cutting asks, and receipts underneath.

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

**Hybrid decisions (long reports):** Chapter-owned asks live at the **end of the chapter that explains them**, as decision blocks (`### N. [?] …`). The renderer gives each block a generous pen room wherever it appears. Human memory is the reason: a trailing-only question list is a memory test the reader did not sign up for. Prefer answering while the chapter is still warm.

### What's next

**Hybrid close** (preferred for long reports):

1. An **index** of chapter-embedded decisions (one plain line each, naming the chapter that holds the pen room).
2. Optional **cross-cutting** decision blocks for asks that span the whole night (company-wide, not owned by one chapter). Same block rules as below. Prefer ≤5 total across chapter embeds + cross-cuts.

**Short reports** may keep all decisions trailing here (no embeds required). Still use self-contained plain-language blocks.

Each full decision block (in a chapter or as a cross-cut):

- One plain-language question
- One short context line if needed
- **Self-contained**: answerable from the block alone; restate anything the reader needs (no "see chapter 3")
- Room to answer (in Markdown: a blank block or `<!-- pen room -->`; in PDF: **generous** pen room — cramped pen room reads as not really wanting an answer)
- Optional `[?]` marker on open decisions

**Rules:** prefer ≤5 questions total; one ask per block; no jargon stacks; no laundry-list "bless or reverse" dumps.

**Plain-reference rule (whole document):** never let an internal ID be the only name for a thing. Ticket numbers, PR numbers, and shorthand codenames mean nothing on paper; say what the thing is in words ("the markdown contract pull request"), with the ID in parentheses at most. A reader with a pen has no terminal to look it up in.

### What we learned

Short. Portable to the next run. Bullets are fine. Not a pen section.

### Appendix

Receipts: pull requests, commits, tests, paths, ledgers, sources, PENDING-HUMAN. Flat and honest. Name artifacts in words first; IDs in parentheses at most.

---

## Length profiles

| Profile | Guidance |
|---------|----------|
| **Default (public OpenBook)** | Length earned by substance. Short is fine when the work is small. Always keep the sixty-second layer. Trailing-only decisions are OK when the report is short. |
| **Long-essay morning** (Mirror Factory) | When the night has substance, prefer a **chaptered essay of 15+ pages** in PDF with **Hybrid** decisions (chapter pens + closing index and any cross-cuts). Do **not** collapse a rich night into a 2–4 page stub. A Georgia letter essay with pen room is the quality bar. |

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
- US Letter; margins ≥2.6cm; page numbers; pen room under decisions (chapter and cross-cut)
- Grayscale-safe figures with captions
- **Never** browser-print a `file://` tab (no Chrome date/URL footers)

---

## Anti-patterns

- Status dump / PR laundry list with no story
- Confident summary with no appendix receipts
- Shrinking a rich night into 2–4 pages to look efficient
- **Trailing-only decisions on a long report** (forces the reader to remember chapter three from the back of the essay)
- Bare internal IDs as the only name for a thing (earns a handwritten "What?")
- Decision blocks that require flipping back to earlier chapters to answer
- More than five fuzzy decision questions
- Jargon that earns a handwritten "What?"
- Browser-chrome PDFs
- Softening failures in editorial assembly

---

## Minimal skeleton (short report)

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

## What we learned

- …

## Appendix

- …
```

## Long-report skeleton (Hybrid)

```markdown
## Cover

…

## The sixty-second version

…

## Narrative

### Chapter 1 · …

…

### 1. [?] Plain-language chapter ask?

One self-contained context line. Restate the choice in words.

### Chapter 2 · …

…

### 2. [?] Another chapter ask?

…

## What's next

Chapter decisions (pen rooms above):

1. … (end of chapter 1)
2. … (end of chapter 2)

### 3. [?] Cross-cutting ask that spans the night?

Self-contained context. No chapter flip required.

## What we learned

- …

## Appendix

- …
```

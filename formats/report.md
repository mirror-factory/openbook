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

### What's next

Ranked decisions for the human. Each item:

- One plain-language question
- One short context line if needed
- Room to answer (in Markdown: a blank block or `<!-- pen room -->`; in PDF: pen room under each ask)
- Optional `[?]` marker on open decisions

**Rules:** prefer ≤5 questions; one ask per block; no jargon stacks; no laundry-list "bless or reverse" dumps.

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

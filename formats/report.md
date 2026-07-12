# OpenBook Report Format

**Load this file** when writing an end-of-run handoff for a human who was not in the loop.

**One line:** A readable report with a two-minute lead, the right amount of story for the length you chose, decisions a human can answer, and receipts underneath.

**Public default length: Brief** (~one page). Use Standard or Essay when the work earns more depth.

---

## Required section headings (exact H2 titles)

Declare length near the top of Cover (recommended):

```markdown
**Length:** Brief
```

Allowed values: `Brief` | `Standard` | `Essay`.

### Brief (default)

1. `## Cover`
2. `## Two Minutes`
3. `## What's next`
4. `## What we learned`
5. `## Appendix`

**Do not include `## Narrative` on Brief.** If the two-minute version cannot hold the story, promote to Standard.

### Standard / Essay

1. `## Cover`
2. `## Two Minutes`
3. `## Narrative`
4. `## What's next`
5. `## What we learned`
6. `## Appendix`

Optional H3 chapters under Narrative (e.g. `### Chapter 1 · …`).

---

## Length profiles

| Profile | Target (letter PDF) | Story | Decisions | When to use |
|---------|---------------------|-------|-----------|-------------|
| **Brief** (default) | ~1 page | Prose lede carries the story; **no Narrative section** | Trailing only; prefer ≤3 asks | Most coding-agent handoffs; small or medium runs |
| **Standard** | ~2–4 pages | Two-minute as abstract; Narrative is short chapters or continuous prose | Trailing, or light Hybrid if two+ chapter-owned asks | Multi-hour runs with a real story but not an overnight essay |
| **Essay** | 10–15+ pages when earned | Two-minute as abstract; full chaptered Narrative | **Hybrid:** chapter pens + closing index + optional cross-cuts | High-substance nights; Mirror Factory morning preference |

Shared at every length: Cover, two-minute, What's next, What we learned, Appendix. Plain-reference and self-contained asks. Length is **earned**, never padded.

There is **no maximum** page count. Padding a Brief into an essay, or shipping a status dump as any length, are both anti-patterns.

---

## Section order and jobs

### Cover

Title + one subtitle. Who wrote it, when. Include `**Length:** …` when known. No padding.

Prefer labeled fields:

```markdown
**Title:** …
**Subtitle:** …
**Length:** Brief
**Author:** …
**When:** …
```

Optional machine-readable `**For:**` is ignored in the rendered byline (a document describing its audience to its audience is chrome).

**Do not put `**Stats:**` on Cover.** Numbers belong in Appendix as `**By the numbers:** …`.

The renderer builds a masthead: title, dek, byline (`Author · When · N-min read`), then a short rule into the body.

### Two Minutes

A reader who stops here should still know what happened and what needs them.

**Brief:** continuous prose, 3–6 paragraphs, ~150–350 words. First sentence is the bottom line. **No bold leads** — the writing carries emphasis. No bullets. End with one plain sentence naming what needs the reader, pointing at the decisions below. This IS the narrative at Brief length.

**Standard / Essay:** an abstract of the Narrative. Maximum 3 paragraphs. Bold leads allowed, maximum one per paragraph, one short sentence each. If the abstract needs a fourth paragraph, the Narrative is under-summarized, not the abstract under-sized.

### Narrative

**Brief:** forbidden. Fold into the two-minute version or declare Standard.

**Standard:** 2–5 short chapters or one continuous narrative, *prose-first*. Bullets only for genuinely parallel facts. A Narrative that is only bullets fails review. Include failures and dead ends that matter.

**Essay:** Chaptered prose. Bezos-memo energy: detailed, honest, story-shaped. Include failures and dead ends.

**Formatting is load-bearing, not decoration** (Standard and Essay especially):

- One idea per paragraph. Parallel items become lists.
- **Bold the lead** when a scanning reader should catch it — one short sentence, not a dense bold run. (Brief: do not use bold leads.)
- Ordered lists when order matters; tables only for tabular facts (renderer uses booktabs-style rules).
- Italics sparingly.
- Flush-left body; aim for a readable measure (~65 characters). Do not pad lines to justify.

**Hybrid decisions (Essay; optional light use on Standard):** Chapter-owned asks live at the **end of the chapter that explains them** (`### Decision N · short handle`). The renderer gives each block a generous pen room in print. Human memory is the reason: a trailing-only list on a long essay is a memory test the reader did not sign up for.

### What's next

**Brief / Standard (trailing):** Ranked decision blocks here. Prefer ≤3 on Brief, ≤5 on Standard.

**Essay (Hybrid close):**

1. An **index** of chapter-embedded decisions (one plain line each, naming the chapter).
2. Optional **cross-cutting** decision blocks for asks that span the whole run. Prefer ≤5 total across embeds + cross-cuts.

Each full decision block:

```markdown
### Decision N · short handle

Plain-language question. One context line. Self-contained.
```

- One plain-language question as the first paragraph
- One short context line if needed
- **Self-contained**: answerable from the block alone
- Room to answer in print (PDF: generous pen room; screen: no pen chrome)

Legacy `### N. [?]` headings still parse with a deprecation warning; prefer `### Decision N · …`.

**Rules:** one ask per block; no jargon stacks; no laundry-list dumps.

**Plain-reference rule (whole document):** never let an internal ID be the only name for a thing. Say what it is in words; ID in parentheses at most.

### What we learned

Short. Portable to the next run. 1–3 lines on Brief. Bullets are fine. Not a pen section.

### Appendix

Receipts: pull requests, commits, tests, paths, sources, PENDING-HUMAN. Flat and honest.

**Extracted, never paraphrased.** Appendix lines are copied from the run (commands, tallies, titles, paths). Softening a failure count or inventing a cleaner summary is forbidden. See [docs/receipts.md](../docs/receipts.md).

Optional machine file: `receipts.jsonl` beside the report. `scripts/render_report.py` folds those records into the Appendix on render. Prefer the jsonl (or identical Markdown bullets) over rewriting the same facts in warmer prose.

Optional leading line:

```markdown
**By the numbers:** 6 research notes · 2 pull requests · 68 tests green
```

Brief: a few receipt lines is enough. Every numeric claim in the two-minute version should be findable here.

---

## Modes

### Full report

One document with the required sections for its length. Default for a single agent or an editor-assembled night.

### Section contribution

A multi-agent contributor may write a Narrative-shaped section in their own voice for an editor to assemble (Standard/Essay). Still tell the truth; still leave receipts. The editor may cut for length and flow, never rewrite voice or soften failures. Missing sections are named, not invented.

---

## Truthfulness

- Report only what happened.
- Dead ends are content.
- Do not inflate stats or invent timestamps.
- Human-dependent items stay explicitly unresolved.
- Delivery failures (e.g. PDF not uploaded) must be loud, never quiet.
- **Audit before handoff.** Verify counts and artifacts against ground truth before delivery, ideally with fresh eyes.

---

## Print / PDF

- Use OpenBook `render/` + `scripts/render_report.py`
- US Letter; margins ≥2.4cm; page numbers; pen room under decisions (print only)
- Grayscale-safe figures with captions
- **Never** browser-print a `file://` tab

---

## Anti-patterns

- Status dump / PR laundry list with no story
- Confident summary with no appendix receipts
- Declaring **Brief** while shipping chaptered essay length (or the reverse without cause)
- **A Brief with a Narrative section** (fold into two-minute lede or promote to Standard)
- **Stats strip thinking:** leading with numbers instead of the story
- Shrinking a rich Essay night into a stub to look efficient
- **Trailing-only decisions on an Essay** (forgot-by-the-end)
- Bare internal IDs as the only name for a thing
- Decision blocks that require flipping back to earlier chapters
- More than five fuzzy decision questions
- Jargon that earns a handwritten "What?"
- Browser-chrome PDFs
- Softening failures in editorial assembly

---

## Skeleton — Brief (default)

```markdown
## Cover

**Title:** …
**Subtitle:** …
**Length:** Brief
**Author:** …
**When:** …

## Two Minutes

(3–6 paragraphs of continuous prose. First sentence is the bottom line.
No box, no bold leads, no bullets. This IS the narrative at Brief length.)

## What's next

### Decision 1 · short handle

Plain-language question. One context line. Self-contained.

## What we learned

- … (1–3 lines max)

## Appendix

**By the numbers:** 6 research notes · 2 pull requests · 68 tests green
- receipts …
```

## Skeleton — Standard

```markdown
## Cover

**Length:** Standard
…

## Two Minutes

…

## Narrative

### …

…

## What's next

### Decision 1 · …

…

## What we learned

- …

## Appendix

**By the numbers:** …
- …
```

## Skeleton — Essay (Hybrid)

```markdown
## Cover

**Length:** Essay
…

## Two Minutes

…

## Narrative

### Chapter 1 · …

…

### Decision 1 · chapter ask

…

### Chapter 2 · …

…

### Decision 2 · another chapter ask

…

## What's next

Chapter decisions (pen rooms above):

1. … (end of chapter 1)
2. … (end of chapter 2)

### Decision 3 · cross-cutting ask

…

## What we learned

- …

## Appendix

- …
```

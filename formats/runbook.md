# OpenBook Runbook Format

**Load this file** when the run's deliverable is a system a human will operate, not a story a human will read once. A report tells them what happened; a runbook tells them what to do, next month, when they have forgotten everything.

**One line:** An operations manual with a sixty-second orientation, the buttons and what they cost, step-by-step procedures, and what to do when it looks wrong.

Declare it near the top of Cover:

```markdown
**Format:** Runbook
```

---

## Required section headings (exact H2 titles)

1. `## Cover`
2. `## The sixty-second version`
3. `## The buttons`
4. `## Procedures`
5. `## When it looks wrong`
6. `## Appendix`

No `## What's next` and no `## What we learned`: a runbook asks nothing and is not a retrospective. If the system also needs decisions from the reader, ship a Report beside it; do not blend the genres.

---

## Section order and jobs

### Cover

Same masthead fields as the Report: Title, Subtitle, Author, When, plus `**Format:** Runbook`. No Stats. The subtitle should say what system this operates ("the staging environment, the refresh, and the release").

### The sixty-second version

Orientation, not summary: what this system is, what it is for, and when a reader would open this document. Continuous prose, no bullets, no bold leads. A reader who stops here should know whether this runbook is the one they need.

### The buttons

Every action the operator can take, one short block each, before any procedure. For each button:

- **Bold lead naming the button** and where it lives ("refresh-staging, in the repository's Actions tab").
- What it does, in one or two sentences.
- What it costs or risks, plainly ("reads production, never writes to it"; "this one touches production and asks for a typed confirmation").

The buttons section is the map; procedures are the routes. A reader skimming only this section should know what is safe to press.

### Procedures

One `### ` heading per procedure, named by intent ("Review a new feature against your data", not "Workflow dispatch instructions"). Numbered steps, one action per step, each step observable: say what the reader should SEE when the step worked ("the run's final step prints the row counts"). Prose between steps only when a step needs a why.

Order procedures by frequency: the everyday loop first, the rare ceremony last.

### When it looks wrong

Symptom-first, not system-first: each entry opens with what the operator observes ("the staging app shows an empty library"), then the first move, then where the deeper truth lives (a log, a run page, a doc). Prefer 3 to 6 entries covering the failures that actually happen. This section is why the runbook gets opened at 11pm; write it for that reader.

### Appendix

Where everything lives: repositories, workflow names, file paths, credential locations (locations, never values). Receipts for claims the runbook makes ("verified on run N").

---

## Voice and formatting

- Load a style (Librarian pairs well). Warmth through specificity; no hype, no fear.
- **Second person, present tense.** "You press Run; the workflow reads production." The reader is doing, not reviewing.
- Plain-reference rule applies: never let an internal ID be the only name for a thing.
- Numbered lists carry procedures; everything else is prose. No pen rooms: nothing here is a question.
- Length is whatever the system needs, and no longer. A runbook that reads like an essay has smuggled a report into the wrong genre.

---

## Truthfulness

- Describe the system as it IS, not as designed. If a step is flaky, say so and say what to do about it.
- Every "you should see X" must be something the author actually saw.
- Unfinished corners are named in place ("this path exists but has not been exercised"), never hidden in an appendix.
- When the system changes, the runbook is wrong until updated; date the Cover and treat staleness as a defect.

---

## Print / PDF

Same pipeline as the Report (`scripts/render_report.py`): the masthead, section rendering, and typography all apply. Decision pen rooms never appear because runbooks contain no decision blocks.

---

## Anti-patterns

- A retrospective wearing procedures (that is a Report; write one)
- Buttons documented only inside procedures, so the map does not exist
- Steps without observable outcomes ("run the workflow" with no "and you should see")
- System-first troubleshooting ("the migration baseline mechanism" instead of "the app shows an empty library")
- Asking the reader questions (no pen rooms; decisions belong in a Report)
- Values of secrets anywhere, ever

---

## Minimal skeleton

```markdown
## Cover

**Title:** …
**Subtitle:** …
**Format:** Runbook
**Author:** …
**When:** …

## The sixty-second version

…

## The buttons

**button-name, where it lives.** What it does. What it costs.

## Procedures

### Do the everyday thing

1. …; you should see …
2. …

## When it looks wrong

**You see X.** First move. Where the deeper truth lives.

## Appendix

- …
```

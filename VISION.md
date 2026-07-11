# OpenBook — Vision

**One line:** A small set of writing contracts that make long-horizon agent work readable to humans who don't live in the terminal.

**Don't trust the agent. Read the OpenBook.**

---

## Why this exists

Coding agents and long-horizon agents are getting good at *doing* work. They are still bad at *leaving a trail a human can trust*.

What usually comes back is a wall of logs, a status dump, or a confident summary with no receipts. Builders can dig. Executives, operators, clients, and non-technical collaborators cannot. The failure mode is always the same: **output without a trustworthy narrative**.

OpenBook starts from a different bet:

> Trust is not a vibe. Trust is a document shape — a story a human can skim, decisions they can answer, and receipts they can verify.

We already know this shape works in private. Overnight agents write narrative morning reports. Humans annotate them with a pen. Those marks become the next day's work. Multi-agent nights only hold together when every writer shares one communication contract.

OpenBook is that contract, extracted and open-sourced — so any coding agent, in any stack, can speak clearly to a human.

---

## What OpenBook is

OpenBook is **not** an agent framework, a runtime, a wiki product, or a chat UI.

It is a **format kit**: opinionated Markdown contracts that agents load and humans read.

Three families of artifact, one principle:

| Family | Job |
|--------|-----|
| **Reports** | End of a long run: what happened, what matters, what needs a human |
| **Specs** | Before and during work: claim, decisions, acceptance — kept current |
| **Styles** | Thin voice cards that keep agent prose human and consistent |

The principle across all three is **semantic zoom**: the representation changes with attention, not just the font size. A sixty-second page is not a shrunk novel. A Summary lens is not a truncated Full. Every level is a real read for a real moment.

### Utility first, values as behavior

Open-sourcing OpenBook promotes how we work: clarity over cleverness, explicit tradeoffs, no inflated scope, receipts required, failures shown. Those values must show up in **constraints and examples**, not in manifesto length.

The public repo should feel like a tool you can use tonight. Philosophy lives in this document; the README stays ruthlessly practical.

### The brand

**OpenBook** leans into two ideas at once:

1. **Library** — knowledge work has shelves, catalogs, and readable volumes; agents should leave books, not scraps.
2. **Open book** — transparency as default. The agent is not a black box you are asked to trust. It is a volume you can open.

The metaphor is brand. The product is the contracts.

---

## Who it is for

### Primary readers (the humans who must believe the work)

- Founders and operators reviewing overnight or multi-hour agent runs
- Non-technical collaborators using coding agents (capable tools, indigestible output)
- Executives who need decisions and risk, not terminal archaeology
- Anyone who annotates a brief with a pen, a comment, or a "yes / not yet / design session"

### Primary writers (the agents)

- Claude Code, Cursor, Codex, and similar coding agents on long-horizon tasks
- Multi-agent setups where several workers must compose into one human read
- Internal ops or librarian agents that already write narrative memos

### Secondary audience (distribution)

- Builders on X, HN, and Discord who will steal a good format overnight if it makes their agents look trustworthy

**Adoption tension (named on purpose):** builders install it; managers and collaborators feel the value. That means zero-friction install is non-negotiable. If it is not pasteable into an existing workflow, it will be admired and unused.

OpenBook succeeds when a non-builder can finish coffee with a clear picture, and a builder can verify every claim from the appendix.

---

## The problem, precisely

Long-horizon agent work creates four communication failures:

1. **Status without story** — lists of PRs and checkmarks that do not answer "so what?"
2. **Story without receipts** — fluent prose that cannot be audited
3. **Many writers, no shared shape** — three agents, three dialects, one exhausted human
4. **Unreadable delivery** — the report arrives as a Discord `.md` attachment or a raw link; the human downloads it, opens an editor, maybe finds a reader — and often never finishes

Existing tools optimize for the builder's loop (plan → code → test). Almost nothing optimizes for the **handoff to a human who was not in the loop**.

Observability stacks show traces. Evals show scores. Neither produces a document you would hand to someone with a pen.

OpenBook sits in that gap: **digestible trust** — narrative enough to think with, structured enough to verify, short enough to finish, and eventually **easy enough to open**.

---

## Design principles

1. **Narrative memo, not status dump.** Prose forces honest thinking. A question raised early is answered later without the reader asking.
2. **Layering is how you get both comprehensive and readable.** Sixty-second first. Decisions next. Story optional. Appendix for receipts.
3. **Dead ends are content.** Do not inflate. Do not paper over missing sections. Say what fought back.
4. **Decisions are first-class.** Ranked questions with room for a human answer — pen, comment, or reply. The report is a session surface, not a monologue.
5. **Receipts live underneath, never instead.** Every important claim has a file, PR, screenshot, or log behind it. Flat and honest beats clever graph syntax in v0.
6. **One contract, many voices.** Multi-agent nights share structure; each contributor keeps their voice.
7. **Editor may cut, never invent.** An assembling editor (human or agent) may shorten and order for flow. It must not rewrite voice, soften failures, invent connective facts, or hide missing sections. Missing sections are named.
8. **Tool-agnostic.** Works with zero proprietary stack. Drop a folder into a repo; point the agent at it.
9. **Screenshotable.** If the sixty-second page and the decision page cannot be shared as images, the format failed the distribution test.
10. **Print-honest when printed.** Letter, serif, margins for handwriting, no browser chrome, grayscale-safe figures.
11. **Small enough to steal.** A useful OpenBook fits in a git clone and a CLAUDE.md paragraph — not a platform install.
12. **Structure is checkable.** Prompt adherence alone will drift on long runs. A tiny structural check before handoff is in scope; a content-judging AI judge is not required for v0.

---

## The three formats

### 1. Reports (the wedge)

The end-of-run document for long-horizon work. **This is v0.** Everything else waits.

**Canonical shape:**

1. **Cover** — what this is, who wrote it, for whom, when, headline stats
2. **Sixty-second version** — the whole run, most important item first
3. **What's next** — ranked decisions the human must make; each one question; room to answer *(placed before deep narrative so "stop here" is real)*
4. **Narrative** — what happened, in order, including failures (optional depth; skip when time is short)
5. **What we learned** — short; portable to the next run
6. **Appendix** — PRs, commits, tests, ledgers, paths, sources

**Hard rules from real annotated morning reports:**

- Prefer fewer, sharper decision questions over laundry lists (target ≤5)
- One decision per block; plain language; no jargon stacks that earn a handwritten "What?"
- Enough whitespace that handwriting or comments do not collide
- Explicit stop-here: many readers should finish after sixty seconds + decisions
- Length is earned, never padded; multi-agent unification must not become a tome by default
- Truthfulness over flattery: fabricated timestamps and quiet delivery failures are bugs

**Light decision markup (optional, parse-friendly):**

- `[?]` — needs a human decision
- `[x]` / answered in follow-up — resolved
- Keep it dumb. No CMS integration required for v0.

**Multi-agent assembly:** each worker writes a section in the same contract; one editor assembles connective tissue, preserves voices, and ships one document. Missing sections are named, not invented. The editor is a bottleneck risk: beauty without integrity is a failed OpenBook.

### 2. Specs (after Report lands)

Contracts for knowledge work and build work that agents and humans share.

**Shape:**

- Frontmatter: status, owner, updated
- Claim (one line)
- Decided bullets
- Acceptance criteria (the definition of done)
- Open questions (explicit)

**Semantic zoom lenses** (representation change, not truncation):

| Lens | Moment |
|------|--------|
| Summary | Ten-second read; the claim and the pulse |
| Brief | Skim sections; enough to steer |
| Full | Working document |
| Source | The bytes; honest |

Specs drift is the enemy. Later: an append-only change ledger so updates stay current without erasing why. Not v0.

### 3. Styles (thin cards)

Reusable voice constraints agents load alongside formats.

Examples:

- **Librarian** — economical, warm through specificity; no hype punctuation; dead ends named plainly
- **Senior engineer** — plainspoken tradeoffs; honest about what fought back
- **Coach** — questions over verdicts; brief; measured

Styles are register as product surface — not entertainment personas.

---

## Enforcement (without becoming a platform)

LLMs drift on long-horizon runs. OpenBook does not rely on goodwill alone.

**v0:** a tiny structural checker (`openbook check` or equivalent script) that verifies required headings and decision-block shape exist before handoff. Fail the check → agent fixes structure → human never sees a broken skeleton.

**Not v0:** semantic grading of prose quality, automatic fact verification against git, or a hosted compliance service.

The checker is a seatbelt. The craft is still in the contract and the examples.

---

## Delivery (getting a human to actually open it)

A perfect report that arrives as an unreadable `.md` download has failed.

**In scope over time:**

| Layer | Job | When |
|-------|-----|------|
| **Frameless render profile** | CSS / print rules for HTML→PDF: no browser chrome, annotation margins, e-ink-safe | with or right after Report v0 |
| **Public URL proxy reader** | `openbook.fyi/<raw-public-markdown-url>` — dumb pipe, no auth, frameless HTML | after the contract is real |
| **Chat "Read" button** | Discord/Slack bot replies with one link into the proxy | later |

**v0 assumption for the proxy:** public Markdown URLs only (raw GitHub, gist, CDN). No private-repo OAuth in the first reader.

OpenBook is still useful as files in a repo before any reader exists. The reader removes friction; it does not define the format.

---

## How someone uses it (without Layers, without our stack)

1. Add the OpenBook folder to a repo (or paste the Report contract into the agent brief).
2. Point the coding agent at it: "At end of long-horizon work, write `REPORT.md` per OpenBook Report. Run the structural check before handoff."
3. Read the sixty-second page and the decisions. Annotate. Route answers into the next brief.
4. Optionally render with the frameless profile for paper or e-ink.

That is the whole install story.

---

## Adjacent work (not competitors for the same job)

| Thing | Job | vs OpenBook |
|-------|-----|-------------|
| **OKF-style knowledge packs** | Stable organizational knowledge for agents | Knowledge *for* agents; OpenBook is handoff *to* humans |
| **skill.md / agent instruction files** | Tell an agent how to act | Action boundaries; OpenBook is how to report back |
| **Observability / evals** | Traces and scores | Machine metrics; OpenBook is human-readable trust |
| **Markdown viewer extensions / generic proxies** | Render `.md` in a browser | Delivery only; no handoff contract |

OpenBook's wedge is **machine → operator handoff**: semantic zoom, explicit decisions, receipts, anti-slop register, frameless consumption.

---

## What success looks like

### Near term (v0)

- A stranger drops the Report kit into Claude Code and gets a better morning read the same day
- Before/after examples that screenshot in thirty seconds (log wall → OpenBook)
- Structural check catches missing sections before a human sees them
- At least one real multi-section assembly example

### Medium term

- Spec + Style packs; frameless reader for public Markdown
- "Wrote an OpenBook" as shorthand the way people say "wrote an ADR"
- Adoption outside our company

### North star

OpenBook becomes a **shared language for agent handoffs**: humans expect it; agents default to it; long-horizon work leaves a paper trail that earns trust without demanding faith.

---

## Non-goals

OpenBook is **not**:

- An agent orchestration framework
- A replacement for eval harnesses, tracing, or observability products
- A wiki host, social graph, or profile network
- A requirement to use Layers, Dewey, reMarkable, or any Mirror Factory system
- A license to write longer documents — layering exists to make *less* mandatory reading
- Brand theater without a boringly useful artifact
- A graph database or knowledge-network product in disguise (relational appendix tagging can wait)

---

## Relationship to Mirror Factory / Layers

OpenBook is born from practice inside Mirror Factory: narrative morning reports, multi-agent night shifts, semantic zoom on specs, and a librarian register aimed at non-technical readers.

That origin is an advantage for **examples and craft**. It is not a dependency for **use**.

Public OpenBook must feel complete without Mirror Factory. If the format later funnels teams toward Layers as a context environment, that is a company outcome — not the README pitch.

---

## Moat (honest)

The format itself will be copied. That is fine.

What compounds:

- Best examples under imperfect conditions (failures shown)
- Clearest defaults and the smallest useful checker
- Reputation for taste and rigor
- Living dogfood from real long-horizon runs

Do not confuse a strong open-source signal with a business. OpenBook creates trust and distribution when it solves a sharp problem so well that people reuse it without needing to admire it first.

---

## Distribution philosophy

Open-sourcing OpenBook is contribution and credibility at once.

Surfaces, in priority order:

1. The Report contract (Markdown in git)
2. One copy-pastable usage path (CLAUDE.md / skill / prompt paragraph)
3. Screenshotable before/after examples
4. Structural checker
5. Frameless render notes, then public reader

Stars are vanity. **Paste-into-prompt adoption** and **reports people actually finish** are the metrics.

---

## Roadmap (intentional sequence)

| Stage | Ship | Why this order |
|-------|------|----------------|
| **v0** | Report contract + one style card + checker + examples + agent install blurb + frameless PDF notes | Acute pain; stealable; proves the category |
| **v0.5** | Multi-agent assembly guide; second example from a parallel-agent night | Composes the screenshot on many desks |
| **v1** | Spec contract + zoom lenses; public Markdown proxy reader | Upstream of the run + delivery friction |
| **Later** | More styles; chat Read button; optional decision harvest; community variants | Grow the language, not the platform |

Resist boiling the ocean. One great report format beats a catalog nobody finishes reading.

---

## The standard we hold ourselves to

A good OpenBook document is one a human can:

1. Understand in sixty seconds
2. Answer in five minutes with a pen or a comment
3. Audit in thirty minutes from the appendix
4. Hand to someone who was not in the session — without a translator
5. Open without a scavenger hunt

If it only impresses the agent author, it failed.

---

## Closing

Agents will keep getting longer horizons. Humans will keep having the same morning.

OpenBook is how those two facts stop fighting: a shared, open, stealable way for agents to leave work that is **trustworthy, digestible, and narratively honest**.

Don't trust the system.  
Make the report trustworthy — and easy to open.

**That's OpenBook.**

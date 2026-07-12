# OpenBook — Requirements

**Title:** OpenBook
**Subtitle:** Agent work, written for humans. The format kit, the reader, and the ambient monitor.
**Status:** Decisions 1–9 resolved by Kyle, 2026-07-11
**Author:** Claude, with Kyle Morrand
**When:** July 11, 2026
**Version:** 0.3 (covers repo v0.1.0 as shipped baseline)

---

## The sixty-second version

Agents got long horizons. Humans still have the same morning. Every response the industry has found to the flood of agent output throttles volume: PR size caps, kill switches, fewer parallel agents. Almost nobody is working on the legibility of what agents hand back. OpenBook is the only bet in that lane: raise the quality of the handoff artifact itself, so a human who was not in the loop can finish coffee with a clear picture and answer what needs answering with a pen.

The product is three surfaces sharing one contract. The **Format Kit** (shipped, v0.1.0) is Markdown contracts agents load and humans read: Brief/Standard/Essay reports with a sixty-second lead, self-contained decision blocks, and receipts in an appendix, enforced by a structural checker and rendered to warm-paper PDF. The **Reader** packages rendering so a report is one link or one command away from readable, never a scavenger hunt through a Discord attachment. The **Local Monitor**, the featured new component, is an ambient display for watching runs in progress: calm instead of chaotic, one glanceable surface replacing a wall of terminals, designed so a bystander can tell how the night is going from across the room.

The monitor is also the format's first software consumer. Standards die when nothing reads them (llms.txt); they stick when downstream tooling makes the structure pay (Conventional Commits). The monitor reads the same decision blocks and run narrative the reports use, which closes that loop.

Success is not stars. It is paste-into-prompt adoption, reports people finish, and the monitor running on a spare display through a real overnight.

---

## 1 · Problem and evidence

**The bottleneck has inverted.** Generation is cheap; review is the constraint. A 2026 study of 1,154 practitioner posts ("An Endless Stream of AI Slop," [arXiv](https://arxiv.org/html/2603.27249v1)) coded the complaints into review friction, quality degradation, and trust erosion. Representative quotes: reviewers feel like "the first human being to ever lay eyes on this code," and "I don't know how you could trust any of it at some point." One team shipped 30 agent PRs a day across six reviewers and concluded the time saved writing was spent reviewing.

**The flood is measurable.** Agents pushed roughly 17M PRs to GitHub in a single month, up from 4M six months earlier; GitHub has published guidance on reviewing agent PRs and floated rate caps ([context](https://www.danilchenko.dev/posts/2026-04-11-github-ai-agents-pull-requests/), [GitHub blog](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/)).

**Oversight decays into rubber-stamping.** Reported telemetry has users approving ~93% of agent permission prompts, with diligence falling as volume rises. Approval UI without comprehension is theater.

**Parallel runs hit a review ceiling, not a compute ceiling.** Practitioner guides converge on 4–8 concurrent worktrees, "above that you're usually bottlenecked on review, not on Claude." Steve Yegge's Gas Town runs 30 Claude instances and frames the entire project around escaping "babysitting terminals" — and answers with more supervising agents. OpenBook answers with better artifacts for the human.

**The run itself is unwatchable.** Today, monitoring a multi-agent night means a desktop tiled with terminals (see the screenshot that started this thread). Existing monitors (ccusage, Claude Code Agent Monitor, Vibe Kanban, Conductor) are metric-dense developer dashboards. Nothing is calm, ambient, or legible to a non-builder.

Four communication failures, precisely (carried from the vision): status without story; story without receipts; many writers with no shared shape; unreadable delivery. The monitor adds a fifth: **unwatchable progress** — the only live view of the work is the builder's own terminal chaos.

---

## 2 · Who it is for

| Persona | Moment | Surface |
|---|---|---|
| **Operator/founder** (Kyle at 7am) | Reviewing an overnight run over coffee | Report (Brief/Essay), Monitor the night before |
| **Non-technical collaborator** | Capable agent tools, indigestible output | Report + Reader; Monitor as ambient awareness |
| **Builder running parallel agents** | 4–8 worktrees, babysitting terminals | Monitor as replacement for the terminal wall |
| **Executive/client** | Needs decisions and risk, not terminal archaeology | Report, screenshotted or printed |
| **The agents themselves** | End of run; during run | Write the formats; emit monitor events |

A caution named honestly: the non-technical viewer of the monitor is a hypothesized persona. All documented pain comes from builders and reviewers. Validate with one or two discovery conversations (Bobby is the named candidate user) before the monitor's scope hardens. See Decision 4.

---

## 3 · Product overview

One contract, three surfaces:

| Surface | Job | Status |
|---|---|---|
| **Format Kit** | Contracts agents load, humans read: reports, styles, checker, render | Shipped v0.1.0 |
| **Reader** | Make opening a report frictionless: render pipeline → public proxy → chat unfurl | render/ shipped; reader packaging next |
| **Local Monitor** | Ambient live view of runs; first software consumer of the format | Concept → this PRD |

The strategic loop: the **format** creates trust at handoff, the **reader** removes friction from opening it, and the **monitor** consumes the format live, justifying its structure the way commitlint justified Conventional Commits. Each surface makes the others more valuable; none requires the others (tool-agnostic, files-first).

---

## 4 · Surface 1: the Format Kit (shipped baseline)

What v0.1.0 contains (receipts: [repo](https://github.com/mirror-factory/openbook), CHANGELOG 0.1.0, 2026-07-11):

- **formats/report.md** — the Report contract. Three length profiles: Brief (~1 page, default; prose lede carries the story, Narrative forbidden), Standard (~2–4 pages, abstract + short Narrative), Essay (long, earned; Hybrid chapter-owned decisions with pen rooms). Required exact H2 headings per profile. Decision blocks as `### Decision N · short handle`, self-contained, plain-reference rule (never a bare internal ID). Truthfulness rules: dead ends are content, no invented timestamps, loud delivery failures, audit before handoff.
- **styles/librarian.md** — voice card: economical, warm through specificity, no exclamation points, no em dashes, failures named plainly.
- **styles/senior-engineer.md** / **styles/coach.md** — alternate voice cards (pager-owner precision; teach-the-next-run).
- **scripts/** — `check_report.py` (length-conditional structural checker: the seatbelt), `render_report.py` (HTML→PDF, never browser-print), `build_demo.py`.
- **render/report.css** — warm paper, Source Serif 4 with Georgia fallbacks, masthead byline with read time, standfirst lede, print-only pen rooms, US Letter, grayscale-safe.
- **examples/before-after/** — one real July 8 night as transcript + Brief + Standard + Essay.
- **docs/** — the live [before/after demo](https://mirror-factory.github.io/openbook/) with the wipe interaction.
- **USE.md** — the paste-into-CLAUDE.md install; **integrations/claude-code.md** for depth.

### Requirements (kit, next increment)

P0 — restyle the demo with the chosen Dragonglass direction, light mode default and night as a toggle; keep the before/after wipe as the marketing hero.
P0 — ship the **/openbook skill** (Decision 7), superseding USE.md. Invoked explicitly as `/openbook [brief|standard|essay]`, described so agents reach for it unprompted at the end of long runs. A skill is the commitlint of this format: generation-side enforcement beats human discipline, and agent authorship makes consistency a prompt problem, not a social contract problem.
P1 — multi-agent assembly guide + a second example from a parallel night (v0.5 per vision roadmap).
P1 — second and third style cards (senior engineer, coach) as thin files.
P1 (v0.5, pulled forward per Decision 9) — receipts hardening: a convention for machine-extracted receipts (commands run, test output paths, diff links) so the appendix is verifiable rather than agent-paraphrased. Research flag: polish can launder slop; a beautiful report that misrepresents the run is worse than a log wall. OpenBook is a legibility layer, not an integrity layer, and should say so — but receipts should be as mechanical as possible.

### Non-goals (kit)

Semantic grading of prose, automatic fact verification against git, hosted compliance service, CMS integration for decision markup. The checker stays a seatbelt.

---

## 5 · Surface 2: the Reader

The vision names the failure: a perfect report delivered as a raw `.md` attachment has failed. The reader is the packaging of what render/ already does.

P0 — **frameless render profile** (shipped in render/, keep hardening): no browser chrome, annotation margins, e-ink safe.
P1 — **easy renderer for agents**: a single command or tiny library an agent can call to produce screen HTML + print PDF from any OpenBook report, suitable for embedding in Layers (this is the "fully formed reader" from the Discord thread: the OpenBook format becomes how Layers presents wiki, specs, and reports to its non-technical audience).
P1 — **public URL proxy reader** (`openbook.fyi/<raw-md-url>`): dumb pipe, public Markdown only, no auth, frameless HTML.
P2 — **chat Read button**: Discord/Slack bot replies to a `.md` attachment with one proxy link.

Non-goals: private-repo OAuth in v1; a hosted wiki; accounts of any kind.

---

## 6 · Surface 3: the Local Monitor (featured)

Repo note (Decision 8): the monitor is built in a separate private repo (openbook-shell) while its future — open source, paid, or part of Layers — stays deliberately open. This section remains its product spec; the public kit stays Markdown-only meanwhile.

### 6.1 Concept

One sentence: **a calm, on-brand ambient display that replaces the wall of terminals with a single glanceable surface showing how the runs are going and what is waiting on a human.**

From the thread: "minimalist, ambient, clean, local" — "game-like observability… minimalist, on-brand, professional clean… packaged and promoted nicely." It is a fragment of the fuller platform the way short-form clips precede the podcast: a flex of design, a daily-driver in Mirror Factory's own workflow, and a marketing surface in one.

Positioning against the field: Cursor 2.0 and the Codex desktop app are building vendor "mission control" for developers; Vibe Kanban and Conductor are interactive orchestration UIs; hobbyist Claude Code monitors are metric-dense dashboards. The monitor's defensible ground is (a) vendor-neutral, (b) legible to non-builders, (c) calm. It is the *spectator* view, not the *operator* console. Where the industry's metaphor is a red-alert NASA control room, this is Apollo-era paper checklists and flight-controller restraint.

### 6.2 Design principles (research-grounded)

1. **Periphery to center** (Weiser & Brown, calm technology). Steady state is wallpaper. Exactly one class of event is allowed to pull attention to center: a pending decision. Everything else informs without demanding.
2. **One pre-attentive signal** (Ambient Orb lineage). A single global element — the paper tone of the surface, or a lamp-like glow (Dragonglass has a signature glow token) — encodes fleet health, readable from across a room without reading anything. Colorblind-safe, no numbers.
3. **Slow refresh is a feature.** Update on the minute, not on the token. Ticker-speed updates recreate the terminal chaos this replaces. An explicit e-ink mode (few refreshes per hour, 1-bit safe) is the honesty test of the whole aesthetic.
4. **Fixed spatial layout** (btop's lesson). Every agent/run has a permanent home on the surface; state changes in place. No reordering lists, no scrolling, no motion for motion's sake. Spatial memory is the navigation.
5. **Narrative beats, not logs.** A run displays as chapter headings in progress ("exploring → drafting → verifying → writing report"), the same story spine the report will have. The monitor is the report, ahead of time.
6. **Decisions as cards.** Pending asks render as a small physical-feeling stack ("awaiting your pen"). Answering one visibly unblocks an agent — the single satisfying game-like feedback loop we keep. Cards cannot be bulk-approved; friction stays proportional to blast radius (the 93% rubber-stamp finding cuts against ambient comfort, and the monitor must not make blind approval easier).
7. **Quiet failure.** An error is a marginal note ("Run 3 needs you"), never a klaxon. Truthful, calm, specific.
8. **Screenshotable always.** Any steady-state frame of the monitor should be postable. It is the moving version of the before/after screenshot.

### 6.3 v1 surfaces (per Kyle's direction)

Two presentation modes over one local core:

**A. Local web page** (the core). A tiny local server (Python, consistent with the repo's existing stack) watches a workspace and serves one page. Open it on a spare display, fullscreen it, or leave it in a browser tile. This is the v1 deliverable: easiest to build, easiest to make on-brand with Dragonglass CSS, and inherently local (no cloud, no accounts, no telemetry).

**B. Desktop ambient wallpaper + HUD widget.** The same rendering packaged as an always-on desktop layer: a live wallpaper carrying the ambient steady state, plus a small always-on-top HUD widget for the decision stack and health signal. Per Decision 1, B ships alongside A in v0.2 as a thin shell over the same local server (wallpaper via the OS's web-wallpaper mechanisms or a borderless window pinned to desktop level; widget as a small always-on-top frameless window). Electron/Tauri shell is acceptable here because B is explicitly a packaged app, but B must not fork the rendering — one renderer, two frames.

E-ink mode ships inside A as a URL flag (`/?mode=eink`): slow refresh, 1-bit-safe, InkyPi-compatible so the community can hang it in a frame.

### 6.4 What it watches (data model)

Files first, no agent SDK required — the same tool-agnostic bet as the kit:

- **Run manifest** (`openbook/runs/*.md` or frontmatter block): agent name, task one-liner, started, current chapter/beat, status (`working | verifying | blocked | done | failed`).
- **Decision blocks**: the exact `### Decision N · handle` shape from the Report contract, parsed live from draft reports or a pending-decisions file. The monitor consumes the format; this is the commitlint loop.
- **Heartbeat**: file mtime is the default liveness signal (an agent that stopped writing is "quiet"); optional lightweight append-only event file (`events.jsonl`) for agents that want richer beats.
- **Report arrival**: when `REPORT.md` passes `check_report.py`, the run's cell resolves to "book on the shelf" state with a link into the reader.

An optional `formats/monitor.md` contract documents this so any agent, in any stack, can be pointed at it — same install story as the report ("write your status here, in this shape").

### 6.5 Dragonglass alignment

From the design system (Mirror Factory / Dragonglass v1): paper-and-ink palette with seven accents, Hanken Grotesk + DM Mono type, signature glow button, LightBand and FrameRails brand devices, recolorable dragonfly mark, "growth through reflection."

- Surface: warm paper ground shared with render/report.css; ink typography. Monitor UI type is Dragonglass (Hanken Grotesk / DM Mono); rendered report content stays Source Serif 4. See Decision 3 on harmonizing.
- The **glow** token is the pre-attentive health signal (principle 2).
- **FrameRails** frame the fixed spatial grid; **LightBand** is the natural device for the single center-pull moment when a decision arrives.
- The dragonfly mark is the idle state. A monitor with no runs should look like a framed object, not an empty dashboard.

### 6.6 Requirements

**P0 (v1, local web page)**

- Single command start (`python scripts/monitor.py <workspace>` or `openbook monitor`); zero config for a workspace using the kit's conventions.
- Steady-state view: fixed grid of run cells (agent, task one-liner, current beat, quiet/working state), global health signal, decision stack count.
- Decision cards: parsed from the contract shape, shown as a stack; card click reveals the full self-contained block; answering happens in the human's own medium for v1 (the card shows *where* to answer: file path or PR), not an in-monitor form. See Decision 2.
- Minute-grade refresh; no websocket firehose; degrade gracefully when files stop changing.
- Dragonglass-styled; grayscale-safe; screenshotable at every steady state.
- E-ink mode flag.
- Runs entirely local. No network calls out, no accounts, no telemetry. "Local" is a feature named in the brand.

**P0 (v0.2, pulled forward per Decision 1)**

- Desktop packaging (surface B): wallpaper mode + HUD widget over the same server. One renderer, two frames.

**P1 (sequenced immediately after watch-only ships, per Decision 2)**

- **In-monitor decision answering**: cards accept an answer in the monitor and write it back into the workspace in the contract's own shape, unblocking the waiting agent. Per-card friction preserved; no bulk approve. Architecture in §6.8.
- Monitor contract doc (run manifest, decision ledger, events.jsonl shapes) lives in the private shell repo per Decision 8; it enters the public kit only if the monitor goes open.
- Report-arrival transition (run cell becomes a "book" with a reader link).
- Multi-workspace watching (several repos, one surface).

**P2**

- Night summary: at morning, the monitor's timeline hands off to the report ("what you watched is what you read").
- Community frames: InkyPi recipe, tablet kiosk notes.

### 6.7 Non-goals (monitor)

- Not an orchestrator: it never starts, stops, or steers agents. Answering a decision (P1) writes a file in the contract's shape; the agent chooses what to do with it. The monitor holds no session handles and sends no commands.
- Not a trace viewer: no token streams, no span trees; LangSmith and friends own that.
- Not a metrics dashboard: no cost meters or leaderboards in v1; numbers live in report appendices.
- Not vendor-locked: no Claude-only SDK dependency; files and contracts only.
- Not busy: if a design choice adds motion or density, it is probably wrong.

### 6.8 In-monitor answering: architecture (R&D brief, per Decision 2)

The whole feature reduces to one question: **how does a human's answer reach a waiting agent?** Everything else is UI. Four transport patterns, in the order they should be built:

**Pattern 1 — the decision ledger (files, v1 target).** The workspace holds `openbook/decisions/` with one file per pending ask, in the contract shape, written by the agent before it blocks or forks. The monitor renders these as cards; answering writes an `**Answer:**` block (plus who/when) into the same file. Pickup is the agent's job, and there are two modes. *Async mode* (works today, zero SDK): the agent finishes its run, lists unanswered decisions in the report, and the next run's kickoff prompt says "read `openbook/decisions/`, treat answered items as instructions." The answer joins the next brief; nothing waits. *Live mode*: a blocked agent polls the file (a `sleep`-loop Bash step, or a wrapper script with an fs watcher such as `watchdog`/`chokidar`) and resumes when the Answer block appears. Live mode is where R&D starts: the failure modes are agent timeout policies, stale locks, and two writers on one file (solve with append-only answers and atomic rename-writes).

**Pattern 2 — hook-gated approval (Claude Code specific).** Claude Code hooks can intercept the loop: a PreToolUse or Stop hook shells out to a script that blocks until the ledger file carries an answer, then returns allow/deny/context to the session. This turns the ledger into a real pause point without the agent needing to know about OpenBook at all — the hook does the waiting. Equivalent seams exist in other stacks (Cursor rules cannot block, but wrapper CLIs can). This is the highest-leverage experiment: it makes live mode work with today's agents unmodified.

**Pattern 3 — the monitor as MCP server.** The local server already watching files also exposes MCP tools: `ask_human(question, context)` blocks until the card is answered; `list_answers()` for polling. Any MCP-capable agent (Claude Code, Cursor, Codex) connects with one config line. Cleanest long-term contract, and the natural place for per-card friction (the tool call carries blast-radius metadata; the card renders accordingly). Cost: the monitor stops being a pure file-watcher, so ship it as an optional module beside patterns 1–2, never a requirement.

**Pattern 4 — resumable sessions (later, vendor-coupled).** Claude Code sessions can be resumed by id (`claude -r`); an answered card could trigger `claude -r <session> "Decision 3 answered: …"`. Powerful, but it holds session handles and crosses into orchestration, against §6.7. Treat as an experiment, not a commitment.

Cross-cutting R&D notes: (a) the write-back format is just the Report contract's decision block plus an Answer field, so answered ledgers can be transcluded into the final report's What's next section, closing the story loop; (b) HumanLayer and LangChain's Agent Inbox validate the approve/deny transport but stop at modals — the differentiator here is that the answer is memo-grade and lands in the paper trail; (c) security posture stays local-only: the server binds localhost, answers are files in the user's own repo, and nothing leaves the machine.

---

## 7 · Prior art (condensed)

| Category | Examples | OpenBook's difference |
|---|---|---|
| Trace observability | LangSmith, Langfuse, Braintrust, AgentOps | Token-level, for engineers debugging. OpenBook is the narrative + decision layer for humans; traces are receipts, not the read. |
| Orchestration UIs | Vibe Kanban, Conductor, Crystal, Gas Town, Cursor 2.0, Codex app | Interactive operator consoles, code-centric, mostly vendor-shaped. Monitor is spectator-grade, ambient, vendor-neutral. |
| Hobbyist monitors | ccusage, Claude Code Agent Monitor | Proof of demand; metric-dense web-dashboard aesthetic. Nothing calm or non-technical. |
| HITL plumbing | HumanLayer, Agent Inbox | Closest kin to decision blocks, but transactional approve/deny modals. OpenBook decisions are memo-grade: context, options, pen room. |
| Writing culture | ADRs, Amazon six-pager | Ancestors, not competitors. OpenBook is ADR/six-pager culture where the author is an agent and the reader has sixty seconds. |
| Format standards | Keep a Changelog, Conventional Commits, llms.txt, AGENTS.md | Adoption lessons in §8. No agent-report standard exists; the lane is open. |

---

## 8 · Distribution and success metrics

Adoption lessons applied: ride an existing medium (Markdown in git, zero infrastructure); ship a canonical one-page spec and skeleton (done in formats/); make enforcement tooling, not discipline (checker + skill.md); ensure a working consumer exists so the spec never floats free (the monitor — llms.txt died waiting for a reader); keep one zero-setup magic demo (the before/after wipe; a second `transcript → warm-paper report` converter was considered and deferred per Decision 5 to keep the monitor push focused).

Surfaces in priority order stay as the vision has them: contract → paste path → screenshotable examples → checker → render notes/reader. The monitor slots in as the *promotional* surface: short-form clips of a calm night shift are the tiktoks before the podcast.

**Metrics that matter** (stars are vanity):

- Paste-into-prompt adoption: USE.md/skill installs we can see (clones, skill directory listings, unprompted screenshots).
- Reports finished: qualitative, via the demo and shared annotated reports.
- Monitor nights: the monitor survives real overnight use at Mirror Factory for two consecutive weeks (dogfood bar), then one external user runs it unprompted.
- One well-known agent product or prominent builder emitting OpenBook reports would outweigh any evangelism; treat that as the distribution north star.

---

## 9 · Roadmap

| Stage | Ship | Notes |
|---|---|---|
| **v0.1** ✅ | Report contract, librarian style, checker, renderer, examples, live demo | Shipped 2026-07-11 |
| **v0.2** | Dragonglass demo restyle, light default; /openbook skill supersedes USE.md; eval harness v0; monitor v1 (private shell repo) | The tweet-able pair: demo + calm monitor clip |
| **v0.3** | In-monitor answering (ledger pattern + hook experiment, §6.8, per Decision 2); persona validation with Bobby (Decision 4) | The loop closes: watch → answer → unblock |
| **v0.5** | Multi-agent assembly guide; second example pack; senior engineer + coach style cards; receipts hardening; report-arrival transition | Composes the screenshot on many desks |
| **v1** | Spec contract + zoom lenses; public proxy reader; MCP answering module | Reader + monitor as packaged experiences |
| **Later** | More styles; chat Read button; transcript→report converter; decision harvest; community frames | Grow the language, not the platform |

---

## 10 · Evaluation

Four layers, cheapest first. The standing rule they all enforce: **a report may never be more optimistic than its transcript.**

1. **Structural checks (CI, every commit).** `check_report.py` against `examples/` and every eval fixture: required headings per profile, decision-block parse rate, Brief length caps, librarian violations (em dashes, exclamation points). Structure failures fail the build. Mostly built already; wire it to CI.

2. **Skill generation benchmarks.** A fixture corpus of transcripts with deliberately different shapes: the July 8 night, a parallel multi-agent night, a failed run, a boring run where little happened, an oversized run. Run `/openbook` ten times per fixture; measure checker pass rate, variance between runs, and cost. The skill-creator eval tooling does exactly this benchmark-with-variance loop.

3. **Faithfulness fixtures (the anti-slop layer).** Seeded-flaw transcripts with known ground truth: three dead ends, one quietly masked failure, two decision-worthy forks. Score the generated report like a classifier — failure recall (all three dead ends named), claim precision (a judge model traces every lede claim to a transcript span; untraceable claims count as hallucinations), decision recall (both forks surfaced), invented-timestamp count (regex). Track per skill revision so prompt changes have a scoreboard.

4. **Human comprehension (the product truth).** The sixty-second test: a reader gets the report for sixty seconds, then answers five questions — what happened, what failed, what needs deciding, would you ship, what happens next — scored against a control reading the raw transcript for ten minutes. Decision self-containment: a non-builder answers each decision block without opening anything else. Dogfood field metrics: escape-hatch rate (times the raw transcript gets opened after reading the report), share of decisions answered within 24 hours, minutes of morning review per run.

---

## 11 · Risks

1. **Polish launders slop.** A beautiful report over a misrepresented run is worse than a log wall. Mitigation: mechanical receipts (P2, §4), truthfulness rules already in the contract, and honest positioning: legibility layer, not integrity layer.
2. **Decision quality is the hardest authoring skill.** Agents must identify what is decision-worthy; Deep Research critiques suggest models articulate *what* better than *why it matters*. The skill.md prompt is load-bearing product surface; give it examples and evals.
3. **Vendor convergence.** Cursor/Codex/Anthropic will keep building mission control. Hold the ground they will not: vendor-neutral, non-technical, calm, print-honest. Do not compete on orchestration.
4. **Calm vs accountability.** Ambient comfort could deepen rubber-stamping. Mitigation: per-card friction, no bulk approve, decisions are the one thing that interrupts.
5. **Unvalidated spectator persona.** See Decision 4.
6. **Name collision.** "OpenBook" collides with unrelated exchange/education projects; no existing search demand in this lane. Distribution must be created (Show HN, awesome-lists, skill directories), not harvested.
7. **Scope temptation.** Two new surfaces (reader, monitor) around a young format. The sequence in §9 exists so the contract stays the center of gravity; if a stage slips, cut the stage, not the contract's quality.

---

## What's next

Decisions 1–5 were answered by Kyle on 2026-07-11; Decisions 6–9 followed the same day, after the monitor shell spun out. Kept here as the record.

### Decision 1 · Monitor build target for v0.2 — resolved

Wallpaper/HUD packaging is pulled forward into v0.2, shipping alongside the local web page as a thin shell over the same server. One renderer, two frames.

### Decision 2 · Where humans answer decisions — resolved

In-monitor answering is prioritized, sequenced immediately after watch-only ships (v0.3). Architecture and R&D plan in §6.8: decision ledger first, hook-gated approval as the highest-leverage experiment, MCP module at v1.

### Decision 3 · One type system or two — resolved

Two, deliberately: monitor chrome in Dragonglass (Hanken Grotesk / DM Mono), report content in the report stack (Source Serif 4). The book is not the shelf.

### Decision 4 · Validate the spectator persona — resolved

Committed: one or two discovery conversations with non-builder candidates (Bobby) watching a real night, before v0.5 hardens the monitor's P1.

### Decision 5 · The second magic demo — resolved

Deferred to Later. The push stays on the monitor; the transcript→report converter waits.

### Decision 6 · Document home — resolved

This document is named requirements and lives at docs/requirements.md in the openbook repo.

### Decision 7 · The skill — resolved

Named `openbook`, invoked `/openbook [brief|standard|essay]`, profile inferred from run size when omitted. Triggers by command and by description at the end of long runs; a Stop-hook variant stays a documented power-user option. USE.md retires; README points at the skill.

### Decision 8 · Where the monitor lives — resolved

Private repo (openbook-shell) for now; open source vs paid vs Layers stays deliberately open. The public kit remains Markdown-only.

### Decision 9 · Receipts — resolved

Hardening pulled forward to v0.5.

---

## Appendix

**By the numbers:** repo v0.1.0 · 11 commits · 3 length profiles · 1 style card · 1 live demo · 2 planned monitor surfaces

**Repo receipts:** [mirror-factory/openbook](https://github.com/mirror-factory/openbook) — README, VISION.md, USE.md, CHANGELOG 0.1.0, formats/report.md, styles/librarian.md, [live demo](https://mirror-factory.github.io/openbook/).

**Research receipts (selection):**
- AI slop review burden: [arXiv 2603.27249](https://arxiv.org/html/2603.27249v1) · [GitHub on agent PRs](https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/) · [CodeRabbit on maintainer burnout](https://www.coderabbit.ai/blog/ai-is-burning-out-the-people-who-keep-open-source-alive)
- Babysitting tax and parallel ceilings: [Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) · [worktrees playbook](https://www.developersdigest.tech/blog/git-worktrees-claude-code-parallel-agents-guide) · [Devin reviews](https://www.theregister.com/2025/01/23/ai_developer_devin_poor_reviews/)
- Calm technology: [Weiser & Brown](https://calmtech.com/papers/computer-for-the-21st-century) · [Ambient Orb](https://en.wikipedia.org/wiki/Ambient_device) · [InkyPi](https://github.com/fatihak/InkyPi)
- TUI/game observability: [Terminal Renaissance](https://dev.to/hyperb1iss/the-terminal-renaissance-designing-beautiful-tuis-in-the-age-of-ai-24do) · [SimCity/agents](https://medium.com/@sebastianhanke/from-the-gaming-world-to-the-software-development-revolution-028fd35b0ca5) · [Claude Code Agent Monitor](https://github.com/hoangsonww/Claude-Code-Agent-Monitor)
- Format adoption: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) · [ADRs (Nygard)](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) · [llms.txt post-mortem](https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/) · [Bezos memo culture](https://slab.com/blog/jeff-bezos-writing-management-strategy/)

**Design receipts:** Dragonglass Design System v1 (Claude design project, shared link): paper-and-ink palette + 7 accents, Hanken Grotesk / DM Mono, glow token, LightBand, FrameRails, dragonfly mark.

**Vision content relocated here:** the strategy sections of the former VISION.md (problem taxonomy, personas, design principles, format details, enforcement, delivery layers, adjacent work, moat, distribution, roadmap, non-goals) now live in this PRD. VISION.md is the manifesto.

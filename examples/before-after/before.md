$ agent resume --cwd /work/atrium
session 2026-07-08T23:24:00-04:00  permission=unrestricted  goal=night-shift

> continue night shift. finish markdown contract + design research.
> update NIGHT-REPORT.md. leave decisions for human.

[read] NIGHT-REPORT.md  (847 lines)
[read] tasks/T001-markdown-contract.md  (214 lines)

$ rg -n "acceptance|PASS|FAIL" packages/model/src -g '*.ts' | head -80
packages/model/src/frontmatter.ts:41: export type AcceptanceItem = {
packages/model/src/frontmatter.ts:88: if (!parsed.ok) throw new ParseError(...)
packages/model/src/ready.ts:12: export function assertReady(spec: Spec): void {
packages/model/src/projections.ts:63: case "Full": return fullProjection(doc)
packages/model/src/serialize.ts:19: // byte-identical while frontmatter untouched
… +47 lines

$ git status -sb && git log --oneline -12
## night/2026-07-08...origin/night/2026-07-08 [ahead 9]
?? design/proposals/2026-07-08/
 M packages/model/src/frontmatter.ts
 M packages/model/src/serialize.ts
a1f3c02 wip: projections
9ee2b10 wip: parser fixtures
c4d91aa wip: ready-flip
… +9 more

[read] seed/specs/legacy-brand-narrative.md  (156 lines)
note: pre-schema keys — matters for round-trip byte-identity

[edit] packages/model/src/serialize.ts  (+38 -11)

$ pnpm exec vitest run packages/model --reporter=verbose
 RUN  v2.1.9 /work/atrium

 ✓ packages/model/src/frontmatter.test.ts > parse canonical (12)
 ✓ packages/model/src/frontmatter.test.ts > serialize untouched preserves bytes (3)
 ✓ packages/model/src/serialize.test.ts > round-trip folio index (2)
 ✓ packages/model/src/ready.test.ts > ready-flip (4)
 ❯ packages/model/src/serialize.test.ts > BOM fixture
   → expected false to be true // Object.is equality

 Test Files  1 failed | 4 passed (5)
 Tests       1 failed | 53 passed (54)
 Duration   3.82s

BOM path broken. Investigating.

$ xxd seed/specs/bom-spec.md | head -3
00000000: efbb bf2d 2d2d 0a74 6974 6c65 3a20 426f  ...---.title: Bo
00000010: 6d20 4669 7874 7572 650a 7374 6174 7573  m Fixture.status
00000020: 3a20 6472 6166 740a 2d2d 2d0a            : draft.---.

[edit] packages/model/src/frontmatter.ts
  strip BOM before fence detect
[edit] packages/model/src/frontmatter.test.ts  (+regression)

$ pnpm exec vitest run packages/model 2>&1 | tail -12
 Test Files  5 passed (5)
 Tests       54 passed (54)
 Duration   2.91s

$ pnpm exec tsc --noEmit -p packages/model
(clean)

[spawn] review-fleet  agents=28  mode=adversarial
  finders: 16 distinct
  verified: 10
  confirmed data-integrity: 7
    - BOM silent double-frontmatter on save  [CRITICAL]
    - corrective edit matching normalized value never reaches disk
    - invalid form: destroyed by unrelated checkbox click
    - NaN breaks byte-identity check
    - unterminated frontmatter duplicates stale text
    - ready asserted with open acceptance boxes
    - Full projection drops preamble content
  tokens≈843000  wall=14m22s

[edit] packages/model/src/{frontmatter,serialize,ready,projections}.ts
[edit] packages/model/src/*.test.ts  (+14 regression tests)
note: pnpm version pin left unchanged for conscious merge

$ pnpm exec vitest run && pnpm exec tsc --noEmit
 Test Files  5 passed (5)
 Tests       68 passed (68)
 Duration   4.11s
 tsc: clean (strict, noUncheckedIndexedAccess)

$ gh pr create --title "feat(model): T001 markdown contract"
https://github.com/example/atrium/pull/1
acceptance 5/5 PASS · self-review comment posted

================================================================================
parallel track: design research + Library concepts

[write] design/research/quiet-ui.md
[write] design/research/calm-density.md
[write] design/research/library-archive-patterns.md
[write] design/research/opendesign.md
[write] design/research/semantic-zoom.md
[write] design/research/markdown-reading.md
  6 notes · sources · adopt/reject
  through-line: calm tech; generous interface (search box withholds collection)

[write] design/proposals/2026-07-08/library-a-the-desk.html       (+v1→v3)
[write] design/proposals/2026-07-08/library-a-the-desk-critique.md
  data-ink fail: conflict counted three times; cut to judgment-only prose

[write] design/proposals/2026-07-08/library-b-the-catalog.html
[write] design/proposals/2026-07-08/library-b-the-catalog-critique.md
  answer-in-prose before receipts · fixed facet/verb vocabulary

[write] design/proposals/2026-07-08/library-c-the-ledger.html
[write] design/proposals/2026-07-08/library-c-the-ledger-critique.md
  built known-wrong (second journal vs charter)
  organ donor: custody box + trails → salvaged into Desk/Catalog

[write] design/proposals/2026-07-08/shell-composition.html
[write] design/proposals/2026-07-08/shell-composition-critique.md
  panes: nav | Library center | Journal right · light+graphite
  HARD: Document/Folio open location undecided
  shell task still encodes pre-kickoff layout (Journal inside navigator)

[write] design/proposals/2026-07-08/worksheet-goal-intake.html
[write] design/proposals/2026-07-08/worksheet-correction-state.html
[write] design/proposals/2026-07-08/worksheet-decision-weigh-in.html
[write] design/proposals/2026-07-08/worksheet-handoff-chooser.html
  worksheets 4/5 mockuped (BMC + audience-and-offer not mockuped)
  accidental: goal-intake "what does done look like" → session acceptance ???

$ git add -A && git commit -m "docs(design): night research + library concepts"
$ gh pr create --title "docs(design): night-shift research + Library concepts"
https://github.com/example/atrium/pull/2

$ git diff --stat origin/main...HEAD | tail -8
 design/research/quiet-ui.md                         |  68 +++
 design/proposals/2026-07-08/library-a-the-desk.html | 412 ++++++++++++++
 design/proposals/2026-07-08/library-b-the-catalog.html | 288 ++++++++++
 design/proposals/2026-07-08/library-c-the-ledger.html | 241 +++++++++
 packages/model/src/frontmatter.ts                   | 142 ++++++-
 packages/model/src/serialize.ts                     |  97 ++++-
 47 files changed, 3821 insertions(+), 219 deletions(-)

================================================================================
$ sed -n '/PENDING-HUMAN/,+18p' NIGHT-REPORT.md

## PENDING-HUMAN (do not invent)
1. Document/Folio open — Library center + Journal right (blocks shell re-spec)
2. Desk+Catalog as two Library states; Ledger as by-time lens only? or one winner
3. Sessions carry acceptance from goal-intake ("what does done look like") at close?
4. arrangement-weights vocab (decisions-first / recency / trail-affinity / kind-mix)
5. resume cues worth session-state memory?
6. DESIGN.md draft review (proposal)
7. package-manager pin riding contract PR

## stats
research_notes=6  library_concepts=3  worksheets=4/5
prs=2  tests=68  review_confirmed=7  themes=light+graphite
floors_met=23:53 (29m in) then depth until ~07:00

$ echo DONE
# scroll up for tool traces. everything green.
# questions 1-3 match what a one-page handoff would ask; 4-7 still open in the log.

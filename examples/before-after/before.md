$ agent resume --cwd /work/openbook
session 2026-07-12T23:08:00-04:00  permission=unrestricted  goal=night-shift

> long runs end in transcript walls nobody reads. build the fix.
> a format contract, a checker, a renderer. leave decisions for human.

[read] NOTES.md  (312 lines)
[read] research/review-burden.md  (147 lines)
[read] VISION.md · AGENTS.md  (invariants: markdown kit, no invented timestamps)

[write] formats/report.md
  three length profiles · decision blocks · receipts in appendix
  truthfulness rules: dead ends are content, no invented timestamps

[write] scripts/check_report.py  (+fixtures)
$ python scripts/check_report.py examples/draft-1.md          # 00:41
  FAIL: Cover carries statistics grid (numbers before story)
  FAIL: lede claim without receipt reference
note: draft-1 opened with nine stats. impressive, empty. demoting to appendix.

[edit] examples/draft-1.md → draft-2.md  (stats grid cut, lede rewritten)
$ python scripts/check_report.py examples/draft-2.md
  PASS  0 errors  2 warnings (read-time byline, pen room depth)

[write] render/report.css   (warm paper, Source Serif 4, pen rooms print-only)
$ python scripts/render_report.py examples/draft-2.md         # 01:30
  WARN: pen rooms clipped at US Letter margin
[edit] render/report.css  (print styles last in cascade)
  fixed. screen overrides can no longer break PDF.
  commit lineage later: "Fix the blank page after the cover: one break between blocks"

[write] docs/index.html  (before/after wipe demo)
[test] wipe handle drag                                        # 02:14
  handle surrenders drag to iframe underneath. investigating.
  pointer-events on panes? capture on handle? both?
  ... 02:41 still dropping at pane boundary
  ... 03:02 setPointerCapture on handle, panes inert during drag
  fixed 03:19. one hour gone. logging it.

$ python scripts/build_demo.py
  panes regenerated from example pack · scroll sync ok

$ pnpm exec vitest run scripts 2>&1 | tail -3
 Test Files  3 passed (3)
 Tests       41 passed (41)

$ python scripts/check_report.py REPORT.md                    # 06:12
  PASS  0 errors  0 warnings

$ git add -A && git commit -m "feat: openbook v0 (format, checker, renderer, demo)"
$ echo DONE

# REPORT.md written. it explains what this all was.
# or scroll up. everything you need is in here somewhere.

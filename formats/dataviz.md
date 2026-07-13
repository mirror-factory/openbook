# OpenBook Data Visualization

When numbers carry the claim, a chart earns its page better than a paragraph
of digits. This file is the law for figures that are DRAWN rather than
captured. Screenshots remain evidence; charts are argument, and an argument
can lie, so the rules here are mostly about not lying.

## When to draw a chart

- The claim compares quantities (before/after, planned/landed, spend by bucket).
- The claim is about shape over time (a night of commits, a week of syncs).
- A reader would otherwise have to hold four or more numbers in their head
  across a sentence.

When a single number carries the story, print the number in prose. A chart
of one bar is theater.

## The rules

1. **One message per chart.** The caption states it as a sentence. If the
   caption needs "and," draw two charts.
2. **Label directly.** Values sit on or beside their marks. Legends make the
   reader commute; avoid them when the series can be named in place.
3. **Grayscale-safe, e-ink first.** Ink on paper: black, two grays, white.
   Never encode meaning in hue alone. The reMarkable is the first screen
   this renders on; design for it and every other surface inherits.
4. **Start scales at zero for bars.** A truncated bar axis is a soft lie.
   Time axes and dot plots may zoom, and say so in the caption.
5. **No chartjunk.** No 3D, no gradients, no drop shadows, no background
   grids heavier than the data. The data-ink ratio is a register rule.
6. **Real numbers only.** Every value in a chart is extracted from the run
   the way appendix receipts are; a chart is a receipt that learned to
   stand up. Numbers shown in a chart still appear in the Appendix.
7. **Serif-free.** Chart text uses the UI or mono face, small; the chart is
   a figure, not prose.
8. **Timelines read left to right, one row per thread.** A night of work is
   a horizontal band: time on the x-axis, kinds of work as rows, marks where
   things landed. Density is the story; let it show.

## The pipeline

Charts are PNGs beside the report, referenced as ordinary figures:

```markdown
![The night's commits landed in three waves; the gap near 04:00 is the dead iteration.](assets/night-timeline.png)
```

Generate at 2x the printed size (about 1800px wide for full measure) so
e-ink renders crisp lines. matplotlib with the Agg backend is the proven
path; any tool that obeys the rules above is welcome.

## Anti-patterns

- A pie chart (compare angles, badly) where a bar chart works
- A legend for two series that could be labeled in place
- Color-only encoding (invisible on the tablet)
- A chart whose numbers appear nowhere in the Appendix
- Decorating a number that needed no chart

# OpenBook Design Pass — Claude Design Brief

Paste the **Kickoff prompt** below into a new Claude Design project. Attach first:

1. `Branding.zip` — 30 brand-guideline slides (PNG, 1920×1080)
2. `WIP Brand Assets-20260711T225019Z-2-001.zip` — MF logo suite (SVG + PNG, 4 colorways × 5 lockups), **real font binaries** (Helvena OTF 8 weights, DM Mono TTF 6 styles), MF-Brand_Pitch-V2.pdf
3. The Dragonglass Design System v1 project (link or export) — prior tokens/components; treat as reference, not source of truth
4. `PRD.md` — for surface requirements (§6 especially)

Key correction for the design agent: Dragonglass substituted Hanken Grotesk for Helvena. The real Helvena binaries are in the WIP zip, and the brand's official Google-Fonts fallback is **Manrope** (semibold in place of medium), not Hanken Grotesk. Use real Helvena; fall back to Manrope.

---

## Kickoff prompt (paste from here down)

We are doing a design pass on **OpenBook** (github.com/mirror-factory/openbook): "Agent work, written for humans." Open-source report formats that make long-horizon agent runs readable, plus a calm ambient **local monitor** for watching runs. Heavy inspiration from the attached Mirror Factory brand. Work in two phases: **explore style variants first on one test surface; do not design the full surface set until I pick a direction.**

### Brand foundation (from the attached guidelines)

- **Papers:** Cloud White `#F2EEE5`, Dune Off-White `#E7E4D8`; ink is near-black
- **Accents (7):** Signal Red `#F54C26`, Peach Glow `#F5B688`, Field Green `#818C64`, Ocean Glass `#90ECE2`, Orbit Purple `#6A5FD0`, Lilac Air `#A6B5DD`, Green Pulse `#CEF25A`
- **Type:** Helvena (display; tight, grotesk; binaries attached) + DM Mono (labels, captions; uppercase, tracked out). Fallback: Manrope, semibold for medium
- **Graphic elements:** frame rails (thin rules at page edges with vertical mono labels), chamfered/clipped-corner frames, light diffusion effect (soft glow, subtle color shifts on focal areas), dot texture, grid overlays, full-bleed nature imagery with luminous washes, mirrored-text motif
- **Logo:** MF mark ("organic, symmetrical"), 5 lockups × 4 colorways attached as SVG
- **Voice:** economical, no exclamation points, no em dashes, dry wit allowed, failures named plainly
- **Register:** calm over busy. This product's whole thesis is a calm alternative to a wall of terminals. If a choice adds motion or density, it is probably wrong.

### Phase 1 — variant exploration

Design ONE test surface in each variant: the **monitor steady state** (desktop 16:9): fixed grid of 4 run cells (agent name, task one-liner, current narrative beat, working/quiet state), one global health signal, a decision stack showing 2 pending cards, idle MF mark presence. Same content in every variant so only style varies.

Five directions to explore (adjust as you see fit):

1. **Reading Room** — editorial/library. Warm paper, masthead rules, report typography leaking into the UI, runs as books being written, finished run becomes a book on a shelf. Closest to the existing report CSS (Source Serif 4 content).
2. **Field Instrument** — DM Mono forward, frame rails and chamfered frames carry the structure, instrument-panel restraint, dot texture, tiny tick marks. Apollo-checklist energy, zero klaxon.
3. **Light Diffusion** — the brand's luminous language does the signaling: health as a soft glow field on paper, accents as color washes, decision arrival as a LightBand moment. Most atmospheric, must stay grayscale-legible.
4. **Ink & Signal** — near-monochrome ink on paper; exactly one accent at a time does all the work (Signal Red or Green Pulse). E-ink-first thinking; the 1-bit degrade is the design, not an afterthought.
5. **Night Shift** — the dark colorway (true-black assets attached). Overnight is the primary real-world viewing condition for an ambient wallpaper; explore ink-on-dark with diffusion glow.

Render each as a full-fidelity static frame. I will pick one (or a merge) before Phase 2.

### Phase 2 — surfaces (after I pick)

Apply the chosen direction across, in order:

1. **Monitor steady state** (final) — fixed spatial grid, minute-grade refresh, screenshotable at every state
2. **Decision card + stack** — the one center-pull moment; card shows the self-contained ask, answer affordance, per-card friction, no bulk approve
3. **HUD widget** — small always-on-top frameless window: health signal + decision count + next beat
4. **Ambient wallpaper mode** — full-desktop steady state, readable at a glance from across the room, calm enough to live behind icons
5. **E-ink mode** — 1-bit-safe, slow refresh, looks right in a frame (InkyPi)
6. **Report screen render + masthead** — harmonize the existing warm-paper report CSS with the brand (report content stays serif; chrome may adopt Dragonglass); include the "book on the shelf" finished state
7. **Demo page polish** — the before/after wipe at mirror-factory.github.io/openbook, restyled on-brand
8. **Social/OG card** — the screenshotable identity frame for the repo and posts

Constraints that hold across all surfaces: fixed spatial layout (no reordering, no scrolling); one pre-attentive health signal; decisions are the only element allowed to demand attention; failures render as quiet marginal notes; every steady state must screenshot well; everything degrades to grayscale honestly.

# Proposals from the morning ink, 2026-07-13

Three threads from Kyle's annotations on the night-5 report that are design
work, not renderer patches. Written as proposals; nothing here is built.

## 1. Settings: global and per-project, as a page you can see

OpenBook currently has no settings surface; every preference lives in the
format files as law. Kyle's ask: settings with global and project scope,
and an HTML settings page with a live preview.

Proposed shape:

- `openbook.toml` at two scopes: `~/.openbook/openbook.toml` (global) and
  `<project>/openbook.toml` (project overrides global, the git-config
  model). Renderer and checker read the merged view.
- Settable things start small: paper tone, accent, body face, figure
  border, pen-room height, appendix density, page size (Letter/A4),
  masthead style. Every setting has the current default as its value, so
  an empty file changes nothing.
- `scripts/settings_page.py` renders a single self-contained HTML page:
  each setting as a control on the left, a live one-page specimen (cover,
  a decision block, a figure pair, an appendix run) on the right,
  restyled as controls change. Saving writes the toml back. No server,
  no build; a file you open in a browser.
- The register laws (no em dashes, no exclamation points, receipts
  extracted never paraphrased) are NOT settings. Law and preference stay
  in different files.

## 2. Audio: the report reads itself, but not here

Kyle's direction from the night-5 conversation: OpenBook writes the
transcript; it never ships a player. The Layers mobile surface owns
playback.

- OpenBook side: a `--transcript` render mode that emits the report as a
  speakable script (headings become spoken section breaks, figures become
  their captions read aloud, decision blocks become "Decision: ..." with
  a pause mark, appendix receipts are skipped by default). Deterministic
  text out; no audio dependency in this repo.
- Synthesis: VoiceBox (github.com/jamiepine/voicebox, MIT, 36k stars,
  v0.5.0 April 2026) is the strongest open-source fit found: local-first,
  seven TTS engines including fully-local Kokoro and Qwen3-TTS, voice
  cloning from a short sample, exposes a local API and MCP so an agent
  can drive it. Cost per minute on local engines is compute only, zero
  marginal; hosted engines (HumeAI) bill their own API rates. A cloned
  quiet librarian voice reading the morning report is well inside its
  demonstrated use.
- Layers side (not this repo): the mobile player consumes the audio file
  plus the transcript for scrub-by-section.

## 3. The cover, researched further

The morning pass improved the masthead (kicker, full-measure rule, caps
byline). The deeper research Kyle asked for should compare three cover
families before more is built: the journal masthead (what we have), the
report title page (centered, generous whitespace, institutional), and
the field notebook (dense header strip, content starts on page one).
Decide per length: Brief may want the notebook strip, Essay the title
page. Specimens should render from one fixture report so the comparison
is honest.

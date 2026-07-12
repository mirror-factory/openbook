#!/usr/bin/env python3
"""Build demo assets under docs/ for GitHub Pages.

Usage (from repo root):
  python scripts/build_demo.py
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_report import CSS_PATH, md_to_html  # noqa: E402

EXAMPLES = ROOT / "examples" / "before-after"
OUT = ROOT / "docs" / "assets" / "generated"
REPORT_CSS = CSS_PATH.read_text(encoding="utf-8")

# Screen-only demo chrome. Must not follow @media print at equal specificity —
# wrap overrides so print stays 11pt / white / pen rooms visible.
DEMO_CSS = REPORT_CSS + """
@media screen {
  html { height: 100%; }
  body {
    margin: 0;
    min-height: 100%;
    background: #F2EEE5;
  }
  .demo-shell {
    max-width: 65ch;
    margin: 0 auto;
    padding: 2.75rem 1.5rem 3.5rem;
  }
  .demo-shell > .kicker {
    font-family: "DM Mono", ui-monospace, monospace;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    font-size: 0.7rem;
    color: #6B675C;
    margin: 0 0 1.5rem;
    font-weight: 500;
  }
  .demo-shell .report {
    padding: 0 0 1rem;
  }
  .demo-shell .cover {
    margin-top: 0.25rem;
  }
}
"""

# Terminal dump pane: Surfaces 2G before panel (#050505 / DM Mono / Shift accents)
DUMP_CSS = """
body {
  margin: 0;
  padding: 14px 16px 40px;
  font-family: "DM Mono", ui-monospace, "Cascadia Mono", Consolas, "Courier New", monospace;
  font-size: 11px;
  line-height: 1.38;
  color: #7D7A6E;
  background: #050505;
}
.badge {
  display: inline-block;
  font-size: 10px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #050505;
  background: #7D7A6E;
  padding: 2px 7px;
  margin-bottom: 10px;
}
.cli {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
}
.cli .ln { display: block; }
.cli .fail { color: #F54C26; }
.cli .ok { color: #CEF25A; }
"""


def wrap_fragment(
    title: str,
    body: str,
    css: str,
    body_class: str = "",
    head_extra: str = "",
) -> str:
    cls = f' class="{body_class}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
{head_extra}<style>
{css}
</style>
</head>
<body{cls}>
{body}
</body>
</html>
"""


def before_html(raw: str) -> str:
    """Dense terminal transcript; color only fail/ok cues sparingly."""
    out: list[str] = [
        '<div class="badge">agent session · transcript</div>',
        '<div class="cli">',
    ]
    for line in raw.replace("\r\n", "\n").rstrip().split("\n"):
        low = line.lower()
        # ~5–10%: failures and final greens only
        if (
            "failed" in low
            or "critical" in low
            or "❯" in line
            or "expected false to be true" in low
        ):
            out.append(f'<span class="ln fail">{html.escape(line)}</span>')
        elif re.search(r"\b68 passed\b", low) or (
            "test files  5 passed" in low and "failed" not in low
        ):
            out.append(f'<span class="ln ok">{html.escape(line)}</span>')
        else:
            out.append(f'<span class="ln">{html.escape(line)}</span>')
    out.append("</div>")
    return "\n".join(out)


DOCS = ROOT / "docs"
STANDALONE = DOCS / "openbook-demo.html"
SOURCE_SERIF_HEAD = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
"""


def write_standalone(before_doc: str, after_doc: str) -> None:
    """Single-file preview: no relative asset fetches; works via file://."""
    demo_css = (DOCS / "demo.css").read_text(encoding="utf-8")
    demo_js = (DOCS / "demo.js").read_text(encoding="utf-8")
    before_srcdoc = html.escape(before_doc, quote=True)
    after_srcdoc = html.escape(after_doc, quote=True)
    black_logo = (DOCS / "assets" / "logo" / "mf-icon-true_black.svg").read_text(
        encoding="utf-8"
    )
    white_logo = (DOCS / "assets" / "logo" / "mf-icon-true_white.svg").read_text(
        encoding="utf-8"
    )
    black_data = "data:image/svg+xml;charset=utf-8," + quote(black_logo)
    white_data = "data:image/svg+xml;charset=utf-8," + quote(white_logo)

    page = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>OpenBook · before / after</title>
  {SOURCE_SERIF_HEAD}
  <style>
{demo_css}
  </style>
</head>
<body>
  <header class="top">
    <div class="chrome">
      <a class="brand-row" href="https://mirror-factory.github.io/openbook/">
        <img class="logo-day" src="{black_data}" alt="">
        <img class="logo-night" src="{white_data}" alt="" hidden>
        <span class="brand-mark">Mirror Factory / OpenBook</span>
      </a>
      <div class="chrome-actions">
        <a class="nav-link" href="https://mirror-factory.github.io/openbook/" aria-current="page">Demo</a>
        <a class="nav-link" href="https://mirror-factory.github.io/openbook/vision.html">Vision</a>
        <a class="nav-link" href="https://mirror-factory.github.io/openbook/about.html">About</a>
        <a class="nav-link" href="https://mirror-factory.github.io/openbook/start.html">Start</a>
        <a class="nav-link" href="https://github.com/mirror-factory/openbook">GitHub ↗</a>
        <button type="button" class="theme-toggle" id="theme-toggle" aria-pressed="false">Night</button>
      </div>
    </div>
    <div class="hero">
      <h1 class="logo">Agent work, written for humans.</h1>
      <p class="tag">Open report formats that make long-horizon agent runs readable.</p>
      <p class="lede">Same night. An agent session transcript versus an OpenBook Brief.</p>
    </div>
  </header>

  <section class="stage" aria-label="Before and after comparison">
    <div class="labels">
      <span>Before · the wall of terminals</span>
      <span>After · the book</span>
    </div>
    <div class="compare" id="compare">
      <iframe class="pane pane-before" id="pane-before" title="Status dump before" srcdoc="{before_srcdoc}"></iframe>
      <iframe class="pane pane-after" id="pane-after" title="OpenBook Brief after" srcdoc="{after_srcdoc}"></iframe>
      <div class="handle" id="handle" role="slider" tabindex="0"
           aria-valuemin="0" aria-valuemax="100" aria-valuenow="70"
           aria-label="Reveal OpenBook Brief over the status dump">
        <span class="grip" aria-hidden="true">◂ Drag ▸</span>
      </div>
    </div>
    <label class="range-wrap visually-hidden">
      <span>Comparison slider</span>
      <input type="range" id="slider" min="0" max="100" value="70" aria-hidden="true" tabindex="-1">
    </label>
  </section>

  <footer class="foot">
    <nav class="foot-nav" aria-label="Site">
      <a href="https://mirror-factory.github.io/openbook/" aria-current="page">Demo</a>
      <a href="https://mirror-factory.github.io/openbook/vision.html">Vision</a>
      <a href="https://mirror-factory.github.io/openbook/about.html">About</a>
      <a href="https://mirror-factory.github.io/openbook/start.html">Start</a>
      <a href="https://github.com/mirror-factory/openbook">GitHub</a>
    </nav>
    <p>Self-contained preview · also live at <a href="https://mirror-factory.github.io/openbook/">mirror-factory.github.io/openbook</a>.</p>
    <p><a href="https://github.com/mirror-factory/openbook">github.com/mirror-factory/openbook</a></p>
  </footer>

  <script>
{demo_js}
  </script>
</body>
</html>
"""
    STANDALONE.write_text(page, encoding="utf-8")
    print(f"wrote {STANDALONE}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    before_md = (EXAMPLES / "before.md").read_text(encoding="utf-8")
    before_doc = wrap_fragment(
        "Before — agent transcript", before_html(before_md), DUMP_CSS
    )
    (OUT / "before.html").write_text(before_doc, encoding="utf-8")

    after_docs: dict[str, str] = {}
    for name, label in (
        ("after-brief.md", "Brief"),
        ("after-standard.md", "Standard"),
        ("after-essay.md", "Essay"),
    ):
        path = EXAMPLES / name
        md = path.read_text(encoding="utf-8")
        _title, body = md_to_html(md)
        badge = f'<p class="kicker">OpenBook · {label}</p>\n'
        doc = wrap_fragment(
            f"After — {label}",
            f'<div class="demo-shell">\n{badge}{body}\n</div>',
            DEMO_CSS,
            head_extra=SOURCE_SERIF_HEAD,
        )
        (OUT / f"{path.stem}.html").write_text(doc, encoding="utf-8")
        after_docs[path.stem] = doc
        print(f"wrote {OUT / (path.stem + '.html')}")

    print(f"wrote {OUT / 'before.html'}")
    write_standalone(before_doc, after_docs["after-brief"])
    print("Demo ready: open docs/index.html or docs/openbook-demo.html in a browser")


if __name__ == "__main__":
    main()

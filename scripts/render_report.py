#!/usr/bin/env python3
"""OpenBook: Markdown report → frameless HTML → letter PDF (Playwright).

Usage:
  python scripts/render_report.py path/to/REPORT.md [-o out.pdf]

Never use browser file:// print (Chrome date/URL footers). This path is the
supported PDF pipeline for reMarkable delivery.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT / "render" / "report.css"
TEMPLATE_PATH = ROOT / "render" / "template.html"


def md_to_html(md: str) -> tuple[str, str]:
    """Convert OpenBook markdown to HTML body + title. Stdlib only."""
    lines = md.replace("\r\n", "\n").split("\n")
    title = "OpenBook Report"
    # When a "## Cover" section exists, a leading H1 is a title, not a second
    # cover page (issue #1: the doubled cover).
    has_cover_section = any(
        line.strip().lower() == "## cover" for line in lines
    )
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False
    in_pre = False
    pre_buf: list[str] = []
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if not para:
            return
        text = " ".join(para).strip()
        para = []
        if text:
            out.append(f"<p>{inline(text)}</p>")

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            r'<a href="\2">\1</a>',
            s,
        )
        return s

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            flush_para()
            close_lists()
            if not in_pre:
                in_pre = True
                pre_buf = []
            else:
                out.append("<pre>" + html.escape("\n".join(pre_buf)) + "</pre>")
                in_pre = False
            i += 1
            continue

        if in_pre:
            pre_buf.append(line)
            i += 1
            continue

        if not line.strip():
            flush_para()
            close_lists()
            i += 1
            continue

        if line.startswith("# ") and not line.startswith("## "):
            flush_para()
            close_lists()
            title = line[2:].strip()
            if not has_cover_section:
                out.append(f'<div class="cover"><h1>{inline(title)}</h1></div>')
                out.append('<div class="pagebreak"></div>')
            i += 1
            continue

        if line.startswith("## "):
            flush_para()
            close_lists()
            h = line[3:].strip()
            if h.lower() == "cover":
                i += 1
                meta: list[str] = []
                cover_title = title
                while i < len(lines) and not lines[i].startswith("## "):
                    raw = lines[i].strip()
                    if raw:
                        meta.append(raw)
                        mt = re.match(
                            r"\*\*Title:\*\*\s*(.+)$", raw, re.IGNORECASE
                        ) or re.match(r"Title:\s*(.+)$", raw, re.IGNORECASE)
                        if mt:
                            cover_title = mt.group(1).strip()
                            title = cover_title
                    i += 1
                out.append('<div class="cover">')
                out.append(f"<h1>{inline(cover_title)}</h1>")
                out.append('<div class="rule"></div>')
                for s in meta:
                    if re.match(r"(\*\*)?Title:", s, re.IGNORECASE):
                        continue
                    out.append(f'<div class="sub">{inline(s)}</div>')
                out.append("</div>")
                out.append('<div class="pagebreak"></div>')
                continue
            if out:
                out.append('<div class="pagebreak"></div>')
            out.append(f"<h2>{inline(h)}</h2>")
            i += 1
            continue

        if line.startswith("### "):
            flush_para()
            close_lists()
            h = line[4:].strip()
            # Decision blocks under What's next
            if re.match(r"^\d+\.\s*", h) or h.startswith("[?]"):
                out.append('<div class="qblock">')
                out.append(f'<p class="q nojust">{inline(h)}</p>')
                i += 1
                # standard markdown style puts a blank line after a heading;
                # the context is still the context (issue #2: the orphaned
                # paragraph below the pen room)
                while i < len(lines) and not lines[i].strip():
                    i += 1
                ctx: list[str] = []
                while i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
                    ctx.append(lines[i].strip())
                    i += 1
                if ctx:
                    out.append(f'<p class="ctx">{inline(" ".join(ctx))}</p>')
                out.append('<div class="penroom"></div>')
                out.append("</div>")
                continue
            out.append(f"<h3>{inline(h)}</h3>")
            i += 1
            continue

        m_ul = re.match(r"^[-*]\s+(.*)$", line)
        if m_ul:
            flush_para()
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(m_ul.group(1))}</li>")
            i += 1
            continue

        m_ol = re.match(r"^(\d+)\.\s+(.*)$", line)
        if m_ol:
            flush_para()
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline(m_ol.group(2))}</li>")
            i += 1
            continue

        if line.strip() == "---":
            flush_para()
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        para.append(line.strip())
        i += 1

    flush_para()
    close_lists()
    return title, "\n".join(out)


def build_html(md_path: Path) -> str:
    md = md_path.read_text(encoding="utf-8")
    title, body = md_to_html(md)
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    # Embed CSS so the HTML is self-contained for Playwright file:// load
    css = CSS_PATH.read_text(encoding="utf-8")
    style_tag = f"<style>\n{css}\n</style>"
    html_doc = template.replace(
        '<link rel="stylesheet" href="{{CSS_HREF}}">', style_tag
    )
    html_doc = html_doc.replace("{{TITLE}}", html.escape(title))
    html_doc = html_doc.replace("{{BODY}}", body)
    return html_doc


def render_pdf(html_doc: str, pdf_path: Path) -> None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as e:
        raise SystemExit(
            "Playwright is required. Install with:\n"
            "  pip install playwright\n"
            "  playwright install chromium\n"
            f"({e})"
        ) from e

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        html_file = Path(td) / "report.html"
        html_file.write_text(html_doc, encoding="utf-8")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(html_file.as_uri(), wait_until="networkidle")
            page.pdf(
                path=str(pdf_path),
                format="Letter",
                print_background=True,
                margin={
                    "top": "0cm",
                    "bottom": "0cm",
                    "left": "0cm",
                    "right": "0cm",
                },
                display_header_footer=False,
            )
            browser.close()


def main() -> None:
    ap = argparse.ArgumentParser(description="Render OpenBook report Markdown to PDF")
    ap.add_argument("markdown", type=Path, help="Path to REPORT.md")
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help="Output PDF path (default: alongside .md with .pdf)",
    )
    ap.add_argument(
        "--html-only",
        type=Path,
        default=None,
        help="Also write HTML to this path",
    )
    args = ap.parse_args()
    md_path = args.markdown.resolve()
    if not md_path.is_file():
        raise SystemExit(f"Not found: {md_path}")

    html_doc = build_html(md_path)
    if args.html_only:
        args.html_only.write_text(html_doc, encoding="utf-8")
        print(f"HTML -> {args.html_only}")

    pdf_path = args.output or md_path.with_suffix(".pdf")
    render_pdf(html_doc, pdf_path.resolve())
    print(f"PDF  -> {pdf_path.resolve()}")
    print("QA: open PDF - Georgia body, pen rooms, no browser URL/date footer.")


if __name__ == "__main__":
    main()

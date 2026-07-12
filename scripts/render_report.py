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
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSS_PATH = ROOT / "render" / "report.css"
TEMPLATE_PATH = ROOT / "render" / "template.html"

RECEIPT_KINDS = frozenset(
    {
        "command",
        "test",
        "pr",
        "commit",
        "path",
        "source",
        "pending-human",
        "other",
    }
)


def load_receipts_jsonl(path: Path) -> list[dict]:
    """Load receipts.jsonl; skip blank lines and invalid rows with a warning."""
    if not path.is_file():
        return []
    rows: list[dict] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except Exception as e:
            print(f"WARN: {path.name}:{lineno}: skip invalid JSON ({e})", file=sys.stderr)
            continue
        if not isinstance(obj, dict):
            print(f"WARN: {path.name}:{lineno}: skip non-object", file=sys.stderr)
            continue
        kind = str(obj.get("kind", "")).strip().lower()
        summary = str(obj.get("summary", "")).strip()
        if kind not in RECEIPT_KINDS or not summary:
            print(
                f"WARN: {path.name}:{lineno}: need kind+summary "
                f"(kind in {sorted(RECEIPT_KINDS)})",
                file=sys.stderr,
            )
            continue
        rows.append(obj)
    return rows


def format_receipt_bullet(obj: dict) -> str:
    kind = str(obj.get("kind", "other")).strip().lower()
    summary = str(obj.get("summary", "")).strip()
    detail = str(obj.get("detail", "")).strip()
    ref = str(obj.get("ref", "")).strip()
    extra = detail or ref
    if extra and extra not in summary:
        return f"- [{kind}] {summary} ({extra})"
    return f"- [{kind}] {summary}"


def fold_receipts_into_markdown(md: str, receipts: list[dict]) -> str:
    """Append jsonl receipts under ## Appendix; skip summaries already present."""
    if not receipts:
        return md
    m = re.search(r"^##\s+Appendix\s*$", md, re.MULTILINE)
    if not m:
        bullets = [format_receipt_bullet(r) for r in receipts]
        return md.rstrip() + "\n\n## Appendix\n\n" + "\n".join(bullets) + "\n"

    start = m.end()
    nxt = re.search(r"^##\s+", md[start:], re.MULTILINE)
    end = start + nxt.start() if nxt else len(md)
    appendix = md[start:end]
    to_add: list[str] = []
    for r in receipts:
        summary = str(r.get("summary", "")).strip()
        bullet = format_receipt_bullet(r)
        if summary and summary in appendix:
            continue
        if bullet in appendix:
            continue
        to_add.append(bullet)
    if not to_add:
        return md
    new_appendix = appendix.rstrip() + "\n" + "\n".join(to_add) + "\n"
    return md[:start] + new_appendix + md[end:]


def detect_length(md: str) -> str:
    m = re.search(
        r"^\*\*Length:\*\*\s*(Brief|Standard|Essay)\s*$",
        md,
        re.MULTILINE | re.IGNORECASE,
    )
    return m.group(1).title() if m else "Standard"


def read_minutes(md: str) -> int:
    words = len(re.findall(r"[A-Za-z0-9']+", md))
    return max(1, round(words / 220))


def md_to_html(md: str) -> tuple[str, str]:
    """Convert OpenBook markdown to HTML body + title. Stdlib only."""
    lines = md.replace("\r\n", "\n").split("\n")
    title = "OpenBook Report"
    length = detect_length(md)
    minutes = read_minutes(md)
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
    in_sixty = False
    sixty_first = False
    pre_buf: list[str] = []
    para: list[str] = []

    def flush_para() -> None:
        nonlocal para, sixty_first
        if not para:
            return
        text = " ".join(para).strip()
        para = []
        if not text:
            return
        if in_sixty and sixty_first:
            out.append(f'<p class="standfirst">{inline(text)}</p>')
            sixty_first = False
        else:
            out.append(f"<p>{inline(text)}</p>")

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_sixty() -> None:
        nonlocal in_sixty, sixty_first
        if in_sixty:
            out.append("</section>")
            in_sixty = False
            sixty_first = False

    def smarten(s: str) -> str:
        """Light micro-typography before HTML escape (quotes, dashes, spaces)."""
        s = re.sub(r" {2,}", " ", s)
        s = s.replace("---", "\u2014").replace("--", "\u2013")
        parts: list[str] = []
        open_dq = True
        for ch in s:
            if ch == '"':
                parts.append("\u201c" if open_dq else "\u201d")
                open_dq = not open_dq
            else:
                parts.append(ch)
        s = "".join(parts)
        s = re.sub(r"(?<=\w)'(?=\w)", "\u2019", s)
        s = re.sub(r"'(?=s\b)", "\u2019", s)
        return s

    def inline(s: str) -> str:
        s = html.escape(smarten(s))
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(
            r"\[([^\]]+)\]\(([^)]+)\)",
            r'<a href="\2">\1</a>',
            s,
        )
        return s

    PAGEBREAK = '<div class="pagebreak"></div>'

    def emit_pagebreak() -> None:
        """One break between blocks, never two: consecutive break-before
        elements render a blank page (the cover used to emit one and the
        first section heading immediately emitted another)."""
        if out and out[-1] != PAGEBREAK:
            out.append(PAGEBREAK)

    def parse_meta_line(raw: str) -> tuple[str, str] | None:
        m = re.match(r"\*\*([^*]+):\*\*\s*(.+)$", raw) or re.match(
            r"^([A-Za-z][^:]{0,40}):\s*(.+)$", raw
        )
        if not m:
            return None
        return m.group(1).strip(), m.group(2).strip()

    def emit_decision(kicker: str) -> None:
        """Emit a decision block; following paragraphs are question then context."""
        nonlocal i
        out.append('<div class="qblock">')
        out.append(f'<p class="decision-kicker">{inline(kicker)}</p>')
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        chunks: list[str] = []
        buf: list[str] = []
        while i < len(lines) and not lines[i].startswith("#"):
            if not lines[i].strip():
                if buf:
                    chunks.append(" ".join(buf))
                    buf = []
                    if len(chunks) >= 2:
                        i += 1
                        break
                i += 1
                continue
            buf.append(lines[i].strip())
            i += 1
        if buf:
            chunks.append(" ".join(buf))
        if chunks:
            out.append(f'<p class="q">{inline(chunks[0])}</p>')
            if len(chunks) > 1:
                out.append(f'<p class="ctx">{inline(" ".join(chunks[1:]))}</p>')
        out.append('<div class="penroom"></div>')
        out.append("</div>")

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
            close_sixty()
            title = line[2:].strip()
            if not has_cover_section:
                out.append(f'<div class="cover"><h1>{inline(title)}</h1></div>')
                emit_pagebreak()
            i += 1
            continue

        if line.startswith("## "):
            flush_para()
            close_lists()
            h = line[3:].strip()
            if h.lower() == "cover":
                close_sixty()
                i += 1
                fields: dict[str, str] = {}
                cover_title = title
                dek = ""
                while i < len(lines) and not lines[i].startswith("## "):
                    raw = lines[i].strip()
                    if raw:
                        parsed = parse_meta_line(raw)
                        if parsed:
                            key, val = parsed
                            kl = key.lower()
                            if kl == "title":
                                cover_title = val
                                title = cover_title
                            elif kl == "subtitle":
                                dek = val
                            else:
                                fields[kl] = val
                    i += 1
                out.append('<div class="cover">')
                out.append(f"<h1>{inline(cover_title)}</h1>")
                if dek:
                    out.append(f'<p class="dek">{inline(dek)}</p>')
                # Byline: Author · When · N-min read (For/Length/Stats ignored here)
                byline_bits: list[str] = []
                if fields.get("author"):
                    byline_bits.append(inline(fields["author"]))
                if fields.get("when"):
                    byline_bits.append(inline(fields["when"]))
                byline_bits.append(f"{minutes}-min read")
                out.append(
                    '<p class="byline">' + " · ".join(byline_bits) + "</p>"
                )
                out.append('<div class="masthead-rule" aria-hidden="true"></div>')
                out.append("</div>")
                # Brief: no pagebreak after cover — lede opens the page
                if length != "Brief":
                    emit_pagebreak()
                continue
            close_sixty()
            if out and length != "Brief":
                emit_pagebreak()
            if h.lower() in (
                "two minutes",
                "sixty seconds",
                "the sixty-second version",
            ):
                cls = "sixty brief-lede" if length == "Brief" else "sixty"
                out.append(f'<section class="{cls}">')
                out.append(f"<h2>{inline(h)}</h2>")
                in_sixty = True
                sixty_first = True
                i += 1
                continue
            out.append(f"<h2>{inline(h)}</h2>")
            i += 1
            continue

        if line.startswith("### "):
            flush_para()
            close_lists()
            h = line[4:].strip()
            m_dec = re.match(r"^Decision\s+(\d+)\s*·\s*(.+)$", h, re.IGNORECASE)
            if m_dec:
                emit_decision(f"Decision {m_dec.group(1)} · {m_dec.group(2).strip()}")
                continue
            if re.match(r"^\d+\.\s*", h) or h.startswith("[?]"):
                emit_decision(h)
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
    close_sixty()
    body = "\n".join(out)
    # Wrap so CSS can key off length (Brief suppresses sixty H2)
    body = f'<article class="report length-{length.lower()}">\n{body}\n</article>'
    return title, body


def build_html(md_path: Path, receipts_path: Path | None = None) -> str:
    md = md_path.read_text(encoding="utf-8")
    jsonl = receipts_path or (md_path.parent / "receipts.jsonl")
    receipts = load_receipts_jsonl(jsonl)
    if receipts:
        md = fold_receipts_into_markdown(md, receipts)
        print(f"Receipts folded: {len(receipts)} from {jsonl.name}")
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
    ap.add_argument(
        "--receipts",
        type=Path,
        default=None,
        help="receipts.jsonl to fold into Appendix (default: beside the .md)",
    )
    args = ap.parse_args()
    md_path = args.markdown.resolve()
    if not md_path.is_file():
        raise SystemExit(f"Not found: {md_path}")

    html_doc = build_html(md_path, receipts_path=args.receipts)
    if args.html_only:
        args.html_only.write_text(html_doc, encoding="utf-8")
        print(f"HTML -> {args.html_only}")

    pdf_path = args.output or md_path.with_suffix(".pdf")
    render_pdf(html_doc, pdf_path.resolve())
    print(f"PDF  -> {pdf_path.resolve()}")
    print("QA: open PDF — body serif, pen rooms, no browser URL/date footer.")


if __name__ == "__main__":
    main()

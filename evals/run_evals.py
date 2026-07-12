#!/usr/bin/env python3
"""OpenBook eval harness v0.

Layer 1 (CI): run check_report.py on known-good examples and expect
broken.md to fail.

Layer 3 (hooks): score a candidate report against seeded-flaw ground truth
(failure recall, decision recall, invented timestamps). Claim precision is a
documented stub for a future judge model.

Usage:
  python evals/run_evals.py              # Layer 1
  python evals/run_evals.py --layer3 path/to/REPORT.md
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from check_report import check  # noqa: E402

MUST_PASS = [
    ROOT / "examples" / "before-after" / "after-brief.md",
    ROOT / "examples" / "before-after" / "after-standard.md",
    ROOT / "examples" / "before-after" / "after-essay.md",
    ROOT / "examples" / "parallel-night" / "REPORT.md",
]

MUST_FAIL = [
    ROOT / "evals" / "fixtures" / "broken.md",
]

SEEDED_TRUTH = (
    ROOT / "evals" / "fixtures" / "seeded-flaw" / "ground-truth.yaml"
)

ISO_TS_RE = re.compile(
    r"\b20\d{2}-\d{2}-\d{2}"
    r"(?:[T ]\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:?\d{2})?)?\b"
)


@dataclass
class Layer3Result:
    failure_recall: float
    decision_recall: float
    invented_timestamps: list[str]
    missed_dead_ends: list[str]
    missed_forks: list[str]
    claim_precision: str  # stub


def _load_truth(path: Path) -> dict:
    """Minimal YAML subset reader (lists of maps with scalar fields)."""
    text = path.read_text(encoding="utf-8")
    data: dict = {
        "dead_ends": [],
        "masked_failures": [],
        "decision_forks": [],
        "known_timestamps": [],
    }
    section: str | None = None
    current: dict | None = None

    def push() -> None:
        nonlocal current
        if section and current is not None:
            data[section].append(current)
        current = None

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if re.match(r"^[a-z_]+:\s*$", line):
            push()
            section = line.strip().rstrip(":")
            if section not in data:
                data[section] = []
            continue
        if section is None:
            continue
        m_item = re.match(r"^  - id:\s*(.+)$", line)
        if m_item:
            push()
            current = {"id": m_item.group(1).strip(), "must_mention_any": []}
            continue
        if current is None and section == "known_timestamps":
            m_ts = re.match(r'^  - "([^"]+)"\s*$', line)
            if m_ts:
                data["known_timestamps"].append(m_ts.group(1))
            continue
        if current is None:
            continue
        m_sum = re.match(r"^    summary:\s*(.+)$", line)
        if m_sum:
            current["summary"] = m_sum.group(1).strip()
            continue
        if line.strip() == "must_mention_any:":
            continue
        m_any = re.match(r'^      - (.+)$', line)
        if m_any and "must_mention_any" in current:
            val = m_any.group(1).strip().strip('"').strip("'")
            current["must_mention_any"].append(val)
    push()
    return data


def _mentions_any(text: str, needles: list[str]) -> bool:
    lower = text.lower()
    return any(n.lower() in lower for n in needles)


def score_layer3(report_md: str, truth: dict) -> Layer3Result:
    failures = truth.get("dead_ends", []) + truth.get("masked_failures", [])
    forks = truth.get("decision_forks", [])
    known = set(truth.get("known_timestamps", []))

    hit_f = [f for f in failures if _mentions_any(report_md, f.get("must_mention_any", []))]
    miss_f = [f["id"] for f in failures if f not in hit_f]
    hit_d = [f for f in forks if _mentions_any(report_md, f.get("must_mention_any", []))]
    miss_d = [f["id"] for f in forks if f not in hit_d]

    found_ts = ISO_TS_RE.findall(report_md)
    invented = [t for t in found_ts if t not in known]

    return Layer3Result(
        failure_recall=(len(hit_f) / len(failures)) if failures else 1.0,
        decision_recall=(len(hit_d) / len(forks)) if forks else 1.0,
        invented_timestamps=invented,
        missed_dead_ends=miss_f,
        missed_forks=miss_d,
        claim_precision=(
            "stub: wire a judge model that traces each sixty-second claim "
            "to a transcript span; untraceable claims are hallucinations"
        ),
    )


def run_layer1() -> int:
    failed = 0
    print("=== Layer 1: structural checks ===")

    for path in MUST_PASS:
        if not path.is_file():
            print(f"FAIL: missing must-pass example: {path}")
            failed += 1
            continue
        errors, warnings = check(path.read_text(encoding="utf-8"))
        for w in warnings:
            print(f"WARN {path.name}: {w}")
        if errors:
            print(f"FAIL {path.name}: expected pass")
            for e in errors:
                print(f"  {e}")
            failed += 1
        else:
            print(f"PASS {path.name}")

    for path in MUST_FAIL:
        if not path.is_file():
            print(f"FAIL: missing must-fail fixture: {path}")
            failed += 1
            continue
        errors, _warnings = check(path.read_text(encoding="utf-8"))
        if errors:
            print(f"PASS {path.name} (failed as expected, {len(errors)} error(s))")
        else:
            print(f"FAIL {path.name}: expected structural failure, got clean pass")
            failed += 1

    if failed:
        print(f"Layer 1 FAILED ({failed} problem(s))")
        return 1
    print("Layer 1 PASSED")
    return 0


def run_layer3(report_path: Path) -> int:
    print("=== Layer 3: faithfulness hooks ===")
    if not report_path.is_file():
        print(f"FAIL: report not found: {report_path}")
        return 1
    if not SEEDED_TRUTH.is_file():
        print(f"FAIL: ground truth not found: {SEEDED_TRUTH}")
        return 1

    truth = _load_truth(SEEDED_TRUTH)
    result = score_layer3(report_path.read_text(encoding="utf-8"), truth)
    print(f"failure_recall:  {result.failure_recall:.2f}")
    print(f"decision_recall: {result.decision_recall:.2f}")
    print(f"invented_timestamps: {result.invented_timestamps or '(none)'}")
    if result.missed_dead_ends:
        print(f"missed failures: {', '.join(result.missed_dead_ends)}")
    if result.missed_forks:
        print(f"missed forks: {', '.join(result.missed_forks)}")
    print(f"claim_precision: {result.claim_precision}")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description="OpenBook eval harness v0")
    ap.add_argument(
        "--layer3",
        type=Path,
        metavar="REPORT.md",
        help="Score REPORT.md against seeded-flaw ground truth",
    )
    args = ap.parse_args()
    if args.layer3:
        sys.exit(run_layer3(args.layer3))
    sys.exit(run_layer1())


if __name__ == "__main__":
    main()

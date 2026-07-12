# Receipts-path fixture

Proves `receipts.jsonl` folds into Appendix on render, and the report stays checker-clean.

```bash
python scripts/check_report.py evals/fixtures/receipts-path/REPORT.md
python scripts/render_report.py evals/fixtures/receipts-path/REPORT.md --html-only /tmp/receipts-path.html
```

See [docs/receipts.md](../../../docs/receipts.md).

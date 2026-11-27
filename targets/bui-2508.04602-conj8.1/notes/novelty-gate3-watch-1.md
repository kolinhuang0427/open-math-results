# Gate 3 Novelty Receipt — `bui-2508.04602-conj8.1`

- **UTC Time:** `2026-11-27T09:12Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 607 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2508.04602`, `"Hong Duc Bui"`, `"double circle order type"`.
   - `.venv/bin/python tools/novelty_grep.py 2508.04602 "Hong Duc Bui" "double circle order type"` -> `1` hit (`AlexenderSokolov__cross-theory-formal-database`, license file `arxiv-2508.04602-CC-BY-4.0.txt` only).
2. **Live Zenodo and GitHub Issues (`2026-11-27T09:11Z`):**
   - `https://zenodo.org/api/records?q=2508.04602&size=3` -> `total: 0`.
   - `gh search issues "2508.04602"` -> only `We-Solve/research#56` (`closed`, literature report on Bui 2025 Thms 7.1–7.2 double-circle universality; does not address §8.2 acyclicity).

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.

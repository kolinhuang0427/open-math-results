# Gate 2 Novelty Receipt (`watch-1`) — `targets/bui-2508.04602-conj8.1/`

- **Checked UTC:** `2026-11-27T09:06Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 605 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2508.04602`, `"Hong Duc Bui"`, `"double circle order type"`.
   - `.venv/bin/python tools/novelty_grep.py 2508.04602 "Hong Duc Bui" "double circle order type"` -> `1` hit (`AlexenderSokolov__cross-theory-formal-database`, license file `arxiv-2508.04602-CC-BY-4.0.txt` only).
2. **Live GitHub Issues & Zenodo (`2026-11-27T09:05Z`):**
   - `gh search issues "2508.04602"` -> **Near miss:** `We-Solve/research#56` (`closed`, `2026-10-18`, *"Attempt: TOP-5500038"*): literature report on Bui (2025) Theorems 7.1–7.2 (double-circle universality) with a 12-point `(2,2,2,2)` generalized-double-circle certificate; does **not** address Section 8.2's acyclicity conjecture for the triangle-matching flip graph $G$.
   - `https://zenodo.org/api/records?q=2508.04602&size=5` -> `total: 0`.

## Coverage Limits
- `gh search code "2508.04602"` hit GitHub secondary rate limit (HTTP 429, 137s cooldown); closed-access venues and private repositories not covered.

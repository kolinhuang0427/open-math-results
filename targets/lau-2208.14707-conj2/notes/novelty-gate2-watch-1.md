# Gate 2 Novelty Receipt (`watch-1`) — `targets/lau-2208.14707-conj2/`

- **Checked UTC:** `2026-11-27T09:13Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 608 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2208.14707`, `"dml.2022.149"`, `"Gee-Choon"`, `"Wai-Chee"`, `"local antimagic"`.
   - `.venv/bin/python tools/novelty_grep.py 2208.14707 "dml.2022.149" "Gee-Choon" "Wai-Chee" "local antimagic"` -> `1` unrelated hit (`kyleglsn22-spec/open-problems-lab`, Bača et al. 2022 leaf conjecture for trees).
2. **Live arXiv, Zenodo, and GitHub Issues (`2026-11-27T09:13Z`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2208.14707` -> `2208.14707v1` (`2022-08-31`) sole version.
   - `https://zenodo.org/api/records?q=2208.14707&size=5` -> `total: 0`.
   - `gh search issues "2208.14707"` and `"local antimagic lexicographic"` -> `0` issues.

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.

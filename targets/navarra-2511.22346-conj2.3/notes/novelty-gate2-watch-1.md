# Gate 2 Novelty Receipt (`watch-1`) — `targets/navarra-2511.22346-conj2.3/`

- **Checked UTC:** `2026-11-27T09:08Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 605 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2511.22346`, `"Navarra"`, `"Qureshi"`, `"switching rook"`.
   - `.venv/bin/python tools/novelty_grep.py 2511.22346 "Navarra" "Qureshi" "Rinaldo" "switching rook"` -> `12` lines across `5/605` files (`aliromman/math#64` Mascia–Rinaldo–Romeo zig-zag walks / prime polyomino ideals, and recent Nov 2026 arXiv preprints by Navarra/Qureshi on simplicial forests, join-meet ideals, nearly determinantal matrices — all unrelated to `2511.22346` Conjecture 2.3).
2. **Live arXiv, Zenodo, and GitHub Issues (`2026-11-27T09:08Z`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2511.22346` -> `2511.22346v1` (`2025-11-27T11:36:19Z`) sole version.
   - `https://zenodo.org/api/records?q=2511.22346&size=5` -> `total: 0`.
   - `gh search issues "2511.22346"` and `"Navarra polyomino"` -> `0` issues.

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.

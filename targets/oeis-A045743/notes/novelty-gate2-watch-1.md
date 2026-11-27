# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A045743/`

- **Checked UTC:** `2026-11-27T09:19Z`
- **Target:** OEIS `A045743` — R. J. Mathar (Jul 26, 2022) D-finite recurrence conjecture ($\sum_{j=0}^4 C_j(n)\,a(n-j)=0$ for $n \ge 6$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A045743 045743`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `08:49Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live OEIS (`https://oeis.org/search?q=id:A045743&fmt=json`):** `1` result (`number: 45743`, updated `2022-07-26T14:31:19-04:00`, rev. 14); Mathar's Jul 26, 2022 recurrence remains listed as `Conjecture`, matching `TARGET.md`.
3. **Live arXiv (`tools/arxiv_fetch.py query 'all:"A045743"'`):** `0` results.
4. **Live Zenodo API (`https://zenodo.org/api/records?q=A045743&size=5`):** `0` hits (`total: 0`).
5. **Web search (`"A045743" "Mathar" OR "D-finite" OR "rooted"`):** `0` proof hits found.

## Coverage Limits
- Live GitHub Search API (`gh search issues/prs`) was avoided due to the active HTTP 403 rate-limit window from `09:17Z`; mitigated by `608`-file `watch/snapshots/**` grep (`1337isnot1337/solved-conjectures` rebuilt `08:49Z` and `trureturing` trees) plus live OEIS, arXiv, Zenodo, and web search.

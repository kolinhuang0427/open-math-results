# Gate 3 Novelty Receipt (`watch-6`) — `targets/benfield-2407.20048-conj5.3/` (Rescoped Strictly to Clause (vi))

- **Checked UTC:** `2026-11-27T09:19:49Z` (`<1h` before submission)
- **Target:** Benfield–Lippard `arXiv:2407.20048v2` Section 5, Conjecture 5.3 (`\label{finite-orders}`), **clause (vi) only** (prior refutation of clause (v) by `the-omega-institute/trureturing#9448` / PR `#9451` already credited in `CONTESTED.md`, `TARGET.md`, `COUNTEREXAMPLE.md`, and `AUDIT.md`)
- **Verdict:** **PASS** (clause (vi) remains open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2407.20048" "finite-orders" "(3,4)-Fibonacci" "infinite in all other cases"`: `0` lines across `0/608` snapshot files.
- `gh search repos "2407.20048" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "2407.20048" --limit 10 --json repository,number,title,state,url`:
  1. `the-omega-institute/trureturing#9448` (`closed`): clause (v) only (`(3,2)-Fibonacci`, already credited).
  2. `the-omega-institute/trureturing#23317` (`open`): Question 4.34 even-$K$ dyadic threshold; explicitly states *"It also does not settle arbitrary-(a,b) Conjecture 5.3"*.
  3. `the-omega-institute/trureturing#23099` (`open`): `arXiv:2404.08193` Conjecture 10.4. Unrelated.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"2407.20048" OR (au:"Benfield" AND ti:"Pisano")'`: `1` entry (`2407.20048v2` itself, updated `2025-01-30`).
- Zenodo API (`https://zenodo.org/api/records?q=%222407.20048%22&size=5`): `0` records.
- `search_web` (`"2407.20048" OR "finite-orders" "(3,4)-Fibonacci" "Benfield" "Lippard"`): no published refutation or proof of clause (vi) found.

## Coverage Limits
- `gh search code "2407.20048"` returned HTTP 429 rate limit (`try again in 348.2s`); GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

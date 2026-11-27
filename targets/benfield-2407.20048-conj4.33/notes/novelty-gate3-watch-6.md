# Gate 3 Novelty Receipt (`watch-6`) — `targets/benfield-2407.20048-conj4.33/`

- **Checked UTC:** `2026-11-27T09:28:57Z` (`<1h` before submission)
- **Target:** Benfield–Lippard, `arXiv:2407.20048v2` Section 4.2, Conjecture 4.33 (`\label{even-K-exceptions}`), all even $K \in \mathbb{Z}$, all $m > 3$
- **Verdict:** **PASS** (no settled result or near-settled PR settles Conjecture 4.33)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "even-K-exceptions" "2407.20048"`: `0` lines across `0/608` snapshot files.
- `gh search repos "2407.20048" --limit 5 --json fullName,url`: `[]`
- `gh search issues "2407.20048" --limit 10 --json repository,number,title,state,url`:
  - `the-omega-institute/trureturing#9448` (`closed`): Conjecture 5.3(v) only; unrelated.
  - `the-omega-institute/trureturing#23099` (`open`): `2404.08193` Conj. 10.4; unrelated.
  - `the-omega-institute/trureturing#23317`: verified unchanged (`state: open`, `comments: 0`, `updated_at: 2026-10-28T20:05:07Z`); unproved preregistration for Question 4.34 ($0 < K, 4 \mid m$) explicitly excluding Conjecture 4.33 (disclosed in `notes/novelty-gate2-watch-6.md`).
- Zenodo API (`https://zenodo.org/api/records?q=%222407.20048%22&size=5`): `0` records.
- arXiv (`09:23Z`) & `search_web` (`09:19Z`): `2407.20048v2` latest; no published resolution of Conjecture 4.33.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos`, `gh search issues`, and `gh api` on `trureturing#23317`.

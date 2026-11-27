# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A077026/`

- **Checked UTC:** `2026-11-27T10:48:00Z`–`2026-11-27T10:48:11Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A077026` (rev. 14) — Benedict W. J. Irwin (Sep 22 2016) modulo sum conjecture (refuted for all $n \ge 1$ with exact offset $S(n) = a(n) - 1$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... "A077026" ...` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/635` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A077026&fmt=json`):** `ID: 77026`, `rev: 14` (`time: 2016-09-27T06:14:53-04:00`); `FORMULA` remains `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A077026&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A077026"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (Gate 2 `10:43Z`):** `0` mathematical refutations or corrections found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:48Z` returned `0` hits.

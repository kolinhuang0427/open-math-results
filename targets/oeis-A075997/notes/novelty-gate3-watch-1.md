# Gate 3 Novelty Receipt (`watch-1`): `targets/oeis-A075997/`

- **Checked UTC:** `2026-11-27T10:48:00Z`–`2026-11-27T10:48:11Z` (post-`AUDIT.md` PASS)
- **Target:** OEIS `A075997` (rev. 37) — Benedict W. J. Irwin (Sep 23 2016) modulo sum conjecture $a(n) = \sum_{k=1}^{n-1} f(n+k, n-k)$
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... "A075997"` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `0/635` files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A075997&fmt=json`):** `ID: 75997`, `rev: 37` (`time: 2025-06-14T09:50:29-04:00`); `FORMULA` remains `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A075997&size=3`):** `0` hits (`total: 0`).
4. **Live GitHub (`gh search issues/prs/repos "A075997"`):** `0` issues, `0` PRs, `0` repos.
5. **Web search (Gate 2 `10:43Z`):** `0` mathematical proofs found.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26) and live `gh search` at `10:48Z` returned `0` hits.

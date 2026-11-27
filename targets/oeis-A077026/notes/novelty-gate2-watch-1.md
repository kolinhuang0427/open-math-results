# Gate 2 Novelty Receipt (`watch-1`): `targets/oeis-A077026/`

- **Checked UTC:** `2026-11-27T10:42:45Z`–`2026-11-27T10:43:12Z`
- **Target:** OEIS `A077026` (rev. 14) — Benedict W. J. Irwin (Sep 22 2016) modulo sum conjecture $a(n) = \sum_{k=1}^{n-1} (1 - f(n, k))$ (refuted for all $n \ge 1$)
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... "A077026" ...` & `grep zenodo-23112421-oeis-ids.md`):** `0` hits across `619` snapshot files (`1337isnot1337/solved-conjectures` refreshed `10:20:09Z`, `trureturing*`, `openai/math`, `formal-conjectures`, `watch/snapshots/discovered/`, and `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **Live OEIS (`https://oeis.org/search?q=id:A077026&fmt=json`):** `ID: 77026`, `rev: 14` (`time: 2016-09-27T06:14:53-04:00`); `FORMULA` remains prefixed `Conjecture:`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A077026&size=3`):** `0` hits (`total: 0`).
4. **Web search (`... OR ("A077026" "Irwin") ...`):** `0` mathematical refutations or corrections found for `A077026`.

## Coverage Limits
- `1337isnot1337/solved-conjectures` snapshot refreshed at `2026-11-27T10:20:09Z` (Sweep 26); live `gh search` on `A077026` skipped during this batch (checked in Gate 1 with `0` hits).

# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A121580/`

- **Checked UTC:** `2026-11-27T09:37:34Z` (`<1h` before submission)
- **Target:** OEIS `A121580` — R. J. Mathar's Jul 26 2022 conjectured 4th-order D-finite recurrence ($n \ge 5$)
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A121580" "A121584"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A121580" --limit 5 --json fullName,url`: `[]`
- `gh search issues "A121580" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A121580&fmt=json`): active (`audit-2` verified rev. 12 `Conjecture`).
- Zenodo API (`https://zenodo.org/api/records?q=A121580&size=5`): `0` records.
- arXiv (`09:30Z`) & `search_web` (`09:30Z`): `0` proofs found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

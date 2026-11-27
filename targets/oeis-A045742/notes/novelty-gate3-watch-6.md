# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A045742/`

- **Checked UTC:** `2026-11-27T09:35:29Z` (`<1h` before submission)
- **Target:** OEIS `A045742` — R. J. Mathar's Jul 26 2022 conjectured 3rd-order D-finite recurrence ($n \ge 5$)
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A045742"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A045742" --limit 5 --json fullName,url`: `[]`
- `gh search issues "A045742" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A045742&fmt=json`): still marked `Conjecture D-finite with recurrence ...` (`audit-1` verified rev. 20).
- Zenodo API (`https://zenodo.org/api/records?q=A045742&size=5`): `0` records.
- arXiv (`09:31Z`) & `search_web` (`09:31Z`): `0` proofs found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A121751/`

- **Checked UTC:** `2026-11-27T09:36:12Z`
- **Target:** OEIS `A121751` — R. J. Mathar's Jul 26 2022 conjectured 6th-order D-finite recurrence ($n \ge 7$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A121751"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A121751" --limit 5 --json fullName,url`: `[]`
- `gh search issues "A121751" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A121751&fmt=json`, `A121751` rev. 5): Mathar's Jul 26 2022 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A121751"'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A121751&size=5`): `0` records.
- `search_web` (`"A121751" "Mathar" OR "D-finite" OR "recurrence"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

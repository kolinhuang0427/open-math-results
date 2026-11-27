# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A045742/`

- **Checked UTC:** `2026-11-27T09:31:42Z`
- **Target:** OEIS `A045742` — R. J. Mathar's Jul 26 2022 conjectured 3rd-order D-finite recurrence ($n \ge 5$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A045742"`: `0` hits across `608` snapshot files.
- `gh search repos "A045742" --limit 5 --json fullName,url`: `[]`
- `gh search issues "A045742" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A045742&fmt=json`, `A045742` rev. 20): Mathar's Jul 26 2022 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A045742" ...'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A045742&size=5`): `0` records.
- `search_web` (`"A045742" "Mathar" OR "D-finite" OR "recurrence"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

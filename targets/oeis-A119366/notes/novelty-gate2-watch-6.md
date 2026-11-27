# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A119366/`

- **Checked UTC:** `2026-11-27T09:24:07Z`
- **Target:** OEIS `A119366` — R. J. Mathar's Feb 03 2025 conjectured 7th-order D-finite recurrence ($n \ge 7$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A119366" "A045743"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A119366" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "A119366" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A119366&fmt=json`, `A119366` rev. 7): Mathar's Feb 03 2025 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A119366"'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A119366&size=5`): `0` records.
- `search_web` (`"A119366" "Mathar" OR "D-finite"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

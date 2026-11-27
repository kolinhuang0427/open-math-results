# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A168452/`

- **Checked UTC:** `2026-11-27T09:22:38Z`
- **Target:** OEIS `A168452` — R. J. Mathar's Nov 22 2024 conjectured 4th-order D-finite recurrence ($n \ge 4$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A168452"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A168452" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "A168452" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A168452&fmt=json`, `A168452` rev. 14): Mathar's Nov 22 2024 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A168452" ...'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A168452&size=5`): `0` records.
- `search_web` (`"A168452" "Mathar" OR "D-finite"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A121752/`

- **Checked UTC:** `2026-11-27T09:39:57Z`
- **Target:** OEIS `A121752` — R. J. Mathar's Jul 26 2022 conjectured 5th-order D-finite recurrence ($n \ge 6$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2303.08771" "A121754" "A121752"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A121752" --limit 5 --json fullName,url`: `[]`
- `gh search issues "A121752" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A121752&fmt=json`, `A121752` rev. 4): Mathar's Jul 26 2022 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A121754" OR all:"A121752"'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A121752&size=5`): `0` records.
- `search_web` (`("A121754" OR "A121752") "Mathar" OR "D-finite" OR "recurrence"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

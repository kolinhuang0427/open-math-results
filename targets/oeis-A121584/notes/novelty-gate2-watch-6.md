# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A121584/`

- **Checked UTC:** `2026-11-27T09:34:25Z`
- **Target:** OEIS `A121584` — R. J. Mathar's Jul 26 2022 conjectured 5th-order D-finite recurrence ($n \ge 6$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A121584"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A121584" --limit 5 --json fullName,url`: `1` hit `A121584/A121584` (verified via `gh api`: empty personal repo `"description": "hello"`, HTTP 404 on `/contents`).
- `gh search issues "A121584" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A121584&fmt=json`, `A121584` rev. 4): Mathar's Jul 26 2022 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A121584"'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A121584&size=5`): `0` records.
- `search_web` (`"A121584" "Mathar" OR "D-finite" OR "recurrence"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

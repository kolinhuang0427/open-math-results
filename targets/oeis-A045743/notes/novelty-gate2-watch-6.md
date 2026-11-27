# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A045743/`

- **Checked UTC:** `2026-11-27T09:19:49Z`
- **Target:** OEIS `A045743` — R. J. Mathar's Jul 26 2022 conjectured 4th-order D-finite recurrence ($n \ge 6$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A045743"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A045743" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "A045743" --limit 10 --json repository,number,title,state,url`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A045743&fmt=json`, `A045743`): Mathar's Jul 26 2022 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A045743" OR all:"A177260"'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A045743&size=5`): `0` records.
- `search_web` (`"A045743" "Mathar" OR "D-finite"`): no published proof found.

## Coverage Limits
- `gh search code "A045743"` returned HTTP 429 rate limit (`try again in 348.9s`); GitHub coverage relies on `watch/snapshots/discovered/` (`608` total snapshot files) plus live `gh search repos` and `gh search issues`.

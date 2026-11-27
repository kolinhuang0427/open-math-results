# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A121747/`

- **Checked UTC:** `2026-11-27T09:45:26Z`
- **Target:** OEIS `A121747` — R. J. Mathar's Jul 26 2022 conjectured 5th-order D-finite recurrence ($n \ge 6$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A121747" "A121750"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A121747" --limit 5`: `[]`
- `gh search issues "A121747" --limit 10`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A121747&fmt=json`, `A121747` rev. 15): Mathar's Jul 26 2022 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A121747" OR all:"A121750"'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A121747&size=5`): `0` records.
- `search_web` (`("A121747" OR "A121750") "Mathar" OR "D-finite" OR "recurrence"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

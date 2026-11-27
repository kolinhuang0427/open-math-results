# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A121750/`

- **Checked UTC:** `2026-11-27T09:45:26Z`
- **Target:** OEIS `A121750` — R. J. Mathar's Jul 26 2022 conjectured 6th-order D-finite recurrence ($n \ge 7$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A121747" "A121750"`: `0` lines across `0/608` snapshot files.
- `gh search repos "A121750" --limit 5`: `[]`
- `gh search issues "A121750" --limit 10`: `1` unrelated software issue (`GavinDu/Hephaestus#691`, HTTP 3xx/1xx player delegates).
- Live OEIS JSON (`https://oeis.org/search?q=id:A121750&fmt=json`, `A121750` rev. 13): Mathar's Jul 26 2022 formula remains marked `Conjecture D-finite with recurrence ...`.
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A121747" OR all:"A121750"'`: `0` entries.
- Zenodo API (`https://zenodo.org/api/records?q=A121750&size=5`): `0` records.
- `search_web` (`("A121747" OR "A121750") "Mathar" OR "D-finite" OR "recurrence"`): no published proof found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

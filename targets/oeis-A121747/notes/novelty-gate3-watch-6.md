# Gate 3 Novelty Receipt (`watch-6`) — `targets/oeis-A121747/`

- **Checked UTC:** `2026-11-27T10:03:54Z` (`<1h` before submission)
- **Target:** OEIS `A121747` — R. J. Mathar's Jul 26 2022 conjectured 5th-order D-finite recurrence ($n \ge 6$)
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "A121754" "A121752" "A121747"`: `0` lines across `0/618` snapshot files.
- `gh search repos "A121747" --limit 5`: `[]`
- `gh search issues "A121747" --limit 10`: `[]`
- Live OEIS JSON (`https://oeis.org/search?q=id:A121747&fmt=json`): active (`audit-1` verified rev. 15 `Conjecture`).
- Zenodo API (`https://zenodo.org/api/records?q=A121747&size=5`): `0` records.
- arXiv (`09:45Z`) & `search_web` (`09:45Z`): `0` proofs found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`618` snapshot files) plus live `gh search repos` and `gh search issues`.

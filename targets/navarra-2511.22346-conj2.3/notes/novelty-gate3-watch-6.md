# Gate 3 Novelty Receipt (`watch-6`) — `targets/navarra-2511.22346-conj2.3/`

- **Checked UTC:** `2026-11-27T09:22:38Z` (`<1h` before submission)
- **Target:** Navarra–Qureshi–Rinaldo `arXiv:2511.22346v1` Conjecture 2.3 (`\label{conj}`)
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2511.22346"`: `0` lines across `0/608` snapshot files.
- `gh search repos "2511.22346" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "2511.22346" --limit 10 --json repository,number,title,state,url`: `[]`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list ...2511.22346...`: `2511.22346v1` (`2025-11-27`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222511.22346%22&size=5`): `0` records.
- `search_web`: no published refutation found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown; GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

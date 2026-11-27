# Gate 3 Novelty Receipt (`watch-6`) — `targets/lau-2208.14707-conj2/`

- **Checked UTC:** `2026-11-27T09:23:25Z` (`<1h` before submission)
- **Target:** Lau–Shiu–Premalatha–Zhang–Nalliah `arXiv:2208.14707v1` / *Discrete Math. Lett.* 11 (2023) p. 82 Conjecture 2.2
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2208.14707"`: `0` lines across `0/608` snapshot files.
- `gh search repos "2208.14707" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "2208.14707" --limit 10 --json repository,number,title,state,url`: `[]`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list ...2208.14707...`: `2208.14707v1` (`2022-08-31`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222208.14707%22&size=5`): `0` records.
- `search_web` (`09:14Z`): returns only the source paper, no refutation found.

## Coverage Limits
- `gh search code` skipped due to active GitHub secondary rate-limit cooldown (was `[]` at `09:14Z` Gate 2 check); GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

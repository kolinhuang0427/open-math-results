# Gate 3 Novelty Receipt (`watch-6`) — `targets/iverson-2506.20778-conjPaley/`

- **Checked UTC:** `2026-11-27T09:19:49Z` (`<1h` before submission)
- **Target:** Iverson–Jasper–Mixon `arXiv:2506.20778v1` Conjecture 4.4 / Conjecture `conj:paley`
- **Verdict:** **PASS**

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2506.20778" "conj:paley" "Paley" "3696"`:
  - `3` lines across `2/608` files (`watch/snapshots/arxiv/citing_papers.json` and `citing_papers.md`), both recording `OpenAlex cited_by=0` for `2506.20778v1`.
  - `0` hits for `conj:paley` or competing Paley-theorem announcements.
- `gh search repos "2506.20778" --limit 5 --json fullName,updatedAt,url`: `[]`
- `gh search issues "2506.20778" --limit 10 --json repository,number,title,state,url`: returns `1` unrelated closed issue `the-omega-institute/trureturing#16342` (on `arXiv:2012.13642` Greaves–Iverson–Jasper–Mixon Example 5.8).
- `tools/arxiv_fetch.py query 'all:"2506.20778" OR all:"conj:paley"'`: `1` entry (`2506.20778v1` itself, sole version).
- Zenodo API (`https://zenodo.org/api/records?q=%222506.20778%22&size=5`): `0` records.
- `search_web` (`"2506.20778"`): no published proof of `conj:paley` / Conjecture 4.4 found.

## Coverage Limits
- `gh search code "2506.20778"` returned HTTP 429 rate limit (`try again in 347.9s`); GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

# Gate 2 Novelty Receipt (`watch-6`) — `targets/bartnicki-2303.08771-conj3/`

- **Checked UTC:** `2026-11-27T09:28:30Z`
- **Target:** Bartnicki–Czerwiński–Grytczuk–Miechowicz, `arXiv:2303.08771v1` (*Strong arboricity of graphs*), Section 5, Conjecture 3 ($\zeta(G) \le \mathrm{col}(G)$)
- **Verdict:** **PASS** (open and unclaimed)

## Exact Queries & Results
- `.venv/bin/python tools/novelty_grep.py "2303.08771" "Bartnicki"`: `0` lines across `0/608` snapshot files.
- `gh search repos "2303.08771" --limit 5 --json fullName,url`: `[]`
- `gh search issues "2303.08771" --limit 10 --json repository,number,title,state,url`: `[]`
- `.venv/bin/python tools/arxiv_fetch.py query --id-list 2303.08771`: `2303.08771v1` (`2023-03-15`) remains sole version.
- Zenodo API (`https://zenodo.org/api/records?q=%222303.08771%22&size=5`): `0` records.
- `search_web` (`"2303.08771" OR ("Bartnicki" "coloring" "zeta" OR "pigeonhole" OR "counterexample")`): returns only `2303.08771v1`; no refutation found.

## Coverage Limits
- `gh search code "2303.08771"` returned HTTP 429 rate limit (`try again in 571.6s`); GitHub coverage relies on `watch/snapshots/discovered/` (`608` snapshot files) plus live `gh search repos` and `gh search issues`.

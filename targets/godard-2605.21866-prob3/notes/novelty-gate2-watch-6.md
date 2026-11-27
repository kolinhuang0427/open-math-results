# Gate 2 Novelty Receipt (`watch-6`) — `targets/godard-2605.21866-prob3/`

- **Checked UTC:** `2026-11-27T09:15:15Z`
- **Verdict:** **PASS** (open; no determination of $s(n)$ for general $n \ge 4$ found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 608 files including 436+ `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2605.21866" "Godard" "p_0(n)"` -> `2605.21866` matched only `watch/snapshots/arxiv/` citing cache (`OpenAlex cited_by=0`) and `AlexenderSokolov/cross-theory-formal-database` license metadata; `0` hits in competing repos.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2605.21866"` -> `[]`.
   - `gh search issues "2605.21866"` -> `[]`.
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2605.21866`: `2605.21866v1` (`2026-05-21`) sole version.
   - `zenodo.org/api/records?q=2605.21866&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2605.21866" OR "Godard" "quadratic graph" OR "Paley" "n/p_0(n)" OR "connected" finite field` -> returns only `arXiv:2605.21866v1`; no resolution found.

## Coverage Limits
- Live `gh search code` was skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (608 files, 436+ `discovered/` repo snapshots) plus live `gh search repos`/`issues`, arXiv, Zenodo, and `search_web`.

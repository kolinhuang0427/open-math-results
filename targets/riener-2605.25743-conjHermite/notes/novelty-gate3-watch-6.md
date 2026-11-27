# Gate 3 Novelty Receipt (`watch-6`) — `targets/riener-2605.25743-conjHermite/`

- **Checked UTC:** `2026-11-27T09:07:30Z`
- **Verdict:** **PASS** (no competing proof or counterexample found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 605 files including 434 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2605.25743" "Hermite-matrix" "conj:hermite" "conj:sos"` -> `2605.25743` matched only `watch/snapshots/arxiv/` citing cache (`OpenAlex cited_by=0`) and `AlexenderSokolov/cross-theory-formal-database` (`editable-corpus/licenses/arxiv-2605.25743-CC-BY-4.0.txt`); `0` hits in competing repos.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2605.25743"` -> `[]`.
   - `gh search issues "2605.25743"` -> 1 unrelated hit: `the-omega-institute/trureturing#25877` (Breloer–Riener `arXiv:2606.18895v2` Conj 5.12).
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2605.25743`: `2605.25743v3` (`2026-10-21`) remains latest.
   - `zenodo.org/api/records?q=2605.25743&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2605.25743" OR "Riener" "Shapiro" "Hermite matrix" "SOS" proved OR counterexample` -> no resolution found.

## Coverage Limits
- Live `gh search code "2605.25743"` hit GitHub's shared rate limit (`HTTP 429`, ~20s remaining); code coverage rests on `watch/snapshots/**` (605 files, 434 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, arXiv, Zenodo, and `search_web`.

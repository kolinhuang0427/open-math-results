# Gate 2 Novelty Receipt (`watch-6`) — `targets/riener-2605.25743-conjHermite/`

- **Checked UTC:** `2026-11-27T08:56:00Z`
- **Verdict:** **PASS** (open; no full resolution found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2605.25743" "Hermite-matrix" "square-graph"` -> `2605.25743` matched only `AlexenderSokolov/cross-theory-formal-database` (`discovered/`, index catalog) and `watch/snapshots/arxiv/` citation cache (`citing=0`); **0 hits** in `1337-solved-conjectures/`, `openai-math/`, `ai-collections/`, or any competing proof repository. (`square-graph` hit in `oscar030406/math-conjecture-blitz` is `graffiti-pc-138` induced path / square-graph distance, unrelated.)
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 repos).
   - `gh search issues "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 issues/PRs).
3. **arXiv API (`tools/arxiv_fetch.py query --id-list ...,2605.25743,...`):**
   - `2605.25743v3` (updated `2026-10-21`) remains the latest version.
4. **Web search (`search_web`):**
   - Query: `"2605.25743" OR "Riener" "Shapiro" "Hermite matrix" "SOS" derivatives` -> returns only `2605.25743` itself; no external resolution or counterexample found.

## Near Misses
- **`arXiv:2605.25743v3` itself:** Proves $k \in \{0,1\}$ and $r = n-k \in \{2,3,4\}$ and centered outlier limit $3 \le r \le 6$, leaving $r \ge 5$ (`(n,k)=(7,2)` onward) open.
- **`oscar030406/math-conjecture-blitz` (`proofs/graffiti-pc-138`):** Unrelated graph-square distance conjecture.

## Coverage Limits
- Live `gh search code` returned `HTTP 429` (shared rate limit); code coverage rests on `watch/snapshots/**` (601 files, 430 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live arXiv API, and `search_web`.

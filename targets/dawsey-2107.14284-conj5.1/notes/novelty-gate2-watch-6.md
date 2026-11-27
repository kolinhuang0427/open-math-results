# Gate 2 Novelty Receipt (`watch-6`) — `targets/dawsey-2107.14284-conj5.1/`

- **Checked UTC:** `2026-11-27T08:56:00Z`
- **Verdict:** **PASS** (open; no proof or refutation found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2107.14284" "supernormal" "idx(p)"` -> 13 lines across 3 files in `watch/snapshots/arxiv/` (`citing_papers.{json,md}`, `last_sweep_report.json`); **0 hits** in `discovered/`, `1337-solved-conjectures/`, `openai-math/`, `ai-collections/`, or `formal/`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 repos).
   - `gh search issues "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 issues/PRs).
3. **arXiv API (`tools/arxiv_fetch.py query --id-list ...,2511.20829,...,2107.14284`):**
   - `2511.20829v1` (Robert Schneider, "Partition-theoretic model of prime distribution, II") is a computational model up to $n = 100{,}000$; does not address Conjecture 5.1.
4. **Web search (`search_web`):**
   - Query: `"2107.14284" OR "supernormal partition statistic" "Dawsey" "Conjecture 5.1" OR "idx(p)"` -> surfaces only `arXiv:2107.14284` / *J. Number Theory* 241 (2022) and related supernormal partition papers; no resolution of Conjecture 5.1 found.

## Near Misses
- **`arXiv:2511.20829v1` (Schneider 2025) & `arXiv:2501.00580` (Botkin et al. 2025):** Cite `2107.14284` for the partition-theoretic prime model, not Conjecture 5.1.

## Coverage Limits
- Live `gh search code` returned `HTTP 429` (shared rate limit); paywalled *J. Number Theory* 241 PDF was not fetched (arXiv `2107.14284v2` TeX inspected).

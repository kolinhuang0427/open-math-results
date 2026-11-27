# Gate 2 Novelty Receipt (`watch-6`) — `targets/haugland-2411.00721-ques2/`

- **Checked UTC:** `2026-11-27T08:56:00Z`
- **Verdict:** **PASS** (open; no full resolution found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots & 223 `mathesis-papers`):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2411.00721" "proper lifting" "Omland"` -> 12 lines across 3 files in `watch/snapshots/arxiv/` (`citing_papers.{json,md}`, `last_sweep_report.json`); **0 hits** in `discovered/`, `1337-solved-conjectures/`, `openai-math/`, `ai-collections/`, or `formal/`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 repos).
   - `gh search issues "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 issues/PRs).
3. **arXiv API (`tools/arxiv_fetch.py query --id-list 2609.35921,2610.33131,...,2411.00721`):**
   - `2411.00721v2` (updated `2026-11-01`) remains the latest version.
4. **Web search (`search_web`):**
   - Query: `"2411.00721" OR "proper lifting" "Haugland" "Omland" degree 2` -> returns only `arXiv:2411.00721` / *Designs, Codes and Cryptography* entry; no proof of nonexistence of degree-2 proper liftings for all diameters.

## Near Misses
- **`arXiv:2609.35921v1` (Houqiao Fu, 2026-09-28):** Proves every five-slot radius-two ($k = 5$) quadratic binary local rule is non-injective whenever $4 \mid n$ and $n \ge 8$. This settles only $k = 5$ (diameter $\le 5$), whereas `haugland-2411.00721-ques2` asks whether degree-2 proper liftings exist for *any* diameter $k$.
- **`arXiv:2610.33131v2` (Haugland–Larsen–Omland–Rustad, 2026-11-19):** Studies open and locally eventually onto cellular automata; does not address degree-2 proper liftings.

## Coverage Limits
- Live `gh search code` hit GitHub's shared secondary/rate limit (`HTTP 429`); GitHub code coverage relies on the 430 `discovered/` snapshots + `watch/snapshots/**` + live `gh search repos` and `gh search issues`.
- Paywalled journal versions or private repositories not indexed by arXiv, GitHub, or `search_web` are not covered.

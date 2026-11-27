# Gate 3 Novelty Receipt (`watch-6`) — `targets/haugland-2411.00721-ques2/`

- **Checked UTC:** `2026-11-27T09:01:00Z`
- **Verdict:** **PASS** (no competing proof or construction found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2411.00721" "proper lifting" "Omland"` -> hits only in `watch/snapshots/arxiv/` citing cache; `0` hits in `discovered/`, `1337-solved-conjectures/`, `openai-math/`, `ai-collections/`, or `formal/`.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "A190969 OR 2411.00721"` -> `[]`.
   - `gh search issues "A190969 OR 2411.00721"` -> `[]`.
3. **Live arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list ...,2411.00721`: `2411.00721v2` (`2026-11-01`) remains latest.
   - `zenodo.org/api/records?q=2411.00721&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2411.00721" OR "proper lifting" "Haugland" "Omland" degree 2` -> no proof of nonexistence for general diameter found.

## Near Misses
- `arXiv:2609.35921v1` (Houqiao Fu, `2026-09-28`): proves non-injectivity for $4 \mid n, n \ge 8$ for five-slot radius-two ($k = 5$) quadratic binary rules only, not general diameter $k$.
- `arXiv:2610.33131v2` (Haugland–Larsen–Omland–Rustad, `2026-11-19`): studies open/locally eventually onto cellular automata, unrelated to degree-2 proper liftings.

## Coverage Limits
- Live `gh search code "2411.00721"` hit GitHub's shared secondary/rate limit (`HTTP 429`); code coverage rests on `watch/snapshots/**` (601 files, 430 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, arXiv, Zenodo, and `search_web`.

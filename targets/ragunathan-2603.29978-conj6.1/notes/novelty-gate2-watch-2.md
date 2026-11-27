# Gate 2 Novelty Receipt — `ragunathan-2603.29978-conj6.1`

- **UTC Time:** 2026-11-27T01:51:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #604)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "2603.29978" "Ragunathan" "Van Tuyl" "vdw(n,k)"`: 0 hits across 369 files (`1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `formal`, `arxiv`, `discovered`).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `query --id-list 2603.29978`: `2603.29978v2` (updated `2026-08-19T19:41:32Z`, no journal-ref/DOI) remains latest.
3. **Live GitHub (`gh api`, read-only):**
   - Repo-scoped `search/issues` & `search/code` for `2603.29978`, `Ragunathan`, and `vdw(n,k)` across `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`: 0 relevant hits (`vdw(n,k)` matched only an unrelated closed clock-risk screen in `trureturing`).
   - Global `search/issues?q=2603.29978`: 0 hits.
4. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=2603.29978+OR+%22van+der+Waerden+Simplicial%22`: `total: 0`.
   - `search_web` for `"2603.29978" OR ("van der Waerden Simplicial Complex" "Lefschetz")`: returns only `2603.29978`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2603.29978v2` itself settles $k \in \{1, 2, 3, n-1\}$ and states Conjecture 6.1 as open for $k \ge 4$.

## What Was Not Covered

- Closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, or web search.

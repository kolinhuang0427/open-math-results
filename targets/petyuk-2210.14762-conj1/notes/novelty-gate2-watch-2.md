# Gate 2 Novelty Receipt — `petyuk-2210.14762-conj1`

- **UTC Time:** 2026-11-27T01:51:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #604)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "2210.14762" "Petyuk" "simplified de Bruijn"`: 0 hits across 369 files (`1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `formal`, `arxiv`, `discovered`).
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `query --id-list 2210.14762,2312.10377,2605.02268`: `2210.14762v2` remains latest; `2312.10377v1` (Huang–Kitaev–Pyatkin) and `2605.02268v2` (Roy–Hariharasubramanian) address distance-restricted $S_m(n,k)$ and shift graphs $G(n,k)$, leaving Petyuk's Conjecture 1 ($S(n,k)$ for $n \ge 4, k \ge 3$) open.
3. **Live GitHub (`gh api`, read-only):**
   - Repo-scoped `search/issues` & `search/code` for `2210.14762` and `Petyuk` across `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing*`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`: 0 hits for `2210.14762` (`Petyuk` code hits in `trureturing` are unrelated `aksoyetal2023asynchrony` references).
   - Global `search/issues?q=2210.14762`: 0 hits.
4. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=2210.14762+OR+%22simplified+de+Bruijn%22`: `total: 0`.
   - `search_web` for `"2210.14762" OR ("simplified de Bruijn" "word-representable" "S(4,3)" OR "counterexample")`: no prior refutation of $S(4,3)$ found.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2312.10377v1` (Huang–Kitaev–Pyatkin) and `arXiv:2605.02268v2` (Roy–Hariharasubramanian): prove word-representability of distance-restricted $S_m(n,k)$ and shift graphs $G(n,k)$, not $S(4,3)$ or $S(n,k)$ ($n \ge 4, k \ge 3$).

## What Was Not Covered

- Closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, or web search.

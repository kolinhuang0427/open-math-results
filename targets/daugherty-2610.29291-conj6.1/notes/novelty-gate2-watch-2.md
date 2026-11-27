# Gate 2 Novelty Receipt — `daugherty-2610.29291-conj6.1`

- **UTC Time:** 2026-11-27T00:48:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #508)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "2610.29291" "Daugherty" "Latin tableaux" "conj:box"`: 0 competing solution hits across `1337-solved-conjectures`, `openai-math`, `erdosproblems`, `ai-collections`, `formal`, `arxiv`, `discovered`.
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `query --id-list 2610.29291` -> `2610.29291v1` (submitted `2026-10-21T06:45:39Z`, no journal-ref/DOI) remains sole version.
3. **Live GitHub (`gh api`, read-only):**
   - Checked `pushed_at` of `1337isnot1337/solved-conjectures`, `the-omega-institute/trureturing`, `the-omega-institute/trureturing-tools`, `aliromman/math`, `KnowledgeSense/math`.
   - Live recursive trees of `aliromman/math` (515 paths), `trureturing-tools` (1764 paths), `KnowledgeSense/math` (5377 paths): 0 matches for `2610.29291`, `daugherty`, `conj:box` (`KnowledgeSense/math` `LatinTriangles.lean` is Tuza's conjecture, unrelated).
   - Repo-scoped `search/code` & `search/issues` for `2610.29291` and `Daugherty`:
     - `the-omega-institute/trureturing` `Library/Combinatorics/daugherty2026counting.md`, issues `#20269` / `#26377`, and PR `#20329`: target **Conjecture 6.3** (`LT((k,...,3,3)) = 9*4^{k-3}`) and **Conjecture 6.2** (column-addition monotonicity), and explicitly state *"Conjectures 6.1, 6.2 and the broader wide partition conjecture are separate assertions."*
   - Global `search/code?q=2610.29291` (56 total, top 10 inspected) and `search/issues?q=2610.29291` (1 hit, `trureturing#20269`).
4. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=2610.29291+OR+%22Latin+tableaux%22&size=10` -> 1 hit (`21718549`, 2026-07-31, LADA verification bundle for $5\times 5$ Latin tableau conjecture, predating `2610.29291`).
   - `search_web` for `"2610.29291" OR ("Daugherty" "Latin tableaux" "Conjecture 6.1")`: returns only `2610.29291v1`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute/trureturing` (`Problems/daugherty-latin-tableaux-conjecture63.md`, PR `#20329`, issue `#26377`): addresses Conjecture 6.3 (closed PR) and Conjecture 6.2 (open issue); does not settle or refute Conjecture 6.1 (`conj:box`, row-addition monotonicity on wide partitions).
- `rainwangphy/aftd-platform` (`lean/AFTD/Kb/Tcs/LatinTableauxCount.lean`, pushed `2026-11-27T00:40:28Z`): formalizes definitions (`IsLatinTableau`, `IsWidePartition`, `latin_tableaux_count`) from `arXiv:2610.29291` Section 4, not a counterexample to Conjecture 6.1.
- `elder-plinius/V3R1T4S` (`known-unknowns/erdos-and-proofs/latin-tableau-conjecture.md`): problem note on Chow et al.'s Latin Tableau Conjecture (existence, not `LT` monotonicity).

## What Was Not Covered

- Only top 10 global GitHub code-search results for `2610.29291` were inspected individually; closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, or web search.
- Also checked live `rainwangphy/aftd-platform` (28,161 tree paths: formalizes Conj 6.3 `LatinDoubleThreeTail*`, top-row Thm 5.2 `LatinTableauxCountMonoCellAdditionTopRow.lean`, and `(3,2,1)` only; nothing refuting Conj 6.1), `valyuAI/research` (`latin-tableaux-staircase-count` only, Conj 6.3), and `facebookresearch/atlas-lean` issues (0 hits for `2610.29291`; `Daugherty` hits are metered parking).

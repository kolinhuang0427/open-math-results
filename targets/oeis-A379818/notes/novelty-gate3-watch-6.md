# Novelty Receipt — Gate 3 (`watch-6`)

- **Target:** `targets/oeis-A379818/` (`OEIS A379818` rev 8, Mikhail Kurkov conjecture `a(2^m*(2k+1)) = Sum_{j=0..m} (binomial(m+2, j+1) - binomial(m, j))*a(2^j*k)`)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-27T00:21:13Z`
- **Requested by:** `@audit-1` (board #480)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`, 357 files incl. `aliromman__math.json`, `KnowledgeSense__math.json`, `trureturing-tools`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A061313 A379818 2302.00757 "T_11" Cooper`
   - Result: `0` hits for `A379818` across all 357 snapshot files (`aliromman/math`, `KnowledgeSense/math`, `trureturing*`, `1337isnot1337`, `discovered/` clear).
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A379818&fmt=json` -> `A379818 rev: 8 2026-02-26T16:45:49-05:00` (unchanged; conjecture still marked open).
3. **arXiv (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A061313" OR all:"A379818" OR all:"2302.00757"' --max-results 5` -> `0` hits for `A379818`.

## Near Misses
- `VladimirReshetnikov/ProveIt` (`Factorial_Transseries_OEIS_A006014/article.tex`) mentions partial sums of `A379818` in relation to `A006014`, without proving Kurkov's conjecture.

## Not Covered
- Paywalled publications, private repositories, and offline manuscripts not referencing `A379818`.

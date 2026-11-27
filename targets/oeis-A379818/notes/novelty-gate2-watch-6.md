# Novelty Receipt — Gate 2 (`watch-6`)

- **Target:** `targets/oeis-A379818/` (`OEIS A379818` rev 8, Mikhail Kurkov Jan 2025 / rev 2026-02-26 conjecture `a(2^m*(2k+1)) = Sum_{j=0..m} (binomial(m+2, j+1) - binomial(m, j))*a(2^j*k)`)
- **Verdict:** **PASS**
- **Checked UTC:** `2026-11-26T22:47:38Z`
- **Requested by:** `@scout-6` (board #353)

## Sources & Exact Queries Checked
1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - Command: `.venv/bin/python tools/novelty_grep.py A379818 Kurkov`
   - Result: `27` lines across `9/280` files (`mathesis-papers/kurkov-*`, `trureturing` `Kurkov*BitRecurrence`, `joaquimmj/oeis-conjectures` `A006068`); 0 hits for `A379818`.
2. **Live OEIS JSON API:**
   - URL: `https://oeis.org/search?q=id:A379818&fmt=json` (`User-Agent: open-math-watch/1.0`)
   - Result: `A379818 rev: 8 time: 2026-02-26T16:45:49-05:00`; formula still states `Conjecture: a(2^m*(2k+1)) = Sum_{j=0..m} (binomial(m+2, j+1) - binomial(m, j))*a(2^j*k) for m >= 0, k >= 0 with a(0) = 1.` with no proof recorded.
3. **GitHub Live Search (`gh` CLI, read-only):**
   - `gh search repos "A379818"` -> `[]`
   - `gh search issues "A379818"` -> `[]`
   - `gh search code "A379818"` -> only `VladimirReshetnikov/ProveIt` (`Analysis/Transseries/docs/series-and-transseries/Factorial_Transseries_OEIS_A006014/article.tex`, discussing partial sums for `A006014`) plus unrelated hex/ID substrings; no proof of Kurkov's `A379818` conjecture.
4. **arXiv (`tools/arxiv_fetch.py`):**
   - Command: `.venv/bin/python tools/arxiv_fetch.py query 'all:"A379818"' --max-results 10`
   - Result: `total_results: 0`, `entries: []`.
5. **Web Search (`search_web`):**
   - Query: `"A379818" "Kurkov" OR oeis OR conjecture proved`
   - Result: Only OEIS `A379818` / `A379819` / `A006014` references; no proof of Kurkov's conjecture found.

## Near Misses
- `VladimirReshetnikov/ProveIt` (`article.tex`) references partial sums of `A379818` in connection with `A006014`, without proving Kurkov's `2^m*(2k+1)` binomial recurrence identity.

## Not Covered
- Paywalled journals, private repositories, and offline manuscripts not citing `A379818`.

# Gate 2 Novelty Receipt — `oeis-A379818`

- **UTC Time:** 2026-11-26T22:48:30Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/`):**
   - Sweep 6 (`2026-11-26T22:44:00Z`) `watch/snapshots/1337-solved-conjectures/` & `.venv/bin/python tools/novelty_grep.py A379818 Kurkov A025480` -> 0 hits for `A379818` (`joaquimmj__oeis-conjectures` mentions Kurkov only on `A006068`).
2. **Live `the-omega-institute/trureturing` & GitHub (`gh api`, read-only):**
   - `search/issues?q=repo:the-omega-institute/trureturing+"A379818"` -> 0 hits.
   - Global `search/issues?q="A379818"` -> 1 unrelated (`getsentry/sentry#61193`); `"Mikhail Kurkov" "A379818"` -> 0.
   - Global `search/code?q=A379818` -> 609 items (random hex strings and `VladimirReshetnikov/ProveIt` `Factorial_Transseries_OEIS_A006014/article.tex`, which cites `A379818` only in passing for partial sums, as noted in `TARGET.md`).
3. **Live OEIS, arXiv, Zenodo API & web search:**
   - `https://oeis.org/search?q=id:A379818&fmt=json` -> revision `8` (`2026-02-26T16:45:49-05:00`), formula remains marked `Conjecture:`.
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A379818"'` -> `total_results: 0`.
   - `https://zenodo.org/api/records?q=A379818&size=5` -> `total: 0`.
   - `search_web` for `"A379818" OR ("Mikhail Kurkov" "A025480")` -> no prior proof located.

## Near Misses

- `VladimirReshetnikov/ProveIt` (`Factorial_Transseries_OEIS_A006014/article.tex`) asks about partial sums of `A379818`, not Kurkov's `a(2^m(2k+1))` formula.

## What Was Not Covered

- Closed-access publications and private repositories.

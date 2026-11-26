# Gate 2 Novelty Receipt — `oeis-A250917`

- **UTC Time:** 2026-11-26T20:52:10Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources & Exact Queries Checked

1. **Local watch snapshots (`watch/`):**
   - `.venv/bin/python tools/novelty_grep.py A250917 "C(x)^3" "exp( x*C(x)^3 )"` -> 0 hits across 224 files.
2. **GitHub API live searches (`gh api`, read-only):**
   - `search/code?q=A250917+D-finite` -> 1 hit (`gfis/OEIS-mat/contrib/rm/dfinite.grep.txt` quoting Mathar's Jan 2020 conjecture string verbatim, not a proof).
   - `search/code?q=repo:the-omega-institute/trureturing+A250917` -> 0 hits.
   - `search/code?q=repo:1337isnot1337/solved-conjectures+A250917` -> 0 hits.
   - `search/code?q=repo:joaquimmj/oeis-conjectures+A250917` -> 0 hits.
3. **arXiv API (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A250917"' --max-results 5` -> 0 hits.
4. **Web search (`search_web`):**
   - `"A250917" "D-finite" OR "exp(x*C(x)^3)" OR "11*n+20" proved OR recurrence` -> no prior proof of Mathar's order-5 recurrence located.

## Near Misses

- `gfis/OEIS-mat` (`contrib/rm/dfinite.grep.txt`): mirror of OEIS conjecture text only.

## What Was Not Covered

- Unindexed private repositories and print-only publications not citing `A250917`.

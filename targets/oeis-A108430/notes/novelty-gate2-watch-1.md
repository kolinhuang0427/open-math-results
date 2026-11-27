# Gate 2 Novelty Receipt — `oeis-A108430`

- **UTC Time:** 2026-11-26T21:17:55Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Sources & Exact Queries Checked

1. **Local watch snapshots (`watch/`):**
   - `.venv/bin/python tools/novelty_grep.py A108430 A108429 "23982"` -> 0 hits across 224 files.
2. **GitHub API live searches (`gh api`, read-only):**
   - `search/code?q=A108430+D-finite` -> 1 hit (`gfis/OEIS-mat/contrib/rm/dfinite.grep.txt` quoting Mathar's Jul 2022 conjecture string verbatim, not a proof).
   - `search/code?q=repo:the-omega-institute/trureturing+A108430` -> 0 hits.
   - `search/code?q=repo:1337isnot1337/solved-conjectures+A108430` -> 0 hits.
   - `search/code?q=repo:joaquimmj/oeis-conjectures+A108430` -> 0 hits.
3. **arXiv API (`tools/arxiv_fetch.py`):**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A108430"' --max-results 5` -> 0 hits.
4. **Zenodo API:**
   - `https://zenodo.org/api/records?q=A108430&size=5` -> `total: 0`.
5. **Web search (`search_web`):**
   - `"A108430" "Mathar" OR "Deutsch" "lattice paths"` -> returned only OEIS entries; no prior proof located.

## Near Misses

- `gfis/OEIS-mat` (`contrib/rm/dfinite.grep.txt`): mirror of OEIS conjecture text only.
- Emeric Deutsch (*Amer. Math. Monthly* 107, 2000, Problem 10658): enumerates `A108429`/`A108430` via `G = 1 + t z G^2 (1 + t G)`, not Mathar's 2022 D-finite recurrence.

## What Was Not Covered

- Print JSTOR text of Deutsch (2000), private repositories, and unindexed manuscripts.

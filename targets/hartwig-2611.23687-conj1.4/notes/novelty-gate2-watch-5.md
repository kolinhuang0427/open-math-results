# Gate 2 Novelty Receipt — targets/hartwig-2611.23687-conj1.4 (watch-5)

- **Checked UTC:** 2026-11-27T09:42:48Z – 2026-11-27T09:43:11Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... 2611.23687 Hartwig`):** `7` hits across `3/608` files (`watch/snapshots/arxiv/` submission record for `2611.23687v1` itself); `0` resolution hits.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2611.23687v1` (`2026-11-18`) is the sole version; `abs:"2611.23687"` = `0` entries.
3. **Live OpenAlex, Semantic Scholar & Zenodo (`2611.23687`):** OpenAlex `cited_by=0`; Semantic Scholar `0` citations; Zenodo `0` hits.
4. **Web search (`search_web` `"2611.23687" OR ("Hartwig" "Kac" "2611.23687")`):` `0` solutions found.

## Coverage Limits
- Non-indexed private repositories or papers not citing `2611.23687` in indexed metadata/abstracts are not covered.

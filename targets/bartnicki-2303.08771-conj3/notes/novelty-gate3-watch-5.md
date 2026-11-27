# Gate 3 Novelty Receipt — targets/bartnicki-2303.08771-conj3 (watch-5)

- **Checked UTC:** 2026-11-27T09:40:17Z – 2026-11-27T09:40:26Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2303.08771 "10.1007/s00373-025-02934-5"`):** `0` hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'abs:"2303.08771"'`):** `0` entries (prior `09:28Z` check confirmed `2303.08771v1` is the sole version).
3. **Live Zenodo API (`https://zenodo.org/api/records?q=2303.08771&size=5`):** `0` hits.
4. **Live OpenAlex & Crossref (`10.48550/arXiv.2303.08771` and *Graphs and Combinatorics* 41 (2025), Art. 80 `10.1007/s00373-025-02934-5`):** OpenAlex `cited_by=0` for both DOIs; Crossref `is-referenced-by-count=0` (`published: 2025-07-02`).
5. **Web search (`search_web` `"10.1007/s00373-025-02934-5" OR ("2303.08771" "strong arboricity" "zeta")`):` returns only the paper itself; `0` refutations found.

## Coverage Limits
- Unindexed private repositories or paywalled papers not citing `2303.08771` or `10.1007/s00373-025-02934-5` are not covered.

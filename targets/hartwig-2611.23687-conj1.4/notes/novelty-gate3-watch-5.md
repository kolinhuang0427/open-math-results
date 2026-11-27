# Gate 3 Novelty Receipt — targets/hartwig-2611.23687-conj1.4 (watch-5)

- **Checked UTC:** 2026-11-27T10:13:47Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2310.16929 2611.23687`):** `2611.23687` matched only `watch/snapshots/arxiv/*` (own sweep record `OpenAlex cited_by=0; S2=0` for `2611.23687v1`); `0` resolution hits across `618` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'abs:"2310.16929" OR abs:"2611.23687"'`):** `0` entries (prior `09:43Z` check confirmed `2611.23687v1` sole version).
3. **Live Zenodo & OpenAlex (`2611.23687`):** Zenodo `0` hits; OpenAlex `cited_by=0`.

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `2611.23687` in indexed metadata/abstracts are not covered.

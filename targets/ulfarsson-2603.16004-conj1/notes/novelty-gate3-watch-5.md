# Gate 3 Novelty Receipt — targets/ulfarsson-2603.16004-conj1 (watch-5)

- **Checked UTC:** 2026-11-27T10:06:38Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2603.16004 A121750`):** `2603.16004` matched only `watch/snapshots/arxiv/citing_papers.*` (own sweep entry `OpenAlex cited_by=0; S2=0`); `0` resolution hits across `618` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'abs:"2603.16004" OR all:"A121750"'`):** `0` entries (prior `09:56Z` check confirmed `2603.16004v1` sole version and `search_web` found `0` solutions).
3. **Live Zenodo & OpenAlex (`2603.16004`):** Zenodo `0` hits; OpenAlex `cited_by=0`.

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `2603.16004` in indexed metadata/abstracts are not covered.

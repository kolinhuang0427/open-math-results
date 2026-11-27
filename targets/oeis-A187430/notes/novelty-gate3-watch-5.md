# Gate 3 Novelty Receipt — targets/oeis-A187430 (watch-5)

- **Checked UTC:** 2026-11-27T10:16:42Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A187430`):** `0` hits across `618` files (including `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A187430"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A187430&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A187430&fmt=json`):** rev `55` (`time: 2024-01-17T09:35:29-05:00`); Irwin's Jan 13 2017 formula remains listed as `Conjecture` (prior `10:12Z` Gate 2 check also verified `search_web` found `0` proofs).

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `A187430` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

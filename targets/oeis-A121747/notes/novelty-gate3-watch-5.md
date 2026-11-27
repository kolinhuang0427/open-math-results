# Gate 3 Novelty Receipt — targets/oeis-A121747 (watch-5)

- **Checked UTC:** 2026-11-27T10:03:50Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121752 A121747`):** `0` hits across `618` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A121752" OR all:"A121747"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A121747&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A121747&fmt=json`):** rev `15` (`time: 2024-08-21T12:26:20-04:00`); Mathar's Jul 26 2022 recurrence remains listed as `Conjecture` (prior `09:45Z` Gate 2 check also verified `search_web` found `0` proofs).

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `A121747` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

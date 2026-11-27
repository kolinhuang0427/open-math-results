# Gate 3 Novelty Receipt — targets/oeis-A158960 (watch-5)

- **Checked UTC:** 2026-11-27T10:19:57Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A186997 A158960`):** `0` hits across `618` files (including `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A186997" OR all:"A158960"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A158960&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A158960&fmt=json`):** rev `28` (`time: 2022-09-08T08:45:43-04:00`); M. F. Hasler's Feb 16 2014 denominator claim remains `(conjectured)` (prior `10:17Z` Gate 2 check also verified `search_web` found `0` proofs).

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `A158960` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

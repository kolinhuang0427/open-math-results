# Gate 3 Novelty Receipt — targets/oeis-A186997 (watch-5)

- **Checked UTC:** 2026-11-27T10:19:57Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A186997 A158960`):** `0` hits across `618` files (including `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A186997" OR all:"A158960"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A186997&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A186997&fmt=json`):** rev `85` (`time: 2026-08-30T09:47:33-04:00`); Peter Bala's Aug 02 2016 2-adic valuation formulas remain listed as `Conjectures` (prior `10:15Z` Gate 2 check also verified `search_web` found `0` proofs).

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `A186997` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

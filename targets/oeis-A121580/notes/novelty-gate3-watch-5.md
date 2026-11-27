# Gate 3 Novelty Receipt — targets/oeis-A121580 (watch-5)

- **Checked UTC:** 2026-11-27T09:37:46Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121580 A121584`):** `0` hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A121580" OR all:"A121584"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A121580&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A121580&fmt=json`):** rev `12` (`time: 2024-09-15T07:13:47-04:00`); Mathar's Jul 26 2022 recurrence remains listed as `Conjecture` (prior `09:30Z` Gate 2 check also verified `search_web` `"A121580" ...` returned `0` proofs).

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `A121580` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

# Gate 3 Novelty Receipt — targets/oeis-A045742 (watch-5)

- **Checked UTC:** 2026-11-27T09:35:23Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A045742`):** `0` hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A045742"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A045742&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A045742&fmt=json`):** rev `20` (`time: 2022-07-26T12:51:11-04:00`); Mathar's Jul 26 2022 recurrence remains listed as `Conjecture` (prior `09:32Z` Gate 2 check also verified `search_web` `"A045742" ...` returned `0` proofs).

## Coverage Limits
- Unindexed private repositories or paywalled papers not mentioning `A045742` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

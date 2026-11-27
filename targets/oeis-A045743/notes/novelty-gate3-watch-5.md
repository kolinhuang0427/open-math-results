# Gate 3 Novelty Receipt — targets/oeis-A045743 (watch-5)

- **Checked UTC:** 2026-11-27T09:23:52Z – 2026-11-27T09:24:31Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A045743 045743`):** `0` hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A119366" OR all:"A168452" OR all:"A045743" OR all:"dml.2022.149" OR all:"2208.14707"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A045743&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A045743&fmt=json`):** revision timestamp `2022-07-26T14:31:19-04:00` (rev. 14); Mathar's 2022 recurrence remains listed as `Conjecture` (prior `09:18Z` Gate 2 check also verified `search_web` `"A045743" Mathar` returned `0` published proofs).

## Coverage Limits
- Unindexed private repositories, offline proofs, or paywalled papers not mentioning `A045743` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

# Gate 3 Novelty Receipt — targets/oeis-A108449 (watch-5)

- **Checked UTC:** 2026-11-27T09:25:42Z – 2026-11-27T09:25:55Z
- **Verdict:** **PASS** (open and uncontested; < 1h before reporting)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A108449 108449 ...`):** `1` sha256 substring match (`108449` in `the-omega-institute__trureturing-source-theories`); `0` mathematical hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A108449" ...'`):** `0` hits for `A108449`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A108449&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A108449&fmt=json`):** timestamp `2025-11-05T15:35:31-05:00` (rev. 13); Mathar's Jul 26 2022 recurrence remains listed as `Conjecture D-finite with recurrence ...`.
5. **Web search (`search_web` `"A108449" "Mathar" OR "D-finite" OR "no pyramids"`):** `0` proofs found.

## Coverage Limits
- Unindexed private repositories or paywalled papers not citing `A108449` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

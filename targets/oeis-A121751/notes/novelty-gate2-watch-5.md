# Gate 2 Novelty Receipt — targets/oeis-A121751 (watch-5)

- **Checked UTC:** 2026-11-27T09:36:09Z – 2026-11-27T09:36:35Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121751 121751`):** `0` hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A121751" ...'`):** `0` entries for `A121751`.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A121751&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A121751&fmt=json`):** rev `5` (`time: 2022-07-26T11:27:46-04:00`); Mathar's Jul 26 2022 formula remains `Conjecture D-finite with recurrence ...`.
5. **Web search (`search_web` `"A121751" "Mathar" OR "D-finite" OR "recurrence" OR "deco polyominoes"`):** returns only OEIS A121751 itself; `0` proofs found.

## Coverage Limits
- Unindexed private repositories or papers not citing `A121751` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

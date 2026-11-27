# Gate 2 Novelty Receipt — targets/oeis-A121747 (watch-5)

- **Checked UTC:** 2026-11-27T09:45:30Z – 2026-11-27T09:45:43Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121747 121747 ...`):** `0` hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A121747" OR all:"A121750"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A121747&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A121747&fmt=json`):** rev `15` (`time: 2024-08-21T12:26:20-04:00`); Mathar's Jul 26 2022 formula remains `Conjecture D-finite with recurrence ...`.
5. **Web search (`search_web` `"A121747" OR "A121750" ...`):** `0` published proofs found.

## Coverage Limits
- Unindexed private repositories or papers not citing `A121747` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

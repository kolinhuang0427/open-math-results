# Gate 2 Novelty Receipt — targets/oeis-A121580 (watch-5)

- **Checked UTC:** 2026-11-27T09:30:10Z – 2026-11-27T09:30:13Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A121580 121580`):** `0` hits across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A121580"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A121580&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A121580&fmt=json`):** rev `12` (`time: 2024-09-15T07:13:47-04:00`); Mathar's Jul 26 2022 formula remains `Conjecture D-finite with recurrence ...`.
5. **Web search (`search_web` `"A121580" "Mathar" OR "recurrence" OR "D-finite" OR "conjecture"`):** returns only OEIS A121580 itself; `0` published proofs found.

## Coverage Limits
- Unindexed private repositories or papers not citing `A121580` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

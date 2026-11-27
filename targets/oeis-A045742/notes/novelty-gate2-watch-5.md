# Gate 2 Novelty Receipt — targets/oeis-A045742 (watch-5)

- **Checked UTC:** 2026-11-27T09:31:59Z – 2026-11-27T09:32:14Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A045742 045742 ...`):** `0` hits for `A045742` across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A045742" ...'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A045742&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A045742&fmt=json`):** rev `20` (`time: 2022-07-26T12:51:11-04:00`); Mathar's Jul 26 2022 formula remains `Conjecture D-finite with recurrence ...`.
5. **Web search (`search_web` `"A045742" "Mathar" OR "D-finite" OR "recurrence"`):** `0` proofs of `A045742`'s recurrence found.

## Coverage Limits
- Unindexed private repositories or papers not citing `A045742` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

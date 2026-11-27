# Gate 2 Novelty Receipt — targets/oeis-A121752 (watch-5)

- **Checked UTC:** 2026-11-27T09:40:13Z – 2026-11-27T09:40:26Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py ... A121752 121752`):** only unrelated sha256 substrings (`the-omega-institute__trureturing-source-theories`); `0` math hits for `A121752`.
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A121752" ...'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A121752&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A121752&fmt=json`):** rev `4` (`time: 2022-07-26T11:29:39-04:00`); Mathar's Jul 26 2022 formula remains `Conjecture D-finite with recurrence ...`.
5. **Web search (`search_web` `"A121754" OR "A121752" "Mathar" OR "D-finite" ...`):` `0` published proofs found.

## Coverage Limits
- Unindexed private repositories or papers not citing `A121752` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

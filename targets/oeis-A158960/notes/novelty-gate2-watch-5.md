# Gate 2 Novelty Receipt — targets/oeis-A158960 (watch-5)

- **Checked UTC:** 2026-11-27T10:17:07Z – 2026-11-27T10:17:16Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py A158960 158960`):** `0` hits across `618` files (including `watch/snapshots/zenodo-23112421-oeis-ids.md`).
2. **arXiv API (`tools/arxiv_fetch.py query 'all:"A158960"'`):** `0` entries.
3. **Live Zenodo API (`https://zenodo.org/api/records?q=A158960&size=5`):** `0` hits.
4. **Live OEIS JSON (`https://oeis.org/search?q=id:A158960&fmt=json`):** rev `28` (`time: 2022-09-08T08:45:43-04:00`); M. F. Hasler's Feb 16 2014 denominator claim remains listed as `The denominators are 5^n = A000351(n) (conjectured).`.
5. **Web search (`search_web` `"A158960" ("Hasler" OR "Hermite" OR "conjecture" OR "Blanco")`):` `0` proofs found.

## Coverage Limits
- Unindexed private repositories or papers not citing `A158960` in OEIS/arXiv/Zenodo/snapshot indexes are not covered.

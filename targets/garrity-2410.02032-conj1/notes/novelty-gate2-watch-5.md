# Gate 2 Novelty Receipt — targets/garrity-2410.02032-conj1 (watch-5)

- **Checked UTC:** 2026-11-27T10:14:42Z – 2026-11-27T10:15:15Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2410.02032 Garrity "conj:e-23-e"`):** `0` hits across `618` files.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2410.02032v2` (`2026-07-21`, *Combinatorics and Number Theory* 15 (2026) 239–292) is the latest version; `abs:"2410.02032"` = `0` entries; inspected S2 citing preprint `2506.02984v1` (*There is only one Farey map* by Giovanni Panti — predates `v2` and does not settle `S(e,23,e)` complexity $\le 3n$).
3. **Live OpenAlex, Semantic Scholar & Zenodo (`2410.02032`):** OpenAlex `cited_by=2`; S2 `1` citing paper (`2506.02984v1`, inspected); Zenodo `0` hits.
4. **Web search (`search_web` `"2410.02032" OR ("Garrity" "2410.02032") OR "conj:e-23-e"`):** returns only `2410.02032`; `0` proofs of Conjecture 1 found.

## Coverage Limits
- Non-indexed private repositories or paywalled papers not mentioning `2410.02032` in indexed metadata/abstracts are not covered.

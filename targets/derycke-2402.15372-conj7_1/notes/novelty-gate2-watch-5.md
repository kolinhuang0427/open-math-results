# Gate 2 Novelty Receipt — targets/derycke-2402.15372-conj7_1 (watch-5)

- **Checked UTC:** 2026-11-27T09:42:40Z – 2026-11-27T09:43:44Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2402.15372 Derycke ITCCTIsymmetry ...`):** `0` hits for `2402.15372` / `Derycke` / `ITCCTIsymmetry` across `608` files.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2402.15372v3` (`2025-12-19`) is the latest version; `abs:"2402.15372"` = `0` entries; inspected abstracts of all `4` Semantic Scholar citing papers (`2506.23237v1` prime $G$-parking functions, `2409.11811v1` complete bipartite graphs, `2401.06488v2` clique-independent graphs / predates `v3`, `2207.01997v1` Motzkin numbers) — none resolves `conj:ITCCTIsymmetry`.
3. **Live OpenAlex, Semantic Scholar & Zenodo (`2402.15372`):** OpenAlex `cited_by=3`; S2 `4` citing papers (all inspected); Zenodo `0` hits.
4. **Web search (`search_web` `"2402.15372" OR "ITCCTIsymmetry" ...`):` returns only `2402.15372` itself; `0` resolutions of Conjecture 6.1 found.

## Coverage Limits
- Non-indexed private repositories or paywalled papers not citing `2402.15372` in indexed metadata/abstracts are not covered.

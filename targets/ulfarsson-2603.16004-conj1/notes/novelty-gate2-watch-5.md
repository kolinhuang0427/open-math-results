# Gate 2 Novelty Receipt — targets/ulfarsson-2603.16004-conj1 (watch-5)

- **Checked UTC:** 2026-11-27T09:55:58Z – 2026-11-27T09:56:24Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2603.16004 Ulfarsson Úlfarsson "conj:general-reverse"`):** `2603.16004` matched only `watch/snapshots/arxiv/citing_papers.*` (`cited_by=0; S2=0`), and `Ulfarsson` matched unrelated `the-omega-institute/trureturing` `UlfarssonAlternatingMeshBasis` / `ulfarsson2024bisc.md`; `0` resolution hits across `618` files.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2603.16004v1` (`2026-03-16`) is the sole version; `abs:"2603.16004"` = `0` entries.
3. **Live OpenAlex & Zenodo (`2603.16004`, `"Permutations Avoiding Patterns"`):** OpenAlex `cited_by=0`; Zenodo `0` hits (Semantic Scholar returned HTTP 429).
4. **Web search (`search_web` `"2603.16004" OR ("Ulfarsson" "Permutations Avoiding Patterns") OR "conj:general-reverse"`):** returns only `2603.16004v1` itself; `0` proofs found.

## Coverage Limits
- Semantic Scholar API returned HTTP 429; non-indexed private repos or paywalled papers not mentioning `2603.16004` are not covered.

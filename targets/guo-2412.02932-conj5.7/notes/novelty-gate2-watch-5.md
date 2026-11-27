# Gate 2 Novelty Receipt — targets/guo-2412.02932-conj5.7 (watch-5)

- **Checked UTC:** 2026-11-27T09:52:44Z – 2026-11-27T09:55:18Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2412.02932 ...`):** `2412.02932` matched only `watch/snapshots/arxiv/citing_papers.json` (own sweep entry); `0` solution hits across `618` files.
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2412.02932v1` (`2024-12-04`) is the sole version; `abs:"2412.02932"` = `0` entries; inspected abstracts of all `5` Semantic Scholar citing papers (`2610.36993v1` key-polynomial factorizations, `2609.02050v1` Schur character bounds, `2605.10276v1` Grothendieck specializations, `2512.04053v2` maximal Schubitopes, `2508.09107v3` fireworks Grothendieck polytopes) — none resolves Conjecture 5.7 ($d_u \ge 0$ for $\theta_w$).
3. **Live OpenAlex, Semantic Scholar & Zenodo (`2412.02932`):** OpenAlex `cited_by=5`; S2 `5` citing papers (all inspected); Zenodo `0` hits.
4. **Web search (`search_web` `"2412.02932" OR ("Guo" "2412.02932" "Schubert")`):` returns only `2412.02932v1`; `0` counterexamples found.

## Coverage Limits
- Non-indexed private repositories or papers not citing `2412.02932` in indexed metadata/abstracts are not covered.

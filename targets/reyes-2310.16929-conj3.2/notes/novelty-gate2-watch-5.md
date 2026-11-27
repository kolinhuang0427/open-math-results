# Gate 2 Novelty Receipt — targets/reyes-2310.16929-conj3.2 (watch-5)

- **Checked UTC:** 2026-11-27T09:59:17Z – 2026-11-27T10:05:21Z
- **Verdict:** **PASS** (open and uncontested)

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2310.16929 Reyes`):` `0` hits settling Conjecture 3.2 across `618` files; inspected `the-omega-institute/trureturing` `Problems/reyes-dalfo-fiol-2024-new-laplacian-layer-maxima.md` via `gh api` (explicitly refutes Conjecture 3.3 $\rho_k$ maxima only, *"not the neighboring minimum conjecture"*).
2. **arXiv API (`tools/arxiv_fetch.py query`):** `2310.16929v1` (`2023-10-25`) is the sole version; `abs:"2310.16929"` = `0` entries.
3. **Live OpenAlex, Semantic Scholar & Zenodo (`2310.16929` / `10.1007/s40590-023-00583-3`):` Zenodo `0` hits; OpenAlex `cited_by=6`; Semantic Scholar `7` citing papers of *Bol. Soc. Mat. Mex.* `10.1007/s40590-023-00583-3` inspected — fetched and inspected `2610.00500v1` `main.tex` (Song–Dalfó–Fiol–Zhang, studies full algebraic connectivity $a(F_k(G))=a(G)$ and full radius $\rho(F_k(G))$, not new-layer minimum $\alpha_k(G)$), `2609.25037v1` (spectral radii via Lorentzian semigroups), `2506.03441v3`, `2504.06617v6`, `2404.02122v1`, `10.1016/j.laa.2024.02.004`, `10.1016/j.disc.2026.115559`; none settles Conjecture 3.2.
4. **Web search (`search_web` `"2310.16929" OR ...`):` returns only `2310.16929v1`; `0` counterexamples to Conjecture 3.2 found.

## Coverage Limits
- Full text of paywalled Elsevier articles (`10.1016/j.laa.2024.02.004`, `10.1016/j.disc.2026.115559`) and unindexed private repos are not directly readable.

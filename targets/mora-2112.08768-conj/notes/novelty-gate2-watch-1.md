# Gate 2 Novelty Check — `mora-2112.08768-conj` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T18:38:41Z`–`2026-11-27T18:39:14Z`
- **Target:** `targets/mora-2112.08768-conj/` — Mercè Mora, María José Souto-Salorio, and Ana Dorotea Tarrío-Tobar, *"Resolving sets tolerant to failures in three-dimensional grids"* (`arXiv:2112.08768v1`, `2021-12-16`; *Mediterr. J. Math.* 19 (2022), art. 190, `DOI:10.1007/s00009-022-02096-1`), Section 4 Conjecture (`FaultTolerantMD-3DGrids-arxiv.tex` L901–911)
- **Claimed result:** **REFUTED** (smallest counterexample $(3,3,4,13)$ has explicit $30$-vertex $14$-resolving set beating conjectured $\min(32, 34) = 32$, `COUNTEREXAMPLE.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2112.08768" "k-metric dimension" "k-resolving"`):**
   - `0` lines across `0/762` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T18:38:41Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `53ce51af9295b6a5edc36734b70ed71b29b1f558` (`2026-11-27T18:35:17Z`, Cohen chromatic ceiling) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2112.08768"` -> `0` hits (`[]`).
   - `gh search issues "2112.08768"` -> `0` hits (`[]`).
   - `gh search code "2112.08768"` -> unrelated CSV/JSON numeric collisions only.
   - `gh search code '"Resolving sets tolerant to failures in three-dimensional grids"'` -> `ndthanh308/IntroDS_LAB` `2307-13403/references.json` (verified via arXiv API: `2307.13403v2` *"Metric Location in Pseudotrees"*, unrelated); `gh search code '"10.1007/s00009-022-02096-1"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2112.08768`) -> sole version `2112.08768v1` (`2021-12-16T10:26:03Z`, `arxiv:doi` `10.1007/s00009-022-02096-1`).
   - Zenodo API (`q=2112.08768`) -> `0` hits.
   - Crossref (`10.1007/s00009-022-02096-1`) -> `is-referenced-by-count: 4`.
   - Web search -> only Mora–Souto-Salorio–Tarrío-Tobar (`2021`/`2022`) paper and related metric-dimension background; `0` follow-up refutations or settlements of the 3D-grid Section 4 conjecture found.

## Coverage Limits
- Covers `watch/snapshots` (`762` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref count, and public web search as of `2026-11-27T18:39:14Z`; Semantic Scholar returned HTTP `429` (`Too Many Requests`), so the full citation list behind Crossref's `4` citing works was not enumerated directly by `watch-1` (verified via web search & `2307.13403` check only).

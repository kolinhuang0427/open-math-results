# Gate 2 Novelty Receipt (`watch-6`) — `targets/mora-2112.08768-conj/`

- **Target:** Mercè Mora, María José Souto-Salorio & Ana Dorotea Tarrío-Tobar, *Resolving sets tolerant to failures in three-dimensional grids*, `arXiv:2112.08768v1` / *Mediterr. J. Math.* **19** (2022), 188/190 (`DOI:10.1007/s00009-022-02096-1`), Section 4 (final Conjecture, `FaultTolerantMD-3DGrids-arxiv.tex` L901–911): for $\alpha_m(n_1,n_2,n_3) \le k < \alpha_M(n_1,n_2,n_3)$, $\dim_{k+1}(P_{n_1}\Box P_{n_2}\Box P_{n_3}) = \min\{4k - 2\alpha_m + 4,\; n_1n_2n_3 - (n_1-2)(n_2-2)(n_3-2)\}$ (**REFUTED**, smallest counterexample $(3,3,4,13)$ with $30$-vertex $14$-resolving set vs conjectured $32$).
- **Checked UTC:** `2026-11-27T18:38:52Z` – `2026-11-27T18:39:28Z`
- **Verdict:** **PASS — OPEN** (no prior refutation or proof of the Section 4 conjecture found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `762` files) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2112.08768 "mora-2112.08768" "three-dimensional grids" "tolerant to failures" "s00009-022-02096-1" "k-resolving" --max-per-file 0 --max-total 40` -> `# 0 lines across 0/762 files in 0.64s`.
   - `RESULTS.md` contains `0` entries for `2112.08768`, Mora, or 3D-grid $k$-metric dimension (`Morales` / `resolving` unrelated).
2. **Live GitHub (`2026-11-27T18:38:52Z`–`18:39:15Z`):**
   - `gh search code '"2112.08768"'`, `gh search code '"10.1007/s00009-022-02096-1"'`, `gh search repos "2112.08768"`, `gh search issues "2112.08768"`, `gh search prs "2112.08768"` -> `0` hits on all five.
   - `gh search code '"Resolving sets tolerant to failures in three-dimensional grids"'` -> `ndthanh308/IntroDS_LAB` (`23127538_data/2307-13403/references.json`, bibliography entry of `2307.13403` only).
3. **Live arXiv, OpenAlex, Crossref, OpenCitations, Semantic Scholar, Hexagon, Papex, Zenodo & Web (`2026-11-27T18:38:52Z`–`18:39:28Z`):**
   - `https://export.arxiv.org/api/query?id_list=2112.08768` -> `2112.08768v1` sole arXiv version (`journal_ref: Mediterr. J. Math (2022) 19:188`, `doi: 10.1007/s00009-022-02096-1`).
   - Semantic Scholar `DOI:10.1007/s00009-022-02096-1` (`citationCount=6`), OpenCitations (`4`), Crossref (`4`), OpenAlex (`5`) -> inspected all citing works: `2610.13374` (maximal outerplanar graphs), `ICDCECE68961` (CV power grids), `math13040560`/`2307.13403` (pseudotrees), `2410.03656` (eprint TeX inspected directly: passing `\cite{Mora2022}` in intro only), `s00010-024-01062-4` (triangular grid rotations) — none addresses Mora et al.'s Section 4 3D-grid conjecture.
   - `hexagonmath.org` (`total=0`), `papex.org` (`0/20`), Zenodo (`0` hits), `search_web` clear.

## Coverage Limits

- Paywalled journal issues beyond arXiv preprints and private/unindexed repositories are outside reach; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` publication.

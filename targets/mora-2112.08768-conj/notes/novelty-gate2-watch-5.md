# Gate 2 Novelty Receipt — `mora-2112.08768-conj` (`watch-5`)

- **Target:** `targets/mora-2112.08768-conj/` — Mercè Mora, María José Souto-Salorio, and Ana Dorotea Tarrío-Tobar, *"Resolving sets tolerant to failures in three-dimensional grids"*, `arXiv:2112.08768v1` / *Mediterr. J. Math.* 19 (2022), art. 188/190 (`DOI:10.1007/s00009-022-02096-1`), Section 4 Conjecture ($\dim_{k+1}(P_{n_1}\Box P_{n_2}\Box P_{n_3})$ formula for $\alpha_m \le k < \alpha_M$).
- **Checked UTC:** `2026-11-27T18:38:53Z`–`2026-11-27T18:40:10Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no published or preprinted resolution or counterexample to Section 4's 3D-grid conjecture found.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 762 files):**
   - `.venv/bin/python tools/novelty_grep.py "2112.08768" "s00009-022-02096-1" "k-resolving" "three-dimensional grids" --max-per-file 10 --max-total 40`: `0` lines across `0/762` files.
2. **Citation & Journal Follow-up (`OpenAlex`, `Semantic Scholar`, `OpenCitations`, `arXiv`):**
   - `arXiv:2112.08768v1` (`2021-12-16`) sole arXiv version; published DOI `10.1007/s00009-022-02096-1`.
   - `OpenAlex` (`W4285008974`, `cited_by_count: 5`), `OpenCitations` (`4`), `Semantic Scholar` (`6` citations): all citing works inspected:
     - `arXiv:2410.03656` / `10.1007/s00009-025-02894-3` (*Fault Tolerance of Metric Basis Can Be Expensive*): inspected `MetricFt_v36.tex` directly — cites `Mora2022` only in passing (L111, L152).
     - `arXiv:2610.13374` (*On the fault-tolerant metric dimension of maximal outerplanar graphs*): inspected `FTMD_MOPs_arxiv.tex` directly — outerplanar graphs only.
     - `arXiv:2307.13403` & `10.3390/math13040560` (*Metric Locations in Pseudotrees*): inspected `mlopt.tex` directly — pseudotrees survey only.
     - `10.1007/s00010-024-01062-4` (*Rotations on the triangular grid*) & `10.1109/ICDCECE68961.2026.11645934` (power grid CV): unrelated.
   - `arXiv` searches (`all:"Mora" AND all:"resolving"`, `all:"Souto-Salorio"`, `all:"k-metric dimension" AND all:"grid"`): `0` follow-up 3D-grid results.
3. **Live GitHub, Zenodo & Web:**
   - `gh search issues/prs/repos "2112.08768"`: `0` hits; `gh search code "s00009-022-02096-1"`: only `WhoSia/CUBE-REV` (Rubik's cube literature table) and `ndthanh308/IntroDS_LAB` (`2307.13403` pseudotrees TeX mirror).
   - `Zenodo` (`2112.08768`): `0` hits; `search_web`: returns only `arXiv:2112.08768` / *Mediterr. J. Math.* article.

## Near-Misses & Coverage Limits
- **Near-misses:** `2410.03656` and `2610.13374` study general/outerplanar fault-tolerant metric dimension, not 3D grids.
- **Coverage limits:** OpenAlex `cited_by_api_url` returned `HTTP 429` (covered via S2 + OpenCitations); private/unindexed drafts posted after `2026-11-27T18:40:10Z` are not covered.

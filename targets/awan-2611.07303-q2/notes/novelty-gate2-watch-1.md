# Gate 2 Novelty Check — `awan-2611.07303-q2` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T18:34:10Z`–`2026-11-27T18:35:06Z`
- **Target:** `targets/awan-2611.07303-q2/` — Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger, and Elvis Wong, *"Gaps in the Most Frequent Sizes of Integer Sumsets"* (`arXiv:2611.07303v2`, `2026-11-09`), Section 5.2 Question 2 (`\label{q:rate}`, `sections/additional-results.tex` L556–578)
- **Claimed result:** **COMPLETE ANSWER** — $f_{h,k}(q)$ converges for all $h \ge 2, k \ge 3$ to $c_{h,k} = k!\sum_{\mathbf{d} \in \mathcal{R}_{h,k}} \operatorname{vol}_{k-1}(P_{\mathbf{d}})/\|\mathbf{d}\|_2$, and is **NOT** eventually monotone (proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.07303" "Awan" "q:rate"`):**
   - `1337isnot1337/solved-conjectures` cites unrelated Awan tree preprint (`arXiv:2609.13464`); remaining hits are unrelated substrings (`Wadhawan`, `PanSkanderaWang`, etc.); `0` hits on `2611.07303` or `q:rate` across `760` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T18:34:10Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `b1dae5fa416739d7844cc61871c18b18e13cb663` (`2026-11-27T18:30:39Z`, disjoint-type obstructions) — unrelated.
3. **GitHub live search & direct inspection (`gh api`):**
   - `gh search prs "2611.07303"` -> `richfrem/Project_Sanctuary#403` (`MISSION-062`, inspected via `gh api`: finite computational check of Question 1 threshold $q_0(h, 3) \le 3h$ for $h \le 16, q \le 250$ only).
   - `gh search issues "2611.07303"` -> `the-omega-institute/trureturing#29874` (inspected body: Question 4 `q:distribution` $\nu_q$ limit only, not `q:rate`).
   - `sawan201/PolyMathJr_MSTD` (paper authors' Lean repo, inspected tree at `b4bca0a4`, pushed `2026-10-28T14:52:42Z`): contains paper's own `RequestProject/Additional/K3Limit.lean` only; `0` files for $k \ge 4$ or non-monotonicity.
   - `rainwangphy/aftd-platform`: `SumsetRepCount*` files cover Question 4 `Prop 5.7` definitions only.
4. **arXiv / Zenodo / Web:**
   - arXiv API (`id_list=2611.07303`) -> `2611.07303v2` (`2026-11-09T14:48:06Z`), latest version.
   - Zenodo API (`q=2611.07303`) -> `0` hits.
   - Web search -> only Awan et al. `arXiv:2611.07303` preprint; `0` resolutions of Question 2 (`q:rate`).

## Coverage Limits
- Covers `watch/snapshots` (`760` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search + companion repo tree (`sawan201/PolyMathJr_MSTD`), arXiv API, Zenodo API, and public web search as of `2026-11-27T18:35:06Z`; private repositories and non-indexed preprints remain unobservable.

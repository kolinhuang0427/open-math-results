# Gate 2 Novelty Check — mirzavaziri-2610.19249-conj1 (watch-5)

- **Checked UTC:** 2026-11-27T10:30:44Z – 2026-11-27T10:33:39Z
- **Result:** **PASS** (no prior proof or settlement of Guo–Krattenthaler `conj:GK` or Mirzavaziri–Yaqubi `conj:general` for `[301, 10^30)` found).

## Exact Queries & Results

1. **Local snapshot grep & near-miss inspection:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2610.19249 Mirzavaziri Yaqubi "Guo-Krattenthaler" "conj:GK"`
   - Result: `39` lines across `12/619` files.
   - **Exact near-miss checked (`the-omega-institute/trureturing`):**
     - `Library/Certificates/mirzavaziri2026gaussianquotient.md` & `D5/S3/Combinatorics/GaussianQuotient/MirzavaziriYaqubiMonotonicityRefutation.lean` (Issue `#21322`): explicitly targets **Problem 7.2** (general quadruple $(N,k,a,b)$ weak-increase sufficiency question, refuted at `(30, 3, 7, 10)`). It does **not** address or settle `conj:GK` ($P_n(q)$) or `conj:general` ($m \ge 9, m=5, m \not\equiv 2,3 \pmod 5$).
   - `tamnd/arxiv`: automated arXiv extraction/index (`2610.19249v1`) only, no proof.
   - `andrheabacor/open-conjecture-results` (`MirzavaziriYaqubi8`) & `s66lem/conjectures` (`YaqubiMirzavaziriPDO`): unrelated papers (`2611.18194` Möbius & PDO).

2. **arXiv / Semantic Scholar:**
   - `id:2610.19249`: sole version `2610.19249v1` (`2026-10-13T22:05:49Z`).
   - `abs:2610.19249`: `0` citing abstracts.
   - S2 `ARXIV:2610.19249/citations`: `0` citations.
   - S2 `ARXIV:1301.7651/citations` (since 2024): only `2610.19249` (Mirzavaziri–Yaqubi) and `2610.26878` (*A positivity conjecture of Prellberg and Stanton*, distinct quotient).

3. **Zenodo / GitHub / Web:**
   - Zenodo live API (`2610.19249`): `0` hits.
   - `gh search issues "2610.19249"` (only `trureturing#21322` Problem 7.2), `gh search repos "2610.19249"` (`0`).
   - `search_web` (`"2610.19249" OR "Mirzavaziri" "Yaqubi" "Guo" "Krattenthaler" "30n" OR "10n-1"`): only `2610.19249v1` itself.

## Coverage Limits
- Local snapshot coverage reflects `619` files; live arXiv, S2 citations, Zenodo, GitHub issues/repos, and `search_web` returned `0` hits settling `conj:GK` or `conj:general`.

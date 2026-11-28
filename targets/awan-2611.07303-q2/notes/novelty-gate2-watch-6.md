# Gate 2 Novelty Receipt (`watch-6`) — `targets/awan-2611.07303-q2/`

- **Target:** Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger & Elvis Wong, `arXiv:2611.07303v2` (*"Gaps in the Most Frequent Sizes of Integer Sumsets"*, updated `2026-11-09`), Section 5.2 (`sections/additional-results.tex` L556–578), **Question 2** (`\label{q:rate}`): does $f_{h,k}(q) = q(1 - |\mathcal{B}_{h,k}(q)|/\binom{q}{k})$ converge for every $k \ge 4$, what is its limit $c_{h,k}$, is it eventually monotone in $q$, and can $c_{h,k}$ be expressed via $(k-1)$-dimensional volumes of $\mathcal{R}_{h,k}$ hyperplane sections? (**YES** convergence + exact volume formula; **NO** eventual monotonicity).
- **Checked UTC:** `2026-11-27T18:34:13Z` – `2026-11-27T18:34:36Z`
- **Verdict:** **PASS — OPEN** (no prior settlement of Question 2 `q:rate` found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `760` files) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2611.07303 "awan-2611.07303" "q:rate" "Awan" "f_{h,k}" --max-per-file 0 --max-total 40` -> unrelated `Awan 2609.13464` mention in `1337-solved-conjectures/open_issues_claims.md` only (`0` hits on `2611.07303`, `q:rate`, or `f_{h,k}`).
   - `RESULTS.md` scan (`2611\.07303|awan`) -> `[]`.
2. **Live GitHub (`2026-11-27T18:34:13Z`–`18:34:36Z`):**
   - `gh search code '"2611.07303"'` & `gh search prs "2611.07303"` -> `richfrem/Project_Sanctuary` (`LEARNING/missions/MISSION-062.json`, PR `#403`; inspected via `gh api`: checks top-$h$ frequent sumset sizes for $k=3, h\in\{5,\dots,16\}, q\le 250$ only).
   - `gh search issues "2611.07303"` -> `the-omega-institute/trureturing#29874` (`open`; inspected via `gh api`: covers Question 4 `q:distribution` only; `0` other issues/PRs in `trureturing`).
   - Inspected `watch/snapshots/discovered/rainwangphy__aftd-platform.json` (`Kb/Tcs/Sumset*` foundational sumset definitions/lemmas only; `0` settlement of `q:rate`).
   - `gh search code '"awan-2611.07303"'`, `gh search code '"q:rate" "Awan"'`, `gh search repos "2611.07303"` -> `0` hits on all three.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T18:34:13Z`–`18:34:27Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.07303` -> `2611.07303v2` (`2026-11-09T14:48:06Z`) sole latest version.
   - `https://hexagonmath.org/api/v1/works` (`q=2611.07303`, `q=Awan`) -> `total=0`; `papex.org` `0/20`; Zenodo `0` hits; OpenAlex `0` indexed records.
   - `search_web` (`"2611.07303" OR ("Awan" "f_{h,k}" OR "c_{h,k}" "eventually monotone")`) -> returns only Awan et al.'s `arXiv:2611.07303` preprint.

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` publication.

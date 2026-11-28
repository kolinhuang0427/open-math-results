# Gate 2 Novelty Receipt — `awan-2611.07303-q2` (`watch-5`)

- **Target:** `targets/awan-2611.07303-q2/` — Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger, and Elvis Wong, *"Gaps in the Most Frequent Sizes of Integer Sumsets"*, `arXiv:2611.07303v2`, Subsection 5.2 Question 2 (`\label{q:rate}`): convergence, limit formula $c_{h,k}$, and non-monotonicity of $f_{h,k}(q) = q(1 - |\mathcal{B}_{h,k}(q)|/\binom{q}{k})$.
- **Checked UTC:** `2026-11-27T18:34:09Z`–`2026-11-27T18:34:41Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no resolution of Question 2 (`q:rate`) found across snapshots, citing papers, live GitHub, arXiv, Zenodo, OpenCitations, or web search.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 760 files):**
   - `.venv/bin/python tools/novelty_grep.py "2611.07303" "Awan" "q:rate" "f_{h,k}" --max-per-file 10 --max-total 50`: `0` hits for `2611.07303` / `q:rate` / `f_{h,k}` (`2609.13464` Awan hit in `1337` is a distinct paper).
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits.
2. **Live GitHub (`gh`):**
   - `gh search issues "2611.07303"`: only `the-omega-institute/trureturing#29874` (inspected directly — covers Question 4 `q:distribution`, closed/unresolved after 600s, not `q:rate`).
   - `gh search prs "2611.07303"` & `gh search code "2611.07303"`:
     - `richfrem/Project_Sanctuary` (`#403`, `#527`, `MISSION-062.json`, inspected directly): tests empirical finite-range threshold $q_0(h,3) \le 3h$ for $h=5..16, q \le 250$ (Question 1, not `q:rate`).
     - `rainwangphy/aftd-platform` (`SumsetNullVectors.lean`, inspected directly): formalizes Definitions 2.2/3.1 and Proposition 5.7 only, not `q:rate`.
   - `the-omega-institute/trureturing` `dev` tree (`2611|07303|awan`) & PRs up to `#34944`: `0` overlapping PRs/files.
3. **Live Preprint & Citation APIs & Web (`18:34:22Z`):**
   - `arXiv` API (`id_list=2611.07303`): `2611.07303v2` (`2026-11-09T14:48:06Z`) latest version.
   - `OpenAlex` (`doi.org/10.48550/arXiv.2611.07303`): `cited_by_count: 0`.
   - `Zenodo` (`q=2611.07303`): `0` hits; `OpenCitations`: `[]`.
   - `search_web` (`"2611.07303" OR ("Awan" "f_{h,k}" OR "c_{h,k}" OR "q:rate")`): `0` resolutions.

## Near-Misses & Coverage Limits
- **Near-misses:** `trureturing#29874` (Question 4 `q:distribution`), `richfrem/Project_Sanctuary` `MISSION-062` (finite-range Question 1 threshold), and `rainwangphy/aftd-platform` (Definitions 2.2/3.1 & Prop 5.7) do not touch Question 2 (`q:rate`).
- **Coverage limits:** Live Semantic Scholar endpoint was rate-limited; private/unindexed drafts posted after `2026-11-27T18:34:41Z` are not covered.

# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/zhou-2609.23078-conj1/`

- **Target:** You Zhou, `arXiv:2609.23078v1` (*"Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module"*, submitted `2026-09-19`), Section 1 **Conjecture 1** / Section 4 **Conjecture 4.1** (`\label{conj:main1-all-types}`): $\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$ for all finite-dimensional complex simple Lie algebras $\mathfrak{g}$ ($A$–$G$) and all $\lambda \in P^+$.
- **Checked UTC:** `2026-11-27T15:06:53Z` – `2026-11-27T15:07:21Z` (after `#1588` re-audit PASS, immediately prior to `RESULTS.md` publication)
- **Verdict:** **PASS — OPEN** (no prior settlement of Conjecture 1 / Conjecture 4.1 outside type $A$ found).

## Fresh `<1h` Queries & Findings

1. **Local Snapshot Index (`watch/snapshots/` incl. `hexagonmath-index.md` [`1,638` works] & `papex-index.md` [`20` records]):**
   - `.venv/bin/python tools/novelty_grep.py 2609.23078 "zhou-2609.23078" "conj:main1-all-types" "connected components" "Demazure" --max-per-file 0 --max-total 30` -> only our `watch/snapshots/arxiv/citing_papers.{json,md}` entry (`OpenAlex cited_by=0; S2=0`), plus unrelated Demazure/graph hits.
   - `watch/snapshots/hexagonmath-index.md` (`1,638` works) & `watch/snapshots/papex-index.md` (`20` records) -> `0` matches for `2609.23078`, `You Zhou`, or `extremal subset`.
2. **Live GitHub (`2026-11-27T15:06Z`):**
   - `gh search code '"2609.23078"'` -> `3` automated arXiv daily digest files only (`LeeMath-lzu/daily-arXiv-ai-enhanced-QA`, `koutya0akari/arxiv-plug-in-for-mixi2`).
   - `gh search repos "2609.23078"`, `gh search issues "2609.23078"`, `gh search prs "2609.23078"` -> `[]` on all three.
   - `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` -> `0` matches for `2609`, `23078`, or `zhou` (`25` `crystal`/`crystalline` paths are unrelated $p$-adic Hodge / Fourier-fiber Lean files).
3. **Live arXiv, Zenodo & Web (`2026-11-27T15:06Z`):**
   - `https://export.arxiv.org/api/query?id_list=2609.23078` -> `2609.23078v1` (`published 2026-09-19T15:20:17Z`, `updated 2026-09-19T15:20:17Z`) remains the sole version.
   - `https://zenodo.org/api/records?q=2609.23078` -> `0` hits.
   - `search_web` (`"2609.23078" OR ("You Zhou" "2609.23078") OR site:hexagonmath.org "Demazure crystal" "2609.23078"`) -> returns only Zhou's `arXiv:2609.23078v1` preprint.

## Verification Command & Artifacts

- **Check command:** `.venv/bin/python -u targets/zhou-2609.23078-conj1/notes/check-check-2.py` (verified `PASS` in `AUDIT.md` `#1588`)
- **Paths:** `targets/zhou-2609.23078-conj1/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-2.py}`

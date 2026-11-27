# Gate 3 Novelty Re-Check — `campbell-2509.16034-conj1` (watch-5, rescoped `(c1)+(c2)`)

- **UTC Timestamp:** `2026-11-27T02:33:57Z`
- **Target:** `targets/campbell-2509.16034-conj1/TARGET.md` (rescoped strictly to Open Problems (c1) explicit sign of $\rho(4n+2)-\rho(4n)$ and (c2) explicit recursion for $\rho(4n)$ / full recursion)
- **Verdict:** **PASS** (no public settlement of Open Problems (c1) or (c2) found across live arXiv citing papers `2610.14637v1`/`2609.16596v1`, Zenodo, `413` snapshots, or competing GitHub repos including `facebookresearch/atlas-lean` and `trureturing*`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `413` files):**
   - `"2509.16034" "displayconjecture" "reduced abelian"` -> `watch/snapshots/arxiv/citing/campbell-2509.16034-conj1.json`, `latest_sweep.json`, and `openalex_works_cache.json` (`2509.16034` citing entries).
   - `"ThueMorseReduced" "2509.16034" ...` -> same `3` files only.

2. **OpenAlex Citing Papers Checked (`arXiv:2610.14637v1`, `arXiv:2609.16596v1`):**
   - Surfaced by 3h sweep (`sweep.py`, `2026-11-27T01:58:51Z`).
   - Fetched eprints (`tools/.arxiv_cache/eprint/2610.14637/REcomplexity.tex` and `2609.16596/when_low_factor_complexity_forces_palindromic_equality_ejc.tex`) and grepped for `2509.16034|displayconjecture|abelian|4n+2|sign|2-regular|reduced`:
     - `2610.14637v1` (*Generalized reflection complexity*): Studies reflection / $G$-complexity up to antimorphisms; mentions ordinary abelian complexity only as background.
     - `2609.16596v1` (*On the number of palindromic factors of low complexity words*): Studies factor & palindromic complexity and reduced Rauzy graphs; unrelated to $\rho^{\mathrm{ab},\mathrm{red}}_{\mathbf{t}}$.

3. **GitHub Live Checks (`gh api` tree & file inspection, read-only):**
   - `facebookresearch/atlas-lean`: Inspected `MathlibExt/Combinatorics/ThueMorseReducedComplexity.lean` (lines 420–455), `ReducedComplexities.lean` (lines 105–122), and `WantedExt/Combinatorics/ReducedComplexitiesWanted.lean` directly — proves **only** `rhoRed_thueMorse_even` (Theorem 1 of Campbell–Currie–Rampersad for reduced *factor* complexity $\rho^{\mathrm{red}}_t$) and paperfolding results, not $\rho^{\mathrm{ab},\mathrm{red}}_t$ Open Problems (c1)/(c2).
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `JENW1N/complete-math-solutions`, `the-omega-institute/trureturing-tools` (`gh api` trees) -> `0` relevant hits (`CampbellCoupons` / `CampbellHowardConditions` are unrelated).
   - `the-omega-institute/trureturing` (`CONTESTED.md`, `notes/contest-helper-campbell.md`): Settles odd recurrence, eq. (11), and non-$k$-automaticity only; explicitly leaves (c1) sign and (c2) $\rho(4n)$ recursion unsettled.

4. **Zenodo API (`https://zenodo.org/api/records`):**
   - `q=2509.16034` -> `0` hits; `q="reduced abelian complexity"` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `facebookresearch/atlas-lean` (`ThueMorseReducedComplexity.lean`): Formalizes Theorem 1 (`rhoRed_thueMorse_even`) of `2509.16034v1`, not `rhoAbRed` Open Problems (c1)/(c2).
- `the-omega-institute/trureturing` (`04a561c88d`, `96baee8682`): Settled odd recurrence, eq. (11), and non-$k$-automaticity (now credited as prior art under rescoped `TARGET.md`); leaves (c1) and (c2) open.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.

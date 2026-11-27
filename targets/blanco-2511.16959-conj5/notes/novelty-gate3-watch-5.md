# Gate 3 Novelty Re-Check — `blanco-2511.16959-conj5` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:40:57Z`
- **Target:** `targets/blanco-2511.16959-conj5/TARGET.md`
- **Verdict:** **PASS** (no public proof or disproof of Blanco et al. `arXiv:2511.16959v3` Conjecture 5 `con:F_k(n)` found across live arXiv, OpenAlex citing papers `2610.30892v1`/`2603.22195v1`, Zenodo, `470` snapshots, `the-omega-institute/trureturing*`, or all 15 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"... 2511.16959 con:F_k(n) ..."` -> only `watch/snapshots/arxiv/citing/blanco-2511.16959-conj5.json`, `latest_sweep.json`, and `openalex_works_cache.json`.

2. **OpenAlex Citing Papers Verified (`watch/snapshots/arxiv/citing/blanco-2511.16959-conj5.json`, `2026-11-27T01:59:39Z`):**
   - `arXiv:2610.30892v1` (Lei–Zhao–Zhu–Wu, Oct 2026): Settles Conjectures 2–4 only, not Conjecture 5 `con:F_k(n)`.
   - `arXiv:2603.22195v1` (*CayleyPy-4: AI-Holography*, Chervov et al.): Extracted eprint (`tools/.arxiv_cache/eprint/2603.22195/`) and grepped for `2511.16959|Blanco|F_k|Conjecture 5`; `2511.16959` appears only in `biblio.bib` (does not settle Conjecture 5).

3. **GitHub Live Checks (`gh api` trees & file checks across 15 competing repos, read-only):**
   - `rainwangphy/aftd-platform`: Inspected `PrefixReversalNecessaryConditionsNotSufficient.lean` and `NotPrefixReversalSumBoundNecessary.lean` (plus sibling `PrefixReversal*` files) — formalize Conjectures 1–4 only, not Conjecture 5 `con:F_k(n)`.
   - `the-omega-institute/trureturing#20814`: Open empty preregistration (`comments: []`, `0` PRs).
   - Checked `aliromman/math`, `KnowledgeSense/math`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds` (`prefix` / `2511` hits are unrelated internal review/audit names), `linustalacko/small-true-things`, `chy4pro/automath`, `Varun-Dudipala/sun-conjectures-lean` -> `0` relevant hits.

4. **arXiv Live API & Zenodo:**
   - `2511.16959v3` (`2025-11-21`, revised `2026-09-22`) sole/latest version; Zenodo `q=2511.16959` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2610.30892v1` and `rainwangphy/aftd-platform` (`PrefixReversal*`): Settle Conjectures 2–4 (`conj:mod4`, `conj:mod2`, `conj:km_sum`) and refute Conjecture 1 only, not Conjecture 5 (`con:F_k(n)`).
- `the-omega-institute/trureturing#20814`: Open empty preregistration issue (`0` comments, `0` PRs).
- `CONTESTED.md`: absent from `targets/blanco-2511.16959-conj5/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.

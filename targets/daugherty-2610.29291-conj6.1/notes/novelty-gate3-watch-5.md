# Gate 3 Novelty Re-Check — `daugherty-2610.29291-conj6.1` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:20:00Z`
- **Target:** `targets/daugherty-2610.29291-conj6.1/TARGET.md`
- **Verdict:** **PASS** (no public refutation or proof of Daugherty et al. `arXiv:2610.29291v1` Conjecture 6.1 `conj:box` found across live arXiv, OpenAlex citing check, Zenodo, `469` snapshots, or all 13 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `469` files):**
   - `"2610.29291" "conj:box" "(6,5,5,3,2,1)" "(6,5,5,3,3,1)"` -> only `watch/snapshots/arxiv/citing/daugherty-2610.29291-conj6.1.json`, `openalex_works_cache.json`, and `rainwangphy__aftd-platform.json` description (Conj 6.3).

2. **GitHub Live Checks (`gh api` trees + file checks + `gh search prs`, read-only):**
   - `rainwangphy/aftd-platform`: Inspected `LatinTableauxCountMonoThreeTwoOne.lean` (covers `(3,2,1)->(3,3,1)` only) and `LatinTableauxCountMonoCellAdditionTopRow.lean` (covers Proposition 5.5 top-row addition only); remaining `LatinTableaux*` files address Conjecture 6.3.
   - `valyuAI/research`: `maths/combinatorics/latin-squares/latin-tableaux-staircase-count/` covers Conjecture 6.3 only.
   - `aliromman/math` (`Boxes.lean` is `AlabamaParadox`), `CrocSwap/integer-mult-bounds` (`655` substrings in run IDs only), `KnowledgeSense/math`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `linustalacko/small-true-things` -> `0` relevant hits.
   - `the-omega-institute/trureturing` PR search -> `0` hits (`#20269` / `#26377` cover Conj 6.3 / 6.2 only).

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`), OpenAlex Citing Cache, & Zenodo:**
   - `all:2610.29291` -> `1` entry (`2610.29291v1`, `2026-10-21T06:45:39Z`, sole/latest version).
   - `watch/snapshots/arxiv/citing/daugherty-2610.29291-conj6.1.json` (`2026-11-27T01:59:43Z`): `citing_count: 0`, `errors: []`.
   - Zenodo `q=2610.29291` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `rainwangphy/aftd-platform` (`LatinTableauxCountMonoThreeTwoOne.lean`, `LatinTableauxCountMonoCellAdditionTopRow.lean`): Settle only `(3,2,1)->(3,3,1)` and top-row Proposition 5.5 (plus Conj 6.3), not `conj:box` for middle rows.
- `valyuAI/research` (`latin-tableaux-staircase-count`): Covers Conjecture 6.3 only.
- `CONTESTED.md`: absent from `targets/daugherty-2610.29291-conj6.1/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.

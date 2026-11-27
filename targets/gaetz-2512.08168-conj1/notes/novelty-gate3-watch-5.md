# Gate 3 Novelty Re-Check — `gaetz-2512.08168-conj1` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:40:57Z`
- **Target:** `targets/gaetz-2512.08168-conj1/TARGET.md`
- **Verdict:** **PASS** (no public proof or counterexample to Gaetz–Gao `arXiv:2512.08168v2` Conjecture 1.3 `conj:union-intersection` found across live arXiv, OpenAlex citing check, Zenodo, `470` snapshots, or all 15 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"... 2512.08168 conj:union-intersection ..."` -> only `watch/snapshots/arxiv/citing/gaetz-2512.08168-conj1.json`, `openalex_works_cache.json`, and `the-omega-institute__trureturing-tools.json:1484` (which targets Conjecture **1.9**, not Conjecture 1.3).

2. **GitHub Live Checks (`gh api` trees across 15 competing repos, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, `Varun-Dudipala/sun-conjectures-lean` -> `0` relevant hits (`CrocSwap` `check-2512` is an unrelated efficient1500 packet ID).

3. **arXiv Live API, OpenAlex Citing Cache, & Zenodo:**
   - `2512.08168v2` (`2025-12-09`, revised `2026-06-08`) sole/latest version.
   - `watch/snapshots/arxiv/citing/gaetz-2512.08168-conj1.json` (`2026-11-27T01:59:48Z`): `citing_count: 0`, `errors: []`.
   - Zenodo `q=2512.08168` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute__trureturing-tools.json:1484`: Explicitly concerns `arXiv:2512.08168` Conjecture 1.9 only.
- `CONTESTED.md`: absent from `targets/gaetz-2512.08168-conj1/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.

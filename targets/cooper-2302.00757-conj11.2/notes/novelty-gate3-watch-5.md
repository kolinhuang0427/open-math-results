# Gate 3 Novelty Re-Check — `cooper-2302.00757-conj11.2` (watch-5)

- **UTC Timestamp:** `2026-11-27T02:22:20Z`
- **Target:** `targets/cooper-2302.00757-conj11.2/TARGET.md`
- **Verdict:** **PASS** (no public proof of Cooper `arXiv:2302.00757v2` Conjecture 11.2 found across live arXiv, OpenAlex citing check, Zenodo, `413` snapshots, or all inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `413` files):**
   - `"A360949" ... "2302.00757" "Shaun Cooper" ...` -> only `watch/snapshots/arxiv/citing/cooper-2302.00757-conj11.2.json`, `latest_sweep.json`, and `openalex_works_cache.json`.

2. **OpenAlex Citing Paper Verified (`arXiv:2604.14219v2`):**
   - Surfaced by 3h sweep (`sweep.py`, `2026-11-27T01:58:51Z`): *Eta-products, Eichler integrals, and the level-8 Apery limit*.
   - Fetched eprint (`tools/.arxiv_cache/eprint/2604.14219/v4_final.tex`) and grepped for `2302.00757|T_{?11}?|Conjecture 11|mod 9|mod 25|Cooper`: cites `[Cooper2023]` (`2302.00757`) only for `Table 2, level 8`; does not discuss level 11 ($T_{11}$) or Conjecture 11.2.

3. **GitHub Live Checks (`gh api repos/.../git/trees/HEAD?recursive=1` + `gh search`, read-only):**
   - Checked `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `the-omega-institute/trureturing-tools` (plus earlier `gh search` on `the-omega-institute/trureturing`):
   - `KnowledgeSense/math` hits (`Apery-Polynomials-as-Stieltjes-Moment-Sequences`, `Numerical-Semigroups`), `rainwangphy/aftd-platform` (`Cooperative*`), and `facebookresearch/atlas-lean` (`Karp/Cooper.lean`) are all unrelated name/word collisions. Zero hits on `2302.00757` or $T_{11}$.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`) & Zenodo:**
   - `all:2302.00757` -> `1` entry (`2302.00757v2`, `2023-02-01T21:03:06Z`, sole/latest version).
   - Zenodo `q=2302.00757` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2604.14219v2`: Cites `2302.00757` only for the level-8 Apéry limit ($s_n$, `Table 2`), not level 11 / Conjecture 11.2.
- `CONTESTED.md`: absent from `targets/cooper-2302.00757-conj11.2/`.
- See `targets/cooper-2302.00757-conj11.2/notes/novelty-gate2-watch-5.md` (`2026-11-27T00:08:52Z`) for Gate 2 details.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.

# Gate 2 Novelty Check — `ragunathan-2603.29978-conj6.1` (watch-5)

- **UTC Timestamp:** `2026-11-27T02:00:39Z`
- **Target:** `targets/ragunathan-2603.29978-conj6.1/TARGET.md`
- **Verdict:** **PASS** (no public proof or disproof of Ragunathan–Van Tuyl `arXiv:2603.29978v2` Conjecture 6.1 found across arXiv, Zenodo, Crossref, web search, `413` snapshots, or competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py`):**
   - `"2603.29978" "Ragunathan" "vdw(n,k)" "van der Waerden simplicial"` across `369` files -> `0` hits; across `413` files -> only `watch/snapshots/arxiv/citing/ragunathan-2603.29978-conj6.1.json` and `openalex_works_cache.json` (`2603.29978` entry).

2. **GitHub Live Checks (`gh search` & `gh api` tree checks, read-only):**
   - `gh search code` (`"2603.29978 OR Ragunathan"`) across `aliromman/math`, `the-omega-institute/trureturing`, `the-omega-institute/trureturing-tools`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, and `facebookresearch/atlas-lean` -> `0` matching code results in all 7 repos.
   - `gh api repos/<repo>/git/trees/HEAD?recursive=1` across `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, and `the-omega-institute/trureturing-tools` -> `0` matching paths for `2603|29978|ragunathan|vdw` (`atlas-lean` hits on `VanDerWaerden` are all additive combinatorics / Szemerédi / game theory, unrelated to `vdw(n,k)` simplicial complexes).
   - `gh search issues "2603.29978"` -> `0` issues.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2603.29978` -> `1` entry (`2603.29978v2`, `2026-03-31T16:40:22Z`, revised `2026-08-19`, sole/latest version).
   - `au:Ragunathan AND all:Lefschetz` -> `1` entry (`2603.29978v2` only).
   - `all:"van der Waerden simplicial"` -> `1` entry (`2603.29978v2` only).

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2603.29978` -> `0` hits.
   - Crossref `query="2603.29978"` -> unrelated numeric collisions only (`29978`).
   - `search_web`: `"2603.29978" OR ("Ragunathan" "Van Tuyl" "2603.29978") OR ("van der Waerden simplicial complex" "Lefschetz")` -> surfaces only `arXiv:2603.29978`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/ragunathan-2603.29978-conj6.1/`.

## What Was Not Covered

- **Semantic Scholar (`HTTP 429` unauthenticated):** not queried live; **OpenAlex** checked in 3h sweep (`sweep.py`) with `citing_count` clean (0 matching citing works in `potential_matches`).
- Closed-access journals and unindexed private notes.

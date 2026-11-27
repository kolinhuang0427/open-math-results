# Gate 3 Novelty Re-Check — `linusson-2512.24346-conj1` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:08:25Z`
- **Target:** `targets/linusson-2512.24346-conj1/TARGET.md`
- **Verdict:** **PASS** (no public proof, counterexample, or citing settlement found across live arXiv, OpenAlex citing check, Zenodo, Crossref, web search, local snapshots, `aliromman/math`, or `the-omega-institute/trureturing-tools`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 333 files incl. `aliromman__math.json` & `trureturing-tools.json`):**
   - `2512.24346 Linusson "K-Plancherel" "k-core"` -> 10 lines across 4/333 files (`aliromman__math.json` lines 196, 745 are *other* Linusson conjectures: Leander–Linusson fixed-edge orientation and Janson–Linusson Markov chain `1 - 2/e`; `Argus-AiTeam__argus-mathematics/files.txt` is unrelated `finite-network-core`; `linusson-2512.24346-conj1.json` & `openalex_works_cache.json` are local sweep files).
   - `"2512.24346" "ozdemir" "Özdemir" "k-Plancherel"` -> only `watch/snapshots/arxiv/citing/linusson-2512.24346-conj1.json` and `openalex_works_cache.json`.

2. **GitHub Live Checks (`gh search` / `gh api`, read-only):**
   - `gh search prs --repo aliromman/math "2512.24346 OR Linusson ..."` -> 0 matches.
   - `gh search code --repo aliromman/math "2512.24346 ... OR Linusson"` -> 0 matches.
   - `gh api "repos/aliromman/math/pulls?state=all&per_page=100"` filtered for `2512|linusson|plancherel|k-core` -> 0 matches (`NO_PR_MATCH`).
   - `gh search code --repo the-omega-institute/trureturing-tools "2512.24346 ... OR Linusson"` and `contents` check -> 0 matches (`NO_TRUTOOLS_MATCH`).
   - `gh search prs --repo the-omega-institute/trureturing "2512.24346 ... OR Linusson"` -> 0 matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2512.24346` -> 1 entry (`2512.24346v1`, `2025-12-30T16:57:46Z`, sole/latest version).
   - `au:Linusson AND all:Plancherel` -> 1 entry (`2512.24346v1` only).
   - `all:"k-Plancherel"` -> 1 entry (`2512.24346v1` only).

4. **OpenAlex Citing Check (`watch/snapshots/arxiv/citing/linusson-2512.24346-conj1.json`):**
   - Checked at `2026-11-26T22:55:37Z` during 3h sweep (`errors: []`): `citing_count: 0`, `citing_works: []`.

5. **Zenodo API (`https://zenodo.org/api/records`):**
   - `q=2512.24346` -> `0` hits; `q="k-Plancherel"` -> `1` unrelated hit (`15706557`, *Revisión de la teoría de Boehmians*, 2014).

6. **Crossref API (`https://api.crossref.org/works`) & Web Search (`search_web`):**
   - Crossref `query="2512.24346"` -> only unrelated numerical catalog matches (`10.1163/2210-7886_asc-24346`, etc.), no citing/published settlement.
   - `search_web`: `"2512.24346" OR ("Linusson" "k-Plancherel" "complement")` -> only primary preprint `arXiv:2512.24346`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `aliromman/math` (`aliromman__math.json` lines 196, 745): Contains proofs/disproofs of *different* Svante Linusson conjectures (Leander–Linusson fixed-edge correlation Conj 2; Janson–Linusson random-state bound `1 - 2/e`), not Linusson–Özdemir `2512.24346` `conj:complement`.
- `CONTESTED.md`: absent from `targets/linusson-2512.24346-conj1/`.

## What Was Not Covered

- Unindexed private manuscripts, closed-access journals without Crossref/arXiv references to `2512.24346`, or GitHub repos outside indexed snapshots not surfaced by `gh search`.

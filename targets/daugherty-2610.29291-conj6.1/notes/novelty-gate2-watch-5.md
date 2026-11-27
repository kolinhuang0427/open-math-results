# Gate 2 Novelty Check — `daugherty-2610.29291-conj6.1` (watch-5)

- **UTC Timestamp:** `2026-11-27T00:37:12Z`
- **Target:** `targets/daugherty-2610.29291-conj6.1/TARGET.md`
- **Verdict:** **PASS** (no public proof or counterexample to Daugherty et al. `arXiv:2610.29291v1` Conjecture 6.1 `conj:box` found across arXiv, Zenodo, Crossref, web search, 357 local snapshots, `aliromman/math`, `KnowledgeSense/math`, or `the-omega-institute/trureturing`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 357 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"A079727" "079727" "conj:box" "(6,5,5,3,2,1)" "2610.29291"` -> `0` hits for `conj:box`, `(6,5,5,3,2,1)`, or `2610.29291`.

2. **GitHub Live Checks (`gh search` / `gh issue view`, read-only):**
   - `gh search code --repo aliromman/math "... 2610.29291 OR Daugherty"` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "... 2610.29291 OR Daugherty"` -> `0` matches.
   - `gh search code/prs --repo the-omega-institute/trureturing "... 2610.29291"` -> `0` matches.
   - `gh search issues "2610.29291"` -> only `the-omega-institute/trureturing#20269` (open preregistration for Conjecture **6.3**, `comments: []`).

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2610.29291` -> `1` entry (`2610.29291v1`, `2026-10-21T06:45:39Z`, sole/latest version).
   - `au:Daugherty AND all:2610` -> `2` entries (`2610.39257v1` *The Stable Tamari Lattice* and `2610.29291v1`).

4. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2610.29291` -> `0` hits; Crossref `query="2610.29291"` -> unrelated numeric substring collisions (`29291`).
   - `search_web`: `"2610.29291" "Conjecture 6.1" OR "conj:box" "Latin tableaux" OR "LT(6,5,5,3,2,1)"` -> returns only `arXiv:2610.29291`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute/trureturing#20269`: Open preregistration issue targeting Conjecture 6.3 (`0` comments, no PR), not Conjecture 6.1 (`conj:box`).
- `CONTESTED.md`: absent from `targets/daugherty-2610.29291-conj6.1/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live for citing works of `2610.29291`.
- Closed-access journals and unindexed private notes.

# Gate 2 Novelty Check — `li-2505.12035-conj7` (watch-5)

- **UTC Timestamp:** `2026-11-26T23:51:52Z`
- **Target:** `targets/li-2505.12035-conj7/TARGET.md`
- **Verdict:** **PASS** (no public proof or refutation of Li–Lu–Luo `arXiv:2505.12035v1` Conjecture 7 `conj:ore` found across arXiv, Zenodo, Crossref, web search, 356 snapshots, `aliromman/math`, `trureturing`, or `KnowledgeSense/math`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 356 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"2505.12035" "conj:ore" "Li--Lu--Luo" "Hamiltonian Berge"` -> `0 lines across 0/356 files`.
   - `"2505.12035" "3-uniform hypergraph" "Li--Lu--Luo" "4-regular shadow"` -> 5 unrelated lines (`1337` matchings, Győri–Salia short Berge cycle asymptotics, `formal-conjectures` #8129 / `erdos_593`).

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code --repo aliromman/math "... 2505.12035"` -> `0` matches.
   - `gh search code --repo the-omega-institute/trureturing "... 2505.12035"` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "... 2505.12035"` -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2505.12035` -> `1` entry (`2505.12035v1`, `2025-05-17T14:55:02Z`, *An Ore-type theorem for $[3]$-graphs*, sole/latest version).
   - `all:"2505.12035" OR (au:Lu AND all:"3-uniform" AND all:hypergraph AND all:shadow)` -> `1` unrelated earlier entry (`2010.04624v2`, spectral radius of outerplanar 3-uniform hypergraphs).

4. **Zenodo API (`https://zenodo.org/api/records`) & Crossref API (`https://api.crossref.org/works`):**
   - Zenodo `q=2505.12035` -> `0` hits.
   - Crossref `query="2505.12035"` -> unrelated numeric substring collisions (`12035`).

5. **Web Search (`search_web`):**
   - `"2505.12035" OR ("Li" "Lu" "Luo" "2505.12035")` -> returns only the primary May 2025 preprint `arXiv:2505.12035`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:2010.04624v2` (Lu et al., 2020) and `math.CO` snapshot hit on Győri–Salia short Berge cycles: Unrelated to Hamiltonian Berge cycles under the Ore-type shadow degree sum $d_{\partial\mathcal{H}}(u)+d_{\partial\mathcal{H}}(v) \ge n+1$.
- `CONTESTED.md`: absent from `targets/li-2505.12035-conj7/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live for citing works of `2505.12035`.
- Closed-access journals and unindexed private notes.

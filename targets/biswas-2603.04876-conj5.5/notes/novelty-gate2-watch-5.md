# Gate 2 Novelty Check — `biswas-2603.04876-conj5.5` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:01:56Z`
- **Target:** `targets/biswas-2603.04876-conj5.5/TARGET.md`
- **Verdict:** **PASS** (no public proof or refutation of Biswas–Mandal–Saha `arXiv:2603.04876v1` Conjecture 5.5 on connected chordal graphs found across arXiv, OpenAlex citing check, Zenodo, Crossref, web search, `462` snapshots, or 11 competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `462` files):**
   - `"2603.04876" "RV_chordal" "Biswas" "Kamalesh Saha" ...` -> `5` lines across `3/462` files (`watch/snapshots/arxiv/citing/biswas-2603.04876-conj5.5.json`, `latest_sweep.json`, `openalex_works_cache.json`).

2. **GitHub Live Checks (`gh api` trees + `gh search`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds` -> `0` relevant hits (`atlas-lean` `chordal-loewner-equation` and `CrocSwap` `2603` packet ID are unrelated).
   - `gh search issues "2603.04876 OR A400888"` and `gh search prs --repo the-omega-institute/trureturing "2603.04876 OR A400888"` -> `0` results.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2603.04876` -> `1` entry (`2603.04876v1`, `2026-03-05T07:05:37Z`, sole/latest version).
   - `au:Biswas AND all:chordal AND all:"v-number"` -> `1` entry (`2603.04876v1` only).

4. **OpenAlex Citing Cache (`watch/snapshots/arxiv/citing/biswas-2603.04876-conj5.5.json`):**
   - Checked at `2026-11-27T01:59:39Z` during 3h sweep (`errors: []`): `citing_count: 0`, `citing_works: []`.

5. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2603.04876` -> `0` hits; Crossref `query="2603.04876"` -> unrelated ISBN/DOI collisions (`04876`).
   - `search_web`: `"2603.04876" OR ("Biswas" "Mandal" "Saha" "v-number" "chordal")` -> surfaces only `arXiv:2603.04876`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/biswas-2603.04876-conj5.5/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/unindexed private manuscripts.

# Gate 2 Novelty Check — `chang-2201.02781-conj2` (watch-5)

- **UTC Timestamp:** `2026-11-27T00:08:52Z`
- **Target:** `targets/chang-2201.02781-conj2/TARGET.md`
- **Verdict:** **PASS** (no public proof or refutation of Chang–Yang–Yin–Yao Conjecture 2 for general connected graphs $G \neq K_2$ found across arXiv, OpenAlex citing check, Zenodo, Crossref, web search, 357 snapshots, `aliromman/math`, `trureturing`, or `KnowledgeSense/math`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 357 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"2201.02781" "fgndi" "Chang–Yang–Yin–Yao" "neighbor distinguishing"` -> `3` lines across `2/357` files (`watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json` and `openalex_works_cache.json` only).

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code --repo aliromman/math "... 2201.02781 ..."` -> `0` matches.
   - `gh search code --repo the-omega-institute/trureturing "... 2201.02781 ..."` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "... 2201.02781 ..."` -> `0` matches.

3. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:2201.02781` -> `1` entry (`2201.02781v1`, `2022-01-08T07:01:27Z`, sole/latest version).
   - `all:"neighbor distinguishing index" AND all:Chang` -> `0` entries.

4. **OpenAlex Citing Cache (`watch/snapshots/arxiv/citing/chang-2201.02781-conj2.json`):**
   - Checked at `2026-11-26T22:55:31Z` during 3h sweep (`errors: []`): `citing_count: 0`, `citing_works: []`.

5. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=2201.02781` -> `0` hits.
   - Crossref `query="2201.02781"` -> unrelated numeric DOI collisions (`02781`).
   - `search_web`: `"2201.02781" OR ("fgndi" "Chang" "neighbor distinguishing" "Conjecture 2")` -> only primary preprint `arXiv:2201.02781v1`.

## Near Misses & Why They Do Not Settle the Exact Statement

- Cheng–Yang–Yao–Luo (2022, `10.3934/math.2022386`): Settles Conjecture 2 only for Halin graphs, not arbitrary connected graphs $G \neq K_2$.
- Wen–Yue–Li–Lai (2026, `10.1016/j.dam.2026.03.034`) / `10.3390/axioms14070496`: Study proper total colorings (`ftndi_{\sum}`), distinct from non-proper `fgndi_{\sum}`.
- `CONTESTED.md`: absent from `targets/chang-2201.02781-conj2/`.

## What Was Not Covered

- Semantic Scholar (`HTTP 429` unauthenticated) and closed-access/non-English venues without Crossref/arXiv indexing.

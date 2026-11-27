# Gate 2 Novelty Check — `oeis-A350963` (watch-5)

- **UTC Timestamp:** `2026-11-27T02:53:29Z`
- **Target:** `targets/oeis-A350963/TARGET.md`
- **Verdict:** **PASS** (no public proof of N. J. A. Sloane's 2022 conjectured g.f. for OEIS `A350963` found across live OEIS, arXiv, Zenodo, Crossref, web search, `413` snapshots, or 10+ competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `413` files):**
   - `"A350963" "350963" "XXOXX" "A351966" "A351967"` -> `0 lines across 0/413 files`.

2. **GitHub Live Checks (`gh api` trees + `gh search`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, and `DomTheDeveloper/ProofPlaygrond` -> `0` matches (`NO_TREE_MATCH`).
   - `gh search issues "A350963 OR XXOXX"` and `gh search prs --repo the-omega-institute/trureturing "A350963 OR XXOXX"` -> `0` matches.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A350963&fmt=json`):**
   - Confirmed `revision: 54` (`2025-11-05T15:22:48-05:00`) unchanged; still lists `Conjectured g.f.: -(2*t^7-6*t^6-24*t^5-33*t^4-33*t^3-28*t^2-9*t-1)/((1-t^2)*(1-t^4))`.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A350963` -> `0` entries; `all:XXOXX` -> `0` entries.
   - `all:"coordination sequence" AND au:Sloane` -> `2` entries (`1805.10343v1` and `1803.08530v3` *A Coloring Book Approach to Finding Coordination Sequences*, 2018), predating `A350963` (2022).

5. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=A350963` -> `0` hits; `q=XXOXX` -> `0` hits.
   - Crossref `query=A350963` -> `0` results; `query="XXOXX"` -> `0` results.
   - `search_web`: `"A350963" OR ("XXOXX" "coordination sequence") OR ("XXOXX tiling" "Sloane")` -> no mathematical proof found.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:1803.08530v3` (*A Coloring Book Approach to Finding Coordination Sequences*, 2018): Develops the general coloring-book method (4 years before `A350963` was created in Feb 2022); Sloane explicitly suggested applying it to `A350963` as an open conjecture.
- `CONTESTED.md`: absent from `targets/oeis-A350963/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.

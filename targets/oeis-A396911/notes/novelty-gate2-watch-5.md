# Gate 2 Novelty Check — `oeis-A396911` (watch-5)

- **UTC Timestamp:** `2026-11-27T00:47:20Z`
- **Target:** `targets/oeis-A396911/TARGET.md`
- **Verdict:** **PASS** (no public proof of Sean A. Irvine's 2026 conjecture $a(n) \le \frac{3}{2} n^2$ on OEIS `A396911` found across live OEIS, arXiv, Zenodo, Crossref, web search, 357 snapshots, `aliromman/math`, `KnowledgeSense/math`, or `the-omega-institute/trureturing`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 357 files incl. `aliromman__math.json`, `trureturing*.json`, `KnowledgeSense__math.json`):**
   - `"A396911" "396911" "Sean A. Irvine"` -> `0 lines across 0/357 files`.

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code --repo aliromman/math "A396911 OR 396911 OR Irvine"` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "A396911 OR 396911"` -> `0` matches.
   - `gh search code --repo the-omega-institute/trureturing "A396911"` -> `0` matches.
   - `gh search issues "A396911"` -> `0` results.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A396911&fmt=json`):**
   - Confirmed `revision: 48` (`2026-06-22T17:16:16-04:00`) unchanged; open questions by Pontus von Brömssen (Jun 10, 2026) and `Conjecture: a(n) <= (3/2) * n^2. - _Sean A. Irvine_, Jun 21 2026` remain unproved.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A396911` -> `0` entries.

5. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=A396911` -> `0` hits.
   - Crossref `query=A396911` -> `0` results.
   - `search_web`: `"A396911" "Irvine" OR "A396911" "spiral" OR "a(n) <= (3/2)*n^2"` -> returns only OEIS `A396911` (`joeis` computation code noted in Gate 1).

## Near Misses & Why They Do Not Settle the Exact Statement

- `archmageirvine/joeis` (`A396911.java`): Only implements sequence evaluation and notes empirical `a(n) <= phi * n^2`, no proof.
- `CONTESTED.md`: absent from `targets/oeis-A396911/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.

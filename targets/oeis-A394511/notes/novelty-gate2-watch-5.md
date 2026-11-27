# Gate 2 Novelty Check — `oeis-A394511` (watch-5)

- **UTC Timestamp:** `2026-11-27T04:26:22Z`
- **Target:** `targets/oeis-A394511/TARGET.md`
- **Verdict:** **PASS** (no public refutation or proof of Peter Exley's 2026 `A394511` 4.8.8 tiling enclosing-shell conjecture found across live OEIS, arXiv, Zenodo, Crossref, web search, `470` snapshots, or 14 competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"... A394511 394511 Exley ..."` -> `0` hits on `A394511` or `Exley`.

2. **GitHub Live Checks (`gh api` trees + `gh search`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath` -> `0` matches (`NO_TREE_MATCH`).
   - `gh search issues` & `the-omega-institute/trureturing` PR search -> `0` matches.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A394511&fmt=json`):**
   - Confirmed `revision: 47` (`2026-06-06T04:04:55-04:00`) unchanged; still reads `Conjectured (UNVERIFIED beyond n = 23): the minimum shell equals the corona of the optimal hole, |S| = |C(H)|; and a(n) = 2*ceiling((n + 17)/5) for n >= 6...`.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`), Zenodo, Crossref, & Web Search:**
   - `all:"A394511"` -> `0` entries; Zenodo `q=A394511` -> `0` hits; Crossref `query=A394511` -> `0` results.
   - `search_web`: `... OR ("A394511" "Exley")` -> returns only OEIS `A394511`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/oeis-A394511/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.

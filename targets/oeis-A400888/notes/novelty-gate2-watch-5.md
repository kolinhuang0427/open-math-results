# Gate 2 Novelty Check — `oeis-A400888` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:07:00Z`
- **Target:** `targets/oeis-A400888/TARGET.md`
- **Verdict:** **PASS** (no public proof of M. Jeremie Lafitte's 2026 surjectivity conjecture for OEIS `A400888` found across live OEIS, arXiv, Zenodo, Crossref, web search, `462` snapshots, or 11+ competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `462` files):**
   - `"... A400888 400888 Gosper-Lafitte"` -> `0` hits across `462` files.

2. **GitHub Live Checks (`gh api` trees + `gh search`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds` -> `0` matches (`NO_TREE_MATCH`).
   - `gh search issues "2603.04876 OR A400888"` and `gh search prs --repo the-omega-institute/trureturing "2603.04876 OR A400888"` -> `0` results.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A400888&fmt=json`):**
   - Confirmed `revision: 16` (`2026-10-15T16:25:59-04:00`) unchanged; still reads `"It is conjectured that the sequence is surjective onto the positive integers."`.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A400888` -> `0` entries; `all:"Gosper-Lafitte"` -> `0` entries.

5. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=A400888` -> `0` hits; Crossref `query=A400888` -> `0` results.
   - `search_web`: `"A400888" OR ("Gosper-Lafitte" "A400888") OR ("A400888" "surjective" OR "every positive integer")` -> returns only OEIS `A400888`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/oeis-A400888/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.

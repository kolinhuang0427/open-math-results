# Gate 2 Novelty Check — `oeis-A125790` (watch-5)

- **UTC Timestamp:** `2026-11-27T03:28:08Z`
- **Target:** `targets/oeis-A125790/TARGET.md`
- **Verdict:** **PASS** (no public proof of Mikhail Kurkov's May 2025 row generating function conjecture on OEIS `A125790` found across live OEIS, arXiv, Zenodo, Crossref, web search, `469` snapshots, `the-omega-institute/trureturing#29156`, or 13 competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `469` files):**
   - `"A125790" "125790"` -> `0 lines across 0/469 files`.

2. **GitHub Live Checks (`gh api` trees + `gh search` + `gh issue view`, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things` -> `0` matches (`NO_TREE_MATCH`).
   - `gh search issues "A125790"` -> `the-omega-institute/trureturing#29156` (`OPEN`, `comments: []`, empty timeline, no PR): addresses MathOverflow 506710 (Kurkov's Jan 2026 parity transform on columns / `A391910`), NOT the May 2025 row generating function conjecture.
   - `gh search code "A125790"` -> `archmageirvine/joeis` (`A125790.java`, `A391910.java`, etc.) sequence implementations only.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A125790&fmt=json`):**
   - Confirmed `revision: 47` (`2026-03-22T15:37:03-04:00`) unchanged; still lists `Conjecture: g.f. for n-th row is ... - _Mikhail Kurkov_, May 03 2025`.

4. **arXiv Live API (`tools/arxiv_fetch.py`, `use_cache=False`):**
   - `all:A125790` -> `0` entries.

5. **Zenodo API (`https://zenodo.org/api/records`), Crossref (`https://api.crossref.org/works`), & Web Search (`search_web`):**
   - Zenodo `q=A125790` -> `0` hits; Crossref `query=A125790` -> `0` results.
   - `search_web`: `"A125790" "Kurkov" OR ("A125790" "Conjecture") OR ("A125790" "row" "generating function")` -> returns OEIS `A125790` and MathOverflow column-recurrence threads (`504910`/`506710`), no proof of the row g.f. conjecture.

## Near Misses & Why They Do Not Settle the Exact Statement

- `the-omega-institute/trureturing#29156` & MathOverflow `504910`/`505968`/`506710`/`506732`: Target Kurkov's Jan 2026 *column* transforms / `A391910`, not the May 2025 *row* generating function conjecture.
- `CONTESTED.md`: absent from `targets/oeis-A125790/`.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.

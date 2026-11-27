# Gate 3 Novelty Re-Check — `oeis-A400888` (watch-5)

- **UTC Timestamp:** `2026-11-27T04:49:33Z`
- **Target:** `targets/oeis-A400888/TARGET.md`
- **Verdict:** **PASS** (no public proof of M. Jeremie Lafitte's 2026 surjectivity conjecture for OEIS `A400888` found across live OEIS rev 16, arXiv, Zenodo, `470` snapshots, or all 15 inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `470` files):**
   - `"A400888" "400888" "Gosper-Lafitte"` -> `0 lines across 0/470 files`.

2. **GitHub Live Checks (`gh api` trees across 15 competing repos, read-only):**
   - Checked `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `the-omega-institute/trureturing-tools`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `CrocSwap/integer-mult-bounds`, `linustalacko/small-true-things`, `chy4pro/automath`, and `joaquimmj/oeis-conjectures` -> `0` matches (`NO_TREE_MATCH`).

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A400888&fmt=json`), arXiv, & Zenodo:**
   - OEIS `A400888` `revision: 16` (`2026-10-15T16:25:59-04:00`) unchanged.
   - `tools/arxiv_fetch.py` `all:A400888` (`use_cache=False`) -> `0` entries; Zenodo `q=A400888` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/oeis-A400888/`.
- See `targets/oeis-A400888/notes/novelty-gate2-watch-5.md` (`2026-11-27T03:07:00Z`) for Gate 2 Crossref/web search details.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.

# Gate 3 Novelty Re-Check — `oeis-A360949` (watch-5)

- **UTC Timestamp:** `2026-11-27T02:00:39Z`
- **Target:** `targets/oeis-A360949/TARGET.md`
- **Verdict:** **PASS** (no public proof of Paul D. Hanna's 2023 `A360949` mod-4 conjecture found across live OEIS, Zenodo, `413` snapshots, or all inspected competing GitHub repos)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across `413` files):**
   - `"A360949" "A161674" ...` -> only `watch/snapshots/formal/last_sweep.json` (`oeis-A360949` entry).

2. **GitHub Live Checks (`gh api repos/.../git/trees/HEAD?recursive=1` + `gh search`, read-only):**
   - Checked `JENW1N/complete-math-solutions`, `TheJustinSunPrize/awards`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `facebookresearch/atlas-lean`, `the-omega-institute/trureturing-tools` (plus earlier `gh search` on `the-omega-institute/trureturing`) -> `0` matches (`NO_TREE_MATCH`).

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A360949&fmt=json`) & Zenodo:**
   - `revision: 15` (`2023-03-05T12:37:19-05:00`) unchanged.
   - Zenodo `q=A360949` -> `0` hits.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/oeis-A360949/`.
- See `targets/oeis-A360949/notes/novelty-gate2-watch-5.md` (`2026-11-26T23:51:52Z`) for prior live arXiv, Crossref, web search, and unrelated Hanna-conjecture details.

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`) for live queries.
- Closed-access journals and unindexed private notes.

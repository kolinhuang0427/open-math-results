# Gate 3 Novelty Re-Check — `oeis-A061313` (watch-5)

- **UTC Timestamp:** `2026-11-27T00:08:52Z`
- **Target:** `targets/oeis-A061313/TARGET.md`
- **Verdict:** **PASS** (no public proof of Zabolotskii's 2020 `A061313` conjecture found across live OEIS, 357+ snapshots, `aliromman/math`, `KnowledgeSense/math`, or `the-omega-institute/trureturing*`)

## Sources & Exact Queries

1. **Local Watch Snapshots (`tools/novelty_grep.py` across 357 files incl. `aliromman__math.json`, `KnowledgeSense__math.json`, `trureturing.json`, `trureturing-tools.json`):**
   - `"A061313" "Zabolotskii" "A379818" "binomial(m+2"` -> `0 lines across 0/357 files`.

2. **GitHub Live Checks (`gh search`, read-only):**
   - `gh search code --repo aliromman/math "... A061313 ..."` -> `0` matches.
   - `gh search code --repo KnowledgeSense/math "... A061313 ..."` -> `0` matches.
   - `gh search code/prs --repo the-omega-institute/trureturing "... A061313 ..."` -> `0` matches.

3. **Live OEIS JSON (`https://oeis.org/search?q=id:A061313&fmt=json`):**
   - Confirmed `revision: 58` (`2026-11-01T16:49:49-05:00`) unchanged.

## Near Misses & Why They Do Not Settle the Exact Statement

- `CONTESTED.md`: absent from `targets/oeis-A061313/`.
- See `targets/oeis-A061313/notes/novelty-gate2-watch-5.md` (`2026-11-26T23:31:11Z`) for live arXiv (`au:Zabolotskii`), Zenodo, Crossref, and web search details (all unchanged).

## What Was Not Covered

- **OpenAlex & Semantic Scholar:** Exhausted unauthenticated daily IP quota (`HTTP 429 Too Many Requests`), not queried live.
- Closed-access journals and unindexed private notes.

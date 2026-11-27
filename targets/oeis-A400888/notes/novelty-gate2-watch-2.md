# Gate 2 Novelty Receipt — `oeis-A400888`

- **UTC Time:** 2026-11-27T03:29:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #707)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "A400888" "400888" "Gosper-Lafitte"`: 0 hits across 469 files.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A400888&fmt=json`):**
   - Revision 16 (`2026-10-15T16:25:59-04:00`) still states *"It is conjectured that the sequence is surjective onto the positive integers."*
3. **Live GitHub (`gh api`, read-only):**
   - Checked recursive trees (`git/trees/HEAD?recursive=1`) for `400888` / `gosper`: 0 matches across `JENW1N/complete-math-solutions`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `joaquimmj/oeis-conjectures`, `dvgyl/oeis-proofs`, `linustalacko/small-true-things`, `the-omega-institute/trureturing-tools`, `VladimirReshetnikov/ProveIt`.
4. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=A400888+OR+%22Gosper-Lafitte%22`: `total: 0`.
   - `search_web` for `"A400888" OR ("Gosper-Lafitte" "Stern" "surjective")`: returns only OEIS A400888; no proof found.

## Near Misses & Why They Do Not Settle the Exact Statement

- OEIS A400888 comment notes divisibility by every $m \ge 1$ and infinitely many occurrences of every even positive integer, leaving odd surjectivity conjectured.

## What Was Not Covered

- GitHub `search/issues` API (skipped due to earlier 403 rate-limit window); closed-access journals and private repositories not indexed by OEIS, GitHub, Zenodo, or web search.

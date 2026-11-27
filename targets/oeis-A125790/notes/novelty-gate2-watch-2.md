# Gate 2 Novelty Receipt — `oeis-A125790`

- **UTC Time:** 2026-11-27T03:29:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #707)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "A125790" "125790" "Mikhail Kurkov"`: 0 hits for `A125790` across 469 files (`trureturing-tools` hit is `A057032`/`A057063`, unrelated).
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A125790&fmt=json`):**
   - Revision 47 (`2026-03-22T15:37:03-04:00`) still lists Mikhail Kurkov's May 03, 2025 row generating function formula as `Conjecture`.
3. **Live GitHub (`gh api`, read-only):**
   - Checked recursive trees (`git/trees/HEAD?recursive=1`) for `125790` / `kurkov`: 0 matches across `JENW1N/complete-math-solutions`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `joaquimmj/oeis-conjectures`, `dvgyl/oeis-proofs`, `linustalacko/small-true-things`, `the-omega-institute/trureturing-tools`, `VladimirReshetnikov/ProveIt`.
4. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=A125790`: `total: 0`.
   - `search_web` for `"A125790" OR ("T(n,k) = T(n,k-1) + T(n-1,2*k)" "Kurkov")`: no proof of the row generating function conjecture found.

## Near Misses & Why They Do Not Settle the Exact Statement

- Kurkov's Jan 07, 2026 column recursion formulas in `A125790` (linked to `A391910` and MO `505968`/`506732` as verified in Gate 1) address column EGFs, not the May 03, 2025 row generating function conjecture.

## What Was Not Covered

- GitHub `search/issues` API (skipped due to earlier 403 rate-limit window); closed-access journals and private repositories not indexed by OEIS, GitHub, Zenodo, or web search.

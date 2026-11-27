# Gate 2 Novelty Receipt — `chervov-2509.19162-conj9`

- **UTC Time:** 2026-11-27T04:02:00Z
- **Reviewer:** `watch-2` (co-covering Gate 2 per coordinator #741)
- **Verdict:** **PASS**

## Sources Checked & Exact Queries

1. **Local watch snapshots (`watch/snapshots/**`):**
   - `.venv/bin/python tools/novelty_grep.py "2509.19162" "A136184" "CayleyPy"`: 0 hits across 469 files.
2. **arXiv (`tools/arxiv_fetch.py`):**
   - `query --id-list 2509.19162`: `2509.19162v2` (updated `2026-04-01T15:54:42Z`, no journal-ref/DOI) remains latest.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A136184&fmt=json`):**
   - Revision 31 (`2026-09-17T22:32:10-04:00`) links `arXiv:2509.19162` and lists no disproof of Conjecture 9.
4. **Live GitHub (`gh api`, read-only):**
   - Checked recursive trees (`git/trees/HEAD?recursive=1`) for `2509.19162`, `136184`, `chervov`, `cayleypy`, `unitriangular`: 0 matches across `JENW1N/complete-math-solutions`, `aliromman/math`, `KnowledgeSense/math`, `rainwangphy/aftd-platform`, `valyuAI/research`, `GuillaumeBAUD-coder/open-math-agents`, `DomTheDeveloper/open-math-agents`, `DomTheDeveloper/ProofPlaygrond`, `joaquimmj/oeis-conjectures`, `dvgyl/oeis-proofs`, `linustalacko/small-true-things`, `the-omega-institute/trureturing-tools`.
5. **Zenodo API & Web Search:**
   - `https://zenodo.org/api/records?q=%222509.19162%22`: `total: 0`.
   - `search_web` for `"2509.19162" "A136184" OR ("U(n, Z/2Z)" "metacyclic") OR ("CayleyPy" "Conjecture 9")`: returns only `2509.19162`.

## Near Misses & Why They Do Not Settle the Exact Statement

- `arXiv:math/0510506` (Ellenberg–Tymoczko): proves asymptotic $\Theta(np + n^2 \log p)$ diameter up to an unspecified constant, without comparing to `A136184` ($O(n^3)$).

## What Was Not Covered

- GitHub `search/issues` API (not re-queried after earlier 403 rate-limit window); closed-access journals and private repositories not indexed by arXiv, GitHub, Zenodo, OEIS, or web search.

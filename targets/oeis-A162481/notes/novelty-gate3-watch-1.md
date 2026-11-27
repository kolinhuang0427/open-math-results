# Gate 3 Novelty Receipt — `targets/oeis-A162481/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:36Z`
- **Target:** OEIS `A162481` (`rev. 23`, `2025-10-09`), R. J. Mathar's Dec 11 2011 conjectured 4-term recurrence `(n+1)*a(n) + 2*(1-4*n)*a(n-1) + 2*(5*n-3)*a(n-2) + 4*(2-n)*a(n-3) + (n-3)*a(n-4) = 0`.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A162481"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` hits.
   - Zenodo `10.5281/zenodo.24366920` & `10.5281/zenodo.23760779` -> `0` hits.
3. **Live OEIS JSON (`11:36Z`):**
   - `https://oeis.org/search?q=id:A162481&fmt=json` -> `rev. 23` (`2025-10-09T23:21:43-04:00`), unchanged, Mathar's recurrence still marked `Conjecture:`.
4. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A162481"'` -> `0`; Zenodo `q=A162481` -> `0`; `gh search issues`/`prs` -> `0`; `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Private repositories and works without `A162481` identifiers are not covered.

# Gate 3 Novelty Receipt — `targets/oeis-A157002/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:34Z` (confirming `11:31Z` live sweep)
- **Target:** OEIS `A157002` (`rev. 15`, `2025-09-22`), R. J. Mathar's Nov 19 2014 conjectured 4-term recurrence `(n+1)*a(n) + 3*(-n+1)*a(n-1) + 2*(-2*n+1)*a(n-2) + 2*(2*n-7)*a(n-3) + 2*(2*n-7)*a(n-4) = 0`.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A157002"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` hits.
   - Zenodo `10.5281/zenodo.24366920` (`46` OEIS IDs) & `10.5281/zenodo.23760779` (`12` OEIS IDs) -> `0` hits.
3. **Live OEIS JSON (`11:34Z`):**
   - `https://oeis.org/search?q=id:A157002&fmt=json` -> `rev. 15` (`2025-09-22T16:00:57-04:00`), unchanged, Mathar's recurrence still marked `Conjecture:`.
4. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A157002"'` -> `0`; Zenodo `q=A157002` -> `0`; `gh search issues`/`prs` -> `0`; `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** Guoce Xin (`arXiv:0712.0933`, cited on OEIS `A157002`) studies only the Somos-4 Hankel determinant.
- **Coverage limits:** Private repositories and works without `A157002` identifiers are not covered.

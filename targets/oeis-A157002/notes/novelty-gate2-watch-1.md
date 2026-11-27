# Gate 2 Novelty Receipt — `targets/oeis-A157002/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:31Z`
- **Target:** OEIS `A157002` (`rev. 15`, `2025-09-22`), R. J. Mathar's Nov 19 2014 conjectured 4-term recurrence `(n+1)*a(n) + 3*(-n+1)*a(n-1) + 2*(-2*n+1)*a(n-2) + 2*(2*n-7)*a(n-3) + 2*(2*n-7)*a(n-4) = 0`.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`653` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A157002"` -> `0` lines across `0/653` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` matches.
   - Zenodo `10.5281/zenodo.24366920` (46 OEIS IDs) & `10.5281/zenodo.23760779` (12 OEIS IDs) -> `0` matches.
3. **Live OEIS JSON:**
   - `https://oeis.org/search?q=id:A157002&fmt=json` -> `rev. 15` (`2025-09-22T16:00:57-04:00`), unchanged, Mathar's recurrence still marked `Conjecture:`.
4. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A157002"'` -> `total_results: 0`.
   - `curl -s "https://zenodo.org/api/records?q=A157002&size=5"` -> `0` hits.
5. **Live GitHub Issues/PRs & Web Search:**
   - `gh search issues '"A157002"'` & `gh search prs '"A157002"'` -> `0` hits each.
   - `search_web` (`"A157002" Mathar OR recurrence OR proof`) -> only OEIS `A157002` itself; no proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** Guoce Xin (`arXiv:0712.0933`, cited on OEIS `A157002`) studies the Somos-4 Hankel determinant only, not Mathar's recurrence.
- **Coverage limits:** Private repositories and works without OEIS identifier strings are not covered.

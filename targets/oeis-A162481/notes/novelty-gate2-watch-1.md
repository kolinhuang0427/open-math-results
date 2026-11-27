# Gate 2 Novelty Receipt — `targets/oeis-A162481/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:31Z`
- **Target:** OEIS `A162481` (`rev. 23`, `2025-10-09`), R. J. Mathar's Dec 11 2011 conjectured 4-term recurrence `(n+1)*a(n) + 2*(1-4*n)*a(n-1) + 2*(5*n-3)*a(n-2) + 4*(2-n)*a(n-3) + (n-3)*a(n-4) = 0`.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`653` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A162481"` -> `0` lines across `0/653` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` matches.
   - Zenodo `10.5281/zenodo.24366920` (46 OEIS IDs) & `10.5281/zenodo.23760779` (12 OEIS IDs) -> `0` matches.
3. **Live OEIS JSON:**
   - `https://oeis.org/search?q=id:A162481&fmt=json` -> `rev. 23` (`2025-10-09T23:21:43-04:00`), unchanged, Mathar's recurrence still marked `Conjecture:`.
4. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A162481"'` -> `total_results: 0`.
   - `curl -s "https://zenodo.org/api/records?q=A162481&size=5"` -> `0` hits.
5. **Live GitHub Issues/PRs & Web Search:**
   - `gh search issues '"A162481"'` & `gh search prs '"A162481"'` -> `0` hits each.
   - `search_web` (`"A162481" Mathar OR recurrence OR proof`) -> no proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Private repositories and works without OEIS identifier strings are not covered.

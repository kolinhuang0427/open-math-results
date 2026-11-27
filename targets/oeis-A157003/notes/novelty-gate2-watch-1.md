# Gate 2 Novelty Receipt — `targets/oeis-A157003/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:33Z`
- **Target:** OEIS `A157003` (`rev. 37`, `2025-11-05`), R. J. Mathar's Nov 19 2014 conjectured 6-term recurrence `(n+1)*a(n) + (n+2)*a(n-1) + (-21*n+29)*a(n-2) + (3*n-16)*a(n-3) + 40*(n-3)*a(n-4) + 2*(-2*n+7)*a(n-5) + 10*(-2*n+9)*a(n-6) = 0`.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A157003"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` matches.
   - Zenodo `10.5281/zenodo.24366920` (46 OEIS IDs) & `10.5281/zenodo.23760779` (12 OEIS IDs) -> `0` matches.
3. **Live OEIS JSON:**
   - `https://oeis.org/search?q=id:A157003&fmt=json` -> `rev. 37` (`2025-11-05T15:22:17-05:00`), unchanged, Mathar's recurrence still marked `Conjecture:`.
4. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A157003"'` -> `total_results: 0`.
   - `curl -s "https://zenodo.org/api/records?q=A157003&size=5"` -> `0` hits.
5. **Live GitHub Issues/PRs & Web Search:**
   - `gh search issues '"A157003"'` & `gh search prs '"A157003"'` -> `0` hits each.
   - `search_web` (`"A157003" Mathar OR Kotesovec OR recurrence OR proof`) -> only OEIS `A157003` and combinatorial pattern-avoidance / Hankel papers (`bacorasisito.pdf`, Xin `arXiv:0712.0933`); no proof of Mathar's recurrence found.

## Near-Misses & Coverage Limits
- **Near-misses:** `A157003` links `arXiv:1410.2847`, `arXiv:2306.05025`, Baril et al. `bacorasisito.pdf`, and Xin `arXiv:0712.0933`, plus Kotesovec's 4-term recurrence comment (all checked in Gate 1; none prove Mathar's recurrence).
- **Coverage limits:** Private repositories and works without `A157003` identifier strings are not covered.

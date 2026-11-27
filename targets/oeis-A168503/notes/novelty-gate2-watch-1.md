# Gate 2 Novelty Receipt — `targets/oeis-A168503/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:35Z`
- **Target:** OEIS `A168503` (`rev. 20`, `2025-02-07`), R. J. Mathar's Feb 10 2015 conjectured 4-term recurrence `(n+1)*a(n) + (-13*n+5)*a(n-1) + 6*(8*n-13)*a(n-2) + 12*(-5*n+13)*a(n-3) + 12*(2*n-7)*a(n-4) = 0`.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A168503"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` hits.
   - Zenodo `10.5281/zenodo.24366920` (`46` OEIS IDs) & `10.5281/zenodo.23760779` (`12` OEIS IDs) -> `0` hits.
3. **Live OEIS JSON (`11:35Z`):**
   - `https://oeis.org/search?q=id:A168503&fmt=json` -> `rev. 20` (`2025-02-07T00:50:52-05:00`), unchanged, Mathar's recurrence still marked `Conjecture:`.
4. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A168503"'` -> `0`; Zenodo `q=A168503` -> `0`; `gh search issues '"A168503"'` -> `1` unrelated `rism-digital/muscat#1151`; `gh search prs` -> `0`; `search_web` -> no prior proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Private repositories and works without `A168503` identifiers are not covered.

# Gate 2 Novelty Receipt — `targets/oeis-A165204/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:29Z`
- **Target:** OEIS `A165204` (`rev. 15`, `2018-02-15`), Colin Barker's Feb 10 2018 conjectured generating function `(1 - 8*x + 2*x^2 - x^3) / (1 - 3*x + 8*x^2 - 3*x^3 + x^4)` and 4-term recurrence `a(n) = 3*a(n-1) - 8*a(n-2) + 3*a(n-3) - a(n-4)` (`n > 3`) for the Hankel transform of `A165203`.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`653` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A165204" "A165203"` -> `0` lines across `0/653` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86` `2026-11-19`) -> `0` matches for `A165204` or `A165203`.
   - Zenodo `10.5281/zenodo.24366920` (Lien-Hung Su, `2026-11-20`) & Zenodo `10.5281/zenodo.23760779` (`2026-10-29`) -> `0` matches for `A165204` or `A165203`.
3. **Live OEIS JSON:**
   - `https://oeis.org/search?q=id:A165204&fmt=json` -> `rev. 15` (`2018-02-15T20:46:11-05:00`), still marked `Conjectures from _Colin Barker_, Feb 10 2018:`.
4. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:"A165204"'` -> `total_results: 0`.
   - `curl -s "https://zenodo.org/api/records?q=A165204&size=5"` -> `0` hits.
5. **Live GitHub Issues/PRs & Web Search:**
   - `gh search issues '"A165204"'` -> `0` hits; `gh search prs '"A165204"'` -> `1` unrelated CI PR (`AgentEnder/cli-forge#58`).
   - `search_web` (`"A165204" "Colin Barker" OR "Hankel transform of A165203"`) -> no prior proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Private repositories and papers published after this UTC timestamp without OEIS identifier strings are not covered.

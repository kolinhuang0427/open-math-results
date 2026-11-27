# Gate 3 Novelty Receipt — `targets/dangeli-2607.17335-conj1/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:32Z`
- **Target:** Daniele D'Angeli & Emanuele Rodaro, `arXiv:2607.17335v1` (*On totally synchronizing graphs*, Section 4, Conjecture 4.6 `\label{conj:typical-total-simplicity}` — Typical Total Simplicity of Random $k$-Out Digraphs).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2607.17335" "typical-total-simplicity"` -> `1` line across `1/658` files: only `AlexenderSokolov/cross-theory-formal-database` license path (`editable-corpus/licenses/arxiv-2607.17335-CC-BY-4.0.txt`), zero solutions/counterexamples.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`) -> `0` hits for `2607.17335`.
3. **Live arXiv API:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2607.17335` -> `total_results: 1`, `2607.17335v1` (`2026-07-19T16:51:23Z`) remains the sole version.
4. **Live Zenodo API:**
   - `curl -s "https://zenodo.org/api/records?q=2607.17335&size=5"` -> `0` hits.
5. **Live GitHub Issues/PRs & Web Search:**
   - `gh search issues '"2607.17335"'` & `gh search prs '"2607.17335"'` -> `0` hits each.
   - `search_web` (`"2607.17335" OR "typical-total-simplicity" OR "totally simple" "SCC_n" D'Angeli`) -> returns only the original preprint `arXiv:2607.17335`; no refutation or proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** `AlexenderSokolov/cross-theory-formal-database` mirrors CC-BY-4.0 arXiv paper licenses only.
- **Coverage limits:** Private repositories and works posted after this UTC timestamp without `2607.17335` or `typical-total-simplicity` identifiers are not covered.

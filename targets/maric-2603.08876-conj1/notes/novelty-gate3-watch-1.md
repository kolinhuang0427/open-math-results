# Gate 3 Novelty Receipt — `targets/maric-2603.08876-conj1/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:41Z`
- **Target:** Nevena Marić, `arXiv:2603.08876v1` (`2026-03-09`), Section 5 **Conjecture 5.1** (`\label{conj:global}` — Global Optimality of $k$-isolated cuts for $n \ge 7$).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2603.08876" "conj:global"` -> `4` lines across `3/658` files: only `watch/snapshots/arxiv/citing_papers.{json,md}` (`OpenAlex cited_by=0; S2=0`) and unrelated `molinzhao27__conjectures.json` (`conj:global_identifiability`).
2. **Live arXiv & Zenodo APIs:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2603.08876` -> `total_results: 1`, `2603.08876v1` (`2026-03-09T19:41:42Z`) sole version.
   - `curl -s "https://zenodo.org/api/records?q=2603.08876&size=3"` -> `0` hits.
3. **Live GitHub & Web Search:**
   - `gh search issues '"2603.08876"'` & `gh search prs '"2603.08876"'` -> `0` hits.
   - `search_web` (`"2603.08876" "Marić" OR "Conjecture 5.1" OR "conj:global" proof`) -> confirms `arXiv:2603.08876v1` only; global proof for $n \ge 7$ remains open.

## Near-Misses & Coverage Limits
- **Near-misses:** `arXiv:2603.08876v1` itself (proves optimality within the isolated-cut family only).
- **Coverage limits:** Private repositories and works without `2603.08876` or `conj:global` identifiers are not covered.

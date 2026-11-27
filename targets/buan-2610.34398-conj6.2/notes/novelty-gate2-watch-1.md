# Gate 2 Novelty Receipt — `targets/buan-2610.34398-conj6.2/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:34Z`
- **Target:** Aslak B. Buan, Eric J. Hanson, Bethany R. Marsh (`arXiv:2610.34398v1`, `2026-10-25`), Section 7.1 **Conjecture 7.2** (`\label{conj:TFordered}`, tracked under directory slug `buan-2610.34398-conj6.2`).
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2610.34398" "conj:TFordered"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` matches.
3. **Live arXiv API:**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2610.34398` -> `total_results: 1`, `2610.34398v1` (`2026-10-25T15:59:39Z`) remains the sole version.
4. **Live Zenodo, GitHub, & Web Search:**
   - `curl -s "https://zenodo.org/api/records?q=2610.34398&size=3"` -> `0` hits.
   - `gh search issues '"2610.34398"'` & `gh search prs '"2610.34398"'` -> `0` hits each.
   - `search_web` (`"2610.34398" OR "TF-ordered" "Buan" "Hanson" "Marsh" OR "conj:TFordered"`) -> returns only `arXiv:2610.34398v1` and background literature on TF-ordering; no resolution of Conjecture 7.2 found.

## Near-Misses & Coverage Limits
- **Near-misses:** `arXiv:2610.34398v1` itself (poses Conjecture 7.2 in Section 7.1).
- **Coverage limits:** Private repositories and preprints without `2610.34398` or `conj:TFordered` identifiers are not covered.

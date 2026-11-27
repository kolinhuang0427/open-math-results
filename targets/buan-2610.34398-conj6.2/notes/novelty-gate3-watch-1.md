# Gate 3 Novelty Receipt — `targets/buan-2610.34398-conj6.2/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:52Z`
- **Target:** Aslak B. Buan, Eric J. Hanson, & Bethany R. Marsh (`arXiv:2610.34398v1`, `2026-10-25`), Section 7.1 **Conjecture 7.2** (`\label{conj:TFordered}`, tracked under directory slug `buan-2610.34398-conj6.2`).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`689` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 29, Zenodo `24366920`/`23760779`, 2026 compendia, `insorrowmeow/oeis-sequence-proofs`, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "2610.34398" "conj:TFordered"` (`11:52Z`) -> `0` lines across `0/689` files.
2. **Live arXiv & Zenodo APIs (`11:52Z`):**
   - `.venv/bin/python tools/arxiv_fetch.py query --id-list 2610.34398` -> `total_results: 1`, `2610.34398v1` (`2026-10-25T15:59:39Z`) sole version.
   - `curl -s "https://zenodo.org/api/records?q=2610.34398&size=3"` -> `0` hits.
3. **Live GitHub & Web Search (`11:34Z`–`11:52Z`):**
   - `gh search issues '"2610.34398"'` & `gh search prs '"2610.34398"'` -> `0` hits each.
   - `search_web` -> returns only `arXiv:2610.34398v1` and background literature on TF-ordering; no proof of Conjecture 7.2 found.

## Near-Misses & Coverage Limits
- **Near-misses:** `arXiv:2610.34398v1` itself (poses Conjecture 7.2 in Section 7.1).
- **Coverage limits:** Private repositories and works without `2610.34398` or `conj:TFordered` identifiers are not covered.

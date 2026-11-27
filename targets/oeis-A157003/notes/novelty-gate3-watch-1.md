# Gate 3 Novelty Receipt — `targets/oeis-A157003/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:41Z`
- **Target:** OEIS `A157003` (`rev. 37`, `2025-11-05`), R. J. Mathar's Nov 19 2014 6-term recurrence conjecture.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A157003"` -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:41Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A157/A157003.seq` -> `%I A157003 #37 Nov 05 2025 15:22:17`, Mathar's Nov 19 2014 recurrence still marked `Conjecture:`.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A157003"'` -> `0`; Zenodo `q=A157003` -> `0`; `gh search issues`/`prs` -> `0`; `search_web` -> `0` proofs of Mathar's recurrence.

## Near-Misses & Coverage Limits
- **Near-misses:** `A157003` linked papers (`arXiv:1410.2847`, `arXiv:2306.05025`, Baril et al., Xin `arXiv:0712.0933`) and Kotesovec's 4-term recurrence comment (checked; none prove Mathar's recurrence).
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A157003` identifiers are not covered.

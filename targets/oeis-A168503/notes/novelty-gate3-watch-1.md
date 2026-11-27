# Gate 3 Novelty Receipt — `targets/oeis-A168503/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:41Z`
- **Target:** OEIS `A168503` (`rev. 20`, `2025-02-07`), R. J. Mathar's Feb 10 2015 4-term recurrence conjecture.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A168503"` -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:41Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A168/A168503.seq` -> `%I A168503 #20 Feb 07 2025 00:50:52`, Mathar's Feb 10 2015 recurrence still marked `Conjecture:`.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A168503"'` -> `0`; Zenodo `q=A168503` -> `0`; `gh search issues` -> only unrelated `rism-digital/muscat#1151`; `gh search prs` -> `0`; `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A168503` identifiers are not covered.

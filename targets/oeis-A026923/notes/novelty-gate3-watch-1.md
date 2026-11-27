# Gate 3 Novelty Receipt — `targets/oeis-A026923/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:45Z`
- **Target:** OEIS `A026923` (`rev. 27`, `2026-02-27`), Colin Barker's Sep 01 2019 rational g.f. and 11-term recurrence conjecture.
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A026923" "A026927"` (`11:45Z`) -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:45Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A026/A026923.seq` -> `%I A026923 #27 Feb 27 2026 15:18:34`, Barker's Sep 01 2019 formulas remain open (`Conjectures from _Colin Barker_`).
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A026923" OR all:"A026927"'` (`11:45Z`) -> `0`; Zenodo `q=A026923` -> only unrelated biology `6081413` (*Afrobethylus swazi Ramos & Azevedo, sp. nov.*); `gh search issues`/`prs` -> `0`; `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** `A026923(n) + A026927(n) = A069905(n)` (R. J. Mathar, Aug 22 2019).
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A026923` identifiers are not covered.

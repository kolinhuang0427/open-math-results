# Gate 2 Novelty Receipt — `targets/oeis-A026927/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:40Z`
- **Target:** OEIS `A026927` (`rev. 23`, `2026-02-27`), Colin Barker's Sep 01 2019 conjectured g.f. `x^4*(1 + x^2 - x^3 + x^4) / ((1 - x)^3*(1 + x)^2*(1 - x + x^2)*(1 + x^2)*(1 + x + x^2))` and 11-term recurrence.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A026923" "A026927"` -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:40Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A026/A026927.seq` -> `%I A026927 #23 Feb 27 2026 15:22:32`, `Conjectures from _Colin Barker_, Sep 01 2019:` still open.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A026927"'` -> `0`; Zenodo `q=A026927` -> `0`.
   - `gh search issues '"A026927"'` & `gh search prs '"A026927"'` -> `0`.
   - `search_web` (`"A026923" OR "A026927" "Colin Barker" OR recurrence OR proof`) -> no proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** `A026927(n) + A026923(n) = A069905(n)` (R. J. Mathar, Aug 22 2019).
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A026927` identifiers are not covered.

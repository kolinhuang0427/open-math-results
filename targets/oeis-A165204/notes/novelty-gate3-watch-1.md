# Gate 3 Novelty Receipt — `targets/oeis-A165204/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:43Z`
- **Target:** OEIS `A165204` (`rev. 15`, `2018-02-15`) / `A165203` (`rev. 28`), Colin Barker's Feb 10 2018 conjectured g.f. `(1 - 8*x + 2*x^2 - x^3) / (1 - 3*x + 8*x^2 - 3*x^3 + x^4)` and 4-term recurrence (`n > 3`).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A165204" "A165203"` -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:43Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A165/A165204.seq` -> `%I A165204 #15 Feb 15 2018 20:46:11`, Barker's Feb 10 2018 formulas remain marked `Conjectures from _Colin Barker_`.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A165204"'` -> `0`; Zenodo `q=A165204` -> `0`; `gh search issues` -> `0`; `gh search prs` -> `1` unrelated CI PR (`AgentEnder/cli-forge#58`); `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A165204` identifiers are not covered.

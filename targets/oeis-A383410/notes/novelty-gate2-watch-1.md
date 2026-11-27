# Gate 2 Novelty Receipt — `targets/oeis-A383410/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:44Z`
- **Target:** OEIS `A383410` (`rev. 6`, `2025-05-03`) / `A005649` (`rev. 123`), Mikhail Kurkov's Apr 26 2025 conjecture `A(n,0) = A005649(n)`.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A383410"` -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:44Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A383/A383410.seq` -> `%I A383410 #6 May 03 2025 19:02:22`, `Conjecture: A(n,0) = A005649(n).` open.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A383410"'` -> `0`; Zenodo `q=A383410` -> `0`; `gh search issues '"A383410"'` -> `0`; `gh search prs '"A383410"'` -> `1` unrelated `dnbexperience/eufemia#10491`; `search_web` -> no prior proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A383410` identifiers are not covered.

# Gate 2 Novelty Receipt — `targets/oeis-A379459/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:41Z`
- **Target:** OEIS `A379459` (`rev. 4`) / `A379460` (`rev. 4`) / `A006351` (`rev. 195`), Mikhail Kurkov's Dec 23 2024 / Jan 16 2025 conjectures `A379459(n,0) = A006351(n+2)` and `A379460(n,0) = A006351(n+1)`.
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A379459" "A379460"` -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:41Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A379/A379459.seq` -> `%I A379459 #4 Jan 03 2025 02:03:22`, `Conjecture: A(n,0) = A006351(n+2).` open.
   - `gh api repos/oeis/oeisdata/contents/seq/A379/A379460.seq` -> `%I A379460 #4 Jan 03 2025 02:03:31`, `Conjecture: A(n,0) = A006351(n+1).` open.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A379459" OR all:"A379460"'` -> `0`; Zenodo `q=A379459` & `q=A379460` -> `0` hits each.
   - `gh search issues '"A379459"'` / `'"A379460"'` -> `the-omega-institute/trureturing#27785` (open preregistration, no proof); `gh search prs` -> `0`.
   - `search_web` -> returns only OEIS pages; no prior proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** `the-omega-institute/trureturing#27785` (open preregistration issue with no proof).
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A379459`/`A379460` identifiers are not covered.

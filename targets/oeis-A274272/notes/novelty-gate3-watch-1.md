# Gate 3 Novelty Receipt — `targets/oeis-A274272/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:40Z`
- **Target:** OEIS `A274272` (`rev. 12`, `2016-06-23`), Colin Barker's Jun 17 2016 conjectures (`a(n) = (57+8*(-1)^n+63*5^n+3*5^(1+2*n)+125^n)/144`, order-5 recurrence for $n > 4$, and rational g.f.).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A274272"` -> `0` lines across `0/658` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:40Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A274/A274272.seq` -> `%I A274272 #12 Jun 23 2016 10:05:23`, `Conjectures (Start)` unchanged/open.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A274272"'` -> `0`; Zenodo `q=A274272` -> `0`; `gh search issues '"A274272"'` -> `0`; `gh search prs '"A274272"'` -> `1` unrelated PR (`DoctorCRE/doctorcre-app#568`); `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** General $p(m, \le 4)$ quasipolynomial formulas do not prove Barker's $5^n$ specialization, order-5 recurrence, and rational g.f.
- **Coverage limits:** Direct `oeis.org` queries hit a temporary IP rate-limit at `11:36Z` (mitigated via official `oeis/oeisdata` mirror `seq/A274/A274272.seq` `#12`). Private repositories and works without `A274272` identifiers are not covered.

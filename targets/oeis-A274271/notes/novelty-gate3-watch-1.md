# Gate 3 Novelty Receipt — `targets/oeis-A274271/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:49Z`
- **Target:** OEIS `A274271` (`rev. 12`, `2016-06-21`), Colin Barker's Jun 17 2016 conjectures (`a(n) = ((3+3^n)^2*(9+3^n))/144` for $n > 1$, order-4 recurrence for $n > 4$, and rational g.f.).
- **Verdict:** **PASS** (`0` competing solutions found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`689` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures`, Zenodo `24366920`/`23760779`, 2026 compendia, & `mylesparslow` ledger):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A274271"` (`11:49Z`) -> `0` lines across `0/689` files.
2. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:49Z`):**
   - `gh api repos/oeis/oeisdata/contents/seq/A274/A274271.seq` -> `%I A274271 #12 Jun 21 2016 09:29:05`, `Conjectures (Start)` still open.
3. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A274271"'` (`11:49Z`) -> `0`; Zenodo `q=A274271` (`11:49Z`) -> `0`; `gh search issues`/`prs` -> `0`; `search_web` -> `0` proofs.

## Near-Misses & Coverage Limits
- **Near-misses:** General $p(m, \le 4)$ quasipolynomial formulas do not prove Barker's $3^n$ specialization, order-4 recurrence, and rational g.f.
- **Coverage limits:** Direct `oeis.org` queries avoided due to `11:36Z` temporary IP rate-limit (official `oeis/oeisdata` mirror checked instead). Private repos and works without `A274271` identifiers are not covered.

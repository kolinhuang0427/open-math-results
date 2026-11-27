# Gate 2 Novelty Receipt — `targets/oeis-A274272/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:36Z`
- **Target:** OEIS `A274272` (`rev. 12`), Colin Barker's Jun 17 2016 conjectures (`a(n) = (57+8*(-1)^n+63*5^n+3*5^(1+2*n)+125^n)/144`, order-5 recurrence for $n > 4$, and rational g.f.).
- **Verdict:** **PASS** (`0` prior proofs found; note live `oeis.org` rate-limit below)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A274272"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` hits.
   - Zenodo `10.5281/zenodo.24366920` & `10.5281/zenodo.23760779` -> `0` hits.
3. **Official OEIS Mirror (`github.com/oeis/oeisdata`, `11:37Z`) & Live APIs:**
   - `gh api repos/oeis/oeisdata/contents/seq/A274/A274272.seq` -> `%I A274272 #12 Jun 23 2016 10:05:23`, `Conjectures (Start)` still open.
   - `arxiv_fetch.py query 'all:"A274272"'` -> `0`; Zenodo `q=A274272` -> `0`.
   - `gh search issues '"A274272"'` -> `0`; `gh search prs '"A274272"'` -> `1` unrelated PR (`DoctorCRE/doctorcre-app#568`).
   - `search_web` (`"A274272" "Colin Barker" OR recurrence OR proof`) -> only OEIS `A274272`; no proof found.

## Near-Misses & Coverage Limits
- **Near-misses:** None.
- **Coverage limits:** Direct `https://oeis.org/search?q=id:A274272` hit a temporary IP rate-limit at `11:36Z`–`11:37Z` (mitigated via official `oeis/oeisdata` mirror `seq/A274/A274272.seq` `#12`). Private repositories and works without `A274272` identifiers are not covered.

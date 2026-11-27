# Gate 2 Novelty Receipt — `targets/oeis-A274271/`

- **Checked by:** `watch-1`
- **UTC Time:** `2026-11-27T11:35Z`
- **Target:** OEIS `A274271` (`rev. 12`, `2016-06-21`), Colin Barker's Jun 17 2016 conjectures (`a(n) = ((3+3^n)^2*(9+3^n))/144` for $n > 1$, order-4 recurrence for $n > 4$, and rational g.f.).
- **Verdict:** **PASS** (`0` prior proofs found)

## Exact Queries & Results
1. **Local Snapshot Sweep (`658` files under `watch/snapshots/**`, incl. `1337isnot1337/solved-conjectures` Sweep 28):**
   - `.venv/bin/python tools/novelty_grep.py --root watch/snapshots "A274271"` -> `0` lines across `0/658` files.
2. **External Compendia Cross-Check:**
   - `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`, PR `#86`) -> `0` hits.
   - Zenodo `10.5281/zenodo.24366920` & `10.5281/zenodo.23760779` -> `0` hits.
3. **Live OEIS JSON (`11:35Z`):**
   - `https://oeis.org/search?q=id:A274271&fmt=json` -> `rev. 12` (`2016-06-21T09:29:05-04:00`), unchanged, conjectures still open.
4. **Live arXiv, Zenodo, GitHub, & Web:**
   - `arxiv_fetch.py query 'all:"A274271"'` -> `0`; Zenodo `q=A274271` -> `0`; `gh search issues`/`prs` -> `0`; `search_web` -> only OEIS `A274271` itself; no published proof of Barker's $3^n$ formulas found.

## Near-Misses & Coverage Limits
- **Near-misses:** General quasipolynomial formulas for partitions into at most 4 parts $p(m, \le 4)$ do not prove Barker's explicit $3^n$ polynomial, recurrence, and rational g.f.
- **Coverage limits:** Private repositories and works without `A274271` identifiers are not covered.

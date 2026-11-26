# Gate 3 Novelty Receipt — `ferrero-2511.16335-conj1.8`

- **UTC Time:** 2026-11-26T20:20:58Z
- **Reviewer:** `watch-1`
- **Verdict:** **PASS**

## Live Pre-Report Re-Checks Performed

1. **Local watch snapshots (`watch/`):**
   - `.venv/bin/python tools/novelty_grep.py 2511.16335 "standard fast join" "fixed propagation time" PTbar` -> only `watch/snapshots/formal/last_sweep.json` entries for sibling `ferrero-2511.16335-conj1.7` (no external matches).
2. **Live `1337isnot1337/solved-conjectures` (`gh api`, read-only):**
   - `commits/main` (`2dfd2a211b`, `2026-11-26T20:03:29Z`, PR #902) and `issues?state=all&since=2026-11-26T20:00:00Z` -> 7 updated issues/PRs (`#902`, `#901`, `#900`, `#897`, `#870`, `#480`, `#352`), none related to `2511.16335` or zero forcing.
3. **Live GitHub global & `trureturing` searches (`gh api`, read-only):**
   - `search/code?q="2511.16335"+OR+"standard+fast+join"` -> 0 hits.
   - `search/issues?q=repo:the-omega-institute/trureturing+2511.16335+OR+"standard+fast+join"` -> only `#8371` (closed unresolved `2026-09-16`).
4. **Live web search (`search_web`):**
   - `"2511.16335" OR "standard fast join" "C_6[2K_1]" OR "Circ(12" OR "counterexample" "Ferrero"` -> only the primary paper (`arXiv:2511.16335` / *Australasian J. Combin.*).

## Near Misses

- Same as Gate 2 (`novelty-gate2-watch-1.md`): `trureturing#8371` closed unresolved; `1337#323` is Boyer–Brimkov–English–Ferrero et al. (2019); `arXiv:2609.35522v1` studies discrepancy of *minimum* zero forcing sets.

## What Was Not Covered

- OpenAlex/arXiv live re-query (covered by `@watch-5`), closed-access papers, and private repositories.

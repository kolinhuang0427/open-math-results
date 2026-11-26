# Gate 2 Novelty Receipt — `oeis-A100691`

- **Verdict:** **PASS** (no prior proof of `a_OEIS(n) = A193641(n+2)-3` or `s(5)=160` SAW counterexample found)
- **Checked at (UTC):** 2026-11-26T20:20:58Z
- **Watcher:** `watch-6`

## Sources Checked

1. All local `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py A100691 A193641`.
2. Live OEIS JSON API (`https://oeis.org/search?q=id:A100691&fmt=json` rev 11; `id:A193641` rev 48).
3. Live GitHub search (`gh search repos`, `gh search issues`).
4. Live arXiv API via `.venv/bin/python tools/arxiv_fetch.py query 'all:"A100691" OR all:"A193641"'`.
5. Web search (`search_web`).

## Exact Queries

- `.venv/bin/python tools/novelty_grep.py A100691 A193641 ...`
- `https://oeis.org/search?q=id:A100691&fmt=json` and `id:A193641`
- `gh search repos "A100691 OR A193641"`
- `gh search issues "\"A100691\" OR \"A193641\""`
- `.venv/bin/python tools/arxiv_fetch.py query 'all:"A100691" OR all:"A193641"' --max-results 10`
- `search_web`: `"self-avoiding paths" "triangular lattice" "Z x {0,1}" OR "A100691" "158" OR "160"`

## Near Misses & Findings

- Live OEIS `A100691` (revision 11, `2022-07-22`) still lists `Conjecture: a(n) = A193641(n+2)-3, n>0 - _R. J. Mathar_, Jul 22 2022` with no recorded proof or erratum for `s(5) = 160` vs `158`.
- Live OEIS `A193641` (revision 48, `2026-09-16`) still lists `Empirical: a(n) = 2*a(n-1) + a(n-3)` with no recorded proof of the `-1..1` array recurrence.
- `mathesis-papers/*` and `joaquimmj/oeis-conjectures` contain other Mathar conjectures (`A084261`, `A081124`, `A027182`, `A379464`, `A386829`, `A174193`, `A000159`, `A036766`, etc.), none touching `A100691` or `A193641`.
- Zero matches in `watch/snapshots/**`, GitHub repos/issues, arXiv, or web search.

## What Was Not Covered

- Print-only/non-digitized literature (e.g., J. Labelle 1996 *Bull. ICA* 17, 47–61) and private repositories.

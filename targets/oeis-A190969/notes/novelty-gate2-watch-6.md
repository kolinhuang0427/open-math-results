# Gate 2 Novelty Receipt (`watch-6`) — `targets/oeis-A190969/`

- **Checked UTC:** `2026-11-27T08:56:00Z`
- **Verdict:** **PASS** (open; no full proof or counterexample found)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 601 files including 430 `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "A190969" "190969" "4096"` -> `A190969` / `190969` matched only `FormalConjectures/OEIS/190969.lean` (`formal/`), `epoch-research/LeanOpenProblems-results` (`discovered/`), and unrelated `trureturing` SHA256/issue IDs; `"4096"` hits were unrelated powers of 2.
2. **Live GitHub search (`gh search`):**
   - `gh search repos "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 repos).
   - `gh search issues "2411.00721 OR A190969 OR 2605.25743 OR 2107.14284 OR A350963 OR A286044"` -> `[]` (0 issues/PRs).
3. **Live OEIS JSON (`oeis.org/search?q=id:A190969&fmt=json`):**
   - Revision `48` (`2025-11-05T15:22:20-05:00`) unchanged; Zhi-Wei Sun's mod $p^2$ and mod $p^3$ supercongruences remain marked `conjectured`.
4. **Web search (`search_web`):**
   - Query: `"A190969" "5*a(n-1)-8*a(n-2)" OR "a(4k)*binomial(2k,k)^3" OR "4096" supercongruence` -> returns only OEIS `A190969` and unrelated $\sum \binom{2k}{k}^3 / 4096^k$ supercongruences without the $a(4k)$ recurrence factor.

## Near Misses
- **`epoch-research/LeanOpenProblems-results`:** Contains failed benchmark runs for `oeis_a190969` using `sorryAx` (`watch-1` `#40` confirmed SafeVerify failure); not a valid proof.
- **`FormalConjectures/OEIS/190969.lean`:** Statement formalization only (`category research open`).

## Coverage Limits
- Live `gh search code` returned `HTTP 429` (shared rate limit); code coverage rests on `watch/snapshots/**` (601 files, 430 `discovered/` repo snapshots) plus live `gh search repos`/`issues`, live OEIS, and `search_web`.

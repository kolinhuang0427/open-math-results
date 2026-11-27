# Gate 2 Novelty Receipt (`watch-6`) — `targets/garrison-2401.09497-conj5.2/`

- **Checked UTC:** `2026-11-27T09:13:00Z`
- **Verdict:** **PASS** (full all-$k$ statement open; competing efforts settle $k \le 16$ / prime-power $k$ only)

## Sources & Exact Queries Checked
1. **Local snapshots (`tools/novelty_grep.py` across 607 files including newly snapshotted `ndesmo/leaning` and 435+ `discovered/` repo snapshots):**
   - Query: `.venv/bin/python tools/novelty_grep.py "2508.04602" "2401.09497" "weakly consecutive"` -> `2401.09497` matched only `AlexenderSokolov/cross-theory-formal-database` license metadata; `rainwangphy/aftd-platform` covers prime-power $k$ only.
2. **Live GitHub search (`gh search` & `gh api` on `ndesmo/leaning`):**
   - `gh search repos "2401.09497"` -> `[]`.
   - `gh search issues "2401.09497"` -> `ndesmo/leaning#21` (`open`), `ndesmo/leaning#46` (`closed`, setup).
   - Inspected `ndesmo/leaning` issues (`#21`, `#47`/PR `#57` Lean $k \le 16$, `#48`/PR `#61` prime-power $k$, `#68` `open` attack on $k = p^a q^b$) and open PRs (`pulls?state=open` -> `[]`): no general-$k$ proof or PR landed.
3. **arXiv & Zenodo API:**
   - `tools/arxiv_fetch.py query --id-list 2508.04602,2401.09497`: `2401.09497v1` (`2024-01-17`) remains sole version.
   - `zenodo.org/api/records?q=2401.09497&size=3`: `0` hits.
4. **Web search (`search_web`):**
   - Query: `"2401.09497" OR "Weakly Consecutive Sequences" "Garrison" "Seiler" proof OR counterexample` -> returns only `arXiv:2401.09497v1`.

## Near Misses
- `rainwangphy/aftd-platform`: proves Conjecture 5.2 for `IsPrimePow k` only.
- `ndesmo/leaning`: proves $k \le 16$ in Lean (PR `#57`) and prime-power $k$ in notes (PR `#61`); issue `#68` (two prime factors $k = p^a q^b$) is `open` with no open PRs; general $k \ge 1$ remains unsettled.

## Coverage Limits
- Live `gh search code` skipped due to shared HTTP 429 rate-limit pressure; code coverage rests on `watch/snapshots/**` (607+ files, 435+ `discovered/` repo snapshots including `ndesmo/leaning`) plus live `gh search repos`/`issues`, `gh api`, arXiv, Zenodo, and `search_web`.

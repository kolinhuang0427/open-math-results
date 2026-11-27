# Gate 2 Novelty Receipt (`watch-1`) — `targets/garrison-2401.09497-conj5.2/`

- **Checked UTC:** `2026-11-27T09:12Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`; actively raced on composite $k$ in `ndesmo/leaning#68`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 607 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2401.09497`, `"Garrison"`, `"A395372"`.
   - `.venv/bin/python tools/novelty_grep.py 2401.09497 "Garrison" "A395372"` -> `2` hits across `2/607` files (`techno-optimist/erdos-frontier-atlas` unrelated Erdős #962 `T. Garrison`, and `AlexenderSokolov` license file `arxiv-2401.09497-CC-BY-4.0.txt`). (Plus `rainwangphy/aftd-platform` proving `IsPrimePow k` only, verified in `notes/novelty-garrison-lit.md`.)
2. **Live GitHub (`gh api` + `gh search issues`), OEIS, and Zenodo (`2026-11-27T09:11Z`):**
   - `ndesmo/leaning`: checked live via `gh api`: PR #57 (Lean $k \le 16$), PR #61 (prime-power $k$ notes, `gap: composite k`), latest merged PR #67 (`2026-11-26T17:34Z`, unrelated `A402341`), and open issue `#68` (`2026-11-26T23:52Z`, *"P1 unit: attack Conjecture 5.2 for k with two distinct prime factors"*, unmerged). General $k$ remains **OPEN** on `ndesmo/leaning` `main`.
   - `gh search issues "2401.09497"` -> only `ndesmo/leaning#21` and `#46` (closed literature setup).
   - `https://oeis.org/search?q=id:A395372&fmt=json` -> rev `5` (`2026-04-22`), no general proof.
   - `https://zenodo.org/api/records?q=2401.09497&size=3` -> `total: 0`.

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); unpushed local work on `ndesmo/leaning#68`, closed-access venues, and private repositories not covered.

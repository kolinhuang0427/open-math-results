# Gate 3 Novelty Receipt (`watch-5`) — `targets/oeis-A092920/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md` in `targets/oeis-A092920/`)
- **Target Scope:** OEIS `A092920` (rev `56`, `2026-03-14T12:38:00-04:00`), Mikhail Kurkov's Apr 24 2023 conjecture $a(n) = \sum_{k=0}^{2^{n-1}-1} b(k)$ for strongly monotone partitions of $[n]$.

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py A092920 'strongly monotone partitions' Kurkov --max-per-file 3 --max-total 15`: `15` lines across `7/368` files (all hits are `Kurkov` on unrelated sequences `A006068`, `A263634`, `A340991`, `A385886`, `A385818`, binary Stirling / Gray code; `0` hits on `A092920` or strongly monotone partitions).
2. **arXiv 7-category snapshot (`watch/snapshots/arxiv/arxiv_submissions.json`, 1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - Sweep 1 (`math.CO`, `math.NT`, `cs.DM`, `math.GR`, `math.AC`, `math.RA`, `math.RT` + `lastUpdatedDate`): `0` matches to `oeis-A092920`.
   - Live query `all:A092920 OR all:A394511 OR all:A190969 OR all:A091524`: `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A092920&fmt=json`):**
   - Revision `56`, timestamp `2026-03-14T12:38:00-04:00` (unchanged; formula remains marked `Conjecture:`).
4. **Web search (`search_web`):**
   - `"A092920" "Kurkov" OR "strongly monotone partitions"`: `0` prior proofs or refutations found.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, web search, or `watch/snapshots/**`.

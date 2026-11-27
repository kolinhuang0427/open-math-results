# Gate 2 Novelty Receipt (`watch-5`) — `targets/oeis-A190969/`

- **Checked UTC:** `2026-11-27T08:48Z` – `2026-11-27T08:52Z`
- **Verdict:** **PASS** (no `CONTESTED.md`)
- **Target Scope:** OEIS `A190969` (rev `48`, `2025-11-05`) & `FormalConjectures/OEIS/190969.lean`: Zhi-Wei Sun supercongruences for $a(n) = 5a(n-1) - 8a(n-2)$, $S(p) \equiv 0 \pmod{p^2}$ (odd prime $p$) and $\pmod{p^3}$ ($p \equiv 1,2,4 \pmod 7$).

## Sources & Exact Queries Checked

1. **Local novelty snapshots (`watch/snapshots/**`, rebuilt 2026-11-27T08:41Z–08:47Z):**
   - `.venv/bin/python tools/novelty_grep.py A190969 190969 '5*a(n-1)' --max-per-file 3 --max-total 15`: `8` lines across `4/587` files (`formal-conjectures-files.tsv`, `BoltonBailey/formal-conjectures-ai-review`, `epoch-research/LeanOpenProblems`, `epoch-research/LeanOpenProblems-results`).
   - **Direct verification of `epoch-research/LeanOpenProblems-results` (`gh api`):** Inspected `runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_a190969_conjecture_0/scores.json` -> SafeVerify failed (`"failureMode": "axioms"`, `"Disallowed axioms used: #[sorryAx]"`). Not solved.
2. **arXiv 7-category snapshot (1,000 entries) & live arXiv API (`tools/arxiv_fetch.py`):**
   - `all:A092920 OR all:A394511 OR all:A190969 OR all:A091524`: `total: 0`.
3. **Live OEIS JSON (`https://oeis.org/search?q=id:A190969&fmt=json`):**
   - Revision `48`, timestamp `2025-11-05T15:22:20-05:00` (unchanged; conjectures remain open).
4. **Web search (`search_web`):**
   - `"A190969" "5*a(n-1)"`: returns only OEIS `A190969`, no proof found.

## What Was Not Covered
- Closed-access venues or private repositories not indexed by OEIS, arXiv, web search, or `watch/snapshots/**`.

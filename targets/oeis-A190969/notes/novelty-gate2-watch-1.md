# Gate 2 Novelty Receipt (`watch-1`) — `targets/oeis-A190969/`

- **Checked UTC:** `2026-11-27T08:50Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 587 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 22 (`2026-11-27T08:41:11Z`): `0` hits for `A190969`, `190969`.
   - `.venv/bin/python tools/novelty_grep.py A190969 190969`:
     - `formal/formal-conjectures-files.tsv`: `FormalConjectures/OEIS/190969.lean` (open conjecture statement).
     - **Near misses checked live via `gh api`:**
       - `BoltonBailey/formal-conjectures-ai-review` (`OeisA190969-conjecture_1.json`, `conjecture_2.json`): statement-fidelity audit only (no proof).
       - `epoch-research/LeanOpenProblems` (`oeis_a190969_conjecture_0.lean`) & `epoch-research/LeanOpenProblems-results` (`ant-j0j0g4uzligm1k41` and `gdm-1s7vwp2si1ap0r6d` `scores.json`): both runs scored `"I"` (SafeVerify failed: `oeis_a190969_conjecture_0` uses disallowed axiom `sorryAx`).
2. **Live OEIS & GitHub (`2026-11-27T08:48Z`):**
   - `https://oeis.org/search?q=id:A190969&fmt=json` -> revision `48` (`2025-11-05T15:22:20-05:00`), Zhi-Wei Sun's Mar 13 2013 conjectures unchanged.
   - `gh search issues "A190969"` -> `0` issues.

## Coverage Limits
- Closed-access venues and private repositories.

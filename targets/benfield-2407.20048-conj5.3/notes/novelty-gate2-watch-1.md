# Gate 2 Novelty Receipt (`watch-1`) — `targets/benfield-2407.20048-conj5.3/`

- **Checked UTC:** `2026-11-27T09:04Z`
- **Reviewer:** `watch-1`
- **Verdict:** **FAIL / CONTESTED (Partial: Clause (v) Settled)** (`CONTESTED.md` written)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 604 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `2407.20048`.
   - `.venv/bin/python tools/novelty_grep.py 2407.20048 "Benfield"` -> hits only on `arXiv:2404.08193v2` (Waring-gap conjectures, unrelated).
2. **Live GitHub Issues & `gh api` (`2026-11-27T09:03Z`):**
   - `gh search issues "2407.20048"` -> **HIT:** `the-omega-institute/trureturing#9448` (`closed`, `2026-09-22`, PR #9451 merged): *"prereg: arXiv:2407.20048 Conjecture 5.3(v) — the Pisano order is not confined to {0,1,2} under the printed condition"*.
   - Inspected `#9448` and `Problems/pisano-order-range-refutation.md` via `gh api`: Lean-4-verified refutation of clause (v) at $(a, b) = (3, 2)$, $m = 13$ ($\omega = 3$), plus numerical check of $(3, 4)$ over $m \le 20000$; explicitly leaves the corrected clause / clause (vi) unproved.
3. **Live Zenodo API (`2026-11-27T09:03Z`):**
   - `https://zenodo.org/api/records?q=2407.20048&size=5` -> `total: 0`.

## Coverage Limits
- `gh search code` was recently rate-limited (HTTP 429); closed-access venues and private repositories not covered.

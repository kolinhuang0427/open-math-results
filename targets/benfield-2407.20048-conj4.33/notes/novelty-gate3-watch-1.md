# Gate 3 Novelty Receipt (`watch-1`): `targets/benfield-2407.20048-conj4.33/`

- **Checked UTC:** `2026-11-27T09:29Z`
- **Target:** Brennan Benfield and Oliver Lippard, *"Connecting Zeros in Pisano Periods to Prime Factors of $K$-Fibonacci Numbers"*, `arXiv:2407.20048v2` (`2025-01-30`), Section 4.2, Conjecture 4.33 (`\label{even-K-exceptions}`)
- **Audited Artifacts Verified:** `TARGET.md`, `PROOF.md`, `AUDIT.md` (`@audit-1` re-audit PASS), cmd `.venv/bin/python targets/benfield-2407.20048-conj4.33/notes/check-check-2.py`
- **Verdict:** **PASS (Open / Uncontested)**

## Queries & Observed Results
1. **Local snapshots (`tools/novelty_grep.py 2407.20048 "even-K-exceptions" "Conjecture 4.33"` at `09:28Z`):** `0` lines across `0/608` files (including `1337isnot1337/solved-conjectures` rebuilt `09:19:40Z`, `the-omega-institute/trureturing*`, `openai/math`, `formal-conjectures`).
2. **Live arXiv (`tools/arxiv_fetch.py query --id-list 2407.20048` at `09:28Z`):** `2407.20048v2` (`2025-01-30T20:24:47Z`) remains latest.
3. **Live GitHub (`gh search issues "2407.20048"` & `gh api repos/the-omega-institute/trureturing/issues/23317` at `09:28Z`):**
   - `trureturing#9448` (closed, Conjecture 5.3(v)), `trureturing#23099` (`2404.08193` Conjecture 10.4), and `trureturing#23317` (`state: open`, `comments: 0`, `updated_at: 2026-10-28T20:05:07Z`, unproved Q4.34 preregistration explicitly noting no Lean proof and excluding Conjecture 4.33).
4. **Live Zenodo API (`https://zenodo.org/api/records?q=2407.20048&size=5` at `09:28Z`):** `0` hits (`total: 0`).

## Coverage Limits
- Journal publication *The Fibonacci Quarterly* 63(2) (2025), 240–258 (`doi:10.1080/00150517.2025.2460555`) remains paywalled (`HTTP 403`) and unread beyond `arXiv:2407.20048v2`.

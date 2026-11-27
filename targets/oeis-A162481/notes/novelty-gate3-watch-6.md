# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A162481/`

- **Checked UTC:** `2026-11-27T11:36:48Z`
- **Target:** OEIS `A162481` (`rev. 23`, `2025-10-09T23:21:43-04:00`) — R. J. Mathar's Dec 11 2011 4-term D-finite recurrence `(n+1)*a(n) + 2*(1-4*n)*a(n-1) + 2*(5*n-3)*a(n-2) + 4*(2-n)*a(n-3) + (n-3)*a(n-4) = 0`.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A162481 162481` -> `# 0 lines across 0/658 files in 0.47s`.
2. **Live OEIS JSON (`https://oeis.org/search?q=id:A162481&fmt=json` at `11:36:48Z`):**
   - `rev: 23`, `time: 2025-10-09T23:21:43-04:00`; Mathar's Dec 11 2011 recurrence remains marked `Conjecture:`.
3. **Zenodo / arXiv / GitHub / Web (verified in Gate 2 at `11:32Z`, plus `trureturing/dev` `Problems/` tree at `11:36Z`):** `0` hits.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

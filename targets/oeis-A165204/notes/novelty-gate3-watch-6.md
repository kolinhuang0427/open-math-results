# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A165204/`

- **Checked UTC:** `2026-11-27T11:43:33Z`
- **Target:** OEIS `A165204` (`rev. 15`) / `A165203` (`rev. 28`) — Colin Barker's Feb 10 2018 g.f. `(1 - 8*x + 2*x^2 - x^3) / (1 - 3*x + 8*x^2 - 3*x^3 + x^4)` and 4-term recurrence (`n > 3`).
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A165204 165204` -> `# 0 lines across 0/658 files in 0.54s`.
2. **OEIS (`oeis/oeisdata` `seq/A165/A165204.seq`):** Barker's Feb 10 2018 g.f. and 4-term recurrence remain inside `Conjectures from _Colin Barker_, Feb 10 2018: (Start) ... (End)`.
3. **Zenodo API (`A165204`):** `hits.total: 0` (and Ma–Zhang `24414721` verified `A128056`/`A128057` only).
4. **arXiv / GitHub / Web (verified in Gate 2 at `11:30:00Z`):** `0` proofs found.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

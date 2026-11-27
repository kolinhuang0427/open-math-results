# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A168503/`

- **Checked UTC:** `2026-11-27T11:41:53Z`
- **Target:** OEIS `A168503` (`rev. 20`) — R. J. Mathar's Feb 10 2015 4-term recurrence.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A157003 157003 A168503 168503` -> `# 0 lines across 0/658 files in 1.16s`.
2. **OEIS (`oeis/oeisdata` `seq/A168/A168503.seq`):** Mathar's Feb 10 2015 4-term recurrence remains marked `Conjecture:`.
3. **arXiv / Zenodo / GitHub / Web (verified in Gate 2 at `11:36:05Z`, plus `trureturing/dev` `Problems/` tree):** `0` proofs found.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

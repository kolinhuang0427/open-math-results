# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A383410/`

- **Checked UTC:** `2026-11-27T11:50:11Z`
- **Target:** OEIS `A383410` (`rev. 6`) / `A005649` (`rev. 123`) — Mikhail Kurkov's Apr 26 2025 conjecture `A(n, 0) = A005649(n)`.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (689 files post Sweep 6, incl. `insorrowmeow/oeis-sequence-proofs`, `soux369/math`, `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py ... A383410 383410 ... A005649` -> `0` hits for `A383410`/`383410`/`A005649`.
2. **OEIS (`oeis/oeisdata` `seq/A383/A383410.seq`):** `%F A383410 Conjecture: A(n,0) = A005649(n).` unchanged.
3. **Zenodo API (`A274271+OR+A383410+OR+A392058`):** `hits.total: 0`.
4. **arXiv / GitHub / Web (verified in Gate 2 at `11:44:04Z`):** `0` proofs found.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

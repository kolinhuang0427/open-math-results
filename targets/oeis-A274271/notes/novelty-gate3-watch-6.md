# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A274271/`

- **Checked UTC:** `2026-11-27T11:50:11Z`
- **Target:** OEIS `A274271` (`rev. 12`) — Colin Barker's Jun 17 2016 closed form `((3+3^n)^2*(9+3^n))/144` ($n > 1$), 4-term recurrence ($n > 4$), and rational g.f. for partitions of `3^n` into at most 4 parts.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (689 files post Sweep 6, incl. `insorrowmeow/oeis-sequence-proofs`, `soux369/math`, `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A274271 274271 ...` -> `0` hits for `A274271`/`274271`.
2. **OEIS (`oeis/oeisdata` `seq/A274/A274271.seq`):** Barker's three formulas remain inside `Conjectures (Start) ... (End)`.
3. **Zenodo API (`A274271+OR+A383410+OR+A392058`):** `hits.total: 0`.
4. **arXiv / GitHub / Web (verified in Gate 2 at `11:34:38Z`):** `0` proofs found.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

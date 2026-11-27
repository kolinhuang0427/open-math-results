# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A392058/`

- **Checked UTC:** `2026-11-27T11:50:11Z`
- **Target:** OEIS `A392058` (`rev. 6`) / `A233335` (`rev. 20`) — Mikhail Kurkov's Dec 29 2025 conjecture `A(n, 0) = A233335(n+1)`.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (689 files post Sweep 6, incl. `insorrowmeow/oeis-sequence-proofs`, `soux369/math`, `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py ... A392058 392058 ... A233335` -> only false-positive Zenodo DOI `23920582`/`23920583` & SHA-256 hex strings (`0` hits for `A392058` or `A233335`).
2. **OEIS (`oeis/oeisdata` `seq/A392/A392058.seq`):** `%F A392058 Conjecture: A(n,0) = A233335(n+1).` unchanged.
3. **Zenodo API (`A274271+OR+A383410+OR+A392058`):** `hits.total: 0`.
4. **arXiv / GitHub / Web (verified in Gate 2 at `11:44:04Z`):** `0` proofs found.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

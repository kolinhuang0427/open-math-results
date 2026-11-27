# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A383410/`

- **Checked UTC:** `2026-11-27T11:44:04Z`
- **Target:** OEIS `A383410` (`rev. 6`) / `A005649` (`rev. 123`) — Mikhail Kurkov's Apr 26 2025 conjecture `A(n, 0) = A005649(n)`.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py ... A383410 383410 ...` -> `1` false-positive SHA-256 hex digest containing `383410` in `trureturing-source-theories`, `0` hits for `A383410`.
2. **OEIS (`oeis/oeisdata` `seq/A383/A383410.seq`):** leaves `%F Conjecture: A(n,0) = A005649(n).` marked `Conjecture:`.
3. **arXiv metadata API (`all:A383410 OR all:A392058`):** `total_results: 0`.
4. **Zenodo API (`A383410+OR+A392058`):** `hits.total: 0`.
5. **GitHub (`gh search repos A383410`, `trureturing/dev` tree):** `[]`.
6. **Web search (`search_web` for `"A383410" OR "A392058" Kurkov proof`):** `0` prior proofs located.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

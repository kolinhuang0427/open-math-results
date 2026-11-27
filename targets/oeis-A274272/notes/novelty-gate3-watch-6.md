# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A274272/`

- **Checked UTC:** `2026-11-27T11:40:08Z`
- **Target:** OEIS `A274272` (`rev. 12`) — Colin Barker's Jun 17 2016 closed form `(57+8*(-1)^n+63*5^n+3*5^(1+2*n)+125^n)/144`, 5-term recurrence (`n > 4`), and rational g.f.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A274272 274272` -> `# 0 lines across 0/658 files in 0.84s`.
2. **Live OEIS (`https://oeis.org/search?q=id:A274272&fmt=text` at `11:40:08Z`):**
   - `A274272` remains unchanged inside `Conjectures (Start) ... (End)`.
3. **Zenodo API (`A274272`):** `hits.total: 0`.
4. **arXiv metadata API (`all:A274272`):** `total_results: 0`.
5. **GitHub (`gh search repos/issues A274272` verified at `11:37:13Z`) & Web:** `0` proofs found.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

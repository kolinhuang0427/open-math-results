# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A392058/`

- **Checked UTC:** `2026-11-27T11:44:04Z`
- **Target:** OEIS `A392058` (`rev. 6`) / `A233335` (`rev. 20`) — Mikhail Kurkov's Dec 29 2025 conjecture `A(n, 0) = A233335(n+1)`.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py ... A392058 392058` -> only false-positive Zenodo DOI `23920582`/`23920583` substrings (`mathesis-papers` / `trureturing-requests#179`), `0` hits for `A392058`.
2. **OEIS (`oeis/oeisdata` `seq/A392/A392058.seq`):** leaves `%F Conjecture: A(n,0) = A233335(n+1).` marked `Conjecture:`.
3. **arXiv metadata API (`all:A383410 OR all:A392058`):** `total_results: 0`.
4. **Zenodo API (`A383410+OR+A392058`):** `hits.total: 0`.
5. **GitHub (`gh search repos A392058`, `trureturing/dev` tree):** `[]`.
6. **Web search (`search_web` for `"A383410" OR "A392058" Kurkov proof`):** `0` prior proofs located.

## Coverage Limits

- arXiv query covers metadata rather than PDF full text; offline or unindexed manuscripts are outside direct visibility.

# Gate 2 Novelty Check (`watch-6`): `targets/oeis-A379459/`

- **Checked UTC:** `2026-11-27T11:41:53Z`
- **Target:** OEIS `A379459` (`rev. 4`) / `A379460` (`rev. 4`) / `A006351` (`rev. 195`) — Mikhail Kurkov's Dec 23 2024 / Jan 16 2025 conjectures `A_459(n,0) = A006351(n+2)` and `A_460(n,0) = A006351(n+1)`.
- **Verdict:** **PASS** (no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A379459 379459 A379460 379460` -> `# 2 lines across 2/658 files` (false-positive SHA-256 hex string containing `379460` in `trureturing-source-theories`).
2. **OEIS (`oeis/oeisdata` `A379459.seq`, `A379460.seq`):** both leave `%F Conjecture: A(n,0) = A006351(...)` marked `Conjecture:`.
3. **arXiv metadata API (`all:A379459 OR all:A379460`):** `total_results: 0`.
4. **Zenodo API (`A379459+OR+A379460`):** `hits.total: 0`.
5. **GitHub (`gh search repos A379459`, `trureturing/dev` tree):** `[]` (note `trureturing#27785` is an open preregistration with `0` comments/PRs).
6. **Web search (`search_web` for `"A379459" OR "A379460" Kurkov proof`):** no published proof surfaced.

## Coverage Limits

- `oeis.org/search` transiently rate-limited, mitigated by `raw.githubusercontent.com/oeis/oeisdata`; arXiv query covers metadata rather than PDF full text.

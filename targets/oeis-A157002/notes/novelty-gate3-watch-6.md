# Gate 3 Novelty Check (`watch-6`): `targets/oeis-A157002/`

- **Checked UTC:** `2026-11-27T11:34:38Z`
- **Target:** OEIS `A157002` (`rev. 15`, `2025-09-22T16:00:57-04:00`) — R. J. Mathar's Nov 19 2014 4-term recurrence `(n+1)*a(n) +3*(-n+1)*a(n-1) +2*(-2*n+1)*a(n-2) +2*(2*n-7)*a(n-3) +2*(2*n-7)*a(n-4)=0`.
- **Verdict:** **PASS** (<1h freshness confirmed; no prior proof found)

## Exact Queries & Results

1. **Snapshot grep (658 files incl. `mylesparslow-conjecture-ledger.md`, Su `24366920`/`23760779`, Cohen `24384895`, Blanco Gómez `23112421`/`23114921`, `zenodo-2026-oeis-compendia-ids.md`):**
   - `.venv/bin/python -u tools/novelty_grep.py A176126 176126 A183063 183063 A157002 157002` -> `0` hits for `A157002`/`157002`.
2. **Live OEIS JSON / arXiv / Zenodo / GitHub (`11:32:31Z`) & `658`-file snapshot refresh (`11:34:38Z`):**
   - `A157002` `rev: 15` (`2025-09-22T16:00:57-04:00`) remains marked `Conjecture:`, arXiv `0`, Zenodo `0`, `gh search repos A157002` `[]`, web clear.

## Coverage Limits

- `gh search issues` / `gh search code` were omitted on `A157002` (`gh search repos` + `novelty_grep` across 658 files clear); arXiv query covers metadata rather than full PDF text.

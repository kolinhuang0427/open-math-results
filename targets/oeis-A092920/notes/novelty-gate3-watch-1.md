# Gate 3 Novelty Receipt — `oeis-A092920`

- **UTC Time:** `2026-11-27T08:50Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 586 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 22 (`2026-11-27T08:41:11Z`): `0` hits for `A092920`, `strongly monotone partitions`, `A006789`.
   - `.venv/bin/python tools/novelty_grep.py A092920 "strongly monotone partitions" "A006789"` -> `0` lines across `0/586` files.
2. **Live GitHub (`gh search`):**
   - `gh search issues "A092920"` -> `0` issues.
   - `gh search code "A092920"` -> only `archmageirvine/joeis` (`A092920.java`) and `africamonkey/OEIS-Spider` (`A092920.txt`), no proof.
3. **Live OEIS & Zenodo API (`2026-11-27T08:48Z`):**
   - `https://oeis.org/search?q=id:A092920&fmt=json` -> revision `56` (`2026-03-14T12:38:00-04:00`), Kurkov's Apr 24 2023 formula still marked `Conjecture:`.
   - `https://zenodo.org/api/records?q=A092920&size=1` -> `total: 0`.

## Coverage Limits
- Closed-access venues and private repositories.

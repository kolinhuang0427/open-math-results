# Gate 3 Novelty Receipt — `oeis-A286044`

- **UTC Time:** `2026-11-27T08:53Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 601 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `A286044`, `Velin Yanev`, `011->0`.
   - `.venv/bin/python tools/novelty_grep.py A286044 286044 "Velin Yanev" "011->0"` -> `joaquimmj__oeis-conjectures/files.txt` (`conjectures/phase0/A286044.txt`, open conjecture dump) and `trureturing#34637` (Velin Yanev `A367865`, unrelated); `0` proofs.
2. **Live GitHub (`gh search`):**
   - `gh search issues "A286044"` -> `0` issues.
   - `gh search code "A286044"` -> `archmageirvine/joeis`, `loda-lang/loda-programs`, `ai4reason/oeis-atp-benchmark` (`pb/A286044.smt2`, pre-2026 definition benchmark without Yanev formula).
3. **Live OEIS & Zenodo API (`2026-11-27T08:52Z`):**
   - `https://oeis.org/search?q=id:A286044&fmt=json` -> revision `8` (`2026-02-19T22:02:10-05:00`), Yanev's Feb 16 2026 formula remains marked `Conjecture:`.
   - `https://zenodo.org/api/records?q=A286044&size=1` -> `total: 0`.

## Coverage Limits
- Closed-access venues and private repositories.

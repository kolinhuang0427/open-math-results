# Gate 3 Novelty Receipt — `oeis-A350963`

- **UTC Time:** `2026-11-27T08:53Z`
- **Reviewer:** `watch-1`
- **Verdict:** **PASS** (no `CONTESTED.md`)

## Sources Checked & Exact Queries

1. **Local rebuilt watch snapshots (`watch/snapshots/**`, 601 files across all 7 snapshot dirs):**
   - `1337isnot1337/solved-conjectures` Sweep 23 (`2026-11-27T08:49:42Z`): `0` hits for `A350963`, `XXOXX`, `A351966`, `A351967`.
   - `.venv/bin/python tools/novelty_grep.py A350963 350963 "XXOXX" A351966 A351967` -> `2` hits (`350963` inside a sha256 filename in `trureturing-source-theories`, unrelated); `0` genuine hits.
2. **Live GitHub (`gh search`):**
   - `gh search issues "A350963"` -> `0` issues.
   - `gh search code "A350963"` -> `archmageirvine/joeis` (`A350963.java`), `loda-lang/loda-programs` (`A350963.asm`), `gfis/joeis-lite`, `kolinhuang0427/open-math-results` (unrelated receipt); no proof.
3. **Live OEIS & Zenodo API (`2026-11-27T08:52Z`):**
   - `https://oeis.org/search?q=id:A350963&fmt=json` -> revision `54` (`2025-11-05T15:22:48-05:00`), unchanged (`Conjectured g.f.`).
   - `https://zenodo.org/api/records?q=A350963&size=1` -> `total: 0`.

## Coverage Limits
- Closed-access venues and private repositories.

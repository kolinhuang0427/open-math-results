# Gate 3 Novelty Check — oeis-A014137 (watch-5)

- **Checked UTC:** 2026-11-27T10:59:13Z – 2026-11-27T10:59:16Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Sergei N. Gladkovskii's May 14 2013 `A014137` continued fraction conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A014137`
   - Result: `0` lines across `0/635` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A014137&fmt=json`):**
   - `A014137` rev. 180: Gladkovskii's May 14 2013 `FORMULA` remains `G.f. (conjecture): Q(0)/(1-x) ...`.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A014137'`: `0` entries.
   - Zenodo live API (`A014137`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A014137/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A014137/notes/check-check-3.py`

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.

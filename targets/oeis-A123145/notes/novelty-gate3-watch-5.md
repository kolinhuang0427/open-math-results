# Gate 3 Novelty Check — oeis-A123145 (watch-5)

- **Checked UTC:** 2026-11-27T10:56:05Z – 2026-11-27T10:56:08Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Sergei N. Gladkovskii's Nov 26 2012 `A123145` 5-step continued fraction EGF conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A123145`
   - Result: `0` lines across `0/635` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A123145&fmt=json`):**
   - `A123145` rev. 31: Gladkovskii's Nov 26 2012 `FORMULA` remains prefixed with `Conjecture:`.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A123145'`: `0` entries.
   - Zenodo live API (`A123145`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A123145/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A123145/notes/check-check-3.py`

## Coverage Limits
- Local snapshot coverage reflects `635` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.

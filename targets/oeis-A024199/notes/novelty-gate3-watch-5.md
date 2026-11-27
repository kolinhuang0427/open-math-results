# Gate 3 Novelty Check — oeis-A024199 (watch-5)

- **Checked UTC:** 2026-11-27T10:41:31Z – 2026-11-27T10:41:35Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Peter Bala's Nov 15 2016 `A024199` double-factorial sum / EGF conjecture found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A024199`
   - Result: `0` lines across `0/619` files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A024199&fmt=json`):**
   - `A024199` rev. 80: Bala's Nov 15 2016 `FORMULA` remains prefixed with `Conjecture:` with no confirmation note.

3. **arXiv / Zenodo / GitHub:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A024199'`: `0` entries.
   - Zenodo live API (`A024199`): `0` hits.
   - `gh search issues "A024199"` & `gh search repos "A024199"`: `0` matches.

## Verification Scope
- Audit target files: `targets/oeis-A024199/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-3.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A024199/notes/check-check-3.py`

## Coverage Limits
- Local snapshot coverage reflects `619` files; live OEIS, arXiv, Zenodo, and GitHub issues/repos returned `0` settlement hits.

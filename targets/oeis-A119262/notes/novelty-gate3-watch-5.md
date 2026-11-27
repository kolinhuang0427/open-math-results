# Gate 3 Novelty Check — oeis-A119262 (watch-5)

- **Checked UTC:** 2026-11-27T10:30:44Z – 2026-11-27T10:32:50Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of Benedict W. J. Irwin's Apr 19 2017 Hessenberg determinant conjecture in `A119262` found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A119262`
   - Result: `0` lines across `0/619` files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A119262&fmt=json`):**
   - `A119262` rev. 55: Irwin Apr 19 2017 formula remains prefixed with `Conjecture:` with no confirmation note.

3. **arXiv / Zenodo / GitHub:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A119262'`: `0` entries.
   - Zenodo live API (`A119262`): `0` hits.
   - `gh search issues "A119262"` & `gh search repos "A119262"`: `0` matches.

## Verification Scope
- Audit target files: `targets/oeis-A119262/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A119262/notes/check-check-1.py`

## Coverage Limits
- Local snapshot coverage reflects `619` files; live OEIS, arXiv, Zenodo, and GitHub issues/repos returned `0` settlement hits.

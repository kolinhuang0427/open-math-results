# Gate 3 Novelty Check — oeis-A361430 (watch-5)

- **Checked UTC:** 2026-11-27T11:01:10Z – 2026-11-27T11:01:21Z (`<1h` before reporting)
- **Result:** **PASS** (no prior proof or confirmation of the `A361430` / `A298826` conjectures by Oudra, Kotesovec, and Schulte found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A361430 A298826`
   - Result: `0` lines across `0/636` snapshot files (also absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`).

2. **Live OEIS JSON (`A361430` & `A298826`):**
   - `A361430` rev. 41: `Conjecture: a(n) = abs(A298826(n)).` remains unconfirmed.
   - `A298826` rev. 125: Oudra, Kotesovec, and Schulte formulas all remain explicitly prefixed with `Conjecture:`.

3. **arXiv / Zenodo:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A361430 OR all:A298826'`: `0` entries.
   - Zenodo live API (`A361430`): `0` hits.

## Verification Scope
- Audit target files: `targets/oeis-A361430/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`
- Verification command: `.venv/bin/python -u targets/oeis-A361430/notes/check-check-1.py`

## Coverage Limits
- Local snapshot coverage reflects `636` files; live OEIS, arXiv, and Zenodo returned `0` settlement hits.

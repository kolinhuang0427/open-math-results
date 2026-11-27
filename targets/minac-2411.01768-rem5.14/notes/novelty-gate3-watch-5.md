# Gate 3 Novelty Check — minac-2411.01768-rem5.14 (watch-5)

- **Checked UTC:** 2026-11-27T10:55:16Z – 2026-11-27T10:55:34Z (`<1h` before reporting)
- **Result:** **PASS** (no prior refutation or resolution of Mináč–Nguyen–Tân `arXiv:2411.01768v2` §5.2 Remark 5.14 `rem:same_degree` found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py 2411.01768 "Remark 5.14" "rem:same_degree" "Mináč"`
   - Result: `4` lines across `4/635` files (unrelated `aliromman__math#88` Fekete polynomials and `mathesis-papers-org` primeness question; `0` hits for `2411.01768`, `Remark 5.14`, or `rem:same_degree`).

2. **arXiv / Semantic Scholar:**
   - `id:2411.01768`: latest version `2411.01768v2` (`updated: 2026-08-03T02:49:58Z`).
   - `abs:2411.01768`: `0` entries.
   - S2 `ARXIV:2411.01768/citations`: `4` citations (`2609.30407`, `2605.11445`, `2508.10348`, `2503.04086` — all previously inspected and distinct from `rem:same_degree`).

3. **Zenodo:**
   - Zenodo live API (`2411.01768`): `0` hits.

## Verification Scope
- Audit target files: `targets/minac-2411.01768-rem5.14/{TARGET.md,COUNTEREXAMPLE.md,AUDIT.md,notes/check-check-2.py}`
- Verification command: `.venv/bin/python -u targets/minac-2411.01768-rem5.14/notes/check-check-2.py`

## Coverage Limits
- Local snapshot coverage reflects `635` files (`gh search` rate-limited in prior call, covered by snapshots); live arXiv, S2 citations, and Zenodo returned `0` settlement hits.

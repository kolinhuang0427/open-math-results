# Novelty Receipt — Gate 2 (`watch-5`)

- **Target:** `targets/oeis-A176126/` (`OEIS:A176126` rev. 18, `OEIS:A127276` rev. 33, `OEIS:A001788`)
- **Timestamp (UTC):** `2026-11-27T11:24Z`
- **Verdict:** **PASS** (no settled prior art found)

## Exact Queries & Results

1. **`watch/snapshots/` (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python tools/novelty_grep.py A176126`
   - Result: `0` lines across `0/653` files (incl. Cohen Zenodo `24384895` and Zenodo `23112421`/`23114921`).
2. **arXiv API (`tools/arxiv_fetch.py`):**
   - Query: `all:A176126` -> `0` entries.
3. **OEIS Live JSON (`https://oeis.org/search?q=id:A176126&fmt=json`):**
   - `A176126` rev. `18` (`2022-08-27`) still marks Mathar's Dec 12 2010 recurrence and generating function as `Conjecture:`.
4. **Zenodo API (`https://zenodo.org/api/records?q=%22A176126%22`):**
   - `0` hits.
5. **Web Search (`search_web`):**
   - Query `"A176126" Mathar OR conjecture OR proof OR recurrence OR generating function` returned only OEIS links (`A176126`, `A001788`), no proof of Mathar's conjecture or `A127276(n)` dependency.

## Coverage Limits

- No cited arXiv preprint on this target for OpenAlex/S2 citing-paper traversal.

# Gate 2 Novelty Check — oeis-A400812 (watch-5)

- **Checked UTC:** 2026-11-27T10:30:03Z – 2026-11-27T10:32:50Z
- **Result:** **PASS** (no prior proof or settlement of Boris K. Horvat's empirical `A400812` / `A400813` / `A400814` Spectre star-triple conjectures found).

## Exact Queries & Results

1. **Local snapshot grep:**
   - Command: `.venv/bin/python tools/novelty_grep.py A400812 A400813 A400814 Horvat`
   - Result: `17` lines across `7/618` files (`Horvath` / `Horvat–Orbanić` EDM substring matches only; `0` hits for `A400812`, `A400813`, `A400814`).
   - Absent from `watch/snapshots/zenodo-23112421-oeis-ids.md`.

2. **Live OEIS JSON (`https://oeis.org/search?q=id:A400812&fmt=json`):**
   - `A400812` rev. 50: formulas remain marked `Conjecture:` and comments explicitly state *"they are not proved"*.

3. **arXiv / Zenodo / GitHub / Web:**
   - `.venv/bin/python tools/arxiv_fetch.py query 'all:A400812'`: `0` entries.
   - Zenodo live API (`A400812`): `0` hits.
   - `gh search issues "A400812"` (`1` unrelated `georchestra/cadastrapp#329`), `gh search repos "A400812"` (`0`).
   - `search_web` (`"A400812" "Horvat" OR "conjecture" OR "gf"`): only OEIS `A400812`/`A400813`/`A400811` cluster entries; `0` proofs found.

## Coverage Limits
- Local snapshot coverage reflects Sweep 2 (`2026-11-27T09:55:58Z`); live OEIS, arXiv, Zenodo, GitHub issues/repos, and `search_web` returned live `0` settlement hits.

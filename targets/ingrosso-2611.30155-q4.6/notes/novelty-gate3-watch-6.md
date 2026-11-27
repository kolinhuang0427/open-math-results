# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/ingrosso-2611.30155-q4.6/`

- **Target:** E. Ingrosso, M. Trombetti, and A. Zitouni, `arXiv:2611.30155v1` / DOI `10.1017/s1446788726101682` (*"Groups with dual classes of subgroups"*, submitted `2026-11-23`), Section 4, **Question 4.6** (sharp subnormal defect in Theorem 4.5 `\label{sip}` proved $= 2$).
- **Checked UTC:** `2026-11-27T16:37:33Z` – `2026-11-27T16:37:43Z` (after `#1687` blind audit PASS, immediately prior to `RESULTS.md` publication)
- **Verdict:** **PASS — OPEN** (no prior proof or settlement of Question 4.6 found).

## Fresh `<1h` Queries & Findings

1. **Local Snapshot Index (`watch/snapshots/`, `742` indexed files incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `jmadeiros__conjecture-desk.json`):**
   - `.venv/bin/python tools/novelty_grep.py 2611.30155 "ingrosso-2611.30155" "s1446788726101682" "pro-norm" --max-per-file 0 --max-total 20` -> `6` lines across `3/742` files, exclusively `watch/snapshots/arxiv/{arxiv_submissions.json,arxiv_submissions.md,state.json}` announcing `2611.30155v1`.
2. **Live GitHub (`2026-11-27T16:37Z`):**
   - `gh search code '"2611.30155"'`, `gh search repos "2611.30155"`, `gh search issues "2611.30155"`, `gh search prs "2611.30155"`, `gh search code '"s1446788726101682"'` -> `[]` on all five.
3. **Live arXiv, Zenodo, Hexagon & Web (`2026-11-27T16:37Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.30155` -> `2611.30155v1` (`published 2026-11-23T07:03:10Z`) remains the sole version.
   - `https://zenodo.org/api/records?q=2611.30155` -> `0` hits.
   - Live `https://hexagonmath.org/api/v1/works` (`q=Ingrosso`, `q=2611.30155`) -> `0` hits.
   - `search_web` (`"2611.30155" OR "s1446788726101682" ("Question 4.6" OR "defect" OR "pronormal")`) -> returns only Ingrosso–Trombetti–Zitouni's `arXiv:2611.30155` / JAMS paper.

## Verification Command & Artifacts

- **Check command:** `.venv/bin/python -u targets/ingrosso-2611.30155-q4.6/notes/check-check-1.py` (verified `PASS` in `AUDIT.md` `#1687`)
- **Paths:** `targets/ingrosso-2611.30155-q4.6/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`

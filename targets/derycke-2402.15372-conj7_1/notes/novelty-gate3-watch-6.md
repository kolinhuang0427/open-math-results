# Gate 3 Novelty Check — `targets/derycke-2402.15372-conj7_1/`

- **Checked at:** `2026-11-27T10:08:58Z`
- **Checker:** `watch-6`
- **Audit reviewed:** `AUDIT.md` (PASS by `audit-2`; command `.venv/bin/python targets/derycke-2402.15372-conj7_1/notes/check-check-2.py`; files: `TARGET.md`, `PROOF.md`, `AUDIT.md`, `notes/check-check-2.py`)
- **Result:** **PASS (no settling prior resolution found)**

## Exact Queries & Results

1. **Local watchlist & snapshot grep (`tools/novelty_grep.py`):**
   - Query: `.venv/bin/python -u tools/novelty_grep.py 2402.15372 Derycke ITCCTIsymmetry` -> `12` lines across `3/618` files (`watch/snapshots/arxiv/citing_papers.json`, `citing_papers.md`, `last_sweep_report.json` listing OpenAlex `cited_by=3; S2=4`: `2506.23237`, `2409.11811`, `2401.06488`, `2207.01997`, previously inspected in Gate 2 and non-settling). `0` hits in GitHub/Zenodo/formal snapshots.
2. **GitHub search (`gh search repos` / `gh search issues`):**
   - `gh search repos "2402.15372"` -> `[]`
   - `gh search issues "2402.15372"` -> `[]`
   - `gh search repos "ITCCTI"` -> `[]`
3. **arXiv live query (`export.arxiv.org/api/query?id_list=2402.15372`):**
   - Latest version remains `arXiv:2402.15372v3` (`published 2024-02-23`, `updated 2025-12-19`).
4. **Zenodo API:**
   - `q=2402.15372` -> `0` hits.
   - `q=ITCCTI` -> `0` hits.

## Coverage Limits
- GitHub code search was skipped during shared secondary rate-limit cooldown; local snapshots (`618` files), `gh search repos/issues`, live arXiv, and Zenodo API queries ran at `2026-11-27T10:08:58Z`.

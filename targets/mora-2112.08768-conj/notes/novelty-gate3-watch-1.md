# Gate 3 Novelty Check — `mora-2112.08768-conj` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T18:45:44Z`–`2026-11-27T18:45:54Z`
- **Target:** `targets/mora-2112.08768-conj/` — Mercè Mora, María José Souto-Salorio, and Ana Dorotea Tarrío-Tobar, *"Resolving sets tolerant to failures in three-dimensional grids"* (`arXiv:2112.08768v1`, `2021-12-16`; *Mediterr. J. Math.* **19** (2022), no. 4, **art. 188**, `DOI:10.1007/s00009-022-02096-1`), Section 3 Conjecture 21
- **Claimed label (`AUDIT.md`):** `counterexample verified by independent exact computation` (**FALSE**: explicit $30$-vertex $14$-resolving set on $P_3 \Box P_3 \Box P_4$ giving $\dim_{14} \le 30 < 32$, plus $(3,3,5,15)$, $(3,4,4,15)$, $(4,4,4,17)$)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/mora-2112.08768-conj/notes/check-check-3.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2112.08768" "k-resolving"`):**
   - `0` lines across `0/762` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T18:45:44Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `19512c9c7be25c0f8d3cca3707767155d8bc34ef` (`2026-11-27T18:45:26Z`, ordinal rayless graphs) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2112.08768"` -> `0` hits (`[]`).
   - `gh search issues "2112.08768"` -> `0` hits (`[]`).
   - `gh search code '"10.1007/s00009-022-02096-1"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2112.08768`) -> sole version `2112.08768v1` (`2021-12-16T10:26:03Z`).
   - Zenodo API (`q=2112.08768`) -> `0` hits.
   - Crossref (`10.1007/s00009-022-02096-1`) -> `is-referenced-by-count: 4` (unchanged since Gate 2, where `watch-5`/`watch-6` verified all 4–6 citing works non-settling).
   - Web search -> only Mora–Souto-Salorio–Tarrío-Tobar paper (`arXiv:2112.08768`, `upc.edu`); `0` refutations or settlements of Conjecture 21.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/mora-2112.08768-conj/notes/check-check-3.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`762` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref count, and public web search as of `2026-11-27T18:45:54Z`; private repositories and non-indexed preprints remain unobservable.

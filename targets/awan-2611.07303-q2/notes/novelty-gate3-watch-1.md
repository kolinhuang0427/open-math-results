# Gate 3 Novelty Check — `awan-2611.07303-q2` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T18:41:36Z`–`2026-11-27T18:41:45Z`
- **Target:** `targets/awan-2611.07303-q2/` — Saad A. Awan, Steven J. Miller, Linh Nguyen, Steven Senger, and Elvis Wong, *"Gaps in the Most Frequent Sizes of Integer Sumsets"* (`arXiv:2611.07303v2`, `2026-11-09`), Section 5.2 Question 2 (`\label{q:rate}`)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (**YES** convergence for all $h \ge 2, k \ge 3$ to normalized volume sum $c_{h,k}$; **NO** not eventually monotone)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/awan-2611.07303-q2/notes/check-check-1.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2611.07303" "q:rate"`):**
   - `0` lines across `0/762` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T18:41:36Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `53ce51af9295b6a5edc36734b70ed71b29b1f558` (`2026-11-27T18:35:17Z`) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2611.07303"` -> `richfrem/Project_Sanctuary#403` (`MISSION-062`, Question 1 finite check for $k=3$ only).
   - `gh search issues "2611.07303"` -> `the-omega-institute/trureturing#29874` (Question 4 `q:distribution` only).
   - `gh search code '"2611.07303" "q:rate"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2611.07303`) -> `2611.07303v2` (`2026-11-09T14:48:06Z`), latest version.
   - Zenodo API (`q=2611.07303`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Awan et al.
   - Web search -> only `arXiv:2611.07303`; `0` resolutions of Question 2 (`q:rate`).
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/awan-2611.07303-q2/notes/check-check-1.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`762` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T18:41:45Z`; private repositories and non-indexed preprints remain unobservable.

# Gate 3 Novelty Check — `fernando-2606.01037-quesQ3` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:53:42Z`–`2026-11-27T17:54:08Z`
- **Target:** `targets/fernando-2606.01037-quesQ3/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"* (`arXiv:2606.01037v1`, `2026-05-31`), Section 6 Question 6.3 (`\label{Q3}`, `draftMay31.tex` L911–915)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (complete iff classification: $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ iff $q = 4$ and $4 \mid e$)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/fernando-2606.01037-quesQ3/notes/check-check-1.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.01037" "Question 6.3"`):**
   - `5` lines across `3/760` files, all unrelated `Question 6.3` matches (Mosquera-Lois–Tanaka in `trureturing`, Goto in `open-logic-24-add-un`); `0` hits on `2606.01037` or Fernando–Kousik Question 6.3 across `760` snapshot files (incl. all Sweep 18 / Sweep 41 additions).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:53:42Z`):**
   - `main` = `f32dec08bc3e36d906b29cad21bc0c8a57ad7589` (`2026-11-27T17:51:24Z`, PR `#1076`, Soukup ordinal thresholds) — unrelated.
   - `research` = `8b76e3d94c331f8e141f17a1f4253057d4dff6fd` (`2026-11-27T17:52:28Z`, stemwise forcing bound) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.01037"` -> `0` hits (`[]`).
   - `gh search issues "2606.01037"` -> `1` closed hit (`the-omega-institute/trureturing#8550`, Conjecture 5.23 only, not Section 6 Question 6.3).
   - `gh search code '"2606.01037" "Question 6.3"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2606.01037`) -> sole version `2606.01037v1` (`2026-05-31T06:04:17Z`).
   - Zenodo API (`q=2606.01037`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Fernando–Kousik `arXiv:2606.01037`.
   - Web search -> only Fernando–Kousik `arXiv:2606.01037` preprint; `0` resolutions of Section 6 Question 6.3.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/fernando-2606.01037-quesQ3/notes/check-check-1.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`760` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:54:08Z`; private repositories and non-indexed preprints remain unobservable.

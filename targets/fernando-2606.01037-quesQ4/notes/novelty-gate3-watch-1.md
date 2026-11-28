# Gate 3 Novelty Check — `fernando-2606.01037-quesQ4` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T18:59:31Z`–`2026-11-27T19:01:49Z`
- **Target:** `targets/fernando-2606.01037-quesQ4/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"* (`arXiv:2606.01037v1`, `2026-05-31`), Section 6 Question 6.4 (`\label{Q4}`, `draftMay31.tex` L923–926)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (complete iff classification: $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ iff $(q, e) = (4, 4)$)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/fernando-2606.01037-quesQ4/notes/check-check-2.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.01037" "Question 6.4"`):**
   - `15` lines across `6/787` files (`watch/snapshots/arxiv/{citing_papers.*,last_sweep_report.json}` indexing `arXiv:2606.01037` OpenAlex `cited_by=0` / S2 `0` and `aliromman/math#93` distinct Question 6.4); `0` settlement hits across all `787` snapshot files (incl. `cs.CC`/`cs.LO`/`math.LO` Sweep 5 / Sweep 20 additions).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T18:59:31Z`):**
   - `main` = `23c9001e01a0af59f2d4899f45cdf72dad67e0af` (`2026-11-27T18:17:50Z`, PR `#1081`) — unrelated.
   - `research` = `d33afee1b4c7b9117cf9421a5da59a0798e7311b` (`2026-11-27T18:52:56Z`, two-pattern avoidance) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.01037"` -> `0` hits (`[]`).
   - `gh search issues "2606.01037"` -> `1` closed hit (`the-omega-institute/trureturing#8550`, Conjecture 5.23 only, not Section 6 Question 6.4).
   - `gh search code '"2606.01037" "Question 6.4"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2606.01037`) -> sole version `2606.01037v1` (`2026-05-31T06:04:17Z`).
   - Zenodo API (`q=2606.01037`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Fernando–Kousik `arXiv:2606.01037`.
   - Web search -> only Fernando–Kousik `arXiv:2606.01037`; `0` resolutions of Section 6 Question 6.4.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/fernando-2606.01037-quesQ4/notes/check-check-2.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`787` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T19:01:49Z`; private repositories and non-indexed preprints remain unobservable.

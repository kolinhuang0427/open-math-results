# Gate 3 Novelty Check — `fernando-2606.01037-quesQ1` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:38:03Z`–`2026-11-27T17:38:26Z`
- **Target:** `targets/fernando-2606.01037-quesQ1/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"* (`arXiv:2606.01037v1`, `2026-05-31`), Section 6 Question 6.1 (`\label{Q1}`, `draftMay31.tex` L893–895)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (complete iff classification: $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ iff ($q = 4$ and $4 \mid e$) or ($e = 4$ and $m \not\equiv 3 \pmod 4$))
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/fernando-2606.01037-quesQ1/notes/check-check-3.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.01037" "Kousik"`):**
   - `0` lines across `0/746` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:38:03Z`):**
   - `main` = `70a39eeb56956ff694e030f23a8eecd34b23e272` (`2026-11-27T17:36:30Z`, PR `#1073`, Stanley distance nullity) — unrelated.
   - `research` = `7701914cafcfbc9e76cb78bb78cdb717da6c101f` (`2026-11-27T17:36:52Z`, $\omega_1$-sized colorings) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.01037"` -> `0` hits (`[]`).
   - `gh search issues "2606.01037"` -> `1` closed hit (`the-omega-institute/trureturing#8550`, covers Conjecture 5.23 only, not Section 6 Question 6.1).
   - `gh search code '"2606.01037" "Question 6.1"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2606.01037`) -> sole version `2606.01037v1` (`2026-05-31T06:04:17Z`).
   - Zenodo API (`q=2606.01037`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Fernando–Kousik `arXiv:2606.01037`.
   - Web search -> only Fernando–Kousik `arXiv:2606.01037` preprint; `0` resolutions of Section 6 Question 6.1.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/fernando-2606.01037-quesQ1/notes/check-check-3.py` exited `0` (`PASS`, Parts 1–5 OK).

## Coverage Limits
- Covers `watch/snapshots` (`746` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:38:26Z`; private repositories and non-indexed preprints remain unobservable.

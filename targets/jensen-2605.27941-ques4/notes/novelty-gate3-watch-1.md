# Gate 3 Novelty Check — `jensen-2605.27941-ques4` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:23:06Z`–`2026-11-27T17:23:22Z`
- **Target:** `targets/jensen-2605.27941-ques4/` — Alathea Jensen, *"Mixed thresholds in the Lonely Runner Conjecture"* (`arXiv:2605.27941v1`, `2026-05-27`), Section 5 Question 4 (`main.tex` L1158–1163)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (**YES** for $k \in \{1, 2\}$ via $(1)$ and $\{(1, 2), (2, 1)\}$; **NO** for all $k \ge 3$)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/jensen-2605.27941-ques4/notes/check-check-1.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2605.27941" "MLPS"`):**
   - `0` lines across `0/745` files.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:23:06Z`):**
   - `main` = `11641cdc821520c75001b9c07ee3b8d517bac201` (`2026-11-27T17:21:09Z`, PR `#1069`, Bourin crossed-Heinz gap) — unrelated.
   - `research` = `875e0cfa0150d5cb16f3873e55d050e1e78f1429` (`2026-11-27T17:22:37Z`, Cinna Davis stable-core reduction) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2605.27941"` -> `0` hits (`[]`).
   - `gh search issues "2605.27941"` -> `0` hits (`[]`).
   - `gh search code '"2605.27941" "Question 4"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2605.27941`) -> sole version `2605.27941v1` (`2026-05-27T04:27:10Z`).
   - Zenodo API (`q=2605.27941`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Jensen's paper.
   - Web search -> only Jensen's `arXiv:2605.27941` preprint; `0` resolutions of Section 5 Question 4.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/jensen-2605.27941-ques4/notes/check-check-1.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`745` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:23:22Z`; private repositories and non-indexed preprints remain unobservable.

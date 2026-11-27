# Gate 3 Novelty Check — `jensen-2605.27941-ques2` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:07:17Z`–`2026-11-27T17:07:42Z`
- **Target:** `targets/jensen-2605.27941-ques2/` — Alathea Jensen, *"Mixed thresholds in the Lonely Runner Conjecture"* (`arXiv:2605.27941v1`, `2026-05-27`), **Section 5** Question 2 (`main.tex` L1138–1140)
- **Claimed label (`AUDIT.md`):** `written proof, internally audited` (**NO** for all $k \ge 3$: $\mathsf{MLPS}_k$ is neither convex nor a finite union of convex sets)
- **Check cmd (verified exit `0` `PASS`):** `.venv/bin/python -u targets/jensen-2605.27941-ques2/notes/check-check-1.py`
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2605.27941" "MLPS"`):**
   - `0` lines across `0/745` files (`watch/snapshots` refreshed cleanly through Sweep 39 / `watch-6` Sweep 17).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:07:17Z`):**
   - `main` = `c68da92f29d66e63c62c720508423f922eecc0f5` (`2026-11-27T17:04:54Z`, PR `#1066`, Chen–Khare–Sahi Conjecture 4) — unrelated.
   - `research` = `9d59de1d0a68d781ba93ed626b8e743b524e54e1` (`2026-11-27T17:03:23Z`, disjoint-type guessing) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2605.27941"` -> `0` hits (`[]`).
   - `gh search issues "2605.27941"` -> `0` hits (`[]`).
   - `gh search code "MLPS_k"` -> `10` unrelated ML/neural-network/HTML (`amlpskaranthur`) substring hits; `0` lonely-runner hits (combining with `16:54Z` `gh search code "2605.27941"` direct `gh api` inspection of literature notes only).
4. **arXiv / Zenodo / Crossref / Web:**
   - arXiv API (`id_list=2605.27941`) -> sole version `2605.27941v1` (`2026-05-27T04:27:10Z`).
   - Zenodo API (`q=2605.27941`) -> `0` hits.
   - Crossref title query -> `0` matching DOIs for Jensen's paper.
   - Web search -> only Jensen's `arXiv:2605.27941` paper (`MLPS_2` convex polygon); `0` resolutions of Section 5 Question 2.
5. **Independent Check Execution:**
   - `.venv/bin/python -u targets/jensen-2605.27941-ques2/notes/check-check-1.py` exited `0` (`PASS`).

## Coverage Limits
- Covers `watch/snapshots` (`745` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, Crossref, and public web search as of `2026-11-27T17:07:42Z`; private repositories and non-indexed preprints remain unobservable.

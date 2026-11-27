# Gate 2 Novelty Check — `fernando-2606.01037-quesQ3` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:41:27Z`–`2026-11-27T17:41:35Z`
- **Target:** `targets/fernando-2606.01037-quesQ3/` — Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"* (`arXiv:2606.01037v1`, `2026-05-31`), Section 6 Question 6.3 (`\label{Q3}`, `draftMay31.tex` L911–915)
- **Claimed result:** Complete classification ($g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ iff $q = 4$ and $4 \mid e$, proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2606.01037" "Question 6.3"`):**
   - `0` hits on `2606.01037` across `746` snapshot files; `Question 6.3` matches only unrelated Mosquera-Lois–Tanaka (`trureturing#34884`, `#34833`) and Goto (`open-logic-24-add-un`).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:41:27Z`):**
   - `main` = `101c2485cae30674d5a411b5437286d48c2ffc29` (`2026-11-27T17:40:23Z`, PR `#1074`, Soukup products) — unrelated.
   - `research` = `4b6c6db62bf7c030dd309b09ee44fea5fa3a9580` (`2026-11-27T17:41:00Z`, disjoint-type guessing) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2606.01037"` -> `0` hits (`[]`).
   - `gh search issues "2606.01037"` -> `1` closed hit (`the-omega-institute/trureturing#8550`, Conjecture 5.23 only, not Section 6 Question 6.3).
   - `gh search code '"2606.01037" "Question 6.3"'` -> `0` hits (`[]`).
4. **arXiv / Zenodo / Web:**
   - arXiv API (`id_list=2606.01037`) -> sole version `2606.01037v1` (`2026-05-31T06:04:17Z`).
   - Zenodo API (`q=2606.01037`) -> `0` hits.
   - Web search -> only Fernando–Kousik `arXiv:2606.01037` preprint; `0` resolutions of Section 6 Question 6.3.

## Coverage Limits
- Covers `watch/snapshots` (`746` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, and public web search as of `2026-11-27T17:41:35Z`; private repositories and non-indexed preprints remain unobservable.

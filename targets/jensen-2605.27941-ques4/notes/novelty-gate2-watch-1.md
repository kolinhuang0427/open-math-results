# Gate 2 Novelty Check — `jensen-2605.27941-ques4` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T17:11:18Z`–`2026-11-27T17:11:41Z`
- **Target:** `targets/jensen-2605.27941-ques4/` — Alathea Jensen, *"Mixed thresholds in the Lonely Runner Conjecture"* (`arXiv:2605.27941v1`, `2026-05-27`), Section 5 Question 4 (`main.tex` L1158–1163: for fixed $k$, is $\mathsf{MLPS}_k$ determined by finitely many speed sets?)
- **Claimed result:** **YES** for $k \in \{1, 2\}$ via $(1)$ and $\{(1, 2), (2, 1)\}$; **NO** for all $k \ge 3$ (proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2605.27941" "MLPS"`):**
   - `0` lines across `0/745` files (`watch/snapshots` refreshed cleanly through Sweep 39 / `watch-6` Sweep 17).
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T17:11:28Z`):**
   - `main` = `83c001ee925136e659c23430da2ac3b65a4878b8` (`2026-11-27T17:11:28Z`, PR `#1062`, Lambie-Hanson–Uhrik disjoint-type guessing) — unrelated.
   - `research` = `7055235d5681b9b839bfed7ba38819bf843713c1` (`2026-11-27T17:09:22Z`, `origin/research` merge) — unrelated.
3. **GitHub live search:**
   - `gh search prs "2605.27941"` -> `0` hits (`[]`).
   - `gh search issues "2605.27941"` -> `0` hits (`[]`).
   - `gh search code '"2605.27941" "Question 4"'` -> `0` hits (`[]`).
   - Combined with prior direct `gh api` content inspection (`16:55Z`) of `"2605.27941"` code matches (`veenrek/openwiki`, `tradingartofwar`, `mountain`, `kavanaghpatrick`, `eliottcassidy2000`): literature references only, `0` Question 4 solutions.
4. **arXiv / Zenodo / Web:**
   - arXiv API (`id_list=2605.27941`) -> sole version `2605.27941v1` (`2026-05-27T04:27:10Z`).
   - Zenodo API (`q=2605.27941`) -> `0` hits.
   - Web search -> only Jensen's `arXiv:2605.27941` preprint and mirror; `0` resolutions of Section 5 Question 4.

## Coverage Limits
- Covers `watch/snapshots` (`745` files), live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search, arXiv API, Zenodo API, and public web search as of `2026-11-27T17:11:41Z`; private repositories and non-indexed preprints remain unobservable.

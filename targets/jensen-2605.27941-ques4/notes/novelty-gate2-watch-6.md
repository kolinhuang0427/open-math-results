# Gate 2 Novelty Receipt (`watch-6`) — `targets/jensen-2605.27941-ques4/`

- **Target:** Alathea Jensen, `arXiv:2605.27941v1` (*"Mixed thresholds in the Lonely Runner Conjecture"*, dated `2026-05-27`), **Section 5** (*Open questions and future work*, `main.tex` L1158–1163), **Question 4**: for fixed $k$, is $\mathsf{MLPS}_k$ determined by finitely many speed sets? (**YES** for $k \in \{1, 2\}$, **NO** for all $k \ge 3$).
- **Checked UTC:** `2026-11-27T17:11:20Z` – `2026-11-27T17:11:39Z`
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 4 found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `745` files after Sweep 17) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2605.27941 "jensen-2605.27941" "ques4" "MLPS" "Alathea Jensen" --max-per-file 0 --max-total 30` -> `3` lines across `3/745` files (unrelated `zhan-2609.05468-ques4`, `fernau-2611.09136-ques4` matching `ques4` only; `0` hits on `2605.27941`, `MLPS`, or `Alathea Jensen`).
   - `RESULTS.md` contains only `targets/jensen-2605.27941-ques2/` (Question 2, `617661a`); `0` entries for Question 4.
2. **Live GitHub (`2026-11-27T17:11:20Z`–`17:11:39Z`):**
   - `gh search code '"2605.27941"'` -> `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) and `kavanaghpatrick/aristotle-math-problems` (`erdos_938` cache, previously inspected abstract metadata only).
   - `gh search code '"Alathea Jensen"'` -> `12` hits (`Lyken17/arXiv-stats`, `kavanaghpatrick` `erdos_938` cache, `veenrek/openwiki` `wiki/math/CO/2605.27941v1.md` inspected via `gh api`: auto-generated arXiv abstract stub only, plus unrelated JSON review file).
   - `gh search code '"jensen-2605.27941"'`, `gh search code '"MLPS" "Question 4"'`, `gh search code '"finitely many speed sets"'`, `gh search repos "2605.27941"`, `gh search issues "2605.27941"`, `gh search prs "2605.27941"` -> `0` hits on all six (`trureturing` tree/issues already verified `0` at `17:07Z`).
3. **Live arXiv, Hexagon, Zenodo & Web (`2026-11-27T17:11:20Z`):**
   - `https://export.arxiv.org/api/query?id_list=2605.27941` -> `2605.27941v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2605.27941`, `q=MLPS`) -> `total=0` (`papex.org` `0/20` verified at `17:07Z`).
   - `https://zenodo.org/api/records?q=2605.27941` -> `0` hits.
   - `search_web` (`"2605.27941" ("Question 4" OR "convex" OR "finite union" OR "k=1" OR "k=2")`) -> returns only Jensen's `arXiv:2605.27941` preprint.

## Coverage Limits

- Unauthenticated Zenodo/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` reporting.

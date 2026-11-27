# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/jensen-2605.27941-ques4/`

- **Target:** Alathea Jensen, `arXiv:2605.27941v1` (*"Mixed thresholds in the Lonely Runner Conjecture"*, submitted `2026-05-27T04:27:10Z`), **Section 5** (*Open questions and future work*), **Question 4**: for fixed $k$, is $\mathsf{MLPS}_k$ determined by finitely many speed sets? (**YES** for $k \in \{1, 2\}$, **NO** for all $k \ge 3$).
- **Checked UTC:** `2026-11-27T17:23:06Z` – `2026-11-27T17:23:24Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 4 found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `745` files) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2605.27941 "jensen-2605.27941" "ques4" "MLPS" "Alathea Jensen" "finitely many speed sets" --max-per-file 0 --max-total 30` -> `3` lines across `3/745` files (`zhan-2609.05468-ques4`, `fernau-2611.09136-ques4` matching `ques4` only; `0` hits on `2605.27941`, `MLPS`, `Alathea Jensen`, or `finitely many speed sets`).
   - `RESULTS.md` contains only `targets/jensen-2605.27941-ques2/` (Question 2, `617661a`); `0` entries for Question 4.
2. **Live GitHub (`2026-11-27T17:23:06Z`–`17:23:24Z`):**
   - `gh search code '"2605.27941"'` -> `7` hits across `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) and `kavanaghpatrick/aristotle-math-problems` (`erdos_938` literature cache only).
   - `gh search code '"jensen-2605.27941"'`, `gh search code '"finitely many speed sets"'`, `gh search repos "2605.27941"`, `gh search issues "2605.27941"`, `gh search prs "2605.27941"` -> `0` hits on all five.
   - `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` matching `2605\.27941|2605_27941|mlps` -> `[]`.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T17:23:06Z`–`17:23:24Z`):**
   - `https://export.arxiv.org/api/query?id_list=2605.27941` -> `2605.27941v1` sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2605.27941`, `q=MLPS`) -> `total=0` on both.
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches.
   - `https://zenodo.org/api/records?q=2605.27941` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2605.27941` -> `0` indexed records (Gate 2 note: OpenAlex citer `2609.06259v3` already verified unrelated passing cite).
   - `search_web` (`"2605.27941" ("Question 4" OR "finitely many speed sets" OR "finite union")`) -> returns only Jensen's `arXiv:2605.27941` preprint.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/jensen-2605.27941-ques4/notes/check-check-1.py` -> exit `0`, `PASS` (`Section 1`, `Lemma 0`, `Section 3.1 & Lemmas 1-2`, `Lemmas 3b, 3c, 4`).

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated math forums are outside reach.

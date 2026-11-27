# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/jensen-2605.27941-ques2/`

- **Target:** Alathea Jensen, `arXiv:2605.27941v1` (*"Mixed thresholds in the Lonely Runner Conjecture"*, submitted `2026-05-27T04:27:10Z`), **Section 5** (*Open questions and future work*), **Question 2**: for $k \ge 3$, off the coordinate planes, is $\mathsf{MLPS}_k$ convex, or a finite union of convex sets? (**NO**, proved for all $k \ge 3$).
- **Checked UTC:** `2026-11-27T17:07:15Z` – `2026-11-27T17:07:45Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 2 found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `745` files after Sweep 17 incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `jmadeiros__conjecture-desk.json`, `kavanaghpatrick__aristotle-math-problems.json`):**
   - `.venv/bin/python tools/novelty_grep.py 2605.27941 "jensen-2605.27941" "MLPS" "Alathea Jensen" "Mixed thresholds" --max-per-file 0 --max-total 30` -> `# 0 lines across 0/745 files in 0.55s`.
   - `RESULTS.md` regex scan `(2605\.27941|jensen|mlps)` -> `[]`.
2. **Live GitHub (`2026-11-27T17:07:25Z`):**
   - `gh search code '"2605.27941"'` -> `7` files across `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) and `kavanaghpatrick/aristotle-math-problems` (`research_fusion/runs/erdos_938/{.cache/*,01_literature.json,fusion_candidate.json}` — already inspected literature/abstract cache only; `0` settlement of Question 2).
   - `gh search code '"jensen-2605.27941"'` -> `0` hits.
   - `gh search code '"Alathea Jensen" "MLPS"'` -> `0` hits.
   - `gh search repos "2605.27941"`, `gh search issues "2605.27941"`, `gh search prs "2605.27941"` -> `0` hits on all three.
   - `gh api "search/issues?q=repo:the-omega-institute/trureturing+2605.27941"` & `+MLPS` -> `total_count=0` on both; `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` matching `2605|27941|mlps` -> `[]`.
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T17:07:15Z`–`17:07:45Z`):**
   - `https://export.arxiv.org/api/query?id_list=2605.27941` -> `2605.27941v1` (`2026-05-27T04:27:10Z`) sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2605.27941`, `q=MLPS`) -> `total=0` on both (`q=Jensen` -> `71` unrelated Jensen's inequality works).
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches (`2605`, `jensen`, `mlps`, `lonely`).
   - `https://zenodo.org/api/records?q=2605.27941` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2605.27941` -> `0` indexed OpenAlex records (Gate 2 note: OpenAlex citer `2609.06259v3` already verified unrelated in TeX).
   - `search_web` (`"2605.27941" OR "Alathea Jensen" "MLPS" OR "Mixed thresholds in the Lonely Runner Conjecture"`) -> returns only Jensen's `arXiv:2605.27941` preprint.

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and math forums behind paywalls/auth are outside reach.

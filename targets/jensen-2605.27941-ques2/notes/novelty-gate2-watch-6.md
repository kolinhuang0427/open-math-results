# Gate 2 Novelty Receipt (`watch-6`) — `targets/jensen-2605.27941-ques2/`

- **Target:** Alathea Jensen, `arXiv:2605.27941v1` (*"Mixed thresholds in the Lonely Runner Conjecture"*, dated `2026-05-27`), Section 4, **Question 2**: for $k \ge 3$, off the coordinate planes, is $\mathsf{MLPS}_k$ convex, or a finite union of convex sets? (**NO**, proved for all $k \ge 3$).
- **Checked UTC:** `2026-11-27T16:54:52Z` – `2026-11-27T16:55:20Z`
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement of Question 2 found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `743` files incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `jmadeiros__conjecture-desk.json`):**
   - `.venv/bin/python tools/novelty_grep.py 2605.27941 "jensen-2605.27941" "MLPS" "Alathea Jensen" "Mixed thresholds" --max-per-file 0 --max-total 30` -> `# 0 lines across 0/743 files in 0.72s`.
   - `grep -iE "lonely runner|Alathea|2605\.27941" watch/snapshots/{hexagonmath-index.md,papex-index.md,raghav-research-math-index.md}` -> `0` matches. (`1337-solved-conjectures` Lonely Runner entries cover only Zhang Q8.4/Q8.5 & uniform-threshold speed bounds, unrelated.)
2. **Live GitHub (`2026-11-27T16:54Z`–`16:55Z`):**
   - `gh search code '"2605.27941"'` -> `koutya0akari/arxiv-plug-in-for-mixi2` (`data/posted.json`) and `kavanaghpatrick/aristotle-math-problems` (`research_fusion/runs/erdos_938/`, verified via `gh api`: metadata/abstract cache of `2605.27941v1` only).
   - `gh search repos "2605.27941"`, `gh search issues "2605.27941"`, `gh search prs "2605.27941"` -> `[]` on all three.
   - `gh search code '"MLPS"'` -> unrelated ML (`isl-org/Open3D-ML`, `EasyNLP`, `stocknet-dataset`).
   - `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` -> `0` paths matching `2605`, `27941`, or `mlps` (`Jensen*` paths are classical Jensen's inequality / Flensted-Jensen / canonical-product zero criteria, unrelated).
3. **Live arXiv, Zenodo, Hexagon & Web (`2026-11-27T16:54Z`):**
   - `https://export.arxiv.org/api/query?id_list=2605.27941` -> `2605.27941v1` (`published 2026-05-27T04:27:10Z`, `updated 2026-05-27T04:27:10Z`) sole version.
   - `https://zenodo.org/api/records?q=2605.27941` -> `0` hits.
   - Live `https://hexagonmath.org/api/v1/works` (`q=2605.27941`, `q=MLPS`) -> `0` hits (`q=Jensen` -> `71` unrelated Jensen's inequality hits).
   - `search_web` -> returns only Alathea Jensen's `arXiv:2605.27941v1` preprint; no settlement of Question 2 found.

## Coverage Limits

- Subsequent `gh search code '"Alathea Jensen" "MLPS"'` hit GitHub's 10/min code-search rate limit (covered by `novelty_grep.py` `0/743`, exact `"2605.27941"` code/repos/issues/prs, and `"MLPS"` code search above).
- Unauthenticated Semantic Scholar / OpenAlex APIs were not queried; independent Gate 3 (`<1h`) freshness check remains required before `RESULTS.md` entry.

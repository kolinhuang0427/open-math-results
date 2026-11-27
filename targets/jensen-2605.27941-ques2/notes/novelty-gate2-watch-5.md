# Gate 2 Novelty Receipt — `jensen-2605.27941-ques2` (`watch-5`)

- **Target:** `targets/jensen-2605.27941-ques2/` — Alathea Jensen, *"Mixed thresholds in the Lonely Runner Conjecture"*, `arXiv:2605.27941v1`, Section 4 Question 2 (for $k \ge 3$ off the coordinate planes, is $\mathsf{MLPS}_k$ convex or a finite union of convex sets?).
- **Checked UTC:** `2026-11-27T16:54:51Z`–`2026-11-27T16:56:49Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no resolution of Question 2 found across snapshots, citing papers, live GitHub, arXiv, Zenodo, OpenCitations, DataCite, or web search.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 743 files):**
   - `.venv/bin/python tools/novelty_grep.py "2605.27941" "MLPS" "Alathea" "Mixed thresholds" --max-per-file 10 --max-total 50`: `0` hits across `0/743` files.
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits.
   - `eliottcassidy2000__math.json`: Lonely Runner files target classical LRC(14), not `2605.27941` / $\mathsf{MLPS}_k$.
2. **arXiv & Citation Follow-up:**
   - **arXiv API (`id_list=2605.27941`, `all:"Alathea Jensen"`, `all:"Lonely Runner"` top 20 sorted by `submittedDate`):** `2605.27941v1` (`2026-05-27T04:27:10Z`) is sole version.
   - **OpenAlex (`doi.org/10.48550/arXiv.2605.27941` / `W7162643258`):** `cited_by_count: 1`. Checked `referenced_works` across all 11 post-May-2026 Lonely Runner arXiv preprints (`2603.24784`, `2604.23906`, `2607.16082`, `2608.13599`, `2608.18818`, `2609.02604`, `2609.03444`, `2609.06259`, `2609.23952`, `2609.36220`, `2610.23790`): **exact citer is `arXiv:2609.06259v3`** (*"Lonely Runner Relations"*, `2026-11-24`).
   - **Direct TeX verification (`tools/.arxiv_cache/eprint/2609.06259.src`, `lonelyrelations.tex` L257–258):** cites `\cite{jensen2026mixed}` only in passing as methodological precedent for Fourier series on distance-threshold functions; zero discussion of $\mathsf{MLPS}_k$ or Question 2.
   - **OpenCitations (`citations/doi:10.48550/arXiv.2605.27941`):** `[]`; **DataCite (`2605.27941`):** `0` hits; **Zenodo (`2605.27941`):** `0` hits.
3. **Live GitHub (`gh`):**
   - `gh search issues "2605.27941"`, `gh search prs "2605.27941"`, `gh search repos "2605.27941"`: `0` hits.
   - `the-omega-institute/trureturing` `dev` tree (`2605|27941|mlps|lonely.?runner`): only `LonelyRunnerDeletion/*` and `LonelyRunnerFourteenOfTwenty` (classical LRC), `0` hits on `2605.27941` or $\mathsf{MLPS}_k$.
   - Inspected `kavanaghpatrick/aristotle-math-problems` (unrelated Jensen–Siggers 2012 graph coloring), `tradingartofwar/the-lonely-runner-conjecture`, `maximilianbehr/OpenTorus`, `mountain/process-geometry` (all classical LRC, `0` hits on `2605.27941` / $\mathsf{MLPS}_k$).
4. **Web search (`search_web`):**
   - Queries `"2605.27941" OR ("MLPS" "lonely runner") OR ("Jensen" "2605.27941")`, `"Mixed thresholds in the Lonely Runner Conjecture" OR ("Alathea Jensen" "Lonely Runner")`, `"MLPS_k" OR "MLRC" "Lonely Runner" OR "13/90" "7/20" "Lonely Runner"`: return only `arXiv:2605.27941v1` summaries.

## Near-Misses & Coverage Limits
- **Near-miss:** `arXiv:2609.06259v3` (*Lonely Runner Relations*, `2026-11-24`) is the sole paper citing `2605.27941` in OpenAlex (`cited_by_count=1`), verified in TeX (`lonelyrelations.tex:257-258`) not to touch $\mathsf{MLPS}_k$ or Question 2.
- **Coverage limits:** Live Semantic Scholar endpoint returned `HTTP 429` at `16:55Z`, and `gh search code "2605.27941"` hit the GitHub code-search secondary rate limit (`HTTP 403`) at `16:55:20Z` (Gate 1 already inspected those code hits at `16:42Z`, and direct REST tree checks verified the LRC repos); private/unindexed drafts posted after `2026-11-27T16:56:49Z` are not covered.

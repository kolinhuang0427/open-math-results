# Gate 2 Novelty Receipt — `kovalyov-2611.32205-q1` (`watch-5`)

- **Target:** `targets/kovalyov-2611.32205-q1/` — Konstantin Kovalyov, *"Some conservativity results for weak arithmetic theories in a language with exponentiation"*, `arXiv:2611.32205v1` (`math.LO`), Section 3 Question 3.4(1)–(2) (conservativity / $\mathcal{L}_{\mathrm{OSR}}$-fragment of $\mathsf{IOpen} + (\mathrm{Exp})$ over $\mathsf{IOpen}$).
- **Checked UTC:** `2026-11-27T16:59:27Z`–`2026-11-27T16:59:55Z`
- **Verdict:** **PASS (OPEN / UNCONTESTED)** — no proof or counterexample settling Question 3.4(1)–(2) found.

## Exact Queries & Results
1. **Local snapshots (`watch/snapshots/**`, 744 files):**
   - `.venv/bin/python tools/novelty_grep.py "2611.32205" "Kovalyov" "IOpen" "L_OSR" --max-per-file 0 --max-total 0`: `0` hits for `2611.32205` / `L_OSR`; only unrelated `derkachkovalyov2017indefinitestieltjes.md`, `TribonacciOpenPathGap`, `LatticeSectorFullIOPentagon`, `piOpens` (19 lines across 3 files).
   - `hexagonmath-index.md`, `papex-index.md`, `hwzw-algebra-number-theory-drafts.md`, `raghav-research-math-index.md`: `0` hits.
2. **Live GitHub (`gh`):**
   - `gh search issues "2611.32205"`, `gh search prs "2611.32205"`, `gh search repos "2611.32205"`: `0` hits.
   - `gh search code "2611.32205"`: 6 hits — 2 arXiv RSS/trend mirrors (`ehijano/rss_fetch`, `yizhuan/research-radar`) and 4 unrelated numeric timestamp/float files.
   - `the-omega-institute/trureturing` `dev` tree (`2611|32205|kovalyov|iopen|dosr`) & recent PRs up to `#34929`: `0` overlapping PRs/files.
3. **Live Preprint / Citation APIs & Web:**
   - **arXiv API (`id_list=2611.32205`, `all:"IOpen"` top 5 by `submittedDate`):** `2611.32205v1` (`2026-11-24T08:51:14Z`) is the sole version and newest `IOpen` preprint on arXiv.
   - **OpenAlex (`doi.org/10.48550/arXiv.2611.32205`):** `cited_by_count: 0`.
   - **Zenodo (`q=2611.32205`):** `0` hits; **OpenCitations:** `[]`.
   - **`search_web` (`"2611.32205" OR ("Kovalyov" "IOpen" "Exp") OR ("DOSR" "IOpen")`)**: returns only `arXiv:2611.32205` itself.

## Near-Misses & Coverage Limits
- **Near-miss:** `the-omega-institute/trureturing` `Library/notes/derkachkovalyov2017indefinitestieltjes.md` is an unrelated 2017 Stieltjes-problem paper.
- **Coverage limits:** Live Semantic Scholar endpoint returned `HTTP 429` at `16:59Z`; private/unindexed drafts posted after `2026-11-27T16:59:55Z` are not covered.

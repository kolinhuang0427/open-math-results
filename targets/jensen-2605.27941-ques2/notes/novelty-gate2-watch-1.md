# Gate 2 Novelty Check — `jensen-2605.27941-ques2` (`watch-1`)

- **Timestamp (UTC):** `2026-11-27T16:54:48Z`–`2026-11-27T16:55:25Z`
- **Target:** `targets/jensen-2605.27941-ques2/` — Alathea Jensen, *"Mixed thresholds in the Lonely Runner Conjecture"* (`arXiv:2605.27941v1`, `2026-05-27`), Section 4 Question 2 (`main.tex` L1138–1140: for $k \ge 3$, off the coordinate planes, is $\mathsf{MLPS}_k$ convex, or a finite union of convex sets?)
- **Claimed result:** **NO** for all $k \ge 3$ ($\mathsf{MLPS}_k$ is neither convex nor a finite union of convex sets, proved in `PROOF.md`, zero-float zero-`/` `verify.py`)
- **Result:** **PASS (novelty clear)**

## Queries & Findings

1. **Local snapshots (`tools/novelty_grep.py --root watch/snapshots "2605.27941" "MLPS" "Jensen" "lonely runner" "Question 2"`):**
   - `1337isnot1337/solved-conjectures` (`227` `results/`): Lonely Runner hits are only `shifted-lonely-runner-counterexamples`, `lonely-runner-two-insertions`, `tight-seven-speeds`, `zhang-deletion-values`, `#130`, and unrelated Jensen-inequality papers (`simon-stable-infimum`); `0` hits on `2605.27941` or `MLPS`.
   - `ai-collections` / `discovered`: only unrelated Jensen inequality / hyperbolicity / coloring refs (`plasma-ai__erdos`, `facebookresearch__atlas-lean`, `the-omega-institute__trureturing`, `eliottcassidy2000__math`); `0` hits on `2605.27941` or `MLPS_k`.
2. **Live `1337isnot1337/solved-conjectures` HEAD check (`2026-11-27T16:54:48Z`):**
   - `main` = `8cd85adb4c5eec716bdb218b633a1e59077e15d0` (`2026-11-27T16:54:17Z`, PR `#1063`, Stanley two-extra-leaf trees) — unrelated.
   - `research` = `81f359df93974f801d30fe9b8981c36061f8f0a3` (`2026-11-27T16:54:37Z`, Bourin spectral band) — unrelated.
3. **GitHub live search & direct file inspection (`gh api`):**
   - `gh search prs "2605.27941"` -> `0` hits (`[]`).
   - `gh search issues "2605.27941"` -> `0` hits (`[]`).
   - `gh search code "2605.27941"` -> literature citations/notes only (`veenrek/openwiki/wiki/math/CO/2605.27941v1.md`, `tradingartofwar/the-lonely-runner-conjecture/notes/SOURCES.md`, `mountain/process-geometry/.../40-global-closure-contract-and-theory-audit.md`, `kavanaghpatrick/aristotle-math-problems/.../01_literature.md`, `eliottcassidy2000/math/07-reflections/lrc-*.md`), plus unrelated RSS/CSV numeric collisions; `gh api` content checks confirm all cite `arXiv:2605.27941v1` (`MLPS_2` polygon / Fourier Lemma 4.1) with `0` Question 2 results.
4. **arXiv / Zenodo / Web:**
   - arXiv API (`id_list=2605.27941`) -> sole version `2605.27941v1` (`2026-05-27T04:27:10Z`).
   - Zenodo API (`q=2605.27941`) -> `0` hits.
   - Web search -> only Jensen's `arXiv:2605.27941` preprint and mirror; no resolution of Section 4 Question 2.

## Coverage Limits
- Covers `watch/snapshots`, live `1337isnot1337/solved-conjectures` HEAD (`main`/`research`), public GitHub PR/issue/code search (note subsequent `gh search code "MLPS"` / `"Alathea" "Jensen"` queries hit GitHub's 10 req/min search rate limit at `16:55:10Z`; direct `gh api` content checks covered the `2605.27941` code hits), arXiv API, Zenodo API, and public web search as of `2026-11-27T16:55:25Z`.

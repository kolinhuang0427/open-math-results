# Gate 2 Novelty Receipt (`watch-6`) — `targets/kovalyov-2611.32205-q1/`

- **Target:** Konstantin Kovalyov, `arXiv:2611.32205v1` (*"Some conservativity results for weak arithmetic theories in a language with exponentiation"*, submitted `2026-11-24`), Section 3, **Question 3.4(1)–(2)**: is $\mathsf{IOpen} + (\mathrm{Exp})$ conservative over $\mathsf{IOpen}$ (and is the $\mathcal{L}_{\mathrm{OSR}}$-fragment of $\mathsf{IOpen}+(\mathrm{Exp})$ equal to $\mathsf{IOpen}$)? (**YES**, proved).
- **Checked UTC:** `2026-11-27T16:59:28Z` – `2026-11-27T16:59:38Z`
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement found).

## Exact Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `744` files incl. `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `kavanaghpatrick`, `jmadeiros`):**
   - `.venv/bin/python tools/novelty_grep.py 2611.32205 "kovalyov-2611.32205" "Kovalyov" "IOpen" "Z-DOSR" --max-per-file 0 --max-total 30` -> `19` lines across `3/744` files (`derkachkovalyov2017indefinitestieltjes.md` and substring matches `TribonacciOpenPathGap`, `LatticeSectorFullIOPentagon`, `piOpens`, `IsingCriticalMultiOpenBoundaryInfluence` — all unrelated).
   - `0` hits in `hexagonmath-index.md`, `papex-index.md`, `raghav-research-math-index.md`, `hwzw-algebra-number-theory-drafts.md`, `insorrowmeow-oeis-ids.md`.
2. **Live GitHub (`2026-11-27T16:59Z`):**
   - `gh search code '"2611.32205"'` -> `yizhuan/research-radar/math/daily/arxiv-trending-math-daily-2026-11-25.signals.json` only (automated daily arXiv feed).
   - `gh search repos "2611.32205"`, `gh search issues "2611.32205"`, `gh search prs "2611.32205"` -> `[]` on all three.
   - `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` -> `0` paths matching `2611`, `32205`, or `kovalyov` (`7` `TribonacciOpenPathGap`/`LatticeSectorFullIOPentagon` substring matches only).
3. **Live arXiv, Zenodo, Hexagon & Web (`2026-11-27T16:59Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.32205` -> `2611.32205v1` (`published 2026-11-24T08:51:14Z`, `updated 2026-11-24T08:51:14Z`) sole version.
   - `https://zenodo.org/api/records?q=2611.32205` -> `0` hits.
   - Live `https://hexagonmath.org/api/v1/works` (`q=Kovalyov`, `q=2611.32205`, `q=IOpen`) -> `0` hits on all three.
   - `search_web` (`"2611.32205" OR ("Kovalyov" "IOpen" "Exp" OR "Z-DOSR")`) -> returns only Kovalyov's `arXiv:2611.32205v1`.

## Coverage Limits

- Unauthenticated Semantic Scholar / OpenAlex APIs were not queried.
- Independent Gate 3 (`<1h`) freshness check remains required prior to `RESULTS.md` entry.

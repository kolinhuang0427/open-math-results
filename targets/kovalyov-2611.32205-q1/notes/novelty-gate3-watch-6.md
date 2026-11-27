# Gate 3 (`<1h`) Novelty Receipt (`watch-6`) — `targets/kovalyov-2611.32205-q1/`

- **Target:** Konstantin Kovalyov, `arXiv:2611.32205v1` (*"Some conservativity results for weak arithmetic theories in a language with exponentiation"*, submitted `2026-11-24T08:51:14Z`), Section 3, **Question 3.5(1)–(2)**: is $\mathsf{IOpen} + (\mathrm{Exp})$ conservative over $\mathsf{IOpen}$, and is its $\mathcal{L}_{\mathrm{OSR}}$-fragment equal to $\mathsf{IOpen}$? (**YES**, proved).
- **Checked UTC:** `2026-11-27T17:21:48Z` – `2026-11-27T17:22:01Z` (within `<1h` of reporting).
- **Verdict:** **PASS — OPEN** (no prior proof, disproof, or settlement found).

## Exact Live Queries & Results

1. **Local Snapshot Index (`watch/snapshots/`, `745` files after Sweep 17) & `RESULTS.md`:**
   - `.venv/bin/python tools/novelty_grep.py 2611.32205 "kovalyov-2611.32205" "IOpen" "Kovalyov" "ordered semirings" --max-per-file 0 --max-total 50` -> `19` lines across `3/745` files (`IsingCriticalMultiOpenBoundaryInfluence`, `TribonacciOpenPathGap`, `LatticeSectorFullIOPentagon`, `derkachkovalyov2017indefinitestieltjes` — all unrelated substring/author matches; `0` hits on `2611.32205`, `kovalyov-2611.32205`, or Kovalyov's `IOpen`).
   - `RESULTS.md` regex scan `(2611\.32205|kovalyov|iopen)` -> `[]`.
2. **Live GitHub (`2026-11-27T17:21:48Z`):**
   - `gh search code '"2611.32205"'` -> `yizhuan/research-radar` (`math/daily/arxiv-trending-math-daily-2026-11-25.signals.json`) only (automated daily arXiv feed).
   - `gh search code '"kovalyov-2611.32205"'`, `gh search code '"IOpen + (Exp)"'`, `gh search repos "2611.32205"`, `gh search issues "2611.32205"`, `gh search prs "2611.32205"` -> `0` hits on all five.
   - `gh api "repos/the-omega-institute/trureturing/git/trees/dev?recursive=1"` matching `2611\.32205|2611_32205|kovalyov|iopen` -> `TribonacciOpenPathGap` and `LatticeSectorFullIOPentagon` substring matches only (`0` Kovalyov/IOpen hits).
3. **Live Registries, arXiv, Zenodo, OpenAlex & Web (`2026-11-27T17:21:48Z`–`17:22:01Z`):**
   - `https://export.arxiv.org/api/query?id_list=2611.32205` -> `2611.32205v1` (`2026-11-24T08:51:14Z`) sole version.
   - `https://hexagonmath.org/api/v1/works` (`q=2611.32205`, `q=Kovalyov`, `q=IOpen`) -> `total=0` on all three.
   - `https://papex.org/sitemaps/records-1.xml` (`20` records) -> `0` matches.
   - `https://zenodo.org/api/records?q=2611.32205` -> `0` hits.
   - `https://api.openalex.org/works?filter=ids.arxiv:2611.32205` -> `0` indexed records.
   - `search_web` (`"2611.32205" OR ("Kovalyov" "IOpen" "Exp") OR ("Kovalyov" "Question 3.5" "IOpen")`) -> returns only Kovalyov's `arXiv:2611.32205` preprint.
4. **Verification Command Confirmed:**
   - `.venv/bin/python -u targets/kovalyov-2611.32205-q1/notes/check-check-2.py` -> exit `0`, `PASS` (`14 Z-DOSR plays` including `c_k=0`, `I_k(3)`, `n=1 a1=2M`, `r=1` collision, `r>=2` weak-weak equality).

## Coverage Limits

- Unauthenticated Zenodo/OpenAlex/web checks cover public indexed records only; private/unindexed repositories and auth-gated forums are outside reach.

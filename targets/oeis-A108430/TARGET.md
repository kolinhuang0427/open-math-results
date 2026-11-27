---
source: https://oeis.org/A108430 (OEIS A108430, revision 14, 2025-11-05)
status: reported
owner: scout-6
updated: 2026-11-26T23:00:00Z
identifiers: ["A108430", "A108429", "R. J. Mathar", "D-finite", "Emeric Deutsch", "lattice paths"]
---

# OEIS A108430 — R. J. Mathar (2022) D-Finite Recurrence for First-Quadrant (2,1),(1,2),(1,-1) Path Down-Steps

## Exact Statement
From OEIS **A108430** (revision 14, 2025-11-05):
- **Name:**
  > "Number of d steps in all paths from (0,0) to (3n,0) that stay in the first quadrant (but may touch the horizontal axis), consisting of steps u=(2,1), U=(1,2), or d=(1,-1)."
- **Data (`offset 1,1`):**
  > `3,31,311,3151,32299,334335,3488239,36627487,386618387,4098713631,43611791783,465496885231,4981942135611,53443871159551,574500093677535,6186886528903231,66735614131858723,720897596248427295`
- **Formula section:**
  > `a(n) = (1/n)*sum(k*binomial(n,2n-k)*binomial(n+k,n-1), k=n..2n).`
  > `Conjecture D-finite with recurrence n*(2*n+1)*(23982*n-28681)*a(n) +(-640736*n^3+1168048*n^2-901220*n+247035)*a(n-1) +(1196488*n^3-6448608*n^2+10992587*n-5911365)*a(n-2) +2*(2*n-5)*(28283*n-6993)*(n-3)*a(n-3)=0. - _R. J. Mathar_, Jul 24 2022`

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-26T20:49:29Z – 2026-11-26T21:00:00Z
- **Sources Checked:**
  - `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py A108430 "23982" "28681"` -> 0 matches for `A108430` (`28681` only matched a git SHA substring).
  - `joaquimmj/oeis-conjectures` (`conjectures/dfinite/proof.md`, `REPORT.md`, `ranked.json`) — `A108430` is unsettled (`dfinite/proof.md` only processed 6 single-square-root algebraic O.G.F. entries; `A108430` is degree-3 algebraic).
  - Live OEIS entries `A108430` (rev 14), `A108429`, `A027307`.
  - `arXiv` API query (`tools/arxiv_fetch.py`): `all:"A108430"` -> 0 results.
  - Zenodo API query (`https://zenodo.org/api/records?q=A108430&size=5`) -> `total=0`.
  - Web search: `"A108430" OR "23982*n-28681" OR "640736*n^3" recurrence` -> no prior proof located.
- **Near Misses:** Emeric Deutsch (Amer. Math. Monthly 107, 2000, Problem 10658, pp. 368–370) established the path enumeration / bivariate equation `G = 1 + t z G^2 (1 + t G)`, not Mathar's 2022 D-finite recurrence for the `d`-step total `A108430`.
- **Not Covered:** Print JSTOR text of Deutsch (2000) not downloaded.

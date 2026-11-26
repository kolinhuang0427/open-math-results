---
source: https://oeis.org/A250917 (OEIS A250917, revision 20, 2025-03-15)
status: reported
owner: scout-6
updated: 2026-11-26T22:18:00Z
identifiers: ["A250917", "R. J. Mathar", "D-finite", "Catalan", "exp(x*C(x)^3)"]
---

# OEIS A250917 — R. J. Mathar (2020) D-Finite Recurrence for exp(x C(x)^3)

## Exact Statement
From OEIS **A250917** (revision 20, 2025-03-15):
- **Name:**
  > "Expansion of e.g.f. exp( x*C(x)^3 ) where C(x) = (1 - sqrt(1-4*x))/(2*x) is the g.f. of the Catalan numbers, A000108."
- **Data (`offset 0,3`):**
  > `1,1,7,73,1033,18541,403831,10351237,305355793,10192132153,379819484551,15634219476481,704566985120857,34506514429777573,1825081888365736183,103685565729559782781,6297505655719537293601,407233553972252986277617,27935786938445348562454663`
- **Formula section:**
  > `Conjecture D-finite with recurrence: +2*a(n) +(-11*n+20)*a(n-1) +(n^3+9*n^2-116*n+164)*a(n-2) +(-4*n^4+35*n^3+n^2-317*n+342)*a(n-3) -6*(n-3)*(6*n^3-50*n^2+147*n-176)*a(n-4) +12*(n-5)*(2*n-9)*(n-3)*(n-4)*a(n-5)=0. - _R. J. Mathar_, Jan 25 2020`

## Gate 1 Novelty Receipt
- **UTC Time:** 2026-11-26T20:32:50Z – 2026-11-26T20:45:00Z
- **Sources Checked:**
  - `watch/snapshots/**` via `.venv/bin/python tools/novelty_grep.py A250917 "379819484551" "C(x)^3"` -> 0 matches across 208 files.
  - `joaquimmj/oeis-conjectures` (`conjectures/dfinite/proof.md`, `REPORT.md`, `ranked.json`) — `A250917` is unsettled (exponential generating function skipped by `dfinite/proof.md`).
  - Live OEIS entry `A250917` (rev 20, 2025-03-15).
  - `arXiv` API query (`tools/arxiv_fetch.py`): `all:"A250917"` -> 0 results.
  - Web search: `"A250917" "D-finite" OR "exp( x*C(x)^3 )" OR "11*n+20" recurrence` -> no prior proof located.
- **Near Misses:** None.
- **Not Covered:** General literature on D-finiteness of $\exp(\text{algebraic})$ establishes existence of *some* P-recurrence, not a proof of Mathar's specific order-5 recurrence for `A250917`.

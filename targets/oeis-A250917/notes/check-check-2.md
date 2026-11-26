# Independent Check Report: `targets/oeis-A250917/`

- **Checker:** `check-2`
- **Verdict:** **PASS**

## 1. Primary-Source Fidelity Check

- **Primary source checked:** Live OEIS JSON API (`https://oeis.org/search?q=id:A250917&fmt=json`), **A250917**, revision 20 (`2025-03-15T11:29:15-04:00`).
- **Exact fields verified:**
  - `name`: `"Expansion of e.g.f. exp( x*C(x)^3 ) where C(x) = (1 - sqrt(1-4*x))/(2*x) is the g.f. of the Catalan numbers, A000108."`
  - `offset`: `"0,3"`
  - `data`: `1,1,7,73,1033,18541,403831,10351237,305355793,10192132153,379819484551,15634219476481,704566985120857,34506514429777573,1825081888365736183,103685565729559782781,6297505655719537293601,407233553972252986277617,27935786938445348562454663`
  - `formula`: `"Conjecture D-finite with recurrence: +2*a(n) +(-11*n+20)*a(n-1) +(n^3+9*n^2-116*n+164)*a(n-2) +(-4*n^4+35*n^3+n^2-317*n+342)*a(n-3) -6*(n-3)*(6*n^3-50*n^2+147*n-176)*a(n-4) +12*(n-5)*(2*n-9)*(n-3)*(n-4)*a(n-5)=0. - _R. J. Mathar_, Jan 25 2020"`
- **Comparison with `TARGET.md` and `PROOF.md`:** Verbatim match with OEIS A250917 (rev 20); zero quantifier, hypothesis, edge-case, or definition drift. (Minor expository note in `PROOF.md`: line 24 writes `P_r(m+5) a(m+r) = Q_r(\theta)[F^{(r)}(x)]` while lines 26–27 index $P_r(n)$ as the coefficient of $a(n-r)$ and write $Q_r(\theta)[F^{(5-r)}(x)]$; the latter formula in line 27 is the mathematically exact one.)

## 2. Independent Mechanical & Symbolic Check

Written independently from OEIS A250917 (rev 20) and `PROOF.md` (without reading `verify.py` or any author `notes/`):

- **Script:** `targets/oeis-A250917/notes/check-check-2.py`
- **Command run:**
  ```bash
  .venv/bin/python -u targets/oeis-A250917/notes/check-check-2.py
  ```
- **Raw output:**
  ```text
  Exact differential operator check in Q(x)[S]/(S^2-(1-4x)): R(x,S) = (0, 0)
  Series & OEIS formula match all 19 OEIS terms and exact values up to n=25
  Direct recurrence check: fails at n=1,2 (as stated), == 0 for all n=3..25
  PASS (all checks passed in 13.813s)
  ```

## 3. Summary

1. Exact symbolic evaluation in $\mathbb{Q}(x)[S]/(S^2 - (1-4x))$ independently confirms $L[F](x) = R(x, S) F(x)$ with $R(x, S) = (0, 0)$ identically.
2. Exact rational power-series expansion of $\exp(x C(x)^3)$ and OEIS's binomial formula match all 19 published OEIS data terms and agree through $n=25$.
3. Direct recurrence evaluation confirms failure at $n=1, 2$ (with $a(-1)=a(-2)=0$) and exact vanishing for all $n = 3, \dots, 25$ (with $a(-1)=0$), matching `PROOF.md`.

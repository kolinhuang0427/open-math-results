# Independent Check Report: `targets/ballantine-2408.13346-e2p4-rec`

- **Checker:** `@check-2`
- **Verdict:** **PASS**
- **Check Script:** `targets/ballantine-2408.13346-e2p4-rec/notes/check-check-2.py`

## 1. Primary Source Fidelity
Checked against `arXiv:2408.13346v1` (`partitions_and_symmetric_functions-arxiv.tex`, Section 1, lines 66, 84–91):
- Definitions of $e_j(\lambda)$, $\mathcal{P}(m,n)$, and $e_j p_m(n)$ match `TARGET.md` verbatim.
- The conjectured 22-term linear recurrence for $e_2 p_4(n)$ (`y(22+n) = -y(n)-y(1+n)+3y(3+n)+...`) matches `TARGET.md` verbatim.

## 2. Independent Exact Mechanical Checks
Command:
```sh
.venv/bin/python -u targets/ballantine-2408.13346-e2p4-rec/notes/check-check-2.py
```
Output:
```
PASS (9-term GF, D(q)/N(q) exact, direct P(4,n) match n=0..40, 22-term recurrence verified)
```
All checks use pure exact integer / `sympy` rational arithmetic (zero floating point):
- **§1 Parameterization:** Verified $\sum \lambda_i = y_1 + 2y_2 + 3y_3 + 4y_4$ and the 9-term expansion of $e_2(\lambda)$ identically in $\mathbb{Z}[y_1,y_2,y_3,y_4]$.
- **§2 Generating function:** Verified all 9 rational summands over $D(q) = (1-q)^6(1+q)^4(1+q^2)^3(1+q+q^2)^3 \in \mathbb{Z}[q]$, their exact numerators in $\mathbb{Z}[q]$, and their sum $N(q)$ of degree $16 < 22$.
- **§3 Recurrence & direct enumeration:** Verified exact expansion of $D(q)$ (degree 22, palindromic coefficients $d_0=1$, $d_j=d_{22-j}$), $[q^n](N(q)/D(q)) = e_2p_4(n)$ against brute-force partition enumeration of $\mathcal{P}(4, n)$ for all $0 \le n \le 40$, and the verbatim 22-term recurrence for $0 \le n \le 18$.

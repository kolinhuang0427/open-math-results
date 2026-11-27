# Independent Check Report: `targets/oeis-A045743`

- **Checker:** `@check-2`
- **Verdict:** **PASS**
- **Check Script:** `targets/oeis-A045743/notes/check-check-2.py`

## 1. Primary Source Fidelity
Checked against live OEIS `A045743` JSON (`revision: 14`, `2022-07-26T14:31:19-04:00`):
- Name (`Number of noncrossing connected graphs on n nodes on a circle having no triangular faces.`), offset (`2,2`), closed-form sum `Sum_{i=0..floor((n-2)/2)} binomial(n-2+i, i)*binomial(3*n-3-i, n-2-2*i)/(n-1)`, Hanna's algebraic equation `x*F(x)^4 = (1 - F(x))*(1 - 3*F(x) + F(x)^2)`, and Mathar's Jul 26 2022 recurrence match `TARGET.md` and `PROOF.md` verbatim.

## 2. Independent Exact Mechanical Checks
Command:
```sh
.venv/bin/python targets/oeis-A045743/notes/check-check-2.py
```
Output:
```
PASS (OEIS data n=2..22, Lagrange/P(x,y)=0, exact Z[x,y] div Q/P=R, Z[n] C_0..C_4 match, recurrence n=6..50)
```
All checks use pure exact integer / `sympy` polynomial arithmetic over $\mathbb{Z}$ (zero floating point):
- **OEIS data & closed form:** Closed-form expression verified integer-valued and matching OEIS `data` for $2 \le n \le 22$.
- **Step 1 (Lagrange inversion & algebraic equation):** Verified $[t^{m-1}]\Phi(t)^m = m\,a(m+1)$ for $1 \le m \le 25$, $G(x)(1+G(x)-G(x)^2) = x(1+G(x))^4$, and $P(x, y(x)) = 0$ identically to $O(x^{32})$.
- **Step 2 (Order-4 ODE via exact division):** Verified $P_y^{2k-1} y^{(k)} = N_k(x, y(x))$ ($1 \le k \le 4$) to $O(x^{28})$, exact division $P(x,y) \mid Q(x,y)$ with zero remainder in $\mathbb{Z}[x,y]$, and $p_{\mathrm{inhom}}(x) + \sum_{k=0}^4 p_k(x) y^{(k)}(x) = 0$ to $O(x^{28})$.
- **Step 3 (Recurrence extraction):** Verified $\deg p_{\mathrm{inhom}} = 5 < 6$, shift range $d - k \in [0, 4]$ across $p_0,\dots,p_4$, exact polynomial equality in $\mathbb{Z}[n]$ between extracted coefficients and $C_0(n),\dots,C_4(n)$, $C_0(n) > 0$, and the full recurrence $\sum_{j=0}^4 C_j(n)a(n-j) = 0$ for all $6 \le n \le 50$.

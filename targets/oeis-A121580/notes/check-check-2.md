# Independent Check Report: `targets/oeis-A121580`

- **Checker:** `@check-2`
- **Verdict:** **PASS** (re-checked after L54–67 fixes in `PROOF.md`)
- **Check Script:** `targets/oeis-A121580/notes/check-check-2.py`

## 1. Primary Source Fidelity
Checked against live OEIS `A121580` JSON (`revision: 12`, `2024-09-15T07:13:47-04:00`):
- Name, offset (`1,2`), defining recurrence `a(1)=1, a(n)=a(n-1)+(n-1)!*(1+n*(n-1)/2)`, and R. J. Mathar's Jul 26 2022 recurrence match `TARGET.md` verbatim.
- `PROOF.md` L54–59 now display the exact polynomial expansions summing to `0`, draft scratchpad lines are removed, and L62–67 give the complete homogeneous order-4 linear ODE for $\hat{y}(x)$.

## 2. Independent Exact Mechanical Checks
Command:
```sh
.venv/bin/python targets/oeis-A121580/notes/check-check-2.py
```
Output:
```
PASS (OEIS data n=1..19, Steps 1-3 identities & EGF ODE to x^44, Mathar recurrence 5<=n<=60)
```
All checks use pure exact integer / `fractions.Fraction` / `sympy` arithmetic (zero floating point):
- **OEIS data & formulas:** Verified OEIS `data` ($1 \le n \le 19$) and Deutsch's closed form ($1 \le n \le 24$).
- **Steps 1–2:** Verified telescoping first-difference decomposition identically, each expanded polynomial term in `PROOF.md` L54–57, $P(n) \equiv 0 \in \mathbb{Z}[n]$, and Mathar's recurrence for all $5 \le n \le 60$.
- **Step 3:** Verified $a(0) = 0$ compatibility and the homogeneous order-4 EGF ODE $(1-x)\hat{y}^{(4)} + (3x-8)\hat{y}^{(3)} + (15-4x)\hat{y}'' + (2x-10)\hat{y}' + 2\hat{y} = 0$ identically to $x^{44}$.

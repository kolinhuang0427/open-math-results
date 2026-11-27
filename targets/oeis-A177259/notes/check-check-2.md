# Independent Check Report: `targets/oeis-A177259`

- **Checker:** `@check-2`
- **Verdict:** **PASS**
- **Check Script:** `targets/oeis-A177259/notes/check-check-2.py`

## 1. Primary Source Fidelity
Checked against live OEIS `A177259` JSON (`revision: 28`, `2025-11-05T15:22:18-05:00`):
- Name (`Number of derangements of {1,2,...,n} having no adjacent 3-cycles (an adjacent 3-cycle is a cycle of the form (i,i+1,i+2)).`), offset (`0,5`), formula `a(n) = Sum_{s=0..n} Sum_{t=0..floor((n-s)/3)} (-1)^(s+t)*(n-2*t)!/(s!*t!)`, and R. J. Mathar's Jul 26 2022 conjecture (`a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + a(n-3) + (n-1)*a(n-4) + 2*a(n-6)`) match `TARGET.md` and `PROOF.md` verbatim.

## 2. Independent Exact Mechanical Checks
Command:
```sh
.venv/bin/python targets/oeis-A177259/notes/check-check-2.py
```
Output:
```
PASS (brute-force n<=8, OEIS data n<=22, Steps 1-2 series to x^34, Mathar recurrence 6<=n<=60)
```
All checks use exact integer / `fractions.Fraction` formal power series arithmetic in $\mathbb{Q}[[x]]$ (zero floating point):
- **Combinatorial definition & OEIS data:** Brute-force permutation enumeration of derangements of $\{1,\dots,n\}$ with no adjacent 3-cycles $(i,i+1,i+2)$ matches OEIS `A177259` `data` for $0 \le n \le 8$; the double-sum formula matches OEIS `data` for $0 \le n \le 22$.
- **Step 1 (OGF identity):** Inner polynomial reindexing identity verified in $\mathbb{Q}[x]$ for $0 \le k \le 20$; OGF $y(x) = \sum_{m \ge 0} m! x^m / (1+x+x^3)^{m+1}$ verified to $x^{35}$.
- **Step 2 (First-order linear ODE):** Verified $u^2 F'(u) + (u-1)F(u) + 1 = 0$, $D(x)y(x) = F(u(x))$, $u'(x) = (1-2x^3)/D(x)^2$, and $x^2(1+x+x^3)y'(x) + (-1+x^2+x^3+3x^4+2x^6)y(x) + (1-2x^3) = 0$ identically to $x^{34}$.
- **Step 3 (Recurrence):** Mathar's recurrence $a(n) = (n-1)a(n-1) + (n-1)a(n-2) + a(n-3) + (n-1)a(n-4) + 2a(n-6)$ verified against the exact double-sum definition for all $6 \le n \le 60$.

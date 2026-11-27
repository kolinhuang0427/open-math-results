# Independent Check Report: targets/oeis-A092920/

- **Checker:** `check-3`
- **Verdict:** `PASS`

## 1. Primary-Source Fidelity Check

- **Primary source checked:**
  - Live OEIS JSON API for `A092920` (revision `56`, `2026-03-14T12:38:00-04:00`, offset `0,3`).
- **Exact statement match:**
  - **Name:** `Number of strongly monotone partitions of [n].`
  - **Data (`offset 0`):** `1,1,2,4,9,22,58,164,496,1601,5502,20075,77531,315947,1354279,6087421,28611385,140239297,715116827,3785445032,20760746393,117759236340,689745339984,4165874930885,25911148634728,165775085602106,1089773992530717,7353740136527305`
  - **Comment:** `A partition is strongly monotone if its blocks can be written in increasing order of their least element and increasing order of their greatest element, simultaneously.`
  - **Formula (Conjecture):** `Conjecture: a(n) = Sum_{k=0..2^(n-1) - 1} b(k) for n > 0 with a(0) = 1 where b(2^m*(2n+1)) = Sum_{k=0..[m > 0]*(m-1)} binomial(m-1, k)*b(2^k*n) for m >= 0, n >= 0 with b(0) = 1. - _Mikhail Kurkov_, Apr 24 2023`
- **Fidelity:** `TARGET.md` and `PROOF.md` match live OEIS `A092920` rev 56 verbatim with zero quantifier, index, or convention drift (`binom(-1, 0) = 1` for `m = 0` matches `[m > 0]*(m - 1) = 0`).

## 2. Independent Mechanical & Mathematical Check

- Independently wrote `targets/oeis-A092920/notes/check-check-3.py` (strictly without reading `verify.py` or `notes/*`), verifying using exact `int` and `fractions.Fraction` formal power series arithmetic:
  1. **Section 1 & Data:** Brute-force enumeration of all strongly monotone partitions of `[n]` (`0 <= n <= 7`), explicit implementation of $\Phi$ and $\Phi^{-1}$ (FIFO queue bijection to labeled Motzkin paths $\mathcal{M}_n$), continued-fraction recurrence $B_m(x) = (1 - (m+1)x - x^2 B_{m+1}(x))^{-1}$ matching all `28` OEIS data terms (`n = 0..27`), and direct Kurkov sum $\sum_{k=0}^{2^{n-1}-1} b(k) = a(n)$ for `1 <= n <= 15`.
  2. **Sections 2 & 3:** Verified $R_j(N)$ recurrences (`0 <= N <= 8`, `0 <= j <= 9`), exact exponential-polynomial $F_N(e^z)$ differential recurrence (`0 <= N <= 12`), bivariate PDE $(k+1)((k+1)x - 1)p_{k+1} + x p_k = 0$, boundary condition $(1-x)H(x,1) - x\partial_u H(x,1) = 1$, $U_m(x)$ / $C_m(x)$ continued-fraction relation, and exact series equality $H(x, 1) = A(x)$ through degree `13`.

- **Command run:**
```bash
.venv/bin/python -u targets/oeis-A092920/notes/check-check-3.py
```

- **Raw output:**
```text
Section 1 & Data PASS: bijection (n<=7), continued fraction (n<=27), and Kurkov b(k) sum (n<=15) verified.
Sections 2 & 3 PASS: R_j(N), F_N PDE, boundary cond, U_m / C_m CF identity, and H(x,1)==A(x) verified to deg 13.
PASS
```

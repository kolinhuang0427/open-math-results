# Independent Check Report (`check-3`): `targets/oeis-A045742/`

## 1. Primary-Source Fidelity Check
Checked live OEIS JSON API (`https://oeis.org/search?q=id:A045742&fmt=json`) directly:
- **OEIS `A045742`** (rev `20`, `2022-07-26T12:51:11-04:00`, offset `2,3`):
  - **Name:** `Number of interior faces in all noncrossing connected graphs on n nodes on a circle.`
  - **Formula:** `a(n) = Sum_{k=1..n-2} k*binomial(n+k-2, k)*binomial(3*n-3, n-2-k)/(n-1).`
  - **Formula (_R. J. Mathar_, Jul 26 2022):** `Conjecture D-finite with recurrence n*(n-1)*(523*n-1993)*a(n) -6*(n-1)*(759*n^2-6019*n+12790)*a(n-1) -12*(n-2)*(4707*n^2-17937*n+6260)*a(n-2) +72*(3*n-10)*(759*n-2224)*(3*n-11)*a(n-3)=0.`
  - **Data:** `0,1,13,141,1456,14778,149031,...` (19 terms, `a(2)..a(20)`).

`TARGET.md` and `PROOF.md` match the primary OEIS statement verbatim (quantifier $n \ge 5$, offset `2`, closed-form binomial sum with $a(2)=0$, and all 4 recurrence coefficients).

## 2. Mathematical Proof Check
Reviewed `targets/oeis-A045742/PROOF.md` Steps 1–3:
- Step 1: Lagrange–Bürmann inversion for $t(x) = x(1+t(x))^3/(1-t(x))$ gives $y(x) = x t^2(1+t)/(1-4t+t^2)$, and $\mathrm{Res}_t(E_1, E_2) = 2x P(x, y)$ gives $P(x, y(x)) = 0$ in $\mathbb{Z}[[x]]$. Exact.
- Step 2: $P_y(x, y(x)) = -x + O(x^2) \ne 0$, inductive $N_k$ satisfy $P_y^{2k-1} y^{(k)} = N_k$, and exact $\mathbb{Z}[x,y]$ divisibility $Q(x,y) = P(x,y)R(x,y)$ gives the order-3 formal ODE $2544x^3 + \sum_{k=0}^3 p_k(x) y^{(k)}(x) = 0$. Exact.
- Step 3: Extracting $[x^n]$ for $n \ge 5$ ($\deg(2544x^3) = 3 < 5$, shifts $0 \le d - k \le 3$) matches Mathar's 4-term recurrence identically in $\mathbb{Z}[n]$. Exact.

## 3. Independent Mechanical Verification
Written solely from live OEIS `A045742` definitions and `PROOF.md` without reading `verify.py` or author notes, using exact `int` / SymPy `ZZ` arithmetic (zero floats):
- Script: `targets/oeis-A045742/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/oeis-A045742/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[1/4] Closed-form sum matches all 19 live OEIS A045742 terms (n=2..20).
[2/4] Step 1 series identity and 6x6 Sylvester resultant Res_t(E1,E2) = 2x P(x,y) verified.
[3/4] Step 2 exact Z[x,y] division Q = P*R and order-3 ODE verified.
[4/4] Step 3 symbolic Z[n] coefficient match and recurrence verified for 5 <= n <= 150.
PASS
```

## 4. Verdict
- **PASS** (awaiting Gate 2 novelty receipts from `@watch-1`/`@watch-5`/`@watch-6` per `#386`).

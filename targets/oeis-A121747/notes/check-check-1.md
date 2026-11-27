# Check Report: `targets/oeis-A121747/`

- **Checker:** `@check-1`
- **Verdict:** **PASS**
- **Primary Source:** OEIS **A121747** (`https://oeis.org/search?q=id:A121747&fmt=text`, rev. 15, offset `1,2`)
- **Verifier Script:** `targets/oeis-A121747/notes/check-check-1.py` (SymPy exact polynomials + pure `int`/`Fraction`, zero floats)

## 1. Primary Source Fidelity
- `TARGET.md` matches the live OEIS **A121747** `%N`, `%F`, and `%O` fields verbatim (`a(1)=1`, `d(n)`, recurrence for $n \ge 2$, and R. J. Mathar's Jul 26 2022 conjectured 5th-order recurrence for $n \ge 6$).

## 2. Independent Exact-Arithmetic Verification
Ran `.venv/bin/python targets/oeis-A121747/notes/check-check-1.py` (exit code 0, `PASS`):
- **Sequence & OEIS `%S/%T` match:** `a(1..16)` matches OEIS `[1, 2, 8, 44, 262, 1938, 15600, 145086, 1461888, 16438446, 198598860, 2623055166, 36933441912, 560697617214, 9014444990964, 154698782105070]`.
- **Direct check:** $M(n) = 0$ verified directly for all $6 \le n \le 60$.
- **Step 1:** Verified $W(k) = D(k) + D(k-1)$ and its even/odd closed forms for all $3 \le k \le 60$.
- **Step 2:** Verified $M(n) = \sum_{i=0}^3 c_i(n) W(n-i)$ identically in $\mathbb{Z}[n]$.
- **Step 3:** Verified $P_{\mathrm{even}}(r) \equiv 0$ and $P_{\mathrm{odd}}(r) \equiv 0$ identically in $\mathbb{Z}[r]$ (and at $n=6, r=3$ all factorials $(2r-5)!=1!=1$ and factors $2r-5,\dots,2r-2 \ge 1$ are positive, so $M(6) = 1!\,P_{\mathrm{even}}(3) = 0$ holds with no zero factor).
- **Step 4:** Verified $n=5$ boundary sum $= 0$ and exact homogeneous order-6 polynomial-coefficient ODE for $\hat{y}(x)$ with leading coefficient $-9x(x-1)^2(x+1) \neq 0$ annihilating $\hat{y}$ through $x^{39}$.

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.

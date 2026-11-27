# Check Report: `targets/oeis-A121754/`

- **Checker:** `@check-1`
- **Verdict:** **PASS**
- **Primary Source:** OEIS **A121754** (`https://oeis.org/search?q=id:A121754&fmt=text`, rev. 4, offset `1,3`)
- **Verifier Script:** `targets/oeis-A121754/notes/check-check-1.py` (SymPy exact rational polynomials + pure `int`/`Fraction`, zero floats)

## 1. Primary Source Fidelity
- `TARGET.md` matches the live OEIS **A121754** `%N`, `%F`, and `%O` fields verbatim (`a(1)=0, a(2)=1`, recurrence for $n \ge 3$, and R. J. Mathar's Jul 26 2022 conjectured 5th-order recurrence for $n \ge 6$).

## 2. Independent Exact-Arithmetic Verification
Ran `.venv/bin/python targets/oeis-A121754/notes/check-check-1.py` (exit code 0, `PASS`):
- **Sequence & OEIS `%S/%T` match:** `a(1..16)` matches OEIS `[0, 1, 6, 31, 211, 1530, 13086, 120888, 1260792, 14140080, 174692880, 2304970560, 32969263680, 500368821120, 8139251433600, 139686867532800]`.
- **Direct check:** $M(n) = 0$ verified directly for all $6 \le n \le 60$.
- **Step 1:** Verified $D(k) - (k-3)D(k-1) = (k-2)!f(k)$ and $D(k) = (k-3)!S(k)$ for $3 \le k \le 60$, plus exact symbolic induction in $\mathbb{Z}[r]$ for $S(2r) = (r-1)^2(4r-1)$ and $S(2r+1) = r^2(4r-1)$.
- **Step 2:** Verified $M(n) = \sum_{i=0}^4 e_i(n) D(n-i)$ identically in $\mathbb{Z}[n]$.
- **Step 3:** Verified $e_4(6) = 0$, $P_{\mathrm{even}}(r) \equiv 0$, and $P_{\mathrm{odd}}(r) \equiv 0$ identically in $\mathbb{Z}[r]$, plus exact verification of the resulting order-6 polynomial-coefficient ODE for $\hat{y}(x) = \sum_{n \ge 1} a(n) x^n/n!$ (leading $\hat{y}^{(6)}$ coefficient $16 x^6 (x-1)^2 (x+1) \neq 0$) on Taylor coefficients $x^6..x^{35}$.

## 3. Gate 2 Novelty
- Gate 2 PASS receipts present: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md`.

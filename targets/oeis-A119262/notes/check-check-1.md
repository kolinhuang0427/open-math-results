# Check Report: `targets/oeis-A119262/`

- **Checker:** `@check-1`
- **Verdict:** **PASS**
- **Primary Source:** OEIS **A119262** (`https://oeis.org/search?q=id:A119262&fmt=text`, rev. 55, offset `0,5`)
- **Verifier Script:** `targets/oeis-A119262/notes/check-check-1.py` (exact `int` and `sympy.Matrix.det()`, zero floats)

## 1. Primary Source Fidelity
- `TARGET.md` matches the live OEIS **A119262** `%N` ($a(0)=0, a(1)=1$, recurrence for $n \ge 2$) and `%F` (Benedict W. J. Irwin, Apr 19 2017 determinant conjecture for $M_n$ and $a(n+1) = \det(M_n)$) verbatim.

## 2. Independent Exact-Arithmetic Verification
Ran `.venv/bin/python targets/oeis-A119262/notes/check-check-1.py` (exit code 0, `PASS`):
- **Sequence match:** $a(0..28)$ matches OEIS `%S/%T` identically (`[0, 1, 1, 1, 2, 3, 5, 8, 14, 25, 46, 85, ...]`).
- **Step 1 (Index reversal):** Verified $P_n M_n P_n^{-1} = B_n$ and the leading principal submatrix property $B_{n-1} = (B_n)_{0..n-2, 0..n-2}$ for all $1 \le n \le 20$.
- **Step 2 (Laplace expansion & minors):** Verified $\det(B_n^{(r, n-1)}) = (-1)^{n-1-r} d_r$ for all $1 \le n \le 12$ and $0 \le r \le n-1$, and $\det(M_n) = \sum_{r=0}^{n-1}\binom{n-1-r}{r}d_r$ for $1 \le n \le 20$.
- **Step 3:** Verified $\det(M_n) = a(n+1)$ for all $1 \le n \le 20$.

## 3. Gate 2 Novelty
- `novelty-gate2-watch-6.md` present (PASS); `@watch-1` and `@watch-5` receipts pending per `#726`.

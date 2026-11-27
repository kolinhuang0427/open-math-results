# Checker Report: `targets/oeis-A178072/` (`check-check-3`)

## Primary Source & Verbatim Statement Verification

- **Live OEIS fetched:** `2026-11-27` via `https://oeis.org/search?q=id:A178072&fmt=json`:
  - `A178072` (`rev. 35`, offset `0,8`): `NAME`, `DATA` (34 terms), Somos's algebraic equation `(2*x + x^3) * A(x)^2 - (1 + x)^2 * A(x) + 1 = 0`, closed-form g.f., double binomial sum formula, and Mathar's Jun 14 2016 7-term recurrence conjecture match `TARGET.md` verbatim.

## Proof Audit (`PROOF.md`)

- **§1 First-order ODE:** Completing the square gives `(R - 2PA)^2 = Delta = 1 - 4x + 6x^2 + x^4`, and uniqueness of the square root `y = R - 2PA` with `y(0) = 1` produces `A_1 A' + A_0 A = R_1` cleanly.
- **§2 Second-order ODE & coefficient extraction:** Applying `L = x(1 + 5x) d/dx + 4x` annihilates `[x^n] R_2(x)` for all `n >= 6` (`deg R_2 = 5`), and exact symbolic expansion of `P_2, P_1, P_0` gives Mathar's 8 quadratic polynomials `c_0(n)..c_7(n)` identically (with `c_7(6) = 0` covering `n = 6` as well as all `n >= 7`).

## Independent Exact Verification (`notes/check-check-3.py`)

Zero-float (`FLOAT_COUNT: 0` via AST check) independent verifier run after final edit:

```text
[1/3] Generating A178072(0..60) from algebraic equation and checking OEIS data...
      Matched all 34 live terms, algebraic equation to x^60, and binomial sum (n<=25).
[2/3] Symbolically verifying Section 1 & Section 2 ODE derivations and polynomials...
      All symbolic ODEs and coefficient polynomials c_0..c_7 match identically.
[3/3] Checking Mathar's 7-term recurrence numerically for n = 6..60...
      Recurrence holds identically for all n = 6..60.
PASS
FLOAT_COUNT: 0
```

## Verdict

**PASS** (blind check complete; Gate 2 novelty pending `@watch-1`/`@watch-5`/`@watch-6`).

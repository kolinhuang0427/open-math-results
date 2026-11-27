# Checker Report: `targets/oeis-A157003/` (`check-check-3`)

## Primary Source & Verbatim Statement Verification

- **Live OEIS fetched:** `2026-11-27` via `https://oeis.org/search?q=id:A157003&fmt=json`:
  - `A157003` (`rev. 37`, offset `0,3`): `NAME`, `DATA` (28 terms), Catalan g.f. `c(x*(1-x^2))`, alternating binomial sum, Kotesovec's 4-term recurrence, and Mathar's Nov 19 2014 6-term recurrence conjecture match `TARGET.md` verbatim.

## Proof Audit (`PROOF.md`)

- **§1 First-order ODE:** Substituting `P(x) = x(1 - x^2)` into `P A^2 - A + 1 = 0` and setting `y = 1 - 2PA = sqrt(Delta)` (`Delta = 1 - 4x + 4x^3`) produces `x(1 - 4x - x^2 + 8x^3 - 4x^5) A'(x) + (1 - 2x - 3x^2 + 8x^3 - 6x^5) A(x) = 1 - 3x^2` cleanly.
- **§2 Coefficient extraction & Mathar's recurrence:** Extracting `[x^n]` for `n >= 3` yields `K(n) = 0` (covering Kotesovec's recurrence for `n >= 5` plus `n = 3, 4`), and `K(n) + 5*K(n-1) = 0` yields Mathar's exact 6-term recurrence for all `n >= 6` (as well as `n = 5` with `a(-1) = 0`).

## Independent Exact Verification (`notes/check-check-3.py`)

Zero-float (`FLOAT_COUNT: 0` via AST check) independent verifier run after final edit:

```text
[1/3] Generating A157003(0..60) from quadratic relation and checking OEIS data...
      Matched all 28 live terms and binomial Catalan formula (n<=45).
[2/3] Symbolically verifying Section 1 ODE and Section 2 K(n) + 5*K(n-1)...
      Symbolic ODE, K(n), and K(n) + 5*K(n-1) match identically.
[3/3] Checking K(n) (n>=3) and Mathar's 6-term recurrence (n>=5) up to n = 60...
      Both recurrences hold identically up to n = 60.
PASS
FLOAT_COUNT: 0
```

## Verdict

**PASS** (`Gate 2` cleared by `@watch-1` `#1218` and `@watch-5` `#1220`).

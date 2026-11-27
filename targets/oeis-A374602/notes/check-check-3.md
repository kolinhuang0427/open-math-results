# Checker Report: `targets/oeis-A374602/` (`check-check-3`)

## Primary Source & Verbatim Statement Verification

- **Live OEIS fetched:** `2026-11-27` via `https://oeis.org/search?q=id:<AID>&fmt=json`:
  - `A374602` (`rev. 31`): `NAME`, `DATA` (55 antidiagonal terms), `COMMENT`, and `FORMULA` match `TARGET.md` verbatim (every quantifier, hypothesis `d >= 2` nonsquare, `b >= 1`, `1 <= c < d`).
  - `A377290` (`rev. 7`, all 67 published terms): `NAME` and `COMMENT` match `TARGET.md` verbatim. *(Minor metadata note: `TARGET.md` L3 writes `A377290 (rev. 11)` whereas live OEIS JSON currently serves `rev. 7`; text and terms match verbatim.)*
  - `A377291` (`rev. 7`, all 46 published terms): `NAME`, `COMMENT`, and `FORMULA` match `PROOF.md` and `TARGET.md`.

## Proof Audit (`PROOF.md`)

Checked all lemmas, propositions, theorems, and the Section 4 algorithm directly against exact arithmetic:
- **§1 Lemma 1 & Lemma 2:** Bijection `(t, b, c) <-> (db + c, t) in S_d^+`, uniqueness of `(b, c)`, and exact threshold `(X, Y) in S_d^+ <=> X + Y*sqrt(d) > 2d` (`z = 2d` impossible) hold unconditionally for all nonsquare `d >= 2`.
- **§2 Lemma 3 & Proposition 4:** Congruence `X == Y (mod 2)` when `d == 1 (mod 4)`, existence of `r in {1, 2}` with `A_r >= 3`, and `T_gamma` bijectivity preserving `S_d`, `c = X mod d`, and `{Y >= 1}` hold as stated (including subtle cases like `d = 44`, where `A = 20, B = 3` is excluded from `Z[sqrt(44)]` since `2 nmid B`, forcing `eps_0 = 199 + 30*sqrt(44)` and `A_2 = 158402 = A377291(38)`).
- **§3 Theorem 5 & Proposition 6:** Monotonicity `Y_1 < Y_2 => X_1 < X_2 => z_1 < z_2 => Y_1' < Y_2'` gives strict global periodicity from `k = 1` with zero exceptions and the exact order-2 recurrence `T(n, (m+2)p+j) = A_r T(n, (m+1)p+j) - T(n, mp+j)`; minimality of `p = |W_0|` and `g(n) = gamma` holds via quadratic-integer norm/congruence reduction.
- **§4 Finite-Time PQa Algorithm:** Termination and completeness via Legendre's theorem and `M_per` transfer matrix hold cleanly (`Q_{k+1} = (-1)^k = 1` on every periodic match).

## Independent Exact Verification (`notes/check-check-3.py`)

Zero-float (`FLOAT_COUNT: 0` via AST check) independent verifier run after final edit:

```text
[1/3] Verifying A377290 (67 rows) and A377291 (46 rows) via PQa algorithm...
      Matched all 67 terms of A377290 and 46 terms of A377291.
[2/3] Exhaustive brute-force check & multi-period recurrence across rows...
      Verified brute-force completeness + recurrence across 16 rows (up to d=44).
[3/3] Verifying live OEIS A374602 antidiagonal array (55 terms)...
      Matched all 55 antidiagonal terms of A374602.
PASS
FLOAT_COUNT: 0
```

## Verdict

**PASS** (`Gate 2` cleared by `@watch-5` `#999`, `@watch-6` `#998`, `@watch-1` `#1019`).

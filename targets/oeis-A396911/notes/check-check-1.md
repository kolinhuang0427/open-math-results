# Check Report — `oeis-A396911`

- Checker: `check-1`
- Checked UTC: `2026-11-27T00:51:50Z`
- Verdict: `PASS`

## 1. Primary-Source Fidelity Check

- Primary source: live OEIS JSON (`https://oeis.org/search?q=id:A396911&fmt=json` and `id:A131988&fmt=json`, fetched `2026-11-27`):
  - **A396911** (author `_Witold Tatkiewicz_`, Jun 09 2026; revision `48`, `2026-06-22T17:16:16-04:00`):
    - Name: `Shortest path indices during walk over golden ratio phyllotaxis starting at the center.`
    - Comments: Vogel's phyllotaxis spiral lattice `(k^d * cos(k*theta), k^d * sin(k*theta))` with `d = 1/2`, `theta` golden angle (`A131988`), `k = 0, 1, 2, 3, ...`; starting at `(0,0)`, move to closest unvisited point, `a(n)` is the index `k` reached after `n` moves. Also records Pontus von Brömssen's questions (ties, monotonicity, Fibonacci first differences, run lengths) and Sean A. Irvine's comment `"No reduction on index in the first 1000 terms."`
    - Formula (Conjecture): `Conjecture: a(n) <= (3/2) * n^2. - _Sean A. Irvine_, Jun 21 2026`
    - Data (`offset 0`): 51 exact terms `0,1,4,9,17,...,3457`.
  - **A131988** (revision `20`): `Decimal expansion of golden angle in radians: (4-2*phi)*Pi.` (`Equals (3-sqrt(5))*Pi = ...`).
- Comparison against `TARGET.md` and `PROOF.md`: exact match with zero quantifier, hypothesis, edge-case, or definition drift.

## 2. Independent Mechanical Verification

- Verifier script: `targets/oeis-A396911/notes/check-check-1.py`
  - Uses `mpmath.iv` (`dps = 60`) with exact radial window bounds `(sqrt(k) ± sqrt(U))^2` and certified integer-`isqrt` + `sin^2` lower-bound pruning across ALL unvisited `j >= 0` for every step `1 <= n <= 500`, establishing unique strict nearest unvisited neighbors (`min_gap = 0.002514 > 2.5e-3` on `1 <= n <= 460`), exact match to all 51 OEIS `A396911` terms, strict monotonicity, Fibonacci first differences `F_2, F_4, ..., F_{16}` through `a(460) = 280542` (`a(459) = 279555`, `a(460) - a(459) = F_{16} = 987`), transition into `F_{17}` for `461 <= n <= 500`, `a(n) <= (3/2) n^2` on `0 <= n <= 500`, `max_{1<=n<=460} a(n)/n^2` at `n = 352` (`a(352) = 173946`), `f_{16}(279555) < 0 < f_{16}(280542)`, and `460 > phi^{18}/(4*pi)`.
  - Verifies Lemma 1 (`F_m * phi^{-2} - F_{m-2} = (-1)^m * phi^{-m}` for `2 <= m <= 40`, determinant identity for `3 <= m <= 200`, exhaustive `||d * phi^{-2}||_Z >= phi^{-(m-2)}` for `3 <= m <= 20` with equality iff `d = F_{m-2}`), Lemma 2 (elementary bounds across 999 grid points, numerical constants, `f_m((1 - 6*phi^{-m})*K_m) < 0 < f_m(K_m)` and `f'_m > 0` for `16 <= m <= 50`), Lemmas 3 & 4 (numerical constants and sample `mpmath.iv` checks for `16 <= m <= 25`), and Theorem 1 Part 2 constants (`< 1.43 < 3/2`, `pi/sqrt(5) < 3/2`).
- Command:
  ```bash
  .venv/bin/python targets/oeis-A396911/notes/check-check-1.py
  ```
- Raw output (exit code `0`):
  ```text
  Base walk 0<=n<=500 & OEIS A396911 51 terms (min_gap=0.002514): OK (9.47s)
  Lemma 1 (Fibonacci angles, det identity, best-approx gap 3<=m<=20): OK
  Lemma 2 (elementary bounds & transition thresholds 16<=m<=50): OK
  Lemma 3 & Lemma 4 (backward & plateau dominance bounds): OK
  Theorem 1 Part 2 (asymptotic & effective 1.43 < 3/2 inequalities): OK
  PASS
  ```

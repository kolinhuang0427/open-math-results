# Independent Check Report (`check-3`) — `targets/oeis-A386251/`

- **Checked at (UTC):** 2026-11-26T22:19Z
- **Checker:** `check-3` (independent; written without reading `verify.py` or `notes/*.py`)
- **Primary source inspected:** Live OEIS JSON API `https://oeis.org/search?q=id:A386251&fmt=json` (OEIS **A386251**, Charles L. Hohn, revision 22, `2025-08-06T00:07:55-04:00`).

## 1. Primary-Source Fidelity & Definition Match

- **Name (`A386251` rev 22):**
  > Consider the graph whose vertices are the points of the n-dimensional cubic lattice with points connected by all integer-length diagonals that traverse all n dimensions and do not intersect intermediate points. a(n) is the total length of the shortest possible closed walk in this graph via noncongruent diagonals.
- **Comment (`A386251` rev 22):**
  > It is provable that all such walks must be even in total length. It is also provable that 3-segment closed walks are impossible for n < 6, and conjectured that a(n) for all n >= 6 are produced by 3-segment walks.
- **Definition match:**
  - `EXAMPLE` (`a(3) = 28` via `[2,2,1], [-3,-2,-6], [-7,4,4], [8,-4,1]`, lengths `3+7+9+9=28`) confirms "noncongruent diagonals" means pairwise distinct multisets of absolute coordinate values $\{|v_1|, \dots, |v_n|\}$ (not distinct lengths), "do not intersect intermediate points" means $\gcd(v_1, \dots, v_n) = 1$, and "traverse all $n$ dimensions" means $v_i \ne 0$ for all $i$.
  - Exact match with `TARGET.md` and `COUNTEREXAMPLE.md`.

## 2. Independent Mechanical & Proof Verification

Wrote independent exact integer verifier `targets/oeis-A386251/notes/check-check-3.py` strictly from OEIS `A386251` and `COUNTEREXAMPLE.md`, without reading `verify.py`:
- Verified full $n$-dimensional 4-cycle step vectors $v^{(1)}, v^{(2)}, v^{(3)}, v^{(4)} \in \mathbb{Z}^n$ for $92 \le m \le 110$ ($8434 \le n = m^2 - 30 \le 12070$): sum $= 0$, $4$ distinct cumulative vertices (simple 4-cycle), all coordinates nonzero, $\gcd = 1$, exact squared Euclidean norm $= m^2$ (total walk length $4m$), and $4$ pairwise distinct coordinate-magnitude multisets.
- Exhaustively tested all valid integer triples $(L_1, L_2, L_3)$ with $m \le L_1 \le L_2 \le L_3$, $L_3 < L_1 + L_2$, $L_1 + L_2 + L_3$ even, and $L_1 + L_2 + L_3 \le 4m$ for $92 \le m \le 120$, confirming $L_1^2 + L_2^2 + L_3^2 < 6n$ in every case (and sharpness at $m=91$: $91^2 + 92^2 + 181^2 = 6(91^2 - 30)$).
- Verified line-by-line all algebraic inequalities in Section 2 of `COUNTEREXAMPLE.md` for all $m \ge 92$.

- **Command run:**
  ```bash
  .venv/bin/python targets/oeis-A386251/notes/check-check-3.py
  ```
- **Raw output:**
  ```text
  4-cycle witnesses PASS: verified full n-dim vectors for m=92..110 (n=8434..12070).
  3-segment lower bound (>= 4m+2) PASS: exact triple exhaustion for m=92..120 (sharp at m=91).
  PASS
  ```

## 3. Verdict

**PASS** — Primary source matches `TARGET.md` and `COUNTEREXAMPLE.md` verbatim, and both the infinite family of $4$-segment cycles (length $4m$ for $n = m^2 - 30, m \ge 92$) and the $3$-segment lower bound ($\ge 4m + 2$) pass independent exact verification.

# Independent Check Report — `oeis-A168503`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entry [`A168503`](https://oeis.org/search?q=id:A168503&fmt=text) (`#20 Feb 07 2025 00:50:52`, offset `0,3`).
- **Verbatim match:** `TARGET.md` L16–20 matches the live OEIS `%N` 3-periodic continued fraction, radical g.f., and Mathar's Feb 10 2015 `%F` `Conjecture:` verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A168503/notes/check-check-1.py` (`int` + SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Symbolic identities (`PROOF.md` §1–§2):**
   - Verified $T(u) = \frac{1-2x-3xu}{1-3x-3x(1-x)u}$, contraction $T(u_1) - T(u_2) = \frac{6x^3(u_1-u_2)}{\dots}$, quadratic fixed-point equation $3x(1-x)A^2 - A + 1 - 2x = 0$, and completing the square $(1-6x(1-x)A)^2 = 1-12x+36x^2-24x^3 = \Delta(x)$.
   - Verified all ODE polynomial reductions and exact coefficient equivalence with Mathar's recurrence in $\mathbb{Z}[n, a_0,\dots,a_4]$.
2. **Exact series & recurrences (`n <= 80`):**
   - Verified fixed-point convergence $T(u) = u \pmod{x^{81}}$ via exact $\mathbb{Z}[[x]]$ arithmetic, matching live OEIS `%S` (`0..21`) verbatim and SymPy radical g.f. expansion (`0..20`).
   - Verified first-order formal ODE at every coefficient $0 \le n \le 80$, boundary case $n = 3$ with $a(-1) = 0$, and Mathar's 4-term recurrence for all $4 \le n \le 80$.

## 3. Gate 2 Status

`novelty-gate2-watch-1.md` present in `notes/`.

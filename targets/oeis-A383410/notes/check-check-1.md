# Independent Check Report — `oeis-A383410`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entries [`A383410`](https://oeis.org/search?q=id:A383410&fmt=text) (`#6 May 03 2025 19:02:22`) and [`A005649`](https://oeis.org/search?q=id:A005649&fmt=text) (`#123 Nov 26 2025 15:59:33`).
- **Verbatim match:** `TARGET.md` L14–19 matches `A383410` `%N`, Kurkov's `%F` `Conjecture: A(n,0) = A005649(n).`, and `A005649` `%N` verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A383410/notes/check-check-1.py` (`int` + SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Symbolic PDE (`PROOF.md` §1–§3):** Verified $\widetilde{U}(0, y) = e^{2y}$, $\partial_x \widetilde{U} = e^{x+y}\partial_y \widetilde{U}$, and $F(x, 0) = (2 - e^x)^{-2}$ identically.
2. **Array, EGF, and OEIS `%S`:**
   - Computed $A(n, k)$ directly from the defining recurrence ($0 \le n + k \le 20$): matches all `55` live OEIS `A383410` `%S` antidiagonal terms (`n+k = 0..9`) verbatim.
   - Computed $[x^n/n!](2 - e^x)^{-2}$ (`0 <= n <= 20`): matches all `20` live OEIS `A005649` `%S` terms (`0..19`) and equals $A(n, 0)$ for every $0 \le n \le 20$.
   - Verified bivariate EGF $F(x, y) = e^{-y}(1 + e^{-y} - e^x)^{-2}$ identically up to total degree $10$.

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md` (`PASS`).

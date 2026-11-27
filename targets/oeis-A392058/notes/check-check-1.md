# Independent Check Report — `oeis-A392058`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entries [`A392058`](https://oeis.org/search?q=id:A392058&fmt=text) (`#6 Jan 04 2026 20:28:11`) and [`A233335`](https://oeis.org/search?q=id:A233335&fmt=text) (`#20 Jun 18 2026 10:15:54`).
- **Verbatim match:** `TARGET.md` L14–19 matches `A392058` `%N`, Kurkov's `%F` `Conjecture: A(n,0) = A233335(n+1).`, and `A233335` `%N` (`E.g.f. A(x) satisfies A( Integral 1/A(x) dx ) = exp(x).`) verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A392058/notes/check-check-1.py` (`int` + SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Array, functional equation, and OEIS `%S`:**
   - Computed $A(n, k)$ directly from the defining recurrence ($0 \le n + k \le 22$): matches all `45` live OEIS `A392058` `%S` antidiagonal terms (`n+k = 0..8`) verbatim.
   - Solved $E(\int_0^x dt/E(t)) = e^x$ ($E(0) = 1$) uniquely term-by-term (`0 <= m <= 22`): matches all `22` live OEIS `A233335` `%S` terms (`0..21`) verbatim and satisfies $A(n, 0) = \mathrm{A233335}(n+1)$ for all $0 \le n \le 21$.
2. **Transport PDE & Characteristics (`PROOF.md` §1–§3):**
   - Verified $H_n(y) = \partial_y(V(y)H_{n-1}(y))$ (`1 <= n <= 9`) and $\partial_x W = V(y)\partial_y W$ identically up to total degree $9$.
   - Verified $V(\Phi(u)) = e^u$ identically modulo $u^{22}$.

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md` (`PASS`).

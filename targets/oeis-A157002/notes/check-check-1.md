# Independent Check Report — `oeis-A157002`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entry [`A157002`](https://oeis.org/search?q=id:A157002&fmt=text) (`#15 Sep 22 2025 16:00:57`, offset `0,4`).
- **Verbatim match:** `TARGET.md` L16–23 matches live OEIS `%N`, `%F` (g.f., explicit Catalan-binomial sum, and Mathar's Nov 19 2014 `Conjecture:`), and `%C` (Riordan array `(1-x, x(1-x^2))` image of Catalan numbers `A000108`) verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A157002/notes/check-check-1.py` (`int` + SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Symbolic identities (`PROOF.md` §1–§2):**
   - Verified completing the square $4P(PA^2 - A + 1 - x) = (1 - 2PA)^2 - (1 - 4x + 4x^3)$ ($P = x(1+x)$, $\Delta = 1 - 4x + 4x^3$) identically in $\mathbb{Z}[x, A]$.
   - Verified ODE reductions $\Delta P = x - 3x^2 - 4x^3 + 4x^4 + 4x^5$, $\Delta P' - \frac{1}{2}\Delta' P = 1 - 6x^2 - 2x^3 + 2x^4$, $-\frac{1}{4}\Delta' = 1 - 3x^2$, and exact coefficient extraction equivalence with Mathar's recurrence in $\mathbb{Z}[n, a_0,\dots,a_4]$.
2. **Exact series & recurrences (`n <= 80`):**
   - Verified Riordan series $(1-x)\,c(x(1-x^2))$ matches OEIS explicit formula $\sum_{k=0}^n (-1)^{\lfloor (n-k+1)/2 \rfloor}\binom{k}{\lfloor (n-k)/2 \rfloor}C_k$ identically for $0 \le n \le 80$, matches live OEIS `%S` (`0..27`) verbatim, and matches SymPy radical expansion (`0..20`).
   - Verified first-order formal ODE at every coefficient $0 \le n \le 80$, boundary case $n = 3$ with $a(-1) = 0$, and Mathar's 4-term recurrence for all $4 \le n \le 80$.

## 3. Gate 2 Status

Pending (`gate1-novelty.md` present; pinging `@watch-1` at handoff).

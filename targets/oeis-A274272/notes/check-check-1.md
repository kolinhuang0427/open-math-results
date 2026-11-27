# Independent Check Report — `oeis-A274272`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entry [`A274272`](https://oeis.org/search?q=id:A274272&fmt=text) (`#12 Jun 23 2016 10:05:23`, offset `0,2`).
- **Verbatim match:** `TARGET.md` L14–22 matches the live OEIS `%N`, `%F` (`Coefficient of x^(5^n) in 1/((1-x)*(1-x^2)*(1-x^3)*(1-x^4)).`), and Colin Barker's Jun 17 2016 `Conjectures (Start)`–`(End)` block verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A274272/notes/check-check-1.py` (`int` + SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Symbolic identities (`PROOF.md` §1–§3):**
   - Verified partial fraction decomposition of $F(x) = \frac{1}{(1-x)(1-x^2)(1-x^3)(1-x^4)}$ and the cleared-denominator polynomial identity (`= 288`).
   - Verified symbolic pole extraction polynomials in $m$ at $x = 1$ and $x = -1$ (odd $m$), and $\frac{1+x}{9(1+x+x^2)} = \frac{1-x^2}{9(1-x^3)}$.
   - Verified the rational g.f. $G(x)$ from the 5 geometric series, expanded denominator $D(x) = (1-x)(1+x)(1-5x)(1-25x)(1-125x)$, and numerator $1 - 149x + 3129x^2 - 5655x^3 - 6750x^4$ identically in $\mathbb{Q}(x)$.
2. **Partitions, OEIS `%S`, g.f., and recurrence:**
   - Verified direct enumeration of partitions of $m$ into $\le 4$ parts at $m = 1, 5, 25$ and exact integer DP at $5^0..5^4$ (`625`) match the closed form $(57 + 8(-1)^n + 63\cdot 5^n + 3\cdot 5^{1+2n} + 125^n)/144$.
   - Verified closed form matches all `15` live OEIS `%S` terms (`a(0..14)`), formal power series $D(x)G(x) = N(x)$ (`0..60`), and Barker's order-5 recurrence (`5..60`).

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md` (`PASS`).

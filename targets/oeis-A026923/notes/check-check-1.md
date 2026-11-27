# Independent Check Report — `oeis-A026923`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entry [`A026923`](https://oeis.org/search?q=id:A026923&fmt=text) (`#27 Feb 27 2026 15:18:34`, offset `1,7`).
- **Verbatim match:** `TARGET.md` L17–23 matches the live OEIS `%N` description and Colin Barker's Sep 01 2019 `Conjectures` G.f. and recurrence verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A026923/notes/check-check-1.py` (`int` + SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Symbolic identities (`PROOF.md` §1–§3):**
   - Verified odd parity projection $(F(x, 1) - F(x, -1))/2 = \frac{x^3(1 - x + x^2 + x^4)}{D(x)}$, all intermediate expansions, factored $D(x) = (1-x)(1-x^6)(1-x^4)$, and expanded $D(x) = 1 - x - x^4 + x^5 - x^6 + x^7 + x^{10} - x^{11}$ identically in $\mathbb{Q}(x)$.
2. **Partitions, OEIS `%S`, bijection, and 11-term recurrence (`n <= 120`):**
   - Directly counted partitions of $n$ into an odd number of parts with max part $3$ for $1 \le n \le 120$: matches all `55` live OEIS `%S` terms (`a(1..55)`) verbatim.
   - Verified the alternate OEIS bijection $a(n+5) =$ partitions of $n+2$ into an even number of parts $\le 3$ for $1 \le n \le 115$.
   - Verified $D(x)A(x) = x^3 - x^4 + x^5 + x^7 \pmod{x^{121}}$ and the 11-term recurrence for all $8 \le n \le 120$.

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-6.md` (`PASS`).

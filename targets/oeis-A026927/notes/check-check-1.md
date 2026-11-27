# Independent Check Report — `oeis-A026927`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entry [`A026927`](https://oeis.org/search?q=id:A026927&fmt=text) (`#23 Feb 27 2026 15:22:32`, offset `1,6`).
- **Verbatim match:** `TARGET.md` L17–23 matches the live OEIS `%N` description and Colin Barker's Sep 01 2019 `Conjectures` G.f. and recurrence verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python -u targets/oeis-A026927/notes/check-check-1.py` (`int` + SymPy, `AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Symbolic identities (`PROOF.md` §1–§3):**
   - Verified even parity projection $(F(x, 1) + F(x, -1))/2 = \frac{x^4(1 + x^2 - x^3 + x^4)}{D(x)}$, all intermediate expansions, factored $D(x) = (1-x)(1-x^6)(1-x^4)$, and expanded $D(x) = 1 - x - x^4 + x^5 - x^6 + x^7 + x^{10} - x^{11}$ identically in $\mathbb{Q}(x)$.
2. **Partitions, OEIS `%S`, bijection, and 11-term recurrence (`n <= 120`):**
   - Directly counted partitions of $n$ into an even number of parts with max part $3$ for $1 \le n \le 120$: matches all `52` live OEIS `%S` terms (`a(1..52)`) verbatim.
   - Verified the alternate OEIS bijection $a(n+5) =$ partitions of $n+2$ into an odd number of parts $\le 3$ for $1 \le n \le 115$.
   - Verified $D(x)A(x) = x^4 + x^6 - x^7 + x^8 \pmod{x^{121}}$ and the 11-term recurrence for all $9 \le n \le 120$.

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-6.md` (`PASS`).

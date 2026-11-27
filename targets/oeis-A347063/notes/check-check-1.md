# Independent Check Report — `oeis-A347063`

- **Checker:** `check-1`
- **Verdict:** **PASS**

## 1. Primary Source Verification

- **Source:** Live OEIS entry [`A347063`](https://oeis.org/search?q=id:A347063&fmt=text) (`#51 Jul 24 2026 17:37:53`) and b-file `b347063.txt` (`a(1)..a(10000)`, max term `45258`).
- **Verbatim match:** `TARGET.md` L14 and L17 match the live OEIS `%N` definition (`Double Zumkeller numbers: numbers whose set of divisors can be partitioned into two disjoint subsets with equal sums and equal cardinalities.`) and Ianakiev's `%C` conjecture (`It seems that for k>=1 all numbers of the form 18k+12 are terms. Verified for k in [1, 45]. - _Ivan N. Ianakiev_, Oct 01 2024`) verbatim.

## 2. Mechanical Verification (`notes/check-check-1.py`)

Executed `.venv/bin/python targets/oeis-A347063/notes/check-check-1.py` using pure integer arithmetic (`AST_FLOATS: []`, `FLOAT_CALLS: []`, exit code `0`):

1. **Base-$p$ forcing & parity lemmas (`COUNTEREXAMPLE.md` §1):**
   - Exhaustively enumerated all $2^6 = 64$ subsets of $D_0 = \{1, 2, 3, 4, 6, 12\}$ (`|D_0| = 6`, `sum = 28`): the only subsets summing to `14` are `(2, 12)` and `(1, 3, 4, 6)`, both of even size, forcing $|A| \equiv 0 \pmod 2 \ne 9$.
   - Verified $12p^2 = 18k + 12$ with $k = 2(p^2-1)/3 \ge 192$ and all base-$p$ digit-forcing inequalities across all `297` primes $p \in [17, 2000]$, plus direct integer DP checks for $p \in \{17, 19, 23, 29, 31\}$.
2. **Minimality of $k = 192$ ($n = 3468$) & live OEIS b-file cross-check (`COUNTEREXAMPLE.md` §2):**
   - Standalone `notes/check-check-1.py` runs purely offline with exact integer bitmask DP to construct valid equal-sum, equal-cardinality divisor partitions for every $n = 18k + 12$ ($1 \le k \le 191$) and enumerates all $\binom{18}{9} = 48620$ nine-element subsets of $D(3468)$ (`0` subsets summing to $\sigma(3468)/2 = 4298$, cross-checked by DP).
   - Separately verified against live OEIS `b347063.txt` (`a(1)..a(10000)`, `max = 45258`): all `191` terms $18k + 12$ ($1 \le k \le 191$) appear in `b347063.txt`, and `3468` is absent.

## 3. Gate 2 Status

Gate 2 receipts already present in `notes/`: `novelty-gate2-watch-1.md`, `novelty-gate2-watch-5.md`, `novelty-gate2-watch-6.md` (`PASS`).

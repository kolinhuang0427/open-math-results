# Blind Audit Report: `targets/oeis-A077026/` (`@audit-2`)

**Verdict: PASS**

---

## 1. Primary Source & Statement Fidelity

- **Primary source verified live:** `https://oeis.org/search?q=id:A077026&fmt=json` (OEIS `A077026`, **revision 14**, `2016-09-27T06:14:53-04:00`).
- **Verbatim check against `TARGET.md`:**
  - `NAME`: `a(n) = Sum_{k=1..n} floor(n/k + 1)-floor(n/k + 1/2).` — exact match.
  - `OFFSET`: `1,2` — exact match.
  - `DATA`: all 73 terms `a(1) = 1` through `a(73) = 48` — exact match.
  - `FORMULA` (Benedict W. J. Irwin, Sep 22 2016): `Conjecture: Let f(a,b)=1, if (a+b) mod |a-b| != (a mod |a-b|)+(b mod |a-b|), and 0 otherwise. a(n) = Sum_{k=1..n-1} 1-f(n,k). - _Benedict W. J. Irwin_, Sep 22 2016` — exact match.
- All operands in $f(n, k)$ for $1 \le k \le n-1$ are strictly positive integers, so `mod` unambiguously denotes the least nonnegative remainder in $\{0, \dots, |n-k|-1\}$.

---

## 2. Line-by-Line Verification (`COUNTEREXAMPLE.md`)

- **Minimal counterexample ($n = 1$) & $n = 2$ (L15–18):**
  - $n = 1$: $a(1) = \lfloor 2 \rfloor - \lfloor 3/2 \rfloor = 1 \ne 0 = \sum_{k=1}^{0}(1 - f(1, k))$.
  - $n = 2$: $a(2) = (3 - 2) + (2 - 1) = 2 \ne 1 = 1 - f(2, 1)$ (since $|2-1| = 1$ gives $f(2,1) = 0$).
- **Exact Discrepancy Theorem for all $n \ge 1$ (L20–39):**
  - Reindexing $k \in \{1, \dots, n-1\}$ by $d = n - k \in \{1, \dots, n-1\}$: $n \equiv k \pmod d$ gives common remainder $r = n \bmod d = k \bmod d \in \{0, \dots, d-1\}$. Since $0 \le 2r \le 2d - 2 < 2d$, $(2r)\bmod d \ne 2r \iff 2r \ge d$, so $1 - f(n, k) = \mathbf{1}_{\{2r < d\}}$.
  - Writing $n = qd + r$ ($q \ge 1, 0 \le r \le d-1$), $\lfloor n/d + 1 \rfloor - \lfloor n/d + 1/2 \rfloor = 1 - \lfloor (2r+d)/(2d) \rfloor = \mathbf{1}_{\{2r < d\}}$, matching $1 - f(n, k)$ term-for-term for $1 \le d \le n-1$.
  - The remaining $d = n$ term of $a(n)$ equals $\lfloor 2 \rfloor - \lfloor 3/2 \rfloor = 1$, proving $\sum_{k=1}^{n-1}(1 - f(n, k)) = a(n) - 1$ for every $n \ge 1$. **PASS.**

---

## 3. Independent Verification & Gate 2 Novelty

- **Checker script:** Re-ran `.venv/bin/python -u targets/oeis-A077026/notes/check-check-3.py` — `exit 0`, raw output `PASS`, AST `FLOAT_CONSTANTS: 0` (pure `int` verification of all 73 OEIS `DATA` terms, $n=1,2$ counterexamples, termwise correspondence, and $S(n) = a(n) - 1$ for $1 \le n \le 200$).
- **Zenodo & Gate 2 receipts:** Independently verified `0` hits for `A077026` in `watch/snapshots/zenodo-23112421-oeis-ids.md`; all three Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) PASS.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.

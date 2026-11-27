# Blind Audit Report: `targets/oeis-A075997/` (`@audit-2`)

**Verdict: PASS**

---

## 1. Primary Source & Statement Fidelity

- **Primary source verified live:** `https://oeis.org/search?q=id:A075997&fmt=json` (OEIS `A075997`, **revision 37**, `2025-06-14T09:50:29-04:00`).
- **Verbatim check against `TARGET.md`:**
  - `NAME`: `a(n) = [n/2] - [n/3] + [n/4] - [n/5] + [n/6] - ..., where [n/k] = floor(n/k).` — exact match.
  - `OFFSET`: `0,5` — exact match.
  - `DATA`: all 80 terms `a(0) = 0` through `a(79) = 21` — exact match.
  - `FORMULA` (Benedict W. J. Irwin, Sep 23 2016): `Conjecture: Let f(a,b)=1, if (a+b) mod |a-b| != (a mod |a-b|)+(b mod |a-b|), and 0 otherwise. a(n) = Sum_{k=1..n-1} f(n+k,n-k). - _Benedict W. J. Irwin_, Sep 23 2016` — exact match.
- For all $n \ge 2$ and $1 \le k \le n-1$, both $n+k$ and $n-k$ and $|(n+k)-(n-k)| = 2k$ are strictly positive integers, so `mod` unambiguously denotes the least nonnegative remainder in $\{0, \dots, 2k-1\}$.

---

## 2. Line-by-Line Proof Verification (`PROOF.md`)

- **Base cases ($n = 0, 1$, L14):** Both sides are empty sums equal to $0$. Exact.
- **Step 1 (L16–22):** For $n \ge 2$, adding and subtracting the $m = 1$ term gives $a(n) = n + \sum_{m=1}^n (-1)^m \lfloor n/m \rfloor$. Expanding $\lfloor n/m \rfloor = \sum_{k=1}^n \mathbf{1}_{\{mk \le n\}}$ and interchanging sums gives $a(n) = n + \sum_{k=1}^n \sum_{m=1}^{\lfloor n/k \rfloor} (-1)^m = \sum_{k=1}^n \mathbf{1}_{\{\lfloor n/k \rfloor \text{ is even}\}}$. Since $\lfloor n/n \rfloor = 1$ is odd, the $k = n$ term is $0$, leaving $a(n) = \sum_{k=1}^{n-1} \mathbf{1}_{\{\lfloor n/k \rfloor \text{ is even}\}}$. Exact.
- **Step 2 (L24–38):** For $1 \le k \le n-1$, $(n+k) - (n-k) = 2k > 0$, so $r := (n+k)\bmod(2k) = (n-k)\bmod(2k) \in \{0, \dots, 2k-1\}$. Since $0 \le 2r \le 4k - 2 < 4k$, $f(n+k, n-k) = 1 \iff (2r)\bmod(2k) \ne 2r \iff 2r \ge 2k \iff (n-k)\bmod(2k) \in \{k, \dots, 2k-1\} \iff n \bmod (2k) \in \{0, \dots, k-1\}$. Writing $n = qk + s$ ($q = \lfloor n/k \rfloor, 0 \le s \le k-1$), $n \bmod (2k) \in \{0, \dots, k-1\} \iff q$ is even. Summing over $k = 1, \dots, n-1$ gives $\sum_{k=1}^{n-1} f(n+k, n-k) = a(n)$ for all $n \ge 0$. **PASS.**

---

## 3. Independent Verification & Gate 2 Novelty

- **Checker script:** Re-ran `.venv/bin/python -u targets/oeis-A075997/notes/check-check-3.py` — `exit 0`, raw output `PASS`, AST `FLOAT_CONSTANTS: 0` (pure `int` verification of all 80 OEIS `DATA` terms, Step 1, Step 2, and full equality for $0 \le n \le 200$).
- **Zenodo & Gate 2 receipts:** Independently verified `0` hits for `A075997` in `watch/snapshots/zenodo-23112421-oeis-ids.md`; all three Gate 2 receipts (`notes/novelty-gate2-watch-{1,5,6}.md`) PASS.

**Final Verdict: PASS.** Ready for Gate 3 freshness check (`@watch-1`, `@watch-5`, `@watch-6`) and reporting to `@coordinator`.

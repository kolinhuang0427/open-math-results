# Independent Check Report (`check-3`): `targets/oeis-A177260/`

## 1. Primary-Source Fidelity Check
Checked live OEIS JSON API (`https://oeis.org/search?q=id:A177260&fmt=json`) directly:
- **OEIS `A177260`** (rev `27`, `2025-11-05T15:22:18-05:00`, offset `0,4`):
  - **Name:** `Number of derangements of {1,2,...,n} having no adjacent 4-cycles (an adjacent 4-cycle is a cycle of the form (i,i+1,i+2,i+3)).`
  - **Formula:** `a(n) = Sum_{s=0..n} Sum_{t=0..floor((n-s)/4)} (-1)^(s+t)*(n-3*t)!/(s!*t!).`
  - **Formula (_R. J. Mathar_, Jul 26 2022):** `Conjecture: D-finite with recurrence a(n) = (n-1)*a(n-1) + (n-1)*a(n-2) + 2*a(n-4) + (n-1)*a(n-5) + 3*a(n-8). - _R. J. Mathar_, Jul 26 2022`
  - **Data:** `1,0,1,2,8,44,262,1846,14789,...` (23 terms, `a(0)..a(22)`).

`TARGET.md` and `PROOF.md` match the primary OEIS statement verbatim (quantifier $n \ge 8$, offset `0`, double sum, and recurrence).

## 2. Mathematical Proof Check
Reviewed `targets/oeis-A177260/PROOF.md` Steps 1–3:
- Step 1: Summation reindexing $k = n - 3t$ and $j = s + t$ reduces $y(x) = \sum_{n\ge 0} a(n)x^n$ to $\sum_{m\ge 0} m!x^m / (1+x+x^4)^{m+1}$ in $\mathbb{Z}[[x]]$. Exact.
- Step 2: $F(u) = \sum_{m\ge 0} m! u^m$ satisfies $u^2 F'(u) + (u-1)F(u) + 1 = 0$; substituting $u(x) = x/D(x)$ with $D(x) = 1+x+x^4$ yields $x^2(1+x+x^4)y'(x) + (-1+x^2+2x^4+4x^5+3x^8)y(x) + (1-3x^4) = 0$ in $\mathbb{Z}[[x]]$. Exact.
- Step 3: Extracting $[x^n]$ for $n \ge 8$ gives Mathar's exact recurrence. Exact.

## 3. Independent Mechanical Verification
Written solely from live OEIS `A177260` definitions and `PROOF.md` without reading `verify.py` or author notes, using pure Python `int` / `Fraction` arithmetic (zero floats):
- Script: `targets/oeis-A177260/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/oeis-A177260/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[1/2] Double sum matches all 23 live OEIS A177260 terms and Step 1 OGF up to x^90.
[2/2] Step 2 ODE and Step 3 Mathar recurrence verified for 8 <= n <= 90.
PASS
```

## 4. Verdict
- **PASS** (awaiting Gate 2 novelty receipts from `@watch-1`/`@watch-5`/`@watch-6` per `#182`).

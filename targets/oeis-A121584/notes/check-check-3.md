# Independent Check Report (`check-3`): `targets/oeis-A121584/`

## 1. Primary-Source Fidelity Check
Checked live OEIS JSON API (`https://oeis.org/search?q=id:A121584&fmt=json`) directly:
- **OEIS `A121584`** (rev `4`, `2022-07-26T11:38:40-04:00`, offset `1,2`):
  - **Name:** `Number of cells in columns 1 and 2 of all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.`
  - **Formula:** `a(1)=1, a(2)=4, a(n)=[(2n-3)a(n-1)-(n-1)a(n-2)]/(n-2) + (1/2)(2n^3-9n^2+17n-16)(n-1)!/(n-2) for n>=3.`
  - **Formula (_R. J. Mathar_, Jul 26 2022):** `Conjecture D-finite with recurrence 14*(-n+1)*a(n) +(14*n^2+1731*n-6995)*a(n-1) +3*(-577*n^2+480*n+7243)*a(n-2) +2*(2781*n^2-11952*n+6004)*a(n-3) +(-5987*n^2+36181*n-54220)*a(n-4) +2*(1071*n-3433)*(n-4)*a(n-5)=0.`
  - **Data:** `1,4,18,93,569,4074,33336,...` (19 terms, `a(1)..a(19)`).

`TARGET.md` and `PROOF.md` match the primary OEIS statement verbatim (quantifier $n \ge 6$, offset `1`, defining recurrence, and all 6 coefficients).

## 2. Mathematical Proof Check
Reviewed `targets/oeis-A121584/PROOF.md` Steps 1–3:
- Step 1: Clearing $k - 2 \ge 1$ for $k \ge 3$ gives $B(k) = \frac{(k-1)!}{2}(2k^3 - 9k^2 + 17k - 16)$. Exact.
- Step 2 & Step 3: Exact $\mathbb{Z}[n]$ operator factorization $(n-2)(n-3) M(n) = \sum_{j=0}^3 d_j(n) B(n-j) = \frac{(n-4)!}{2} P(n)$ with $P(n) \equiv 0$, proving $M(n) = 0$ for all $n \ge 6$ and D-finiteness of $\hat{y}(x)$. Exact.

## 3. Independent Mechanical Verification
Written solely from live OEIS `A121584` definitions and `PROOF.md` without reading `verify.py` or author notes, using exact `int` / `Fraction` / SymPy `ZZ` arithmetic (zero floats):
- Script: `targets/oeis-A121584/notes/check-check-3.py`
- Command: `.venv/bin/python -u targets/oeis-A121584/notes/check-check-3.py`
- Raw output (exit code `0`):
```text
[1/3] Defining recurrence matches all 19 live OEIS A121584 terms (n=1..19).
[2/3] Steps 2 & 3 exact Z[n] operator factorization and P(n) == 0 verified.
[3/3] Mathar recurrence verified for 6 <= n <= 120.
PASS
```

## 4. Verdict
- **PASS** (awaiting Gate 2 novelty receipts from `@watch-1`/`@watch-5`/`@watch-6` per `#402`).

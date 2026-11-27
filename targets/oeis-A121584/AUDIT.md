# Independent Blind Audit — `targets/oeis-A121584/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:37Z`
- **Verdict:** **PASS**

---

## 1. Primary Source & Statement Fidelity

Verified verbatim against live OEIS **A121584** JSON (`https://oeis.org/search?q=id:A121584&fmt=json`, revision `4`, `2022-07-26T11:38:40-04:00`, offset `1,2`):
- **Name:** `Number of cells in columns 1 and 2 of all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.`
- **Formula:** `a(1)=1, a(2)=4, a(n)=[(2n-3)a(n-1)-(n-1)a(n-2)]/(n-2) + (1/2)(2n^3-9n^2+17n-16)(n-1)!/(n-2) for n>=3.`
- **Conjecture (`_R. J. Mathar_`, Jul 26 2022):**
  `Conjecture D-finite with recurrence 14*(-n+1)*a(n) +(14*n^2+1731*n-6995)*a(n-1) +3*(-577*n^2+480*n+7243)*a(n-2) +2*(2781*n^2-11952*n+6004)*a(n-3) +(-5987*n^2+36181*n-54220)*a(n-4) +2*(1071*n-3433)*(n-4)*a(n-5)=0.`
- Every coefficient $C_0(n), \dots, C_5(n)$, offset `1`, defining recurrence, and quantifier $n \ge 6$ (all indices $n-5 \ge 1$) in `TARGET.md` and `PROOF.md` match the live OEIS entry verbatim.

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`)

1. **Step 1 — Second-order difference operator (lines 24–29):**
   - For every integer $k \ge 3$, $k - 2 \ge 1$. Clearing the denominator $k - 2$ in the defining formula yields $B(k) := (k-2)a(k) - (2k-3)a(k-1) + (k-1)a(k-2) = \frac{(k-1)!}{2} f(k)$ with $f(k) = 2k^3 - 9k^2 + 17k - 16$. Exact.
2. **Step 2 — Exact operator factorization (lines 31–44):**
   - Checked every displayed polynomial $d_0, d_1, d_2, d_3 \in \mathbb{Z}[n]$ on lines 35–38 against `check-check-3.py` lines 55–60: exact match.
   - The polynomial identity $(n-2)(n-3)\sum_{j=0}^5 C_j(n) a(n-j) = \sum_{j=0}^3 d_j(n) B(n-j)$ holds identically in $\mathbb{Z}[n, a_0, \dots, a_5]$. Exact.
3. **Step 3 — Exact cancellation & D-finiteness (lines 46–58):**
   - For every $n \ge 6$, all four shifted indices $k \in \{n, n-1, n-2, n-3\}$ satisfy $k \ge 3$ (so Step 1 applies to every term) and $n - 4 \ge 2$ (so $(n-4)!$ is a positive integer).
   - Factoring out $\frac{(n-4)!}{2}$ gives $(n-2)(n-3)M(n) = \frac{(n-4)!}{2} P(n)$ with $P(n) \equiv 0 \in \mathbb{Z}[n]$ verified symbolically.
   - Since $(n-2)(n-3) > 0$ for all $n \ge 6$, $M(n) = 0$ for all $n \ge 6$.
   - Summing $M(n) \frac{x^{n-5}}{(n-5)!}$ over $n \ge 6$ yields a polynomial-coefficient linear ODE (with constant inhomogeneous term from the omitted $m=0$ index, hence D-finite) for $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$. Airtight.

---

## 3. Independent Verification & Gate 2 Novelty Check

- **Independent Checker Re-run (`notes/check-check-3.py`):**
  - Command: `.venv/bin/python targets/oeis-A121584/notes/check-check-3.py`
  - Exit code: `0`
  - Raw output:
    ```text
    [1/3] Defining recurrence matches all 19 live OEIS A121584 terms (n=1..19).
    [2/3] Steps 2 & 3 exact Z[n] operator factorization and P(n) == 0 verified.
    [3/3] Mathar recurrence verified for 6 <= n <= 120.
    PASS
    ```
  - Pure exact `int` / `Fraction` / SymPy `ZZ` arithmetic (zero floats).
- **Gate 2 Novelty Receipts:** Verified all three (`notes/novelty-gate2-watch-{1,5,6}.md`) — all **PASS**.

---

## 4. Verdict & Handoff

**PASS** (label: `"written proof, internally audited"`). Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.

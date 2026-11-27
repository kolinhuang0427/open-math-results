# Independent Blind Audit — `targets/oeis-A121580/`

- **Auditor:** `@audit-2`
- **Audited UTC:** `2026-11-27T09:37Z`
- **Verdict:** **PASS**

---

## 1. Primary Source & Statement Fidelity

Verified verbatim against live OEIS **A121580** JSON (`https://oeis.org/search?q=id:A121580&fmt=json`, revision `12`, `2024-09-15T07:13:47-04:00`, offset `1,2`):
- **Name:** `Number of cells in column 1 of all deco polyominoes of height n. A deco polyomino is a directed column-convex polyomino in which the height, measured along the diagonal, is attained only in the last column.`
- **Formula:** `a(1) = 1, a(n) = a(n-1)+(n-1)!*(1+n*(n-1)/2) for n>=2.`
- **Conjecture (`_R. J. Mathar_`, Jul 26 2022):**
  `Conjecture D-finite with recurrence a(n) +(-n-4)*a(n-1) +3*(n+1)*a(n-2) +2*(-2*n+3)*a(n-3) +2*(n-3)*a(n-4)=0.`
- `TARGET.md` and `PROOF.md` match the live OEIS statement verbatim (quantifier $n \ge 5$ keeps all indices $n-4 \ge 1$ inside offset `1`).

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`)

1. **Step 1 — First-difference telescoping (lines 12–30):**
   - For $k \ge 2$, $b(k) := a(k) - a(k-1) = (k-1)!(1 + k(k-1)/2) = \frac{(k-1)!}{2}(k^2 - k + 2)$.
   - Hand-checked coefficient matching on $a(n), \dots, a(n-4)$: $1$, $-1 + (-n-3) = -n-4$, $(n+3)+2n = 3(n+1)$, $-2n + (-2n+6) = 2(-2n+3)$, $2n-6 = 2(n-3)$. Exact.
2. **Step 2 — Exact polynomial cancellation (lines 32–60):**
   - For $n \ge 5$, all $k \in \{n, n-1, n-2, n-3\}$ satisfy $k \ge 2$ and $n - 4 \ge 1$, so $(n-4)!$ is a well-defined positive integer.
   - Factoring out $\frac{(n-4)!}{2}$ leaves $P(n) \in \mathbb{Z}[n]$ on lines 45–48.
   - Verified all four expanded quintic/quartic/cubic summands on lines 54–57 individually and checked degree-by-degree sums ($n^5: 1-1=0$, $n^4: -7+5+2=0$, $n^3: 19-1-16-2=0$, $n^2: -29-37+46+20=0$, $n^1: 28+90-48-70=0$, $n^0: -12-72+84=0$), yielding $P(n) \equiv 0 \in \mathbb{Z}[n]$. Airtight.
3. **Step 3 — D-finiteness of EGF (lines 62–67):**
   - Extending by $a(0) = 0$ satisfies the $n = 4$ recurrence ($53 - 88 + 45 - 10 + 0 = 0$).
   - Setting $m = n - 4 \ge 0$, multiplying by $x^m / m!$, and summing over $m \ge 0$ using $\sum_{m \ge 0} a(m+k)\frac{x^m}{m!} = \hat{y}^{(k)}(x)$ and $\sum_{m \ge 0} m\,a(m+k)\frac{x^m}{m!} = x\hat{y}^{(k+1)}(x)$ yields the exact homogeneous order-4 linear ODE $(1-x)\hat{y}^{(4)} + (3x-8)\hat{y}^{(3)} + (15-4x)\hat{y}'' + (2x-10)\hat{y}' + 2\hat{y} = 0$. Airtight.

---

## 3. Independent Verification & Gate 2 Novelty Check

- **Independent Checker Re-run (`notes/check-check-2.py`):**
  - Command: `.venv/bin/python targets/oeis-A121580/notes/check-check-2.py`
  - Exit code: `0`
  - Raw output: `PASS (OEIS data n=1..19, Steps 1-3 identities & EGF ODE to x^44, Mathar recurrence 5<=n<=60)`
  - Uses pure exact `int` / `Fraction` / SymPy arithmetic (zero floats).
- **Gate 2 Novelty Receipts:** Verified all three (`notes/novelty-gate2-watch-{1,5,6}.md`) — all **PASS**.

---

## 4. Verdict & Handoff

**PASS** (label: `"written proof, internally audited"`). Handed off to `@watch-1`, `@watch-5`, `@watch-6` for Gate 3 freshness check (<1h) prior to `@coordinator` final verification.

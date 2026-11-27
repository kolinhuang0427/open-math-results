# Adversarial Audit Report (`audit-1`): `targets/oeis-A157003/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A157003` (rev. 37, Nov 05 2025 `15:22:17`, offset `0,3`) — R. J. Mathar's Nov 19 2014 6-term D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-3.md`, `notes/check-check-3.py`, live OEIS `A157003` (`/A157003/internal`, rev. 37), `watch/snapshots/**` (658 files)
- **Verdict:** **PASS** (Label: `written proof, internally audited`)

---

## 1. Primary-Source & Statement Fidelity — PASS

Verified verbatim against live OEIS `A157003` (`https://oeis.org/A157003/internal`, `#37 Nov 05 2025 15:22:17`, offset `0,3`):
- `%N`: `Transform of Catalan numbers whose Hankel transform gives the Somos-4 sequence.` — exact match.
- `%C`: `Image of the Catalan numbers A000108 by the Riordan array (1, x*(1-x^2)).` — exact match.
- `%F`:
  - `G.f.: c(x*(1-x^2)) where c(x) is the g.f. of A000108;` — exact match.
  - `a(n) = Sum_{k=0..n} (-1)^((n-k)/2)*(1+(-1)^(n-k))*C(k,floor((n-k)/2))*A000108(k)/2.` — exact match (and directly verified as $[x^n]\sum_{k\ge 0} C_k x^k(1-x^2)^k$).
  - `Conjecture: (n+1)*a(n) +(n+2)*a(n-1) +(-21*n+29)*a(n-2) +(3*n-16)*a(n-3) +40*(n-3)*a(n-4) +2*(-2*n+7)*a(n-5) +10*(-2*n+9)*a(n-6)=0. - _R. J. Mathar_, Nov 19 2014` — exact match (still marked `Conjecture:`).
  - `Recurrence: (n+1)*a(n) = 2*(2*n-1)*a(n-1) + (n+1)*a(n-2) - 8*(n-2)*a(n-3) + 2*(2*n-7)*a(n-5). - _Vaclav Kotesovec_, Feb 01 2015` — exact match.
- `%S/%T/%U` (28 terms, `n = 0..27`): `1,1,2,4,10,27,...,8333765738127` — exact match with `notes/check-check-3.py`.
- Quantifier/domain: offset `0` with `a(n-6)` implies $n \ge 6$ for Mathar's 6-term recurrence (and $n = 5$ also holds under the natural convention $a(-1) = 0$). Exact.
- Novelty check: `.venv/bin/python tools/novelty_grep.py A157003` -> `0` matches across `658` snapshot files (incl. Zenodo compendia & `mylesparslow-conjecture-ledger`). Gate 2 cleared by `@watch-1` (`#1218`) and `@watch-5` (`#1220`).

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`) — PASS

- **Section 1 (Quadratic & first-order ODE, L19–29):**
  - Setting $P(x) = x(1 - x^2) = x - x^3 \in x\mathbb{Z}[x]$ in the Catalan identity $u c(u)^2 - c(u) + 1 = 0$ gives $P(x) A(x)^2 - A(x) + 1 = 0$ in $\mathbb{Z}[[x]]$.
  - $y(x) := 1 - 2 P(x) A(x) = 1 + O(x) \in \mathbb{Z}[[x]]^\times$ satisfies $y(x)^2 = 1 - 4 P(x) = \Delta(x) := 1 - 4x + 4x^3$.
  - Formal differentiation $2 y y' = \Delta'$ multiplied by $y$ gives $2 \Delta y' = \Delta' y$ in $\mathbb{Q}[[x]]$. Substituting $y = 1 - 2 P A$, $y' = -2 P' A - 2 P A'$ and dividing by $-4$ yields $\Delta P A' + (\Delta P' - \frac{1}{2}\Delta' P)A = -\frac{1}{4}\Delta'$.
  - Direct polynomial expansions verified term-by-term:
    - $\Delta P = (1 - 4x + 4x^3)(x - x^3) = x(1 - 4x - x^2 + 8x^3 - 4x^5)$,
    - $\Delta P' - \frac{1}{2}\Delta' P = (1 - 3x^2)(1 - 2x + 2x^3) = 1 - 2x - 3x^2 + 8x^3 - 6x^5$,
    - $-\frac{1}{4}\Delta' = 1 - 3x^2$.
- **Section 2 (Coefficient extraction & Mathar's recurrence, L35–46):**
  - Since $\deg(1 - 3x^2) = 2$, extracting $[x^n]$ for every integer $n \ge 3$ (with $a(k) = 0$ for $k < 0$) yields $K(n) := (n+1)a(n) - 2(2n-1)a(n-1) - (n+1)a(n-2) + 8(n-2)a(n-3) - 2(2n-7)a(n-5) = 0$, proving Kotesovec's recurrence for all $n \ge 5$ (and $n = 3, 4$).
  - For all $n \ge 6$ (and $n = 5$ with $a(-1) = 0$), forming $K(n) + 5 K(n-1) = 0$ gives:
    - $[a(n)]$: $n + 1$,
    - $[a(n-1)]$: $-2(2n-1) + 5n = n + 2$,
    - $[a(n-2)]$: $-(n+1) - 10(2n-3) = -21n + 29$,
    - $[a(n-3)]$: $8(n-2) - 5n = 3n - 16$,
    - $[a(n-4)]$: $40(n-3)$,
    - $[a(n-5)]$: $-2(2n-7) = 2(-2n + 7)$,
    - $[a(n-6)]$: $-10(2n-9) = 10(-2n + 9)$,
    matching Mathar's conjectured 6-term recurrence verbatim. Zero gaps.

---

## 3. Independent Exact Verification — PASS

- Command: `.venv/bin/python -u targets/oeis-A157003/notes/check-check-3.py`
- Exit code: `0`, raw output: `PASS`
- AST zero-float check: `FLOATS: []` (pure exact Python `int` + SymPy `QQ[x]`/`QQ[n]`).
- Verified all 28 live OEIS terms, binomial Catalan formula ($n \le 45$), symbolic ODE & $K(n) + 5 K(n-1)$ identity, formal ODE to $x^{59}$, $K(n) = 0$ ($3 \le n \le 60$), and Mathar's 6-term recurrence ($5 \le n \le 60$).

---

## 4. Verdict & Handoff

**PASS.** Ready for Gate 3 freshness verification (`<1h`) by `@watch-1`, `@watch-5`, `@watch-6` prior to `@coordinator` final check.

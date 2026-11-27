# Adversarial Audit Report (`audit-1`): `targets/oeis-A168503/`

- **Auditor:** `@audit-1` (strictly blind to `verify.py` and author scratch `notes/`)
- **Target:** OEIS `A168503` (rev. 20, Feb 07 2025 `00:50:52`, offset `0,3`) — R. J. Mathar's Feb 10 2015 4-term D-finite recurrence conjecture
- **Audited Files:** `TARGET.md`, `PROOF.md`, `notes/check-check-1.md`, `notes/check-check-1.py`, live OEIS `A168503` (`/A168503/internal`, rev. 20), `watch/snapshots/**` (658 files)
- **Verdict:** **PASS** (Label: `written proof, internally audited`)

---

## 1. Primary-Source & Statement Fidelity — PASS

Verified verbatim against live OEIS `A168503` (`https://oeis.org/A168503/internal`, `#20 Feb 07 2025 00:50:52`, offset `0,3`):
- `%N`: `Expansion of 1/(1-x/(1-2x/(1-3x/(1-x/(1-2x/(1-3x/(1-... (continued fraction).` — exact match.
- `%F`:
  - `G.f.: (1-sqrt(1-12*x+36*x^2-24*x^3))/(6*x*(1-x)).` — exact match.
  - `Conjecture: (n+1)*a(n) +(-13*n+5)*a(n-1) +6*(8*n-13)*a(n-2) +12*(-5*n+13)*a(n-3) +12*(2*n-7)*a(n-4)=0. - _R. J. Mathar_, Feb 10 2015` — exact match (still marked `Conjecture:`, no `%H` links).
- `%S/%T/%U` (22 terms, `n = 0..21`): `1,1,3,15,87,...,13907901060055467` — exact match with `notes/check-check-1.py`.
- Quantifier/domain: offset `0` with `a(n-4)` gives $n \ge 4$ (and $n = 3$ also holds with $a(-1) = 0$). Exact.
- Novelty check: `.venv/bin/python tools/novelty_grep.py A168503` -> `0` matches across `658` snapshot files (incl. Zenodo compendia & `mylesparslow-conjecture-ledger`). Gate 2 cleared by `@watch-1` (`#1244`) and `@watch-5` (`#1251`).

---

## 2. Line-by-Line Mathematical Audit (`PROOF.md`) — PASS

- **Section 1 (3-periodic continued fraction, $x$-adic contraction, quadratic & radical, L16–26):**
  - Computing the 3-step continued-fraction operator from inside out:
    $$T(u) = \frac{1}{1 - \frac{x}{1 - \frac{2x}{1 - 3xu}}} = \frac{1}{1 - \frac{x(1 - 3xu)}{1 - 2x - 3xu}} = \frac{1 - 2x - 3xu}{1 - 3x - 3x(1 - x)u}.$$
    Since the denominator is $1 + O(x) \in \mathbb{Z}[[x]]^\times$, $T$ maps $\mathbb{Z}[[x]]$ into $1 + x\mathbb{Z}[[x]]$.
  - Difference identity:
    $$T(u_1) - T(u_2) = \frac{3x\bigl(-(1-3x) + (1-x)(1-2x)\bigr)(u_1 - u_2)}{(1 - 3x - 3x(1-x)u_1)(1 - 3x - 3x(1-x)u_2)} = \frac{6x^3(u_1 - u_2)}{(1 - 3x - 3x(1-x)u_1)(1 - 3x - 3x(1-x)u_2)} \in x^3(u_1 - u_2)\mathbb{Z}[[x]].$$
    Hence $T$ is a strict $x$-adic contraction on $\mathbb{Z}[[x]]$, so all finite convergents (including $T^m(1)$, $T^m((1-x)^{-1})$, $T^m((1-x/(1-2x))^{-1})$) converge $x$-adically to the unique fixed point $A(x) = T(A(x)) \in 1 + x\mathbb{Z}[[x]]$.
  - Clearing denominators in $A = T(A)$ cancels $-3x A$ on both sides and yields $3x(1 - x)A(x)^2 - A(x) + (1 - 2x) = 0$.
  - Multiplying by $12x(1 - x)$ and completing the square yields $y(x)^2 = \Delta(x)$ for $y(x) := 1 - 6x(1 - x)A(x) = 1 + O(x)$ and $\Delta(x) := 1 - 12x(1 - x)(1 - 2x) = 1 - 12x + 36x^2 - 24x^3$, confirming the radical g.f. $A(x) = \frac{1 - \sqrt{\Delta(x)}}{6x(1 - x)}$.
- **Section 2 (First-order linear ODE & coefficient extraction, L32–45):**
  - Differentiating $y^2 = \Delta$ in $\mathbb{Q}[[x]]$ and multiplying by the unit $y = 1 + O(x)$ gives $2\Delta y' = \Delta' y$.
  - Writing $P(x) = 3x(1 - x)$ ($y = 1 - 2PA$, $y' = -2P'A - 2PA'$) and dividing by $-12$ yields
    $$\Delta(x)\frac{P(x)}{3}A'(x) + \frac{1}{3}\left(\Delta(x)P'(x) - \frac{1}{2}\Delta'(x)P(x)\right)A(x) = -\frac{1}{12}\Delta'(x).$$
  - Direct polynomial expansions verified term-by-term:
    - $\Delta(x)(x - x^2) = x(1 - 13x + 48x^2 - 60x^3 + 24x^4)$,
    - $\Delta(x)(1 - 2x) + (6 - 36x + 36x^2)(x - x^2) = 1 - 8x + 18x^2 - 24x^3 + 12x^4$,
    - $-\frac{1}{12}\Delta'(x) = 1 - 6x + 6x^2$.
  - Since $\deg(1 - 6x + 6x^2) = 2$, extracting $[x^n]$ for every integer $n \ge 3$ (and hence all $n \ge 4$, with $a(-1) = 0$ at $n = 3$) gives:
    - $[a(n)]$: $n + 1$,
    - $[a(n-1)]$: $-13(n - 1) - 8 = -13n + 5$,
    - $[a(n-2)]$: $48(n - 2) + 18 = 6(8n - 13)$,
    - $[a(n-3)]$: $-60(n - 3) - 24 = 12(-5n + 13)$,
    - $[a(n-4)]$: $24(n - 4) + 12 = 12(2n - 7)$,
    matching Mathar's conjectured recurrence verbatim. Zero gaps.

---

## 3. Independent Exact Verification — PASS

- Command: `.venv/bin/python -u targets/oeis-A168503/notes/check-check-1.py`
- Exit code: `0`, raw output: `PASS`
- AST zero-float check: `FLOATS: []` (pure exact Python `int` + SymPy).
- Verified symbolic identities ($T(u)$, $x$-adic contraction, quadratic, completing the square, ODE reductions, Mathar coefficients), exact fixed-point convergence $T(u) = u \pmod{x^{81}}$, all 22 live OEIS terms, SymPy radical g.f. to $x^{20}$, formal ODE at $0 \le n \le 80$, boundary $n = 3$, and Mathar's recurrence for $4 \le n \le 80$.

---

## 4. Verdict & Handoff

**PASS.** Ready for Gate 3 freshness verification (`<1h`) by `@watch-1`, `@watch-5`, `@watch-6` prior to `@coordinator` final check.

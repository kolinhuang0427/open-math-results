# Blind Audit: `targets/oeis-A157002/`

- **Auditor:** `audit-3` (`auto`)
- **Date (UTC):** 2026-11-27
- **Verdict:** **PASS** (`written proof, internally audited`)
- **Audited Files:** `targets/oeis-A157002/TARGET.md`, `targets/oeis-A157002/PROOF.md`, `targets/oeis-A157002/notes/check-check-1.md`, `targets/oeis-A157002/notes/check-check-1.py` (strictly blind to `verify.py` and author scratch `notes/`)
- **Primary Sources Checked:** Live OEIS JSON (`2026-11-27`) for `A157002` (`rev. 15`, offset `0,4`); `0` hits across `watch/snapshots/**` and live `mylesparslow-collab/mylesparslow-collab.github.io` (`demos/conjecture-ledger/index.html`).

---

## 1. Primary-Source & Statement Fidelity

- Verified verbatim match between live OEIS `A157002` (`rev. 15`, offset `0,4`) and `TARGET.md` L16–23:
  - `NAME`: `Transform of Catalan numbers whose Hankel transform gives the Somos-4 sequence.`
  - `COMMENT`: `Image of the Catalan numbers A000108 by the Riordan array (1-x,x(1-x^2)).`
  - `FORMULA`: radical g.f. `(1 - sqrt(1-4*x*(1-x^2)))/(2*x*(1+x))`, explicit Catalan-binomial sum, and R. J. Mathar's Nov 19 2014 `Conjecture: (n+1)*a(n) +3*(-n+1)*a(n-1) +2*(-2*n+1)*a(n-2) +2*(2*n-7)*a(n-3) +2*(2*n-7)*a(n-4)=0`.

---

## 2. Adversarial Line-by-Line Proof Audit (`PROOF.md`)

1. **Section 1 (Algebraic equation from the Riordan definition):**
   - From $u c(u)^2 - c(u) + 1 = 0$ ($c(u) = \frac{1-\sqrt{1-4u}}{2u} \in \mathbb{Z}[[u]]$) and $A(x) = (1-x)c(x(1-x^2))$, setting $u = x(1-x^2)$ and cancelling $(1-x)$ yields $A(x) = \frac{1-\sqrt{1-4x(1-x^2)}}{2x(1+x)}$ and $x(1+x)A(x)^2 - A(x) + (1-x) = 0$.
   - Verified directly that $(1-x)\sum_{k\ge 0} C_k x^k (1-x^2)^k$ also equals OEIS's explicit sum $\sum_{k=0}^n (-1)^{\lfloor (n-k+1)/2 \rfloor}\binom{k}{\lfloor (n-k)/2 \rfloor} C_k$.
   - Setting $y(x) := 1 - 2x(1+x)A(x) = 1 + O(x) \in \mathbb{Z}[[x]]$ and $\Delta(x) := 1 - 4x + 4x^3$ gives $y(x)^2 = \Delta(x)$ identically in $\mathbb{Z}[[x]]$. **Verified.**
2. **Section 2 (First-order linear ODE & coefficient extraction):**
   - Differentiating $y^2 = \Delta$ gives $2\Delta y' = \Delta' y$. Substituting $y = 1 - 2PA$ ($P = x + x^2$) yields $4\Delta P A' + (4\Delta P' - 2\Delta' P)A = -\Delta'$.
   - Verified all three polynomial reductions by hand: $\Delta P = x - 3x^2 - 4x^3 + 4x^4 + 4x^5$, $\Delta P' - \frac{1}{2}\Delta' P = 1 - 6x^2 - 2x^3 + 2x^4$, and $-\frac{1}{4}\Delta' = 1 - 3x^2$.
   - Extracting $[x^n]$ for every $n \ge 3$ (since $\deg(1 - 3x^2) = 2$) yields $(n+1)a(n) + 3(-n+1)a(n-1) + 2(-2n+1)a(n-2) + 2(2n-7)a(n-3) + 2(2n-7)a(n-4) = 0$ identically (for all $n \ge 4$, and at $n = 3$ with $a(-1) = 0$). **Verified.**

---

## 3. Independent Computation Check

- Inspected `targets/oeis-A157002/notes/check-check-1.py` via AST: zero floats (`[]`), sole `/` on L93 operates on exact SymPy expressions.
- Independently executed `.venv/bin/python -u targets/oeis-A157002/notes/check-check-1.py`: exited `0` with raw `PASS` (exact symbolic verification of algebraic equation, ODE polynomials, and coefficient identity; exact Riordan vs OEIS formula for $0 \le n \le 80$; live OEIS prefix $0..27$; radical g.f. $0..20$; ODE/Mathar recurrence up to $n = 80$ plus $n = 3$ boundary).

---

## 4. Handoff

**PASS** (`written proof, internally audited`). Handing off to `@watch-1 @watch-5 @watch-6` for Gate 3 novelty check (`<1h`), instructing them to mention `@coordinator` on PASS with verifier command `.venv/bin/python -u targets/oeis-A157002/notes/check-check-1.py` and paths `targets/oeis-A157002/{TARGET.md,PROOF.md,AUDIT.md,notes/check-check-1.py}`.

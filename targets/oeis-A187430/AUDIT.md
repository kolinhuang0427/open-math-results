# Blind Adversarial Audit Report: `targets/oeis-A187430/`

- **Auditor:** `@audit-2`
- **Audit UTC:** `2026-11-27T10:18Z`
- **Verdict:** **PASS**
- **Files Audited (strictly blind):** Live OEIS JSON `A187430` (rev. 55), `TARGET.md`, `PROOF.md`, `notes/check-check-2.md`, `notes/check-check-2.py`, and Gate 2 receipts `notes/novelty-gate2-watch-{1,5,6}.md`. Author `verify.py` and scratch notes were **not** read.

---

## 1. Primary-Source Fidelity (Live OEIS `A187430`, rev. 55)

Queried live `https://oeis.org/search?q=id:A187430&fmt=json` (`revision: 55`, `time: 2024-01-17T09:35:29-05:00`, `offset: 0,3`):
- **NAME:** `Number of nonnegative walks of n steps with step sizes 1 and 2, starting and ending at 0.` — verbatim match.
- **COMMENTS:** `Equivalently, the number of paths from (0,0) to (n,0) using steps of the form (1,2),(1,1),(1,-1) or (1,-2) and staying on or above the x-axis.` — verbatim match.
- **FORMULA:** `Conjecture: 1 + Sum_{n>=0} a(n)*(-1)^n x^(n+1)/(1-x)^(2*n+2) = C(x), the g.f. for the Catalan numbers A000108. - _Benedict W. J. Irwin_, Jan 13 2017` — verbatim match; remains marked `Conjecture:` on OEIS rev. 55 with no confirmation note.

---

## 2. Adversarial Line-by-Line Proof Audit

- **Step 1 (Kernel Equation from Primary Walk Definition):** Hand-verified directly from the nonnegative walk recurrence $w(n, h) = w(n-1, h-2) + w(n-1, h-1) + w(n-1, h+1) + w(n-1, h+2)$ ($h \ge 0$, $w(n-1, j) = 0$ for $j < 0$) that multiplying by $u^2 t^n$ and summing over $n \ge 1$ yields
  $$K(t, u) G(t, u) = u^2 - t(u+1) A(t) - t u G_1(t), \qquad K(t, u) = u^2 - t(u^4 + u^3 + u + 1)$$
  exactly in $\mathbb{Z}[u][[t]]$.
- **Step 2 (Algebraic Kernel Elimination in $\mathbb{Z}[[t]][u]$):** Hand-verified every algebraic detail without any analytic/branch-cut assumptions:
  - $f(y) = \frac{y(1-y)^2}{(1-y+y^2)^2} = y - 2y^3 + \dots \in y + y^2 \mathbb{Z}[[y]]$ has unique compositional inverse $y(t) = t + 2t^3 + \dots \in t\mathbb{Z}[[t]]$.
  - With $s(t) = \frac{y(t)}{1-y(t)} \in t\mathbb{Z}[[t]]$, direct hand expansion confirms $(u^2 - su - y)(-yu^2 - su + 1) = \frac{(1-y+y^2)^2}{(1-y)^2} u^2 - y(u^4+u^3+u+1)$, so multiplying by $\frac{(1-y)^2}{(1-y+y^2)^2}$ gives $M(t,u)Q(t,u) = K(t,u)$ identically in $\mathbb{Z}[[t]][u]$.
  - Because $M(t, u)$ is monic of degree $2$ in $u$, $R = \mathbb{Z}[[t]][u]/(M(t,u)) = \mathbb{Z}[[t]]\cdot 1 \oplus \mathbb{Z}[[t]]\cdot \bar{u}$ is a free $\mathbb{Z}[[t]]$-module of rank $2$, complete in the $t$-adic topology, and term-by-term reduction in $t$ defines a continuous ring homomorphism $\mathbb{Z}[u][[t]] \to R$ (finite convolutions at each $t^N$ preserve multiplication). Reducing the kernel equation annihilates $K(t,\bar{u}) = 0$, and reading the coefficient of $1$ in $\{1, \bar{u}\}$ gives $t A(t) = y(t)$ (completely from first principles, without relying on unproved OEIS formulas).
- **Step 3 (Substitution $t = -x/(1-x)^2$ & Catalan Identification):** Hand-verified directly from $x C(x)^2 = C(x) - 1$ ($C(0) = 1$, $Y(x) = 1 - C(x) \in x\mathbb{Z}[[x]]$):
  - $C^2 - C + 1 = (1-x)C^2$ gives $(1-x)^2(1-C)C^2 + x(C^2-C+1)^2 = (1-x)^2 C^2((1-C)+xC^2) = 0$.
  - Dividing by the unit $(1-x)^2(1 - Y(x) + Y(x)^2)^2 \in \mathbb{Z}[[x]]^\times$ yields $f(Y(x)) = \frac{-x}{(1-x)^2} = u(x) \in x\mathbb{Z}[[x]]$.
  - Applying $y(f(Y)) = Y$ gives $1 - C(x) = Y(x) = y(u(x)) = \sum_{n \ge 0} a(n) \bigl(\frac{-x}{(1-x)^2}\bigr)^{n+1} = -\sum_{n \ge 0} a(n) \frac{(-1)^n x^{n+1}}{(1-x)^{2n+2}}$, rearranging to Irwin's exact identity in $\mathbb{Z}[[x]]$.

---

## 3. Independent Computational Verification & Gate 2 Novelty

- **Direct Re-Run of Independent Checker:** Executed `.venv/bin/python targets/oeis-A187430/notes/check-check-2.py`:
  - **Exit code:** `0` (`FLOAT_CONSTANTS: 0` by AST check; pure integer DP + exact SymPy polynomial arithmetic).
  - **Raw output:**
    ```text
    PASS
    Verified OEIS A187430 data n=0..28, Step 1 kernel (n<=32), Step 2 K=MQ + reversion f(t*A(t))=t (t^32), Step 3 mod (xC^2-C+1), and Irwin g.f. == Catalan through x^30.
    ```
- **Gate 2 Novelty Receipts:** `notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, and `notes/novelty-gate2-watch-6.md` all report **PASS** (open and uncontested across 618 snapshots including `zenodo-23112421-oeis-ids.md`, live OEIS rev. 55, arXiv, Zenodo, GitHub, and web search).

**Conclusion:** Proof is elementary, completely self-contained, algebraically rigorous, and independently verified. Ready for Gate 3 freshness check (`<1h`) before reporting.

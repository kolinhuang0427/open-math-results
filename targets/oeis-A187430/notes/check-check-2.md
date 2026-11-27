# Check Report: `targets/oeis-A187430/` (`@check-2`)

- **Primary Source Fidelity:** Verified against live OEIS **A187430** (revision 55, offset `0,3`, Irwin Jan 13 2017 conjecture). `TARGET.md` and `PROOF.md` match the walk definition (`steps {-2,-1,+1,+2}`, nonnegative heights, start/end `0`) and Irwin's formal power series identity $1 + \sum_{n \ge 0} a(n) \frac{(-1)^n x^{n+1}}{(1-x)^{2n+2}} = C(x)$ verbatim.
- **Proof & Computation Verification (`check-check-2.py` -> `PASS`):**
  - **Direct Walk DP:** Computed $w(n, h)$ directly from the primary nonnegative-walk definition ($0 \le n \le 32$), reproducing all 29 live OEIS rev. 55 data terms ($n = 0..28$).
  - **Step 1 (Kernel Equation):** Verified $u^2 G(t, u) = u^2 + t(u^4 + u^3 + u + 1)G(t, u) - t(u+1)A(t) - t u G_1(t)$ across all $(n, m)$ with $0 \le n \le 32$ and $0 \le m \le 2n+2$.
  - **Step 2 (Kernel Elimination):** Verified exact rational identity $K(t, u) = M(t, u) Q(t, u)$ in $\mathbb{Q}(y)[u]$ after substituting $t = \frac{y(1-y)^2}{(1-y+y^2)^2}$ and $s = \frac{y}{1-y}$, verified exact formal series reversion $f(t A(t)) = t \bmod t^{33}$ and $G_1(t) = (s(t) - y(t))/t \bmod t^{32}$, and confirmed the $t$-adic module reduction $\mathbb{Z}[u][[t]] \to \mathbb{Z}[[t]][u]/(M(t,u))$ yields $t A(t) = y(t)$.
  - **Step 3 (Catalan Identification):** Verified $(1-x)^2(1-C)C^2 + x(C^2 - C + 1)^2 \equiv 0 \pmod{x C^2 - C + 1}$ in $\mathbb{Z}[x, C]$ with $1 - Y(x) + Y(x)^2$ a unit in $\mathbb{Z}[[x]]$, and verified directly that $1 + \sum_{n=0}^{29} a(n)\frac{(-1)^n x^{n+1}}{(1-x)^{2n+2}} \equiv C(x) \pmod{x^{31}}$.
- **Script & Result:** `.venv/bin/python -u targets/oeis-A187430/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

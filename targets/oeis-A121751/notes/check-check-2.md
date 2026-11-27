# Check Report: `targets/oeis-A121751/` (`@check-2`)

- **Primary Source Fidelity:** Verified against live OEIS **A121751** (revision 5, offset `1,3`, Mathar Jul 26 2022 conjecture). `TARGET.md` matches the primary definition of $a(n)$, initial conditions $a(1)=0, a(2)=1$, Mathar's 7-term recurrence $M(n) = \sum_{j=0}^6 C_j(n) a(n-j) = 0$, and domain $n \ge 7$ verbatim.
- **Proof Verification (`PROOF.md`):**
  - **Step 1:** Both even ($m = 2r \ge 4$) and odd ($m = 2r+1 \ge 3$) floor-recurrence splits match the primary formula identically (tested for $m = 3..200$).
  - **Step 2:** Both 5-step reductions ($n = 2k$, $k \ge 4$; $n = 2k+1$, $k \ge 3$) match the parity rules, and exact univariate polynomial arithmetic in $\mathbb{Z}[k]$ via SymPy confirms $A_{\mathrm{even}}(k) = B_{\mathrm{even}}(k) = A_{\mathrm{odd}}(k) = B_{\mathrm{odd}}(k) \equiv 0$. Direct integer checks confirm $M(n) = 0$ for $7 \le n \le 100$.
  - **Step 3:** Summing $M(n)\frac{x^{n-6}}{(n-6)!}$ over $n \ge 7$ produces a 6th-order linear ODE with leading coefficient $16(x-2)^2(x+2)^2 \ne 0$ on $\hat{y}^{(6)}(x)$ and constant inhomogeneous term $-20$; differentiating once annihilates the constant to give a non-trivial 7th-order homogeneous linear ODE with polynomial coefficients (verified on the truncated EGF through $x^{23}$).
- **Script & Result:** `.venv/bin/python -u targets/oeis-A121751/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

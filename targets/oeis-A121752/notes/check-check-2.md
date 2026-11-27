# Check Report: `targets/oeis-A121752/` (`@check-2`)

- **Primary Source Fidelity:** Verified against live OEIS **A121752** (revision 4, offset `1,2`, Mathar Jul 26 2022 conjecture). `TARGET.md` matches the primary definition of $a(n)$, initial conditions $a(1)=1, a(2)=2$, Mathar's 6-term recurrence $M(n) = \sum_{j=0}^5 C_j(n) a(n-j) = 0$, and domain $n \ge 6$ verbatim.
- **Proof Verification (`PROOF.md`):**
  - **Step 1:** $D(k) = a(k) - k a(k-1) = (k-3)! S(k)$ for $k \ge 3$ and parity formulas $f(2m)=4m-3$, $f(2m+1)=2m-1$, $S(2r)=(r-1)(4r^2-3r+1)$, $S(2r+1)=r^2(4r-3)$ hold identically (verified numerically for $k=3..80$ and against all 19 OEIS rev. 4 terms).
  - **Step 2:** Exact symbolic identity $M(n) = \sum_{i=0}^4 e_i(n) D(n-i)$ holds in $\mathbb{Z}[n]$.
  - **Step 3:** Both parity polynomials $P_{\mathrm{even}}(r)$ and $P_{\mathrm{odd}}(r)$ vanish identically in $\mathbb{Z}[r]$ (with $e_4(6)=0$ cleanly handling $n=6$), and $M(n) = 0$ holds directly for $n=6..80$. Summing $M(n)\frac{x^{n-5}}{(n-5)!}$ over $n \ge 6$ yields a non-trivial 5th-order linear ODE with leading coefficient $(x-1)(1223x^3 - 8897x^2 - 4443x + 1077) \ne 0$ (verified through $x^{19}$), proving $\hat{y}(x)$ is D-finite.
- **Script & Result:** `.venv/bin/python -u targets/oeis-A121752/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

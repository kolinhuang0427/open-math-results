# Check Report: `targets/oeis-A121750/` (`@check-2`)

- **Primary Source Fidelity:** Verified against live OEIS **A121750** (revision 13, offset `1,3`, Mathar Jul 26 2022 conjecture). `TARGET.md` matches the primary definitions of $d(n)$ and $a(n)$, initial conditions $a(1)=0, d(1)=1, d(2)=0$, Mathar's 7-term recurrence $M(n) = \sum_{j=0}^6 C_j(n) a(n-j) = 0$, and domain $n \ge 7$ verbatim.
- **Proof Verification (`PROOF.md`):**
  - **Step 1:** $W(k) = D(k) + D(k-1) = a(k) - (k-1)a(k-1) - (k-1)a(k-2)$ eliminates $d$, giving $W(2m) = (2m-2)!(2m^2-2m)$ ($m \ge 2$) and $W(2m+1) = (2m-1)!(2m^2+m)$ ($m \ge 1$) (verified against primary sequence for $k = 3..80$ and all 19 live OEIS rev. 13 terms).
  - **Step 2:** Exact symbolic identity $M(n) = \sum_{i=0}^4 c_i(n) W(n-i)$ holds identically in $\mathbb{Z}[n]$.
  - **Step 3:** Both parity polynomials $P_{\mathrm{even}}(r)$ ($r \ge 4$) and $P_{\mathrm{odd}}(r)$ ($r \ge 3$) vanish identically in $\mathbb{Z}[r]$, and $M(n) = 0$ holds directly for $n = 7..80$.
  - **Step 4:** Summing $M(n)\frac{x^{n-6}}{(n-6)!}$ over $n \ge 7$ produces a 6th-order linear ODE with leading coefficient $(1-x)^2(1+x) \ne 0$ on $\hat{y}^{(6)}(x)$ and constant inhomogeneous term $-3$; differentiating once yields a non-trivial 7th-order homogeneous linear ODE with polynomial coefficients (verified on the truncated EGF through $x^{18}$).
- **Script & Result:** `.venv/bin/python -u targets/oeis-A121750/notes/check-check-2.py` -> `PASS`.
- **Gate 2 Status:** `PASS` (`notes/novelty-gate2-watch-1.md`, `notes/novelty-gate2-watch-5.md`, `notes/novelty-gate2-watch-6.md`).

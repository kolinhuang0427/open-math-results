# Check Report — `oeis-A024199` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** Live OEIS entry `https://oeis.org/search?q=id:A024199&fmt=text` (`%I A024199 #80 Jun 28 2026 15:47:50`).
- **`TARGET.md` check:**
  - Revision (`rev. 80`), `%N` definition `a(n) = (2n-1)!! * Sum_{k=0..n-1}(-1)^k/(2k+1)`, `%O` (`0,3`), `%S..%U` initial 21 terms (`a(0)=0` through `a(20)=247199273204273879989500`), and Peter Bala's Nov 15, 2016 `%F` conjecture + e.g.f. block match the live OEIS record verbatim.
  - Both `TARGET.md` (L30) and `PROOF.md` (L10-12) accurately resolve the minor notation typo in Bala's parenthetical remark (`(2*N - 1)!!` vs. `M!! = 2^((M+1)/2)*Gamma(M/2+1)/sqrt(Pi)` at odd `M = 2N - 1`), giving the standard Gamma continuation $(2m-1)!! = 2^m \Gamma(m+1/2)/\sqrt{\pi}$ for all $m \in \mathbb{Z}$.

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–84:
  - **Lemma 1** ($(2m-1)(2m-3)!! = (2m-1)!!$ for all $m \in \mathbb{Z}$): verified algebraically and across $m \in [-40, 40]$. *(Harmless parenthetical slip in L12: at $r = 1$, $2r - 1 = 1$, so the denominator in $(-1)^r/(2r-1)!!$ is $1!! = 1$, whereas $(-1)!! = 1$ corresponds to $m = 0$ / $r = 0$; this does not affect Lemma 1 or any subsequent step.)*
  - **Lemma 2** ($a(n) - (2n-1)a(n-1) = (-1)^{n-1}(2n-3)!!$ for $n \ge 1$, $a(0)=0$): verified directly from the NAME definition.
  - **Theorem 1** ($a(n) = \frac{1}{2}\sum_{k=0}^{2n-1}(-1)^{n-k+1}k!(2n-2k-3)!!$ for all $n \ge 1$): verified base case $n=1$ ($T(1,0)=T(1,1)=1 \implies b(1)=1=a(1)$), row-shift identities $T(n,k) = -(2n-2k-3)T(n-1,k)$ and $T(n,k+1) = (k+1)T(n-1,k)$, telescoping identity, exact cancellation $T(n,2n-2) = T(n,2n-1) = 2^{n-1}(n-1)!$, and $T(n,0) = (-1)^{n-1}(2n-3)!!$.
  - **Theorem 2** (EGF $Y(x) = \frac{\arcsin(2x)}{2\sqrt{1-2x}}$ in $\mathbb{Q}[[x]]$): verified first-order linear ODE $(1-2x)Y'(x)-Y(x) = (1+2x)^{-1/2}$ and integrating factor $(1-2x)^{1/2}$.

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A024199/notes/check-check-3.py) (zero floating-point literals/operations; `FLOAT_COUNT: 0` via Python AST check).
- Checks performed in `Fraction`/`int`:
  1. Direct NAME formula matches all 21 OEIS `%S..%U` terms ($n=0..20$) and Sloane's recurrence $a(n+1) = 2a(n) + (2n-1)^2 a(n-1)$ ($n=1..49$).
  2. Lemma 1 for all $m \in [-40, 40]$; Lemma 2 for all $n \in [1, 50]$.
  3. Theorem 1 row identities, boundary values, and telescoping identity for $n \in [2, 30]$, $0 \le k \le 2n-3$, and exact equality $b(n) = a(n)$ for $n \in [1, 50]$.
  4. Theorem 2 formal power series ODE check modulo $x^{40}$ and exact series product $\frac{1}{2}\arcsin(2x)(1-2x)^{-1/2} \pmod{x^{41}}$ matching $\sum_{n=0}^{40} a(n)x^n/n!$.
- Command & output:
  ```
  .venv/bin/python -u targets/oeis-A024199/notes/check-check-3.py && ...
  PASS
  FLOAT_COUNT: 0
  ```

# Check Report — `oeis-A028495` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** Live OEIS entries `A028495` (`%I A028495 #162`), `A160389` (`%I A160389 #125`), and `A116425` (`%I A116425 #57`).
- **`TARGET.md` check:** Revision (`rev. 162`), `%N` definition (`Expansion of g.f. (1-x^2)/(1-x-2*x^2+x^3).`), `%O` (`0,3`), `%S..%U` initial 37 terms ($a(0)=1$ through $a(36)=874055885$), Bill McEachen's Feb 11, 2026 `%F` conjectures, and the referenced `%N` definitions of `A160389` (`Decimal expansion of 2*cos(Pi/7).`) and `A116425` (`Decimal expansion of 2 + 2*cos(2*Pi/7).`) match the live OEIS records verbatim. *(Minor cosmetic note: `TARGET.md` L28–29 cites `A160389 (rev. 12)` and `A116425 (rev. 11)`, whereas live OEIS shows `#125` and `#57`, with identical `%N` definitions.)*

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–42:
  - **Lemma 1:** Cyclotomic identity $(\zeta^7+1)/(\zeta+1) = \zeta^3 P(\zeta+\zeta^{-1})$ for $P(r) = r^3 - r^2 - 2r + 1$, giving distinct real roots $r_1 = 2\cos(\pi/7) > r_2 = 2\cos(3\pi/7) > r_3 = 2\cos(5\pi/7)$. Rational endpoint signs isolate $r_3 \in (-3/2, -1)$, $r_2 \in (0, 1/2)$, $r_1 \in (3/2, 2)$, hence $r_1 > |r_3| > r_2 > 0$, and $2\cos(\pi/7) = \sqrt{2 + 2\cos(2\pi/7)} > 0$.
  - **Theorem:** Partial fraction expansion $a(n) = \sum_{j=1}^3 \frac{r_j^2 - 1}{P'(r_j)} r_j^n$ for all $n \ge 0$, with $c_1 > 0$ and $|r_2/r_1| < 1/3 < 1$, $|r_3/r_1| < 1$, yielding $\lim_{n\to\infty} a(n)/a(n-1) = r_1$.

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A028495/notes/check-check-3.py) (`int`/`Fraction` + SymPy exact algebra, `FLOAT_COUNT: 0`).
- Checked:
  1. Recurrence $a(n) = a(n-1) + 2a(n-2) - a(n-3)$ matches all 37 OEIS `%S..%U` terms ($n=0..36$).
  2. Exact rational signs of $P(r)$ at $\{-3/2, -1, 0, 1/2, 3/2, 2\}$, symbolic cyclotomic factorization, companion-matrix trace verification of $\sum_{j=1}^3 c_j r_j^n = a(n)$ for $n=0..29$, exact minimal polynomial relation $(r_1^2 - 2)^3 + (r_1^2 - 2)^2 - 2(r_1^2 - 2) - 1 = 0 \pmod{P(r_1)}$, and 120-step exact rational bisection verifying $|a(120)/a(119) - r_1| < 10^{-8}$.
- Output:
  ```
  PASS
  FLOAT_COUNT: 0
  ```

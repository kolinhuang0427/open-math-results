# Check Report — `oeis-A014137` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** Live OEIS entry `https://oeis.org/search?q=id:A014137&fmt=text` (`%I A014137 #180 Aug 07 2026 18:53:11`).
- **`TARGET.md` check:** Revision (`rev. 180`), `%N` definition (`Partial sums of Catalan numbers (A000108).`), `%O` (`0,2`), `%S..%U` initial 29 terms ($a(0)=1$ through $a(28)=358268702159069$), and `%F` formulas including Sergei N. Gladkovskii's May 14, 2013 continued fraction conjecture match the live OEIS record verbatim.

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–49:
  - **Lemma 1:** Two-step Catalan ratios $r_1(k) = C_{2k+1}/C_{2k} = (4k+1)/(k+1)$ and $r_2(k) = C_{2k+2}/C_{2k+1} = 2(4k+3)/(2k+3)$.
  - **Lemma 2:** Shift identity $Q(k) = 1 + r_1(k)x + r_1(k)r_2(k)x^2 Q(k+1)$.
  - **Theorem:** Bottom-up unit evaluation $D_2 = (2k+3)(1+r_2 x q)/q$ and $D_1 = (k+1)/(1+r_2 x q)$ yields $1 + (4k+1)x/D_1 = Q(k)$, exact truncation discrepancy $Q^{(K)}(0) - Q(0) = C_{2K+2}x^{2K+2}(1 - Q(K+1)) \in x^{2K+3}\mathbb{Q}[[x]]$, and uniform analytic convergence on compact subsets of $\{|x| < 1/4\}$.

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A014137/notes/check-check-3.py) (pure `int`/`Fraction` formal power series arithmetic modulo $x^{40}$, `FLOAT_COUNT: 0`).
- Checked all 29 OEIS `%S..%U` terms ($n=0..28$), Lemma 1 ($k=0..10$), exact 3-step CF collapse for $k=0..10$ mod $x^{40}$, $Q(0)/(1-x) = A(x)$, and exact error formula + $x^{2K+3}$ convergence for $K=0..11$.
- Output:
  ```
  PASS
  FLOAT_COUNT: 0
  ```

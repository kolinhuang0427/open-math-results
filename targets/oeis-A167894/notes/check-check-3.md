# Check Report — `oeis-A167894` (check-3)

## Primary Source & Statement Fidelity
- **Primary source checked:** Live OEIS entry `https://oeis.org/search?q=id:A167894&fmt=text` (`%I A167894 #83 Jan 02 2026 20:45:39`).
- **`TARGET.md` check:** Revision (`rev. 83`), `%N` definition (`Expansion of g.f.: 1/(Sum_{k >= 0} k!*x^k).`), `%O` (`0,4`), `%S..%U` initial 20 terms ($a(0)=1$ through $a(19)=-108355864447215063$), and Sergei N. Gladkovskii's Nov 19, 2013 `%F` continued fraction conjecture match the live OEIS record verbatim.

## Proof Verification (`PROOF.md`)
- Audited `PROOF.md` lines 1–31:
  - **Lemma 1:** Shift identity $P_{k-1}(x) = 1 + kx P_k(x)$ for $P_k(x) = \sum_{m\ge 0} \frac{(k+m)!}{k!}x^m$ and $P_{-1}(x) = 1$.
  - **Theorem:** Setting $Q(k) = P_{k-1}(x)/P_k(x) \in \mathbb{Z}[[x]]^\times$ gives $Q(0) = 1/P_0(x) = A(x)$ and $Q(k) = 1 + kx - (k+1)x/Q(k+1)$, and $x$-adic contraction $\mathrm{ord}_x(T_k(q_1)-T_k(q_2)) \ge 1 + \mathrm{ord}_x(q_1 - q_2)$ proves $Q^{(K)}(0) - A(x) \in x^{K+2}\mathbb{Z}[[x]]$ (for seeds $1 + O(x)$) and $\in x^{K+1}\mathbb{Z}[[x]]$ (for general unit seeds).

## Mechanical Verification
- Independent verifier: [check-check-3.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A167894/notes/check-check-3.py) (pure `int`/`Fraction` formal power series arithmetic mod $x^{32}$, `FLOAT_COUNT: 0`).
- Checked all 20 OEIS `%S..%U` terms ($n=0..19$), Lemma 1 ($k=0..10$), CF step ($k=0..10$), and finite truncations $K=0..15$ with both seed $1$ ($O(x^{K+2})$) and unit seed $2+x$ ($O(x^{K+1})$).
- Output:
  ```
  PASS
  FLOAT_COUNT: 0
  ```

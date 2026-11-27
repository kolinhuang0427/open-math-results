# Blind Check Report — `targets/oeis-A127276/` (`check-2`)

**Verdict: PASS** (Gate 2 novelty pending — pinging `@watch-1`).

## 1. Primary Source & `TARGET.md` Fidelity
- **Primary sources checked:** Live OEIS JSON for [A127276](https://oeis.org/A127276) (`rev. 33`, `2026-11-25T15:43:26-05:00`) and [A127275](https://oeis.org/A127275) (`rev. 18`).
- **`TARGET.md` comparison:** Matches verbatim — `A127276` `NAME: Hankel transform of A127275.`, `FORMULA: Conjectured g.f.: -(4*x-1)*(x-1) / ( (2*x-1)^3 ) and a(n) = 2^n-n*(n+1)*2^(n-2). - _R. J. Mathar_, Dec 11 2010`, and `A127275` `NAME: Expansion of (sqrt(1-4x)-x)/(1-4x).` (`DATA` offset `0`, matching `1,1,-2,-16,-64,-208,-608,...`).

## 2. Independent Exact-Arithmetic Verification
- **Verifier script:** [targets/oeis-A127276/notes/check-check-2.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A127276/notes/check-check-2.py) (zero floating-point arithmetic; pure-Python `int`, `fractions.Fraction`, `math.comb`, and exact integer Bareiss determinant).
- **Command & result:** `.venv/bin/python -u targets/oeis-A127276/notes/check-check-2.py` exited with code `0` (`PASS`):
  1. `A127275 series`: verified $(1-4x)B(x) = \sqrt{1-4x}-x$, $b_0=1$, $b_m = \binom{2m}{m} - 4^{m-1}$ ($1 \le m \le 50$), and exact match with all 26 live OEIS `A127275` `DATA` terms.
  2. `Lemma 1 & diagonalization`: verified $[z^0](z+2+z^{-1})^m = \binom{2m}{m}$, $P_k(z+2+z^{-1}) = z^k + z^{-k}$, $P_k(4) = 1\ (k=0),\ 2\ (k\ge 1)$, $P_k(0) = 1\ (k=0),\ 2(-1)^k\ (k\ge 1)$, and exact matrix identity $P C_n P^T = \mathrm{diag}(1,2,\dots,2)$ for $n \le 25$.
  3. `Rank-2 decomposition & Weinstein–Aronszajn`: verified $M_n = C_n - \frac{1}{4}vv^T + \frac{1}{4}e_0e_0^T$, $C_n C_n^{-1} = I_{n+1}$ ($C_n^{-1} = P^T D^{-1} P$), $v^T C_n^{-1} v = e_0^T C_n^{-1} e_0 = 2n+1$, $v^T C_n^{-1} e_0 = (-1)^n$, $\det(I_2 + V^T C_n^{-1} U) = 1 - \frac{n(n+1)}{4}$, direct exact integer Bareiss determinant $\det(M_n) = 2^n - n(n+1)2^{n-2}$, and all 26 live OEIS `A127276` `DATA` terms ($n=0..25$).
  4. `Ordinary g.f.`: verified $(1-2x)^3 \sum_{n\ge 0} a(n) x^n \equiv 1 - 5x + 4x^2 = -(4x-1)(x-1) \pmod{x^{41}}$.

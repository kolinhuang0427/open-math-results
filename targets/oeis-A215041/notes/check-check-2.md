# Blind Check Report — `targets/oeis-A215041/` (`check-2`)

**Verdict: PASS** (Gate 2 novelty pending — pinging `@watch-1`).

## 1. Primary Source & `TARGET.md` Fidelity
- **Primary sources checked:** Live OEIS JSON for [A215041](https://oeis.org/A215041) (`rev. 10`, `2023-12-25T18:06:42-05:00`) and Wolfdieter Lang `arXiv:1210.1018` (`ArXivngonGalois2017.tex` L541–555 and L927–928 Open Problems).
- **`TARGET.md` comparison:** Matches verbatim — `a(n) = n^{\delta(n)}/\operatorname{Disc}(C(n,x))` for minimal polynomials $C(n,x)$ of $2\cos(\pi/n)$, with $a(1)=1$, $a(2^k)=2$, $a(p^k)=p^{(p^{k-1}+1)/2}$ for odd prime $p$ and $k \ge 1$, and $a(n) = \prod_{\text{odd } p \mid n} p^{\delta(n)/(p-1)}$ otherwise.

## 2. Independent Exact-Arithmetic Verification
- **Verifier script:** [targets/oeis-A215041/notes/check-check-2.py](file:///Users/kolinhuang/Documents/open-math/targets/oeis-A215041/notes/check-check-2.py) (zero floating-point arithmetic; uses exact `sympy` integers/polynomials over $\mathbb{Z}$).
- **Command & result:** `.venv/bin/python -u targets/oeis-A215041/notes/check-check-2.py` exited with code `0` (`PASS`):
  1. `Minimal polynomials C(n,x)`: verified exact match against `sp.minimal_polynomial(2*cos(pi/n), x)` for $n=1..24$, irreducibility over $\mathbb{Z}$, degree $\delta(n) = \varphi(2n)/2$, and $\Phi_{2n}(z) = z^{\delta(n)} C(n, z+z^{-1})$ for $n=2..60$.
  2. `Lemma 1`: verified $\Phi_k(1) \in \{q, 1\}$ for $k=2..160$ and exact $|\mathrm{Disc}(\Phi_m)| = m^{\varphi(m)}/\prod_{q\mid m} q^{\varphi(m)/(q-1)}$ against direct `sp.discriminant(Phi_m)` for $m=2..80$.
  3. `Lemmas 2 & 3`: verified cyclotomic negation identities $\Phi_{2n}(-z) = \Phi_n(z)$ ($n$ odd) and $\Phi_{2n}(-z) = \Phi_{2n}(z)$ ($n$ even with odd prime factor), $|C(n,2)C(n,-2)| \in \{4, p, 1\}$ ($n=2..80$), and $\mathrm{Disc}(C(n,x))^2 = |\mathrm{Disc}(\Phi_{2n})| / |C(n,2)C(n,-2)|$ ($n=2..60$).
  4. `Main Theorem`: verified exact integer divisibility $\mathrm{Disc}(C(n,x)) \mid n^{\delta(n)}$ and $n^{\delta(n)}/\mathrm{Disc}(C(n,x)) = a(n)$ across all three conjectured cases for $n=1..60$, matching all 55 live OEIS `A215041` `DATA` terms.

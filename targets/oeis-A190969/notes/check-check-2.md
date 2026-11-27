# Independent Check Report: `targets/oeis-A190969`

- **Checker:** `@check-2`
- **Verdict:** **PASS**
- **Check Script:** `targets/oeis-A190969/notes/check-check-2.py`

## 1. Primary Source Fidelity
Checked against live OEIS `A190969` JSON (`revision: 48`, `2025-11-05T15:22:20-05:00`) and `google-deepmind/formal-conjectures` (`FormalConjectures/OEIS/190969.lean`, fetched via `gh api`):
- Recurrence `a(n) = 5*a(n-1) - 8*a(n-2)`, `a(0)=0, a(1)=1`, and sum `S(p) := Sum_{k=0..p-1} a(4k)*binomial(2k,k)^3/(-4096)^k` match OEIS `A190969` verbatim.
- `conjecture_1` (`sMod p 2 = 0` for all primes `p != 2`) and `conjecture_2` (`sMod p 3 = 0` for all primes `p != 2` with `p % 7 in {1, 2, 4}`) match `FormalConjectures/OEIS/190969.lean` and `TARGET.md` verbatim.
- Beukers citation (`arXiv:2403.03301v3`, `SupercongruencesRevise.tex`) checked: Assumption (II) (lines 570–584), Remark item 2 (lines 597–606), Theorem `\label{thm:CMpoints3}` (lines 610–622), and Appendix C subsection `Hypergeometric F(1/2,1/2,1/2;1,1|64t)` (lines 2158–2181) match the hypotheses and conclusions invoked in `PROOF.md` §3.

## 2. Independent Exact Mechanical Checks
Command:
```sh
.venv/bin/python targets/oeis-A190969/notes/check-check-2.py
```
Output:
```
PASS (checked Sec 2-5 lemmas, 61 odd primes <= 300 for conj_1, 27 split primes <= 300 for conj_2)
```
All checks use exact integer / `fractions.Fraction` / $\mathbb{Q}(\sqrt{-7})$ / modular arithmetic (zero floating point):
- **§2 Algebraic decomposition:** Binet formula verified for $0 \le n \le 40$; $\alpha^2, \alpha^4, \beta^4, t_1, t_2$, identity (2.1) for primes $3 \le p \le 23$, and polynomial factorization (2.2) verified identically.
- **§3 Split primes:** $q$-series identities (3.1), (3.2), and $F(t(\tau)) = \Theta(\tau)$ verified to $O(q^{26})$ in $\mathbb{Z}\llbracket q \rrbracket$; Lemma 3.2 ($p = x^2 + 7y^2$) and Proposition 3.3 (Beukers Theorem 1.15 congruences $F_p(\iota(t_1)) \equiv F_p(\iota(t_2)) \equiv \iota(x+ys)^2 \pmod{p^3}$ and $S(p) \equiv 0 \pmod{p^3}$) verified for all 27 split primes $p \le 300$.
- **§4 Inert primes:** Lemma 4.1 differential operator identity and finite Clausen polynomial identity (4.1) verified identically in $\mathbb{Q}[u]$ for $0 \le m \le 15$; `[x^{p-1}](x(x-1)(x-\lambda))^m = (-1)^m H_p(\lambda)` verified for $1 \le m \le 14$; $u_1(1-u_1) = 16t_1$, norms, and $j(E_{u_1}) = -3375$ verified in $\mathbb{Q}(\sqrt{-7})$; Lemma 4.2(1)–(2) polynomial congruences verified for all odd primes $p \le 47$; Proposition 4.3 ($H_p(u_1) \equiv 0 \pmod p$, $P_m(1-2u_1)^2 \equiv 0 \pmod{p^2}$, $F_p(t_{1,2}) \equiv 0 \pmod{p^2}$) verified for all inert primes $p \le 150$.
- **§5 Ramified prime $p=7$:** Recurrence for $a(4k)$, $(-4096)^{-1} \equiv 27 \pmod{49}$, all 7 summands $T_0,\dots,T_6 \pmod{49}$, $S(7) \equiv 0 \pmod{49}$, and $S(7) \equiv 294 \pmod{343}$ verified.
- **Direct conjecture sweep:** `sMod p 2 == 0` verified for all 61 odd primes $p \le 300$, and `sMod p 3 == 0` verified for all 27 split primes $p \equiv 1,2,4 \pmod 7$ with $p \le 300$.

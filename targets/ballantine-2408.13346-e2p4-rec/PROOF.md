# Proof of Ballantine–Beck–Merca `arXiv:2408.13346v1` Conjectured Linear Recurrence for $e_2p_4(n)$

**Result:** **TRUE** (complete generating-function proof that $e_2p_4(n)$ satisfies the conjectured 22-term linear recurrence for **all** $n \ge 0$).

---

## 1. Bijective Parameterization of $\mathcal{P}(4, n)$

Every integer partition $\lambda = (\lambda_1, \lambda_2, \lambda_3, \lambda_4)$ of $n$ into $4$ parts ($\lambda_1 \ge \lambda_2 \ge \lambda_3 \ge \lambda_4 \ge 1$, $\sum_{i=1}^4 \lambda_i = n$) corresponds bijectively to a $4$-tuple $(y_1, y_2, y_3, y_4) \in \mathbb{Z}_{\ge 0}^3 \times \mathbb{Z}_{\ge 1}$ via
$$y_1 = \lambda_1 - \lambda_2 \ge 0, \qquad y_2 = \lambda_2 - \lambda_3 \ge 0, \qquad y_3 = \lambda_3 - \lambda_4 \ge 0, \qquad y_4 = \lambda_4 \ge 1,$$
with inverse
$$\lambda_4 = y_4, \qquad \lambda_3 = y_4 + y_3, \qquad \lambda_2 = y_4 + y_3 + y_2, \qquad \lambda_1 = y_4 + y_3 + y_2 + y_1,$$
and size
$$|\lambda| = \lambda_1 + \lambda_2 + \lambda_3 + \lambda_4 = y_1 + 2y_2 + 3y_3 + 4y_4.$$

Expanding $e_2(\lambda) = \sum_{1 \le i < j \le 4} \lambda_i \lambda_j$ in terms of $(y_1, y_2, y_3, y_4)$ yields the exact $9$-term polynomial identity:
$$e_2(\lambda) = y_1 y_2 + 2y_1 y_3 + 3y_1 y_4 + y_2^2 + 4y_2 y_3 + 6y_2 y_4 + 3y_3^2 + 9y_3 y_4 + 6y_4^2.$$
*(Quick check: setting $y_1=y_2=y_3=0$ gives $\lambda=(y_4,y_4,y_4,y_4)$ and $e_2 = \binom{4}{2}y_4^2 = 6y_4^2$; matching all mixed and pure quadratic coefficients gives $(y_4+y_3+y_2+y_1)(3y_4+2y_3+y_2) + (y_4+y_3+y_2)(2y_4+y_3) + (y_4+y_3)y_4$, which expands to the exact $9$ terms above.)*

---

## 2. Exact Rational Generating Function of $e_2p_4(n)$

Let $G(q) = \sum_{n=0}^\infty e_2p_4(n)\, q^n$ as a formal power series in $\mathbb{Z}[[q]]$. Using the elementary geometric series identities (valid in $\mathbb{Z}[[x]]$):
$$\sum_{y \ge 0} x^y = \frac{1}{1-x}, \qquad \sum_{y \ge 0} y x^y = \frac{x}{(1-x)^2}, \qquad \sum_{y \ge 0} y^2 x^y = \frac{x(1+x)}{(1-x)^3},$$
$$\sum_{y \ge 1} x^y = \frac{x}{1-x}, \qquad \sum_{y \ge 1} y x^y = \frac{x}{(1-x)^2}, \qquad \sum_{y \ge 1} y^2 x^y = \frac{x(1+x)}{(1-x)^3},$$
summing each of the $9$ monomials of $e_2(\lambda)\, q^{y_1 + 2y_2 + 3y_3 + 4y_4}$ over $y_1, y_2, y_3 \ge 0$ and $y_4 \ge 1$ factors completely by variable separation (with $x = q, q^2, q^3, q^4$ respectively):
1. $y_1 y_2$: $\dfrac{q}{(1-q)^2} \cdot \dfrac{q^2}{(1-q^2)^2} \cdot \dfrac{1}{1-q^3} \cdot \dfrac{q^4}{1-q^4} = \dfrac{q^7}{(1-q)^6 (1+q)^3 (1+q^2) (1+q+q^2)}$
2. $2y_1 y_3$: $2 \cdot \dfrac{q}{(1-q)^2} \cdot \dfrac{1}{1-q^2} \cdot \dfrac{q^3}{(1-q^3)^2} \cdot \dfrac{q^4}{1-q^4} = \dfrac{2q^8}{(1-q)^6 (1+q)^2 (1+q^2) (1+q+q^2)^2}$
3. $3y_1 y_4$: $3 \cdot \dfrac{q}{(1-q)^2} \cdot \dfrac{1}{1-q^2} \cdot \dfrac{1}{1-q^3} \cdot \dfrac{q^4}{(1-q^4)^2} = \dfrac{3q^5}{(1-q)^6 (1+q)^3 (1+q^2)^2 (1+q+q^2)}$
4. $y_2^2$: $\dfrac{1}{1-q} \cdot \dfrac{q^2(1+q^2)}{(1-q^2)^3} \cdot \dfrac{1}{1-q^3} \cdot \dfrac{q^4}{1-q^4} = \dfrac{q^6}{(1-q)^6 (1+q)^4 (1+q+q^2)}$
5. $4y_2 y_3$: $4 \cdot \dfrac{1}{1-q} \cdot \dfrac{q^2}{(1-q^2)^2} \cdot \dfrac{q^3}{(1-q^3)^2} \cdot \dfrac{q^4}{1-q^4} = \dfrac{4q^9}{(1-q)^6 (1+q)^3 (1+q^2) (1+q+q^2)^2}$
6. $6y_2 y_4$: $6 \cdot \dfrac{1}{1-q} \cdot \dfrac{q^2}{(1-q^2)^2} \cdot \dfrac{1}{1-q^3} \cdot \dfrac{q^4}{(1-q^4)^2} = \dfrac{6q^6}{(1-q)^6 (1+q)^4 (1+q^2)^2 (1+q+q^2)}$
7. $3y_3^2$: $3 \cdot \dfrac{1}{1-q} \cdot \dfrac{1}{1-q^2} \cdot \dfrac{q^3(1+q^3)}{(1-q^3)^3} \cdot \dfrac{q^4}{1-q^4} = \dfrac{3q^7(1-q+q^2)}{(1-q)^6 (1+q) (1+q^2) (1+q+q^2)^3}$
8. $9y_3 y_4$: $9 \cdot \dfrac{1}{1-q} \cdot \dfrac{1}{1-q^2} \cdot \dfrac{q^3}{(1-q^3)^2} \cdot \dfrac{q^4}{(1-q^4)^2} = \dfrac{9q^7}{(1-q)^6 (1+q)^3 (1+q^2)^2 (1+q+q^2)^2}$
9. $6y_4^2$: $6 \cdot \dfrac{1}{1-q} \cdot \dfrac{1}{1-q^2} \cdot \dfrac{1}{1-q^3} \cdot \dfrac{q^4(1+q^4)}{(1-q^4)^3} = \dfrac{6q^4(1+q^4)}{(1-q)^6 (1+q)^4 (1+q^2)^3 (1+q+q^2)}$.

*(Notice in (4) and (7) that $1+q^2$ cancels in (4) and $1+q^3 = (1+q)(1-q+q^2)$ simplifies (7).)*

Let
$$D(q) = (1-q)^6 (1+q)^4 (1+q^2)^3 (1+q+q^2)^3.$$
Every one of the $9$ denominators divides $D(q)$ in $\mathbb{Z}[q]$. Putting all $9$ fractions over $D(q)$ gives the $9$ polynomial numerators:
- Term 1: $q^7 + 3q^8 + 7q^9 + 11q^{10} + 14q^{11} + 14q^{12} + 11q^{13} + 7q^{14} + 3q^{15} + q^{16}$
- Term 2: $2q^8 + 6q^9 + 12q^{10} + 18q^{11} + 20q^{12} + 18q^{13} + 12q^{14} + 6q^{15} + 2q^{16}$
- Term 3: $3q^5 + 9q^6 + 18q^7 + 24q^8 + 24q^9 + 18q^{10} + 9q^{11} + 3q^{12}$
- Term 4: $q^6 + 2q^7 + 6q^8 + 8q^9 + 13q^{10} + 12q^{11} + 13q^{12} + 8q^{13} + 6q^{14} + 2q^{15} + q^{16}$
- Term 5: $4q^9 + 8q^{10} + 16q^{11} + 20q^{12} + 20q^{13} + 16q^{14} + 8q^{15} + 4q^{16}$
- Term 6: $6q^6 + 12q^7 + 24q^8 + 24q^9 + 24q^{10} + 12q^{11} + 6q^{12}$
- Term 7: $3q^7 + 6q^8 + 9q^9 + 15q^{10} + 15q^{11} + 15q^{12} + 15q^{13} + 9q^{14} + 6q^{15} + 3q^{16}$
- Term 8: $9q^7 + 18q^8 + 27q^9 + 27q^{10} + 18q^{11} + 9q^{12}$
- Term 9: $6q^4 + 12q^5 + 18q^6 + 12q^7 + 12q^8 + 12q^9 + 18q^{10} + 12q^{11} + 6q^{12}$.

Summing these $9$ polynomials term-by-term gives
$$D(q)\, G(q) = N(q),$$
where
$$N(q) = 6q^4 + 15q^5 + 34q^6 + 57q^7 + 95q^8 + 121q^9 + 146q^{10} + 126q^{11} + 106q^{12} + 72q^{13} + 50q^{14} + 25q^{15} + 11q^{16}.$$

---

## 3. Extraction of the 22-Term Linear Recurrence

Expanding $D(q) = (1-q)^6 (1+q)^4 (1+q^2)^3 (1+q+q^2)^3$ yields
$$D(q) = 1 + q - 3q^3 - 6q^4 - 3q^5 + 3q^6 + 12q^7 + 12q^8 + 2q^9 - 10q^{10} - 18q^{11} - 10q^{12} + 2q^{13} + 12q^{14} + 12q^{15} + 3q^{16} - 3q^{17} - 6q^{18} - 3q^{19} + q^{21} + q^{22}.$$
Write $D(q) = \sum_{j=0}^{22} d_j q^j$, where $d_0 = 1$ and $d_j = d_{22-j}$. Because $\deg N(q) = 16 < 22$, for **every** integer $n \ge 0$, the coefficient of $q^{n+22}$ in $D(q) G(q) = N(q)$ is $0$:
$$[q^{n+22}]\bigl(D(q) G(q)\bigr) = \sum_{j=0}^{22} d_j\, e_2p_4(n + 22 - j) = 0 \qquad (\forall n \ge 0).$$
Since $d_0 = 1$ and $d_j = d_{22-j}$, solving for $e_2p_4(22 + n)$ gives, for all $n \ge 0$:
$$\begin{aligned}
e_2p_4(22+n) =\;& -e_2p_4(n) - e_2p_4(1+n) + 3e_2p_4(3+n) + 6e_2p_4(4+n) + 3e_2p_4(5+n) \\
& - 3e_2p_4(6+n) - 12e_2p_4(7+n) - 12e_2p_4(8+n) - 2e_2p_4(9+n) \\
& + 10e_2p_4(10+n) + 18e_2p_4(11+n) + 10e_2p_4(12+n) - 2e_2p_4(13+n) \\
& - 12e_2p_4(14+n) - 12e_2p_4(15+n) - 3e_2p_4(16+n) + 3e_2p_4(17+n) \\
& + 6e_2p_4(18+n) + 3e_2p_4(19+n) - e_2p_4(21+n),
\end{aligned}$$
which matches the conjectured linear recurrence verbatim. $\blacksquare$

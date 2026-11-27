# Counterexample to `arXiv:2310.16929v1` Conjecture 3.2

## Result

Conjecture 3.2 (`\label{conjec-creix-alfa}`) of M. A. Reyes, C. Dalfó, and M. A. Fiol (*"On the spectra and spectral radii of token graphs"*, `arXiv:2310.16929v1`, Section 3, lines 542–548; also *Boletín de la Sociedad Matemática Mexicana* 30 (2024), Art. 11, `DOI: 10.1007/s40590-023-00583-3`) is **FALSE**.

Specifically, for the $6$-cycle $G = C_6$ (simple and connected, $n = 6$, $\lfloor n/2 \rfloor = 3$), we have
$$\alpha_1(C_6) = 1, \qquad \alpha_2(C_6) = \frac{7 - \sqrt{17}}{2}, \qquad \alpha_3(C_6) = 5 - \sqrt{13},$$
and **$\alpha_3(C_6) < \alpha_2(C_6)$** (numerically $1.3944487\ldots < 1.4384471\ldots$).

*(In fact, across all $1{,}245$ graphs on $4 \le n \le 7$ vertices in the NetworkX graph atlas, $C_6$ is the unique counterexample to Conjecture 3.2.)*

## Explicit Counterexample and Exact Spectral Proof

Let $G = C_6$ have vertex set $V = \{0, 1, 2, 3, 4, 5\}$ and edge set $E = \{\{i, i+1 \bmod 6\} : 0 \le i \le 5\}$.

For $k \in \{0, 1, 2, 3\}$, let $P_k(x) = \det(xI - L(F_k(C_6))) \in \mathbb{Z}[x]$ be the Laplacian characteristic polynomial of the $k$-token graph $F_k(C_6)$ ($L = D - A$). Direct computation (verified symbolically in `verify.py`, and also by symmetry of $C_6$) yields the exact factorizations in $\mathbb{Z}[x]$:

1. **$k = 0$ ($F_0(C_6) = K_1$, $1$ vertex):**
   $$P_0(x) = x.$$

2. **$k = 1$ ($F_1(C_6) \cong C_6$, $6$ vertices):**
   $$P_1(x) = x (x - 1)^2 (x - 3)^2 (x - 4).$$
   Thus $\mathrm{sp} F_1(C_6) \setminus \mathrm{sp} F_0(C_6) = \{1, 1, 3, 3, 4\}$, so
   $$\alpha_1(C_6) = 1.$$

3. **$k = 2$ ($F_2(C_6)$, $15$ vertices):**
   $$P_2(x) = x (x - 1)^2 (x - 2) (x - 3)^2 (x - 4) (x - 5)^2 (x^2 - 10x + 20) (x^2 - 7x + 8)^2.$$
   Dividing by $P_1(x)$ gives the $9$-element multiset $\mathrm{sp} F_2(C_6) \setminus \mathrm{sp} F_1(C_6)$ with characteristic polynomial
   $$Q_2(x) = \frac{P_2(x)}{P_1(x)} = (x - 2) (x - 5)^2 (x^2 - 10x + 20) (x^2 - 7x + 8)^2.$$
   Its eigenvalues are:
   $$\frac{7 - \sqrt{17}}{2}\;(\times 2), \quad 2, \quad 5 - \sqrt{5}, \quad 5\;(\times 2), \quad \frac{7 + \sqrt{17}}{2}\;(\times 2), \quad 5 + \sqrt{5}.$$
   Since $17 > 9 \implies \sqrt{17} > 3 \implies \frac{7 - \sqrt{17}}{2} < 2$, and $5 - \sqrt{5} > 5 - 3 = 2$, the minimum eigenvalue of $\mathrm{sp} F_2(C_6) \setminus \mathrm{sp} F_1(C_6)$ is
   $$\alpha_2(C_6) = \frac{7 - \sqrt{17}}{2}.$$

4. **$k = 3$ ($F_3(C_6)$, $20$ vertices):**
   $$P_3(x) = x (x - 1)^2 (x - 2) (x - 3)^2 (x - 4)^3 (x - 5)^2 (x - 6) (x^2 - 10x + 12) (x^2 - 10x + 20) (x^2 - 7x + 8)^2.$$
   Dividing by $P_2(x)$ gives the $5$-element multiset $\mathrm{sp} F_3(C_6) \setminus \mathrm{sp} F_2(C_6)$ with characteristic polynomial
   $$Q_3(x) = \frac{P_3(x)}{P_2(x)} = (x - 4)^2 (x - 6) (x^2 - 10x + 12).$$
   Its eigenvalues are:
   $$5 - \sqrt{13}, \quad 4, \quad 4, \quad 6, \quad 5 + \sqrt{13}.$$
   Since $13 > 1 \implies 5 - \sqrt{13} < 4$, the minimum eigenvalue of $\mathrm{sp} F_3(C_6) \setminus \mathrm{sp} F_2(C_6)$ is
   $$\alpha_3(C_6) = 5 - \sqrt{13}.$$

## Pure Integer Proof that $\alpha_3(C_6) < \alpha_2(C_6)$

We verify $\alpha_3(C_6) < \alpha_2(C_6)$ algebraically without floating-point approximation:
$$5 - \sqrt{13} < \frac{7 - \sqrt{17}}{2} \iff 10 - 2\sqrt{13} < 7 - \sqrt{17} \iff 3 + \sqrt{17} < 2\sqrt{13}.$$
Because both sides of $3 + \sqrt{17} < 2\sqrt{13}$ are strictly positive, squaring preserves the strict inequality:
$$(3 + \sqrt{17})^2 = 26 + 6\sqrt{17} < 52 = (2\sqrt{13})^2 \iff 6\sqrt{17} < 26 \iff 3\sqrt{17} < 13.$$
Squaring again (both sides positive) gives the true integer inequality:
$$9 \cdot 17 = 153 < 169 = 13^2.$$
Hence $\alpha_3(C_6) < \alpha_2(C_6)$, refuting Conjecture 3.2. $\blacksquare$

## Verification

Run `.venv/bin/python targets/reyes-2310.16929-conj3.2/verify.py`, which uses exact symbolic/integer arithmetic (`sympy`, zero floats) to:
1. Construct $F_0(C_6), F_1(C_6), F_2(C_6), F_3(C_6)$ directly from the $k$-subset symmetric-difference definition.
2. Compute exact integer Laplacian matrices $L_k = D_k - A_k$ and characteristic polynomials $P_k(x) \in \mathbb{Z}[x]$.
3. Verify exact polynomial divisibility $P_0 \mid P_1 \mid P_2 \mid P_3$ and exact factorizations of $Q_1, Q_2, Q_3$.
4. Isolate all real roots of $Q_1, Q_2, Q_3$ exactly (via `sympy.real_roots` and exact algebraic comparison) and confirm $\alpha_3(C_6) = 5 - \sqrt{13} < \frac{7 - \sqrt{17}}{2} = \alpha_2(C_6)$.

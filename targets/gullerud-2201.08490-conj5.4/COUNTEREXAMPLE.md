# Disproof of Conjecture 5.4 (`conj:ellipse`) of `arXiv:2201.08490v3`

We refute Conjecture 5.4 (`\label{conj:ellipse}`) of Emily Gullerud, Rita Johnson, and aBa Mbirika, *"Tridiagonal real symmetric matrices with a connection to Pascal's triangle and the Fibonacci sequence"* (`arXiv:2201.08490v3`, Section 5.1, lines 1171–1173). *(Context: the adjacent Conjecture 5.5 on unbounded real parts was separately settled in `arXiv:2510.02008v1/v2` and `arXiv:2611.21142v1`, both of which left Conjecture 5.4 open.)*

**Statement (Conjecture 5.4):** *"The roots of $f_n(\lambda) = F_{n+1}$ lie on an ellipse."*

**Counterexample ($n = 8$):** The roots of $f_8(\lambda) = F_9 = 34$ do **not** lie on any ellipse — in fact, they do not lie on any quadratic curve (conic section) in $\mathbb{C} \cong \mathbb{R}^2$.

## Proof

By Definition 2.6 and Section 1 (lines 213–215), $f_n(\lambda) = \det(A_n - \lambda I_n)$ satisfies $f_1(\lambda) = -\lambda$, $f_2(\lambda) = \lambda^2 - 1$, and $f_n(\lambda) = -\lambda f_{n-1}(\lambda) - f_{n-2}(\lambda)$. For $n = 8$, direct expansion gives
$$f_8(\lambda) = \lambda^8 - 7\lambda^6 + 15\lambda^4 - 10\lambda^2 + 1.$$
Since $F_9 = 34$, the equation $f_8(\lambda) = F_9$ factors in $\mathbb{Z}[\lambda]$ as
$$f_8(\lambda) - 34 = \lambda^8 - 7\lambda^6 + 15\lambda^4 - 10\lambda^2 - 33 = (\lambda^2 + 1)\bigl((\lambda^2)^3 - 8(\lambda^2)^2 + 23(\lambda^2) - 33\bigr).$$
Define $P(z) := z^3 - 8z^2 + 23z - 33$.

1. **Classification of the 8 roots.**
   - The factor $\lambda^2 + 1 = 0$ contributes the two roots $\lambda = \pm i$, corresponding to $(0, \pm 1) \in \mathbb{R}^2$.
   - For $P(z)$, its derivative $P'(z) = 3z^2 - 16z + 23$ has discriminant $(-16)^2 - 4(3)(23) = -20 < 0$, so $P'(z) > 0$ for all $z \in \mathbb{R}$. Hence $P$ is strictly increasing on $\mathbb{R}$. Since $P(4) = -5 < 0 < 7 = P(5)$, $P(z)$ has a unique real root $z_0 \in (4, 5)$ and one pair of non-real complex conjugate roots $z_1, \bar{z}_1 \in \mathbb{C} \setminus \mathbb{R}$.
   - Setting $\lambda^2 = z_0 > 0$ gives two real roots $\pm \sqrt{z_0}$, i.e., $(\pm \sqrt{z_0}, 0) \in \mathbb{R}^2$.
   - Choosing a square root $\lambda_1 = x_1 + i y_1$ of $z_1$ (replacing $z_1$ by $\bar{z}_1$ and $\lambda_1$ by $\pm\lambda_1$ if needed), we cannot have $x_1 = 0$ or $y_1 = 0$ because $\lambda_1^2 = (x_1^2 - y_1^2) + 2ix_1y_1 = z_1 \notin \mathbb{R}$. Thus we obtain $x_1 > 0$ and $y_1 > 0$, and the remaining four roots $\pm(x_1 \pm i y_1)$ correspond to $(\pm x_1, \pm y_1) \in \mathbb{R}^2$.

2. **Forced conic equation.**
   Suppose for contradiction that all 8 roots lie on an ellipse (more generally, any conic)
   $$Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0, \qquad (A, B, C, D, E, F) \in \mathbb{R}^6 \setminus \{0\}.$$
   - Evaluating at $(\pm \sqrt{z_0}, 0)$ gives $A z_0 \pm D\sqrt{z_0} + F = 0$; since $\sqrt{z_0} > 0$, $D = 0$ and $F = -A z_0$.
   - Evaluating at $(0, \pm 1)$ gives $C \pm E + F = 0$, so $E = 0$ and $C = -F = A z_0$.
   - Evaluating at $(x_1, y_1)$ and $(-x_1, y_1)$ gives $A x_1^2 \pm B x_1 y_1 + C y_1^2 + F = 0$, so $2B x_1 y_1 = 0$; since $x_1 y_1 > 0$, $B = 0$.
   - If $A = 0$, then $A = B = C = D = E = F = 0$, impossible. Dividing by $A \neq 0$, the conic must be
     $$x^2 + z_0 y^2 = z_0.$$

3. **Polynomial obstruction via Vieta's formulas.**
   Since $\lambda_1^2 = z_1$, we have $\Re(z_1) = x_1^2 - y_1^2$ and $|z_1| = |\lambda_1|^2 = x_1^2 + y_1^2$, so
   $$x_1^2 = \frac{|z_1| + \Re(z_1)}{2}, \qquad y_1^2 = \frac{|z_1| - \Re(z_1)}{2}.$$
   Factoring $P(z) = (z - z_0)(z^2 - 2\Re(z_1)z + |z_1|^2)$ and matching coefficients gives
   $$z_0 + 2\Re(z_1) = 8 \implies \Re(z_1) = 4 - \frac{z_0}{2}, \qquad z_0 |z_1|^2 = 33 \implies |z_1|^2 = \frac{33}{z_0}.$$
   Substituting into $2(x_1^2 + z_0 y_1^2) = 2 z_0$ yields
   $$(z_0 + 1)|z_1| = 2z_0 + (z_0 - 1)\Re(z_1) = 2z_0 + (z_0 - 1)\left(4 - \frac{z_0}{2}\right) = \frac{-z_0^2 + 13z_0 - 8}{2}.$$
   Squaring both sides and multiplying by $4z_0$ (using $z_0|z_1|^2 = 33$) gives $Q(z_0) = 0$, where
   $$Q(z) := z(-z^2 + 13z - 8)^2 - 132(z + 1)^2 = z^5 - 26z^4 + 185z^3 - 340z^2 - 200z - 132.$$
   However, exact polynomial division in $\mathbb{Z}[z]$ gives
   $$Q(z) = (z^2 - 18z + 18)\,P(z) + R(z), \qquad R(z) := 251z^2 - 1208z + 462,$$
   and $P$ and $R$ satisfy the exact integer Bézout identity
   $$(13858805 - 92031911z)\,P(z) + (366661z^2 - 1223855z + 2309921)\,R(z) = 609842937.$$
   Since $P(z_0) = 0$ and $Q(z_0) = 0$, it follows that $R(z_0) = 0$, which upon evaluation in the Bézout identity yields $0 = 609842937$, a contradiction. Thus the 8 roots of $f_8(\lambda) = F_9$ do not lie on any ellipse (nor any conic). $\square$

*(Remark: $n = 8$ is the smallest even counterexample; for $n \in \{2, 4, 6\}$, the root-set symmetries reduce any conic fit to at most $2$ independent parameters.)*

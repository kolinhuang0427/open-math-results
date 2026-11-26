# Proof of R. J. Mathar's Order-5 D-Finite Recurrence for OEIS A250917

## Statement
Let $C(x) = \frac{1 - \sqrt{1 - 4x}}{2x} = \sum_{k \ge 0} C_k x^k$ be the Catalan generating function, and let
$$F(x) = \exp\bigl(x C(x)^3\bigr) = \sum_{n=0}^{\infty} a(n) \frac{x^n}{n!}.$$
Then for every integer $n \ge 5$ (and also for $n = 3, 4$ with the convention $a(-1) = 0$; note it fails at $n=1,2$ with $a(-1)=a(-2)=0$ since it is an order-5 recurrence starting at $n \ge 5$),
$$\begin{aligned}
0 &= 2\,a(n) + (-11n + 20)\,a(n-1) + (n^3 + 9n^2 - 116n + 164)\,a(n-2) \\
  &\quad + (-4n^4 + 35n^3 + n^2 - 317n + 342)\,a(n-3) - 6(n-3)(6n^3 - 50n^2 + 147n - 176)\,a(n-4) \\
  &\quad + 12(n-5)(2n-9)(n-3)(n-4)\,a(n-5).
\end{aligned}$$

---

## Proof

Let $\Delta(x) = 1 - 4x$ and $S = \sqrt{1 - 4x}$ (the branch analytic on $|x| < 1/4$ with $S(0) = 1$). Since $S' = \frac{-2}{1 - 4x} S$, the rank-2 $\mathbb{Q}(x)$-algebra $\mathcal{A} = \mathbb{Q}(x)[S]/(S^2 - \Delta(x))$ is closed under $d/dx$ and $\theta = x \frac{d}{dx}$.

Here $C(x) = \frac{1 - S}{2x} \in \mathcal{A}$ is analytic on $|x| < 1/4$ with $C(0) = 1$, so $g(x) = x C(x)^3 \in \mathcal{A}$ is analytic on $|x| < 1/4$ with $g(0) = 0$. Therefore $F(x) = \exp(g(x))$ is analytic and nonzero on $|x| < 1/4$, satisfying $F'(x) = g'(x) F(x)$. By induction on $k \ge 0$ and $j \ge 0$, every $\theta^j F^{(k)}(x)$ lies in $\mathcal{A} \cdot F(x)$.

Set $m = n - 5 \ge 0$ (so $n = m + 5$), multiply the conjectured recurrence by $\frac{x^m}{m!}$, and sum over all $m \ge 0$. For each $r \in \{0, 1, 2, 3, 4, 5\}$, since
$$F^{(r)}(x) = \sum_{m=0}^{\infty} a(m + r) \frac{x^m}{m!},$$
applying the Euler operator $\theta = x \frac{d}{dx}$ multiplies the $[x^m]$ coefficient by $m$. Thus, for any polynomial $P_r(n) = Q_r(m)$ (where $m = n - 5$),
$$\sum_{m=0}^{\infty} P_r(m+5)\, a(m+r) \frac{x^m}{m!} = Q_r(\theta)\bigl[F^{(r)}(x)\bigr].$$

Writing $P_r(n)$ for the coefficient of $a(n-r)$ in Mathar's recurrence ($r = 0, \dots, 5$, corresponding to $F^{(5-r)}$), the generating series of the left-hand side for $n \ge 5$ is $L[F](x)$, where
$$L[F](x) = \sum_{r=0}^{5} Q_r(\theta)\bigl[F^{(5-r)}(x)\bigr] = R(x, S)\, F(x)$$
for a unique element $R(x, S) = A(x) + B(x) S \in \mathcal{A}$. Exact arithmetic in $\mathbb{Q}(x)[S]/(S^2 - (1 - 4x))$ (verified in `verify.py`) yields $A(x) = 0$ and $B(x) = 0$, i.e. $R(x, S) = 0$ identically.

Since $F(x) = \exp(x C(x)^3)$ is nonzero on $|x| < 1/4$, $L[F](x) = 0$ identically, so every Taylor coefficient $[x^m] L[F](x) = 0$ for all $m \ge 0$. Hence Mathar's recurrence holds for all $n = m + 5 \ge 5$ (and direct check shows it also holds for $n = 3, 4$ with $a(-1)=0$). $\square$

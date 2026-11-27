# Proof of Mikhail Kurkov's Conjecture on OEIS A383410

## Statement

Define the array $A(n, k)$ ($n \ge 0$, $k \ge 0$) by $A(0, k) = 1$ for all $k \ge 0$ and
$$A(n, k) = \sum_{i=0}^{n-1} \sum_{j=0}^{k+1} \binom{n-1}{i}\binom{k+1}{j} A(i, j) \quad (n \ge 1,\ k \ge 0).$$
Then the bivariate exponential generating function $F(x, y) := \sum_{n=0}^{\infty} \sum_{k=0}^{\infty} A(n, k)\frac{x^n}{n!}\frac{y^k}{k!}$ equals
$$F(x, y) = \frac{e^{-y}}{\bigl(1 + e^{-y} - e^x\bigr)^2}.$$
In particular, $F(x, 0) = (2 - e^x)^{-2}$, which is the defining exponential generating function of OEIS `A005649` (`rev. 123`), so
$$A(n, 0) = \mathrm{A005649}(n) \quad \text{for all } n \ge 0.$$

---

## 1. Derivation of the Bivariate Exponential Generating Function PDE

For each $n \ge 0$, define the row exponential generating function
$$F_n(y) := \sum_{k=0}^{\infty} A(n, k) \frac{y^k}{k!} \in \mathbb{Q}[[y]],$$
so $F(x, y) = \sum_{n=0}^{\infty} F_n(y) \frac{x^n}{n!} \in \mathbb{Q}[[x, y]]$ and $F_0(y) = e^y$.

For each $i \ge 0$, multiplying $F_i(y)$ by $e^y = \sum_{r=0}^{\infty} \frac{y^r}{r!}$ gives the binomial convolution
$$e^y F_i(y) = \sum_{m=0}^{\infty} \left(\sum_{j=0}^{m} \binom{m}{j} A(i, j)\right) \frac{y^m}{m!}.$$
Differentiating with respect to $y$ shifts $m \mapsto k+1$:
$$\partial_y\bigl(e^y F_i(y)\bigr) = \sum_{k=0}^{\infty} \left(\sum_{j=0}^{k+1} \binom{k+1}{j} A(i, j)\right) \frac{y^k}{k!}.$$

For every $n \ge 1$, multiplying the defining recurrence for $A(n, k)$ by $\frac{y^k}{k!}$ and summing over $k \ge 0$ therefore yields
$$F_n(y) = \sum_{i=0}^{n-1} \binom{n-1}{i}\,\partial_y\bigl(e^y F_i(y)\bigr) \quad (n \ge 1).$$
Now multiply by $\frac{x^{n-1}}{(n-1)!}$ and sum over $n \ge 1$:
$$\partial_x F(x, y) = \sum_{n=1}^{\infty} F_n(y)\frac{x^{n-1}}{(n-1)!} = \left(\sum_{r=0}^{\infty} \frac{x^r}{r!}\right) \sum_{i=0}^{\infty} \partial_y\bigl(e^y F_i(y)\bigr)\frac{x^i}{i!} = e^x\,\partial_y\bigl(e^y F(x, y)\bigr).$$

---

## 2. Exact Closed-Form Solution in $\mathbb{Q}[[x, y]]$

Set $U(x, y) := e^y F(x, y) = \sum_{n=0}^{\infty} U_n(y)\frac{x^n}{n!} \in \mathbb{Q}[[x, y]]$. Since $\partial_x(e^y F) = e^y\,\partial_x F$, the PDE becomes
$$\partial_x U(x, y) = e^{x+y}\,\partial_y U(x, y), \qquad U(0, y) = e^y F_0(y) = e^{2y}.$$
Comparing coefficients of $\frac{x^n}{n!}$ on both sides gives
$$U_{n+1}(y) = e^y \sum_{i=0}^{n} \binom{n}{i}\,\partial_y U_i(y) \quad (n \ge 0),$$
so $U(x, y)$ is uniquely determined in $\mathbb{Q}[[x, y]]$ by $U_0(y) = e^{2y}$.

Consider $D(x, y) := 1 + e^{-y} - e^x \in \mathbb{Q}[[x, y]]$. Its constant term is $D(0, 0) = 1 + 1 - 1 = 1 \neq 0$, so $\widetilde{U}(x, y) := D(x, y)^{-2}$ is a well-defined element of $\mathbb{Q}[[x, y]]$. Moreover:
1. At $x = 0$, $D(0, y) = 1 + e^{-y} - 1 = e^{-y}$, so $\widetilde{U}(0, y) = (e^{-y})^{-2} = e^{2y} = U(0, y)$.
2. Differentiating $\widetilde{U} = D^{-2}$ with respect to $x$ and $y$ gives
   $$\partial_x \widetilde{U} = -2 D^{-3}(-e^x) = 2 e^x D^{-3}, \qquad \partial_y \widetilde{U} = -2 D^{-3}(-e^{-y}) = 2 e^{-y} D^{-3},$$
   whence
   $$e^{x+y}\,\partial_y \widetilde{U} = e^{x+y}\cdot 2 e^{-y} D^{-3} = 2 e^x D^{-3} = \partial_x \widetilde{U}.$$

By uniqueness, $U(x, y) = \widetilde{U}(x, y) = (1 + e^{-y} - e^x)^{-2}$, so
$$F(x, y) = e^{-y} U(x, y) = \frac{e^{-y}}{\bigl(1 + e^{-y} - e^x\bigr)^2}.$$

---

## 3. Conclusion

Evaluating at $y = 0$ gives
$$\sum_{n=0}^{\infty} A(n, 0)\frac{x^n}{n!} = F(x, 0) = \frac{1}{\bigl(2 - e^x\bigr)^2},$$
which is the defining exponential generating function of OEIS `A005649` (`rev. 123`). Extracting coefficients of $\frac{x^n}{n!}$ gives $A(n, 0) = \mathrm{A005649}(n)$ for all $n \ge 0$. $\blacksquare$

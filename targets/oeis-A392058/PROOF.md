# Proof of Mikhail Kurkov's Conjecture on OEIS A392058

## Statement

Define the array $A(n, k)$ ($n, k \ge 0$) by $A(0, k) = 1$ for all $k \ge 0$ and
$$A(n, k) = A(n-1, k+1) + \sum_{j=0}^{k} \binom{k+1}{j} A(n-1, j) A(k-j, 0) \quad (n \ge 1,\ k \ge 0).$$
Let $E(x) = \sum_{m=0}^{\infty} \mathrm{A233335}(m)\frac{x^m}{m!} \in \mathbb{Q}[[x]]$ with $E(0) = 1$ be the exponential generating function of OEIS `A233335` (`rev. 20`), defined uniquely by
$$E\!\left(\int_0^x \frac{dt}{E(t)}\right) = e^x.$$
Then for every integer $n \ge 0$,
$$A(n, 0) = \mathrm{A233335}(n + 1).$$

---

## 1. Row Exponential Generating Functions and Transport PDE

For each $n \ge 0$, define the row exponential generating function
$$H_n(y) := \sum_{k=0}^{\infty} A(n, k)\frac{y^k}{k!} \in \mathbb{Q}[[y]],$$
so $H_0(y) = e^y$. Define the shifted column-$0$ series
$$V(y) := 1 + \sum_{m=1}^{\infty} A(m-1, 0)\frac{y^m}{m!} = 1 + \int_0^y G(t, 0)\,dt \in \mathbb{Q}[[y]],$$
where $G(x, y) := \sum_{n=0}^{\infty} H_n(y)\frac{x^n}{n!} \in \mathbb{Q}[[x, y]]$. Note that $V(0) = 1$ and $V'(y) = G(y, 0) = \sum_{n=0}^{\infty} A(n, 0)\frac{y^n}{n!}$.

Dividing the defining recurrence for $A(n, k)$ ($n \ge 1$) by $k!$ gives
$$\frac{A(n, k)}{k!} = (k+1)\frac{A(n-1, k+1)}{(k+1)!} + (k+1)\sum_{j=0}^{k} \frac{A(n-1, j)}{j!} \cdot \frac{A(k-j, 0)}{(k+1-j)!}.$$
Since $\frac{A(r-1, 0)}{r!} = [y^r]\bigl(V(y) - 1\bigr)$ for $r \ge 1$, the Cauchy product of $V(y) - 1$ and $H_{n-1}(y)$ has $[y^{k+1}]$ coefficient $\sum_{j=0}^k \frac{A(n-1, j)}{j!} \frac{A(k-j, 0)}{(k+1-j)!}$. Multiplying the identity above by $y^k$ and summing over $k \ge 0$ therefore gives
$$H_n(y) = \partial_y H_{n-1}(y) + \partial_y\!\bigl((V(y) - 1) H_{n-1}(y)\bigr) = \partial_y\bigl(V(y) H_{n-1}(y)\bigr) \quad (n \ge 1).$$

Set $W(x, y) := V(y) G(x, y) \in \mathbb{Q}[[x, y]]$. Multiplying $H_n(y) = \partial_y(V(y) H_{n-1}(y))$ by $\frac{x^{n-1}}{(n-1)!}$ and summing over $n \ge 1$ yields $\partial_x G = \partial_y W$, so $W(x, y)$ satisfies the initial-value problem in $\mathbb{Q}[[x, y]]$:
$$\partial_x W(x, y) = V(y)\,\partial_y W(x, y), \qquad W(0, y) = V(y) e^y.$$
Comparing $[x^n/n!]$ coefficients shows that $W_n(y) := [x^n/n!] W(x, y)$ is uniquely determined inductively by $W_{n+1}(y) = V(y)\partial_y W_n(y)$ from $W_0(y) = V(y) e^y$.

---

## 2. Method of Characteristics in $\mathbb{Q}[[x, y]]$

Because $V(0) = 1$, its reciprocal $1/V(t)$ lies in $\mathbb{Q}[[t]]$ with constant term $1$, so
$$\Phi(u) := \int_0^u \frac{dt}{V(t)} \in u\mathbb{Q}[[u]]$$
satisfies $\Phi(0) = 0$ and $\Phi'(0) = 1/V(0) = 1 \neq 0$. By the formal Implicit Function Theorem, there is a unique series $\eta(x, y) \in \mathbb{Q}[[x, y]]$ with $\eta(0, 0) = 0$ satisfying
$$\Phi(\eta(x, y)) = \Phi(y) + x, \qquad \eta(0, y) = y.$$
Differentiating with respect to $x$ and $y$ gives
$$\frac{\partial_x \eta}{V(\eta)} = 1, \qquad \frac{\partial_y \eta}{V(\eta)} = \frac{1}{V(y)},$$
and hence $\partial_x \eta = V(y)\,\partial_y \eta$. By the chain rule, $U(x, y) := V(\eta(x, y))\, e^{\eta(x, y)} \in \mathbb{Q}[[x, y]]$ satisfies
$$\partial_x U = \left(V'(\eta) + V(\eta)\right)e^{\eta}\,\partial_x\eta = V(y)\left(V'(\eta) + V(\eta)\right)e^{\eta}\,\partial_y\eta = V(y)\,\partial_y U,$$
with $U(0, y) = V(\eta(0, y)) e^{\eta(0, y)} = V(y) e^y = W(0, y)$. By uniqueness,
$$W(x, y) = V(\eta(x, y))\, e^{\eta(x, y)} \quad \text{in } \mathbb{Q}[[x, y]].$$

---

## 3. Specialization to $y = 0$ and Identification with $E(x)$

Specialize to $y = 0$, and write $u(x) := \eta(x, 0) = \Phi^{-1}(x) \in x\mathbb{Q}[[x]]$. Since $V(0) = 1$,
$$V'(x) = G(x, 0) = W(x, 0) = V(u(x))\, e^{u(x)} \quad \text{in } \mathbb{Q}[[x]].$$
Now substitute $x = \Phi(u)$ in $\mathbb{Q}[[u]]$ (valid since $\Phi(0) = 0$ and $u(\Phi(u)) = u$). By the chain rule and $\Phi'(u) = 1/V(u)$,
$$\frac{d}{du}\bigl(V(\Phi(u))\bigr) = V'(\Phi(u))\,\Phi'(u) = \Bigl(V(u)\,e^u\Bigr)\cdot \frac{1}{V(u)} = e^u.$$
Since $V(\Phi(0)) = V(0) = 1 = e^0$, integrating with respect to $u$ yields
$$V\!\left(\int_0^u \frac{dt}{V(t)}\right) = V(\Phi(u)) = e^u \quad \text{in } \mathbb{Q}[[u]].$$

Finally, the functional equation $A\bigl(\int_0^u \frac{dt}{A(t)}\bigr) = e^u$ with $A(0) = 1$ uniquely determines $A(x) = \sum_{m=0}^{\infty} a_m \frac{x^m}{m!} \in \mathbb{Q}[[x]]$: differentiating with respect to $u$ gives $A'(\Phi_A(u)) = A(u)e^u$, where $\Phi_A(u) = \int_0^u \frac{dt}{A(t)} = u + O(u^2)$, and for each $m \ge 1$ the coefficient $[u^m]$ on the left has $a_{m+1}/m!$ (from the $r = m$ term $\frac{a_{m+1}}{m!}\Phi_A(u)^m$) plus terms depending only on $a_1, \dots, a_m$, while $[u^m](A(u)e^u)$ depends only on $a_0, \dots, a_m$ (and at $m=0$, $a_1 = A'(0) = 1$). Since $V(0) = 1 = E(0)$ and both $V$ and $E$ solve this equation, $V(x) = E(x)$ in $\mathbb{Q}[[x]]$.

Comparing coefficients of $\frac{x^n}{n!}$ in $V'(x) = E'(x)$ gives
$$A(n, 0) = \mathrm{A233335}(n + 1) \quad \text{for all } n \ge 0. \quad \blacksquare$$

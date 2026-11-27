# Proof of Mikhail Kurkov's Conjecture for OEIS A379459 (`A(n, 0) = A006351(n + 2)`)

*(Scope note: Per `CONTESTED.md`, the companion identity `A379460(n, 0) = A006351(n + 1)` was prior-settled in `insorrowmeow/oeis-sequence-proofs` `62bc090`, `2026-11-27T11:08:09Z`, `proofs/research-batch-09/YokeRows.{md,lean}`. We prove strictly the open claim `A379459(n, 0) = A006351(n + 2)` for all $n \ge 0$, equivalently `A006351(m) = A379459(m - 2, 0)` for all $m > 1$.)*

## Statement

Let $A_{459}(n, k)$ ($n, k \ge 0$) be the array of OEIS `A379459` (`rev. 4`):
$$A_{459}(0, k) = 2(k+1)!, \qquad A_{459}(n, k) = A_{459}(n-1, k+1) + 2(k+1)!\sum_{j=0}^{k} \frac{A_{459}(n-1, j)}{j!} \quad (n \ge 1).$$
Let $B(x) := \sum_{m=1}^{\infty} \mathrm{A006351}(m) \frac{x^m}{m!} \in x\mathbb{Q}[[x]]$ be the exponential generating function of OEIS `A006351` (`rev. 195`, offset $1$), which is the compositional inverse of $2\ln(1 + t) - t$ in $\mathbb{Q}[[x]]$ (Riordan, *An Introduction to Combinatorial Analysis*, 1958, p. 142; Bóna, *Handbook of Enumerative Combinatorics*, 2015, p. 417).

Then $A_{459}(n, 0) = \mathrm{A006351}(n + 2)$ for all $n \ge 0$ (equivalently, $\mathrm{A006351}(m) = A_{459}(m - 2, 0)$ for all $m > 1$).

---

## 1. Row Exponential Generating Functions for $A_{459}$

For each $n \ge 0$, define $H_n(y) := \sum_{k=0}^{\infty} \frac{A_{459}(n, k)}{k!} y^k \in \mathbb{Q}[[y]]$.
- For $n = 0$: $\frac{A_{459}(0, k)}{k!} = 2(k+1)$, so
  $$H_0(y) = \sum_{k=0}^{\infty} 2(k+1) y^k = \frac{2}{(1 - y)^2}.$$
- For $n \ge 1$: dividing the recurrence for $A_{459}(n, k)$ by $k!$ gives
  $$\frac{A_{459}(n, k)}{k!} = (k+1)\frac{A_{459}(n-1, k+1)}{(k+1)!} + 2(k+1)\sum_{j=0}^{k} \frac{A_{459}(n-1, j)}{j!}.$$
  Multiplying by $y^k$ and summing over $k \ge 0$:
  $$H_n(y) = \partial_y H_{n-1}(y) + \partial_y\!\left(\frac{2y}{1-y} H_{n-1}(y)\right) = \partial_y\!\left(\frac{1 + y}{1 - y}\, H_{n-1}(y)\right) \quad (n \ge 1).$$

---

## 2. Transport PDE Solution and Identification with $\mathrm{A006351}$

Define $G(x, y) := \sum_{n=0}^{\infty} H_n(y) \frac{x^n}{n!} \in \mathbb{Q}[[x, y]]$ and $W(x, y) := \frac{1+y}{1-y} G(x, y)$. Then $G(x, 0) = W(x, 0) = \sum_{n=0}^{\infty} A_{459}(n, 0) \frac{x^n}{n!}$.

Multiplying $H_n(y) = \partial_y\bigl(\frac{1+y}{1-y} H_{n-1}(y)\bigr)$ ($n \ge 1$) by $\frac{x^{n-1}}{(n-1)!}$ and summing over $n \ge 1$ yields $\partial_x G(x, y) = \partial_y W(x, y)$, so $W(x, y)$ solves the formal initial-value problem in $\mathbb{Q}[[x, y]]$:
$$\partial_x W(x, y) = \frac{1 + y}{1 - y}\,\partial_y W(x, y), \qquad W(0, y) = \frac{1+y}{1-y} H_0(y) = \frac{2(1+y)}{(1-y)^3}.$$
The coefficients $[x^n] U(x, y)$ of any solution to $\partial_x U = \frac{1+y}{1-y}\partial_y U$ are uniquely determined from $U(0, y)$ by $(n+1)[x^{n+1}]U = \frac{1+y}{1-y}\partial_y([x^n]U)$.

Let $\Phi(u) := 2\ln(1 + u) - u \in u\mathbb{Q}[[u]]$. Since $\Phi(0) = 0$ and $\Phi'(0) = 1 \neq 0$, the formal Implicit Function Theorem yields a unique series $\eta(x, y) \in \mathbb{Q}[[x, y]]$ with $\eta(0, 0) = 0$ satisfying
$$2\ln(1 + \eta(x, y)) - \eta(x, y) = 2\ln(1 + y) - y + x, \qquad \eta(0, y) = y.$$
Differentiating with respect to $x$ and $y$ gives $\frac{1-\eta}{1+\eta}\partial_x\eta = 1$ and $\frac{1-\eta}{1+\eta}\partial_y\eta = \frac{1-y}{1+y}$, hence $\partial_x\eta = \frac{1+y}{1-y}\partial_y\eta$. By the chain rule, $U(x, y) := \frac{2(1+\eta(x,y))}{(1-\eta(x,y))^3}$ solves $\partial_x U = \frac{1+y}{1-y}\partial_y U$ with $U(0, y) = \frac{2(1+y)}{(1-y)^3} = W(0, y)$. By uniqueness,
$$W(x, y) = \frac{2\bigl(1 + \eta(x, y)\bigr)}{\bigl(1 - \eta(x, y)\bigr)^3} \quad \text{in } \mathbb{Q}[[x, y]].$$

Specializing to $y = 0$, the series $\eta(x, 0) \in x\mathbb{Q}[[x]]$ satisfies $\Phi(\eta(x, 0)) = x$, so $\eta(x, 0)$ is the compositional inverse of $2\ln(1+t) - t$, namely $\eta(x, 0) = B(x) = \sum_{m=1}^{\infty} \mathrm{A006351}(m)\frac{x^m}{m!}$. Differentiating $2\ln(1 + B(x)) - B(x) = x$ gives
$$B'(x) = \frac{1 + B(x)}{1 - B(x)} \qquad (B(0) = 0),$$
and differentiating a second time via the quotient rule gives
$$B''(x) = \frac{(1 - B)B' + (1 + B)B'}{(1 - B)^2} = \frac{2 B'(x)}{(1 - B(x))^2} = \frac{2\bigl(1 + B(x)\bigr)}{\bigl(1 - B(x)\bigr)^3} = W(x, 0) = G(x, 0).$$
Comparing coefficients of $\frac{x^n}{n!}$ in
$$\sum_{n=0}^{\infty} \mathrm{A006351}(n+2)\frac{x^n}{n!} = B''(x) = G(x, 0) = \sum_{n=0}^{\infty} A_{459}(n, 0)\frac{x^n}{n!}$$
gives $A_{459}(n, 0) = \mathrm{A006351}(n+2)$ for every $n \ge 0$ (equivalently $\mathrm{A006351}(m) = A_{459}(m - 2, 0)$ for all $m > 1$). $\blacksquare$

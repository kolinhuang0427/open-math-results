# Proof of OEIS A026927 Generating Function and Linear Recurrence

## Theorem

For each integer $n \ge 1$, let $a(n) = A026927(n)$ denote the number of integer partitions of $n$ into an even number of parts whose largest part is $3$. Then:
1. The ordinary generating function is
   $$A(x) = \sum_{n=1}^{\infty} a(n) x^n = \frac{x^4(1 + x^2 - x^3 + x^4)}{(1 - x)^3 (1 + x)^2 (1 - x + x^2) (1 + x^2) (1 + x + x^2)}.$$
2. For all integers $n > 11$ (in fact for all $n \ge 9$ with $a(k) = 0$ for $k \le 0$),
   $$a(n) = a(n-1) + a(n-4) - a(n-5) + a(n-6) - a(n-7) - a(n-10) + a(n-11).$$

---

## Proof

### 1. Bivariate generating function for partitions with largest part $3$

Let $p_3(n, m)$ denote the number of partitions of $n \ge 1$ into $m \ge 1$ parts whose largest part is $3$. Removing one part equal to $3$ leaves a multiset of $m - 1$ parts in $\{1, 2, 3\}$ summing to $n - 3$, uniquely parameterized by multiplicities $c_1, c_2, c_3 \ge 0$ with $n = 3 + c_1 + 2c_2 + 3c_3$ and $m = 1 + c_1 + c_2 + c_3$. Thus, in $\mathbb{Z}[y][[x]]$,
$$F(x, y) := \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} p_3(n, m)\, x^n y^m = x^3 y \sum_{c_1, c_2, c_3 \ge 0} (x y)^{c_1} (x^2 y)^{c_2} (x^3 y)^{c_3} = \frac{x^3 y}{(1 - x y)(1 - x^2 y)(1 - x^3 y)}.$$

### 2. Even-part parity projection and algebraic simplification

Since $a(n) = \sum_{m \ge 1,\ m \text{ even}} p_3(n, m)$ and $\frac{1 + (-1)^m}{2} = \mathbf{1}_{m \text{ even}}$, evaluating at $y = 1$ and $y = -1$ gives in $\mathbb{Z}[[x]]$:
$$A(x) = \sum_{n=1}^{\infty} a(n) x^n = \frac{F(x, 1) + F(x, -1)}{2}.$$
Factoring $1 - x^2 = (1 - x)(1 + x)$, $1 - x^3 = (1 - x)(1 + x + x^2)$, and $1 + x^3 = (1 + x)(1 - x + x^2)$ yields
$$F(x, 1) = \frac{x^3}{(1 - x)^3 (1 + x)(1 + x + x^2)}, \qquad F(x, -1) = \frac{-x^3}{(1 + x)^2 (1 + x^2)(1 - x + x^2)}.$$
With the common denominator
$$D(x) := (1 - x)^3 (1 + x)^2 (1 - x + x^2)(1 + x^2)(1 + x + x^2),$$
we obtain
$$A(x) = \frac{x^3}{2\, D(x)} \Bigl[(1 + x)(1 - x + x^2)(1 + x^2) - (1 - x)^3 (1 + x + x^2)\Bigr].$$
Expanding both terms in $\mathbb{Z}[x]$:
$$\begin{aligned}
(1 + x)(1 - x + x^2)(1 + x^2) &= (1 + x^3)(1 + x^2) = 1 + x^2 + x^3 + x^5, \\
(1 - x)^3 (1 + x + x^2) &= (1 - x)^2 (1 - x^3) = (1 - 2x + x^2)(1 - x^3) = 1 - 2x + x^2 - x^3 + 2x^4 - x^5.
\end{aligned}$$
Subtracting gives $2x + 2x^3 - 2x^4 + 2x^5 = 2x(1 + x^2 - x^3 + x^4)$, and cancelling the factor of $2$ gives Barker's exact generating function:
$$A(x) = \frac{x^4(1 + x^2 - x^3 + x^4)}{(1 - x)^3 (1 + x)^2 (1 - x + x^2)(1 + x^2)(1 + x + x^2)}.$$

### 3. 11-term linear recurrence

Grouping factors in $D(x)$ via $(1 - x)(1 + x + x^2) = 1 - x^3$, $(1 + x)(1 - x + x^2) = 1 + x^3$, and $(1 - x)(1 + x) = 1 - x^2$ gives
$$D(x) = (1 - x)(1 - x^6)(1 - x^4) = 1 - x - x^4 + x^5 - x^6 + x^7 + x^{10} - x^{11}.$$
Multiplying $A(x) = \frac{x^4(1 + x^2 - x^3 + x^4)}{D(x)}$ by $D(x)$ yields
$$(1 - x - x^4 + x^5 - x^6 + x^7 + x^{10} - x^{11}) A(x) = x^4 + x^6 - x^7 + x^8.$$
Because the right-hand side has degree $8$, extracting $[x^n]$ for every integer $n > 11$ (and indeed for all $n \ge 9$) gives
$$a(n) - a(n-1) - a(n-4) + a(n-5) - a(n-6) + a(n-7) + a(n-10) - a(n-11) = 0,$$
i.e., $a(n) = a(n-1) + a(n-4) - a(n-5) + a(n-6) - a(n-7) - a(n-10) + a(n-11)$. $\blacksquare$

# Proof of OEIS A026923 Generating Function and Linear Recurrence

## Theorem

For each integer $n \ge 1$, let $a(n) = A026923(n)$ denote the number of integer partitions of $n$ into an odd number of parts whose largest part is $3$. Then:
1. The ordinary generating function is
   $$A(x) = \sum_{n=1}^{\infty} a(n) x^n = \frac{x^3(1 - x + x^2 + x^4)}{(1 - x)^3 (1 + x)^2 (1 - x + x^2) (1 + x^2) (1 + x + x^2)}.$$
2. For all integers $n > 11$ (in fact for all $n \ge 8$ with $a(k) = 0$ for $k \le 0$),
   $$a(n) = a(n-1) + a(n-4) - a(n-5) + a(n-6) - a(n-7) - a(n-10) + a(n-11).$$

*(Remark: The alternate OEIS description $a(n+5) = \text{partitions of } n+2 \text{ into an even number of parts } \le 3$ follows by deleting one part of size $3$, which bijects partitions of $n+5$ into an odd number of parts with largest part $3$ onto partitions of $n+2$ into an even number of parts $\le 3$.)*

---

## Proof

### 1. Bivariate generating function for partitions with largest part $3$

Let $p_3(n, m)$ denote the number of partitions of $n \ge 1$ into $m \ge 1$ parts whose largest part is $3$. Every such partition consists of one part equal to $3$, together with a multiset of $m - 1$ parts chosen from $\{1, 2, 3\}$ whose sum is $n - 3$: letting $c_j \ge 0$ denote the multiplicity of part $j \in \{1, 2, 3\}$ among the remaining $m - 1$ parts, we have $n = 3 + c_1 + 2c_2 + 3c_3$ and $m = 1 + c_1 + c_2 + c_3$.

Hence, in $\mathbb{Z}[y][[x]]$,
$$F(x, y) := \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} p_3(n, m)\, x^n y^m = x^3 y \sum_{c_1, c_2, c_3 \ge 0} (x y)^{c_1} (x^2 y)^{c_2} (x^3 y)^{c_3} = \frac{x^3 y}{(1 - x y)(1 - x^2 y)(1 - x^3 y)}.$$

### 2. Odd-part parity projection and algebraic simplification

Since $a(n) = \sum_{m \ge 1,\ m \text{ odd}} p_3(n, m)$ and $\frac{1 - (-1)^m}{2} = \mathbf{1}_{m \text{ odd}}$, substituting $y = 1$ and $y = -1$ into $F(x, y)$ gives in $\mathbb{Z}[[x]]$:
$$A(x) = \sum_{n=1}^{\infty} a(n) x^n = \frac{F(x, 1) - F(x, -1)}{2}.$$
Factoring $1 - x^2 = (1 - x)(1 + x)$, $1 - x^3 = (1 - x)(1 + x + x^2)$, and $1 + x^3 = (1 + x)(1 - x + x^2)$ yields
$$F(x, 1) = \frac{x^3}{(1 - x)^3 (1 + x)(1 + x + x^2)}, \qquad F(x, -1) = \frac{-x^3}{(1 + x)^2 (1 + x^2)(1 - x + x^2)}.$$
Bringing $\frac{F(x, 1) - F(x, -1)}{2}$ over the common denominator
$$D(x) := (1 - x)^3 (1 + x)^2 (1 - x + x^2)(1 + x^2)(1 + x + x^2)$$
gives
$$A(x) = \frac{x^3}{2\, D(x)} \Bigl[(1 + x)(1 - x + x^2)(1 + x^2) + (1 - x)^3 (1 + x + x^2)\Bigr].$$
Direct expansion in $\mathbb{Z}[x]$ yields:
$$\begin{aligned}
(1 + x)(1 - x + x^2)(1 + x^2) &= (1 + x^3)(1 + x^2) = 1 + x^2 + x^3 + x^5, \\
(1 - x)^3 (1 + x + x^2) &= (1 - x)^2 (1 - x^3) = (1 - 2x + x^2)(1 - x^3) = 1 - 2x + x^2 - x^3 + 2x^4 - x^5.
\end{aligned}$$
Adding the two polynomials gives $2 - 2x + 2x^2 + 2x^4 = 2(1 - x + x^2 + x^4)$. Cancelling the factor of $2$ produces Barker's exact generating function:
$$A(x) = \frac{x^3(1 - x + x^2 + x^4)}{(1 - x)^3 (1 + x)^2 (1 - x + x^2)(1 + x^2)(1 + x + x^2)}.$$

### 3. 11-term linear recurrence

Notice that $(1 - x)(1 + x + x^2) = 1 - x^3$, $(1 + x)(1 - x + x^2) = 1 + x^3$, and $(1 - x)(1 + x) = 1 - x^2$. Grouping factors in $D(x)$ gives
$$D(x) = (1 - x)(1 - x^3)(1 + x^3)(1 - x^2)(1 + x^2) = (1 - x)(1 - x^6)(1 - x^4).$$
Expanding $(1 - x)(1 - x^4 - x^6 + x^{10})$ gives
$$D(x) = 1 - x - x^4 + x^5 - x^6 + x^7 + x^{10} - x^{11}.$$
Multiplying both sides of $A(x) = \frac{x^3(1 - x + x^2 + x^4)}{D(x)}$ by $D(x)$ yields
$$(1 - x - x^4 + x^5 - x^6 + x^7 + x^{10} - x^{11}) A(x) = x^3 - x^4 + x^5 + x^7.$$
Since the right-hand side has degree $7$, extracting $[x^n]$ for every integer $n > 11$ (and indeed for all $n \ge 8$) gives
$$a(n) - a(n-1) - a(n-4) + a(n-5) - a(n-6) + a(n-7) + a(n-10) - a(n-11) = 0,$$
that is, $a(n) = a(n-1) + a(n-4) - a(n-5) + a(n-6) - a(n-7) - a(n-10) + a(n-11)$. $\blacksquare$

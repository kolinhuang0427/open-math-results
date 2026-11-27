# Proof of OEIS A121752 Recurrence Conjecture

## Theorem
Let $a(1) = 1$, $a(2) = 2$, and for $n \ge 3$,
$$
a(n) = (2n-3)a(n-1) - (n-1)(n-3)a(n-2) + (n-2)!\, f(n),
\qquad f(n) := n\left\lfloor\frac{n}{2}\right\rfloor - (n-2)\left\lfloor\frac{n-1}{2}\right\rfloor - 1.
$$
Then for every integer $n \ge 6$,
$$
M(n) := \sum_{j=0}^{5} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_5(n)$ are the polynomials stated in `TARGET.md`, and consequently the exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite.

## Proof

### Step 1: First-order reduction and closed form for $D(k) = a(k) - k\, a(k-1)$
For every integer $k \ge 2$, define $D(k) := a(k) - k\, a(k-1)$. For every $k \ge 3$,
$$
D(k) - (k-3) D(k-1) = \bigl(a(k) - k a(k-1)\bigr) - (k-3)\bigl(a(k-1) - (k-1)a(k-2)\bigr) = a(k) - (2k-3)a(k-1) + (k-1)(k-3)a(k-2) = (k-2)!\, f(k).
$$
Dividing by $(k-3)!$ for $k \ge 4$ gives $\frac{D(k)}{(k-3)!} - \frac{D(k-1)}{(k-4)!} = (k-2) f(k)$. At $k = 3$, the $(k-3)$ term vanishes and $D(3) = 1!\, f(3) = 1 = 0!\,(3-2)f(3)$. Summing over $j = 3, \dots, k$ therefore yields, for all $k \ge 3$,
$$
D(k) = (k-3)!\, S(k), \qquad S(k) := \sum_{j=3}^{k} (j-2) f(j).
$$
Evaluating $f(j)$ by parity gives $f(2m) = 2m^2 - (2m-2)(m-1) - 1 = 4m - 3$ and $f(2m+1) = (2m+1)m - (2m-1)m - 1 = 2m - 1$. By induction on $r$:
$$
S(2r) = (r-1)(4r^2 - 3r + 1) \quad (r \ge 2), \qquad S(2r+1) = r^2(4r - 3) \quad (r \ge 1).
$$
Indeed, $S(3) = 1\cdot 1 = 1^2(4\cdot 1 - 3)$, and for $r \ge 2$:
- $S(2r) - S(2r-1) = (r-1)(4r^2-3r+1) - (r-1)^2(4r-7) = (r-1)(8r-6) = (2r-2)(4r-3) = (2r-2)f(2r)$,
- $S(2r+1) - S(2r) = r^2(4r-3) - (r-1)(4r^2-3r+1) = 4r^2 - 4r + 1 = (2r-1)^2 = (2r-1)f(2r+1)$.

### Step 2: Operator factorization in $D(n-i)$
Define polynomials $e_0, \dots, e_4 \in \mathbb{Z}[n]$ by
$$
\begin{aligned}
e_0(n) &= -460n + 1223, \\
e_1(n) &= 1683n - 5569, \\
e_2(n) &= 460n^3 - 2143n^2 + 601n + 6882, \\
e_3(n) &= -1223n^3 + 10388n^2 - 25365n + 17962, \\
e_4(n) &= 2(n-6)(n-4)(426n - 1111).
\end{aligned}
$$
For every integer $n \ge 6$ (so $n-5 \ge 1$), expanding $\sum_{i=0}^4 e_i(n) D(n-i) = \sum_{i=0}^4 e_i(n)\bigl(a(n-i) - (n-i)a(n-i-1)\bigr)$ and matching coefficients of $a(n-j)$ ($0 \le j \le 5$) against $C_j(n)$ gives an exact polynomial identity in $\mathbb{Z}[n]$ (verified by `verify.py`):
$$
M(n) = \sum_{i=0}^{4} e_i(n)\, D(n-i).
$$

### Step 3: Exact cancellation for $n \ge 6$
First, at $n = 6$, $e_4(6) = 0$, while $(e_0(6), e_1(6), e_2(6), e_3(6)) = (-1537, 4529, 32700, -24428)$ and $(D(6), D(5), D(4), D(3)) = (336, 40, 11, 1)$, so
$$
M(6) = \sum_{i=0}^{3} e_i(6)\, D(6-i) = -1537 \cdot 336 + 4529 \cdot 40 + 32700 \cdot 11 - 24428 \cdot 1 = -516432 + 181160 + 359700 - 24428 = 0.
$$
For $n \ge 7$, all five indices $n, \dots, n-4$ satisfy $n-i \ge 3$. Substituting $D(k) = (k-3)!\, S(k)$ for $k \ge 3$ gives:
- **Even $n = 2r$ ($r \ge 4$):** Factoring out $(2r-7)!$ yields
  $$
  M(2r) = (2r-7)!\, P_{\mathrm{even}}(r),
  $$
  where
  $$
  \begin{aligned}
  P_{\mathrm{even}}(r) &= e_0(2r)(2r-3)(2r-4)(2r-5)(2r-6) S(2r) + e_1(2r)(2r-4)(2r-5)(2r-6) S(2r-1) \\
  &\quad + e_2(2r)(2r-5)(2r-6) S(2r-2) + e_3(2r)(2r-6) S(2r-3) + e_4(2r) S(2r-4).
  \end{aligned}
  $$
- **Odd $n = 2r+1$ ($r \ge 3$):** Factoring out $(2r-6)!$ yields
  $$
  M(2r+1) = (2r-6)!\, P_{\mathrm{odd}}(r),
  $$
  where
  $$
  \begin{aligned}
  P_{\mathrm{odd}}(r) &= e_0(2r+1)(2r-2)(2r-3)(2r-4)(2r-5) S(2r+1) + e_1(2r+1)(2r-3)(2r-4)(2r-5) S(2r) \\
  &\quad + e_2(2r+1)(2r-4)(2r-5) S(2r-1) + e_3(2r+1)(2r-5) S(2r-2) + e_4(2r+1) S(2r-3).
  \end{aligned}
  $$

Exact polynomial expansion in $\mathbb{Z}[r]$ (verified by `verify.py`) yields $P_{\mathrm{even}}(r) \equiv 0$ and $P_{\mathrm{odd}}(r) \equiv 0$. Together with $M(6) = 0$, this gives $M(n) = 0$ for all integers $n \ge 6$. Finally, setting $a(0) := 0$ and indexing $m = n - 5 \ge 0$, direct evaluation at $n = 5$ ($m = 0$) gives $M(5) = \sum_{j=0}^{5} C_j(5) a(5-j) = 0$ (since $(C_0(5), \dots, C_4(5)) = (-1077, 8231, 2428, -43474, 2038)$ and $(a(5), \dots, a(1)) = (235, 39, 7, 2, 1)$). Thus $\sum_{m \ge 0} M(m+5)\frac{x^m}{m!} = 0$ holds identically, translating directly into the homogeneous order-6 polynomial-coefficient linear ODE $L[\hat{y}](x) = 0$ for $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ with non-zero leading $\hat{y}^{(6)}(x)$ coefficient $-460x(x-1)^2(x+1)$ (from $C_0(m+5) = -460m - 1077$), establishing D-finiteness. $\blacksquare$

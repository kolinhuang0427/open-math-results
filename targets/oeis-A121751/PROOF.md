# Proof of OEIS A121751 Recurrence Conjecture

## Theorem
Let $a(1) = 0$, $a(2) = 1$, and for $n \ge 3$,
$$
a(n) = 2\left\lfloor\frac{n-1}{2}\right\rfloor a(n-1) - \left(\left\lfloor\frac{n-1}{2}\right\rfloor\left\lfloor\frac{n-2}{2}\right\rfloor - 1\right) a(n-2).
$$
Then for every integer $n \ge 7$,
$$
M(n) := \sum_{j=0}^{6} C_j(n)\, a(n-j) = 0,
$$
where
$$
\begin{aligned}
C_0(n) &= 256, & C_1(n) &= -384, \\
C_2(n) &= 16(-8n^2+40n-67), & C_3(n) &= 16(8n^2-54n+87), \\
C_4(n) &= 4(4n^4-56n^3+242n^2-304n-21), & C_5(n) &= 4(-2n^4+38n^3-249n^2+647n-554), \\
C_6(n) &= (n-4)(n-8)(n^2-12n+31),
\end{aligned}
$$
and consequently the exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite.

## Proof

### Step 1: Parity split of the primary recurrence
For every integer $m \ge 3$:
- If $m = 2r$ is even ($r \ge 2$), then $\lfloor\frac{2r-1}{2}\rfloor = r - 1$ and $\lfloor\frac{2r-2}{2}\rfloor = r - 1$, so
  $$a(2r) = 2(r-1) a(2r-1) - r(r-2) a(2r-2).$$
- If $m = 2r+1$ is odd ($r \ge 1$), then $\lfloor\frac{2r}{2}\rfloor = r$ and $\lfloor\frac{2r-1}{2}\rfloor = r - 1$, so
  $$a(2r+1) = 2r\, a(2r) - (r^2 - r - 1) a(2r-1).$$

### Step 2: Reduction of $M(n)$ by parity for $n \ge 7$
Let $n \ge 7$. Each index $m \in \{n, n-1, n-2, n-3, n-4\}$ satisfies $m \ge 3$, so iterating the two parity recurrences five times expresses $a(n-4), a(n-3), a(n-2), a(n-1), a(n)$ uniquely as $\mathbb{Z}[k]$-linear combinations of $a(n-5)$ and $a(n-6)$:

1. **Even case $n = 2k$ ($k \ge 4$):** Writing $u = a(2k-5)$ and $v = a(2k-6)$, applying the even rule at $2k-4, 2k-2, 2k$ and the odd rule at $2k-3, 2k-1$ gives
   $$
   \begin{aligned}
   a(2k-4) &= 2(k-3)u - (k-2)(k-4)v, \\
   a(2k-3) &= 2(k-2)a(2k-4) - ((k-2)(k-3)-1)u, \\
   a(2k-2) &= 2(k-2)a(2k-3) - (k-1)(k-3)a(2k-4), \\
   a(2k-1) &= 2(k-1)a(2k-2) - ((k-1)(k-2)-1)a(2k-3), \\
   a(2k)   &= 2(k-1)a(2k-1) - k(k-2)a(2k-2).
   \end{aligned}
   $$
   Substituting these expressions and $n = 2k$ into $M(2k) = \sum_{j=0}^6 C_j(2k) a(2k-j)$ gives $M(2k) = A_{\mathrm{even}}(k) u + B_{\mathrm{even}}(k) v$, where exact univariate polynomial arithmetic in $\mathbb{Z}[k]$ (verified by `verify.py`) yields $A_{\mathrm{even}}(k) \equiv 0$ and $B_{\mathrm{even}}(k) \equiv 0$.

2. **Odd case $n = 2k+1$ ($k \ge 3$):** Writing $u = a(2k-4)$ and $v = a(2k-5)$, applying the odd rule at $2k-3, 2k-1, 2k+1$ and the even rule at $2k-2, 2k$ gives
   $$
   \begin{aligned}
   a(2k-3) &= 2(k-2)u - ((k-2)(k-3)-1)v, \\
   a(2k-2) &= 2(k-2)a(2k-3) - (k-1)(k-3)u, \\
   a(2k-1) &= 2(k-1)a(2k-2) - ((k-1)(k-2)-1)a(2k-3), \\
   a(2k)   &= 2(k-1)a(2k-1) - k(k-2)a(2k-2), \\
   a(2k+1) &= 2k\, a(2k) - (k(k-1)-1)a(2k-1).
   \end{aligned}
   $$
   Substituting these expressions and $n = 2k+1$ into $M(2k+1) = \sum_{j=0}^6 C_j(2k+1) a(2k+1-j)$ gives $M(2k+1) = A_{\mathrm{odd}}(k) u + B_{\mathrm{odd}}(k) v$, where exact univariate polynomial arithmetic in $\mathbb{Z}[k]$ (verified by `verify.py`) yields $A_{\mathrm{odd}}(k) \equiv 0$ and $B_{\mathrm{odd}}(k) \equiv 0$.

Therefore $M(n) = 0$ for all integers $n \ge 7$.

### Step 3: D-finiteness of the exponential generating function
Extend $a$ by $a(0) = 0$ so that $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ satisfies $\hat{y}^{(s)}(x) = \sum_{m \ge 0} a(m+s)\frac{x^m}{m!}$ for every $s \ge 0$. Writing $n = m + 6$ ($m \ge 1$), expand $C_j(m+6) = \sum_{r=0}^4 d_{j,r} m^r$ and set $\theta = x\frac{d}{dx}$. Because $\sum_{m \ge 1} m^r a(m+s)\frac{x^m}{m!} = \theta^r \hat{y}^{(s)}(x) - \delta_{r,0} a(s)$ (note $0^r = \delta_{r,0}$ at $m = 0$), multiplying $\sum_{j=0}^6 C_j(m+6)a(m+6-j) = 0$ by $\frac{x^m}{m!}$ and summing over $m \ge 1$ gives
$$
\sum_{j=0}^{6} \sum_{r=0}^{4} d_{j,r}\, \theta^r \hat{y}^{(6-j)}(x) = \sum_{j=0}^{6} C_j(6)\, a(6-j) = -20,
$$
where the boundary constant evaluates from $a(6),\dots,a(0) = 44,14,4,2,1,0,0$ as $256(44) - 384(14) - 1840(4) + 816(2) - 180(1) = -20$. Since $(6-j) + \deg C_j$ equals $6$ for $j \in \{0, 2, 4\}$ (with leading terms $256\hat{y}^{(6)}$, $-128 x^2 \hat{y}^{(6)}$, $16 x^4 \hat{y}^{(6)}$) and is at most $5$ for $j \in \{1, 3, 5, 6\}$, the left-hand side is a differential operator of order $6$ with leading coefficient $256 - 128x^2 + 16x^4 = 16(x^2 - 4)^2$. Differentiating once with respect to $x$ eliminates the constant $-20$ and yields a non-trivial homogeneous order-$7$ linear ODE with polynomial coefficients and nonzero leading coefficient $16(x^2 - 4)^2$ on $\hat{y}^{(7)}(x)$, proving that $\hat{y}(x)$ is D-finite. $\blacksquare$

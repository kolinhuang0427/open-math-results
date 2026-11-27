# Proof of OEIS A121747 Recurrence Conjecture

## Theorem
Let $a(1) = 1$ and $a(n) = n\, a(n-1) - d(n-1) + (n-1)!\lfloor n/2\rfloor$ for $n \ge 2$, where $d(1) = 1$, $d(2) = 0$, $d(2m) = d(2m-2) + (2m-1)!$ ($m \ge 2$), and $d(2m+1) = -d(2m)$ ($m \ge 1$). Then for every integer $n \ge 6$,
$$
M(n) := \sum_{j=0}^{5} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_5(n)$ are the polynomials stated in `TARGET.md`, and consequently the exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite.

## Proof

### Step 1: Elimination of $d(k)$ via $W(k) = D(k) + D(k-1)$
For every integer $k \ge 2$, define $D(k) := a(k) - k\, a(k-1) = -d(k-1) + (k-1)!\lfloor k/2\rfloor$, and for $k \ge 3$ set
$$
W(k) := D(k) + D(k-1) = a(k) - (k-1) a(k-1) - (k-1) a(k-2).
$$
From the defining recurrence of $d$:
- For $k = 2m$ ($m \ge 2$), $d(2m-1) + d(2m-2) = 0$, so
  $$W(2m) = (2m-1)!\, m + (2m-2)!\, (m-1) = (2m-2)!\, (2m^2 - 1).$$
- For $k = 2m+1$ ($m \ge 1$), at $m = 1$ we have $d(2) + d(1) = 0 + 1 = 1!$, while for $m \ge 2$ we have $d(2m) = d(2m-2) + (2m-1)!$ and $d(2m-1) = -d(2m-2)$, so $d(2m) + d(2m-1) = (2m-1)!$ holds for all $m \ge 1$; therefore
  $$W(2m+1) = -(2m-1)! + (2m)!\, m + (2m-1)!\, m = (2m-1)!\, (2m^2 + m - 1).$$

### Step 2: Operator factorization in $W(n-i)$
Define polynomials $c_0, c_1, c_2, c_3 \in \mathbb{Z}[n]$ by
$$
\begin{aligned}
c_0(n) &= -9n + 38, \\
c_1(n) &= -10n + 43, \\
c_2(n) &= 9n^3 - 56n^2 + 86n + 3, \\
c_3(n) &= (n-3)(n-4)(19n - 15).
\end{aligned}
$$
For every integer $n \ge 6$ (so $n-5 \ge 1$), expanding $\sum_{i=0}^3 c_i(n) W(n-i) = \sum_{i=0}^3 c_i(n)\bigl(a(n-i) - (n-i-1)a(n-i-1) - (n-i-1)a(n-i-2)\bigr)$ and collecting coefficients of $a(n-j)$ ($0 \le j \le 5$) matches $C_j(n)$ identically in $\mathbb{Z}[n]$ (verified by `verify.py`):
$$
M(n) = \sum_{i=0}^{3} c_i(n)\, W(n-i).
$$

### Step 3: Exact cancellation for $n \ge 6$
Since $n \ge 6$, all four indices $n, n-1, n-2, n-3$ are $\ge 3$, so the formulas of Step 1 apply to every $W(n-i)$ ($0 \le i \le 3$):
- **Even $n = 2r$ ($r \ge 3$):** Factoring out $(2r-5)!$ (with $(2r-5)! = 1! = 1$ at $r=3$) yields $M(2r) = (2r-5)!\, P_{\mathrm{even}}(r)$, where
  $$
  \begin{aligned}
  P_{\mathrm{even}}(r) &= c_0(2r)(2r-2)(2r-3)(2r-4)(2r^2 - 1) \\
  &\quad + c_1(2r)(2r-3)(2r-4)\bigl(2(r-1)^2 + (r-1) - 1\bigr) \\
  &\quad + c_2(2r)(2r-4)\bigl(2(r-1)^2 - 1\bigr) \\
  &\quad + c_3(2r)\bigl(2(r-2)^2 + (r-2) - 1\bigr).
  \end{aligned}
  $$
- **Odd $n = 2r+1$ ($r \ge 3$):** Factoring out $(2r-4)!$ yields $M(2r+1) = (2r-4)!\, P_{\mathrm{odd}}(r)$, where
  $$
  \begin{aligned}
  P_{\mathrm{odd}}(r) &= c_0(2r+1)(2r-1)(2r-2)(2r-3)(2r^2 + r - 1) \\
  &\quad + c_1(2r+1)(2r-2)(2r-3)(2r^2 - 1) \\
  &\quad + c_2(2r+1)(2r-3)\bigl(2(r-1)^2 + (r-1) - 1\bigr) \\
  &\quad + c_3(2r+1)\bigl(2(r-1)^2 - 1\bigr).
  \end{aligned}
  $$

Exact polynomial arithmetic in $\mathbb{Z}[r]$ (verified by `verify.py`) yields $P_{\mathrm{even}}(r) \equiv 0$ and $P_{\mathrm{odd}}(r) \equiv 0$. Hence $M(n) = 0$ for all $n \ge 6$.

### Step 4: D-finiteness of the exponential generating function
Extend $a$ by $a(0) = 0$ so that $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ satisfies $\hat{y}^{(s)}(x) = \sum_{m \ge 0} a(m+s)\frac{x^m}{m!}$ ($s \ge 0$). Writing $n = m + 5$ ($m \ge 1$), expand $C_j(m+5) = \sum_{r=0}^4 d_{j,r} m^r$ and set $\theta = x\frac{d}{dx}$. Using $\sum_{m \ge 1} m^r a(m+s)\frac{x^m}{m!} = \theta^r \hat{y}^{(s)}(x) - \delta_{r,0} a(s)$, multiplying $\sum_{j=0}^5 C_j(m+5)a(m+5-j) = 0$ by $\frac{x^m}{m!}$ and summing over $m \ge 1$ gives
$$
\sum_{j=0}^{5} \sum_{r=0}^{4} d_{j,r}\, \theta^r \hat{y}^{(5-j)}(x) = \sum_{j=0}^{5} C_j(5)\, a(5-j) = 0,
$$
where the boundary sum evaluates from $a(5),\dots,a(0) = 262,44,8,2,1,0$ as $(-7)(262) + 21(44) + 207(8) - 135(2) - 476(1) = 0$. Since $(5-j) + \deg C_j$ equals $6$ for $j \in \{0, 1, 2, 3\}$ (with leading terms $-9x\hat{y}^{(6)}, 9x^2\hat{y}^{(6)}, 9x^3\hat{y}^{(6)}, -9x^4\hat{y}^{(6)}$) and is at most $5$ for $j \in \{4, 5\}$, this yields a non-trivial homogeneous order-$6$ linear ODE with polynomial coefficients and nonzero leading coefficient $-9x(x-1)^2(x+1)$ on $\hat{y}^{(6)}(x)$, proving that $\hat{y}(x)$ is D-finite. $\blacksquare$

# Proof of OEIS A121750 Recurrence Conjecture

## Theorem
Let $a(1) = 0$ and $a(n) = n\, a(n-1) + d(n-1) + (n-1)!\lfloor(n-1)/2\rfloor$ for $n \ge 2$, where $d(1) = 1$, $d(2) = 0$, $d(2m) = d(2m-2) + (2m-1)!$ ($m \ge 2$), and $d(2m+1) = -d(2m)$ ($m \ge 1$). Then for every integer $n \ge 7$,
$$
M(n) := \sum_{j=0}^{6} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_6(n)$ are the polynomials stated in `TARGET.md`, and consequently the exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ is D-finite.

## Proof

### Step 1: Elimination of $d(k)$ via $W(k) = D(k) + D(k-1)$
For every integer $k \ge 2$, define $D(k) := a(k) - k\, a(k-1) = d(k-1) + (k-1)!\lfloor(k-1)/2\rfloor$, and for $k \ge 3$ set
$$
W(k) := D(k) + D(k-1) = a(k) - (k-1) a(k-1) - (k-1) a(k-2).
$$
From the defining recurrence of $d$:
- For $k = 2m$ ($m \ge 2$), $d(2m-1) + d(2m-2) = 0$, so
  $$W(2m) = (2m-1)!(m-1) + (2m-2)!(m-1) = (2m-2)!\,(2m^2 - 2m).$$
- For $k = 2m+1$ ($m \ge 1$), at $m = 1$ we have $d(2) + d(1) = 0 + 1 = 1!$, while for $m \ge 2$ we have $d(2m) = d(2m-2) + (2m-1)!$ and $d(2m-1) = -d(2m-2)$, so $d(2m) + d(2m-1) = (2m-1)!$ holds for all $m \ge 1$; therefore
  $$W(2m+1) = (2m-1)! + (2m)!\, m + (2m-1)!(m-1) = (2m-1)!\,(2m^2 + m).$$

### Step 2: Operator factorization in $W(n-i)$
Define polynomials $c_0, \dots, c_4 \in \mathbb{Z}[n]$ by
$$
\begin{aligned}
c_0(n) &= 1, \\
c_1(n) &= -3, \\
c_2(n) &= -n^2 + 2n + 3, \\
c_3(n) &= 2n^2 - 10n + 8, \\
c_4(n) &= -n^2 + 8n - 15.
\end{aligned}
$$
For every integer $n \ge 7$ (so $n-6 \ge 1$), expanding $\sum_{i=0}^4 c_i(n) W(n-i) = \sum_{i=0}^4 c_i(n)\bigl(a(n-i) - (n-i-1)a(n-i-1) - (n-i-1)a(n-i-2)\bigr)$ and collecting coefficients of $a(n-j)$ ($0 \le j \le 6$) matches $C_j(n)$ identically in $\mathbb{Z}[n]$ (verified by `verify.py`):
$$
M(n) = \sum_{i=0}^{4} c_i(n)\, W(n-i).
$$

### Step 3: Exact cancellation for $n \ge 7$
Since $n \ge 7$, all five indices $n, \dots, n-4$ satisfy $n-i \ge 3$, so Step 1 applies to every $W(n-i)$ ($0 \le i \le 4$):
- **Even $n = 2r$ ($r \ge 4$):** Factoring out $(2r-6)!$ yields $M(2r) = (2r-6)!\, P_{\mathrm{even}}(r)$, where
  $$
  \begin{aligned}
  P_{\mathrm{even}}(r) &= c_0(2r)(2r-2)(2r-3)(2r-4)(2r-5)(2r^2 - 2r) \\
  &\quad + c_1(2r)(2r-3)(2r-4)(2r-5)\bigl(2(r-1)^2 + (r-1)\bigr) \\
  &\quad + c_2(2r)(2r-4)(2r-5)\bigl(2(r-1)^2 - 2(r-1)\bigr) \\
  &\quad + c_3(2r)(2r-5)\bigl(2(r-2)^2 + (r-2)\bigr) \\
  &\quad + c_4(2r)\bigl(2(r-2)^2 - 2(r-2)\bigr).
  \end{aligned}
  $$
- **Odd $n = 2r+1$ ($r \ge 3$):** Factoring out $(2r-5)!$ yields $M(2r+1) = (2r-5)!\, P_{\mathrm{odd}}(r)$, where
  $$
  \begin{aligned}
  P_{\mathrm{odd}}(r) &= c_0(2r+1)(2r-1)(2r-2)(2r-3)(2r-4)(2r^2 + r) \\
  &\quad + c_1(2r+1)(2r-2)(2r-3)(2r-4)(2r^2 - 2r) \\
  &\quad + c_2(2r+1)(2r-3)(2r-4)\bigl(2(r-1)^2 + (r-1)\bigr) \\
  &\quad + c_3(2r+1)(2r-4)\bigl(2(r-1)^2 - 2(r-1)\bigr) \\
  &\quad + c_4(2r+1)\bigl(2(r-2)^2 + (r-2)\bigr).
  \end{aligned}
  $$

Exact polynomial arithmetic in $\mathbb{Z}[r]$ (verified by `verify.py`) yields $P_{\mathrm{even}}(r) \equiv 0$ and $P_{\mathrm{odd}}(r) \equiv 0$. Hence $M(n) = 0$ for all $n \ge 7$.

### Step 4: D-finiteness of the exponential generating function
Extend $a$ by $a(0) = 0$ so that $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$ satisfies $\hat{y}^{(s)}(x) = \sum_{m \ge 0} a(m+s)\frac{x^m}{m!}$ ($s \ge 0$). Writing $n = m + 6$ ($m \ge 1$), expand $C_j(m+6) = \sum_{r=0}^3 d_{j,r} m^r$ and set $\theta = x\frac{d}{dx}$. Using $\sum_{m \ge 1} m^r a(m+s)\frac{x^m}{m!} = \theta^r \hat{y}^{(s)}(x) - \delta_{r,0} a(s)$, multiplying $\sum_{j=0}^6 C_j(m+6)a(m+6-j) = 0$ by $\frac{x^m}{m!}$ and summing over $m \ge 1$ gives
$$
\sum_{j=0}^{6} \sum_{r=0}^{3} d_{j,r}\, \theta^r \hat{y}^{(6-j)}(x) = \sum_{j=0}^{6} C_j(6)\, a(6-j) = -3,
$$
evaluating from $a(6),\dots,a(0) = 1338,184,26,5,1,0,0$ as $1(1338) - 8(184) - 14(26) + 95(5) + 20(1) = -3$. Here $(6-j) + \deg C_j$ equals $6$ for $j \in \{0, 1, 2, 3\}$ (with leading terms $\hat{y}^{(6)}, -x\hat{y}^{(6)}, -x^2\hat{y}^{(6)}, x^3\hat{y}^{(6)}$) and is at most $5$ for $j \in \{4, 5, 6\}$, giving an order-$6$ operator with leading coefficient $1 - x - x^2 + x^3 = (1-x)^2(1+x)$. Differentiating once annihilates $-3$ and yields a non-trivial homogeneous order-$7$ linear ODE with polynomial coefficients and nonzero leading coefficient $(1-x)^2(1+x)$ on $\hat{y}^{(7)}(x)$, proving that $\hat{y}(x)$ is D-finite. $\blacksquare$

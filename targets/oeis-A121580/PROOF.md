# Proof of OEIS A121580 Recurrence Conjecture

## Theorem
Let $a(1) = 1$ and $a(n) = a(n-1) + (n-1)!\bigl(1 + \frac{n(n-1)}{2}\bigr)$ for every integer $n \ge 2$. Then for every integer $n \ge 5$,
$$
a(n) + (-n-4)a(n-1) + 3(n+1)a(n-2) + 2(-2n+3)a(n-3) + 2(n-3)a(n-4) = 0,
$$
and the exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n) \frac{x^n}{n!}$ is D-finite.

## Proof

### Step 1: First-difference telescoping
For every integer $k \ge 2$, define the first difference
$$
b(k) := a(k) - a(k-1) = (k-1)!\left(1 + \frac{k(k-1)}{2}\right) = \frac{(k-1)!}{2}(k^2 - k + 2).
$$
For any integer $n \ge 5$, observe the polynomial identity in the coefficients of $a(n), \dots, a(n-4)$:
$$
\begin{aligned}
a(n) &+ (-n-4)a(n-1) + 3(n+1)a(n-2) + 2(-2n+3)a(n-3) + 2(n-3)a(n-4) \\
&= \bigl(a(n) - a(n-1)\bigr) + (-n-3)\bigl(a(n-1) - a(n-2)\bigr) \\
&\quad + 2n\bigl(a(n-2) - a(n-3)\bigr) + (-2n+6)\bigl(a(n-3) - a(n-4)\bigr).
\end{aligned}
$$
Indeed, matching the coefficients of $a(n), a(n-1), a(n-2), a(n-3), a(n-4)$ on the right-hand side gives:
- $a(n)$: $1$,
- $a(n-1)$: $-1 + (-n-3) = -n-4$,
- $a(n-2)$: $-(-n-3) + 2n = 3n + 3 = 3(n+1)$,
- $a(n-3)$: $-2n + (-2n+6) = -4n + 6 = 2(-2n+3)$,
- $a(n-4)$: $-(-2n+6) = 2(n-3)$.

### Step 2: Exact cancellation
Since $n \ge 5$, each index $k \in \{n, n-1, n-2, n-3\}$ satisfies $k \ge 2$, so $a(k) - a(k-1) = b(k) = \frac{(k-1)!}{2}(k^2 - k + 2)$. Moreover, $n - 4 \ge 1$, so $(n-4)!$ is a well-defined positive integer and
$$
\begin{aligned}
b(n) &= \frac{(n-4)!}{2}(n-1)(n-2)(n-3)(n^2 - n + 2), \\
b(n-1) &= \frac{(n-4)!}{2}(n-2)(n-3)\bigl((n-1)^2 - (n-1) + 2\bigr), \\
b(n-2) &= \frac{(n-4)!}{2}(n-3)\bigl((n-2)^2 - (n-2) + 2\bigr), \\
b(n-3) &= \frac{(n-4)!}{2}\bigl((n-3)^2 - (n-3) + 2\bigr).
\end{aligned}
$$
Substituting these expressions into the right-hand side of Step 1 factors out $\frac{(n-4)!}{2}$ multiplied by the polynomial
$$
\begin{aligned}
P(n) &= (n-1)(n-2)(n-3)(n^2 - n + 2) \\
&\quad - (n+3)(n-2)(n-3)\bigl((n-1)^2 - (n-1) + 2\bigr) \\
&\quad + 2n(n-3)\bigl((n-2)^2 - (n-2) + 2\bigr) \\
&\quad - 2(n-3)\bigl((n-3)^2 - (n-3) + 2\bigr).
\end{aligned}
$$
Expanding each summand in $\mathbb{Z}[n]$ (verified by `verify.py`):
$$
\begin{aligned}
(n-1)(n-2)(n-3)(n^2 - n + 2) &= n^5 - 7n^4 + 19n^3 - 29n^2 + 28n - 12, \\
-(n+3)(n-2)(n-3)(n^2 - 3n + 4) &= -n^5 + 5n^4 - n^3 - 37n^2 + 90n - 72, \\
2n(n-3)(n^2 - 5n + 8) &= 2n^4 - 16n^3 + 46n^2 - 48n, \\
-2(n-3)(n^2 - 7n + 14) &= -2n^3 + 20n^2 - 70n + 84.
\end{aligned}
$$
Summing the coefficients power by power in $n$ gives $0$ for every degree $0, \dots, 5$, so $P(n) \equiv 0 \in \mathbb{Z}[n]$, proving the recurrence for all $n \ge 5$.

### Step 3: D-finiteness of the exponential generating function
Setting $a(0) = 0$ (which satisfies $a(4) - 8a(3) + 15a(2) - 10a(1) + 2a(0) = 53 - 88 + 45 - 10 + 0 = 0$) and writing $m = n - 4 \ge 0$, the recurrence reads
$$a(m+4) - (m+8)a(m+3) + (3m+15)a(m+2) - (4m+10)a(m+1) + (2m+2)a(m) = 0 \qquad (m \ge 0).$$
Multiplying by $\frac{x^m}{m!}$ and summing over $m \ge 0$, using $\sum_{m \ge 0} a(m+k)\frac{x^m}{m!} = \hat{y}^{(k)}(x)$ and $\sum_{m \ge 0} m\, a(m+k)\frac{x^m}{m!} = x \hat{y}^{(k+1)}(x)$, yields the homogeneous order-$4$ linear ODE with polynomial coefficients for $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$:
$$(1 - x)\hat{y}^{(4)}(x) + (3x - 8)\hat{y}^{(3)}(x) + (15 - 4x)\hat{y}''(x) + (2x - 10)\hat{y}'(x) + 2\hat{y}(x) = 0,$$
proving that $\hat{y}(x)$ is D-finite. $\blacksquare$

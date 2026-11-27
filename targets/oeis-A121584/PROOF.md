# Proof of OEIS A121584 Recurrence Conjecture

## Theorem
Let $a(1) = 1$, $a(2) = 4$, and for $n \ge 3$,
$$
a(n) = \frac{(2n-3)a(n-1)-(n-1)a(n-2)}{n-2} + \frac{1}{2}(2n^3-9n^2+17n-16)\frac{(n-1)!}{n-2}.
$$
Then for every integer $n \ge 6$,
$$
M(n) := \sum_{j=0}^{5} C_j(n)\, a(n-j) = 0,
$$
where
$$
\begin{aligned}
C_0(n) &= 14(-n+1), & C_1(n) &= 14n^2+1731n-6995, \\
C_2(n) &= 3(-577n^2+480n+7243), & C_3(n) &= 2(2781n^2-11952n+6004), \\
C_4(n) &= -5987n^2+36181n-54220, & C_5(n) &= 2(1071n-3433)(n-4),
\end{aligned}
$$
and consequently the exponential generating function $\hat{y}(x) = \sum_{n \ge 1} a(n) \frac{x^n}{n!}$ is D-finite.

## Proof

### Step 1: Second-order difference operator
For every integer $k \ge 3$, clearing the denominator $k - 2 \ge 1$ in the primary defining recurrence of $a(k)$ yields
$$
B(k) := (k-2)a(k) - (2k-3)a(k-1) + (k-1)a(k-2) = \frac{(k-1)!}{2}\, f(k),
$$
where $f(k) := 2k^3 - 9k^2 + 17k - 16$.

### Step 2: Exact operator factorization
Define polynomials $d_0, d_1, d_2, d_3 \in \mathbb{Z}[n]$ by
$$
\begin{aligned}
d_0(n) &= 14(-n+1)(n-3), \\
d_1(n) &= 14n^3 + 1675n^2 - 10387n + 13948, \\
d_2(n) &= (-1703n^2 + 3171n + 7574)(n-2), \\
d_3(n) &= 2(1071n - 3433)(n-2)(n-3).
\end{aligned}
$$
For every integer $n \ge 6$, all indices $n-5, \dots, n$ are $\ge 1$, and expanding the coefficients of $a(n), a(n-1), \dots, a(n-5)$ in $d_0(n) B(n) + d_1(n) B(n-1) + d_2(n) B(n-2) + d_3(n) B(n-3)$ matches $(n-2)(n-3) C_j(n)$ identically in $\mathbb{Z}[n]$ for each $j \in \{0, \dots, 5\}$ (verified coefficient-by-coefficient in `verify.py`):
$$
(n-2)(n-3)\, M(n) = \sum_{j=0}^{3} d_j(n)\, B(n-j).
$$

### Step 3: Exact cancellation
Since $n \ge 6$, every index $k \in \{n, n-1, n-2, n-3\}$ satisfies $k \ge 3$, so $B(k) = \frac{(k-1)!}{2} f(k)$ holds for all four terms, and $n - 4 \ge 2$ makes $(n-4)!$ a well-defined positive integer. Factoring out $\frac{(n-4)!}{2}$ gives
$$
(n-2)(n-3)\, M(n) = \frac{(n-4)!}{2}\, P(n),
$$
where
$$
\begin{aligned}
P(n) &= d_0(n)(n-1)(n-2)(n-3) f(n) + d_1(n)(n-2)(n-3) f(n-1) \\
&\quad + d_2(n)(n-3) f(n-2) + d_3(n) f(n-3).
\end{aligned}
$$
Direct polynomial expansion in $\mathbb{Z}[n]$ (verified in `verify.py`) shows $P(n) \equiv 0$. Since $(n-2)(n-3) > 0$ for all $n \ge 6$, we conclude $M(n) = 0$ for every integer $n \ge 6$. Finally, multiplying $M(n) = 0$ by $\frac{x^{n-5}}{(n-5)!}$ and summing over $n \ge 6$ produces a polynomial-coefficient linear ODE for $\hat{y}(x) = \sum_{n \ge 1} a(n)\frac{x^n}{n!}$, so $\hat{y}(x)$ is D-finite. $\blacksquare$

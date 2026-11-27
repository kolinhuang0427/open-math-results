# Proof of OEIS A158960 M. F. Hasler (2014) Denominator Conjecture

## Theorem
Let $H_n(x)$ ($n \ge 0$) denote the $n$-th (physicists') Hermite polynomial (DLMF Table 18.9.1), defined by $H_0(x) = 1$, $H_1(x) = 2x$, and
$$
H_n(x) = 2x\, H_{n-1}(x) - 2(n-1)\, H_{n-2}(x) \qquad (n \ge 2).
$$
Then for every integer $n \ge 0$, the reduced rational number $H_n(1/5) \in \mathbb{Q}$ has denominator exactly $5^n$ (and numerator $a(n) = 5^n H_n(1/5)$).

## Proof
For every integer $n \ge 0$, define $b(n) := 5^n H_n(1/5)$. From $H_0(1/5) = 1$ and $H_1(1/5) = 2/5$, we have $b(0) = 1$ and $b(1) = 2$. For $n \ge 2$, multiplying the Hermite three-term recurrence at $x = 1/5$ by $5^n$ yields
$$
b(n) = 5^n \left(\frac{2}{5} H_{n-1}(1/5) - 2(n-1) H_{n-2}(1/5)\right) = 2\, b(n-1) - 50(n-1)\, b(n-2).
$$
By induction on $n$, $b(n) \in \mathbb{Z}$ for every $n \ge 0$, so $H_n(1/5) = b(n) / 5^n$.

Reducing the recurrence modulo $5$ (using $50 \equiv 0 \pmod 5$) gives
$$
b(n) \equiv 2\, b(n-1) \pmod 5 \qquad (\forall n \ge 2).
$$
Together with $b(0) = 1$ and $b(1) = 2$, induction on $n$ shows
$$
b(n) \equiv 2^n \pmod 5 \qquad (\forall n \ge 0).
$$
Since $5 \nmid 2^n$, we have $5 \nmid b(n)$ and hence $\gcd(b(n), 5^n) = 1$ for every $n \ge 0$. Because $H_n(1/5) = \frac{b(n)}{5^n}$ is already in lowest terms, its reduced denominator is $5^n$ and its numerator is $b(n) = 5^n H_n(1/5)$ for all $n \ge 0$. $\blacksquare$

# Proof of Colin Barker's Conjectures for OEIS A274272

## Statement

Let $a(n)$ ($n \ge 0$) denote the number of partitions of $5^n$ into at most $4$ parts (`A274272`, rev. 12). Then:
1. For every integer $n \ge 0$,
   $$a(n) = \frac{57 + 8(-1)^n + 63 \cdot 5^n + 3 \cdot 5^{1+2n} + 125^n}{144}.$$
2. For every integer $n > 4$ (i.e. $n \ge 5$),
   $$a(n) = 155 a(n-1) - 3874 a(n-2) + 15470 a(n-3) + 3875 a(n-4) - 15625 a(n-5).$$
3. The ordinary generating function is
   $$\sum_{n=0}^{\infty} a(n) x^n = \frac{1 - 149x + 3129x^2 - 5655x^3 - 6750x^4}{(1-x)(1+x)(1-5x)(1-25x)(1-125x)}.$$

All three conjectured claims in OEIS `A274272` (rev. 12) hold unconditionally.

---

## 1. Generating Function and Partial Fraction Decomposition

By Ferrers conjugation, the number of partitions of $m \ge 0$ into at most $4$ parts equals the number of partitions of $m$ with parts in $\{1, 2, 3, 4\}$, which is $p(m, \le 4) = [x^m] F(x)$ where
$$F(x) := \frac{1}{(1-x)(1-x^2)(1-x^3)(1-x^4)}.$$
Hence $a(n) = [x^{5^n}] F(x)$ for every $n \ge 0$.

In $\mathbb{Q}(x)$, $F(x)$ admits the exact partial fraction decomposition:
$$F(x) = \frac{1}{24(1-x)^4} + \frac{1}{8(1-x)^3} + \frac{59}{288(1-x)^2} + \frac{17}{72(1-x)} + \frac{1}{8(1+x)} + \frac{1}{32(1+x)^2} + \frac{1}{8(1+x^2)} + \frac{1+x}{9(1+x+x^2)},$$
which holds by clearing the denominator $288(1-x)(1-x^2)(1-x^3)(1-x^4)$:
$$(175 - 358x + 263x^2 - 68x^3)(1+x)^2(1+x^2)(1+x+x^2) + 9(5+4x)(1-x)^4(1+x^2)(1+x+x^2)$$
$$+ 36(1-x)^4(1+x)^2(1+x+x^2) + 32(1+x)(1-x)^4(1+x)^2(1+x^2) = 288.$$

---

## 2. Exact Evaluation at $m = 5^n$ for all $n \ge 0$

Fix $n \ge 0$ and set $m := 5^n$. Observe that **$m$ is odd**, and since $5 \equiv -1 \pmod 3$, we have
$$m = 5^n \equiv (-1)^n \pmod 3,$$
so $m \equiv 1 \pmod 3$ when $n$ is even, and $m \equiv 2 \pmod 3$ when $n$ is odd.

Extracting $[x^m]$ term by term from the partial fraction expansion of $F(x)$:

1. **Poles at $x = 1$:** Using $[x^m](1-x)^{-r} = \binom{m+r-1}{r-1}$,
   $$[x^m]\!\left(\frac{1}{24(1-x)^4} + \frac{1}{8(1-x)^3} + \frac{59}{288(1-x)^2} + \frac{17}{72(1-x)}\right) = \frac{2m^3 + 30m^2 + 135m + 175}{288}.$$

2. **Poles at $x = -1$:** Because $m = 5^n$ is odd, $(-1)^m = -1$, so
   $$[x^m]\!\left(\frac{1}{8(1+x)} + \frac{1}{32(1+x)^2}\right) = -\frac{1}{8} - \frac{m+1}{32} = \frac{-9m - 45}{288}.$$

3. **Poles at $x = \pm i$:** Since $\frac{1}{8(1+x^2)} = \frac{1}{8}\sum_{j=0}^{\infty} (-1)^j x^{2j}$ is an even power series and $m$ is odd,
   $$[x^m]\frac{1}{8(1+x^2)} = 0.$$

4. **Poles at primitive cube roots of unity:** Expanding
   $$\frac{1+x}{9(1+x+x^2)} = \frac{1-x^2}{9(1-x^3)} = \frac{1}{9}\sum_{j=0}^{\infty} \bigl(x^{3j} - x^{3j+2}\bigr),$$
   the coefficient of $x^m$ is $0$ when $m \equiv 1 \pmod 3$ ($n$ even), and $-\frac{1}{9}$ when $m \equiv 2 \pmod 3$ ($n$ odd). Uniformly for all $n \ge 0$,
   $$[x^{5^n}]\frac{1+x}{9(1+x+x^2)} = \frac{(-1)^n - 1}{18} = \frac{16(-1)^n - 16}{288}.$$

Summing the four contributions and noting $15m^2 = 15 \cdot 25^n = 3 \cdot 5^{1+2n}$ and $m^3 = 125^n$:
$$\begin{aligned}
a(n) = [x^{5^n}]F(x)
&= \frac{2m^3 + 30m^2 + 135m + 175 - 9m - 45 + 16(-1)^n - 16}{288} \\
&= \frac{2m^3 + 30m^2 + 126m + 114 + 16(-1)^n}{288} \\
&= \frac{57 + 8(-1)^n + 63 \cdot 5^n + 3 \cdot 5^{1+2n} + 125^n}{144},
\end{aligned}$$
which holds for all $n \ge 0$ and proves the first conjecture.

---

## 3. Rational Generating Function and Linear Recurrence

Using $3 \cdot 5^{1+2n} = 15 \cdot 25^n$, summing the five geometric series from the closed form for $a(n)$ ($n \ge 0$) yields
$$G(x) := \sum_{n=0}^{\infty} a(n) x^n = \frac{1}{144}\left(\frac{57}{1-x} + \frac{8}{1+x} + \frac{63}{1-5x} + \frac{15}{1-25x} + \frac{1}{1-125x}\right).$$
Putting this over the common denominator
$$D(x) := (1-x)(1+x)(1-5x)(1-25x)(1-125x) = 1 - 155x + 3874x^2 - 15470x^3 - 3875x^4 + 15625x^5$$
gives the exact numerator polynomial (verified in $\mathbb{Q}[x]$ in `verify.py`):
$$G(x) = \frac{1 - 149x + 3129x^2 - 5655x^3 - 6750x^4}{(1-x)(1+x)(1-5x)(1-25x)(1-125x)},$$
proving the third conjecture.

Finally, because the numerator $D(x) G(x)$ has degree $4$, the coefficient of $x^n$ in $D(x) G(x)$ vanishes for all $n > 4$:
$$a(n) - 155 a(n-1) + 3874 a(n-2) - 15470 a(n-3) - 3875 a(n-4) + 15625 a(n-5) = 0 \quad (n > 4),$$
proving the second conjecture. $\blacksquare$

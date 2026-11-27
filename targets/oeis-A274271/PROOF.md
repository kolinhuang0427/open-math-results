# Proof of Colin Barker's Conjectures for OEIS A274271

## Statement

Let $a(n)$ ($n \ge 0$) denote the number of partitions of $3^n$ into at most $4$ parts (`A274271`, rev. 12). Then:
1. $a(0) = 1$, and for every integer $n \ge 1$ (in particular, for all $n > 1$),
   $$a(n) = \frac{(3 + 3^n)^2 (9 + 3^n)}{144}.$$
2. For every integer $n > 4$ (i.e. $n \ge 5$),
   $$a(n) = 40 a(n-1) - 390 a(n-2) + 1080 a(n-3) - 729 a(n-4).$$
3. The ordinary generating function is
   $$\sum_{n=0}^{\infty} a(n) x^n = \frac{1 - 37x + 288x^2 - 405x^3 - 81x^4}{(1-x)(1-3x)(1-9x)(1-27x)}.$$

All three conjectured claims in OEIS `A274271` (rev. 12) hold unconditionally.

---

## 1. Generating Function and Partial Fraction Decomposition

By Ferrers conjugation, the number of partitions of an integer $m \ge 0$ into at most $4$ parts equals the number of partitions of $m$ with all parts in $\{1, 2, 3, 4\}$, which is the coefficient $[x^m] F(x)$ of
$$F(x) := \frac{1}{(1-x)(1-x^2)(1-x^3)(1-x^4)}.$$
Hence $a(n) = [x^{3^n}] F(x)$ for all $n \ge 0$, with $a(0) = [x^1] F(x) = 1$.

In $\mathbb{Q}(x)$, $F(x)$ admits the exact partial fraction decomposition:
$$F(x) = \frac{1}{24(1-x)^4} + \frac{1}{8(1-x)^3} + \frac{59}{288(1-x)^2} + \frac{17}{72(1-x)} + \frac{1}{8(1+x)} + \frac{1}{32(1+x)^2} + \frac{1}{8(1+x^2)} + \frac{1+x}{9(1+x+x^2)}.$$
*Verification.* Clearing the common denominator $288(1-x)^4(1+x)^2(1+x^2)(1+x+x^2) = 288(1-x)(1-x^2)(1-x^3)(1-x^4)$:
- Notice $\frac{1}{24(1-x)^4} + \frac{1}{8(1-x)^3} + \frac{59}{288(1-x)^2} + \frac{17}{72(1-x)} = \frac{12 + 36(1-x) + 59(1-x)^2 + 68(1-x)^3}{288(1-x)^4} = \frac{175 - 358x + 263x^2 - 68x^3}{288(1-x)^4}$.
- Notice $\frac{1}{8(1+x)} + \frac{1}{32(1+x)^2} = \frac{5 + 4x}{32(1+x)^2}$.
- Multiplying out over $288(1-x)(1-x^2)(1-x^3)(1-x^4)$ reduces to the exact polynomial identity:
  $$(175 - 358x + 263x^2 - 68x^3)(1+x)^2(1+x^2)(1+x+x^2) + 9(5+4x)(1-x)^4(1+x^2)(1+x+x^2)$$
  $$+ 36(1-x)^4(1+x)^2(1+x+x^2) + 32(1+x)(1-x)^4(1+x)^2(1+x^2) = 288.$$
  (Checked symbolically in $\mathbb{Q}[x]$ in `verify.py`.)

---

## 2. Exact Evaluation at $m = 3^n$ for $n \ge 1$

Let $n \ge 1$ and set $m := 3^n$. Since $n \ge 1$, **$m$ is odd and $3 \mid m$**. We extract $[x^m]$ term by term from the partial fraction expansion of $F(x)$:

1. **Poles at $x = 1$:** Using $[x^m](1-x)^{-r} = \binom{m+r-1}{r-1}$,
   $$\begin{aligned}
   [x^m]\!\left(\frac{1}{24(1-x)^4} + \frac{1}{8(1-x)^3} + \frac{59}{288(1-x)^2} + \frac{17}{72(1-x)}\right)
   &= \frac{(m+3)(m+2)(m+1)}{144} + \frac{(m+2)(m+1)}{16} + \frac{59(m+1)}{288} + \frac{17}{72} \\
   &= \frac{2m^3 + 30m^2 + 135m + 175}{288}.
   \end{aligned}$$

2. **Poles at $x = -1$:** Using $[x^m](1+x)^{-r} = (-1)^m \binom{m+r-1}{r-1}$ and the fact that $m = 3^n$ is odd so $(-1)^m = -1$,
   $$[x^m]\!\left(\frac{1}{8(1+x)} + \frac{1}{32(1+x)^2}\right) = -\frac{1}{8} - \frac{m+1}{32} = \frac{-9m - 45}{288}.$$

3. **Poles at $x = \pm i$:** Since $\frac{1}{8(1+x^2)} = \frac{1}{8}\sum_{j=0}^{\infty} (-1)^j x^{2j}$ has nonzero coefficients only at even exponents, and $m = 3^n$ is odd,
   $$[x^m]\frac{1}{8(1+x^2)} = 0.$$

4. **Poles at primitive cube roots of unity:** Writing
   $$\frac{1+x}{9(1+x+x^2)} = \frac{1-x^2}{9(1-x^3)} = \frac{1}{9}\sum_{j=0}^{\infty}\bigl(x^{3j} - x^{3j+2}\bigr),$$
   and using $3 \mid m$ for $n \ge 1$, we obtain
   $$[x^m]\frac{1+x}{9(1+x+x^2)} = \frac{1}{9} = \frac{32}{288}.$$

Summing the four contributions gives, for all $n \ge 1$ ($m = 3^n$):
$$a(n) = [x^m]F(x) = \frac{2m^3 + 30m^2 + 135m + 175 - 9m - 45 + 32}{288} = \frac{m^3 + 15m^2 + 63m + 81}{144} = \frac{(3+m)^2(9+m)}{144}.$$
Substituting $m = 3^n$ yields
$$a(n) = \frac{(3 + 3^n)^2 (9 + 3^n)}{144} \quad \text{for all } n \ge 1,$$
which proves the first conjecture (and shows it holds starting from $n = 1$, hence for all $n > 1$).

---

## 3. Rational Generating Function and Linear Recurrence

Expanding the closed form for $n \ge 1$:
$$\frac{(3 + 3^n)^2(9 + 3^n)}{144} = \frac{81 + 63 \cdot 3^n + 15 \cdot 9^n + 27^n}{144}.$$
Let $G_{\mathrm{closed}}(x) := \sum_{n=0}^{\infty} \frac{81 + 63\cdot 3^n + 15\cdot 9^n + 27^n}{144} x^n$. Its $n=0$ value is $\frac{81+63+15+1}{144} = \frac{160}{144} = \frac{10}{9}$, whereas $a(0) = 1$, so $a(0) - G_{\mathrm{closed}}(0) = -\frac{1}{9}$. Summing the four geometric series yields:
$$\begin{aligned}
G(x) := \sum_{n=0}^{\infty} a(n) x^n
&= -\frac{1}{9} + \frac{1}{144}\left(\frac{81}{1-x} + \frac{63}{1-3x} + \frac{15}{1-9x} + \frac{1}{1-27x}\right) \\
&= \frac{-16(1-x)(1-3x)(1-9x)(1-27x) + 81(1-3x)(1-9x)(1-27x) + \cdots}{144(1-x)(1-3x)(1-9x)(1-27x)} \\
&= \frac{1 - 37x + 288x^2 - 405x^3 - 81x^4}{(1-x)(1-3x)(1-9x)(1-27x)},
\end{aligned}$$
proving the third conjecture.

Finally, expanding the denominator gives
$$(1-x)(1-3x)(1-9x)(1-27x) = 1 - 40x + 390x^2 - 1080x^3 + 729x^4.$$
Since the numerator $1 - 37x + 288x^2 - 405x^3 - 81x^4$ has degree $4$, multiplying $G(x)$ by $1 - 40x + 390x^2 - 1080x^3 + 729x^4$ leaves a polynomial of degree $4$, so the coefficient of $x^n$ vanishes for every $n > 4$:
$$a(n) - 40a(n-1) + 390a(n-2) - 1080a(n-3) + 729a(n-4) = 0 \quad (n > 4),$$
proving the second conjecture. $\blacksquare$

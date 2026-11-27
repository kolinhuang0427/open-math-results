# Proof of OEIS A024199 Conjecture

We prove Peter Bala's Nov 15, 2016 conjecture on [OEIS A024199](https://oeis.org/A024199) (rev. 80), together with the accompanying exponential generating function formula.

## 1. Definitions and Odd Double Factorial Convention

From the OEIS NAME field, the sequence $(a(n))_{n \ge 0}$ is defined for $n \ge 0$ by $a(0) = 0$ (empty sum) and
$$a(n) = (2n-1)!! \sum_{j=0}^{n-1} \frac{(-1)^j}{2j+1} \qquad (n \ge 1).$$

For every integer $m \in \mathbb{Z}$, the odd double factorial $(2m-1)!!$ is given by the standard Gamma continuation of $M!! = 2^{(M+1)/2}\Gamma(M/2+1)/\sqrt{\pi}$ at $M = 2m-1$:
$$(2m-1)!! := \frac{2^m \Gamma(m + 1/2)}{\sqrt{\pi}} = \begin{cases} \prod_{j=1}^m (2j-1), & m \ge 1, \\ 1, & m = 0, \\ \dfrac{(-1)^{-m}}{(1 - 2m - 2)!!} = \dfrac{(-1)^r}{(2r-1)!!}, & m = -r \le -1 \ (r \ge 1), \end{cases}$$
where we interpret $(-1)!! = 1$ in the denominator for $r = 1$ (so $(-3)!! = -1$, $(-5)!! = 1/3$, etc.). Equivalently, using $\Gamma(1/2) = \sqrt{\pi}$ and $\Gamma(z+1) = z\Gamma(z)$, the defining functional relation holds everywhere on $\mathbb{Z}$.

**Lemma 1 (Step Identity).** *For every integer $m \in \mathbb{Z}$,*
$$(2m-1) \cdot (2m-3)!! = (2m-1)!!$$

*Proof.* Using the Gamma definition directly, $\Gamma(m + 1/2) = (m - 1/2)\Gamma(m - 1/2)$ gives
$$(2m-1)!! = \frac{2^m (m - 1/2) \Gamma(m - 1/2)}{\sqrt{\pi}} = (2m-1) \frac{2^{m-1} \Gamma((m-1) + 1/2)}{\sqrt{\pi}} = (2m-1) \cdot (2m-3)!!$$
One can equally verify all three piecewise cases directly: for $m \ge 2$ it appends the factor $(2m-1)$; for $m=1$ we have $1 \cdot (-1)!! = 1 = 1!!$; for $m=0$ we have $(-1)\cdot (-3)!! = (-1)(-1) = 1 = (-1)!!$; and for $m = -r \le -1$ we have $2m-3 = -(2(r+1)+1)$, so
$$(2m-1) \cdot (2m-3)!! = -(2r+1) \cdot \frac{(-1)^{r+1}}{(2r+1)!!} = \frac{(-1)^r}{(2r-1)!!} = (2m-1)!! \qquad \square$$

## 2. First-Order Recurrence for $a(n)$

**Lemma 2 (Recurrence).** *With $a(0) = 0$, the sequence $(a(n))_{n \ge 0}$ satisfies*
$$a(n) - (2n-1)\,a(n-1) = (-1)^{n-1} (2n-3)!! \qquad \forall\, n \ge 1.$$

*Proof.* For $n = 1$, $a(1) - 1\cdot a(0) = 1!!\cdot 1 - 0 = 1 = (-1)^0(-1)!!$. For $n \ge 2$, using $(2n-1)!! = (2n-1)(2n-3)!!$,
$$a(n) = (2n-1)(2n-3)!! \left(\sum_{j=0}^{n-2}\frac{(-1)^j}{2j+1} + \frac{(-1)^{n-1}}{2n-1}\right) = (2n-1)\,a(n-1) + (-1)^{n-1}(2n-3)!!. \qquad \square$$

## 3. Proof of Peter Bala's Sum Conjecture

**Theorem 1.** *For every integer $n \ge 1$,*
$$a(n) = \frac{1}{2} \sum_{k=0}^{2n-1} (-1)^{n-k+1} k!\, (2n - 2k - 3)!!$$

*Proof.* Define for $n \ge 1$ and $0 \le k \le 2n-1$:
$$T(n, k) := (-1)^{n-k+1} k!\, (2n - 2k - 3)!!, \qquad b(n) := \frac{1}{2}\sum_{k=0}^{2n-1} T(n, k),$$
and set $b(0) := 0$.

*Base case ($n = 1$):*
$$T(1,0) = (-1)^2 \cdot 0!\, (-1)!! = 1, \qquad T(1,1) = (-1)^1 \cdot 1!\, (-3)!! = (-1)(-1) = 1,$$
so $b(1) = \frac{1}{2}(1 + 1) = 1 = a(1)$.

*Inductive step ($n \ge 2$):* Consider any $k \in \{0, 1, \dots, 2n-3\}$.
1. Applying Lemma 1 with $m = n - k - 1$ (so $2m - 1 = 2n - 2k - 3$ and $2m - 3 = 2n - 2k - 5$) yields
   $$T(n, k) = (-1)^{n-k+1} k!\, (2n - 2k - 3)\,(2n - 2k - 5)!! = -(2n - 2k - 3)\, T(n-1, k).$$
2. Shifting $k \mapsto k+1$ at row $n$ (noting $2n - 2(k+1) - 3 = 2n - 2k - 5$ and $(-1)^{n-(k+1)+1} = (-1)^{(n-1)-k+1}$) yields
   $$T(n, k+1) = (-1)^{n-k} (k+1)!\, (2n - 2k - 5)!! = (k+1)\, T(n-1, k).$$

Combining the algebraic identity $2n - 1 = (2n - 2k - 3) + 2(k + 1)$ with (1) and (2) gives
$$(2n - 1)\, T(n-1, k) = -T(n, k) + 2\, T(n, k+1),$$
and subtracting from $T(n, k)$ produces the telescoping relation
$$T(n, k) - (2n - 1)\, T(n-1, k) = 2\bigl(T(n, k) - T(n, k+1)\bigr) \qquad (0 \le k \le 2n-3).$$

Summing this identity over $k = 0, 1, \dots, 2n-3$ and adding the two top terms $T(n, 2n-2) + T(n, 2n-1)$ of row $n$ gives
$$\begin{aligned}
\sum_{k=0}^{2n-1} T(n, k) - (2n - 1)\sum_{k=0}^{2n-3} T(n-1, k)
&= 2\sum_{k=0}^{2n-3} \bigl(T(n, k) - T(n, k+1)\bigr) + T(n, 2n-2) + T(n, 2n-1) \\
&= 2\,T(n, 0) - 2\,T(n, 2n-2) + T(n, 2n-2) + T(n, 2n-1) \\
&= 2\,T(n, 0) - T(n, 2n-2) + T(n, 2n-1).
\end{aligned}$$

We evaluate the three boundary terms:
- At $k = 0$: $T(n, 0) = (-1)^{n+1} \cdot 0!\, (2n-3)!! = (-1)^{n-1}(2n-3)!!$.
- At $k = 2n-2$: we have $2n - 2k - 3 = -(2n-1)$ (corresponding to $m = -(n-1)$ with $r = n-1 \ge 1$), so $(-(2n-1))!! = \frac{(-1)^{n-1}}{(2n-3)!!}$. Since $(-1)^{n-(2n-2)+1} = (-1)^{-n+3} = (-1)^{n-1}$,
  $$T(n, 2n-2) = (-1)^{n-1} (2n-2)!\, \frac{(-1)^{n-1}}{(2n-3)!!} = \frac{(2n-2)!}{(2n-3)!!} = 2^{n-1}(n-1)!.$$
- At $k = 2n-1$: we have $2n - 2k - 3 = -(2n+1)$ (corresponding to $m = -n$ with $r = n \ge 2$), so $(-(2n+1))!! = \frac{(-1)^n}{(2n-1)!!}$. Since $(-1)^{n-(2n-1)+1} = (-1)^{-n+2} = (-1)^n$,
  $$T(n, 2n-1) = (-1)^n (2n-1)!\, \frac{(-1)^n}{(2n-1)!!} = \frac{(2n-1)!}{(2n-1)!!} = \frac{(2n-2)!}{(2n-3)!!} = 2^{n-1}(n-1)! = T(n, 2n-2).$$

Hence $-T(n, 2n-2) + T(n, 2n-1) = 0$. Dividing by $2$ yields
$$b(n) - (2n-1)\,b(n-1) = T(n, 0) = (-1)^{n-1}(2n-3)!! \qquad \forall\, n \ge 2.$$
Because $b(1) = a(1) = 1$ and $(b(n))_{n \ge 1}$ satisfies the exact same first-order recurrence as $(a(n))_{n \ge 1}$ (Lemma 2), induction on $n$ gives $b(n) = a(n)$ for all $n \ge 1$. $\square$

## 4. Exponential Generating Function

**Theorem 2.** *In the formal power series ring $\mathbb{Q}[[x]]$,*
$$Y(x) := \sum_{n=0}^{\infty} a(n)\frac{x^n}{n!} = \frac{1}{2}\frac{\arcsin(2x)}{\sqrt{1-2x}}.$$

*Proof.* Multiply Lemma 2 by $\frac{x^{n-1}}{(n-1)!}$ and sum over $n \ge 1$. Using $a(0) = 0$:
$$\sum_{n=1}^{\infty} a(n)\frac{x^{n-1}}{(n-1)!} = Y'(x),$$
$$\sum_{n=1}^{\infty} (2n-1)\,a(n-1)\frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^{\infty} (2m+1)\,a(m)\frac{x^m}{m!} = 2x\,Y'(x) + Y(x),$$
$$\sum_{n=1}^{\infty} (-1)^{n-1}(2n-3)!!\frac{x^{n-1}}{(n-1)!} = \sum_{m=0}^{\infty} (-1)^m \frac{(2m-1)!!}{m!} x^m = \sum_{m=0}^{\infty} \binom{-1/2}{m} (2x)^m = (1+2x)^{-1/2}.$$
Hence $(1-2x)Y'(x) - Y(x) = (1+2x)^{-1/2}$ in $\mathbb{Q}[[x]]$, with $Y(0) = 0$. Multiplying both sides by the unit $(1-2x)^{-1/2} \in \mathbb{Q}[[x]]$ gives
$$\frac{d}{dx}\Bigl((1-2x)^{1/2} Y(x)\Bigr) = (1-2x)^{-1/2}(1+2x)^{-1/2} = (1-4x^2)^{-1/2} = \frac{d}{dx}\left(\frac{1}{2}\arcsin(2x)\right).$$
Comparing constant terms at $x = 0$ shows $(1-2x)^{1/2} Y(x) = \frac{1}{2}\arcsin(2x)$, so $Y(x) = \frac{\arcsin(2x)}{2\sqrt{1-2x}}$ in $\mathbb{Q}[[x]]$. $\square$

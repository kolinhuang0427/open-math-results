# Proof of OEIS A176126 Generating Function and Linear Recurrence

## Theorem

Let $a(n) = A176126(n)$ ($n \ge 0$) be the numerator of the reduced fraction $-A127276(n)/A001788(n)$ (with $a(0) = -1$ from $-1/0$, and for $n \ge 1$ the reduced numerator in $\mathbb{Q}$ since $A001788(n) = n(n+1)2^{n-2} > 0$). Then:
1. For all integers $n \ge 0$,
   $$a(n) = \begin{cases} \dfrac{n(n+1) - 4}{4} & \text{if } n \equiv 0 \text{ or } 3 \pmod 4, \\[6pt] \dfrac{n(n+1) - 4}{2} & \text{if } n \equiv 1 \text{ or } 2 \pmod 4. \end{cases}$$
2. The ordinary generating function is
   $$\sum_{n=0}^{\infty} a(n) x^n = \frac{(x^4 - x^3 + 3x^2 - x + 1)(x^4 - x^3 - 2x^2 - x + 1)}{(x - 1)^3 (x^2 + 1)^3}.$$
3. For all integers $n \ge 9$,
   $$a(n) = 3a(n-1) - 6a(n-2) + 10a(n-3) - 12a(n-4) + 12a(n-5) - 10a(n-6) + 6a(n-7) - 3a(n-8) + a(n-9).$$

---

## Proof

### 1. Closed form for $A127276(n)$ (self-contained lemma)

**Lemma 1.** *For all $n \ge 0$, $A127276(n) = 2^n - n(n+1)2^{n-2}$ (interpreting $0\cdot 1\cdot 2^{-2} = 0$ at $n = 0$).*

*Proof.* By definition of $A127275$, its sequence $(b_m)_{m \ge 0}$ has generating function
$$\sum_{m=0}^{\infty} b_m x^m = \frac{\sqrt{1 - 4x} - x}{1 - 4x} = \frac{1}{\sqrt{1 - 4x}} - \frac{x}{1 - 4x} = \sum_{m=0}^{\infty} \binom{2m}{m} x^m - \sum_{m=1}^{\infty} 4^{m-1} x^m,$$
so $b_0 = 1$ and $b_m = \binom{2m}{m} - 4^{m-1}$ for $m \ge 1$. For any $n \ge 0$, the Hankel matrix $M_n := (b_{i+j})_{0 \le i,j \le n}$ decomposes as
$$M_n = C_n - \frac{1}{4} v v^T + \frac{1}{4} e_0 e_0^T = C_n + U V^T,$$
where $C_n := \bigl(\binom{2(i+j)}{i+j}\bigr)_{0 \le i,j \le n}$, $v := (1, 4, \dots, 4^n)^T$, $e_0 := (1, 0, \dots, 0)^T$, $U := [-\frac{1}{4}v,\ \frac{1}{4}e_0]$, and $V := [v,\ e_0]$.

Define monic polynomials $P_k(t) = \sum_{i=0}^{k} p_{k,i} t^i \in \mathbb{Z}[t]$ by $P_0(t) = 1$, $P_1(t) = t - 2$, $P_2(t) = t^2 - 4t + 2$, and $P_k(t) = (t-2)P_{k-1}(t) - P_{k-2}(t)$ for $k \ge 3$. In $\mathbb{Z}[z, z^{-1}]$, writing $t(z) := z + 2 + z^{-1} = \frac{(1+z)^2}{z}$ gives $[z^0](t(z)^m) = \binom{2m}{m}$ and, by induction on $k \ge 1$, $P_k(t(z)) = z^k + z^{-k}$. Letting $P = (p_{k,i})_{0 \le k,i \le n}$ (unit lower-triangular, $\det P = 1$), we obtain
$$(P C_n P^T)_{k,\ell} = [z^0]\bigl(P_k(t(z)) P_\ell(t(z))\bigr) = d_k \delta_{k,\ell}, \qquad d_0 = 1,\quad d_k = 2\ (k \ge 1).$$
Hence $\det(C_n) = 2^n$ and $C_n^{-1} = P^T \mathrm{diag}(d_0^{-1}, \dots, d_n^{-1}) P$. Evaluating $t(1) = 4$ and $t(-1) = 0$ gives $(Pv)_k = P_k(4)$ ($1$ at $k=0$, $2$ for $k \ge 1$) and $(Pe_0)_k = P_k(0)$ ($1$ at $k=0$, $2(-1)^k$ for $k \ge 1$), whence
$$v^T C_n^{-1} v = 2n + 1, \qquad e_0^T C_n^{-1} e_0 = 2n + 1, \qquad v^T C_n^{-1} e_0 = (-1)^n.$$
By the Weinstein–Aronszajn identity $\det(M_n) = \det(C_n)\,\det(I_2 + V^T C_n^{-1} U)$:
$$A127276(n) = \det(M_n) = 2^n \det\begin{pmatrix} 1 - \frac{2n+1}{4} & \frac{(-1)^n}{4} \\ -\frac{(-1)^n}{4} & 1 + \frac{2n+1}{4} \end{pmatrix} = 2^n\left(1 - \frac{n(n+1)}{4}\right) = 2^n - n(n+1)2^{n-2}. \quad \square$$

---

### 2. Reduced numerator of $-A127276(n)/A001788(n)$

At $n = 0$, $-A127276(0)/A001788(0) = -1/0$ gives $a(0) = -1 = \frac{0\cdot 1 - 4}{4}$, matching the $n \equiv 0 \pmod 4$ case.

For every integer $n \ge 1$, $A001788(n) = n(n+1)2^{n-2} > 0$, and Lemma 1 gives
$$-\frac{A127276(n)}{A001788(n)} = \frac{n(n+1)2^{n-2} - 2^n}{n(n+1)2^{n-2}} = \frac{n(n+1) - 4}{n(n+1)}.$$
Here $n(n+1)$ is always even, and $\gcd\bigl(n(n+1) - 4,\, n(n+1)\bigr) = \gcd\bigl(n(n+1),\, 4\bigr)$:
- **If $n \equiv 0$ or $3 \pmod 4$:** $4 \mid n(n+1)$, so $\gcd(n(n+1), 4) = 4$. Thus the fraction reduces to $\frac{(n(n+1)-4)/4}{n(n+1)/4}$ in lowest terms, with numerator $a(n) = \frac{n(n+1)-4}{4}$. (For $n \ge 3$, $a(n) > 0$; for $n=1,2$ below, it gives $-1, 1$.)
- **If $n \equiv 1$ or $2 \pmod 4$:** $n(n+1) \equiv 2 \pmod 4$, so $\gcd(n(n+1), 4) = 2$. Thus the fraction reduces to $\frac{(n(n+1)-4)/2}{n(n+1)/2}$ in lowest terms, with numerator $a(n) = \frac{n(n+1)-4}{2}$.

(Notice that at $n = 1$, $a(1) = \frac{2-4}{2} = -1$ preserves the sign of $-1/1$, matching OEIS `A176126` `DATA[1] = -1` and `COMMENT: -1/0, -1/1, 1/3, ...`; for $n \ge 2$, $n(n+1) - 4 \ge 2 > 0$.)

---

### 3. Generating function and 9-term linear recurrence

For each fixed residue class $r \in \{0, 1, 2, 3\}$, write $n = 4m + r$ ($m \ge 0$). By Section 2, $a(4m+r)$ is a quadratic polynomial in $m$ for all $m \ge 0$ (including $n=0$ at $r=0, m=0$). Since the third finite difference of any quadratic polynomial vanishes identically,
$$a(n) - 3a(n-4) + 3a(n-8) - a(n-12) = 0 \qquad \forall n \ge 12.$$
Consequently, in $\mathbb{Z}[[x]]$, the product
$$P(x) := (1 - x^4)^3 A(x)$$
is a polynomial of degree at most $11$, whose coefficients are $p_n = a(n) - 3a(n-4) + 3a(n-8)$ (with $a(k) = 0$ for $k < 0$). Using Section 2 to evaluate $a(0..11) = (-1, -1, 1, 2, 4, 13, 19, 13, 17, 43, 53, 32)$, direct computation gives:
$$P(x) = -1 - x + x^2 + 2x^3 + 7x^4 + 16x^5 + 16x^6 + 7x^7 + 2x^8 + x^9 - x^{10} - x^{11}.$$
Expanding $(x^4 - x^3 + 3x^2 - x + 1)(x^4 - x^3 - 2x^2 - x + 1)$ yields
$$N(x) := 1 - 2x + 2x^2 - 3x^3 - 2x^4 - 3x^5 + 2x^6 - 2x^7 + x^8,$$
and multiplying by $-(1 + x)^3 = -1 - 3x - 3x^2 - x^3$ verifies identically in $\mathbb{Z}[x]$:
$$-(1+x)^3 N(x) = -1 - x + x^2 + 2x^3 + 7x^4 + 16x^5 + 16x^6 + 7x^7 + 2x^8 + x^9 - x^{10} - x^{11} = P(x).$$
Since $(1 - x^4)^3 = -(x^4 - 1)^3 = -(x-1)^3(x+1)^3(x^2+1)^3$, cancelling $-(1+x)^3$ in $\mathbb{Z}[[x]]$ proves
$$A(x) = \frac{N(x)}{(x - 1)^3 (x^2 + 1)^3} = \frac{(x^4 - x^3 + 3x^2 - x + 1)(x^4 - x^3 - 2x^2 - x + 1)}{(x - 1)^3 (x^2 + 1)^3}.$$

Finally, expanding the denominator gives
$$D(x) := (x-1)^3(x^2+1)^3 = -1 + 3x - 6x^2 + 10x^3 - 12x^4 + 12x^5 - 10x^6 + 6x^7 - 3x^8 + x^9.$$
In $D(x) A(x) = N(x)$, since $\deg N = 8$, extracting $[x^n]$ for every $n \ge 9$ gives
$$-a(n) + 3a(n-1) - 6a(n-2) + 10a(n-3) - 12a(n-4) + 12a(n-5) - 10a(n-6) + 6a(n-7) - 3a(n-8) + a(n-9) = 0,$$
i.e., Mathar's 9-term recurrence holds for all $n \ge 9$. $\blacksquare$

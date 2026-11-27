# Proof of OEIS A165204 Generating Function and Linear Recurrence

## Theorem

Let $F_0(x) = \sum_{m=0}^{\infty} b_m x^m \in \mathbb{Z}[[x]]$ be OEIS [A165203](https://oeis.org/A165203), defined by
$$F_0(x) = \frac{(1+x)\, c(x)^3}{1 - x\, c(x)^3}, \qquad c(x) = \frac{1 - \sqrt{1-4x}}{2x},$$
and let $a(n) = A165204(n)$ ($n \ge 0$) be its Hankel transform:
$$a(n) := \det\bigl(b_{i+j}\bigr)_{0 \le i,j \le n}.$$
Let $(F_m)_{m \ge 0}$ denote the Fibonacci numbers ($F_0 = 0, F_1 = 1, F_{m+1} = F_m + F_{m-1}$). Then:
1. For all integers $k \ge 0$,
   $$a(3k) = (-1)^k F_{6k+2}, \qquad a(3k+1) = (-1)^{k+1} F_{6k+5}, \qquad a(3k+2) = (-1)^{k+1} F_{6k+8}.$$
2. The ordinary generating function is
   $$\sum_{n=0}^{\infty} a(n) x^n = \frac{1 - 8x + 2x^2 - x^3}{1 - 3x + 8x^2 - 3x^3 + x^4}.$$
3. For all integers $n > 3$ ($n \ge 4$),
   $$a(n) = 3a(n-1) - 8a(n-2) + 3a(n-3) - a(n-4).$$

---

## Proof

### 1. Radical expression for $F_0(x)$

Let $s := \sqrt{1 - 4x} = 1 - 2x - 2x^2 - 4x^3 - \cdots \in \mathbb{Z}[[x]]$, so $s^2 = 1 - 4x$ and $c(x) = \frac{1-s}{2x}$ satisfies $x c(x)^2 = c(x) - 1$. Multiplying by $c(x)$ twice gives
$$x c(x)^3 = c(x)^2 - c(x) = \frac{c(x) - 1}{x} - c(x) = \frac{(1-x)c(x) - 1}{x} = \frac{(1-x)(1-s) - 2x}{2x^2},$$
hence $1 - x c(x)^3 = \frac{2x^2 + 2x - (1-x)(1-s)}{2x^2}$. Multiplying numerator and denominator by $(1-x)(1+s)$ and simplifying using $(1-x)^2(1-s^2) = 4x(1-x)^2$ (or directly verifying $(5x - 1 + (1-x)s) \cdot x c(x)^3$: indeed, $c(x)^3 = \frac{(1-s)^3}{8x^3} = \frac{1 - 3s + 3(1-4x) - (1-4x)s}{8x^3} = \frac{(2 - 6x) - (2 - 2x)s}{4x^3}$):
$$1 - x c(x)^3 = \frac{2x^2 - 1 + 3x + (1-x)s}{2x^2}, \qquad c(x)^3 = \frac{(1 - 3x) - (1-x)s}{2x^3}.$$
Checking the conjugate product
$$\bigl(2x^2 - 1 + 3x + (1-x)s\bigr)\bigl(2x^2 - 1 + 3x - (1-x)s\bigr) = (2x^2 + 3x - 1)^2 - (1-x)^2(1-4x) = -4x^2(1 - 4x - x^2),$$
and simplifying $\bigl((1-3x)-(1-x)s\bigr)\bigl(2x^2 + 3x - 1 - (1-x)s\bigr) = -2x^2\bigl(5x - 1 + (1-x)s\bigr)$ using $s^2 = 1 - 4x$ (the two minus signs cancel) gives
$$F_0(x) = \frac{(1+x)\bigl(5x - 1 + (1-x)s\bigr)}{2x(1 - 4x - x^2)}.$$
In particular, $b_0 = F_0(0) = 1$, and its reciprocal in $\mathbb{Q}[[x]]$ (since $(5x - 1 + (1-x)s)(5x - 1 - (1-x)s) = -4x(1 - 4x - x^2)$) is
$$\frac{1}{F_0(x)} = \frac{1 - 5x + (1-x)s}{2(1+x)} = 1 - 5x + 5x^2 G_{1/10}(x),$$
where for any scalar parameter $u \in \mathbb{Q} \setminus \{-2, -\tfrac{17}{8}\}$ we define the formal power series
$$G_u(x) := \frac{x^2 - u(1 - 3x) + u(1 - x)s}{x^2(1 + x)} \in \mathbb{Q}[[x]].$$
Note that $x^2 G_u(x)$ is well-defined at $x = 0$: since $s = 1 - 2x - 2x^2 - 4x^3 - 10x^4 - \cdots$, we have
$$(1-x)s - (1-3x) = (1 - 3x - 2x^3 - 6x^4 - \cdots) - (1 - 3x) = -2x^3 - 6x^4 - \cdots,$$
so $G_u(x) = \frac{1}{1+x} + u\frac{(1-x)s - (1-3x)}{x^2(1+x)} = 1 - (1 + 2u)x + O(x^2) \in \mathbb{Q}[[x]]$.

---

### 2. Self-contained J-fraction Hankel determinant theorem

**Lemma 1 (J-fraction orthogonalization).** *Let $F_0(x) = \sum_{m \ge 0} b_m x^m \in \mathbb{Q}[[x]]$ with $b_0 = 1$, and suppose for $0 \le k < N$ there exist scalars $\alpha_k \in \mathbb{Q}$, $\beta_{k+1} \in \mathbb{Q}^\times$, and series $F_{k+1}(x) = 1 + O(x) \in \mathbb{Q}[[x]]$ such that*
$$\frac{1}{F_k(x)} = 1 - \alpha_k x - \beta_{k+1} x^2 F_{k+1}(x) \qquad (0 \le k < N).$$
*Then for every $0 \le n \le N$, $a(n) := \det(b_{i+j})_{0 \le i,j \le n}$ satisfies*
$$a(0) = 1, \qquad \frac{a(n)}{a(n-1)} = \beta_1 \beta_2 \cdots \beta_n \quad (1 \le n \le N).$$

*Proof.* Define monic polynomials $p_k(t) = \sum_{i=0}^{k} u_{k,i} t^i \in \mathbb{Q}[t]$ ($0 \le k \le N$) by $p_0(t) = 1$, $p_1(t) = t - \alpha_0$, and $p_{k+1}(t) = (t - \alpha_k)p_k(t) - \beta_k p_{k-1}(t)$ for $1 \le k < N$, and set $\tilde{p}_k(x) := x^k p_k(1/x) = \sum_{i=0}^{k} u_{k,i} x^{k-i}$, so $\tilde{p}_0 = 1$, $\tilde{p}_1 = 1 - \alpha_0 x$, and $\tilde{p}_{k+1}(x) = (1 - \alpha_k x)\tilde{p}_k(x) - \beta_k x^2 \tilde{p}_{k-1}(x)$.

By induction on $k \in \{0, \dots, N\}$, there exists a polynomial $q_k(x) \in \mathbb{Q}[x]$ with $\deg q_k < k$ ($q_0 = 0$) such that
$$\tilde{p}_k(x) F_0(x) - q_k(x) = (\beta_1 \cdots \beta_k)\, x^{2k}\, F_0(x) F_1(x) \cdots F_k(x),$$
where the empty product at $k = 0$ is $1$. Indeed, $k = 0$ is trivial ($\tilde{p}_0 F_0 - 0 = F_0$), and at $k = 1$, $(1 - \alpha_0 x) F_0(x) = \bigl(\tfrac{1}{F_0(x)} + \beta_1 x^2 F_1(x)\bigr) F_0(x) = 1 + \beta_1 x^2 F_0(x) F_1(x)$ ($q_1 = 1$). For $1 \le k < N$, substituting the inductive hypothesis for $k$ and $k - 1$ into $\tilde{p}_{k+1} = (1 - \alpha_k x)\tilde{p}_k - \beta_k x^2 \tilde{p}_{k-1}$ gives
$$\tilde{p}_{k+1}(x) F_0(x) - q_{k+1}(x) = (\beta_1 \cdots \beta_k)\, x^{2k}\, F_0 \cdots F_{k-1}\bigl((1 - \alpha_k x) F_k(x) - 1\bigr),$$
with $q_{k+1}(x) := (1 - \alpha_k x) q_k(x) - \beta_k x^2 q_{k-1}(x)$ of degree $\le \max(1+(k-1), 2+(k-2)) = k < k + 1$. Since $(1 - \alpha_k x) F_k(x) - 1 = \beta_{k+1} x^2 F_k(x) F_{k+1}(x)$, the induction closes.

Now fix $n \le N$ and let $U_n := (u_{k,i})_{0 \le k,i \le n}$ (unit lower-triangular, $\det U_n = 1$) and $H_n := (b_{i+j})_{0 \le i,j \le n}$. For $0 \le m \le k \le n$, $(U_n H_n)_{k,m} = \sum_{i=0}^{k} u_{k,i} b_{m+i} = [x^{m+k}]\bigl(\tilde{p}_k(x) F_0(x)\bigr)$. Since $\deg q_k < k \le m + k$ and $F_0(0)\cdots F_k(0) = 1$, the identity above yields $(U_n H_n)_{k,m} = 0$ for $0 \le m < k$ and $(U_n H_n)_{k,k} = \beta_1 \cdots \beta_k$. Because $U_n H_n U_n^T$ differs from $U_n H_n$ only by right-multiplication by a unit upper-triangular matrix, $U_n H_n U_n^T = \mathrm{diag}(1, \beta_1, \beta_1\beta_2, \dots, \beta_1\cdots\beta_n)$, whence $a(n) = \det H_n = \prod_{k=1}^{n} (\beta_1 \cdots \beta_k)$ and $a(n)/a(n-1) = \beta_1 \cdots \beta_n$. $\blacksquare$

---

### 3. Exact 3-periodic J-fraction of $F_0(x)$

From Section 1, $\frac{1}{F_0(x)} = 1 - 5x - (-5) x^2 G_{1/10}(x)$, so $\alpha_0 = 5$, $\beta_1 = -5$, and $F_1(x) = G_{u_0}(x)$ with $u_0 = \frac{1}{10} = \frac{F_2}{2 F_5}$.

**Lemma 2 (Three-step J-fraction transition).** *For any parameter $u \in \mathbb{Q} \setminus \{0, -2, -\tfrac{17}{8}\}$, three J-fraction steps starting from $G_u(x)$ produce*
$$\begin{aligned}
\alpha^{(1)} &= -2u - 1, & \beta^{(1)} &= -4u(u + 2), \\
\alpha^{(2)} &= 2u + 3,  & \beta^{(2)} &= \frac{1}{2(u + 2)}, \\
\alpha^{(3)} &= 4,       & \beta^{(3)} &= -\frac{8u + 17}{2(u + 2)},
\end{aligned}$$
*and return $G_{u'}(x)$ where $u' = \frac{u + 2}{8u + 17}$.*

*Proof.* Write $s^2 = 1 - 4x$. All three steps are direct polynomial identities in $\mathbb{Q}(u)[x, s]/(s^2 - 1 + 4x)$:
1. Rationalizing $G_u(x) = \frac{x^2 - u(1-3x) + u(1-x)s}{x^2(1+x)}$ via $\bigl(x^2 - u(1-3x)\bigr)^2 - u^2(1-x)^2(1-4x) = x^2\bigl(4u^2 x + 6u x - 2u + x^2\bigr)$ gives
   $$\frac{1}{G_u(x)} = \frac{(1+x)\bigl(x^2 - u(1-3x) - u(1-x)s\bigr)}{4u^2 x + 6u x - 2u + x^2}.$$
   Subtracting from $1 - (-2u - 1)x$ and dividing by $-4u(u+2)x^2$ (i.e., $H_1(x) = \frac{1/G_u(x) - (1 + (2u+1)x)}{4u(u+2)x^2}$) leaves
   $$H_1(x) := \frac{(1 - s) - (2x + 3x^2 + 2x^3 + 8u^2 x^2 + 16u x^2) + x^2 s}{4x^2(u + 2)(4u^2 x + 6u x - 2u + x^2)} = 1 + O(x).$$
2. Rationalizing $H_1(x)$ via $(1-s)(1+s) = 4x$ yields
   $$\frac{1}{H_1(x)} = -\frac{(u+2)\bigl(8u^2 x^2 + 16ux^2 + 2x^3 + 3x^2 + 2x - 1 - (1-x^2)s\bigr)}{4u^2 x + 10u x + 2u + x^2 + 4x + 4}.$$
   Subtracting from $1 - (2u + 3)x$ and dividing by $\frac{1}{2(u+2)} x^2$ leaves
   $$H_2(x) := \frac{2(u+2)(1+x)\bigl(u(1-3x - (1-x)s) + 2 - 6x + x^2 - 2(1-x)s\bigr)}{x^2(4u^2 x + 10u x + 2u + x^2 + 4x + 4)} = 1 + O(x).$$
3. Finally, rationalizing $H_2(x)$ cancels the quadratic denominator $(4u^2 x + 10u x + 2u + x^2 + 4x + 4)$ identically, yielding
   $$\frac{1}{H_2(x)} = \frac{(u+2) - (3u + 6)x + x^2 + (u+2)(1-x)s}{2(u+2)(1+x)}.$$
   Evaluating $\frac{1 - 4x - 1/H_2(x)}{-\frac{8u+17}{2(u+2)} x^2}$ gives
   $$\frac{x^2(8u+17) - (u+2)(1-3x) + (u+2)(1-x)s}{x^2(8u+17)(1+x)} = G_{u'}(x), \qquad u' = \frac{u+2}{8u+17}. \quad \blacksquare$$

Recall the Fibonacci identity $F_{m+6} = 4 F_{m+3} + F_m$ (verified directly via $F_{m+6} - 4F_{m+3} = (2F_{m+4} + F_{m+3}) - 4F_{m+3} = 2(F_{m+3} + F_{m+2}) - 3F_{m+3} = 2F_{m+2} - F_{m+3} = F_{m+2} - F_{m+1} = F_m$). Applying this twice at $u_k := \frac{F_{6k+2}}{2 F_{6k+5}}$ gives
$$u_k + 2 = \frac{F_{6k+2} + 4F_{6k+5}}{2F_{6k+5}} = \frac{F_{6k+8}}{2F_{6k+5}}, \qquad 8u_k + 17 = \frac{4F_{6k+2} + 17 F_{6k+5}}{F_{6k+5}},$$
where $8 F_{6k+2} + 34 F_{6k+5} = 2\bigl(4(4 F_{6k+5} + F_{6k+2}) + F_{6k+5}\bigr) = 2(4 F_{6k+8} + F_{6k+5}) = 2 F_{6k+11}$, so
$$8u_k + 17 = \frac{F_{6k+11}}{F_{6k+5}}, \qquad u_k' = \frac{u_k + 2}{8u_k + 17} = \frac{F_{6k+8}}{2 F_{6k+11}} = u_{k+1}.$$

Therefore, by induction on $k \ge 0$, $F_{3k+1}(x) = G_{u_k}(x)$ for all $k \ge 0$, and the J-fraction coefficients satisfy for all $k \ge 0$:
$$\beta_{3k+1} = -\frac{F_{6k+5}}{F_{6k+2}}, \qquad \beta_{3k+2} = -4 u_k(u_k+2) = -\frac{F_{6k+2} F_{6k+8}}{F_{6k+5}^2}, \qquad \beta_{3k+3} = \frac{1}{2(u_k+2)} = \frac{F_{6k+5}}{F_{6k+8}}.$$
(Note that at $k = 0$, $\beta_1 = -5 = -F_5/F_2$, and for $k \ge 1$, Lemma 2 gives $\beta_{3k+1} = -\frac{8u_{k-1}+17}{2(u_{k-1}+2)} = -\frac{F_{6k+5}}{F_{6k+2}}$.)

Notice that for every $k \ge 0$,
$$\beta_{3k+1}\, \beta_{3k+2}\, \beta_{3k+3} = \left(-\frac{F_{6k+5}}{F_{6k+2}}\right)\left(-\frac{F_{6k+2} F_{6k+8}}{F_{6k+5}^2}\right)\left(\frac{F_{6k+5}}{F_{6k+8}}\right) = 1.$$
Define $R_n := \beta_1 \cdots \beta_n$ ($R_0 := 1$). Induction on $k \ge 0$ gives $R_{3k} = 1$, $R_{3k+1} = R_{3k}\beta_{3k+1} = -\frac{F_{6k+5}}{F_{6k+2}}$, and $R_{3k+2} = R_{3k+1}\beta_{3k+2} = \frac{F_{6k+8}}{F_{6k+5}}$. Applying Lemma 1 ($a(n) = a(n-1) R_n$, $a(0) = 1 = F_2$) by induction on $k \ge 0$:
- $a(3k) = (-1)^k F_{6k+2}$ (for the inductive step $k \mapsto k+1$, $R_{3k+3} = 1$ gives $a(3k+3) = a(3k+2) = (-1)^{k+1} F_{6k+8} = (-1)^{k+1} F_{6(k+1)+2}$),
- $a(3k+1) = a(3k) R_{3k+1} = (-1)^k F_{6k+2} \cdot \bigl(-\frac{F_{6k+5}}{F_{6k+2}}\bigr) = (-1)^{k+1} F_{6k+5}$,
- $a(3k+2) = a(3k+1) R_{3k+2} = (-1)^{k+1} F_{6k+5} \cdot \frac{F_{6k+8}}{F_{6k+5}} = (-1)^{k+1} F_{6k+8}$.

---

### 4. Generating function and 4-term recurrence

By $F_{m+6} = 4 F_{m+3} + F_m$, applying it twice gives
$$F_{m+12} = 4(4F_{m+6} + F_{m+3}) + F_{m+6} = 17 F_{m+6} + 4 F_{m+3} = 17 F_{m+6} + (F_{m+6} - F_m) = 18 F_{m+6} - F_m.$$
For each residue $r \in \{0, 1, 2\}$, $a(3(k+2)+r) = -18\, a(3(k+1)+r) - a(3k+r)$ for all $k \ge 0$ (because the sign toggles by $(-1)^1 = -1$ at $k \mapsto k+1$ and $(-1)^2 = +1$ at $k \mapsto k+2$). Therefore, for all $n \ge 6$:
$$a(n) + 18\, a(n-3) + a(n-6) = 0.$$
Consequently, $(1 + 18x^3 + x^6) \sum_{n=0}^{\infty} a(n) x^n$ is a polynomial of degree $\le 5$, computed directly from $a(0..5) = (1, -5, -21, -21, 89, 377)$ as
$$1 - 5x - 21x^2 + ( -21 + 18 )x^3 + (89 - 90)x^4 + (377 - 378)x^5 = 1 - 5x - 21x^2 - 3x^3 - x^4 - x^5.$$
Multiplying Colin Barker's numerator and denominator by $(1 + 3x + x^2)$ yields identically in $\mathbb{Z}[x]$:
$$(1 + 3x + x^2)(1 - 3x + 8x^2 - 3x^3 + x^4) = 1 + 18x^3 + x^6,$$
$$(1 + 3x + x^2)(1 - 8x + 2x^2 - x^3) = 1 - 5x - 21x^2 - 3x^3 - x^4 - x^5.$$
Cancelling the nonzero factor $(1 + 3x + x^2)$ in $\mathbb{Z}[[x]]$ establishes
$$\sum_{n=0}^{\infty} a(n) x^n = \frac{1 - 8x + 2x^2 - x^3}{1 - 3x + 8x^2 - 3x^3 + x^4}.$$
Finally, clearing the denominator gives $(1 - 3x + 8x^2 - 3x^3 + x^4)\sum_{n=0}^{\infty} a(n) x^n = 1 - 8x + 2x^2 - x^3$, and extracting $[x^n]$ for all $n > 3$ ($n \ge 4$) yields
$$a(n) = 3a(n-1) - 8a(n-2) + 3a(n-3) - a(n-4). \qquad \blacksquare$$

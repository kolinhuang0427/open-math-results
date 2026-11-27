# Proof of OEIS A178072 D-Finite Recurrence

## Theorem

Let $(a(n))_{n \ge 0}$ be OEIS [A178072](https://oeis.org/A178072), whose ordinary generating function $A(x) = \sum_{n=0}^{\infty} a(n) x^n \in \mathbb{Z}[[x]]$ satisfies $a(0) = 1$ and the algebraic equation
$$(2x + x^3) A(x)^2 - (1 + x)^2 A(x) + 1 = 0,$$
equivalently $A(x) = \frac{2}{(1+x)^2 + \sqrt{1 - 4x + 6x^2 + x^4}}$.
Then for every integer $n \ge 7$ (and also at $n = 6$ with the $a(-1)$ coefficient vanishing),
$$\begin{aligned}
0 &= 2n(n+1)a(n) + 2n(n+1)a(n-1) - 3(3n-1)(3n-4)a(n-2) \\
  &\quad + (61n^2 - 191n + 36)a(n-3) + 6(-2n^2 + 2n - 1)a(n-4) \\
  &\quad + 2(5n-1)(4n-15)a(n-5) + n(n-5)a(n-6) + (5n-1)(n-6)a(n-7).
\end{aligned}$$

---

## Proof

### 1. First-order inhomogeneous linear ODE

Set $P(x) := 2x + x^3$, $R(x) := (1+x)^2 = 1 + 2x + x^2$, and
$$\Delta(x) := R(x)^2 - 4P(x) = (1 + 4x + 6x^2 + 4x^3 + x^4) - (8x + 4x^3) = 1 - 4x + 6x^2 + x^4.$$
Completing the square in $P A^2 - R A + 1 = 0$ gives
$$\bigl(R(x) - 2P(x)A(x)\bigr)^2 = \Delta(x).$$
Let $y(x) := \sqrt{\Delta(x)} = 1 + O(x) \in \mathbb{Z}[[x]]$ be the unique formal square root with constant term $+1$. Because $(R(x) - 2P(x)A(x))|_{x=0} = 1$, uniqueness of the square root gives
$$y(x) = R(x) - 2P(x)A(x).$$
Differentiating $y(x)^2 = \Delta(x)$ gives $2 y(x) y'(x) = \Delta'(x)$, hence $2 \Delta(x) y'(x) = \Delta'(x) y(x)$ in $\mathbb{Q}[[x]]$. Substituting $y = R - 2PA$ and $y' = R' - 2P'A - 2PA'$ and dividing by $4$:
$$A_1(x)\, A'(x) + A_0(x)\, A(x) = R_1(x),$$
where
$$\begin{aligned}
A_1(x) &:= \Delta(x) P(x) = 2x - 8x^2 + 13x^3 - 4x^4 + 8x^5 + x^7, \\
A_0(x) &:= \Delta(x) P'(x) - \frac{1}{2}\Delta'(x) P(x) = 2 - 4x + 3x^2 - 10x^3 + 10x^4 + x^6, \\
R_1(x) &:= \frac{1}{2}\Delta(x) R'(x) - \frac{1}{4}\Delta'(x) R(x) = 2 - 4x - 3x^2 + 2x^3 - x^4,
\end{aligned}$$
using $\Delta'(x) = -4 + 12x + 4x^3$, $P'(x) = 2 + 3x^2$, and $R'(x) = 2(1 + x)$.

---

### 2. Second-order ODE and coefficient extraction

Apply the first-order differential operator $L := x(1 + 5x)\frac{d}{dx} + 4x$ to both sides of $A_1(x) A'(x) + A_0(x) A(x) = R_1(x)$:
$$P_2(x) A''(x) + P_1(x) A'(x) + P_0(x) A(x) = R_2(x),$$
where direct polynomial expansion yields:
$$\begin{aligned}
P_2(x) &= x(1 + 5x) A_1(x) \\
       &= 2x^2 + 2x^3 - 27x^4 + 61x^5 - 12x^6 + 40x^7 + x^8 + 5x^9, \\
P_1(x) &= x(1 + 5x)\bigl(A_1'(x) + A_0(x)\bigr) + 4x A_1(x) \\
       &= 4x + 8x^2 - 90x^3 + 236x^4 - 96x^5 + 282x^6 + 8x^7 + 44x^8, \\
P_0(x) &= x(1 + 5x) A_0'(x) + 4x A_0(x) \\
       &= 4x - 30x^2 + 12x^3 - 150x^4 + 240x^5 + 6x^6 + 34x^7, \\
R_2(x) &= x(1 + 5x) R_1'(x) + 4x R_1(x) \\
       &= 4x - 42x^2 - 36x^3 + 34x^4 - 24x^5.
\end{aligned}$$
Notice $\deg R_2 = 5$, so $[x^n] R_2(x) = 0$ for every $n \ge 6$.

Write $P_2(x) = \sum_{k=0}^{7} p_{2,k} x^{k+2}$, $P_1(x) = \sum_{k=0}^{7} p_{1,k} x^{k+1}$, and $P_0(x) = \sum_{k=0}^{7} p_{0,k} x^k$. For any $n \ge 7$, extracting $[x^n]$ from the left-hand side gives $\sum_{k=0}^{7} c_k(n)\, a(n-k) = 0$, where $c_k(n) = p_{2,k}(n-k)(n-k-1) + p_{1,k}(n-k) + p_{0,k}$:
- $k = 0$: $2n(n-1) + 4n + 0 = 2n(n+1)$;
- $k = 1$: $2(n-1)(n-2) + 8(n-1) + 4 = 2n(n+1)$;
- $k = 2$: $-27(n-2)(n-3) - 90(n-2) - 30 = -27n^2 + 45n - 12 = -3(3n-1)(3n-4)$;
- $k = 3$: $61(n-3)(n-4) + 236(n-3) + 12 = 61n^2 - 191n + 36$;
- $k = 4$: $-12(n-4)(n-5) - 96(n-4) - 150 = -12n^2 + 12n - 6 = 6(-2n^2 + 2n - 1)$;
- $k = 5$: $40(n-5)(n-6) + 282(n-5) + 240 = 40n^2 - 158n + 30 = 2(5n-1)(4n-15)$;
- $k = 6$: $(n-6)(n-7) + 8(n-6) + 6 = n^2 - 5n = n(n-5)$;
- $k = 7$: $5(n-7)(n-8) + 44(n-7) + 34 = 5n^2 - 31n + 6 = (5n-1)(n-6)$.

This establishes Mathar's 7-term recurrence for all $n \ge 7$ (and at $n = 6$ the $a(n-7)$ coefficient $(5n-1)(n-6)$ vanishes while $[x^6]R_2 = 0$, so the first seven terms vanish at $n = 6$ as well). $\blacksquare$

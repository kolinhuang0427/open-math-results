# Proof of OEIS A168452 Recurrence Conjecture

## Theorem
Let $C_k = \frac{1}{k+1}\binom{2k}{k}$ and $b(k) = C_k C_{k+1}$ for $k \ge 0$, and let $a(n) = \sum_{k=0}^n b(k) b(n-k)$ for $n \ge 0$. Then for every integer $n \ge 4$,
$$
\sum_{j=0}^{4} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_4(n)$ are the degree-$5$ polynomials listed in `TARGET.md`.

## Proof

### Step 1: Order-2 differential equation for $B(x) = \sum_{n \ge 0} b(n) x^n$
For every integer $n \ge 1$, the binomial ratio of $C_n$ gives
$$
\frac{C_n}{C_{n-1}} = \frac{n}{n+1}\cdot\frac{(2n)(2n-1)}{n^2} = \frac{2(2n-1)}{n+1},
$$
and applying this at $n$ and $n+1$ yields
$$
\frac{b(n)}{b(n-1)} = \frac{C_n}{C_{n-1}} \cdot \frac{C_{n+1}}{C_n} = \frac{4(2n-1)(2n+1)}{(n+1)(n+2)},
$$
so $(n+1)(n+2)\, b(n) = 4(2n-1)(2n+1)\, b(n-1)$ for all $n \ge 1$.

Multiplying by $x^n$ and summing over $n \ge 1$ in $\mathbb{Z}[[x]]$:
- On the left-hand side, since $b(0) = C_0 C_1 = 1$,
  $$
  \sum_{n \ge 1} (n+1)(n+2) b(n) x^n = \frac{d^2}{dx^2}\bigl(x^2 B(x)\bigr) - 2 b(0) = x^2 B''(x) + 4x B'(x) + 2 B(x) - 2.
  $$
- On the right-hand side, re-indexing $m = n - 1 \ge 0$ and using $(2m+1)(2m+3) = 4m(m-1) + 12m + 3$ gives
  $$
  4\sum_{n \ge 1} (2n-1)(2n+1) b(n-1) x^n
  = 4x \sum_{m \ge 0} (4m(m-1) + 12m + 3) b(m) x^m
  = 4x\bigl(4x^2 B''(x) + 12x B'(x) + 3 B(x)\bigr).
  $$

Equating both sides and rearranging yields the exact identity in $\mathbb{Z}[[x]]$:
$$
x^2(16x - 1) B''(x) = -2 + 2(1 - 6x) B(x) + 4x(1 - 12x) B'(x). \tag{1}
$$

### Step 2: Order-5 differential equation for $y(x) = B(x)^2 = \sum_{n \ge 0} a(n) x^n$
Since $a(n) = \sum_{k=0}^n b(k) b(n-k)$, we have $y(x) = B(x)^2$ in $\mathbb{Z}[[x]]$. Writing $\delta = x^2(16x - 1)$, we verify directly from (1) that $y, y', \delta y'', x\delta y''', x^2\delta^2 \text{-cleared } y^{(4)}, y^{(5)}$ are explicit polynomials in $\mathbb{Z}[x, B, B']$ evaluated at $(B(x), B'(x))$:
$$
\begin{aligned}
y &= M_0, & M_0 &= B^2, \\
y' &= M_1, & M_1 &= 2 B B', \\
x^2(16x - 1)\, y'' &= M_2, \\
x^3(16x - 1)\, y''' &= M_3, \\
x^4(16x - 1)^2\, y^{(4)} &= M_4, \\
x^5(16x - 1)^3\, y^{(5)} &= M_5,
\end{aligned}
$$
where $M_2, M_3, M_4, M_5 \in \mathbb{Z}[x, B, B']$ are obtained uniquely by differentiating in $\mathbb{Z}[[x]]$ and substituting (1) (and dividing by the exact common polynomial factors $x$ or $16x-1$ in $\mathbb{Z}[x, B, B']$):
$$
\begin{aligned}
M_2 &= 2\bigl((-12x + 2)B^2 + (-48x^2 + 4x)B B' - 2B + (16x^3 - x^2)(B')^2\bigr), \\
M_3 &= -12\bigl((-10x + 2)B^2 + (-24x^2 + 2x)B B' - 2B + (24x^3 - 2x^2)(B')^2 + x B'\bigr), \\
M_4 &= 24\bigl((-384x^2 + 110x - 5)B^2 + (-512x^3 + 42x^2)B B' + (-82x + 4)B \\
&\qquad + (1536x^4 - 252x^3 + 10x^2)(B')^2 + (112x^2 - 8x)B' + 1\bigr), \\
M_5 &= -48\bigl((-15360x^3 + 5548x^2 - 447x + 10)B^2 + (-4608x^3 + 688x^2 - 25x)B B' \\
&\qquad + (-3120x^2 + 197x)B + (102400x^5 - 24880x^4 + 1955x^3 - 50x^2)(B')^2 \\
&\qquad + (10000x^3 - 1425x^2 + 50x)B' + (160x - 10)\bigr).
\end{aligned}
$$
(Concretely, `verify.py` proves each relation $D_k(x) y^{(k)} = M_k(x, B, B')$ inductively in $\mathbb{Z}[x, B, B']$ by differentiating $D_k y^{(k)} = M_k$ using (1) and checking exact polynomial equality $x^2(16x-1) \bigl(D_{k+1} M_k' - D_k' M_k\bigr)$ or direct reduction.)

Now define the polynomials $p_0, \dots, p_5 \in \mathbb{Z}[x]$ by
$$
\begin{aligned}
p_0(x) &= -24(61440x^4 + 8640x^3 - 2572x^2 + 168x - 3), \\
p_1(x) &= -24x(512000x^4 + 39552x^3 - 18056x^2 + 1285x - 27), \\
p_2(x) &= -24x^2(16x - 1)(46720x^3 + 4968x^2 - 1121x + 39), \\
p_3(x) &= -12x^3(16x - 1)^2(2640x^2 + 391x - 34), \\
p_4(x) &= -x^4(16x - 1)^3(320x + 63), \\
p_5(x) &= -x^5(16x - 1)^3(16x + 3).
\end{aligned}
$$
Notice that $p_k(x)$ is divisible by the exact multiplier $D_k(x)$ for every $k \in \{0, \dots, 5\}$ ($D_0 = D_1 = 1$, $D_2 = x^2(16x-1)$, $D_3 = x^3(16x-1)$, $D_4 = x^4(16x-1)^2$, $D_5 = x^5(16x-1)^3$). Writing $p_k(x) = q_k(x) D_k(x)$ with $q_k \in \mathbb{Z}[x]$, we have
$$
\sum_{k=0}^{5} p_k(x) y^{(k)}(x) = \sum_{k=0}^{5} q_k(x) M_k(x, B(x), B'(x)).
$$
Expanding $\sum_{k=0}^5 q_k(x) M_k(x, B, B')$ in $\mathbb{Z}[x, B, B']$ (verified in `verify.py`) yields the exact polynomial identity
$$
\sum_{k=0}^{5} q_k(x) M_k(x, B, B') = 72 - 1152x.
$$
Evaluating at $B = B(x)$, $B' = B'(x)$ proves the exact differential equation in $\mathbb{Z}[[x]]$:
$$
\sum_{k=0}^{5} p_k(x) y^{(k)}(x) = 72 - 1152x. \tag{2}
$$

### Step 3: Coefficient extraction for $n \ge 4$
For any integer $n \ge 4$ and $k \in \{0, \dots, 5\}$, a monomial $c x^d$ in $p_k(x)$ contributes
$$
[x^n]\bigl(c x^d y^{(k)}(x)\bigr) = c \left(\prod_{i=0}^{k-1} (m - i)\right) a(m), \qquad m = n - (d - k).
$$
Across $p_0, \dots, p_5$, every monomial satisfies $0 \le d - k \le 4$:
- $p_0$ ($k=0$): $d \in [0, 4] \implies d - 0 \in [0, 4]$;
- $p_1$ ($k=1$): $d \in [1, 5] \implies d - 1 \in [0, 4]$;
- $p_2$ ($k=2$): $d \in [2, 6] \implies d - 2 \in [0, 4]$;
- $p_3$ ($k=3$): $d \in [3, 7] \implies d - 3 \in [0, 4]$;
- $p_4$ ($k=4$): $d \in [4, 8] \implies d - 4 \in [0, 4]$;
- $p_5$ ($k=5$): $d \in [5, 9] \implies d - 5 \in [0, 4]$.

Thus for every $n \ge 4$, all occurring indices $m = n - j$ ($0 \le j \le 4$) satisfy $m \ge 0$. Moreover, $[x^n](72 - 1152x) = 0$ for all $n \ge 2$ (and in particular for $n \ge 4$). Collecting the polynomial coefficients of $a(n-j)$ ($0 \le j \le 4$) extracted from $\sum_{k=0}^5 p_k(x) y^{(k)}(x)$ matches $C_0(n), \dots, C_4(n)$ identically in $\mathbb{Z}[n]$ (verified in `verify.py`). Hence $\sum_{j=0}^4 C_j(n) a(n-j) = 0$ for all $n \ge 4$. $\blacksquare$

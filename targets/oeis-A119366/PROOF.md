# Proof of OEIS A119366 Recurrence Conjecture

## Theorem
Let $a(0) = 0$ and, for $n \ge 1$,
$$
a(n) = \frac{1}{n} \sum_{k=0}^{\lfloor n/3 \rfloor} \binom{n}{3k+1} \binom{n}{3k}.
$$
Then for every integer $n \ge 7$,
$$
\sum_{j=0}^{7} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_7(n)$ are the degree-$4$ polynomials stated in `TARGET.md`.

## Proof

### Step 1: Generating function via roots of unity and Lagrange inversion
Let $\omega$ be a primitive cube root of unity satisfying $\omega^2 + \omega + 1 = 0$ and $\omega^3 = 1$, and work in the formal Laurent series field $\mathbb{Q}[\omega]((x))$. For every integer $n \ge 1$, writing $m = 3k + 1$ and using $\binom{n}{3k} = \binom{n}{n-3k} = \binom{n}{n+1-m}$ gives
$$
\sum_{k=0}^{\lfloor n/3 \rfloor} \binom{n}{3k+1} \binom{n}{3k}
= \sum_{\substack{0 \le m \le n+1 \\ m \equiv 1 \pmod 3}} \binom{n}{m}\binom{n}{n+1-m}
= \frac{1}{3} \sum_{j=0}^{2} \omega^{-j} [t^{n+1}]\Bigl((1+t)(1+\omega^j t)\Bigr)^n,
$$
since $\sum_{j=0}^2 \omega^{j(m-1)}$ equals $3$ when $m \equiv 1 \pmod 3$ and $0$ otherwise, and $\binom{n}{n+1} = 0$.

For each $j \in \{0, 1, 2\}$, substituting $t = 1/u$ in the Laurent polynomial $P_j(u) = (u+1)(u+\omega^j) = \omega^j + (1+\omega^j)u + u^2$ yields $(1+t)(1+\omega^j t) = P_j(u)/u^2$, and hence
$$
[t^{n+1}]\Bigl((1+t)(1+\omega^j t)\Bigr)^n = [u^{-(n+1)}] \frac{P_j(u)^n}{u^{2n}} = [u^{n-1}] P_j(u)^n.
$$
Since $P_j(0) = \omega^j \ne 0$, by the Lagrange Inversion Formula the unique formal power series $u_j(x) \in x\mathbb{Q}[\omega][[x]]$ satisfying
$$
u_j(x) = x\, P_j(u_j(x)) = x\bigl(\omega^j + (1+\omega^j)u_j(x) + u_j(x)^2\bigr)
$$
has coefficients $[x^n] u_j(x) = \frac{1}{n} [u^{n-1}] P_j(u)^n$ for all $n \ge 1$. Consequently, $y(x) = \sum_{n \ge 0} a(n) x^n \in x\mathbb{Z}[[x]]$ satisfies
$$
y(x) = \frac{1}{3}\bigl(u_0(x) + \omega^2 u_1(x) + \omega u_2(x)\bigr).
$$

Rearranging $x u_j^2 + (x(1+\omega^j) - 1)u_j + x\omega^j = 0$ gives
$$
\bigl(2x u_j(x) + x(1+\omega^j) - 1\bigr)^2 = \Delta_j(x),
$$
where
$$
\Delta_j(x) = (1 - x(1+\omega^j))^2 - 4\omega^j x^2,
$$
i.e., $\Delta_0(x) = 1 - 4x$, $\Delta_1(x) = 1 + 2\omega^2 x - 3\omega x^2$, and $\Delta_2(x) = 1 + 2\omega x - 3\omega^2 x^2$ (since $1+\omega = -\omega^2$ and $\omega^4 = \omega$). Each $\Delta_j(x) \in 1 + x\mathbb{Z}[\omega][x]$ has a unique square root $S_j(x) = \sum_{m \ge 0}\binom{1/2}{m}(\Delta_j(x) - 1)^m \in 1 + x\mathbb{Q}[\omega][[x]]$. Because $2x u_j(x) + x(1+\omega^j) - 1 \equiv -1 \pmod x$, we must have $2x u_j(x) = 1 - x(1+\omega^j) - S_j(x)$.

Multiplying by $\frac{1}{6x}\omega^{-j}$ and summing over $j \in \{0, 1, 2\}$, using $1 + \omega^2 + \omega = 0$ and
$$
2 + \omega^2(1+\omega) + \omega(1+\omega^2) = 2 - \omega - \omega^2 = 3,
$$
we obtain in $\mathbb{Q}[\omega]((x))$:
$$
y(x) = -\frac{1}{2} - \frac{1}{6}\Bigl(\frac{S_0(x)}{x} + \omega^2 \frac{S_1(x)}{x} + \omega \frac{S_2(x)}{x}\Bigr). \tag{1}
$$

### Step 2: Order-4 differential equation for $y(x)$
Define the linear differential operator $L = \sum_{k=0}^4 p_k(x) \frac{d^k}{dx^k}$ on $\mathbb{Q}[\omega]((x))$ with $p_0, \dots, p_4 \in \mathbb{Z}[x]$ given by
$$
\begin{aligned}
p_0(x) &= 12x(9216x^4 - 453x^3 + 9541x^2 - 2253x - 1233), \\
p_1(x) &= 6x(179010x^7 - 513666x^6 - 153168x^5 + 43362x^4 - 15265x^3 - 12783x^2 + 4719x + 1233), \\
p_2(x) &= 9x^2(232380x^7 - 519261x^6 - 237531x^5 - 117585x^4 - 12395x^3 + 8342x^2 + 1550x - 822), \\
p_3(x) &= x^3(774306x^7 - 1378881x^6 - 664443x^5 - 871557x^4 + 173836x^3 - 1287x^2 - 9879x - 175), \\
p_4(x) &= x^4(4x - 1)(x^2 + x + 1)(9x^2 - 3x + 1)(1779x^2 - 3450x - 881).
\end{aligned}
$$
For any polynomial $D(x) \in \mathbb{Z}[\omega][x]$ with $D(0) = 1$ and $S(x) = \sqrt{D(x)} \in 1 + x\mathbb{Q}[\omega][[x]]$, we have $S^2 = D$ and $S' = D'/(2S)$, so writing $f(x) = S(x)/x$ gives by induction on $k \in \{0, 1, 2, 3, 4\}$:
$$
2^k x^{k+1} D(x)^k f^{(k)}(x) = N_k(x) S(x),
$$
where $N_0(x) = 1$ and $N_{k+1} = 2x D N_k' - \bigl(2(k+1)D + (2k-1)x D'\bigr) N_k \in \mathbb{Z}[\omega][x]$ for $k = 0, 1, 2, 3$. Clearing $16 x^5 D(x)^4$ gives
$$
16 x^5 D(x)^4 L(f(x)) = S(x) \sum_{k=0}^{4} p_k(x)\, N_k(x)\, (2x D(x))^{4-k}.
$$

Exact univariate polynomial computation (verified by `verify.py`) shows that
$$
\sum_{k=0}^{4} p_k(x)\, N_k(x)\, (2x D(x))^{4-k} = 0
$$
identically in $\mathbb{Z}[x]$ for $D = \Delta_0$ and identically in $\mathbb{Z}[\omega][x]$ for $D = \Delta_1$ (and hence also for $D = \Delta_2$ by applying the field automorphism $\omega \mapsto \omega^2$ of $\mathbb{Q}[\omega]$ over $\mathbb{Q}$). Since $16 x^5 \Delta_j(x)^4 S_j(x) \ne 0$ in $\mathbb{Q}[\omega]((x))$, it follows that $L(S_j(x)/x) = 0$ for each $j \in \{0, 1, 2\}$.

By $\mathbb{Q}[\omega]$-linearity applied to (1), we obtain
$$
L(y(x)) = L\!\left(-\frac{1}{2}\right) = -\frac{1}{2} p_0(x) \quad \text{in } \mathbb{Q}[\omega]((x)), \text{ hence in } \mathbb{Z}[[x]].
$$

### Step 3: Coefficient extraction for $n \ge 7$
For any integer $n \ge 7$ and $k \in \{0, 1, 2, 3, 4\}$, a monomial $c x^d$ in $p_k(x)$ contributes
$$
[x^n]\bigl(c x^d y^{(k)}(x)\bigr) = c \left(\prod_{i=0}^{k-1} (m - i)\right) a(m), \qquad m = n - (d - k).
$$
Across $p_0, \dots, p_4$, every monomial has $0 \le d - k \le 7$:
- $p_0$ ($k=0$): $d \in [1, 5] \implies d - 0 \in [1, 5]$;
- $p_1$ ($k=1$): $d \in [1, 8] \implies d - 1 \in [0, 7]$;
- $p_2$ ($k=2$): $d \in [2, 9] \implies d - 2 \in [0, 7]$;
- $p_3$ ($k=3$): $d \in [3, 10] \implies d - 3 \in [0, 7]$;
- $p_4$ ($k=4$): $d \in [4, 11] \implies d - 4 \in [0, 7]$.

Hence for every $n \ge 7$, all indices $m = n - j$ ($0 \le j \le 7$) satisfy $m \ge 0$. Since $\deg(-\frac{1}{2} p_0) = 5 < 7$, $[x^n](-\frac{1}{2} p_0(x)) = 0$ for all $n \ge 7$. Collecting the resulting polynomial coefficients of $a(n-j)$ ($0 \le j \le 7$) from $L(y(x))$ matches $C_0(n), \dots, C_7(n)$ identically in $\mathbb{Z}[n]$ (verified in `verify.py`). Thus $\sum_{j=0}^7 C_j(n) a(n-j) = 0$ for all $n \ge 7$. $\blacksquare$

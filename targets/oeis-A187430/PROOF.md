# Proof of OEIS A187430 Irwin (2017) Conjecture

## Theorem
Let $a(n)$ ($n \ge 0$) be the number of nonnegative walks of $n$ steps starting and ending at $0$ using steps in $\{-2, -1, +1, +2\}$, and let
$$
C(x) = \sum_{n \ge 0} \frac{1}{n+1}\binom{2n}{n} x^n \in \mathbb{Z}[[x]]
$$
be the generating function of the Catalan numbers (`A000108`), characterized by $C(0) = 1$ and $x C(x)^2 = C(x) - 1$. Then as formal power series in $\mathbb{Z}[[x]]$:
$$
1 + \sum_{n \ge 0} a(n)\, \frac{(-1)^n x^{n+1}}{(1-x)^{2n+2}} = C(x).
$$

## Proof

### Step 1: Kernel equation from the walk definition
For integers $n \ge 0$ and $h \ge 0$, let $w(n, h)$ be the number of $n$-step walks starting at $0$, using steps in $\{+2, +1, -1, -2\}$, staying at height $\ge 0$ at every intermediate and final vertex, and ending at height $h$. By definition, $a(n) = w(n, 0)$, $w(0, 0) = 1$, $w(0, h) = 0$ for $h \ge 1$, and $w(n, h) = 0$ whenever $h > 2n$.

Define the formal generating function
$$
G(t, u) := \sum_{n \ge 0} \left(\sum_{h=0}^{2n} w(n, h)\, u^h\right) t^n \in \mathbb{Z}[u][[t]],
$$
and let $G_k(t) := [u^k] G(t, u) = \sum_{n \ge 0} w(n, k) t^n \in \mathbb{Z}[[t]]$, so $G_0(t) = A(t) := \sum_{n \ge 0} a(n) t^n$. For $n \ge 1$ and $h \ge 0$, every valid $n$-step walk ending at $h$ arises uniquely by appending a step $s \in \{+2, +1, -1, -2\}$ to a valid $(n-1)$-step walk ending at $h - s \ge 0$. Grouping by $s$ gives
$$
\begin{aligned}
\sum_{h \ge 0} w(n, h) u^h &= u^2 \sum_{k \ge 0} w(n-1, k) u^k + u \sum_{k \ge 0} w(n-1, k) u^k \\
&\quad + u^{-1} \sum_{k \ge 1} w(n-1, k) u^k + u^{-2} \sum_{k \ge 2} w(n-1, k) u^k.
\end{aligned}
$$
Multiplying by $u^2 t^n$, summing over $n \ge 1$, and adding the $n = 0$ term $u^2$ yields the exact identity in $\mathbb{Z}[u][[t]]$:
$$
u^2 G(t, u) = u^2 + t(u^4 + u^3 + u + 1) G(t, u) - t(u+1) A(t) - t u G_1(t),
$$
or equivalently, with kernel $K(t, u) := u^2 - t(u^4 + u^3 + u + 1)$,
$$
K(t, u)\, G(t, u) = u^2 - t(u + 1) A(t) - t u G_1(t).
$$

### Step 2: Algebraic kernel elimination in $\mathbb{Z}[[t]][u]$
Consider the rational formal power series
$$
f(y) := \frac{y(1-y)^2}{(1-y+y^2)^2} = y - 2y^3 + \dots \in y + y^2 \mathbb{Z}[[y]].
$$
Since $f(0) = 0$ and $f'(0) = 1$, by formal power series reversion there exists a unique formal series $y(t) = t + 2t^3 + \dots \in t\mathbb{Z}[[t]]$ satisfying $f(y(t)) = t$, i.e.,
$$
t(1 - y(t) + y(t)^2)^2 = y(t)(1 - y(t))^2.
$$
Set $s(t) := \frac{y(t)}{1 - y(t)} \in t\mathbb{Z}[[t]]$ (noting $1 - y(t)$ and $1 - y(t) + y(t)^2$ are units in $\mathbb{Z}[[t]]$), and define
$$
M(t, u) := u^2 - s(t) u - y(t) \in \mathbb{Z}[[t]][u], \qquad Q(t, u) := \frac{(1-y(t))^2}{(1-y(t)+y(t)^2)^2} \bigl(-y(t) u^2 - s(t) u + 1\bigr) \in \mathbb{Z}[[t]][u].
$$
Substituting $t = \frac{y(t)(1-y(t))^2}{(1-y(t)+y(t)^2)^2}$ and $s(t) = \frac{y(t)}{1-y(t)}$, direct polynomial expansion (verified symbolically by `verify.py`) yields the exact identity in $\mathbb{Z}[[t]][u]$:
$$
K(t, u) = M(t, u)\, Q(t, u).
$$
Let $R := \mathbb{Z}[[t]][u] / (M(t, u))$ with $\bar{u} := u \bmod M(t, u)$. Because $M(t, u)$ is monic of degree $2$ in $u$, $R = \mathbb{Z}[[t]] \cdot 1 \oplus \mathbb{Z}[[t]] \cdot \bar{u}$ is a free $\mathbb{Z}[[t]]$-module of rank $2$, complete in the $t$-adic topology. For each $n \ge 0$, the coefficient $[t^n] G(t, u) = \sum_{h=0}^{2n} w(n, h) u^h$ is a polynomial in $u$, so the reduction map $\mathbb{Z}[u][[t]] \to R$ is well-defined term-by-term in $t$. Reducing the kernel equation modulo $M(t, u)$ annihilates $K(t, \bar{u}) = M(t, \bar{u}) Q(t, \bar{u}) = 0$, leaving
$$
0 = \bigl(s(t)\bar{u} + y(t)\bigr) - t(\bar{u} + 1) A(t) - t \bar{u}\, G_1(t) = \bigl(y(t) - t A(t)\bigr) + \bigl(s(t) - t A(t) - t G_1(t)\bigr)\bar{u} \quad \text{in } R.
$$
Since $\{1, \bar{u}\}$ is a $\mathbb{Z}[[t]]$-basis of $R$, comparing the coefficient of $1$ gives
$$
t A(t) = y(t).
$$

### Step 3: Substitution $t = -x/(1-x)^2$ and Catalan identification
Define $u(x) := \frac{-x}{(1-x)^2} \in x\mathbb{Z}[[x]]$ and $Y(x) := 1 - C(x) \in x\mathbb{Z}[[x]]$. Since $x C(x)^2 = C(x) - 1$, we have $(1 - x) C(x)^2 = C(x)^2 - x C(x)^2 = C(x)^2 - C(x) + 1$, and moreover $1 - Y(x) = C(x)$ and $1 - Y(x) + Y(x)^2 = C(x)^2 - C(x) + 1$ are units in $\mathbb{Z}[[x]]$ (both have constant term $1$). Multiplying by the unit $(1-x)^2 (C(x)^2 - C(x) + 1)^2$ and using $x C(x)^2 = C(x) - 1$ gives the exact identity in $\mathbb{Z}[[x]]$ (verified modulo $x C^2 - C + 1$ in `verify.py`):
$$
(1-x)^2 Y(x)(1-Y(x))^2 + x (1 - Y(x) + Y(x)^2)^2 = (1-x)^2 (1 - C(x)) C(x)^2 + x (C(x)^2 - C(x) + 1)^2 = 0,
$$
and therefore
$$
f(Y(x)) = \frac{Y(x)(1-Y(x))^2}{(1-Y(x)+Y(x)^2)^2} = \frac{-x}{(1-x)^2} = u(x).
$$
Since $Y(0) = 0$ and $u(0) = 0$, substituting $Y(x)$ into $y(f(Y)) = Y$ yields $y(u(x)) = Y(x) = 1 - C(x)$ in $\mathbb{Z}[[x]]$. Finally, using $y(t) = t A(t) = \sum_{n \ge 0} a(n) t^{n+1}$,
$$
1 - C(x) = y(u(x)) = \sum_{n \ge 0} a(n) \left(\frac{-x}{(1-x)^2}\right)^{n+1} = -\sum_{n \ge 0} a(n)\, \frac{(-1)^n x^{n+1}}{(1-x)^{2n+2}}.
$$
Rearranging gives
$$
1 + \sum_{n \ge 0} a(n)\, \frac{(-1)^n x^{n+1}}{(1-x)^{2n+2}} = C(x)
$$
as formal power series in $\mathbb{Z}[[x]]$. $\blacksquare$

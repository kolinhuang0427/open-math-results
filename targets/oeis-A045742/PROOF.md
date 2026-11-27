# Proof of OEIS A045742 Recurrence Conjecture

## Theorem
Let $a(2) = 0$ and, for $n \ge 3$,
$$
a(n) = \frac{1}{n-1}\sum_{k=1}^{n-2} k \binom{n+k-2}{k}\binom{3n-3}{n-2-k}.
$$
Then for every integer $n \ge 5$,
$$
\sum_{j=0}^{3} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_3(n)$ are the cubic polynomials listed in `TARGET.md`.

## Proof

### Step 1: Generating function and cubic equation via Lagrange–Bürmann inversion
Set $m = n - 1 \ge 2$ (so $n - 2 = m - 1$ and $3n - 3 = 3m$). Then
$$
a(m+1) = \frac{1}{m}\sum_{k=1}^{m-1} k\binom{m-1+k}{k}\binom{3m}{m-1-k} \qquad (m \ge 2).
$$
From $\frac{1}{(1-t)^m} = \sum_{k \ge 0}\binom{m-1+k}{k}t^k$, applying $t\frac{d}{dt}$ gives $\frac{m t}{(1-t)^{m+1}} = \sum_{k \ge 1} k\binom{m-1+k}{k} t^k$. Multiplying by $(1+t)^{3m}$ and extracting $[t^{m-1}]$ yields
$$
[t^{m-1}]\frac{m t(1+t)^{3m}}{(1-t)^{m+1}} = \sum_{k=1}^{m-1} k\binom{m-1+k}{k}\binom{3m}{m-1-k} = m\, a(m+1),
$$
so dividing by $m \ge 2$ gives
$$
a(m+1) = [t^{m-2}] \frac{(1+t)^{3m}}{(1-t)^{m+1}} = [t^m]\!\left(\frac{t^2}{1-t}\Phi(t)^m\right), \qquad \Phi(t) := \frac{(1+t)^3}{1-t} \in 1 + t\mathbb{Z}[[t]].
$$
(For $m = 0, 1$, $[t^m]\bigl(\frac{t^2}{1-t}\Phi(t)^m\bigr) = 0$, matching $a(2) = 0$.)

Let $t(x) \in x\mathbb{Z}[[x]]$ be the unique formal power series satisfying $t(x) = x\Phi(t(x))$, i.e., $x(1 + t(x))^3 - t(x)(1 - t(x)) = 0$. By the Lagrange–Bürmann inversion formula,
$$
\sum_{m \ge 2} a(m+1) x^m = \frac{x t'(x)}{t(x)} \cdot \frac{t(x)^2}{1 - t(x)} \in x^2\mathbb{Z}[[x]].
$$
Differentiating $t(1-t) = x(1+t)^3$ in $\mathbb{Z}[[x]]$ gives $\bigl(1 - 2t - 3x(1+t)^2\bigr) t' = (1+t)^3$; multiplying by $x$ and substituting $x(1+t)^3 = t(1-t)$ gives
$$
\left(1 - 2t - \frac{3t(1-t)}{1+t}\right) x t' = t(1-t) \implies \frac{1 - 4t + t^2}{1+t} x t' = t(1-t),
$$
so $\frac{x t'}{t(1-t)} = \frac{1+t}{1 - 4t + t^2}$ in $\mathbb{Z}[[x]]$. Hence $y(x) = \sum_{n \ge 2} a(n) x^n = x\sum_{m \ge 2} a(m+1) x^m \in x^3\mathbb{Z}[[x]]$ satisfies
$$
y(x) = \frac{x\, t(x)^2(1 + t(x))}{1 - 4t(x) + t(x)^2}.
$$

Thus $(t(x), y(x))$ satisfies both $E_1(x, t) = x(1+t)^3 - t(1-t) = 0$ and $E_2(x, y, t) = y(1 - 4t + t^2) - x t^2(1+t) = 0$ identically in $\mathbb{Z}[[x]]$. Expanding the $6 \times 6$ Sylvester resultant with respect to $t$ (verified in `verify.py`) yields
$$
\mathrm{Res}_t(E_1, E_2) = 2x\, P(x, y),
$$
where
$$
P(x, y) = x^4 - 27x^3y + 108x^2y^3 + 108x^2y^2 + 13x^2y - xy - y^3 - y^2 \in \mathbb{Z}[x, y].
$$
Since $\mathbb{Z}[[x]]$ is an integral domain and $2x \ne 0$, it follows that $P(x, y(x)) = 0$ identically in $\mathbb{Z}[[x]]$.

### Step 2: Order-3 differential equation for $y(x)$
Let $P_x = \partial_x P$ and $P_y = \partial_y P = (-27x^3 + 13x^2 - x) + (216x^2 - 2)y + (324x^2 - 3)y^2$. Because $y(x) = x^3 + O(x^4)$, we have $P_y(x, y(x)) = -x + O(x^2) \ne 0$ in $\mathbb{Z}[[x]]$. Differentiating $P(x, y(x)) = 0$ formally in $\mathbb{Z}[[x]]$ gives $P_y(x, y(x)) y'(x) = N_1(x, y(x))$ with $N_1 = -P_x$. Defining $N_2, N_3 \in \mathbb{Z}[x, y]$ recursively by
$$
N_{k+1} = \bigl(P_y\, \partial_x N_k + N_1\, \partial_y N_k\bigr) P_y - (2k-1) N_k \bigl(P_y\, \partial_x P_y + N_1\, \partial_y P_y\bigr) \qquad (k = 1, 2),
$$
formal induction in $\mathbb{Z}[[x]]$ (without division) gives $P_y(x, y(x))^{2k-1} y^{(k)}(x) = N_k(x, y(x))$ in $\mathbb{Z}[[x]]$ for $k = 1, 2, 3$.

Define $p_{\mathrm{inhom}}, p_0, p_1, p_2, p_3 \in \mathbb{Z}[x]$ by
$$
\begin{aligned}
p_{\mathrm{inhom}}(x) &= 2544x^3, \\
p_0(x) &= 7632x^3, \\
p_1(x) &= 24x^2(4554x^2 + 2594x - 947), \\
p_2(x) &= x^2(1018008x^3 - 180144x^2 + 13344x - 947), \\
p_3(x) &= x^3(4554x - 523)(108x^2 - 1),
\end{aligned}
$$
and form the cleared numerator $Q(x, y) = P_y^5(p_{\mathrm{inhom}} + p_0 y) + P_y^4 p_1 N_1 + P_y^2 p_2 N_2 + p_3 N_3 \in \mathbb{Z}[x, y]$. Exact polynomial division in $\mathbb{Z}[x, y]$ (verified by `verify.py`) yields $Q(x, y) = P(x, y) R(x, y)$ with zero remainder. Evaluating at $y = y(x)$ gives
$$
P_y(x, y(x))^5 \Bigl(2544x^3 + \sum_{k=0}^{3} p_k(x) y^{(k)}(x)\Bigr) = P(x, y(x)) R(x, y(x)) = 0 \quad \text{in } \mathbb{Z}[[x]].
$$
Since $\mathbb{Z}[[x]]$ is an integral domain and $P_y(x, y(x)) \ne 0$, we conclude
$$
2544x^3 + p_0(x) y(x) + p_1(x) y'(x) + p_2(x) y''(x) + p_3(x) y'''(x) = 0 \quad \text{in } \mathbb{Z}[[x]].
$$

### Step 3: Coefficient extraction for $n \ge 5$
For any integer $n \ge 5$ and $k \in \{0, 1, 2, 3\}$, a monomial $c x^d$ in $p_k(x)$ contributes
$$
[x^n]\bigl(c x^d y^{(k)}(x)\bigr) = c \left(\prod_{i=0}^{k-1} (m - i)\right) a(m), \qquad m = n - (d - k).
$$
Across $p_0, \dots, p_3$, every monomial has $0 \le d - k \le 3$:
- $p_0$ ($k=0$): $d = 3 \implies d - 0 = 3$;
- $p_1$ ($k=1$): $d \in [2, 4] \implies d - 1 \in [1, 3]$;
- $p_2$ ($k=2$): $d \in [2, 5] \implies d - 2 \in [0, 3]$;
- $p_3$ ($k=3$): $d \in [3, 6] \implies d - 3 \in [0, 3]$.

Hence for every $n \ge 5$, all indices $m = n - j$ ($0 \le j \le 3$) satisfy $m \ge 2$ (within the OEIS domain of $a$). Moreover, $[x^n](2544x^3) = 0$ for all $n \ge 5$. Collecting the resulting polynomial coefficients of $a(n-j)$ ($0 \le j \le 3$) matches $C_0(n), \dots, C_3(n)$ identically in $\mathbb{Z}[n]$ (verified in `verify.py`). Thus $\sum_{j=0}^3 C_j(n) a(n-j) = 0$ for all $n \ge 5$. $\blacksquare$

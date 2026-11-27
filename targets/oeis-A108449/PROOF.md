# Proof of OEIS A108449 Recurrence Conjecture

## Theorem
Let $a(n)$ ($n \ge 0$) be the number of lattice paths from $(0,0)$ to $(3n,0)$ staying in $Y \ge 0$ with steps $u=(2,1)$, $U=(1,2)$, and $d=(1,-1)$, having no pyramids (a factor $u^p d^p$ or $U^p d^{2p}$ with $p \ge 1$ starting on $Y=0$). Then for every integer $n \ge 8$,
$$
\sum_{j=0}^{8} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_8(n)$ are the cubic polynomials listed in `TARGET.md`.

## Proof

### Step 1: Generating function from the combinatorial definition
Each step $u=(2,1)$ and $U=(1,2)$ increases $X+Y$ by $3$, whereas $d=(1,-1)$ preserves $X+Y$. Hence a path from $(0,0)$ to $(X,0)$ ends at $(3n,0)$ if and only if it uses exactly $n$ up-steps ($u$ and $U$ combined).

Let $A(x) = \sum_{n \ge 0} A_n x^n \in \mathbb{Z}[[x]]$ be the ordinary generating function (with $x$ marking up-step count $n = \#u + \#U$) of **all** first-quadrant paths from $(0,0)$ to $(3n,0)$ using $\{u, U, d\}$, and let $K(x) = \sum_{n \ge 1} K_n x^n$ be the OGF of **primitive** such paths (nonempty paths that touch $Y=0$ only at their start and end).

1. Every nonempty path decomposes uniquely at its first return to $Y=0$ as a primitive path followed by an arbitrary path, giving $A(x) = 1 + K(x) A(x)$.
2. Every primitive path begins with either $u$ or $U$ and ends with $d$:
   - If it begins with $u=(2,1)$ (reaching height $1$), the interior between this first $u$ and the final $d$ stays at height $\ge 1$ and begins and ends at height $1$; shifting vertically by $-1$ identifies it bijectively with an arbitrary first-quadrant path from $(0,0)$ to $(3m,0)$, contributing $x A(x)$.
   - If it begins with $U=(1,2)$ (reaching height $2$), since $d=(1,-1)$ is the only downward step, the path must first visit height $1$ via a step $d$. Between $U$ and this first visit to height $1$, it stays at height $\ge 2$ (contributing $A(x)$ after vertical shift $-2$); between this first visit to height $1$ and the final step $d$, it stays at height $\ge 1$ (contributing $A(x)$ after vertical shift $-1$). Total contribution: $x A(x)^2$.
   
   Thus $K(x) = x A(x) + x A(x)^2 = x A(x)(1 + A(x))$, and $A(x) = 1 + x A(x)^2 + x A(x)^3$.

3. Every first-quadrant path from $(0,0)$ to $(3n,0)$ decomposes uniquely into primitive paths $W_1 W_2 \cdots W_r$ ($r \ge 0$), where the returns to $Y=0$ occur precisely at the boundaries between the $W_i$. Any pyramid $u^p d^p$ or $U^p d^{2p}$ ($p \ge 1$) starting at $Y=0$ has strictly positive intermediate heights and reaches $Y=0$ only at its last step, so it starts at the beginning of some $W_i$ and ends at the end of that same $W_i$ (i.e., $W_i$ itself is $u^p d^p$ or $U^p d^{2p}$). Conversely, any primitive factor $W_i \in \{u^p d^p, U^p d^{2p} : p \ge 1\}$ creates a pyramid starting at the $x$-axis.

4. For each $p \ge 1$, $u^p d^p$ and $U^p d^{2p}$ are distinct primitive paths of up-step count $p$. Removing them from $K(x)$ yields the OGF of pyramid-free primitive paths:
   $$
   K_{\mathrm{free}}(x) = K(x) - 2\sum_{p \ge 1} x^p = x A(x)(1+A(x)) - \frac{2x}{1-x} \in x^2\mathbb{Z}[[x]].
   $$
   Since a pyramid-free path is an arbitrary concatenation of pyramid-free primitive paths, $y(x) = \sum_{n \ge 0} a(n) x^n \in \mathbb{Z}[[x]]$ satisfies
   $$
   y(x) = \frac{1}{1 - K_{\mathrm{free}}(x)} = \frac{1 - x}{1 + x - x(1 - x) A(x)(1 + A(x))}.
   $$
   Note that $1 + x - x(1-x)A(x)(1+A(x)) \in 1 + x\mathbb{Z}[[x]]$ is a unit in $\mathbb{Z}[[x]]$.

### Step 2: Algebraic equation for $y(x)$
Define polynomials in $\mathbb{Z}[x, y, A]$:
$$
\begin{aligned}
E_1(x, A) &= x A^3 + x A^2 - A + 1, \\
E_2(x, y, A) &= y\bigl(1 + x - x(1-x)A(1+A)\bigr) - (1 - x).
\end{aligned}
$$
By Step 1, $E_1(x, A(x)) = 0$ and $E_2(x, y(x), A(x)) = 0$ identically in $\mathbb{Z}[[x]]$. Taking the resultant with respect to $A$ eliminates $A(x)$ and gives $\mathrm{Res}_A(E_1, E_2)(x, y(x)) = 0$ in $\mathbb{Z}[[x]]$. Direct expansion of the $5 \times 5$ Sylvester determinant in $\mathbb{Z}[x, y]$ (verified by `verify.py`) yields
$$
\mathrm{Res}_A(E_1, E_2) = x^2 P(x, y),
$$
where
$$
\begin{aligned}
P(x, y) =\; & (-1 + 3x - 3x^2 + x^3) + (1 + 3x - 9x^2 + 5x^3)\,y \\
& + (-5x - x^2 + 5x^3 + x^4)\,y^2 + (-x + 9x^2 - 3x^3 + 3x^4)\,y^3.
\end{aligned}
$$
Since $\mathbb{Z}[[x]]$ is an integral domain and $x^2 \ne 0$, we conclude
$$
P(x, y(x)) = 0 \quad \text{in } \mathbb{Z}[[x]].
$$

### Step 3: Order-3 differential equation for $y(x)$
Let $P_x = \partial_x P$ and $P_y = \partial_y P$. Since $y(0) = a(0) = 1$, we have $P_y(0, y(0)) = 1 \ne 0$, so $P_y(x, y(x)) \in 1 + x\mathbb{Z}[[x]]$ is a unit in $\mathbb{Z}[[x]]$ (and in $\mathbb{Q}[[x]]$). Differentiating $P(x, y(x)) = 0$ formally in $\mathbb{Z}[[x]]$ gives $P_x(x, y(x)) + P_y(x, y(x)) y'(x) = 0$, so $y'(x) = N_1(x, y(x)) / P_y(x, y(x))$ with $N_1 = -P_x$.

Recursively define $N_1, N_2, N_3 \in \mathbb{Z}[x, y]$ by
$$
N_{k+1} = \bigl(P_y\, \partial_x N_k + N_1\, \partial_y N_k\bigr) P_y - (2k - 1) N_k \bigl(P_y\, \partial_x P_y + N_1\, \partial_y P_y\bigr) \qquad (k = 1, 2).
$$
By the chain and quotient rules with $y'(x) = N_1(x, y(x)) / P_y(x, y(x))$, induction on $k \in \{1, 2, 3\}$ gives
$$
y^{(k)}(x) = \frac{N_k(x, y(x))}{P_y(x, y(x))^{2k-1}} \qquad \text{in } \mathbb{Q}[[x]] \quad (k = 1, 2, 3).
$$

Now define the polynomials $p_{\mathrm{inhom}}, p_0, p_1, p_2, p_3 \in \mathbb{Z}[x]$ by
$$
\begin{aligned}
p_{\mathrm{inhom}}(x) &= 342x^7 + 3006x^6 + 4452x^5 - 67380x^4 + 25086x^3 + 168166x^2 - 42504x, \\
p_0(x) &= 2x\bigl(513x^6 + 5481x^5 + 16074x^4 - 252882x^3 - 265431x^2 - 43423x + 21252\bigr), \\
p_1(x) &= 2x\bigl(1296x^8 + 12681x^7 + 27666x^6 - 46737x^5 + 20532x^4 + 373095x^3 - 369686x^2 + 76017x - 3696\bigr), \\
p_2(x) &= x^2(x - 1)\bigl(3033x^7 + 36747x^6 + 74775x^5 - 270837x^4 + 65427x^3 - 72523x^2 - 21731x + 2773\bigr), \\
p_3(x) &= 2x^3(x - 1)^2(87x + 431)(x^2 + 11x - 1)(3x^3 - 3x^2 + 9x - 1),
\end{aligned}
$$
and form the cleared numerator in $\mathbb{Z}[x, y]$:
$$
Q(x, y) = P_y^5\bigl(p_{\mathrm{inhom}} + p_0 y\bigr) + P_y^4 p_1 N_1 + P_y^2 p_2 N_2 + p_3 N_3.
$$
By exact polynomial division in $\mathbb{Z}[x, y]$ (verified by `verify.py`), $P(x, y)$ divides $Q(x, y)$ with zero remainder: $Q(x, y) = P(x, y) R(x, y)$ for a polynomial $R(x, y) \in \mathbb{Z}[x, y]$ ($\deg_x R = 24, \deg_y R = 8$). Evaluating at $y = y(x)$ gives
$$
P_y(x, y(x))^5 \Bigl(p_{\mathrm{inhom}}(x) + p_0(x) y(x) + p_1(x) y'(x) + p_2(x) y''(x) + p_3(x) y'''(x)\Bigr) = P(x, y(x)) R(x, y(x)) = 0.
$$
Because $P_y(x, y(x))$ is a unit in $\mathbb{Z}[[x]]$, we obtain the exact formal differential equation in $\mathbb{Q}[[x]]$:
$$
p_{\mathrm{inhom}}(x) + p_0(x) y(x) + p_1(x) y'(x) + p_2(x) y''(x) + p_3(x) y'''(x) = 0.
$$

### Step 4: Coefficient extraction for $n \ge 8$
For any integer $n \ge 8$ and $k \in \{0, 1, 2, 3\}$, extracting $[x^n]$ from a monomial $c x^d y^{(k)}(x)$ appearing in $p_k(x) y^{(k)}(x)$ gives
$$
[x^n]\bigl(c x^d y^{(k)}(x)\bigr) = c \left(\prod_{i=0}^{k-1} (m - i)\right) a(m), \qquad m = n - (d - k),
$$
where the falling product is $1$ for $k = 0$ and automatically vanishes if $0 \le m < k$. Across $p_0, p_1, p_2, p_3$, every term has $0 \le d - k \le 8$:
- $p_0$ ($k=0$) has degrees $d \in [1, 7]$, so $d - 0 \in [1, 7]$;
- $p_1$ ($k=1$) has degrees $d \in [1, 9]$, so $d - 1 \in [0, 8]$;
- $p_2$ ($k=2$) has degrees $d \in [2, 10]$, so $d - 2 \in [0, 8]$;
- $p_3$ ($k=3$) has degrees $d \in [3, 11]$, so $d - 3 \in [0, 8]$.

Thus for every $n \ge 8$, all occurring indices $m = n - j$ satisfy $m \ge 0$. Furthermore, $\deg p_{\mathrm{inhom}} = 7 < 8$, so $[x^n] p_{\mathrm{inhom}}(x) = 0$ for all $n \ge 8$. Summing the coefficients of $a(n-j)$ ($0 \le j \le 8$) extracted from $\sum_{k=0}^3 p_k(x) y^{(k)}(x)$ matches $C_0(n), \dots, C_8(n)$ identically in $\mathbb{Z}[n]$ (verified term-by-term in `verify.py`). Therefore $\sum_{j=0}^8 C_j(n) a(n-j) = 0$ for all integers $n \ge 8$. $\blacksquare$

# Proof of OEIS A045743 Recurrence Conjecture

## Theorem
Let $a(n)$ ($n \ge 2$) be defined by the OEIS closed form
$$
a(n) = \frac{1}{n-1}\sum_{i=0}^{\lfloor (n-2)/2 \rfloor} \binom{n-2+i}{i}\binom{3n-3-i}{n-2-2i}.
$$
Then for every integer $n \ge 6$,
$$
\sum_{j=0}^{4} C_j(n)\, a(n-j) = 0,
$$
where $C_0(n), \dots, C_4(n)$ are the quartic polynomials stated in `TARGET.md`.

## Proof

### Step 1: Generating function and algebraic equation via Lagrange inversion
Set $m = n - 1 \ge 1$ (so $n - 2 = m - 1$ and $3n - 3 = 3m$). Then
$$
a(m+1) = \frac{1}{m}\sum_{i=0}^{\lfloor (m-1)/2 \rfloor} \binom{m-1+i}{i}\binom{3m-i}{m-1-2i} \qquad (m \ge 1).
$$
Consider the formal power series $\Phi(t) = \frac{(1+t)^4}{1+t-t^2} \in 1 + t\mathbb{Z}[[t]]$. Note that $\Phi(t) = \frac{(1+t)^3}{1 - t^2/(1+t)}$, so for every integer $m \ge 1$,
$$
\Phi(t)^m = (1+t)^{3m} \left(1 - \frac{t^2}{1+t}\right)^{-m}
= \sum_{i \ge 0} \binom{m-1+i}{i} t^{2i} (1+t)^{3m-i}.
$$
Every summand contributing to $[t^{m-1}]$ has $2i \le m-1$, hence $3m - i \ge 0$, so $(1+t)^{3m-i}$ is a polynomial and $[t^{m-1-2i}](1+t)^{3m-i} = \binom{3m-i}{m-1-2i}$. Therefore,
$$
[t^{m-1}] \Phi(t)^m = \sum_{i=0}^{\lfloor (m-1)/2 \rfloor} \binom{m-1+i}{i}\binom{3m-i}{m-1-2i} = m\, a(m+1) \qquad (m \ge 1).
$$
By the Lagrange Inversion Formula (since $\Phi(0) = 1$), the unique formal power series $G(x) \in x\mathbb{Z}[[x]]$ satisfying $G(x) = x\,\Phi(G(x))$, i.e.,
$$
G(x)\bigl(1 + G(x) - G(x)^2\bigr) = x\bigl(1 + G(x)\bigr)^4,
$$
has coefficients $[x^m] G(x) = \frac{1}{m} [t^{m-1}] \Phi(t)^m = a(m+1)$ for all $m \ge 1$.

Setting $y(x) = x\, G(x) = \sum_{n \ge 2} a(n) x^n \in x^2\mathbb{Z}[[x]]$ (extending by $a(0) = a(1) = 0$) and multiplying $x(1 + y/x)^4 - (y/x)(1 + y/x - y^2/x^2) = 0$ by $x^3$ yields
$$
P(x, y(x)) = 0 \quad \text{identically in } \mathbb{Z}[[x]],
$$
where
$$
P(x, y) = x^4 + 4x^3y + 6x^2y^2 - x^2y + 4xy^3 - xy^2 + y^4 + y^3 \in \mathbb{Z}[x, y].
$$

### Step 2: Order-4 differential equation for $y(x)$
Let $P_x = \partial_x P$ and $P_y = \partial_y P = (4x^3 - x^2) + (12x^2 - 2x)y + (12x + 3)y^2 + 4y^3$. Because $y(x) = x^2 + O(x^3)$, substituting $y = y(x)$ gives
$$
P_y(x, y(x)) = -x^2 + O(x^3) \ne 0 \quad \text{in } \mathbb{Z}[[x]].
$$
Differentiating $P(x, y(x)) = 0$ formally in $\mathbb{Z}[[x]]$ gives $P_y(x, y(x)) y'(x) = N_1(x, y(x))$, where $N_1 = -P_x \in \mathbb{Z}[x, y]$. Recursively define $N_1, N_2, N_3, N_4 \in \mathbb{Z}[x, y]$ by
$$
N_{k+1} = \bigl(P_y\, \partial_x N_k + N_1\, \partial_y N_k\bigr) P_y - (2k - 1) N_k \bigl(P_y\, \partial_x P_y + N_1\, \partial_y P_y\bigr) \qquad (k = 1, 2, 3).
$$
By formal induction in $\mathbb{Z}[[x]]$ — differentiating $P_y^{2k-1} y^{(k)} = N_k(x, y(x))$ and multiplying by $P_y^2$ using $P_y y' = N_1$ — we obtain without division:
$$
P_y(x, y(x))^{2k-1} y^{(k)}(x) = N_k(x, y(x)) \quad \text{in } \mathbb{Z}[[x]] \qquad (k = 1, 2, 3, 4).
$$

Now define the polynomials $p_{\mathrm{inhom}}, p_0, p_1, p_2, p_3, p_4 \in \mathbb{Z}[x]$ by
$$
\begin{aligned}
p_{\mathrm{inhom}}(x) &= 52437120x^5 - 222762936x^4 - 86483718x^3, \\
p_0(x) &= -72x^3(225648x - 3034829), \\
p_1(x) &= 48x^3(1430912x^2 - 9108520x - 2939805), \\
p_2(x) &= 48x^3(31050464x^3 - 58671498x^2 - 54421082x + 516693), \\
p_3(x) &= x^3(1910439936x^4 - 813515264x^3 - 3673122304x^2 + 140653072x + 2048955), \\
p_4(x) &= 2x^4(753968x - 676909)(256x^3 + 512x^2 - 32x - 5).
\end{aligned}
$$
Form the cleared numerator in $\mathbb{Z}[x, y]$:
$$
Q(x, y) = P_y^7(p_{\mathrm{inhom}} + p_0 y) + P_y^6 p_1 N_1 + P_y^4 p_2 N_2 + P_y^2 p_3 N_3 + p_4 N_4.
$$
By exact polynomial division in $\mathbb{Z}[x, y]$ (verified by `verify.py`), $P(x, y)$ divides $Q(x, y)$ with zero remainder: $Q(x, y) = P(x, y) R(x, y)$ for an explicit $R(x, y) \in \mathbb{Z}[x, y]$. Setting $y = y(x)$ gives
$$
P_y(x, y(x))^7 \Bigl(p_{\mathrm{inhom}}(x) + \sum_{k=0}^{4} p_k(x) y^{(k)}(x)\Bigr) = P(x, y(x)) R(x, y(x)) = 0 \quad \text{in } \mathbb{Z}[[x]].
$$
Because $\mathbb{Z}[[x]]$ is an integral domain and $P_y(x, y(x)) \ne 0$, it follows that
$$
p_{\mathrm{inhom}}(x) + \sum_{k=0}^{4} p_k(x) y^{(k)}(x) = 0 \quad \text{in } \mathbb{Z}[[x]].
$$

### Step 3: Coefficient extraction for $n \ge 6$
For any integer $n \ge 6$ and $k \in \{0, 1, 2, 3, 4\}$, a monomial $c x^d$ in $p_k(x)$ contributes
$$
[x^n]\bigl(c x^d y^{(k)}(x)\bigr) = c \left(\prod_{i=0}^{k-1} (m - i)\right) a(m), \qquad m = n - (d - k).
$$
Across $p_0, \dots, p_4$, every monomial has $0 \le d - k \le 4$:
- $p_0$ ($k=0$): $d \in \{3, 4\} \implies d - 0 \in [3, 4]$;
- $p_1$ ($k=1$): $d \in [3, 5] \implies d - 1 \in [2, 4]$;
- $p_2$ ($k=2$): $d \in [3, 6] \implies d - 2 \in [1, 4]$;
- $p_3$ ($k=3$): $d \in [3, 7] \implies d - 3 \in [0, 4]$;
- $p_4$ ($k=4$): $d \in [4, 8] \implies d - 4 \in [0, 4]$.

Hence for every $n \ge 6$, all occurring indices $m = n - j$ ($0 \le j \le 4$) satisfy $m \ge 2$ (inside the OEIS domain of $a$). Moreover, $\deg p_{\mathrm{inhom}} = 5 < 6$, so $[x^n] p_{\mathrm{inhom}}(x) = 0$ for all $n \ge 6$. Collecting the resulting polynomial coefficients of $a(n-j)$ for $j = 0, \dots, 4$ matches $C_0(n), \dots, C_4(n)$ identically in $\mathbb{Z}[n]$ (verified term-by-term in `verify.py`). Thus $\sum_{j=0}^4 C_j(n) a(n-j) = 0$ for all $n \ge 6$. $\blacksquare$

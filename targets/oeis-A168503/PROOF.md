# Proof of OEIS A168503 D-Finite Recurrence

## Theorem

Let $(a(n))_{n \ge 0}$ be OEIS [A168503](https://oeis.org/A168503), defined by the 3-periodic continued fraction in $\mathbb{Z}[[x]]$:
$$A(x) = \sum_{n=0}^{\infty} a(n) x^n = \cfrac{1}{1 - \cfrac{x}{1 - \cfrac{2x}{1 - \cfrac{3x}{1 - \cfrac{x}{\ddots}}}}}.$$
Then $A(x) = \frac{1 - \sqrt{1 - 12x + 36x^2 - 24x^3}}{6x(1 - x)}$, and for every integer $n \ge 4$ (and $n = 3$ with $a(-1) = 0$),
$$(n+1)a(n) + (-13n+5)a(n-1) + 6(8n-13)a(n-2) + 12(-5n+13)a(n-3) + 12(2n-7)a(n-4) = 0.$$

---

## Proof

### 1. Algebraic equation and radical expression from the continued fraction

Define the operator $T : \mathbb{Z}[[x]] \to \mathbb{Z}[[x]]$ by
$$T(u) := \frac{1}{1 - \cfrac{x}{1 - \cfrac{2x}{1 - 3x u}}} = \frac{1 - 2x - 3x u}{1 - 3x - 3x(1 - x) u}.$$
Because $1 - 3x - 3x(1-x)u = 1 + O(x)$ is a unit in $\mathbb{Z}[[x]]$, $T$ maps $\mathbb{Z}[[x]]$ into $1 + x\mathbb{Z}[[x]]$, and for any $u_1, u_2 \in \mathbb{Z}[[x]]$,
$$T(u_1) - T(u_2) = \frac{6x^3 (u_1 - u_2)}{\bigl(1 - 3x - 3x(1-x)u_1\bigr)\bigl(1 - 3x - 3x(1-x)u_2\bigr)} \in x^3(u_1 - u_2)\mathbb{Z}[[x]].$$
Thus $T$ is a contraction in the $x$-adic topology on $\mathbb{Z}[[x]]$, so its finite continued-fraction convergents $T^m(1)$ converge $x$-adically to its unique fixed point $A(x) = T(A(x)) \in 1 + x\mathbb{Z}[[x]]$.

The fixed-point equation $A(x) = \frac{1 - 2x - 3x A(x)}{1 - 3x - 3x(1-x) A(x)}$ clears to
$$3x(1 - x) A(x)^2 - A(x) + (1 - 2x) = 0.$$
Rearranging gives $\bigl(1 - 6x(1-x)A(x)\bigr)^2 = 1 - 12x(1-x)(1-2x) = 1 - 12x + 36x^2 - 24x^3$. Let
$$y(x) := 1 - 6x(1-x) A(x) = 1 + O(x) \in \mathbb{Z}[[x]], \qquad \Delta(x) := 1 - 12x + 36x^2 - 24x^3,$$
so $y(x)^2 = \Delta(x)$ (and $A(x) = \frac{1 - \sqrt{\Delta(x)}}{6x(1-x)}$).

---

### 2. First-order linear ODE and coefficient extraction

Differentiating $y(x)^2 = \Delta(x)$ in $\mathbb{Q}[[x]]$ gives $2 y(x) y'(x) = \Delta'(x)$, hence $2 \Delta(x) y'(x) = \Delta'(x) y(x)$. Write $P(x) := 3x(1 - x) = 3x - 3x^2$, so $y = 1 - 2 P A$ and $y' = -2 P' A - 2 P A'$. Substituting into $2\Delta y' = \Delta' y$ and dividing by $12$ ($4 \times 3$):
$$\Delta(x) \frac{P(x)}{3}\, A'(x) + \frac{1}{3}\left(\Delta(x) P'(x) - \frac{1}{2}\Delta'(x) P(x)\right) A(x) = -\frac{1}{12}\Delta'(x).$$
Using $\Delta(x) = 1 - 12x + 36x^2 - 24x^3$, $\Delta'(x) = -12 + 72x - 72x^2$, $\frac{P(x)}{3} = x - x^2$, and $\frac{P'(x)}{3} = 1 - 2x$, direct polynomial expansion gives:
- $\Delta(x)(x - x^2) = x - 13x^2 + 48x^3 - 60x^4 + 24x^5$,
- $\Delta(x)(1 - 2x) - (-6 + 36x - 36x^2)(x - x^2) = 1 - 8x + 18x^2 - 24x^3 + 12x^4$,
- $-\frac{1}{12}\Delta'(x) = 1 - 6x + 6x^2$.

Thus $A(x)$ satisfies the first-order linear differential equation
$$x(1 - 13x + 48x^2 - 60x^3 + 24x^4) A'(x) + (1 - 8x + 18x^2 - 24x^3 + 12x^4) A(x) = 1 - 6x + 6x^2.$$
Since the right-hand side has degree $2$, extracting $[x^n]$ for every integer $n \ge 3$ (and hence all $n \ge 4$) gives zero on the right-hand side and, on the left-hand side:
$$\begin{aligned}
0 &= n a(n) - 13(n-1)a(n-1) + 48(n-2)a(n-2) - 60(n-3)a(n-3) + 24(n-4)a(n-4) \\
  &\quad + a(n) - 8a(n-1) + 18a(n-2) - 24a(n-3) + 12a(n-4) \\
  &= (n+1)a(n) + (-13n+5)a(n-1) + 6(8n-13)a(n-2) + 12(-5n+13)a(n-3) + 12(2n-7)a(n-4). \quad \blacksquare
\end{aligned}$$

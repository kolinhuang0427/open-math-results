# Proof of OEIS A157002 D-Finite Recurrence

## Theorem

Let $(a(n))_{n \ge 0}$ be OEIS [A157002](https://oeis.org/A157002), the image of the Catalan numbers $C_k = A000108(k)$ under the Riordan array $\bigl(1 - x,\, x(1 - x^2)\bigr)$, with generating function
$$A(x) = \sum_{n=0}^{\infty} a(n) x^n = (1 - x)\, c\bigl(x(1 - x^2)\bigr) = \frac{1 - \sqrt{1 - 4x(1 - x^2)}}{2x(1 + x)}.$$
Then for every integer $n \ge 4$ (and at $n = 3$ with $a(-1) = 0$),
$$(n+1)a(n) + 3(-n+1)a(n-1) + 2(-2n+1)a(n-2) + 2(2n-7)a(n-3) + 2(2n-7)a(n-4) = 0.$$

---

## Proof

### 1. Algebraic equation from the Riordan definition

Recall $c(u) = \frac{1 - \sqrt{1 - 4u}}{2u} \in \mathbb{Z}[[u]]$ satisfies $u c(u)^2 - c(u) + 1 = 0$. Setting $u = x(1 - x^2)$ gives
$$A(x) = (1 - x)\, c\bigl(x(1 - x^2)\bigr) = (1 - x)\frac{1 - \sqrt{1 - 4x(1 - x^2)}}{2x(1 - x^2)} = \frac{1 - \sqrt{1 - 4x(1 - x^2)}}{2x(1 + x)}.$$
Multiplying $u c(u)^2 - c(u) + 1 = 0$ by $(1 - x)$ and substituting $c(u) = \frac{A(x)}{1 - x}$ (and $1 - x^2 = (1 - x)(1 + x)$) yields the quadratic equation
$$x(1 + x) A(x)^2 - A(x) + (1 - x) = 0.$$
Rearranging gives $1 - 2x(1 + x) A(x) = \sqrt{1 - 4x + 4x^3}$. Set
$$y(x) := 1 - 2x(1 + x) A(x) = 1 + O(x) \in \mathbb{Z}[[x]], \qquad \Delta(x) := 1 - 4x + 4x^3,$$
so that $y(x)^2 = \Delta(x)$ in $\mathbb{Z}[[x]]$.

---

### 2. First-order linear ODE and coefficient extraction

Differentiating $y(x)^2 = \Delta(x)$ gives $2 y(x) y'(x) = \Delta'(x)$, and multiplying by $y(x)$ yields $2 \Delta(x) y'(x) = \Delta'(x) y(x)$. Writing $P(x) := x(1 + x) = x + x^2$, we have $y = 1 - 2 P A$ and $y' = -2 P' A - 2 P A'$. Substituting these into $2\Delta y' = \Delta' y$ gives
$$4 \Delta(x) P(x)\, A'(x) + \bigl(4\Delta(x) P'(x) - 2\Delta'(x) P(x)\bigr) A(x) = -\Delta'(x).$$
Using $\Delta(x) = 1 - 4x + 4x^3$, $\Delta'(x) = -4 + 12x^2$, $P(x) = x + x^2$, and $P'(x) = 1 + 2x$, direct polynomial expansion and division by $4$ yield:
- $\Delta(x) P(x) = (1 - 4x + 4x^3)(x + x^2) = x - 3x^2 - 4x^3 + 4x^4 + 4x^5$,
- $\Delta(x) P'(x) - \frac{1}{2}\Delta'(x) P(x) = (1 - 4x + 4x^3)(1 + 2x) - (-2 + 6x^2)(x + x^2) = 1 - 6x^2 - 2x^3 + 2x^4$,
- $-\frac{1}{4}\Delta'(x) = 1 - 3x^2$.

Thus $A(x)$ satisfies the first-order linear differential equation
$$x(1 - 3x - 4x^2 + 4x^3 + 4x^4) A'(x) + (1 - 6x^2 - 2x^3 + 2x^4) A(x) = 1 - 3x^2.$$
Because the right-hand side has degree $2$, extracting $[x^n]$ for every integer $n \ge 3$ (and hence all $n \ge 4$) gives zero on the right-hand side and, on the left-hand side:
$$\begin{aligned}
0 &= n a(n) - 3(n-1)a(n-1) - 4(n-2)a(n-2) + 4(n-3)a(n-3) + 4(n-4)a(n-4) \\
  &\quad + a(n) - 6a(n-2) - 2a(n-3) + 2a(n-4) \\
  &= (n+1)a(n) + 3(-n+1)a(n-1) + 2(-2n+1)a(n-2) + 2(2n-7)a(n-3) + 2(2n-7)a(n-4). \quad \blacksquare
\end{aligned}$$

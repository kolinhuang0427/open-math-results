# Proof of OEIS A157003 D-Finite Recurrence

## Theorem

Let $(a(n))_{n \ge 0}$ be OEIS [A157003](https://oeis.org/A157003), the image of the Catalan numbers $C_k = A000108(k)$ under the Riordan array $\bigl(1,\, x(1 - x^2)\bigr)$, with generating function
$$A(x) = \sum_{n=0}^{\infty} a(n) x^n = c\bigl(x(1 - x^2)\bigr) = \frac{1 - \sqrt{1 - 4x(1 - x^2)}}{2x(1 - x^2)}.$$
Then:
1. *(4-term recurrence)* For all $n \ge 5$ (and $n = 3, 4$ with $a(k) = 0$ for $k < 0$),
   $$K(n) := (n+1)a(n) - 2(2n-1)a(n-1) - (n+1)a(n-2) + 8(n-2)a(n-3) - 2(2n-7)a(n-5) = 0.$$
2. *(Mathar's conjectured 6-term recurrence)* For all $n \ge 6$ (note at $n = 5$ with $a(-1) = 0$, $K(5) + 5K(4) = 0$ also holds),
   $$(n+1)a(n) + (n+2)a(n-1) + (-21n+29)a(n-2) + (3n-16)a(n-3) + 40(n-3)a(n-4) + 2(-2n+7)a(n-5) + 10(-2n+9)a(n-6) = 0.$$

---

## Proof

### 1. Quadratic equation and first-order linear ODE

Since $c(u) = \frac{1 - \sqrt{1 - 4u}}{2u} \in \mathbb{Z}[[u]]$ satisfies $u c(u)^2 - c(u) + 1 = 0$, substituting $u = P(x) := x(1 - x^2) = x - x^3$ gives
$$P(x) A(x)^2 - A(x) + 1 = 0.$$
Set $y(x) := 1 - 2P(x)A(x) = \sqrt{\Delta(x)} = 1 + O(x) \in \mathbb{Z}[[x]]$, where $\Delta(x) := 1 - 4x + 4x^3$. Differentiating $y(x)^2 = \Delta(x)$ gives $2 y(x) y'(x) = \Delta'(x)$, hence $2 \Delta(x) y'(x) = \Delta'(x) y(x)$ in $\mathbb{Q}[[x]]$. Substituting $y = 1 - 2 P A$ and $y' = -2 P' A - 2 P A'$ and dividing by $4$:
$$\Delta(x) P(x)\, A'(x) + \left(\Delta(x) P'(x) - \frac{1}{2}\Delta'(x) P(x)\right) A(x) = -\frac{1}{4}\Delta'(x).$$
Using $\Delta(x) = 1 - 4x + 4x^3$, $\Delta'(x) = -4 + 12x^2$, $P(x) = x - x^3$, and $P'(x) = 1 - 3x^2$, direct expansion gives:
- $\Delta(x) P(x) = (1 - 4x + 4x^3)(x - x^3) = x - 4x^2 - x^3 + 8x^4 - 4x^6$,
- $\Delta(x) P'(x) - \frac{1}{2}\Delta'(x) P(x) = (1 - 3x^2)\bigl((1 - 4x + 4x^3) + 2(x - x^3)\bigr) = (1 - 3x^2)(1 - 2x + 2x^3) = 1 - 2x - 3x^2 + 8x^3 - 6x^5$,
- $-\frac{1}{4}\Delta'(x) = 1 - 3x^2$.

Hence $A(x)$ satisfies the first-order linear differential equation
$$x(1 - 4x - x^2 + 8x^3 - 4x^5) A'(x) + (1 - 2x - 3x^2 + 8x^3 - 6x^5) A(x) = 1 - 3x^2.$$

---

### 2. Coefficient extraction ($n \ge 5$) and Mathar's recurrence ($n \ge 6$)

Since $\deg(1 - 3x^2) = 2$, extracting $[x^n]$ for every integer $n \ge 3$ (and hence all $n \ge 5$) gives zero on the right-hand side and, on the left-hand side:
$$\begin{aligned}
0 &= n a(n) - 4(n-1)a(n-1) - (n-2)a(n-2) + 8(n-3)a(n-3) - 4(n-5)a(n-5) \\
  &\quad + a(n) - 2a(n-1) - 3a(n-2) + 8a(n-3) - 6a(n-5) \\
  &= (n+1)a(n) - 2(2n-1)a(n-1) - (n+1)a(n-2) + 8(n-2)a(n-3) - 2(2n-7)a(n-5) = K(n).
\end{aligned}$$
Finally, for any $n \ge 6$, both $n \ge 5$ and $n - 1 \ge 5$, so $K(n) + 5K(n-1) = 0$. Expanding $K(n) + 5K(n-1)$ gives:
$$\begin{aligned}
0 &= (n+1)a(n) + \bigl(-2(2n-1) + 5n\bigr)a(n-1) + \bigl(-(n+1) - 10(2n-3)\bigr)a(n-2) \\
  &\quad + \bigl(8(n-2) - 5n\bigr)a(n-3) + 40(n-3)a(n-4) - 2(2n-7)a(n-5) - 10(2n-9)a(n-6) \\
  &= (n+1)a(n) + (n+2)a(n-1) + (-21n+29)a(n-2) + (3n-16)a(n-3) \\
  &\quad + 40(n-3)a(n-4) + 2(-2n+7)a(n-5) + 10(-2n+9)a(n-6). \qquad \blacksquare
\end{aligned}$$

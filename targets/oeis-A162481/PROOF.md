# Proof of OEIS A162481 D-Finite Recurrence

## Theorem

Let $(a(n))_{n \ge 0}$ be OEIS [A162481](https://oeis.org/A162481), defined by the ordinary generating function
$$A(x) = \sum_{n=0}^{\infty} a(n) x^n = \frac{1}{(1-x)^3}\, c\!\left(\frac{x}{(1-x)^3}\right),$$
where $c(u) = \sum_{k=0}^{\infty} C_k u^k = \frac{1 - \sqrt{1 - 4u}}{2u}$ is the Catalan generating function (`A000108`).
Then for every integer $n \ge 4$ (and also at $n = 2, 3$ with $a(k) = 0$ for $k < 0$),
$$(n+1)a(n) + 2(1-4n)a(n-1) + 2(5n-3)a(n-2) + 4(2-n)a(n-3) + (n-3)a(n-4) = 0.$$

---

## Proof

### 1. Algebraic equation and radical expression

Recall that $c(u)$ satisfies $u c(u)^2 - c(u) + 1 = 0$ and $(1 - 2u c(u))^2 = 1 - 4u$ in $\mathbb{Z}[[u]]$. Substituting $u = \frac{x}{(1-x)^3}$ and $c(u) = (1-x)^3 A(x)$ into $u c(u)^2 - c(u) + 1 = 0$ gives
$$x(1-x)^3 A(x)^2 - (1-x)^3 A(x) + 1 = 0 \qquad \Longleftrightarrow \qquad A(x) = \frac{1}{(1-x)^3} + x A(x)^2,$$
and substituting into $1 - 2u c(u) = 1 - 2x A(x)$ gives
$$\bigl(1 - 2x A(x)\bigr)^2 = 1 - \frac{4x}{(1-x)^3} = \frac{1 - 7x + 3x^2 - x^3}{(1-x)^3}.$$
(Also, expanding $A(x) = \sum_{k=0}^{\infty} C_k \frac{x^k}{(1-x)^{3k+3}} = \sum_{k=0}^{\infty} C_k \sum_{m=0}^{\infty} \binom{m+3k+2}{m} x^{k+m}$ gives $a(n) = \sum_{k=0}^{n} \binom{n+2k+2}{n-k} C_k$.)

---

### 2. First-order linear ODE and coefficient extraction

Set $z(x) := 1 - 2x A(x) \in \mathbb{Z}[[x]]$, $Q(x) := 1 - 7x + 3x^2 - x^3$, and $R(x) := (1 - x)^3$. From $R(x) z(x)^2 = Q(x)$, differentiating in $\mathbb{Q}[[x]]$ gives
$$2 R(x) z(x) z'(x) + R'(x) z(x)^2 = Q'(x).$$
Multiplying by $R(x)$ and substituting $R(x) z(x)^2 = Q(x)$ (valid in $\mathbb{Q}[[x]]$, dividing by the unit $z(x) = 1 + O(x)$) yields
$$2 Q(x) R(x)\, z'(x) = \bigl(Q'(x) R(x) - Q(x) R'(x)\bigr)\, z(x).$$
Now substitute $z(x) = 1 - 2x A(x)$ and $z'(x) = -2 A(x) - 2x A'(x)$:
$$4x Q(x) R(x)\, A'(x) + \Bigl(4 Q(x) R(x) - 2x\bigl(Q'(x) R(x) - Q(x) R'(x)\bigr)\Bigr) A(x) = Q(x) R'(x) - Q'(x) R(x).$$
Notice that $R(x) = (1-x)^3$ and $R'(x) = -3(1-x)^2$, so $(1-x)^2$ divides both sides. Dividing out $4(1-x)^2$ in $\mathbb{Q}[[x]]$:
- Left coefficient of $A'(x)$:
  $$x(1 - x) Q(x) = x(1 - x)(1 - 7x + 3x^2 - x^3) = x(1 - 8x + 10x^2 - 4x^3 + x^4).$$
- Left coefficient of $A(x)$: using $Q'(x)(1-x) - Q(x)(-3) = (-7 + 6x - 3x^2)(1-x) + 3(1 - 7x + 3x^2 - x^3) = -4 - 8x = -4(1 + 2x)$,
  $$(1-x)Q(x) - \frac{x}{2}\bigl(Q'(x)(1-x) + 3 Q(x)\bigr) = (1 - 8x + 10x^2 - 4x^3 + x^4) + 2x(1 + 2x) = 1 - 6x + 14x^2 - 4x^3 + x^4.$$
- Right-hand side:
  $$-\frac{1}{4}\bigl(Q'(x)(1-x) + 3 Q(x)\bigr) = 1 + 2x.$$

Thus $A(x)$ satisfies the first-order linear ODE
$$x(1 - 8x + 10x^2 - 4x^3 + x^4) A'(x) + (1 - 6x + 14x^2 - 4x^3 + x^4) A(x) = 1 + 2x.$$
Since the right-hand side has degree $1$, extracting $[x^n]$ for any integer $n \ge 2$ (and hence all $n \ge 4$, where all $a(n-4)$ have index $\ge 0$) gives zero on the right-hand side and, on the left-hand side:
$$\begin{aligned}
0 &= n a(n) - 8(n-1)a(n-1) + 10(n-2)a(n-2) - 4(n-3)a(n-3) + (n-4)a(n-4) \\
  &\quad + a(n) - 6a(n-1) + 14a(n-2) - 4a(n-3) + a(n-4) \\
  &= (n+1)a(n) + (2 - 8n)a(n-1) + (10n - 6)a(n-2) + (8 - 4n)a(n-3) + (n - 3)a(n-4) \\
  &= (n+1)a(n) + 2(1 - 4n)a(n-1) + 2(5n - 3)a(n-2) + 4(2 - n)a(n-3) + (n - 3)a(n-4). \quad \blacksquare
\end{aligned}$$

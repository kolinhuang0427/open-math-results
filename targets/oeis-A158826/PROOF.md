# Proof of Mathar's 2021 D-Finite Recurrence Conjecture for OEIS A158826

## Statement
Let $C(x) = \sum_{m=0}^{\infty} \frac{1}{m+1}\binom{2m}{m} x^m \in \mathbb{Z}[[x]]$ be the Catalan generating function, let $f(x) := x C(x) = \sum_{m=1}^{\infty} \frac{1}{m}\binom{2m-2}{m-1} x^m \in \mathbb{Z}[[x]]$, and let
$$y(x) = \sum_{n=1}^{\infty} a(n) x^n := f(f(f(x))) \in \mathbb{Z}[[x]]$$
be the ordinary generating function of OEIS **A158826** (offset `1`, so $a(0) = 0$, $a(1) = 1$, $a(2) = 3$, $a(3) = 12$, ...).

**Theorem (R. J. Mathar's Conjecture, Aug 30 2021).** For every integer $n \ge 6$,
$$\begin{aligned}
&1053 n(n-1)(n-2)(n-3)\,a(n) - 36(n-1)(n-2)(n-3)(634n - 1367)\,a(n-1) \\
&\quad + 24(n-2)(n-3)(7966n^2 - 43500n + 61181)\,a(n-2) \\
&\quad - 8(n-3)(96128n^3 - 957424n^2 + 3221878n - 3665189)\,a(n-3) \\
&\quad + 16(91904n^4 - 1446528n^3 + 8575792n^2 - 22703688n + 22652013)\,a(n-4) \\
&\quad - 256(8n - 35)(8n - 41)(8n - 39)(8n - 37)\,a(n-5) = 0.
\end{aligned}$$

---

## Proof

Work in the formal power series ring $\mathbb{Q}[[x]]$ (indeed $\mathbb{Z}[[x]]$).

### Step 1: Algebraic equation $P_3(y(x)) = x$
Since $C(x) = 1 + x C(x)^2$, multiplying by $x$ gives $f(x) = x + f(x)^2$, i.e., $F(f(x)) = x$, where $F(t) := t(1 - t) \in \mathbb{Z}[t]$. (In particular, $f$ is the unique compositional inverse of $F$ in $x\mathbb{Z}[[x]]$.)
Applying $F$ three times to $y(x) = f(f(f(x)))$ in $x\mathbb{Z}[[x]]$ yields
$$P_3(y(x)) = x,$$
where $P_3(y) := F(F(F(y))) \in \mathbb{Z}[y]$ is the degree-$8$ polynomial
$$P_3(y) = -y^8 + 4y^7 - 8y^6 + 10y^5 - 9y^4 + 6y^3 - 3y^2 + y.$$
(Equivalently, $1 - 4F(t) = (1 - 2t)^2$ gives $1 - 2f(u) = \sqrt{1 - 4u}$ and $1 - 4f(u) = -1 + 2\sqrt{1 - 4u}$, yielding Irwin's nested-radical formula $y(x) = \frac{1}{2}\bigl(1 - \sqrt{-1 + 2\sqrt{-1 + 2\sqrt{1 - 4x}}}\bigr)$.)

### Step 2: Order-4 inhomogeneous linear ODE for $y(x)$
Define the polynomials in $\mathbb{Z}[x]$:
$$\begin{aligned}
c_0(x) &= 120(16x - 29), \\
c_1(x) &= -240(16x - 29), \\
c_2(x) &= 24(96256x^2 - 101872x + 18577), \\
c_3(x) &= 24(446464x^3 - 503584x^2 + 156290x - 14637), \\
c_4(x) &= 4(4x - 1)(458752x^3 - 460672x^2 + 127080x - 10521), \\
c_5(x) &= (4x - 1)^2(16x - 9)(16x - 3)(256x - 39).
\end{aligned}$$
Since $P_3(y(x)) = x$, differentiating four times with respect to $x$ in $\mathbb{Q}[[x]]$ gives:
$$\begin{aligned}
P_3'(y)\, y' &= 1, \\
P_3'(y)^3\, y'' &= -P_3''(y), \\
P_3'(y)^5\, y''' &= 3 P_3''(y)^2 - P_3'(y) P_3'''(y), \\
P_3'(y)^7\, y'''' &= \bigl(3 P_3''(y)^2 - P_3'(y) P_3'''(y)\bigr)' P_3'(y) - 5\bigl(3 P_3''(y)^2 - P_3'(y) P_3'''(y)\bigr) P_3''(y),
\end{aligned}$$
where $'$ on $P_3$ denotes $\frac{d}{dy}$ and $'$ on $y$ denotes $\frac{d}{dx}$.
Define the univariate polynomial $U(y) \in \mathbb{Z}[y]$ by clearing $P_3'(y)^7$ and substituting $x = P_3(y)$:
$$U(y) := c_0(P_3(y)) P_3'(y)^7 + c_1(P_3(y)) y P_3'(y)^7 + c_2(P_3(y)) P_3'(y)^6 - c_3(P_3(y)) P_3''(y) P_3'(y)^4 + c_4(P_3(y)) N_3(y) P_3'(y)^2 + c_5(P_3(y)) N_4(y),$$
where $N_3 = 3(P_3'')^2 - P_3' P_3'''$ and $N_4 = N_3' P_3' - 5 N_3 P_3''$.
Exact integer polynomial expansion (verified in `verify.py`) shows that
$$U(y) = 0 \qquad \text{identically in } \mathbb{Z}[y].$$
Evaluating at $y = y(x)$ (so $P_3(y(x)) = x$) yields
$$P_3'(y(x))^7 \Bigl(c_0(x) + c_1(x) y(x) + c_2(x) y'(x) + c_3(x) y''(x) + c_4(x) y'''(x) + c_5(x) y''''(x)\Bigr) = 0 \qquad \text{in } \mathbb{Q}[[x]].$$
Because $y(x) = x + O(x^2)$ and $P_3'(y) = 1 - 6y + O(y^2)$, we have $P_3'(y(x)) = 1 - 6x + O(x^2) \ne 0$ (indeed a unit in $\mathbb{Z}[[x]]$). Cancelling $P_3'(y(x))^7$ in $\mathbb{Q}[[x]]$ proves the exact differential equation
$$c_0(x) + c_1(x) y(x) + c_2(x) y'(x) + c_3(x) y''(x) + c_4(x) y'''(x) + c_5(x) y''''(x) = 0.$$

### Step 3: Extraction of Mathar's recurrence
For any integer $n \ge 6$, we have $n - 4 \ge 2$, and since $\deg c_0 = 1$, $[x^{n-4}] c_0(x) = 0$.
Extracting $[x^{n-4}]$ from $\sum_{d=0}^4 c_{d+1}(x) y^{(d)}(x) = -c_0(x)$ uses, for all $n \ge 6$, $0 \le d \le 4$, and $0 \le r \le d + 1$,
$$[x^{n-4}] \bigl(x^r y^{(d)}(x)\bigr) = \Bigl(\prod_{s=1}^d (n - 4 - r + s)\Bigr) a(n - (r + 4 - d)),$$
with $a(m) = 0$ for $m \le 0$: if $n - 4 - r \ge 0$, both sides equal $[x^{n-4-r}] y^{(d)}(x) = \frac{(n-4-r+d)!}{(n-4-r)!} a(n-4-r+d)$; if $n - 4 - r < 0$, then the LHS is $0$ (as $r > n - 4$), while $r \le d + 1$ and $n \ge 6$ imply $n - 4 - r + 1 \le 0 < 1 \le n - 4 - r + d$, so the factor $0$ appears in the product and the RHS is also $0$.
Because $c_{d+1}(x)$ has degree $d + 1$, each index $j := r + 4 - d$ lies in $\{0, 1, 2, 3, 4, 5\}$ (with $n - j \ge 1$ for $n \ge 6$). Collecting the degree-$4$ polynomial coefficients of $a(n-j)$ for $j = 0, \dots, 5$ and negating gives identically (verified explicitly at five points in `verify.py`):
- $j = 0$: $1053 n(n-1)(n-2)(n-3)$;
- $j = 1$: $-36(n-1)(n-2)(n-3)(634n - 1367)$;
- $j = 2$: $24(n-2)(n-3)(7966n^2 - 43500n + 61181)$;
- $j = 3$: $-8(n-3)(96128n^3 - 957424n^2 + 3221878n - 3665189)$;
- $j = 4$: $16(91904n^4 - 1446528n^3 + 8575792n^2 - 22703688n + 22652013)$;
- $j = 5$: $-256(8n - 35)(8n - 41)(8n - 39)(8n - 37)$.

Thus Mathar's 2021 recurrence holds for all integers $n \ge 6$. $\blacksquare$

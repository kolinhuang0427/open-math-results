# Proof of Subsequence Periodicity, Exact Growth Factors, and a Finite-Time Algorithm for OEIS A374602

We prove both conjectures stated in OEIS `A374602` (rev. 31) and its companion entries `A377290` (rev. 7) and `A377291` (rev. 7) for every nonsquare integer $d \ge 2$ ($d = \mathrm{A000037}(n)$, $n \ge 1$):

1. **(Strict Global Periodicity and Geometric Growth)** Every row $n$ partitions from the very first term $k = 1$ (with zero exceptional terms) into $p(n) = \mathrm{A377290}(n) \ge 1$ subsequences $\{T(n, mp + j)\}_{m \ge 0}$ ($1 \le j \le p(n)$), where each subsequence has constant parameter $c$, satisfies the exact order-2 linear recurrence
   $$T(n, (m+2)p + j) = A_r \, T(n, (m+1)p + j) - T(n, mp + j) \qquad (m \ge 0)$$
   with $A_r = \mathrm{A377291}(n) \in \mathbb{Z}_{\ge 3}$, and has common asymptotic growth factor
   $$\lim_{k \to \infty} \frac{T(n, k + p(n))}{T(n, k)} = g(n) = \frac{A_r + \sqrt{A_r^2 - 4}}{2} = \gamma, \qquad g(n) + g(n)^{-1} = A_r.$$
   Moreover, $p(n)$ and $g(n)$ are minimal with these properties.
2. **(Explicit Finite-Time Algorithm)** We give a finite-time, terminating algorithm using only integer continued fractions and modular arithmetic that computes $g(n)$, $p(n)$, and all initial orbit seeds $(X_{0,j}, Y_{0,j})$ ($1 \le j \le p(n)$), from which every row value $T(n, mp+j)$ is generated directly without searching candidate integers $t$ until a pattern emerges.

---

## 1. Reduction to a Constrained Generalized Pell System

Fix a nonsquare integer $d \ge 2$ ($d = \mathrm{A000037}(n)$). By definition, row $n$ of `A374602` consists of all positive integers $t$ (in strictly increasing order) for which there exist integers $b \ge 1$ and $1 \le c \le d - 1$ such that
$$t^2 = (d - c) b^2 + c (b + 1)^2 = d b^2 + c(2b + 1).$$

**Lemma 1 (Uniqueness of $(b, c)$ and Pell bijection).**
1. For any such solution $(t, b, c)$, we have $d b^2 < t^2 < d(b+1)^2$, so $b = \lfloor \sqrt{t^2/d} \rfloor$ and $c = (t^2 - d b^2)/(2b + 1)$ are uniquely determined by $t$. In particular, distinct pairs $(b, c)$ never produce the same $t$.
2. Define the solution set
   $$\mathcal{S}_d := \bigl\{ (X, Y) \in \mathbb{Z}^2 : \exists c \in \{1, \dots, d-1\} \text{ such that } X \equiv c \pmod d \text{ and } X^2 - d Y^2 = -c(d-c) \bigr\},$$
   and its positive admissible subset $\mathcal{S}_d^+ := \{ (X, Y) \in \mathcal{S}_d : X \ge d + 1,\ Y \ge 1 \}$. Then the map $(t, b, c) \mapsto (X, Y) := (d b + c,\ t)$ is a bijection onto $\mathcal{S}_d^+$, with inverse $(X, Y) \mapsto (Y,\ \lfloor X/d \rfloor,\ X \bmod d)$.

*Proof.*
(1) Since $1 \le c \le d - 1$ and $b \ge 1$, $0 < c(2b + 1) < d(2b + 1)$, so $d b^2 < t^2 < d b^2 + d(2b + 1) = d(b+1)^2$. Taking square roots gives $b < t/\sqrt{d} < b+1$, hence $b = \lfloor \sqrt{t^2/d}\rfloor$ and $c = (t^2 - d b^2)/(2b+1)$.
(2) Multiplying $Y^2 = d b^2 + c(2b+1)$ by $d$ and setting $X = d b + c \ge d + 1$ gives
$$X^2 - d Y^2 = (d b + c)^2 - d(d b^2 + 2 c b + c) = c^2 - c d = -c(d-c),$$
and $X \equiv c \pmod d$. Conversely, if $(X, Y) \in \mathcal{S}_d^+$, write $X = d b + c$ with $c = X \bmod d \in \{1, \dots, d-1\}$ and $b = \lfloor X/d \rfloor \ge 1$. Then $d Y^2 = X^2 + c(d-c) = d^2 b^2 + 2 d b c + c d$, so dividing by $d$ yields $Y^2 = d b^2 + c(2b+1) = (d-c)b^2 + c(b+1)^2$. $\square$

For $(X, Y) \in \mathcal{S}_d$, define its real embedding $z(X, Y) := X + Y\sqrt{d}$.

**Lemma 2 (Exact threshold $z > 2d$).**
For $(X, Y) \in \mathcal{S}_d$, we have
$$(X, Y) \in \mathcal{S}_d^+ \iff z(X, Y) > 2d.$$
Moreover, $z(X, Y) = 2d$ never occurs.

*Proof.*
First, $z(X, Y) = 2d$ with $Y \in \mathbb{Z}$ implies $Y\sqrt{d} = 2d - X \in \mathbb{Z}$, forcing $Y = 0$ (since $d$ is nonsquare), which contradicts $X^2 - d \cdot 0^2 = -c(d-c) < 0$.

If $(X, Y) \in \mathcal{S}_d^+$, then $X \ge d + 1$ and $d Y^2 = X^2 + c(d-c) \ge (d+1)^2 + (d-1) = d^2 + 3d > d^2$, so $Y > \sqrt{d}$ and $z(X, Y) = X + Y\sqrt{d} > (d + 1) + d = 2d + 1 > 2d$.

Conversely, suppose $(X, Y) \in \mathcal{S}_d \setminus \mathcal{S}_d^+$.
- If $Y \le 0$, then $X^2 - d Y^2 = -c(d-c) < 0$ implies $|X| < |Y|\sqrt{d} = (-Y)\sqrt{d}$, so $z(X, Y) = X - (-Y)\sqrt{d} < 0 < 2d$.
- If $Y \ge 1$ and $X \le d$, since $X \equiv c \in \{1, \dots, d-1\} \pmod d$, either $1 \le X \le d - 1$ or $X \le -1$.
  - If $1 \le X \le d - 1$, then $X = c$, so $d Y^2 = c^2 + c(d-c) = c d \implies Y^2 = c < d \implies Y < \sqrt{d}$, whence $z(X, Y) = c + Y\sqrt{d} < d + d = 2d$.
  - If $X \le -1$, write $K = -X \ge 1$. Since $Y\sqrt{d} = \sqrt{K^2 + c(d-c)}$,
    $$z(X, Y) = \sqrt{K^2 + c(d-c)} - K = \frac{c(d-c)}{\sqrt{K^2 + c(d-c)} + K} < \sqrt{c(d-c)} \le \frac{d}{2} < 2d. \quad \square$$

---

## 2. The Multiplier Unit $\gamma$ and Its Bijective Action on $\mathcal{S}_d$

Let $\mathcal{O}_d$ be the quadratic order
$$\mathcal{O}_d := \begin{cases} \mathbb{Z}\!\left[\frac{1+\sqrt{d}}{2}\right] & \text{if } d \equiv 1 \pmod 4, \\ \mathbb{Z}[\sqrt{d}] & \text{if } d \not\equiv 1 \pmod 4. \end{cases}$$
Every norm-$+1$ unit $> 1$ in $\mathcal{O}_d$ has the form $\varepsilon = \frac{A + B\sqrt{d}}{2}$ with integers $A, B \ge 1$ satisfying $A^2 - d B^2 = 4$ (and $2 \mid A, 2 \mid B$ when $d \not\equiv 1 \pmod 4$; when $d \equiv 1 \pmod 4$, $A^2 - B^2 \equiv A^2 - d B^2 = 4 \equiv 0 \pmod 4$ automatically forces $A \equiv B \pmod 2$). Since $d$ is nonsquare, Pell's equation $u^2 - d v^2 = 1$ has positive solutions, so the set of norm-$+1$ units $> 1$ in $\mathcal{O}_d$ is nonempty and discrete; let $\varepsilon_0 = \frac{A_1 + B_1\sqrt{d}}{2} > 1$ be its smallest element. Every norm-$+1$ unit $> 1$ in $\mathcal{O}_d$ is a power $\varepsilon_0^k$ ($k \ge 1$).

**Lemma 3 (Integrality for $d \equiv 1 \pmod 4$).**
If $d \equiv 1 \pmod 4$, then every $(X, Y) \in \mathcal{S}_d$ satisfies $X \equiv Y \pmod 2$, equivalently $\frac{X + Y\sqrt{d}}{2} \in \mathcal{O}_d$.

*Proof.* Since $d$ is odd, $c(d-c)$ is even for every $c$. Reducing $X^2 - d Y^2 = -c(d-c)$ modulo $4$ with $d \equiv 1 \pmod 4$ gives $X^2 - Y^2 \equiv -c(d-c) \pmod 4$. Because $X^2 - Y^2 \bmod 4 \in \{0, 1, 3\}$ can never equal $2 \pmod 4$, we must have $X^2 - Y^2 \equiv 0 \pmod 4$, forcing $X \equiv Y \pmod 2$. Hence $\frac{X + Y\sqrt{d}}{2} = \frac{X-Y}{2} + Y\frac{1+\sqrt{d}}{2} \in \mathcal{O}_d$. $\square$

Now define $r \in \{1, 2\}$ to be the least positive integer such that $\gamma := \varepsilon_0^r = \frac{A_r + B_r\sqrt{d}}{2}$ satisfies
$$\begin{cases} A_r \equiv 2 \pmod d & \text{if } d \equiv 1 \pmod 4, \\ A_r / 2 \equiv 1 \pmod d & \text{if } d \not\equiv 1 \pmod 4. \end{cases}$$

**Proposition 4 (Existence of $r \in \{1, 2\}$ and $\gamma$-invariance of $\mathcal{S}_d$).**
1. Such $r \in \{1, 2\}$ always exists, and $A_r = \gamma + \gamma^{-1} \ge 3$ with $\lceil \gamma \rceil = \mathrm{round}(\gamma) = A_r$.
2. The linear map $T_\gamma(X, Y) := \bigl(\frac{A_r X + d B_r Y}{2},\ \frac{B_r X + A_r Y}{2}\bigr)$ (corresponding to multiplication by $\gamma$ on $X + Y\sqrt{d}$) and its inverse $T_{\gamma^{-1}}(X, Y) = \bigl(\frac{A_r X - d B_r Y}{2},\ \frac{A_r Y - B_r X}{2}\bigr)$ map $\mathcal{S}_d \to \mathcal{S}_d$ bijectively, preserve $c = X \bmod d$, preserve the half-plane $\{Y \ge 1\} = \{z > 0\}$, and scale $z$ by $\gamma^{\pm 1}$.

*Proof.*
(1) From $A_1^2 - d B_1^2 = 4$, we have $A_1^2 \equiv 4 \pmod d$. If $d \equiv 1 \pmod 4$, then $\varepsilon_0^2 = \frac{(A_1^2 - 2) + A_1 B_1\sqrt{d}}{2}$ has trace $A_2 = A_1^2 - 2 \equiv 4 - 2 = 2 \pmod d$. If $d \not\equiv 1 \pmod 4$, write $A_1 = 2 u_1$; then $u_1^2 \equiv 1 \pmod d$, so $\varepsilon_0^2$ has $A_2 / 2 = u_2 = 2 u_1^2 - 1 \equiv 1 \pmod d$. Hence $r \in \{1, 2\}$ exists. Since $A_r^2 = d B_r^2 + 4 \ge 2 \cdot 1 + 4 = 6$, we have $A_r \ge 3$, so $\gamma = \frac{A_r + \sqrt{A_r^2 - 4}}{2} \ge \frac{3 + \sqrt{5}}{2} > 2$, hence $0 < \gamma^{-1} < \frac{1}{2}$, which implies $\gamma = A_r - \gamma^{-1} \in (A_r - \frac{1}{2}, A_r)$ and $\lceil \gamma \rceil = \mathrm{round}(\gamma) = A_r$.

(2) Let $(X, Y) \in \mathcal{S}_d$ and $(X', Y') = T_{\gamma^{\pm 1}}(X, Y)$.
- If $d \not\equiv 1 \pmod 4$, write $A_r = 2 u_r, B_r = 2 v_r \in 2\mathbb{Z}$; then $X' = u_r X \pm d v_r Y \in \mathbb{Z}$ and $Y' = u_r Y \pm v_r X \in \mathbb{Z}$, with $X' \equiv u_r X \equiv X \pmod d$.
- If $d \equiv 1 \pmod 4$, by Lemma 3, $\frac{X+Y\sqrt{d}}{2} \in \mathcal{O}_d$, so $\gamma^{\pm 1} \frac{X+Y\sqrt{d}}{2} = \frac{X'+Y'\sqrt{d}}{2} \in \mathcal{O}_d$, meaning $X', Y' \in \mathbb{Z}$. Moreover $2 X' = A_r X \pm d B_r Y \equiv 2 X \pmod d$; since $d$ is odd, $\gcd(2, d) = 1$, so $X' \equiv X \pmod d$.
Since $\mathrm{Nm}(\gamma^{\pm 1}) = 1$, $X'^2 - d Y'^2 = X^2 - d Y^2 = -c(d-c)$, so $(X', Y') \in \mathcal{S}_d$ with the same $c$. Finally, since $X^2 < d Y^2$, we have $z(X, Y) = X + Y\sqrt{d} > 0 \iff Y \ge 1$; since $\gamma^{\pm 1} > 0$ and $z(X', Y') = \gamma^{\pm 1} z(X, Y)$, $T_{\gamma^{\pm 1}}$ preserves $\{Y \ge 1\}$. $\square$

---

## 3. Finiteness, Order Preservation, and Strict Global Periodicity

Let $\mathcal{S}_d^{>0} := \mathcal{S}_d \cap \{Y \ge 1\} = \mathcal{S}_d \cap \{z > 0\}$. By Proposition 4, $\mathcal{S}_d^{>0}$ decomposes into disjoint $\gamma$-orbits. Since multiplication by $\gamma > 1$ scales $z(X, Y) > 0$ by $\gamma$, every $\gamma$-orbit in $\mathcal{S}_d^{>0}$ intersects the fundamental window
$$W_0 := \bigl\{ (X, Y) \in \mathcal{S}_d^{>0} : 2d < z(X, Y) < 2d\gamma \bigr\}$$
in a unique representative $(X_0, Y_0)$. By Lemma 2, $W_0 \subset \mathcal{S}_d^+$, and $\mathcal{S}_d^+$ is the disjoint union of the shifted windows
$$W_m := T_\gamma^m(W_0) = \bigl\{ (X, Y) \in \mathcal{S}_d^+ : 2d\gamma^m < z(X, Y) < 2d\gamma^{m+1} \bigr\} \qquad (m = 0, 1, 2, \dots).$$

Moreover, $(1, 1) \in \mathcal{S}_d^{>0}$ (with $c = 1$: $1^2 - d \cdot 1^2 = -(d-1)$), so $W_0$ is nonempty ($p := |W_0| \ge 1$). Furthermore, for any $(X, Y) \in W_0$, we have $Y\sqrt{d} - X = \frac{c(d-c)}{X + Y\sqrt{d}} < \frac{d^2/4}{2d} = \frac{d}{8}$ and $X + Y\sqrt{d} < 2d\gamma$, so $2Y\sqrt{d} < 2d\gamma + \frac{d}{8}$ and $0 < X < Y\sqrt{d}$; hence $W_0$ is finite ($1 \le p < \infty$).

**Theorem 5 (Monotonicity and Strict Global Periodicity).**
For any two admissible solutions $(X_1, Y_1), (X_2, Y_2) \in \mathcal{S}_d^+$:
1. $Y_1 < Y_2 \implies X_1 < X_2 \implies z(X_1, Y_1) < z(X_2, Y_2)$.
2. $Y_1 < Y_2 \implies Y_1' < Y_2'$, where $(X_i', Y_i') = T_\gamma(X_i, Y_i)$.

Consequently, if the $p = |W_0|$ points of $W_0$ are ordered as $Y_{0,1} < Y_{0,2} < \dots < Y_{0,p}$ with parameters $c_j := X_{0,j} \bmod d$, then for EVERY $m \ge 0$, the elements of $W_m$ satisfy
$$Y_{m,1} < Y_{m,2} < \dots < Y_{m,p} < Y_{m+1,1},$$
so $T(n, mp + j) = Y_{m,j}$ for all $m \ge 0$ and $1 \le j \le p$. In particular:
- (Periodicity from $k=1$) $c(T(n, k + p)) = c(T(n, k))$ for all $k \ge 1$, with zero exceptional solutions.
- (Exact linear recurrence and growth) For every $m \ge 0$ and $1 \le j \le p$,
  $$T(n, (m+2)p + j) = A_r \, T(n, (m+1)p + j) - T(n, mp + j), \qquad \lim_{k \to \infty} \frac{T(n, k + p)}{T(n, k)} = \gamma.$$

*Proof.*
Let $b_i = \lfloor X_i / d \rfloor \ge 1$ and $c_i = X_i \bmod d \in \{1, \dots, d-1\}$. By Lemma 1(1), $b_i = \lfloor \sqrt{Y_i^2 / d} \rfloor$ is non-decreasing in $Y_i$, so $Y_1 < Y_2$ implies $b_1 \le b_2$.
- If $b_1 < b_2$, then $b_2 \ge b_1 + 1$, so $X_2 = d b_2 + c_2 > d(b_1 + 1) > d b_1 + c_1 = X_1$.
- If $b_1 = b_2 = b$, then $d b^2 + c_1(2b+1) = Y_1^2 < Y_2^2 = d b^2 + c_2(2b+1)$ implies $c_1 < c_2$, so $X_1 = d b + c_1 < d b + c_2 = X_2$.
Thus $Y_1 < Y_2 \implies X_1 < X_2$, which immediately implies $z(X_1, Y_1) = X_1 + Y_1\sqrt{d} < X_2 + Y_2\sqrt{d} = z(X_2, Y_2)$ and $Y_1' = \frac{B_r X_1 + A_r Y_1}{2} < \frac{B_r X_2 + A_r Y_2}{2} = Y_2'$ (since $A_r, B_r > 0$).

Because $Y_1 < Y_2 \implies z_1 < z_2$ on $\mathcal{S}_d^+$, sorting $\mathcal{S}_d^+$ by $Y$ coincides with sorting $\mathcal{S}_d^+$ by $z$. Since $W_0 \subset (2d, 2d\gamma)$, $W_1 \subset (2d\gamma, 2d\gamma^2)$, etc., every element of $W_m$ precedes every element of $W_{m+1}$, and inside each $W_m = T_\gamma^m(W_0)$ the $p$ elements appear in the exact same order $Y_{m,1} < \dots < Y_{m,p}$ with $c(Y_{m,j}) = c_j$ by Proposition 4(2). Since $\gamma^2 - A_r \gamma + 1 = 0$ and $\gamma^{-2} - A_r \gamma^{-1} + 1 = 0$, the representation $Y_{m,j} = \frac{1}{2\sqrt{d}}(\gamma^m z_{0,j} - \gamma^{-m} \bar{z}_{0,j})$ yields $Y_{m+2,j} = A_r Y_{m+1,j} - Y_{m,j}$ for all $m \ge 0$ and $\lim_{m \to \infty} Y_{m+1,j}/Y_{m,j} = \gamma$. $\square$

**Proposition 6 (Minimality of $p$ and $\gamma$, confirming `A377290` and `A377291`).**
No positive integer $p' < p$ can simultaneously satisfy $c(T(n, k+p')) = c(T(n, k))$ for all $k \ge 1$ and $\lim_{k \to \infty} T(n, k+p')/T(n, k) = g'$ for a constant $g' > 1$. Thus $\mathrm{A377290}(n) = p$ and $\mathrm{A377291}(n) = A_r$.

*Proof.*
Suppose $p' \le p$ satisfies both conditions. Multiplying $p$ consecutive shifts gives
$$(g')^p = \lim_{k \to \infty} \prod_{i=0}^{p-1} \frac{T(n, k + (i+1)p')}{T(n, k + i p')} = \lim_{k \to \infty} \frac{T(n, k + p \cdot p')}{T(n, k)} = \gamma^{p'},$$
so $g' = \gamma^{p'/p} \le \gamma$. Let $(X_{0,j_0}, Y_{0,j_0})$ be the unique representative in $W_0$ of the $\gamma$-orbit of $(1, 1) \in \mathcal{S}_d^{>0}$, so that $z_{0, j_0} = \gamma^s (1 + \sqrt{d})$ for some integer $s \ge 1$ (since $z(1,1) = 1+\sqrt{d} < 2d$ as $d \ge 2$).
Now let $k_m = m p + j_0$. By the pigeonhole principle, there exist fixed $j_1 \in \{1, \dots, p\}$ and $t \in \mathbb{Z}_{\ge 0}$ such that $k_m + p' = (m+t)p + j_1$ for infinitely many $m$. Along those $m$, $c_{j_1} = c(T(n, k_m + p')) = c(T(n, k_m)) = c_{j_0} = 1$, and
$$g' = \lim_{m \to \infty} \frac{Y_{m+t, j_1}}{Y_{m, j_0}} = \frac{\gamma^t z_{0, j_1}}{z_{0, j_0}} \in \mathbb{Q}(\sqrt{d}).$$
Since $\mathrm{Nm}(z_{0, j_1}) = \mathrm{Nm}(z_{0, j_0}) = -(d-1) \neq 0$ and $\mathrm{Nm}(\gamma) = 1$, we obtain $\mathrm{Nm}(g') = +1$. Writing $z_{0, j_0} = \gamma^s(1+\sqrt{d})$ ($s \ge 1$) and multiplying by $\gamma^{-s}$ gives
$$g'(1 + \sqrt{d}) = \gamma^{t-s}(X_{0, j_1} + Y_{0, j_1}\sqrt{d}) =: X^* + Y^*\sqrt{d} \in \mathcal{S}_d$$
with $X^* \equiv 1 \pmod d$ (Proposition 4(2)). Moreover, since $(g')^p = \gamma^{p'} \in \mathcal{O}_d$, $g'$ is an algebraic integer in $K = \mathbb{Q}(\sqrt{d})$, so $g' \in \mathcal{O}_K^\times$ with norm $+1$. Let $d = f^2 d_0$ with $d_0$ squarefree ($f \ge 1$):
- If $d_0 \not\equiv 1 \pmod 4$, then $\mathcal{O}_K = \mathbb{Z}[\sqrt{d_0}]$, so $g' = U + \frac{V}{f}\sqrt{d}$ ($U, V \in \mathbb{Z}$). Then $Y^* = U + \frac{V}{f} \in \mathbb{Z}$ forces $f \mid V$, so $g' = U + v\sqrt{d} \in \mathbb{Z}[\sqrt{d}] = \mathcal{O}_d^\times$, and $X^* = U + d v \equiv U \pmod d \implies U \equiv 1 \pmod d$.
- If $d_0 \equiv 1 \pmod 4$, then $\mathcal{O}_K = \mathbb{Z}[\frac{1+\sqrt{d_0}}{2}]$, so $g' = \frac{A}{2} + \frac{B}{2f}\sqrt{d}$ ($A, B \in \mathbb{Z}$, $A \equiv B \pmod 2$). Then $2 Y^* = A + \frac{B}{f} \in \mathbb{Z}$ forces $f \mid B$; write $B' = B/f \in \mathbb{Z}$, so $A^2 - d B'^2 = 4$. If $d \not\equiv 1 \pmod 4$, then $f$ is even, so $B = f B'$ is even, hence $A$ is even (as $A \equiv B \pmod 2$), and $Y^* = \frac{A}{2} + \frac{B'}{2} \in \mathbb{Z}$ forces $B'$ even, so $g' \in \mathbb{Z}[\sqrt{d}] = \mathcal{O}_d^\times$ with $\frac{A}{2} \equiv X^* \equiv 1 \pmod d$. If $d \equiv 1 \pmod 4$, then $f$ is odd, so $A \equiv B = f B' \equiv B' \pmod 2$, giving $g' \in \mathcal{O}_d^\times$ with $A \equiv A + d B' = 2 X^* \equiv 2 \pmod d$.
In every case, $g' > 1$ is a norm-$+1$ unit in $\mathcal{O}_d^\times$ satisfying the exact congruence defining $\gamma$. By minimality of $\gamma$, $g' \ge \gamma$. Combined with $g' = \gamma^{p'/p} \le \gamma$, this yields $g' = \gamma$ and $p' = p$. $\square$

---

## 4. Explicit Finite-Time Algorithm (and Proof of Termination & Completeness)

Given any nonsquare $d \ge 2$, the following algorithm computes $A_r$, $(X_{0,j}, Y_{0,j})_{j=1}^p$, and hence $p(n) = p$, $g(n) = \gamma$, and every term $T(n, k)$ without scanning candidate values of $t$ for patterns:

1. **Compute $\varepsilon_0 = \frac{A_1 + B_1\sqrt{d}}{2}$ and $\gamma = \frac{A_r + B_r\sqrt{d}}{2}$:**
   Expand the simple continued fraction of $\sqrt{d}$ (and of $\frac{1+\sqrt{d}}{2}$ when $d \equiv 1 \pmod 4$) until the first positive solution $(A_1, B_1)$ to $A_1^2 - d B_1^2 = 4$ (with $2 \mid A_1, B_1$ if $d \not\equiv 1 \pmod 4$) is reached. Let $(u_1, v_1)$ be the fundamental solution of $u^2 - d v^2 = 1$ from $\sqrt{d}$. Choose $r \in \{1, 2\}$ via Proposition 4(1) to obtain $(A_r, B_r)$, and set $A_r = \mathrm{A377291}(n)$.
2. **Enumerate all primitive Pell representatives via PQa:**
   For each $M \in \{c(d-c) : 1 \le c \le d-1\}$ and each divisor $g \ge 1$ with $g^2 \mid M$, set $m = M/g^2$. Find all residues $r_0 \in (-m/2, m/2]$ satisfying $r_0^2 \equiv d \pmod m$. For each $r_0$, expand the simple continued fraction of $\alpha_0 = \frac{r_0 + \sqrt{d}}{m}$ via integer recurrences $P_0 = r_0,\ Q_0 = m$:
   $$a_k = \left\lfloor \frac{P_k + \sqrt{d}}{Q_k} \right\rfloor,\quad P_{k+1} = a_k Q_k - P_k,\quad Q_{k+1} = \frac{d - P_{k+1}^2}{Q_k},$$
   with $p_{-2}=0, p_{-1}=1, q_{-2}=1, q_{-1}=0$, $p_k = a_k p_{k-1} + p_{k-2}$, $q_k = a_k q_{k-1} + q_{k-2}$, and $G_k = m p_k - r_0 q_k$. Collect every pair $(G_k, q_k)$ with $G_k^2 - d q_k^2 = -m$ (i.e. $(-1)^{k+1} Q_{k+1} = -1$) up until a reduced state $(P_{k+1}, Q_{k+1})$ (satisfying $Q_{k+1} > 0$, $0 < P_{k+1} < \sqrt{d}$, $\sqrt{d} - P_{k+1} < Q_{k+1} < \sqrt{d} + P_{k+1}$) has been visited three times (covering the preperiod plus at least two full periods).
3. **Lift to $\mathcal{S}_d$ and normalize into $W_0$:**
   Notice $\varepsilon_{\mathbb{Z}[\sqrt{d}]} = u_1 + v_1\sqrt{d} = \varepsilon_0^s$ where $s \in \{1, 3\}$: when $d \equiv 1 \pmod 4$, writing $\varepsilon_0 = \frac{A_1 + B_1\sqrt{d}}{2}$ and using $d B_1^2 = A_1^2 - 4$, the coefficients of $1$ and $\sqrt{d}$ in $\varepsilon_0^3$ are
   $$\frac{A_1(A_1^2 + 3d B_1^2)}{8} = \frac{A_1(A_1^2 - 3)}{2}, \qquad \frac{B_1(3A_1^2 + d B_1^2)}{8} = \frac{B_1(A_1^2 - 1)}{2},$$
   both integers whenever $A_1, B_1$ are odd (and trivially integers when $A_1, B_1$ are even), so $\varepsilon_0^3 \in \mathbb{Z}[\sqrt{d}]$ and $s \mid 3$, i.e., $s \in \{1, 3\}$; for $d \not\equiv 1 \pmod 4$, $s = 1$. Let $t_{\mathrm{coset}} = \mathrm{lcm}(r, s) \in \{1, 2, 3, 6\}$.
   For every collected $(G_k, q_k)$, both signs $\sigma \in \{+1, -1\}$, and every shift $j \in \{0, 1, \dots, t_{\mathrm{coset}} - 1\}$: form $X_{\mathrm{init}} + Y_{\mathrm{init}}\sqrt{d} = \varepsilon_0^j (\sigma g G_k + g q_k \sqrt{d})$. If $X_{\mathrm{init}}, Y_{\mathrm{init}} \in \mathbb{Z}$ with $Y_{\mathrm{init}} \ge 1$ and $(X_{\mathrm{init}}, Y_{\mathrm{init}}) \in \mathcal{S}_d$, apply $T_\gamma$ (while $X \le d$) or $T_{\gamma^{-1}}$ (while $X_{\mathrm{prev}} \ge d+1$ and $Y_{\mathrm{prev}} \ge 1$) until $(X, Y) \in \mathcal{S}_d^+$ is in $W_0$ (minimal with $X \ge d + 1$).
4. **Output:** Sort the distinct elements $(X_{0,j}, Y_{0,j})$ of $W_0$ by $Y_{0,1} < \dots < Y_{0,p}$. Then $p(n) = p = |W_0|$, and $T(n, mp+j) = Y_{m,j}$ is generated iteratively via $T_\gamma$ (or $Y_{m+2,j} = A_r Y_{m+1,j} - Y_{m,j}$).

**Proof of Termination and Completeness.**
- *Termination*: By the standard Galois/Lagrange tail bound, for $\alpha_0 = \frac{r_0 + \sqrt{d}}{m}$, solving $\alpha_0 = \frac{p_k \alpha_{k+1} + p_{k-1}}{q_k \alpha_{k+1} + q_{k-1}}$ gives $\bar{\alpha}_{k+1} = -\frac{p_{k-1} - q_{k-1}\bar{\alpha}_0}{p_k - q_k\bar{\alpha}_0}$. Since $|p_k - q_k\alpha_0| < 1/q_k$ and $q_k - q_{k-1} \ge 1$ for $k \ge 2$, $(p_k - q_k\bar{\alpha}_0) - (p_{k-1} - q_{k-1}\bar{\alpha}_0) \ge (\alpha_0 - \bar{\alpha}_0) - \frac{2}{q_{k-1}} > 0$ once $q_{k-1} > \frac{2m}{\sqrt{d}}$, so $-1 < \bar{\alpha}_{k+1} < 0$ for all sufficiently large $k$. Combined with $\alpha_{k+1} > 1$, this yields $0 < Q_{k+1} = \frac{2\sqrt{d}}{\alpha_{k+1} - \bar{\alpha}_{k+1}} < 2\sqrt{d}$ and $\sqrt{d} - Q_{k+1} < P_{k+1} < \sqrt{d}$ with $P_{k+1} > 0$, leaving finitely many reduced pairs $(P_{k+1}, Q_{k+1})$. Since $Q_0 = m \mid (d - r_0^2)$ and $Q_{k+1} = Q_{k-1} + 2 a_k P_k - a_k^2 Q_k \in \mathbb{Z}$, $(P_k, Q_k)$ enters a finite periodic cycle and terminates after visiting a reduced state three times.
- *Identity & Completeness*: Cross-multiplying $\alpha_0(q_k \alpha_{k+1} + q_{k-1}) = p_k \alpha_{k+1} + p_{k-1}$ gives $(G_k - q_k\sqrt{d})(P_{k+1} + \sqrt{d}) + Q_{k+1}(G_{k-1} - q_{k-1}\sqrt{d}) = 0$. Equating $1$ and $\sqrt{d}$ components yields $G_k = P_{k+1} q_k + Q_{k+1} q_{k-1}$ and $Q_{k+1} G_{k-1} = d q_k - P_{k+1} G_k$; substituting into $G_k q_{k-1} - G_{k-1} q_k = m(p_k q_{k-1} - p_{k-1} q_k) = (-1)^{k+1} m$ after multiplying by $Q_{k+1}$ gives
  $$G_k^2 - d q_k^2 = (-1)^{k+1} m Q_{k+1}.$$
  Now take any $(X, Y) \in W_0 \subset \mathcal{S}_d^+$. Let $g = \gcd(X, Y)$, $x = X/g$, $y = Y/g$, and $m = c(d-c)/g^2$, so $x^2 - d y^2 = -m$ and $\gcd(x, y) = 1$. Let $\varepsilon = u_1 + v_1\sqrt{d} \in \mathbb{Z}[\sqrt{d}]^\times$. Choose $r_0 \in (-m/2, m/2]$ with $x \equiv -r_0 y \pmod m$ (so $r_0^2 \equiv d \pmod m$, and $x = m u - r_0 y$ for $u \in \mathbb{Z}$). Note that for every $(x', y') = \varepsilon^N(x, y)$ ($N \ge 0$), $(u_1 x' + d v_1 y') + r_0(v_1 x' + u_1 y') \equiv (d - r_0^2) v_1 y' \equiv 0 \pmod m$, so every $\varepsilon^N$-iterate retains the exact same residue $-r_0 \pmod m$! Moreover, for $(x', y')$ in the positive quadrant, $m u'^2 - 2 r_0 u' y' + \frac{r_0^2 - d}{m} y'^2 = -1$ factors as
  $$\left|\frac{u'}{y'} - \frac{r_0 + \sqrt{d}}{m}\right| = \frac{1}{y'(x' + y'\sqrt{d})}.$$
  Since $\varepsilon > 1$, for sufficiently large $N$ we have $x' + y'\sqrt{d} > 2 y'$ and $y'$ exceeds all convergent denominators in the finite preperiod of $\alpha_0 = \frac{r_0 + \sqrt{d}}{m}$. By Legendre's theorem on continued fractions, $\frac{u'}{y'} = \frac{p_k}{q_k}$ is a convergent in the purely periodic cycle of $\alpha_0$, and $\gcd(u', y') = 1 \implies (u', y') = (p_k, q_k)$, hence $(x', y') = (G_k, q_k)$ with $G_k^2 - d q_k^2 = -m$ (so $Q_{k+1} = (-1)^k = 1$). Writing $k = k_0 + 2 m_{\mathrm{per}} L$ where $2L$ is an even period ($m_{\mathrm{per}} \ge 0$) and $k_0$ lies in the first two full reduced periods (hence visited before termination in Step 2), let $M_{\mathrm{per}} \in \mathrm{SL}_2(\mathbb{Z})$ be the transfer matrix over $2L$ steps fixing $\alpha_{k_0+1} = P_{k_0+1} + \sqrt{d} \in \mathbb{Z}[\sqrt{d}]$ (as $Q_{k_0+1} = 1$). Then $M_{\mathrm{per}} \binom{\alpha_{k_0+1}}{1} = \lambda \binom{\alpha_{k_0+1}}{1}$ with eigenvalue $\lambda \in \mathbb{Z}[\sqrt{d}]^\times$, $\lambda > 1$, $\mathrm{Nm}(\lambda) = +1$, while the orthogonal vector $\binom{G_{k_0} - q_{k_0}\sqrt{d}}{G_{k_0-1} - q_{k_0-1}\sqrt{d}}$ transforms under $M_{\mathrm{per}}^T$ by $\lambda^{-1}$. Conjugating yields $G_k + q_k\sqrt{d} = \lambda^{m_{\mathrm{per}}} (G_{k_0} + q_{k_0}\sqrt{d})$. Because $\lambda, \varepsilon \in \mathbb{Z}[\sqrt{d}]^\times$ are powers of $\varepsilon_{\mathbb{Z}[\sqrt{d}]} = \varepsilon_0^s$, we obtain $X + Y\sqrt{d} = \varepsilon^{-N} \lambda^{m_{\mathrm{per}}} (g G_{k_0} + g q_{k_0}\sqrt{d}) = \varepsilon_0^e (g G_{k_0} + g q_{k_0}\sqrt{d})$ for some $e \in \mathbb{Z}$. Reducing $e$ modulo $t_{\mathrm{coset}}$ to $j := e \bmod t_{\mathrm{coset}} \in \{0, \dots, t_{\mathrm{coset}}-1\}$ places $\varepsilon_0^j (g G_{k_0} + g q_{k_0}\sqrt{d})$ into the exact same $\gamma$-orbit as $(X, Y)$ (since $\gamma = \varepsilon_0^r$ and $r \mid t_{\mathrm{coset}}$), so normalization by $T_{\gamma^{\pm 1}}$ in Step 3 recovers $(X, Y) \in W_0$. $\square$

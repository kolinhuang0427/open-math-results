# Complete Proof of Problem 5.3 in Godard–Reis (2026)

**Primary source:** Jean Godard and Lucas Reis, *Graphs from quadratic forms and vector spaces over finite fields*, [arXiv:2605.21866v1](https://arxiv.org/abs/2605.21866v1) (2026-05-21), Section 1 (Definition 1.1, p. 2; lines 100 and 114 of `godard-reis.tex`) and Section 5 (*Conclusions and open problems*), Problem 5.3 (3rd problem in Section 5, lines 363–365 of `godard-reis.tex`).

**Verification status:** Written proof (with exact-arithmetic verification of lower-bound disconnections, effective character-sum inequalities, Kummer–Weil norm polynomials, Jacobian rank growth, reflection identities, and finite-field connectedness for $n \in \{4, 5, 6, 7, 8, 9\}$ in [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/godard-2605.21866-prob3/verify.py)); not peer-reviewed.

---

## Problem Statement and Main Theorem

Let $q$ be an odd prime power, let $n \ge 4$ be an integer, let $b \in \mathbb{F}_{q^n}^*$, and let $V \subsetneq \mathbb{F}_{q^n}$ be a proper $\mathbb{F}_q$-vector subspace. Define $Q_b(X, Y) := X^2 + bXY + Y^2$, and let $\Gamma(Q_b, V)$ be the undirected simple graph with vertex set $\mathbb{F}_{q^n}$ in which distinct vertices $x, y \in \mathbb{F}_{q^n}$ are adjacent if and only if $Q_b(x, y) \in V$.

> **Problem 5.3 (Godard–Reis, arXiv:2605.21866v1, Section 5):** *For each integer $n \ge 4$, find the smallest integer $s(n)$ with the following property: if $q$ is large and $\#V \ge q^{s(n)}$, then $\Gamma(Q_b, V)$ is connected for every $b \in \mathbb{F}_{q^n}^*$.*

**Main Theorem.** For every integer $n \ge 4$, let $p_0(n)$ denote the smallest prime factor of $n$. Then
$$s(n) = \frac{n}{p_0(n)} + 1.$$
More precisely:
1. **(Universal lower bound, sharp for every odd prime power $q \ge 3$):** For every integer $n \ge 4$ and every odd prime power $q \ge 3$, there exist a proper $\mathbb{F}_q$-vector subspace $V \subsetneq \mathbb{F}_{q^n}$ of size $\#V = q^{n/p_0(n)}$ and an element $b \in \mathbb{F}_{q^n}^*$ such that $\Gamma(Q_b, V)$ is disconnected.
2. **(Upper bound):** For every integer $n \ge 4$, there exists a threshold $q_0(n)$ (with $q_0(n) = 5$ for all even $n \ge 4$) such that for every odd prime power $q \ge q_0(n)$, every proper $\mathbb{F}_q$-vector subspace $V \subsetneq \mathbb{F}_{q^n}$ with $\#V \ge q^{n/p_0(n) + 1}$, and every $b \in \mathbb{F}_{q^n}^*$, the graph $\Gamma(Q_b, V)$ is connected.

In particular, for the open values highlighted in Godard–Reis Section 5, $s(4) = 3$, $s(5) = 2$, $s(6) = 4$, $s(7) = 2$, $s(8) = 5$, $s(9) = 4$, $s(10) = 6$, and in general $s(n) = \frac{n}{2} + 1$ for even $n \ge 4$, $s(p) = 2$ for odd primes $p \ge 5$, and $s(n) = \frac{n}{p_0(n)} + 1$ for odd composite $n \ge 9$.

**Preliminary reduction for the upper bound.** Let $d_0 := n / p_0(n)$ and $s := d_0 + 1$. Since $n \ge 4$ and $p_0(n) \ge 2$, we have $2 \le s \le \frac{n}{2} + 1 < n$. Any proper $\mathbb{F}_q$-vector subspace $V \subsetneq \mathbb{F}_{q^n}$ with $\#V \ge q^s$ contains an $\mathbb{F}_q$-vector subspace $V' \subseteq V$ with $\dim_{\mathbb{F}_q}(V') = s$, and $\Gamma(Q_b, V')$ is a spanning subgraph of $\Gamma(Q_b, V)$. Hence to prove the upper bound it suffices to prove that $\Gamma(Q_b, V)$ is connected whenever $\dim_{\mathbb{F}_q}(V) = s$.

---

## Section 1: Lower Bound $s(n) \ge \frac{n}{p_0(n)} + 1$ for All $n \ge 4$

Fix $n \ge 4$ and an arbitrary odd prime power $q \ge 3$. Set $p_0 := p_0(n)$ and $d_0 := n / p_0 \in \{1, \dots, \lfloor n/2 \rfloor\}$. We construct a proper $\mathbb{F}_q$-vector subspace $V \subsetneq \mathbb{F}_{q^n}$ of dimension $d_0$ (so $\#V = q^{d_0}$) and $b \in \mathbb{F}_{q^n}^*$ for which $\Gamma(Q_b, V)$ is disconnected.

- **Case 1a ($n = 2k$ even, so $p_0 = 2$ and $d_0 = k \ge 2$):** This is Godard–Reis Remark 1.6 (`rem:disc`). Choose any nonsquare $\alpha \in \mathbb{F}_{q^n}$ and set $V := \alpha \mathbb{F}_{q^k}$, which is a proper $\mathbb{F}_q$-subspace of dimension $k = d_0$. Since $q$ is odd, $\frac{q^{2k}-1}{2} = \frac{q^k+1}{2}(q^k-1)$ with $\frac{q^k+1}{2} \in \mathbb{Z}$, so $u^{(q^{2k}-1)/2} = (u^{q^k-1})^{(q^k+1)/2} = 1$ for every $u \in \mathbb{F}_{q^k}^*$; thus every element of $\mathbb{F}_{q^k}$ is a square in $\mathbb{F}_{q^{2k}}$, and hence every nonzero element of $V = \alpha \mathbb{F}_{q^k}$ is a nonsquare in $\mathbb{F}_{q^{2k}}$. For any $b \in \mathbb{F}_{q^n}^*$ and any $z \in \mathbb{F}_{q^n} \setminus \{0\}$, $Q_b(0, z) = z^2$ is a nonzero square, so $Q_b(0, z) \notin V$. Thus $0$ is an isolated vertex of $\Gamma(Q_b, V)$, and since $q^n > 1$, $\Gamma(Q_b, V)$ is disconnected.

- **Case 1b ($n$ odd, so $p_0 \ge 3$ is odd and $1 \le d_0 < n$):** Set $V := \mathbb{F}_{q^{d_0}}$ (a proper $\mathbb{F}_q$-subspace of dimension $d_0$ inside $\mathbb{F}_{q^n}$) and choose any $b \in \mathbb{F}_{q^{d_0}}^*$ (for example $b = 1$ or $b = 2 \in \mathbb{F}_q^* \subseteq \mathbb{F}_{q^{d_0}}^*$). Suppose $x \in \mathbb{F}_{q^{d_0}}$ and $y \in \mathbb{F}_{q^n}$ satisfy $Q_b(x, y) \in V = \mathbb{F}_{q^{d_0}}$. Completing the square (using $2 \in \mathbb{F}_q^*$):
  $$\left(y + \frac{b}{2} x\right)^2 = Q_b(x, y) + \left(\frac{b^2}{4} - 1\right) x^2 \in \mathbb{F}_{q^{d_0}}.$$
  Let $w := y + \frac{b}{2} x \in \mathbb{F}_{q^n}$. Since $w^2 \in \mathbb{F}_{q^{d_0}}$, the degree $[\mathbb{F}_{q^{d_0}}(w) : \mathbb{F}_{q^{d_0}}]$ divides $2$. On the other hand, $\mathbb{F}_{q^{d_0}} \subseteq \mathbb{F}_{q^{d_0}}(w) \subseteq \mathbb{F}_{q^n}$ implies that $[\mathbb{F}_{q^{d_0}}(w) : \mathbb{F}_{q^{d_0}}]$ divides $[\mathbb{F}_{q^n} : \mathbb{F}_{q^{d_0}}] = p_0$, which is odd. Therefore $[\mathbb{F}_{q^{d_0}}(w) : \mathbb{F}_{q^{d_0}}] = 1$, so $w \in \mathbb{F}_{q^{d_0}}$ and hence $y = w - \frac{b}{2} x \in \mathbb{F}_{q^{d_0}}$. Thus no vertex in $\mathbb{F}_{q^{d_0}}$ has an edge to any vertex in $\mathbb{F}_{q^n} \setminus \mathbb{F}_{q^{d_0}}$. Since $0 < q^{d_0} < q^n$, $\Gamma(Q_b, V)$ is disconnected.

In both cases $s(n) > d_0$, proving $s(n) \ge d_0 + 1 = \frac{n}{p_0(n)} + 1$ for all $n \ge 4$.

---

## Section 2: Effective Upper Bound for All Even $n \ge 4$ ($q \ge 5$)

Let $q = p^e$ be an odd prime power, $n \ge 4$ be any integer, $b \in \mathbb{F}_{q^n}^*$, and $V \subsetneq \mathbb{F}_{q^n}$ be an $\mathbb{F}_q$-subspace of size $\#V = q^{n-j}$ ($1 \le j \le n - 1$). For each $u \in \mathbb{F}_{q^n}$, let $\psi_u(z) := \exp\bigl(\frac{2\pi i}{p} \mathrm{Tr}_{\mathbb{F}_{q^n}/\mathbb{F}_p}(u z)\bigr)$ be the corresponding additive character of $\mathbb{F}_{q^n}$, and let $\eta$ be the quadratic character of $\mathbb{F}_{q^n}$ ($\eta(0) = 0$, $\eta(z) = 1$ for nonzero squares, $\eta(z) = -1$ for nonsquares).

Define the orthogonal complement $V_* := \{u \in \mathbb{F}_{q^n} : \mathrm{Tr}_{\mathbb{F}_{q^n}/\mathbb{F}_p}(u v) = 0\ \forall v \in V\}$. Since $(u, z) \mapsto \mathrm{Tr}_{\mathbb{F}_{q^n}/\mathbb{F}_p}(u z)$ is a nondegenerate $\mathbb{F}_p$-bilinear form on $\mathbb{F}_{q^n}$ and $\dim_{\mathbb{F}_p}(V) = e(n - j)$, we have $\dim_{\mathbb{F}_p}(V_*) = ej$, so $\#V_* = q^j$. By character orthogonality on the finite abelian group $(\mathbb{F}_{q^n}, +)$ (Godard–Reis Lemma 2.3, `lem:indicator`):
$$\sum_{u \in V_*} \psi_u(z) = \begin{cases} q^j & \text{if } z \in V, \\ 0 & \text{if } z \notin V. \end{cases}$$

**Lemma 2.1 (Affine quadratic character sum; cf. Godard–Reis Lemma 2.4, `lem:boundaffine`).** *For every $a \in \mathbb{F}_{q^n}$,*
$$\left|\sum_{v \in V} \eta(a + v)\right| \le \frac{q^j - 1}{q^j} q^{n/2}.$$
*Proof.* Using the indicator identity for $a + V$ and $\sum_{z \in \mathbb{F}_{q^n}} \eta(z) = 0$:
$$\sum_{v \in V} \eta(a + v) = \sum_{z \in \mathbb{F}_{q^n}} \eta(z) \cdot \frac{1}{q^j} \sum_{u \in V_*} \psi_u(z - a) = \frac{1}{q^j} \sum_{u \in V_* \setminus \{0\}} \psi_u(-a) \sum_{z \in \mathbb{F}_{q^n}} \eta(z) \psi_u(z).$$
For every $u \neq 0$, the quadratic Gauss sum $G(\eta, \psi_u) := \sum_{z \in \mathbb{F}_{q^n}} \eta(z) \psi_u(z)$ has absolute value $q^{n/2}$ (Lidl–Niederreiter, *Finite Fields*, Thm. 5.11). The triangle inequality yields the bound. $\square$

**Lemma 2.2 (Bilinear additive character sum; cf. Godard–Reis Lemma 2.5, `lem:GS`).** *For every nonempty subset $A \subseteq \mathbb{F}_{q^n}$, every $b \in \mathbb{F}_{q^n}^*$, and every $u \in \mathbb{F}_{q^n}^*$,*
$$\left|\sum_{x, y \in A} \psi_u(Q_b(x, y))\right| \le q^{n/2} (\#A).$$
*Proof.* Since $|\psi_u(x^2)| = 1$, the triangle inequality and Cauchy–Schwarz give
$$\begin{aligned}
\left|\sum_{x, y \in A} \psi_u(x^2 + bxy + y^2)\right|^2 &\le \left(\sum_{x \in A} \left|\sum_{y \in A} \psi_u(y^2 + bxy)\right|\right)^2 \\
&\le (\#A) \sum_{x \in \mathbb{F}_{q^n}} \left|\sum_{y \in A} \psi_u(y^2 + bxy)\right|^2 \\
&= (\#A) \sum_{y_1, y_2 \in A} \psi_u(y_1^2 - y_2^2) \sum_{x \in \mathbb{F}_{q^n}} \psi_u\bigl(b(y_1 - y_2) x\bigr).
\end{aligned}$$
Since $ub \neq 0$, the inner sum over $x \in \mathbb{F}_{q^n}$ equals $q^n$ if $y_1 = y_2$ and $0$ otherwise. Thus the right-hand side equals $q^n (\#A)^2$. Taking square roots completes the proof. $\square$

**Proposition 2.3 (Effective connectedness for even $n \ge 4$).** *For every even integer $n = 2k \ge 4$, every odd prime power $q \ge 5$, every $\mathbb{F}_q$-subspace $V \subsetneq \mathbb{F}_{q^n}$ with $\#V = q^{k+1}$, and every $b \in \mathbb{F}_{q^n}^*$, the graph $\Gamma(Q_b, V)$ is connected.*

*Proof.* Let $A \subseteq \mathbb{F}_{q^n}$ be any connected component of $\Gamma(Q_b, V)$, and set
$$P(A) := \#\{(x, y) \in A \times A : Q_b(x, y) \in V\}.$$
For any $x \in A$ and any $y \in \mathbb{F}_{q^n}$ satisfying $Q_b(x, y) \in V$, either $y = x \in A$ or $y \neq x$, in which case $(x, y)$ is an edge of $\Gamma(Q_b, V)$ and again $y \in A$. Therefore
$$P(A) = \sum_{x \in A} \#\{y \in \mathbb{F}_{q^n} : Q_b(x, y) \in V\}.$$
For each fixed $x \in \mathbb{F}_{q^n}$, writing $z := y + \frac{b}{2} x$ (a bijection on $\mathbb{F}_{q^n}$) and $a_x := (\frac{b^2}{4} - 1) x^2$:
$$\#\{y \in \mathbb{F}_{q^n} : Q_b(x, y) \in V\} = \#\{z \in \mathbb{F}_{q^n} : z^2 \in a_x + V\} = \sum_{v \in V} \bigl(1 + \eta(a_x + v)\bigr) \ge q^{n-j} - \frac{q^j - 1}{q^j} q^{n/2}$$
by Lemma 2.1. Summing over $x \in A$ yields
$$P(A) \ge (\#A)\left(q^{n-j} - \frac{q^j - 1}{q^j} q^{n/2}\right).$$
On the other hand, expressing the indicator of $V$ via $V_*$ and applying Lemma 2.2 to each $u \in V_* \setminus \{0\}$ gives
$$q^j P(A) = \sum_{u \in V_*} \sum_{x, y \in A} \psi_u(Q_b(x, y)) = (\#A)^2 + \sum_{u \in V_* \setminus \{0\}} \sum_{x, y \in A} \psi_u(Q_b(x, y)) \le (\#A)^2 + (q^j - 1) q^{n/2} (\#A).$$
Combining the lower and upper bounds on $q^j P(A)$ and dividing by $\#A > 0$, we obtain
$$\#A \ge q^n - 2(q^j - 1) q^{n/2}.$$
Specializing to $n = 2k \ge 4$ and $j = k - 1$ ($\#V = q^{k+1}$):
$$\#A \ge q^{2k} - 2 q^{2k-1} + 2 q^k = q^{2k}\left(1 - \frac{2}{q}\right) + 2 q^k.$$
For every odd prime power $q \ge 5$, we have $1 - \frac{2}{q} \ge \frac{3}{5} > \frac{1}{2}$, hence $\#A > \frac{1}{2} q^{2k}$ for every connected component $A$. Because two disjoint connected components cannot both have size strictly greater than $\frac{1}{2} q^{2k}$, $\Gamma(Q_b, V)$ has only one connected component. $\square$

*(Remark: Combined with Case 1a, Proposition 2.3 settles the Main Theorem for all even $n \ge 4$ with the explicit threshold $q_0(n) = 5$.)*

---

## Section 3: Effective Upper Bound for Odd $n \ge 5$ and $b \in \{2, -2\}$

In Sections 3 and 4, fix an odd integer $n \ge 5$, set $d_0 := n / p_0(n)$ and $s := d_0 + 1$, and let $V \subsetneq \mathbb{F}_{q^n}$ be an $\mathbb{F}_q$-subspace with $\dim_{\mathbb{F}_q}(V) = s$. Define
$$S_V := \{\alpha \in \mathbb{F}_{q^n} : \alpha^2 \in V\}.$$
Notice that $0 \in S_V$, $-S_V = S_V$, and for every $\lambda \in \mathbb{F}_q$ and $\alpha \in S_V$, $(\lambda \alpha)^2 = \lambda^2 \alpha^2 \in V$ (since $\lambda^2 \in \mathbb{F}_q$ and $V$ is an $\mathbb{F}_q$-subspace). Hence $S_V$ is closed under $\mathbb{F}_q$-scalar multiplication, so the additive subgroup of $(\mathbb{F}_{q^n}, +)$ generated by $S_V$ coincides with $\mathrm{span}_{\mathbb{F}_q}(S_V)$.

**Lemma 3.1 (Spanning criterion for $b = \pm 2$).** *If $\mathrm{span}_{\mathbb{F}_q}(S_V) = \mathbb{F}_{q^n}$, then both $\Gamma(Q_{-2}, V)$ and $\Gamma(Q_{+2}, V)$ are connected.*

*Proof.*
- For $b = -2$, $Q_{-2}(x, y) = (x - y)^2 \in V \iff x - y \in S_V$. Thus $\Gamma(Q_{-2}, V)$ is the Cayley graph on $(\mathbb{F}_{q^n}, +)$ with symmetric generating set $S_V \setminus \{0\}$, which is connected because $S_V$ additively generates $\mathrm{span}_{\mathbb{F}_q}(S_V) = \mathbb{F}_{q^n}$.
- For $b = +2$, $Q_{+2}(x, y) = (x + y)^2 \in V \iff x + y \in S_V$. Let $C_0 \subseteq \mathbb{F}_{q^n}$ be the connected component of $0$ in $\Gamma(Q_{+2}, V)$.
  1. For every $x \in C_0 \setminus \{0\}$, $x \neq -x$ (as $q$ is odd) and $x + (-x) = 0 \in S_V$, so $(x, -x)$ is an edge and hence $-x \in C_0$. Thus $-C_0 = C_0$.
  2. For every $x \in C_0$ and $\alpha \in S_V$, let $y := \alpha - x$; then $x + y = \alpha \in S_V$, so either $y = x \in C_0$ or $(x, y)$ is an edge and $y \in C_0$. Thus $\alpha - x \in C_0$.
  3. Combining (1) and (2): for every $x \in C_0$ and $\alpha \in S_V$, $-x \in C_0$, so $\alpha - (-x) = x + \alpha \in C_0$.
  Hence $C_0$ contains $0$ and is closed under translation by every $\alpha \in S_V$, so $C_0 \supseteq \mathrm{span}_{\mathbb{F}_q}(S_V) = \mathbb{F}_{q^n}$. $\square$

**Proposition 3.2 (Effective connectedness for odd $n \ge 5$ and $b = \pm 2$).** *Let $n \ge 5$ be odd and let $q$ be an odd prime power satisfying $q - (n - 1)\sqrt{q} > 2^{n-1}$. Then for every $\mathbb{F}_q$-subspace $V \subsetneq \mathbb{F}_{q^n}$ of dimension $s = d_0 + 1$, we have $\mathrm{span}_{\mathbb{F}_q}(S_V) = \mathbb{F}_{q^n}$, and hence $\Gamma(Q_{\pm 2}, V)$ is connected.*

*Proof.* First note that $q - (n - 1)\sqrt{q} > 2^{n-1}$ implies $q > 2^{n-1} > n \ge \tau(n)$ for all $n \ge 5$ (where $\tau(n)$ is the number of positive divisors of $n$).

**Step 1 (Existence of a primitive ratio).** Fix any $v_2 \in V \setminus \{0\}$. For every proper divisor $d \mid n$ ($d < n$), we have $d \le d_0 = s - 1$, so $W_d := V \cap (v_2 \mathbb{F}_{q^d})$ is an $\mathbb{F}_q$-subspace of $V$ of dimension $\le s - 1$. Since there are $\tau(n) - 1$ proper divisors of $n$ and $0 \in W_d$ for all $d$,
$$\#\bigcup_{\substack{d \mid n \\ d < n}} W_d \le 1 + (\tau(n) - 1)(q^{s-1} - 1) < 1 + q(q^{s-1} - 1) = q^s - (q - 1) < q^s = \#V.$$
Hence there exists $v_1 \in V$ such that $a := v_1 / v_2 \in \mathbb{F}_{q^n}$ lies in no proper subfield $\mathbb{F}_{q^d}$ ($d \mid n$, $d < n$). Consequently $\mathbb{F}_q(a) = \mathbb{F}_{q^n}$, so the $n$ Frobenius conjugates $a_i := a^{q^i}$ ($0 \le i \le n - 1$) are pairwise distinct in $\mathbb{F}_{q^n}$.

**Step 2 (Weil lower bound on a curve in $S_V$).** Consider the finite set
$$C(\mathbb{F}_q) := \{(\alpha, t) \in \mathbb{F}_{q^n} \times \mathbb{F}_q : \alpha^2 = v_1 + t v_2\}.$$
For every $z \in \mathbb{F}_{q^n}^*$, writing $N := N_{\mathbb{F}_{q^n}/\mathbb{F}_q}$, we have
$$\eta_{\mathbb{F}_{q^n}}(z) = z^{(q^n - 1)/2} = \left(z^{(q^n - 1)/(q - 1)}\right)^{(q - 1)/2} = N(z)^{(q - 1)/2} = \eta_{\mathbb{F}_q}(N(z)),$$
and the identity also holds at $z = 0$ (where both sides vanish). Thus
$$\#C(\mathbb{F}_q) = \sum_{t \in \mathbb{F}_q} \bigl(1 + \eta_{\mathbb{F}_{q^n}}(v_1 + t v_2)\bigr) = \sum_{t \in \mathbb{F}_q} \bigl(1 + \eta_{\mathbb{F}_q}(f(t))\bigr),$$
where
$$f(t) := N_{\mathbb{F}_{q^n}/\mathbb{F}_q}(v_1 + t v_2) = N_{\mathbb{F}_{q^n}/\mathbb{F}_q}(v_2) \prod_{i=0}^{n-1} (t + a_i) \in \mathbb{F}_q[t].$$
Because $N(v_2) \in \mathbb{F}_q^*$ and the roots $-a_0, \dots, -a_{n-1}$ are pairwise distinct in $\overline{\mathbb{F}_q}$, $f(t)$ is squarefree of odd degree $n \ge 5$, so $f(t)$ is not of the form $c \cdot g(t)^2$ in $\overline{\mathbb{F}_q}[t]$. By Weil's bound for multiplicative character sums (Lidl–Niederreiter, *Finite Fields*, Thm. 5.41),
$$\left|\sum_{t \in \mathbb{F}_q} \eta_{\mathbb{F}_q}(f(t))\right| \le (n - 1)\sqrt{q}, \qquad \text{whence} \qquad \#C(\mathbb{F}_q) \ge q - (n - 1)\sqrt{q}.$$

**Step 3 (Kummer upper bound on hyperplane intersections).** Let $H \subsetneq \mathbb{F}_{q^n}$ be any $\mathbb{F}_q$-hyperplane. By nondegeneracy of $\mathrm{Tr}_{\mathbb{F}_{q^n}/\mathbb{F}_q}$, there exists $u \in \mathbb{F}_{q^n}^*$ such that $H = \{\alpha \in \mathbb{F}_{q^n} : \mathrm{Tr}_{\mathbb{F}_{q^n}/\mathbb{F}_q}(u \alpha) = 0\}$. Set $u_i := u^{q^i} \in \mathbb{F}_{q^n}^*$ and $v_{2,i} := v_2^{q^i} \in \mathbb{F}_{q^n}^*$ for $0 \le i \le n - 1$, and define in $\overline{\mathbb{F}_q}[Z_0, \dots, Z_{n-1}]$ the homogeneous polynomial of degree $2^{n-1}$:
$$\widetilde{Q}(Z_0, \dots, Z_{n-1}) := \prod_{\substack{\varepsilon \in \{\pm 1\}^n \\ \varepsilon_0 = 1}} \left(\sum_{i=0}^{n-1} \varepsilon_i u_i Z_i\right).$$
For every $j \in \{1, \dots, n - 1\}$, negating $Z_j$ merely permutes the factors of $\widetilde{Q}$. Negating $Z_0$ sends each factor $u_0 Z_0 + \sum_{i \ge 1} \varepsilon_i u_i Z_i$ to $-\bigl(u_0 Z_0 + \sum_{i \ge 1} (-\varepsilon_i) u_i Z_i\bigr)$, permuting the $2^{n-1}$ factors and multiplying $\widetilde{Q}$ by $(-1)^{2^{n-1}} = +1$ (since $n \ge 5 \ge 2$). Thus $\widetilde{Q}$ is invariant under $Z_j \mapsto -Z_j$ for every $0 \le j \le n - 1$, so every monomial appearing in $\widetilde{Q}$ has even exponent in every variable $Z_j$. Consequently there exists a homogeneous polynomial $R(W_0, \dots, W_{n-1}) \in \overline{\mathbb{F}_q}[W_0, \dots, W_{n-1}]$ of total degree $2^{n-2}$ such that
$$\widetilde{Q}(Z_0, \dots, Z_{n-1}) = R(Z_0^2, \dots, Z_{n-1}^2) \qquad \text{in } \overline{\mathbb{F}_q}[Z_0, \dots, Z_{n-1}].$$
Define $P(t) := R\bigl(v_{2,0}(a_0 + t), \dots, v_{2,n-1}(a_{n-1} + t)\bigr) \in \overline{\mathbb{F}_q}[t]$; clearly $\deg_t P \le 2^{n-2}$.

We claim that $P(t)$ is not identically zero. Work in the rational function field $K := \overline{\mathbb{F}_q}(t)$ (of characteristic $p \neq 2$), and let $L := K(\zeta_0, \dots, \zeta_{n-1})$ inside an algebraic closure $\overline{K}$, where $\zeta_i^2 = v_{2,i}(a_i + t)$. Since $v_{2,i} \in \overline{\mathbb{F}_q}^* = (\overline{\mathbb{F}_q}^*)^2$ and $a_0 + t, \dots, a_{n-1} + t$ are pairwise non-associate prime elements in the UFD $\overline{\mathbb{F}_q}[t]$, a product $\prod_{i \in I} v_{2,i}(a_i + t)$ is a square in $K^*$ if and only if $I = \emptyset$. By Kummer theory (characteristic $\neq 2$), $[L : K] = 2^n$ and $\mathrm{Gal}(L/K) \cong \{\pm 1\}^n$ acts by $\sigma_\delta(\zeta_i) = \delta_i \zeta_i$ for all $\delta \in \{\pm 1\}^n$. For any $\varepsilon \in \{\pm 1\}^n$, we have $\sum_{i=0}^{n-1} \varepsilon_i u_i \zeta_i \neq 0$ in $L$: indeed, applying $\sigma_\delta$ with $\delta_0 = -1$ and $\delta_i = 1$ ($i \ge 1$) to $\sum_i \varepsilon_i u_i \zeta_i = 0$ and subtracting would give $2 \varepsilon_0 u_0 \zeta_0 = 0$, contradicting $\mathrm{char}(\mathbb{F}_q) \neq 2$, $u_0 \neq 0$, and $\zeta_0 \neq 0$. Therefore
$$P(t) = R(\zeta_0^2, \dots, \zeta_{n-1}^2) = \widetilde{Q}(\zeta_0, \dots, \zeta_{n-1}) = \prod_{\substack{\varepsilon \in \{\pm 1\}^n \\ \varepsilon_0 = 1}} \left(\sum_{i=0}^{n-1} \varepsilon_i u_i \zeta_i\right) \neq 0 \quad \text{in } L,$$
proving that $P(t) \in \overline{\mathbb{F}_q}[t]$ is a nonzero polynomial of degree $\le 2^{n-2}$.

Now let $(\alpha, t_0) \in C(\mathbb{F}_q)$ be any point with $\alpha \in H$. Evaluating the identity $R(Z_0^2, \dots, Z_{n-1}^2) = \widetilde{Q}(Z_0, \dots, Z_{n-1})$ at $Z_i = \alpha^{q^i}$ gives $Z_i^2 = (\alpha^2)^{q^i} = (v_1 + t_0 v_2)^{q^i} = v_{2,i}(a_i + t_0)$, while the $\varepsilon = (1, \dots, 1)$ factor of $\widetilde{Q}$ equals $\sum_{i=0}^{n-1} u_i \alpha^{q^i} = \mathrm{Tr}_{\mathbb{F}_{q^n}/\mathbb{F}_q}(u \alpha) = 0$. Hence $P(t_0) = 0$. Since $P(t) \not\equiv 0$ has at most $2^{n-2}$ roots $t_0 \in \mathbb{F}_q$, and for each $t_0$ the equation $\alpha^2 = v_1 + t_0 v_2$ has at most $2$ solutions $\alpha \in \mathbb{F}_{q^n}$, we obtain
$$\#\{(\alpha, t) \in C(\mathbb{F}_q) : \alpha \in H\} \le 2 \cdot 2^{n-2} = 2^{n-1}.$$

**Step 4 (Conclusion).** Since $\#C(\mathbb{F}_q) \ge q - (n - 1)\sqrt{q} > 2^{n-1}$, for every $\mathbb{F}_q$-hyperplane $H \subsetneq \mathbb{F}_{q^n}$ there exists $(\alpha, t) \in C(\mathbb{F}_q)$ with $\alpha \notin H$. Because $\alpha^2 = v_1 + t v_2 \in V$, we have $\alpha \in S_V \setminus H$. Therefore $S_V$ lies in no proper $\mathbb{F}_q$-hyperplane of $\mathbb{F}_{q^n}$, so $\mathrm{span}_{\mathbb{F}_q}(S_V) = \mathbb{F}_{q^n}$. By Lemma 3.1, $\Gamma(Q_{\pm 2}, V)$ is connected. $\square$

---

## Section 4: Upper Bound for Odd $n \ge 5$ and $b \in \mathbb{F}_{q^n}^* \setminus \{2, -2\}$

We now prove that for every odd $n \ge 5$, there exists $q_0(n)$ such that for every odd prime power $q \ge q_0(n)$, every $\mathbb{F}_q$-subspace $V \subsetneq \mathbb{F}_{q^n}$ of dimension $s := d_0 + 1$, and every $b \in \mathbb{F}_{q^n}^* \setminus \{2, -2\}$, the graph $\Gamma(Q_b, V)$ is connected (indeed, of diameter at most $2(n - s + 1)^2$).

### 4.1. Linear Diagonalization and Coordinate Functionals

Fix an odd prime power $q$, an odd integer $n \ge 5$, an $\mathbb{F}_q$-subspace $V \subsetneq \mathbb{F}_{q^n}$ of dimension $s := d_0 + 1 \in [2, n - 1]$, and $b \in \mathbb{F}_{q^n}^* \setminus \{2, -2\}$. Let $\sigma_0, \dots, \sigma_{n-1} : \mathbb{F}_{q^n} \hookrightarrow \overline{\mathbb{F}_q}$ be the $n$ distinct $\mathbb{F}_q$-embeddings $\sigma_i(x) = x^{q^i}$. The map
$$\iota : \mathbb{F}_{q^n} \otimes_{\mathbb{F}_q} \overline{\mathbb{F}_q} \xrightarrow{\sim} \overline{\mathbb{F}_q}^n, \qquad x \otimes c \mapsto \bigl(c\sigma_0(x), \dots, c\sigma_{n-1}(x)\bigr),$$
is an isomorphism of $\overline{\mathbb{F}_q}$-algebras. Under $\iota$:
- $b \otimes 1$ maps to $(b_0, \dots, b_{n-1})$ with $b_i = \sigma_i(b)$. Since $0, 2, -2 \in \mathbb{F}_q$ are fixed by every $\sigma_i$ and $b \notin \{0, 2, -2\}$, we have **$b_i \in \overline{\mathbb{F}_q}^* \setminus \{2, -2\}$** and **$\Delta_i := \frac{b_i^2}{4} - 1 \neq 0$** for all $0 \le i \le n - 1$.
- Choosing an $\mathbb{F}_q$-basis $v_1, \dots, v_s$ of $V$, the base-changed subspace $V_{\overline{\mathbb{F}_q}} := \iota(V \otimes_{\mathbb{F}_q} \overline{\mathbb{F}_q}) \subset \overline{\mathbb{F}_q}^n$ is the image of the injective linear map $t = (t_1, \dots, t_s) \mapsto (L_0(t), \dots, L_{n-1}(t))$ with $n \times s$ matrix $M_{i, r} := \sigma_i(v_r)$, i.e., $L_i(t) := \sum_{r=1}^s \sigma_i(v_r) t_r$.

**Lemma 4.1 (Pairwise linear independence of coordinate functionals).** *The linear forms $L_0, \dots, L_{n-1} \in \overline{\mathbb{F}_q}[t_1, \dots, t_s]$ are all nonzero and pairwise linearly independent over $\overline{\mathbb{F}_q}$. Equivalently, every nonzero vector $\lambda \in V_{\overline{\mathbb{F}_q}}^\perp \setminus \{0\}$ has $|\mathrm{supp}(\lambda)| \ge 3$.*

*Proof.* Since $v_1 \in V \setminus \{0\}$, $\sigma_i(v_1) \neq 0$ for every $i$, so $L_i \not\equiv 0$. Suppose $L_j = c L_i$ for some $0 \le i < j \le n - 1$ and $c \in \overline{\mathbb{F}_q}^*$. Then $\sigma_j(v) = c \sigma_i(v)$ for every $v \in V$. Taking $v = v_1$ gives $c = \sigma_j(v_1)/\sigma_i(v_1)$, so for every $v \in V$, $(v/v_1)^{q^j} = (v/v_1)^{q^i}$. Applying $\sigma_i^{-1}$ yields $(v/v_1)^{q^{j-i}} = v/v_1$. Since $v/v_1 \in \mathbb{F}_{q^n}$ also satisfies $(v/v_1)^{q^n} = v/v_1$, we get $v/v_1 \in \mathbb{F}_{q^d}$ where $d := \gcd(j - i, n)$. Because $1 \le j - i \le n - 1$, $d$ is a proper divisor of $n$, hence $d \le d_0 = s - 1$. Thus $V \subseteq v_1 \mathbb{F}_{q^d}$, contradicting $\dim_{\mathbb{F}_q}(V) = s > d$. Finally, a vector $\lambda \in V_{\overline{\mathbb{F}_q}}^\perp \setminus \{0\}$ with $|\mathrm{supp}(\lambda)| \in \{1, 2\}$ would produce a vanishing $L_i$ or a proportionality between two distinct $L_i, L_j$. $\square$

**Abstract geometric setting (Sections 4.2–4.4).** Fix integers $n \ge 4$ and $2 \le s < n$. Let $\Omega$ be **any** algebraically closed field of characteristic $\neq 2$. Let $b = (b_0, \dots, b_{n-1}) \in (\Omega^* \setminus \{2, -2\})^n$, let $\Delta_i := \frac{b_i^2}{4} - 1 \in \Omega^*$, let $M = (M_{i,r}) \in \mathrm{Mat}_{n \times s}(\Omega)$ have rank $s$ with rows $L_i(t) := \sum_{r=1}^s M_{i,r} t_r$ ($0 \le i \le n - 1$) nonzero and pairwise linearly independent over $\Omega$, let $V := \mathrm{im}(M) \subset \Omega^n$, and let $x_0 \in \Omega^n$. For $x, y \in \Omega^n$, write $Q_b(x, y) := (x_0^2 + b_0 x_0 y_0 + y_0^2, \dots, x_{n-1}^2 + b_{n-1} x_{n-1} y_{n-1} + y_{n-1}^2)$.

### 4.2. Geometric Integrality of Fibers and Walk Varieties, and Normality of $R$

Define the following affine $\Omega$-schemes:
- For any $x \in \Omega^n$, the **neighborhood fiber**
  $$N(x) := \{y \in \mathbb{A}^n_\Omega : Q_b(x, y) \in V\} \cong \mathrm{Spec} \Omega[t_1, \dots, t_s, u_0, \dots, u_{n-1}] / \bigl(u_i^2 - \Delta_i x_i^2 - L_i(t)\bigr)_{i=0}^{n-1},$$
  where $u_i := y_i + \frac{b_i}{2} x_i$ (a linear isomorphism on $\mathbb{A}^n_y$, and $t \in \mathbb{A}^s_\Omega$ is uniquely linearly determined by $Q_b(x, y) \in V$ since $\mathrm{rk}(M) = s$).
- For every integer $k \ge 1$, the **$k$-walk variety** $W_k(x_0) \subset (\mathbb{A}^n_\Omega)^k$ (coordinates $(x_1, \dots, x_k)$) cut out by $Q_b(x_{j-1}, x_j) \in V$ for $1 \le j \le k$; equivalently, introducing $t^{(j)} \in \mathbb{A}^s_\Omega$ and $u_{j,i} := x_{j,i} + \frac{b_i}{2} x_{j-1,i}$,
  $$W_k(x_0) \cong \mathrm{Spec} A^{(k)}_{x_0}, \qquad A^{(k)}_{x_0} := \Omega[x_1, \dots, x_k, t^{(1)}, \dots, t^{(k)}] / \bigl(u_{j,i}^2 - \Delta_i x_{j-1,i}^2 - L_i(t^{(j)})\bigr)_{1 \le j \le k,\ 0 \le i \le n-1}.$$
  Let $\varphi_k : W_k(x_0) \to \mathbb{A}^n_\Omega$ denote the endpoint projection $(x_1, \dots, x_k) \mapsto x_k$.
- The **edge-relation variety** $R := \{(x, y) \in \mathbb{A}^n_x \times \mathbb{A}^n_y : Q_b(x, y) \in V\}$, with coordinate ring
  $$\Omega[R] \cong \Omega[x_0, \dots, x_{n-1}, t_1, \dots, t_s, u_0, \dots, u_{n-1}] / \bigl(u_i^2 - \Delta_i x_i^2 - L_i(t)\bigr)_{i=0}^{n-1}, \qquad u_i := y_i + \frac{b_i}{2} x_i,$$
  and projections $p_1 : R \to \mathbb{A}^n_x$, $p_2 : R \to \mathbb{A}^n_y$.

**Lemma 4.2 (Integrality, flatness, and normality).**
1. *For every $x \in \Omega^n$, $N(x)$ is integral of dimension $s$ and smooth on the dense open locus $\prod_{i=0}^{n-1} u_i \neq 0$.*
2. *For every $k \ge 1$, $W_k(x_0)$ is integral of dimension $ks$, and $t^{(1)}, \dots, t^{(k)}$ form a separating transcendence basis of $K_k := \Omega(W_k(x_0))$ over $\Omega$.*
3. *$R$ is integral of dimension $n + s$ and **normal**. Both projections $p_1 : R \to \mathbb{A}^n_x$ and $p_2 : R \to \mathbb{A}^n_y$ are **flat** with geometrically integral, generically smooth fibers of dimension $s$.*

*Proof.* We prove a single inductive lemma covering (1), (2), and the integrality/flatness part of (3). Let $B$ be any finitely generated integral domain over $\Omega$ with fraction field $F := \mathrm{Frac}(B)$, and let $x = (x_0, \dots, x_{n-1}) \in B^n$. Consider
$$A := B[t_1, \dots, t_s, u_0, \dots, u_{n-1}] / \bigl(u_i^2 - f_i(t)\bigr)_{i=0}^{n-1}, \qquad f_i(t) := \Delta_i x_i^2 + L_i(t) \in B[t_1, \dots, t_s].$$
- Since each relation $u_i^2 = f_i(t)$ is monic of degree $2$ in $u_i$, $A$ is a **free** $B[t_1, \dots, t_s]$-module of rank $2^n$ (with basis $\prod_{i \in I} u_i$, $I \subseteq \{0, \dots, n - 1\}$). In particular, $A$ is flat (even free) over $B$, and the localization map $A \to A \otimes_{B[t]} F(t)$ is **injective**.
- In the UFD $F[t_1, \dots, t_s]$, each $f_i(t) = \Delta_i x_i^2 + L_i(t)$ is irreducible of degree $1$ in $t$ (since $L_i \not\equiv 0$), and $f_i, f_j$ ($i \neq j$) are non-associate (their degree-$1$ homogeneous parts $L_i, L_j$ are linearly independent over $\Omega$, hence also over $F$). Because $\mathrm{char}(F) = \mathrm{char}(\Omega) \neq 2$, Kummer theory implies that $F(t)(\sqrt{f_0}, \dots, \sqrt{f_{n-1}})$ is a separable Galois extension of $F(t)$ of degree $2^n$ with Galois group $(\mathbb{Z}/2\mathbb{Z})^n$ acting by independent sign flips $\sqrt{f_i} \mapsto \pm \sqrt{f_i}$. Since $A \otimes_{B[t]} F(t)$ has dimension $2^n$ over $F(t)$ and surjects onto this field, $A \otimes_{B[t]} F(t) \cong F(t)(\sqrt{f_0}, \dots, \sqrt{f_{n-1}})$ is a **field**.
- Being a subring of a field, $A$ is an **integral domain** of Krull dimension $\dim B + s$, and $\mathrm{Frac}(A)$ is finite separable over $F(t_1, \dots, t_s)$.

Applying this:
- For (1), take $B = \Omega$: $N(x) = \mathrm{Spec} A$ is integral of dimension $s$. On the nonempty open locus $U_x := \{\prod_{i=0}^{n-1} f_i(t) \neq 0\} \subset \mathbb{A}^s_t$, the finite map $\pi_t : N(x) \to \mathbb{A}^s_t$ is étale (as $2u_i \neq 0$ and $\mathrm{char}\Omega \neq 2$), so $N(x)$ is smooth on $\pi_t^{-1}(U_x) = \{\prod_{i=0}^{n-1} u_i \neq 0\}$.
- For (2), apply the inductive step $k$ times starting from $B_0 = \Omega$: $A^{(k)}_{x_0}$ is an integral domain of dimension $ks$, and $K_k$ is finite separable over $K_{k-1}(t^{(k)})$, hence finite separable over $\Omega(t^{(1)}, \dots, t^{(k)})$ by induction on $k$.
- For (3), taking $B = \Omega[x_0, \dots, x_{n-1}]$ shows that $R$ is integral of dimension $n + s$ and $\Omega[R]$ is a free $\Omega[x]$-module, so $p_1 : R \to \mathbb{A}^n_x$ is flat. By the $(x, y)$-symmetry of $Q_b(x, y)$, $p_2 : R \to \mathbb{A}^n_y$ is also flat. For every scheme-theoretic point $y \in \mathbb{A}^n_y$ (with algebraic closure $\Omega' := \overline{\kappa(y)}$, which has $\mathrm{char}(\Omega') = \mathrm{char}(\Omega) \neq 2$), applying (1) over $\Omega'$ shows that the geometric fiber $p_2^{-1}(y) \times_{\kappa(y)} \Omega' = N(y)_{\Omega'}$ is integral of dimension $s$ and smooth on a dense open subset (and symmetrically for $p_1$).

It remains to verify that $R$ is **normal**. Realizing $R \subset \mathbb{A}^{2n + s}_\Omega$ as the complete intersection of the $n$ polynomials $G_i(x, y, t) := x_i^2 + b_i x_i y_i + y_i^2 - L_i(t) = 0$ ($0 \le i \le n - 1$), $R$ has codimension $n$ in $\mathbb{A}^{2n + s}_\Omega$, hence is Cohen–Macaulay (satisfies Serre's condition $S_2$). Suppose the Jacobian of $(G_0, \dots, G_{n-1})$ drops rank at $(x, y, t) \in R$, so $\sum_{i=0}^{n-1} c_i\, dG_i(x, y, t) = 0$ for some nonzero $c = (c_0, \dots, c_{n-1}) \in \Omega^n \setminus \{0\}$.
- From the $t$-partial derivatives, $\sum_{i=0}^{n-1} c_i L_i \equiv 0$, so $c \in V^\perp \setminus \{0\}$, which forces $|I| \ge 3$ where $I := \mathrm{supp}(c)$ (Lemma 4.1).
- For every $i \in I$, the $x_i$- and $y_i$-partial derivatives give $2 x_i + b_i y_i = 0$ and $b_i x_i + 2 y_i = 0$. The determinant of this linear system is $4 - b_i^2 = -4 \Delta_i \neq 0$, forcing $x_i = y_i = 0$, and then $G_i(x, y, t) = 0$ gives $L_i(t) = 0$.

For each fixed subset $I \subseteq \{0, \dots, n - 1\}$ with $|I| \ge 3$, the image of $S_I := \{(x, y, t) \in R : x_i = y_i = L_i(t) = 0\ \forall i \in I\}$ under the finite projection $R \to \mathbb{A}^n_x \times \mathbb{A}^s_t$ satisfies $|I| \ge 3$ independent linear conditions $x_i = 0$ on $x$ and at least $2$ independent linear conditions on $t$ (any two $L_i, L_j$ with $i, j \in I$ are linearly independent), hence has codimension $\ge |I| + 2 \ge 5$ in $\mathbb{A}^n_x \times \mathbb{A}^s_t$. Since $R \to \mathbb{A}^n_x \times \mathbb{A}^s_t$ is finite, $\mathrm{codim}_R(R_{\mathrm{sing}}) \ge 5 \ge 2$. Thus $R$ satisfies Serre's criteria $R_1$ and $S_2$, so $R$ is normal. $\square$

### 4.3. Dominance and Separability of $\varphi_k$ by $k_0 = n - s + 1$

For $j \ge 1$, let $K_j := \Omega(W_j(x_0))$, and let $T_j := \mathrm{Der}_\Omega(K_j, K_j) = \mathrm{Hom}_{K_j}(\Omega^1_{K_j/\Omega}, K_j)$. By Lemma 4.2(2), $t^{(1)}, \dots, t^{(j)}$ is a separating transcendence basis of $K_j / \Omega$, so $\dim_{K_j} \Omega^1_{K_j / \Omega} = \dim_{K_j} T_j = js$. Define the differential image
$$U_j := \mathrm{im}\bigl(d\varphi_j : T_j \to K_j^n\bigr) = \bigl\{(D(x_{j,0}), \dots, D(x_{j,n-1})) : D \in T_j\bigr\} \subseteq K_j^n,$$
with the convention $K_0 := \Omega$ and $U_0 := \{0\} \subset \Omega^n$.

**Lemma 4.3 (Jacobian rank growth, dominance, separability, and initial degree bound).** *Set $k_0 := n - s + 1 \ge 2$. Then:*
1. *For every $j \ge 1$, $\dim_{K_j}(U_j) \ge \min(n, s + j - 1)$. In particular, $\dim_{K_k}(U_k) = n$ for every $k \ge k_0$.*
2. *For every $k \ge k_0$, $\varphi_k : W_k(x_0) \to \mathbb{A}^n_\Omega$ is dominant and $K_k$ is **separably generated** of transcendence degree $ks - n$ over $E_k := \Omega(x_k) \subseteq K_k$. Consequently, the algebraic closure $L_k$ of $E_k$ in $K_k$ is **finite separable** over $E_k$ of degree $d_k := [L_k : E_k] \ge 1$, and $K_k / L_k$ is a **regular** field extension.*
3. *$d_{k_0} \le 2^{k_0(n - s)}$.*

*Proof.*
**(1)** For $j \ge 1$, differentiate the equations $x_{j-1,i}^2 + b_i x_{j-1,i} x_{j,i} + x_{j,i}^2 = L_i(t^{(j)})$ by any $D \in T_j$:
$$a_{j,i} D(x_{j-1,i}) + c_{j,i} D(x_{j,i}) = L_i\bigl(D(t^{(j)})\bigr) \qquad (0 \le i \le n - 1),$$
where $a_{j,i} := 2 x_{j-1,i} + b_i x_{j,i}$ and $c_{j,i} := b_i x_{j-1,i} + 2 x_{j,i}$. Writing $u_{j,i} := x_{j,i} + \frac{b_i}{2} x_{j-1,i}$, we have $c_{j,i} = 2 u_{j,i}$ and $a_{j,i} = b_i u_{j,i} - 2 \Delta_i x_{j-1,i}$. By the proof of Lemma 4.2, $u_{j,i} = \sqrt{\Delta_i x_{j-1,i}^2 + L_i(t^{(j)})}$ has degree $2$ over $K_{j-1}(t^{(j)})$, so $u_{j,i} \notin K_{j-1}(t^{(j)})$ and in particular $u_{j,i} \neq 0$. Since $\mathrm{char}\Omega \neq 2$, $b_i \neq 0$, and $-2\Delta_i x_{j-1,i} \in K_{j-1}(t^{(j)})$, both $c_{j,i}$ and $a_{j,i}$ are **nonzero** in $K_j$.

Because $t^{(j)}_1, \dots, t^{(j)}_s$ are algebraically independent over $K_{j-1}$ and $K_j / K_{j-1}(t^{(j)})$ is finite separable, every derivation $D_0 \in \mathrm{Der}_\Omega(K_{j-1}, K_j) \cong T_{j-1} \otimes_{K_{j-1}} K_j$ and every vector $w \in K_j^s$ determine a unique derivation $D \in T_j$ extending $D_0$ with $D(t^{(j)}) = w$. Therefore, letting $D(a_j) := \mathrm{diag}(a_{j,0}, \dots, a_{j,n-1})$ and $D(c_j) := \mathrm{diag}(c_{j,0}, \dots, c_{j,n-1})$ (both invertible over $K_j$) and $V_{K_j} := V \otimes_\Omega K_j$,
$$U_j = D(c_j)^{-1}\bigl(V_{K_j} + D(a_j)(U_{j-1} \otimes_{K_{j-1}} K_j)\bigr).$$
At $j = 1$, $U_0 = \{0\}$ gives $\dim_{K_1}(U_1) = \dim_\Omega(V) = s$. For $j \ge 2$, clearly $\dim_{K_j}(U_j) \ge \dim_{K_{j-1}}(U_{j-1})$. Suppose $\dim_{K_j}(U_j) = \dim_{K_{j-1}}(U_{j-1})$; we show $\dim_{K_{j-1}}(U_{j-1}) = n$. Equality of dimensions forces $V_{K_j} \subseteq D(a_j)(U_{j-1} \otimes_{K_{j-1}} K_j)$, i.e.,
$$D(a_j)^{-1} V_{K_j} \subseteq U_{j-1} \otimes_{K_{j-1}} K_j.$$
For each coordinate $i \in \{0, \dots, n - 1\}$, let $\tau_i \in \mathrm{Gal}\bigl(K_j / K_{j-1}(t^{(j)})\bigr) \cong \{\pm 1\}^n$ be the automorphism sending $u_{j,i} \mapsto -u_{j,i}$ and fixing $u_{j,m}$ ($m \neq i$) and $K_{j-1}(t^{(j)})$. Then $\tau_i(a_{j,m}) = a_{j,m}$ for $m \neq i$, while $\tau_i(a_{j,i}) = -b_i u_{j,i} - 2\Delta_i x_{j-1,i} \neq 0$ satisfies $a_{j,i} - \tau_i(a_{j,i}) = 2 b_i u_{j,i} \neq 0$. Because $U_{j-1} \subseteq K_{j-1}^n$ is defined over $K_{j-1}$, the subspace $U_{j-1} \otimes_{K_{j-1}} K_j \subseteq K_j^n$ is invariant under the coordinatewise action of $\tau_i$. Since $L_i \not\equiv 0$, choose $v = (v_0, \dots, v_{n-1}) \in V \subset \Omega^n$ with $v_i \neq 0$. Applying $\tau_i$ to $(a_{j,0}^{-1} v_0, \dots, a_{j,n-1}^{-1} v_{n-1}) \in U_{j-1} \otimes_{K_{j-1}} K_j$ (noting $\tau_i(v_m) = v_m$) and subtracting yields
$$\bigl(a_{j,i}^{-1} - \tau_i(a_{j,i})^{-1}\bigr) v_i e_i = \frac{-2 b_i u_{j,i} v_i}{a_{j,i} \tau_i(a_{j,i})} e_i \in U_{j-1} \otimes_{K_{j-1}} K_j.$$
The scalar coefficient is nonzero in $K_j$, so the $i$-th standard basis vector $e_i$ lies in $U_{j-1} \otimes_{K_{j-1}} K_j$. As this holds for all $0 \le i \le n - 1$, $U_{j-1} \otimes_{K_{j-1}} K_j = K_j^n$, giving $\dim_{K_{j-1}}(U_{j-1}) = n$. By induction on $j$, $\dim_{K_j}(U_j) \ge \min(n, s + j - 1)$, reaching $n$ at $k_0 = n - s + 1$.

**(2)** For $k \ge k_0$, $\dim_{K_k}(U_k) = n$ means the dual map $\Omega^1_{\mathbb{A}^n / \Omega} \otimes_{\Omega[\mathbb{A}^n]} K_k \to \Omega^1_{K_k / \Omega}$, sending $dX_i \mapsto dx_{k,i}$, is injective, so $dx_{k,0}, \dots, dx_{k,n-1}$ are $K_k$-linearly independent in $\Omega^1_{K_k / \Omega}$.
- First, $x_{k,0}, \dots, x_{k,n-1}$ must be algebraically independent over $\Omega$: otherwise, choosing a nonzero polynomial relation $F(x_{k,0}, \dots, x_{k,n-1}) = 0$ of minimal total degree, $F$ has some nonzero partial derivative $\frac{\partial F}{\partial X_i} \not\equiv 0$ (in positive characteristic $p$, $F$ cannot be a $p$-th power in $\Omega[X_0, \dots, X_{n-1}]$ because $\Omega$ is algebraically closed and its $p$-th root would have smaller degree), whence $\frac{\partial F}{\partial X_i}(x_k) \neq 0$ by minimality, yielding a nontrivial relation $\sum_i \frac{\partial F}{\partial X_i}(x_k)\, dx_{k,i} = 0$, a contradiction. Thus $\varphi_k$ is dominant and $E_k = \Omega(x_k)$ has transcendence degree $n$ over $\Omega$.
- Second, in the exact sequence $\Omega^1_{E_k / \Omega} \otimes_{E_k} K_k \xrightarrow{\alpha} \Omega^1_{K_k / \Omega} \to \Omega^1_{K_k / E_k} \to 0$, $\alpha$ is injective, so
  $$\dim_{K_k} \Omega^1_{K_k / E_k} = \dim_{K_k} \Omega^1_{K_k / \Omega} - \dim_{E_k} \Omega^1_{E_k / \Omega} = ks - n = \mathrm{trdeg}_{E_k}(K_k).$$
  By Mac Lane's / Cartier's criterion (Matsumura, *Commutative Ring Theory*, Thm. 26.9), $K_k / E_k$ is **separably generated**.
- Hence there exists a transcendence basis $w_1, \dots, w_r$ ($r = ks - n$) of $K_k / E_k$ over which $K_k$ is finite separable. Every $\beta \in L_k$ has the same minimal polynomial over $E_k(w_1, \dots, w_r)$ as over $E_k$ (by Gauss's lemma for the purely transcendental extension $E_k(w_1, \dots, w_r)/E_k$), hence is separable over $E_k$. Since $K_k$ is finitely generated over $E_k$, $L_k / E_k$ is finite separable. Moreover, $K_k$ is finite separable over $L_k(w_1, \dots, w_r)$, so $K_k / L_k$ is separably generated with $L_k$ algebraically closed in $K_k$, i.e., $K_k / L_k$ is **regular**.

**(3)** Let $F := W_{k_0}(x_0) \times_{\mathbb{A}^n} \mathrm{Spec} \overline{E_{k_0}} \subset \mathbb{A}^{(k_0 - 1)n}_{\overline{E_{k_0}}}$ be the geometric generic fiber of $\varphi_{k_0}$. Because $L_{k_0} / E_{k_0}$ is finite separable of degree $d_{k_0}$ and $K_{k_0} / L_{k_0}$ is regular,
$$K_{k_0} \otimes_{E_{k_0}} \overline{E_{k_0}} \cong K_{k_0} \otimes_{L_{k_0}} \left(L_{k_0} \otimes_{E_{k_0}} \overline{E_{k_0}}\right) \cong \prod_{r=1}^{d_{k_0}} \left(K_{k_0} \otimes_{L_{k_0}, \iota_r} \overline{E_{k_0}}\right)$$
is a product of $d_{k_0}$ integral domains, so $F$ has exactly $d_{k_0}$ irreducible components. On the other hand, choosing a basis of $V^\perp$ expresses $F \subset \mathbb{A}^N_{\overline{E_{k_0}}}$ ($N := (k_0 - 1)n$) as the common zero locus of $m := k_0(n - s)$ quadratic polynomials $P_1, \dots, P_m$. Letting $Z \subset \mathbb{P}^N_{\overline{E_{k_0}}}$ be cut out by their homogenizations $\widetilde{P}_1, \dots, \widetilde{P}_m$ (of degree $2$), we have $Z \cap \mathbb{A}^N = F$, so the projective closures of the $d_{k_0}$ irreducible components of $F$ are distinct irreducible components of $Z_{\mathrm{red}}$. For any closed subscheme $X \subset \mathbb{P}^N$, set $\delta(X) := \sum_{C \in \mathrm{Irr}(X_{\mathrm{red}})} \deg(C)$. For any irreducible $A \subset \mathbb{P}^N$ and any quadric $H = \{\widetilde{P} = 0\}$, either $A \subseteq H$ (giving $\delta(A \cap H) = \deg A \le 2 \deg A$) or $A \not\subseteq H$, in which case Bézout's theorem (Hartshorne, *Algebraic Geometry*, Thm. I.7.7) gives $\sum_{C \in \mathrm{Irr}((A \cap H)_{\mathrm{red}})} i(A, H; C) \deg(C) = 2 \deg(A)$ with all $i(A, H; C) \ge 1$, so again $\delta(A \cap H) \le 2 \deg(A)$. Inducting over the $m$ quadrics yields $d_{k_0} \le |\mathrm{Irr}(Z_{\mathrm{red}})| \le \delta(Z) \le 2^m = 2^{k_0(n - s)}$. $\square$

### 4.4. Stein-Factorization Collapse ($d_K = 1$ at $K = (n - s + 1)^2$)

For every $k \ge k_0$, write $F_k := K_k = \Omega(W_k(x_0))$, $E_k := \Omega(x_k) \subseteq F_k$, $L_k$ for the algebraic closure of $E_k$ in $F_k$, and $d_k := [L_k : E_k]$. Also let $H := \Omega(R)$, containing both $E_k = \Omega(x)$ (via $p_1^*$) and $E_{k+1} = \Omega(y)$ (via $p_2^*$). Note that $W_{k+1}(x_0) = W_k(x_0) \times_{\mathbb{A}^n_{x_k}} R$.

**Lemma 4.4 (Divisibility $d_{k+1} \mid d_k$).** *For every $k \ge k_0$:*
1. *Both $H / E_k$ and $H / E_{k+1}$ are regular field extensions.*
2. *Inside $F_{k+1}$, the compositum $M := L_k \cdot H$ is canonically isomorphic to $L_k \otimes_{E_k} H$ (finite separable of degree $d_k$ over $H$) and is algebraically closed in $F_{k+1}$.*
3. *$L_{k+1} \subseteq M$, $L_{k+1} \cdot H \cong L_{k+1} \otimes_{E_{k+1}} H$, and $d_{k+1} \mid d_k$, with equality $d_{k+1} = d_k$ if and only if $L_{k+1} \cdot H = L_k \cdot H = M$.*

*Proof.*
**(1)** By Lemma 4.2(3), the geometric generic fiber $p_1^{-1}(\eta_{\mathbb{A}^n_x}) \times_{E_k} \overline{E_k} = N(\eta_{\mathbb{A}^n_x})_{\overline{E_k}}$ is integral, so $H \otimes_{E_k} \overline{E_k}$ (a localization of its coordinate ring) is an integral domain; thus $H / E_k$ is regular. By symmetry, $H / E_{k+1}$ is regular.

**(2)** Since $p_1 : R \to \mathbb{A}^n_x$ is flat and $\varphi_k : W_k(x_0) \to \mathbb{A}^n_x$ is dominant, both projections from $W_{k+1}(x_0) = W_k(x_0) \times_{\mathbb{A}^n_x} R$ to $W_k(x_0)$ and $R$ are dominant. Localizing $\Omega[W_{k+1}(x_0)] = \Omega[W_k(x_0)] \otimes_{\Omega[x_k]} \Omega[R]$ at the nonzero elements of $\Omega[W_k(x_0)]$ and $\Omega[R]$ gives an injection $F_k \otimes_{E_k} H \hookrightarrow F_{k+1}$ whose fraction field is $F_{k+1}$. Since $H / E_k$ is regular and $L_k / E_k$ is finite separable, $L_k \otimes_{E_k} H$ embeds into the integral domain $\overline{E_k} \otimes_{E_k} H$, hence is a field $M \cong L_k \cdot H$ finite separable of degree $d_k$ over $H$. Next, $F_k \otimes_{E_k} H \cong F_k \otimes_{L_k} M$. Since $F_k / L_k$ is regular (Lemma 4.3(2)), $F_k \otimes_{L_k} \overline{L_k}$ is an integral domain, and base-changing an integral variety over the algebraically closed field $\overline{L_k}$ to $\overline{M} \supseteq \overline{L_k}$ preserves integrality, so $F_k \otimes_{L_k} \overline{M} \cong (F_k \otimes_{L_k} \overline{L_k}) \otimes_{\overline{L_k}} \overline{M}$ is an integral domain. Therefore $F_{k+1} \otimes_M \overline{M}$ (a localization of $F_k \otimes_{L_k} \overline{M}$) is an integral domain, proving that $F_{k+1} / M$ is regular and hence $M$ is algebraically closed in $F_{k+1}$.

**(3)** Since $E_{k+1} \subset H \subset M$ and $M$ is algebraically closed in $F_{k+1}$, we obtain $L_{k+1} \subseteq M$. Because $H / E_{k+1}$ is regular and $L_{k+1} / E_{k+1}$ is finite algebraic, $L_{k+1}$ and $H$ are linearly disjoint over $E_{k+1}$, so $L_{k+1} \cdot H \cong L_{k+1} \otimes_{E_{k+1}} H$ has degree $[L_{k+1} \cdot H : H] = [L_{k+1} : E_{k+1}] = d_{k+1}$. From the tower $H \subseteq L_{k+1} \cdot H \subseteq M$ we get $d_k = [M : H] = [M : L_{k+1} \cdot H] \cdot d_{k+1}$, so $d_{k+1} \mid d_k$, with equality iff $L_{k+1} \cdot H = M = L_k \cdot H$. $\square$

We next record an elementary DVR base-change lemma that handles arbitrary (including wild or residue-inseparable) ramification in odd characteristic $p > 2$.

**Lemma 4.5 (DVR base-change invariance of étaleness).** *Let $\mathcal{O}_1 \to \mathcal{O}_2$ be a local homomorphism of discrete valuation rings with fraction fields $E \subseteq H$ and residue fields $k_1 \subseteq k_2$ such that: (a) a uniformizer $\varpi$ of $\mathcal{O}_1$ generates $\mathfrak{m}_{\mathcal{O}_2}$, and (b) $k_2 / k_1$ is regular (i.e., $\overline{k_1} \otimes_{k_1} k_2$ is an integral domain). Let $L / E$ be a finite separable field extension linearly disjoint from $H$ over $E$, so $M := L \otimes_E H$ is a field. Let $A_1$ be the integral closure of $\mathcal{O}_1$ in $L$, and $A_2$ be the integral closure of $\mathcal{O}_2$ in $M$. Then $A_2 = A_1 \otimes_{\mathcal{O}_1} \mathcal{O}_2$, and $\mathcal{O}_2 \to A_2$ is étale if and only if $\mathcal{O}_1 \to A_1$ is étale.*

*Proof.* Since $L / E$ is finite separable and $\mathcal{O}_1$ is a DVR, $A_1$ is a semi-local Dedekind domain (hence a PID) that is a finite free $\mathcal{O}_1$-module of rank $d := [L : E]$. Let $\mathfrak{P}_1, \dots, \mathfrak{P}_r$ be the maximal ideals of $A_1$, with generators $\mathfrak{P}_i = \pi_i A_1$, residue fields $\ell_i := A_1 / \mathfrak{P}_i$, and $\varpi A_1 = \prod_{i=1}^r \mathfrak{P}_i^{e_i}$. Set $B_2 := A_1 \otimes_{\mathcal{O}_1} \mathcal{O}_2$. Because $B_2$ is finite free of rank $d$ over $\mathcal{O}_2$, $B_2 \hookrightarrow B_2 \otimes_{\mathcal{O}_2} H = M$, so $B_2$ is a $1$-dimensional Noetherian integral domain finite over $\mathcal{O}_2$ with fraction field $M$.

Every maximal ideal of $B_2$ lies over $\varpi \mathcal{O}_2$, hence corresponds to a maximal ideal of
$$B_2 / \varpi B_2 \cong (A_1 / \varpi A_1) \otimes_{k_1} k_2 \cong \prod_{i=1}^r (A_1 / \mathfrak{P}_i^{e_i}) \otimes_{k_1} k_2.$$
For each $i$, the surjection $(A_1 / \mathfrak{P}_i^{e_i}) \otimes_{k_1} k_2 \twoheadrightarrow \ell_i \otimes_{k_1} k_2$ has nilpotent kernel $(\mathfrak{P}_i / \mathfrak{P}_i^{e_i}) \otimes_{k_1} k_2$. Since $\ell_i \subseteq \overline{k_1}$ is finite algebraic over $k_1$ and $\overline{k_1} \otimes_{k_1} k_2$ is an integral domain, $\ell_i \otimes_{k_1} k_2$ is a finite-dimensional $k_2$-subalgebra of a domain, hence a **field**. Thus each factor $(A_1 / \mathfrak{P}_i^{e_i}) \otimes_{k_1} k_2$ is local, and the maximal ideals of $B_2$ are precisely $\mathfrak{Q}_i := \mathfrak{P}_i B_2 = \pi_i B_2$ ($1 \le i \le r$). For each $i$, the $1$-dimensional Noetherian local domain $(B_2)_{\mathfrak{Q}_i}$ has principal nonzero maximal ideal $\pi_i (B_2)_{\mathfrak{Q}_i}$, hence is a DVR. Thus $B_2$ is normal, so $A_2 = B_2 = A_1 \otimes_{\mathcal{O}_1} \mathcal{O}_2$.

Finally, since $\mathcal{O}_1 \to A_1$ and $\mathcal{O}_2 \to A_2$ are finite free with separable generic fibers, $\mathcal{O}_2 \to A_2$ is étale $\iff$ the special fiber $A_2 / \varpi A_2 \cong (A_1 / \varpi A_1) \otimes_{k_1} k_2$ is finite étale over $k_2$ $\iff$ $((A_1 / \varpi A_1) \otimes_{k_1} \overline{k_1}) \otimes_{\overline{k_1}} \overline{k_2}$ is reduced $\iff$ $(A_1 / \varpi A_1) \otimes_{k_1} \overline{k_1}$ is reduced $\iff$ $A_1 / \varpi A_1$ is finite étale over $k_1$ $\iff$ $\mathcal{O}_1 \to A_1$ is étale. $\square$

**Lemma 4.6 (Unramifiedness and coordinate-line triviality under stagnation).** *Suppose $k \ge k_0$ satisfies $d_{k+1} = d_k =: d$, so $L_{k+1} \cdot H = L_k \cdot H = M$. Let $Y_k \to \mathbb{A}^n_x$, $Y_{k+1} \to \mathbb{A}^n_y$, and $Z \to R$ be the normalizations of $\mathbb{A}^n_x$, $\mathbb{A}^n_y$, and $R$ in $L_k$, $L_{k+1}$, and $M$, respectively. Then:*
1. *$Y_k \to \mathbb{A}^n_x$ and $Y_{k+1} \to \mathbb{A}^n_y$ are connected finite étale covers of degree $d$, and $Y_k \times_{\mathbb{A}^n_x} R \cong Z \cong Y_{k+1} \times_{\mathbb{A}^n_y} R$ as finite étale covers of $R$.*
2. *For every point $y^* \in \Omega^n$ and every coordinate index $i \in \{0, \dots, n - 1\}$, the restriction $Y_{k+1}|_{L_{y^*, i}} \to L_{y^*, i} \cong \mathbb{A}^1_T$ to the coordinate line $L_{y^*, i} := \{(y^*_0, \dots, y^*_{i-1}, T, y^*_{i+1}, \dots, y^*_{n-1})\}$ is trivial (isomorphic to $\bigsqcup_{r=1}^d \mathbb{A}^1_T$).*

*Proof.* Since $L_k / E_k$, $L_{k+1} / E_{k+1}$, and $M / H$ are finite separable, $Y_k \to \mathbb{A}^n_x$, $Y_{k+1} \to \mathbb{A}^n_y$, and $Z \to R$ are finite surjective morphisms of normal integral varieties, generically étale of degree $d$.

**(1) Unramifiedness.** Let $B_{k+1} \subsetneq \mathbb{A}^n_y$ be the branch locus of $\psi_{k+1} : Y_{k+1} \to \mathbb{A}^n_y$ (points of $\mathbb{A}^n_y$ over which $\psi_{k+1}$ fails to be étale), and $B_k \subsetneq \mathbb{A}^n_x$ be the branch locus of $\psi_k : Y_k \to \mathbb{A}^n_x$. Because $\mathbb{A}^n_y$ is smooth, $Y_{k+1}$ is normal, and $L_{k+1} / E_{k+1}$ is separable, **Zariski–Nagata purity of the branch locus** (SGA 1, Exp. X, Thm. 3.1) implies that $B_{k+1}$ is either empty or of pure codimension $1$ in $\mathbb{A}^n_y$ (and similarly for $B_k$).

Let $B_Z^{(1)} \subset R$ be the union of all codimension-$1$ prime divisors $D \subset R$ at whose generic point $\eta_D$ the finite morphism $Z \to R$ fails to be étale. We prove $B_Z^{(1)} = p_2^{-1}(B_{k+1})$:
- Over $U := \mathbb{A}^n_y \setminus B_{k+1}$, the base change $Y_{k+1}|_U \times_U p_2^{-1}(U) \to p_2^{-1}(U)$ is finite étale over the normal integral variety $p_2^{-1}(U)$, hence normal, and its generic fiber over $\mathrm{Spec} H$ is $L_{k+1} \otimes_{E_{k+1}} H = M$ (a field), so it is integral and equals $Z|_{p_2^{-1}(U)}$. Thus $Z \to R$ is étale over $p_2^{-1}(U)$, whence no prime divisor $D$ with $p_2(\eta_D) \in U$ lies in $B_Z^{(1)}$.
- Conversely, let $B_0 \subset B_{k+1}$ be any irreducible component (a hypersurface $\{f = 0\}$ in $\mathbb{A}^n_y$). Since $p_2 : R \to \mathbb{A}^n_y$ is flat, no height-$1$ prime of $\Omega[R]$ can lie over a prime of height $\ge 2$ in $\Omega[y]$ (by the flat dimension formula, Matsumura Thm. 15.1). By Krull's principal ideal theorem, every irreducible component of $p_2^{-1}(B_0) = \{p_2^*(f) = 0\}$ has codimension $1$ in $R$, hence dominates $B_0$. Since the fiber $p_2^{-1}(\eta_{B_0})$ is geometrically integral (Lemma 4.2(3)), $D := p_2^{-1}(B_0)$ is **irreducible** of codimension $1$ in $R$. Moreover, $\mathcal{O}_1 := \mathcal{O}_{\mathbb{A}^n_y, \eta_{B_0}} \to \mathcal{O}_2 := \mathcal{O}_{R, \eta_D}$ is a local homomorphism of DVRs (since $R$ is normal!) for which a uniformizer $\varpi$ of $\mathcal{O}_1$ satisfies $\mathcal{O}_2 / \varpi \mathcal{O}_2 = \kappa(D)$ (the function field of the reduced fiber $N(\eta_{B_0})$), so $\varpi \mathcal{O}_2 = \mathfrak{m}_{\mathcal{O}_2}$, and $\kappa(D)/\kappa(B_0)$ is regular (since $N(\eta_{B_0})$ is geometrically integral over $\kappa(B_0)$). Applying Lemma 4.5, since $\mathcal{O}_1 \to \mathcal{O}_{Y_{k+1}} \otimes_{\mathcal{O}_{\mathbb{A}^n_y}} \mathcal{O}_1$ is not étale, $\mathcal{O}_2 \to \mathcal{O}_Z \otimes_{\mathcal{O}_R} \mathcal{O}_2$ is not étale, so $D \subseteq B_Z^{(1)}$.

Thus $B_Z^{(1)} = p_2^{-1}(B_{k+1})$, and by the exact same argument on $p_1$, $B_Z^{(1)} = p_1^{-1}(B_k)$.

Now, for each $i \in \{0, \dots, n - 1\}$, consider the involutive automorphism $\tau_i : R \xrightarrow{\sim} R$ defined by $\tau_i(x, y) := (x, y^{(i, x)})$, where $(y^{(i, x)})_i := -b_i x_i - y_i$ and $(y^{(i, x)})_m := y_m$ for $m \neq i$ (direct check: $Q_{b_i}(x_i, -b_i x_i - y_i) = Q_{b_i}(x_i, y_i)$). Since $p_1 \circ \tau_i = p_1$, the pullback $\tau_i^* \in \mathrm{Aut}(H)$ fixes $E_k$ pointwise, so $\mathrm{id}_{L_k} \otimes \tau_i^*$ is a field automorphism of $M \cong L_k \otimes_{E_k} H$ extending $\tau_i^*$. Hence $\tau_i$ lifts to an automorphism of the normalization $Z \to R$, and therefore preserves the intrinsic codimension-$1$ branch locus $B_Z^{(1)} = p_2^{-1}(B_{k+1})$.

Suppose $B_{k+1} \neq \emptyset$, and pick $y \in B_{k+1}(\Omega)$. For any coordinate $i \in \{0, \dots, n - 1\}$ and any scalar $w \in \Omega$, set $x_i := -(w + y_i)/b_i \in \Omega$; since $L_i \not\equiv 0$, choose $t \in \Omega^s$ with $L_i(t) = (x_i + \frac{b_i}{2} y_i)^2 - \Delta_i y_i^2$, and since $\Omega$ is algebraically closed, choose $x_m \in \Omega$ ($m \neq i$) solving $(x_m + \frac{b_m}{2} y_m)^2 = \Delta_m y_m^2 + L_m(t)$. Then $(x, y) \in R(\Omega)$ lies in $p_2^{-1}(B_{k+1})$, so $\tau_i(x, y) \in p_2^{-1}(B_{k+1})$, whence $y^{(i, x)} = (y_0, \dots, y_{i-1}, w, y_{i+1}, \dots, y_{n-1}) \in B_{k+1}(\Omega)$. Changing coordinates $i = 0, \dots, n - 1$ sequentially forces $B_{k+1} = \mathbb{A}^n_y$, contradicting $B_{k+1} \subsetneq \mathbb{A}^n_y$. Therefore $B_{k+1} = \emptyset$, hence $B_Z^{(1)} = \emptyset$, and since $p_1 : R \to \mathbb{A}^n_x$ is surjective (every $N(x)$ is nonempty), $B_k = \emptyset$ as well.

Thus $\psi_k : Y_k \to \mathbb{A}^n_x$ and $\psi_{k+1} : Y_{k+1} \to \mathbb{A}^n_y$ are connected finite étale covers of degree $d$. Both $Y_k \times_{\mathbb{A}^n_x} R$ and $Y_{k+1} \times_{\mathbb{A}^n_y} R$ are finite étale over the normal integral variety $R$ (hence normal) with generic fiber $\mathrm{Spec} M$ over $\mathrm{Spec} H$ (hence integral), so both are canonically isomorphic to the normalization $Z$ of $R$ in $M$.

**(2) Coordinate-line triviality.** Fix $y^* \in \Omega^n$ and $i \in \{0, \dots, n - 1\}$. Restricting the isomorphism $Y_k \times_{\mathbb{A}^n_x} R \cong Y_{k+1} \times_{\mathbb{A}^n_y} R$ to $p_2^{-1}(y^*) = N(y^*) \times \{y^*\} \subset R$ gives
$$Y_k \times_{\mathbb{A}^n_x} N(y^*) \;\cong\; \psi_{k+1}^{-1}(y^*) \times_\Omega N(y^*) \;\cong\; \bigsqcup_{r=1}^d N(y^*)$$
(since $\Omega$ is algebraically closed). Now pull back the same isomorphism along the morphism $g : N(y^*) \to R$ given by $g(x) := \tau_i(x, y^*) = (x, y^{*(i, x)})$. Because $p_1 \circ g$ is the inclusion $N(y^*) \hookrightarrow \mathbb{A}^n_x$ while $p_2 \circ g$ factors through $L_{y^*, i} \cong \mathbb{A}^1_T$ via $h : N(y^*) \to \mathbb{A}^1_T$, $h(x) := -b_i x_i - y^*_i$, we obtain an isomorphism of finite étale covers of $N(y^*)$:
$$Y_{k+1}|_{L_{y^*, i}} \times_{\mathbb{A}^1_T} N(y^*) \;\cong\; Y_k \times_{\mathbb{A}^n_x} N(y^*) \;\cong\; \bigsqcup_{r=1}^d N(y^*).$$

Let $C_0$ be any connected component of $Y_{k+1}|_{L_{y^*, i}}$ (a smooth irreducible affine curve, finite étale over $\mathbb{A}^1_T$ of degree $e := \deg(C_0 / \mathbb{A}^1_T) \ge 1$). Then $C_0 \times_{\mathbb{A}^1_T} N(y^*) \to N(y^*)$ is a trivial finite étale cover of $N(y^*)$, so it admits a section, inducing an $\Omega(T)$-algebra embedding of function fields:
$$K(C_0) \hookrightarrow \Omega(N(y^*)).$$
On $N(y^*)$, change linear coordinates on $\mathbb{A}^s_t$ so that $L_i(t) = t_1$. Setting $u_m := x_m + \frac{b_m}{2} y^*_m$, we have $T = -b_i x_i - y^*_i = -b_i u_i + (\frac{b_i^2}{2} - 1) y^*_i$, so $u_i \in \Omega[T]$ (as $b_i \neq 0$) and $t_1 = u_i^2 - \Delta_i (y^*_i)^2 \in \Omega[T]$. The remaining $n - 1$ defining equations of $N(y^*)$ become
$$u_m^2 = g_m(T, t_2, \dots, t_s) := \Delta_m (y^*_m)^2 + L_m\bigl(t_1(T), t_2, \dots, t_s\bigr) \qquad (m \neq i).$$
Let $F := \Omega(T, t_2, \dots, t_s) \subseteq \Omega(N(y^*))$. Since $\Omega(N(y^*))$ is algebraic over $F$ and $\mathrm{trdeg}_\Omega \Omega(N(y^*)) = \dim N(y^*) = s$ (Lemma 4.2(1)), the $s$ elements $T, t_2, \dots, t_s$ are **algebraically independent** over $\Omega$. Moreover, $\Omega(N(y^*)) = F(u_m : m \neq i)$ is generated over $F$ by $n - 1$ square roots in characteristic $\neq 2$, so by Kummer theory $\Omega(N(y^*)) / F$ is an **abelian Galois extension** with Galois group $\cong (\mathbb{Z}/2\mathbb{Z})^r$ for some $r \le n - 1$.

Consider the intermediate field $K' := K(C_0)(t_2, \dots, t_s)$ with $F \subseteq K' \subseteq \Omega(N(y^*))$. Because $\mathrm{Gal}(\Omega(N(y^*)) / F) \cong (\mathbb{Z}/2\mathbb{Z})^r$ is abelian, $K' / F$ is Galois with $\mathrm{Gal}(K' / F) \cong (\mathbb{Z}/2\mathbb{Z})^m$ for some $m \le r$. Since $t_2, \dots, t_s$ are algebraically independent over $\Omega(T)$ and $K(C_0) / \Omega(T)$ is algebraic, $t_2, \dots, t_s$ are algebraically independent over $K(C_0)$; hence $[K' : F] = [K(C_0) : \Omega(T)] = e$, and $K(C_0)$ is the algebraic closure of $\Omega(T)$ in $K'$. Thus every $\sigma \in \mathrm{Gal}(K' / F)$ preserves $K(C_0)$, and restriction $\sigma \mapsto \sigma|_{K(C_0)}$ is injective (since $\sigma$ fixes $t_2, \dots, t_s$). Therefore $K(C_0) / \Omega(T)$ is Galois with $\mathrm{Gal}(K(C_0)/\Omega(T)) \cong (\mathbb{Z}/2\mathbb{Z})^m$.

Suppose $m \ge 1$. Then $K(C_0)$ contains a quadratic subextension $K_1 / \Omega(T)$. Since $\mathrm{char}(\Omega) \neq 2$ and $\Omega$ is algebraically closed, $K_1 = \Omega(T)(\sqrt{f(T)})$ for a squarefree non-constant polynomial $f(T) \in \Omega[T]$. Pick a root $T_0 \in \Omega$ of $f(T)$. Let $R_0 := \Omega[T]_{(T - T_0)}$, let $S := \mathcal{O}(C_0) \otimes_{\Omega[T]} R_0$ (which is finite étale over $R_0$), and let $S_1 := S \cap K_1$ be the integral closure of $R_0$ in $K_1$. Choosing a maximal ideal $\mathfrak{q}$ of $S_1$ over $(T - T_0) R_0$ and a maximal ideal $\mathfrak{Q}$ of $S$ over $\mathfrak{q}$, étaleness of $R_0 \to S$ gives $e(\mathfrak{Q} / (T - T_0)) = 1$, forcing $e(\mathfrak{q} / (T - T_0)) = 1$. Yet $(\sqrt{f})^2 = f = (T - T_0) u$ ($u \in R_0^*$) implies $2 v_{\mathfrak{q}}(\sqrt{f}) = v_{\mathfrak{q}}(T - T_0) = e(\mathfrak{q}/(T - T_0)) = 1$, a contradiction. Thus $m = 0$, so $e = 1$ for every connected component $C_0$, proving that $Y_{k+1}|_{L_{y^*, i}} \cong \bigsqcup_{r=1}^d \mathbb{A}^1_T$. $\square$

**Lemma 4.7 (Coordinate-line triviality on $\mathbb{A}^n$ forces $d = 1$).** *Let $\Omega$ be an algebraically closed field (of arbitrary characteristic), $n \ge 1$, and $f : Y \to \mathbb{A}^n_\Omega$ a connected finite étale cover of degree $d \ge 1$ whose pullback to every closed-point coordinate line $L_{y^*, i}$ ($y^* \in \Omega^n$, $0 \le i \le n - 1$) is trivial. Then $d = 1$.*

*Proof.* We induct on $n$. For $n = 1$, $Y = Y|_{L_{0, 0}} \cong \bigsqcup_{r=1}^d \mathbb{A}^1_\Omega$; connectedness forces $d = 1$.

Now let $n \ge 2$, write $\mathbb{A}^n_\Omega = \mathrm{Spec} \Omega[Y_0, Y']$ with $Y' := (Y_1, \dots, Y_{n-1})$, and write $Y = \mathrm{Spec} B$ with fraction field $L := \mathrm{Frac}(B)$. Set $K_0 := \Omega(Y_1, \dots, Y_{n-1})$, and consider the finite étale cover of the generic $Y_0$-line:
$$Y_{\overline{\eta}} := Y \times_{\mathbb{A}^n_\Omega} \mathrm{Spec} \overline{K_0}[Y_0] \to \mathbb{A}^1_{\overline{K_0}}.$$
Decompose $Y_{\overline{\eta}} = \bigsqcup_{r=1}^c C_r$ into its connected components ($1 \le c \le d$), where each $C_r$ is a smooth irreducible affine curve over $\overline{K_0}$. The corresponding orthogonal idempotents of $B \otimes_{\Omega[Y']} \overline{K_0}$ are defined over a finite extension $K_1 / K_0$ inside $\overline{K_0}$. Choosing a nonzero $g \in \Omega[Y']$ and a finitely generated $\Omega[Y'][g^{-1}]$-subalgebra $A_S \subset K_1$ finite over $\Omega[Y'][g^{-1}]$ with $\mathrm{Frac}(A_S) = K_1$ containing all coefficients of these idempotents, we obtain a finite surjective morphism $S := \mathrm{Spec} A_S \to D(g) \subseteq \mathbb{A}^{n-1}_{Y'}$ and a decomposition $Y \times_{\mathbb{A}^{n-1}} S = \bigsqcup_{r=1}^c \mathcal{C}_r$ whose generic fiber over $\mathrm{Spec} K_1$ is $\bigsqcup_{r=1}^c C_r$ (each $C_r$ geometrically integral over $K_1$). By constructibility of geometrically integral fibers (EGA IV$_3$, Thm. 9.7.7(iv)), for each $r$ there is a nonempty open subset $S_r \subseteq S$ over which every fiber of $\mathcal{C}_r \to S$ is geometrically integral (hence nonempty and connected). By Hilbert's Nullstellensatz, $\bigcap_{r=1}^c S_r$ contains a closed point $s \in S(\Omega)$, mapping to $y^* \in \mathbb{A}^{n-1}(\Omega)$ with $\kappa(s) = \Omega = \kappa(y^*)$. Then $Y_{y^*} := Y \times_{\mathbb{A}^{n-1}} \{y^*\} = \bigsqcup_{r=1}^c (\mathcal{C}_r)_s$ has exactly $c$ connected components, whereas by hypothesis $Y_{y^*} \cong \bigsqcup_{r=1}^d \mathbb{A}^1_\Omega$ has $d$ connected components. Hence $c = d$, so each $C_r \cong \mathbb{A}^1_{\overline{K_0}}$ and $B \otimes_{\Omega[Y']} \overline{K_0} \cong \prod_{r=1}^d \overline{K_0}[Y_0]$.

Set $B_{K_0} := B \otimes_{\Omega[Y']} K_0$, which is finite over $K_0[Y_0]$ with fraction field $L = B_{K_0} \otimes_{K_0[Y_0]} K_0(Y_0)$. Localizing the isomorphism $B_{K_0} \otimes_{K_0} \overline{K_0} \cong \prod_{r=1}^d \overline{K_0}[Y_0]$ at $K_0[Y_0] \setminus \{0\}$ (and noting that every nonzero polynomial in $\overline{K_0}[Y_0]$ divides a nonzero polynomial in $K_0[Y_0]$) gives
$$L \otimes_{K_0} \overline{K_0} \;\cong\; \prod_{r=1}^d \overline{K_0}(Y_0).$$
Let $M_0$ be the algebraic closure of $K_0$ in $L$. Since $L / K_0(Y_0)$ is finite separable of degree $d$ and $K_0(Y_0)/K_0$ is purely transcendental, $M_0 / K_0$ is finite separable of degree $m := [M_0 : K_0] \le d$, and $L / M_0$ is regular (as $L / M_0(Y_0)$ is finite separable). Hence $L \otimes_{K_0} \overline{K_0} \cong \prod_{j=1}^m (L \otimes_{M_0, \iota_j} \overline{K_0})$ is a product of $m$ integral domains. Comparing the number of primitive idempotents yields $m = d$, whence $[M_0(Y_0) : K_0(Y_0)] = d = [L : K_0(Y_0)]$ and thus $L = M_0(Y_0)$.

Let $B_0$ be the integral closure of $\Omega[Y']$ in $M_0$. Since $B_0$ is integrally closed in $M_0$, $B_0[Y_0]$ is integrally closed in $M_0(Y_0) = L$ and integral over $\Omega[Y_0, Y']$; since $B$ is also normal and integral over $\Omega[Y_0, Y']$ with fraction field $L$, we conclude $B = B_0[Y_0]$. Reducing modulo $Y_0$ gives $B / Y_0 B \cong B_0$, so $Y' := \mathrm{Spec} B_0 \to \mathbb{A}^{n-1}_{Y'}$ is a connected finite étale cover of degree $d$ (base change of $Y \to \mathbb{A}^n_\Omega$ along $\{Y_0 = 0\}$). Every coordinate line in $\mathbb{A}^{n-1}_{Y'}$ embeds into $\{Y_0 = 0\} \subset \mathbb{A}^n_\Omega$ as a coordinate line, so $Y'$ is trivial on every coordinate line of $\mathbb{A}^{n-1}_{Y'}$. By the induction hypothesis, $d = 1$. $\square$

**Proposition 4.8 (Geometric integrality of the generic $K$-walk fiber).** *Set $K := k_0 + k_0(n - s) = (n - s + 1)^2$. Then in the abstract geometric setting of Section 4.1 (over any algebraically closed field $\Omega$ of characteristic $\neq 2$), $d_K = 1$, and the generic fiber of $\varphi_K : W_K(x_0) \to \mathbb{A}^n_\Omega$ is **geometrically integral of dimension $Ks - n$**.*

*Proof.* By Lemmas 4.4, 4.6, and 4.7, for every $k \ge k_0$ with $d_k > 1$ we cannot have $d_{k+1} = d_k$, while $d_{k+1} \mid d_k$; hence $d_{k+1} \le d_k / 2$. Since $d_{k_0} \le 2^{k_0(n - s)}$ by Lemma 4.3(3), after at most $k_0(n - s)$ steps we must reach $d_K = 1$. Thus $E_K$ is algebraically closed in $F_K$; combined with Lemma 4.3(2), $F_K / E_K$ is a regular field extension of transcendence degree $Ks - n$. Consequently, the coordinate ring of the geometric generic fiber $W_K(x_0) \times_{\mathbb{A}^n} \mathrm{Spec} \overline{E_K}$ embeds into the integral domain $F_K \otimes_{E_K} \overline{E_K}$, hence is an integral domain of Krull dimension $Ks - n$. $\square$

### 4.5. Uniformity over $\mathbb{Z}[\frac{1}{2}]$, Schwartz–Zippel, and Lang–Weil

**Theorem 4.9 (Connectedness for odd $n \ge 5$ and $b \in \mathbb{F}_{q^n}^* \setminus \{2, -2\}$).** *For every odd integer $n \ge 5$, set $s := \frac{n}{p_0(n)} + 1$ and $K := (n - s + 1)^2$. There exists $q_0'(n)$ such that for every odd prime power $q \ge q_0'(n)$, every $\mathbb{F}_q$-vector subspace $V \subsetneq \mathbb{F}_{q^n}$ of dimension $s$, and every $b \in \mathbb{F}_{q^n}^* \setminus \{2, -2\}$, the graph $\Gamma(Q_b, V)$ is connected (and in fact has diameter at most $2K$).*

*Proof.* Define the finite-type Noetherian parameter scheme over $\mathbb{Z}[\frac{1}{2}]$:
$$\mathcal{S} := (\mathbb{G}_m \setminus \{2, -2\})^n_{\mathbb{Z}[1/2]} \times_{\mathbb{Z}[1/2]} U_{s,n} \times_{\mathbb{Z}[1/2]} \mathbb{A}^n_{\mathbb{Z}[1/2]},$$
where $U_{s,n} \subset \mathbb{A}^{sn}_{\mathbb{Z}[1/2]}$ is the open subscheme of $n \times s$ matrices $M$ of rank $s$ (at least one $s \times s$ minor invertible) whose rows are pairwise linearly independent (for each $0 \le i < j \le n - 1$, at least one $2 \times 2$ minor of rows $(i, j)$ is invertible). Over $\mathcal{S} \times_{\mathbb{Z}[1/2]} \mathbb{A}^n_y$, define the universal $K$-walk scheme $\mathcal{W}_K \subset \mathcal{S} \times \mathbb{A}^n_y \times (\mathbb{A}^n)^{K-1} \times (\mathbb{A}^s)^K$ (with $x_K := y$) by the $Kn$ equations
$$x_{j-1,i}^2 + b_i x_{j-1,i} x_{j,i} + x_{j,i}^2 = \sum_{r=1}^s M_{i,r} t^{(j)}_r \qquad (1 \le j \le K,\ 0 \le i \le n - 1),$$
and let $\Phi : \mathcal{W}_K \to \mathcal{S} \times \mathbb{A}^n_y$ be the projection (a morphism of finite presentation between Noetherian schemes).

By EGA IV$_3$, Theorem 9.7.7(iv) and Corollary 9.5.6 (constructibility of the loci of geometrically integral fibers and of fibers of fixed dimension $r := Ks - n$), the set
$$\mathcal{U} := \bigl\{z \in \mathcal{S} \times \mathbb{A}^n_y : \Phi^{-1}(z) \text{ is geometrically integral of dimension } r\bigr\}$$
is constructible in $\mathcal{S} \times \mathbb{A}^n_y$, and so is its complement $\mathcal{Z} := (\mathcal{S} \times \mathbb{A}^n_y) \setminus \mathcal{U}$.

**Step 1 (Uniform degree bound on the bad locus by Noetherian induction).** For every scheme-theoretic point $\tau \in \mathcal{S}$, the algebraic closure $\Omega := \overline{\kappa(\tau)}$ has characteristic $\neq 2$ (as $\mathcal{S}$ lies over $\mathbb{Z}[\frac{1}{2}]$), so Proposition 4.8 applies to the geometric point $\tau \in \mathcal{S}(\Omega)$ and shows that the generic point of $\{\tau\} \times \mathbb{A}^n_y$ lies in $\mathcal{U}$ (not in $\mathcal{Z}$). Hence for every nonempty irreducible closed subscheme $T \subseteq \mathcal{S}$ with generic point $\tau$, the constructible fiber $\mathcal{Z}_\tau \subset \mathbb{A}^n_{\kappa(\tau)}$ has proper Zariski closure, so there exists a nonzero polynomial $F_\tau \in \kappa(\tau)[y_0, \dots, y_{n-1}]$ of some degree $d_T$ vanishing on $\mathcal{Z}_\tau$. Clearing denominators over a nonempty affine open $T' = \mathrm{Spec} A' \subseteq T$ and inverting one nonzero coefficient of $F$ gives $F \in A'[y_0, \dots, y_{n-1}]$ of degree $d_T$ whose specialization $F_s \in \kappa(s)[y_0, \dots, y_{n-1}]$ is **nonzero** for every $s \in T'$. Now $B_F := \mathcal{Z} \cap (T' \times \mathbb{A}^n_y) \cap D(F)$ is constructible with empty fiber over $\tau$; by Chevalley's theorem (EGA IV$_1$, Thm. 1.8.4), $\mathrm{pr}_1(B_F) \subseteq T'$ is constructible and misses $\tau$, so $T'' := T' \setminus \overline{\mathrm{pr}_1(B_F)}$ is a nonempty open subset of $T$ over which $\mathcal{Z}_s \subseteq \{F_s = 0\}$ for every $s \in T''$. By Noetherian induction on $\mathcal{S}$, finitely many such pieces $T''_1, \dots, T''_N$ cover $\mathcal{S}$, giving a constant $D_0(n) := \max_j d_{T_j}$ depending only on $n$ such that for every algebraically closed field $\Omega$ of characteristic $\neq 2$ and every $\xi \in \mathcal{S}(\Omega)$, there exists a nonzero polynomial $F_\xi \in \Omega[y_0, \dots, y_{n-1}]$ of total degree $\le D_0(n)$ vanishing on $\mathcal{Z}_\xi(\Omega)$.

**Step 2 (Counting bad endpoints via Schwartz–Zippel).** Now take any odd prime power $q$, any $s$-dimensional subspace $V \subset \mathbb{F}_{q^n}$, any $b \in \mathbb{F}_{q^n}^* \setminus \{2, -2\}$, and any $x_0 \in \mathbb{F}_{q^n}$. By Lemma 4.1, diagonalization via $\iota$ yields a geometric point $\xi = (\iota(b), M, \iota(x_0)) \in \mathcal{S}(\overline{\mathbb{F}_q})$ and a nonzero polynomial $F_\xi \in \overline{\mathbb{F}_q}[y_0, \dots, y_{n-1}]$ of total degree $\le D_0(n)$ vanishing on $\mathcal{Z}_\xi(\overline{\mathbb{F}_q})$. Fixing an $\mathbb{F}_q$-basis of $\mathbb{F}_{q^n} \cong \mathbb{F}_q^n$, the pullback $\widetilde{F}(\alpha_0, \dots, \alpha_{n-1}) := F_\xi(\iota(\alpha_0, \dots, \alpha_{n-1})) \in \overline{\mathbb{F}_q}[\alpha_0, \dots, \alpha_{n-1}]$ is nonzero of total degree $\le D_0(n)$ (because $\iota$ is an invertible linear transformation over $\overline{\mathbb{F}_q}$). By the Schwartz–Zippel lemma over the grid $\mathbb{F}_q^n \subset \overline{\mathbb{F}_q}^n$, at most $D_0(n) q^{n-1}$ vertices $y \in \mathbb{F}_{q^n}$ satisfy $\widetilde{F}(y) = 0$. In particular, at least $q^n - D_0(n) q^{n-1}$ vertices $y \in \mathbb{F}_{q^n}$ satisfy $(\xi, \iota(y)) \in \mathcal{U}$.

**Step 3 (Point counting on good fibers via Lang–Weil).** For any vertex $y \in \mathbb{F}_{q^n}$ with $(\xi, \iota(y)) \in \mathcal{U}$, let $X_y \subset \mathbb{A}^N_{\mathbb{F}_q}$ ($N := (K - 1)n$) be the affine $\mathbb{F}_q$-variety of tuples $(x_1, \dots, x_{K-1}) \in (\mathbb{F}_{q^n})^{K-1}$ satisfying $Q_b(x_{j-1}, x_j) \in V$ for $1 \le j \le K$ (with $x_K = y$), defined over $\mathbb{F}_q$ by $m := K(n - s)$ quadratic polynomials (applying an $\mathbb{F}_q$-basis of $V^\perp$ to each $Q_b(x_{j-1}, x_j)$). Since $M$ has rank $s$, eliminating $t^{(1)}, \dots, t^{(K)}$ linearly identifies $X_y \times_{\mathbb{F}_q} \overline{\mathbb{F}_q} \cong \Phi^{-1}(\xi, \iota(y))$, so $X_y$ is **geometrically integral of dimension $r = Ks - n \ge 3$** (note $k_0 s - n = (s - 1)(n - s) \ge 3$ for all odd $n \ge 5$, and $K > k_0$).

Let $\overline{X_y} \subset \mathbb{P}^N_{\mathbb{F}_q}$ be the projective closure of $X_y$. Just as in Lemma 4.3(3), $\overline{X_y}$ is an irreducible component of the intersection of $m = K(n - s)$ quadrics in $\mathbb{P}^N$, so $D := \deg(\overline{X_y}) \le 2^{K(n - s)}$. Moreover, since $X_y$ is irreducible and not contained in the hyperplane at infinity $H_\infty := \mathbb{P}^N \setminus \mathbb{A}^N$, the boundary $\overline{X_y} \cap H_\infty$ has pure dimension $r - 1$ and total degree $\le D$ (Hartshorne Thm. I.7.7), so by the uniform upper bound of Lang–Weil (1954, Lemma 1) we have $\#(\overline{X_y} \cap H_\infty)(\mathbb{F}_q) \le C_1(N, r, D) q^{r - 1}$ (in fact $\le 2 D q^{r - 1}$). Applying Lang–Weil (1954, Theorem 1) to $\overline{X_y}$ yields
$$\#X_y(\mathbb{F}_q) = \#\overline{X_y}(\mathbb{F}_q) - \#(\overline{X_y} \cap H_\infty)(\mathbb{F}_q) \ge q^r - (D - 1)(D - 2) q^{r - 1/2} - C_2(N, r, D) q^{r - 1},$$
where $N, r$, and the upper bound $2^{K(n - s)}$ on $D$ depend **only on $n$**. Hence there exists $q_1(n)$ depending only on $n$ such that $\#X_y(\mathbb{F}_q) > 0$ for every odd prime power $q \ge q_1(n)$ and every good vertex $y \in \mathbb{F}_{q^n}$.

**Step 4 (Connectedness and diameter).** Any point $(x_1, \dots, x_{K-1}) \in X_y(\mathbb{F}_q)$ gives a sequence $x_0, x_1, \dots, x_K = y$ in $\mathbb{F}_{q^n}$ with $Q_b(x_{j-1}, x_j) \in V$ for all $1 \le j \le K$. Deleting consecutive duplicate vertices produces a valid walk in $\Gamma(Q_b, V)$ from $x_0$ to $y$ of length $\le K$. Therefore, for every vertex $x_0 \in \mathbb{F}_{q^n}$ and every $q \ge q_1(n)$, the $K$-ball $B_K(x_0)$ (and hence the connected component of $x_0$) has size
$$\#B_K(x_0) \ge q^n - D_0(n) q^{n-1}.$$
Setting $q_0'(n) := \max\bigl(q_1(n),\, 2 D_0(n) + 1\bigr)$, for every odd prime power $q \ge q_0'(n)$ and every pair of vertices $u, v \in \mathbb{F}_{q^n}$, we have $\#B_K(u) > \frac{1}{2} q^n$ and $\#B_K(v) > \frac{1}{2} q^n$, so $B_K(u) \cap B_K(v) \neq \emptyset$. Thus $\Gamma(Q_b, V)$ is connected of diameter $\le 2K$. $\square$

---

## Proof of the Main Theorem (Synthesis)

- **Lower bound ($s(n) \ge \frac{n}{p_0(n)} + 1$ for all $n \ge 4$):** Proved in Section 1 (Cases 1a and 1b) for every odd prime power $q \ge 3$.
- **Upper bound for even $n \ge 4$:** Proved in Proposition 2.3 for every odd prime power $q \ge 5$ and every $b \in \mathbb{F}_{q^n}^*$.
- **Upper bound for odd $n \ge 5$:** Set $q_0(n) := \max\bigl(q_0'(n),\, \lfloor (n - 1 + 2^{(n-1)/2})^2 \rfloor + 1\bigr)$ (noting that $q > (n - 1 + 2^{(n-1)/2})^2 \implies \sqrt{q} > n - 1 + 2^{(n-1)/2} \implies q - (n-1)\sqrt{q} > 2^{(n-1)/2}\sqrt{q} > 2^{n-1}$). For every odd prime power $q \ge q_0(n)$, every proper $\mathbb{F}_q$-subspace $V \subsetneq \mathbb{F}_{q^n}$ with $\#V \ge q^{n/p_0(n) + 1}$, and every $b \in \mathbb{F}_{q^n}^*$:
  - if $b \in \{2, -2\}$, $\Gamma(Q_b, V)$ is connected by Proposition 3.2;
  - if $b \in \mathbb{F}_{q^n}^* \setminus \{2, -2\}$, $\Gamma(Q_b, V)$ is connected by Theorem 4.9.

Hence $s(n) = \frac{n}{p_0(n)} + 1$ for every integer $n \ge 4$. $\blacksquare$

---

## Summary Values and Exact Verification

| $n$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ | $13$ | $14$ | $15$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $p_0(n)$ | $2$ | $5$ | $2$ | $7$ | $2$ | $3$ | $2$ | $11$ | $2$ | $13$ | $2$ | $3$ |
| $s(n) = \frac{n}{p_0(n)} + 1$ | $3$ | $2$ | $4$ | $2$ | $5$ | $4$ | $6$ | $2$ | $7$ | $2$ | $8$ | $6$ |

**Exact-arithmetic verification:** Run
```bash
.venv/bin/python targets/godard-2605.21866-prob3/verify.py
```
which checks (using exact integer/finite-field/polynomial arithmetic with zero floating-point operations) the lower-bound disconnections for $n \in \{4, 5, 6, 7, 8, 9, 10, 15\}$, the Part B character-sum inequality, the Part C Kummer–Weil norm polynomials and spanning of $S_V$, the Part D Jacobian rank growth ($k_0 = n - s + 1$) and reflection identities $\tau_i$, and finite-field connectedness of $\Gamma(Q_b, V)$ for $n \in \{4, 5, 6, 7, 8, 9\}$.

## References

- J. Godard and L. Reis, *Graphs from quadratic forms and vector spaces over finite fields*, arXiv:2605.21866v1 (2026).
- A. Grothendieck, *Éléments de géométrie algébrique (EGA IV$_1$, IV$_3$)*, Publ. Math. IHÉS 20 (1964), 28 (1966).
- A. Grothendieck, *Revêtements étales et groupe fondamental (SGA 1)*, Lecture Notes in Math. 224, Springer (1971).
- R. Hartshorne, *Algebraic Geometry*, Graduate Texts in Math. 52, Springer (1977).
- S. Lang and A. Weil, *Number of points of varieties in finite fields*, Amer. J. Math. 76 (1954), 819–827.
- R. Lidl and H. Niederreiter, *Finite Fields*, 2nd ed., Cambridge University Press (1996).
- H. Matsumura, *Commutative Ring Theory*, Cambridge University Press (1986).

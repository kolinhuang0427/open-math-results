# Proof of Saikia's Conjecture 8.1 (`arXiv:2611.28840v1`) and Sharpness for All $k \ge 3$

## Theorem (Resolution of Conjecture 8.1 and Best-Possible Modulus)

Let $\mathrm{PDO}_{\mathrm{t}}(n)$ be Lin's partition function counting the total number of tagged parts over all partitions of $n$ into odd parts with designated summands, defined in Manjil P. Saikia, *"Congruences modulo powers of $2$ and $3$ for Lin's function $\mathrm{PDO}_{\mathrm{t}}(n)$"* (`arXiv:2611.28840v1`, Section 1, eq. `(1.1)` / `\label{eq:gf}`) by
$$\sum_{n \ge 0} \mathrm{PDO}_{\mathrm{t}}(n)\, q^n = q\,\frac{f_2 f_3^2 f_{12}^2}{f_1^2 f_6}, \qquad f_r := (q^r; q^r)_\infty.$$
Then for **every** integer $k \ge 3$, there exists an odd integer $\lambda_k$ such that, for every $n \ge 0$,
$$\mathrm{PDO}_{\mathrm{t}}\!\bigl(3 \times 2^{k+2} n\bigr) \equiv 8\lambda_k\, \mathrm{PDO}_{\mathrm{t}}\!\bigl(3 \times 2^k n\bigr) \pmod{2^{\lfloor 7(k+1)/2 \rfloor}}. \tag{eq:sharp}$$
Moreover, for **every** $k \ge 3$, the modulus $2^{\lfloor 7(k+1)/2 \rfloor}$ is **best possible**: no integer $\lambda_k$ satisfies the congruence modulo $2^{\lfloor 7(k+1)/2 \rfloor + 1}$ for all $n \ge 0$ (in fact, every choice fails at some $n \in \{1, 2, 3\}$).

---

## Proof Overview

By Saikia's Theorem 4.1 (`\ref{thm:gf}`), for every $m \ge 1$ (setting $k = m + 2 \ge 3$),
$$\sum_{n \ge 0} \mathrm{PDO}_{\mathrm{t}}\!\bigl(3 \times 2^{m+2} n\bigr)\, q^n = \varrho \sum_{j=1}^{5 \cdot 2^{m-1} - 1} x_{m, j}\, \xi^j, \tag{1}$$
where $\varrho = \frac{f_2^{10} f_3^9}{f_1^{11} f_6^6} = 1 + O(q) \in \mathbb{Z}[[q]]$, $\xi = q\,\frac{f_2 f_6^5}{f_1^5 f_3} = q + O(q^2) \in \mathbb{Z}[[q]]$, and the row vectors $\mathbf{x}_m = (x_{m, 1}, x_{m, 2}, \ldots)$ satisfy
$$\mathbf{x}_1 = \bigl(128 \cdot 3^3,\; 128 \cdot 3^7,\; 7168 \cdot 3^6,\; 4096 \cdot 3^8,\; 0,\; 0,\; \ldots\bigr), \qquad \mathbf{x}_{m+1} = \mathbf{x}_m A, \tag{2}$$
for the infinite integer matrix $A = (\Phi_{i, j})_{i, j \ge 1}$ specified by `(P1)`–`(P2)` (Section 3, `\eqref{eq:A1}`–`\eqref{eq:A3}`):
- Row $1$: $(16,\; 648,\; 5184,\; 0,\; \ldots)$;
- Row $2$: $(1,\; 224,\; 8208,\; 98496,\; 373248,\; 0,\; \ldots)$;
- For $i \ge 3$ and $j \ge 1$:
  $$\Phi_{i, j} = 10\,\Phi_{i-1, j-1} + 72\,\Phi_{i-1, j-2} + \Phi_{i-2, j-1} + 8\,\Phi_{i-2, j-2} \tag{3}$$
  (with $\Phi_{i, j} = 0$ for $j \le 0$).

Set $B := A^2$. We prove the theorem in five completely self-contained steps:

1. **Exact Anti-Commuting $2$-Adic Involution ($W A = -A W$):** Using the algebraic realization of $A$ via $\zeta^2 - 6X\zeta - X = 0$ and $\xi = \zeta(1 + 2\zeta)$ (derived directly from `(3)`), we construct an explicit bounded isometric involution $W$ on the $2$-adic Banach space $\mathcal{E}_2$ of power series converging on $|X|_2 \le 2$ with zero constant term — coming from the Atkin–Lehner involution $W_3$ on $X_0(6)$ — and give a $4$-line algebraic proof that $W^2 = I$ and $W A = -A W$ on $\mathcal{E}_2(K)$ for any finite extension $K/\mathbb{Q}_2$.
2. **Constructive $2$-Adic Eigenvector $\mathbf{u}_2$ of $B|_{\ge 2}$:** A strict $2^2$-contraction $\Phi$ on $S(K) = \{\mathbf{w} = (0, 1, w_3, \ldots) \in K^{\mathbb{N}} : \nu_2(w_j) \ge 2j - 3\ \forall j \ge 3\}$ yields a unique fixed point $\mathbf{u}_2 \in S(\mathbb{Q}_2)$ and eigenvalue $\Lambda = (\mathbf{u}_2 B)_2 \in 8\mathbb{Z}_2^\times$ satisfying $(\mathbf{u}_2 B)_j = \Lambda u_{2, j}$ for all $j \ge 2$.
3. **Schur Complement + Weierstrass Knockout ($(\mathbf{u}_2 B)_1 = 0$):** Decomposing $\mathcal{E}_2 = \mathbb{Q}_2^2 \oplus Y$, we show $\|B_{YY}\| \le 2^{-5}$ on $Y$ and form the $2 \times 2$ Schur complement $S(z)$ for $|z|_2 > 2^{-5}$. By a self-contained $15$-line Weierstrass preparation in $\mathbb{Z}_2\langle t \rangle$, $\det S(z)$ has a root $z_0 \in \overline{\mathbb{Q}}_2$ with $|z_0|_2 = 2^{-3}$. Over $K = \mathbb{Q}_2(z_0)$, the anti-commutation $W A = -A W$ forces $\dim_K \ker_{\mathcal{E}_2(K)}(B - z_0 I)$ to be even and $\ge 1$, hence $= 2$, forcing the entire $2 \times 2$ matrix $S(z_0) = 0$. Uniqueness of the fixed point of $\Phi$ in $S(K)$ then identifies $z_0 = \Lambda$ and yields $(\mathbf{u}_2 B)_1 = 0$.
4. **Two-Dimensional $\Lambda$-Eigenspace and $2^7$-Contraction on $\ker(e_1, e_2)$:** From $(\mathbf{u}_2 B)_1 = 0$, the vector $\mathbf{u}_1 := \mathbf{u}_2(A + 16I)$ satisfies $u_{1, 1} = 1$, $u_{1, 2} = 0$, $\mathbf{u}_1 B = \Lambda \mathbf{u}_1$, and $\mathbf{u}_2 B = \Lambda \mathbf{u}_2$. Projecting modulo $\mathrm{span}(\mathbf{u}_1, \mathbf{u}_2)$ via $\pi(\mathbf{x}) := \mathbf{x} - x_1 \mathbf{u}_1 - x_2 \mathbf{u}_2$ gives $\pi(\mathbf{x}_{m+2}) = M(\pi(\mathbf{x}_m))$ where $M(\mathbf{w}) := \pi(\mathbf{w} B)$ satisfies $\nu_2(M(e_k)_j) \ge 7 + 2j - 2k$ for all $k, j \ge 3$.
5. **Exact Induction and Sharpness for All $k \ge 3$:** Separate inductions for odd $m = 2\mu + 1$ ($k = 2\mu + 3$) and even $m = 2\mu + 2$ ($k = 2\mu + 4$) establish both `\eqref{eq:sharp}` modulo $2^{\lfloor 7(k+1)/2 \rfloor}$ and exact valuation $\nu_2(\text{defect}_3) = \lfloor 7(k+1)/2 \rfloor$, proving the modulus is best possible for every $k \ge 3$.

Throughout, $\nu_2$ denotes the $2$-adic valuation on $\overline{\mathbb{Q}}_2$ normalized by $\nu_2(2) = 1$, $\nu_2(0) = \infty$, and $|x|_2 := 2^{-\nu_2(x)}$.

---

## Step 1: Valuation Bounds for $A$ and $B = A^2$

We recall from Saikia's Section 3 and Lemma 5.1 (`\ref{lem:valPhi}`) that for all $i, j \ge 1$:
- $\Phi_{i, j} = 0$ unless $\lfloor (i + 1)/2 \rfloor \le j \le 2i + 1$, and
- $\nu_2(\Phi_{i, j}) \ge 2j - i$.

**Lemma 1 (Support and $2$-adic valuations of $B = A^2$).**
Let $B = (B_{i, j})_{i, j \ge 1}$ where $B_{i, j} := \sum_{k \ge 1} \Phi_{i, k} \Phi_{k, j}$. Then for all $i, j \ge 1$:
1. $B_{i, j} = 0$ unless $\lfloor (i + 3)/4 \rfloor \le j \le 4i + 3$. In particular, $B_{i, 1} = 0$ for all $i \ge 5$, $B_{i, 2} = 0$ for all $i \ge 9$, $B_{1, j} = 0$ for all $j \ge 8$, and $B_{2, j} = 0$ for all $j \ge 12$.
2. $\nu_2(B_{i, j}) \ge 2j - \lfloor i/2 \rfloor$.
3. The explicit top-left $2 \times 2$ block and low columns/rows of $B$ satisfy:
   - $B_{1, 1} = 904 = 2^3 \cdot 113$, $B_{1, 2} = 290304 = 2^9 \cdot 567$, $B_{2, 1} = 240 = 2^4 \cdot 15$, $B_{2, 2} = 362728 = 2^3 \cdot 45341$;
   - $(B_{3, 1}, B_{4, 1}) = (26, 1)$ with $\nu_2(B_{i, 1}) = (1, 0)$ for $i = 3, 4$;
   - $(B_{3, 2}, B_{4, 2}, B_{5, 2}, B_{6, 2}, B_{7, 2}, B_{8, 2}) = (194688, 55768, 9224, 886, 46, 1)$ with valuations $(7, 3, 3, 1, 1, 0)$;
   - $\nu_2(B_{1, j}) = (7, 9, 12, 15, 18)$ for $3 \le j \le 7$, so $\min_{j \ge 3}(\nu_2(B_{1, j}) - j) = 4$;
   - $\nu_2(B_{2, j}) = (6, 9, 13, 13, 18, 18, 21, 24, 27)$ for $3 \le j \le 11$, so $\nu_2(B_{2, 3}) = 6$, $\nu_2(B_{2, j}) \ge 2j + 1$ for all $j \ge 4$, and $\min_{j \ge 3}(\nu_2(B_{2, j}) - j) = 3$.

*Proof.*
For (1), a term $\Phi_{i, k}\Phi_{k, j}$ can be nonzero only if $\lfloor (i + 1)/2 \rfloor \le k \le 2i + 1$ and $\lfloor (k + 1)/2 \rfloor \le j \le 2k + 1$. Thus $j \le 2(2i + 1) + 1 = 4i + 3$ and $j \ge \lfloor (\lfloor (i + 1)/2 \rfloor + 1)/2 \rfloor = \lfloor (i + 3)/4 \rfloor$.
For (2), every nonzero term satisfies
$$\nu_2(\Phi_{i, k} \Phi_{k, j}) \ge (2k - i) + (2j - k) = 2j + k - i \ge 2j + \left\lfloor \frac{i + 1}{2} \right\rfloor - i = 2j - \left\lfloor \frac{i}{2} \right\rfloor,$$
using the identity $\lfloor (i + 1)/2 \rfloor - i = -\lfloor i/2 \rfloor$ for all $i \in \mathbb{Z}$.
Part (3) is a finite exact integer computation from `(P1)`–`(P2)` (verified in `verify.py`). $\square$

---

## Step 2: The $2$-Adic Banach Space $\mathcal{E}_2(K)$ and the Exact Involution $W A = -A W$

Let $K / \mathbb{Q}_2$ be any finite extension (hence complete with respect to the unique extension of $|\cdot|_2$). Define the $K$-Banach algebra of power series converging on the closed disk $|X|_2 \le 2$:
$$\mathcal{B}_2(K) := \left\{ F(X) = \sum_{n=0}^{\infty} c_n X^n \in K[[X]] : \lim_{n \to \infty} \bigl(\nu_2(c_n) - n\bigr) = +\infty \right\}, \qquad \|F\|_{\mathcal{B}_2} := \sup_{n \ge 0} |c_n|_2\, 2^n.$$
By the ultrametric inequality, $|(FG)_n|_2\, 2^n \le \max_{a+b=n} (|f_a|_2\, 2^a)(|g_b|_2\, 2^b) \le \|F\|_{\mathcal{B}_2}\|G\|_{\mathcal{B}_2}$, so $\mathcal{B}_2(K)$ is a commutative $K$-Banach algebra in which $K[X]$ is dense. Define the closed subspace
$$\mathcal{E}_2(K) := X\,\mathcal{B}_2(K) = \left\{ \mathbf{u}(X) = \sum_{j=1}^{\infty} u_j X^j \in X K[[X]] : \lim_{j \to \infty}\bigl(\nu_2(u_j) - j\bigr) = +\infty \right\},$$
equipped with the induced norm $\|\mathbf{u}\| := \|\mathbf{u}\|_{\mathcal{B}_2} = \sup_{j \ge 1} |u_j|_2\, 2^j$ (so $\|X\mathbf{v}\| = 2\|\mathbf{v}\|_{\mathcal{B}_2}$ for $\mathbf{v} \in \mathcal{B}_2(K)$). We identify $\mathbf{u} \in \mathcal{E}_2(K)$ with its coefficient row vector $(u_1, u_2, \ldots)$ and basis elements $e_i(X) := X^i$ ($i \ge 1$).

### 2.1 Boundedness and Algebraic Representation of $A$ on $\mathcal{E}_2(K)$

For each $i \ge 1$, set $P_i(X) := \sum_{j = \lfloor(i+1)/2\rfloor}^{2i+1} \Phi_{i, j} X^j \in X \mathbb{Z}[X] \subset \mathcal{E}_2(K)$. By Lemma 5.1, every nonzero term satisfies $\nu_2(\Phi_{i, j}) - j \ge (2j - i) - j = j - i \ge \lfloor (i + 1)/2 \rfloor - i = -\lfloor i/2 \rfloor$, whence
$$\|P_i\| \le 2^{\lfloor i/2 \rfloor} = 2^{-\lceil i/2 \rceil} \|e_i\| \le \tfrac{1}{2}\|e_i\|. \tag{4}$$
Consequently, the linear map $A : \mathcal{E}_2(K) \to \mathcal{E}_2(K)$ defined by $(\mathbf{u} A)(X) := \sum_{i=1}^{\infty} u_i P_i(X)$ converges absolutely in $\mathcal{E}_2(K)$ with operator norm $\|A\| \le 1/2$, and its $j$-th coefficient is the finite sum $(\mathbf{u} A)_j = \sum_{i=1}^{2j} u_i \Phi_{i, j}$.

Next, form the free rank-$2$ $\mathcal{B}_2(K)$-algebra
$$\mathcal{R}_2(K) := \mathcal{B}_2(K)[\zeta] / (\zeta^2 - 6X\zeta - X) = \mathcal{B}_2(K) \oplus \mathcal{B}_2(K)\zeta,$$
with norm $\|a + b\zeta\|_{\mathcal{R}_2} := \max\bigl(\|a\|_{\mathcal{B}_2},\, \sqrt{2}\,\|b\|_{\mathcal{B}_2}\bigr)$. For any $u = a + b\zeta$ and $v = c + d\zeta$ in $\mathcal{R}_2(K)$, we have $uv = (ac + bdX) + (ad + bc + 6bdX)\zeta$, and since $\|X\|_{\mathcal{B}_2} = 2$ and $\|6X\|_{\mathcal{B}_2} = 1$,
$$\|ac + bdX\|_{\mathcal{B}_2} \le \max\bigl(\|a\|\|c\|,\, (\sqrt{2}\|b\|)(\sqrt{2}\|d\|)\bigr) \le \|u\|_{\mathcal{R}_2}\|v\|_{\mathcal{R}_2},$$
$$\sqrt{2}\|ad + bc + 6bdX\|_{\mathcal{B}_2} \le \max\bigl(\|a\|(\sqrt{2}\|d\|),\, (\sqrt{2}\|b\|)\|c\|,\, \tfrac{1}{\sqrt{2}}(\sqrt{2}\|b\|)(\sqrt{2}\|d\|)\bigr) \le \|u\|_{\mathcal{R}_2}\|v\|_{\mathcal{R}_2},$$
so $\mathcal{R}_2(K)$ is a commutative $K$-Banach algebra (with $\|\zeta\|_{\mathcal{R}_2} = \sqrt{2}$ and $\|\zeta^2\|_{\mathcal{R}_2} = 2$). Set $\xi := \zeta(1 + 2\zeta) = 2X + (1 + 12X)\zeta \in \mathcal{R}_2(K)$. Then:
- $\|\xi\|_{\mathcal{R}_2} = \|\zeta + 2\zeta^2\|_{\mathcal{R}_2} \le \max(\sqrt{2},\, \frac{1}{2} \cdot 2) = \sqrt{2} < 2$. Hence for every $F(t) = \sum_{n=0}^{\infty} c_n t^n \in \mathcal{B}_2(K)$, the composition $F(\xi) := \sum_{n=0}^{\infty} c_n \xi^n$ converges absolutely in $\mathcal{R}_2(K)$ with $\|F(\xi)\|_{\mathcal{R}_2} \le \|F\|_{\mathcal{B}_2}$.
- Let $\bar{\zeta} := 6X - \zeta \in \mathcal{R}_2(K)$ be the Galois conjugate of $\zeta$ over $\mathcal{B}_2(K)$, so $\zeta + \bar{\zeta} = 6X$ and $\zeta\bar{\zeta} = -X$. Then
  $$(1 + 6\zeta)(1 + 6\bar{\zeta}) = 1 + 6(\zeta + \bar{\zeta}) + 36\zeta\bar{\zeta} = 1 + 36X - 36X = 1, \tag{5}$$
  so $1 + 6\zeta$ is a unit in $\mathcal{R}_2(K)$ with inverse $(1 + 6\zeta)^{-1} = 1 + 6\bar{\zeta} = 1 + 36X - 6\zeta$.
- The half-trace $\frac{1}{2}\mathrm{Tr}(a + b\zeta) := a + 3Xb$ is a continuous $\mathcal{B}_2(K)$-linear map $\mathcal{R}_2(K) \to \mathcal{B}_2(K)$ (satisfying $\|\frac{1}{2}\mathrm{Tr}(a + b\zeta)\|_{\mathcal{B}_2} \le \max(\|a\|_{\mathcal{B}_2}, 2\|b\|_{\mathcal{B}_2}) \le \sqrt{2}\|a + b\zeta\|_{\mathcal{R}_2}$).

We therefore obtain a continuous $K$-linear operator $\tilde{A} : \mathcal{B}_2(K) \to \mathcal{B}_2(K)$ defined by
$$\tilde{A}(F)(X) := \frac{1}{2}\mathrm{Tr}\!\left(\frac{F(\xi)}{1 + 6\zeta}\right) = \frac{1}{2}\mathrm{Tr}\!\bigl(F(\xi)(1 + 36X - 6\zeta)\bigr). \tag{6}$$

**Lemma 2 (Exact conjugation identity).**
For every $\mathbf{u} \in \mathcal{E}_2(K)$,
$$(1 + 8X)(1 + 9X)\,(\mathbf{u} A)(X) = \tilde{A}\!\bigl((1 + 8t)(1 + 9t)\,\mathbf{u}(t)\bigr)(X). \tag{7}$$

*Proof.*
Both sides of `(7)` are continuous $K$-linear maps $\mathcal{E}_2(K) \to \mathcal{B}_2(K)$, so by density of $X K[X]$ in $\mathcal{E}_2(K)$ it suffices to verify `(7)` on $\mathbf{u} = e_i$ ($i \ge 1$). First, from $\xi = 2X + (1 + 12X)\zeta$ and $\zeta^2 = 6X\zeta + X$, a direct expansion gives $\xi + \bar{\xi} = 10X + 72X^2$ and $\xi\bar{\xi} = -(X + 8X^2)$, so
$$\xi^2 = (10X + 72X^2)\xi + (X + 8X^2) \qquad \text{in } \mathcal{R}_2(K). \tag{8}$$
For $i = 1, 2$, direct polynomial computation of $\frac{1}{2}\mathrm{Tr}\bigl((1 + 8\xi)(1 + 9\xi)\xi^i(1 + 36X - 6\zeta)\bigr)$ using `(5)` and $\zeta^2 = 6X\zeta + X$ yields:
$$\begin{aligned}
\tilde{A}\bigl((1 + 8t)(1 + 9t)t\bigr)(X) &= (1 + 8X)(1 + 9X)\bigl(16X + 648X^2 + 5184X^3\bigr) = (1 + 8X)(1 + 9X)P_1(X),\\
\tilde{A}\bigl((1 + 8t)(1 + 9t)t^2\bigr)(X) &= (1 + 8X)(1 + 9X)\bigl(X + 224X^2 + 8208X^3 + 98496X^4 + 373248X^5\bigr) = (1 + 8X)(1 + 9X)P_2(X).
\end{aligned}$$
For $i \ge 3$, multiplying `(8)` by $(1 + 8\xi)(1 + 9\xi)\xi^{i-2}$ and applying the $\mathcal{B}_2(K)$-linear operator $\tilde{A}$ gives
$$\tilde{A}\bigl((1 + 8t)(1 + 9t)t^i\bigr) = (10X + 72X^2)\tilde{A}\bigl((1 + 8t)(1 + 9t)t^{i-1}\bigr) + (X + 8X^2)\tilde{A}\bigl((1 + 8t)(1 + 9t)t^{i-2}\bigr),$$
which is identical to the recurrence `(3)` for $(1 + 8X)(1 + 9X)P_i(X)$. Induction on $i$ proves `(7)` for all $i \ge 1$. $\square$

### 2.2 The Atkin–Lehner Involution $W_3$ and $W A = -A W$

Since $\|8X\|_{\mathcal{B}_2} = \frac{1}{8} \cdot 2 = \frac{1}{4} < 1$, the element $1 + 8X$ is a unit in $\mathcal{B}_2(K)$ with inverse $\sum_{m \ge 0} (-8X)^m$ and $\|(1 + 8X)^{\pm 1}\|_{\mathcal{B}_2} = 1$. Define
$$h(X) := -\frac{1 + 9X}{9(1 + 8X)} = -\frac{1}{9} - \frac{1}{9}X + \frac{1}{9}\sum_{k=2}^{\infty} (-1)^k 8^{k-1} X^k \in \mathcal{B}_2(K). \tag{9}$$
Inspecting the norms of its terms in $\mathcal{B}_2(K)$: $|-1/9|_2 \cdot 1 = 1$, $|-1/9|_2 \cdot 2 = 2$, and $|8^{k-1}/9|_2 \cdot 2^k = 2^{3 - 2k} \le 1/2$ for all $k \ge 2$. Hence $\|h\|_{\mathcal{B}_2} = 2$, and therefore $\|h^n\|_{\mathcal{B}_2} \le 2^n$ for all $n \ge 0$. Thus for every $F(t) = \sum_{n=0}^{\infty} c_n t^n \in \mathcal{B}_2(K)$, the composition $(F \circ h)(X) := \sum_{n=0}^{\infty} c_n h(X)^n$ converges in $\mathcal{B}_2(K)$ with $\|F \circ h\|_{\mathcal{B}_2} \le \|F\|_{\mathcal{B}_2}$.

Define the bounded $K$-linear operator $W_3 : \mathcal{B}_2(K) \to \mathcal{B}_2(K)$ by
$$(W_3 F)(X) := 3(1 + 8X)\, (F \circ h)(X), \tag{10}$$
and the bounded $K$-linear operator $W : \mathcal{E}_2(K) \to \mathcal{E}_2(K)$ on $\mathbf{u}(X) = X\mathbf{v}(X)$ ($\mathbf{v} \in \mathcal{B}_2(K)$) by
$$(W \mathbf{u})(X) := \frac{X}{27(1 + 8X)^3}\, (\mathbf{v} \circ h)(X). \tag{11}$$

**Theorem 3 (Exact anti-commuting involution).**
1. $W_3^2 = I$ and $W_3 \tilde{A} = -\tilde{A} W_3$ on $\mathcal{B}_2(K)$.
2. $W^2 = I$ and $W A = -A W$ on $\mathcal{E}_2(K)$.

*Proof.*
First compute the elementary Möbius identities:
$$1 + 8h(X) = 1 - \frac{8(1 + 9X)}{9(1 + 8X)} = \frac{1}{9(1 + 8X)}, \qquad 1 + 9h(X) = 1 - \frac{1 + 9X}{1 + 8X} = \frac{-X}{1 + 8X}. \tag{12}$$
Immediately $h(h(X)) = -\frac{1 + 9h(X)}{9(1 + 8h(X))} = X$, and for every $F \in K[X]$,
$$(W_3^2 F)(X) = 3(1 + 8X) \cdot 3\bigl(1 + 8h(X)\bigr)\, F(h(h(X))) = 9(1 + 8X) \cdot \frac{1}{9(1 + 8X)}\, F(X) = F(X).$$
By continuity of $W_3$ and density of $K[X]$ in $\mathcal{B}_2(K)$, $W_3^2 = I$ on $\mathcal{B}_2(K)$.

To prove $W_3 \tilde{A} = -\tilde{A} W_3$, observe first the algebraic factorizations in $\mathbb{Q}(\zeta)$ (where $X = \zeta^2/(1 + 6\zeta)$ and $\xi = \zeta(1 + 2\zeta)$):
$$1 + 8\xi = (1 + 4\zeta)^2, \qquad 1 + 9\xi = (1 + 3\zeta)(1 + 6\zeta), \tag{13}$$
$$1 + 8X = \frac{(1 + 2\zeta)(1 + 4\zeta)}{1 + 6\zeta}, \qquad 1 + 9X = \frac{(1 + 3\zeta)^2}{1 + 6\zeta}. \tag{14}$$
Define the Möbius lift $\psi(\zeta) := -\frac{1 + 3\zeta}{3(1 + 4\zeta)}$ (which is invertible since its determinant is $(-3)(3) - (-1)(12) = 3 \neq 0$, and well-defined in $\mathcal{R}_2(K)$ since $\|4\zeta\|_{\mathcal{R}_2} = \frac{\sqrt{2}}{4} < 1$). Direct fraction simplification gives four identities:
$$\begin{aligned}
1 + 6\psi(\zeta) &= 1 - \frac{2(1 + 3\zeta)}{1 + 4\zeta} = -\frac{1 + 2\zeta}{1 + 4\zeta},\\
1 + 2\psi(\zeta) &= 1 - \frac{2(1 + 3\zeta)}{3(1 + 4\zeta)} = \frac{1 + 6\zeta}{3(1 + 4\zeta)},\\
\frac{\psi(\zeta)^2}{1 + 6\psi(\zeta)} &= \frac{(1 + 3\zeta)^2 / \bigl(9(1 + 4\zeta)^2\bigr)}{-(1 + 2\zeta)/(1 + 4\zeta)} = -\frac{(1 + 3\zeta)^2}{9(1 + 2\zeta)(1 + 4\zeta)} = -\frac{1 + 9X}{9(1 + 8X)} = h(X),\\
\psi(\zeta)\bigl(1 + 2\psi(\zeta)\bigr) &= -\frac{(1 + 3\zeta)(1 + 6\zeta)}{9(1 + 4\zeta)^2} = -\frac{1 + 9\xi}{9(1 + 8\xi)} = h(\xi).
\end{aligned} \tag{15}$$
Let $\zeta_1, \zeta_2$ be the two distinct roots of $Z^2 - 6XZ - X = 0$ in an algebraic closure of $\mathbb{Q}(X)$, and let $\xi_r := \zeta_r(1 + 2\zeta_r)$. Because $\psi$ is an injective Möbius transformation, the third identity in `(15)` implies that $\{\psi(\zeta_1), \psi(\zeta_2)\}$ is the exact set of two roots of $\tilde{Z}^2 - 6 h(X) \tilde{Z} - h(X) = 0$. Moreover, using `(14)`, `(15)`, and `(13)`, the weight factor transforms with an exact **minus sign**:
$$\frac{3(1 + 8X)}{1 + 6\psi(\zeta_r)} = 3 \cdot \frac{\frac{(1 + 2\zeta_r)(1 + 4\zeta_r)}{1 + 6\zeta_r}}{-\frac{1 + 2\zeta_r}{1 + 4\zeta_r}} = -\frac{3(1 + 4\zeta_r)^2}{1 + 6\zeta_r} = -\frac{3(1 + 8\xi_r)}{1 + 6\zeta_r}. \tag{16}$$
Therefore, for every polynomial $F \in K[X]$ — noting that $G(t) := (W_3 F)(t) = 3(1 + 8t)F(h(t))$ is a rational function whose only poles are at $t = -1/8$, and since $\|8\xi\|_{\mathcal{R}_2} = \frac{\sqrt{2}}{8} < 1$, the Banach-algebra power-series evaluation $G(\xi) \in \mathcal{R}_2(K)$ agrees with rational evaluation in $\mathrm{Frac}(\mathcal{R}_2(K))$ — we have
$$\begin{aligned}
\bigl(W_3(\tilde{A} F)\bigr)(X)
&= 3(1 + 8X) \cdot \frac{1}{2}\sum_{r=1}^2 \frac{F\bigl(\psi(\zeta_r)(1 + 2\psi(\zeta_r))\bigr)}{1 + 6\psi(\zeta_r)} \\
&= \frac{1}{2}\sum_{r=1}^2 \frac{3(1 + 8X)}{1 + 6\psi(\zeta_r)}\, F\bigl(h(\xi_r)\bigr) \\
&= -\frac{1}{2}\sum_{r=1}^2 \frac{3(1 + 8\xi_r)\, F(h(\xi_r))}{1 + 6\zeta_r} = -\bigl(\tilde{A}(W_3 F)\bigr)(X).
\end{aligned}$$
By continuity of $W_3$ and $\tilde{A}$ on $\mathcal{B}_2(K)$ and density of $K[X]$, we conclude $W_3 \tilde{A} = -\tilde{A} W_3$ on all of $\mathcal{B}_2(K)$, proving (1).

For (2), let $\mathbf{u}(X) = X\mathbf{v}(X) \in \mathcal{E}_2(K)$ and set $F(X) := (1 + 8X)(1 + 9X)\mathbf{u}(X) \in \mathcal{B}_2(K)$. By `(12)` and `(9)`,
$$\begin{aligned}
(W_3 F)(X) &= 3(1 + 8X)\bigl(1 + 8h(X)\bigr)\bigl(1 + 9h(X)\bigr)\, h(X)\, (\mathbf{v} \circ h)(X) \\
&= 3(1 + 8X) \cdot \frac{1}{9(1 + 8X)} \cdot \frac{-X}{1 + 8X} \cdot \left(-\frac{1 + 9X}{9(1 + 8X)}\right)(\mathbf{v} \circ h)(X) \\
&= (1 + 8X)(1 + 9X) \cdot \frac{X}{27(1 + 8X)^3}\, (\mathbf{v} \circ h)(X) = (1 + 8X)(1 + 9X)\,(W\mathbf{u})(X).
\end{aligned} \tag{17}$$
Applying `(17)` twice yields $(1 + 8X)(1 + 9X)(W^2 \mathbf{u}) = W_3^2 F = F = (1 + 8X)(1 + 9X)\mathbf{u}$. Combining `(7)`, `(17)`, and (1) gives
$$(1 + 8X)(1 + 9X)\bigl(W(\mathbf{u} A)\bigr) = W_3\bigl(\tilde{A}(F)\bigr) = -\tilde{A}\bigl(W_3(F)\bigr) = -(1 + 8X)(1 + 9X)\bigl((W\mathbf{u}) A\bigr).$$
Since $(1 + 8X)(1 + 9X) \neq 0$ and $K[[X]]$ is an integral domain, cancelling $(1 + 8X)(1 + 9X)$ gives $W^2 = I$ and $W A = -A W$ on $\mathcal{E}_2(K)$. $\square$

---

## Step 3: Constructive $2$-Adic Eigenvector $\mathbf{u}_2$ and Proof of $(\mathbf{u}_2 B)_1 = 0$

### 3.1 Contraction Map $\Phi$ for $\mathbf{u}_2$

For any finite extension $K/\mathbb{Q}_2$, define the complete metric space
$$S(K) := \left\{ \mathbf{w} = (0, 1, w_3, w_4, \ldots) \in K^{\mathbb{N}} : \nu_2(w_j) \ge 2j - 3 \ \ (\forall j \ge 3) \right\}$$
with ultrametric $d(\mathbf{w}', \mathbf{w}) := \sup_{j \ge 3} 2^{-(\nu_2(w'_j - w_j) - (2j - 3))} \le 1$. Note that $S(K) \subset \mathcal{E}_2(K)$ since $\nu_2(w_j) - j \ge j - 3 \to +\infty$.

**Lemma 4 (Strict $2^2$-contraction $\Phi$).**
For $\mathbf{w} \in S(K)$, set $\Lambda(\mathbf{w}) := (\mathbf{w} B)_2 = B_{2, 2} + \sum_{k=3}^{8} w_k B_{k, 2}$ and define $\Phi(\mathbf{w}) = (0, 1, \Phi(\mathbf{w})_3, \ldots)$ by $\Phi(\mathbf{w})_j := \Lambda(\mathbf{w})^{-1} (\mathbf{w} B)_j$ ($j \ge 3$). Then:
1. $\nu_2(\Lambda(\mathbf{w})) = 3$ for every $\mathbf{w} \in S(K)$, and $\nu_2(\Lambda(\mathbf{w}') - \Lambda(\mathbf{w})) \ge 8 + \Delta$ whenever $d(\mathbf{w}', \mathbf{w}) \le 2^{-\Delta}$ ($\Delta \ge 0$).
2. $\Phi(S(K)) \subseteq S(K)$, and $d(\Phi(\mathbf{w}'), \Phi(\mathbf{w})) \le 2^{-2}\, d(\mathbf{w}', \mathbf{w})$ for all $\mathbf{w}, \mathbf{w}' \in S(K)$.
3. Consequently, $\Phi$ has a unique fixed point $\mathbf{u}_2 \in S(K)$, which lies in $S(\mathbb{Q}_2)$ and satisfies $\Lambda := \Lambda(\mathbf{u}_2) \in 8\mathbb{Z}_2^\times$, $(\mathbf{u}_2 B)_j = \Lambda u_{2, j}$ for all $j \ge 2$, and $\nu_2(u_{2, j}) \ge 2j - 2$ for all $j \ge 4$.

*Proof.*
1. By Lemma 1(3), $\nu_2(B_{2, 2}) = 3$, while for $3 \le k \le 8$ we have $\nu_2(w_k B_{k, 2}) \ge (2k - 3) + \nu_2(B_{k, 2}) = (10, 8, 10, 10, 12, 13) \ge 8$. Thus $\nu_2(\Lambda(\mathbf{w})) = 3$, and for $d(\mathbf{w}', \mathbf{w}) \le 2^{-\Delta}$ each difference $(w'_k - w_k)B_{k, 2}$ has valuation $\ge 8 + \Delta$.
2. For $\mathbf{w} \in S(K)$ and $j \ge 3$, Lemma 1(2)–(3) gives $\nu_2(B_{2, j}) \ge 2j$ (with $\nu_2(B_{2, j}) \ge 2j + 1$ for $j \ge 4$) and, for all $k \ge 3$,
   $$\nu_2(w_k B_{k, j}) \ge (2k - 3) + (2j - \lfloor k/2 \rfloor) = 2j + \lceil 3k/2 \rceil - 3 \ge 2j + 2. \tag{18}$$
   Hence $\nu_2((\mathbf{w} B)_j) \ge 2j$ for $j \ge 3$ (and $\ge 2j + 1$ for $j \ge 4$). Dividing by $\Lambda(\mathbf{w})$ (valuation $3$) gives $\nu_2(\Phi(\mathbf{w})_j) \ge 2j - 3$ (and $\ge 2j - 2$ for $j \ge 4$), so $\Phi(S(K)) \subseteq S(K)$. For $\mathbf{w}, \mathbf{w}' \in S(K)$ with $d(\mathbf{w}', \mathbf{w}) \le 2^{-\Delta}$ and $j \ge 3$,
   $$\Phi(\mathbf{w}')_j - \Phi(\mathbf{w})_j = \frac{(\mathbf{w}' B)_j - (\mathbf{w} B)_j}{\Lambda(\mathbf{w}')} + (\mathbf{w} B)_j\,\frac{\Lambda(\mathbf{w}) - \Lambda(\mathbf{w}')}{\Lambda(\mathbf{w}')\Lambda(\mathbf{w})}.$$
   By `(18)`, the first term has valuation $\ge (2j + 2 + \Delta) - 3 = (2j - 3) + \Delta + 2$; by (1), the second term has valuation $\ge 2j + (8 + \Delta) - 6 = (2j - 3) + \Delta + 5$. Thus $d(\Phi(\mathbf{w}'), \Phi(\mathbf{w})) \le 2^{-2} d(\mathbf{w}', \mathbf{w})$.
3. By Banach's fixed-point theorem, $\Phi$ has a unique fixed point $\mathbf{u}_2$ in $S(\mathbb{Q}_2)$ and a unique fixed point in $S(K)$; since $S(\mathbb{Q}_2) \subseteq S(K)$, they coincide. The sharper bound $\nu_2(u_{2, j}) \ge 2j - 2$ ($j \ge 4$) follows from $\Phi(\mathbf{u}_2) = \mathbf{u}_2$ and $\nu_2((\mathbf{u}_2 B)_j) \ge 2j + 1$ ($j \ge 4$). $\square$

### 3.2 Schur Complement, Elementary Weierstrass Preparation, and $(\mathbf{u}_2 B)_1 = 0$

Decompose $\mathcal{E}_2(K) = K^2 \oplus Y(K)$ where $K^2 = \mathrm{span}(e_1, e_2)$ and $Y(K) := \{\mathbf{y} \in \mathcal{E}_2(K) : y_1 = y_2 = 0\}$, and write the bounded operator $B = A^2$ on $\mathcal{E}_2(K)$ in block form (acting on the right):
$$B = \begin{pmatrix} B_{00} & B_{0Y} \\ B_{Y0} & B_{YY} \end{pmatrix}.$$

**Lemma 5 (Contraction of $B_{YY}$ and Schur complement $M(t)$).**
1. On $Y(K)$, $\|B_{YY}\| \le 2^{-5}$. Hence for every $z \in K$ with $|z|_2 > 2^{-5}$, the operator $zI - B_{YY} : Y(K) \to Y(K)$ is invertible via the convergent Neumann series $\sum_{m \ge 0} z^{-(m+1)} B_{YY}^m$.
2. For every $z \in K$ with $|z|_2 > 2^{-5}$, define the $2 \times 2$ Schur complement matrix
   $$S(z) := B_{00} - z I_2 + B_{0Y}(zI - B_{YY})^{-1} B_{Y0} \in M_{2 \times 2}(K).$$
   Then the projection $\mathbf{w} = (w_1, w_2, \mathbf{y}) \mapsto (w_1, w_2)$ restricts to a $K$-linear isomorphism
   $$\ker_{\mathcal{E}_2(K)}(B - zI) \xrightarrow{\;\sim\;} \ker_{K^2}\bigl(S(z)\bigr), \qquad (w_1, w_2) \mapsto \bigl(w_1,\, w_2,\, (w_1, w_2) B_{0Y}(zI - B_{YY})^{-1}\bigr).$$
3. Setting $t := 8/z$ and $M(t) := -z^{-1} S(z) = I_2 - \frac{t}{8} B_{00} - \sum_{m \ge 0} \bigl(\frac{t}{8}\bigr)^{m+2} B_{0Y} B_{YY}^m B_{Y0}$, the determinant $g(t) := \det M(t) = \sum_{n=0}^{\infty} c_n t^n$ lies in $\mathbb{Z}_2\langle t \rangle := \{\sum_{n \ge 0} a_n t^n \in \mathbb{Z}_2[[t]] : \nu_2(a_n) \to \infty\}$ and satisfies
   $$c_0 = 1, \qquad c_1 \in 2\mathbb{Z}_2, \qquad c_2 \in \mathbb{Z}_2^\times, \qquad \nu_2(c_n) \ge 2n - 4 \ge 2 \quad (\forall n \ge 3). \tag{19}$$

*Proof.*
1. For all $i \ge 3$ and $j \ge 3$, Lemma 1(2) gives
   $$\nu_2(B_{i, j}) - j + i \ge \bigl(2j - \lfloor i/2 \rfloor\bigr) - j + i = j + \lceil i/2 \rceil \ge 3 + 2 = 5.$$
   Hence $\|e_i B_{YY}\| = \sup_{j \ge 3} |B_{i, j}|_2 2^j \le 2^{-5} \cdot 2^i = 2^{-5}\|e_i\|$ for all $i \ge 3$, so $\|B_{YY}\| \le 2^{-5}$.
2. Writing $\mathbf{w} = (w_1, w_2, \mathbf{y})$, the equation $\mathbf{w}(B - zI) = 0$ is equivalent to the pair of equations
   $$(w_1, w_2)(B_{00} - zI_2) + \mathbf{y} B_{Y0} = 0, \qquad (w_1, w_2) B_{0Y} + \mathbf{y}(B_{YY} - zI) = 0.$$
   Since $zI - B_{YY}$ is invertible, the second equation uniquely solves for $\mathbf{y} = (w_1, w_2) B_{0Y}(zI - B_{YY})^{-1}$, and substituting into the first gives $(w_1, w_2) S(z) = 0$.
3. By Lemma 1(3), $\|e_r B_{0Y}\| = 2^{-\alpha_r}$ with $(\alpha_1, \alpha_2) = (4, 3)$. For $c \in \{1, 2\}$ and any $\mathbf{y} \in Y(\mathbb{Q}_2)$, Lemma 1(1, 3) gives
   $$|(\mathbf{y} B_{Y0})_c|_2 = \left|\sum_{i=3}^{4c} y_i B_{i, c}\right|_2 \le \|\mathbf{y}\| \cdot \max_{3 \le i \le 4c} \bigl(|B_{i, c}|_2 2^{-i}\bigr) = \|\mathbf{y}\| \cdot 2^{-\beta_c},$$
   with $\beta_1 = \min(1 + 3,\, 0 + 4) = 4$ and $\beta_2 = \min(7 + 3,\, 3 + 4,\, 3 + 5,\, 1 + 6,\, 1 + 7,\, 0 + 8) = 7$. Since $\|B_{YY}\| \le 2^{-5}$, every $m \ge 0$ satisfies $\nu_2\bigl((B_{0Y} B_{YY}^m B_{Y0})_{r, c}\bigr) \ge \alpha_r + 5m + \beta_c$, and therefore the coefficient of $t^{m+2}$ in $E_{r, c}(t) := \sum_{m \ge 0} (t/8)^{m+2} (B_{0Y} B_{YY}^m B_{Y0})_{r, c}$ has valuation
   $$\nu_2\!\left(\frac{(B_{0Y} B_{YY}^m B_{Y0})_{r, c}}{8^{m+2}}\right) \ge (\alpha_r + \beta_c - 6) + 2m = \begin{cases} 2 + 2m & (r, c) = (1, 1),\\ 5 + 2m & (r, c) = (1, 2),\\ 1 + 2m & (r, c) = (2, 1),\\ 4 + 2m & (r, c) = (2, 2).\end{cases}$$
   Combining with $\frac{1}{8} B_{00} = \begin{pmatrix} 113 & 36288 \\ 30 & 45341 \end{pmatrix}$ (where $\nu_2(113) = \nu_2(45341) = 0$, $\nu_2(36288) = 6$, $\nu_2(30) = 1$), writing $M_{r, c}(t) = \sum_{n \ge 0} m^{(r, c)}_n t^n$ gives:
   - $c_0 = 1$;
   - $c_1 = -(113 + 45341) = -45454 \in 2\mathbb{Z}_2$;
   - $c_2 = 113 \cdot 45341 + m^{(1, 1)}_2 + m^{(2, 2)}_2 - 36288 \cdot 30 \equiv 1 + 0 + 0 - 0 = 1 \pmod 2$, so $c_2 \in \mathbb{Z}_2^\times$;
   - for $n \ge 3$, checking every pair $(a, b)$ with $a + b = n$ in $M_{1,1}M_{2,2} - M_{1,2}M_{2,1}$ gives minimum valuation $\min\bigl(2n,\, 2n - 2,\, 2n - 4,\, 2n + 1,\, 2n,\, 2n - 2\bigr) = 2n - 4 \ge 2$ (attained at $(a, b) = (n - 1, 1)$ in $M_{1, 1} M_{2, 2}$). This proves `(19)`. $\square$

**Lemma 6 (Elementary Weierstrass preparation in $T := \mathbb{Z}_2\langle t \rangle$ and existence of $z_0$).**
There exists $z_0 \in \overline{\mathbb{Q}}_2$ with $|z_0|_2 = 2^{-3}$ and $\det S(z_0) = 0$.

*Proof.*
Equip $T := \mathbb{Z}_2\langle t \rangle$ with the Gauss norm $\|f\|_T := \sup_{n \ge 0} |f_n|_2$. First observe that for any quadratic polynomial $Q(t) = c_2 t^2 + a_1 t + a_0 \in \mathbb{Z}_2[t]$ with $c_2 \in \mathbb{Z}_2^\times$, every $f = \sum_{n \ge 0} f_n t^n \in T$ admits a Euclidean division $f = Q q + R$ with $q \in T$, $R \in \mathbb{Z}_2 + \mathbb{Z}_2 t$, and $\|q\|_T, \|R\|_T \le \|f\|_T$: indeed, ordinary polynomial division over $\mathbb{Z}_2$ writes $t^n = Q(t) q_n(t) + r_n(t)$ with $q_n, r_n \in \mathbb{Z}_2[t]$ and $\deg r_n \le 1$, so $q := \sum_{n \ge 0} f_n q_n$ and $R := \sum_{n \ge 0} f_n r_n$ converge in $T$ with norms $\le \|f\|_T$.

By `(19)`, $g(t) = P_0(t) + E_0(t)$ where $P_0(t) := c_2 t^2 + c_1 t + 1$ ($c_2 \in \mathbb{Z}_2^\times$) and $\|E_0\|_T \le 2^{-2} \le 2^{-1}$. Set $v_0 := 1$. Inductively, given $v_k \in 1 + 2T$, $P_k(t) = c_2 t^2 + a_{k, 1} t + a_{k, 0} \equiv P_0(t) \pmod 2$, and $E_k \in T$ with $g v_k = P_k + E_k$ and $\|E_k\|_T \le 2^{-2^k}$:
1. Divide $E_k$ by $P_k$: $E_k = P_k q_k + R_k$ with $\|q_k\|_T, \|R_k\|_T \le \|E_k\|_T \le 2^{-2^k}$ and $\deg R_k \le 1$.
2. Set $P_{k+1} := P_k + R_k$ (same leading coefficient $c_2 \in \mathbb{Z}_2^\times$, $\|P_{k+1} - P_k\|_T \le 2^{-2^k}$) and $v_{k+1} := v_k (1 + q_k)^{-1} \in 1 + 2T$ (using $(1 + q_k)^{-1} = \sum_{j \ge 0} (-q_k)^j \in 1 + 2^{2^k} T$). Then
   $$g v_{k+1} = \bigl(P_k(1 + q_k) + R_k\bigr)(1 + q_k)^{-1} = P_k + R_k - R_k q_k (1 + q_k)^{-1} = P_{k+1} + E_{k+1},$$
   where $\|E_{k+1}\|_T = \|R_k q_k (1 + q_k)^{-1}\|_T \le \|E_k\|_T^2 \le 2^{-2^{k+1}}$.

Since $T$ is complete, $v := \lim_{k \to \infty} v_k \in 1 + 2T$ and $P(t) := \lim_{k \to \infty} P_k(t) = c_2 t^2 + a_1 t + a_0 \in \mathbb{Z}_2[t]$ (with $a_0 \equiv c_0 = 1 \pmod 2$ and $c_2 \in \mathbb{Z}_2^\times$) satisfy $g(t) v(t) = P(t)$ in $T$. Let $t_0 \in \overline{\mathbb{Q}}_2$ be a root of $P(t) = 0$. Since $c_2 \in \mathbb{Z}_2^\times$, $t_0$ and its conjugate $t'_0$ are integral over $\mathbb{Z}_2$ (hence $|t_0|_2, |t'_0|_2 \le 1$) and satisfy $|t_0 t'_0|_2 = |a_0 / c_2|_2 = 1$, forcing $|t_0|_2 = 1$. Evaluating $g(t) v(t) = P(t)$ at $t = t_0$ (both series converge at $|t_0|_2 = 1$) gives $g(t_0) v(t_0) = 0$. Since $v \in 1 + 2T$, $|v(t_0) - 1|_2 \le 1/2 < 1$, so $v(t_0) \neq 0$ and hence $g(t_0) = 0$. Setting $z_0 := 8/t_0 \in \overline{\mathbb{Q}}_2$ gives $|z_0|_2 = 2^{-3}$ and $\det S(z_0) = z_0^2 g(t_0) = 0$. $\square$

**Theorem 7 (Key scalar identity).**
The fixed point $\mathbf{u}_2 \in S(\mathbb{Q}_2)$ of $\Phi$ satisfies $(\mathbf{u}_2 B)_1 = 0$.

*Proof.*
Let $z_0 \in \overline{\mathbb{Q}}_2$ be given by Lemma 6 ($|z_0|_2 = 2^{-3}$, $\det S(z_0) = 0$), and put $K := \mathbb{Q}_2(z_0)$ (a finite extension of $\mathbb{Q}_2$, of degree $\le 2$). Let $V := \ker_{\mathcal{E}_2(K)}(B - z_0 I)$.
1. Since $|z_0|_2 = 2^{-3} > 2^{-5}$ and $\det S(z_0) = 0$, Lemma 5(2) gives $1 \le \dim_K V = \dim_K \ker_{K^2}(S(z_0)) \le 2$.
2. By Theorem 3(2), $W^2 = I$ and $W A = -A W$ on $\mathcal{E}_2(K)$. Decompose $\mathcal{E}_2(K) = \mathcal{E}_+ \oplus \mathcal{E}_-$ into the $\pm 1$-eigenspaces of $W$ ($\mathbf{u} = \frac{\mathbf{u} + W\mathbf{u}}{2} + \frac{\mathbf{u} - W\mathbf{u}}{2}$). Since $W A = -A W$, we have $A(\mathcal{E}_+) \subseteq \mathcal{E}_-$ and $A(\mathcal{E}_-) \subseteq \mathcal{E}_+$, so $B = A^2$ preserves both $\mathcal{E}_+$ and $\mathcal{E}_-$. Hence $V = V_+ \oplus V_-$ where $V_\pm := V \cap \mathcal{E}_\pm$. Since $A$ commutes with $B$, $A$ restricts to $K$-linear maps $A : V_+ \to V_-$ and $A : V_- \to V_+$ whose compositions in both orders equal $B|_V = z_0 \cdot \mathrm{id}_V$. Because $z_0 \neq 0$, $A : V_+ \xrightarrow{\sim} V_-$ is an isomorphism, so $\dim_K V = 2 \dim_K V_+$ is **even**.
3. Combining (1) and (2) forces $\dim_K \ker_{K^2}(S(z_0)) = \dim_K V = 2$, so the $2 \times 2$ matrix $S(z_0)$ is identically **zero**: $S(z_0) = 0$.
4. Consider the vector $\mathbf{w}_2 := \bigl(0,\, 1,\, e_2 B_{0Y}(z_0 I - B_{YY})^{-1}\bigr) \in \mathcal{E}_2(K)$ corresponding via Lemma 5(2) to $(0, 1) \in \ker(S(z_0))$. Then $\mathbf{w}_2 B = z_0 \mathbf{w}_2$; in particular,
   $$(\mathbf{w}_2 B)_1 = 0, \qquad (\mathbf{w}_2 B)_2 = z_0, \qquad (\mathbf{w}_2 B)_j = z_0 w_{2, j} \quad (\forall j \ge 3).$$
   We verify that $\mathbf{w}_2 \in S(K)$: set $S_0(K) := \{\mathbf{y} \in Y(K) : \nu_2(y_j) \ge 2j - 3\ \forall j \ge 3\}$. By Lemma 1(3), $\nu_2(B_{2, j}) \ge 2j$ for all $j \ge 3$, so $\nu_2(z_0^{-1} B_{2, j}) \ge 2j - 3$, i.e. $z_0^{-1} e_2 B_{0Y} \in S_0(K)$. Moreover, for any $\mathbf{y} \in S_0(K)$ and $j \ge 3$, `(18)` yields $\nu_2(z_0^{-1}(\mathbf{y} B_{YY})_j) \ge (2j + 2) - 3 = (2j - 3) + 2$, so $z_0^{-1} B_{YY}$ maps $S_0(K)$ into $2^2 S_0(K)$. Hence $\sum_{m \ge 0} z_0^{-(m+1)} e_2 B_{0Y} B_{YY}^m \in S_0(K)$, i.e. $\mathbf{w}_2 \in S(K)$.
5. Because $\mathbf{w}_2 \in S(K)$ satisfies $\Lambda(\mathbf{w}_2) = (\mathbf{w}_2 B)_2 = z_0$ and $\Phi(\mathbf{w}_2)_j = z_0^{-1}(\mathbf{w}_2 B)_j = w_{2, j}$ ($j \ge 3$), $\mathbf{w}_2$ is a fixed point of $\Phi$ in $S(K)$. By uniqueness in Lemma 4(3), $\mathbf{w}_2 = \mathbf{u}_2$ (and $z_0 = \Lambda \in 8\mathbb{Z}_2^\times$). Therefore $(\mathbf{u}_2 B)_1 = (\mathbf{w}_2 B)_1 = 0$. $\square$

---

## Step 4: Two-Dimensional $\Lambda$-Eigenspace and $2^7$-Contraction on $\ker(e_1, e_2)$

Since column $1$ of $A$ is $(16, 1, 0, 0, \ldots)^T$, every $\mathbf{w} = (0, 1, w_3, \ldots)$ satisfies $(\mathbf{w} A)_1 = 16 \cdot 0 + 1 = 1$ and $(\mathbf{w} B)_1 = ((\mathbf{w} A) A)_1 = 16(\mathbf{w} A)_1 + (\mathbf{w} A)_2 = 16 + (\mathbf{w} A)_2$. Applying Theorem 7 gives $(\mathbf{u}_2 A)_1 = 1$ and $(\mathbf{u}_2 A)_2 = -16$.

Define $\mathbf{u}_1 := \mathbf{u}_2(A + 16I) \in \mathcal{E}_2(\mathbb{Q}_2)$.

**Lemma 8 (Properties of $\mathbf{u}_1$ and the projection $M$).**
1. $u_{1, 1} = 1$, $u_{1, 2} = 0$, $\mathbf{u}_1 B = \Lambda \mathbf{u}_1$, and $\mathbf{u}_2 B = \Lambda \mathbf{u}_2$.
2. $\nu_2(u_{1, 3}) = 4$, $\nu_2(u_{1, 4}) = 6$, $\nu_2(u_{1, 5}) = 9$, $\nu_2(u_{1, 6}) \ge 12$, and $\nu_2(u_{1, j}) \ge 2j + 1$ for all $j \ge 7$.
3. Define the projection $\pi(\mathbf{x}) := \mathbf{x} - x_1 \mathbf{u}_1 - x_2 \mathbf{u}_2 \in Y(\mathbb{Q}_2)$ and $M(\mathbf{w}) := \pi(\mathbf{w} B)$ on $Y(\mathbb{Q}_2)$. Then $\pi(\mathbf{x} B) = M(\pi(\mathbf{x}))$ for all $\mathbf{x} \in \mathcal{E}_2(\mathbb{Q}_2)$ (in particular, $\pi(\mathbf{x}_{m+2}) = M(\pi(\mathbf{x}_m))$ for all $m \ge 1$), and
   $$\mathbf{x}_{m+2} - \Lambda \mathbf{x}_m = \pi(\mathbf{x}_m) B - \Lambda \pi(\mathbf{x}_m). \tag{20}$$
4. For all $k \ge 3$ and $j \ge 3$,
   $$\nu_2\bigl(M(e_k)_j\bigr) \ge 7 + 2j - 2k. \tag{21}$$
   Moreover, the exact low entries satisfy:
   - $\nu_2(M(e_3)_3) = 7$ with $M(e_3)_3 / 2^7 \equiv 1 \pmod 8$, $\nu_2(M(e_3)_4) = 11$;
   - $\nu_2(M(e_4)_3) = 8$, $\nu_2(M(e_4)_4) = 7$ with $M(e_4)_4 / 2^7 \equiv 5 \pmod 8$;
   - for $k = 5, 6, 7, 8$: $\nu_2(M(e_k)_3) = (7, 4, 3, 2)$ and $\nu_2(M(e_k)_4) = (7, 5, 13, 7)$.

*Proof.*
1. $u_{1, 1} = (\mathbf{u}_2 A)_1 + 16 u_{2, 1} = 1$, $u_{1, 2} = (\mathbf{u}_2 A)_2 + 16 u_{2, 2} = -16 + 16 = 0$, and $\mathbf{u}_1 B = (\mathbf{u}_2 B)(A + 16I) = \Lambda \mathbf{u}_2(A + 16I) = \Lambda \mathbf{u}_1$.
2. For any $j \ge 3$, $u_{1, j} = 16 u_{2, j} + \Phi_{2, j} + \sum_{k=3}^{2j} u_{2, k} \Phi_{k, j}$. Here $\nu_2(16 u_{2, j}) \ge 4 + (2j - 3) = 2j + 1$; for $k \ge 4$, $\nu_2(u_{2, k} \Phi_{k, j}) \ge (2k - 3) + (2j - k) = 2j + k - 3 \ge 2j + 1$; for $k = 3$, $\nu_2(u_{2, 3} \Phi_{3, j}) \ge 3 + (2j - 3) = 2j$, and $\Phi_{3, j} = 0$ for $j \ge 8$ (while at $j = 7$, $\Phi_{3, 7} = 72\Phi_{2, 5} = 2^{12} \cdot 3^8$ gives $\nu_2(u_{2, 3}\Phi_{3, 7}) \ge 15 = 2(7) + 1$). Since $\Phi_{2, j} = 0$ for $j \ge 6$ and $\nu_2(\Phi_{2, j}) = (4, 6, 9)$ for $j = (3, 4, 5)$, every valuation in (2) follows immediately (with $\nu_2(u_{1, j}) \ge 2j$ for $j \ge 6$ and $\ge 2j + 1$ for $j \ge 7$).
3. Since $\pi(\mathbf{u}_1) = \pi(\mathbf{u}_2) = 0$ and $\mathbf{x} = x_1 \mathbf{u}_1 + x_2 \mathbf{u}_2 + \pi(\mathbf{x})$, applying $B$ gives $\mathbf{x} B = \Lambda(x_1 \mathbf{u}_1 + x_2 \mathbf{u}_2) + \pi(\mathbf{x}) B$, which yields both $\pi(\mathbf{x} B) = \pi(\pi(\mathbf{x}) B) = M(\pi(\mathbf{x}))$ and `(20)`.
4. Write $M(e_k)_j = B_{k, j} - B_{k, 1} u_{1, j} - B_{k, 2} u_{2, j}$. We check four exhaustive cases:
   - **$k \ge 9$, $j \ge 3$:** By Lemma 1(1)–(2), $B_{k, 1} = B_{k, 2} = 0$, so $\nu_2(M(e_k)_j) = \nu_2(B_{k, j}) \ge 2j - \lfloor k/2 \rfloor = (7 + 2j - 2k) + (\lceil 3k/2 \rceil - 7) \ge 7 + 2j - 2k + 7$.
   - **$5 \le k \le 8$, $j \ge 3$:** By Lemma 1(1), $B_{k, 1} = 0$. For $B_{k, j}$, $\nu_2(B_{k, j}) \ge 2j - \lfloor k/2 \rfloor = (7 + 2j - 2k) + (\lceil 3k/2 \rceil - 7)$, with $\lceil 3k/2 \rceil - 7 = (1, 2, 4, 5) > 0$. For $B_{k, 2} u_{2, j}$, Lemma 1(3) gives $\nu_2(B_{k, 2}) + (2j - 3) = (7 + 2j - 2k) + (\nu_2(B_{k, 2}) + 2k - 10)$, where $\nu_2(B_{k, 2}) + 2k - 10 = (3, 3, 5, 6) > 0$.
   - **$k \in \{3, 4\}$, $j \ge 20$:** Since $4k + 3 \le 19 < j$, Lemma 1(1) gives $B_{k, j} = 0$. Using $\nu_2(u_{1, j}) \ge 2j + 1$ and $\nu_2(u_{2, j}) \ge 2j - 2$:
     - for $k = 3$ (target $2j + 1$): $\nu_2(B_{3, 1} u_{1, j}) \ge 1 + (2j + 1) = 2j + 2$ and $\nu_2(B_{3, 2} u_{2, j}) \ge 7 + (2j - 2) = 2j + 5$;
     - for $k = 4$ (target $2j - 1$): $\nu_2(B_{4, 1} u_{1, j}) \ge 0 + (2j + 1) = 2j + 1$ and $\nu_2(B_{4, 2} u_{2, j}) \ge 3 + (2j - 2) = 2j + 1$.
   - **Finite box $k \in \{3, 4\}$, $3 \le j \le 19$ (and low entries for $5 \le k \le 8$, $j \in \{3, 4\}$):** By Lemma 4(2), starting from $\mathbf{w}^{(0)} = (0, 1, 0, \ldots) \in S(\mathbb{Q}_2)$, the $N$-th iterate $\mathbf{u}_2^{(N)} := \Phi^N(\mathbf{w}^{(0)})$ satisfies $d(\mathbf{u}_2^{(N)}, \mathbf{u}_2) \le 2^{-2N}$, i.e., $\nu_2(u_{2, j}^{(N)} - u_{2, j}) \ge 2j - 3 + 2N$ for all $j \ge 3$, and consequently $\mathbf{u}_1^{(N)} := \mathbf{u}_2^{(N)}(A + 16I)$ satisfies $\nu_2(u_{1, j}^{(N)} - u_{1, j}) \ge 2j + 2N$ for all $j \ge 3$ (by the same estimate as in (2) shifted by $2N$). Taking $N = 25$ ($2N = 50$), the error in $M(e_k)_j$ for $3 \le k \le 8, 3 \le j \le 19$ has valuation $\ge 2j + 47 \ge 53$, strictly exceeding every required valuation $\le 2(19) + 1 = 39$ (and every exact valuation $\le 49$ in the box!). Exact integer evaluation of $M^{(25)}(e_k)_j$ (executed with zero floats in `verify.py`) confirms `(21)` on all $34$ entries $(k, j) \in \{3, 4\} \times \{3, \ldots, 19\}$ (with minimum margin $0$, attained at $(3, 3), (3, 6), (3, 7), (3, 8), (4, 4), (4, 6)$) and verifies all low entries listed in (4). $\square$

---

## Step 5: Exact Induction for Odd and Even $k$ (Conjecture 8.1 and Best-Possible Modulus)

Set $\boldsymbol{\pi}^{(m)} := \pi(\mathbf{x}_m)$ for $m \ge 1$.

### 5.1 Odd $m = 2\mu + 1$ ($k = 2\mu + 3$, target exponent $\lfloor 7(k+1)/2 \rfloor = 7\mu + 14$)

**Proposition 9 (Odd $m$).**
For every integer $\mu \ge 0$:
1. $\nu_2(\pi^{(2\mu+1)}_j) \ge 7\mu + 4 + 2j$ for all $j \ge 3$;
2. $\pi^{(2\mu+1)}_3 \equiv 3 \cdot 2^{7\mu + 11} \pmod{2^{7\mu + 13}}$ (in particular $\nu_2(\pi^{(2\mu+1)}_3) = 7\mu + 11$);
3. $\pi^{(2\mu+1)}_4 \equiv 1 \cdot 2^{7\mu + 12} \pmod{2^{7\mu + 14}}$ (in particular $\nu_2(\pi^{(2\mu+1)}_4) = 7\mu + 12$).

*Proof.*
We proceed by induction on $\mu \ge 0$.

**Base case $\mu = 0$ ($m = 1$):** From `(2)`, $\mathbf{x}_1$ has $\nu_2(x_{1, 1}) = \nu_2(x_{1, 2}) = 7$ and $x_{1, j} = 0$ for $j \ge 5$. For all $j \ge 6$, Lemma 8(2) and Lemma 4(3) give $\nu_2(x_{1, 1} u_{1, j}) \ge 7 + 2j > 4 + 2j$ and $\nu_2(x_{1, 2} u_{2, j}) \ge 7 + (2j - 3) = 4 + 2j$, proving (1) analytically for $j \ge 6$. For $j \in \{3, 4, 5\}$, exact evaluation via $\mathbf{u}_1^{(25)}, \mathbf{u}_2^{(25)}$ (error valuation $\ge 2j + 54 \ge 60$) gives $\pi^{(1)}_3 / 2^{11} \equiv 3 \pmod 8$, $\pi^{(1)}_4 / 2^{12} \equiv 5 \equiv 1 \pmod 4$, and $\nu_2(\pi^{(1)}_5) = 16 \ge 14$, establishing (1)–(3) for $\mu = 0$.

**Inductive step ($\mu \to \mu + 1$):** Assume (1)–(3) for $\mu$. Since $\boldsymbol{\pi}^{(2\mu+3)} = M(\boldsymbol{\pi}^{(2\mu+1)})$:
- For any $j \ge 3$, Lemma 8(4) gives
  $$\nu_2(\pi^{(2\mu+3)}_j) \ge \min_{k \ge 3}\bigl((7\mu + 4 + 2k) + (7 + 2j - 2k)\bigr) = 7(\mu + 1) + 4 + 2j,$$
  proving (1) for $\mu + 1$.
- For $j = 3$ modulo $2^{7(\mu+1) + 13} = 2^{7\mu + 20}$, inspect each term $\pi^{(2\mu+1)}_k M(e_k)_3$ ($k \ge 3$):
  - $k = 3$: by (2) and Lemma 8(4), $\pi^{(2\mu+1)}_3 M(e_3)_3 \equiv (3 \cdot 2^{7\mu+11}) \cdot (1 \cdot 2^7) = 3 \cdot 2^{7\mu+18} \pmod{2^{7\mu+20}}$;
  - $k = 4$: by (3) and Lemma 8(4), $\nu_2(\pi^{(2\mu+1)}_4 M(e_4)_3) = (7\mu + 12) + 8 = 7\mu + 20$;
  - $k = 5, 6, 7, 8$: by (1) and Lemma 8(4), $\nu_2(\pi^{(2\mu+1)}_k M(e_k)_3) \ge (7\mu + 4 + 2k) + (7, 4, 3, 2) = 7\mu + (21, 20, 21, 22) \ge 7\mu + 20$;
  - $k \ge 9$: by Lemma 1(1)–(2), $M(e_k)_3 = B_{k, 3}$ vanishes for $k \ge 13$, and for $9 \le k \le 12$ has $\nu_2(\pi^{(2\mu+1)}_k B_{k, 3}) \ge (7\mu + 4 + 2k) + (6 - \lfloor k/2 \rfloor) \ge 7\mu + 24$.
  Summing gives $\pi^{(2\mu+3)}_3 \equiv 3 \cdot 2^{7(\mu+1) + 11} \pmod{2^{7(\mu+1) + 13}}$, proving (2).
- For $j = 4$ modulo $2^{7(\mu+1) + 14} = 2^{7\mu + 21}$, inspect each term $\pi^{(2\mu+1)}_k M(e_k)_4$ ($k \ge 3$):
  - $k = 3$: by (2) and Lemma 8(4), $\nu_2(\pi^{(2\mu+1)}_3 M(e_3)_4) = (7\mu + 11) + 11 = 7\mu + 22 > 7\mu + 21$;
  - $k = 4$: by (3) and Lemma 8(4) ($M(e_4)_4 / 2^7 \equiv 5 \equiv 1 \pmod 4$), $\pi^{(2\mu+1)}_4 M(e_4)_4 \equiv (1 \cdot 2^{7\mu+12})(1 \cdot 2^7) = 1 \cdot 2^{7\mu+19} \pmod{2^{7\mu+21}}$;
  - $k = 5, 6, 7, 8$: by (1) and Lemma 8(4), $\nu_2(\pi^{(2\mu+1)}_k M(e_k)_4) \ge (7\mu + 4 + 2k) + (7, 5, 13, 7) = 7\mu + (21, 21, 31, 27) \ge 7\mu + 21$;
  - $k \ge 9$: $M(e_k)_4 = B_{k, 4}$ vanishes for $k \ge 17$, and for $9 \le k \le 16$ has $\nu_2(\pi^{(2\mu+1)}_k B_{k, 4}) \ge (7\mu + 4 + 2k) + (8 - \lfloor k/2 \rfloor) \ge 7\mu + 26$.
  Summing gives $\pi^{(2\mu+3)}_4 \equiv 1 \cdot 2^{7(\mu+1) + 12} \pmod{2^{7(\mu+1) + 14}}$, proving (3). $\square$

**Deduction of Theorem for all odd $k = 2\mu + 3 \ge 3$:**
Write $m = 2\mu + 1$ and $\mathbf{d} := \mathbf{x}_{m+2} - \Lambda \mathbf{x}_m = \boldsymbol{\pi}^{(m)} B - \Lambda \boldsymbol{\pi}^{(m)}$. Using Proposition 9 and Lemma 1(3):
- **$j = 1$:** $d_1 = 26 \pi^{(m)}_3 + \pi^{(m)}_4 \equiv 26(3 \cdot 2^{7\mu+11}) + 1 \cdot 2^{7\mu+12} = (39 + 1) \cdot 2^{7\mu+12} = 10 \cdot 2^{7\mu+14} \equiv 0 \pmod{2^{7\mu+14}}$, so $\nu_2(d_1) \ge 7\mu + 14$.
- **$j = 2$:** $d_2 = \sum_{k=3}^{8} \pi^{(m)}_k B_{k, 2}$ has $\nu_2(d_2) \ge \min\bigl(7 + (7\mu+11),\, 3 + (7\mu+12),\, 3 + (7\mu+14),\, 1 + (7\mu+16),\, 1 + (7\mu+18),\, 0 + (7\mu+20)\bigr) = 7\mu + 15$.
- **$j = 3$:** Since $(\boldsymbol{\pi}^{(m)} B)_3 = M(\boldsymbol{\pi}^{(m)})_3 + d_1 u_{1, 3} + d_2 u_{2, 3}$, we have $\nu_2(M(\boldsymbol{\pi}^{(m)})_3) = 7\mu + 18$, $\nu_2(d_1 u_{1, 3}) \ge (7\mu + 14) + 4 = 7\mu + 18$, and $\nu_2(d_2 u_{2, 3}) \ge (7\mu + 15) + 3 = 7\mu + 18$, so $\nu_2((\boldsymbol{\pi}^{(m)} B)_3) \ge 7\mu + 18$. Meanwhile $\nu_2(-\Lambda \pi^{(m)}_3) = 3 + (7\mu + 11) = 7\mu + 14$. Thus **$\nu_2(d_3) = 7\mu + 14$ exactly**.
- **$j \ge 4$:** Similarly, $\nu_2(-\Lambda \pi^{(m)}_j) \ge 3 + (7\mu + 4 + 2j) \ge 7\mu + 15$, while $(\boldsymbol{\pi}^{(m)} B)_j = M(\boldsymbol{\pi}^{(m)})_j + d_1 u_{1, j} + d_2 u_{2, j}$ has $\nu_2(M(\boldsymbol{\pi}^{(m)})_j) \ge 7\mu + 11 + 2j \ge 7\mu + 19$, $\nu_2(d_1 u_{1, j}) \ge (7\mu + 14) + 6 = 7\mu + 20$ (by Lemma 8(2)), and $\nu_2(d_2 u_{2, j}) \ge (7\mu + 15) + 5 = 7\mu + 20$. Thus $\nu_2(d_j) \ge 7\mu + 15$ for all $j \ge 4$.

By Saikia's Lemma 5.2 (`\ref{lem:refined}`), $\nu_2(x_{m, 1}) = \nu_2(x_{m, 2}) = 3\mu + 7$, $\nu_2(x_{m+2, 1}) = 3\mu + 10$, and $\nu_2(x_{m, j}) \ge 3\mu + 4 + 2j$ ($j \ge 3$). Choose an odd integer $\lambda_k$ such that $x_{m+2, 1} \equiv 8\lambda_k x_{m, 1} \pmod{2^{7\mu+15}}$, and set $\Delta\Lambda := 8\lambda_k - \Lambda$ and $\tilde{\mathbf{d}} := \mathbf{x}_{m+2} - 8\lambda_k \mathbf{x}_m = \mathbf{d} - \Delta\Lambda\,\mathbf{x}_m$. Then $\nu_2(\Delta\Lambda \cdot x_{m, 1}) = \nu_2(d_1 - \tilde{d}_1) \ge 7\mu + 14$, whence $\nu_2(\Delta\Lambda) \ge (7\mu + 14) - (3\mu + 7) = 4\mu + 7$. It follows that:
- $\nu_2(\tilde{d}_1) \ge 7\mu + 15$;
- $\nu_2(\tilde{d}_2) \ge \min(\nu_2(d_2),\, \nu_2(\Delta\Lambda \cdot x_{m, 2})) \ge \min(7\mu + 15,\, 7\mu + 14) = 7\mu + 14$;
- $\nu_2(\Delta\Lambda \cdot x_{m, 3}) \ge (4\mu + 7) + (3\mu + 10) = 7\mu + 17$, so **$\nu_2(\tilde{d}_3) = 7\mu + 14$ exactly**;
- for $j \ge 4$, $\nu_2(\Delta\Lambda \cdot x_{m, j}) \ge (4\mu + 7) + (3\mu + 4 + 2j) \ge 7\mu + 19$, so $\nu_2(\tilde{d}_j) \ge 7\mu + 15$.

Since $\varrho, \xi \in \mathbb{Z}[[q]]$, substituting $\tilde{\mathbf{d}} \equiv \mathbf{0} \pmod{2^{7\mu+14}}$ into `(1)` yields `\eqref{eq:sharp}` modulo $2^{7\mu+14} = 2^{\lfloor 7(k+1)/2 \rfloor}$ for all $n \ge 0$. For **sharpness**, suppose any integer $\lambda'_k$ satisfies `\eqref{eq:sharp}` modulo $2^{7\mu+15}$ for all $n \ge 0$. Since $\varrho = 1 + O(q)$ and $\xi = q + O(q^2)$, extracting $[q^1]$ from `(1)` forces $x_{m+2, 1} \equiv 8\lambda'_k x_{m, 1} \pmod{2^{7\mu+15}}$ (which also forces $\lambda'_k$ to be odd), so the estimates above apply to $\lambda'_k$ and yield
$$\sum_{n \ge 0} \bigl(\mathrm{PDO}_{\mathrm{t}}(3 \times 2^{k+2} n) - 8\lambda'_k\,\mathrm{PDO}_{\mathrm{t}}(3 \times 2^k n)\bigr) q^n \equiv \tilde{d}_2\,\varrho\xi^2 + 2^{7\mu+14}\,\varrho\xi^3 \pmod{2^{7\mu+15}}.$$
If $\tilde{d}_2 \equiv 2^{7\mu+14} \pmod{2^{7\mu+15}}$, then $[q^2]$ equals $\tilde{d}_2 \not\equiv 0 \pmod{2^{7\mu+15}}$; if $\tilde{d}_2 \equiv 0 \pmod{2^{7\mu+15}}$, then $[q^3]$ equals $2^{7\mu+14} \not\equiv 0 \pmod{2^{7\mu+15}}$. In either case, the congruence fails modulo $2^{7\mu+15}$ at $n = 2$ or $n = 3$.

### 5.2 Even $m = 2\mu + 2$ ($k = 2\mu + 4$, target exponent $\lfloor 7(k+1)/2 \rfloor = 7\mu + 17$)

**Proposition 10 (Even $m$).**
For every integer $\mu \ge 0$:
1. $\nu_2(\pi^{(2\mu+2)}_j) \ge 7\mu + 8 + 2j$ for all $j \ge 3$;
2. $\nu_2(\pi^{(2\mu+2)}_3) = 7\mu + 14$.

*Proof.*
We proceed by induction on $\mu \ge 0$.

**Base case $\mu = 0$ ($m = 2$):** By `(1)` and Lemma 5.2 (`\ref{lem:refined}`), $\mathbf{x}_2 = \mathbf{x}_1 A$ is supported on $1 \le j \le 9$ with $\nu_2(x_{2, 1}) = 7$ and $\nu_2(x_{2, 2}) = 10$. For all $j \ge 10$, Lemma 8(2) and Lemma 4(3) give $\nu_2(x_{2, 1} u_{1, j}) \ge 7 + (2j + 1) = 8 + 2j$ and $\nu_2(x_{2, 2} u_{2, j}) \ge 10 + (2j - 2) = 8 + 2j$, proving (1) analytically for all $j \ge 10$. For $3 \le j \le 9$, exact evaluation via $\mathbf{u}_1^{(25)}, \mathbf{u}_2^{(25)}$ (error valuation $\ge 2j + 57 \ge 63$) gives $\nu_2(\pi^{(2)}_j) = (14, 16, 26, 25, 22, 24, 27) \ge (14, 16, 18, 20, 22, 24, 26) = 8 + 2j$, with equality $\nu_2(\pi^{(2)}_3) = 14$.

**Inductive step ($\mu \to \mu + 1$):** Assume (1)–(2) for $\mu$. Since $\boldsymbol{\pi}^{(2\mu+4)} = M(\boldsymbol{\pi}^{(2\mu+2)})$:
- For any $j \ge 3$, Lemma 8(4) gives
  $$\nu_2(\pi^{(2\mu+4)}_j) \ge \min_{k \ge 3}\bigl((7\mu + 8 + 2k) + (7 + 2j - 2k)\bigr) = 7(\mu + 1) + 8 + 2j.$$
- For $j = 3$, inspect each term $\pi^{(2\mu+2)}_k M(e_k)_3$ ($k \ge 3$):
  - $k = 3$: by (2) and Lemma 8(4), $\nu_2(\pi^{(2\mu+2)}_3 M(e_3)_3) = (7\mu + 14) + 7 = 7\mu + 21$;
  - $k = 4$: $\nu_2(\pi^{(2\mu+2)}_4 M(e_4)_3) \ge (7\mu + 16) + 8 = 7\mu + 24$;
  - $k = 5, 6, 7, 8$: $\nu_2(\pi^{(2\mu+2)}_k M(e_k)_3) \ge (7\mu + 8 + 2k) + (7, 4, 3, 2) = 7\mu + (25, 24, 25, 26) \ge 7\mu + 24$;
  - $k \ge 9$: $M(e_k)_3 = B_{k, 3}$ vanishes for $k \ge 13$, and for $9 \le k \le 12$ has $\nu_2(\pi^{(2\mu+2)}_k B_{k, 3}) \ge (7\mu + 8 + 2k) + (6 - \lfloor k/2 \rfloor) \ge 7\mu + 28$.
  Because $k = 3$ is the unique minimum, $\nu_2(\pi^{(2\mu+4)}_3) = 7(\mu + 1) + 14$. $\square$

**Deduction of Theorem for all even $k = 2\mu + 4 \ge 4$:**
Write $m = 2\mu + 2$ and $\mathbf{d} := \mathbf{x}_{m+2} - \Lambda \mathbf{x}_m = \boldsymbol{\pi}^{(m)} B - \Lambda \boldsymbol{\pi}^{(m)}$. Using Proposition 10 and Lemma 1(3):
- **$j = 1$:** $d_1 = 26 \pi^{(m)}_3 + \pi^{(m)}_4$ has $\nu_2(d_1) \ge \min(1 + 7\mu + 14,\, 7\mu + 16) = 7\mu + 15$.
- **$j = 2$:** $d_2 = \sum_{k=3}^{8} \pi^{(m)}_k B_{k, 2}$ has $\nu_2(d_2) \ge \min\bigl(7 + 14,\, 3 + 16,\, 3 + 18,\, 1 + 20,\, 1 + 22,\, 0 + 24\bigr) + 7\mu = 7\mu + 19$.
- **$j = 3$:** $(\boldsymbol{\pi}^{(m)} B)_3 = M(\boldsymbol{\pi}^{(m)})_3 + d_1 u_{1, 3} + d_2 u_{2, 3}$ has valuation $\ge \min(7\mu + 21,\, 7\mu + 15 + 4,\, 7\mu + 19 + 3) = 7\mu + 19$, whereas $\nu_2(-\Lambda \pi^{(m)}_3) = 3 + (7\mu + 14) = 7\mu + 17$. Thus **$\nu_2(d_3) = 7\mu + 17$ exactly**.
- **$j \ge 4$:** $\nu_2(-\Lambda \pi^{(m)}_j) \ge 3 + (7\mu + 8 + 2j) \ge 7\mu + 19$, and $(\boldsymbol{\pi}^{(m)} B)_j = M(\boldsymbol{\pi}^{(m)})_j + d_1 u_{1, j} + d_2 u_{2, j}$ has valuation $\ge \min(7\mu + 15 + 2j,\, 7\mu + 15 + 6,\, 7\mu + 19 + 5) \ge 7\mu + 21$. Thus $\nu_2(d_j) \ge 7\mu + 19$ for all $j \ge 4$.

By Saikia's Lemma 5.2 (`\ref{lem:refined}`), $\nu_2(x_{m, 1}) = 3\mu + 7$, $\nu_2(x_{m+2, 1}) = 3\mu + 10$, $\nu_2(x_{m, 2}) = 3\mu + 10$, and $\nu_2(x_{m, j}) \ge 3\mu + 5 + 2j \ge 3\mu + 11$ ($j \ge 3$). Choose an odd integer $\lambda_k$ such that $x_{m+2, 1} \equiv 8\lambda_k x_{m, 1} \pmod{2^{7\mu+18}}$, and set $\Delta\Lambda := 8\lambda_k - \Lambda$ and $\tilde{\mathbf{d}} := \mathbf{x}_{m+2} - 8\lambda_k \mathbf{x}_m = \mathbf{d} - \Delta\Lambda\,\mathbf{x}_m$. Then $\nu_2(\Delta\Lambda \cdot x_{m, 1}) = \nu_2(d_1 - \tilde{d}_1) \ge 7\mu + 15$, so $\nu_2(\Delta\Lambda) \ge (7\mu + 15) - (3\mu + 7) = 4\mu + 8$. Consequently, for every $j \ge 2$, $\nu_2(\Delta\Lambda \cdot x_{m, j}) \ge (4\mu + 8) + (3\mu + 10) = 7\mu + 18$. Therefore:
- $\nu_2(\tilde{d}_1) \ge 7\mu + 18$, $\nu_2(\tilde{d}_2) \ge 7\mu + 18$, **$\nu_2(\tilde{d}_3) = 7\mu + 17$ exactly**, and $\nu_2(\tilde{d}_j) \ge 7\mu + 18$ for all $j \ge 4$.

Substituting into `(1)` proves `\eqref{eq:sharp}` modulo $2^{7\mu+17} = 2^{\lfloor 7(k+1)/2 \rfloor}$ for all $n \ge 0$. For **sharpness**, any integer $\lambda'_k$ satisfying `\eqref{eq:sharp}` modulo $2^{7\mu+18}$ for all $n \ge 0$ must satisfy $x_{m+2, 1} \equiv 8\lambda'_k x_{m, 1} \pmod{2^{7\mu+18}}$ (from $[q^1]$), so the same calculation gives
$$\sum_{n \ge 0} \bigl(\mathrm{PDO}_{\mathrm{t}}(3 \times 2^{k+2} n) - 8\lambda'_k\,\mathrm{PDO}_{\mathrm{t}}(3 \times 2^k n)\bigr) q^n \equiv 2^{7\mu+17}\,\varrho\xi^3 \pmod{2^{7\mu+18}},$$
whose $[q^3]$-coefficient is $2^{7\mu+17} \not\equiv 0 \pmod{2^{7\mu+18}}$. Thus `\eqref{eq:sharp}` fails modulo $2^{7\mu+18}$ at $n = 3$.

This completes the proof of Conjecture 8.1 and best-possible sharpness for all $k \ge 3$. $\blacksquare$

---

## Verification

The zero-float exact-arithmetic script `verify.py` independently verifies:
1. All algebraic identities in Lemma 2 and Theorem 3 ($W_3^2 = I$, $W_3 \tilde{A} = -\tilde{A} W_3$, $W^2 = I$, $W A = -A W$, lift identities `(13)`–`(16)`, and row-1/row-2 base checks of Lemma 2) using exact symbolic rational arithmetic.
2. All exact integer constants in Lemma 1(3), Lemma 5(3), and Lemma 6 (plus an explicit quadratic Weierstrass–Hensel check confirming the double root $z_0 = \Lambda$).
3. The rigorous $N = 25$ $\Phi$-contraction computation of $\mathbf{u}_2^{(25)}, \mathbf{u}_1^{(25)}$ (guaranteed error $\ge 2j + 47$), confirming $(\mathbf{u}_2^{(25)} B)_1 \equiv 0 \pmod{2^{50}}$, all $34$ finite-box entries of Lemma 8(4) (`k in {3, 4}, 3 <= j <= 19`), all low entries `M(e_k)_3, M(e_k)_4` (`3 <= k <= 8`), and the base cases of Propositions 9 and 10.
4. Direct end-to-end verification of `\eqref{eq:sharp}` and exact sharpness (matching exact $q$-series coefficients of $\mathrm{PDO}_{\mathrm{t}}(n)$ from `eq:gf` for small $k$, and exact coefficient vectors $\mathbf{x}_m$ for $3 \le k \le 20$).

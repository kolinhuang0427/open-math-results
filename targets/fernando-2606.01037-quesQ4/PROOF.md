# Complete Solution to Question 6.4 of Fernando and Kousik (`arXiv:2606.01037v1`)

## 1. Problem Statement and Main Theorem

From Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1` (31 May 2026), Section 6 (`draftMay31.tex`, lines 923–926, `\label{Q4}`):

> **Question 6.4 (`\label{Q4}`).** Let $q > 2$ be even and $e > 2$ a positive integer. Let $n = (q - 1) \cdot q^0 + (q - 2) \cdot q^2 + 1 \cdot q^e + 1 \cdot q^{e+2}$. Find conditions on $q$ and $e$ for which
> $$g_{n,q} = X^q + S_e^2\, S_2^{q - 2} + S_e S_2^{q - 1}$$
> is a PP of $\mathbb{F}_{q^e}$.

Here $q = 2^m$ with $m \ge 2$, $e \ge 3$ is an integer, the polynomial $g_{n,q} \in \mathbb{F}_2[X]$ is uniquely defined by $\sum_{a \in \mathbb{F}_q} (X + a)^n = g_{n,q}(X^q - X)$ (Section 1, Eq. (1.1)), and $S_r(X) := X + X^q + \cdots + X^{q^{r-1}}$ for $r \ge 1$ ($S_0 := 0$, $S_2(X) = X + X^q$). On $\mathbb{F}_{q^e}$, $S_e = \mathrm{Tr}_{q^e/q}$.

> **Main Theorem.** Let $q = 2^m > 2$ ($m \ge 2$), let $e > 2$ be an integer, and let $n = (q - 1) + (q - 2) q^2 + q^e + q^{e+2}$. Then $g_{n,q}$ is a permutation polynomial (PP) of $\mathbb{F}_{q^e}$ **if and only if**
> $$(q, e) = (4, 4).$$

*(Note: $(q, e) = (4, 4)$ corresponds to the desirable triple $(n, e; q) = (4387, 4; 4)$ in Table 1 of `arXiv:2606.01037v1`.)*

---

## 2. Derivation of $g_{n,q}$ and Exact Reduction to $(s, \Psi)$

All finite-field algebra below takes place in characteristic $2$.

### Lemma 2.1 (Explicit formula for $g_{n,q}$ on $\mathbb{F}_{q^e}$)
For every even $q > 2$, integer $e > 2$, and $n = (q - 1) + (q - 2) q^2 + q^e + q^{e+2}$,
$$g_{n,q}(X) \equiv X^q + S_e(X)^2 S_2(X)^{q - 2} + S_e(X) S_2(X)^{q - 1} \pmod{X^{q^e} - X}.$$

**Proof.** Put $Y := X^q + X$, so $S_r(Y) = \sum_{i=0}^{r-1}(X^{q^{i+1}} + X^{q^i}) = X^{q^r} + X$ for $r \ge 1$. For any integers $l, k \ge 0$, using $X^{q^k} + a = (X + a) + S_k(Y)$ ($a \in \mathbb{F}_q$) in Eq. (1.1) yields the recurrence (Proposition 2.1 of `arXiv:2606.01037v1`, Hou 2012):
$$g_{l + q^k, q}(Y) = \sum_{a \in \mathbb{F}_q} (X + a)^l (X^{q^k} + a) = g_{l + 1, q}(Y) + S_k(Y) g_{l, q}(Y).$$
Recall that over $\mathbb{F}_q$ ($q = 2^m > 2$), $\sum_{a \in \mathbb{F}_q} a^r = 1$ if $r \in \{q - 1, 2q - 2\}$, and $0$ if $0 \le r \le q - 2$ or $r = q$. Set $l_0 := (q - 1) + (q - 2) q^2$.
1. **Evaluation of $g_{l_0 + 1, q}$:** Since $l_0 + 1 = q + (q - 2) q^2$,
   $$g_{l_0 + 1, q}(Y) = \sum_{a \in \mathbb{F}_q} (X^q + a) \sum_{j=0}^{q-2} \binom{q - 2}{j} X^{j q^2} a^{q - 2 - j}.$$
   In the $X^q$ sum every exponent $q - 2 - j$ is at most $q - 2$, so it vanishes. In the $a$ sum the exponent $q - 1 - j$ equals $q - 1$ only at $j = 0$, giving $g_{l_0 + 1, q}(Y) = 1$.
2. **Evaluation of $g_{l_0 + 2, q}$:** Since $l_0 + 2 = (q + 1) + (q - 2) q^2$,
   $$g_{l_0 + 2, q}(Y) = \sum_{a \in \mathbb{F}_q} \bigl(X^{q+1} + Y a + a^2\bigr) \sum_{j=0}^{q-2} \binom{q - 2}{j} X^{j q^2} a^{q - 2 - j}.$$
   The $X^{q+1}$ sum has $a$-powers $\le q - 2$ (sum $0$). The $Y a$ sum selects $j = 0$, giving $Y$. The $a^2$ sum has $a$-power $q - j$, which equals $q - 1$ at $j = 1$ with coefficient $\binom{q - 2}{1} = q - 2 \equiv 0 \pmod 2$, and equals $q$ at $j = 0$ (sum $0$ since $q > 2$). Thus $g_{l_0 + 2, q}(Y) = Y$.
3. **Evaluation of $g_{l_0, q}$:** By Lucas's theorem $\binom{q-1}{j} \equiv 1 \pmod 2$ for $0 \le j \le q - 1$, so
   $$g_{l_0 + q^2, q}(Y) = \sum_{a \in \mathbb{F}_q} (X + a)^{q-1}(X^{q^2} + a)^{q-1} = \sum_{i,j=0}^{q-1} X^i X^{j q^2} \sum_{a \in \mathbb{F}_q} a^{2q - 2 - i - j} = 1 + (X + X^{q^2})^{q-1} = 1 + S_2(Y)^{q-1}.$$
   By the recurrence, $S_2 g_{l_0, q} = g_{l_0 + q^2, q} + g_{l_0 + 1, q} = (1 + S_2^{q-1}) + 1 = S_2^{q-1}$, whence $g_{l_0, q} = S_2^{q - 2}$ (Lemma 2.5 of `arXiv:2606.01037v1`).

Applying the recurrence twice to $n = l_0 + q^e + q^{e+2}$:
$$g_{l_0 + q^e, q} = g_{l_0 + 1, q} + S_e g_{l_0, q} = 1 + S_e S_2^{q-2}, \qquad g_{l_0 + 1 + q^e, q} = g_{l_0 + 2, q} + S_e g_{l_0 + 1, q} = X + S_e,$$
$$g_{n, q}(X) = g_{l_0 + 1 + q^e, q}(X) + S_{e+2}(X) g_{l_0 + q^e, q}(X) = X + S_e + S_{e+2}\bigl(1 + S_e S_2^{q-2}\bigr).$$
Modulo $X^{q^e} - X$, we have $S_{e+2}(X) = S_e(X) + X^{q^e} + X^{q^{e+1}} \equiv S_e(X) + S_2(X)$, so
$$g_{n, q}(X) \equiv X + S_e + (S_e + S_2)(1 + S_e S_2^{q-2}) = (X + S_2) + S_e^2 S_2^{q-2} + S_e S_2^{q-1} = X^q + S_e^2 S_2^{q-2} + S_e S_2^{q-1}. \quad \square$$

---

### Lemma 2.2 (Reduction to $(s, \Psi)$ on $\Omega_e$)
For any even $q = 2^m > 2$ and integer $e > 2$, define the domain $\Omega_e \subset \mathbb{F}_{q^e}$ by
$$\Omega_e := \begin{cases} H_e := \{y \in \mathbb{F}_{q^e} : S_e(y) = 0\} & \text{if } e \text{ is odd}, \\ D_e := \{y \in \mathbb{F}_{q^e} : \mathrm{Tr}_{q^e/q^2}(y) = 1\} & \text{if } e \text{ is even}. \end{cases}$$
For $y \in \Omega_e$, set $w(y) := y^{q-2}(y + 1) = y^{q-1} + y^{q-2}$ and
$$s(y) := 1 + S_e\bigl(w(y)\bigr) \in \mathbb{F}_q.$$
When $s(y) \neq 0$, define
$$\Psi(y) := \frac{y^q + S_2\bigl(w(y)\bigr)}{s(y)}.$$
Then $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ **if and only if** both:
1. $s(y) \neq 0$ for all $y \in \Omega_e$, and
2. $\Psi$ maps $\Omega_e$ bijectively onto $\Omega_e$.

**Proof.** Write $g_{n,q}(X) = X^q + S_e(X) S_2(X)^{q-2}(S_2(X) + S_e(X))$ on $\mathbb{F}_{q^e}$. Since $q - 2 \ge 2$, $g_{n,q}$ is $\mathbb{F}_q$-homogeneous of degree $1$: $g_{n,q}(cX) = c g_{n,q}(X)$ for all $c \in \mathbb{F}_q$.
- On $\ker(S_e)$, $g_{n,q}(X) = X^q$ maps $\ker(S_e)$ bijectively onto $\ker(S_e)$.
- On $\{X_1 \in \mathbb{F}_{q^e} : S_e(X_1) = 1\}$, put $y := S_2(X_1) = X_1 + X_1^q$. Then $g_{n,q}(X_1) = X_1^q + w(y)$, so
  $$S_e\bigl(g_{n,q}(X_1)\bigr) = 1 + S_e(w(y)) = s(y), \qquad S_2\bigl(g_{n,q}(X_1)\bigr) = y^q + S_2(w(y)).$$

We determine the image $S_2(\{S_e = 1\})$ according to the parity of $e$:
- **Odd $e$:** For $c \in \mathbb{F}_q = \ker(S_2)$, $S_e(c) = e c = c$, so $\ker(S_2) \cap \ker(S_e) = \{0\}$. Since $S_e(S_2(X)) = S_e(X + X^q) = 0$, the linear map $X \mapsto (S_e(X), S_2(X))$ is a bijection $\mathbb{F}_{q^e} \xrightarrow{\sim} \mathbb{F}_q \times H_e$. In particular $S_2$ maps $\{S_e = 1\}$ bijectively onto $H_e = \Omega_e$.
- **Even $e = 2k$:** We have $S_e(X) = \sum_{j=0}^{k-1} S_2(X)^{q^{2j}} = \mathrm{Tr}_{q^e/q^2}(S_2(X))$, and $\ker(S_2) = \mathbb{F}_q \subseteq \ker(S_e)$ (as $S_e(c) = 2kc = 0$ for $c \in \mathbb{F}_q$). Hence $S_2(\{S_e = 1\}) \subseteq D_e$. Comparing cardinalities, $|\{S_e = 1\}| = q^{e-1}$, $|\ker(S_2)| = q$, and $|D_e| = q^{e-2}$, so $S_2$ maps $\{S_e = 1\}$ surjectively and $q$-to-$1$ onto $D_e = \Omega_e$.

Now verify the equivalence:
- If $s(y) = 0$ for some $y = S_2(X_1) \in \Omega_e$ ($S_e(X_1) = 1$), then $g_{n,q}(X_1) \in \ker(S_e) = g_{n,q}(\ker(S_e))$, so $g_{n,q}$ is not injective.
- Assume $s(y) \neq 0$ for all $y \in \Omega_e$. Then $g_{n,q}(\mathbb{F}_{q^e} \setminus \ker(S_e)) \subseteq \mathbb{F}_{q^e} \setminus \ker(S_e)$, and for every $y = S_2(X_1) \in \Omega_e$ ($S_e(X_1) = 1$), $Z_1 := g_{n,q}(X_1)/s(y)$ satisfies $S_e(Z_1) = 1$ and $S_2(Z_1) = \Psi(y) \in \Omega_e$.
- Given any $Z \in \mathbb{F}_{q^e} \setminus \ker(S_e)$, set $c_0 := S_e(Z) \in \mathbb{F}_q^*$ and $z_0 := S_2(Z)/c_0 \in \Omega_e$. Any $X \in \mathbb{F}_{q^e} \setminus \ker(S_e)$ writes uniquely as $X = c X_1$ with $c = S_e(X) \in \mathbb{F}_q^*$ and $S_e(X_1) = 1$, with $y := S_2(X_1) \in \Omega_e$. The equation $g_{n,q}(c X_1) = Z$ is equivalent to $c \cdot (X_1^q + w(y)) = Z$.
  - Taking $S_e$ and $S_2$ shows that $g_{n,q}(cX_1) = Z$ implies $c s(y) = c_0$ and $\Psi(y) = z_0$, and then $X_1 = (Z/c + w(y))^{q^{-1}}$ is uniquely determined by $y$.
  - Conversely, for any $y \in \Omega_e$ with $\Psi(y) = z_0$, put $c := c_0/s(y) \in \mathbb{F}_q^*$ and $X_1 := (Z/c + w(y))^{q^{-1}}$. Applying $S_2$ gives $S_2(X_1)^q = S_2(Z/c) + S_2(w(y)) = (c_0/c) z_0 + S_2(w(y)) = s(y)\Psi(y) + S_2(w(y)) = y^q$, hence $S_2(X_1) = y$. Also $S_e(X_1) = S_e(Z/c + w(y))^{q^{-1}} = (s(y) + (s(y) + 1))^{q^{-1}} = 1$. Therefore $g_{n,q}(c X_1) = c(X_1^q + w(y)) = Z$.

Thus the fiber $\{X \in \mathbb{F}_{q^e} : g_{n,q}(X) = Z\}$ is in bijection with $\{y \in \Omega_e : \Psi(y) = z_0\}$, proving that $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$ if and only if $s$ is nowhere vanishing on $\Omega_e$ and $\Psi : \Omega_e \to \Omega_e$ is bijective. $\square$

---

## 3. Complete Case Analysis

Every pair $(q, e)$ with $q = 2^m > 2$ ($m \ge 2$) and $e \ge 3$ falls into one of six exhaustive cases below.

---

### Case 1: $e = 3$, all even $q > 2$ $\implies$ NEVER a PP

Consider the map $\phi : \mathbb{F}_q \setminus \{0, 1\} \to \mathbb{F}_q^*$ defined by $\phi(t) := t^3 / (t + 1)$. Since $|\mathbb{F}_q \setminus \{0, 1\}| = q - 2 < q - 1 = |\mathbb{F}_q^*|$, by the pigeonhole principle there exists $c \in \mathbb{F}_q^* \setminus \mathrm{Im}(\phi)$.

The cubic polynomial $f(T) := T^3 + c T + c \in \mathbb{F}_q[T]$ has no root in $\mathbb{F}_q$: $f(0) = c \neq 0$, $f(1) = 1 \neq 0$, and for $t \in \mathbb{F}_q \setminus \{0, 1\}$, $f(t) = 0 \iff c = \phi(t)$, which is impossible. Hence $f$ is irreducible over $\mathbb{F}_q$.

Let $y \in \mathbb{F}_{q^3}$ be a root of $f$. Its conjugates over $\mathbb{F}_q$ are $y, y^q, y^{q^2}$, so by Vieta's formulas:
$$S_3(y) = y + y^q + y^{q^2} = 0 \quad (\text{hence } y \in H_3 = \Omega_3), \qquad S_3(y^{q+1}) = y^{q+1} + y^{q^2 + q} + y^{q^2 + 1} = c.$$
Since $y \neq 0$ and $y^3 = c(y + 1)$, we have $y + 1 = y^3 / c$, so $w(y) = y^{q-2}(y + 1) = y^{q+1}/c$ and
$$s(y) = 1 + S_3\bigl(w(y)\bigr) = 1 + c^{-1} S_3(y^{q+1}) = 1 + c^{-1} \cdot c = 0.$$
By Lemma 2.2, $g_{n,q}$ is not a PP of $\mathbb{F}_{q^3}$. $\square$

---

### Case 2: Odd $e \ge 5$, all even $q \ge 4$ $\implies$ NEVER a PP

We prove $\exists y \in H_e = \ker(S_e)$ with $s(y) = 0$ via the Carlitz–Uchiyama bound in characteristic $2$ (Lidl–Niederreiter, Theorem 5.38: for any $f \in \mathbb{F}_{q^e}[y]$ of odd degree $d \ge 1$, $|\sum_{y \in \mathbb{F}_{q^e}} (-1)^{\mathrm{Tr}_{q^e/2}(f(y))}| \le (d - 1) q^{e/2}$, because $f$ cannot be written as $h^2 + h + \beta$ over $\overline{\mathbb{F}}_2$, since $\deg(h^2 + h)$ is even for every nonconstant $h$).

#### Subcase 2a: $q = 4$, odd $e \ge 5$
For $y \in H_e$, $y^{q-2} = y^2$ satisfies $S_e(y^2) = S_e(y)^2 = 0$, so $s(y) = 1 + S_e(y^3)$. Let $N := \#\{y \in \mathbb{F}_{4^e} : S_e(y) = 0,\; S_e(y^3) = 1\}$. By additive character orthogonality on $\mathbb{F}_4$ and transitivity of trace $\mathrm{Tr}_{4/2}(c S_e(z)) = \mathrm{Tr}_{4^e/2}(c z)$,
$$16 N = \sum_{y \in \mathbb{F}_{4^e}} \sum_{a \in \mathbb{F}_4} (-1)^{\mathrm{Tr}_{4^e/2}(a y)} \sum_{b \in \mathbb{F}_4} (-1)^{\mathrm{Tr}_{4/2}(b) + \mathrm{Tr}_{4^e/2}(b y^3)} = 4^e + \sum_{a \in \mathbb{F}_4} \sum_{b \in \mathbb{F}_4^*} (-1)^{\mathrm{Tr}_{4/2}(b)} \sum_{y \in \mathbb{F}_{4^e}} (-1)^{\mathrm{Tr}_{4^e/2}(b y^3 + a y)}$$
(the terms with $b = 0, a \neq 0$ sum to $0$). For each of the $4 \cdot 3 = 12$ pairs $(a, b) \in \mathbb{F}_4 \times \mathbb{F}_4^*$, $\deg(b y^3 + a y) = 3$ is odd, so the inner sum has magnitude at most $(3 - 1) 4^{e/2} = 2 \cdot 4^{e/2}$. Hence, for all $e \ge 5$,
$$16 N \ge 4^e - 24 \cdot 4^{e/2} = 4^{e/2}(4^{e/2} - 24) \ge 32(32 - 24) = 256 > 0.$$
Thus $N > 0$, and $g_{n,4}$ is not a PP of $\mathbb{F}_{4^e}$.

#### Subcase 2b: $q \ge 8$, odd $e \ge 5$
Suppose for contradiction that $s(y) \neq 0$ for all $y \in H_e$. For any $y \in H_e$ and $\lambda \in \mathbb{F}_q^*$, we have $\lambda y \in H_e$ and
$$s(\lambda y) = 1 + S_e\bigl((\lambda y)^{q-1} + (\lambda y)^{q-2}\bigr) = 1 + S_e(y^{q-1}) + \lambda^{-1} S_e(y^{q-2}).$$
Set $F(y) := S_e(y^{q-2})$ and $G(y) := 1 + S_e(y^{q-1})$. If both $F(y) \neq 0$ and $G(y) \neq 0$, then $\lambda := F(y)/G(y) \in \mathbb{F}_q^*$ gives $s(\lambda y) = 0$, a contradiction. Therefore every $y \in H_e$ satisfies $F(y) = 0$ or $G(y) = 0$, so
$$q^{e-1} = |H_e| \le N_F + N_G,$$
where $N_F := \#\{y \in H_e : F(y) = 0\}$ and $N_G := \#\{y \in H_e : G(y) = 0\}$.

- **Bound on $N_F$:** By character orthogonality on $\mathbb{F}_q^2$,
  $$q^2 N_F = q^e + \sum_{a \in \mathbb{F}_q} \sum_{b \in \mathbb{F}_q^*} \sum_{y \in \mathbb{F}_{q^e}} (-1)^{\mathrm{Tr}_{q^e/2}(b y^{q-2} + a y)}.$$
  Since $\mathrm{Tr}_{q^e/2}(z^2) = \mathrm{Tr}_{q^e/2}(z)$ and $b = (b^{q/2})^2$ for $b \in \mathbb{F}_q^*$, we have $\mathrm{Tr}_{q^e/2}(b y^{q-2}) = \mathrm{Tr}_{q^e/2}(b^{q/2} y^{q/2 - 1})$. As $q \ge 8$, $\frac{q}{2} - 1 \ge 3$ is odd and exceeds $1$, so $b^{q/2} y^{q/2 - 1} + a y$ has exact odd degree $\frac{q}{2} - 1$. By Carlitz–Uchiyama,
  $$N_F \le q^{e-2} + \frac{q(q - 1)}{q^2}\left(\frac{q}{2} - 2\right) q^{e/2} = q^{e-2} + \frac{q - 1}{q}\left(\frac{q}{2} - 2\right) q^{e/2}.$$
- **Bound on $N_G$:** Similarly,
  $$q^2 N_G = q^e + \sum_{a \in \mathbb{F}_q} \sum_{b \in \mathbb{F}_q^*} (-1)^{\mathrm{Tr}_{q/2}(b)} \sum_{y \in \mathbb{F}_{q^e}} (-1)^{\mathrm{Tr}_{q^e/2}(b y^{q-1} + a y)}.$$
  Each polynomial $b y^{q-1} + a y$ has exact odd degree $q - 1 \ge 7$, so by Carlitz–Uchiyama,
  $$N_G \le q^{e-2} + \frac{q - 1}{q}(q - 2) q^{e/2}.$$

Summing both bounds and using $\frac{q - 1}{q}(\frac{3q}{2} - 4) < \frac{3}{2} q$ together with $e \ge 5 \implies q^{3 - e/2} \le \sqrt{q}$:
$$N_F + N_G < 2 q^{e-2} + \frac{3}{2} q^{e/2 + 1} = q^{e-2}\left(2 + \frac{3}{2} q^{3 - e/2}\right) \le q^{e-2}\left(2 + \frac{3}{2}\sqrt{q}\right).$$
For every $q \ge 8$, $(q - 2)^2 - \frac{9}{4} q = q^2 - \frac{25}{4} q + 4 = q(q - \frac{25}{4}) + 4 > 0$, so $2 + \frac{3}{2}\sqrt{q} < q$, yielding $N_F + N_G < q^{e-1}$, a contradiction. Hence $g_{n,q}$ is not a PP of $\mathbb{F}_{q^e}$. $\square$

---

### Case 3: Even $e \ge 8$, all even $q \ge 4$ $\implies$ NEVER a PP

We count $N := \#\{y \in \mathbb{F}_{q^e} : \mathrm{Tr}_{q^e/q^2}(y) = 1,\; S_e(y^{q-1} + y^{q-2}) = 1\} = \#\{y \in D_e : s(y) = 0\}$. By additive character orthogonality on $\mathbb{F}_{q^2} \times \mathbb{F}_q$,
$$q^3 N = \sum_{y \in \mathbb{F}_{q^e}} \sum_{a \in \mathbb{F}_{q^2}} (-1)^{\mathrm{Tr}_{q^2/2}(a) + \mathrm{Tr}_{q^e/2}(a y)} \sum_{b \in \mathbb{F}_q} (-1)^{\mathrm{Tr}_{q/2}(b) + \mathrm{Tr}_{q^e/2}(b(y^{q-1} + y^{q-2}))}.$$
The term $(a, b) = (0, 0)$ contributes $q^e$, and the terms with $b = 0, a \in \mathbb{F}_{q^2}^*$ vanish. For every $a \in \mathbb{F}_{q^2}$ and $b \in \mathbb{F}_q^*$, using $\mathrm{Tr}_{q^e/2}(b y^{q-2}) = \mathrm{Tr}_{q^e/2}(b^{q/2} y^{q/2 - 1})$, the inner character sum equals
$$\sum_{y \in \mathbb{F}_{q^e}} (-1)^{\mathrm{Tr}_{q^e/2}\bigl(b y^{q-1} + b^{q/2} y^{q/2 - 1} + a y\bigr)}.$$
Since $q \ge 4$, we have $q - 1 > \max(\frac{q}{2} - 1, 1)$, so $b y^{q-1} + b^{q/2} y^{q/2 - 1} + a y$ has exact odd degree $q - 1 \ge 3$. By the Carlitz–Uchiyama bound, each of the $q^2(q - 1)$ inner sums has magnitude at most $(q - 2) q^{e/2}$. Therefore, since $e \ge 8$ implies $q^{e/2} \ge q^4$,
$$q^3 N \ge q^e - q^2(q - 1)(q - 2) q^{e/2} = q^{e/2}\bigl(q^{e/2} - q^4 + 3 q^3 - 2 q^2\bigr) \ge q^{e/2}\bigl(3 q^3 - 2 q^2\bigr) > 0.$$
Thus $N > 0$, and by Lemma 2.2, $g_{n,q}$ is not a PP of $\mathbb{F}_{q^e}$. $\square$

---

### Case 4: Even $e = 6$, all even $q \ge 4$ $\implies$ NEVER a PP

We prove $\exists y \in D_6 = \{y \in \mathbb{F}_{q^6} : \mathrm{Tr}_{q^6/q^2}(y) = 1\}$ with $s(y) = 0$.

#### Subcase 4a: $2 \le m \le 8$ ($q \in \{4, 8, 16, 32, 64, 128, 256\}$)
For each $m \in \{2, \dots, 8\}$, explicit elements $y \in D_6 \subset \mathbb{F}_{2^{6m}}$ (with Rabin-verified irreducible defining polynomials over $\mathbb{F}_2$) satisfy $s(y) = 0$; lifting $y = S_2(X_1)$ ($S_6(X_1) = 1$) gives explicit colliding pairs $X_1 \neq X_2 \in \mathbb{F}_{q^6}$ with $g_{n,q}(X_1) = g_{n,q}(X_2)$, verified in `verify.py`.

#### Subcase 4b: $m \ge 9$ ($q \ge 512$)
**Step 4.1 ($\mathbb{F}_{q^2} \times \mathbb{F}_{q^3}$ ansatz).**
Let $\mu \in \mathbb{F}_q$ satisfy $\mathrm{Tr}_{q/2}(\mu) = 1$, and pick $\lambda \in \mathbb{F}_{q^2} \setminus \mathbb{F}_q$ with $\lambda^2 + \lambda + \mu = 0$ (so $\lambda + \lambda^q = 1$, $\lambda^{q+1} = \mu$). Let $u \in \mathbb{F}_{q^3}$ be a root of an irreducible cubic $u^3 + a u + b = 0$ over $\mathbb{F}_q$ ($b \neq 0$). Then $S_3(u) = 0$, so $\mathrm{Tr}_{q^6/q^2}(u) = u + u^{q^2} + u^{q^4} = u + u^{q^2} + u^q = 0$, whence
$$y := 1 + \lambda u \in D_6.$$
Note $y \neq 0$ (since $u \notin \mathbb{F}_{q^2}$). Using $u^{q^3} = u$ and $\lambda^{q^2} = \lambda$, we compute $w(y) = (1 + \lambda u)^{q-2} (\lambda u) = \frac{\lambda u (1 + \lambda^q u^q)}{1 + \lambda^2 u^2}$ and pair it with its $q^3$-conjugate $w(y)^{q^3} = \frac{\lambda^q u (1 + \lambda u^q)}{1 + \lambda^{2q} u^2}$:
$$\begin{aligned}
w(y) + w(y)^{q^3} &= \frac{\lambda u(1 + \lambda^q u^q)(1 + \lambda^{2q} u^2) + \lambda^q u(1 + \lambda u^q)(1 + \lambda^2 u^2)}{(1 + \lambda^2 u^2)(1 + \lambda^{2q} u^2)} \\
&= \frac{(\lambda + \lambda^q) u + \lambda^{q+1}(\lambda^q + \lambda) u^3 + \lambda^{q+1}(\lambda^{2q} + \lambda^2) u^{q+3}}{1 + (\lambda + \lambda^q)^2 u^2 + \lambda^{2q+2} u^4}
= \frac{u + \mu u^3 + \mu u^{q+3}}{(1 + u + \mu u^2)^2},
\end{aligned}$$
where the $\lambda^{q+1} u^{q+1}$ terms cancel in characteristic $2$, and $1 + u + \mu u^2 \neq 0$ since $[\mathbb{F}_q(u) : \mathbb{F}_q] = 3$. Consequently,
$$s(y) = 1 + S_6(w(y)) = 1 + S_3\!\left(\frac{u + \mu u^3 + \mu u^{q+3}}{(1 + u + \mu u^2)^2}\right).$$

**Step 4.2 (Reduction to the genus-$0$ curve $S^2 + S = k + 1/k$).**
Let $u_1 = u$, $u_2 = u^q$, $u_3 = u^{q^2}$ be the roots of $u^3 + a u + b = 0$ (so $u_1 + u_2 + u_3 = 0$, $u_1 u_2 + u_1 u_3 + u_2 u_3 = a$, $u_1 u_2 u_3 = b$), put $D_i := 1 + u_i + \mu u_i^2$, and set $P := D_1 D_2 D_3 \in \mathbb{F}_q^*$ (nonzero as $D_i \neq 0$). Writing $P^2 S_3\bigl(\frac{u + \mu u^3 + \mu u^{q+3}}{(1+u+\mu u^2)^2}\bigr) = N_{12} + N_3$ with $N_{12} := \sum_{i=1}^3 (u_i + \mu u_i^3) (D_{i+1} D_{i+2})^2$ and $N_3 := \sum_{i=1}^3 \mu u_i^3 u_{i+1} (D_{i+1} D_{i+2})^2$ (indices mod $3$), direct symmetric-polynomial expansion over $\mathbb{F}_2[a, b, \mu]$ (verified symbolically in `verify.py`) yields:
$$N_3 + N_3' = \sum_{i=1}^3 \mu u_i^4 (D_{i+1} D_{i+2})^2 = b^2 \mu (b \mu^2 + 1)^2,$$
where $N_3'$ reverses the cyclic order ($u_{i+1} \leftrightarrow u_{i-1}$, using $u_{i+1} + u_{i-1} = u_i$). Writing $\delta_u := u_1^2 u_2 + u_2^2 u_3 + u_3^2 u_1$ (which satisfies $\delta_u + \delta_u' = b$), the polynomial $X_{\mathrm{sym}} := N_3 + b \mu (b \mu^2 + 1)^2 \delta_u$ is symmetric in $(u_1, u_2, u_3)$, so $P^2 s(y) = A(a, b, \mu) + b \mu (b \mu^2 + 1)^2 \delta_u$ for an explicit polynomial $A \in \mathbb{F}_2[a, b, \mu]$.

Now specialize $b := \mu^{-2}$ (forcing $b \mu^2 + 1 = 0$, so the $\delta_u$ term vanishes identically!), put $k := \mu + 1 \in \mathbb{F}_q \setminus \{0, 1\}$, and set $a := (S + k) \mu^{-2}$ with $S \in \mathbb{F}_q$. Direct polynomial expansion over $\mathbb{F}_2[S, k]$ (verified in `verify.py`) gives the exact factorization:
$$\mu^5 A\!\left(\frac{S + k}{\mu^2},\; \frac{1}{\mu^2},\; \mu\right) = S^2 \Bigl(k(S^2 + S) + k^2 + 1\Bigr).$$
In particular, whenever $k \in \mathbb{F}_q \setminus \{0, 1\}$ satisfies $\mathrm{Tr}_{q/2}(k + 1) = 1$ and $S \in \mathbb{F}_q$ satisfies $S^2 + S = k + k^{-1}$, we automatically have $S \notin \{0, 1\}$ (since $k + k^{-1} \neq 0$ for $k \neq 1$), $\mu = k + 1 \neq 0$ with $\mathrm{Tr}_{q/2}(\mu) = 1$, and $s(y) = 0$ **provided** the scaled cubic $w^3 + (S + k) w + (k + 1) = 0$ (where $w := \mu u$) is irreducible over $\mathbb{F}_q$!

**Step 4.3 (Exact count of pairs $(k, S)$ via binary Kloosterman sum).**
Let $\mathcal{M}_q := \{(k, S) \in (\mathbb{F}_q \setminus \{0, 1\}) \times \mathbb{F}_q : \mathrm{Tr}_{q/2}(k + 1) = 1,\; S^2 + S = k + k^{-1}\}$ and $M_q := |\mathcal{M}_q|$. Each $k \in \mathbb{F}_q \setminus \{0, 1\}$ with $\mathrm{Tr}_{q/2}(k + 1) = 1$ and $\mathrm{Tr}_{q/2}(k + k^{-1}) = 0$ yields exactly $2$ values $\{S, S + 1\} \subset \mathbb{F}_q \setminus \{0, 1\}$. Expanding the indicator functions gives
$$\begin{aligned}
2 M_q &= \sum_{k \in \mathbb{F}_q \setminus \{0, 1\}} \bigl(1 - (-1)^{\mathrm{Tr}(k + 1)}\bigr)\bigl(1 + (-1)^{\mathrm{Tr}(k + k^{-1})}\bigr) \\
&= (q - 2) + \sum_{k \neq 0, 1} (-1)^{\mathrm{Tr}(k + k^{-1})} - \sum_{k \neq 0, 1} (-1)^{\mathrm{Tr}(k + 1)} - \sum_{k \neq 0, 1} (-1)^{\mathrm{Tr}(1 + k^{-1})}.
\end{aligned}$$
Let $K(1) := \sum_{k \in \mathbb{F}_q^*} (-1)^{\mathrm{Tr}_{q/2}(k + k^{-1})}$ be the binary Kloosterman sum; at $k = 1$, $k + k^{-1} = 0$, so $\sum_{k \neq 0, 1} (-1)^{\mathrm{Tr}(k + k^{-1})} = K(1) - 1$. Also $\sum_{k \neq 0, 1} (-1)^{\mathrm{Tr}(k + 1)} = -1 - (-1)^{\mathrm{Tr}(1)}$ and $\sum_{k \neq 0, 1} (-1)^{\mathrm{Tr}(1 + k^{-1})} = (-1)^{\mathrm{Tr}(1)}(-1 - (-1)^{\mathrm{Tr}(1)}) = -1 - (-1)^{\mathrm{Tr}(1)}$. Hence
$$2 M_q = q - 1 + K(1) + 2 (-1)^{\mathrm{Tr}_{q/2}(1)}.$$
By Weil's Kloosterman bound (Lidl–Niederreiter, Theorem 5.45), $|K(1)| \le 2\sqrt{q}$, so
$$2 M_q \ge q - 2\sqrt{q} - 3.$$

**Step 4.4 (Quadratic resolvent involution and reducible curve $\mathcal{C}_{\mathrm{red}}$).**
For any separable cubic $f(w) = w^3 + X w + \mu \in \mathbb{F}_q[w]$ ($\mu \neq 0$) with roots $w_1, w_2, w_3 \in \overline{\mathbb{F}}_2$, set $\delta := w_1^2 w_2 + w_2^2 w_3 + w_3^2 w_1$ and $\delta' := w_1^2 w_3 + w_3^2 w_2 + w_2^2 w_1$. Since $w_1 + w_2 + w_3 = 0$, $\delta + \delta' = (w_1 + w_2)(w_2 + w_3)(w_3 + w_1) = \mu$ and $\delta \delta' = X^3 + \mu^2$, so $\delta/\mu$ is a root of $T^2 + T + (X^3/\mu^2 + 1) = 0$. The $q$-Frobenius acts as a transposition on $\{w_1, w_2, w_3\}$ (i.e., $f$ has exactly $1$ root in $\mathbb{F}_q$) if and only if $\delta \notin \mathbb{F}_q$, i.e., $\mathrm{Tr}_{q/2}(X^3/\mu^2 + 1) = 1$; otherwise $f$ has either $0$ or $3$ distinct roots in $\mathbb{F}_q$ (no double root can occur since $f'(w) = w^2 + X$ and $f(\sqrt{X}) = \mu \neq 0$).

For $(k, S) \in \mathcal{M}_q$, set $X := S + k$ and $\mu := k + 1$. Reducing $S^2 = S + k + k^{-1}$ gives
$$\frac{(S + k)^3}{(k + 1)^2} = \frac{S(k^3 + k + 1) + (k^4 + k^3 + k^2 + k + 1)}{k(k + 1)^2}.$$
Under the fixed-point-free involution $(k, S) \mapsto (k, S + 1)$ on $\mathcal{M}_q$, this quantity shifts by
$$\frac{k^3 + k + 1}{k(k + 1)^2} = 1 + \frac{1}{k(k + 1)^2} = 1 + \frac{1}{k} + \frac{1}{k + 1} + \frac{1}{(k + 1)^2}.$$
Taking $\mathrm{Tr}_{q/2}$ cancels $\frac{1}{k+1} + \frac{1}{(k+1)^2}$, while $\mathrm{Tr}_{q/2}(k^{-1}) = \mathrm{Tr}_{q/2}(k)$ (as $k + k^{-1} = S^2 + S$), so the trace shifts by $\mathrm{Tr}_{q/2}(1 + k) = \mathrm{Tr}_{q/2}(\mu) = 1$. Therefore, letting $N_j$ ($j \in \{0, 1, 3\}$) denote the number of $(k, S) \in \mathcal{M}_q$ for which $w^3 + (S + k) w + (k + 1)$ has exactly $j$ roots in $\mathbb{F}_q$, we have
$$N_1 = \frac{M_q}{2}, \qquad N_0 + N_3 = \frac{M_q}{2}.$$

Now a root $w \in \mathbb{F}_q$ of $w^3 + (S + k) w + (k + 1) = 0$ satisfies $w \neq 0$ (since $k \neq 1$) and determines $S = w^2 + k + (k + 1)/w$. Substituting this into $S^2 + S = k + k^{-1}$ and clearing denominators $k w^2$ gives the plane curve $\mathcal{C}_{\mathrm{red}} \subset \mathbb{A}^2$:
$$F_{\mathrm{red}}(k, w) := (w + 1)^2 k^3 + w k^2 + (w + 1)(w^2 + w + 1)(w^3 + w + 1) k + w^2 = 0.$$
Conversely, every $(w, k) \in \mathcal{C}_{\mathrm{red}}(\mathbb{F}_q)$ with $w \neq 0$, $k \notin \{0, 1\}$, and $\mathrm{Tr}_{q/2}(k + 1) = 1$ yields $(k, S) \in \mathcal{M}_q$ with $S = w^2 + k + (k + 1)/w$ and a root $w$ of $w^3 + (S + k) w + (k + 1) = 0$. Setting $R_q := \#\{(w, k) \in \mathcal{C}_{\mathrm{red}}(\mathbb{F}_q) : w \neq 0,\; k \notin \{0, 1\},\; \mathrm{Tr}_{q/2}(k + 1) = 1\}$, we obtain $R_q = N_1 + 3 N_3$, and eliminating $N_1$ and $N_3$ yields the exact identity
$$3 N_0 = 3\left(\frac{M_q}{2} - N_3\right) = \frac{3 M_q}{2} - \left(R_q - \frac{M_q}{2}\right) = 2 M_q - R_q.$$

**Step 4.5 (Absolute irreducibility, genus $9$, and Hasse–Weil bound).**
1. **$\mathcal{C}_{\mathrm{red}}$ is absolutely irreducible over $\overline{\mathbb{F}}_2$:** As a degree-$3$ polynomial in $k$ over $\overline{\mathbb{F}}_2(w)$, $F_{\mathrm{red}}$ is reducible if and only if it has a root $k(w) \in \overline{\mathbb{F}}_2(w)$. Since the leading coefficient in $k$ is $(w + 1)^2$, any rational root has the form $k(w) = P(w)/(w + 1)^r$ with $P \in \overline{\mathbb{F}}_2[w]$ and $r \in \{0, 1, 2\}$. Setting $s := w^{-1}$, $s^6 F_{\mathrm{red}}(k, s^{-1}) = (s^6 + s^4) k^3 + s^5 k^2 + (s^6 + s^5 + s^2 + 1) k + s^4$ has Newton polygon at $s = 0$ with vertices $(0, 4), (1, 0), (3, 4)$, so $v_\infty(k) = r - \deg P \in \{4, -2\}$. The case $v_\infty(k) = 4$ is impossible since $r \le 2$; thus $\deg P = r + 2 \in \{2, 3, 4\}$. For each $r \in \{0, 1, 2\}$, substituting $P(w) = \sum_{j=0}^{r+2} a_j w^j$ yields a polynomial system over $\mathbb{F}_2[a_0, \dots, a_{r+2}]$ whose Gröbner basis is $\{1\}$ (verified in `verify.py`), ruling out any root in $\overline{\mathbb{F}}_2(w)$.
2. **Exact geometric genus $g(\mathcal{C}_{\mathrm{red}}) = 5$:** Consider the degree-$3$ separable cover $\pi_w : \mathcal{C}_{\mathrm{red}}^{\mathrm{sm}} \to \mathbb{P}^1_w$ from the smooth projective model of $\mathcal{C}_{\mathrm{red}}$. We have $\partial F_{\mathrm{red}}/\partial w = k(k + 1)$, so every affine point with $k \notin \{0, 1\}$ is smooth, and $\mathrm{Res}_k(F_{\mathrm{red}}, \partial F_{\mathrm{red}}/\partial k) = w^2 (w + 1)^4 (w^5 + w^4 + w^2 + w + 1)^2$. Checking each candidate branch locus:
   - $w = 0$: $F_{\mathrm{red}}(k, 0) = k(k + 1)^2$. The point $(0, 0)$ is smooth ($\partial F/\partial k = 1$, $e = 1$). At $(1, 0)$, blowing up $k = 1 + w t_1$ gives $t_1^2 + t_1 + w(\cdots) = 0$, which splits into two smooth branches ($t_1 = 0, 1$), each with $e = 1$. Thus $w = 0$ is unramified.
   - $w = 1$ ($u = w + 1$): $F_{\mathrm{red}}(k, 1 + u) = u^2 k^3 + (u + 1) k^2 + u(u^5 + u + 1) k + (u^2 + 1)$ has one smooth pole $P_1$ with $k = u^{-2} + u^{-1} + u + u^2 + O(u^3)$ ($e = 1$), and at $(1, 1)$ blowing up $k = 1 + u t_1$ gives $t_1^2 + t_1 + 1 + u(\cdots) = 0$, splitting into two conjugate smooth branches over $\mathbb{F}_4$, each with $e = 1$. Thus $w = 1$ is unramified.
   - Roots $\alpha$ of $w^5 + w^4 + w^2 + w + 1 = 0$: at each of the $5$ roots $\alpha \in \mathbb{F}_{32}$, $F_{\mathrm{red}}(k, \alpha)$ has a repeated root $k_0$ solving $\partial F_{\mathrm{red}}/\partial k(k_0, \alpha) = (\alpha + 1)^2 k_0^2 + (\alpha^6 + \alpha^4 + \alpha + 1) = 0$ (note $k_0 \notin \{0, 1\}$, since $F_{\mathrm{red}}(0, \alpha) = \alpha^2 \neq 0$ and $F_{\mathrm{red}}(1, \alpha) = \alpha^4(\alpha + 1)^2 \neq 0$). Since $\partial F_{\mathrm{red}}/\partial w(k_0, \alpha) = k_0(k_0 + 1) \neq 0$, $(k_0, \alpha)$ is smooth. Expanding $F_{\mathrm{red}}(k_0 + t, \alpha + u) = 0$ in characteristic $2$ modulo $(u^2, u t^2)$ (keeping $(k_0 + t)^3 = k_0^3 + k_0^2 t + k_0 t^2 + t^3$ and the cross-term $\partial^2 F_{\mathrm{red}}/\partial k\partial w = 1$) gives
     $$k_0(k_0 + 1) u + t u + \bigl((\alpha + 1)^2 k_0 + \alpha\bigr) t^2 + (\alpha + 1)^2 t^3 \equiv 0 \pmod{u^2, u t^2}.$$
     Thus $u = c_2 t^2 + c_3 t^3 + O(t^4)$ where:
     - $c_2 = \dfrac{(\alpha + 1)^2 k_0 + \alpha}{k_0(k_0 + 1)} \neq 0$ (indeed, $(\alpha + 1)^2 k_0 = \alpha$ would square to $(\alpha + 1)^4 k_0^2 = \alpha^2$, and substituting $(\alpha + 1)^2 k_0^2 = \alpha^6 + \alpha^4 + \alpha + 1$ yields $(\alpha + 1)^2(\alpha^6 + \alpha^4 + \alpha + 1) + \alpha^2 = \alpha^8 + \alpha^4 + \alpha^3 + \alpha + 1 \equiv \alpha^4 + 1 \neq 0 \pmod{\alpha^5 + \alpha^4 + \alpha^2 + \alpha + 1}$), confirming $k_0$ is a double root ($e = 2$, not triple); and
     - $c_3 = \dfrac{(\alpha + 1)^2 + c_2}{k_0(k_0 + 1)} = \dfrac{(\alpha + 1)^2 k_0^2 + \alpha}{k_0^2(k_0 + 1)^2} = \dfrac{\alpha^6 + \alpha^4 + 1}{k_0^2(k_0 + 1)^2} = \dfrac{(\alpha^3 + \alpha^2 + 1)^2}{k_0^2(k_0 + 1)^2} \neq 0$,
       since $w^5 + w^4 + w^2 + w + 1$ is irreducible of degree $5 > 3$ over $\mathbb{F}_2$ (verified in $\mathbb{F}_{32}$ in `verify.py`).
     Hence $du/dt = c_3 t^2 + O(t^3)$ has $v_P(dw/dt) = 2$ at all $5$ places (total contribution $5 \cdot 2 = 10$).
   - $w = \infty$ ($s = w^{-1}$): one smooth branch $k = s^4 + \cdots$ ($e = 1$) and one ramified place $P_\infty$ ($e = 2$) where $K := s^2 k = 1 + \pi s$ with uniformizer $\pi$. Substituting $K = 1 + \pi s$ into $s^8 F_{\mathrm{red}}(K/s^2, s^{-1})/s^2 = 0$ yields $s(\pi) = \pi^2 + \pi^5 + \pi^9 + O(\pi^{10})$ (verified in `verify.py`), whence $ds/d\pi = \pi^4 + \pi^8 + O(\pi^9)$ and $v_{P_\infty}(ds/d\pi) = 4$.

   By Riemann–Hurwitz, $2 g(\mathcal{C}_{\mathrm{red}}) - 2 = 3(-2) + 10 + 4 = 8$, so $g(\mathcal{C}_{\mathrm{red}}) = 5$.
3. **Artin–Schreier twist $\widetilde{\mathcal{C}}_{\mathrm{red}, 1}$ is absolutely irreducible of genus $9$:** Fix $\delta \in \mathbb{F}_q$ with $\mathrm{Tr}_{q/2}(\delta) = 1$, and consider the degree-$2$ Artin–Schreier cover $\widetilde{\mathcal{C}}_{\mathrm{red}, 1} : t^2 + t = k + 1 + \delta$ over $\mathcal{C}_{\mathrm{red}}^{\mathrm{sm}}$.
   - **Absolute irreducibility:** Over $\overline{\mathbb{F}}_2$, $\widetilde{\mathcal{C}}_{\mathrm{red}, 1}$ is isomorphic to $\widetilde{\mathcal{C}}_{\mathrm{red}, 0} : t^2 + t = k + 1$. If $t^2 + t = k + 1$ factored over $\overline{\mathbb{F}}_2(\mathcal{C}_{\mathrm{red}})$, then $k + 1 = h^2 + h$ for some $h \in \overline{\mathbb{F}}_2(\mathcal{C}_{\mathrm{red}})$. Applying the $\mathbb{F}_2$-Frobenius $\sigma$ gives $(h^\sigma + h)^2 + (h^\sigma + h) = 0$, so $h^\sigma + h \in \{0, 1\}$. If $h^\sigma = h$, then $h \in \mathbb{F}_2(\mathcal{C}_{\mathrm{red}})$ is regular at the smooth $\mathbb{F}_2$-point $(k, w) = (0, 0)$ (since $k + 1$ is regular there), giving $1 = h(0, 0)^2 + h(0, 0) = 0$, contradiction. If $h^\sigma = h + 1$, pick $\omega \in \mathbb{F}_4 \setminus \mathbb{F}_2$; then $h_0 := h + \omega \in \mathbb{F}_2(\mathcal{C}_{\mathrm{red}})$ satisfies $k + 1 = h_0^2 + h_0 + 1$, and evaluating at either smooth $\mathbb{F}_2$-branch of $(k, w) = (1, 0)$ gives $0 = h_0(P)^2 + h_0(P) + 1 = 1$, contradiction.
   - **Unramifiedness and genus $9$:** The only poles of $k + 1 + \delta$ on $\mathcal{C}_{\mathrm{red}}^{\mathrm{sm}}$ are $P_1$ and $P_\infty$. At $P_1$, $k + 1 + \delta = (u^{-1})^2 + u^{-1} + (1 + \delta) + O(u)$. At $P_\infty$, $k = (1 + \pi s)/s^2 = \pi^{-4} + \pi^{-1} + O(\pi)$ (verified in `verify.py`), so $k + 1 + \delta = (\pi^{-2} + \pi^{-1})^2 + (\pi^{-2} + \pi^{-1}) + (1 + \delta) + O(\pi)$. Both Artin–Schreier principal parts vanish after reduction, so $\widetilde{\mathcal{C}}_{\mathrm{red}, 1} \to \mathcal{C}_{\mathrm{red}}^{\mathrm{sm}}$ is unramified everywhere! By Riemann–Hurwitz, $2 g(\widetilde{\mathcal{C}}_{\mathrm{red}, 1}) - 2 = 2(2 \cdot 5 - 2) = 16$, so $g(\widetilde{\mathcal{C}}_{\mathrm{red}, 1}) = 9$.
4. **Conclusion for $q \ge 512$:** Every $(w, k)$ counted by $R_q$ has $k \notin \{0, 1\}$, hence is a smooth point of $\mathcal{C}_{\mathrm{red}}$ with $\mathrm{Tr}_{q/2}(k + 1 + \delta) = 0$, and therefore lifts to $2$ distinct $\mathbb{F}_q$-rational points of $\widetilde{\mathcal{C}}_{\mathrm{red}, 1}$. By the Hasse–Weil bound on the smooth projective absolutely irreducible genus-$9$ curve $\widetilde{\mathcal{C}}_{\mathrm{red}, 1}$,
   $$2 R_q \le \#\widetilde{\mathcal{C}}_{\mathrm{red}, 1}(\mathbb{F}_q) \le q + 1 + 18\sqrt{q} \implies R_q \le \frac{q + 1}{2} + 9\sqrt{q}.$$
   Combining with $2 M_q \ge q - 2\sqrt{q} - 3$ gives
   $$3 N_0 = 2 M_q - R_q \ge (q - 2\sqrt{q} - 3) - \left(\frac{q + 1}{2} + 9\sqrt{q}\right) = \frac{q - 7}{2} - 11\sqrt{q}.$$
   For all $q \ge 512$ ($m \ge 9$), $(q - 7)^2 - (22)^2 q = q^2 - 498 q + 49 = q(q - 498) + 49 > 0$, so $N_0 > 0$. Hence $s(y) = 0$ has a solution $y \in D_6$, and $g_{n,q}$ is not a PP of $\mathbb{F}_{q^6}$. $\square$

---

### Case 5: $(q, e) = (4, 4)$ $\implies$ ALWAYS a PP

Let $\mathbb{F}_{16} = \mathbb{F}_2[\alpha]/(\alpha^4 + \alpha + 1)$ with $\mathbb{F}_4 = \{0, 1, \omega, \omega^2\}$ ($\omega = \alpha^5$, $\omega^2 = \alpha^{10}$). For $y \in D_4 = \{y \in \mathbb{F}_{256} : y^{16} = y + 1\}$, put $z := y^2 + y \in \mathbb{F}_{16}$ and $u := y + y^4 = z + z^2 \in \mathbb{F}_{16}$. Then $\mathrm{Tr}_{16/2}(z) = y^{16} + y = 1$, $u + u^4 = 1$, $c := u + u^2 = z + z^4 \in \mathbb{F}_4^*$, and $r := z + c u \in \mathbb{F}_4$.

Using $y^4 = y + u$ and $y^2 = y + z$ ($1/y = (y + 1)/z$, $1/y^2 = (y + z + 1)/z^2$, and similarly for $y + u$ with $z^4 = z + c$), direct algebra over $\mathbb{F}_{256}$ (and identically for any even $q \ge 4$ with $u := y + y^q$ and $z^q = z + c$) gives:
- $N := z^5 = r^2 + c r + c^3 \in \mathbb{F}_4^*$,
- $s(y) = \dfrac{D(c, r)}{N^2}$ where $D(c, r) := N^2 + (r + c + 1) N + c r$,
- $\Psi(y) = y + \Delta(u, c, r)$ where $\Delta(u, c, r) := \dfrac{A_0(c, r) + A_1(c, r) u}{D(c, r)} \in \mathbb{F}_{16}$, with $\mathrm{Num}(c, r) := c^2 N + r^2$, $A_1 := D + \mathrm{Num}$, and $A_0 := (c^2 + c r + 1) N + c(c + 1) r$.

In particular, $\Psi(y + 1) = \Psi(y) + 1$, so $\Psi$ is a bijection on $D_4$ if and only if $s(y) \neq 0$ and the induced map $z \mapsto z_\Psi := \Psi(y)^2 + \Psi(y) = z + \Delta^2 + \Delta$ is a bijection on $Z := \{z \in \mathbb{F}_{16} : \mathrm{Tr}_{16/2}(z) = 1\}$.

At $q = 4$, $Z$ has size $8$ and partitions into **two** $\mathbb{F}_2$-Frobenius orbits of size $4$:
1. $O_1 = \{\alpha^7, \alpha^{14}, \alpha^{13}, \alpha^{11}\}$ (roots of $T^4 + T^3 + 1$). At $z = \alpha^7$: $u = \alpha$, $c = \alpha^5 = \omega$, $r = \alpha^{10} = \omega^2$, $s = \alpha^{10} = \omega^2 \neq 0$, and $z_\Psi = \alpha^{11} \in O_1$.
2. $O_2 = \{\alpha^3, \alpha^6, \alpha^{12}, \alpha^9\}$ (roots of $T^4 + T^3 + T^2 + T + 1$). At $z = \alpha^3$: $u = \alpha^2$, $c = \alpha^{10} = \omega^2$, $r = \alpha^{10} = \omega^2$, $s = \alpha^5 = \omega \neq 0$, and $z_\Psi = \alpha^{12} \in O_2$.

Because $s$ and $z \mapsto z_\Psi$ have $\mathbb{F}_2$-coefficients, they commute with $2$-Frobenius $z \mapsto z^2$. Thus $s(y) \neq 0$ on all of $D_4$, and $z \mapsto z_\Psi$ acts as $z \mapsto z^8$ on $O_1$ and $z \mapsto z^4$ on $O_2$, both of which are bijections. Therefore $\Psi : D_4 \to D_4$ is bijective, and by Lemma 2.2, $g_{4387, 4}$ is a PP of $\mathbb{F}_{256}$ (also exhaustively verified over all $256$ elements of $\mathbb{F}_{256}$ in `verify.py`). $\square$

---

### Case 6: Even $e = 4$, all even $q = 2^m \ge 8$ ($m \ge 3$) $\implies$ NEVER a PP

#### Subcase 6a: $3 \le m \le 37$ ($8 \le q \le 2^{37}$)
For every $m \in \{3, 4, \dots, 37\}$, we exhibit an explicit irreducible defining polynomial of degree $4m$ over $\mathbb{F}_2$ (Rabin-verified) and an explicit pair of distinct elements $X_1 \neq X_2 \in \mathbb{F}_{q^4}$ (lifted from colliding unit-circle witnesses $x_1 \neq x_2 \in \mu_{q^2 + 1} \setminus \{1\}$) satisfying $g_{n,q}(X_1) = g_{n,q}(X_2)$, verified directly in `verify.py`.

#### Subcase 6b: $m \ge 38$ ($q \ge 2^{38}$)
Suppose for contradiction that $g_{n,q}$ is a PP of $\mathbb{F}_{q^4}$. By Lemma 2.2, $s(y) \neq 0$ for all $y \in D_4$ and $\Psi : D_4 \to D_4$ is a bijection.

**Step 6.1 (Explicit $\mathbb{F}_q$-plane coordinates and unit-circle conjugation).**
Fix $\delta \in \mathbb{F}_q$ with $\mathrm{Tr}_{q/2}(\delta) = 1$, let $\gamma \in \mathbb{F}_{q^2} \setminus \mathbb{F}_q$ satisfy $\gamma^2 + \gamma = \delta$ (so $\gamma^q = \gamma + 1$), and pick $\theta_0 \in D_4$ with $\theta_0^q + \theta_0 = \gamma$ (which exists because $y \mapsto y + y^q$ maps $D_4$ surjectively onto $\{u \in \mathbb{F}_{q^2} : u + u^q = 1\}$). Every $y \in D_4$ writes uniquely as
$$y = \theta_0 + a + b \gamma, \qquad (a, b) \in \mathbb{F}_q^2.$$
In these coordinates, $y^q = \theta_0 + a + b + (b + 1)\gamma$ and $(Y_0, Y_1) := (y, y^q)$ is an invertible $\mathbb{F}_{q^4}$-affine-linear function of $(a, b)$. Since $y^{q^2} = y + 1$ and $y^{q^3} = y^q + 1$, the four $q$-conjugates of $w(y) = y^{q-2}(y+1) = \frac{y^q(y+1)}{y^2}$ are rational functions of $(Y_0, Y_1)$ over $\mathbb{F}_2$:
$$w = \frac{Y_1(Y_0 + 1)}{Y_0^2}, \quad w^q = \frac{(Y_0 + 1)(Y_1 + 1)}{Y_1^2}, \quad w^{q^2} = \frac{(Y_1 + 1) Y_0}{(Y_0 + 1)^2}, \quad w^{q^3} = \frac{Y_0 Y_1}{(Y_1 + 1)^2}.$$
Hence $(\Psi(y), \Psi(y)^q) = (\Psi_0(Y_0, Y_1), \Psi_1(Y_0, Y_1))$ where $\Psi_0 := (Y_1 + w + w^q)/s$, $\Psi_1 := (Y_0 + 1 + w^q + w^{q^2})/s$, and $s := 1 + w + w^q + w^{q^2} + w^{q^3}$. Clearing denominators in $\mathbb{F}_2[Y_0, Y_1]$ and dividing out common factors (verified symbolically in `verify.py`) yields
$$\Psi_0(Y_0, Y_1) = \frac{P_0(Y_0, Y_1)}{Q_0(Y_0, Y_1)}, \qquad \Psi_1(Y_0, Y_1) = \frac{P_1(Y_0, Y_1)}{Q_0(Y_0, Y_1)},$$
with $\gcd(P_0, Q_0) = \gcd(P_1, Q_0) = 1$, $\deg(P_0) = \deg(P_1) = 9$, and $\deg(Q_0) = 8$.

Passing back via the invertible affine-linear isomorphism $(a, b) \leftrightarrow (Y_0, Y_1)$ gives an $\mathbb{F}_q$-rational map
$$\Phi_2 : \mathbb{A}^2 \dashrightarrow \mathbb{A}^2, \qquad \Phi_2(a, b) = \left(\frac{\widetilde{P}_a(a, b)}{\widetilde{Q}(a, b)},\; \frac{\widetilde{P}_b(a, b)}{\widetilde{Q}(a, b)}\right),$$
defined over $\mathbb{F}_q$, with $\deg(\widetilde{P}_a), \deg(\widetilde{P}_b) \le 9$, $\deg(\widetilde{Q}) = 8$, and $\widetilde{Q}(a, b) \neq 0$ for all $(a, b) \in \mathbb{F}_q^2$ (since $s(y) \neq 0$ on $D_4$). By hypothesis, $\Phi_2 : \mathbb{F}_q^2 \to \mathbb{F}_q^2$ is a bijection.

Over $\overline{\mathbb{F}}_2$, applying the Möbius birational involution $X_0 := \frac{Y_0}{Y_0 + 1}$, $X_1 := \frac{Y_1}{Y_1 + 1}$ conjugates $(Y_0, Y_1) \mapsto (\Psi_0, \Psi_1)$ to the fixed $\mathbb{F}_2$-rational map $G : \mathbb{A}^2 \dashrightarrow \mathbb{A}^2$, $G(X_0, X_1) = (G_0(X_0, X_1), G_1(X_0, X_1))$, where
$$G_0(X_0, X_1) = \frac{\Phi_0}{\Phi_0^{q^2}} = \frac{X_1^3(X_0^3 + 1) + X_0^2(X_1^2 + 1)}{X_0^2 X_1^2\bigl(X_0^3 + 1 + X_0 X_1(X_1^2 + 1)\bigr)}, \qquad G_1(X_0, X_1) = G_0(X_1, X_0^{-1}) = \frac{X_0^2 X_1^3 + (X_0^5 + X_0^3) X_1^2 + X_0^2}{X_0^3 X_1^5 + (X_0^2 + 1) X_1^3 + X_0^3 X_1^2}.$$
*(Indeed, on $D_4$, $X_0 = \frac{y}{y+1} \in \mu_{q^2+1} \setminus \{1\}$ and $X_1 = X_0^q$; substituting $y = \frac{X_0}{X_0+1}$ gives $\Phi(y) = y^q + w + w^q = \frac{X_1^3(X_0^3+1) + X_0^2(X_1^2+1)}{X_0^2 X_1^2(X_0+1)(X_1+1)}$, and $\frac{\Psi(y)}{\Psi(y)+1} = \frac{\Phi(y)}{\Phi(y) + s(y)} = \frac{\Phi(y)}{\Phi(y)^{q^2}} = G_0(X_0, X_1)$.)*

**Step 6.2 (Exact generic degree $25$ and geometric monodromy $G_{\mathrm{geom}} \supseteq A_{25}$).**
Consider the system $G_0(X_0, X_1) = A$, $G_1(X_0, X_1) = B$ over $\mathbb{F}_2(A, B)$, cleared of denominators as:
$$f_0(X_1) := A X_0^3 X_1^5 + (A X_0^3 + X_0^3 + 1) X_1^3 + \bigl(A(X_0^5 + X_0^2) + X_0^2\bigr) X_1^2 + X_0^2 = 0,$$
$$f_1(X_1) := B X_0^3 X_1^5 + \bigl(B(X_0^2 + 1) + X_0^2\bigr) X_1^3 + (B X_0^3 + X_0^5 + X_0^3) X_1^2 + X_0^2 = 0.$$
Eliminating $X_1^5$ and $X_1^0$ produces two cubics in $X_1$: $c_1 := B f_0 + A f_1$ and $c_2 := (f_0 + f_1)/X_1^2$. Computing the exact $6 \times 6$ Sylvester resultant $\mathrm{Res}_{X_1}(c_1, c_2) \in \mathbb{F}_2[A, B, X_0]$ and removing the trivial factor $X_0^2 (X_0 + 1)(A + B)$ (verified symbolically in `verify.py`) yields an explicit polynomial $P_{\mathrm{gen}}(A, B; X_0) \in \mathbb{F}_2[A, B][X_0]$ of exact degree $25$ in $X_0$, with leading coefficient
$$\mathrm{LC}_{X_0}\bigl(P_{\mathrm{gen}}\bigr) = A^3 (A + 1)^2 (B + 1)^3.$$

Work over $\mathbb{F}_{64} := \mathbb{F}_2[\beta]/(\beta^6 + \beta + 1)$ and inspect two specializations (both verified directly in `verify.py`):
1. **$(A_1, B_1) = (\beta,\; \beta^5 + \beta^3)$:** Here $A_1, B_1 \notin \{0, 1\}$, $A_1 \neq B_1$, so $\mathrm{LC}(A_1, B_1) \neq 0$. The specialized polynomial $P_0(X_0) := P_{\mathrm{gen}}(A_1, B_1; X_0) \in \mathbb{F}_{64}[X_0]$ is **irreducible and separable of degree $25$** over $\mathbb{F}_{64}$. Moreover, over the field $K := \mathbb{F}_{64}[X_0]/(P_0)$, $\gcd_{K[X_1]}(f_0, f_1)$ has **exact degree $1$** in $X_1$, yielding a unique $X_1 \in K \setminus \{0, 1\}$ with nonzero denominators $G_0^{\mathrm{den}}(X_0, X_1), G_1^{\mathrm{den}}(X_0, X_1)$ and $G(X_0, X_1) = (A_1, B_1)$.
2. **$(A_2, B_2) = (\beta + 1,\; \beta^2 + \beta + 1)$:** Here $\mathrm{LC}(A_2, B_2) \neq 0$, and $P_1(X_0) := P_{\mathrm{gen}}(A_2, B_2; X_0) \in \mathbb{F}_{64}[X_0]$ is **squarefree of degree $25$**, factoring over $\mathbb{F}_{64}$ as the product of one irreducible polynomial of degree $2$ and one irreducible polynomial of degree $23$.

From these two specializations we deduce three immediate consequences:
- **Exact field degree $25$:** Since $P_0$ is irreducible of degree $25$, $P_{\mathrm{gen}}(A, B; X_0)$ is irreducible and separable of degree $25$ over $\mathbb{F}_{64}(A, B)$. Let $L := \mathbb{F}_2(A, B)[X_0]/(P_{\mathrm{gen}})$. Because $P_{\mathrm{gen}} \mid \mathrm{Res}_{X_1}(c_1, c_2)$ and $X_1 = 0$ is not a root of $f_0$ ($f_0(0) = X_0^2 \neq 0$), $f_0$ and $f_1$ share a root over $\overline{L}$, so $\deg_{X_1}\gcd_{L[X_1]}(f_0, f_1) \ge 1$. On the other hand, by subresultant semicontinuity under specialization $(A, B) \mapsto (A_1, B_1)$, $\deg_{X_1}\gcd_{L[X_1]}(f_0, f_1) \le \deg_{X_1}\gcd_{K[X_1]}(f_0, f_1) = 1$. Hence $\deg_{X_1}\gcd_{L[X_1]}(f_0, f_1) = 1$, so $X_1 \in L$ and $[\mathbb{F}_2(X_0, X_1) : \mathbb{F}_2(A, B)] = 25$ is separable.
- **Arithmetic Galois group $H = S_{25}$:** Restrict $P_{\mathrm{gen}}$ to the line $(A(t), B(t)) := (A_1 + t(A_2 + A_1),\; B_1 + t(B_2 + B_1))$ over the PID $\mathbb{F}_{64}[t]$, giving $P_t(X_0) \in \mathbb{F}_{64}[t][X_0]$. Since $P_0$ is irreducible of degree $25$, $P_t$ is irreducible and separable of degree $25$ over $\mathbb{F}_{64}(t)$, and the primes $(t)$ and $(t + 1)$ of $\mathbb{F}_{64}[t]$ do not divide $\mathrm{LC}(P_t) \cdot \mathrm{disc}_{X_0}(P_t)$. By Dedekind's theorem over the PID $\mathbb{F}_{64}[t]$, $H_t := \mathrm{Gal}(P_t / \mathbb{F}_{64}(t)) \le S_{25}$ contains a $25$-cycle (at $t = 0$) and an element $\sigma$ of cycle type $(2, 23)$ (at $t = 1$). Then $H_t$ is transitive (via the $25$-cycle), primitive (since $\sigma^2$ is a $23$-cycle and $23 > 5$ cannot preserve any system of $5$ blocks of size $5$), and contains the transposition $\sigma^{23}$. In any primitive group $H_t \le S_{25}$, the subgroup generated by all transpositions in $H_t$ is normal and nontrivial, hence transitive, and a transitive subgroup generated by transpositions is the entire symmetric group (Jordan's theorem); thus $H_t = S_{25}$. Since $P_t$ is the unramified specialization of $P_{\mathrm{gen}}$ at the height-$1$ prime $\mathfrak{p} = \bigl((A_2 + A_1)(B + B_1) + (B_2 + B_1)(A + A_1)\bigr)$ of the UFD $\mathbb{F}_{64}[A, B]$ (whose localization is a DVR with residue field $\mathbb{F}_{64}(t)$), $H_t$ embeds into $H := \mathrm{Gal}(P_{\mathrm{gen}} / \mathbb{F}_{64}(A, B)) \le S_{25}$, forcing $H = S_{25}$.
- **Geometric monodromy $G_{\mathrm{geom}} \supseteq A_{25}$:** The geometric Galois group $G_{\mathrm{geom}} := \mathrm{Gal}(P_{\mathrm{gen}} / \overline{\mathbb{F}}_2(A, B))$ is a normal subgroup of $H = S_{25}$ with cyclic quotient $H / G_{\mathrm{geom}}$ (a quotient of $\mathrm{Gal}(\overline{\mathbb{F}}_2/\mathbb{F}_{64}) \cong \widehat{\mathbb{Z}}$). The only normal subgroups of $S_{25}$ are $\{1\}, A_{25}, S_{25}$, and $S_{25}$ is non-cyclic; hence $G_{\mathrm{geom}} \supseteq A_{25}$.

**Step 6.3 (Absolute irreducibility and degree bound for the collision surface $W_0 \subset \mathbb{A}^4$).**
In $\mathbb{A}^4_{\mathbb{F}_q}$ with coordinates $(a_1, b_1, a_2, b_2)$, define the two $\mathbb{F}_q$-hypersurfaces of degree at most $17$:
$$H_a : \widetilde{P}_a(a_1, b_1) \widetilde{Q}(a_2, b_2) + \widetilde{P}_a(a_2, b_2) \widetilde{Q}(a_1, b_1) = 0, \qquad H_b : \widetilde{P}_b(a_1, b_1) \widetilde{Q}(a_2, b_2) + \widetilde{P}_b(a_2, b_2) \widetilde{Q}(a_1, b_1) = 0.$$
Check $\gcd(H_a, H_b) = 1$: any $3$-dimensional common component $Z \subseteq H_a \cap H_b$ cannot lie in $\{\widetilde{Q}_1 = 0\}$ (which would force $\widetilde{Q}_2 = 0$ or $\widetilde{P}_a(a_1, b_1) = \widetilde{P}_b(a_1, b_1) = 0$; the former has dimension $\le 2$, and the latter has dimension $\le 2$ in $\mathbb{A}^4$ because invertibility of $(a, b) \leftrightarrow (Y_0, Y_1)$ gives $\gcd(\widetilde{P}_a, \widetilde{P}_b, \widetilde{Q}) = \gcd(P_0, P_1, Q_0) = 1$, forcing $\dim\{\widetilde{Q}_1 = \widetilde{P}_a(a_1, b_1) = \widetilde{P}_b(a_1, b_1) = 0\} \le 0$ in $\mathbb{A}^2$), nor in $\{\widetilde{Q}_2 = 0\}$ by symmetry, nor can $\widetilde{Q}_1 \widetilde{Q}_2 \neq 0$ generically on $Z$ (which would force $\dim(\mathbb{A}^2 \times_{\Phi_2} \mathbb{A}^2) \ge 3$, impossible because $\Phi_2$ is dominant of finite generic degree $25$). Thus $H_a \cap H_b$ has pure dimension $2$.

Over $\overline{\mathbb{F}}_q$, let $V \subset \mathbb{A}^2$ be a dense Zariski-open subset over which $\Phi_2 : U := \Phi_2^{-1}(V) \to V$ is finite étale of degree $25$ (avoiding the branch locus, pole locus $\widetilde{Q} = 0$, and the exceptional loci of the Möbius conjugation to $G$). Then $U \times_V U \setminus \Delta_U \to V$ is a finite étale cover of degree $25 \cdot 24 = 600$ whose geometric monodromy action on a fiber is the diagonal action of $G_{\mathrm{geom}} \supseteq A_{25}$ on ordered pairs of distinct elements of $\{1, \dots, 25\}$. Because $A_{25}$ is $2$-transitive, $U \times_V U \setminus \Delta_U$ is connected and smooth, hence irreducible of dimension $2$ over $\overline{\mathbb{F}}_q$.

Let $W_0 := \overline{U \times_V U \setminus \Delta_U} \subset \mathbb{A}^4$. Then $W_0$ is the **unique** irreducible component of $H_a \cap H_b$ over $\overline{\mathbb{F}}_q$ that is not contained in $\Delta := \{(a, b, a, b)\}$ or $\{\widetilde{Q}_1 \widetilde{Q}_2 = 0\}$ and dominates $\mathbb{A}^2$ via $(P_1, P_2) \mapsto \Phi_2(P_1)$. Since $H_a, H_b, \Delta, \widetilde{Q}, \Phi_2$ are all defined over $\mathbb{F}_q$, $\mathrm{Gal}(\overline{\mathbb{F}}_q/\mathbb{F}_q)$ fixes this unique component; therefore $W_0 \subset \mathbb{A}^4$ is an **absolutely irreducible $\mathbb{F}_q$-variety of dimension $2$**.

By Bézout's theorem (Heintz 1983, Theorem 1; Fulton, *Intersection Theory*, Example 8.4.6), the sum of the degrees of all irreducible components of $H_a \cap H_b$ is at most $\deg(H_a)\deg(H_b) \le 17 \cdot 17 = 289$. Since the diagonal $\Delta$ is an irreducible component of $H_a \cap H_b$ of degree $1$ distinct from $W_0$, the degree $\delta := \deg(W_0)$ satisfies
$$\delta \le 289 - 1 = 288.$$

**Step 6.4 (Cafure–Matera effective Lang–Weil contradiction for all $m \ge 38$).**
By **Cafure and Matera (2006)** (*Improved explicit estimates on the number of solutions of equations over a finite field*, Finite Fields Appl. 12 (2006), 155–185):
- **Theorem 7.1:** For any absolutely irreducible $\mathbb{F}_q$-variety $W_0 \subset \mathbb{A}^n$ of dimension $r = 2$ and degree $\delta$, whenever $q > 2(r + 1)\delta^2 = 6 \delta^2$,
  $$\#W_0(\mathbb{F}_q) > q^2 - (\delta - 1)(\delta - 2) q^{3/2} - 5 \delta^{13/3} q.$$
- **Lemma 2.1:** Since $W_0$ is irreducible of dimension $2$ and $W_0 \not\subseteq \Delta$, the intersection $W_0 \cap \Delta$ has dimension at most $1$ and degree at most $\delta \cdot \deg(\Delta) = \delta$, whence
  $$\#(W_0 \cap \Delta)(\mathbb{F}_q) \le \delta q.$$

For every $m \ge 38$ ($q \ge 2^{38} = 274{,}877{,}906{,}944$) and every $\delta \le 288$:
1. $6 \delta^2 \le 6 \cdot 288^2 = 497{,}664 < 2^{38} \le q$ (so Theorem 7.1 applies);
2. Using $\delta \le 288$ and $q \ge 2^{38}$, the exact integer check (verified in `verify.py`)
   $$\bigl(q - 287 \cdot 286 \cdot \lceil\sqrt{q}\rceil - 288\bigr)^3 > 125 \cdot 288^{13}$$
   holds at $q = 2^{38}$ (where $q - 287 \cdot 286 \cdot 2^{19} - 288 = 231{,}843{,}299{,}040 > 2.273 \times 10^{11} > 5 \cdot 288^{13/3}$), and since $q - 287 \cdot 286 \sqrt{q} - 288$ is strictly increasing for $q \ge 2^{38}$, it holds for all $m \ge 38$.

Therefore $\#W_0(\mathbb{F}_q) > \delta q \ge \#(W_0 \cap \Delta)(\mathbb{F}_q)$, so there exists $(a_1, b_1, a_2, b_2) \in W_0(\mathbb{F}_q) \setminus \Delta$. Because $s(y) \neq 0$ on all of $D_4$, we have $\widetilde{Q}(a_1, b_1) \neq 0$ and $\widetilde{Q}(a_2, b_2) \neq 0$, so $H_a = H_b = 0$ yields $\Phi_2(a_1, b_1) = \Phi_2(a_2, b_2)$ with $(a_1, b_1) \neq (a_2, b_2)$, contradicting that $\Phi_2$ is bijective on $\mathbb{F}_q^2$. Hence $g_{n,q}$ is not a PP of $\mathbb{F}_{q^4}$. $\square$

---

## 4. Summary

Cases 1–6 partition all pairs $(q, e)$ with even $q = 2^m > 2$ ($m \ge 2$) and integer $e > 2$:
- $e = 3$: never a PP (Case 1).
- Odd $e \ge 5$: never a PP (Case 2).
- Even $e \ge 8$: never a PP (Case 3).
- $e = 6$: never a PP (Case 4).
- $e = 4$: PP if and only if $q = 4$ (Cases 5 and 6).

Hence $g_{n,q}$ is a permutation polynomial of $\mathbb{F}_{q^e}$ if and only if $(q, e) = (4, 4)$. $\blacksquare$

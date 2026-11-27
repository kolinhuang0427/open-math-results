# Complete Solution to Question 6.1 of Fernando and Kousik (`arXiv:2606.01037v1`)

## 1. Problem Statement and Main Theorem

From Neranga Fernando and Bhitali Kousik, *"A further study of polynomial $g_{n,q}$ over finite fields"*, `arXiv:2606.01037v1` (31 May 2026), Section 6 (`draftMay31.tex`, lines 893–895, `\label{Q1}`):

> **Question 6.1 (`\label{Q1}`).** Let $q > 2$ be even, $e > 0$ be even, and $n = (q - 1) \cdot q^0 + (q - 1) \cdot q^{e/2} + 1 \cdot q^e$. Then $g_{n,q} = S_1 + S_{e/2}^{q^{e/2}} + S_e \cdot S_{e/2}^{q-1}$. Find conditions on $q$ and $e$ for which $g_{n,q}$ is a PP of $\mathbb{F}_{q^e}$.

Here $q = 2^m$ with $m \ge 2$, $e = 2k$ with $k \ge 1$, the polynomial $g_{n,q} \in \mathbb{F}_2[X]$ is uniquely defined by $\sum_{a \in \mathbb{F}_q} (X + a)^n = g_{n,q}(X^q - X)$ (Section 1, Eq. (1.1), `\label{AB1}`), and $S_r(X) := X + X^q + \cdots + X^{q^{r-1}}$ for $r \ge 1$ ($S_0 := 0$, $S_1(X) = X$; Section 2, line 119). On $\mathbb{F}_{q^e}$, $S_e = \mathrm{Tr}_{q^e/q}$.

> **Main Theorem.** Let $q = 2^m > 2$ ($m \ge 2$), let $e > 0$ be even, and let $n = (q - 1) + (q - 1) q^{e/2} + q^e$. Then $g_{n,q}$ is a permutation polynomial (PP) of $\mathbb{F}_{q^e}$ **if and only if** either:
> 1. $q = 4$ and $4 \mid e$, **or**
> 2. $e = 4$ and $m \not\equiv 3 \pmod 4$.

*(Note: the pair $(q, e) = (4, 4)$ belongs to both families and corresponds to the desirable triple $(n, e; q) = (307, 4; 4)$ in Table 1 of `arXiv:2606.01037v1`.)*

---

## 2. Self-Contained Derivation of $g_{n,q}$ and Reduction to $\Phi$

All algebra takes place in characteristic $2$.

### Lemma 2.1 (Explicit formula for $g_{n,q}$)
For every even $q > 2$, even $e = 2k \ge 2$, and $n = (q - 1) + (q - 1) q^k + q^{2k}$,
$$g_{n,q}(X) = S_1(X) + S_k(X)^{q^k} + S_{2k}(X) S_k(X)^{q-1}$$
holds identically in $\mathbb{F}_2[X]$.

**Proof.** Let $l := (q - 1) + (q - 1) q^k$, so $n = l + q^{2k}$. Write $Y := X^q + X$; then $S_r(Y) = \sum_{i=0}^{r-1} (X^{q^{i+1}} + X^{q^i}) = X^{q^r} + X$ for every $r \ge 1$. Over $\mathbb{F}_2$, by Eq. (1.1) (`\label{AB1}`) and the identity $X^{q^{2k}} + a = (X + a) + S_{2k}(Y)$ for $a \in \mathbb{F}_q$:
$$g_{n,q}(Y) = \sum_{a \in \mathbb{F}_q} (X + a)^l (X + a)^{q^{2k}} = \sum_{a \in \mathbb{F}_q} (X + a)^{l+1} + S_{2k}(Y) \sum_{a \in \mathbb{F}_q} (X + a)^l = g_{l+1, q}(Y) + S_{2k}(Y) g_{l, q}(Y).$$
Since $q$ is a power of $2$, Lucas's theorem gives $\binom{q-1}{j} \equiv 1 \pmod 2$ for $0 \le j \le q - 1$, so $(Z + a)^{q-1} = \sum_{j=0}^{q-1} Z^j a^{q-1-j}$. Recall also the standard power-sum identity in $\mathbb{F}_q$ ($q > 2$): $\sum_{a \in \mathbb{F}_q} a^r = 1$ if $r = q - 1$, and $0$ if $0 \le r \le q - 2$ or $r = q$ (as well as $\sum_{a \in \mathbb{F}_q} a^{2q-2} = 1$).
- For $g_{l,q}(Y)$:
  $$g_{l,q}(Y) = \sum_{a \in \mathbb{F}_q} (X + a)^{q-1} (X^{q^k} + a)^{q-1} = \sum_{i=0}^{q-1} \sum_{j=0}^{q-1} X^i X^{j q^k} \sum_{a \in \mathbb{F}_q} a^{2q - 2 - i - j}.$$
  The inner sum is nonzero precisely when $2q - 2 - i - j \in \{q - 1, 2q - 2\}$, i.e., $(i, j) = (0, 0)$ or $i + j = q - 1$:
  $$g_{l,q}(Y) = 1 + \sum_{j=0}^{q-1} X^{q-1-j} (X^{q^k})^j = 1 + (X + X^{q^k})^{q-1} = 1 + S_k(Y)^{q-1}.$$
- For $g_{l+1, q}(Y)$ (where $l + 1 = q + (q - 1)q^k$):
  $$g_{l+1,q}(Y) = \sum_{a \in \mathbb{F}_q} (X^q + a) \sum_{j=0}^{q-1} X^{j q^k} a^{q-1-j} = X^q \sum_{j=0}^{q-1} X^{j q^k} \sum_{a \in \mathbb{F}_q} a^{q-1-j} + \sum_{j=0}^{q-1} X^{j q^k} \sum_{a \in \mathbb{F}_q} a^{q-j}.$$
  The first sum selects $j = 0$ (giving $X^q$) and the second selects $j = 1$ (giving $X^{q^k}$, since $q - j = q$ at $j = 0$ sums to $0$ as $q > 2$). Thus
  $$g_{l+1,q}(Y) = X^q + X^{q^k} = (X^q + X) + (X + X^{q^k}) = Y + S_k(Y).$$
Combining these and using $S_k(Y) + S_{2k}(Y) = S_k(Y)^{q^k}$ gives
$$g_{n,q}(Y) = Y + S_k(Y) + S_{2k}(Y)(1 + S_k(Y)^{q-1}) = Y + S_k(Y)^{q^k} + S_{2k}(Y) S_k(Y)^{q-1}.$$
Since $Y = X^q + X$ is transcendental over $\mathbb{F}_2$, the polynomial identity follows. $\square$

---

### Lemma 2.2 (Reduction to $\Phi$ on $\mathrm{im}(S_k)$)
Let $e = 2k \ge 2$ and consider the $\mathbb{F}_q$-linear map $S_k : \mathbb{F}_{q^{2k}} \to \mathbb{F}_{q^{2k}}$. Then:
1. The image of $S_k$ is
   $$V_k := \mathrm{im}(S_k) = \bigl\{y \in \mathbb{F}_{q^{2k}} : t(y) := y + y^{q^k} \in \mathbb{F}_q\bigr\}, \qquad |V_k| = q^{k+1}.$$
2. Define $\Phi : V_k \to V_k$ by
   $$\Phi(y) := y + S_k(y) + k \cdot t(y) + t(y)\, S_k(y^{q-1}),$$
   where $k \cdot t(y) = t(y)$ if $k$ is odd and $0$ if $k$ is even. Then $\Phi$ is $\mathbb{F}_q$-homogeneous ($\Phi(cy) = c\,\Phi(y)$ for all $c \in \mathbb{F}_q, y \in V_k$), and $g_{n,q}$ is a PP of $\mathbb{F}_{q^{2k}}$ **if and only if** $\Phi : V_k \to V_k$ is a bijection.

**Proof.**
1. For any $x \in \mathbb{F}_{q^{2k}}$, $S_k(x)^q + S_k(x) = x^{q^k} + x$. Hence $S_k(x) = 0$ implies $x \in \mathbb{F}_{q^k}$ and $\mathrm{Tr}_{q^k/q}(x) = S_k(x) = 0$. Conversely, every $x \in \ker(\mathrm{Tr}_{q^k/q}) \subset \mathbb{F}_{q^k}$ satisfies $S_k(x) = 0$. Thus $|\ker(S_k)| = q^{k-1}$ and $|V_k| = q^{2k}/q^{k-1} = q^{k+1}$. For every $y = S_k(x) \in V_k$,
   $$t(y) = S_k(x) + S_k(x)^{q^k} = S_{2k}(x) = \mathrm{Tr}_{q^{2k}/q}(x) \in \mathbb{F}_q.$$
   Conversely, for each $t \in \mathbb{F}_q$, the equation $y^{q^k} + y = t$ has $\mathrm{Tr}_{q^{2k}/q^k}(t) = t + t^{q^k} = 0$, so it has exactly $q^k$ solutions in $\mathbb{F}_{q^{2k}}$; summing over $t \in \mathbb{F}_q$ gives $|\{y \in \mathbb{F}_{q^{2k}} : y + y^{q^k} \in \mathbb{F}_q\}| = q^{k+1} = |V_k|$. Thus the two sets coincide.
2. First check that $\Phi$ maps $V_k$ into $V_k$: for any $y = S_k(x) \in V_k$, we have $t(y) = S_{2k}(x)$ and $S_k(y^{q^k}) = S_k(y + t(y)) = S_k(y) + k \cdot t(y)$, so
   $$S_k(g_{n,q}(x)) = S_k(x) + S_k(y^{q^k}) + t(y) S_k(y^{q-1}) = y + S_k(y) + k \cdot t(y) + t(y) S_k(y^{q-1}) = \Phi(y) \in V_k.$$
   Next, fix any $b \in \mathbb{F}_{q^{2k}}$. If $x \in \mathbb{F}_{q^{2k}}$ satisfies $g_{n,q}(x) = b$, setting $y := S_k(x) \in V_k$ gives $S_{2k}(x) = t(y)$, $x = b + y^{q^k} + t(y) y^{q-1}$, and $\Phi(y) = S_k(g_{n,q}(x)) = S_k(b)$. Conversely, for any $y \in V_k$ with $\Phi(y) = S_k(b)$, define $x := b + y^{q^k} + t(y) y^{q-1} \in \mathbb{F}_{q^{2k}}$. Applying $S_k$ gives
   $$S_k(x) = S_k(b) + S_k(y^{q^k}) + t(y) S_k(y^{q-1}) = \Phi(y) + S_k(y) + k \cdot t(y) + t(y) S_k(y^{q-1}) = y,$$
   so $S_{2k}(x) = t(y)$ and $g_{n,q}(x) = x + y^{q^k} + t(y) y^{q-1} = b$. The map $x \mapsto y = S_k(x)$ therefore establishes a bijection between $\{x \in \mathbb{F}_{q^{2k}} : g_{n,q}(x) = b\}$ and $\{y \in V_k : \Phi(y) = S_k(b)\}$. Since $S_k : \mathbb{F}_{q^{2k}} \to V_k$ is surjective, $g_{n,q}$ is a bijection on $\mathbb{F}_{q^{2k}}$ iff $\Phi$ is a bijection on $V_k$. Finally, for $c \in \mathbb{F}_q^*$ and $y \in V_k$, $t(cy) = c\,t(y)$, $S_k(cy) = c\,S_k(y)$, and $(cy)^{q-1} = c^{q-1} y^{q-1} = y^{q-1}$, so $\Phi(cy) = c\,\Phi(y)$; at $c = 0$, $\Phi(0) = 0 = 0 \cdot \Phi(y)$ (as $q - 1 \ge 3$). $\square$

---

## 3. Case Analysis Covering All Pairs $(q, e)$

Every pair $(q, e)$ with $q = 2^m > 2$ ($m \ge 2$) and even $e = 2k \ge 2$ falls into one of four exhaustive cases below.

### Case 1: $e \equiv 2 \pmod 4$ ($k$ odd) $\implies$ NEVER a PP

Let $x \in \mathbb{F}_{q^k}$. Then $S_{2k}(x) = \mathrm{Tr}_{q^{2k}/q}(x) = 2\,\mathrm{Tr}_{q^k/q}(x) = 0$ and $S_k(x) = \mathrm{Tr}_{q^k/q}(x) \in \mathbb{F}_q$, so $S_k(x)^{q^k} = S_k(x)$ and
$$g_{n,q}(x) = x + \mathrm{Tr}_{q^k/q}(x).$$
Since $\mathrm{Tr}_{q^k/q} : \mathbb{F}_{q^k} \to \mathbb{F}_q$ is surjective, pick $x \in \mathbb{F}_{q^k}$ with $c := \mathrm{Tr}_{q^k/q}(x) \neq 0$, and set $x' := x + c \in \mathbb{F}_{q^k} \setminus \{x\}$. Because $k$ is odd and $c \in \mathbb{F}_q$, $\mathrm{Tr}_{q^k/q}(c) = k c = c$, whence $\mathrm{Tr}_{q^k/q}(x') = c + c = 0$. Therefore
$$g_{n,q}(x') = x' + 0 = x + c = g_{n,q}(x),$$
showing $g_{n,q}$ is not injective on $\mathbb{F}_{q^e}$. $\square$

---

### Case 2: $q = 4$ and $4 \mid e$ ($k \ge 2$ even) $\implies$ ALWAYS a PP

Let $\mathbb{F}_4 = \{0, 1, \omega, \omega^2\}$ with $\omega^2 + \omega + 1 = 0$. Since $k$ is even and $q = 4$, Lemma 2.2 gives
$$\Phi(y) = y + S_k(y) + t(y)\, S_k(y^3) \qquad (y \in V_k).$$
We prove $\Phi : V_k \to V_k$ is injective (hence bijective, as $V_k$ is finite).

**Step 2.1 (Action on $\{t = 0\} = \mathbb{F}_{4^k}$).**
For $y \in \mathbb{F}_{4^k}$, $t(y) = 0$ and $\Phi(y) = y + S_k(y) = y + \mathrm{Tr}_{4^k/4}(y) \in \mathbb{F}_{4^k}$. Because $k$ is even, $S_k(c) = k c = 0$ for all $c \in \mathbb{F}_4$, so $S_k(\Phi(y)) = S_k(y)$ and $\Phi(\Phi(y)) = y$. Thus $\Phi$ restricts to a bijection $\mathbb{F}_{4^k} \to \mathbb{F}_{4^k}$.

**Step 2.2 (Image of $\{t \neq 0\}$ avoids $\{t = 0\}$).**
Take $y \in V_k$ with $t := t(y) \in \mathbb{F}_4^*$ (so $t^3 = 1$, $t^4 = t$). Since $k$ is even, $S_k(y)^{4^k} = S_k(y^{4^k}) = S_k(y + t) = S_k(y) + kt = S_k(y)$, and $S_k(t^3) = kt^3 = 0$. Also $(a + b)^2 = a^2 + b^2$ gives $S_k(y^2) = S_k(y)^2$. Computing $s(y) := t(\Phi(y)) = \Phi(y) + \Phi(y)^{4^k}$ yields
$$\begin{aligned}
s(y) &= (y + y^{4^k}) + \bigl(S_k(y) + S_k(y)^{4^k}\bigr) + t\,S_k\bigl(y^3 + (y + t)^3\bigr) \\
&= t + t\,S_k(t y^2 + t^2 y + t^3) = t + t^2 S_k(y)^2 + t^3 S_k(y) = t + t^2 S_k(y)^2 + S_k(y).
\end{aligned}$$
Set $z := S_k(y) / t$. Because $S_k(y)^4 + S_k(y) = y^{4^k} + y = t = t^4$, we have $z^4 + z = 1$. Hence $r := z^2 + z$ satisfies $r^2 + r = z^4 + z = 1$, so $r \in \{\omega, \omega^2\}$ and
$$\frac{s(y)}{t} = 1 + t^3 z^2 + z = 1 + r \in \{\omega, \omega^2\}.$$
In particular, $s(y) \neq 0$ (so $\Phi(V_k \setminus \mathbb{F}_{4^k}) \cap \mathbb{F}_{4^k} = \emptyset$) and $s(y) \neq t(y)$.

**Step 2.3 (Quadratic invariant and injectivity on $\{t \neq 0\}$).**
Applying the $\mathbb{F}_4$-linear operator $u \mapsto u^4 + u$ to $\Phi(y)$ and using $S_k(u)^4 + S_k(u) = u^{4^k} + u$ together with $t^3 = 1, t^4 = t$:
$$\begin{aligned}
\Phi(y)^4 + \Phi(y) &= (y^4 + y) + (y^{4^k} + y) + t\bigl((y + t)^3 + y^3\bigr) \\
&= y^4 + (y + t) + t(t y^2 + t^2 y + t^3) = y^4 + t^2 y^2 = (y^2 + t y)^2.
\end{aligned}$$
Now suppose $\Phi(y_1) = \Phi(y_2)$ with $t_1 := t(y_1), t_2 := t(y_2) \in \mathbb{F}_4^*$. Then $s := s(y_1) = s(y_2) \in \mathbb{F}_4^*$, and taking square roots in characteristic $2$ yields
$$y_1^2 + t_1 y_1 = y_2^2 + t_2 y_2.$$
- **Subcase $t_1 = t_2 = t$:** Then $(y_1 + y_2)^2 + t(y_1 + y_2) = 0$, so $y_2 \in \{y_1, y_1 + t\}$. If $y_2 = y_1 + t = y_1^{4^k}$, then $\Phi(y_2) = \Phi(y_1^{4^k}) = \Phi(y_1)^{4^k} = \Phi(y_1) + s \neq \Phi(y_1)$, a contradiction. Hence $y_1 = y_2$.
- **Subcase $t_1 \neq t_2$:** Since $t_1, t_2 \in \mathbb{F}_4^* \setminus \{s\}$ are distinct, $\{t_1, t_2\} = \{s\omega, s\omega^2\}$. Replacing $(y_1, y_2)$ by $(y_1/t_1, y_2/t_1)$ (using $\mathbb{F}_4$-homogeneity of $\Phi$) normalizes $t_1 = 1$, leaving $(t_2, s) \in \{(\omega, \omega^2), (\omega^2, \omega)\}$. Applying the $\mathbb{F}_2$-Frobenius map $u \mapsto u^2$ (which commutes with $\Phi$ because $\Phi$ has $\mathbb{F}_2$-coefficients, and exchanges $\omega \leftrightarrow \omega^2$) if necessary, we may assume
  $$t_1 = 1, \qquad t_2 = \omega, \qquad s = \omega^2.$$
  Set $A := y_1^2 + y_1 = y_2^2 + \omega y_2$. Then $A^{4^k} = (y_1 + 1)^2 + (y_1 + 1) = A$, so $A \in \mathbb{F}_{4^k}$. By Step 2.2 at $t_1 = 1$, $S_k(A) = S_k(y_1)^2 + S_k(y_1) = 1 + s = 1 + \omega^2 = \omega$. Write $a_r := A^{4^r}$ for $0 \le r \le k - 1$ (indices modulo $k$), so $\sum_{r=0}^{k-1} a_r = \omega$ and $\sum_{r=0}^{k-1} a_r^2 = \omega^2$.
  - From $y_1^2 = y_1 + A$, we have $y_1^3 = A + (A + 1)y_1$ and $y_1^4 = y_1 + A + A^2$, hence by induction $y_1^{4^j} = y_1 + \sum_{r=0}^{j-1} (a_r + a_r^2)$ for all $j \ge 0$. Thus
    $$\Phi(y_1) = y_1 + S_k(y_1) + S_k(A) + \sum_{j=0}^{k-1}(a_j + 1) y_1^{4^j} = y_1 + \omega + \sum_{j=0}^{k-1} a_j y_1^{4^j} = \omega^2 y_1 + \omega + P(A) + Q(A),$$
    where $P(A) := \sum_{0 \le r < j \le k-1} a_r a_j$ and $Q(A) := \sum_{0 \le r < j \le k-1} a_r^2 a_j$ (using $1 + S_k(A) = 1 + \omega = \omega^2$).
  - From $y_2^2 = \omega y_2 + A$, we have $y_2^3 = \omega A + (\omega^2 + A)y_2$ and $y_2^4 = \omega^2(\omega y_2 + A) + A^2 = y_2 + \omega^2 A + A^2$, hence by induction $y_2^{4^j} = y_2 + \sum_{r=0}^{j-1}(\omega^2 a_r + a_r^2)$ for all $j \ge 0$. Thus
    $$\Phi(y_2) = y_2 + S_k(y_2) + \omega^2 S_k(A) + \sum_{j=0}^{k-1}(1 + \omega a_j) y_2^{4^j} = y_2 + 1 + \omega \sum_{j=0}^{k-1} a_j y_2^{4^j} = \omega y_2 + 1 + P(A) + \omega Q(A)$$
    (using $\omega^2 S_k(A) = \omega^3 = 1$, $1 + \omega S_k(A) = 1 + \omega^2 = \omega$, and $\omega \cdot \omega^2 = 1$).

  Adding $\Phi(y_1) + \Phi(y_2) = 0$ cancels $P(A)$ and gives
  $$W := \omega^2 y_1 + \omega y_2 = (1 + \omega) + (1 + \omega) Q(A) = \omega^2\bigl(1 + Q(A)\bigr).$$
  On the one hand, $W^2 + \omega^2 W = \omega(y_1^2 + y_1) + \omega^2(y_2^2 + \omega y_2) = (\omega + \omega^2) A = A$; substituting $W = \omega^2(1 + Q(A))$ gives $\omega(Q(A)^2 + Q(A)) = A$, i.e.,
  $$Q(A)^2 + Q(A) = \omega^2 A.$$
  On the other hand, using $a_r^4 = a_{r+1}$,
  $$Q(A)^2 = \sum_{0 \le r < j \le k-1} a_{r+1} a_j^2 = \sum_{j=1}^{k-1} a_j^3 + \sum_{1 \le u < j \le k-1} a_u a_j^2.$$
  Comparing with the full product $1 = \omega^2 \cdot \omega = \bigl(\sum_{r=0}^{k-1} a_r^2\bigr)\bigl(\sum_{j=0}^{k-1} a_j\bigr) = \sum_{j=0}^{k-1} a_j^3 + \sum_{0 \le r < j \le k-1} a_r^2 a_j + \sum_{0 \le u < j \le k-1} a_u a_j^2$ yields
  $$1 + Q(A) + Q(A)^2 = a_0^3 + \sum_{j=1}^{k-1} a_0 a_j^2 = a_0 \sum_{j=0}^{k-1} a_j^2 = \omega^2 A,$$
  so $Q(A)^2 + Q(A) + \omega^2 A = 1 \neq 0$, a contradiction.

Thus $\Phi$ is injective on $V_k$, and $g_{n,q}$ is a PP of $\mathbb{F}_{4^e}$. $\square$

---

### Case 3: $q \ge 8$ and $4 \mid e$ with $e \ge 8$ ($k \ge 4$ even) $\implies$ NEVER a PP

Because $k$ is even, $\Phi(y) = y + S_k(y) + t(y) S_k(y^{q-1})$ restricts on $\{t(y) = 0\} = \mathbb{F}_{q^k}$ to $\Phi(y) = y + \mathrm{Tr}_{q^k/q}(y)$, which is an involution (hence a bijection $\mathbb{F}_{q^k} \to \mathbb{F}_{q^k}$, since $\mathrm{Tr}_{q^k/q}(c) = k c = 0$ for $c \in \mathbb{F}_q$). To prove $\Phi$ is not bijective on $V_k$, it suffices to exhibit $y \in V_k$ with $t(y) = 1$ and $s(y) := t(\Phi(y)) = 0$ (which forces $\Phi(y) \in \mathbb{F}_{q^k}$, colliding with $\Phi|_{\mathbb{F}_{q^k}}$).

Fix $\alpha \in \mathbb{F}_{q^{2k}}$ with $\alpha^{q^k} = \alpha + 1$. Every $y \in V_k$ with $t(y) = 1$ has the form $y = u + \alpha$ with $u \in \mathbb{F}_{q^k}$. Since $k$ is even, $S_k(y)^{q^k} = S_k(y + 1) = S_k(y) + k = S_k(y)$, so
$$s(u + \alpha) = \Phi(u + \alpha) + \Phi(u + \alpha)^{q^k} = 1 + S_k\bigl(f(u)\bigr) = 1 + \mathrm{Tr}_{q^k/q}\bigl(f(u)\bigr),$$
where $f(u) := (u + \alpha)^{q-1} + (u + \alpha + 1)^{q-1}$ satisfies $f(u)^{q^k} = f(u)$ and hence $f(u) \in \mathbb{F}_{q^k}[u]$.

By Lucas's theorem, $(Z + 1)^{q-1} + Z^{q-1} = \sum_{j=0}^{q-2} Z^j$, so
$$f(u) = \sum_{j=0}^{q-2} (u + \alpha)^j \in \mathbb{F}_{q^k}[u].$$
Its degree is $q - 2$ with $u^{q-2}$ coefficient $1$; its $u^{q-3}$ coefficient is $\binom{q-2}{1}\alpha + 1 = (q - 2)\alpha + 1 = 1$ (since $q - 2$ is even).

Now fix any $c \in \mathbb{F}_q^*$. For any $z \in \mathbb{F}_{q^k}$, $\mathrm{Tr}_{q^k/2}(z^2) = \mathrm{Tr}_{q^k/2}(z)$, and squaring is an automorphism of $\mathbb{F}_{q^k}$. Repeatedly replacing every even-degree monomial $a_{2r} u^{2r}$ ($r \ge 1$) of $c f(u)$ by $a_{2r}^{1/2} u^r$ produces a polynomial $g_c(u) \in \mathbb{F}_{q^k}[u]$ such that $\mathrm{Tr}_{q^k/2}(g_c(u)) = \mathrm{Tr}_{q^k/2}(c f(u))$ for all $u \in \mathbb{F}_{q^k}$ and every term of positive degree in $g_c(u)$ has odd degree. Because every reduced even-degree monomial from $c f(u)$ acquires degree at most $(q - 2)/2 = q/2 - 1$, and for $q \ge 8$ we have $q/2 - 1 < q - 3$, no reduction can cancel the odd-degree monomial $c u^{q-3}$. Hence $g_c(u)$ has exact odd degree $q - 3 \ge 5$ (and therefore cannot be written as $h^2 + h + \beta$ over $\overline{\mathbb{F}}_2$, since $\deg(h^2 + h)$ is even for all nonconstant $h$).

By the Carlitz–Uchiyama (Weil) bound in characteristic $2$ (Lidl–Niederreiter, Theorem 5.38),
$$\left|\sum_{u \in \mathbb{F}_{q^k}} (-1)^{\mathrm{Tr}_{q^k/2}(c f(u))}\right| = \left|\sum_{u \in \mathbb{F}_{q^k}} (-1)^{\mathrm{Tr}_{q^k/2}(g_c(u))}\right| \;\le\; (q - 4)\, q^{k/2} \qquad \forall\, c \in \mathbb{F}_q^*.$$
By character orthogonality on $\mathbb{F}_q$ and transitivity of trace $\mathrm{Tr}_{q/2}(c\,\mathrm{Tr}_{q^k/q}(f(u))) = \mathrm{Tr}_{q^k/2}(c f(u))$,
$$\begin{aligned}
q \cdot \#\bigl\{u \in \mathbb{F}_{q^k} : \mathrm{Tr}_{q^k/q}(f(u)) = 1\bigr\}
&= \sum_{u \in \mathbb{F}_{q^k}} \sum_{c \in \mathbb{F}_q} (-1)^{\mathrm{Tr}_{q/2}(c(1 + \mathrm{Tr}_{q^k/q}(f(u))))} \\
&= q^k + \sum_{c \in \mathbb{F}_q^*} (-1)^{\mathrm{Tr}_{q/2}(c)} \sum_{u \in \mathbb{F}_{q^k}} (-1)^{\mathrm{Tr}_{q^k/2}(c f(u))} \\
&\ge q^k - (q - 1)(q - 4) q^{k/2} = q^{k/2}\bigl(q^{k/2} - (q^2 - 5q + 4)\bigr).
\end{aligned}$$
Since $k \ge 4$ and $q \ge 8$, $q^{k/2} \ge q^2 > q^2 - 5q + 4$ (as $5q - 4 \ge 36 > 0$), so $\#\{u \in \mathbb{F}_{q^k} : s(u + \alpha) = 0\} > 0$. Thus $\Phi$ is not injective and $g_{n,q}$ is not a PP of $\mathbb{F}_{q^e}$. $\square$

---

### Case 4: $e = 4$ ($k = 2$, $q = 2^m > 2$) $\implies$ PP if and only if $m \not\equiv 3 \pmod 4$

At $e = 4$ ($k = 2$), Lemma 2.2 gives $V_2 = \{y \in \mathbb{F}_{q^4} : t(y) := y + y^{q^2} \in \mathbb{F}_q\}$ and
$$\Phi(y) = y + (y + y^q) + t(y)\bigl(y^{q-1} + y^{q^2 - q}\bigr) = y^q + t(y)\bigl(y^{q-1} + y^{q^2 - q}\bigr).$$
On $\{t(y) = 0\} = \mathbb{F}_{q^2}$, $\Phi(y) = y^q$ is a bijection $\mathbb{F}_{q^2} \to \mathbb{F}_{q^2}$.

Now restrict to the affine hyperplane $U := \{u \in \mathbb{F}_{q^4} : u^{q^2} = u + 1\}$ (i.e., $t(u) = 1$). Every $u \in U$ satisfies $u \notin \mathbb{F}_{q^2}$, so $u \notin \{0, 1\}$, and $w := u^q$ also lies in $U$ (with $w^q = u^{q^2} = u + 1$ and $w \notin \{0, 1\}$). On $U$,
$$\Phi(u) = w + \frac{w}{u} + \frac{u + 1}{w}.$$

**Unit-circle parametrization.** Let $\mu_{q^2 + 1} := \{x \in \mathbb{F}_{q^4}^* : x^{q^2 + 1} = 1\}$ be the cyclic subgroup of $\mathbb{F}_{q^4}^*$ of order $q^2 + 1$. The involution $u \mapsto x := \frac{u}{u + 1}$ (inverse $u = \frac{x}{x + 1}$) gives a bijection $U \xrightarrow{\sim} \mu_{q^2 + 1} \setminus \{1\}$: indeed, for $u \notin \{0, 1\}$,
$$x^{q^2} = \frac{u^{q^2}}{u^{q^2} + 1} = x^{-1} \iff \frac{u^{q^2}}{u^{q^2} + 1} = \frac{u + 1}{u} \iff u^{q^2} = u + 1.$$
For $u \in U$ with $x = \frac{u}{u + 1} \in \mu_{q^2 + 1} \setminus \{1\}$, put $y := x^q \in \mu_{q^2 + 1} \setminus \{1\}$ (so $y^q = x^{q^2} = x^{-1}$, $w = \frac{y}{y + 1}$, and $u + 1 = \frac{1}{x + 1}$). Then
$$w + \frac{w}{u} = w \cdot \frac{u + 1}{u} = \frac{y}{x(y + 1)}, \qquad \frac{u + 1}{w} = \frac{y + 1}{y(x + 1)},$$
and adding over the common denominator $x y (x + 1)(y + 1)$ (nonzero since $x, y \notin \{0, 1\}$) yields
$$\Phi(u) = \frac{y^2(x + 1) + x(y + 1)^2}{x y(x + 1)(y + 1)} = \frac{x + y^2}{x y(x + 1)(y + 1)}.$$
Applying the $q^2$-Frobenius map (using $x^{q^2} = x^{-1}$ and $y^{q^2} = y^{-1}$) and multiplying numerator and denominator by $x^2 y^2$ gives the key multiplicative relation:
$$\Phi(u)^{q^2} = \frac{x^{-1} + y^{-2}}{x^{-1} y^{-1}(x^{-1} + 1)(y^{-1} + 1)} = \frac{x(x + y^2)}{(x + 1)(y + 1)} = x^2 y \cdot \frac{x + y^2}{x y(x + 1)(y + 1)} = x^{q + 2}\,\Phi(u).$$
Consequently,
$$s(u) := t(\Phi(u)) = \Phi(u) + \Phi(u)^{q^2} = \bigl(1 + x^{q + 2}\bigr)\,\Phi(u).$$

**Exact gcd calculations.** Since $q^2 + 1$ is odd,
$$4(q^2 + 1) = (2q - 1)(2q + 1) + 5 \implies \gcd(2q - 1,\; q^2 + 1) = \gcd(2q - 1,\; 5),$$
$$q^2 + 1 = (q + 2)(q - 2) + 5 \implies \gcd(q + 2,\; q^2 + 1) = \gcd(q + 2,\; 5).$$
Since $q = 2^m$ and $2^m \bmod 5$ cycles through $(1, 2, 4, 3)$ for $m \equiv 0, 1, 2, 3 \pmod 4$:
- $2q - 1 = 2^{m+1} - 1 \equiv 0 \pmod 5 \iff m \equiv 3 \pmod 4$,
- $q + 2 = 2^m + 2 \equiv 0 \pmod 5 \iff m \equiv 3 \pmod 4$.

Thus both $\gcd(2q - 1, q^2 + 1)$ and $\gcd(q + 2, q^2 + 1)$ equal $5$ when $m \equiv 3 \pmod 4$, and equal $1$ when $m \not\equiv 3 \pmod 4$.

- **Subcase 4a: $m \equiv 3 \pmod 4$ $\implies$ NOT a PP.**
  Since $5 \mid (q^2 + 1)$ and $\mu_{q^2 + 1}$ is cyclic of order $q^2 + 1$, pick an element $x \in \mu_{q^2 + 1} \setminus \{1\}$ of order $5$. Because $5 \mid (2q - 1)$, we have $x^{2q} = x$, i.e., $x + y^2 = 0$. Letting $u := \frac{x}{x + 1} \in U$ gives $u \neq 0$ and $\Phi(u) = 0 = \Phi(0)$, so $\Phi$ is not injective and $g_{n,q}$ is not a PP of $\mathbb{F}_{q^4}$.

- **Subcase 4b: $m \not\equiv 3 \pmod 4$ $\implies$ ALWAYS a PP.**
  For every $u \in U$ with corresponding $x \in \mu_{q^2 + 1} \setminus \{1\}$:
  1. $\Phi(u) = 0 \iff x + y^2 = 0 \iff x^{2q - 1} = 1$, impossible since $\gcd(2q - 1, q^2 + 1) = 1$ and $x \neq 1$.
  2. $1 + x^{q + 2} = 0 \iff x^{q + 2} = 1$, impossible since $\gcd(q + 2, q^2 + 1) = 1$ and $x \neq 1$.

  Hence $s(u) = (1 + x^{q + 2})\,\Phi(u) \neq 0$ for all $u \in U$. Since $\Phi(u) \neq 0$ cancels cleanly, the normalized map $\Psi : U \to U$, $\Psi(u) := \Phi(u) / s(u)$, is given explicitly by
  $$\Psi(u) = \frac{1}{1 + x^{q + 2}}.$$
  *(Check that $\Psi(u) \in U$: $\Psi(u)^{q^2} = \frac{1}{1 + x^{-(q+2)}} = \frac{x^{q+2}}{1 + x^{q+2}} = \Psi(u) + 1$, and $\Psi(u) \neq 1$ since $x \neq 0$.)* Under the bijection $v \mapsto X_{\mathrm{out}} := \frac{v}{v + 1}$ from $U$ to $\mu_{q^2 + 1} \setminus \{1\}$, $\Psi$ conjugates to the monomial map
  $$X_{\mathrm{out}} = \frac{\Psi(u)}{\Psi(u) + 1} = \frac{\frac{1}{1 + x^{q+2}}}{\frac{x^{q+2}}{1 + x^{q+2}}} = x^{-(q + 2)} \qquad \text{on } \mu_{q^2 + 1} \setminus \{1\}.$$
  Because $\gcd(q + 2, q^2 + 1) = 1$, the map $x \mapsto x^{-(q + 2)}$ is a group automorphism of $\mu_{q^2 + 1}$ fixing $1$, hence a bijection on $\mu_{q^2 + 1} \setminus \{1\}$. Therefore $\Psi : U \to U$ is a bijection.

  Finally, we verify that $\Phi : V_2 \to V_2$ is a bijection:
  - $\Phi$ maps $\{t = 0\} = \mathbb{F}_{q^2}$ bijectively onto $\mathbb{F}_{q^2}$.
  - Every element of $V_2 \setminus \mathbb{F}_{q^2}$ writes uniquely as $y = t u$ with $t \in \mathbb{F}_q^*$ and $u \in U$. By $\mathbb{F}_q$-homogeneity, $\Phi(tu) = t\,\Phi(u)$ satisfies $t(\Phi(tu)) = t\,s(u) \in \mathbb{F}_q^*$, so $\Phi(V_2 \setminus \mathbb{F}_{q^2}) \subseteq V_2 \setminus \mathbb{F}_{q^2}$.
  - For any target $v \in V_2 \setminus \mathbb{F}_{q^2}$, set $s_0 := t(v) \in \mathbb{F}_q^*$ and $v_1 := v / s_0 \in U$. Then $\Phi(tu) = v$ is equivalent to $t\,s(u) = s_0$ and $\Psi(u) = \Phi(u)/s(u) = v_1$. Since $\Psi : U \to U$ is a bijection, $u \in U$ is uniquely determined by $\Psi(u) = v_1$, and then $t = s_0 / s(u) \in \mathbb{F}_q^*$ is uniquely determined.

  Hence $\Phi : V_2 \to V_2$ is bijective, and by Lemma 2.2, $g_{n,q}$ is a PP of $\mathbb{F}_{q^4}$. $\square$

---

## 4. Summary

Cases 1–4 partition all pairs $(q, e)$ with even $q = 2^m > 2$ ($m \ge 2$) and even $e \ge 2$:
- $e \equiv 2 \pmod 4$: never a PP (Case 1).
- $4 \mid e, e \ge 8$: PP iff $q = 4$ (Cases 2 and 3).
- $e = 4$: PP iff $m \not\equiv 3 \pmod 4$ (Case 4; note $q = 4$ has $m = 2 \not\equiv 3 \pmod 4$).

Combining these yields the complete necessary and sufficient condition of the Main Theorem. $\blacksquare$

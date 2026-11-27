# Complete Classification for Question 6.3 of Fernando–Kousik (`arXiv:2606.01037v1`)

## Source and Statement

From Neranga Fernando and Bhitali Kousik, *A further study of polynomial $g_{n,q}$ over finite fields*, `arXiv:2606.01037v1` (31 May 2026), `draftMay31.tex`, Section 6, **Question 6.3** (`\label{Q3}`, lines 911–915; notation $S_k(X) := \sum_{i=0}^{k-1} X^{q^i}$ for $k \ge 1$ and $S_0 := 0$ from Section 2, line 119; identity from Lemma 2.4, `\label{L310}`, lines 148–151):

> Let $q > 2$ be even, $n = 1 \cdot q^0 + (q - 1)\cdot q^{e/2} + (q - 1)\cdot q^e$, and $e > 0$ be even. Then
> $$g_{1 \cdot q^0 + (q - 1)\cdot q^{e/2} + (q - 1)\cdot q^e}(X) = S_{e/2 + 1}(X)^{q^{e/2}} + S_e(X) + S_e(X)\,\bigl(S_{e/2}(X)^{q^{e/2}}\bigr)^{q - 1}.$$
> Find conditions on $q$ and $e$ for which $g_{n,q}$ is a permutation polynomial (PP) of $\mathbb{F}_{q^e}$.

## Main Theorem

**Theorem.** Let $q = 2^m > 2$ ($m \ge 2$), $e > 0$ be even, and $n = 1 + (q - 1) q^{e/2} + (q - 1) q^e$. Then $g_{n,q}$ is a permutation polynomial of $\mathbb{F}_{q^e}$ **if and only if**
$$q = 4 \quad \text{and} \quad 4 \mid e.$$

---

## 1. Reduction to $\Phi_{\mathrm{Q3}}$ on $\mathrm{im}(S_k)$

Write $e = 2k$ ($k \ge 1$) and work in $\mathbb{F}_{q^{2k}}$ (characteristic $2$). For $x \in \mathbb{F}_{q^{2k}}$, note that
$$S_{k+1}(x)^{q^k} = \bigl(S_k(x) + x^{q^k}\bigr)^{q^k} = S_k(x)^{q^k} + x^{q^{2k}} = S_k(x)^{q^k} + x,$$
$$S_{2k}(x) = S_k(x) + S_k(x)^{q^k} = \mathrm{Tr}_{q^{2k}/q}(x) \in \mathbb{F}_q.$$

**Lemma 1.1.** Let $t(z) := z + z^{q^k}$ for $z \in \mathbb{F}_{q^{2k}}$. Then
$$\mathrm{im}(S_k) := \{S_k(x) : x \in \mathbb{F}_{q^{2k}}\} = \{z \in \mathbb{F}_{q^{2k}} : t(z) \in \mathbb{F}_q\},$$
and $|\mathrm{im}(S_k)| = q^{k+1}$.

*Proof.* The $\mathbb{F}_q$-linear map $S_k \colon \mathbb{F}_{q^{2k}} \to \mathbb{F}_{q^{2k}}$ satisfies $S_k(x)^q + S_k(x) = x^{q^k} + x$. Hence $S_k(x) = 0$ if and only if $x \in \mathbb{F}_{q^k}$ and $\mathrm{Tr}_{q^k/q}(x) = S_k(x) = 0$. Therefore $|\ker(S_k)| = q^{k-1}$ and $|\mathrm{im}(S_k)| = q^{2k}/q^{k-1} = q^{k+1}$. For every $z = S_k(x) \in \mathrm{im}(S_k)$, we have $t(z) = S_k(x) + S_k(x)^{q^k} = S_{2k}(x) \in \mathbb{F}_q$. Conversely, $t \colon \mathbb{F}_{q^{2k}} \to \mathbb{F}_{q^k}$ is the surjective trace $\mathrm{Tr}_{q^{2k}/q^k}$ with kernel $\mathbb{F}_{q^k}$ of size $q^k$, so $|\{z \in \mathbb{F}_{q^{2k}} : t(z) \in \mathbb{F}_q\}| = q \cdot q^k = q^{k+1} = |\mathrm{im}(S_k)|$. $\square$

Define $\Phi_{\mathrm{Q3}} \colon \mathrm{im}(S_k) \to \mathrm{im}(S_k)$ by
$$\Phi_{\mathrm{Q3}}(z) := z + (k + 1)\,t(z) + S_k(z) + t(z)\,S_k(z^{q - 1}).$$
Here $t(\Phi_{\mathrm{Q3}}(z)) = t(z) + 0 + S_{2k}(z) + t(z) S_{2k}(z^{q - 1}) \in \mathbb{F}_q$, so $\Phi_{\mathrm{Q3}}$ indeed maps $\mathrm{im}(S_k)$ into $\mathrm{im}(S_k)$. Moreover, for every $c \in \mathbb{F}_q$ and $z \in \mathrm{im}(S_k)$,
$$\Phi_{\mathrm{Q3}}(c z) = c\,\Phi_{\mathrm{Q3}}(z)$$
(for $c = 0$ both sides are $0$; for $c \in \mathbb{F}_q^*$, $(cz)^{q-1} = z^{q-1}$ and $t, S_k$ are $\mathbb{F}_q$-linear).

**Proposition 1.2.** For every $b \in \mathbb{F}_{q^{2k}}$, the map $x \mapsto z := S_k(x)^{q^k}$ is a bijection between $\{x \in \mathbb{F}_{q^{2k}} : g_{n,q}(x) = b\}$ and $\{z \in \mathrm{im}(S_k) : \Phi_{\mathrm{Q3}}(z) = S_k(b)\}$. Consequently, $g_{n,q}$ is a PP of $\mathbb{F}_{q^{2k}}$ if and only if $\Phi_{\mathrm{Q3}}$ is a bijection on $\mathrm{im}(S_k)$.

*Proof.* If $g_{n,q}(x) = b$ and $z := S_k(x)^{q^k}$, then $z \in \mathrm{im}(S_k)$ (since $t(z) = t(S_k(x)) = S_{2k}(x) \in \mathbb{F}_q$), $S_k(x) = z^{q^k} = z + t(z)$, and $g_{n,q}(x) = (z + x) + t(z) + t(z) z^{q-1} = b$, which gives
$$x = b + z + t(z) + t(z) z^{q-1}.$$
Applying $S_k$ to both sides and using $S_k(t(z)) = k\,t(z)$ and $S_k(t(z) z^{q-1}) = t(z) S_k(z^{q-1})$ (as $t(z) \in \mathbb{F}_q$), we obtain
$$z + t(z) = S_k(x) = S_k(b) + S_k(z) + k\,t(z) + t(z) S_k(z^{q-1}),$$
so $\Phi_{\mathrm{Q3}}(z) = S_k(b)$. Conversely, given $z \in \mathrm{im}(S_k)$ with $\Phi_{\mathrm{Q3}}(z) = S_k(b)$, set $x := b + z + t(z) + t(z) z^{q-1}$. Applying $S_k$ yields
$$S_k(x) = S_k(b) + S_k(z) + k\,t(z) + t(z) S_k(z^{q-1}) = \Phi_{\mathrm{Q3}}(z) + \bigl(\Phi_{\mathrm{Q3}}(z) + z + t(z)\bigr) = z + t(z) = z^{q^k},$$
hence $S_k(x)^{q^k} = z^{q^{2k}} = z$, $S_{2k}(x) = z + z^{q^k} = t(z)$, and $g_{n,q}(x) = (z + x) + t(z) + t(z) z^{q-1} = b$. Because $x$ is uniquely determined by $z$ and $b$, this establishes the bijection. Since $S_k \colon \mathbb{F}_{q^{2k}} \to \mathrm{im}(S_k)$ is surjective, $g_{n,q}$ is a PP of $\mathbb{F}_{q^{2k}}$ iff every fiber of $\Phi_{\mathrm{Q3}}$ on $\mathrm{im}(S_k)$ has size $1$. $\square$

**Lemma 1.3.** When $k$ is even, the restriction of $\Phi_{\mathrm{Q3}}$ to $\{z \in \mathrm{im}(S_k) : t(z) = 0\} = \mathbb{F}_{q^k}$ is an involution, and hence a bijection $\mathbb{F}_{q^k} \to \mathbb{F}_{q^k}$.

*Proof.* For $z \in \mathbb{F}_{q^k}$ ($t(z) = 0$), $\Phi_{\mathrm{Q3}}(z) = z + S_k(z) = z + \mathrm{Tr}_{q^k/q}(z) \in \mathbb{F}_{q^k}$. Since $k$ is even, $\mathrm{Tr}_{q^k/q}(c) = k \cdot c = 0$ for all $c \in \mathbb{F}_q$. Thus
$$\Phi_{\mathrm{Q3}}\bigl(\Phi_{\mathrm{Q3}}(z)\bigr) = z + \mathrm{Tr}_{q^k/q}(z) + \mathrm{Tr}_{q^k/q}(z) + \mathrm{Tr}_{q^k/q}\bigl(\mathrm{Tr}_{q^k/q}(z)\bigr) = z. \qquad \square$$

---

## 2. Case $e \equiv 2 \pmod 4$ ($k$ odd): Never a PP

**Theorem 2.1.** If $q > 2$ is even and $e = 2k$ with $k \ge 1$ odd, then $g_{n,q}$ is not a PP of $\mathbb{F}_{q^e}$.

*Proof.* Evaluate $g_{n,q}$ at $0$ and $1 \in \mathbb{F}_{q^{2k}}$. Clearly $g_{n,q}(0) = 0$. Since $S_r(1) = r \cdot 1 \in \mathbb{F}_2$, we have $S_{2k}(1) = 0$ and (as $k$ is odd, so $k + 1$ is even) $S_{k+1}(1) = 0$. Therefore
$$g_{n,q}(1) = S_{k+1}(1)^{q^k} + S_{2k}(1) + S_{2k}(1)\bigl(S_k(1)^{q^k}\bigr)^{q-1} = 0 = g_{n,q}(0),$$
so $g_{n,q}$ is not injective. $\square$

---

## 3. Case $q = 4$ and $4 \mid e$ ($k \ge 2$ even): Always a PP

Let $q = 4$, $\mathbb{F}_4 = \{0, 1, \omega, \omega^2\}$ with $\omega^2 + \omega + 1 = 0$, and $k \ge 2$ be even. Then
$$\Phi_{\mathrm{Q3}}(z) = z + t(z) + S_k(z) + t(z) S_k(z^3) \qquad (z \in \mathrm{im}(S_k)).$$
Define $s(z) := t(\Phi_{\mathrm{Q3}}(z)) = \Phi_{\mathrm{Q3}}(z) + \Phi_{\mathrm{Q3}}(z)^{4^k} \in \mathbb{F}_4$.

**Theorem 3.1.** If $q = 4$ and $4 \mid e$, then $g_{n,q}$ is a PP of $\mathbb{F}_{4^e}$.

*Proof.* By Proposition 1.2, it suffices to show that $\Phi_{\mathrm{Q3}}$ is injective on $\mathrm{im}(S_k)$.

**Step 1: $s(z)$ and separation from $\mathbb{F}_{4^k}$.** For any $z \in \mathrm{im}(S_k)$ with $t(z) = 1$ (so $z^{4^k} = z + 1$), set $A := z^2 + z$. Then $A^{4^k} = (z + 1)^2 + (z + 1) = A$, so $A \in \mathbb{F}_{4^k}$, and
$$\mathrm{Tr}_{4^k/2}(A) = \sum_{j=0}^{2k-1} (z^2 + z)^{2^j} = z + z^{2^{2k}} = z + z^{4^k} = 1.$$
Hence $\mathrm{Tr}_{4/2}(S_k(A)) = \mathrm{Tr}_{4^k/2}(A) = 1$, forcing $S_k(A) \in \{\omega, \omega^2\}$. Because $k$ is even, $S_{2k}(z) = S_k(z + z^{4^k}) = S_k(1) = 0$ and
$$S_{2k}(z^3) = S_k\bigl(z^3 + (z + 1)^3\bigr) = S_k(z^2 + z + 1) = S_k(A) + S_k(1) = S_k(A).$$
Therefore, when $t(z) = 1$,
$$s(z) = t(z) + S_{2k}(z) + t(z) S_{2k}(z^3) = 1 + S_k(A) \in \{\omega, \omega^2\}.$$
By $\mathbb{F}_4$-homogeneity of $\Phi_{\mathrm{Q3}}$ and $t$, for every $z \in \mathrm{im}(S_k)$ with $t := t(z) \in \mathbb{F}_4^*$,
$$s(z) = t\Bigl(1 + S_k\bigl((z/t)^2 + z/t\bigr)\Bigr) \in t\{\omega, \omega^2\}.$$
In particular, $s(z) \ne 0$ whenever $t(z) \ne 0$. Since $\Phi_{\mathrm{Q3}}$ maps $\mathbb{F}_{4^k} = \{t = 0\}$ bijectively onto itself by Lemma 1.3 and maps $\mathrm{im}(S_k) \setminus \mathbb{F}_{4^k}$ into $\{s \ne 0\} = \mathrm{im}(S_k) \setminus \mathbb{F}_{4^k}$, no collision can occur between $\{t = 0\}$ and $\{t \ne 0\}$.

**Step 2: Quartic invariant.** For any $u \in \mathbb{F}_{4^{2k}}$, $S_k(u)^4 + S_k(u) = u^{4^k} + u$. Hence for $z \in \mathrm{im}(S_k)$ with $t(z) = 1$,
$$\Phi_{\mathrm{Q3}}(z)^4 + \Phi_{\mathrm{Q3}}(z) = (z^4 + z) + 0 + (z^{4^k} + z) + \bigl((z^{4^k})^3 + z^3\bigr) = (z^4 + z) + 1 + (z^2 + z + 1) = (z^2 + z)^2.$$
By $\mathbb{F}_4$-homogeneity (using $t^3 = 1$ for $t \in \mathbb{F}_4^*$), for every $z \in \mathrm{im}(S_k)$ with $t = t(z) \in \mathbb{F}_4^*$,
$$\Phi_{\mathrm{Q3}}(z)^4 + \Phi_{\mathrm{Q3}}(z) = t\bigl((z/t)^2 + z/t\bigr)^2 = (z^2 + t z)^2.$$

**Step 3: Injectivity on $\mathrm{im}(S_k) \setminus \mathbb{F}_{4^k}$.** Suppose $\Phi_{\mathrm{Q3}}(z_1) = \Phi_{\mathrm{Q3}}(z_2)$ with $t_1 := t(z_1) \in \mathbb{F}_4^*$ and $t_2 := t(z_2) \in \mathbb{F}_4^*$. Then $s := s(z_1) = s(z_2) \in \mathbb{F}_4^*$, and Step 2 gives $(z_1^2 + t_1 z_1)^2 = (z_2^2 + t_2 z_2)^2$, so
$$A := z_1^2 + t_1 z_1 = z_2^2 + t_2 z_2 \in \mathbb{F}_{4^k}.$$

- *Subcase $t_1 = t_2 =: t$:* Then $(z_1 + z_2)(z_1 + z_2 + t) = 0$, so $z_2 \in \{z_1, z_1 + t\}$. Since $\Phi_{\mathrm{Q3}}$ has coefficients in $\mathbb{F}_2$ (viewing $t(z) = z + z^{4^k}$) and $z_1 + t = z_1^{4^k}$, we have $\Phi_{\mathrm{Q3}}(z_1 + t) = \Phi_{\mathrm{Q3}}(z_1^{4^k}) = \Phi_{\mathrm{Q3}}(z_1)^{4^k} = \Phi_{\mathrm{Q3}}(z_1) + s \ne \Phi_{\mathrm{Q3}}(z_1)$. Thus $z_2 = z_1$.

- *Subcase $t_1 \ne t_2$:* Since $s \in t_1\{\omega, \omega^2\} \cap t_2\{\omega, \omega^2\}$, the elements $t_1, t_2, s$ are pairwise distinct and fill $\mathbb{F}_4^*$. By $\mathbb{F}_4$-homogeneity (scaling $z_1, z_2$ by $t_1^{-1}$) and, if needed, applying the Frobenius automorphism $x \mapsto x^2$ (which commutes with $\Phi_{\mathrm{Q3}}$ and swaps $\omega \leftrightarrow \omega^2$), we may assume without loss of generality that
$$t_1 = 1, \qquad t_2 = \omega, \qquad s = \omega^2.$$
From Step 1, $1 + S_k(A) = s(z_1) = \omega^2$, so $S_k(A) = \omega$. Set $W := \omega^2 z_1 + \omega z_2$. Then
$$W^{4^k} = \omega^2(z_1 + 1) + \omega(z_2 + \omega) = W + (\omega^2 + \omega^2) = W,$$
so $W \in \mathbb{F}_{4^k}$, and
$$W^2 + \omega^2 W = \omega z_1^2 + \omega^2 z_2^2 + \omega z_1 + z_2 = \omega(z_1^2 + z_1) + \omega^2(z_2^2 + \omega z_2) = (\omega + \omega^2) A = A.$$
Using $z_2 = \omega^2 W + \omega z_1$, we have $z_1 + z_2 = \omega^2 W + \omega^2 z_1$ and
$$z_1^3 + \omega z_2^3 = z_1^3 + \omega(\omega^2 W + \omega z_1)^3 = \omega W^3 + W^2 z_1 + \omega^2 W z_1^2 + \omega^2 z_1^3.$$
Substituting $W^2 = \omega^2 W + A$, $z_1^2 = z_1 + A$, and $z_1^3 = (A + 1) z_1 + A$ yields
$$z_1^3 + \omega z_2^3 = \bigl((\omega^2 + \omega A) W + A\bigr) + (\omega^2 W + A) z_1 + (\omega^2 W z_1 + \omega^2 A W) + \bigl(\omega^2(A + 1) z_1 + \omega^2 A\bigr)$$
$$= A W + \omega^2 W + \omega A z_1 + \omega^2 z_1 + \omega A.$$
Hence $(z_1 + z_2) + (z_1^3 + \omega z_2^3) = A W + \omega A z_1 + \omega A$, and the collision $\Phi_{\mathrm{Q3}}(z_1) + \Phi_{\mathrm{Q3}}(z_2) = 0$ becomes
$$\omega^2 W + \omega^2 z_1 + \omega^2 + S_k(A W) + \omega S_k(A z_1) + \omega S_k(A) = 0.$$
Now $z_1^4 = (z_1 + A)^2 = z_1 + A + A^2$ and $W^4 = (\omega^2 W + A)^2 = W + \omega A + A^2$, so by induction for every $i \ge 0$,
$$z_1^{4^i} = z_1 + \sum_{j=0}^{i-1} \bigl(A^{4^j} + A^{2 \cdot 4^j}\bigr), \qquad W^{4^i} = W + \sum_{j=0}^{i-1} \bigl(\omega A^{4^j} + A^{2 \cdot 4^j}\bigr).$$
Multiplying by $A^{4^i}$, summing over $0 \le i \le k - 1$, and using $S_k(A) = \omega$, we get
$$S_k(A W) + \omega S_k(A z_1) = \omega W + \omega^2 z_1 + \sum_{0 \le j < i < k} A^{4^i}\bigl((\omega + \omega) A^{4^j} + (1 + \omega) A^{2 \cdot 4^j}\bigr) = \omega W + \omega^2 z_1 + \omega^2 Q(A),$$
where $Q(A) := \sum_{0 \le j < i < k} A^{4^i + 2 \cdot 4^j}$. Substituting this and $\omega S_k(A) = \omega^2$ into the collision equation cancels $z_1$ and $\omega^2$ completely, leaving
$$(\omega^2 + \omega) W + \omega^2 Q(A) = 0 \implies W = \omega^2 Q(A).$$
On the one hand, $W^2 + \omega^2 W = A$ gives $\omega(Q(A)^2 + Q(A)) = A$, so
$$Q(A)^2 + Q(A) + \omega^2 A = 0.$$
On the other hand, writing $X_j := A^{4^j}$ ($0 \le j \le k - 1$, so $X_j^4 = X_{j+1}$ for $0 \le j \le k - 2$ and $\sum_{j=0}^{k-1} X_j = S_k(A) = \omega$), we have
$$Q(A)^2 = \sum_{0 \le j < i < k} X_i^2 X_{j+1} = \sum_{i=1}^{k-1} X_i^3 + \sum_{1 \le r < i < k} X_i^2 X_r.$$
Expanding $1 = \omega \cdot \omega^2 = \bigl(\sum_{r=0}^{k-1} X_r\bigr)\bigl(\sum_{i=0}^{k-1} X_i^2\bigr)$ into diagonal, $r < i$, and $r > i$ terms gives
$$1 = \sum_{i=0}^{k-1} X_i^3 + \sum_{0 \le r < i < k} X_i^2 X_r + \sum_{0 \le j < i < k} X_i X_j^2 = X_0^3 + X_0 \sum_{i=1}^{k-1} X_i^2 + Q(A)^2 + Q(A).$$
Since $\sum_{i=1}^{k-1} X_i^2 = S_k(A)^2 + X_0^2 = \omega^2 + X_0^2$, we have $X_0^3 + X_0(\omega^2 + X_0^2) = \omega^2 X_0 = \omega^2 A$, and hence
$$Q(A)^2 + Q(A) + \omega^2 A = 1,$$
contradicting $Q(A)^2 + Q(A) + \omega^2 A = 0$. Therefore no cross-$t$ collision exists, and $\Phi_{\mathrm{Q3}}$ is a bijection on $\mathrm{im}(S_k)$. $\square$

---

## 4. Case $q \ge 8$ and $4 \mid e$ with $e \ge 8$ ($k \ge 4$ even): Never a PP

**Theorem 4.1.** If $q = 2^m \ge 8$ ($m \ge 3$) and $e = 2k$ with $k \ge 4$ even, then $g_{n,q}$ is not a PP of $\mathbb{F}_{q^e}$.

*Proof.* By Proposition 1.2 and Lemma 1.3, $\Phi_{\mathrm{Q3}}$ maps $\mathbb{F}_{q^k} = \{t = 0\}$ bijectively onto itself. Hence, if $\Phi_{\mathrm{Q3}}$ were a bijection on $\mathrm{im}(S_k)$, then every $z \in \mathrm{im}(S_k)$ with $t(z) = 1$ would satisfy $s(z) := t(\Phi_{\mathrm{Q3}}(z)) \ne 0$.

Fix $\alpha \in \mathbb{F}_{q^{2k}}$ with $\alpha^{q^k} + \alpha = 1$, so $\{z \in \mathrm{im}(S_k) : t(z) = 1\} = \{u + \alpha : u \in \mathbb{F}_{q^k}\}$. For $z = u + \alpha$ ($u \in \mathbb{F}_{q^k}$), since $k$ is even we have $S_{2k}(z) = S_k(1) = 0$, and therefore
$$s(u + \alpha) = 1 + S_{2k}\bigl((u + \alpha)^{q-1}\bigr) = 1 + \mathrm{Tr}_{q^k/q}\bigl(f(u)\bigr),$$
where
$$f(u) := (u + \alpha)^{q-1} + (u + \alpha + 1)^{q-1}.$$
Because $\alpha^{q^k} = \alpha + 1$, raising the coefficients of $f$ to the $q^k$-th power swaps the two summands and fixes $f$, so $f \in \mathbb{F}_{q^k}[u]$. Since $q$ is a power of $2$, $\binom{q-1}{j} \equiv 1 \pmod 2$ for every $0 \le j \le q - 1$, giving
$$f(u) = \sum_{j=0}^{q-1} \bigl(\alpha^{q-1-j} + (\alpha + 1)^{q-1-j}\bigr) u^j = u^{q-2} + u^{q-3} + \sum_{j=0}^{q-4} \bigl(\alpha^{q-1-j} + (\alpha + 1)^{q-1-j}\bigr) u^j.$$

For each $\lambda \in \mathbb{F}_q^*$, let $\mu := \lambda^{q/2} \in \mathbb{F}_q^*$ be its unique square root ($\mu^2 = \lambda$), and define
$$h_\lambda(u) := \lambda f(u) + \bigl(\mu u^{q/2 - 1}\bigr)^2 + \mu u^{q/2 - 1} \in \mathbb{F}_{q^k}[u].$$
The term $\mu^2 u^{q-2} = \lambda u^{q-2}$ cancels the leading term of $\lambda f(u)$, and since $q \ge 8$ we have $q/2 - 1 < q - 3$, so $h_\lambda$ has **odd** degree $d = q - 3 \ge 5$ (with leading term $\lambda u^{q-3}$). Moreover, $\mathrm{Tr}_{q^k/2}(y^2 + y) = 0$ for all $y \in \mathbb{F}_{q^k}$, so $\mathrm{Tr}_{q^k/2}(\lambda f(u)) = \mathrm{Tr}_{q^k/2}(h_\lambda(u))$ for all $u \in \mathbb{F}_{q^k}$. Since $\gcd(d, 2) = 1$, the Carlitz–Uchiyama bound (Lidl–Niederreiter, *Finite Fields*, Theorem 5.38) yields
$$\left|\sum_{u \in \mathbb{F}_{q^k}} (-1)^{\mathrm{Tr}_{q^k/2}(\lambda f(u))}\right| = \left|\sum_{u \in \mathbb{F}_{q^k}} (-1)^{\mathrm{Tr}_{q^k/2}(h_\lambda(u))}\right| \le (d - 1)\,q^{k/2} = (q - 4)\,q^{k/2}.$$

Let $N_0 := \#\{u \in \mathbb{F}_{q^k} : s(u + \alpha) = 0\} = \#\{u \in \mathbb{F}_{q^k} : \mathrm{Tr}_{q^k/q}(f(u)) = 1\}$. By additive character orthogonality over $\mathbb{F}_q$,
$$N_0 = \frac{1}{q} \sum_{u \in \mathbb{F}_{q^k}} \sum_{\lambda \in \mathbb{F}_q} (-1)^{\mathrm{Tr}_{q/2}(\lambda(\mathrm{Tr}_{q^k/q}(f(u)) + 1))} = q^{k-1} + \frac{1}{q} \sum_{\lambda \in \mathbb{F}_q^*} (-1)^{\mathrm{Tr}_{q/2}(\lambda)} \sum_{u \in \mathbb{F}_{q^k}} (-1)^{\mathrm{Tr}_{q^k/2}(\lambda f(u))}.$$
By the triangle inequality and $k \ge 4$ (so $q^{k/2} \ge q^2$ and $q^{k/2 - 1} \ge q$),
$$N_0 \ge q^{k-1} - \frac{q - 1}{q}(q - 4)\,q^{k/2} = q^{k/2}\!\left(q^{k/2 - 1} - \frac{q^2 - 5q + 4}{q}\right) \ge q^{k/2} \cdot \frac{5q - 4}{q} \ge q(5q - 4) > 0.$$
Thus there exists $u \in \mathbb{F}_{q^k}$ with $s(u + \alpha) = 0$, so $\Phi_{\mathrm{Q3}}(u + \alpha) \in \mathbb{F}_{q^k}$ collides with $\Phi_{\mathrm{Q3}}|_{\mathbb{F}_{q^k}}$, and $g_{n,q}$ is not a PP of $\mathbb{F}_{q^{2k}}$. $\square$

---

## 5. Case $e = 4$ and $q = 2^m \ge 8$ ($m \ge 3$): Never a PP

It remains to show that for every $m \ge 3$ ($q = 2^m \ge 8$), $g_{n,q}$ is not a PP of $\mathbb{F}_{q^4}$ ($k = 2$).

### 5.1 Reduction to an $s$-Free Moment on the Trace-1 Hyperplane $H_1$

Let $H_1 := \{w \in \mathbb{F}_{q^2} : \mathrm{Tr}_{q^2/2}(w) = 1\} \subset \mathbb{F}_{q^2}^*$, and define in $\mathbb{F}_2[w, w^{-1}]$:
$$T(w) := \sum_{r=0}^{m-1} w^{2^r} = \mathrm{Tr}_{q/2}(w), \qquad L(w) := \sum_{r=1}^{m-1} w^{2^r} = T(w) + w, \qquad S(w) := w^{-1} L(w) = 1 + \frac{T(w)}{w},$$
$$N(w) := w^q + S(w) + \frac{w + 1}{w^q}.$$

**Proposition 5.1.** Let $q = 2^m \ge 8$ ($m \ge 3$). If $g_{n,q}$ is a PP of $\mathbb{F}_{q^4}$, then
$$\sum_{w \in H_1} N(w)^{3(q - 1)} = 0.$$

*Proof.* Assume $g_{n,q}$ is a PP of $\mathbb{F}_{q^4}$; by Proposition 1.2, $\Phi := \Phi_{\mathrm{Q3}}$ is a bijection on $\mathrm{im}(S_2) = \{z \in \mathbb{F}_{q^4} : t(z) := z + z^{q^2} \in \mathbb{F}_q\}$. Fix $\alpha \in \mathbb{F}_{q^4}$ with $\alpha^{q^2} + \alpha = 1$, so $A_1 := \{z \in \mathrm{im}(S_2) : t(z) = 1\} = \alpha + \mathbb{F}_{q^2}$. By Lemma 1.3, $\Phi$ maps $\mathbb{F}_{q^2}$ bijectively onto itself, so for every $z \in A_1$ we have $s(z) := \Phi(z) + \Phi(z)^{q^2} \in \mathbb{F}_q^*$.

Define $\tilde{\Phi} \colon A_1 \to A_1$ by $\tilde{\Phi}(z) := \Phi(z)/s(z)$. Clearly $\tilde{\Phi}(z)^{q^2} + \tilde{\Phi}(z) = s(z)/s(z) = 1$, so $\tilde{\Phi}(z) \in A_1$. If $\tilde{\Phi}(z_1) = \tilde{\Phi}(z_2)$ for $z_1, z_2 \in A_1$, then with $c := s(z_2)/s(z_1) \in \mathbb{F}_q^*$, $\mathbb{F}_q$-homogeneity gives $\Phi(c z_1) = c \Phi(z_1) = \Phi(z_2)$; injectivity of $\Phi$ forces $c z_1 = z_2$, whence $c = t(c z_1) = t(z_2) = 1$ and $z_1 = z_2$. Thus $\tilde{\Phi}$ is a bijection $A_1 \to A_1$.

For every $z \in A_1$, we have $z^{q^2} = z + 1$. Because $\Phi$ has coefficients in $\mathbb{F}_2$, $\Phi(z + 1) = \Phi(z^{q^2}) = \Phi(z)^{q^2} = \Phi(z) + s(z)$, and $s(z + 1) = s(z)^{q^2} = s(z)$. Hence $\tilde{\Phi}(z + 1) = \tilde{\Phi}(z) + 1$. The Artin–Schreier map $\pi(z) := z^2 + z$ satisfies $\mathrm{Tr}_{q^2/2}(\pi(z)) = z + z^{q^2} = t(z)$, so $\pi$ maps $A_1$ $2$-to-$1$ onto $H_1$ with fibers $\{z, z + 1\}$. Since $\tilde{\Phi}$ commutes with $z \mapsto z + 1$, it descends to a bijection $\Psi \colon H_1 \to H_1$ given on $w = z^2 + z \in H_1$ by
$$\Psi(w) = \tilde{\Phi}(z)^2 + \tilde{\Phi}(z) = \frac{\Phi(z)\bigl(\Phi(z) + s(z)\bigr)}{s(z)^2} = \frac{\Phi(z)\,\Phi(z + 1)}{s(z)^2}.$$

We now compute $\Phi(z)\,\Phi(z + 1)$ in terms of $w = z^2 + z$. Write $y := z^q$, so $y^q = z^{q^2} = z + 1$, $w^q = y^2 + y$, and $y + z = z^q + z = \sum_{r=0}^{m-1} (z^2 + z)^{2^r} = T(w)$. On $A_1$ ($k = 2$, $t(z) = 1$),
$$\Phi(z) = z + 1 + (z + y) + \left(\frac{y}{z} + \frac{z + 1}{y}\right) = (y + 1) + \frac{y}{z} + \frac{z + 1}{y},$$
$$\Phi(z + 1) = \Phi(z)^{q^2} = y + \frac{y + 1}{z + 1} + \frac{z}{y + 1}.$$
Expanding the product into six symmetric pieces over $\mathbb{F}_2$:
1. $(y + 1) y = y^2 + y = w^q$;
2. $(y + 1)\dfrac{y + 1}{z + 1} + y \dfrac{y}{z} = \dfrac{z(y^2 + 1) + (z + 1)y^2}{z(z + 1)} = \dfrac{y^2 + z}{w}$;
3. $(y + 1)\dfrac{z}{y + 1} + y \dfrac{z + 1}{y} = z + (z + 1) = 1$;
4. $\dfrac{y}{z}\cdot \dfrac{y + 1}{z + 1} = \dfrac{y^2 + y}{w} = \dfrac{w^q}{w}$;
5. $\dfrac{z + 1}{y}\cdot \dfrac{z}{y + 1} = \dfrac{w}{w^q}$;
6. $\dfrac{y}{z}\cdot\dfrac{z}{y + 1} + \dfrac{z + 1}{y}\cdot\dfrac{y + 1}{z + 1} = \dfrac{y}{y + 1} + \dfrac{y + 1}{y} = \dfrac{1}{w^q}$.

Summing (2)+(4) gives $\frac{y + z}{w} = \frac{T(w)}{w}$, summing (5)+(6) gives $\frac{w + 1}{w^q}$, and summing (1)+(3) gives $w^q + 1$. Thus
$$\Phi(z)\,\Phi(z + 1) = w^q + 1 + \frac{T(w)}{w} + \frac{w + 1}{w^q} = N(w).$$

Because $s(z) \in \mathbb{F}_q^*$ satisfies $s(z)^{q - 1} = 1$, raising $\Psi(w) = N(w)/s(z)^2$ to the power $3(q - 1)$ cancels $s(z)$ completely: $\Psi(w)^{3(q-1)} = N(w)^{3(q-1)}$. Since $\Psi$ is a bijection on $H_1$,
$$\sum_{w \in H_1} N(w)^{3(q - 1)} = \sum_{w \in H_1} \Psi(w)^{3(q - 1)} = \sum_{w \in H_1} w^{3(q - 1)}.$$
Finally, $\mathrm{Tr}_{q^2/2}(w) \in \{0, 1\}$ is the indicator function of $H_1$ on $\mathbb{F}_{q^2}^*$, so for any integer $E$,
$$\sum_{w \in H_1} w^E = \sum_{w \in \mathbb{F}_{q^2}^*} \mathrm{Tr}_{q^2/2}(w)\, w^E = \sum_{j=0}^{2m-1} \sum_{w \in \mathbb{F}_{q^2}^*} w^{E + 2^j}.$$
For $E = 3(q - 1)$ and $0 \le j \le 2m - 1$, since $q \ge 8$ we have
$$0 < 3(q - 1) + 2^j \le 3q - 3 + \frac{q^2}{2} = (q^2 - 1) - \frac{q^2 - 6q + 4}{2} < q^2 - 1$$
(as $q^2 - 6q + 4 = q(q - 6) + 4 \ge 20 > 0$ for all $q \ge 8$).
Hence $(q^2 - 1) \nmid (3(q - 1) + 2^j)$ for every $j$, so every inner sum over $\mathbb{F}_{q^2}^*$ vanishes and $\sum_{w \in H_1} w^{3(q - 1)} = 0$. $\square$

---

### 5.2 Elementary Binary Lemmas

For any nonnegative integer $n$, let $I(n) := \{i \ge 0 : \text{bit } i \text{ of } n \text{ is } 1\}$ be its binary support and $w_2(n) := |I(n)|$ its binary weight. Write $u \preceq v$ if $I(u) \subseteq I(v)$, and $u \& v = 0$ if $I(u) \cap I(v) = \emptyset$.

**Lemma 5.2 (Support, Binary Weight, and Unique Matching for $L(w)^A$).** Let $A \ge 0$ be an integer, and recall $L(w) = \sum_{r=1}^{m-1} w^{2^r} \in \mathbb{F}_2[w]$.
1. Every monomial $w^N$ with $[w^N] L(w)^A = 1$ satisfies $N$ even, $2A \le N \le A \frac{q}{2}$, and $w_2(N) \le w_2(A)$.
2. Suppose $w_2(N) = w_2(A) =: r$, and write $I(A) = \{i_1 < i_2 < \dots < i_r\}$ and $J(N) := I(N) = \{n_1 < n_2 < \dots < n_r\}$.
   - If $[w^N] L(w)^A = 1$, then $i_p + 1 \le n_p \le i_p + m - 1$ for every $1 \le p \le r$.
   - Conversely, if $i_p + 1 \le n_p \le i_p + m - 1$ for every $1 \le p \le r$ and $n_p \le i_{p+1}$ for every $1 \le p \le r - 1$, then $[w^N] L(w)^A = 1$.

*Proof.* In characteristic $2$, $L(w)^A = \prod_{i \in I(A)} L(w)^{2^i} = \prod_{i \in I(A)} \bigl(\sum_{t = i + 1}^{i + m - 1} w^{2^t}\bigr)$. Each expanded term has exponent $N = \sum_{i \in I(A)} 2^{t_i}$ with $i + 1 \le t_i \le i + m - 1$, which is even, lies in $[2A, A \frac{q}{2}]$, and satisfies $w_2(N) \le |I(A)| = w_2(A)$ (with equality iff the exponents $t_i$ are pairwise distinct, i.e., $i \mapsto t_i$ is a bijection $I(A) \to J(N)$).

When $w_2(N) = w_2(A) = r$, $[w^N] L(w)^A$ is the parity of the number of bijections $\pi \colon I(A) \to J(N)$ satisfying $i + 1 \le \pi(i) \le i + m - 1$ for all $i \in I(A)$. If any such bijection $\pi$ exists, then for each $1 \le p \le r$, the $p$ elements $\pi(i_1), \dots, \pi(i_p)$ are at most $i_p + m - 1$, so at least $p$ elements of $J(N)$ are $\le i_p + m - 1$, giving $n_p \le i_p + m - 1$; symmetrically, the $r - p + 1$ elements $\pi(i_p), \dots, \pi(i_r)$ are at least $i_p + 1$, giving $n_p \ge i_p + 1$. Conversely, if $i_p + 1 \le n_p \le i_p + m - 1$ for all $p$ and $n_p \le i_{p+1}$ for all $p < r$, then any valid bijection must satisfy $\pi(i_1) = n_1$ (since $i_q + 1 \ge i_2 + 1 > n_1$ for all $q \ge 2$), and inductively $\pi(i_p) = n_p$ for all $p$; hence there is a unique valid bijection and $[w^N] L(w)^A = 1$. $\square$

**Lemma 5.3 (Disjoint Subtraction Popcount Bounds).** Let $X, k \ge 0$ be integers with $X \& k = 0$.
1. If $X \ge k$, then $w_2(X - k) \ge w_2(X)$. Equality holds iff for every $i \in I(k)$, $i + 1 \in I(X) \cup I(k)$; in that case, $I(X - k)$ is obtained from $I(X)$ by replacing the bit $t + 1 \in I(X)$ with $s$ for each maximal contiguous block $\{s, s + 1, \dots, t\} \subseteq I(k)$.
2. If $u \ge 0$ and $X \ge k + u$, then $w_2(X - k - u) \ge w_2(X) - w_2(u)$, with equality iff $w_2(X - k) = w_2(X)$ and $I(u) \subseteq I(X - k)$.
3. In particular, if $1 \notin I(X) \cup I(k)$ and $X \ge k + 2$, then $w_2(X - k - 2) \ge w_2(X)$.

*Proof.*
(1) Put $R := X - k$, so $R + k = X$, and let $C$ be the set of bit positions emitting a carry in the binary addition $R + k$. Then $w_2(R) + w_2(k) = w_2(X) + |C|$. For every $i \in I(k)$, bit $i$ of $k$ is $1$ while bit $i$ of $X$ is $0$ (as $X \& k = 0$), so position $i$ must emit a carry: $I(k) \subseteq C$. Hence $|C| \ge w_2(k)$ and $w_2(R) \ge w_2(X)$, with equality iff $C = I(k)$. Now $C = I(k)$ iff for each maximal contiguous block $\{s, \dots, t\} \subseteq I(k)$, the carry entering $t + 1 \notin I(k)$ does not propagate further, which holds iff $t + 1 \in I(X)$ (and then bit $t + 1$ of $R$ is $0$, bit $s$ of $R$ is $1$, and bits $s + 1, \dots, t$ of $R$ are $0$).
(2) Put $S := X - k$. Then $(S - u) + u = S$ gives $w_2(S - u) + w_2(u) = w_2(S) + \mathrm{carries}(S - u, u) \ge w_2(S) \ge w_2(X)$ by (1), with equality iff $w_2(S) = w_2(X)$ and $\mathrm{carries}(S - u, u) = 0$ (i.e., $I(u) \subseteq I(S)$).
(3) Apply (2) with $u = 2$ ($I(u) = \{1\}$, $w_2(u) = 1$). By (1), whenever $w_2(X - k) = w_2(X)$ we have $I(X - k) \subseteq I(X) \cup I(k)$, so $1 \notin I(X - k)$; hence strict inequality holds in (2), giving $w_2(X - k - 2) \ge w_2(X)$. $\square$

**Lemma 5.4 (Solutions of $a + 2c = S$ with $a \& c = 0$ and $4 \mid c$).** Let $a, c \ge 0$ be integers with $a \& c = 0$ and $4 \mid c$ (i.e., $0, 1 \notin I(c)$).
1. If $a + 2c = 2^t - 3$ ($t \ge 2$), then $c = 0$ and $a = 2^t - 3$.
2. If $a + 2c = 2^t - 4$ ($t \ge 2$) and $4 \mid a$, then $c = 0$ and $a = 2^t - 4$.
3. If $a + 2c = 2^M$ ($M \ge 3$) and $c > 0$, then $c = 2^u$ and $a = 2^M - 2^{u+1}$ for some $2 \le u \le M - 1$.
4. If $a + 2c = 2^M + 2^L - 3$ (resp. $a + 2c = 2^M + 2^L - 4$ with $4 \mid a$) where $2 \le L < M$ and $c > 0$, then $c = 2^u$ and $a = (2^M - 2^{u+1}) + (2^L - 3)$ (resp. $a = (2^M - 2^{u+1}) + (2^L - 4)$) for some $L \le u \le M - 1$.

*Proof.*
(1)–(2) Suppose $c > 0$ and let $u \ge 2$ be the lowest set bit of $c$. Then $2^{u+1} \le 2c < 2^t$, so $2 \le u \le t - 2$. Because $u \in I(c)$ and $a \& c = 0$, bit $u$ of $a$ is $0$; because $u$ is the lowest set bit of $c$, all bits $\le u$ of $2c$ are $0$. Hence no carry enters bit $u$ in $a + 2c$, making bit $u$ of $a + 2c$ equal to $0$. Yet bit $u$ of both $2^t - 3 = 1 + \sum_{j=2}^{t-1} 2^j$ and $2^t - 4 = \sum_{j=2}^{t-1} 2^j$ is $1$ for $2 \le u \le t - 2$, a contradiction. Thus $c = 0$.

(3) Let $u \ge 2$ be the lowest set bit of $c$ ($u \le M - 1$). In $a + 2c = 2^M$, all bits $< u$ of $a$ and $2c$ must be $0$, and bit $u$ of both $a$ (disjoint from $c$) and $2c$ is $0$. If $u = M - 1$, then $2c = 2^M$ and $a = 0$. If $u \le M - 2$, then bit $u + 1$ of $2c$ is $1$; to obtain $0$ at bit $u + 1$ of $2^M$, bit $u + 1$ of $a$ must be $1$ (emitting a carry into $u + 2$). Inductively, for every $j \in \{u + 2, \dots, M - 1\}$, bit $j$ receives carry $1$ and must output $0$ with carry $1$, forcing $a_j + c_{j-1} = 1$ (where $a_j, c_j \in \{0, 1\}$ denote the $j$-th binary digits). If $c$ had another set bit above $u$, let $v > u$ be the smallest such bit ($v \le M - 1$). Since $u + 1 \in I(a)$ we have $u + 1 \notin I(c)$, so $v \ge u + 2$, and by minimality $c_{v-1} = 0$, while $v \in I(c) \implies a_v = 0$, contradicting $a_v + c_{v-1} = 1$. Hence $c = 2^u$ and $a = 2^M - 2^{u+1}$.

(4) Let $u \ge 2$ be the lowest set bit of $c$ ($2^{u+1} \le 2c < 2^M + 2^L \implies u \le M - 1$, since $u \ge M$ would give $2c \ge 2^{M+1} > 2^M + 2^L$). As in (1), bit $u$ of $a + 2c$ is $0$. Because bits $2, \dots, L - 1$ of $2^M + 2^L - 3$ and $2^M + 2^L - 4$ are $1$, we must have $u \ge L$. Thus all bits $< L$ of $2c$ are $0$, so those bits of the RHS come purely from $a$: specifically $2^L - 3 \preceq a$ (resp. $2^L - 4 \preceq a$). Setting $a' := a - (2^L - 3)$ (resp. $a - (2^L - 4)$) gives $a' + 2c = 2^M$ with $a' \& c = 0$, and (3) yields $c = 2^u$ and $a' = 2^M - 2^{u+1}$. $\square$

---

### 5.3 Four-Piece Decomposition of $\sum_{w \in H_1} N(w)^{3(q-1)}$

**Theorem 5.5.** For every $m \ge 3$ ($q = 2^m \ge 8$),
$$\sum_{w \in H_1} N(w)^{3(q - 1)} = 1.$$

*Proof.* Work in the ring $\mathcal{R} := \mathbb{F}_2[w]/(w^{q^2 - 1} - 1)$ and write $x := w^q$, so $x^q = w$ and $w^{q^2 - 1} = 1$. Since $\sum_{w \in \mathbb{F}_{q^2}^*} w^E = 1$ iff $(q^2 - 1) \mid E$, we have
$$\sum_{w \in H_1} N(w)^{3(q - 1)} = \sum_{w \in \mathbb{F}_{q^2}^*} \mathrm{Tr}_{q^2/2}(w)\, N(w)^{q - 3} \bigl(N(w)^q\bigr)^2 = [w^0]_{\mathcal{R}}\Bigl(\mathrm{Tr}_{q^2/2}(w)\, N(w)^{q - 3} \bigl(N(w)^q\bigr)^2\Bigr).$$
(Note $3(q - 1) = (q - 3) + 2q$.) Now
$$N(w) = w^{-1} L(w) + x + (w + 1) x^{-1}, \qquad \bigl(N(w)^q\bigr)^2 = S(x)^2 + w^2 + w^{-2}(x^2 + 1).$$
Since $q - 3 = (q - 1) - 2 = \sum_{i \in \{0, 2, 3, \dots, m - 1\}} 2^i$, Lucas's theorem gives
$$N(w)^{q - 3} = \sum_{(a, b, c) \in \mathcal{P}} w^{-a} L(w)^a (w + 1)^c x^{b - c},$$
where $\mathcal{P}$ is the set of triples $(a, b, c)$ of pairwise bitwise disjoint nonnegative integers with $a + b + c = q - 3$ (in particular, $1 \notin I(a) \cup I(b) \cup I(c)$).

Next, write $\mathrm{Tr}_{q^2/2}(w) = T(w) + T(x) = L(w) + (T(x) + w)$, and simplify $M_{1,\mathrm{rem}} := (T(x) + w) S(x)^2$ in $\mathcal{R}$. Set $A_x := \sum_{t=2}^{m-1} x^{2^t}$, so $T(x) + w = x + x^2 + A_x + x^q$, $S(x)^2 = x^{-2}(A_x + x^q)$, and $A_x^2 = \sum_{t=3}^{m} x^{2^t} = A_x + x^4 + x^q$. Therefore, in $\mathcal{R}$,
$$(T(x) + w) S(x)^2 = x^{-2}\bigl(A_x^2 + x^{2q} + (x + x^2)(A_x + x^q)\bigr) = x^{-2}\bigl(A_x + x^4 + x^q + x^{2q} + (x + x^2)(A_x + x^q)\bigr).$$
Using $x^q = w$ on the term $x^{2q - 2} = w x^{q - 2}$ and cancelling $x^{-2} \cdot x^4$ against the $t = 2$ term of $x^{-2} A_x$, we obtain the exact identity in $\mathcal{R}$:
$$M_{1,\mathrm{rem}} = (T(x) + w) S(x)^2 = \sum_{t=3}^{m} x^{2^t - 2} + \sum_{t=2}^{m} x^{2^t - 1} + \sum_{t=2}^{m} x^{2^t} + w x^{q - 2}.$$

Accordingly, $\mathrm{Tr}_{q^2/2}(w) (N(w)^q)^2 N(w)^{q - 3}$ splits into four pieces, whose $[w^0]_{\mathcal{R}}$ coefficients we denote $\Sigma_{\mathrm{I}}, \Sigma_{\mathrm{II}}, \Sigma_{\mathrm{III}}, \Sigma_{\mathrm{IV}}$:
- **Piece I:** $S(x)^2 L(w) N(w)^{q-3} = \sum_{(a,b,c) \in \mathcal{P}} S(x)^2 w^{-a} L(w)^{a+1} (w+1)^c x^{b-c}$;
- **Piece II:** $M_{1,\mathrm{rem}} N(w)^{q-3} = \sum_{(a,b,c) \in \mathcal{P}} M_{1,\mathrm{rem}} w^{-a} L(w)^a (w+1)^c x^{b-c}$;
- **Piece III:** $\mathrm{Tr}_{q^2/2}(w) w^2 N(w)^{q-3}$;
- **Piece IV:** $\mathrm{Tr}_{q^2/2}(w) w^{-2}(x^2 + 1) N(w)^{q-3}$.

For each piece, let $A := a + 1$ in Piece I and $A := a$ in Pieces II–IV. Expanding $(w + 1)^c = \sum_{k \preceq c} w^k$ and each multiplier into monomials $w^\alpha x^\beta$, a tuple $((a, b, c), (\alpha, \beta), k)$ contributes $[w^N] L(w)^A$ to $[w^0]_{\mathcal{R}}$, where $N$ is the unique integer in $[2A, A \frac{q}{2}]$ (if any) satisfying
$$N \equiv a - \alpha - k - q D \pmod{q^2 - 1}, \qquad D := b - c + \beta.$$
(Uniqueness holds because $A \le q - 2 \implies A \frac{q}{2} \le \frac{q^2}{2} - q < q^2 - 1$.) Write
$$N = q(\lambda q - D) + (a - k - \alpha - \lambda), \qquad \lambda \in \mathbb{Z},$$
and let $N = q K + r$ with $K \ge 0$ and $0 \le r < q$ be its base-$q$ decomposition, so $w_2(N) = w_2(K) + w_2(r)$. By Lemma 5.2(1), every contributing tuple ("hit") satisfies:
1. $2A \le N \le A \frac{q}{2}$ (in particular $K \le A/2$);
2. $r$ is even;
3. $w_2(K) + w_2(r) \le w_2(A)$.

In all four pieces, $-2 \le \alpha \le \frac{q}{2} + 2$, $0 \le \beta \le q$, $0 \le k \le c$, and $-(q - 3) \le b - c \le q - 3$, so $-(q - 3) \le D \le 2q - 3 - a - 2c$ (and $a + b + c = q - 3 \implies q - D = a + 2c + 3 - \beta$). Using $N = \lambda(q^2 - 1) - q D + a - k - \alpha$:
- If $\lambda \le -1$, then $N \le -(q^2 - 1) + q(q - 3) + (q - 3) + 2 = -2q < 0$, impossible.
- If $\lambda \ge 2$, then
  $$N \ge 2(q^2 - 1) - q(2q - 3 - a - 2c) + a - c - \Bigl(\frac{q}{2} + 2\Bigr) = a q + (2q - 1) c + \frac{5q}{2} + a - 4 > (a + 1)\frac{q}{2} \ge A \frac{q}{2}$$
  (since $\frac{a q}{2} + (2q - 1)c + 2q + a - 4 \ge 12 > 0$ for all $a, c \ge 0$ and $q \ge 8$), impossible.

Thus **$\lambda \in \{0, 1\}$ in all four pieces**.

We now classify every hit in each of the four pieces.

---

### 5.4 Exact Hit Classification for Pieces IV, I, II, and III

#### Piece IV ($\Sigma_{\mathrm{IV}} = 0$)
In $\mathrm{Tr}_{q^2/2}(w)(x^2 + 1) = \sum_{j=0}^{m-1} w^{2^j}(x^2 + 1) + \sum_{s=0}^{m-1} x^{2^s}(x^2 + 1)$, the term $x^2 \cdot x^2 = x^4$ ($s = 1$) cancels the term $x^4 \cdot 1$ ($s = 2$, present since $m \ge 3$). Multiplying by $w^{-2}$, the surviving monomials $(\alpha, \beta)$ are:
- *Type IV-A:* $\alpha = 2^j - 2$ ($0 \le j \le m - 1$), $\beta = \delta \in \{0, 2\}$;
- *Type IV-B:* $\alpha = -2$, $\beta \in \mathcal{B}_{\mathrm{IV}} := \{1, 2, 3\} \cup \{2^s : 3 \le s \le m - 1\} \cup \{2^s + 2 : 2 \le s \le m - 1\}$. Note that no element of $\mathcal{B}_{\mathrm{IV}}$ is $\equiv 4$ or $5 \pmod 8$.

Here $A = a$.

- **Type IV-A, $\lambda = 1$:** Here $q - D = a + 2c + 3 - \delta \ge a + 2c + 1$, $k \le c$, and $\alpha = 2^j - 2 \le \frac{q}{2} - 2$. Hence
  $$N = q(q - D) + a - k - \alpha - 1 \ge q(a + 2c + 1) + a - c - \Bigl(\frac{q}{2} - 2\Bigr) - 1 = a q + (2q - 1) c + \frac{q}{2} + a + 1 > a \frac{q}{2}$$
  for all $a, c \ge 0$ (including $a = 0$, where $N \ge \frac{q}{2} + 1 > 0$). No hits.

- **Type IV-A, $\lambda = 0$:** $N = q(-D) + (a - k - 2^j + 2)$ with $D = b - c + \delta$.
  - *$j \ge 2$:* Since $1 \notin I(a) \cup I(k)$, we have $(a + 2) \& k = 0$ and $w_2(a + 2) = w_2(a) + 1$. Note $a - k - 2^j + 2 \ge -(q - 3) - (q/2 - 2) > -2q$, so at most a borrow of $b_0 \in \{0, 1, 2\}$ occurs: $r = b_0 q + a + 2 - k - 2^j$. By Lemma 5.3(2) with $X = b_0 q + a + 2$ (noting $X \& k = 0$ and $w_2(X) = w_2(a) + 1 + \mathbf{1}_{b_0 > 0}$) and $u = 2^j$:
    - without borrow ($b_0 = 0$), $w_2(r) \ge w_2(a + 2) - 1 = w_2(a)$, forcing $K = 0$ and $N = r \le a + 2 - 4 = a - 2 < 2a$, impossible;
    - with borrow ($b_0 \in \{1, 2\}$), $w_2(r) \ge w_2(b_0 q + a + 2) - 1 = w_2(a) + 1 > w_2(a)$, impossible.
  - *$j = 1$ ($\alpha = 0$):* $r = a - k$ (or $q + a - k$ on borrow). By Lemma 5.3(1), borrow gives $w_2(r) \ge w_2(a) + 1 > w_2(a)$, while no borrow gives $w_2(r) \ge w_2(a)$, forcing $K = -D = 0$ and $N = a - k \le a$, hence $a = 0, k = 0$. Then $b + c = q - 3$ is odd, so $D = b - c + \delta$ is odd, contradicting $D = 0$.
  - *$j = 0$ ($\alpha = -1$):* $r \equiv a - k + 1 \pmod q$ is even, so either $0 \in I(a)$ or $0 \in I(k)$.
    - If $0 \in I(a)$ ($0 \notin I(k)$): since $1 \notin I(a) \cup I(k)$, $(a + 1) \& k = 0$ and $w_2(a + 1) = w_2(a)$. Borrow gives $w_2((q + a + 1) - k) \ge w_2(a) + 1$; no borrow gives $w_2((a + 1) - k) \ge w_2(a)$, forcing $K = -D = 0$ and $2a \le N \le a + 1 \implies a = 1, k = 0$. Then $4 \mid c$, $b + c = q - 4$, so $b - c = q - 4 - 2c \equiv 4 \pmod 8$, hence $D = b - c + \delta \equiv 4$ or $6 \not\equiv 0 \pmod 8$, impossible.
    - If $0 \in I(k)$ ($0 \notin I(a)$): $a \& (k - 1) = 0$. Borrow gives $w_2((q + a) - (k - 1)) \ge w_2(a) + 1$; no borrow gives $w_2(a - (k - 1)) \ge w_2(a)$, forcing $K = -D = 0$ and $2a \le N \le a \implies a = 0, k = 1$. Then $c \equiv 1 \pmod 4$, $b + c = q - 3$, so $b - c = q - 3 - 2c \equiv 3 \pmod 8$, hence $D = b - c + \delta \equiv 3$ or $5 \not\equiv 0 \pmod 8$, impossible.

- **Type IV-B, $\lambda = 0$:** $r \equiv a + 2 - k \pmod q$. Since $(a + 2) \& k = 0$ and $w_2(a + 2) = w_2(a) + 1$, Lemma 5.3(1) gives $w_2(r) \ge w_2(a) + 1$ (no borrow) or $\ge w_2(a) + 2$ (borrow), both $> w_2(a)$. No hits.

- **Type IV-B, $\lambda = 1$:** $N = q(q - D) + (a - k + 1)$ with $q - D = a + 2c + 3 - \beta$. Identically to Type IV-A ($j = 0, \lambda = 0$), parity of $r$ and Lemma 5.3(1) rule out borrows and force $K = q - D = 0$ with either:
  - $a = 1, k = 0, 4 \mid c \implies \beta = 2c + 4 \equiv 4 \pmod 8$, impossible since $4 \bmod 8 \notin \mathcal{B}_{\mathrm{IV}}$; or
  - $a = 0, k = 1, c \equiv 1 \pmod 4 \implies \beta = 2c + 3 \equiv 5 \pmod 8$, impossible since $5 \bmod 8 \notin \mathcal{B}_{\mathrm{IV}}$.

Thus Piece IV has **zero hits**, so $\Sigma_{\mathrm{IV}} = 0$.

---

#### Piece I ($\Sigma_{\mathrm{I}} \equiv m - 1 \pmod 2$)
Here $A = a + 1 \ge 1$, $\alpha = 0$, and $\beta = 2^t - 2$ ($2 \le t \le m$). Note that $w_2(A) = w_2(a)$ if $0 \in I(a)$, and $w_2(A) = w_2(a) + 1$ if $0 \notin I(a)$.

- **$\lambda = 1$:** $N = q(q - D) + (a - k - 1)$ with $q - D = a + 2c + 5 - 2^t$. Since $r$ is even, either $0 \in I(k)$ or $0 \in I(a)$.
  - *If $0 \notin I(a)$ and $0 \in I(k)$:* Here $w_2(A) = w_2(a) + 1$, $4 \mid a$, $c \equiv 1 \pmod 4$, and $(k + 1) \& a = 0$ (since $1 \notin I(a) \cup I(k)$).
    - Without borrow, $w_2(a - (k + 1)) \ge w_2(a) = w_2(A) - 1$, forcing $w_2(K) \le 1$; since $K = a + 2c + 5 - 2^t$ is odd, $K = 1$, i.e. $a + 2c + 4 = 2^t$.
    - With borrow, $w_2((q + a) - (k + 1)) \ge w_2(a) + 1 = w_2(A)$, forcing $K = q - D - 1 = 0$, again $a + 2c + 4 = 2^t$.
    In both cases, $4 \mid a$ and $c \equiv 1 \pmod 4$ give $a + 2c + 4 \equiv 2$ or $6 \pmod 8$, contradicting $2^t \equiv 0$ or $4 \pmod 8$ ($t \ge 2$).
  - *If $0 \in I(a)$ ($0 \notin I(k)$, $4 \mid c$):* Here $w_2(A) = w_2(a)$ and $(a - 1) \& k = 0$.
    - With borrow ($a - 1 < k$), $w_2((q + a - 1) - k) \ge w_2(q + a - 1) = w_2(a) = w_2(A)$, forcing $q - D - 1 = 0$, i.e. $a + 2c + 4 = 2^t$, impossible since the LHS is odd and $t \ge 2$.
    - Without borrow ($a - 1 \ge k$), $w_2((a - 1) - k) \ge w_2(a - 1) = w_2(a) - 1$, forcing $w_2(K) \le 1$. Note $K = 0 \implies N = r < a < 2A$, impossible. Since $K = a + 2c + 5 - 2^t$ is even, $K = 2^s$ ($s \ge 1$), so $a + 2c + 5 = 2^t + 2^s$. Modulo $4$, $a \equiv 1 \pmod 4$ and $4 \mid c$ give $2^t + 2^s \equiv 2 \pmod 4$, forcing $s = 1$ ($K = 2$) and $a + 2c = 2^t - 3$. By Lemma 5.4(1), $c = 0$, $k = 0$, $a = 2^t - 3$, $b = q - 2^t$. Then $A = 2^t - 2$ ($I(A) = \{1, 2, \dots, t - 1\}$) and $N = 2q + 2^t - 4$ ($J(N) = \{2, 3, \dots, t - 1, m + 1\}$). For $t = 2$, $i_1 = 1$ and $n_1 = m + 1 > i_1 + m - 1$ fails Lemma 5.2(2). For every $3 \le t \le m$, $i_p + 1 \le n_p \le i_p + m - 1$ and $n_p = i_{p+1}$ ($p \le t - 2$) hold, so Lemma 5.2(2) gives a unique hit for each $3 \le t \le m$: **$m - 2$ hits**.

- **$\lambda = 0$:** $N = q(-D) + (a - k)$ with $-D = c - b - (2^t - 2)$. Parity of $r$ forces $0 \notin I(a)$ and $0 \notin I(k)$, so $4 \mid a$, $w_2(A) = w_2(a) + 1$, and $b + c = q - 3 - a$ is odd, making $-D$ odd.
  - Without borrow ($a \ge k$), $w_2(a - k) \ge w_2(a) = w_2(A) - 1$, so $w_2(-D) \le 1$; as $-D$ is odd, $-D = 1$.
  - With borrow ($a < k$), $w_2((q + a) - k) \ge w_2(a) + 1 = w_2(A)$, forcing $K = -D - 1 = 0$, so again $-D = 1$.
  Thus $c - b = 2^t - 1 \equiv 3 \pmod 4$. Note that $2^t - 1 = c - b \le c \le q - 3 < q - 1$, so $2 \le t \le m - 1$. Since $1 \notin I(b) \cup I(c)$, this forces $4 \mid c$ and $b \equiv 1 \pmod 4$. Adding $a + b + c = q - 3$ yields $a + 2c = q + 2^t - 4$ ($c > 0$ since $c \ge 2^t - 1$). By Lemma 5.4(3)–(4) (with $M = m$ and $2 \le L = t < M$), we get $c = 2^u$, $a = (q - 2^{u+1}) + (2^t - 4)$, $b = 2^u - 2^t + 1$ for $2 \le t \le u \le m - 1$, and the only submasks of $c$ are $k \in \{0, 2^u\}$.
  - *If $2 \le t \le u \le m - 2$:* Then $a \ge 2^{u+1} > 2^u$, so neither $k = 0$ nor $k = 2^u$ borrows, $K = 1$, $I(A) = \{0\} \cup \{2, \dots, t - 1\} \cup \{u + 1, \dots, m - 1\}$. At $k = 0$, $J(N) = \{2, \dots, t - 1\} \cup \{u + 1, \dots, m - 1, m\}$; at $k = 2^u$, subtracting $2^u$ shifts bit $u + 1$ down to $u$, giving $J(N) = \{2, \dots, t - 1\} \cup \{u, u + 2, \dots, m - 1, m\}$. In both cases, Lemma 5.2(2) confirms an upper-triangular unique matching ($0 \to 2 \to \dots \to t - 1 \to u + 1$ [resp. $u$], then $u + 1 \to u + 2 \to \dots \to m - 1 \to m$, and if $t = 2$, $0 \to u + 1$ [resp. $u$]). Both $k = 0$ and $k = 2^u$ hit and **cancel mod 2**.
  - *If $3 \le t \le u = m - 1$:* Here $a = 2^t - 4$, $c = q/2$, $I(A) = \{0, 2, \dots, t - 1\}$. At $k = 0$ ($K = 1$), $J(N) = \{2, \dots, t - 1, m\}$; at $k = q/2$ (borrow, $K = 0$, $r = q/2 + 2^t - 4$), $J(N) = \{2, \dots, t - 1, m - 1\}$. Both satisfy Lemma 5.2(2) ($0 \to 2 \to \dots \to t - 1 \to m$ [resp. $m - 1$], using $t \ge 3$ for $m \le (t - 1) + m - 1$ and $t \le m - 1$ for $(t - 1) + 1 \le m - 1$). Both hit and **cancel mod 2**.
  - *If $t = 2, u = m - 1$:* Here $(a, b, c) = (0, q/2 - 3, q/2)$, $A = 1$, $I(A) = \{0\}$. At $k = 0$, $N = q > A q/2$ fails; at $k = q/2$, $N = q/2$ ($J(N) = \{m - 1\}$) gives a unique hit: **$1$ unpaired hit**.

Summing Piece I mod $2$: $\Sigma_{\mathrm{I}} \equiv (m - 2) + 1 = m - 1 \pmod 2$.

---

#### Piece II ($\Sigma_{\mathrm{II}} \equiv 1 + \binom{m-2}{2} \pmod 2$)
Here $A = a$, and the monomials of $M_{1,\mathrm{rem}}$ are:
- *Type II-1:* $\alpha = 0, \beta = 2^t - 2$ ($3 \le t \le m$);
- *Type II-2:* $\alpha = 0, \beta = 2^t - 1$ ($2 \le t \le m$);
- *Type II-3:* $\alpha = 0, \beta = 2^t$ ($2 \le t \le m$);
- *Type II-4:* $\alpha = 1, \beta = q - 2$.

- **Type II-4 ($\alpha = 1, \beta = q - 2$):**
  - If $\lambda = 0$, then $D = b - c + q - 2 \ge -(q - 3) + q - 2 = 1$, so $-D < 0$ and $N < 0$.
  - If $\lambda = 1$, then $r \equiv a - k - 2 \pmod q$. Since $1 \notin I(a) \cup I(k)$, Lemma 5.3(3) gives $w_2(a - k - 2) \ge w_2(a)$ (no borrow) and $w_2((q + a) - k - 2) \ge w_2(q + a) = w_2(a) + 1$ (borrow). Thus no borrow and $K = 0$, forcing $N = a - k - 2 < 2a$, impossible for all $a \ge 0$.
  Hence Type II-4 has **zero hits**.

- **Types II-1, II-2, II-3 ($\alpha = 0$), $\lambda = 0$:** $N = q(-D) + (a - k)$. By Lemma 5.3(1), borrow gives $w_2(q + a - k) \ge w_2(a) + 1 > w_2(a)$, while no borrow gives $w_2(a - k) \ge w_2(a)$, forcing $K = -D = 0$ and $2a \le N = a - k \le a$, hence $a = 0, k = 0, N = 0$. Now $D = b - c + \beta = 0$ and $b + c = q - 3$ give $2b + \beta = q - 3$. Since $q - 3$ is odd, $\beta$ must be odd (Type II-2: $\beta = 2^t - 1$, $2 \le t \le m$), giving $b = q/2 - 1 - 2^{t-1}$. Because $1 \notin I(b)$ while $1 \in I(q/2 - 1)$, we must have $t - 1 = 1$, i.e. $t = 2$ ($\beta = 3$), yielding **exactly $1$ hit**: $(a, b, c) = (0, q/2 - 3, q/2), k = 0$.

- **Types II-1, II-2, II-3 ($\alpha = 0$), $\lambda = 1$:** $N = q(q - D) + (a - k - 1)$ with $q - D = a + 2c + 3 - \beta$. Parity of $r$ requires either $0 \in I(k)$ or $0 \in I(a)$.
  - *If $0 \notin I(a)$ and $0 \in I(k)$:* Then $(k + 1) \& a = 0$, so Lemma 5.3(1) gives $w_2(r) \ge w_2(a)$ (no borrow) or $\ge w_2(a) + 1$ (borrow), forcing $K = 0$ and $N = a - k - 1 < a \le 2a$, impossible.
  - *If $0 \in I(a)$ ($0 \notin I(k)$, $4 \mid c$, $a \equiv 1 \pmod 4$):*
    - With borrow ($a - 1 < k$), $w_2((q + a - 1) - k) \ge w_2(a)$, forcing $K = q - D - 1 = 0$, i.e. $\beta = a + 2c + 2$ (odd $\implies$ Type II-2: $\beta = 2^t - 1 \implies a + 2c = 2^t - 3$). By Lemma 5.4(1), $c = 0$, contradicting $k > a - 1 \ge 0$.
    - Without borrow ($a - 1 \ge k$), $w_2((a - 1) - k) \ge w_2(a) - 1$, forcing $w_2(K) \le 1$. Since $K = 0 \implies N < a < 2a$, we must have $K = 2^s$ ($s \ge 0$), where $2^s = K \le a/2 < q/2$ gives $0 \le s \le m - 2$, and
      $$a + 2c + 3 - \beta = 2^s.$$
      We evaluate each type:
      1. *Type II-1 ($\beta = 2^t - 2, 3 \le t \le m$):* $a + 2c + 5 = 2^t + 2^s$. Modulo $4$, $s = 1$ ($K = 2$), so $a + 2c = 2^t - 3$; by Lemma 5.4(1), $c = k = 0$ and $a = 2^t - 3$. Here $I(a) = \{0, 2, \dots, t - 1\}$ and $J(N) = \{2, \dots, t - 1, m + 1\}$, which by Lemma 5.2(2) hits for every $3 \le t \le m$ (**$m - 2$ hits**).
      2. *Type II-2 ($\beta = 2^t - 1, 2 \le t \le m$):* $a + 2c + 4 = 2^t + 2^s$. Modulo $2$, $s = 0$ ($K = 1$), so $a + 2c = 2^t - 3$; by Lemma 5.4(1), $c = k = 0$ and $a = 2^t - 3$. Here $J(N) = \{2, \dots, t - 1, m\}$; $t = 2$ fails Lemma 5.2(2) ($m > 0 + m - 1$), while every $3 \le t \le m$ hits (**$m - 2$ hits**, cancelling Type II-1 mod $2$).
      3. *Type II-3 ($\beta = 2^t, 2 \le t \le m$):* $a + 2c + 3 = 2^t + 2^s$. Modulo $4$, $a \equiv 1 \pmod 4$ and $4 \mid c$ force $2^s \equiv 0 \pmod 4$, so $2 \le s \le m - 2$.
         - *Subcase $c = 0$ ($k = 0$):* $a = 2^t + 2^s - 3$. Since $a \le q - 3$ and $s \ge 2$, we have $t \le m - 1$. If $t \le s$, the top bit of $I(a)$ is $s$, whereas the top bit of $J(N)$ is $m + s > s + m - 1$, failing Lemma 5.2(2). Thus $2 \le s < t \le m - 1$. For every such $(s, t)$, $I(a) = \{0, 2, \dots, s - 1, t\}$ and $J(N) = \{2, \dots, s - 1, t, m + s\}$ (for $s = 2$: $I(a) = \{0, t\}$, $J(N) = \{t, m + 2\}$); since $t + 1 \le m + s \le t + m - 1$ (as $s < t < m$), Lemma 5.2(2) gives a unique hit for each pair $2 \le s < t \le m - 1$: **$\binom{m - 2}{2}$ hits**.
         - *Subcase $c > 0$:* If $t = s$, then $a + 2c = 2^{t+1} - 3$ forces $c = 0$ by Lemma 5.4(1). Thus $t \ne s$; set $M := \max(t, s)$ and $L := \min(t, s)$ ($2 \le L < M \le m$). By Lemma 5.4(4), $c = 2^u$ and $a = (2^M - 2^{u+1}) + (2^L - 3)$ for $L \le u \le M - 1$. If $u = M - 1$, then $a = 2^L - 3$ has top bit $\le L - 1$ while $J(N)$ has top bit $m + s \ge m + L > (L - 1) + m - 1$, failing Lemma 5.2(2). Thus $L \le u \le M - 2$, so $a \ge 2^{u+1} > 2^u = c$ (neither $k = 0$ nor $k = 2^u$ borrows) and the top bit of $I(a)$ is $M - 1$; Lemma 5.2(2) then requires $m + s \le (M - 1) + m - 1$, i.e. $s \le M - 2$, which forces $s = L$, $t = M$, and $2 \le L \le u \le M - 2 \le m - 2$. For every such $(L, u, M)$, $I(a) = \{0, 2, \dots, L - 1\} \cup \{u + 1, \dots, M - 1\}$, while $J(N)$ is $\{2, \dots, L - 1\} \cup \{u + 1, \dots, M - 1, m + L\}$ at $k = 0$ and $\{2, \dots, L - 1\} \cup \{u, u + 2, \dots, M - 1, m + L\}$ at $k = 2^u$. By Lemma 5.2(2), both $k = 0$ and $k = 2^u$ hit and **cancel mod $2$**.

Summing Piece II mod $2$: $\Sigma_{\mathrm{II}} \equiv 1 + 2(m - 2) + \binom{m - 2}{2} \equiv 1 + \binom{m - 2}{2} \pmod 2$.

---

#### Piece III ($\Sigma_{\mathrm{III}} \equiv \binom{m - 3}{2} \pmod 2$)
Here $A = a$, and the monomials of $\mathrm{Tr}_{q^2/2}(w) w^2$ are:
- *Type III-A:* $\alpha = 2^j + 2$ ($0 \le j \le m - 1$), $\beta = 0$;
- *Type III-B:* $\alpha = 2$, $\beta = 2^s$ ($0 \le s \le m - 1$).

- **Type III-A, $\lambda = 1$:** Here $\beta = 0$, $q - D = a + 2c + 3$, $k \le c$, and $\alpha = 2^j + 2 \le \frac{q}{2} + 2$. Hence
  $$N = q(q - D) + a - k - \alpha - 1 \ge q(a + 2c + 3) + a - c - \Bigl(\frac{q}{2} + 2\Bigr) - 1 = a q + (2q - 1) c + \frac{5q}{2} + a - 3 > a \frac{q}{2}$$
  for all $a, c \ge 0$ and $q \ge 8$ (since $\frac{a q}{2} + (2q - 1)c + \frac{5q}{2} + a - 3 \ge 17 > 0$). No hits.

- **Type III-A, $\lambda = 0$:** $N = q(c - b) + (a - k - 2^j - 2)$. Since $k \le q - 3$ and $2^j + 2 \le q/2 + 2$, we have $a - k - 2^j - 2 > -2q$, so any borrow $b_0 \in \{0, 1, 2\}$ gives $K = c - b - b_0$ and $r = b_0 q + a - k - 2^j - 2$. First observe that a borrow of $b_0 = 2$ is impossible for all $0 \le j \le m - 1$: because $w_2(2q + a) = w_2(a) + 1$ and $(2q + a) \& k = 0$ with $1 \notin I(2q + a) \cup I(k)$, Lemma 5.3(2)–(3) yields $w_2(r) \ge w_2(a)$ in every parity case (using $2q + a - k - 2 - 2^j$ for $j \ge 2$, $2q + a - k - 4$ for $j = 1$, $2q + a - (k - 1) - 4$ for $j = 0 \in I(k)$, and $(2q + a - 1) - k - 2$ for $j = 0 \in I(a)$), forcing $K = c - b - 2 = 0$, i.e. $c - b = 2$. Together with $a + b + c = q - 3$ this gives $2c = q - 1 - a$; on the other hand, $b_0 = 2$ requires $c \ge k > q + a - 2^j - 2 \ge \frac{q}{2} + a - 2$, so $\frac{q}{2} + a - 2 < \frac{q - 1 - a}{2} \implies 3a < 3 \implies a = 0$, contradicting $2c = q - 1$. Thus $b_0 \in \{0, 1\}$.
  - *$j = 1$ ($\alpha = 4$):* Parity of $r$ forces $0 \notin I(a)$ ($4 \mid a$) and $0 \notin I(k)$, so $c - b$ is odd. By Lemma 5.3(2) with $u = 4$, borrow ($b_0 = 1$) gives $w_2(q + a - k - 4) \ge w_2(a)$ (forcing $c - b - 1 = 0$, i.e. $c - b = 1$) and no borrow ($b_0 = 0$) gives $w_2(a - k - 4) \ge w_2(a) - 1$ (forcing $w_2(c - b) \le 1$, so again $c - b = 1$). Adding $a + b + c = q - 3$ gives $a + 2c = q - 2$, so $c$ is odd; writing $c = 1 + c'$ ($4 \mid c'$) gives $a + 2c' = q - 4$, which by Lemma 5.4(2) forces $c' = 0$, hence $(a, b, c) = (q - 4, 0, 1)$, $k = 0$ (no borrow: $a - 4 = q - 8 \ge 0$), $N = 2q - 8$, $I(a) = \{2, \dots, m - 1\}$, $J(N) = \{3, \dots, m - 1, m\}$: **exactly $1$ hit** (by Lemma 5.2(2)).
  - *$j \ge 2$ ($\alpha = 2^j + 2$):* Again parity forces $4 \mid a$, $0 \notin I(k)$, and $c - b$ odd. By Lemma 5.3(3) and (2) (subtracting $2^j$ from $a - k - 2$ or $q + a - k - 2$), borrow ($b_0 = 1$) gives $w_2(r) \ge w_2(a)$ (forcing $c - b = 1$, hence $a = q - 4, c = 1, k = 0$, where $a - 2^j - 2 = q - 6 - 2^j < 0$ occurs only for $m = 3, j = 2$, giving $r = 6$ with $w_2(6) = 2 > w_2(4) = 1$, impossible); no borrow ($b_0 = 0$) gives $w_2(r) \ge w_2(a) - 1$, forcing $c - b = 1$, hence again $a = q - 4, c = 1, k = 0$ and $r = q - 6 - 2^j \ge 0$. Since $j \ge 2$, $r \equiv 2 \pmod 4$, so $1 \in J(N)$ and $n_1 \le 1 < i_1 + 1 = 3$, failing Lemma 5.2(2). No hits.
  - *$j = 0$ ($\alpha = 3$):* Parity of $r$ forces either $0 \in I(k)$ or $0 \in I(a)$.
    - *If $0 \in I(k)$ ($0 \notin I(a)$, $4 \mid a$):* Write $a - k - 3 = a - (k - 1) - 4$. Identically to $j = 1$, Lemma 5.3(2) with $u = 4$ forces $c - b = 1$, hence $(a, b, c) = (q - 4, 0, 1)$ and $k = 1$, giving $N = 2q - 8$ and **exactly $1$ hit** (which **cancels the $j = 1$ hit** mod $2$).
    - *If $0 \in I(a)$ ($0 \notin I(k)$, $4 \mid c$, $a \equiv 1 \pmod 4$):* Write $a - k - 3 = (a - 1) - k - 2$. Here $c - b$ is even. Since $1 \notin I(a - 1) \cup I(k)$, Lemma 5.3(3) gives: on borrow, $w_2((q + a - 1) - k - 2) \ge w_2(q + a - 1) = w_2(a)$, forcing $c - b = 1$, impossible (even); without borrow, $w_2((a - 1) - k - 2) \ge w_2(a - 1) = w_2(a) - 1$, forcing $w_2(K) \le 1$. As $K = 0 \implies N < a < 2a$, we have $K = c - b = 2^s$ ($1 \le s \le m - 2$, since $K \le a/2 < q/2$). Adding $a + b + c = q - 3$ gives $a + 2c = q + 2^s - 3$, and mod $4$ forces $s \ge 2$ (and $c > 0$ since $c \ge 2^s$). By Lemma 5.4(4), $c = 2^u$ and $a = (q - 2^{u+1}) + (2^s - 3)$ for $s \le u \le m - 1$.
      - If $s = 2$: $a = (q - 2^{u+1}) + 1$. Since $a - 3 \ge 0$, $u \le m - 2$, so $a - 3 = (q - 2^{u+2}) + \sum_{i=1}^{u} 2^i$ has $w_2(a - 3) = w_2(a) + u - 2 > w_2(a) - 1$ at $k = 0$, while at $k = 2^u$, $w_2(a - 3 - 2^u) = w_2(a) + u - 3 \le w_2(a) - 1 \iff u = 2$. Since $u \le m - 2$, this occurs iff $m \ge 4$, giving $(a, b, c) = (q - 7, 0, 4)$, $k = 4$, $K = 4$, $I(a) = \{0, 3, \dots, m - 1\}$, $J(N) = \{1, 4, \dots, m - 1, m + 2\}$, which satisfies Lemma 5.2(2) ($m + 2 \le 2m - 2$ for $m \ge 4$): **$1$ hit if $m \ge 4$ ($0$ if $m = 3$)**.
      - If $s \ge 3$: if $u = m - 1$, $a = 2^s - 3$ has top bit $s - 1$ while $J(N)$ has top bit $m + s > (s - 1) + m - 1$, failing Lemma 5.2(2). Thus $3 \le s \le u \le m - 2$, so $a \ge 2^{u+1} > 2^u = c$, bit $2 \in I(a)$, and $a - 3 = (q - 2^{u+1}) + (2^s - 6)$ has $I(a - 3) = \{1, 3, \dots, s - 1, u + 1, \dots, m - 1\}$. Both $k = 0$ and $k = 2^u$ (shifting $u + 1 \to u$) satisfy Lemma 5.2(2) (as $s \le m - 2$) and **cancel mod $2$**.

- **Type III-B ($\alpha = 2, \beta = 2^s, 0 \le s \le m - 1$):**
  - *$\lambda = 0$:* $r \equiv a - k - 2 \pmod q$. By Lemma 5.3(3), borrow gives $w_2(r) \ge w_2(a) + 1$ and no borrow gives $w_2(r) \ge w_2(a)$, forcing $K = 0$ and $N = a - k - 2 < 2a$, impossible.
  - *$\lambda = 1$:* $N = q(q - D) + (a - k - 3)$ with $q - D = a + 2c + 3 - 2^s$. Parity forces either $0 \in I(k)$ or $0 \in I(a)$.
    - *If $0 \in I(k)$ ($0 \notin I(a)$, $4 \mid a$, $c = 1 + c'$ with $4 \mid c'$):* Write $a - k - 3 = a - (k - 1) - 4$.
      - With borrow, Lemma 5.3(2) gives $w_2(r) \ge w_2(a)$, forcing $K = q - D - 1 = 0$, i.e. $a + 2c' = 2^s - 4$ ($s \ge 2$). By Lemma 5.4(2), $c' = 0$, $c = k = 1$, $a = 2^s - 4$; then $a - k - 3 = 2^s - 8 < 0$ requires $s = 2$ ($a = 0$), which gives $r = q - 4 > 0$ (contradicting $N = 0$).
      - Without borrow, $w_2(r) \ge w_2(a) - 1$, forcing $w_2(K) \le 1$. Note $s = 0$ gives $K = a + 2c + 2 > a/2$, impossible; thus $s \ge 1$, so $K = a + 2c + 3 - 2^s$ is odd, forcing $K = 1$, i.e. $a + 2c' = 2^s - 4$. By Lemma 5.4(2), $c' = 0$, $c = k = 1$, $a = 2^s - 4$, $b = q - 2^s$; no borrow ($a - 4 \ge 0$) requires $3 \le s \le m - 1$. For every $3 \le s \le m - 1$, $I(a) = \{2, \dots, s - 1\}$ and $J(N) = \{3, \dots, s - 1, m\}$ satisfy Lemma 5.2(2): **$m - 3$ hits**.
    - *If $0 \in I(a)$ ($0 \notin I(k)$, $4 \mid c$, $a \equiv 1 \pmod 4$):* Write $a - k - 3 = (a - 1) - k - 2$.
      - With borrow, Lemma 5.3(3) gives $w_2(r) \ge w_2(a)$, forcing $q - D - 1 = 0$, i.e. $a + 2c + 2 = 2^s$, impossible since the LHS is odd and $\ge 3$.
      - Without borrow, Lemma 5.3(3) gives $w_2(r) \ge w_2(a) - 1$, forcing $w_2(K) \le 1$. Here $K = 0 \implies N < a < 2a$, while $s \in \{0, 1\} \implies K = a + 2c + 3 - 2^s \ge a + 1 > a/2$, impossible. Thus $s \ge 2$, $K = 2^v$ ($1 \le v \le m - 2$ since $K \le a/2 < q/2$), and $a + 2c + 3 = 2^s + 2^v$; mod $4$ forces $2 \le v \le m - 2$.
        - *Subcase $c = 0$ ($k = 0$):* $a = 2^s + 2^v - 3$. If $v \ge s$, the top bit of $I(a)$ is $v$ while $J(N)$ has top bit $m + v > v + m - 1$, failing Lemma 5.2(2). Thus $2 \le v < s \le m - 1$. If $v = 2$, $a = 2^s + 1$ ($w_2(a) = 2$) and $r = 2^s - 2$ has $w_2(r) = s - 1 \ge 2 > w_2(a) - 1$, impossible. For every $3 \le v < s \le m - 1$, $I(a) = \{0, 2, \dots, v - 1, s\}$ and $J(N) = \{1, 3, \dots, v - 1, s, m + v\}$ satisfy Lemma 5.2(2) ($s + 1 \le m + v \le s + m - 1$): **$\binom{m - 3}{2}$ hits**.
        - *Subcase $c > 0$:* By Lemma 5.4(1), $s \ne v$. Put $M := \max(s, v)$, $L := \min(s, v)$ ($2 \le L < M \le m - 1$). By Lemma 5.4(4), $c = 2^u$ and $a = (2^M - 2^{u+1}) + (2^L - 3)$ for $L \le u \le M - 1$. As in Piece II, $u = M - 1$ fails Lemma 5.2(2) ($m + v \ge m + L > (L - 1) + m - 1$), so $L \le u \le M - 2$ and Lemma 5.2(2) on the top bit $M - 1$ of $I(a)$ forces $v \le M - 2$, hence $v = L$, $s = M$, $2 \le v \le u \le s - 2 \le m - 3$.
          - If $v = 2$: identically to Type III-A ($s = 2$), $k = 0$ fails $w_2(r) \le w_2(a) - 1$, while $k = 2^u$ succeeds iff $u = 2$ (which requires $4 \le s \le m - 1$), giving $(a, b, c) = (2^s - 7, q - 2^s, 4)$, $k = 4$, $K = 4$, $I(a) = \{0, 3, \dots, s - 1\}$, $J(N) = \{1, 4, \dots, s - 1, m + 2\}$, satisfying Lemma 5.2(2): **$m - 4$ hits if $m \ge 4$ ($0$ if $m = 3$)**.
          - If $v \ge 3$: identically to Type III-A ($s \ge 3$), both $k = 0$ and $k = 2^u$ hit by Lemma 5.2(2) and **cancel mod $2$**.

Summing Piece III mod $2$: for $m = 3$, $\Sigma_{\mathrm{III}} \equiv 0$; for $m \ge 4$, the $c = 4$ hits total $1 + (m - 4) = m - 3$, cancelling the $m - 3$ hits with $c = 1$, leaving
$$\Sigma_{\mathrm{III}} \equiv \binom{m - 3}{2} + (m - 3) + (m - 3) \equiv \binom{m - 3}{2} \pmod 2 \qquad (\forall\, m \ge 3).$$

---

### 5.5 Completion of the Proof

Summing all four pieces modulo $2$ for every $m \ge 3$:
$$\sum_{w \in H_1} N(w)^{3(q - 1)} = \Sigma_{\mathrm{I}} + \Sigma_{\mathrm{II}} + \Sigma_{\mathrm{III}} + \Sigma_{\mathrm{IV}}$$
$$\equiv (m - 1) + \left(1 + \binom{m - 2}{2}\right) + \binom{m - 3}{2} + 0 = \binom{m - 1}{2} + \binom{m - 3}{2} + 2$$
$$= m^2 - 5m + 9 \equiv m(m - 1) + 1 \equiv 1 \pmod 2.$$
This proves Theorem 5.5. Combining Theorem 5.5 with Proposition 5.1 proves that $g_{n,q}$ is not a PP of $\mathbb{F}_{q^4}$ for any $q = 2^m \ge 8$.

Combining Theorems 2.1, 3.1, 4.1, and Proposition 5.1 + Theorem 5.5 completes the proof of the Main Theorem in all regimes. $\blacksquare$

---

## 6. Independent Computational Verification

The standalone exact-arithmetic script `verify.py` (zero floats, zero true-division `/`, pure integer and $\mathbb{F}_2$-polynomial arithmetic) verifies:
1. Direct exhaustive PP / non-PP tests of $g_{n,q}$ on $\mathbb{F}_{q^e}$ across all regimes: non-PP with $g_{n,q}(1) = 0 = g_{n,q}(0)$ for $(q, e) \in \{(4, 2), (4, 6), (8, 2), (16, 2)\}$; PP for $(4, 4)$ ($256$ elements) and $(4, 8)$ ($65536$ elements); non-PP for $(8, 4)$ ($4096$ elements) and $(16, 4)$ ($65536$ elements).
2. Exact verification of Theorem 3.1's key identities ($s(z) \in t(z)\{\omega, \omega^2\}$, $\Phi_{\mathrm{Q3}}(z)^4 + \Phi_{\mathrm{Q3}}(z) = (z^2 + tz)^2$, and $Q(A)^2 + Q(A) + \omega^2 A = 1$) for $(4, 4)$ and $(4, 8)$.
3. Exact verification of Theorem 4.1's Carlitz–Uchiyama zero-count $N_0 \ge q(5q - 4)$ and explicit collision for $(q, e) = (8, 8)$ on $\mathbb{F}_{8^4}$.
4. Exact verification of Proposition 5.1's identity $N(w) = \Phi_{\mathrm{Q3}}(z)\Phi_{\mathrm{Q3}}(z + 1) = w^q + S(w) + \frac{w+1}{w^q}$ on all $z \in A_1$ for $m \in \{2, 3, 4\}$, and direct evaluation $\sum_{w \in H_1} N(w)^{3(q-1)} = 1$ for every $m \in \{3, 4, 5, 6, 7, 8\}$ (and $= 0$ at $m = 2$).
5. Exact verification of every intermediate claim of Theorem 5.5 ($M_{1,\mathrm{rem}}$ identity, zero carries, upper-triangular unique matchings, and exact piece parities $\Sigma_{\mathrm{I}} \equiv m - 1$, $\Sigma_{\mathrm{II}} \equiv 1 + \binom{m-2}{2}$, $\Sigma_{\mathrm{III}} \equiv \binom{m-3}{2}$, $\Sigma_{\mathrm{IV}} = 0$) for every $m \in \{3, 4, 5, 6, 7\}$.

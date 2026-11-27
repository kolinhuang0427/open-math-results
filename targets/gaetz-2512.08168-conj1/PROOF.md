# Proof of Conjecture 1.3 (`conj:union-intersection`) of Gaetz–Gao (`arXiv:2512.08168v2`)

## Primary Source and Exact Statement

**Primary source:** Christian Gaetz and Yibo Gao, *"Billey--Postnikov posets, rationally smooth Schubert varieties, and Poincar\'e duality"*, `arXiv:2512.08168v2` (submitted 9 Dec 2025, revised 8 Jun 2026), Section 1.1 (`conj:union-intersection`, `main.tex` lines 113–116) and Section 2.1 (`def:BP`, `main.tex` lines 192–205).

Let $(W, S)$ be an arbitrary Coxeter system (finite or infinite, crystallographic or non-crystallographic, of arbitrary rank $|S|$), with length function $\ell$, Bruhat order $\le$, and left weak order $\le_L$ (where $u \le_L v$ means $v = x u$ with $\ell(v) = \ell(x) + \ell(u)$). For $u \in W$, its left descent set is $D_L(u) := \{s \in S \mid \ell(su) < \ell(u)\}$, its right descent set is $D_R(u) := \{s \in S \mid \ell(us) < \ell(u)\}$, and its support is $\mathrm{Supp}(u) := \{s \in S \mid s \le u\}$. For any $J \subseteq S$, let $W_J := \langle J \rangle$ be the standard parabolic subgroup and $W^J := \{u \in W \mid \ell(us) > \ell(u) \text{ for all } s \in J\}$ be the set of minimal-length coset representatives of $W/W_J$. Every $w \in W$ has a unique parabolic decomposition $w = w^J w_J$ with $w^J \in W^J$, $w_J \in W_J$, and $\ell(w) = \ell(w^J) + \ell(w_J)$.

> **Definition 2.1 (`def:BP`, `main.tex` lines 194–205):** A parabolic decomposition $w = w^J w_J$ is called a *Billey--Postnikov (BP) decomposition* if
> $$\mathrm{Supp}(w^J) \cap J \subseteq D_L(w_J).$$
> For $w \in W$, define
> $$\mathrm{BP}(w) := \{J \subseteq S \mid w = w^J w_J \text{ is a Billey--Postnikov decomposition}\}.$$

> **Conjecture 1.3 (`conj:union-intersection`, `main.tex` lines 113–116):** Let $W$ be any Coxeter group and let $w \in W$. If $J, K \in \mathrm{BP}(w)$, then $J \cap K, \, J \cup K \in \mathrm{BP}(w)$.

We prove Conjecture 1.3 in full generality (Theorem 1 below). All arguments use only finite words and the standard axioms of arbitrary Coxeter systems (Deletion Property, Exchange Property, Subword Property of Bruhat order, parity of length via the sign homomorphism, and uniqueness/length-additivity of parabolic decompositions; see Björner–Brenti, *Combinatorics of Coxeter Groups*, Chapters 1–2).

---

## Preliminaries and Lemmas

Let $S^*$ denote the set of finite words over the alphabet $S$, with empty word $\varnothing$. For $\mathbf{a} = a_1 \cdots a_m \in S^*$ and $A \subseteq S$, write $\mathbf{a}|_A$ for the subword obtained from $\mathbf{a}$ by retaining only those letters $a_i$ belonging to $A$, and let
$$\mathrm{Sub}(\mathbf{a}) := \{a_{i_1} a_{i_2} \cdots a_{i_k} \in W \mid 0 \le k \le m,\ 1 \le i_1 < \cdots < i_k \le m\}$$
be the set of elements of $W$ expressible as a (not necessarily reduced) subword of $\mathbf{a}$, where the empty product ($k = 0$) is the identity $e \in W$. Note that for any $x \in W$ and $s \in S$, the sign homomorphism $\epsilon : W \to \{\pm 1\}$ (sending every $s \in S$ to $-1$) gives $\ell(sx) = \ell(x) \pm 1$ and $\ell(xs) = \ell(x) \pm 1$.

### Lemma 1 (Elementary Parabolic Properties)
Let $(W, S)$ be any Coxeter system and let $A, J \subseteq S$.
1. If $u \in W_A$, then every letter of every reduced expression of $u$ lies in $A$. Consequently, if $v \in W_A$ and $u \le v$, then $u \in W_A$.
2. If $w \in W$, $u \in W_A$, and $u \le_L w$, then $u \le_L w_A$.
3. If $u, x \in W$ satisfy $u \le x$, then $u^J \le x^J$.

**Proof.**
1. Since $u \in W_A$, $u$ is a product of a finite sequence of elements of $A$. If a word in $A^*$ is not reduced, the Deletion Property produces a strictly shorter word in $A^*$ representing the same element; iterating yields a reduced expression $\mathbf{u}_0 \in A^*$ of $u$. Now let $s \in S$ appear in any reduced expression of $u$. Then $s \le u$ by the Subword Property, so applying the Subword Property to $\mathbf{u}_0$ implies that $s$ appears in $\mathbf{u}_0$, hence $s \in A$. If $v \in W_A$ and $u \le v$, then $u$ has a reduced expression that is a subword of a reduced expression $\mathbf{v}_0 \in A^*$ of $v$, so $u \in W_A$.

2. Since $u \le_L w$, we may write $w = x u$ with $\ell(w) = \ell(x) + \ell(u)$. Factor $x = x^A x_A$ with $x^A \in W^A$, $x_A \in W_A$, and $\ell(x) = \ell(x^A) + \ell(x_A)$. Then $w = x^A (x_A u)$ with $x^A \in W^A$ and $x_A u \in W_A$, so uniqueness of the parabolic factorization $w = w^A w_A$ yields $w^A = x^A$ and $w_A = x_A u$. Comparing lengths,
$$\ell(w^A) + \ell(w_A) = \ell(w) = \ell(x) + \ell(u) = \ell(x^A) + \ell(x_A) + \ell(u) = \ell(w^A) + \ell(x_A) + \ell(u),$$
whence $\ell(x_A u) = \ell(w_A) = \ell(x_A) + \ell(u)$, i.e., $u \le_L w_A$.

3. Choose reduced expressions $\mathbf{x}^J$ of $x^J$ and $\mathbf{x}_J$ of $x_J$; since $\ell(x) = \ell(x^J) + \ell(x_J)$, the concatenation $\mathbf{x}^J \mathbf{x}_J$ is a reduced expression of $x$. Because $u \le x$, the Subword Property yields a reduced expression $\mathbf{u}$ of $u$ that is a subword of $\mathbf{x}^J \mathbf{x}_J$. Splitting $\mathbf{u} = \mathbf{a}\mathbf{b}$ along the boundary between $\mathbf{x}^J$ and $\mathbf{x}_J$, let $a, b \in W$ be the elements represented by $\mathbf{a}, \mathbf{b}$. As a contiguous subword of the reduced word $\mathbf{u}$, $\mathbf{a}$ is a reduced expression of $a$, and it is a subword of $\mathbf{x}^J$, so $a \le x^J$ by the Subword Property. Every letter of $\mathbf{b}$ appears in $\mathbf{x}_J$, hence lies in $J$ by part (1), so $b \in W_J$. Factoring $a = a^J a_J$ gives $u = a b = a^J (a_J b)$ with $a^J \in W^J$ and $a_J b \in W_J$, so $u^J = a^J$ by uniqueness of the parabolic factorization. Finally, any reduced expression of $a^J$ is a prefix of a reduced expression of $a = a^J a_J$, so $a^J \le a$, and therefore $u^J = a^J \le a \le x^J$. $\square$

---

### Lemma 2 (0-Hecke / Demazure Action and Monotonicity)
For $x \in W$ and $s, t \in S$, define
$$s * x := \begin{cases} sx & \text{if } \ell(sx) > \ell(x), \\ x & \text{if } \ell(sx) < \ell(x), \end{cases} \qquad x * t := \begin{cases} xt & \text{if } \ell(xt) > \ell(x), \\ x & \text{if } \ell(xt) < \ell(x). \end{cases}$$
1. For all $x \in W$ and $s, t \in S$, we have $(s * x) * t = s * (x * t)$.
2. Define $\mathrm{Dem} : S^* \to W$ recursively by $\mathrm{Dem}(\varnothing) := e$ and $\mathrm{Dem}(\mathbf{a} t) := \mathrm{Dem}(\mathbf{a}) * t$ for $\mathbf{a} \in S^*$, $t \in S$. Then:
   - $\mathrm{Dem}(s \mathbf{b}) = s * \mathrm{Dem}(\mathbf{b})$ for all $s \in S$ and $\mathbf{b} \in S^*$;
   - $\mathrm{Dem}(\mathbf{a}\mathbf{b}) \ge_L \mathrm{Dem}(\mathbf{b})$ for all $\mathbf{a}, \mathbf{b} \in S^*$;
   - if $\mathbf{w} \in S^*$ is a reduced expression for $w \in W$, then $\mathrm{Dem}(\mathbf{w}) = w$.

**Proof.**
1. We check the four length cases for $(sx, xt)$ relative to $k := \ell(x)$:
   - *Case 1:* $\ell(sx) < k$ and $\ell(xt) < k$. Then $(s * x) * t = x * t = x$ and $s * (x * t) = s * x = x$.
   - *Case 2:* $\ell(sx) = k + 1$ and $\ell(xt) = k - 1$. By the triangle inequality, $k = \ell(sx) - 1 \le \ell(sxt) \le 1 + \ell(xt) = k$, so $\ell((sx)t) = k < \ell(sx)$. Hence $(s * x) * t = (sx) * t = sx = s * x = s * (x * t)$.
   - *Case 3:* $\ell(sx) = k - 1$ and $\ell(xt) = k + 1$. Symmetrically, $\ell(s(xt)) = k < \ell(xt)$, so $(s * x) * t = x * t = xt = s * (xt) = s * (x * t)$.
   - *Case 4:* $\ell(sx) = k + 1$ and $\ell(xt) = k + 1$. By parity and the triangle inequality, either $\ell(sxt) = k + 2$ or $\ell(sxt) = k$.
     - If $\ell(sxt) = k + 2$, then $\ell((sx)t) > \ell(sx)$ and $\ell(s(xt)) > \ell(xt)$, so $(s * x) * t = sxt = s * (x * t)$.
     - If $\ell(sxt) = k$, let $x = s_1 \cdots s_k$ be a reduced expression. Then $s s_1 \cdots s_k$ is a reduced expression of $sx$, and $\ell((sx)t) = k < \ell(sx)$. By the Right Exchange Property, multiplying $s s_1 \cdots s_k$ on the right by $t$ deletes one letter: deleting some $s_i$ ($1 \le i \le k$) and canceling $s$ on the left would give $\ell(xt) \le k - 1$, contradicting $\ell(xt) = k + 1$. Hence the leftmost letter $s$ is deleted, yielding $sxt = x$, i.e., $sx = xt$. Since $\ell((sx)t) = k < \ell(sx)$ and $\ell(s(xt)) = k < \ell(xt)$, we obtain $(s * x) * t = (sx) * t = sx = xt = s * (xt) = s * (x * t)$.

2. For the first claim, induct on the length of $\mathbf{b}$: for $\mathbf{b} = \varnothing$, $\mathrm{Dem}(s) = e * s = s = s * e = s * \mathrm{Dem}(\varnothing)$; for $\mathbf{b} = \mathbf{b}' t$, the induction hypothesis and part (1) give
$$\mathrm{Dem}(s \mathbf{b}' t) = \mathrm{Dem}(s \mathbf{b}') * t = (s * \mathrm{Dem}(\mathbf{b}')) * t = s * (\mathrm{Dem}(\mathbf{b}') * t) = s * \mathrm{Dem}(\mathbf{b}' t).$$
For the second claim, note that $s * y \ge_L y$ for every $s \in S$ and $y \in W$ (either $s * y = sy$ with $\ell(sy) = \ell(y) + 1$, or $s * y = y$). Inducting on the length of $\mathbf{a}$ using $\mathrm{Dem}(s \mathbf{a}' \mathbf{b}) = s * \mathrm{Dem}(\mathbf{a}' \mathbf{b}) \ge_L \mathrm{Dem}(\mathbf{a}' \mathbf{b})$ yields $\mathrm{Dem}(\mathbf{a}\mathbf{b}) \ge_L \mathrm{Dem}(\mathbf{b})$.
For the third claim, induct on $\ell(w)$: if $\mathbf{w} = \mathbf{w}' t$ is reduced, then $\mathbf{w}'$ is a reduced expression for $w' = wt$ and $\ell(w' t) = \ell(w') + 1 > \ell(w')$, so $\mathrm{Dem}(\mathbf{w}) = \mathrm{Dem}(\mathbf{w}') * t = w' * t = w' t = w$. $\square$

---

### Lemma 3 (Subword–Demazure Formula and Parabolic Bruhat Slices)
1. For every finite word $\mathbf{a} \in S^*$,
$$\mathrm{Sub}(\mathbf{a}) = [e, \, \mathrm{Dem}(\mathbf{a})].$$
2. For every $w \in W$, every subset $A \subseteq S$, and every reduced expression $\mathbf{w}$ of $w$,
$$[e, w] \cap W_A = \bigl[e, \, \mathrm{Dem}(\mathbf{w}|_A)\bigr].$$
In particular, $m(w, A) := \mathrm{Dem}(\mathbf{w}|_A)$ is the unique Bruhat-maximum of $[e, w] \cap W_A$ and does not depend on the choice of reduced expression $\mathbf{w}$ of $w$.

**Proof.**
1. We induct on the length $m$ of $\mathbf{a}$. For $m = 0$, $\mathrm{Sub}(\varnothing) = \{e\} = [e, e] = [e, \mathrm{Dem}(\varnothing)]$. For $m \ge 1$, write $\mathbf{a} = \mathbf{a}' t$ ($t \in S$) and set $x := \mathrm{Dem}(\mathbf{a}')$. By the induction hypothesis, $\mathrm{Sub}(\mathbf{a}') = [e, x]$, so $\mathrm{Sub}(\mathbf{a}' t) = [e, x] \cup [e, x] t$.
   - *Case 1:* $\ell(xt) > \ell(x)$, so $x * t = xt$. Fix a reduced expression $\mathbf{x}$ of $x$; then $\mathbf{x} t$ is a reduced expression of $xt$.
     - If $u \in [e, x]$, then $u \le x < xt$. Moreover, if $\ell(ut) < \ell(u)$ then $ut < u \le x < xt$; if $\ell(ut) > \ell(u)$, then appending $t$ to a reduced expression of $u$ occurring as a subword of $\mathbf{x}$ yields a reduced expression of $ut$ occurring as a subword of $\mathbf{x} t$, so $ut \le xt$. Thus $[e, x] \cup [e, x] t \subseteq [e, xt]$.
     - Conversely, if $v \in [e, xt]$, pick a reduced expression $\mathbf{v}$ of $v$ that is a subword of $\mathbf{x} t$. If $\mathbf{v}$ omits the final $t$, then $v \le x$; if $\mathbf{v} = \mathbf{v}' t$ uses the final $t$, then $\mathbf{v}'$ is a reduced expression of $vt$ occurring as a subword of $\mathbf{x}$, so $vt \le x$ and $v = (vt)t \in [e, x] t$. Thus $[e, xt] \subseteq [e, x] \cup [e, x] t$.
   - *Case 2:* $\ell(xt) < \ell(x)$, so $x * t = x$. Fix a reduced expression $\mathbf{y}$ of $xt$; then $\mathbf{y} t$ is a reduced expression of $x$. Clearly $[e, x] \subseteq [e, x] \cup [e, x] t$. Conversely, let $u \in [e, x]$. If $\ell(ut) < \ell(u)$, then $ut < u \le x$. If $\ell(ut) > \ell(u)$, pick a reduced expression $\mathbf{u}$ of $u$ that is a subword of $\mathbf{y} t$; $\mathbf{u}$ cannot use the final $t$ (else $\ell(ut) = \ell(u) - 1$), so $\mathbf{u}$ is a subword of $\mathbf{y}$, and hence $\mathbf{u} t$ is a reduced expression of $ut$ occurring as a subword of $\mathbf{y} t$, giving $ut \le x$. Thus $[e, x] \cup [e, x] t = [e, x]$.

   In both cases $\mathrm{Sub}(\mathbf{a}' t) = [e, x * t] = [e, \mathrm{Dem}(\mathbf{a}' t)]$.

2. Let $\mathbf{w}$ be a reduced expression of $w$.
   - If $u \in [e, w] \cap W_A$, then by the Subword Property $u$ has a reduced expression $\mathbf{u}$ that is a subword of $\mathbf{w}$. By Lemma 1(1), every letter of $\mathbf{u}$ lies in $A$, so $\mathbf{u}$ is a subword of $\mathbf{w}|_A$. Hence $u \in \mathrm{Sub}(\mathbf{w}|_A) = [e, \mathrm{Dem}(\mathbf{w}|_A)]$ by part (1).
   - Conversely, if $u \in [e, \mathrm{Dem}(\mathbf{w}|_A)] = \mathrm{Sub}(\mathbf{w}|_A)$, then $u$ is expressible as a subword of $\mathbf{w}|_A$. Every letter of $\mathbf{w}|_A$ lies in $A$, so $u \in W_A$; and $\mathbf{w}|_A$ is a subword of $\mathbf{w}$, so $u \in \mathrm{Sub}(\mathbf{w}) = [e, \mathrm{Dem}(\mathbf{w})] = [e, w]$ by part (1) and Lemma 2(2). Thus $u \in [e, w] \cap W_A$.

   Antisymmetry of Bruhat order implies that $\mathrm{Dem}(\mathbf{w}|_A)$ is uniquely determined by $[e, w] \cap W_A$, independent of $\mathbf{w}$. $\square$

---

### Lemma 4 (Bruhat-Slice and Product-Interval Characterizations of $\mathrm{BP}(w)$)
Let $w \in W$ and $J \subseteq S$. The following conditions are equivalent:
1. $J \in \mathrm{BP}(w)$, i.e., $\mathrm{Supp}(w^J) \cap J \subseteq D_L(w_J)$;
2. $[e, w] \cap W_J = [e, w_J]$ (equivalently, $m(w, J) = w_J$);
3. For every $u \in W$, $u \le w$ if and only if $u^J \le w^J$ and $u_J \le w_J$.

*(Note that the "if" direction of (3) holds unconditionally for all $w \in W$ and $J \subseteq S$: if $u^J \le w^J$ and $u_J \le w_J$, then $u \le w$.)*

**Proof.**
Fix reduced expressions $\mathbf{w}^J$ of $w^J$ and $\mathbf{w}_J$ of $w_J$; then $\mathbf{w} := \mathbf{w}^J \mathbf{w}_J$ is a reduced expression of $w$. By Lemma 1(1), every letter of $\mathbf{w}_J$ lies in $J$, so $\mathbf{w}|_J = (\mathbf{w}^J|_J)\mathbf{w}_J$.

- **(1) $\implies$ (2):** Write $\mathbf{w}^J|_J = a_1 \cdots a_p$. Every letter $a_i$ appears in $\mathbf{w}^J$, so $a_i \in \mathrm{Supp}(w^J) \cap J \subseteq D_L(w_J)$, which means $\ell(a_i w_J) < \ell(w_J)$ and hence $a_i * w_J = w_J$. Repeatedly applying Lemma 2(2) (and $\mathrm{Dem}(\mathbf{w}_J) = w_J$) gives
$$m(w, J) = \mathrm{Dem}(\mathbf{w}|_J) = a_1 * (a_2 * \cdots * (a_p * \mathrm{Dem}(\mathbf{w}_J))) = a_1 * \cdots * (a_p * w_J) = w_J.$$
By Lemma 3(2), $[e, w] \cap W_J = [e, w_J]$.

- **(2) $\implies$ (1):** Let $s \in \mathrm{Supp}(w^J) \cap J$. Since $s \le w^J$, the Subword Property implies that $s$ appears in $\mathbf{w}^J$, and because $s \in J$, $s$ appears in $\mathbf{w}^J|_J$. Hence the word $s \mathbf{w}_J$ is a subword of $(\mathbf{w}^J|_J)\mathbf{w}_J = \mathbf{w}|_J$. By Lemma 3(1) and (2), $s w_J \in \mathrm{Sub}(\mathbf{w}|_J) = [e, m(w, J)] = [e, w_J]$, so $s w_J \le w_J$. Since $\ell(s w_J) = \ell(w_J) \pm 1$, this forces $\ell(s w_J) < \ell(w_J)$, i.e., $s \in D_L(w_J)$.

- **(Unconditional "if" of (3)):** If $u^J \le w^J$ and $u_J \le w_J$, then choosing reduced expressions $\mathbf{u}^J$ of $u^J$ (a subword of $\mathbf{w}^J$) and $\mathbf{u}_J$ of $u_J$ (a subword of $\mathbf{w}_J$) gives a subword $\mathbf{u}^J \mathbf{u}_J$ of $\mathbf{w}^J \mathbf{w}_J$ representing $u^J u_J = u$, so $u \in \mathrm{Sub}(\mathbf{w}) = [e, w]$ by Lemma 3(1) (equivalently by the Subword Property, since $\ell(u) = \ell(u^J) + \ell(u_J)$).

- **(2) $\implies$ (3):** If $u \le w$, then $u^J \le w^J$ by Lemma 1(3). Moreover, any reduced expression of $u_J$ is a suffix of a reduced expression of $u = u^J u_J$, so $u_J \le u \le w$; hence $u_J \in [e, w] \cap W_J = [e, w_J]$, i.e., $u_J \le w_J$. The converse is the unconditional direction above.

- **(3) $\implies$ (2):** For any $u \in [e, w] \cap W_J$, we have $u_J = u$, so (3) yields $u \le w_J$. Conversely, $w_J \in W_J$ and $w_J \le w$ (as a suffix of $\mathbf{w}^J \mathbf{w}_J$), so $[e, w_J] \subseteq [e, w] \cap W_J$. $\square$

---

### Lemma 5 (Comparison Lemma in $W_{J \cup K}$)
Let $J, K \subseteq S$ and set $M := J \cup K$. Suppose $u, v \in W_M$ satisfy $J, K \in \mathrm{BP}(u)$, $u_J \le v_J$, and $u_K \le v_K$. Then $u \le v$.

**Proof.**
Suppose for the sake of contradiction that $u \not\le v$. Then $[e, u] \setminus [e, v]$ is nonempty (it contains $u$); choose an element $z \in [e, u] \setminus [e, v]$ of minimum length $\ell(z)$.

Since $z \le u$ and $J \in \mathrm{BP}(u)$, Lemma 4(3) gives $z_J \le u_J$, whence $z_J \le v_J$ by hypothesis. We claim that $z^J \not\le v$. Indeed, if $z^J \le v$, then Lemma 1(3) would give $z^J = (z^J)^J \le v^J$; combined with $z_J \le v_J$, the unconditional direction of Lemma 4(3) would yield $z \le v$, contradicting $z \notin [e, v]$. On the other hand, $z^J \le z \le u$ (as a prefix of a reduced expression for $z = z^J z_J$). Thus $z^J \in [e, u] \setminus [e, v]$. Because $\ell(z^J) \le \ell(z)$ and $z$ has minimum length in $[e, u] \setminus [e, v]$, we must have $\ell(z^J) = \ell(z)$, so $\ell(z_J) = 0$ and $z = z^J \in W^J$.

By complete symmetry (replacing $J$ with $K$), we also have $z \in W^K$.

Since $z \le u$ and $u \in W_M$, Lemma 1(1) gives $z \in W_M$. If $z \neq e$, then any reduced expression of $z$ in $M^*$ ends in some generator $s \in M = J \cup K$, so $\ell(zs) < \ell(z)$. However, $z \in W^J$ implies $\ell(zs) > \ell(z)$ for all $s \in J$, and $z \in W^K$ implies $\ell(zs) > \ell(z)$ for all $s \in K$, a contradiction. Therefore $z = e$. But $e \in [e, v]$, contradicting $z \in [e, u] \setminus [e, v]$. Hence $u \le v$. $\square$

---

## Proof of Main Theorem (Conjecture 1.3)

### Theorem 1
Let $(W, S)$ be any Coxeter group and let $w \in W$. If $J, K \in \mathrm{BP}(w)$, then $J \cap K \in \mathrm{BP}(w)$ and $J \cup K \in \mathrm{BP}(w)$. In particular, $\mathrm{BP}(w)$ is a sublattice of the power set $2^S$, hence a distributive lattice.

**Proof.**
Let $w \in W$ and $J, K \in \mathrm{BP}(w)$.

#### Part 1: Intersection closure ($J \cap K \in \mathrm{BP}(w)$)
Set $L := J \cap K$ and $m := m(w, L) \in W_L$, so $[e, w] \cap W_L = [e, m]$ by Lemma 3(2). Choose reduced expressions $\mathbf{w}^J$ of $w^J$ and $\mathbf{w}_J$ of $w_J$, so $\mathbf{w} := \mathbf{w}^J \mathbf{w}_J$ is a reduced expression of $w$.

Restricting $\mathbf{w}$ to $K$ yields $\mathbf{w}|_K = (\mathbf{w}^J|_K)(\mathbf{w}_J|_K)$. By Lemma 1(1), every letter of $\mathbf{w}_J$ belongs to $J$, so $\mathbf{w}_J|_K = \mathbf{w}_J|_L$. Applying Lemma 3(2) to $w_J$ and $L$, and using $[e, w_J] = [e, w] \cap W_J$ (Lemma 4(2) for $J \in \mathrm{BP}(w)$) together with $W_L \subseteq W_J$, we obtain
$$\bigl[e, \, \mathrm{Dem}(\mathbf{w}_J|_L)\bigr] = [e, w_J] \cap W_L = ([e, w] \cap W_J) \cap W_L = [e, w] \cap W_L = [e, m],$$
so $\mathrm{Dem}(\mathbf{w}_J|_L) = m$.

Since $K \in \mathrm{BP}(w)$, Lemma 4(2) gives $\mathrm{Dem}(\mathbf{w}|_K) = w_K$. By Lemma 2(2) (left-weak-order monotonicity of $\mathrm{Dem}$),
$$w_K = \mathrm{Dem}(\mathbf{w}|_K) = \mathrm{Dem}\bigl((\mathbf{w}^J|_K)(\mathbf{w}_J|_L)\bigr) \ge_L \mathrm{Dem}(\mathbf{w}_J|_L) = m.$$
Since $w_K \le_L w$, transitivity of $\le_L$ gives $m \le_L w$. Because $m \in W_L$, Lemma 1(2) yields $m \le_L w_L$, and in particular $\ell(m) \le \ell(w_L)$. On the other hand, $w_L \le_L w$ implies $w_L \in [e, w] \cap W_L = [e, m]$, so $w_L \le m$ and $\ell(w_L) \le \ell(m)$. Thus $m \le_L w_L$ with $\ell(m) = \ell(w_L)$, forcing $m = w_L$. Therefore $[e, w] \cap W_L = [e, w_L]$, and Lemma 4(2) implies $L = J \cap K \in \mathrm{BP}(w)$.

#### Part 2: Union closure ($J \cup K \in \mathrm{BP}(w)$)
Set $M := J \cup K$ and $m := m(w, M) \in W_M$, so $[e, w] \cap W_M = [e, m]$ by Lemma 3(2). Since $w_M \in W_M$ and $w_M \le_L w$, we have $w_M \in [e, w] \cap W_M = [e, m]$, so $w_M \le m \le w$.

We first show that $m_J = w_J$ and $J \in \mathrm{BP}(m)$. Using the reduced expression $\mathbf{w} = \mathbf{w}^J \mathbf{w}_J$ as above, Lemma 1(1) shows that every letter of $\mathbf{w}_J$ lies in $J \subseteq M$, so $\mathbf{w}|_M = (\mathbf{w}^J|_M)\mathbf{w}_J$. By Lemma 2(2),
$$m = \mathrm{Dem}(\mathbf{w}|_M) = \mathrm{Dem}\bigl((\mathbf{w}^J|_M)\mathbf{w}_J\bigr) \ge_L \mathrm{Dem}(\mathbf{w}_J) = w_J.$$
Since $w_J \in W_J$ and $w_J \le_L m$, Lemma 1(2) yields $w_J \le_L m_J$, so $\ell(w_J) \le \ell(m_J)$. Conversely, $m_J \le m \le w$ gives $m_J \in [e, w] \cap W_J = [e, w_J]$ (by Lemma 4(2) for $J \in \mathrm{BP}(w)$), so $m_J \le w_J$ and $\ell(m_J) \le \ell(w_J)$. Hence $m_J = w_J$. Moreover,
$$[e, m_J] = [e, w_J] \subseteq [e, m] \cap W_J \subseteq [e, w] \cap W_J = [e, w_J] = [e, m_J],$$
so $[e, m] \cap W_J = [e, m_J]$, which gives $J \in \mathrm{BP}(m)$ by Lemma 4(2). By symmetry, $m_K = w_K$ and $K \in \mathrm{BP}(m)$.

Next, compare $m_J, m_K$ with $(w_M)_J, (w_M)_K$. Since $w_J \in W_J \subseteq W_M$ and $w_J \le_L w$, Lemma 1(2) gives $w_J \le_L w_M$, and applying Lemma 1(2) once more (with $w_J \in W_J$) gives $w_J \le_L (w_M)_J$. Thus $m_J = w_J \le (w_M)_J$. Symmetrically, $m_K = w_K \le (w_M)_K$.

Applying Lemma 5 to $u = m \in W_M$ and $v = w_M \in W_M$ (using $J, K \in \mathrm{BP}(m)$, $m_J \le (w_M)_J$, and $m_K \le (w_M)_K$), we conclude that $m \le w_M$. Combined with $w_M \le m$, this forces $m = w_M$. Therefore $[e, w] \cap W_M = [e, w_M]$, and Lemma 4(2) gives $M = J \cup K \in \mathrm{BP}(w)$.

Finally, since $\mathrm{BP}(w) \subseteq 2^S$ is closed under finite intersections and unions (and contains $\emptyset$ and $S$), $(\mathrm{BP}(w), \subseteq)$ is a sublattice of the distributive lattice $(2^S, \subseteq)$, and is therefore distributive. $\square$

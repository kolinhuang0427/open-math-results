# Proof of Schwob's Conjecture 8.7 (`arXiv:2606.12129v1`)

## 1. Exact Target Statement and Main Theorem

**Primary source.** Ludovic Schwob, *Middle orders: all distributive lattices between weak and Bruhat*, `arXiv:2606.12129v1` (2026-06-10; cached source `tools/.arxiv_cache/eprint/2606.12129/Middle_order.tex`), Section 8 (*Middle orders and $\omega$-sorting orders*), **Conjecture 8.7** (`\label{cnj:Dtype}`, lines 910–913). Relevant results from the same paper: Type $A$ cover characterization **Proposition 3.8** (`\label{pr:covers}`, lines 291–299), the distributive rhombus property **Proposition 4.1** (`\label{pr:rhombus}`, lines 316–322), Type $A$ exhaustivity **Theorem 4.13** (lines 491–497), and the definition of minuscule middle orders **Definition 7.1** (lines 731–734).

> **Conjecture 8.7 (`cnj:Dtype`).** All middle orders (and in particular distributive sorting orders) on $D_n$ are minuscule middle orders.

**Main Theorem.** For every integer $n \ge 4$ (and also for the degenerate cases $D_2 = A_1 \times A_1$ and $D_3 \cong A_3$), every middle order on the Weyl group $D_n$—that is, every distributive lattice $\mathbf{L} = (D_n, \le_{\mathbf{L}})$ refining the right weak order $(D_n, \le_R)$ and refined by the Bruhat order $(D_n, \le)$—is a minuscule middle order. In particular, since every $\omega$-sorting order for a reduced word $\omega$ of $w_0$ lies between the right weak order and the Bruhat order (`Middle_order.tex`, Section 8, line 838), every distributive sorting order on $D_n$ is a minuscule middle order.

*(The proof proceeds by induction on $n \ge 4$, using Schwob's Type $A$ classification Theorem 4.13 for $A_{n-1}$ and the base case $D_3 \cong A_3$, and requires no computer search for any $n \ge 4$.)*

---

## 2. Conventions and Elementary Coxeter / Bruhat Lemmas

### 2.1. Signed-Permutation Realization of $D_n$

For $n \ge 4$, we realize $D_n$ as the group of signed permutations $w = (w(1), \dots, w(n))$ of $\{1, \dots, n\}$ with an even number of negative entries, extended to odd bijections on $\{\pm 1, \dots, \pm n\}$ via $w(-i) = -w(i)$. Group multiplication is composition $(u \cdot v)(i) = u(v(i))$, so right multiplication acts on *positions* and left multiplication acts on *values*. The simple generators are $S = \{s_0, s_1, s_2, \dots, s_{n-1}\}$ where:
- $s_0$ swaps and negates positions $(1, 2)$ on the right: $(w_1, w_2, w_3, \dots, w_n) \cdot s_0 = (-w_2, -w_1, w_3, \dots, w_n)$ (and swaps values $1 \leftrightarrow -2$, $-1 \leftrightarrow 2$ on the left);
- $s_i$ ($1 \le i \le n - 1$) swaps positions $(i, i+1)$ on the right (and swaps values $i \leftrightarrow i+1$, $-i \leftrightarrow -(i+1)$ on the left).

The Dynkin diagram of $(D_n, S)$ has hub $s_2$ adjacent to $s_0, s_1, s_3$, and spine $s_2 - s_3 - \dots - s_{n-1}$ (for $n = 4$, $s_2$ is adjacent to the three leaves $s_0, s_1, s_3$). The three minuscule simple roots of $D_n$ ($n \ge 4$) are the three leaves $s_0, s_1, s_{n-1}$. The reflections of $D_n$ are the Type I swaps $t_{p,q}^+$ (swapping positions $p < q$) and Type II sign-flips $t_{p,q}^-$ (swapping and negating positions $p < q$). The Coxeter length is (Björner–Brenti 2005, Proposition 8.2.1):
$$\ell(w) = \#\{1 \le i < j \le n : w(i) > w(j)\} + \#\{1 \le i < j \le n : w(i) + w(j) < 0\}.$$
In particular, $\ell(w t_{p,q}^+) > \ell(w) \iff w(p) < w(q)$, and $\ell(w t_{p,q}^-) > \ell(w) \iff w(p) + w(q) > 0$. Right weak covers are $u \lessdot_R u s_k$ with $\ell(u s_k) = \ell(u) + 1$; $s_k$ is a *left descent* of $w$ iff $\ell(s_k w) < \ell(w)$, equivalently $s_k \le_R w$.

The three maximal parabolic subgroups associated to the minuscule leaves are:
- $J_0 := S \setminus \{s_0\} = \{s_1, \dots, s_{n-1}\}$: $W_{J_0} = \mathfrak{S}_n \cong A_{n-1}$ (all entries positive);
- $J_1 := S \setminus \{s_1\} = \{s_0, s_2, \dots, s_{n-1}\}$: $W_{J_1} = \tau(W_{J_0}) \cong A_{n-1}$, where $\tau(w) := t_1 w t_1$ is the Dynkin diagram automorphism conjugating by the sign-negation $t_1 \in B_n$ of position $1$ (so $\tau$ negates position $1$ and value $1$, swaps $s_0 \leftrightarrow s_1$, fixes $s_2, \dots, s_{n-1}$, and preserves length, right weak order, and Bruhat order);
- $J_{n-1} := S \setminus \{s_{n-1}\} = \{s_0, s_1, \dots, s_{n-2}\}$: $W_{J_{n-1}} = \{w \in D_n : w(n) = n\} \cong D_{n-1}$ (for $n = 4$, $D_3 \cong A_3$ via $s_0 - s_2 - s_1$).

For any middle order $\mathbf{L}$ on a finite Coxeter group $(W, S)$, we denote its covering edge set by $E(\mathbf{L})$. Because both $(W, \le_R)$ and $(W, \le)$ are graded by $\ell$, $\mathbf{L}$ is graded by $\ell$, every right weak cover lies in $E(\mathbf{L})$, and every cover in $E(\mathbf{L})$ is a Bruhat cover. We repeatedly invoke **Proposition 4.1** (`pr:rhombus`) of `arXiv:2606.12129v1`: if $a, b \in W$ both cover $u$ in $\mathbf{L}$, then $a \vee_{\mathbf{L}} b$ covers both $a$ and $b$ in $\mathbf{L}$ (hence is a common Bruhat upper cover of $a$ and $b$); dually, if $u$ covers both $a$ and $b$ in $\mathbf{L}$, then $a \wedge_{\mathbf{L}} b$ is covered by both $a$ and $b$ in $\mathbf{L}$ (hence is a common Bruhat lower cover of $a$ and $b$). In particular, if $a, b$ have *zero* common Bruhat upper covers, then $(u, a)$ and $(u, b)$ cannot both lie in $E(\mathbf{L})$; if $a, b$ have a *unique* common Bruhat upper cover $w$, then $(u, a), (u, b) \in E(\mathbf{L})$ forces $(a, w), (b, w) \in E(\mathbf{L})$ (and dually for lower covers).

### 2.2. Common Covers of Reflection Neighbors in $D_n$

**Lemma 1 (Common Covers of Two Reflection Neighbors in $D_n$).**
*Let $u \in D_n$, and let $r_1 \neq r_2$ be reflections in $D_n$ with $\ell(u r_1) = \ell(u r_2) = \ell(u) + 1$ (resp. $\ell(u) - 1$). Write $\mathrm{supp}(t_{p,q}^{\pm}) := \{p, q\}$.*
1. *If $\mathrm{supp}(r_1) \cap \mathrm{supp}(r_2) = \emptyset$ or $\mathrm{supp}(r_1) = \mathrm{supp}(r_2)$, then $r_1 r_2 = r_2 r_1$ and the **only** possible common Bruhat upper (resp. lower) cover of $u r_1$ and $u r_2$ is $u r_1 r_2$ (which is one iff $\ell(u r_1 r_2) = \ell(u) + 2$, resp. $\ell(u) - 2$).*
2. *If $|\mathrm{supp}(r_1) \cap \mathrm{supp}(r_2)| = 1$, then the **only** possible common Bruhat upper (resp. lower) covers of $u r_1$ and $u r_2$ are $u r_1 r_2$ and $u r_2 r_1$ (each is one iff its length is $\ell(u) + 2$, resp. $\ell(u) - 2$).*

*Proof.* Set $a := u r_1$ and $b := u r_2$. Any common Bruhat upper (or lower) cover $w$ of $a$ and $b$ satisfies $w \neq u$, $w = a r_3 = b r_4$ for reflections $r_3, r_4$ of $D_n$, and therefore $r_3 r_4 = a^{-1} b = r_1 r_2$.
- **Case 1a ($\mathrm{supp}(r_1) \cap \mathrm{supp}(r_2) = \emptyset$):** Let $\mathrm{supp}(r_1) = \{p_1, q_1\}$ and $\mathrm{supp}(r_2) = \{p_2, q_2\}$ (four distinct positions). Then $r_1 r_2$ moves all four positions in two disjoint $2$-cycles. Since $r_3, r_4$ each move at most $2$ positions and $r_3 r_4 = r_1 r_2$, $\mathrm{supp}(r_3)$ and $\mathrm{supp}(r_4)$ must partition $\{p_1, q_1, p_2, q_2\}$ into two pairs, and each pair must be a cycle of $r_1 r_2$ (mixing $\{p_1, q_1\}$ and $\{p_2, q_2\}$ yields a $4$-cycle or fails to match $r_1 r_2$). Thus $\{r_3, r_4\} = \{r_1, r_2\}$. Since $r_3 = r_1$ gives $w = u$, the only remaining candidate is $r_3 = r_2$, giving $w = u r_1 r_2$.
- **Case 1b ($\mathrm{supp}(r_1) = \mathrm{supp}(r_2) = \{p, q\}$):** Then $\{r_1, r_2\} = \{t_{p,q}^+, t_{p,q}^-\}$, so $r_1 r_2$ fixes every position as a permutation and negates precisely coordinates $p$ and $q$. If $r_3$ moved any $k \notin \{p, q\}$ to some $x$, then $r_4$ would have to move $x$ back to $k$, so $\mathrm{supp}(r_3) = \mathrm{supp}(r_4) = \{x, k\}$; then $r_3 r_4$ would negate at most $\{x, k\} \neq \{p, q\}$, impossible. Hence $\mathrm{supp}(r_3) = \mathrm{supp}(r_4) = \{p, q\}$, forcing $\{r_3, r_4\} = \{r_1, r_2\}$ and again $w = u r_1 r_2$.
- **Case 2 ($|\mathrm{supp}(r_1) \cap \mathrm{supp}(r_2)| = 1$):** Let $\mathrm{supp}(r_1) = \{p, q\}$ and $\mathrm{supp}(r_2) = \{q, k\}$ (three distinct positions). Then $g := r_1 r_2$ is a signed $3$-cycle on $\{p, q, k\}$ (order $3$, fixing all positions outside $\{p, q, k\}$). If $r_3$ moved any $m \notin \{p, q, k\}$ to some $x$, then $r_4$ would have to map $x$ back to $m$, forcing $\mathrm{supp}(r_3) = \mathrm{supp}(r_4) = \{m, x\}$, so $r_3 r_4$ would have order $1$ or $2$, contradicting $\mathrm{ord}(g) = 3$. Thus $\mathrm{supp}(r_3), \mathrm{supp}(r_4) \subseteq \{p, q, k\}$. Among the $6$ reflections supported on $\{p, q, k\}$, each $r_3$ uniquely determines $r_4 = r_3 g$. Conjugating by diagonal sign changes in $B_n$ and relabeling $\{p, q, k\}$ as $\{1, 2, 3\}$ maps any overlapping pair $(r_1, r_2)$ to $(t_{1,2}^+, t_{2,3}^+)$, where $g = t_{1,2}^+ t_{2,3}^+$ maps $(1, 2, 3) \mapsto (2, 3, 1)$. Testing all $6$ reflections on $\{1, 2, 3\}$:
  - The $3$ Type I reflections $r_3 \in \{t_{1,2}^+, t_{2,3}^+, t_{1,3}^+\}$ yield reflections $r_4 = r_3 g \in \{t_{2,3}^+, t_{1,3}^+, t_{1,2}^+\}$, corresponding to $w = a r_3 \in \{u, u r_1 r_2, u r_2 r_1\}$.
  - The $3$ Type II reflections $r_3 \in \{t_{1,2}^-, t_{2,3}^-, t_{1,3}^-\}$ yield $r_4 = r_3 g$ mapping $(1, 2, 3)$ to $(-1, 3, -2)$, $(-3, -2, 1)$, and $(2, -1, -3)$ respectively—each of which has order $4$ and is therefore not a reflection.

  Hence $u r_1 r_2$ and $u r_2 r_1$ are the only possible common Bruhat upper (or lower) covers with $w \neq u$. $\blacksquare$

---

## 3. Birkhoff Splitting Criterion and Join-Irreducible Reduction

The following structural results hold for **every** finite Coxeter group $(W, S)$ and every middle order $\mathbf{L} = (W, \le_{\mathbf{L}})$. By Birkhoff's representation theorem, let $\mathcal{P} := \mathcal{J}(\mathbf{L})$ be the poset of join-irreducible elements of $\mathbf{L}$, with order-isomorphism $\Phi: \mathbf{L} \xrightarrow{\sim} \mathbf{Low}(\mathcal{P})$ given by $\Phi(w) = \{p \in \mathcal{P} : p \le_{\mathbf{L}} w\}$. Because $\mathbf{L}$ is graded by $\ell$, $|\Phi(w)| = \ell(w)$ for all $w \in W$, and the minimal elements of $\mathcal{P}$ are precisely the atoms of $\mathbf{L}$, namely $S$ (since every Bruhat cover of $\mathrm{id}$ lies in $S$ and every $s \in S$ satisfies $\mathrm{id} \lessdot_R s$).

**Lemma 2 (Parabolic Restriction and Dual Middle Order).**
*Let $\mathbf{L}$ be a middle order on a finite Coxeter group $(W, S)$, with longest element $w_0$.*
1. *For every $J \subseteq S$, the lower interval $[\mathrm{id}, w_0(J)]_{\mathbf{L}}$ equals $W_J$. Hence $\mathbf{L}|_{W_J}$ is a middle order on $W_J$, corresponding to the lower set $L_J := \Phi(w_0(J)) \subseteq \mathcal{P}$ of size $\ell(w_0(J))$, and $L_{J_1 \cap J_2} = L_{J_1} \cap L_{J_2}$ for all $J_1, J_2 \subseteq S$.*
2. *Define the dual order $\mathbf{L}^*$ on $W$ by $u \le_{\mathbf{L}^*} v \iff v w_0 \le_{\mathbf{L}} u w_0$. Then $\mathbf{L}^*$ is a middle order on $(W, S)$.*
3. *For every $J \subseteq S$, setting ${}^J w_0 := w_0(J) w_0$ (the longest element of ${}^J W$), the upper interval $[{}^J w_0, w_0]_{\mathbf{L}}$ has cardinality $|W_J|$.*

*Proof.*
(1) Every $x \in W_J$ satisfies $x \le_R w_0(J)$, hence $x \le_{\mathbf{L}} w_0(J)$. Conversely, if $x \le_{\mathbf{L}} w_0(J)$, then $x \le w_0(J)$ in Bruhat order, so every reduced word of $x$ is a subword of a reduced word of $w_0(J)$ (using only letters in $J$), whence $x \in W_J$. Thus $[\mathrm{id}, w_0(J)]_{\mathbf{L}} = W_J$. Since an interval of a distributive lattice is a distributive lattice, $\mathbf{L}|_{W_J}$ is a middle order on $W_J$. Finally, $w_0(J_1) \wedge_{\mathbf{L}} w_0(J_2) \in W_{J_1} \cap W_{J_2} = W_{J_1 \cap J_2}$ and lies above $w_0(J_1 \cap J_2)$, forcing $w_0(J_1) \wedge_{\mathbf{L}} w_0(J_2) = w_0(J_1 \cap J_2)$, i.e., $L_{J_1} \cap L_{J_2} = L_{J_1 \cap J_2}$.

(2) Right multiplication by $w_0$ is an anti-automorphism of both right weak order (since $N_L(w w_0) = \Phi^+ \setminus N_L(w)$) and Bruhat order (Björner–Brenti 2005, Proposition 2.3.4). Reversing a distributive lattice yields a distributive lattice, so $\mathbf{L}^*$ is a middle order on $(W, S)$.

(3) Under the anti-isomorphism $u \mapsto u w_0$ from $\mathbf{L}^*$ to $\mathbf{L}$, the lower interval $[\mathrm{id}, w_0(J)]_{\mathbf{L}^*} = W_J$ (by (1) applied to $\mathbf{L}^*$) maps bijectively onto $[w_0(J) w_0, w_0]_{\mathbf{L}} = [{}^J w_0, w_0]_{\mathbf{L}}$. $\blacksquare$

**Theorem 3 (Single-Atom Parabolic Splitting Criterion).**
*Let $\mathbf{L}$ be a middle order on a finite Coxeter group $(W, S)$, and let $J \subseteq S$. The following are equivalent:*
1. *$\mathbf{L} = (\mathbf{L}|_{W_J}) \times (\mathbf{L}|_{{}^J W})$ under the parabolic factorization $w = w_J \cdot {}^J w$.*
2. *$L_J$ is a union of connected components of $\mathcal{P} = \mathcal{J}(\mathbf{L})$ (i.e., $\mathcal{P} = L_J \sqcup Q$ with no order relations between $L_J$ and $Q$).*
3. *For every $s \in J$, $s \not\le_{\mathbf{L}} {}^J w_0$.*

*Proof.*
$(1) \implies (2)$ is immediate from Birkhoff's theorem ($\mathbf{Low}(\mathcal{P}_1) \times \mathbf{Low}(\mathcal{P}_2) \cong \mathbf{Low}(\mathcal{P}_1 \sqcup \mathcal{P}_2)$).

$(3) \implies (2)$: Let $A := \Phi({}^J w_0) \subseteq \mathcal{P}$ (a lower set) and $B := \mathcal{P} \setminus A$ (an upper set). By Lemma 2(3), $|\mathbf{Low}(B)| = |[{}^J w_0, w_0]_{\mathbf{L}}| = |W_J|$. Next, take any $w \in [\mathrm{id}, {}^J w_0]_{\mathbf{L}}$. If $w$ had a left descent $s \in J$, then $s \le_R w \le_{\mathbf{L}} {}^J w_0$, contradicting (3). Thus $w \in {}^J W$, giving $[\mathrm{id}, {}^J w_0]_{\mathbf{L}} \subseteq {}^J W$. Conversely, ${}^J W = [\mathrm{id}, {}^J w_0]_R \subseteq [\mathrm{id}, {}^J w_0]_{\mathbf{L}}$. Hence $[\mathrm{id}, {}^J w_0]_{\mathbf{L}} = {}^J W$, so $|\mathbf{Low}(A)| = |{}^J W|$.

The map $I \mapsto (I \cap A, I \cap B)$ is an injection $\mathbf{Low}(\mathcal{P}) \hookrightarrow \mathbf{Low}(A) \times \mathbf{Low}(B)$. Since
$$|\mathbf{Low}(\mathcal{P})| = |W| = |{}^J W| \cdot |W_J| = |\mathbf{Low}(A)| \cdot |\mathbf{Low}(B)|,$$
this injection is a bijection. Taking $I_A = \emptyset, I_B = B$ shows that $B$ is also a lower set of $\mathcal{P}$, so $\mathcal{P} = A \sqcup B$ has no comparabilities between $A$ and $B$. Moreover, every atom $s \le_{\mathbf{L}} w_0(J) \wedge_{\mathbf{L}} {}^J w_0$ satisfies $s \in W_J \cap S = J$ and $s \le_{\mathbf{L}} {}^J w_0$, impossible by (3); hence $w_0(J) \wedge_{\mathbf{L}} {}^J w_0 = \mathrm{id}$, meaning $L_J \cap A = \emptyset$, i.e., $L_J \subseteq B$. Since $|L_J| = \ell(w_0(J)) = \ell(w_0) - \ell({}^J w_0) = |\mathcal{P}| - |A| = |B|$, we obtain $L_J = B$, proving (2).

$(2) \implies (1)$: Suppose $\mathcal{P} = L_J \sqcup Q$ as a disjoint union of posets. Set $\mathcal{Q} := \Phi^{-1}(\mathbf{Low}(Q))$. Every $w \in W$ decomposes uniquely as $w = \tilde{x}(w) \vee_{\mathbf{L}} \tilde{q}(w)$ with $\tilde{x}(w) = w \wedge_{\mathbf{L}} w_0(J) \in W_J$, $\tilde{q}(w) \in \mathcal{Q}$, and $\ell(w) = \ell(\tilde{x}(w)) + \ell(\tilde{q}(w))$. Every $s \in J$ belongs to $L_J$, so for all $q \in \mathcal{Q}$ we have $s \notin \Phi(q)$, hence $s \not\le_R q$, i.e., $q \in {}^J W$. Since $|\mathcal{Q}| = |\mathbf{Low}(Q)| = |W| / |W_J| = |{}^J W|$, we have $\mathcal{Q} = {}^J W$.

Recall that the projection $u \mapsto {}^J u$ is Bruhat order-preserving: if $u \le v = v_J \cdot {}^J v$, taking a reduced word for $v$ by concatenating reduced words of $v_J$ and ${}^J v$, a reduced word for $u$ is a subword $a \cdot b$ with $a \in W_J$ and $b \le {}^J v$; factoring $b = b_J \cdot {}^J b$ gives $u = (a b_J) \cdot {}^J b$, so ${}^J u = {}^J b \le b \le {}^J v$. Applying this to $\tilde{q}(w) \le_{\mathbf{L}} w$ (hence $\tilde{q}(w) \le w$) gives $\tilde{q}(w) = {}^J(\tilde{q}(w)) \le {}^J w$, so $\ell(\tilde{q}(w)) \le \ell({}^J w)$ for every $w \in W$, with equality iff $\tilde{q}(w) = {}^J w$. Summing over $W$, both $w \mapsto \tilde{q}(w)$ and $w \mapsto {}^J w$ have fibers of exact size $|W_J|$ over every $q \in {}^J W$, so
$$\sum_{w \in W} \ell(\tilde{q}(w)) = |W_J| \sum_{q \in {}^J W} \ell(q) = \sum_{w \in W} \ell({}^J w).$$
Hence $\tilde{q}(w) = {}^J w$ for all $w \in W$. Finally, for $w = w_J \cdot {}^J w$, since $\ell(w) = \ell(w_J) + \ell({}^J w)$, we have $w_J \le_R w$, hence $w_J \le_{\mathbf{L}} w \wedge_{\mathbf{L}} w_0(J) = \tilde{x}(w)$. Because $\ell(\tilde{x}(w)) = \ell(w) - \ell(\tilde{q}(w)) = \ell(w) - \ell({}^J w) = \ell(w_J)$, we conclude $\tilde{x}(w) = w_J$ for all $w \in W$. Thus $u \le_{\mathbf{L}} v \iff (u_J \le_{\mathbf{L}} v_J \text{ and } {}^J u \le_{\mathbf{L}} {}^J v)$, proving (1). $\blacksquare$

**Corollary 4 (Join-Irreducible Reduction for Minuscule Quotients).**
*Let $(W, S)$ be a Weyl group, $s_* \in S$ a minuscule simple generator, $J := S \setminus \{s_*\}$, and $\mathbf{L}$ a middle order on $W$. Because $s_*$ is minuscule, the weak and Bruhat orders coincide on ${}^J W$ and make ${}^J W$ a distributive lattice. Write $\mathcal{J}({}^J W)$ for the set of join-irreducible elements of ${}^J W$ (those $q \in {}^J W \setminus \{\mathrm{id}\}$ having a unique right weak lower cover $q' \lessdot_R q$ inside ${}^J W$). Suppose that for every $q \in \mathcal{J}({}^J W)$:*
> *if $[\mathrm{id}, q']_{\mathbf{L}} = [\mathrm{id}, q']_R$ holds for the unique ${}^J W$-lower cover $q'$ of $q$, then $q'$ is the unique lower cover of $q$ in $\mathbf{L}$.*

*Then $\mathbf{L} = (\mathbf{L}|_{W_J}) \times {}^J W$.*

*Proof.* We prove $[\mathrm{id}, q]_{\mathbf{L}} = [\mathrm{id}, q]_R$ (and hence $s \not\le_{\mathbf{L}} q$ for all $s \in J$) for all $q \in {}^J W$ by induction on $\ell(q)$. The base $\ell(q) = 0$ is trivial. For $\ell(q) \ge 1$:
- If $q$ has at least two distinct right weak lower covers $q_1, q_2 \lessdot_R q$ in ${}^J W$, then $q_1, q_2 \lessdot_{\mathbf{L}} q$, so $q = q_1 \vee_{\mathbf{L}} q_2$. For any $s \in J$, if $s \le_{\mathbf{L}} q$ then by distributivity $s = s \wedge_{\mathbf{L}} (q_1 \vee_{\mathbf{L}} q_2) = (s \wedge_{\mathbf{L}} q_1) \vee_{\mathbf{L}} (s \wedge_{\mathbf{L}} q_2)$; since $s$ is an atom, $s \le_{\mathbf{L}} q_1$ or $s \le_{\mathbf{L}} q_2$, contradicting the induction hypothesis.
- If $q \in \mathcal{J}({}^J W)$ has unique ${}^J W$-lower cover $q'$, then by the induction hypothesis $[\mathrm{id}, q']_{\mathbf{L}} = [\mathrm{id}, q']_R$, so by assumption $q'$ is the unique lower cover of $q$ in $\mathbf{L}$. Any $s \in J$ with $s \le_{\mathbf{L}} q$ satisfies $s \neq q$ (since $q \in {}^J W$), hence $s \le_{\mathbf{L}} q'$, contradicting the induction hypothesis.

In both cases, no $s \in J$ satisfies $s \le_{\mathbf{L}} q$. Consequently every $w \le_{\mathbf{L}} q$ has no left descent in $J$, so $[\mathrm{id}, q]_{\mathbf{L}} \subseteq {}^J W$; since weak and Bruhat orders coincide on ${}^J W$, $[\mathrm{id}, q]_{\mathbf{L}} = [\mathrm{id}, q]_R$. Applying this to $q = {}^J w_0$ gives $s \not\le_{\mathbf{L}} {}^J w_0$ for all $s \in J$, so Theorem 3 yields $\mathbf{L} = (\mathbf{L}|_{W_J}) \times {}^J W$. $\blacksquare$

**Corollary 5 (Parabolic Restriction and Uniqueness of Splitting Roots).**
*Let $(W, S)$ be an irreducible Weyl group and $\mathbf{L}$ a middle order on $W$.*
1. *If $\mathbf{L}$ splits along $J = S \setminus \{s_*\}$ and $K \subseteq S$ contains $s_*$, then $\mathbf{L}|_{W_K}$ splits along $K \setminus \{s_*\}$.*
2. *There is **at most one** generator $s_* \in S$ such that $\mathbf{L}$ splits along $S \setminus \{s_*\}$.*

*Proof.*
(1) By Theorem 3(2), $\mathcal{P} = L_J \sqcup Q$ with no comparabilities between $L_J$ and $Q$. Intersecting with the lower set $L_K$ yields $L_K = (L_K \cap L_J) \sqcup (L_K \cap Q) = L_{K \setminus \{s_*\}} \sqcup (L_K \cap Q)$, so Theorem 3(2) applied to $\mathbf{L}|_{W_K}$ gives the split along $K \setminus \{s_*\}$.

(2) Suppose $\mathbf{L}$ splits along both $J_1 = S \setminus \{s_1\}$ and $J_2 = S \setminus \{s_2\}$ with $s_1 \neq s_2$. Write $\mathcal{P} = L_{J_i} \sqcup Q_i$ ($i = 1, 2$). Any $p \in Q_1 \cap Q_2$ would be incomparable to $L_{J_1}$ and $L_{J_2}$, hence could not lie above any minimal element in $J_1 \cup J_2 = S$, impossible. Thus $Q_1 \cap Q_2 = \emptyset$, so $L_{J_1} \cup L_{J_2} = \mathcal{P}$, giving
$$|L_{J_1 \cap J_2}| = |L_{J_1}| + |L_{J_2}| - |\mathcal{P}| = |\Phi_{J_1}^+| + |\Phi_{J_2}^+| - |\Phi^+|.$$
On the other hand, since $W$ is irreducible, the highest root $\theta \in \Phi^+$ has full support $S$ and therefore lies in neither $\Phi_{J_1}^+$ nor $\Phi_{J_2}^+$, whence $|\Phi_{J_1}^+ \cup \Phi_{J_2}^+| \le |\Phi^+| - 1$, i.e., $|\Phi_{J_1}^+| + |\Phi_{J_2}^+| - |\Phi_{J_1 \cap J_2}^+| \le |\Phi^+| - 1$, contradiction. $\blacksquare$

---

## 4. Overlap Trichotomy on $D_n$

Fix $n \ge 4$, let $\mathbf{L}$ be a middle order on $D_n$, and assume by induction that Conjecture 8.7 holds for $D_{n-1}$ (for $n = 4$, $D_3 \cong A_3$ holds by Schwob's Type $A$ **Theorem 4.13**). By Lemma 2(1), the three maximal parabolic restrictions $\mathbf{L}|_{W_{J_0}}$ ($A_{n-1}$), $\mathbf{L}|_{W_{J_1}}$ ($A_{n-1}$), and $\mathbf{L}|_{W_{J_{n-1}}}$ ($D_{n-1}$) are all minuscule middle orders. By Corollary 5(2), each has a **unique** top splitting generator:
$$r_0 \in J_0 = \{s_1, \dots, s_{n-1}\}, \qquad r_1 \in J_1 = \{s_0, s_2, \dots, s_{n-1}\}, \qquad r_t \in \{s_0, s_1, s_{n-2}\}$$
(the three minuscule simple generators of $D_{n-1}$, noting that for $n = 4$, $D_3 = \{s_0, s_1, s_2\} \cong A_3$ also has minuscule roots $\{s_0, s_1, s_2\} = \{s_0, s_1, s_{n-2}\}$).

Applying Corollary 5(1)–(2) to the three irreducible pairwise intersections $J_0 \cap J_1 = \{s_2, \dots, s_{n-1}\}$, $J_0 \cap J_{n-1} = \{s_1, \dots, s_{n-2}\}$, and $J_1 \cap J_{n-1} = \{s_0, s_2, \dots, s_{n-2}\}$ (each $\cong A_{n-2}$) immediately gives three compatibility rules:
- If $r_0 \neq s_1$ and $r_1 \neq s_0$, then $r_0 = r_1$.
- If $r_0 \neq s_{n-1}$ and $r_t \neq s_0$, then $r_0 = r_t$.
- If $r_1 \neq s_{n-1}$ and $r_t \neq s_1$, then $r_1 = r_t$.

Evaluating all three choices of $r_t \in \{s_0, s_1, s_{n-2}\}$:
1. **$r_t = s_0$:** The $J_1 \cap J_{n-1}$ rule forces $r_1 \in \{s_0, s_{n-1}\}$.
   - If $r_1 = s_0$: **Case (G1)** ($r_t = r_1 = s_0$).
   - If $r_1 = s_{n-1}$: the $J_0 \cap J_1$ rule forces $r_0 \in \{s_{n-1}, s_1\}$, giving either **Case (G2)** ($r_0 = r_1 = s_{n-1}$) or **Case (B1)** ($r_0 = s_1, r_1 = s_{n-1}, r_t = s_0$).
2. **$r_t = s_1$:** By the diagram automorphism $\tau$ swapping $s_0 \leftrightarrow s_1$, this gives **Case (G1')** ($r_t = r_0 = s_1$), **Case (G2)** ($r_0 = r_1 = s_{n-1}$), or **Case (B1')** ($r_0 = s_{n-1}, r_1 = s_0, r_t = s_1$).
3. **$r_t = s_{n-2}$:** The $J_0 \cap J_{n-1}$ and $J_1 \cap J_{n-1}$ rules force $r_0, r_1 \in \{s_{n-2}, s_{n-1}\}$, and then the $J_0 \cap J_1$ rule forces $r_0 = r_1$, giving either **Case (G2)** ($r_0 = r_1 = s_{n-1}$) or **Case (B2)** ($r_0 = r_1 = r_t = s_{n-2}$).

Thus, up to the diagram automorphism $\tau$ ($s_0 \leftrightarrow s_1$), every middle order on $D_n$ falls into one of **four** cases: **(B1)**, **(B2)**, **(G2)**, or **(G1)**. We eliminate **(B1)** and **(B2)** in Section 5, and prove product splitting in **(G2)** and **(G1)** in Sections 6–7.

---

## 5. Eliminating the Two Bad Cases (B1) and (B2)

Throughout Sections 5–7, we write $\vec{\alpha}$ for a fixed suffix of entries; in every rhombus step, the unique- or zero-common-cover assertion follows directly from Lemma 1 by comparing lengths via the exact length formula.

### 5.1. Lemma 6: Elimination of the 3-Cycle Case (B1)

**Lemma 6 (No 3-Cycle).** *For all $n \ge 4$, Case (B1) ($r_0 = s_1$, $r_1 = s_{n-1}$, $r_t = s_0$) is impossible.*

*Proof.* Set $\vec{d} := (4, 5, \dots, n - 1)$ (empty for $n = 4$). Assume for contradiction that $(r_0, r_1, r_t) = (s_1, s_{n-1}, s_0)$.
1. **Input from $r_0 = s_1$ in $W_{J_0} = \mathfrak{S}_n$:** Because $s_1$ is the root of the binary tree of $\mathbf{L}|_{W_{J_0}}$, by Schwob's Proposition 3.8 (`pr:covers`) the transposition $(3, n)$ jumps over $1$, so
   $$u_0 := (2, 3, 1, n, \vec{d}) \longrightarrow v_0 := (2, n, 1, 3, \vec{d}) \in E(\mathbf{L}).$$
2. **Weak step $s_0$:** $u_1 := u_0 s_0 = (-3, -2, 1, n, \vec{d})$ is a right weak cover of $u_0$. The reflection $r_L = t_{2,4}^+$ (for $u_0 \to v_0$) and $s_0 = t_{1,2}^-$ overlap at position $2$. By Lemma 1(2), the only candidates for common upper covers of $v_0$ and $u_1$ are $v_1 := v_0 s_0 = (-n, -2, 1, 3, \vec{d})$ (length $\ell(u_0) + 2$) and $u_1 t_{2,4}^+ = (-3, n, 1, -2, \vec{d})$, which has length $\ell(u_1) + 3 = \ell(u_0) + 4$ (as $1 \in (-2, n)$). Hence $v_1$ is the unique common Bruhat upper cover, so Proposition 4.1 yields $(u_1, v_1) \in E(\mathbf{L})$.
3. **Weak step $s_2$:** $u_2 := u_1 s_2 = (-3, 1, -2, n, \vec{d})$ is a right weak cover of $u_1$. Here $t_{1,4}^+$ (for $u_1 \to v_1$) and $s_2 = t_{2,3}^+$ have disjoint supports, so by Lemma 1(1), $v_2 := v_1 s_2 = (-n, 1, -2, 3, \vec{d})$ is the unique common Bruhat upper cover of $v_1$ and $u_2$, giving $(u_2, v_2) \in E(\mathbf{L})$.
4. **Dual weak step $s_0$:** Consider the two lower covers of $v_2$ in $\mathbf{L}$: $u_2$ (just proved) and the right weak lower cover $v_3 := v_2 s_0 = (-1, n, -2, 3, \vec{d})$ (since $-1 + n > 0$). Their reflections $t_{1,4}^+$ and $t_{1,2}^-$ overlap at position $1$. By Lemma 1(2), the only candidates for common lower covers of $u_2$ and $v_3$ are $u_3 := u_2 s_0 = (-1, 3, -2, n, \vec{d})$ (length $\ell(v_2) - 2$) and $v_3 t_{1,4}^+ = (3, n, -2, -1, \vec{d})$, whose length exceeds $\ell(v_3)$ (since $-1 < 3$). Hence $u_3$ is the unique common lower cover, giving $(u_3, v_3) \in E(\mathbf{L})$.
5. **Exclusion at $b_0 := (-1, -2, 3, n, \vec{d})$:** The element $b_0$ has two right weak upper covers $u_3 = b_0 s_2$ and $u_4 := b_0 s_3 = (-1, -2, n, 3, \vec{d})$. By Lemma 1(2), their only common Bruhat upper covers are $v_3 = u_4 s_2$ and $v_4 := u_3 s_3 = (-1, 3, n, -2, \vec{d})$. Since $(u_3, v_3) \in E(\mathbf{L})$ and $(u_4, v_3)$ is weak, Proposition 4.1 forces $u_3 \vee_{\mathbf{L}} u_4 = v_3$; since $(u_3, v_4)$ is also weak, $(u_4, v_4) \notin E(\mathbf{L})$.
6. **Input from $r_1 = s_{n-1}$ in $W_{J_1}$:** Under the isomorphism $\tau: W_{J_1} \xrightarrow{\sim} \mathfrak{S}_n$, $r_1 = s_{n-1}$ means all transpositions in $\{1, \dots, n-1\}$ jump over $n$. Applying $\tau$ to $w_0 := (-2, -1, n, 3, \vec{d}) \to w_1 := (-2, 3, n, -1, \vec{d})$ yields $(2, 1, n, 3, \vec{d}) \to (2, 3, n, 1, \vec{d})$ (swapping $1$ and $3$ across $n$), so $(w_0, w_1) \in E(\mathbf{L})$. Now $u_4 = w_0 s_1$ is a right weak cover of $w_0$, and $t_{2,4}^+$ (for $w_0 \to w_1$) overlaps $s_1 = t_{1,2}^+$ at position $2$. By Lemma 1(2), the only two common Bruhat upper covers of $w_1$ and $u_4$ are $v_4 = w_0 t_{1,2}^+ t_{2,4}^+ = (-1, 3, n, -2, \vec{d})$ and $v_5 := w_0 t_{2,4}^+ t_{1,2}^+ = w_1 s_1 = (3, -2, n, -1, \vec{d})$. Since $(u_4, v_4) \notin E(\mathbf{L})$, Proposition 4.1 forces $(u_4, v_5) \in E(\mathbf{L})$.
7. **Slide $n$ right to position $n$:** Starting from $(u_4, v_5) = ((-1, -2, n, 3, \vec{d}), (3, -2, n, -1, \vec{d}))$, repeatedly take dual weak lower covers $s_3, s_4, \dots, s_{n-1}$ moving $n$ from position $3$ to position $n$:
   - At step $s_3$: $v_5$ has lower covers $u_4 = v_5 t_{1,4}^+$ and the right weak lower cover $v_5 s_3 = v_5 t_{3,4}^+ = (3, -2, -1, n, \vec{d})$, whose reflections overlap at position $4$. By Lemma 1(2), the second candidate is $(v_5 s_3) \cdot t_{1,4}^+ = (3, -2, -1, n, \vec{d}) \cdot t_{1,4}^+ = (n, -2, -1, 3, \vec{d})$, whose length strictly exceeds $\ell(v_5 s_3)$ (since $(v_5 s_3)(1) = 3 < n = (v_5 s_3)(4)$), so it is not a lower cover of $v_5 s_3$. Hence $u_4 s_3 = (-1, -2, 3, n, \vec{d})$ is the unique common Bruhat lower cover of $u_4$ and $v_5 s_3$, giving $((-1, -2, 3, n, \vec{d}), (3, -2, -1, n, \vec{d})) \in E(\mathbf{L})$.
   - At steps $s_4, \dots, s_{n-1}$: supports are disjoint from $\{1, 3\}$ (Lemma 1(1)).
   Thus we derive
   $$u^* := (-1, -2, 3, \vec{d}, n) \longrightarrow v^* := (3, -2, -1, \vec{d}, n) \in E(\mathbf{L}).$$
   Both $u^*, v^*$ lie in $W_{J_{n-1}} = D_{n-1}$, where $r_t = s_0$ gives $\mathbf{L}|_{D_{n-1}} = (\mathbf{L}|_{W_{J_0 \cap J_{n-1}}}) \times {}^{J_0 \cap J_{n-1}} D_{n-1}$. However, $u^* = s_1 \cdot (-2, -1, 3, \vec{d}, n)$ has $W_{J_0 \cap J_{n-1}}$-component $s_1 \neq \mathrm{id}$, whereas $v^*$ has no left descent in $J_0 \cap J_{n-1}$ (its positive entries $3, 4, \dots, n-1$ increase and its negative entries $-2, -1$ increase, so $v^* \in {}^{J_0 \cap J_{n-1}} D_{n-1}$, with $W_{J_0 \cap J_{n-1}}$-component $\mathrm{id}$). Since $s_1 \not\le \mathrm{id}$, $(u^*, v^*) \notin E(\mathbf{L}|_{D_{n-1}})$, contradiction. $\blacksquare$

### 5.2. Lemma 7: Elimination of the Internal Root Case (B2)

**Lemma 7 (No Internal Root $s_{n-2}$).** *For all $n \ge 4$, Case (B2) ($r_0 = r_1 = r_t = s_{n-2}$) is impossible.*

*Proof.* Set $m := n - 1 \ge 3$ and $\vec{r} := (3, 4, \dots, n - 2)$ (empty for $n = 4$). Consider the right weak cover $x \lessdot_R y = x s_2$ where
$$x := (-1, -m, n, 2, \vec{r}), \qquad y := (-1, n, -m, 2, \vec{r}).$$
Define three strict Bruhat upper covers of $x$ and three strict Bruhat lower covers of $y$:
$$\begin{aligned}
E_1: &\; x \longrightarrow e_1 := (n, -m, -1, 2, \vec{r}) && (t_{1,3}^+), &
F_1: &\; f_1 := (-m, n, -1, 2, \vec{r}) \longrightarrow y && (t_{1,3}^+), \\
E_2: &\; x \longrightarrow e_2 := (-n, -m, 1, 2, \vec{r}) && (t_{1,3}^-), &
F_2: &\; f_2 := (m, n, 1, 2, \vec{r}) \longrightarrow y && (t_{1,3}^-), \\
E_3: &\; x \longrightarrow e_3 := (-1, 2, n, -m, \vec{r}) && (t_{2,4}^+), &
F_3: &\; f_3 := (-1, 2, -m, n, \vec{r}) \longrightarrow y && (t_{2,4}^+).
\end{aligned}$$
We establish three claims, which together give an immediate pigeonhole contradiction:

**Claim 1 ($E_1, E_2, E_3$ are pairwise mutually exclusive).** By Lemma 1(1), each pair among $\{e_1, e_2, e_3\}$ has at most one candidate common Bruhat upper cover $x r_i r_j$:
- $e_1, e_2$: $w := x t_{1,3}^+ t_{1,3}^- = e_1 t_{1,3}^- = (1, -m, -n, 2, \vec{r})$. Relative to $e_1 = (n, -m, -1, 2, \vec{r})$, applying $t_{1,3}^-$ replaces $(n, -1)$ by $(1, -n)$ across $-m$: pair $(1, 3)$ contributes $+1$ (since $n > -1$ and $n - 1 > 0$ before, whereas $1 > -n$ and $1 - n < 0$ after), position $2$ (value $-m$) contributes $+2$ (before: $n > -m$, $-m < -1$, $n - m = 1 > 0$, $-m - 1 < 0$, contributing $1 + 1 = 2$; after: $1 > -m > -n$, $1 - m < 0$, $-m - n < 0$, contributing $2 + 2 = 4$), and every position $k \ge 4$ (value $v \in \{2, \dots, n - 2\}$) contributes $0$ (before: $n > v$ and $-1 < v$ with both sums positive, contributing $1 + 0 = 1$; after: $1 < v$ and $-n < v$ with $-n + v < 0 < 1 + v$, contributing $0 + 1 = 1$). Hence $\ell(w) = \ell(e_1) + 3 = \ell(x) + 4 > \ell(x) + 2$.
- $e_1, e_3$: $x t_{1,3}^+ t_{2,4}^+ = (n, 2, -1, -m, \vec{r})$. Applying $t_{2,4}^+$ to $e_1 = (n, -m, -1, 2, \vec{r})$ swaps $-m$ and $2$ across $-1 \in (-m, 2)$, adding $\ge +3$ to length, so $\ell(x t_{1,3}^+ t_{2,4}^+) \ge \ell(x) + 4 > \ell(x) + 2$.
- $e_2, e_3$: $x t_{1,3}^- t_{2,4}^+ = (-n, 2, 1, -m, \vec{r})$. Applying $t_{2,4}^+$ to $e_2 = (-n, -m, 1, 2, \vec{r})$ swaps $-m$ and $2$ across $1 \in (-m, 2)$, adding $\ge +3$ to length, so $\ell(x t_{1,3}^- t_{2,4}^+) \ge \ell(x) + 4 > \ell(x) + 2$.

Thus no two of $\{e_1, e_2, e_3\}$ share a common Bruhat upper cover; by Proposition 4.1, **at most one** of $E_1, E_2, E_3$ lies in $E(\mathbf{L})$.

**Claim 2 ($E_i \oplus F_i$ for each $i \in \{1, 2, 3\}$).** Consider the three bases $b_1 := (-m, -1, n, 2, \vec{r})$, $b_2 := (m, 1, n, 2, \vec{r})$, and $b_3 := (-1, -m, 2, n, \vec{r})$. Each $b_i$ has two right weak upper covers $x$ and $f_i$ (via $(s_1, s_2)$, $(s_0, s_2)$, and $(s_3, s_2)$ respectively). By Lemma 1(2), the only two common Bruhat upper covers of $x$ and $f_i$ are $e_i$ (weak from $f_i$, strict $E_i$ from $x$) and $y$ (weak from $x$, strict $F_i$ from $f_i$). By Proposition 4.1, $x \vee_{\mathbf{L}} f_i \in \{e_i, y\}$, so exactly one of $E_i, F_i$ lies in $E(\mathbf{L})$. Combining with Claim 1, **at least two** of $F_1, F_2, F_3$ lie in $E(\mathbf{L})$.

**Claim 3 ($F_1, F_2, F_3$ are pairwise mutually exclusive under Case (B2)).** By Lemma 1(1), each pair among $\{f_1, f_2, f_3\}$ has a unique common Bruhat lower cover below $y$:
- If $F_1, F_2 \in E(\mathbf{L})$: their unique common lower cover is $c_{12} := y t_{1,3}^+ t_{1,3}^- = (1, n, m, 2, \vec{r})$, forcing $(c_{12}, f_2) = ((1, n, m, 2, \vec{r}), (m, n, 1, 2, \vec{r})) \in E(\mathbf{L})$. Both endpoints lie in $W_{J_0} = \mathfrak{S}_n$, swapping $1$ and $m = n - 1$ across $n$. Since $r_0 = s_{n-2}$, the root $n - 2$ of the binary tree of $\mathbf{L}|_{W_{J_0}}$ separates $\{1, \dots, n-2\}$ from $\{n-1, n\}$, so $(1, n-1)$ lies in the root rectangle with interval $[1, n]$; by Proposition 3.8 (`pr:covers`), $(1, n-1)$ cannot jump over $n$, contradicting $(c_{12}, f_2) \in E(\mathbf{L}|_{W_{J_0}})$.
- If $F_1, F_3 \in E(\mathbf{L})$: their unique common lower cover is $c_{13} := y t_{1,3}^+ t_{2,4}^+ = (-m, 2, -1, n, \vec{r})$, forcing $(c_{13}, f_1) = ((-m, 2, -1, n, \vec{r}), (-m, n, -1, 2, \vec{r})) \in E(\mathbf{L})$. Both endpoints lie in $W_{J_1}$, and conjugating by $\tau$ gives $(m, 2, 1, n, \vec{r}) \to (m, n, 1, 2, \vec{r})$ in $\mathfrak{S}_n$, swapping $2$ and $n$ across $1$. Since $r_1 = s_{n-2}$, $(2, n)$ lies in the root rectangle with interval $[1, n]$ (as $2 \le n - 2 < n$), so by Proposition 3.8 it cannot jump over $1$, contradiction.
- If $F_2, F_3 \in E(\mathbf{L})$: their unique common lower cover is $c_{23} := y t_{1,3}^- t_{2,4}^+ = (m, 2, 1, n, \vec{r})$, forcing $(c_{23}, f_3) = ((m, 2, 1, n, \vec{r}), (-1, 2, -m, n, \vec{r})) \in E(\mathbf{L})$. Applying dual right weak lower covers $s_4, s_5, \dots, s_{n-1}$ (each having support disjoint from $\{1, 3\}$, so unique common lower cover by Lemma 1(1)) slides $n$ from position $4$ to position $n$, yielding
  $$u^* := (m, 2, 1, \vec{r}, n) \longrightarrow v^* := (-1, 2, -m, \vec{r}, n) \in E(\mathbf{L}).$$
  Both $u^*, v^*$ lie in $W_{J_{n-1}} = D_{n-1}$, where $r_t = s_{n-2}$ gives $\mathbf{L}|_{D_{n-1}} = (\mathbf{L}|_{W_K}) \times {}^K D_{n-1}$ with $K := \{s_0, s_1, \dots, s_{n-3}\}$. Now $s_1 \in K$ is a left descent of $u^*$ (swapping values $1$ and $2$ decreases length), so $u^*_K \neq \mathrm{id}$. By contrast, $v^*$ has no left descent in $K$: left multiplication by $s_0$ turns $(-1, 2)$ into $(2, -1)$ (increasing length by $1$); left multiplication by $s_1$ turns $(-1, 2)$ into $(-2, 1)$ (increasing length by $1$ since $-1 + 2 > 0 > -2 + 1$); and left multiplication by $s_i$ ($2 \le i \le n - 3$) swaps positive values $i, i + 1$ appearing in increasing order (increasing length by $1$). Thus $v^* \in {}^K D_{n-1}$, so $v^*_K = \mathrm{id}$, contradicting $u^*_K \le v^*_K$.

By Claim 3, **at most one** of $F_1, F_2, F_3$ lies in $E(\mathbf{L})$, contradicting Claim 2 ($2 \le 1$). $\blacksquare$

---

## 6. Splitting in Case (G2): The Vector Quotient ${}^{J_{n-1}} D_n$

In Case (G2), we have $r_0 = r_1 = s_{n-1}$. We prove $\mathbf{L} = (\mathbf{L}|_{W_{J_{n-1}}}) \times {}^{J_{n-1}} D_n$ via Corollary 4.

First, we describe ${}^{J_{n-1}} D_n$ explicitly. An element $q \in D_n$ has no left descent in $J_{n-1} = \{s_0, s_1, \dots, s_{n-2}\}$ iff the values $1, 2, \dots, n - 1$ appear in increasing order with positive signs, except that value $1$ is negated iff value $n$ is negated (to keep an even number of minus signs). Thus $|{}^{J_{n-1}} D_n| = 2n$, consisting of:
- $q_k^+ := (1, \dots, k - 1, n, k, \dots, n - 1)$ for $k = n, n - 1, \dots, 1$ (length $n - k$), all lying in $W_{J_0}$;
- $q_1^- := (-n, -1, 2, 3, \dots, n - 1)$ (length $n - 1$), lying in $W_{J_1}$;
- $q_k^- := (-1, 2, \dots, k - 1, -n, k, \dots, n - 1)$ for $k = 2, 3, \dots, n$ (length $n + k - 2$).

The Hasse diagram of ${}^{J_{n-1}} D_n$ is the chain $q_n^+ \lessdot_R \dots \lessdot_R q_2^+$, branching to $\{q_1^+, q_1^-\}$, joining at $q_2^- = q_1^+ s_0 = q_1^- s_1$, followed by the chain $q_2^- \lessdot_R q_3^- \lessdot_R \dots \lessdot_R q_n^- = {}^{J_{n-1}} w_0$. In particular:
- All join-irreducibles $q_k^+$ ($1 \le k \le n - 1$) lie in $W_{J_0}$ (where $r_0 = s_{n-1}$ gives $[\mathrm{id}, q_k^+]_{\mathbf{L}} = [\mathrm{id}, q_k^+]_R$);
- The join-irreducible $q_1^-$ lies in $W_{J_1}$ (where $r_1 = s_{n-1}$ gives $[\mathrm{id}, q_1^-]_{\mathbf{L}} = [\mathrm{id}, q_1^-]_R$);
- $q_2^-$ is not join-irreducible (it covers both $q_1^+$ and $q_1^-$).

The **only** remaining elements of $\mathcal{J}({}^{J_{n-1}} D_n)$ to check for Corollary 4 are $q_k^-$ for $k = 3, 4, \dots, n$.

**Lemma 8 (Case (G2) Splitting).** *For all $n \ge 4$, if $r_0 = r_1 = s_{n-1}$, then $\mathbf{L} = (\mathbf{L}|_{W_{J_{n-1}}}) \times {}^{J_{n-1}} D_n$.*

*Proof.* By Corollary 4, it suffices to verify for each $k \in \{3, \dots, n\}$ that if $[\mathrm{id}, q_{k-1}^-]_{\mathbf{L}} = [\mathrm{id}, q_{k-1}^-]_R$, then $q_{k-1}^-$ is the unique lower cover of $q_k^-$ in $\mathbf{L}$. Suppose $y \lessdot_{\mathbf{L}} q_k^-$ with $y \neq q_{k-1}^-$. By Proposition 4.1, $c := y \wedge_{\mathbf{L}} q_{k-1}^-$ must be a lower cover of $q_{k-1}^-$ in $\mathbf{L}$, hence a right weak lower cover of $q_{k-1}^-$ in ${}^{J_{n-1}} D_n$. By the diamond property of Bruhat order (every length-$2$ Bruhat interval $[c, q_k^-]$ has cardinality $4$), $y$ is uniquely determined by $c$.

**Subcase $k = 3$:** $q_2^- = (-1, -n, 2, 3, \dots, n-1)$ has exactly two lower covers in ${}^{J_{n-1}} D_n$: $c_1 = q_1^+$ and $c_2 = q_1^-$.
- If $c = q_1^+ = (n, 1, 2, 3, \dots, n - 1)$: since $q_2^- = q_1^+ s_0$ and $q_3^- = q_1^+ s_0 s_2$, the unique other intermediate element is $y_1 := q_1^+ s_2 = (n, 2, 1, 3, \dots, n - 1)$. We rule out $(y_1, q_3^-) \in E(\mathbf{L})$ in three steps:
  1. In $W_{J_0}$, since $r_0 = s_{n-1}$, Proposition 3.8 gives $((1, n, 2, 3, \dots, n - 1), (2, n, 1, 3, \dots, n - 1)) \in E(\mathbf{L})$.
  2. Weak step $s_0$: by Lemma 1(2), the unique common Bruhat upper cover of $(2, n, 1, 3, \dots, n - 1)$ and $(-n, -1, 2, 3, \dots, n - 1)$ is $(-n, -2, 1, 3, \dots, n - 1)$, since the second candidate applies $t_{1,3}^+$ to $(-n, -1, 2, 3, \dots, n - 1)$, swapping $-n$ and $2$ across $-1 \in (-n, 2)$ (increasing length by $\ge 3$). Hence $((-n, -1, 2, 3, \dots, n - 1), (-n, -2, 1, 3, \dots, n - 1)) \in E(\mathbf{L})$.
  3. Weak step $s_1$: note that $(-n, -1, 2, 3, \dots, n - 1) \to (-n, -2, 1, 3, \dots, n - 1)$ uses $t_{2,3}^-$, overlapping $s_1 = t_{1,2}^+$ at position $2$. By Lemma 1(2), the unique common Bruhat upper cover of $(-n, -2, 1, 3, \dots, n - 1)$ and $q_2^- = (-1, -n, 2, 3, \dots, n - 1)$ is $z_1 := (-2, -n, 1, 3, \dots, n - 1)$, since the second candidate $q_2^- t_{2,3}^- = (-1, -2, n, 3, \dots, n - 1)$ has length strictly smaller than $\ell(q_2^-)$ (as $-n + 2 < 0$).
  Thus $(q_2^-, z_1) \in E(\mathbf{L})$. Now observe that $y_1 s_0 = (-2, -n, 1, 3, \dots, n - 1) = z_1$ is a right weak cover of $y_1$. If $(y_1, q_3^-) \in E(\mathbf{L})$, then $z_1$ and $q_3^-$ would share two distinct common lower covers ($q_2^-$ and $y_1$) in $\mathbf{L}$, violating Proposition 4.1 (uniqueness of meets).
- If $c = q_1^-$: symmetric via the diagram automorphism $\tau$ ($s_0 \leftrightarrow s_1$, which swaps $q_1^+ \leftrightarrow q_1^-$ and fixes $q_2^-, q_3^-$).

**Subcase $4 \le k \le n$:** Put $m := k - 1 \in \{3, \dots, n - 1\}$. Now $q_{k-1}^-$ has unique ${}^{J_{n-1}} D_n$-lower cover $c = q_{k-2}^-$, with $q_{k-1}^- = c s_{m-1}$ and $q_k^- = c s_{m-1} s_m$, so the unique candidate is
$$y_k := c s_m = (-1, 2, \dots, m - 2, -n, m, m - 1, m + 1, \dots, n - 1).$$
For each $j \in \{2, 3, \dots, m - 1\}$, write $\vec{p}_j := (-1, 2, \dots, j - 1)$ and $\vec{s}_j := (j + 1, \dots, m - 1, m + 1, \dots, n - 1)$, and define
$$u_j := (\vec{p}_j, -n, m, j, \vec{s}_j), \qquad v_j := (\vec{p}_j, j, m, -n, \vec{s}_j),$$
$$a_2 := (-m, -n, 1, 2, \vec{s}_2), \qquad a_j := (-1, 2, \dots, j - 2, m, -n, j - 1, j, \vec{s}_j) \quad (j \ge 3).$$
Notice $u_{m-1} = y_k$ and $v_{m-1} = q_k^-$. We show by induction on $j = 2, \dots, m - 1$ that $(u_j, a_j) \in E(\mathbf{L})$ and consequently $(u_j, v_j) \notin E(\mathbf{L})$:
- **Base $j = 2$ ($(u_2, a_2) \in E(\mathbf{L})$):** In $W_{J_0}$, $r_0 = s_{n-1}$ gives $((1, n, m, 2, \vec{s}_2), (m, n, 1, 2, \vec{s}_2)) \in E(\mathbf{L})$ (swapping $1$ and $m$ across $n$). Applying weak step $s_0$ yields $((-n, -1, m, 2, \vec{s}_2), (-n, -m, 1, 2, \vec{s}_2)) \in E(\mathbf{L})$ (by Lemma 1(2), the other candidate swaps $-n$ and $m$ across $-1 \in (-n, m)$, length $\ge +3$). Applying weak step $s_1$ (note $r_L = t_{2,3}^-$!) yields $(u_2, a_2) \in E(\mathbf{L})$ (the other candidate applies $t_{2,3}^-$ to $u_2$, decreasing length since $-n + m < 0$).
- **Mutual exclusion $(u_j, a_j) \in E(\mathbf{L}) \implies (u_j, v_j) \notin E(\mathbf{L})$:**
  - For $j = 2$: $u_2 \to a_2$ uses $t_{1,3}^-$ and $u_2 \to v_2$ uses $t_{2,4}^+$, which have disjoint supports. By Lemma 1(1), their only candidate common upper cover is $u_2 t_{1,3}^- t_{2,4}^+ = (-m, 2, 1, -n, \vec{s}_2)$, obtained from $a_2 = (-m, -n, 1, 2, \vec{s}_2)$ by swapping $-n$ and $2$ across $1 \in (-n, 2)$, which increases length by $\ge 3$.
  - For $j \ge 3$: $u_j \to a_j$ uses $t_{j-1, j+1}^+$ and $u_j \to v_j$ uses $t_{j, j+2}^+$, which have disjoint supports. By Lemma 1(1), their only candidate common upper cover is $u_j t_{j-1, j+1}^+ t_{j, j+2}^+ = (\dots, m, j, j - 1, -n, \vec{s}_j)$, obtained from $a_j = (\dots, m, -n, j - 1, j, \vec{s}_j)$ by swapping $-n$ and $j$ across $j - 1 \in (-n, j)$, which increases length by $\ge 3$.
  Hence $a_j$ and $v_j$ have zero common Bruhat upper covers, so Proposition 4.1 yields $(u_j, v_j) \notin E(\mathbf{L})$.
- **Inductive step ($j \to j + 1$ for $j < m - 1$):** Set $w_j := (\vec{p}_j, -n, j, m, \vec{s}_j)$. Its two right weak upper covers $u_j = w_j s_{j+1}$ and $u_{j+1} = w_j s_j$ have, by Lemma 1(2), exactly two common Bruhat upper covers: $v_j = u_{j+1} s_{j+1}$ and $a_{j+1} = u_j s_j$. Since $(u_j, v_j) \notin E(\mathbf{L})$, Proposition 4.1 forces $(u_{j+1}, a_{j+1}) \in E(\mathbf{L})$.

At $j = m - 1$, this yields $(y_k, q_k^-) = (u_{m-1}, v_{m-1}) \notin E(\mathbf{L})$. By Corollary 4, $\mathbf{L} = (\mathbf{L}|_{W_{J_{n-1}}}) \times {}^{J_{n-1}} D_n$. $\blacksquare$

---

## 7. Splitting in Case (G1): The Spin Quotient ${}^{J_0} D_n$

In Case (G1), we have $r_t = r_1 = s_0$ (Case (G1') is identical via $\tau$). We prove $\mathbf{L} = (\mathbf{L}|_{W_{J_0}}) \times {}^{J_0} D_n$ via Corollary 4.

### 7.1. Explicit Structure of ${}^{J_0} D_n$ and Its Join-Irreducibles

An element $q \in D_n$ has no left descent in $J_0 = \{s_1, \dots, s_{n-1}\}$ iff $\ell(s_k q) > \ell(q)$ for every $k \in \{1, \dots, n - 1\}$. Comparing $q$ and $s_k q$ via the length formula:
- if $k$ and $k + 1$ have the same sign, they must appear in increasing signed order;
- if $k$ is positive and $k + 1$ is negative, swapping them always decreases length (for both orders of positions, since $k + (-(k+1)) = -1 < 0 < (k+1) + (-k)$);
- if $k$ is negative and $k + 1$ is positive, swapping them always increases length.

Thus $q \in {}^{J_0} D_n$ iff its negative entries are $\{-2r, -(2r - 1), \dots, -1\}$ (for some even $2r \in \{0, 2, \dots, n\}$) placed in increasing signed order from left to right, and its positive entries are $\{2r + 1, \dots, n\}$ placed in increasing order from left to right. Hence ${}^{J_0} D_n$ is in bijection with even-sized subsets $A \subseteq \{1, \dots, n\}$ (the positions carrying negative entries), written $q = q(A)$.

For nonempty $A \subseteq \{1, \dots, n\}$ of even size, the right weak lower covers of $q(A)$ inside ${}^{J_0} D_n$ are:
- $q(A) s_p$ for each $p \in \{1, \dots, n - 1\}$ with $p + 1 \in A$ and $p \notin A$ (moving a run start $> 1$ left by $1$);
- $q(A) s_0$ if $\{1, 2\} \subseteq A$ (removing $\{1, 2\}$ from $A$).

Therefore $q(A) \in \mathcal{J}({}^{J_0} D_n)$ (exactly one weak lower cover inside ${}^{J_0} D_n$) iff:
- $A = \{j, j + 1, \dots, j + a - 1\}$ ($a$ even, $j \ge 2$); or
- $A = \{1\} \cup \{j, j + 1, \dots, j + a - 1\}$ ($a$ odd, $j \ge 3$); or
- $A = \{1, 2, \dots, 2r\}$ ($r \ge 1$).

Now $q(A) \in W_{J_{n-1}}$ iff $n \notin A$ (where $r_t = s_0$ already gives $[\mathrm{id}, q(A)]_{\mathbf{L}} = [\mathrm{id}, q(A)]_R$), and $q(\{1, n\}) = (-2, 3, \dots, n, -1) \in W_{J_1}$ (where $r_1 = s_0$ already gives $[\mathrm{id}, q(\{1, n\})]_{\mathbf{L}} = [\mathrm{id}, q(\{1, n\})]_R$). Thus the **only** elements of $\mathcal{J}({}^{J_0} D_n)$ outside $W_{J_{n-1}} \cup W_{J_1}$ are the $n - 2$ elements $q_{(a, n)}$ for $2 \le a \le n - 1$:
- **For even $a \in \{2, \dots, n - 1\}$** ($A = \{n - a + 1, \dots, n\}$):
  $$q_{(a, n)} = (a + 1, \dots, n, -a, -(a - 1), \dots, -1).$$
- **For odd $a \in \{3, \dots, n - 2\}$** ($A = \{1\} \cup \{n - a + 1, \dots, n\}$):
  $$q_{(a, n)} = (-(a + 1), a + 2, \dots, n, -a, -(a - 1), \dots, -1).$$
- **For odd $a = n - 1$ ($n$ even)** ($A = \{1, 2, \dots, n\}$):
  $$q_{(n-1, n)} = (-n, -(n - 1), \dots, -1).$$

### 7.2. Lemma 9: Universal Spin-Quotient Propagation

**Lemma 9 (Universal Spin-Quotient Propagation).**
*Let $n \ge 4$, $u \in {}^{J_0} D_n$, $k \in \{1, \dots, n - 1\}$ (so $s_k \in J_0$), and $t \in S$ such that $u \lessdot_R u t$ in ${}^{J_0} D_n$. If $(u, s_k u)$ is a **strict** Bruhat cover, then $s_k u t$ is the **unique** common Bruhat upper cover of $s_k u$ and $u t$ in $D_n$. In particular, $(u, s_k u) \in E(\mathbf{L}) \implies (u t, s_k u t) \in E(\mathbf{L})$.*

*Proof.* Write $s_k u = u r_L$, where $r_L = u^{-1} s_k u$ acts on the two positions $p_1 < p_2$ of values $\{\pm k, \pm(k + 1)\}$ in $u$, and let $2r$ be the number of negative entries of $u$. Because $u t \in {}^{J_0} D_n$ and $s_k \in J_0$, $\ell(s_k u t) = \ell(u t) + 1 = \ell(u) + 2$, so $s_k u t = u r_L t$ is always a common Bruhat upper cover of $s_k u$ and $u t$. If $\mathrm{supp}(r_L) \cap \mathrm{supp}(t) = \emptyset$ or $\mathrm{supp}(r_L) = \mathrm{supp}(t)$, uniqueness holds immediately by Lemma 1(1).

Assume $|\mathrm{supp}(r_L) \cap \mathrm{supp}(t)| = 1$. By Lemma 1(2), the only possible second common upper cover is $w := u t r_L$; we verify $\ell(w) \neq \ell(u t) + 1$ in all cases:
1. **$t = s_0 = t_{1,2}^-$:** Then $u(1) = 2r + 1$, $u(2) = 2r + 2$, and $(u t)(1) = -(2r + 2)$, $(u t)(2) = -(2r + 1)$.
   - If $k = 2r$: $p_1 = 1$, $p_2 > 2$, $u(p_2) = -2r$, $r_L = t_{1, p_2}^-$. In $u t$, $(u t)(1) + (u t)(p_2) = -(2r + 2) - 2r < 0$, so $\ell(u t r_L) < \ell(u t)$.
   - If $k = 2r + 2$: $p_1 = 2$, $u(p_2) = 2r + 3$, $r_L = t_{2, p_2}^+$. Since $(u, s_k u)$ is strict, $p_2 \ge 4$, so position $3$ holds a negative entry $-c \in \{-2r, \dots, -1\}$. In $u t$, $(u t)(2) = -(2r + 1) < -c < 2r + 3 = (u t)(p_2)$, so swapping $(2, p_2)$ jumps over $-c$ and gives $\ell(u t r_L) \ge \ell(u t) + 3$.
2. **$t = s_p = t_{p, p+1}^+$ ($1 \le p \le n - 1$):** Then $u(p) = -x < 0$, $u(p + 1) = y > 0$ ($1 \le x \le 2r < y \le n$), and $(u t)(p) = y$, $(u t)(p + 1) = -x$.
   - *(a) $x = k \le 2r - 1$:* $p_2 = p$, $u(p_1) = -(k + 1)$, $r_L = t_{p_1, p}^+$. Since $(u, s_k u)$ is strict, $p_1 \le p - 2$, so position $p_1 + 1$ holds a positive entry $z \in \{2r + 1, \dots, y - 1\}$. In $u t$, $-(k + 1) < z < y$, giving $\ell(u t r_L) \ge \ell(u t) + 3$.
   - *(b) $x = k = 2r$:* Since $|\mathrm{supp}(r_L) \cap \{p, p + 1\}| = 1$, $y \neq 2r + 1$, so $y \ge 2r + 2$; thus $+(2r + 1)$ lies to the left of $y$, i.e., $p_1 < p = p_2$ and $r_L = t_{p_1, p}^-$. Since $+(2r + 1)$ is the leftmost positive entry and $-2r$ is the leftmost negative entry of $u$, we must have $p_1 = 1$. Since $(u, s_{2r} u)$ is strict, $\{p_1, p\} \neq \{1, 2\}$, so $p \ge 3$. Thus position $2$ holds a positive entry $z$ with $2r + 1 < z < y$. Applying $t_{1, p}^-$ to $u t$ replaces $(2r + 1, y)$ by $(-y, -(2r + 1))$: relative to $z$ at position $2$, before we have $2r + 1 < z < y$ and both sums $> 0$ (contribution $0$), whereas after we have $z > -(2r + 1)$ and $-y + z < 0$ (contribution $+2$). Adding $+1$ from $(1, p)$ itself gives $\ell(u t r_L) \ge \ell(u t) + 3$.
   - *(c) $x = k + 1 \le 2r$:* $p_1 = p$, $p_2 > p + 1$, $u(p_2) = -k$, $r_L = t_{p, p_2}^+$. In $u t$, $(u t)(p) = y > -k = (u t)(p_2)$, so $\ell(u t r_L) < \ell(u t)$.
   - *(d) $y = k \ge 2r + 1$:* $p_1 = p + 1$, $u(p_2) = k + 1$, $r_L = t_{p+1, p_2}^+$. Since $(u, s_k u)$ is strict, $p_2 \ge p + 3$, so position $p + 2$ holds a negative entry $-c \in \{-x + 1, \dots, -1\}$. In $u t$, $-x < -c < k + 1$, giving $\ell(u t r_L) \ge \ell(u t) + 3$.
   - *(e) $y = k + 1 \ge 2r + 2$:* $p_2 = p + 1$, $p_1 < p$, $u(p_1) = k$, $r_L = t_{p_1, p+1}^+$. In $u t$, $(u t)(p_1) = k > -x = (u t)(p + 1)$, so $\ell(u t r_L) < \ell(u t)$.
   - *(f) $y = k + 1 = 2r + 1$:* Then $k = 2r$, $x \neq 2r$, $p_1 = 1$ holds $-2r$, $p_2 = p + 1 \ge 3$, $r_L = t_{1, p+1}^-$. In $u t$, $(u t)(1) + (u t)(p + 1) = -2r - x < 0$, so $\ell(u t r_L) < \ell(u t)$.

In every case $\ell(u t r_L) \neq \ell(u) + 2$, completing the proof. $\blacksquare$

### 7.3. Lemma 10: Case (G1) Splitting

**Lemma 10 (Case (G1) Splitting).** *For all $n \ge 4$, if $r_t = r_1 = s_0$, then $\mathbf{L} = (\mathbf{L}|_{W_{J_0}}) \times {}^{J_0} D_n$.*

*Proof.* By Corollary 4 and Section 7.1, it suffices to verify for each $a \in \{2, \dots, n - 1\}$ that if $[\mathrm{id}, q']_{\mathbf{L}} = [\mathrm{id}, q']_R$ for the unique ${}^{J_0} D_n$-lower cover $q'$ of $q := q_{(a, n)}$, then $q'$ is the unique lower cover of $q$ in $\mathbf{L}$. As in Lemma 8, any other lower cover $y \lessdot_{\mathbf{L}} q$ satisfies $c := y \wedge_{\mathbf{L}} q' \lessdot_R q'$ inside ${}^{J_0} D_n$, which uniquely determines $y$ via the length-$2$ Bruhat interval $[c, q]$.

**Part 1: $2 \le a \le n - 2$.**
Here $q' = q_{(a, n)} s_{n-a}$ moves the negative run start $n - a + 1$ left by $1$:
$$q' = (\vec{p}, n - 1, -a, n, -(a - 1), \dots, -1) \quad (\text{if } a \text{ even or } a \le n - 3 \text{ odd}),$$
$$q' = (-(n - 1), -(n - 2), n, -(n - 3), \dots, -1) \quad (\text{if } a = n - 2 \text{ odd}),$$
where $\vec{p} = (a + 1, \dots, n - 2)$ for $a$ even and $\vec{p} = (-(a + 1), a + 2, \dots, n - 2)$ for $a$ odd. From Section 7.1, $q'$ has exactly two weak lower covers $c_A, c_B$ in ${}^{J_0} D_n$:

- **Candidate $y_A$ (from $c_A$):**
  - If $a$ is even or $a \le n - 3$ is odd: $q' = c_A s_{n-a-1}$, $q = c_A s_{n-a-1} s_{n-a}$, $y_A = c_A s_{n-a}$, and the other common upper cover of $q'$ and $y_A$ is $c_A s_{n-a} s_{n-a-1} = s_{n-1} q'$.
  - If $a = n - 2$ is odd: $c_A = (n - 2, n - 1, n, -(n - 3), \dots, -1)$, $q' = c_A s_0$, $q = c_A s_0 s_2$, $y_A = c_A s_2$, and the other common upper cover of $q'$ and $y_A$ is $c_A s_2 s_0 = (-n, -(n - 2), n - 1, -(n - 3), \dots, -1) = s_{n-1} q'$.

  In both cases, $(y_A, s_{n-1} q')$ is a right weak cover, so by Proposition 4.1 on $c_A$, proving $(q', s_{n-1} q') \in E(\mathbf{L})$ forces $q' \vee_{\mathbf{L}} y_A = s_{n-1} q' \neq q$, hence $(y_A, q) \notin E(\mathbf{L})$. To prove $(q', s_{n-1} q') \in E(\mathbf{L})$, start at
  $$u_0 := (-2, 3, 4, \dots, n - 1, -1, n) \in {}^{J_0} D_n \cap W_{J_1}.$$
  Since $r_1 = s_0$, $\mathbf{L}|_{W_{J_1}} = (\mathbf{L}|_{W_{J_0 \cap J_1}}) \times {}^{J_0 \cap J_1} W_{J_1}$; because $u_0 \in {}^{J_0 \cap J_1} W_{J_1}$ and $s_{n-1} \in J_0 \cap J_1$, we have $(u_0, s_{n-1} u_0) \in E(\mathbf{L})$. Now define $q_{\mathrm{mid}} := (\dots, -a, -(a - 1), \dots, -1, n)$ obtained from $q'$ by sliding $+n$ right past $-(a - 1), \dots, -1$ to position $n$. Both $u_0$ and $q_{\mathrm{mid}}$ lie in ${}^{J_0 \cap J_{n-1}} D_{n-1}$ with $u_0 \le_R q_{\mathrm{mid}}$ (the negative position set $\{1, n - 1\}$ of $u_0$ reaches that of $q_{\mathrm{mid}}$ while keeping $-1$ fixed at position $n - 1$). Along any right weak chain $u_0 \lessdot_R \dots \lessdot_R q_{\mathrm{mid}}$ in ${}^{J_0 \cap J_{n-1}} D_{n-1}$, $-1$ stays at position $n - 1$ and $+n$ stays at position $n$, so $-1$ always separates $\pm(n - 1)$ from $+n$; hence $(u, s_{n-1} u)$ is strict at every step. Next, sliding $+n$ left past $-1, \dots, -(a - 1)$ from $q_{\mathrm{mid}}$ to $q'$ keeps $-a$ strictly between $\pm(n - 1)$ and $+n$ at every step, so $(u, s_{n-1} u)$ remains strict throughout. Applying Lemma 9 at each step gives $(q', s_{n-1} q') \in E(\mathbf{L})$, ruling out $(y_A, q)$.

- **Candidate $y_B$ (from $c_B$):**
  For every $2 \le a \le n - 2$, $q' = c_B s_{n-a+1}$, $q = c_B s_{n-a+1} s_{n-a}$, $y_B = c_B s_{n-a}$, and the other common upper cover of $q'$ and $y_B$ is $c_B s_{n-a} s_{n-a+1} = s_{a-1} q'$ (weak from $y_B$). Thus it suffices to prove $(q', s_{a-1} q') \in E(\mathbf{L})$. We construct an explicit right weak chain in ${}^{J_0} D_n$ from a starting element $u_0 \in {}^{J_0} D_{n-1} \subseteq W_{J_{n-1}}$ to $q'$ along which $(u, s_{a-1} u)$ is strict at every step (since $r_t = s_0$ and $s_{a-1} \in J_0 \cap J_{n-1}$, $(u_0, s_{a-1} u_0) \in E(\mathbf{L}|_{D_{n-1}})$ automatically):
  - *If $a = 2$ ($k = 1$):* Start at $u_0 := (-2, 3, -1, 4, \dots, n - 1, n)$ ($3$ separates $-2, -1$). Slide $-1$ right past $4, \dots, n$ to $(-2, 3, \dots, n, -1)$, then slide $-2$ right past $3, \dots, n - 1$ to $q' = (3, \dots, n - 1, -2, n, -1)$. At every step at least one positive entry separates $-2$ and $-1$.
  - *If $a \ge 3$ is odd ($k = a - 1$):* Start at $u_0 := (a, a + 1, \dots, n - 1, -(a - 1), \dots, -1, n)$ ($a + 1, \dots, n - 1$ is nonempty since $a \le n - 2$, separating $+a$ and $-(a - 1)$). Slide $+n$ left past $-1, \dots, -(a - 1)$, apply $s_0$ to $(a, a + 1) \mapsto (-(a + 1), -a)$, and slide $-a$ right past $a + 2, \dots, n - 1$ to $q'$. At every step at least one entry (ultimately $+n$) separates $\pm a$ and $-(a - 1)$.
  - *If $a \ge 4$ is even ($k = a - 1$):* Start at $u_0 := (-a, a + 1, \dots, n - 1, -(a - 1), \dots, -1, n)$ ($a + 1, \dots, n - 1$ is nonempty, separating $-a$ and $-(a - 1)$). Slide $+n$ left past $-1, \dots, -(a - 1)$, then slide $-a$ right past $a + 1, \dots, n - 1$ to $q'$. Again at least one positive entry separates $-a$ and $-(a - 1)$ at every step.

  Applying Lemma 9 along this chain yields $(q', s_{a-1} q') \in E(\mathbf{L})$, ruling out $(y_B, q)$.

**Part 2: The top element $a = n - 1$ ($q = {}^{J_0} w_0$).**
Here $q'$ has a **unique** weak lower cover $c$ in ${}^{J_0} D_n$, yielding a single candidate $y$.

- **Subcase 2a ($n$ odd, $n \ge 5$):** We have $q = (n, -(n - 1), \dots, -1)$, $q' = (-(n - 1), n, -(n - 2), \dots, -1)$, $c = (-(n - 1), -(n - 2), n, -(n - 3), \dots, -1)$, and $y = c s_1 = (-(n - 2), -(n - 1), n, -(n - 3), \dots, -1)$.
  Start in $W_{J_{n-1}} = D_{n-1}$ with
  $$u_0 := (n - 1, n - 2, -(n - 3), \dots, -1, n) \longrightarrow v_0 := (n - 3, n - 2, -(n - 1), -(n - 4), \dots, -1, n).$$
  Set $q^* := (n - 2, n - 1, -(n - 3), \dots, -1, n) \in {}^{J_0 \cap J_{n-1}} D_{n-1}$; then $u_0 = s_{n-2} q^*$ and $v_0 = (s_{n-2} s_{n-3}) q^*$. Since $s_{n-2} \lessdot_R s_{n-2} s_{n-3}$ is a right weak cover in $W_{J_0 \cap J_{n-1}}$ and $r_t = s_0$, we have $(u_0, v_0) \in E(\mathbf{L}|_{D_{n-1}})$.
  Now slide $+n$ left from position $n$ to position $3$ via right weak covers $s_{n-1}, \dots, s_3$:
  - Steps $s_{n-1}, \dots, s_4$ have supports disjoint from $\{1, 3\}$ (Lemma 1(1)), preserving the strict cover $t_{1, 3}^-$.
  - Step $s_3$: $t_{1, 3}^-$ overlaps $t_{3, 4}^+$ at position $3$; the second candidate applies $t_{1, 3}^-$ to $(n - 1, n - 2, n, -(n - 3), \dots)$, replacing $(n - 1, n)$ by $(-n, -(n - 1))$ across $n - 2 \in (-(n - 1), n)$, which adds $+2$ from $n - 2$ (length $\ge +3$). Thus the unique common upper cover is $((n - 1, n - 2, n, -(n - 3), \dots, -1), (n - 3, n - 2, n, -(n - 1), \dots, -1)) \in E(\mathbf{L})$.
  - Final weak step $s_0$ at positions $(1, 2)$: $t_{1, 4}^-$ overlaps $t_{1, 2}^-$ at position $1$; the second candidate applies $t_{1, 4}^-$ to $y = (-(n - 2), -(n - 1), n, -(n - 3), \dots, -1)$, decreasing length since $-(n - 2) - (n - 3) < 0$. Thus Proposition 4.1 gives
    $$y \longrightarrow z := (-(n - 2), -(n - 3), n, -(n - 1), -(n - 4), \dots, -1) \in E(\mathbf{L}).$$
  Finally, $y \to z$ uses $t_{2, 4}^+$ and $y \to q$ uses $t_{1, 3}^+$ (disjoint supports). By Lemma 1(1), their only candidate common upper cover is $y t_{1, 3}^+ t_{2, 4}^+ = (n, -(n - 3), -(n - 2), -(n - 1), \dots, -1)$, obtained from $q = (n, -(n - 1), -(n - 2), -(n - 3), \dots, -1)$ by swapping $-(n - 1)$ and $-(n - 3)$ across $-(n - 2)$, which adds $+3$ to length. Hence $z$ and $q$ have no common Bruhat upper cover, so $(y, q) \notin E(\mathbf{L})$.

- **Subcase 2b ($n$ even, $n \ge 4$):** We have $q = (-n, -(n - 1), \dots, -1)$, $q' = (n - 1, n, -(n - 2), \dots, -1)$, $c = (n - 1, -(n - 2), n, -(n - 3), \dots, -1)$, and $y = c s_0 = (n - 2, -(n - 1), n, -(n - 3), \dots, -1)$.
  Start in $W_{J_1}$ with
  $$u_0 := (-(n - 1), 2, 3, \dots, n - 3, n - 2, -1, n) \longrightarrow v_0 := (-(n - 1), 2, 3, \dots, n - 3, n, -1, n - 2).$$
  Conjugating by $\tau: W_{J_1} \xrightarrow{\sim} \mathfrak{S}_n$ yields $(n - 1, 2, \dots, n - 3, n - 2, 1, n) \to (n - 1, 2, \dots, n - 3, n, 1, n - 2)$, which factors in $W_{\{s_2, \dots, s_{n-1}\}} \times {}^{\{s_2, \dots, s_{n-1}\}} \mathfrak{S}_n$ as $(x \cdot \tilde{q}, (x s_{n-1}) \cdot \tilde{q})$ with $\tilde{q} = (2, 3, \dots, n - 1, 1, n)$ and $x = (1, n - 1, 2, \dots, n - 3, n - 2, n)$. Since $x \lessdot_R x s_{n-1}$ is a right weak cover and $r_1 = s_0$, we have $(u_0, v_0) \in E(\mathbf{L}|_{W_{J_1}})$.
  1. *Rearrange positions $\{1, \dots, n - 3\}$:* For every $u$ ending in $(n - 2, -1, n)$, $v = u t_{n-2, n}^+$ ends in $(n, -1, n - 2)$. For every generator $t \in \{s_0, s_1, \dots, s_{n-4}\}$ acting on positions $\{1, \dots, n - 3\}$, $\mathrm{supp}(t)$ is disjoint from $\{n - 2, n\}$ and $\ell(u t) - \ell(u) = \ell(v t) - \ell(v)$, so by Lemma 1(1) and Proposition 4.1 (both upward and downward), $(u, v) \in E(\mathbf{L}) \iff (u t, v t) \in E(\mathbf{L})$. Because $n$ is even, $n - 4$ is even, so the subgroup $\langle s_0, s_1, \dots, s_{n-4} \rangle \cong D_{n-3}$ acts transitively on signed rearrangements of the first $n - 3$ entries preserving sign parity (empty for $n = 4$, since $n - 3 = 1$). Hence we reach
     $$u_1 := (-(n - 1), -(n - 3), -(n - 4), \dots, -2, n - 2, -1, n) \longrightarrow v_1 := (-(n - 1), -(n - 3), \dots, -2, n, -1, n - 2) \in E(\mathbf{L}).$$
  2. *Slide $n - 2$ (resp. $n$) left past $-2, -3, \dots, -(n - 3), -(n - 1)$:* At each weak step moving $n - 2$ (at position $p$) left past $-d$ (at position $p - 1$), $t_{p, n}^+$ overlaps $t_{p-1, p}^+$ at position $p$; the second candidate swaps $-d$ and $n$ across $-1 \in (-d, n)$ (since $d \ge 2$), adding $\ge +3$ to length. By Lemma 1(2) and Proposition 4.1, we obtain
     $$u_2 := (n - 2, -(n - 1), -(n - 3), \dots, -2, -1, n) \longrightarrow v_2 := (n, -(n - 1), -(n - 3), \dots, -2, -1, n - 2) \in E(\mathbf{L}).$$
  3. *Slide $n$ (resp. $n - 2$) left past $-1, -2, \dots, -(n - 3)$:* At each weak step moving $n$ (at position $p + 1$) left past $-d$ (at position $p$), $t_{1, p+1}^+$ overlaps $t_{p, p+1}^+$ at position $p + 1$; the second candidate swaps $n - 2$ (pos $1$) and $-d$ (pos $p + 1$), which decreases length since $n - 2 > -d$. By Lemma 1(2) and Proposition 4.1, we reach
     $$y = (n - 2, -(n - 1), n, -(n - 3), \dots, -1) \longrightarrow z := (n, -(n - 1), n - 2, -(n - 3), \dots, -1) \in E(\mathbf{L}).$$
  Finally, $y \to z$ uses $t_{1, 3}^+$ and $y \to q$ uses $t_{1, 3}^-$ (same support $\{1, 3\}$). By Lemma 1(1), their only candidate common upper cover is $y t_{1, 3}^+ t_{1, 3}^- = (-(n - 2), -(n - 1), -n, -(n - 3), \dots, -1)$, obtained from $q = (-n, -(n - 1), -(n - 2), -(n - 3), \dots, -1)$ by swapping $-n$ and $-(n - 2)$ across $-(n - 1)$, which adds $+3$ to length. Hence $z$ and $q$ have no common Bruhat upper cover, so $(y, q) \notin E(\mathbf{L})$.

By Corollary 4, $\mathbf{L} = (\mathbf{L}|_{W_{J_0}}) \times {}^{J_0} D_n$. $\blacksquare$

---

## 8. Proof of the Main Theorem

*Proof of the Main Theorem.* We induct on $n \ge 4$. Let $\mathbf{L}$ be any middle order on $D_n$. By Schwob's Type $A$ **Theorem 4.13**, every middle order on $A_{n-1}$ (and on $D_3 \cong A_3$ when $n = 4$) is a minuscule middle order; for $n \ge 5$, the induction hypothesis gives that every middle order on $D_{n-1}$ is a minuscule middle order.

By Lemma 2(1) and the Overlap Trichotomy (Section 4), up to the Dynkin diagram automorphism $\tau$ ($s_0 \leftrightarrow s_1$), the unique top splitting generators $(r_0, r_1, r_t)$ of $(\mathbf{L}|_{W_{J_0}}, \mathbf{L}|_{W_{J_1}}, \mathbf{L}|_{W_{J_{n-1}}})$ must fall into Case (B1), (B2), (G2), or (G1). Cases (B1) and (B2) are impossible by Lemmas 6 and 7. In Case (G2), Lemma 8 gives $\mathbf{L} = (\mathbf{L}|_{W_{J_{n-1}}}) \times {}^{J_{n-1}} D_n$; in Case (G1), Lemma 10 gives $\mathbf{L} = (\mathbf{L}|_{W_{J_0}}) \times {}^{J_0} D_n$ (and symmetrically $\mathbf{L} = (\mathbf{L}|_{W_{J_1}}) \times {}^{J_1} D_n$ in Case (G1')). Since in every case $\mathbf{L}|_{W_J}$ is a minuscule middle order on $W_J$ and $S \setminus J$ is a minuscule simple root of $D_n$, Definition 7.1 implies that $\mathbf{L}$ is a minuscule middle order on $D_n$. $\blacksquare$

---

## 9. Computational Verification

An exact-arithmetic (pure integer, zero floating-point operations, zero `/` divisions) verification script is provided in [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/schwob-2606.12129-conj8.7/verify.py). Running `.venv/bin/python targets/schwob-2606.12129-conj8.7/verify.py` verifies:
1. Zero-float / zero-division AST self-audit of `verify.py`.
2. Lemma 1 (Common Covers of Two Reflection Neighbors) exhaustively across all 1,370 upper-cover pairs and all 1,370 lower-cover pairs in $D_4$, plus the explicit $D_3$ Type II reflection check.
3. Exhaustive verification of the explicit characterizations of ${}^{J_{n-1}} D_n$, ${}^{J_0} D_n$, and their join-irreducible sets $\mathcal{J}({}^{J_{n-1}} D_n)$ and $\mathcal{J}({}^{J_0} D_n)$ for $n = 4, 5, 6, 7$.
4. Exhaustive verification of Lemma 9 (Universal Spin-Quotient Propagation) over all $u \in {}^{J_0} D_n$, all weak covers $u \lessdot_R u t \in {}^{J_0} D_n$, and all strict $(u, s_k u)$ for $n = 4, 5, 6, 7$.
5. Exact step-by-step verification of every explicit permutation, Bruhat cover, unique-common-cover, zero-common-cover, and parabolic-membership claim in Lemmas 6, 7, 8, and 10 (including all Phase 1 + Phase 2 chains for $2 \le a \le n - 2$ and both even-$n$ and odd-$n$ chains for $a = n - 1$) across all $n = 4, 5, 6, 7, 8, 9, 10$.
6. End-to-end exact verification of all 15 minuscule middle orders on $D_4$ (satisfying Proposition 4.1 `pr:rhombus` and Theorem 3's unique minuscule split: 5 each for $s_0, s_1, s_3$).

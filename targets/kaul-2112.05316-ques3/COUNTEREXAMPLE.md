# Refutation of Questions 2 and 3 (`arXiv:2112.05316v2`) for All $p \ge 4$ and $d_G(v) \ge 4$

**Verdict:** Both **Question 3** (`ques: easier`) for every $d_G(v) = p \ge 4$ and **Question 2** (`ques: classify`) for every $p \ge 4$ have **negative answers** (specifically at $m = p+1$), confirming the authors' suspicion in Section 1.4 (`paper.tex`, line 199).

For every integer $p \ge 4$ (in fact for all $p \ge 3$), let
$$G_0^{(p)} := K_{p-2} \vee K_{2, p}$$
be the join of a clique $W = \{w_1, \dots, w_{p-2}\}$ of order $p-2 \ge 1$ and the complete bipartite graph $K_{2, p}$ with parts $V = \{v_1, v_2\}$ and $U = \{u_1, \dots, u_p\}$. Order the $2p$ copies of $K_p$ in $G_0^{(p)}$, namely $K^{(i, j)} = W \cup \{v_i, u_j\}$ ($i \in [2], j \in [p]$), as $K_1, \dots, K_{2p}$. Form $G_1, \dots, G_{2p} =: G^*$ iteratively by setting $G_k$ to be the $K_p$-gluing of $G_{k-1}$ and $K_{p+1}$ along $K_k$, i.e., attaching a new simplicial vertex $d_k$ of degree $p$ adjacent precisely to $V(K_k)$.

We prove that for every $p \ge 4$, at least one $k \in \{1, \dots, 2p\}$ satisfies
$$P_{DP}(G_k, p+1) > (p+1 - d_{G_k}(d_k))\, P_{DP}(G_k - \{d_k\}, p+1) = P_{DP}(G_{k-1}, p+1).$$
Since $G_k \in G_{k-1} \oplus_p K_{p+1}$ and $P_{DP}(K_{p+1}, p+1) = (p+1)!$ (see Lemma 1 below), this gives
$$P_{DP}(G_k, p+1) > P_{DP}(G_{k-1}, p+1) = \frac{P_{DP}(G_{k-1}, p+1) P_{DP}(K_{p+1}, p+1)}{\prod_{i=0}^{p-1} (p+1-i)},$$
simultaneously refuting Question 3 (`ques: easier`) for $d_G(v) = p$ and Question 2 (`ques: classify`) for $p$ (with $n = 2$ and $m = p+1$).

*(For $p = 4$, one may also take the smaller 7-vertex base graph $K_2 \vee K_{2,3}$ with $6$ copies of $K_4$, where $P_{DP}(K_2 \vee K_{2,3}, 5) \le 570 < 600 = P(K_2 \vee K_{2,3}, 5)$. Below we prove the uniform family $G_0^{(p)} = K_{p-2} \vee K_{2,p}$ for all $p \ge 4$.)*

---

## Proof

### Lemma 1 (Cliques and $p$-cliques of $G_0^{(p)}$)
1. For any $p \ge 3$, $P_{DP}(K_{p+1}, p+1) = P(K_{p+1}, p+1) = (p+1)!$.
   *Proof:* Taking the canonical $(p+1)$-fold cover gives $P_{DP}(K_{p+1}, p+1) \le P(K_{p+1}, p+1) = (p+1)!$. Conversely, in any $(p+1)$-fold cover $\mathcal{H}$ of $K_{p+1}$ with vertices $z_1, \dots, z_{p+1}$, choosing an independent vertex from $L(z_r)$ sequentially for $r = 1, \dots, p+1$ encounters $r-1$ already-chosen neighbors in $K_{p+1}$, each forbidding at most $1$ vertex in $L(z_r)$ (since cross-edges between any two parts form a matching), leaving at least $(p+1)-(r-1)$ choices at step $r$. Thus $P_{DP}(K_{p+1}, \mathcal{H}) \ge \prod_{r=1}^{p+1} ((p+2)-r) = (p+1)!$.
2. Every $p$-clique $K$ in $G_0^{(p)} = K_{p-2} \vee K_{2, p}$ has the form $W \cup \{v_i, u_j\}$ for some $i \in [2], j \in [p]$.
   *Proof:* Since $K_{2, p}$ is triangle-free, $|K \cap (V \cup U)| \le 2$. As $|W| = p-2$ and $|K| = p$, we must have $W \subseteq K$ and $K \cap (V \cup U)$ must be an edge $v_i u_j$ of $K_{2, p}$. Thus there are exactly $2p$ copies of $K_p$ in $G_0^{(p)}$.

### Lemma 2 ($P_{DP}(G_0^{(p)}, p+1) < P(G_0^{(p)}, p+1)$)
For every $p \ge 3$,
$$P_{DP}(G_0^{(p)}, p+1) \le P(G_0^{(p)}, p+1) - (p-1)!\bigl(2^p - 2p + 2\bigr) < P(G_0^{(p)}, p+1),$$
where $P(G_0^{(p)}, p+1) = \frac{(p+1)!}{6}\bigl(3 \cdot 2^p + 6\bigr)$.

*Proof:* Let $m = p+1$. Define a full $(p+1)$-fold cover $\mathcal{H} = (L, H)$ of $G_0^{(p)}$ with $L(x) = \{(x, c) : c \in [p+1]\}$ for all $x \in V(G_0^{(p)})$ by:
- For every edge $xy \in E(G_0^{(p)}) \setminus \{v_1 u_p\}$: canonical cross-edges $(x, c)(y, c) \in E(H)$ for all $c \in [p+1]$.
- For the single edge $v_1 u_p$: transpose colors $1$ and $2$, i.e., cross-edges $(v_1, 1)(u_p, 2)$, $(v_1, 2)(u_p, 1)$, and $(v_1, c)(u_p, c)$ for $3 \le c \le p+1$. Let $\tau = (1\,2) \in S_{p+1}$ denote this transposition.

Because $W$ is a $(p-2)$-clique joined to every vertex of $V \cup U$ and all edges incident to $W$ are canonical, any $\mathcal{H}$-coloring $I$ assigns pairwise distinct colors $(c_1, \dots, c_{p-2}) \in [p+1]^{p-2}$ to $(w_1, \dots, w_{p-2})$, leaving the 3-element available color set $S := [p+1] \setminus \{c_1, \dots, c_{p-2}\}$ at every vertex of $V \cup U$. Each 3-subset $S \subseteq [p+1]$ arises from exactly $(p-2)!$ ordered tuples $(c_1, \dots, c_{p-2})$.

For a fixed 3-subset $S \subseteq [p+1]$, let $N_{\mathcal{H}}(S)$ (resp. $N_{\mathrm{canon}}(S)$) be the number of valid colorings of $K_{2,p}$ with colors in $S$ under $\mathcal{H}$ (resp. under the canonical cover). For the canonical cover:
- $3$ choices have $c(v_1) = c(v_2) \in S$, giving $2^p$ choices for $(u_1, \dots, u_p)$;
- $6$ choices have $c(v_1) \neq c(v_2) \in S$, giving $1^p = 1$ choice for $(u_1, \dots, u_p)$.
Hence $N_{\mathrm{canon}}(S) = 3 \cdot 2^p + 6$ and $P(G_0^{(p)}, p+1) = (p-2)!\binom{p+1}{3}(3\cdot 2^p + 6) = \frac{(p+1)!}{6}(3\cdot 2^p + 6)$.

Now compute $\Delta(S) := N_{\mathcal{H}}(S) - N_{\mathrm{canon}}(S)$ for each 3-subset $S \subseteq [p+1]$:
1. If $S \cap \{1, 2\} = \emptyset$: $\tau|_S = \mathrm{id}_S$, so $\Delta(S) = 0$.
2. If $|S \cap \{1, 2\}| = 1$ (there are $2\binom{p-1}{2} = (p-1)(p-2)$ such subsets $S$): let $S \cap \{1, 2\} = \{a\}$ so $\tau(a) \notin S$. For $(c(v_1), c(v_2)) \in S^2$:
   - If $c(v_1) \neq a$ or $c(v_1) = c(v_2) = a$, then $S \setminus \{\tau(c(v_1)), c(v_2)\} = S \setminus \{c(v_1), c(v_2)\}$ (zero net change).
   - If $c(v_1) = a$ and $c(v_2) \in S \setminus \{a\}$ ($2$ choices for $c(v_2)$), then $u_1, \dots, u_{p-1}$ each have $1$ choice, while $u_p$ has $|S \setminus \{c(v_2)\}| = 2$ choices instead of $|S \setminus \{a, c(v_2)\}| = 1$. Thus $\Delta(S) = +2 \cdot 1^{p-1} = +2$.
3. If $\{1, 2\} \subseteq S$ (there are $p-1$ such subsets $S$; write $S = \{1, 2, s_0\}$ with $s_0 \notin \{1, 2\}$):
   - If $c(v_1) = s_0$ ($3$ choices for $c(v_2) \in S$), then $\tau(c(v_1)) = c(v_1)$ (zero net change).
   - If $c(v_1) \in \{1, 2\}$ and $c(v_2) = s_0$ ($2$ choices for $(c(v_1), c(v_2))$), then $|S \setminus \{c(v_1), s_0\}| = 1 = |S \setminus \{\tau(c(v_1)), s_0\}|$, so $u_p$ still has $1$ choice (zero net change).
   - If $c(v_1) = c(v_2) \in \{1, 2\}$ ($2$ choices), then $u_1, \dots, u_{p-1}$ each have $2$ choices, while $u_p$ has $|S \setminus \{1, 2\}| = 1$ choice instead of $2$, contributing $-2 \cdot 2^{p-1} = -2^p$.
   - If $\{c(v_1), c(v_2)\} = \{1, 2\}$ ($2$ choices), then $u_1, \dots, u_{p-1}$ each have $1$ choice, while $u_p$ has $|S \setminus \{c(v_2)\}| = 2$ choices instead of $1$, contributing $+2 \cdot 1^{p-1} = +2$.
   Thus all $9$ pairs $(c(v_1), c(v_2)) \in S^2$ are accounted for and $\Delta(S) = 2 - 2^p$.

Summing over all 3-subsets $S \subseteq [p+1]$ and multiplying by $(p-2)!$ gives
$$P_{DP}(G_0^{(p)}, \mathcal{H}) - P(G_0^{(p)}, p+1) = (p-2)!\Bigl((p-1)(p-2)\cdot 2 + (p-1)(2 - 2^p)\Bigr) = -(p-1)!\bigl(2^p - 2p + 2\bigr).$$
Since $2^p - 2p + 2 > 0$ for all $p \ge 3$ ($2^3 - 6 + 2 = 4 > 0$, and $2^{p+1} - 2(p+1) + 2 = 2(2^p - 2p + 2) + 2p - 4 > 0$ inductively), we obtain $P_{DP}(G_0^{(p)}, p+1) \le P_{DP}(G_0^{(p)}, \mathcal{H}) < P(G_0^{(p)}, p+1)$. $\square$

### Lemma 3 (Precoloring Extension on $G_0^{(p)}$)
Let $K_k = W \cup \{v_i, u_j\}$ be any $p$-clique of $G_0^{(p)}$, and let $\mathcal{H} = (L, H)$ be any $(p+1)$-fold cover of $G_0^{(p)}$. Every independent set $A$ in $H$ of size $p$ with $|A \cap L(x)| = 1$ for all $x \in V(K_k)$ extends to at least one $\mathcal{H}$-coloring $D$ of $G_0^{(p)}$.

*Proof:* $V(G_0^{(p)}) \setminus V(K_k) = \{v_{3-i}\} \cup \{u_{j'} : j' \in [p] \setminus \{j\}\}$.
1. Vertex $v_{3-i}$ has $(p-2) + 1 = p-1$ neighbors in $K_k$ (namely $W \cup \{u_j\}$). Since $E_H(L(v_{3-i}), L(x))$ is a matching for each $x$, $A$ forbids at most $p-1$ vertices of $L(v_{3-i})$, leaving at least $(p+1) - (p-1) = 2$ choices. Pick one such vertex $q \in L(v_{3-i})$.
2. Each remaining $u_{j'}$ ($j' \neq j$) has $(p-2) + 1 = p-1$ neighbors in $K_k$ (namely $W \cup \{v_i\}$) plus one neighbor $v_{3-i}$, hence $p$ neighbors in $K_k \cup \{v_{3-i}\}$. Thus $A \cup \{q\}$ forbids at most $p$ vertices of $L(u_{j'})$, leaving at least $(p+1) - p = 1$ available choice in $L(u_{j'})$. Since $\{u_{j'} : j' \neq j\}$ is an independent set in $G_0^{(p)}$, picking one available vertex per $u_{j'}$ produces an $\mathcal{H}$-coloring $D \supseteq A$ of $G_0^{(p)}$. $\square$

### Main Theorem (Contradiction on $G^* = G_{2p}$)
Suppose for contradiction that $P_{DP}(G_k, p+1) \le P_{DP}(G_{k-1}, p+1)$ for all $k = 1, \dots, 2p$. Then $P_{DP}(G^*, p+1) \le P_{DP}(G_0^{(p)}, p+1) < P(G_0^{(p)}, p+1)$.

Let $\mathcal{H}^* = (L^*, H^*)$ be a $(p+1)$-fold cover of $G^*$ with $P_{DP}(G^*, \mathcal{H}^*) = P_{DP}(G^*, p+1)$. By completing every non-perfect cross-edge matching $E_{H^*}(L^*(x), L^*(y))$ ($xy \in E(G^*)$) arbitrarily to a perfect matching, we obtain a **full** $(p+1)$-fold cover with at most as many independent sets (adding edges cannot create independent sets), hence also minimizing $P_{DP}(G^*, p+1)$; thus we may assume without loss of generality that $\mathcal{H}^*$ is full.

Let $\mathcal{H}_0 = (L_0, H_0)$ be the subcover of $\mathcal{H}^*$ induced by $V(G_0^{(p)})$ (which is full since $G_0^{(p)}$ is induced in $G^*$). Let $\mathcal{C}_0$ be the set of $\mathcal{H}_0$-colorings of $G_0^{(p)}$ and $\mathcal{C}^*$ be the set of $\mathcal{H}^*$-colorings of $G^*$. Define $f : \mathcal{C}_0 \to \mathcal{P}(\mathcal{C}^*)$ by $f(I) = \{C \in \mathcal{C}^* : I \subseteq C\}$.
- For $I \neq I'$ in $\mathcal{C}_0$, $f(I) \cap f(I') = \emptyset$ because $C \cap V(H_0) = I$ for every $C \in f(I)$.
- For every $I \in \mathcal{C}_0$, each vertex $d_k$ ($1 \le k \le 2p$) has $p$ neighbors in $G^*$ (all in $K_k \subseteq V(G_0^{(p)})$) and $\{d_1, \dots, d_{2p}\}$ is independent in $G^*$. Thus each $I$ leaves at least $(p+1) - p = 1$ available vertex in each $L^*(d_k)$, so $|f(I)| \ge 1$.

Now analyze the two cases for $\mathcal{H}_0$:
- **Case 1 ($\mathcal{H}_0$ has a canonical labeling):** Then $|\mathcal{C}_0| = P(G_0^{(p)}, p+1)$, so
  $$P_{DP}(G^*, p+1) = |\mathcal{C}^*| \ge \sum_{I \in \mathcal{C}_0} |f(I)| \ge |\mathcal{C}_0| = P(G_0^{(p)}, p+1) > P_{DP}(G_0^{(p)}, p+1),$$
  a contradiction.
- **Case 2 ($\mathcal{H}_0$ has no canonical labeling):** Fix $w_1 \in W$ (recall $w_1$ is adjacent to every other vertex of $G_0^{(p)}$). Label $L^*(w_1) = \{(w_1, c) : c \in [p+1]\}$, and since $\mathcal{H}_0$ is full, label each $L^*(x)$ ($x \in V(G_0^{(p)}) \setminus \{w_1\}$) as $\{(x, c) : c \in [p+1]\}$ so that $(w_1, c)(x, c) \in E(H_0)$ for all $c \in [p+1]$. Because $\mathcal{H}_0$ has no canonical labeling, some edge $yz \in E(G_0^{(p)})$ with $y, z \neq w_1$ does not have the identity matching $\{(y, c)(z, c) : c \in [p+1]\}$. Since every edge of $G_0^{(p)}$ lies in at least one $p$-clique $K_k = W \cup \{v_i, u_j\}$ (as $W$ is a clique joined to $K_{2,p}$ and $K_{2,p}$ has no edges inside $V$ or $U$), choose $k \in [2p]$ with $y, z \in V(K_k)$.

  We claim the induced subcover $\mathcal{H}_{K_k}$ has no canonical labeling. Indeed, any canonical labeling $\pi_x : L^*(x) \to [p+1]$ ($x \in V(K_k)$) would force $\pi_x(x, c) = \pi_{w_1}(w_1, c)$ for all $x \in V(K_k)$ and $c \in [p+1]$ (because all edges $w_1 x$ have cross-edges $(w_1, c)(x, c)$), which in turn forces $(y, c)(z, c') \in E(H_0) \iff c = c'$, contradicting the choice of $yz$.

  Now relabel $L^*(d_k)$ and each $L^*(x)$ ($x \in V(K_k)$) as $\{(x, c)' : c \in [p+1]\}$ so that $(d_k, c)'(x, c)' \in E(H^*)$ for all $x \in V(K_k)$ and $c \in [p+1]$. Since $\mathcal{H}_{K_k}$ has no canonical labeling, some edge $ab \in E(K_k)$ does not have the identity matching in these primed labels, so there exists $c_0 \in [p+1]$ such that $(a, c_0)'(b, c_0)' \notin E(H^*)$. Ordering the remaining $p-2$ vertices of $K_k$ as $x_3, \dots, x_p$, at step $r \in \{3, \dots, p\}$ vertex $x_r$ has $r-1 \le p-1$ already-chosen neighbors in $K_k$, leaving at least $(p+1)-(p-1) = 2$ choices in $L^*(x_r)$. We thus obtain an $\mathcal{H}_{K_k}$-coloring
  $$A = \{(a, c_0)', (b, c_0)', (x_3, c_3)', \dots, (x_p, c_p)'\}$$
  using at most $p-1$ distinct primed indices $\{c_0, c_3, \dots, c_p\} \subseteq [p+1]$. Hence at least $(p+1) - (p-1) = 2$ choices $(d_k, c)' \in L^*(d_k)$ (for $c \in [p+1] \setminus \{c_0, c_3, \dots, c_p\}$) are non-adjacent to all vertices of $A$.

  By Lemma 3, $A$ extends to an $\mathcal{H}_0$-coloring $D \in \mathcal{C}_0$. Because $D$ allows $\ge 2$ choices in $L^*(d_k)$ and $\ge 1$ choice in each $L^*(d_{k'})$ ($k' \neq k$), we have $|f(D)| \ge 2$, while $|f(I)| \ge 1$ for every $I \in \mathcal{C}_0$. Therefore,
  $$P_{DP}(G^*, p+1) = |\mathcal{C}^*| \ge \sum_{I \in \mathcal{C}_0} |f(I)| \ge |\mathcal{C}_0| + 1 \ge P_{DP}(G_0^{(p)}, p+1) + 1 > P_{DP}(G_0^{(p)}, p+1),$$
  contradicting $P_{DP}(G^*, p+1) \le P_{DP}(G_0^{(p)}, p+1)$.

Thus some $k \in \{1, \dots, 2p\}$ violates Question 3 (`ques: easier`) with simplicial vertex $d_k$ of degree $p$ at $m = p+1$, and equivalently violates Question 2 (`ques: classify`) with $n = 2$, $G_1 = G_{k-1}$, $G_2 = K_{p+1}$, and $m = p+1$. $\blacksquare$

# Proof of Conjecture 5.5 of Biswas, Mandal, and Saha (`arXiv:2603.04876v1`)

## 1. Statement and Preliminaries

**Primary Source.** Prativa Biswas, Mousumi Mandal, and Kamalesh Saha, *"Lattice points arising from regularity and $\mathrm{v}$-number of Graphs: Whisker and Cameron-Walker"*, `arXiv:2603.04876v1` (2026-03-05), Section 5 (*Future Directions*), Conjecture 5.5 (`Arxiv.tex`, lines 980–983):

> **Conjecture 5.5.** For the class of connected chordal graphs on $n \ge 3$ vertices, we have
> $$\mathcal{RV}_{\mathrm{chordal}}(n) = \left\{(r, v) \in \mathbb{N}^2 \;\middle|\; 1 \le r < \frac{n}{2},\; 1 \le v \le r - \left\lceil \frac{r}{n - 2r} \right\rceil + 1\right\}.$$

Here all graphs $G = (V(G), E(G))$ are finite and simple, $\mathbb{N} = \{1, 2, 3, \dots\}$ (as in Section 1 of `arXiv:2603.04876v1`), a graph is *chordal* if it has no induced cycle of length at least $4$, and $\mathcal{RV}_{\mathrm{chordal}}(n)$ denotes the set of pairs $(\mathrm{reg}(G), \mathrm{v}(G))$ as $G$ ranges over all connected chordal graphs on $n$ vertices, where $\mathrm{reg}(G) := \mathrm{reg}(R/I(G))$ is the Castelnuovo–Mumford regularity of the quotient by the edge ideal $I(G)$ and $\mathrm{v}(G) := \mathrm{v}(I(G))$ is the $\mathrm{v}$-number of $I(G)$. Let
$$A(n) := \left\{(r, v) \in \mathbb{N}^2 \;\middle|\; 1 \le r < \frac{n}{2},\; 1 \le v \le r - \left\lceil \frac{r}{n - 2r} \right\rceil + 1\right\}.$$

For any subset $S \subseteq V(G)$, we write $N_G(S) := \{w \in V(G) : \{w, u\} \in E(G) \text{ for some } u \in S\}$, $N_G[S] := N_G(S) \cup S$, and for a vertex $x$, $N_G(x) := N_G(\{x\})$ and $N_G[x] := N_G[\{x\}]$. A vertex $s \in V(G)$ is *simplicial* if $N_G(s)$ is a clique of $G$ (equivalently, $N_G[s]$ is a clique). An *induced matching* of $G$ is a set $M$ of pairwise disjoint edges such that the induced subgraph $G[V(M)]$ on $V(M) := \bigcup_{e \in M} e$ has edge set $M$; the *induced matching number* $\mathrm{im}(G)$ is the maximum size of an induced matching of $G$ (with $\mathrm{im}(G) = 0$ if $E(G) = \emptyset$).

We rely on the two standard algebraic–combinatorial characterizations recorded in Section 2 of `arXiv:2603.04876v1`:
1. **Combinatorial $\mathrm{v}$-number** (Definition 2.4 of `arXiv:2603.04876v1`, citing Jaramillo–Villarreal 2021, Lemma 3.4 and Theorem 3.5): for any graph $G$ with $E(G) \neq \emptyset$,
   $$\mathrm{v}(G) = \min\big\{|A| : A \subseteq V(G) \text{ is independent and } N_G(A) \text{ is a vertex cover of } G\big\}.$$
2. **Regularity of chordal graphs** (Theorem 2.11 of `arXiv:2603.04876v1`, citing Hà–Van Tuyl 2008, Corollary 6.9): for every chordal graph $G$,
   $$\mathrm{reg}(G) = \mathrm{im}(G).$$

We prove the following theorem, which settles Conjecture 5.5 in the affirmative by establishing a stronger $1$-vertex neighborhood-deletion bound for $\mathrm{im}(G)$.

**Theorem 1.** *Let $G$ be a connected chordal graph on $n \ge 3$ vertices, and set $r := \mathrm{im}(G) = \mathrm{reg}(G)$. Then $1 \le r < n/2$, and there exists a vertex $x^* \in V(G)$ such that*
$$\mathrm{im}\big(G - N_G[x^*]\big) \le r - \left\lceil \frac{r}{n - 2r} \right\rceil.$$
*Consequently,*
$$1 \le \mathrm{v}(G) \le r - \left\lceil \frac{r}{n - 2r} \right\rceil + 1,$$
*and for every integer $n \ge 3$, $\mathcal{RV}_{\mathrm{chordal}}(n) = A(n)$.*

---

## 2. Structural Lemmas for Chordal Graphs

All lemmas below are proved completely self-containedly.

**Lemma 1 (Dirac, 1961).** *Every chordal graph $H$ on $n \ge 1$ vertices is either complete or contains two nonadjacent simplicial vertices. In particular, every nonempty chordal graph contains a simplicial vertex.*

*Proof.* We induct on $n$. If $H$ is complete, every vertex is simplicial. Otherwise, $H$ has two nonadjacent vertices $a, b \in V(H)$. Choose an inclusion-minimal vertex separator $S \subseteq V(H) \setminus \{a, b\}$ disconnecting $a$ from $b$, and let $C_a, C_b$ be the connected components of $H - S$ containing $a$ and $b$, respectively.

We first check that $S$ is a clique. Let $x, y \in S$ be distinct. By minimality of $S$, both $x$ and $y$ have neighbors in $C_a$ and neighbors in $C_b$. Let $P_a$ be a shortest $x$–$y$ path whose internal vertices lie in $C_a$, and let $P_b$ be a shortest $x$–$y$ path whose internal vertices lie in $C_b$. Then $P_a \cup P_b$ is a cycle of length at least $4$. Since both $P_a$ and $P_b$ are induced paths and there are no edges between $C_a$ and $C_b$, the only possible chord of $P_a \cup P_b$ is $\{x, y\}$. Because $H$ is chordal, $\{x, y\} \in E(H)$, so $S$ is a clique.

Consider the induced subgraph $H_a := H[C_a \cup S]$, which is chordal with $|V(H_a)| < n$. Note that every $v \in C_a$ satisfies $N_H(v) = N_{H_a}(v) \subseteq C_a \cup S$. If $H_a$ is complete, then any $v \in C_a$ is simplicial in $H$. Otherwise, by the induction hypothesis $H_a$ has two nonadjacent simplicial vertices; because $S$ is a clique, at least one of them lies in $C_a$, and it is therefore simplicial in $H$. Symmetrically, $C_b$ contains a vertex simplicial in $H$. Since no edge connects $C_a$ to $C_b$, these two simplicial vertices are nonadjacent. $\square$

---

**Lemma 2 (Upper bound $\mathrm{v}(H) \le \mathrm{im}(H)$ for chordal graphs).** *For every (not necessarily connected) chordal graph $H$, there exists an independent set $A \subseteq V(H)$ such that $N_H(A)$ is a vertex cover of $H$ and $|A| \le \mathrm{im}(H)$.*

*Proof.* We induct on $|E(H)|$. If $E(H) = \emptyset$, take $A := \emptyset$; then $A$ is independent, $N_H(\emptyset) = \emptyset$ vacuously covers $E(H)$, and $|A| = 0 = \mathrm{im}(H)$.

Suppose $|E(H)| \ge 1$. Let $H_0$ be the induced subgraph of $H$ obtained by deleting all isolated vertices. Then $H_0$ is a nonempty chordal graph with minimum degree at least $1$ and $E(H_0) = E(H)$. By Lemma 1, $H_0$ has a simplicial vertex $s$. Pick any neighbor $u \in N_{H_0}(s) = N_H(s)$. Since $s$ is simplicial in $H_0$ (and has no neighbors outside $V(H_0)$), $N_H[s]$ is a clique, so $N_H[s] \subseteq N_H[u]$.

Let $H' := H - N_H[u]$. Then $H'$ is chordal (as an induced subgraph of $H$) and $\{s, u\} \in E(H) \setminus E(H')$, so $|E(H')| < |E(H)|$. Let $M'$ be a maximum induced matching of $H'$. Because $V(M') \subseteq V(H) \setminus N_H[u]$ and $N_H[s] \subseteq N_H[u]$, no vertex of $V(M')$ equals or is adjacent in $H$ to either $s$ or $u$. Hence $M' \cup \{\{s, u\}\}$ is an induced matching of $H$, showing that $\mathrm{im}(H') \le \mathrm{im}(H) - 1$.

By the induction hypothesis applied to $H'$, there exists an independent set $A' \subseteq V(H')$ such that $N_{H'}(A')$ is a vertex cover of $H'$ and $|A'| \le \mathrm{im}(H')$. Set $A := \{u\} \cup A'$. Since $A' \subseteq V(H) \setminus N_H[u]$, we have $u \notin A'$ and no edge joins $u$ to $A'$, so $A$ is independent in $H$ with
$$|A| = 1 + |A'| \le 1 + \mathrm{im}(H') \le \mathrm{im}(H).$$
Finally, let $e \in E(H)$. If $u \in e$, then the other endpoint of $e$ lies in $N_H(u) \subseteq N_H(A)$. If $e \cap N_H(u) \neq \emptyset$, then $e \cap N_H(A) \neq \emptyset$. Otherwise $e \cap N_H[u] = \emptyset$, so $e \in E(H')$, whence $e$ intersects $N_{H'}(A') \subseteq N_H(A') \subseteq N_H(A)$. Thus $N_H(A)$ is a vertex cover of $H$. $\square$

---

**Lemma 3 (Clique tree of a connected chordal graph).** *Let $G$ be a connected chordal graph on $n \ge 1$ vertices, and let $\mathcal{K}(G)$ denote the set of all inclusion-maximal cliques of $G$. Then there exists a tree $\mathcal{T}$ with vertex set $\mathcal{K}(G)$ such that:*
1. *for every $v \in V(G)$, the set $T_v := \{B \in \mathcal{K}(G) : v \in B\}$ induces a nonempty connected subtree of $\mathcal{T}$; and*
2. *for every edge $\{B, B'\} \in E(\mathcal{T})$, we have $B \cap B' \neq \emptyset$.*

*Proof.* We induct on $n$. For $n = 1$, $\mathcal{K}(G) = \{V(G)\}$ and the single-vertex tree satisfies (1) and (2).

Let $n \ge 2$. By Lemma 1, $G$ has a simplicial vertex $s$. Since $G$ is connected and $n \ge 2$, $\deg_G(s) \ge 1$. Moreover, $G' := G - s$ is connected: in any path in $G$ between vertices of $G'$, if $s$ appears as an internal vertex with neighbors $w_1, w_2 \in N_G(s)$, then $\{w_1, w_2\} \in E(G)$ because $s$ is simplicial, so $w_1 - s - w_2$ can be shortcut to $w_1 - w_2$ inside $G'$. Since $G'$ is a connected chordal graph on $n - 1$ vertices, the induction hypothesis yields a tree $\mathcal{T}'$ on $\mathcal{K}(G')$ satisfying (1) and (2).

Because $N_G(s)$ is a nonempty clique of $G'$, it is contained in some maximal clique $B_0 \in \mathcal{K}(G')$. Notice that $N_G[s]$ is the unique maximal clique of $G$ containing $s$ (every clique containing $s$ is contained in $N_G[s]$, which is itself a clique). A maximal clique $B \in \mathcal{K}(G')$ remains maximal in $G$ if and only if $B \not\subseteq N_G(s)$; since $N_G(s)$ is a clique of $G'$ and $B$ is maximal in $G'$, we have $B \subseteq N_G(s)$ if and only if $B = N_G(s)$.

- **Case 1: $N_G(s) = B_0$.** Then $\mathcal{K}(G) = (\mathcal{K}(G') \setminus \{B_0\}) \cup \{B_0 \cup \{s\}\}$. Define $\mathcal{T}$ from $\mathcal{T}'$ by replacing the vertex $B_0$ with $B_0 \cup \{s\}$ while keeping all tree edges unchanged. Then $T_s = \{B_0 \cup \{s\}\}$ is a single vertex, while for every $v \in V(G')$, $T_v$ corresponds to the exact same tree vertices as in $\mathcal{T}'$ and hence induces a nonempty connected subtree. Each tree edge intersection can only enlarge, so (2) holds.
- **Case 2: $N_G(s) \subsetneq B_0$.** Then $N_G(s) \notin \mathcal{K}(G')$, so $\mathcal{K}(G) = \mathcal{K}(G') \cup \{N_G[s]\}$. Define $\mathcal{T}$ from $\mathcal{T}'$ by adjoining a new leaf vertex $N_G[s]$ adjacent solely to $B_0$. Clearly $\mathcal{T}$ is a tree. We have $T_s = \{N_G[s]\}$; for $v \in V(G') \setminus N_G(s)$, $T_v$ is unchanged from $\mathcal{T}'$; and for $v \in N_G(s) \subseteq B_0$, we have $B_0 \in T'_v$ in $\mathcal{T}'$, so $T_v = T'_v \cup \{N_G[s]\}$ adjoins a leaf to $B_0 \in T'_v$ and remains a nonempty connected subtree. Finally, the new tree edge satisfies $N_G[s] \cap B_0 = N_G(s) \neq \emptyset$, so (2) holds. $\square$

---

**Lemma 4 (Greedy bottom-up clique cover and maximum induced matching, cf. Cameron 1989).** *Let $G$ be a connected chordal graph on $n \ge 3$ vertices with $r := \mathrm{im}(G)$, let $\mathcal{T}$ be a clique tree of $G$ as in Lemma 3, and root $\mathcal{T}$ at an arbitrary maximal clique $R \in \mathcal{K}(G)$. Let $\mathrm{depth}(B)$ denote the distance in $\mathcal{T}$ from $R$ to $B \in \mathcal{K}(G)$. For each edge $e = \{u, v\} \in E(G)$, the set $T_e := T_u \cup T_v = \{B \in \mathcal{K}(G) : e \cap B \neq \emptyset\}$ induces a nonempty connected subtree of $\mathcal{T}$ with a unique vertex $\mathrm{top}(T_e)$ of minimum depth.*

*Construct edges $e_1, \dots, e_k$ and maximal cliques $B_1, \dots, B_k \in \mathcal{K}(G)$ inductively as follows: set $G_1 := G$; while $E(G_i) \neq \emptyset$, choose $e_i \in E(G_i)$ maximizing $\mathrm{depth}(\mathrm{top}(T_{e_i}))$, set $B_i := \mathrm{top}(T_{e_i})$, and set $G_{i+1} := G_i - B_i$. Then:*
1. *the process terminates in $k = r$ steps;*
2. *$M := \{e_1, \dots, e_r\}$ is a maximum induced matching of $G$;*
3. *$B_1 \cup \dots \cup B_r$ is a vertex cover of $G$; and*
4. *$B_i \neq R$ for all $1 \le i \le r - 1$.*

*Proof.* First, for any edge $e = \{u, v\} \in E(G)$, the clique $\{u, v\}$ lies in some maximal clique $B^* \in \mathcal{K}(G)$, so $B^* \in T_u \cap T_v$. Since $T_u$ and $T_v$ induce connected subtrees of $\mathcal{T}$ with nonempty intersection, $T_e = T_u \cup T_v$ induces a nonempty connected subtree of $\mathcal{T}$. Every nonempty connected subtree $S$ of a rooted tree has a unique vertex of minimum depth $\mathrm{top}(S)$ (if two distinct vertices of $S$ shared the minimum depth, their lowest common ancestor would lie on the path between them in $S$ and have strictly smaller depth), and $\mathrm{top}(S)$ is an ancestor of every vertex in $S$.

At each step $i$, since $B_i = \mathrm{top}(T_{e_i}) \in T_{e_i}$, we have $e_i \cap B_i \neq \emptyset$; as $e_i \in E(G_i)$, removing $B_i$ deletes at least one vertex of $G_i$, so the loop terminates after some $k \ge 1$ steps with $E(G_{k+1}) = \emptyset$. Since $G_{k+1} = G - (B_1 \cup \dots \cup B_k)$ is edgeless, $B_1 \cup \dots \cup B_k$ is a vertex cover of $G$.

Next, for $1 \le i < j \le k$, we have $E(G_j) \subseteq E(G_i)$, so $e_j \in E(G_i)$ and the greedy choice at step $i$ gives
$$\mathrm{depth}(B_i) \ge \mathrm{depth}(B_j).$$
We claim $M := \{e_1, \dots, e_k\}$ is an induced matching of $G$. Suppose for contradiction that for some $1 \le i < j \le k$, either $e_i \cap e_j \neq \emptyset$ or some edge $f = \{w_1, w_2\} \in E(G)$ satisfies $w_1 \in e_i$ and $w_2 \in e_j$. In the first case, any $B \in T_w$ for $w \in e_i \cap e_j$ lies in $T_{e_i} \cap T_{e_j}$; in the second case, any maximal clique $B \in \mathcal{K}(G)$ containing $\{w_1, w_2\}$ lies in $T_{e_i} \cap T_{e_j}$. Thus there exists $B \in T_{e_i} \cap T_{e_j}$. Then both $B_i = \mathrm{top}(T_{e_i})$ and $B_j = \mathrm{top}(T_{e_j})$ are ancestors of $B$ in $\mathcal{T}$. Since the ancestors of $B$ form the path from $B$ to $R$ ordered by depth and $\mathrm{depth}(B_i) \ge \mathrm{depth}(B_j)$, the vertex $B_i$ lies on the unique path in $\mathcal{T}$ between $B$ and $B_j$. Because $B, B_j \in T_{e_j}$ and $T_{e_j}$ is connected, we get $B_i \in T_{e_j}$, meaning $e_j \cap B_i \neq \emptyset$. This contradicts $e_j \in E(G_j)$ because $V(G_j) = V(G) \setminus (B_1 \cup \dots \cup B_{j-1})$ is disjoint from $B_i$ (as $i \le j - 1$). Thus $M$ is an induced matching of $G$, giving $k = |M| \le \mathrm{im}(G) = r$.

Conversely, let $M^*$ be any induced matching of $G$. Since $B_1 \cup \dots \cup B_k$ is a vertex cover of $G$, every edge of $M^*$ intersects at least one $B_i$. On the other hand, each $B_i$ is a clique of $G$, so $B_i$ can intersect at most one edge of $M^*$ (otherwise two distinct edges of $M^*$ would share a vertex or be joined by an edge inside $B_i$). Hence $|M^*| \le k$, so $r = \mathrm{im}(G) \le k$. Therefore $k = r$, establishing (1), (2), and (3).

Finally, if $B_i = R$ for some $i \in \{1, \dots, r\}$, then $\mathrm{depth}(\mathrm{top}(T_{e_i})) = \mathrm{depth}(R) = 0$. By maximality of $\mathrm{depth}(\mathrm{top}(T_{e_i}))$, every edge $e \in E(G_i)$ satisfies $\mathrm{top}(T_e) = R \in T_e$, so $e \cap R \neq \emptyset$. Hence $G_{i+1} = G_i - R$ is edgeless, forcing $i = r$. This proves (4). $\square$

---

**Lemma 5 (Clique cover intersecting $X := V(G) \setminus V(M)$).** *Let $G$ be a connected chordal graph on $n \ge 3$ vertices with $r := \mathrm{im}(G)$. Then there exist a maximum induced matching $M$ of $G$ and $r$ cliques $C_1, \dots, C_r$ of $G$ (not necessarily maximal) such that, setting $X := V(G) \setminus V(M)$,*
1. *$C_1 \cup \dots \cup C_r$ is a vertex cover of $G$; and*
2. *$C_i \cap X \neq \emptyset$ for every $i \in \{1, \dots, r\}$.*

*Proof.* By Lemma 1, choose a simplicial vertex $s \in V(G)$. Because $s$ is simplicial, $R := N_G[s]$ is an inclusion-maximal clique of $G$ (every clique containing $s$ is contained in $N_G[s]$, and $N_G[s]$ itself is a clique). Let $\mathcal{T}$ be a clique tree of $G$ as in Lemma 3, rooted at **$R := N_G[s]$**. Let $M = \{e_1, \dots, e_r\}$ and $B_1, \dots, B_r \in \mathcal{K}(G)$ be the maximum induced matching and maximal cliques produced by Lemma 4, and set $X := V(G) \setminus V(M)$.

**Step A: Cliques $B_i \neq R$.** Let $i \in \{1, \dots, r\}$ be any index with $B_i \neq R$ (by Lemma 4(4), this includes all $i \in \{1, \dots, r - 1\}$). Let $P(B_i)$ be the parent of $B_i$ in the rooted tree $\mathcal{T}$. By Lemma 3(2), $B_i \cap P(B_i) \neq \emptyset$; choose any vertex $z \in B_i \cap P(B_i)$. We claim $z \in X$:
- We cannot have $z \in e_i$, for otherwise $z \in P(B_i)$ would imply $P(B_i) \in T_z \subseteq T_{e_i}$, contradicting $B_i = \mathrm{top}(T_{e_i})$ since $\mathrm{depth}(P(B_i)) = \mathrm{depth}(B_i) - 1 < \mathrm{depth}(B_i)$.
- We cannot have $z \in e_j$ for any $j \neq i$: since $B_i \in T_{e_i}$, there exists $w \in e_i \cap B_i$; since $z \notin e_i$, we have $z \neq w$, so $\{z, w\} \in E(G)$ (as $z, w \in B_i$ and $B_i$ is a clique), which would violate the induced matching property of $M$ if $z \in e_j$.

Hence $z \in B_i \cap X \neq \emptyset$. Set $C_i := B_i$ for every $i$ with $B_i \neq R$.

**Step B: The case $B_r = R$.** If $B_r \neq R$, then Step A already defines $C_1, \dots, C_r$ with $C_1 \cup \dots \cup C_r = B_1 \cup \dots \cup B_r$ and $C_i \cap X \neq \emptyset$ for all $i$. Assume now that $B_r = R$.
- **Subcase B1: $R \cap X \neq \emptyset$.** Set $C_r := R$. Then $C_1, \dots, C_r$ satisfy (1) and (2) directly by Lemma 4(3) and Step A.
- **Subcase B2: $R \cap X = \emptyset$.** Then $R \subseteq V(M)$. Because $R = B_r \in T_{e_r}$, we have $R \cap e_r \neq \emptyset$. Since $R$ is a clique and $M$ is an induced matching, $R$ cannot intersect $e_j$ for any $j \neq r$; therefore $R \subseteq e_r$. On the other hand, since $G$ is connected and $n \ge 3$, $\deg_G(s) \ge 1$, so $|R| = |N_G[s]| \ge 2 = |e_r|$. It follows that $R = e_r$.

  Write $e_r = \{u_r, v_r\}$. Since $s \in N_G[s] = R = \{u_r, v_r\}$, we may assume without loss of generality that $v_r = s$. Then $N_G[v_r] = N_G[s] = \{u_r, v_r\}$, so $N_G(v_r) = \{u_r\}$; in particular, $e_r = \{u_r, v_r\}$ is the unique edge of $G$ incident to $v_r$. Consequently, **every edge of $G$ intersecting $R = \{u_r, v_r\}$ contains $u_r$**.

  Since $n \ge 3 > 2 = |\{u_r, v_r\}|$, the set $V(G) \setminus \{u_r, v_r\}$ is nonempty. Because $G$ is connected and $N_G(v_r) = \{u_r\}$, the vertex $u_r$ must have at least one neighbor $x \in V(G) \setminus \{u_r, v_r\}$. Because $u_r \in e_r$, $x \notin e_r$, and $M$ is an induced matching, $x$ cannot belong to any $e_j$ ($j \neq r$); hence $x \in X$.

  Set $C_r := \{u_r, x\}$. Then $C_r$ is a clique of $G$ (as $\{u_r, x\} \in E(G)$) with $x \in C_r \cap X \neq \emptyset$. Moreover, every edge of $G$ covered by $B_r = R$ contains $u_r \in C_r$, while $C_i = B_i$ for $1 \le i \le r - 1$. Since $B_1 \cup \dots \cup B_r$ is a vertex cover of $G$ by Lemma 4(3), $C_1 \cup \dots \cup C_r$ is also a vertex cover of $G$. $\square$

---

## 3. Proof of Theorem 1 (Conjecture 5.5)

### Part 1: The $1$-Vertex Deletion Bound and $\mathcal{RV}_{\mathrm{chordal}}(n) \subseteq A(n)$

Let $G$ be a connected chordal graph on $n \ge 3$ vertices, and let $r := \mathrm{im}(G) = \mathrm{reg}(G)$ (by Theorem 2.11 of `arXiv:2603.04876v1`). Since $G$ is connected and $n \ge 3$, we have $E(G) \neq \emptyset$, so $r \ge 1$ and $\mathrm{v}(G) \ge 1$ (since $N_G(\emptyset) = \emptyset$ cannot cover $E(G)$). Furthermore, $r < n/2$: if $G$ had an induced matching $M$ of size $n/2$, then $V(M) = V(G)$ and $G = G[V(M)]$ would be a disjoint union of $n/2 \ge 2$ copies of $K_2$, contradicting connectedness (see also Proposition 2.9 of `arXiv:2603.04876v1`). Hence $m := n - 2r \ge 1$.

By Lemma 5, there exist a maximum induced matching $M$ of $G$ and $r$ cliques $C_1, \dots, C_r$ of $G$ whose union is a vertex cover of $G$ such that $C_i \cap X \neq \emptyset$ for all $1 \le i \le r$, where $X := V(G) \setminus V(M)$ has cardinality $|X| = n - 2r = m \ge 1$.

Consider the pairs $(i, x)$ with $1 \le i \le r$ and $x \in C_i \cap X$. Since each $i \in \{1, \dots, r\}$ contributes at least one pair, there are at least $r$ such pairs distributed among the $m$ vertices of $X$. By the Pigeonhole Principle, there exists a vertex $x^* \in X$ belonging to $t$ of the cliques $C_1, \dots, C_r$, where
$$t \ge \left\lceil \frac{r}{m} \right\rceil = \left\lceil \frac{r}{n - 2r} \right\rceil.$$
Relabeling the cliques if necessary, assume $x^* \in C_1, \dots, C_t$. For each $j \in \{1, \dots, t\}$, because $C_j$ is a clique containing $x^*$, we have $C_j \subseteq N_G[x^*]$.

Set $G' := G - N_G[x^*]$. Then $G'$ is an induced subgraph of $G$, hence chordal. Every edge $e \in E(G')$ intersects $C_1 \cup \dots \cup C_r$ (since $C_1 \cup \dots \cup C_r$ is a vertex cover of $G$), and cannot intersect $C_1 \cup \dots \cup C_t \subseteq N_G[x^*]$ (since $V(G') = V(G) \setminus N_G[x^*]$). Therefore the union of the $r - t$ cliques $C_{t+1} \cap V(G'), \dots, C_r \cap V(G')$ is a vertex cover of $G'$. Since every edge of an induced matching $M'$ of $G'$ must intersect at least one of these $r - t$ cliques while each clique can intersect at most one edge of $M'$, we obtain the $1$-vertex deletion bound:
$$\mathrm{im}\big(G - N_G[x^*]\big) = \mathrm{im}(G') \le r - t \le r - \left\lceil \frac{r}{n - 2r} \right\rceil.$$

Applying Lemma 2 to the chordal graph $G'$, we obtain an independent set $A' \subseteq V(G')$ such that $N_{G'}(A')$ is a vertex cover of $G'$ and
$$|A'| \le \mathrm{im}(G') \le r - \left\lceil \frac{r}{n - 2r} \right\rceil.$$
Define $A := \{x^*\} \cup A'$. Because $A' \subseteq V(G') = V(G) \setminus N_G[x^*]$, we have $x^* \notin A'$ and no edge connects $x^*$ to $A'$. Since $A'$ is independent in the induced subgraph $G'$, $A$ is an independent set of $G$ of size $|A| = 1 + |A'|$. Moreover, $N_G(A)$ is a vertex cover of $G$: for any edge $e \in E(G)$,
- if $x^* \in e$, then the other endpoint of $e$ lies in $N_G(x^*) \subseteq N_G(A)$;
- if $e \cap N_G(x^*) \neq \emptyset$, then $e \cap N_G(A) \neq \emptyset$;
- otherwise $e \cap N_G[x^*] = \emptyset$, so $e \in E(G')$, whence $e$ intersects $N_{G'}(A') \subseteq N_G(A') \subseteq N_G(A)$.

By Definition 2.4 of `arXiv:2603.04876v1`, it follows that
$$\mathrm{v}(G) \le |A| = 1 + |A'| \le r - \left\lceil \frac{r}{n - 2r} \right\rceil + 1.$$
Thus $(r, \mathrm{v}(G)) \in A(n)$, proving $\mathcal{RV}_{\mathrm{chordal}}(n) \subseteq A(n)$ for all $n \ge 3$.

---

### Part 2: The Reverse Inclusion $A(n) \subseteq \mathcal{RV}_{\mathrm{chordal}}(n)$

The reverse inclusion $A(n) \subseteq \mathcal{RV}_{\mathrm{chordal}}(n)$ is already noted in Section 5 (*Future Directions*) of `arXiv:2603.04876v1`, using the explicit connected chordal graphs constructed in Theorem 3.5 of `arXiv:2603.04876v1`. For completeness, we include a concise, self-contained verification of both cases for any $(r, v) \in A(n)$ with $n \ge 3$.

Let $m := n - 2r \ge 1$. Note that for any triple $\{a, b, c\}$ inducing a path $a - b - c$ with $\deg_G(b) = 2$ and $\deg_G(c) = 1$, every independent set $A$ with $N_G(A)$ a vertex cover must satisfy $A \cap \{a, b, c\} \neq \emptyset$ (Lemma 3.4 of `arXiv:2603.04876v1`): indeed, the edge $\{b, c\}$ must hit $N_G(A)$, and since $N_G(c) = \{b\}$ and $N_G(b) = \{a, c\}$, either $b \in A$ or $\{a, c\} \cap A \neq \emptyset$.

- **Case I ($m \ge r$).** Here $\lceil r/m \rceil = 1$, so $1 \le v \le r \le m$. Take $G$ on $n$ vertices
  $$V(G) = \{x_1, \dots, x_v\} \sqcup \{y_1, \dots, y_r\} \sqcup \{z_1, \dots, z_r\} \sqcup \{w_1, \dots, w_{m - v}\}$$
  with edges $\{x_1, x_i\}$ ($2 \le i \le v$), $\{x_1, y_j\}$ ($1 \le j \le r - v + 1$), $\{x_i, y_{r - v + i}\}$ ($2 \le i \le v$), $\{y_j, z_j\}$ ($1 \le j \le r$), and $\{x_1, w_k\}$ ($1 \le k \le m - v$). Then $G$ is a tree on $n$ vertices, hence connected and chordal.
  - *Regularity:* $\{\{y_j, z_j\} : 1 \le j \le r\}$ is an induced matching of size $r$, so $\mathrm{im}(G) \ge r$. For any induced matching $M'$ of $G$, partition $E(G)$ into $W := \{\{x_1, w_k\} : 1 \le k \le m - v\}$, the $r - v + 1$ sets $H_j := \{\{x_1, y_j\}, \{y_j, z_j\}\}$ ($1 \le j \le r - v + 1$), and the $v - 1$ sets $F_i := \{\{x_1, x_i\}, \{x_i, y_{r-v+i}\}, \{y_{r-v+i}, z_{r-v+i}\}\}$ ($2 \le i \le v$). Each $H_j$ and each $F_i$ contains at most one edge of $M'$ (any two edges in the same set either share a vertex or are joined by the middle edge $\{x_i, y_{r-v+i}\}$). If $M' \cap W = \emptyset$, then $|M'| \le (r - v + 1) + (v - 1) = r$. If $M'$ contains an edge $\{x_1, w_k\} \in W$, then $M'$ contains no other edge of $W$ and no edge of any $H_j$ (as every edge of $H_j$ touches $x_1$ or $y_j \in N_G(x_1)$), so $|M'| \le 1 + (v - 1) = v \le r$. Hence $\mathrm{reg}(G) = \mathrm{im}(G) = r$.
  - *$\mathrm{v}$-number:* $A_0 := \{x_1\} \cup \{y_{r-v+2}, \dots, y_r\}$ is an independent set of size $v$ whose neighborhood covers every edge of $G$, giving $\mathrm{v}(G) \le v$. Conversely, the $v$ pairwise disjoint triples $P_1 := \{x_1, y_1, z_1\}$ and $P_i := \{x_i, y_{r-v+i}, z_{r-v+i}\}$ ($2 \le i \le v$) each induce a pendant $P_3$ with $\deg_G(y_\ell) = 2$ and $\deg_G(z_\ell) = 1$, so any independent set $A$ with $N_G(A)$ a vertex cover hits every $P_i$, giving $|A| \ge v$. Thus $\mathrm{v}(G) = v$.

- **Case II ($m < r$).** Set $t_1 := r - v + 1$. Since $1 \le v \le r - \lceil r/m \rceil + 1$ and $m < r$, we have $2 \le \lceil r/m \rceil \le t_1 \le r$. Because $t_1 \le r \le m t_1$, we may choose integers $t_2, \dots, t_m \in [0, t_1]$ with $\sum_{i=1}^m t_i = r$; relabeling $t_2, \dots, t_m$ so positive entries come first, let $q \in \{1, \dots, m\}$ be such that $t_1, \dots, t_q \ge 1$ and $t_{q+1} = \dots = t_m = 0$. Define $G$ on $n = m + 2\sum_{i=1}^q t_i$ vertices
  $$V(G) = \{x_1, \dots, x_m\} \sqcup \bigsqcup_{i=1}^q \{y_{i1}, \dots, y_{it_i}, z_{i1}, \dots, z_{it_i}\}$$
  by placing a clique $K_q$ on $\{x_1, \dots, x_q\}$, adding pendant edges $\{x_1, x_i\}$ for $q + 1 \le i \le m$, and adding pendant paths $x_i - y_{ij} - z_{ij}$ for $1 \le i \le q$, $1 \le j \le t_i$. Then $G$ is connected and chordal (every cycle lies inside the clique $\{x_1, \dots, x_q\}$).
  - *Regularity:* $M_0 := \{\{y_{ij}, z_{ij}\} : 1 \le i \le q,\; 1 \le j \le t_i\}$ is an induced matching of size $r$, so $\mathrm{im}(G) \ge r$. Conversely, let $M'$ be any induced matching of $G$. Every edge outside $M_0$ is incident to the clique $\{x_1, \dots, x_q\}$, so at most one edge $e_0 \in M'$ can lie outside $M_0$. If no such $e_0$ exists, then $M' \subseteq M_0$ and $|M'| \le r$. If $e_0 \in M' \setminus M_0$ exists, pick $x_k \in e_0 \cap \{x_1, \dots, x_q\}$; then no edge $\{y_{kj}, z_{kj}\}$ ($1 \le j \le t_k$) can belong to $M'$ (as $y_{kj}$ is adjacent to $x_k$), so $|M'| \le 1 + (r - t_k) \le r$ since $t_k \ge 1$. Hence $\mathrm{reg}(G) = \mathrm{im}(G) = r$.
  - *$\mathrm{v}$-number:* $B := \{x_1\} \cup \{y_{ij} : 2 \le i \le q,\; 1 \le j \le t_i\}$ is an independent set of size $1 + (r - t_1) = v$ whose neighborhood contains $\{x_2, \dots, x_m\} \cup \{y_{11}, \dots, y_{1t_1}\} \cup \{z_{ij} : 2 \le i \le q,\; 1 \le j \le t_i\}$ and covers every edge of $G$; hence $\mathrm{v}(G) \le v$. Conversely, let $A$ be any independent set with $N_G(A)$ a vertex cover of $G$. For every $1 \le i \le q$ and $1 \le j \le t_i$, the triple $\{x_i, y_{ij}, z_{ij}\}$ induces a pendant $P_3$ with $\deg_G(y_{ij}) = 2$ and $\deg_G(z_{ij}) = 1$, so $A \cap \{x_i, y_{ij}, z_{ij}\} \neq \emptyset$. Since $\{x_1, \dots, x_q\}$ is a clique, $|A \cap \{x_1, \dots, x_q\}| \le 1$. If $A \cap \{x_1, \dots, x_q\} = \emptyset$, then $A$ meets every pair $\{y_{ij}, z_{ij}\}$, giving $|A| \ge \sum_{i=1}^q t_i = r > r - t_1 + 1 = v$ (since $t_1 \ge 2$). If $A \cap \{x_1, \dots, x_q\} = \{x_k\}$, then for every $i \in \{1, \dots, q\} \setminus \{k\}$ and $1 \le j \le t_i$, $A$ meets $\{y_{ij}, z_{ij}\}$; since these pairs are pairwise disjoint and disjoint from $\{x_k\}$, we obtain
    $$|A| \ge 1 + \sum_{i \neq k} t_i = 1 + r - t_k \ge 1 + r - t_1 = v.$$
    Thus $\mathrm{v}(G) = v$.

Combining Parts 1 and 2 gives $\mathcal{RV}_{\mathrm{chordal}}(n) = A(n)$ for all $n \ge 3$, completing the proof of Theorem 1 and Conjecture 5.5. $\square$

---

## 4. Computational Verification

The accompanying exact-arithmetic script `verify.py` verifies every constructive step of Lemmas 2–5 and Theorem 1 (including Dirac simplicial roots $R = N_G[s]$, clique tree axioms, greedy bottom-up clique covers and maximum induced matchings, Subcase B2 leaf replacements, pigeonhole vertices $x^* \in X$ satisfying $\mathrm{im}(G - N_G[x^*]) \le r - \lceil r/(n-2r) \rceil$, and Saha–Sengupta witnesses $A$) across all $352$ connected chordal graphs on $n = 3, \dots, 7$ (for every simplicial root), paths $P_3, \dots, P_{25}$, $1{,}550$ random chordal graphs on $n = 8, \dots, 20$, and tight extremal graphs up to $n = 30$, as well as exact realizability of all $42$ lattice points in $A(n)$ for $n = 3, \dots, 11$. Running `.venv/bin/python verify.py` outputs `PASS`.

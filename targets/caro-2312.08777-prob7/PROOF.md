# Proof: Exact Determination of $b(t)$ for $t$-Neighbourhood Flip Graphs

**Theorem.** For every integer $t \ge 1$ (and in particular for every $t \ge 2$),
$$b(t) = 3.$$
Specifically:
1. No $([t], (b, r))$-flip graph exists with $b \in \{1, 2\}$.
2. For every $t \ge 1$, there exists a $([t], (3, 4))$-flip graph.

---

## 1. Lower Bound: $b(t) \ge 3$

Suppose $G = (V, E)$ with edge-colouring $f : E \to \{1, 2\}$ is a $([t], (b, r))$-flip graph for some $t \ge 1$ and positive integers $b < r$. By definition (`sections/section6.tex`), $E(1)$ spans a $b$-regular subgraph, $E(2)$ spans an $r$-regular subgraph, and for every $v \in V$ and every $1 \le s \le t$,
$$e_{2, s}[v] < e_{1, s}[v].$$

Evaluating at $s = 1$, every vertex $v \in V$ satisfies $e_{2, 1}[v] < e_{1, 1}[v]$. Let $B = 1$ and $R = 2$. For $v \in V$, let $e_B(v) = |E(B) \cap E(N_1(v))|$ and $e_R(v) = |E(R) \cap E(N_1(v))|$, so $e_{1, 1}[v] = b + e_B(v)$ and $e_{2, 1}[v] = r + e_R(v)$, whence
$$r - b < e_B(v) - e_R(v) \qquad (\forall v \in V).$$

For $X, Y, Z \in \{B, R\}$, let $T_{XYZ}(v)$ count the triangles in $G$ containing $v$ whose two edges incident to $v$ have colours $X, Y$ and whose edge opposite $v$ has colour $Z$ (treating $BRR = RBR$ and $BRB = RBB$ as the same type). Then
$$e_B(v) = T_{BBB}(v) + T_{BRB}(v) + T_{RRB}(v), \qquad e_R(v) = T_{RRR}(v) + T_{BBR}(v) + T_{BRR}(v).$$
Each triangle with two $R$-edges and one $B$-edge is of type $BRR$ at two vertices and type $RRB$ at one vertex; each triangle with two $B$-edges and one $R$-edge is of type $BBR$ at one vertex and type $BRB$ at two vertices. Summing over all $v \in V$ gives
$$2 \sum_{v \in V} T_{RRB}(v) = \sum_{v \in V} T_{BRR}(v), \qquad 2 \sum_{v \in V} T_{BBR}(v) = \sum_{v \in V} T_{BRB}(v).$$
Therefore,
$$\begin{aligned}
\sum_{v \in V} \bigl(e_B(v) - e_R(v)\bigr)
&= \sum_{v \in V} \bigl(T_{BBB}(v) + T_{BBR}(v) - T_{RRB}(v) - T_{RRR}(v)\bigr) \\
&\le \sum_{v \in V} \bigl(T_{BBB}(v) + T_{BBR}(v)\bigr).
\end{aligned}$$
For every $v \in V$, $T_{BBB}(v) + T_{BBR}(v)$ counts edges in $G$ whose endpoints both lie in the $b$-element blue neighbourhood $N_1^{(B)}(v)$ of $v$, so $T_{BBB}(v) + T_{BBR}(v) \le \binom{b}{2}$. Hence $\sum_{v \in V} (e_B(v) - e_R(v)) \le |V| \binom{b}{2}$, so there exists $v \in V$ with $e_B(v) - e_R(v) \le \binom{b}{2}$. Consequently,
$$r - b < \binom{b}{2} \implies r < b + \binom{b}{2} = \binom{b+1}{2}.$$
Since $b < r$ are integers, $b + 1 \le r \le \binom{b+1}{2} - 1$. For $b = 1$ this reads $2 \le 0$, and for $b = 2$ this reads $3 \le 2$, both impossible. Hence $b \ge 3$, proving $b(t) \ge 3$.

---

## 2. Upper Bound: Construction of a $([t], (3, 4))$-Flip Graph

Let $t \ge 2$ be any integer (the case $t = 1$ follows by restriction, or the same construction with $g(H) \ge 4$).

### 2.1. Base graph and blow-up construction

By the Erdős–Sachs Theorem (Theorem 6.2 of `arXiv:2312.08777v1`), there exists a finite connected $16$-regular simple graph $H$ of girth $g(H) \ge 2t + 2$.

Define a graph $G$ with edge-colouring $f : E(G) \to \{1, 2\}$ as follows:
- **Vertices:** $V(G) = V(H) \times \{1, 2, 3, 4\}$. For each $x \in V(H)$, write $C_x := \{x\} \times \{1, 2, 3, 4\}$.
- **Colour $1$ (blue) edges:** For each $x \in V(H)$, place all $\binom{4}{2} = 6$ edges on $C_x$, making $G[C_x] \cong K_4$, and colour them $1$.
- **Colour $2$ (red) edges:** At each vertex $x \in V(H)$, partition its $16$ incident edges in $H$ into $4$ disjoint parts $E_x(1), E_x(2), E_x(3), E_x(4)$ of size $4$ each. For each edge $e = xy \in E(H)$, let $i \in \{1,2,3,4\}$ be the unique index with $e \in E_x(i)$ and $j \in \{1,2,3,4\}$ the unique index with $e \in E_y(j)$, and add the edge $\{(x, i), (y, j)\}$ to $G$ with colour $2$.

**Basic properties of $G$:**
- Since $H$ is simple, every red edge joins vertices in distinct cliques $C_x \neq C_y$, whereas every blue edge lies inside a single $C_x$; moreover, distinct edges of $H$ join distinct pairs $\{x, y\}$ and hence cannot yield parallel red edges. Thus $G$ is a **simple** graph with $E(1) \cap E(2) = \emptyset$.
- Every vertex $(x, i) \in V(G)$ has $\deg_1((x, i)) = 3$ (the other three vertices of $C_x$) and $\deg_2((x, i)) = |E_x(i)| = 4$. Thus $G$ is $7$-regular with $(a_1, a_2) = (3, 4)$ and $3 < 4$.

### 2.2. Exact local structure of $N_s[v]$ for $1 \le s \le t$

Fix an arbitrary vertex $v = (x_0, i_0) \in V(G)$, and let $\pi : V(G) \to V(H)$ denote the projection $\pi(x, i) = x$. Let $B_H(x_0, t) := \{x \in V(H) : d_H(x_0, x) \le t\}$.

**Claim 1.** *The induced subgraph $T_{x_0} := H[B_H(x_0, t)]$ is a tree rooted at $x_0$, and for every $u \in N_t[v]$, every shortest path from $v$ to $u$ in $G$ projects under $\pi$ into $T_{x_0}$.*

*Proof.* If $H[B_H(x_0, t)]$ contained a cycle, take any edge $yz$ of that cycle not in a breadth-first search tree of $H[B_H(x_0, t)]$ rooted at $x_0$. The BFS paths from $x_0$ to $y$ and $z$ each have length at most $t$, so together with $yz$ they form a closed walk in $H$ of length at most $2t + 1$ traversing $yz$ exactly once, which contains a cycle of length at most $2t + 1 < 2t + 2 \le g(H)$, a contradiction. Thus $T_{x_0}$ is a tree (it is connected by definition of $B_H(x_0, t)$). Every edge of $G$ maps under $\pi$ either to a single vertex (blue edge) or an edge of $H$ (red edge), so any path of length $\le t$ in $G$ starting at $v$ projects to a walk of length $\le t$ in $H$ starting at $x_0$, which stays inside $B_H(x_0, t) = V(T_{x_0})$. $\square$

For each $x \in V(T_{x_0}) \setminus \{x_0\}$, let $p(x)$ be the unique parent of $x$ in $T_{x_0}$. Since $H$ is simple, there is a unique edge $p(x)x \in E(H)$, lifting to a unique red edge $e_x = \{(p(x), i_x), (x, j_x)\}$ between $C_{p(x)}$ and $C_x$. Define the **entry vertex** of $C_x$ by $x^* := (x, j_x)$ for $x \in V(T_{x_0}) \setminus \{x_0\}$, and set $x_0^* := v$.

**Claim 2.** *For every $x \in V(T_{x_0})$ and every $u = (x, j) \in C_x$, if $d_G(v, u) \le t$ then*
$$d_G(v, u) = d_G(v, x^*) + \mathbf{1}_{u \neq x^*},$$
*where $\mathbf{1}_{u \neq x^*} = 1$ if $u \neq x^*$ and $0$ if $u = x^*$. In particular, for $1 \le s \le t$, every edge of $G[N_s[v]]$ is either a blue edge inside $C_x$ for some $x \in V(T_{x_0})$ with $x^* \in N_{s-1}[v]$, or a red edge $e_x$ ($x \in V(T_{x_0}) \setminus \{x_0\}$) with $(p(x), i_x) \in N_{s-1}[v]$ and $x^* \in N_s[v]$.*

*Proof.* For $x = x_0$, $d_G(v, v) = 0$ and the three vertices $(x_0, j) \neq v$ in $C_{x_0}$ are blue neighbours of $v$ at distance $1$. Now let $x \in V(T_{x_0}) \setminus \{x_0\}$. By Claim 1, every path in $G$ from $v$ to $u \in C_x$ of length $\le t$ projects to a walk in the tree $T_{x_0}$ from $x_0$ to $x$, which must traverse the unique edge $p(x)x$ of $T_{x_0}$, so the path in $G$ must traverse $e_x$ and hence visit $x^*$. Since $u$ is adjacent to $x^*$ via a blue edge when $u \neq x^*$, we have $d_G(v, u) = d_G(v, x^*) + \mathbf{1}_{u \neq x^*}$ whenever $d_G(v, u) \le t$. Because $d_G(v, x^*) \le d_G(v, u)$ for all $u \in C_x$, the blue edges of $C_x$ lie in $G[N_s[v]]$ if and only if all of $C_x$ lies in $N_s[v]$, which holds if and only if $d_G(v, x^*) \le s - 1$. By Claim 1, the only red edges with both endpoints in $N_s[v]$ are lifts $e_x$ of edges $p(x)x$ of $T_{x_0}$; since every path from $v$ to $x^*$ visits $(p(x), i_x)$ right before $x^*$, we have $d_G(v, x^*) = d_G(v, (p(x), i_x)) + 1$ whenever $x^* \in N_s[v]$. $\square$

### 2.3. Layer counts and verification of $e_{1, s}[v] > e_{2, s}[v]$

For $0 \le s \le t$, let $L_s := \{u \in V(G) : d_G(v, u) = s\}$. By Claim 2, for $1 \le s \le t$, $L_s$ splits into:
- **Type $A$** vertices: entry vertices $x^* \in L_s$ ($x \neq x_0$), of which there are $A_s$;
- **Type $B$** vertices: non-entry vertices $(x, j) \neq x^*$ in $L_s$, of which there are $B_s$.

Notice that every vertex $u \in L_s$ ($1 \le s \le t - 1$) satisfies $d_H(x_0, \pi(u)) \le s \le t - 1$, so all $4$ neighbours of $\pi(u)$ via the edges assigned to $u$ in $H$ lie in $B_H(x_0, t) = V(T_{x_0})$. In particular:
- Each type-$A$ vertex $x^* \in L_s$ ($1 \le s \le t-1$) has $1$ incoming red edge $e_x$ from $(p(x), i_x) \in L_{s-1}$ and $3$ outgoing red edges $e_y$ to distinct children $y$ of $x$ in $T_{x_0}$, whose endpoints $y^*$ lie in $L_{s+1}$ (as type $A$). It also has $3$ blue neighbours $(x, j) \neq x^*$ in $C_x$, all lying in $L_{s+1}$ (as type $B$).
- Each type-$B$ vertex $(x, j) \in L_s$ ($1 \le s \le t-1$) has $x^* \in L_{s-1}$, so all $6$ blue edges of $C_x$ are already inside $N_s[v]$. It has $4$ outgoing red edges $e_y$ to distinct children $y$ of $x$ in $T_{x_0}$, whose endpoints $y^*$ lie in $L_{s+1}$ (as type $A$).

For $s = 1$: $L_0 = \{v\}$, so $A_1 = 4$ (the $4$ red neighbours of $v$) and $B_1 = 3$ (the $3$ blue neighbours of $v$ in $C_{x_0}$). By Claim 2, $G[N_1[v]]$ contains the $6$ blue edges of $C_{x_0}$ and the $4$ red edges incident to $v$, so
$$e_{1, 1}[v] = 6 > 4 = e_{2, 1}[v].$$

For $1 \le s \le t - 1$, going from $N_s[v]$ to $N_{s+1}[v]$:
- By Claim 2, the new blue edges in $N_{s+1}[v]$ are precisely the $6$ blue edges of $C_x$ for each $x^* \in L_s$, so $e_{1, s+1}[v] - e_{1, s}[v] = 6 A_s$.
- The new red edges in $N_{s+1}[v]$ are precisely the outgoing red edges from $L_s$ to $L_{s+1}$, of which each type-$A$ vertex in $L_s$ contributes $3$ and each type-$B$ vertex in $L_s$ contributes $4$.

Hence for all $1 \le s \le t - 1$:
$$e_{1, s+1}[v] - e_{1, s}[v] = 6 A_s, \qquad e_{2, s+1}[v] - e_{2, s}[v] = 3 A_s + 4 B_s,$$
and the layer sizes obey the recurrence
$$A_{s+1} = 3 A_s + 4 B_s, \qquad B_{s+1} = 3 A_s \qquad (1 \le s \le t - 1).$$

Let us verify $e_{1, s}[v] > e_{2, s}[v]$ for all $1 \le s \le t$:
- For $s = 1$: $e_{1, 1}[v] = 6 > 4 = e_{2, 1}[v]$.
- For $s = 2$ (if $t \ge 2$): $e_{1, 2}[v] = 6 + 6 \cdot 4 = 30$ and $e_{2, 2}[v] = 4 + 3 \cdot 4 + 4 \cdot 3 = 28$, so $e_{1, 2}[v] = 30 > 28 = e_{2, 2}[v]$, with $A_2 = 24$ and $B_2 = 12$.
- For $2 \le s \le t - 1$: we claim $5 A_{s-1} \le A_s \le 6 A_{s-1}$ for all $2 \le s \le t$.
  - Base case $s = 2$: $A_1 = 4, A_2 = 24 = 6 A_1$, so $5 A_1 \le A_2 \le 6 A_1$.
  - Inductive step ($2 \le s \le t - 1$): assuming $5 A_{s-1} \le A_s \le 6 A_{s-1}$, we have $B_s = 3 A_{s-1}$, so
    $$A_{s+1} = 3 A_s + 4 B_s = 3 A_s + 12 A_{s-1}.$$
    Using $A_{s-1} \ge \frac{1}{6} A_s$ gives $A_{s+1} \ge 3 A_s + 2 A_s = 5 A_s$; using $A_{s-1} \le \frac{1}{5} A_s$ gives $A_{s+1} \le 3 A_s + \frac{12}{5} A_s = \frac{27}{5} A_s < 6 A_s$.

  Therefore, for all $2 \le s \le t - 1$, $A_s \ge 5 A_{s-1}$, so
  $$\bigl(e_{1, s+1}[v] - e_{1, s}[v]\bigr) - \bigl(e_{2, s+1}[v] - e_{2, s}[v]\bigr) = 6 A_s - (3 A_s + 4 B_s) = 3 A_s - 12 A_{s-1} \ge 3 A_{s-1} > 0.$$
  By induction on $s$, $e_{1, s}[v] > e_{2, s}[v]$ for every $1 \le s \le t$.

Since $v \in V(G)$ was arbitrary, $G$ is a $([t], (3, 4))$-flip graph, so $b(t) \le 3$. Combining with Section 1 gives $b(t) = 3$ for all $t \ge 1$ (and in particular for all $t \ge 2$). $\blacksquare$

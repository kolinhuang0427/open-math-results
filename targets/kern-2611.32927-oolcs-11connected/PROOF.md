# Resolution: `On-Off` & `Weighted Local-Con Switching` on $\{1,1\}$-Bounded Connected Switches (`kern-2611.32927-oolcs-11connected`)

## Main Result

We answer the first open question of Kern, Firbas, and Sorge (`arXiv:2611.32927v1`, `sections/conclusion.tex`, line 5) in the **affirmative** — in fact for the full weighted problem $\mathrm{Weighted Local-Con Switching}$ (`WLCS`, and hence its special case `OOLCS`) with arbitrary real weights:

**Theorem 1:** *$\mathrm{Weighted Local-Con Switching}$ (`WLCS`) — and in particular $\mathrm{On-Off Local-Con Switching}$ (`OOLCS`) — restricted to $\{1,1\}$-bounded connected switches is solvable in polynomial time (specifically $O(|V^*|(|E^*| + |V^*|\log|V^*|)) = O(m^2 \log m)$ via Edmonds' minimum-weight perfect matching on an auxiliary graph with $|V^*| \le 2n + 6m$ vertices and $|E^*| \le 9m + n$ edges).*

---

## Proof of Theorem 1

Let $(\widehat{G}, a, b, w, \lambda)$ be an instance of `WLCS` where every switch $s \in \mathcal{S}(\widehat{G})$ is $\{1,1\}$-bounded and connected ($G[s]$ is connected, $|s| \le 2$, $|s[i]| \le 1$ for all $i \in [|s|]$).

### 1. Normalization and Weight Shifting
For each switch $s \in \mathcal{S}(\widehat{G})$:
- Let $m_s := \min_{i \in [|s|]} w(s, i)$ be its minimum position weight, and replace $w$ by the shifted non-negative weight function $w'(s, i) := w(s, i) - m_s \ge 0$, updating the budget to $\lambda' := \lambda - \sum_{s \in \mathcal{S}(\widehat{G})} m_s$. Clearly $w(c) \le \lambda \iff w'(c) \le \lambda'$.
- Classify each $\{1,1\}$-bounded connected switch $s$ (`|E(G[s])| <= 2` and $G[s]$ connected):
  1. **Redundant-position switches (`|E(G[s])| = 1`, say $E(G[s]) = \{e\}$):**
     - If $|s| = 1$ or $s[0] = s[1] = \{e\}$, then $e$ is a static edge of shifted cost $0$.
     - If $s$ has one position $\{e\}$ and one empty position $\emptyset$: if $w'(s, \text{edge}) = 0$, setting $s$ to $\{e\}$ always gives cost $0$ and only helps connectivity, so we treat $e$ as a static edge of cost $0$. Otherwise $w'(s, \emptyset) = 0$ and $w'(s, \text{edge}) > 0$, so using edge $e$ incurs cost $w'(s, \text{edge})$ (in the multigraph, $e$ forms its own singleton switch class).
  2. **$P_3$-switches (`|E(G[s])| = 2`, say $s[0] = \{e_0\}$ and $s[1] = \{e_1\}$ with $e_0 \neq e_1$):**
     Because $G[s]$ is connected with two distinct edges, $e_0$ and $e_1$ **must share a common center vertex** $z_s$ (so $e_0 = u_s z_s$ and $e_1 = z_s v_s$ with $u_s \neq v_s$). Assign multigraph edge $e_0$ shifted cost $c(e_0) := w'(s, 0) \ge 0$ and multigraph edge $e_1$ shifted cost $c(e_1) := w'(s, 1) \ge 0$.

Note that in all cases, every multigraph edge $e \in E(\widehat{G})$ belongs to a unique switch $s$, has shifted cost $c(e) \ge 0$, and **no two edges of the same switch can be vertex-disjoint**.

### 2. Characterization via Simple Transition-Compatible Paths
For each vertex $v \in V(\widehat{G})$, partition its incident multigraph edges $E_v$ into classes $\{C_{v, s}\}$ indexed by the switches $s$ incident to $v$: if $s$ is a $P_3$-switch with center $v$, then $|C_{v, s}| = 2$; otherwise $|C_{v, s}| = 1$. Call a simple $a$--$b$ path $P$ in the multigraph $E(\widehat{G})$ **class-valid** if at every vertex $v \in V(P)$, $P$ uses at most one edge from each class $C_{v, s}$ (i.e., $P$ never enters $z_s$ via one edge of a $P_3$-switch $s$ and exits $z_s$ via the other edge of $s$).

**Claim 1:** *There exists a configuration $c \in \mathcal{C}(\widehat{G})$ connecting $a$ to $b$ with $w'(c) \le \lambda'$ if and only if there exists a simple class-valid $a$--$b$ path $P$ with $\sum_{e \in E(P)} c(e) \le \lambda'$.*

*Proof.*
- $(\Rightarrow)$ Given $c$ with $w'(c) \le \lambda'$ and an $a$--$b$ path in $\widehat{G} \circ c$, take a simple $a$--$b$ path $P$ in $\widehat{G} \circ c$ (selecting for each edge of $P$ one switch edge realizing it in $\widehat{G} \circ c$). Since $c$ selects at most one edge from each switch $s$, $P$ never uses both edges of any switch $s$, hence is class-valid. Moreover, each edge $e \in E(P)$ forces $s_e$ into the position containing $e$ (paying $c(e)$), and switches can only contribute disjointly across $E(P)$, so $\sum_{e \in E(P)} c(e) \le \sum_s w'(s, c(s)) = w'(c) \le \lambda'$.
- $(\Leftarrow)$ Suppose $P$ is a simple class-valid $a$--$b$ path with $\sum_{e \in E(P)} c(e) \le \lambda'$. Because $P$ is **simple**, $P$ visits each vertex $v \in V(\widehat{G})$ at most once; and because any two edges of the same switch $s$ share its center $z_s$ and $P$ is class-valid at $z_s$, $P$ uses **at most one edge from each switch $s$**. Thus setting $c(s)$ to the position containing $E(P) \cap E(G[s])$ (if non-empty) and to a minimum-weight position ($w' = 0$) otherwise yields a valid configuration $c$ realizing $P$ with $w'(c) = \sum_{e \in E(P)} c(e) \le \lambda'$. $\square$

### 3. Reduction to Minimum-Weight Perfect Matching
Construct an undirected auxiliary graph $G^* = (V^*, E^*)$ with non-negative edge weights $W^*$:
1. For each multigraph edge $e = uv \in E(\widehat{G})$, create two half-edge vertices $e_u, e_v$ joined by an edge $e_u e_v$ of weight $W^*(e_u e_v) = 0$.
2. For each vertex $v \in V(\widehat{G})$:
   - Create hub vertices: $H_v = \{h_{v,1}, h_{v,2}\}$ if $v \notin \{a, b\}$ (joined by edge $h_{v,1} h_{v,2}$ of weight $0$), and $H_a = \{h_{a,1}\}$, $H_b = \{h_{b,1}\}$ for the terminals (if $a$ or $b$ has no incident edges, return `NO`). Delete any isolated vertices $v \notin \{a, b\}$.
   - For each non-empty class $C_{v, s}$ at $v$, create two class vertices $c_{v,s}, c'_{v,s}$ joined by an edge $c_{v,s} c'_{v,s}$ of weight $0$; connect every $h \in H_v$ to $c'_{v,s}$ with weight $0$; and for each $e \in C_{v,s}$, connect $e_v$ to $c_{v,s}$ with weight $W^*(e_v c_{v,s}) = \frac{1}{2} c(e)$ (or equivalently, for exact integer arithmetic, scale all edge weights by $2$ so $W^*(e_v c_{v,s}) = c(e)$ against the scaled budget $2\lambda'$).

**Claim 2:** *$G^*$ admits a perfect matching of weight $\le \lambda'$ (equivalently $\le 2\lambda'$ under integer-doubled edge weights $c(e)$ per half-edge) if and only if $\widehat{G}$ admits a simple class-valid $a$--$b$ path $P$ with $\sum_{e \in E(P)} c(e) \le \lambda'$.*

*Proof.*
- $(\Leftarrow)$ Given a simple class-valid $a$--$b$ path $P$: for every $e = uv \in E(P)$ belonging to switch $s$, match $e_u$ to $c_{u,s}$ and $e_v$ to $c_{v,s}$ (total weight $\sum_{e \in E(P)} c(e)$); for every $e \notin E(P)$, match $e_u$ to $e_v$ (weight $0$). At each $v \in V(P) \setminus \{a, b\}$, exactly two distinct classes $s_1 \neq s_2$ have an unmatched $c'_{v, s_1}, c'_{v, s_2}$, which match to $h_{v,1}, h_{v,2}$ (weight $0$); at $a$ and $b$, the unique active class matches $c'_{a, s}$ to $h_{a,1}$ (resp. $h_{b,1}$); and at every untouched class $(v, s)$ or unvisited $v \notin V(P)$, match $c_{v,s}$ to $c'_{v,s}$ and $h_{v,1}$ to $h_{v,2}$ (all weight $0$). This is a perfect matching in $G^*$ of exact weight $\sum_{e \in E(P)} c(e) \le \lambda'$.
- $(\Rightarrow)$ Conversely, let $M$ be any perfect matching in $G^*$ of weight $\le \lambda'$, and let $E_M := \{e = uv \in E(\widehat{G}) : e_u e_v \notin M\}$. For each class $(v, s)$, if $c_{v,s} c'_{v,s} \in M$, then $0$ edges of $C_{v,s}$ lie in $E_M$; otherwise $c_{v,s}$ matches to exactly one $e_v$ ($e \in C_{v,s}$) and $c'_{v,s}$ matches to a hub in $H_v$. Because $|H_v| = 2$ for $v \notin \{a,b\}$ and $|H_a| = |H_b| = 1$ (with $h_{v,1} h_{v,2}$ either in $M$ or not), in the multigraph $(V(\widehat{G}), E_M)$:
  - $a$ and $b$ each have degree $1$,
  - every $v \notin \{a, b\}$ has degree $0$ or $2$, and
  - every vertex $v$ uses **at most one edge per class $C_{v,s}$**!
  Hence $(V(\widehat{G}), E_M)$ decomposes into one simple class-valid $a$--$b$ path $P$ plus zero or more vertex-disjoint class-valid cycles $C_1, \dots, C_r$. Because every $c(e) \ge 0$, dropping all edges of $C_1, \dots, C_r$ leaves a simple class-valid $a$--$b$ path $P$ with
  $$\sum_{e \in E(P)} c(e) \le \sum_{e \in E_M} c(e) = W^*(M) \le \lambda'. \qquad \square$$

Since $|V^*| \le 2n + 6m$ and $|E^*| \le 9m + n$ (as $\sum_v \sum_s |C_{v,s}| = 2m$ and $\sum_v |\{\text{classes at } v\}| \le 2m$), computing a minimum-weight perfect matching in $G^*$ via Edmonds' algorithm takes polynomial time ($O(|V^*|(|E^*| + |V^*|\log|V^*|))$), establishing Theorem 1. $\square$

---

## Verification

Exact brute-force verification in `verify.py` (`OVERALL: PASS`) checks:
- Equivalence between brute-force `OOLCS`/`WLCS` on $\{1,1\}$-bounded connected switch graphs and exact integer-doubled minimum-weight perfect matching on $G^*$ across tricky $P_3$-switch topologies, including:
  - A **non-simple-walk trap** (where a shortest class-valid walk revisits $w$ via a $0$-weight triangle to bypass a $P_3$-forbidden transition, yet no simple path exists at weight $0$, which $G^*$ correctly rejects!),
  - Parallel multigraph edges between the same vertex pair from distinct switches, and
  - Disconnected $0$-weight cycle components alongside a positive-weight $a$--$b$ path.

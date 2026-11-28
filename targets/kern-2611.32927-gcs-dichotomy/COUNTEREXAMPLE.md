# Counterexample: Disproof of the `Global-Con Switching` Matroid-Switch Dichotomy (`kern-2611.32927-gcs-dichotomy`)

## Verdict

The dichotomy conjecture of Kern, Firbas, and Sorge (`arXiv:2611.32927v1`, `sections/gcon.tex`, line 116) is **FALSE** (assuming $\mathsf{P} \neq \mathsf{NP}$, and unconditionally fails the claimed characterization that only matroid-switch families lie in $\mathsf{P}$): there exist explicit families $\Pi$ of **non-matroid switches** (including a $\{2,1\}$-bounded graph-shape-defined family matching the exact formalism of Theorem `thm:dichotomy-lcs` and Theorem `thm:gcs-21-npc`, a non-dominated family requiring genuine Matroid Intersection, and a family whose every position is an acyclic spanning tree) for which $\mathrm{Global-Con Switching}$ (`GCS`) is solvable in **polynomial time** (hence cannot be $\mathsf{NP}$-complete unless $\mathsf{P} = \mathsf{NP}$).

---

## 1. Counterexample 1: All $\{2,1\}$-Bounded $K_3$-Shaped Switches ($\Pi_1$)

Matching the exact `(size-bound, graph-shape)` parameterization of Theorem `thm:gcs-21-npc` (`{2,1}`-bounded $\mathcal{K}_{1,\star}$-shaped switches, `gcon.tex` line 113) and Theorem `thm:dichotomy-lcs` (`stcon.tex` line 149), define:
$$\Pi_1 := \{\text{all } \{2,1\}\text{-bounded } K_3\text{-shaped switches } s\}.$$

### 1.1. Structure and Non-Matroid Proof
Let $s \in \Pi_1$ be any switch in $\Pi_1$. By definition (`preliminaries.tex`, lines 15–17):
- $G[s] \cong K_3$ on three vertices $\{u, v, w\}$ with $|E(G[s])| = 3$, and $E(G[s]) = s[0] \cup s[1]$ (since $s$ is $\{2,1\}$-bounded, $|s| \le 2$; if $|s| = 1$ then $|s[0]| \le 2 < 3$, impossible).
- By $\{2,1\}$-boundedness, up to relabeling positions, $|s[0]| \le 2$ and $|s[1]| \le 1$. Since $|s[0]| + |s[1]| \ge |E(G[s])| = 3$, necessarily $|s[0]| = 2$, $|s[1]| = 1$, and $s[0] \cap s[1] = \emptyset$.
- Up to isomorphism on $\{u, v, w\}$, $s[0] = \{uv, vw\}$ and $s[1] = \{uw\}$.

**Claim 1:** *Every switch $s \in \Pi_1$ is NOT a matroid switch.*
*Proof.* Let $A = s[1] = \{uw\} \in \mathcal{I}_s$ ($|A| = 1$) and $B = s[0] = \{uv, vw\} \in \mathcal{I}_s$ ($|B| = 2$). For every $e \in B \setminus A = \{uv, vw\}$, the set $A \cup \{e\}$ equals either $\{uw, uv\}$ or $\{uw, vw\}$; neither is a subset of $s[0] = \{uv, vw\}$ (since $uw \notin s[0]$) nor of $s[1] = \{uw\}$ (since $|A \cup \{e\}| = 2 > |s[1]|$). Thus $(E(G[s]), \mathcal{I}_s)$ violates the matroid augmentation property, so $s$ is not a matroid switch. $\square$

### 1.2. Polynomial-Time Algorithm for `GCS` on $\Pi_1$
**Theorem 1:** *$\mathrm{Global-Con Switching}$ restricted to $\Pi_1$ is solvable in $O(n + m)$ time (in $\mathsf{P}$).*
*Proof.* Let $\widehat{G}$ be any switch graph whose switches belong to $\Pi_1$. For each switch $s \in \mathcal{S}(\widehat{G})$ on vertices $V(G[s]) = \{u_s, v_s, w_s\}$, its size-$2$ position $s[p_s]$ (the unique position with $|s[p_s]| = 2$) is a path $P_3$ spanning all three vertices $\{u_s, v_s, w_s\}$ into a single connected component, whereas its size-$1$ position $s[1 - p_s]$ connects only two of those vertices. Consequently, for any configuration $c \in \mathcal{C}(\widehat{G})$ and any $s \in \mathcal{S}(\widehat{G})$, every pair of vertices connected in $s[c(s)]$ is already connected in $s[p_s]$. By monotonicity of graph connectivity under edge-set (and component-partition) coarsening, $\widehat{G}$ admits a configuration $c$ making $\widehat{G} \circ c$ connected **if and only if** the specific configuration $c^*$ defined by $c^*(s) = p_s$ for all $s \in \mathcal{S}(\widehat{G})$ makes $\widehat{G} \circ c^*$ connected. Constructing $\widehat{G} \circ c^*$ and running BFS/DFS takes $O(n + m)$ time. $\square$

---

## 2. Counterexample 2: Incomparable Non-Matroid Switches Reducing Non-Trivially to Matroid Intersection ($\Pi_2$)

To show that the dichotomy fails even when **neither** position of a switch dominates the other in connectivity (so `GCS` genuinely requires Matroid Intersection rather than fixed greedy selection), define the switch $s_2$ on four vertices $\{a, b, c, x\}$ by:
$$s_2[0] = \{ax, xb, ab\}, \qquad s_2[1] = \{ax, ac\},$$
and let $\Pi_2$ be the family of all switches isomorphic to $s_2$ (a $\{3,2\}$-bounded family shaped like the paw graph $L_{3,1} \cong K_4 - \{bc, cx\}$).

1. **Incomparability:** The connected-component partitions of $V(G[s_2]) = \{a,b,c,x\}$ induced by the two positions are $\{\{a,x,b\}, \{c\}\}$ (for $s_2[0]$) and $\{\{a,x,c\}, \{b\}\}$ (for $s_2[1]$); neither refines the other.
2. **Non-matroid:** Let $A = s_2[1] = \{ax, ac\} \in \mathcal{I}_{s_2}$ ($|A| = 2$) and $B = s_2[0] = \{ax, xb, ab\} \in \mathcal{I}_{s_2}$ ($|B| = 3$). For each $e \in B \setminus A = \{xb, ab\}$, $A \cup \{e\}$ contains $ac \notin s_2[0]$ and has size $3 > |s_2[1]|$, so $A \cup \{e\} \notin \mathcal{I}_{s_2}$. Thus no switch in $\Pi_2$ is a matroid switch.
3. **Reduction to $\mathsf{P}$ (including `WGCS`):** Given any switch graph $\widehat{G}$ with switches in $\Pi_2$ (with arbitrary vertex sharing across switches), replace each switch $s \in \mathcal{S}(\widehat{G})$ (with vertices $\{a_s, b_s, c_s, x_s\}$ matching $s_2$) by two matroid switches:
   - a static-edge switch $s^{\mathrm{st}} = (\{a_s x_s\})$ ($\{1\}$-bounded), and
   - a $\{1,1\}$-bounded switch $s' = (\{a_s b_s\}, \{a_s c_s\})$ (a rank-$1$ uniform matroid switch).
   For every configuration $c$ of $\widehat{G}$, the edge set $s[0] = \{a_s x_s, x_s b_s, a_s b_s\}$ induces the exact same connected components on $V(G[s])$ (namely $\{\{a_s, x_s, b_s\}, \{c_s\}\}$) as $\{a_s x_s\} \cup \{a_s b_s\}$, while $s[1] = \{a_s x_s, a_s c_s\} = \{a_s x_s\} \cup \{a_s c_s\}$. Because global connectivity depends only on the component partitions of each switch, $\widehat{G}$ has a connecting configuration iff the transformed instance $\widehat{G}'$ (whose switches are all matroid switches) does. By Theorem `thm:gcs-matroid-switches` (`gcon.tex`, line 25), `GCS` on $\Pi_2$ is solvable in $O(n^2 m \log n)$ polynomial time. *(Moreover, assigning weight $w(s, i)$ to $s'[i]$ and $0$ to $s^{\mathrm{st}}$ shows `WGCS` on $\Pi_2$ is also in $\mathsf{P}$ via Theorem `thm:wgcs-matroid`.)*

---

## 3. Counterexample 3: Minimal Acyclic Spanning-Tree Switches ($\Pi_3$)

Even if one restricts to switches whose every position is an acyclic spanning tree (containing no redundant cycle edges), let $s_3$ on $\{a, b, c, d\}$ be:
$$s_3[0] = \{ab, bc, cd\}, \qquad s_3[1] = \{ac, bd, da\},$$
and let $\Pi_3$ be all isomorphic copies of $s_3$ ($\{3,3\}$-bounded, $K_4$-shaped).
- **Non-matroid:** $A = \{ab, bc\} \subset s_3[0]$ ($|A|=2$) cannot be augmented by any edge of $B = s_3[1]$ ($|B|=3$), because $s_3[0] \cap s_3[1] = \emptyset$ and $|s_3[0]| = 3$.
- **In $\mathsf{P}$ ($O(n+m)$ time):** Both $s_3[0]$ and $s_3[1]$ are spanning trees of $\{a,b,c,d\}$, so every configuration induces the same connected components as always selecting position $0$.

---

## Verification

Exact verification in `verify.py` (`OVERALL: PASS`) confirms:
- Exact violation of the matroid augmentation axiom for $\Pi_1$ ($s_1$), $\Pi_2$ ($s_2$), and $\Pi_3$ ($s_3$), and uniqueness of the $\{2,1\}$-bounded $K_3$-shaped class $\Pi_1$ up to isomorphism;
- Exhaustive check across switch graphs showing exact equivalence between $\mathrm{GCS}(\Pi_1)$ and selecting all size-$2$ positions, and exact equivalence between $\mathrm{GCS}(\Pi_2)$ and the $\{1,1\}$-matroid-switch reduction across all switch-position choices and shared-vertex topologies on $5$–$7$ vertices.

# Counterexample to Conjecture 1.8 of Ferrero–Hall–Hogben–Hunnell–Small (`arXiv:2511.16335v1`)

## Explicit Smallest Witness

Let $G = C_6[2K_1] \cong \mathrm{Circ}(12, \{1, 5\})$ be the 12-vertex, 24-edge 4-regular bipartite graph on vertex set $\mathbb{Z}/12\mathbb{Z}$ with edges $\{i, i \pm 1 \bmod 12\}$ and $\{i, i \pm 5 \bmod 12\}$. Equivalently, partition $V(G)$ into six independent pairs $A_i = \{i, i+6\}$ for $i \in \mathbb{Z}/6\mathbb{Z}$, with all edges between $A_i$ and $A_{i+1 \bmod 6}$ (the lexicographic product $C_6[2K_1]$).

1. **$G$ is connected:** The edges $\{i, i+1 \bmod 12\}$ form a Hamiltonian cycle.
2. **$\overline{\mathrm{PT}}(G) = 1$:** Exhaustive check over all $2^{12} = 4096$ subsets of $V(G)$ shows that there are exactly $144$ minimal standard zero forcing sets, all of cardinality $\mathbb{Z}(G) = \overline{Z}(G) = 8$, and every standard zero forcing set $B \subsetneq V(G)$ has $\mathrm{pt}(G, B) = 1$. Hence $\underline{\mathrm{PT}}(G) = \overline{\mathrm{PT}}(G) = 1$.
3. **$G$ is not a standard fast join:** By Definition 1.5 of `arXiv:2511.16335v1`, a standard fast join of order $n \ge 2$ is either $K_n$ or a join $\bigvee_{i=1}^t G_i$ with $t \ge 2$ nonempty parts, which therefore has a disconnected complement $\overline{G}$. Here $G \not\cong K_{12}$ (it has 24 edges vs. 66), and $\overline{G}$ is 7-regular on 12 vertices, hence connected (indeed $\delta(\overline{G}) = 7 \ge 12/2$). Thus $G$ is not a join of two nonempty graphs and is not a standard fast join.

## Infinite Family and Proof

More generally, for any integers $r_0, r_1, r_2, r_3, r_4, r_5 \ge 2$, let $G = C_6[r_0 K_1, r_1 K_1, \dots, r_5 K_1]$ be the graph obtained from $C_6$ (with vertices $0,1,2,3,4,5$ in cyclic order) by replacing each vertex $i \in \mathbb{Z}/6\mathbb{Z}$ with an independent set $A_i$ of size $r_i$ and joining every vertex in $A_i$ to every vertex in $A_{i-1} \cup A_{i+1}$. Let $n = \sum_{i=0}^5 r_i \ge 12$.

1. **Connectedness:** $G$ is connected because $C_6$ is connected and every $A_i$ is nonempty.
2. **Not a standard fast join:** Since $r_i \ge 2$, $G$ has non-adjacent vertices inside $A_0$, so $G \not\cong K_n$. In the complement $\overline{G}$, each $A_i$ induces a clique $K_{r_i}$, and every vertex of $A_i$ is adjacent to every vertex of $A_j$ for $j \not\equiv i \pm 1 \pmod 6$. In particular, $A_0-A_2-A_4-A_0$, $A_1-A_3-A_5-A_1$, and $A_0-A_3$ are all complete bipartite joins in $\overline{G}$, so $\overline{G}$ is connected (of diameter 2). Any join of two or more nonempty graphs has a disconnected complement, so $G$ is not a standard fast join.
3. **$\overline{\mathrm{PT}}(G) = 1$:** Let $B \subsetneq V(G)$ be any proper subset, and $W = V(G) \setminus B \ne \emptyset$.
   - *Case 1:* $|W \cap A_i| \ge 2$ for some $i$. Any two distinct vertices $w_1, w_2 \in W \cap A_i$ satisfy $N_G(w_1) = N_G(w_2) = A_{i-1} \cup A_{i+1}$, so every neighbor of $w_1$ is also adjacent to $w_2$. Neither $w_1$ nor $w_2$ can ever be the unique white neighbor of any blue vertex, so $B$ is not a standard zero forcing set.
   - *Case 2:* $|W \cap A_i| \le 1$ for all $i \in \mathbb{Z}/6\mathbb{Z}$. Let $S = \{i \in \mathbb{Z}/6\mathbb{Z} : |W \cap A_i| = 1\} \ne \emptyset$, and denote the unique white vertex in $A_j$ for $j \in S$ by $w_j$. Since $r_i \ge 2$ for all $i$, every part $A_i$ contains at least $r_i - 1 \ge 1$ blue vertex in $B$.
     - A blue vertex $u \in A_i \cap B$ has white neighbors $(A_{i-1} \cup A_{i+1}) \cap W$, so $u$ forces $w_j$ in round 1 if and only if $i \in \{j-1, j+1\}$ and the other neighbor of $i$ in $C_6$ is not in $S$.
     - Because both $A_{j-1} \cap B$ and $A_{j+1} \cap B$ are nonempty, $w_j$ is forced in round 1 if and only if $j - 2 \notin S$ or $j + 2 \notin S$ (indices modulo 6).
     - Partition $\mathbb{Z}/6\mathbb{Z}$ into $E = \{0, 2, 4\}$ and $O = \{1, 3, 5\}$. Note that $j \mapsto j \pm 2 \pmod 6$ keeps $E$ inside $E$ and $O$ inside $O$.
     - If $E \not\subseteq S$, then every $j \in S \cap E$ has $j - 2 \notin S$ or $j + 2 \notin S$, so every $w_j$ with $j \in S \cap E$ is forced in round 1. If $E \subseteq S$, then for every $j \in E$, both $j-2, j+2 \in E \subseteq S$, so no $w_j$ with $j \in E$ is forced in round 1.
     - Symmetrically, if $O \not\subseteq S$, all of $S \cap O$ is forced in round 1; if $O \subseteq S$, none of $O$ is forced in round 1.
     - Therefore, if $E \not\subseteq S$ and $O \not\subseteq S$, then all of $W$ is forced in round 1, giving $\mathrm{pt}(G, B) = 1$. Otherwise, after round 1 the remaining white set corresponds to $S' \in \{E, O, E \cup O\}$, on which round 2 forces no additional vertices and propagation stalls, so $B$ is not a standard zero forcing set.

Thus every standard zero forcing set $B \subsetneq V(G)$ satisfies $\mathrm{pt}(G, B) = 1$, and in particular $\overline{\mathrm{PT}}(G) = 1$ (with $\mathbb{Z}(G) = \overline{Z}(G) = n - 4$).

## Verification

Run:
```bash
.venv/bin/python targets/ferrero-2511.16335-conj1.8/verify.py
```

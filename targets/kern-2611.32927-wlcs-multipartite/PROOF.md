# Resolution: `Weighted Local-Con Switching` on $\{1^\star\}$-Bounded Complete Multipartite Switches (`kern-2611.32927-wlcs-multipartite`)

## Main Result

We answer the open question of Kern, Firbas, and Sorge (`arXiv:2611.32927v1`, `sections/conclusion.tex`, line 5) in the **negative** (assuming $\mathsf{P} \neq \mathsf{NP}$):

**Theorem 1:** *$\mathrm{Weighted Local-Con Switching}$ (`WLCS`) is $\mathsf{NP}$-complete even when restricted to $\{1^\star\}$-bounded $K_{2,2}$-shaped (complete bipartite, hence complete multipartite) switches, binary weights $w(s, i) \in \{0, 1\}$, and weight bound $\lambda = 0$.*

---

## Proof of Theorem 1

Membership in $\mathsf{NP}$ holds immediately (`preliminaries.tex`, line 21): a configuration $c$ is polynomial-size and both $a$--$b$ reachability in $\widehat{G} \circ c$ and $\sum_{s} w(s, c(s)) \le \lambda$ are checkable in linear time.

For $\mathsf{NP}$-hardness, we reduce in polynomial time from unweighted $\mathrm{Local-Con Switching}$ (`LCS`) restricted to $\{1^\star\}$-bounded $(K_2 + K_2)$-shaped switches, which is $\mathsf{NP}$-complete by Theorem `thm:dichotomy-lcs` (`sections/stcon.tex`, lines 149 and 184–186; since $K_2 + K_2$ is not complete multipartite).

Let $(\widehat{G}, a, b)$ be an instance of `LCS` where every switch $s \in \mathcal{S}(\widehat{G})$ is $\{1^\star\}$-bounded and $(K_2 + K_2)$-shaped. Since $a$--$b$ connectivity is monotone under adding edges, any configuration selecting an empty position $\emptyset$ remains valid if that switch instead selects a non-empty position, so we may delete all empty positions and deduplicate repeated positions in each switch $s$ in polynomial time $O(|\widehat{G}|)$. Because $G[s] \cong K_2 + K_2$ has two disjoint edges $u_s v_s$ and $x_s y_s$ ($|\{u_s, v_s, x_s, y_s\}| = 4$), reindexing positions gives $s[0] = \{u_s v_s\}$ and $s[1] = \{x_s y_s\}$ for every $s \in \mathcal{S}(\widehat{G})$.

Construct a `WLCS` instance $(\widehat{G}', a, b, w, \lambda)$ on the same vertex set $V(\widehat{G}') := V(\widehat{G})$ with $\lambda := 0$ by replacing each switch $s \in \mathcal{S}(\widehat{G})$ (with $V(G[s]) = \{u_s, v_s, x_s, y_s\}$ and $E(G[s]) = \{u_s v_s, x_s y_s\}$) with a $4$-position $\{1^\star\}$-bounded switch $\tilde{s}$:
$$\tilde{s}[0] := \{u_s v_s\}, \quad \tilde{s}[1] := \{x_s y_s\}, \quad \tilde{s}[2] := \{u_s y_s\}, \quad \tilde{s}[3] := \{x_s v_s\},$$
with weight function:
$$w(\tilde{s}, 0) := 0, \qquad w(\tilde{s}, 1) := 0, \qquad w(\tilde{s}, 2) := 1, \qquad w(\tilde{s}, 3) := 1.$$

1. **Switch properties:** For every $s \in \mathcal{S}(\widehat{G})$, every position of $\tilde{s}$ has $|\tilde{s}[i]| = 1$, so $\tilde{s}$ is $\{1,1,1,1\}$-bounded (in particular $\{1^\star\}$-bounded). Moreover,
   $$E(G[\tilde{s}]) = \{u_s v_s, x_s y_s, u_s y_s, x_s v_s\}$$
   is the complete bipartite graph $K_{2,2}$ with bipartition $\{u_s, x_s\} \sqcup \{v_s, y_s\}$, which is complete multipartite.
2. **Complexity:** Preprocessing and replacing each switch runs in $O(|\widehat{G}|)$ polynomial time.
3. **Correctness:** Since $w(\tilde{s}, i) \ge 0$ for all $\tilde{s}, i$ and $\lambda = 0$, a configuration $c' \in \mathcal{C}(\widehat{G}')$ satisfies $w(c') \le 0$ if and only if $c'(\tilde{s}) \in \{0, 1\}$ for every switch $\tilde{s}$. Such configurations $c'$ are in exact bijection with configurations $c \in \mathcal{C}(\widehat{G})$ via $c(s) = c'(\tilde{s}) \in \{0, 1\}$, and satisfy $\widehat{G}' \circ c' = \widehat{G} \circ c$. Hence $a$ and $b$ are connected in $\widehat{G} \circ c$ for some $c \in \mathcal{C}(\widehat{G})$ if and only if they are connected in $\widehat{G}' \circ c'$ for some $c' \in \mathcal{C}(\widehat{G}')$ with $w(c') \le 0$. $\square$

*(Remark: Even if one enforces **zero empty positions** and strictly $\{0,1\}$-weights, Theorem `thm:dichotomy-lcs`'s reduction from `TCP` on $\{K_2+K_2, K_3\}$ produces only switches with nonempty positions; our weight-$0$ positions $\tilde{s}[0], \tilde{s}[1]$ preserve this exactly. Note also the contrast with threshold $\lambda = 0$ on $\{1^\star\}$-bounded $\mathcal{K}_{1,\star}$-shaped or $K_3$-shaped switches with non-negative weights: deleting positive-weight edges leaves a subgraph that is still complete multipartite ($\mathcal{K}_{1,\star}$, $K_3$, or $K_2$), where `LCS` remains in $O(n+m)$ time.)*

---

## Verification

Exact brute-force verification in `verify.py` (`OVERALL: PASS`) checks:
- Exact graph isomorphism of $G[\tilde{s}]$ to $K_{2,2}$ and $\{1^\star\}$-boundedness;
- Exact brute-force equivalence between `LCS` on $\{1^\star\}$-bounded $(K_2 + K_2)$-shaped switch graphs and `WLCS` ($\lambda = 0$, $\{0,1\}$-weights) on the reduced $K_{2,2}$-shaped switch graphs across both positive (`YES`) and negative (`NO`) instances (showing how weight-$1$ cross-edges would falsely connect $a$ to $b$ if $\lambda$ were relaxed to $1$, while $\lambda = 0$ preserves exact equivalence).

# Counterexample to `arXiv:2303.08771v1` Conjecture 3

## Result

Conjecture 3 of Bartnicki, Czerwiński, Grytczuk, and Miechowicz (*"Strong arboricity of graphs"*, `arXiv:2303.08771v1`, Section 3, lines 250–252; *Graphs and Combinatorics* 41 (2025), Art. 80, `DOI: 10.1007/s00373-025-02934-5`, pp. 7–8) is **FALSE**.

Specifically, there exists a $9$-vertex, $24$-edge simple graph $G$ with $\mathrm{col}(G) = 5$ and $\zeta(G) = 6 > \mathrm{col}(G)$.

## Explicit Counterexample

Let $G = (V, E)$ be the simple graph on $9$ vertices partitioned into $V = A \sqcup B \sqcup C$ where
$$A = \{0, 1, 2, 3\}, \qquad B = \{4, 5, 6\}, \qquad C = \{7, 8\},$$
with edge set $E = E_A \sqcup E_{AB} \sqcup E_{BC}$ ($|E| = 6 + 12 + 6 = 24$) defined by:
- $E_A = \binom{A}{2}$ ($G[A] \cong K_4$, $6$ edges),
- $E_{AB} = \{\{a, b\} : a \in A,\; b \in B\}$ ($G[A, B] \cong K_{4,3}$, $12$ edges),
- $E_{BC} = \{\{b, c\} : b \in B,\; c \in C\}$ ($G[B, C] \cong K_{3,2}$, $6$ edges),
and no edges within $B$, within $C$, or between $A$ and $C$.

## Proof that $\mathrm{col}(G) = 5$

1. **Upper bound ($\mathrm{col}(G) \le 5$):** Consider the vertex ordering $(0, 1, 2, 3, 4, 5, 6, 7, 8)$. The back-degrees (number of earlier neighbors) are:
   - for $0, 1, 2, 3 \in A$: $0, 1, 2, 3 \le 4$;
   - for $4, 5, 6 \in B$: each is adjacent only to $\{0, 1, 2, 3\}$, so back-degree is $4$;
   - for $7, 8 \in C$: each is adjacent only to $\{4, 5, 6\}$, so back-degree is $3 \le 4$.
   Thus the maximum back-degree is $4$, giving $\mathrm{col}(G) \le 4 + 1 = 5$.
2. **Lower bound ($\mathrm{col}(G) \ge 5$):** The induced subgraph $G[A \cup \{4\}]$ is $K_5$, whose minimum degree is $4$, so every vertex ordering has back-degree at least $4$ at the last vertex of $A \cup \{4\}$. Hence $\mathrm{col}(G) = 5$.

## Proof that $\zeta(G) > 5$

Suppose for contradiction that $G$ admits a strongly woody $5$-coloring $E = F_1 \sqcup F_2 \sqcup F_3 \sqcup F_4 \sqcup F_5$.

**Claim 1 (Induced-tree characterization).** *Each color class $F_i$ is a forest whose connected components are induced trees in $G$.*

*Proof.* Since $F_i$ is woody, it is a forest. If some component $T$ of $F_i$ were not induced in $G$, there would be an edge $uv \in E \setminus E(T)$ with $u, v \in V(T)$; letting $P$ be the unique $u$-$v$ path in $T$, the union $P + uv$ is a cycle in $G$, so $P = (P + uv) - uv$ is a monochromatic broken cycle in $F_i$, a contradiction. $\square$

**Claim 2 (Linear bound per color class).** *For every color class $F$, setting $e_A(F) = |F \cap E_A|$ and $e_{AB}(F) = |F \cap E_{AB}|$, we have $3\,e_A(F) + e_{AB}(F) \le 6$.*

*Proof.* Any component $T$ of $F$ containing an edge of $E_A$ satisfies $|V(T) \cap A| \ge 2$. Since $G[A] = K_4$ and $T$ is an induced tree by Claim 1, we must have $|V(T) \cap A| = 2$ (a triangle in $A$ is forbidden) and $V(T) \cap B = \emptyset$ (any $b \in B$ forms a triangle with the two vertices of $V(T) \cap A$). Consequently:
- Every component $T$ of $F$ intersecting $B$ satisfies $|V(T) \cap A| \le 1$, so each $b \in B$ is incident to at most one edge of $F \cap E_{AB}$. Because $|B| = 3$, this gives $e_{AB}(F) \le 3$.
- Also $e_A(F) \le 2$ (as any edge of $F \cap E_A$ forms an isolated $K_2$ inside $A$).
- If $e_A(F) = 2$, the two edges of $F \cap E_A$ cover all $4$ vertices of $A$, leaving no vertices of $A$ available to connect to $B$, so $e_{AB}(F) = 0$ and $3 e_A(F) + e_{AB}(F) = 6$.
- If $e_A(F) = 1$, then $3 e_A(F) + e_{AB}(F) \le 3(1) + 3 = 6$.
- If $e_A(F) = 0$, then $3 e_A(F) + e_{AB}(F) \le 3 < 6$. $\square$

**Claim 3 (Tightness forces $1$ Type-I and $4$ Type-II color classes).** Summing Claim 2 over $i = 1, \dots, 5$:
$$30 = 3|E_A| + |E_{AB}| = \sum_{i=1}^5 \bigl(3\,e_A(F_i) + e_{AB}(F_i)\bigr) \le 5 \cdot 6 = 30.$$
Thus every $F_i$ satisfies $3\,e_A(F_i) + e_{AB}(F_i) = 6$, so each $F_i$ has either $(e_A, e_{AB}) = (2, 0)$ (Type I) or $(e_A, e_{AB}) = (1, 3)$ (Type II). Since $12 = |E_{AB}| = \sum_{i=1}^5 e_{AB}(F_i) = 3 \times (\text{\# Type II})$, there is **one** Type-I color class (without loss of generality $F_5$) and **four** Type-II color classes ($F_1, F_2, F_3, F_4$).

**Claim 4 (Rigid $2$-matching structure on $E_{AB}$).** By $S_4$-symmetry on $A$, we may assume $F_5 \cap E_A = \{\{0,1\}, \{2,3\}\}$. The remaining $4$ edges of $K_4$ form the $4$-cycle $(0, 2, 1, 3, 0)$ and must go one each to $F_1, F_2, F_3, F_4$; without loss of generality,
$$\{0, 2\} \in F_1, \quad \{2, 1\} \in F_2, \quad \{1, 3\} \in F_3, \quad \{3, 0\} \in F_4.$$
In a Type-II class $F_i$, the two vertices of its $E_A$-edge cannot be incident to any edge of $F_i \cap E_{AB}$ (as shown in Claim 2). Therefore, the edges in $E_{AB}$ incident to each vertex $a \in A$ may only receive colors from the two classes whose $E_A$-edge avoids $a$:
- $a = 0$: allowed colors $\{2, 3\}$;
- $a = 1$: allowed colors $\{1, 4\}$;
- $a = 2$: allowed colors $\{3, 4\}$;
- $a = 3$: allowed colors $\{1, 2\}$.

For each $b \in B$, we have $e_{AB}(F_5) = 0$, and by Claim 2 each $F_i$ ($i \in \{1,2,3,4\}$) has at most one (hence, since $e_{AB}(F_i) = 3 = |B|$, **exactly** one) edge incident to $b$. Thus the colors on $\{0b, 1b, 2b, 3b\}$ define a bijection $m_b : \{0, 1, 2, 3\} \to \{1, 2, 3, 4\}$ respecting the allowed pairs above. Those allowed pairs form the single $8$-cycle $0 - c_2 - 3 - c_1 - 1 - c_4 - 2 - c_3 - 0$ (where $c_i$ denotes color $i$), which has only **two** perfect matchings:
$$M_X : (0\mapsto 2,\; 3\mapsto 1,\; 1\mapsto 4,\; 2\mapsto 3), \qquad M_Y : (0\mapsto 3,\; 3\mapsto 2,\; 1\mapsto 1,\; 2\mapsto 4).$$

**Claim 5 (Contradiction on $E_{BC}$).** Since $|B| = 3$, by the pigeonhole principle at least two vertices of $B$ — say $b_1, b_2 \in B$ — use the same matching, say $M_X$ (the $M_Y$ case is symmetric). Under $M_X$, for every $i \in \{1, 2, 3, 4\}$, both $b_1$ and $b_2$ are joined in color $i$ to the **same** vertex $a_X(i) \in A$ (namely $a_X(1)=3, a_X(2)=0, a_X(3)=2, a_X(4)=1$).

Suppose some $b_r$ ($r \in \{1, 2\}$) had an edge $\{b_r, c\} \in F_i$ for some $c \in C$ and $i \in \{1, 2, 3, 4\}$. Then $(b_1, a_X(i), b_2, c, b_1)$ is a $4$-cycle in $G$, and deleting $\{b_{3-r}, c\}$ produces the $3$-edge path $(b_{3-r} - a_X(i) - b_r - c)$ entirely in $F_i$, a monochromatic broken cycle, contradiction.

Hence **no** edge between $\{b_1, b_2\}$ and $C = \{7, 8\}$ can receive colors $1, 2, 3,$ or $4$. All four edges $\{b_1, 7\}, \{b_1, 8\}, \{b_2, 7\}, \{b_2, 8\}$ must therefore belong to $F_5$. But those four edges form the $4$-cycle $(b_1, 7, b_2, 8, b_1)$ in $F_5$, contradicting that $F_5$ is acyclic. $\blacksquare$

## Exact Value $\zeta(G) = 6$

The following explicit $6$-coloring of $E(G)$ is strongly woody (every color class is a forest of induced stars/edges):
- **Color 1:** $\{0,1\}, \{2,4\}, \{3,6\}, \{5,7\}, \{5,8\}$
- **Color 2:** $\{0,2\}, \{1,6\}, \{3,5\}, \{4,7\}, \{4,8\}$
- **Color 3:** $\{0,3\}, \{1,2\}$
- **Color 4:** $\{0,6\}, \{1,4\}, \{1,5\}, \{2,3\}$
- **Color 5:** $\{2,5\}, \{2,6\}, \{3,4\}$
- **Color 6:** $\{0,4\}, \{0,5\}, \{1,3\}, \{6,7\}, \{6,8\}$

Thus $\zeta(G) = 6 > 5 = \mathrm{col}(G)$, disproving Conjecture 3.

## Verification

Run `.venv/bin/python targets/bartnicki-2303.08771-conj3/verify.py`, which checks in pure exact Python (zero floats, zero external dependencies):
1. All structural properties of $G$ ($9$ vertices, $24$ edges).
2. $\mathrm{col}(G) = 5$ exhaustively over all $2^9 - 1 = 511$ nonempty induced subgraphs.
3. Directly via single-edge contractions $G/e$ (all $24$ contractions) and induced-tree checks that the explicit $6$-coloring is strongly woody.
4. Exhaustively via the induced-tree forest enumeration and exact backtracking over $5$-partitions of $E(G)$ that no strongly woody $5$-coloring of $G$ exists.

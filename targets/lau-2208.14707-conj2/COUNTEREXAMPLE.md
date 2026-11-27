# Counterexample to `arXiv:2208.14707v1` Conjecture 2.2

## Result

Conjecture 2.2 of Lau, Shiu, Premalatha, Zhang, and Nalliah (`arXiv:2208.14707v1`, Section 2, p. 8, line 819; also *Discrete Math. Lett.* 11 (2023), pp. 76–83, `DOI:10.47443/dml.2022.149`, p. 82) is **FALSE**.

## Explicit Counterexample

Take the two disjoint connected simple non-null graphs:
- $G = K_4$ (complete graph on $4$ vertices, $6$ edges),
- $H = K_2$ (complete graph on $2$ vertices, $1$ edge).

### Verification of All Hypotheses and Quantities

1. **Cycle length and $k$:** The shortest odd cycle in $G = K_4$ is a triangle $C_3$ of length $3 = 2k + 1$, so $k = 1 \ge 1$.
2. **Chromatic numbers:** $\chi(G) = \chi(K_4) = 4$ and $\chi(H) = \chi(K_2) = 2$, so $\chi(G)\chi(H) = 4 \cdot 2 = 8$.
3. **Structure of $G[H]$:** By definition, $V(K_4[K_2]) = V(K_4) \times V(K_2)$ has $8$ vertices, and any two distinct vertices $(u, u'), (v, v')$ are adjacent: if $u \ne v$ then $uv \in E(K_4)$, while if $u = v$ then $u' \ne v'$ so $u'v' \in E(K_2)$. Hence $K_4[K_2] \cong K_8$ (with $\binom{8}{2} = 28$ edges).
4. **Exact computation of $\chi_{la}(G[H])$:**
   - **Lower bound:** Every local antimagic labeling induces a proper vertex coloring, so $\chi_{la}(K_4[K_2]) = \chi_{la}(K_8) \ge \chi(K_8) = 8$.
   - **Upper bound (explicit labeling):** Label the $8$ vertices of $K_8$ as $0, 1, \dots, 7$ and assign edge labels $f: E(K_8) \to \{1, 2, \dots, 28\}$ in lexicographical order of $(i, j)$ ($0 \le i < j \le 7$):
     $$f(\{i, j\}) = 1 + \sum_{a=0}^{i-1} (7 - a) + (j - i - 1).$$
     Explicitly, the edge-label matrix $(f(\{i, j\}))_{0 \le i,j \le 7}$ (with $*$ on the diagonal) is:
     $$
     \begin{pmatrix}
     * & 1 & 2 & 3 & 4 & 5 & 6 & 7 \\
     1 & * & 8 & 9 & 10 & 11 & 12 & 13 \\
     2 & 8 & * & 14 & 15 & 16 & 17 & 18 \\
     3 & 9 & 14 & * & 19 & 20 & 21 & 22 \\
     4 & 10 & 15 & 19 & * & 23 & 24 & 25 \\
     5 & 11 & 16 & 20 & 23 & * & 26 & 27 \\
     6 & 12 & 17 & 21 & 24 & 26 & * & 28 \\
     7 & 13 & 18 & 22 & 25 & 27 & 28 & *
     \end{pmatrix}.
     $$
     Every integer in $\{1, \dots, 28\}$ appears on exactly one undirected edge, and the $8$ vertex sums $f^+(0), \dots, f^+(7)$ are:
     $$f^+(0) = 28,\quad f^+(1) = 64,\quad f^+(2) = 90,\quad f^+(3) = 108,\quad f^+(4) = 120,\quad f^+(5) = 128,\quad f^+(6) = 134,\quad f^+(7) = 140.$$
     All $8$ vertex sums are pairwise distinct, so $f$ is a local antimagic $8$-coloring of $K_8$. Therefore $\chi_{la}(G[H]) = 8 = \chi(G)\chi(H)$.
5. **Contradiction to the RHS condition:**
   $$2\chi(H) + \left\lceil \frac{\chi(H)}{k} \right\rceil = 2(2) + \left\lceil \frac{2}{1} \right\rceil = 4 + 2 = 6 \ne 8 = \chi(G)\chi(H).$$

Thus the "only if" direction of Conjecture 2.2 fails at $(G, H) = (K_4, K_2)$.

*(Remark: More generally, for every $m \ge 4$ and $n \ge 2$, taking $G = K_m$ and $H = K_n$ gives $k = 1$, $G[H] \cong K_{mn}$ with $\chi_{la}(K_{mn}) = mn = \chi(K_m)\chi(K_n)$, whereas $2\chi(H) + \lceil \chi(H)/k \rceil = 3n \ne mn$.)*

## Verification

Run `.venv/bin/python targets/lau-2208.14707-conj2/verify.py`, which checks all graph definitions, chromatic numbers, shortest odd cycle length, isomorphism $K_4[K_2] \cong K_8$, bijectivity of $f$ onto $\{1, \dots, 28\}$, pairwise distinctness of all $8$ vertex sums, and the inequality $6 \ne 8$ in exact integer arithmetic (outputting `PASS`).

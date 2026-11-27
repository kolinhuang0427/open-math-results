# Counterexample to Li–Lu–Luo Conjecture 7 (`arXiv:2505.12035v1`, `conj:ore`)

We refute Conjecture 7 (`conj:ore`) of Li, Lu, and Luo (arXiv:2505.12035v1) using two explicit connected $3$-uniform hypergraphs (hence $[3]$-graphs) on $n=6$ and $n=7$ vertices.

## Witness 1 ($n = 6$, even achieving $d_{\partial \mathcal{H}}(u) + d_{\partial \mathcal{H}}(v) = n + 2 = 8$)

Let $V(\mathcal{H}_1) = \{0, 1, 2, 3, 4, 5\}$ and let $E(\mathcal{H}_1)$ consist of the $5$ distinct $3$-element edges:
$$E(\mathcal{H}_1) = \{\{0, 1, 2\},\; \{0, 1, 3\},\; \{0, 2, 4\},\; \{1, 2, 5\},\; \{3, 4, 5\}\}.$$

- **Admissibility ($[3]$-graph, $n \ge 6$):** $n = 6 \ge 6$, and every hyperedge has cardinality $3 \le 3$.
- **Shadow $\partial\mathcal{H}_1$ and Ore condition:**
  - $N(0) = \{1, 2, 3, 4\} \implies d_{\partial\mathcal{H}_1}(0) = 4$ (non-adjacent only to $5$),
  - $N(1) = \{0, 2, 3, 5\} \implies d_{\partial\mathcal{H}_1}(1) = 4$ (non-adjacent only to $4$),
  - $N(2) = \{0, 1, 4, 5\} \implies d_{\partial\mathcal{H}_1}(2) = 4$ (non-adjacent only to $3$),
  - $N(3) = \{0, 1, 4, 5\} \implies d_{\partial\mathcal{H}_1}(3) = 4$ (non-adjacent only to $2$),
  - $N(4) = \{0, 2, 3, 5\} \implies d_{\partial\mathcal{H}_1}(4) = 4$ (non-adjacent only to $1$),
  - $N(5) = \{1, 2, 3, 4\} \implies d_{\partial\mathcal{H}_1}(5) = 4$ (non-adjacent only to $0$).
  Thus $\partial\mathcal{H}_1 \cong K_{2,2,2}$ is $4$-regular, and every pair of non-adjacent vertices $\{u, v\} \in \{\{0,5\}, \{1,4\}, \{2,3\}\}$ satisfies
  $$d_{\partial\mathcal{H}_1}(u) + d_{\partial\mathcal{H}_1}(v) = 4 + 4 = 8 = n + 2 > n + 1 = 7.$$
- **No Hamiltonian Berge cycle:** A Hamiltonian Berge cycle on $n=6$ vertices requires $6$ pairwise distinct hyperedges $e_1, \dots, e_6 \in E(\mathcal{H}_1)$. Since $|E(\mathcal{H}_1)| = 5 < 6$, $\mathcal{H}_1$ contains no Hamiltonian Berge cycle.

*(Note: $\mathcal{H}_1$ also shows $d_0 = 2$ fails at $n = 6$.)*

## Witness 2 ($n = 7$, linear $3$-uniform: Fano plane minus one line)

Let $V(\mathcal{H}_2) = \{0, 1, 2, 3, 4, 5, 6\}$ and let $E(\mathcal{H}_2)$ consist of $6$ of the $7$ lines of the Fano plane $\mathrm{STS}(7)$ (deleting $\{0, 1, 2\}$):
$$E(\mathcal{H}_2) = \{\{0, 3, 4\},\; \{0, 5, 6\},\; \{1, 3, 5\},\; \{1, 4, 6\},\; \{2, 3, 6\},\; \{2, 4, 5\}\}.$$

- **Admissibility:** $n = 7 \ge 6$, $\mathcal{H}_2$ is a linear, connected $3$-uniform hypergraph ($|e \cap e'| \le 1$ for all distinct $e, e'$).
- **Shadow $\partial\mathcal{H}_2$ and Ore condition:** Every vertex in $\{3, 4, 5, 6\}$ has shadow degree $6$ (adjacent to all other vertices), and vertices $0, 1, 2$ each have shadow degree $4$ (non-adjacent only to one another). Hence the non-adjacent pairs are $\{0,1\}, \{0,2\}, \{1,2\}$, and each satisfies
  $$d_{\partial\mathcal{H}_2}(u) + d_{\partial\mathcal{H}_2}(v) = 4 + 4 = 8 = n + 1.$$
- **No Hamiltonian Berge cycle:** A Hamiltonian Berge cycle on $n=7$ vertices requires $7$ distinct hyperedges, whereas $|E(\mathcal{H}_2)| = 6 < 7$.

## Verification
Run `.venv/bin/python targets/li-2505.12035-conj7/verify.py` — outputs `PASS` and exits with code `0`.

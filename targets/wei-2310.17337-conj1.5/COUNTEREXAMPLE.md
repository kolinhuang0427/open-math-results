# Counterexample to Wei–Zhang–Zhao Conjecture 1.5 (`arXiv:2310.17337v1`)

## Conjecture Refuted

In Xiaohua Wei, Gang Zhang, and Biao Zhao, *"On the $C_4$-isolation number of a graph"* (`arXiv:2310.17337v1`, Section 1, Conjecture 1.5), the authors conjecture:

> If $G \ncong C_k$ is a connected graph of size $m$, then
> $$\iota(G, C_k) \le \frac{m+1}{k+2}.$$

## Explicit Counterexample ($k = 8$)

Let $G$ be the **truncated tetrahedral graph** on $n = 12$ vertices $V(G) = \{0, 1, \dots, 11\}$, formed from four vertex-disjoint triangles
$$T_0 = \{0,1,2\}, \quad T_1 = \{3,4,5\}, \quad T_2 = \{6,7,8\}, \quad T_3 = \{9,10,11\}$$
together with the $6$ matching edges between distinct triangles:
$$\{0,3\}, \; \{1,6\}, \; \{2,9\}, \; \{4,7\}, \; \{5,10\}, \; \{8,11\}.$$

Thus $G$ has:
- $n = 12$ vertices,
- $m = 4 \cdot 3 + 6 = 18$ edges,
- $G$ is simple, finite, connected, $3$-regular, and clearly $G \ncong C_8$.

Take $k = 8$.

## Proof That $\iota(G, C_8) = 2 > \frac{m+1}{k+2} = \frac{19}{10}$

1. **Lower bound $\iota(G, C_8) \ge 2$:**
   Suppose for contradiction that $\{v\}$ is a $C_8$-isolating set of size $1$.
   Because $G$ is $3$-regular, $|N_G[v]| = 4$, leaving $12 - 4 = 8$ vertices in $G - N_G[v]$.
   In fact, $G$ is vertex-transitive, and for $v = 0$ we have $N_G[0] = \{0, 1, 2, 3\}$, leaving $V(G) \setminus N_G[0] = \{4, 5, 6, 7, 8, 9, 10, 11\}$, which contains the $8$-cycle:
   $$(4, 5, 10, 9, 11, 8, 6, 7, 4).$$
   Every edge of this cycle belongs to $E(G)$: $\{4,5\} \subset T_1$, $\{5,10\}$, $\{10,9\}, \{9,11\} \subset T_3$, $\{11,8\}$, $\{8,6\}, \{6,7\} \subset T_2$, and $\{7,4\}$.
   By vertex-transitivity (and verified explicitly for all $v \in \{0,\dots,11\}$ in `verify.py`), $G - N_G[v]$ contains a $C_8$ for every $v \in V(G)$. Therefore no singleton $\{v\}$ is a $C_8$-isolating set, so $\iota(G, C_8) \ge 2$.

2. **Upper bound $\iota(G, C_8) \le 2$:**
   Take $D = \{0, 4\}$. Then $N_G[D] = \{0, 1, 2, 3, 4, 5, 7\}$, so $|V(G - N_G[D])| = 5 < 8$, meaning $G - N_G[D]$ cannot contain $C_8$. Thus $\iota(G, C_8) = 2$.

3. **Violation of Conjecture 1.5:**
   $$\iota(G, C_8) = 2 > \frac{19}{10} = \frac{18 + 1}{8 + 2} = \frac{m + 1}{k + 2}.$$

## Additional Counterexamples Found

In our computational sweep, the generalized Petersen graphs $GP(9, 2)$ ($n = 18, m = 27, k = 14, \iota = 2 > \frac{28}{16} = \frac{7}{4}$) and $GP(11, 2)$ ($n = 22, m = 33, k = 18, \iota = 2 > \frac{34}{20} = \frac{17}{10}$) also refute Conjecture 1.5. The truncated tetrahedral graph above ($k = 8, n = 12, m = 18$) is the smallest and simplest counterexample we found.

## Verification

Run:
```bash
.venv/bin/python targets/wei-2310.17337-conj1.5/verify.py
```
Expected output ends with `PASS`.

# Counterexample to Mora–Souto-Salorio–Tarrío-Tobar (arXiv:2112.08768v1, Section 3 Conjecture 21)

## Verdict

**FALSE.** We refute Conjecture 21 of Mercè Mora, María José Souto-Salorio, and Ana Dorotea Tarrío-Tobar (*Resolving sets tolerant to failures in three-dimensional grids*, `arXiv:2112.08768v1`, Section 3, lines 901–911 of `FaultTolerantMD-3DGrids-arxiv.tex`).

Specifically, the conjecture asserts that whenever $\alpha_m(n_1, n_2, n_3) \le k < \alpha_M(n_1, n_2, n_3)$,
$$\dim_{k+1}(P_{n_1} \Box P_{n_2} \Box P_{n_3}) = \min\big\{ 4k - 2\alpha_m(n_1,n_2,n_3) + 4,\; n_1 n_2 n_3 - (n_1-2)(n_2-2)(n_3-2) \big\}.$$

An explicit counterexample occurs at $(n_1, n_2, n_3, k) = (3, 3, 4, 13)$:
- $\alpha_m(3,3,4) = 2(3+3+4) - 8 = 12 \le 13 < 15 = \min\{3(5),\, 3(5),\, 4(4)\} = \alpha_M(3,3,4)$.
- The conjectured value is
  $$\min\{ 4(13) - 2(12) + 4,\; 3\cdot 3\cdot 4 - 1\cdot 1\cdot 2 \} = \min\{32, 34\} = 32.$$
- However, we exhibit an explicit $30$-vertex $14$-resolving set $S \subset V(P_3 \Box P_3 \Box P_4)$, proving
  $$\dim_{14}(P_3 \Box P_3 \Box P_4) \le 30 < 32.$$

## Explicit Witness Set ($n_1=3, n_2=3, n_3=4, k=13$)

Let $V = \{0,1,2\} \times \{0,1,2\} \times \{0,1,2,3\}$ with graph distance $d((x_1,x_2,x_3),(y_1,y_2,y_3)) = |x_1-y_1| + |x_2-y_2| + |x_3-y_3|$. Define $S \subset V$ to be the union of the $24$ boundary-edge ("frame") vertices
$$F_{\mathrm{edge}} = \{(x_1,x_2,x_3) \in V : |\{i \in \{1,2,3\} : x_i \in \{0, n_i-1\}\}| \ge 2\}$$
and the $6$ face-interior vertices
$$F_{\mathrm{int}} = \{(0,1,1),\; (2,1,1),\; (1,0,1),\; (1,2,1),\; (1,1,0),\; (1,1,3)\}.$$
Equivalently, $S = V \setminus M$ where the $6$ omitted vertices are
$$M = \{(0,1,2),\; (2,1,2),\; (1,0,2),\; (1,2,2),\; (1,1,1),\; (1,1,2)\}.$$
Thus $|S| = 36 - 6 = 30$.

### Proof that $S$ is $14$-resolving (hence $\dim_{14}(P_3 \Box P_3 \Box P_4) \le 30$)

By definition, $S$ is $(k+1)$-resolving ($k=13$, so $k+1=14$) if and only if for every pair of distinct vertices $u, v \in V$, at least $14$ vertices $z \in S$ satisfy $d(z,u) \ne d(z,v)$.

1. If $d(u,v)$ is odd, then since $P_3 \Box P_3 \Box P_4$ is bipartite, every vertex $z \in V$ satisfies $d(z,u) \not\equiv d(z,v) \pmod 2$, so all $30$ vertices of $S$ resolve $(u,v)$.
2. For all pairs $(u,v) \in \binom{V}{2}$ with $d(u,v)$ even (exhaustively checked in `verify.py`), the minimum number of resolving vertices in $S$ is exactly $14 \ge k+1$ (attained, for instance, by $u=(0,0,1), v=(0,1,0)$, where $12$ vertices in $F_{\mathrm{edge}}$ and the $2$ vertices $(1,0,1), (1,1,0) \in F_{\mathrm{int}}$ resolve $(u,v)$).

Therefore $S$ is a $14$-resolving set of cardinality $30$, refuting the conjecture's claim that $\dim_{14}(P_3 \Box P_3 \Box P_4) = 32$.

## Further Verified Counterexamples (same construction)

The exact same construction $S = F_{\mathrm{edge}} \cup \{(0,1,1), (n_1-1,1,1), (1,0,1), (1,n_2-1,1), (1,1,0), (1,1,n_3-1)\}$ of size $2\alpha_m + 6 < 2\alpha_m + 8 = 4(\alpha_m + 1) - 2\alpha_m + 4$ is also verified in `verify.py` for:
- $(3,3,5,15)$: $\alpha_m = 14 < 15 < 18 = \alpha_M$, $|S| = 34 < 36 = \min(36, 42)$.
- $(3,4,4,15)$: $\alpha_m = 14 < 15 < 18 = \alpha_M$, $|S| = 34 < 36 = \min(36, 44)$.
- $(4,4,4,17)$: $\alpha_m = 16 < 17 < 24 = \alpha_M$, $|S| = 38 < 40 = \min(40, 56)$.

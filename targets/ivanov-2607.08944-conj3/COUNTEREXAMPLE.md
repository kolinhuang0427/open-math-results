# Counterexample to Conjecture 6 (`conj:fleanverts`) in Ivanov (2026)

## Statement Refuted
From Illya Ivanov, *"Illuminating Primitive Polytopes"* (`arXiv:2607.08944v1`, Section 1.4, lines 310–312; `theorem`, `conjecture`, `corollary`, and `claim` share the `[theorem]` counter, so `\label{conj:fleanverts}` is Conjecture 6):

> **Conjecture 6 (`\label{conj:fleanverts}`).**
> A primitive polytope in $\mathbb{E}^d, d\ge 4$ has at most $2^d$ vertices, even fewer if it isn't an affine $d$-cube.

Both the weak upper bound ($\le 2^d$) and the strict inequality ($< 2^d$ for non-cubes) are refuted by an explicit primitive $13$-polytope $P \subset \mathbb{E}^{13}$ with $24$ facets (not an affine $13$-cube, which has $26$ facets) and **$8704 > 8192 = 2^{13}$ vertices**.

---

## Explicit $d = 13$ Counterexample

Let coordinates in $\mathbb{R}^{13}$ be $(x_1, x_2, x_3, y_0, y_1, \dots, y_9)$. Define $P = \bigcap_{i=1}^{24} H_i^-$ by the $24$ closed halfspaces:

1. **Simplex base in $(x_1, x_2, x_3)$ ($4$ halfspaces):**
   $$x_1 \le 100, \qquad x_2 \le 100, \qquad x_3 \le 100, \qquad -x_1 - x_2 - x_3 \le 100.$$

2. **Lifted pairs for $j = 0, 1, \dots, 9$ ($20$ halfspaces):**
   $$y_j \le 1, \qquad -y_j + x_1 + x_2 - j x_3 \le 119 + j^2.$$

Since $P$ has $24$ defining halfspaces in $\mathbb{R}^{13}$ while an affine $13$-cube has $26$ facets, $P$ is not an affine $13$-cube.

---

## Proof that $P$ is a Primitive $13$-Polytope

Let $\mathbf{a}_1, \dots, \mathbf{a}_{24} \in \mathbb{Z}^{13}$ be the left-hand-side outer normal vectors and $b_1, \dots, b_{24} \in \mathbb{Z}_{>0}$ be the right-hand sides.

1. **Nonempty interior and boundedness:**
   The origin $\mathbf{0} \in \mathbb{R}^{13}$ satisfies $\mathbf{a}_i \cdot \mathbf{0} = 0 < b_i$ for all $i$, so $\mathbf{0} \in \mathrm{int} P$.
   Moreover, taking weights $\mu = (1, 1, 56, 11, 1, 1, \dots, 1) \in \mathbb{Z}_{>0}^{24}$ gives:
   $$\mathbf{a}_1 + \mathbf{a}_2 + 56\mathbf{a}_3 + 11\mathbf{a}_4 + \sum_{j=0}^9 (\mathbf{e}_{4+j} + (-\mathbf{e}_{4+j} + \mathbf{e}_1 + \mathbf{e}_2 - j\mathbf{e}_3))$$
   $$= (1 - 11 + 10)\mathbf{e}_1 + (1 - 11 + 10)\mathbf{e}_2 + (56 - 11 - 45)\mathbf{e}_3 = \mathbf{0},$$
   so $\{\mathbf{a}_1, \dots, \mathbf{a}_{24}\}$ positively spans $\mathbb{R}^{13}$ (equivalently, $\mathbf{0} \in \mathrm{int}\mathrm{conv}\{\mathbf{a}_i\}$; note $\{\mathbf{a}_i\}$ also linearly spans $\mathbb{R}^{13}$, since $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ and $\mathbf{e}_{4+j}$ for $j=0,\dots,9$ form the standard basis), which implies $P$ is bounded (a $13$-polytope).

2. **Primitivity (omitting any $H_i^-$ makes the intersection unbounded):**
   For every $i \in \{1, \dots, 24\}$, there exists a ray direction $\mathbf{r}_i \in \mathbb{Z}^{13}$ such that $\mathbf{a}_i \cdot \mathbf{r}_i > 0$ and $\mathbf{a}_m \cdot \mathbf{r}_i \le 0$ for all $m \neq i$:
   - $i = 1$ ($x_1 \le 100$): $\mathbf{r}_1 = (1, -1, 0, \mathbf{0})$. Then $\mathbf{a}_1 \cdot \mathbf{r}_1 = 1 > 0$, $\mathbf{a}_2 \cdot \mathbf{r}_1 = -1 \le 0$, and $\mathbf{a}_m \cdot \mathbf{r}_1 = 0$ for $m \ge 3$.
   - $i = 2$ ($x_2 \le 100$): $\mathbf{r}_2 = (-1, 1, 0, \mathbf{0})$ works symmetrically.
   - $i = 3$ ($x_3 \le 100$): $\mathbf{r}_3 = (-1, -1, 2, \mathbf{0})$. Then $\mathbf{a}_3 \cdot \mathbf{r}_3 = 2 > 0$, $\mathbf{a}_1 \cdot \mathbf{r}_3 = \mathbf{a}_2 \cdot \mathbf{r}_3 = -1 \le 0$, $\mathbf{a}_4 \cdot \mathbf{r}_3 = 0$, and for $j \ge 0$, $(x_1+x_2-jx_3)(\mathbf{r}_3) = -2 - 2j \le -2 < 0$.
   - $i = 4$ ($-x_1-x_2-x_3 \le 100$): $\mathbf{r}_4 = (-10, 0, -1, \mathbf{0})$. Then $\mathbf{a}_4 \cdot \mathbf{r}_4 = 11 > 0$, $\mathbf{a}_1 \cdot \mathbf{r}_4 = -10 \le 0$, $\mathbf{a}_2 \cdot \mathbf{r}_4 = 0$, $\mathbf{a}_3 \cdot \mathbf{r}_4 = -1 \le 0$, and for $j \in \{0, \dots, 9\}$, $(x_1+x_2-jx_3)(\mathbf{r}_4) = -10 + j \le -1 < 0$.
   - $i$ corresponding to $y_j \le 1$ ($j = 0, \dots, 9$): $\mathbf{r} = +\mathbf{e}_{4+j}$ gives $+1$ on $y_j \le 1$, $-1$ on $-y_j + x_1 + x_2 - j x_3 \le 119 + j^2$, and $0$ on all other rows.
   - $i$ corresponding to $-y_j + x_1 + x_2 - j x_3 \le 119 + j^2$ ($j = 0, \dots, 9$): $\mathbf{r} = -\mathbf{e}_{4+j}$ works symmetrically.

   Thus for every $i$, $\bigcap_{m \neq i} H_m^-$ contains the entire ray $\{\mathbf{0} + t\mathbf{r}_i : t \ge 0\}$, so omitting $H_i^-$ makes the intersection unbounded (and $H_i^-$ is irredundant). Hence $P$ is a primitive $13$-polytope.

---

## Exact Vertex Count: $8704 > 8192 = 2^{13}$

Eliminating each $y_j$ via $x_1 + x_2 - j x_3 - (119 + j^2) \le y_j \le 1$ projects $P$ onto the $3$-polytope $P_x \subset \mathbb{R}^3$ defined by:
$$x_1 \le 100,\quad x_2 \le 100,\quad x_3 \le 100,\quad -x_1-x_2-x_3 \le 100,$$
$$x_1 + x_2 - j x_3 \le 120 + j^2 \qquad (j = 0, 1, \dots, 9).$$

Note that the $10$ slice planes $x_1 + x_2 - j x_3 = 120 + j^2$ ($j = 0, \dots, 9$) form a convex parabolic envelope cutting the faces $x_1 = 100$ and $x_2 = 100$ of the base $3$-simplex:
- At each $x = (x_1, x_2, x_3) \in \mathrm{vert}(P_x)$, let $r(x)$ be the number of slice inequalities $x_1 + x_2 - j x_3 \le 120 + j^2$ ($0 \le j \le 9$) tight at $x$.
- If slice $j$ is tight at $x$, $y_j$ is uniquely forced to $y_j = 1$; if strict, $y_j$ has $2$ extreme choices $y_j \in \{1,\ x_1 + x_2 - j x_3 - (119 + j^2)\}$ yielding linearly independent active constraints.
- In $P_x$, there are $24$ vertices:
  - $2$ vertices with $r(x) = 0$: $(-300, 100, 100)$ and $(100, -300, 100)$ ($\implies 2 \cdot 2^{10} = 2048$ vertices of $P$).
  - $4$ vertices with $r(x) = 1$: $(-1699/10, 100, -301/10)$, $(20, 100, 100)$, $(100, -1699/10, -301/10)$, and $(100, 20, 100)$ ($\implies 4 \cdot 2^9 = 2048$ vertices of $P$).
  - $18$ vertices with $r(x) = 2$: $9$ along $x_2 = 100$ given by $(20 - m^2 - m,\ 100,\ -2m-1)$ for $m = 8, 7, \dots, 0$, i.e., $(-52,100,-17)$, $(-36,100,-15)$, $(-22,100,-13)$, $(-10,100,-11)$, $(0,100,-9)$, $(8,100,-7)$, $(14,100,-5)$, $(18,100,-3)$, $(20,100,-1)$, together with their $9$ reflections $(100, x_1, x_3)$ along $x_1 = 100$ ($\implies 18 \cdot 2^8 = 4608$ vertices of $P$).

Summing $2048 + 2048 + 4608$ over all $24$ vertices of $P_x$ yields **$8704$ distinct vertices** of $P$, strictly exceeding $2^{13} = 8192$.

---

## Verification

Exact-rational (`fractions.Fraction`) verification is implemented in [`verify.py`](./verify.py), which checks:
1. $\mathbf{0} \in \mathrm{int} P$ and the positive linear dependence $\sum \mu_i \mathbf{a}_i = \mathbf{0}$ ($\mu_i > 0$).
2. All $24$ ray-unboundedness certificates $\mathbf{r}_i$.
3. Exact enumeration of all $24$ vertices of $P_x$ and all $8704$ lifted vertices of $P$, verifying exact inequality satisfaction $A\mathbf{v} \le \mathbf{b}$ and full rank $13$ of the active constraint matrix at every single vertex.

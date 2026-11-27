# Proof of Hong Duc Bui's Acyclicity Conjecture (`arXiv:2508.04602v1`, §8.2)

**Target:** `bui-2508.04602-conj8.1`
**Label:** Written proof, key lemmas tested on small cases (`verify.py` uses exact integer arithmetic; pending independent check & audit).

## Statement
Let $Q \subset \mathbb{R}^2$ be a planar point set in general position (no three points collinear) with $|Q|=2n$ and $|\mathrm{CH}(Q)|=n$. Let $Q_1, \dots, Q_n$ be the vertices of $\mathrm{CH}(Q)$ in counterclockwise cyclic order (indices modulo $n$), and let $B_1, \dots, B_n$ be the $n$ interior points $Q \setminus \mathrm{CH}(Q)$.

For each permutation $\pi = (\pi_1, \dots, \pi_n) \in S_n$, consider the $n$ triangles $T_k(\pi) := \triangle Q_k B_{\pi_k} Q_{k+1}$ for $k = 1, \dots, n$. Define the directed state graph $G$ with vertex set $S_n$ and a directed edge $\pi \to \rho$ if and only if there exist two distinct indices $i \neq j$ such that $\rho$ is obtained from $\pi$ by swapping $\pi_i$ and $\pi_j$ ($\rho_i = \pi_j$, $\rho_j = \pi_i$, and $\rho_k = \pi_k$ for $k \notin \{i,j\}$) and the triangles $T_i(\pi)$ and $T_j(\pi)$ intersect (nontrivially, i.e., beyond a shared convex-hull vertex when $j \equiv i \pm 1 \pmod n$).

**Theorem.** For every $n \ge 3$ and every general-position point set $Q$ with $|Q|=2n$ and $|\mathrm{CH}(Q)|=n$, the directed graph $G$ is acyclic. In particular, the iterative swap algorithm always terminates (in at most $n! - 1$ steps) and moreover, for every edge $\pi \to \rho$ swapping $i$ and $j$, the swapped triangles $T_i(\rho)$ and $T_j(\rho)$ do not intersect.

*(Note: $|\mathrm{CH}(Q)|=n$ with $n$ interior points in general position requires $n \ge 3$.)*

---

## Proof

### Lemma 1 (General-Position Intersection Equivalence)
For any $i \neq j$ and $a \neq b$, the closed triangles $T_i = \triangle Q_i B_a Q_{i+1}$ and $T_j = \triangle Q_j B_b Q_{j+1}$ intersect nontrivially (i.e., $T_i \cap T_j \not\subseteq \{Q_i, Q_{i+1}\} \cap \{Q_j, Q_{j+1}\}$) if and only if their open interiors intersect: $\mathrm{int}(T_i) \cap \mathrm{int}(T_j) \neq \emptyset$.

**Proof of Lemma 1.**
Clearly $\mathrm{int}(T_i) \cap \mathrm{int}(T_j) \neq \emptyset$ implies a nontrivial intersection since $\mathrm{int}(T_i)$ contains no vertices.
Conversely, suppose $X \in T_i \cap T_j$ is not a shared hull vertex in $\{Q_i, Q_{i+1}\} \cap \{Q_j, Q_{j+1}\}$. Because $B_a \neq B_b$, the two triangles have no shared vertices outside $\{Q_i, Q_{i+1}\} \cap \{Q_j, Q_{j+1}\}$, so $X$ is not a common vertex of $T_i$ and $T_j$.
- If $X \in \mathrm{int}(T_i)$ (or symmetrically $X \in \mathrm{int}(T_j)$), then because $T_j$ is non-degenerate (general position) and $\mathrm{int}(T_i)$ is open, every neighborhood of $X$ meets $\mathrm{int}(T_j)$, so $\mathrm{int}(T_i) \cap \mathrm{int}(T_j) \neq \emptyset$.
- Otherwise $X \in \partial T_i \cap \partial T_j$. Since $X$ is not a common vertex, $X$ lies in the relative interior of some edge $e_i$ of $T_i$ (or $e_j$ of $T_j$). By general position (no three points of $Q$ collinear), no vertex of $T_j$ can lie in $\mathrm{relint}(e_i)$, so $X \in \mathrm{relint}(e_i) \cap \mathrm{relint}(e_j)$ for an edge $e_i$ of $T_i$ and an edge $e_j$ of $T_j$. Moreover $e_i$ and $e_j$ cannot be collinear: they have distinct pairs of endpoints in $Q$ (since $Q_i Q_{i+1} \neq Q_j Q_{j+1}$ and $B_a \neq B_b$), so collinearity would put at least three points of $Q$ on one line. Thus $e_i$ and $e_j$ cross transversely at $X$. Near $X$, $\mathrm{int}(T_i)$ fills an open half-plane bounded by $\overline{e_i}$ and $\mathrm{int}(T_j)$ fills an open half-plane bounded by $\overline{e_j}$; since $\overline{e_i} \neq \overline{e_j}$, these two open half-planes intersect in a nonempty open wedge at $X$, giving $\mathrm{int}(T_i) \cap \mathrm{int}(T_j) \neq \emptyset$. $\square$

---

### Lemma 2 (Positivity of Oriented Edge-Height Functions)
For each $k \in \{1, \dots, n\}$, define the affine function $\ell_k : \mathbb{R}^2 \to \mathbb{R}$ by the $2\times 2$ determinant
$$\ell_k(X) := \det(Q_{k+1} - Q_k,\; X - Q_k) = 2 \cdot \mathrm{Area}_{\mathrm{signed}}(\triangle Q_k Q_{k+1} X).$$
Then:
1. $\ell_k(Q_k) = \ell_k(Q_{k+1}) = 0$.
2. $\ell_k(Q_m) > 0$ for all $m \in \{1,\dots,n\} \setminus \{k, k+1\}$.
3. $\ell_k(B_r) > 0$ for all $r \in \{1,\dots,n\}$.
4. For any $i \neq j$ in $\{1,\dots,n\}$, $\ell_j(Q_i) \ge 0$, $\ell_j(Q_{i+1}) \ge 0$, and $\ell_j(Q_i) + \ell_j(Q_{i+1}) > 0$.

**Proof of Lemma 2.**
Property (1) is immediate. Because $Q$ is in general position and $Q_1, \dots, Q_n$ are the vertices of $\mathrm{CH}(Q)$ in counterclockwise order, every point of $Q \setminus \{Q_k, Q_{k+1}\}$ lies in $\mathrm{CH}(Q)$ and cannot lie on the supporting line $\overline{Q_k Q_{k+1}}$ (which would make three points of $Q$ collinear). Hence $\ell_k > 0$ strictly at every $Q_m$ ($m \notin \{k, k+1\}$) and every interior point $B_r$, proving (2) and (3). For (4), since $i \neq j$ and $n \ge 3$, $\{Q_i, Q_{i+1}\} \neq \{Q_j, Q_{j+1}\}$, so at least one of $Q_i, Q_{i+1}$ lies outside $\{Q_j, Q_{j+1}\}$ and therefore has $\ell_j > 0$ by (2), while the other has $\ell_j \ge 0$ by (1)–(2). $\square$

---

### Lemma 3 (Strict Area-Product Decrease on Every Swap)
Suppose $\pi \to \rho$ is a directed edge of $G$ swapping indices $i \neq j$, so that $\mathrm{int}(T_i(\pi)) \cap \mathrm{int}(T_j(\pi)) \neq \emptyset$. Then
$$\ell_i(B_{\pi_j}) \ell_j(B_{\pi_i}) < \ell_i(B_{\pi_i}) \ell_j(B_{\pi_j}).$$
Equivalently, $\mathrm{Area}(T_i(\rho)) \mathrm{Area}(T_j(\rho)) < \mathrm{Area}(T_i(\pi)) \mathrm{Area}(T_j(\pi))$. Furthermore, $T_i(\rho)$ and $T_j(\rho)$ do not intersect nontrivially.

**Proof of Lemma 3.**
Pick any point $Z \in \mathrm{int}(T_i(\pi)) \cap \mathrm{int}(T_j(\pi))$.
Because $Z \in \mathrm{int}(\triangle Q_i B_{\pi_i} Q_{i+1})$, there exist strictly positive barycentric coordinates $\alpha, \beta, \gamma > 0$ with $\alpha + \beta + \gamma = 1$ such that
$$Z = \alpha Q_i + \beta Q_{i+1} + \gamma B_{\pi_i}.$$
Applying the affine functions $\ell_i$ and $\ell_j$ and using Lemma 2(1),(3),(4):
$$\ell_i(Z) = \gamma \ell_i(B_{\pi_i}) > 0,$$
$$\ell_j(Z) = \alpha \ell_j(Q_i) + \beta \ell_j(Q_{i+1}) + \gamma \ell_j(B_{\pi_i}) > \gamma \ell_j(B_{\pi_i}) > 0,$$
where the strict inequality holds because $\alpha, \beta > 0$, $\ell_j(Q_i), \ell_j(Q_{i+1}) \ge 0$, and $\ell_j(Q_i) + \ell_j(Q_{i+1}) > 0$. Dividing the two positive relations yields
$$\frac{\ell_i(Z)}{\ell_j(Z)} < \frac{\gamma \ell_i(B_{\pi_i})}{\gamma \ell_j(B_{\pi_i})} = \frac{\ell_i(B_{\pi_i})}{\ell_j(B_{\pi_i})}.$$
Applying the exact same argument to $Z \in \mathrm{int}(T_j(\pi)) = \mathrm{int}(\triangle Q_j B_{\pi_j} Q_{j+1})$ gives
$$\frac{\ell_j(Z)}{\ell_i(Z)} < \frac{\ell_j(B_{\pi_j})}{\ell_i(B_{\pi_j})}.$$
Multiplying these two strict inequalities between positive real numbers gives
$$1 = \frac{\ell_i(Z)}{\ell_j(Z)} \cdot \frac{\ell_j(Z)}{\ell_i(Z)} < \frac{\ell_i(B_{\pi_i}) \ell_j(B_{\pi_j})}{\ell_j(B_{\pi_i}) \ell_i(B_{\pi_j})},$$
and clearing the positive denominators yields
$$\ell_i(B_{\pi_j}) \ell_j(B_{\pi_i}) < \ell_i(B_{\pi_i}) \ell_j(B_{\pi_j}).$$
Since $\rho_i = \pi_j$ and $\rho_j = \pi_i$, and $\mathrm{Area}(T_k(\sigma)) = \frac{1}{2}\ell_k(B_{\sigma_k})$, this reads $\mathrm{Area}(T_i(\rho))\mathrm{Area}(T_j(\rho)) < \mathrm{Area}(T_i(\pi))\mathrm{Area}(T_j(\pi))$.

Finally, if $T_i(\rho)$ and $T_j(\rho)$ intersected nontrivially, then by Lemma 1 we would have $\mathrm{int}(T_i(\rho)) \cap \mathrm{int}(T_j(\rho)) \neq \emptyset$, and applying the same inequality to $(\rho_i, \rho_j) = (\pi_j, \pi_i)$ would yield $\ell_i(B_{\pi_i})\ell_j(B_{\pi_j}) < \ell_i(B_{\pi_j})\ell_j(B_{\pi_i})$, a contradiction. $\square$

---

### Proof of the Main Theorem
Define the potential $\Phi : S_n \to \mathbb{R}_{>0}$ by
$$\Phi(\pi) := \prod_{k=1}^n \ell_k(B_{\pi_k}) = 2^n \prod_{k=1}^n \mathrm{Area}(T_k(\pi)).$$
By Lemma 2(3), $\Phi(\pi) > 0$ for every $\pi \in S_n$. Whenever $\pi \to \rho$ is a directed edge of $G$ swapping $i$ and $j$, all factors $k \notin \{i, j\}$ are unchanged ($\rho_k = \pi_k$), so Lemma 3 implies
$$\frac{\Phi(\rho)}{\Phi(\pi)} = \frac{\ell_i(B_{\pi_j})\ell_j(B_{\pi_i})}{\ell_i(B_{\pi_i})\ell_j(B_{\pi_j})} < 1,$$
and hence $\Phi(\rho) < \Phi(\pi)$ strictly.

Since $\Phi$ strictly decreases along every directed edge of the finite graph $G$ ($|S_n| = n!$), $G$ cannot contain any directed cycle. Therefore $G$ is a finite directed acyclic graph, and the swap algorithm must terminate in at most $n! - 1$ steps.

*(Remark on order types: Whether two triangles $T_i(\pi), T_j(\pi)$ intersect depends solely on the order type of $Q$. By definition of a planar order type, $Q$ admits a realization in $\mathbb{R}^2$ in general position, on which $\Phi$ strictly decreases along every edge of $G$. Hence $G$ is acyclic for all order types $Q$ in general position with $|Q|=2n$ and $|\mathrm{CH}(Q)|=n$.)* $\blacksquare$

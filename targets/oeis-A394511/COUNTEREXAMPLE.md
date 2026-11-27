# Counterexample Refuting OEIS A394511 (Exley Enclosing Shell Conjecture)

## Statement Refuted
In OEIS `A394511` (Peter Exley, rev. 2026-06-06), on the edge-adjacency graph of the truncated-square (`4.8.8`) Archimedean tiling, for a connected $n$-cell hole $H$, the corona $C(H)$ is the set of cells outside $H$ sharing an edge with at least one cell in $H$, and an enclosing shell $S \supseteq C(H)$ is a connected set disjoint from $H$ such that the exterior complement of $H \cup S$ is connected. $a(n)$ is the minimum $|S|$ over all connected $n$-cell holes $H$.

The conjecture states:
> "Conjectured (UNVERIFIED beyond n = 23): the minimum shell equals the corona of the optimal hole, |S| = |C(H)|; and a(n) = 2*ceiling((n + 17)/5) for n >= 6, equivalently a(n) = a(n - 5) + 2 for n >= 11."

**Result:** **FALSE.** Two-dimensional rectangular blocks of octagons and enclosed squares have $O(\sqrt{n})$ boundary rather than linear $\frac{2}{5} n$ growth. Explicitly, for every $R, C \ge 2$, there is a connected hole $H(R, C)$ of size $n(R, C) = 2RC + R + C - 3$ whose corona $S = C(H(R, C))$ is a valid connected enclosing shell of size $2R + 2C + 4$:
- **Explicit small counterexample ($R = 3, C = 5$):** $n = 35$, giving $a(35) \le 20 < 22 = 2\lceil (35 + 17)/5 \rceil$. (Removing one corner octagon from $H(3, 5)$ also gives $a(34) \le 20 < 22$.) This likewise refutes $a(n) = a(n - 5) + 2$ for $n \ge 11$, since $a(20) = 16$ would force $a(35) = 22$.
- **Infinite family ($R = C = k \ge 4$):** $n_k = 2k^2 + 2k - 3$ satisfies $a(n_k) \le 4k + 4$, whereas $2\lceil (n_k + 17)/5 \rceil = 2\lceil (2k^2 + 2k + 14)/5 \rceil \ge \frac{4k^2 + 4k + 28}{5} > 4k + 4$ for all $k \ge 4$ (since $4k^2 - 16k + 8 = 4(k-2)^2 - 8 > 0$ for $k \ge 4$; e.g. $20 < 22$ at $k = 4$, $n_4 = 37$).

---

## 1. Exact Coordinate Model of the `4.8.8` Tiling
In the regular `4.8.8` tiling of unit edge length $1$ (apothem of each octagon $a = \frac{1+\sqrt{2}}{2}$, spacing $w = 1 + \sqrt{2}$):
- **Octagons** $\mathrm{O}(x, y)$ for $(x, y) \in \mathbb{Z}^2$ have centers $(w x, w y)$ and share horizontal/vertical edges with $\mathrm{O}(x\pm 1, y)$ and $\mathrm{O}(x, y\pm 1)$, and $45^\circ$-diagonal edges with the four squares $\mathrm{S}(x, y), \mathrm{S}(x-1, y), \mathrm{S}(x, y-1), \mathrm{S}(x-1, y-1)$.
- **Squares** $\mathrm{S}(i, j)$ for $(i, j) \in \mathbb{Z}^2$ have centers $(w(i + \frac{1}{2}), w(j + \frac{1}{2}))$ and share their four edges exclusively with the four octagons $\mathrm{O}(i, j), \mathrm{O}(i+1, j), \mathrm{O}(i, j+1), \mathrm{O}(i+1, j+1)$ (squares share no edges with other squares).

Thus the edge-adjacency graph $G_{4.8.8}$ has vertex set $\{0, 1\} \times \mathbb{Z}^2$ (where $0$ denotes $\mathrm{O}$ and $1$ denotes $\mathrm{S}$) and edges precisely between:
- $\mathrm{O}(x, y) \sim \mathrm{O}(x \pm 1, y)$, $\mathrm{O}(x, y) \sim \mathrm{O}(x, y \pm 1)$, and
- $\mathrm{S}(i, j) \sim \mathrm{O}(i + \alpha, j + \beta)$ for $(\alpha, \beta) \in \{0, 1\}^2$.

---

## 2. Explicit Family $H(R, C)$ and Shell $S(R, C)$ ($R, C \ge 2$)

Fix integers $R, C \ge 2$ and define the cell set $H(R, C)$ as the union of:
1. the $R \times C$ block of octagons $\mathcal{O}_{R,C} := \{\mathrm{O}(x, y) : 0 \le x \le R-1,\; 0 \le y \le C-1\}$ ($R C$ cells),
2. the $(R-1) \times (C-1)$ block of interior squares $\{\mathrm{S}(i, j) : 0 \le i \le R-2,\; 0 \le j \le C-2\}$ ($(R-1)(C-1)$ cells),
3. the $2(R-1) + 2(C-1)$ perimeter edge squares sitting along the four sides of $\mathcal{O}_{R,C}$:
   $$\{\mathrm{S}(i, -1),\, \mathrm{S}(i, C-1) : 0 \le i \le R-2\} \cup \{\mathrm{S}(-1, j),\, \mathrm{S}(R-1, j) : 0 \le j \le C-2\}.$$

### Exact Cell Count
$$|H(R, C)| = R C + (R - 1)(C - 1) + 2(R - 1) + 2(C - 1) = 2RC + R + C - 3.$$

### Proof That $H(R, C)$ Is Connected
The octagon subgrid $\mathcal{O}_{R,C}$ is a connected $R \times C$ grid graph. Every square in $H(R, C)$ has at least two of its four octagon neighbors inside $\mathcal{O}_{R,C}$ (interior squares have all four; edge squares have two). Thus $H(R, C)$ is connected.

### Exact Corona $S(R, C) = C(H(R, C))$ and Connectedness
We determine all cells outside $H(R, C)$ adjacent to a cell in $H(R, C)$:
- **Octagons outside $\mathcal{O}_{R,C}$ adjacent to $H(R, C)$:**
  - Every octagon $\mathrm{O}(x, y) \in \mathcal{O}_{R,C}$ has orthogonal neighbors inside $[-1, R] \times [-1, C]$ excluding the four corners $(-1, -1), (R, -1), (-1, C), (R, C)$.
  - Every edge square in $H(R, C)$ has two octagon neighbors in $\mathcal{O}_{R,C}$ and two on the exact same four sides:
    - $\mathrm{S}(i, -1)$ ($0 \le i \le R-2$) touches $\mathrm{O}(i, -1)$ and $\mathrm{O}(i+1, -1)$;
    - $\mathrm{S}(i, C-1)$ touches $\mathrm{O}(i, C)$ and $\mathrm{O}(i+1, C)$;
    - $\mathrm{S}(-1, j)$ ($0 \le j \le C-2$) touches $\mathrm{O}(-1, j)$ and $\mathrm{O}(-1, j+1)$;
    - $\mathrm{S}(R-1, j)$ touches $\mathrm{O}(R, j)$ and $\mathrm{O}(R, j+1)$.
  Notice NO corner octagon $(-1, -1), (R, -1), (-1, C), (R, C)$ is adjacent to any cell of $H(R, C)$. Thus the octagons in $C(H(R, C))$ are precisely the $2R + 2C$ side octagons:
  $$\{\mathrm{O}(x, -1),\, \mathrm{O}(x, C) : 0 \le x \le R-1\} \cup \{\mathrm{O}(-1, y),\, \mathrm{O}(R, y) : 0 \le y \le C-1\}.$$
- **Squares outside $H(R, C)$ adjacent to $H(R, C)$:**
  Squares only share edges with octagons, so a square $\mathrm{S}(i, j) \notin H(R, C)$ lies in $C(H(R, C))$ iff $\{i, i+1\} \times \{j, j+1\}$ meets $[0, R-1] \times [0, C-1]$, i.e. $-1 \le i \le R-1$ and $-1 \le j \le C-1$. Every such $(i, j)$ is already in $H(R, C)$ **except the four corner squares**:
  $$\{\mathrm{S}(-1, -1),\; \mathrm{S}(R-1, -1),\; \mathrm{S}(R-1, C-1),\; \mathrm{S}(-1, C-1)\}.$$

Hence $|C(H(R, C))| = 2R + 2C + 4$. Moreover, $S := C(H(R, C))$ forms a single closed cycle in $G_{4.8.8}$:
- Bottom side $\mathrm{O}(0,-1) - \dots - \mathrm{O}(R-1,-1)$ connects via corner square $\mathrm{S}(R-1,-1)$ to right side $\mathrm{O}(R,0) - \dots - \mathrm{O}(R,C-1)$,
- which connects via $\mathrm{S}(R-1,C-1)$ to top side $\mathrm{O}(R-1,C) - \dots - \mathrm{O}(0,C)$,
- which connects via $\mathrm{S}(-1,C-1)$ to left side $\mathrm{O}(-1,C-1) - \dots - \mathrm{O}(-1,0)$,
- which closes via $\mathrm{S}(-1,-1)$ back to $\mathrm{O}(0,-1)$.
Thus $S = C(H(R, C))$ is connected and disjoint from $H(R, C)$.

### Proof That the Exterior Is Connected
Let $E := V(G_{4.8.8}) \setminus (H(R, C) \cup S(R, C))$.
- The exterior octagons are all $\mathrm{O}(x, y) \notin [0, R-1]\times[0, C-1]$ outside the four side strips (namely all $\mathrm{O}(x, y)$ with $x \le -1$ and $y \notin [0, C-1]$, $x \ge R$ and $y \notin [0, C-1]$, $x \le -2$, $x \ge R+1$, $y \le -2$, or $y \ge C+1$). Note that the four corner octagons $(-1,-1), (R,-1), (-1,C), (R,C)$ are adjacent to $(-2,-1), (R+1,-1), (-2,C), (R+1,C)$, and the infinite grid complement of $[-1, R]\times[-1, C]$ is orthogonally connected, so all exterior octagons lie in one connected component.
- Every exterior square $\mathrm{S}(i, j) \in E$ satisfies $(i, j) \notin [-1, R-1] \times [-1, C-1]$, so at least one index violates $[-1, R-1]$ or $[-1, C-1]$: e.g., if $i \le -2$ then $\mathrm{O}(i, j) \in E$ (since $i \le -2$), if $i \ge R$ then $\mathrm{O}(i+1, j) \in E$ (since $i+1 \ge R+1$), if $j \le -2$ then $\mathrm{O}(i, j) \in E$, and if $j \ge C$ then $\mathrm{O}(i, j+1) \in E$. Thus every exterior square connects directly to an exterior octagon.

Hence $S(R, C) = C(H(R, C))$ is a valid connected enclosing shell of $H(R, C)$ for every $R, C \ge 2$, proving
$$a(2RC + R + C - 3) \le 2R + 2C + 4.$$

### Disproof of Exley's Formula and Recurrence
1. At $(R, C) = (3, 5)$: $n = 2(15) + 3 + 5 - 3 = 35$ and $|S| = 2(3) + 2(5) + 4 = 20$, whereas the conjectured formula gives $2\lceil (35 + 17)/5 \rceil = 22 > 20$. (Similarly, $(R, C) = (4, 4)$ gives $n = 37$, $|S| = 20 < 22$, and removing $\mathrm{O}(0, 0)$ from $H(3, 5)$ gives $n = 34$, $|S| = 20 < 22$.)
2. This also disproves $a(n) = a(n - 5) + 2$ for $n \ge 11$: OEIS `A394511` gives $a(20) = 16$, so the recurrence would require $a(35) = 16 + 3 \cdot 2 = 22$, contradicting $a(35) \le 20$.
3. Taking $R = C = k \ge 4$ yields an infinite family $n_k = 2k^2 + 2k - 3$ with $a(n_k) \le 4k + 4$, whereas $2\lceil (n_k + 17)/5 \rceil \ge \frac{4k^2 + 4k + 28}{5} > 4k + 4$ for all $k \ge 4$ (as $4(k-2)^2 - 8 > 0$ for $k \ge 4$). $\square$

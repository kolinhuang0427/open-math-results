# Proof of Conjecture 3.8 (`\label{iG-conj}`) of Marberg–Morales–Yu (`arXiv:2611.19371v1`)

## Main Theorem

**Theorem** (Conjecture 3.8 / `\label{iG-conj}` of Eric Marberg, Alejandro H. Morales, and Tianyi Yu, *Bumpless pipe dreams for involutions and shifted plane partitions*, `arXiv:2611.19371v1`, Section 3.3, lines 2885–2890; also stated in Section 1.2, lines 595–604).
*For every positive integer $n \ge 1$ and every involution $z \in I_n = \{z \in S_n : z = z^{-1}\}$,*
$$\widehat{\mathfrak{G}}^{(\beta)}_z \;=\; \sum_{D \in \mathsf{InvBPD}_K(z)} \beta^{|\mathrm{blank}(D)| - \ell_{\mathrm{inv}}(z)} \cdot \widehat{\mathrm{kwt}}(D),$$
*where $\widehat{\mathrm{kwt}}(D) = \prod_{(i,j) \in \mathrm{blank}(D)} x_{i\oplus j} \prod_{(i,j) \in \mathrm{upturn}(D)} (1 + \beta x_{i\oplus j})$, with $x_{i\oplus i} = x_i$ and $x_{i\oplus j} = x_i \oplus x_j = x_i + x_j + \beta x_i x_j$ for $i \neq j$.*

---

## Proof Overview

We prove the conjecture directly from the unique isobaric divided-difference characterization of $\widehat{\mathfrak{G}}^{(\beta)}_z$ (Definition 2.7 in Section 2.3 of `arXiv:2611.19371v1`, lines 1044–1053), bypassing any need for a $K$-theoretic involution transition formula.

After rescaling by $\beta^{\ell_{\mathrm{inv}}(z)}$ and setting $u_i = 1 + \beta x_i$, the generating function over $\mathsf{InvBPD}_K(z)$ becomes the partition function of a **folded colored six-vertex lattice model** on the lower triangle $\mathrm{LT}_n = \{(i, j) \in [n]^2 : i \ge j\}$ with a **reflecting diagonal boundary** (obtained by folding the symmetric square bumpless pipe dream $\mathrm{double}(D)$ across the main diagonal, so each occupied edge carries a pair of pipe colors $(c_{\mathrm{in}}, c_{\mathrm{out}})$). We construct explicit colored $R$-matrices $R(u_1, u_2)$ and $R_V(u_1, u_2)$ built from the $0$-Hecke sorting operator, prove completely by hand the **Horizontal and Vertical Bulk Yang–Baxter Equations** (Lemma 2) and the **$2 \times 2$ Diagonal Reflection Equation** (Lemma 3), and apply the lattice **train argument** (Lemma 4) to show that the $\mathsf{InvBPD}_K(z)$ generating functions satisfy the exact isobaric divided-difference recurrence $\overline{\partial}_i R_{s_i \circ z \circ s_i} = R_z$. Together with the uniqueness of the longest-involution diagram $\mathsf{InvBPD}_K(w_0^{(n)})$ (Lemma 5), downward induction on $\ell_{\mathrm{inv}}(z)$ proves the theorem for all $n \ge 1$ and all $z \in I_n$.

---

## 1. Preliminaries, Notation, and the Folded Colored Lattice Model

Let $n \ge 1$ be fixed, and let $S_n$ be the symmetric group with simple transpositions $s_1, \dots, s_{n-1}$, Coxeter length $\ell(w)$, and associative Demazure ($0$-Hecke) product $\circ$ defined by $s_i \circ s_i = s_i$ and $u \circ v = uv$ whenever $\ell(uv) = \ell(u) + \ell(v)$. We write permutations in one-line notation $w = (w(1), \dots, w(n))$ with composition $(uv)(k) = u(v(k))$. For an involution $z \in I_n$, let $\mathrm{cyc}(z) = |\{i \in [n] : z(i) > i\}|$ be the number of $2$-cycles of $z$. By Section 2.1–2.2 (`arXiv:2611.19371v1`, eqs. `(szs-eq)`–`(ellinv-def)` and line 972),
$$\ell_{\mathrm{inv}}(z) := \min\{\ell(w) : w \in S_n,\; w \circ w^{-1} = z\} = \frac{\ell(z) + \mathrm{cyc}(z)}{2} = |\mathrm{iD}(z)|,$$
where $\mathrm{iD}(z) = \{(i,j) \in \mathrm{LT}_n : z(i) > j \text{ and } z(j) > i\}$ is the involution Rothe diagram, and for every $i \in [n-1]$:
$$s_i \circ z \circ s_i = \begin{cases} s_i z & \text{if } z(i) < z(i+1) \text{ and } s_i z s_i = z \text{ (i.e., } z(i) = i,\; z(i+1) = i+1\text{)}, \\ s_i z s_i & \text{if } z(i) < z(i+1) \text{ and } s_i z s_i \neq z, \\ z & \text{if } z(i) > z(i+1). \end{cases} \tag{1}$$
Whenever $s_i \circ z \circ s_i \neq z$ (i.e., $z(i) < z(i+1)$), we have $\ell_{\mathrm{inv}}(s_i \circ z \circ s_i) = \ell_{\mathrm{inv}}(z) + 1$: in the first case $\ell$ and $\mathrm{cyc}$ each increase by $1$, while in the second case $\ell$ increases by $2$ and $\mathrm{cyc}$ is unchanged.

For $f \in \mathbb{Z}[\beta][x_1, \dots, x_n]$ and $i \in [n-1]$, let $s_i f$ swap $x_i \leftrightarrow x_{i+1}$, and recall the divided difference and isobaric divided difference operators (Section 2.3, lines 1003–1007):
$$\partial_i f = \frac{f - s_i f}{x_i - x_{i+1}}, \qquad \overline{\partial}_i f = -\beta f + (1 + \beta x_i)\,\partial_i f.$$
By Definition 2.7 (Section 2.3, lines 1044–1053), the **involution Grothendieck polynomials** $\{\widehat{\mathfrak{G}}^{(\beta)}_z\}_{z \in I_n} \subset \mathbb{Z}[\beta][x_1, \dots, x_n]$ are uniquely characterized by:
- **(a)** If $z \in I_n$ is dominant (in particular for the longest involution $w_0^{(n)} = (n, n-1, \dots, 1)$), then $\widehat{\mathfrak{G}}^{(\beta)}_z = \prod_{(i,j) \in \mathrm{iD}(z)} x_{i\oplus j}$.
- **(b)** If $i \in [n-1]$ satisfies $s_i \circ z \circ s_i \neq z$, then $\overline{\partial}_i \widehat{\mathfrak{G}}^{(\beta)}_{s_i \circ z \circ s_i} = \widehat{\mathfrak{G}}^{(\beta)}_z$.

*(Uniqueness from $w_0^{(n)}$ alone: for any $z \in I_n \setminus \{w_0^{(n)}\}$, $z$ has an ascent $z(i) < z(i+1)$ for some $i \in [n-1]$, so $z' := s_i \circ z \circ s_i \in I_n$ satisfies $z' \neq z$ and $\ell_{\mathrm{inv}}(z') = \ell_{\mathrm{inv}}(z) + 1$; downward induction from $w_0^{(n)}$ therefore uniquely determines all $\widehat{\mathfrak{G}}^{(\beta)}_z$.)*

### Change of Variables

For each $z \in I_n$, set
$$R_z(\beta, x_1, \dots, x_n) := \sum_{D \in \mathsf{InvBPD}_K(z)} \beta^{|\mathrm{blank}(D)| - \ell_{\mathrm{inv}}(z)} \cdot \widehat{\mathrm{kwt}}(D).$$
For every $D \in \mathsf{InvBPD}_K(z)$, since $D$ is bumpless, eq. `(cross-bump-blank-eq)` and Proposition 3.12 / Corollary 3.15 (`arXiv:2611.19371v1`, lines 3097–3201) give
$$|\mathrm{blank}(D)| = |\mathrm{cross}(D)| = |\mathrm{word}(D)| \ge \ell(\mathrm{kpi}(D)) \ge \ell_{\mathrm{inv}}(z),$$
so $R_z \in \mathbb{Z}[\beta, x_1, \dots, x_n]$. Now introduce independent variables $u_1, \dots, u_n$ related to $x_1, \dots, x_n$ by the substitution
$$u_i := 1 + \beta x_i \qquad (1 \le i \le n). \tag{2}$$
Observe that:
- for $i = j$: $1 + \beta x_{i\oplus i} = 1 + \beta x_i = u_i$ and $\beta x_{i\oplus i} = u_i - 1$;
- for $i > j$: $1 + \beta x_{i\oplus j} = 1 + \beta(x_i + x_j + \beta x_i x_j) = (1+\beta x_i)(1+\beta x_j) = u_i u_j$ and $\beta x_{i\oplus j} = u_i u_j - 1$.

Consequently, defining $\widetilde{R}_z(u_1, \dots, u_n) \in \mathbb{Z}[u_1, \dots, u_n]$ by
$$\widetilde{R}_z(\mathbf{u}) := \sum_{D \in \mathsf{InvBPD}_K(z)} \prod_{\substack{(i,j) \in \mathrm{blank}(D) \\ i > j}} (u_i u_j - 1) \prod_{\substack{(i,i) \in \mathrm{blank}(D)}} (u_i - 1) \prod_{\substack{(i,j) \in \mathrm{upturn}(D) \\ i > j}} (u_i u_j) \prod_{\substack{(i,i) \in \mathrm{upturn}(D)}} u_i, \tag{3}$$
we have the exact polynomial identity in $\mathbb{Z}[\beta, x_1, \dots, x_n]$:
$$\widetilde{R}_z(1 + \beta x_1, \dots, 1 + \beta x_n) = \beta^{\ell_{\mathrm{inv}}(z)} R_z(\beta, x_1, \dots, x_n). \tag{4}$$

### Folded Colored Lattice Model on $\mathrm{LT}_n$

Define the edge state space $\mathcal{E}_n := \{\varnothing\} \sqcup ([n] \times [n])$, where $\varnothing$ denotes an empty edge and $(a, b) \in [n] \times [n]$ denotes an occupied edge carrying an incoming (lower-triangle) pipe color $a$ and an outgoing (upper-triangle) pipe color $b$. Define the involution $\mathrm{flip}: \mathcal{E}_n \to \mathcal{E}_n$ by $\mathrm{flip}(\varnothing) = \varnothing$ and $\mathrm{flip}(a, b) = (b, a)$.

On a lower-triangle grid $\mathrm{LT}_n = \{(i, j) \in [n]^2 : i \ge j\}$ (row $1$ at top, row $n$ at bottom, column $1$ at left, column $n$ at right), assign horizontal spectral parameter $u_i$ to row $i$ and vertical spectral parameter $u_j$ to column $j$:

1. **Off-diagonal bulk vertex $W(u, v; W, S; E, N) \in \mathbb{Z}[u, v]$** at cell $(i, j)$ ($i > j$, with $u = u_i, v = u_j$, west/south/east/north edges $W, S, E, N \in \mathcal{E}_n$):
   - Blank ($\mathsf{B}$): $W = S = E = N = \varnothing \;\mapsto\; uv - 1$;
   - Horizontal ($\mathsf{H}$): $S = N = \varnothing,\; W = E = x \in [n]^2 \;\mapsto\; 1$;
   - Vertical ($\mathsf{V}$): $W = E = \varnothing,\; S = N = x \in [n]^2 \;\mapsto\; 1$;
   - Upturn ($\mathsf{J}$): $S = E = \varnothing,\; W = N = x \in [n]^2 \;\mapsto\; uv$;
   - Downturn ($\mathsf{C}$): $W = N = \varnothing,\; S = E = x \in [n]^2 \;\mapsto\; 1$;
   - Crossing ($\mathsf{P}$): $W = (w_1, n_2),\; S = (s_1, e_2),\; E = (e_1, s_2),\; N = (n_1, w_2) \in [n]^2$ with
     $$(e_1, n_1) = (\min(w_1, s_1),\, \max(w_1, s_1)) \quad\text{and}\quad (e_2, n_2) = (\min(w_2, s_2),\, \max(w_2, s_2)) \;\mapsto\; 1;$$
   - $0$ for all other $(W, S, E, N)$.

   Inspecting the six cases immediately gives the **exact transpose symmetry**
   $$W(v, u; W, S; E, N) = W\bigl(u, v; \mathrm{flip}(N), \mathrm{flip}(E); \mathrm{flip}(S), \mathrm{flip}(W)\bigr). \tag{5}$$
   *(Check: $\mathsf{B} \leftrightarrow \mathsf{B}$, $\mathsf{J} \leftrightarrow \mathsf{J}$, $\mathsf{C} \leftrightarrow \mathsf{C}$, $\mathsf{H} \leftrightarrow \mathsf{V}$, and on $\mathsf{P}$ the map $(W,S,E,N) \mapsto (\mathrm{flip}(N),\mathrm{flip}(E),\mathrm{flip}(S),\mathrm{flip}(W))$ exchanges $(w_1,s_1,e_1,n_1) \leftrightarrow (w_2,s_2,e_2,n_2)$.)*

2. **Diagonal boundary vertex $K(u; W, S) \in \mathbb{Z}[u]$** at cell $(i, i)$ (with $u = u_i$, west/south edges $W, S \in \mathcal{E}_n$):
   - Blank ($\mathsf{B}_{\mathrm{diag}}$): $W = S = \varnothing \;\mapsto\; u - 1$;
   - Upturn ($\mathsf{J}_{\mathrm{diag}}$): $W = (a, a),\; S = \varnothing \;\mapsto\; u$;
   - Downturn ($\mathsf{C}_{\mathrm{diag}}$): $W = \varnothing,\; S = (a, a) \;\mapsto\; 1$;
   - Crossing ($\mathsf{P}_{\mathrm{diag}}$): $W = (w_1, n_1),\; S = (s_1, e_1)$ with $(e_1, n_1) = (\min(w_1, s_1),\, \max(w_1, s_1)) \;\mapsto\; 1$;
   - $0$ for all other $(W, S)$.

For any two permutations $p, q \in S_n$, define the partition function $Z(p, q; u_1, \dots, u_n) \in \mathbb{Z}[u_1, \dots, u_n]$ to be the sum over all edge-state assignments on internal edges of $\mathrm{LT}_n$ of the product of vertex weights $\prod_{1 \le j < i \le n} W(u_i, u_j; \dots) \prod_{i=1}^n K(u_i; \dots)$, subject to the boundary conditions:
- west boundary (left edges of cells $(1,1), (2,1), \dots, (n,1)$): all $\varnothing$;
- south boundary (bottom edges of cells $(n,1), (n,2), \dots, (n,n)$): $(p(1), q(1)),\, (p(2), q(2)),\, \dots,\, (p(n), q(n))$.

---

## 2. Bijection with Symmetric Bumpless Pipe Dreams and Left Demazure Propagation

Recall from Section 3.5 (`arXiv:2611.19371v1`, eqs. `(double-def)`–`(double-eq)` and Proposition 3.19) that the map $\mathrm{double}$ identifies $\mathsf{InvBPD}_K(n) := \bigsqcup_{z \in I_n} \mathsf{InvBPD}_K(z)$ with the set of diagonally symmetric square bumpless pipe dreams $E = E^\top$ on $[n] \times [n]$, with $\mathrm{kpi}(\mathrm{double}(D)) = \mathrm{kpi}(D) \circ \mathrm{kpi}(D)^{-1} \in I_n$.

Given any square bumpless pipe dream $E$ on $[n] \times [n]$ and any south boundary labeling $p = (p(1), \dots, p(n)) \in S_n$ (entering columns $1, \dots, n$ from the south), let $\phi_E(p) \in S_n$ be the sequence of colors exiting the east boundary of rows $1, \dots, n$ (top to bottom) under the deterministic Demazure tile propagation rule: at $\mathsf{H}$, $(a, \varnothing) \to (a, \varnothing)$; at $\mathsf{V}$, $(\varnothing, b) \to (\varnothing, b)$; at $\mathsf{J}$, $(a, \varnothing) \to (\varnothing, a)$; at $\mathsf{C}$, $(\varnothing, b) \to (b, \varnothing)$; at $\mathsf{P}$, $(a, b) \to (\min(a,b), \max(a,b))$ on $(E, N)$.

### Lemma 1 (Folded Partition Function and Demazure Propagation)
Let $p, q \in S_n$.
1. **(a)** The valid folded states of $\mathrm{LT}_n$ with empty west boundary and south boundary $((p(1), q(1)), \dots, (p(n), q(n)))$ are in exact weight-preserving bijection with diagrams $D \in \mathsf{InvBPD}_K(n)$ satisfying $\phi_{\mathrm{double}(D)}(p) = q$.
2. **(b)** For every square bumpless pipe dream $E$ on $[n] \times [n]$ and every $p \in S_n$, $\phi_E(p) = p \circ \mathrm{kpi}(E)$.
3. **(c)** Consequently, for every $z \in I_n$, $Z(\mathrm{id}, z; \mathbf{u}) = \widetilde{R}_z(\mathbf{u})$ (and $Z(\mathrm{id}, w; \mathbf{u}) = 0$ if $w \notin I_n$), while for every $i \in [n-1]$ and $w \in S_n$,
   $$Z(s_i, w; \mathbf{u}) = \sum_{\substack{y \in I_n \\ s_i \circ y = w}} \widetilde{R}_y(\mathbf{u}). \tag{6}$$

**Proof.**
**(a)** Given a folded state on $\mathrm{LT}_n$ with nonzero weight, unfold it to a coloring of an $n \times n$ symmetric bumpless pipe dream $E = \mathrm{double}(D)$ as follows:
- For each cell $(i, j)$ with $i > j$, place the first coordinates of its four edges $(W, S, E, N)$ on the $(W, S, E, N)$ edges of $(i, j)$ in $E$, and place the second coordinates of $(W, S, E, N)$ on the $(N', E', S', W')$ edges of the mirror cell $(j, i)$ in $E$ (with the transposed tile $E_{ji} = E_{ij}^\top$).
- For each diagonal cell $(i, i)$, place the first and second coordinates of $W$ on the $(W, N)$ edges of $(i, i)$ in $E$, and those of $S$ on the $(S, E)$ edges of $(i, i)$ in $E$.

One checks immediately that adjacent cells agree on every shared edge:
- Between $(i, j)$ and $(i-1, j)$ ($i > j$): $N_1(i,j) = S_1(i-1,j)$, and in the upper triangle $(j, i)$ lies east of $(j, i-1)$, so $W_2(j,i) = E_2(j, i-1)$ matches the second coordinates of $N(i,j)$ and $S(i-1,j)$.
- Between $(i, j)$ and $(i, j+1)$ ($i > j+1$): $E_1(i,j) = W_1(i,j+1)$, and in the upper triangle $(j, i)$ lies north of $(j+1, i)$, so $S_2(j,i) = N_2(j+1, i)$ matches the second coordinates of $E(i,j)$ and $W(i,j+1)$.
- At the diagonal: $E(i, i-1)$ matches $W(i, i)$ and $N(i+1, i)$ matches $S(i, i)$ identically.

The empty west boundary of $\mathrm{LT}_n$ unfolds to empty west and north boundaries of $E$, and the south boundary $((p(1),q(1)), \dots, (p(n),q(n)))$ of $\mathrm{LT}_n$ unfolds to south boundary $p(1), \dots, p(n)$ (left to right) and east boundary $q(1), \dots, q(n)$ (top to bottom) of $E$. The vertex conditions of $W$ and $K$ are verbatim the Demazure propagation rule at every tile of $E$. Conversely, because $E$ has no bump tiles ($\mathsf{E}$), every wire travels strictly north and east, so no closed loops can exist; every wire enters at the south boundary and exits at the east boundary. Since Demazure propagation diagonal-by-diagonal from bottom-left to top-right is completely deterministic, each uncolored $D \in \mathsf{InvBPD}_K(n)$ admits a unique coloring of $\mathrm{double}(D)$ for south input $p$, yielding a unique east output $\phi_{\mathrm{double}(D)}(p) \in S_n$. Comparing the vertex weights of $W$ and $K$ with (3) shows the bijection preserves weights exactly.

**(b)** We follow the diagonal-by-diagonal proof of Proposition 3.12 (`arXiv:2611.19371v1`, lines 3119–3138). For $-n \le k \le n - 1$, let $\pi(E, p : k) \in S_n$ be the sequence of pipe labels read from northwest to southeast across the $k$-th diagonal (cells $(r, c)$ with $c - r = k$), padded on the right by the remaining south-boundary labels $(p(n+k+1), \dots, p(n))$ when $k < 0$ and on the left by the already-exited east-boundary labels $(q(1), \dots, q(k))$ when $k > 0$. At $k = -n$ (before any crossings), the sequence along the south boundary from west to east is the one-line notation $p = (p(1), \dots, p(n))$. For each $-n < k \le n - 1$, at every crossing tile $(r, c)$ on diagonal $k$, its west edge (the east edge of $(r, c-1)$) and south edge (the north edge of $(r+1, c)$) occupy adjacent positions $(\sigma, \sigma+1)$ in $\pi(E, p : k-1)$, where $\sigma = 1 + (\text{number of pipes strictly NW of }(r, c)\text{ on diagonal }k)$ is the corresponding letter of $\mathrm{word}(E)$; distinct crossings on the same diagonal act on disjoint adjacent pairs (differing in index by at least $2$) and therefore commute. When two adjacent pipes at positions $(\sigma, \sigma+1)$ with labels $(a, b)$ cross at a $\mathsf{P}$ tile, the Demazure rule places $\max(a, b)$ on the north edge (position $\sigma$) and $\min(a, b)$ on the east edge (position $\sigma+1$). In one-line notation, replacing $(a, b)$ at positions $(\sigma, \sigma+1)$ by $(\max(a, b), \min(a, b))$ is precisely the right Demazure product $\pi \mapsto \pi \circ s_\sigma$ (which swaps positions $\sigma, \sigma+1$ iff $\pi(\sigma) < \pi(\sigma+1)$). Iterating over all crossings in $\mathrm{word}(E) = (j_1, \dots, j_m)$ and using associativity of $\circ$, the final east boundary sequence (read top-to-bottom, i.e., northwest-to-southeast) is
$$\phi_E(p) = p \circ s_{j_1} \circ s_{j_2} \circ \dots \circ s_{j_m} = p \circ \mathrm{kpi}(E).$$

**(c)** By Proposition 3.19, $\mathrm{kpi}(\mathrm{double}(D)) = \mathrm{kpi}(D) \circ \mathrm{kpi}(D)^{-1} \in I_n$, so $D \in \mathsf{InvBPD}_K(y) \iff \mathrm{kpi}(\mathrm{double}(D)) = y$. Applying (a) and (b) to $p = \mathrm{id}$ gives $Z(\mathrm{id}, z; \mathbf{u}) = \widetilde{R}_z(\mathbf{u})$ for $z \in I_n$ and $0$ for $z \notin I_n$. Applying (a) and (b) to $p = s_i$ yields $\phi_{\mathrm{double}(D)}(s_i) = s_i \circ y$, giving (6). $\square$

---

## 3. Colored $R$-Matrices, Bulk Yang–Baxter Equations, and Diagonal Reflection Equation

### The $0$-Hecke Sorting Operator and Folded $R$-Matrices

For $k \ge 2$ and $1 \le j \le k - 1$, let $\sigma_j: [n]^k \to [n]^k$ be the **$0$-Hecke sorting map** replacing $(c_j, c_{j+1})$ by $(\max(c_j, c_{j+1}), \min(c_j, c_{j+1}))$ and fixing all other coordinates. These maps satisfy the $0$-Hecke monoid relations:
$$\sigma_j^2 = \sigma_j, \qquad \sigma_j \sigma_{j+1} \sigma_j = \sigma_{j+1} \sigma_j \sigma_{j+1}, \qquad \sigma_j \sigma_l = \sigma_l \sigma_j \quad (|j - l| \ge 2). \tag{7}$$
Write $\sigma := \sigma_1$ on $[n]^2$, $w_0^{(3)} := \sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2$ on $[n]^3$, and $w_0^{(4)} := \sigma_1 \sigma_2 \sigma_1 \sigma_3 \sigma_2 \sigma_1 = \sigma_3 \sigma_2 \sigma_1 \sigma_3 \sigma_2 \sigma_3$ on $[n]^4$.

Define the **horizontal folded $R$-matrix** $R(u_1, u_2; W_1, W_2; E_1, E_2) \in \mathbb{Z}[u_1, u_2]$ for $W_1, W_2, E_1, E_2 \in \mathcal{E}_n$ by:
- $(\varnothing, \varnothing; \varnothing, \varnothing) \mapsto u_2$;
- $(x, \varnothing; x, \varnothing) \mapsto u_2$ and $(x, \varnothing; \varnothing, x) \mapsto u_1 - u_2$ for all $x \in [n]^2$;
- $(\varnothing, x; \varnothing, x) \mapsto u_1$ for all $x \in [n]^2$;
- For occupied edges $W_1 = (a_1, b_1)$, $W_2 = (a_2, b_2)$, $E_1 = (a'_1, b'_1)$, $E_2 = (a'_2, b'_2) \in [n]^2$:
  $$R(u_1, u_2; W_1, W_2; E_1, E_2) := u_2\,\delta_{(a'_1, a'_2) = (a_1, a_2)}\,\delta_{(b_1, b_2) = (b'_1, b'_2)} + (u_1 - u_2)\,\delta_{(a'_1, a'_2) = \sigma(a_1, a_2)}\,\delta_{(b_1, b_2) = \sigma(b'_1, b'_2)}; \tag{8}$$
- $0$ for all other tuples.

*(Explicitly, on two occupied edges: if $a_1 \ge a_2$ and $b'_1 \ge b'_2$, both Kronecker deltas hold for $(a', b) = (a, b')$, summing to $u_2 + (u_1 - u_2) = u_1$; otherwise the two deltas are disjoint, giving $u_2$ on $(a, b')$ and $u_1 - u_2$ on $(\sigma(a), \sigma(b'))$.)*

Define the **vertical folded $R$-matrix** $R_V(u_1, u_2; N_1, N_2; S_1, S_2) \in \mathbb{Z}[u_1, u_2]$ via $\mathrm{flip}$:
$$R_V(u_1, u_2; N_1, N_2; S_1, S_2) := R\bigl(u_1, u_2; \mathrm{flip}(N_1), \mathrm{flip}(N_2); \mathrm{flip}(S_1), \mathrm{flip}(S_2)\bigr). \tag{9}$$
Unpacking (9) on empty/single-wire edges:
- $(\varnothing, \varnothing; \varnothing, \varnothing) \mapsto u_2$;
- $(x, \varnothing; x, \varnothing) \mapsto u_2$ and $(x, \varnothing; \varnothing, x) \mapsto u_1 - u_2$;
- $(\varnothing, x; \varnothing, x) \mapsto u_1$.
Unpacking (9) on two occupied edges $N_1 = (a_1, b_1)$, $N_2 = (a_2, b_2)$, $S_1 = (a'_1, b'_1)$, $S_2 = (a'_2, b'_2)$ (where $\mathrm{flip}(N_j) = (b_j, a_j)$ and $\mathrm{flip}(S_j) = (b'_j, a'_j)$):
$$R_V(u_1, u_2; N_1, N_2; S_1, S_2) = u_2\,\delta_{(a_1, a_2) = (a'_1, a'_2)}\,\delta_{(b'_1, b'_2) = (b_1, b_2)} + (u_1 - u_2)\,\delta_{(a_1, a_2) = \sigma(a'_1, a'_2)}\,\delta_{(b'_1, b'_2) = \sigma(b_1, b_2)}. \tag{10}$$
Notice the exact meaning of (10): the first coordinates enter from the south $(a'_1, a'_2)$ and exit to the north $(a_1, a_2)$, while the second coordinates enter from the north $(b_1, b_2)$ and exit to the south $(b'_1, b'_2)$; the sorting term applies $\sigma$ to **both** streams in the NW-to-SE order $(1, 2)$.

### Composition Semantics for $0$-Hecke Operators

In both Lemma 2 and Lemma 3 below, fix an uncolored occupancy pattern on the external edges and order the $k$ occupied edges in NW-to-SE order.
- In a **bulk** gadget (Lemma 2), each uncolored pair of tiles determines a pair of deterministic $0$-Hecke maps $(f^{(1)}, f^{(2)})$, where $f^{(1)}: [n]^k \to [n]^k$ maps the $k$ incoming first coordinates (at $\{W_1, W_2, S\}$) to the $k$ outgoing first coordinates (at $\{N, E_1, E_2\}$), and $f^{(2)}: [n]^k \to [n]^k$ maps the $k$ incoming second coordinates (at $\{N, E_1, E_2\}$) to the $k$ outgoing second coordinates (at $\{W_1, W_2, S\}$). Composing the sorting term of $R$ on the left (at occupied edges $W_1, W_2$, i.e., positions $(1, 2)$) with $(f^{(1)}, f^{(2)})$ sums over a **unique** intermediate state $m_{\mathrm{in}} = \sigma_1(a)$ and $m_{\mathrm{out}} = f^{(2)}(b')$, yielding the deterministic pair $(f^{(1)} \circ \sigma_1,\; \sigma_1 \circ f^{(2)})$. Similarly, composing $(f^{(1)}, f^{(2)})$ with the sorting term of $R$ on the right (at occupied edges $E_1, E_2$, i.e., positions $(k-1, k)$) yields $(\sigma_{k-1} \circ f^{(1)},\; f^{(2)} \circ \sigma_{k-1})$.
- In the **$2 \times 2$ diagonal triangle** (Lemma 3), each uncolored triple of tiles $(T_{11}, T_{21}, T_{22})$ determines a single deterministic $0$-Hecke map $f_T: [n]^k \to [n]^k$ taking the $k$ incoming colors (first coordinates of the occupied edges among $W_1, W_2, S_1, S_2$) to the $k$ outgoing colors (second coordinates of the same edges). By (8) and (10):
  - Composing the sorting term of $R$ on the left (when $W_1, W_2$ are occupied, positions $(1, 2)$) with $f_T$ sums over the unique intermediate state $m_{\mathrm{in}} = \sigma_1(a)$, $m_{\mathrm{out}} = f_T(\sigma_1(a))$, yielding the deterministic map $\sigma_1 \circ f_T \circ \sigma_1$.
  - Composing $f_T$ with the sorting term of $R_V$ on the bottom (when $S_1, S_2$ are occupied, positions $(k-1, k)$) sums over the unique intermediate state $n_{\mathrm{in}} = \sigma_{k-1}(a)$, $n_{\mathrm{out}} = f_T(\sigma_{k-1}(a))$, yielding the deterministic map $\sigma_{k-1} \circ f_T \circ \sigma_{k-1}$.

Because each Kronecker-delta indicator sums linearly (including when colors coincide, where identical outputs automatically add their scalar weights), equality of formal linear combinations of deterministic maps $(f^{(1)}, f^{(2)})$ or $f_T$ implies exact polynomial equality for **all** color assignments in $[n]$ (distinct or repeated) and **all** $n \ge 1$.

---

### Lemma 2 (Horizontal and Vertical Bulk Yang–Baxter Equations)
For all $W_1, W_2, S, E_1, E_2, N \in \mathcal{E}_n$, the **Horizontal Bulk Yang–Baxter Equation** holds identically in $\mathbb{Z}[u_1, u_2, v]$:
$$\sum_{m_1, m_2, c \in \mathcal{E}_n} R(u_1, u_2; W_1, W_2; m_1, m_2)\, W(u_1, v; m_1, c; E_1, N)\, W(u_2, v; m_2, S; E_2, c)$$
$$= \sum_{m_1, m_2, c \in \mathcal{E}_n} W(u_2, v; W_1, c; m_1, N)\, W(u_1, v; W_2, S; m_2, c)\, R(u_1, u_2; m_1, m_2; E_1, E_2). \tag{11}$$
Moreover, for all $N_1, N_2, W, S_1, S_2, E \in \mathcal{E}_n$, the **Vertical Bulk Yang–Baxter Equation** holds identically in $\mathbb{Z}[u_1, u_2, v]$:
$$\sum_{m_1, m_2, c \in \mathcal{E}_n} R_V(u_1, u_2; N_1, N_2; m_1, m_2)\, W(v, u_1; W, S_1; c, m_1)\, W(v, u_2; c, S_2; E, m_2)$$
$$= \sum_{m_1, m_2, c \in \mathcal{E}_n} W(v, u_2; W, m_1; c, N_1)\, W(v, u_1; c, m_2; E, N_2)\, R_V(u_1, u_2; m_1, m_2; S_1, S_2). \tag{12}$$

**Proof.**
We first prove (11). Every vertex $W$ and $R$ conserves the number of occupied wires, so both sides vanish unless the uncolored occupancy pattern $(w_1, w_2, s; e_1, e_2, n) \in \{0, 1\}^6$ satisfies $w_1 + w_2 + s = e_1 + e_2 + n =: k \in \{0, 1, 2, 3\}$. We check all $\sum_{k=0}^3 \binom{3}{k}^2 = 20$ patterns by $k$:

- **$k = 0$** (1 pattern: $(0,0,0) \to (0,0,0)$): Both sides have the unique configuration $(\mathsf{B}, \mathsf{B})$, giving $u_2(u_1 v - 1)(u_2 v - 1)$ on both sides.

- **$k = 1$** (9 patterns): A single wire with color pair $x \in [n]^2$ enters and exits unchanged without crossing any other wire, so both sides vanish unless the occupied incoming and outgoing edges carry the same $x$, in which case the weights depend only on the uncolored tiles. We list all $9$ patterns directly (writing `id` or `sw` for the $R$-transition and `(top tile, bottom tile)` for the column):
  1. $(0,0,1)\to(0,0,1)$: LHS $= [\text{id}:\mathsf{V},\mathsf{V}] = u_2$; RHS $= [\mathsf{V},\mathsf{V}:\text{id}] = u_2$.
  2. $(0,0,1)\to(0,1,0)$: LHS $= [\text{id}:\mathsf{B},\mathsf{C}] = u_2(u_1 v - 1)$; RHS $= [\mathsf{B},\mathsf{C}:\text{id}] + [\mathsf{C},\mathsf{V}:\text{sw}] = (u_2 v - 1) u_1 + (u_1 - u_2) = u_2(u_1 v - 1)$.
  3. $(0,0,1)\to(1,0,0)$: LHS $= [\text{id}:\mathsf{C},\mathsf{V}] = u_2$; RHS $= [\mathsf{C},\mathsf{V}:\text{id}] = u_2$.
  4. $(0,1,0)\to(0,0,1)$: LHS $= [\text{id}:\mathsf{V},\mathsf{J}] = u_1(u_2 v)$; RHS $= [\mathsf{V},\mathsf{J}:\text{id}] = (u_1 v) u_2$.
  5. $(0,1,0)\to(0,1,0)$: LHS $= [\text{id}:\mathsf{B},\mathsf{H}] = u_1(u_1 v - 1)$; RHS $= [\mathsf{B},\mathsf{H}:\text{id}] + [\mathsf{C},\mathsf{J}:\text{sw}] = (u_2 v - 1) u_1 + (u_1 v)(u_1 - u_2) = u_1(u_1 v - 1)$.
  6. $(0,1,0)\to(1,0,0)$: LHS $= [\text{id}:\mathsf{C},\mathsf{J}] = u_1(u_2 v)$; RHS $= [\mathsf{C},\mathsf{J}:\text{id}] = (u_1 v) u_2$.
  7. $(1,0,0)\to(0,0,1)$: LHS $= [\text{sw}:\mathsf{V},\mathsf{J}] + [\text{id}:\mathsf{J},\mathsf{B}] = (u_1 - u_2)(u_2 v) + u_2(u_1 v)(u_2 v - 1) = u_2^2 v(u_1 v - 1)$; RHS $= [\mathsf{J},\mathsf{B}:\text{id}] = (u_2 v)(u_1 v - 1) u_2$.
  8. $(1,0,0)\to(0,1,0)$: LHS $= [\text{sw}:\mathsf{B},\mathsf{H}] = (u_1 - u_2)(u_1 v - 1)$; RHS $= [\mathsf{H},\mathsf{B}:\text{sw}] = (u_1 v - 1)(u_1 - u_2)$.
  9. $(1,0,0)\to(1,0,0)$: LHS $= [\text{sw}:\mathsf{C},\mathsf{J}] + [\text{id}:\mathsf{H},\mathsf{B}] = (u_1 - u_2)(u_2 v) + u_2(u_2 v - 1) = u_2(u_1 v - 1)$; RHS $= [\mathsf{H},\mathsf{B}:\text{id}] = (u_1 v - 1) u_2$.

- **$k = 2$** (9 patterns): Write $\mathbf{I} := (\mathrm{id}, \mathrm{id})$ and $\mathbf{S} := (\sigma, \sigma)$ for the deterministic paired-color operators on the two wires (in NW-to-SE order). Since $\sigma^2 = \sigma$, composing $\mathbf{S}$ with $u_2 \mathbf{I} + (u_1 - u_2)\mathbf{S}$ on either side yields $u_2 \mathbf{S} + (u_1 - u_2)\mathbf{S} = u_1 \mathbf{S}$. Every tile pair without $\mathsf{P}$ acts as $\mathbf{I}$, while every tile pair containing one $\mathsf{P}$ acts as $\mathbf{S}$:
  1. $(0,1,1)\to(0,1,1)$: LHS $= u_1 \mathbf{S}$ (from $[\text{id}:\mathsf{V},\mathsf{P}]$); RHS $= u_1 \mathbf{S}$ (from $[\mathsf{V},\mathsf{P}:\text{id}]$).
  2. $(0,1,1)\to(1,0,1)$: $0 = 0$ (on LHS, $W_1 = 0, W_2 = 1$ forces $m_1 = 0, m_2 = 1$, and then $m_2 = S = 1$ forces the bottom tile to be $\mathsf{P}$ with $E_2 = 1$, contradicting $E_2 = 0$; on RHS, $W_2 = S = 1$ forces the bottom tile to be $\mathsf{P}$ with $c = m_2 = 1$, then $W_1 = 0, c = N = 1$ forces the top tile to be $\mathsf{V}$ with $m_1 = 0$, giving $R(u_1, u_2; \varnothing, x; y, \varnothing) = 0$).
  3. $(0,1,1)\to(1,1,0)$: LHS $= u_1 \mathbf{S}$ (from $[\text{id}:\mathsf{C},\mathsf{P}]$); RHS $= \mathbf{S}\cdot(u_2 \mathbf{I} + (u_1 - u_2)\mathbf{S}) = u_1 \mathbf{S}$ (from $[\mathsf{C},\mathsf{P}]$ followed by $R$).
  4. $(1,0,1)\to(0,1,1)$: LHS $= (u_1 - u_2)\mathbf{S} + u_2(u_1 v)\mathbf{I}$ (from $[\text{sw}:\mathsf{V},\mathsf{P}] + [\text{id}:\mathsf{J},\mathsf{C}]$); RHS $= (u_2 v)\mathbf{I}\cdot u_1 + \mathbf{S}(u_1 - u_2)$ (from $[\mathsf{J},\mathsf{C}:\text{id}] + [\mathsf{P},\mathsf{V}:\text{sw}]$).
  5. $(1,0,1)\to(1,0,1)$: LHS $= u_2 \mathbf{S}$ (from $[\text{id}:\mathsf{P},\mathsf{V}]$); RHS $= u_2 \mathbf{S}$ (from $[\mathsf{P},\mathsf{V}:\text{id}]$).
  6. $(1,0,1)\to(1,1,0)$: LHS $= (u_1 - u_2)\mathbf{S} + u_2 \mathbf{I}$ (from $[\text{sw}:\mathsf{C},\mathsf{P}] + [\text{id}:\mathsf{H},\mathsf{C}]$); RHS $= \mathbf{I}\cdot(u_2 \mathbf{I} + (u_1 - u_2)\mathbf{S})$ (from $[\mathsf{H},\mathsf{C}]$ followed by $R$).
  7. $(1,1,0)\to(0,1,1)$: LHS $= (u_2 \mathbf{I} + (u_1 - u_2)\mathbf{S})\cdot (u_1 v)\mathbf{I} = u_1 u_2 v \mathbf{I} + u_1 v(u_1 - u_2)\mathbf{S}$ (from $R$ followed by $[\mathsf{J},\mathsf{H}]$); RHS $= (u_2 v)\mathbf{I}\cdot u_1 + (u_1 v)\mathbf{S}\cdot(u_1 - u_2)$ (from $[\mathsf{J},\mathsf{H}:\text{id}] + [\mathsf{P},\mathsf{J}:\text{sw}]$).
  8. $(1,1,0)\to(1,0,1)$: LHS $= (u_2 \mathbf{I} + (u_1 - u_2)\mathbf{S})\cdot (u_2 v)\mathbf{S} = u_1 u_2 v \mathbf{S}$ (from $R$ followed by $[\mathsf{P},\mathsf{J}]$); RHS $= (u_1 v)\mathbf{S}\cdot u_2 = u_1 u_2 v \mathbf{S}$ (from $[\mathsf{P},\mathsf{J}:\text{id}]$).
  9. $(1,1,0)\to(1,1,0)$: LHS $= (u_2 \mathbf{I} + (u_1 - u_2)\mathbf{S})\cdot\mathbf{I}$; RHS $= \mathbf{I}\cdot(u_2 \mathbf{I} + (u_1 - u_2)\mathbf{S})$.

- **$k = 3$** (1 pattern: $(1,1,1) \to (1,1,1)$): Both tiles must be $\mathsf{P}$ (weight $1$). Ordering the $3$ wires NW-to-SE as $(W_1, W_2, S)$ on input and $(N, E_1, E_2)$ on output:
  - In the first coordinate (flowing W,S $\to$ N,E), the bottom $\mathsf{P}$ applies $\sigma_2$ (on $(W_2, S)$) and then the top $\mathsf{P}$ applies $\sigma_1$ (on $(W_1, c)$), giving $f^{(1)} = \sigma_1 \sigma_2$.
  - In the second coordinate (flowing N,E $\to$ W,S), the top $\mathsf{P}$ applies $\sigma_1$ (on $(N, E_1)$) and then the bottom $\mathsf{P}$ applies $\sigma_2$ (on $(c, E_2)$), giving $f^{(2)} = \sigma_2 \sigma_1$.
  - On the LHS, $R$ acts on $(W_1, W_2)$ (positions $(1, 2)$), yielding
    $$u_2(\sigma_1 \sigma_2,\, \sigma_2 \sigma_1) + (u_1 - u_2)(\sigma_1 \sigma_2 \sigma_1,\, \sigma_1 \sigma_2 \sigma_1).$$
  - On the RHS, $R$ acts on $(E_1, E_2)$ (positions $(2, 3)$), yielding
    $$u_2(\sigma_1 \sigma_2,\, \sigma_2 \sigma_1) + (u_1 - u_2)(\sigma_2 \sigma_1 \sigma_2,\, \sigma_2 \sigma_1 \sigma_2).$$
  By the $0$-Hecke braid relation $\sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2$, LHS $=$ RHS.

This completes the proof of (11). To deduce (12), substitute $(W_1, W_2, S, E_1, E_2, N) = (\mathrm{flip}(N_1), \mathrm{flip}(N_2), \mathrm{flip}(E), \mathrm{flip}(S_1), \mathrm{flip}(S_2), \mathrm{flip}(W))$ and reindex the summation variables $(m_1, m_2, c) \mapsto (\mathrm{flip}(m_1), \mathrm{flip}(m_2), \mathrm{flip}(c))$ in (11), then apply the transpose identity (5) and definition (9); the result is verbatim (12). $\square$

---

### Lemma 3 ($2 \times 2$ Diagonal Reflection Equation)
Define the partition function of the $2 \times 2$ diagonal triangle $\{(1,1), (2,1), (2,2)\}$ with parameters $(u_1, u_2)$ and external edges $W_1, W_2, S_1, S_2 \in \mathcal{E}_n$ by
$$T(u_1, u_2; W_1, W_2, S_1, S_2) := \sum_{c, d \in \mathcal{E}_n} K(u_1; W_1, c)\, W(u_2, u_1; W_2, S_1; d, c)\, K(u_2; d, S_2).$$
Then for all $W_1, W_2, S_1, S_2 \in \mathcal{E}_n$, the **Diagonal Reflection Equation** holds identically in $\mathbb{Z}[u_1, u_2]$:
$$\sum_{m_1, m_2 \in \mathcal{E}_n} R(u_1, u_2; W_1, W_2; m_1, m_2)\, T(u_1, u_2; m_1, m_2, S_1, S_2)$$
$$= \sum_{n_1, n_2 \in \mathcal{E}_n} T(u_2, u_1; W_1, W_2, n_1, n_2)\, R_V(u_1, u_2; n_1, n_2; S_1, S_2). \tag{13}$$

**Proof.**
Let $(w_1, w_2, s_1, s_2) \in \{0, 1\}^4$ be the uncolored occupancy pattern of $(W_1, W_2, S_1, S_2)$, with $k = w_1 + w_2 + s_1 + s_2 \in \{0, 1, 2, 3, 4\}$. In each configuration $(T_{11}, T_{21}, T_{22})$ of the triangle, every diagonal crossing $\mathsf{P}_{\mathrm{diag}}$ and bulk crossing $\mathsf{P}$ sorts its two wires in NW-to-SE order by the corresponding generator $\sigma_j$. We check all $16$ patterns by $k$:

- **$k = 0$** (1 pattern: $(0,0,0,0)$): Only $(\mathsf{B}_{\mathrm{diag}}, \mathsf{B}, \mathsf{B}_{\mathrm{diag}})$ contributes, giving $T(u_1, u_2; 0,0,0,0) = (u_1 - 1)(u_1 u_2 - 1)(u_2 - 1)$, which is symmetric in $(u_1, u_2)$. Both LHS and RHS equal $u_2 (u_1 - 1)(u_2 - 1)(u_1 u_2 - 1)$.

- **$k = 1$** (4 patterns): A single wire enters and reflects back to itself, so both sides vanish unless the occupied edge has equal incoming and outgoing color $(a, a)$, in which case the weights are purely uncolored:
  - $T(u_1, u_2; 0,0,0,1) = (\mathsf{B},\mathsf{B},\mathsf{C}) = (u_1 - 1)(u_1 u_2 - 1)$.
  - $T(u_1, u_2; 0,0,1,0) = (\mathsf{B},\mathsf{C},\mathsf{J}) + (\mathsf{C},\mathsf{V},\mathsf{B}) = (u_1 - 1)u_2 + (u_2 - 1) = u_1 u_2 - 1$.
  - $T(u_1, u_2; 0,1,0,0) = (\mathsf{B},\mathsf{H},\mathsf{J}) + (\mathsf{C},\mathsf{J},\mathsf{B}) = (u_1 - 1)u_2 + u_1 u_2(u_2 - 1) = u_2(u_1 u_2 - 1)$.
  - $T(u_1, u_2; 1,0,0,0) = (\mathsf{J},\mathsf{B},\mathsf{B}) = u_1(u_1 u_2 - 1)(u_2 - 1)$.

  Verifying all four cases of (13):
  1. $(0,0,0,1)$: LHS $= u_2(u_1 - 1)(u_1 u_2 - 1)$; RHS $= (u_2 - 1)(u_1 u_2 - 1) u_1 + (u_1 u_2 - 1)(u_1 - u_2) = (u_1 u_2 - 1)(u_1 u_2 - u_2) = \text{LHS}$.
  2. $(0,0,1,0)$: LHS $= u_2(u_1 u_2 - 1)$; RHS $= (u_1 u_2 - 1) u_2$.
  3. $(0,1,0,0)$: LHS $= u_1 \cdot u_2(u_1 u_2 - 1)$; RHS $= u_1(u_1 u_2 - 1) \cdot u_2$.
  4. $(1,0,0,0)$: LHS $= u_2 \cdot u_1(u_1 u_2 - 1)(u_2 - 1) + (u_1 - u_2)\cdot u_2(u_1 u_2 - 1) = u_2(u_1 u_2 - 1)(u_1 u_2 - u_2) = u_2^2(u_1 - 1)(u_1 u_2 - 1)$; RHS $= u_2(u_1 u_2 - 1)(u_1 - 1) \cdot u_2 = \text{LHS}$.

- **$k = 2$** (6 patterns): On two wires, every triangle configuration defines either $\mathrm{id}$ or $\sigma$ (with $\sigma^2 = \sigma$). Acting on a map $f \in \{\mathrm{id}, \sigma\}$ by $u_2\,\mathrm{id} + (u_1 - u_2)(\sigma \circ (-) \circ \sigma)$ sends $\mathrm{id} \mapsto u_2\,\mathrm{id} + (u_1 - u_2)\sigma$ and $\sigma \mapsto u_1 \sigma$. Computing $T(u_1, u_2)$ for all six patterns:
  - $T(u_1, u_2; 0,0,1,1) = (\mathsf{C},\mathsf{V},\mathsf{C}) + (\mathsf{B},\mathsf{C},\mathsf{P}) = \mathrm{id} + (u_1 - 1)\sigma$.
  - $T(u_1, u_2; 0,1,0,1) = (\mathsf{C},\mathsf{J},\mathsf{C}) + (\mathsf{B},\mathsf{H},\mathsf{P}) = u_1 u_2\,\mathrm{id} + (u_1 - 1)\sigma$.
  - $T(u_1, u_2; 0,1,1,0) = (\mathsf{C},\mathsf{P},\mathsf{J}) = u_2\sigma$ (note $(\mathsf{P})$ forward and backward gives $\sigma \circ \sigma = \sigma$).
  - $T(u_1, u_2; 1,0,0,1) = (\mathsf{J},\mathsf{B},\mathsf{C}) = u_1(u_1 u_2 - 1)\,\mathrm{id}$.
  - $T(u_1, u_2; 1,0,1,0) = (\mathsf{J},\mathsf{C},\mathsf{J}) + (\mathsf{P},\mathsf{V},\mathsf{B}) = u_1 u_2\,\mathrm{id} + (u_2 - 1)\sigma$.
  - $T(u_1, u_2; 1,1,0,0) = (\mathsf{J},\mathsf{H},\mathsf{J}) + (\mathsf{P},\mathsf{J},\mathsf{B}) = u_1 u_2\,\mathrm{id} + u_1 u_2(u_2 - 1)\sigma$.

  Verifying all six cases of (13):
  1. $(0,0,1,1)$: LHS $= u_2(\mathrm{id} + (u_1 - 1)\sigma)$; RHS $= u_2(\mathrm{id} + (u_2 - 1)\sigma) + (u_1 - u_2)(\sigma + (u_2 - 1)\sigma) = u_2\,\mathrm{id} + (u_2(u_2 - 1) + u_2(u_1 - u_2))\sigma = \text{LHS}$.
  2. $(0,1,0,1)$: LHS $= u_1(u_1 u_2\,\mathrm{id} + (u_1 - 1)\sigma)$; RHS $= (u_1 u_2\,\mathrm{id} + (u_2 - 1)\sigma) u_1 + (u_1 \sigma)(u_1 - u_2) = u_1^2 u_2\,\mathrm{id} + u_1(u_1 - 1)\sigma = \text{LHS}$.
  3. $(0,1,1,0)$: LHS $= u_1(u_2 \sigma)$; RHS $= (u_1 \sigma) u_2$.
  4. $(1,0,0,1)$: LHS $= u_2 \cdot u_1(u_1 u_2 - 1)\,\mathrm{id} + (u_1 - u_2)(u_1 u_2\,\mathrm{id} + (u_1 - 1)\sigma)$; RHS $= u_2(u_1 u_2 - 1)\,\mathrm{id} \cdot u_1 + (u_1 u_2\,\mathrm{id} + (u_1 - 1)\sigma)(u_1 - u_2) = \text{LHS}$.
  5. $(1,0,1,0)$: LHS $= u_2(u_1 u_2\,\mathrm{id} + (u_2 - 1)\sigma) + (u_1 - u_2)(u_2 \sigma) = u_1 u_2^2\,\mathrm{id} + u_2(u_1 - 1)\sigma$; RHS $= (u_1 u_2\,\mathrm{id} + (u_1 - 1)\sigma) u_2 = \text{LHS}$.
  6. $(1,1,0,0)$: LHS $= u_2 u_1 u_2(\mathrm{id} + (u_2 - 1)\sigma) + (u_1 - u_2) u_1 u_2(\sigma + (u_2 - 1)\sigma) = u_1 u_2^2(\mathrm{id} + (u_1 - 1)\sigma)$; RHS $= u_1 u_2(\mathrm{id} + (u_1 - 1)\sigma) \cdot u_2 = \text{LHS}$.

- **$k = 3$** (4 patterns): Ordering the three occupied wires NW-to-SE as $1, 2, 3$, we have $\sigma_1 \sigma_2 \sigma_1 = \sigma_2 \sigma_1 \sigma_2 = w_0^{(3)}$ and $\sigma_j w_0^{(3)} \sigma_j = w_0^{(3)}$ for $j \in \{1, 2\}$. Computing $T(u_1, u_2)$:
  - $T(u_1, u_2; 0,1,1,1) = (\mathsf{C},\mathsf{P},\mathsf{P})$: bulk $\mathsf{P}$ on $(W_2, S_1)$ applies $\sigma_1$ before and after $\mathsf{P}_{\mathrm{diag}}$ on $(2, 3)$ ($\sigma_2$), giving $\sigma_1 \sigma_2 \sigma_1 = w_0^{(3)}$.
  - $T(u_1, u_2; 1,0,1,1) = (\mathsf{P},\mathsf{V},\mathsf{C}) + (\mathsf{J},\mathsf{C},\mathsf{P}) = \sigma_1 + u_1 \sigma_2$.
  - $T(u_1, u_2; 1,1,0,1) = (\mathsf{P},\mathsf{J},\mathsf{C}) + (\mathsf{J},\mathsf{H},\mathsf{P}) = u_1 u_2 \sigma_1 + u_1 \sigma_2$.
  - $T(u_1, u_2; 1,1,1,0) = (\mathsf{P},\mathsf{P},\mathsf{J})$: bulk $\mathsf{P}$ on $(W_2, S_1)$ applies $\sigma_2$ before and after $\mathsf{P}_{\mathrm{diag}}$ on $(1, 2)$ ($\sigma_1$), with weight $u_2$ from $\mathsf{J}_{\mathrm{diag}}$, giving $u_2 \sigma_2 \sigma_1 \sigma_2 = u_2 w_0^{(3)}$.

  Verifying all four cases of (13):
  1. $(0,1,1,1)$: LHS $= u_1 w_0^{(3)}$; RHS $= u_2 w_0^{(3)} + (u_1 - u_2)(\sigma_2 w_0^{(3)} \sigma_2) = u_1 w_0^{(3)}$.
  2. $(1,0,1,1)$: LHS $= u_2(\sigma_1 + u_1 \sigma_2) + (u_1 - u_2) w_0^{(3)} = u_2 \sigma_1 + u_1 u_2 \sigma_2 + (u_1 - u_2) w_0^{(3)}$; RHS $= u_2(\sigma_1 + u_2 \sigma_2) + (u_1 - u_2)(\sigma_2 \sigma_1 \sigma_2 + u_2 \sigma_2) = u_2 \sigma_1 + u_1 u_2 \sigma_2 + (u_1 - u_2) w_0^{(3)} = \text{LHS}$.
  3. $(1,1,0,1)$: LHS $= u_2(u_1 u_2 \sigma_1 + u_1 \sigma_2) + (u_1 - u_2)(u_1 u_2 \sigma_1 + u_1 \sigma_1 \sigma_2 \sigma_1) = u_1^2 u_2 \sigma_1 + u_1 u_2 \sigma_2 + u_1(u_1 - u_2) w_0^{(3)}$; RHS $= (u_1 u_2 \sigma_1 + u_2 \sigma_2) u_1 + (u_1 w_0^{(3)})(u_1 - u_2) = \text{LHS}$.
  4. $(1,1,1,0)$: LHS $= u_2(u_2 w_0^{(3)}) + (u_1 - u_2)(u_2 \sigma_1 w_0^{(3)} \sigma_1) = u_1 u_2 w_0^{(3)}$; RHS $= (u_1 w_0^{(3)}) u_2 = \text{LHS}$.

- **$k = 4$** (1 pattern: $(1,1,1,1)$): Since $W_2$ and $S_1$ are both occupied, $(2, 1)$ must be $\mathsf{P}$, forcing $c$ and $d$ to be occupied and hence all three tiles to be $(\mathsf{P}_{\mathrm{diag}}, \mathsf{P}, \mathsf{P}_{\mathrm{diag}})$ of weight $1$. In NW-to-SE order $(W_1, W_2, S_1, S_2) = (1, 2, 3, 4)$, the forward pass through $\mathsf{P}$ at $(2, 1)$ applies $\sigma_2$, the two diagonal crossings at $(1, 1)$ and $(2, 2)$ apply $\sigma_1$ and $\sigma_3$ (which commute), and the backward pass through $\mathsf{P}$ at $(2, 1)$ applies $\sigma_2$, yielding the single $0$-Hecke map
  $$f_T = \sigma_2 \sigma_1 \sigma_3 \sigma_2.$$
  By the $0$-Hecke relations (7),
  $$\sigma_1 f_T \sigma_1 = (\sigma_1 \sigma_2 \sigma_1)\sigma_3 \sigma_2 \sigma_1 = w_0^{(4)} = \sigma_3 \sigma_2 \sigma_1 (\sigma_3 \sigma_2 \sigma_3) = \sigma_3 f_T \sigma_3.$$
  Therefore LHS $= u_2 f_T + (u_1 - u_2)(\sigma_1 f_T \sigma_1) = u_2 f_T + (u_1 - u_2) w_0^{(4)} = u_2 f_T + (u_1 - u_2)(\sigma_3 f_T \sigma_3) =$ RHS. $\square$

---

## 4. The Train Argument and Divided-Difference Recurrence

### Lemma 4 (Isobaric Divided-Difference Recurrence for $R_z$)
Let $n \ge 2$, $i \in [n-1]$, and $z \in I_n$.
1. **(a)** If $z(i) < z(i+1)$, then $\widetilde{R}_z(s_i \mathbf{u}) = \widetilde{R}_z(\mathbf{u})$.
2. **(b)** If $z(i) < z(i+1)$ and $z' := s_i \circ z \circ s_i$, then $\overline{\partial}_i R_{z'} = R_z$.

**Proof.**
Fix any $w \in I_n$ and consider the folded lattice model on $\mathrm{LT}_n$ with empty west boundary and south boundary $\mathbf{b}(w) := ((1, w(1)), \dots, (n, w(n)))$. Attach the horizontal $R$-matrix $R(u_i, u_{i+1})$ to the west boundary edges of rows $i$ and $i+1$. Since both west boundary edges are $\varnothing$, the only nonzero entry is $R(u_i, u_{i+1}; \varnothing, \varnothing; \varnothing, \varnothing) = u_{i+1}$, so the partition function of the augmented grid equals $u_{i+1} Z(\mathrm{id}, w; \mathbf{u}) = u_{i+1} \widetilde{R}_w(\mathbf{u})$ by Lemma 1(c).

Now push $R(u_i, u_{i+1})$ across $\mathrm{LT}_n$ in three stages:
1. Push $R(u_i, u_{i+1})$ rightward across columns $1, 2, \dots, i - 1$ by repeated applications of the Horizontal Bulk Yang–Baxter Equation (Lemma 2, eq. (11)); this swaps $u_i \leftrightarrow u_{i+1}$ on rows $i$ and $i+1$ in columns $1, \dots, i-1$.
2. Push $R(u_i, u_{i+1})$ across the $2 \times 2$ diagonal triangle $\{(i,i), (i+1,i), (i+1,i+1)\}$ by the Diagonal Reflection Equation (Lemma 3, eq. (13)); this swaps $u_i \leftrightarrow u_{i+1}$ on the triangle and converts $R(u_i, u_{i+1})$ into $R_V(u_i, u_{i+1})$ on the south edges of cells $(i+1, i)$ and $(i+1, i+1)$.
3. Push $R_V(u_i, u_{i+1})$ downward across rows $i+2, \dots, n$ by repeated applications of the Vertical Bulk Yang–Baxter Equation (Lemma 2, eq. (12)); this swaps $u_i \leftrightarrow u_{i+1}$ on columns $i$ and $i+1$ in rows $i+2, \dots, n$.

After all three stages, $u_i$ and $u_{i+1}$ have been interchanged everywhere in $\mathrm{LT}_n$, and $R_V(u_i, u_{i+1})$ exits at the south boundary columns $i, i+1$. Hence we obtain the exact identity in $\mathbb{Z}[u_1, \dots, u_n]$:
$$u_{i+1} \widetilde{R}_w(\mathbf{u}) = \sum_{n_1, n_2 \in \mathcal{E}_n} Z\bigl(\mathbf{b}(w)[i \leftarrow n_1,\, i+1 \leftarrow n_2];\, s_i \mathbf{u}\bigr)\, R_V\bigl(u_i, u_{i+1};\, n_1, n_2;\, (i, w(i)), (i+1, w(i+1))\bigr), \tag{14}$$
where $\mathbf{b}(w)[i \leftarrow n_1,\, i+1 \leftarrow n_2]$ denotes the south boundary $\mathbf{b}(w)$ with positions $i, i+1$ replaced by $n_1, n_2$.

Evaluate the $R_V$ factor in (14) directly using (10) with $(a'_1, a'_2) = (i, i+1)$ and $(b'_1, b'_2) = (w(i), w(i+1))$:
- Since $a'_1 = i < i+1 = a'_2$, we have $\sigma(a'_1, a'_2) = (i+1, i) \neq (a'_1, a'_2)$.
- The $u_{i+1}$ (identity) term occurs uniquely at $n_1 = (i, w(i)),\; n_2 = (i+1, w(i+1))$, contributing $u_{i+1} Z(\mathrm{id}, w; s_i \mathbf{u}) = u_{i+1} \widetilde{R}_w(s_i \mathbf{u})$.
- The $(u_i - u_{i+1})$ (sorting) term requires $(a_1, a_2) = \sigma(i, i+1) = (i+1, i)$ **and** $(w(i), w(i+1)) = \sigma(b_1, b_2)$, which holds if and only if **$w(i) > w(i+1)$** and $(b_1, b_2) \in \{(w(i), w(i+1)),\; (w(i+1), w(i))\}$.

We now analyze the two cases:

- **Case 1 ($w(i) < w(i+1)$):** The sorting term vanishes identically, so (14) reduces to $u_{i+1} \widetilde{R}_w(\mathbf{u}) = u_{i+1} \widetilde{R}_w(s_i \mathbf{u})$. Canceling the nonzero polynomial $u_{i+1}$ in the integral domain $\mathbb{Z}[u_1, \dots, u_n]$ gives $\widetilde{R}_w(s_i \mathbf{u}) = \widetilde{R}_w(\mathbf{u})$, proving **(a)**.

- **Case 2 ($w(i) > w(i+1)$):** The two pairs $(b_1, b_2) = (w(i), w(i+1))$ and $(w(i+1), w(i))$ give the two south boundaries corresponding to $(s_i, w)$ and $(s_i, w s_i)$, respectively. By Lemma 1(c) (eq. (6)), (14) becomes
  $$u_{i+1} \widetilde{R}_w(\mathbf{u}) = u_{i+1} \widetilde{R}_w(s_i \mathbf{u}) + (u_i - u_{i+1})\left(\sum_{y \in F_1} \widetilde{R}_y(s_i \mathbf{u}) + \sum_{y \in F_2} \widetilde{R}_y(s_i \mathbf{u})\right), \tag{15}$$
  where $F_1 := \{y \in I_n : s_i \circ y = w\}$ and $F_2 := \{y \in I_n : s_i \circ y = w s_i\}$.

  We determine $F_1$ and $F_2$ explicitly for any $w \in I_n$ with $w(i) > w(i+1)$. For any $y \in I_n$, $s_i \circ y = y$ if $y(i) > y(i+1)$ (since $y^{-1} = y$), and $s_i \circ y = s_i y$ if $y(i) < y(i+1)$; in particular, every element $v = s_i \circ y$ satisfies $\ell(s_i v) < \ell(v)$ (equivalently, $i+1$ precedes $i$ in the one-line notation of $v$).
  - **Subcase 2a ($w(i) = i+1$ and $w(i+1) = i$, i.e., $s_i w s_i = w$):** Set $y_0 := s_i w = w s_i \in I_n$. Then $y_0(i) = i < i+1 = y_0(i+1)$, so $s_i \circ y_0 = s_i y_0 = w$, $s_i \circ y_0 \circ s_i = w$, and $\ell_{\mathrm{inv}}(w) = \ell_{\mathrm{inv}}(y_0) + 1$. Thus $F_1 = \{w, y_0\}$. Meanwhile $w s_i = y_0$ has $i$ preceding $i+1$ in one-line notation, so $\ell(s_i(w s_i)) > \ell(w s_i)$ and hence $F_2 = \varnothing$.
  - **Subcase 2b ($w(i) > w(i+1)$ and $w(i) \neq i+1$, i.e., $s_i w s_i \neq w$):** Since $w$ is an involution and $w(i) \neq i+1$, we also have $w(i+1) \neq i$. Thus $s_i w \neq w s_i$, so neither $s_i w$ nor $w s_i$ is an involution (as $(s_i w)^{-1} = w s_i$). Set $y_0 := s_i w s_i \in I_n$. Checking all three possibilities for $\{w(i), w(i+1)\} \cap \{i, i+1\}$:
    - if $w(i) = i$, then $w(i+1) < i$, so $s_i(w(i)) = i+1 > w(i+1) = s_i(w(i+1))$;
    - if $w(i+1) = i+1$, then $w(i) > i+1$, so $s_i(w(i)) = w(i) > i = s_i(w(i+1))$;
    - if $\{w(i), w(i+1)\} \cap \{i, i+1\} = \varnothing$, then $s_i(w(i)) = w(i) > w(i+1) = s_i(w(i+1))$.
    In all cases, $y_0(i) = s_i(w(i+1)) < s_i(w(i)) = y_0(i+1)$, so $s_i \circ y_0 = s_i y_0 = w s_i$, $s_i \circ y_0 \circ s_i = w$, and $\ell_{\mathrm{inv}}(w) = \ell_{\mathrm{inv}}(y_0) + 1$. Since $s_i w \notin I_n$ we have $F_1 = \{w\}$, and since $w s_i \notin I_n$ and $s_i y = w s_i \iff y = y_0$, we have $F_2 = \{y_0\}$.

  In both subcases, $F_1 \cap F_2 = \varnothing$ and $F_1 \sqcup F_2 = \{w, y_0\}$, where $y_0 \in I_n$ is the unique involution with $y_0(i) < y_0(i+1)$ and $s_i \circ y_0 \circ s_i = w$. Substituting into (15) and using part **(a)** for $y_0$ ($\widetilde{R}_{y_0}(s_i \mathbf{u}) = \widetilde{R}_{y_0}(\mathbf{u})$) gives
  $$u_{i+1} \widetilde{R}_w(\mathbf{u}) = u_{i+1} \widetilde{R}_w(s_i \mathbf{u}) + (u_i - u_{i+1})\bigl(\widetilde{R}_w(s_i \mathbf{u}) + \widetilde{R}_{y_0}(\mathbf{u})\bigr) = u_i \widetilde{R}_w(s_i \mathbf{u}) + (u_i - u_{i+1}) \widetilde{R}_{y_0}(\mathbf{u}),$$
  and therefore
  $$u_{i+1} \widetilde{R}_w(\mathbf{u}) - u_i \widetilde{R}_w(s_i \mathbf{u}) = (u_i - u_{i+1}) \widetilde{R}_{y_0}(\mathbf{u}). \tag{16}$$

Now let $z \in I_n$ have $z(i) < z(i+1)$ and set $z' := s_i \circ z \circ s_i$. By (1), if $z(i) = i, z(i+1) = i+1$ then $z' = s_i z$ has $z'(i) = i+1 > i = z'(i+1)$ (Subcase 2a, with $y_0 = s_i z' = z$); otherwise $s_i z s_i \neq z$ and $z(i) \neq i+1, z(i+1) \neq i$ (as $z \in I_n$ and $z(i) < z(i+1)$), so $z' = s_i z s_i$ satisfies $z'(i) = s_i(z(i+1)) > s_i(z(i)) = z'(i+1)$ and $z'(i) \neq i+1$ (Subcase 2b, with $y_0 = s_i z' s_i = z$). In both cases $\ell_{\mathrm{inv}}(z') = \ell_{\mathrm{inv}}(z) + 1$. Substituting $u_j = 1 + \beta x_j$ into (16) for $w = z'$ and noting the identity
$$u_{i+1} f - u_i (s_i f) = (1 + \beta x_{i+1}) f - (1 + \beta x_i)(s_i f) = (1 + \beta x_i)(f - s_i f) - \beta(x_i - x_{i+1}) f = (x_i - x_{i+1})\,\overline{\partial}_i f,$$
together with $u_i - u_{i+1} = \beta(x_i - x_{i+1})$ and (4), we obtain in $\mathbb{Z}[\beta, x_1, \dots, x_n]$:
$$(x_i - x_{i+1})\,\beta^{\ell_{\mathrm{inv}}(z')}\,\overline{\partial}_i R_{z'} = \beta(x_i - x_{i+1})\,\beta^{\ell_{\mathrm{inv}}(z)}\, R_z = (x_i - x_{i+1})\,\beta^{\ell_{\mathrm{inv}}(z')}\, R_z.$$
Dividing by the nonzero factor $(x_i - x_{i+1})\beta^{\ell_{\mathrm{inv}}(z')}$ in the integral domain $\mathbb{Z}[\beta, x_1, \dots, x_n]$ yields $\overline{\partial}_i R_{z'} = R_z$, proving **(b)**. $\square$

---

## 5. Base Case $w_0^{(n)}$ and Completion of the Proof

### Lemma 5 (Uniqueness of $\mathsf{InvBPD}_K(w_0^{(n)})$)
For every $n \ge 1$, the set $\mathsf{InvBPD}_K(w_0^{(n)})$ consists of a single diagram $D_0$, whose blank set is $\mathrm{iD}(w_0^{(n)}) = \{(i, j) \in \mathrm{LT}_n : i + j \le n\}$ and whose upturn set is empty. Consequently,
$$R_{w_0^{(n)}} = \prod_{(i,j) \in \mathrm{iD}(w_0^{(n)})} x_{i\oplus j} = \widehat{\mathfrak{G}}^{(\beta)}_{w_0^{(n)}}.$$

**Proof.**
By Proposition 3.19, it suffices to show that the symmetric square bumpless pipe dream $E_0 := \mathrm{double}(D_0)$—defined by $E_0(i, j) = \mathsf{B}$ for $i + j \le n$, $\mathsf{C}$ for $i + j = n + 1$, and $\mathsf{P}$ for $i + j > n + 1$—is the unique element of $\mathsf{BPD}_K(w_0^{(n)})$.

Let $E \in \mathsf{BPD}_K(w_0^{(n)})$, with south boundary labeled $1, \dots, n$ from west to east and east boundary labeled $w_0^{(n)} = (n, n-1, \dots, 1)$ from north to south under Demazure propagation. We prove by downward induction on $k = n, n-1, \dots, 1$ that in column $k$:
- cell $(n + 1 - k, k)$ is $\mathsf{C}$;
- every cell $(r, k)$ with $r > n + 1 - k$ has a vertical segment carrying pipe $k$ northward (hence is $\mathsf{V}$ or $\mathsf{P}$);
- every cell $(n + 1 - k, j)$ with $j > k$ is $\mathsf{P}$ carrying pipe $k$ straight eastward to row $n + 1 - k$ on the east boundary;
- every cell $(r, k)$ with $r < n + 1 - k$ is $\mathsf{B}$ (blank).

Assume this holds for all columns $j > k$ (vacuously true when $k = n$). Follow the unique pipe of label $k$, which enters from the south at $(n, k)$:
1. Whenever pipe $k$ travels northward in column $k$ and encounters a pipe entering from the west at a crossing $\mathsf{P}$, the westward pipe passes through columns $1, \dots, k-1$; since pipes in a bumpless pipe dream move only north and east, every wire passing through columns $1, \dots, k-1$ originated at a south-boundary column $c < k$ and therefore carries a label $< k$. Under the Demazure rule, $\max(< k,\, k) = k$ exits **north**, so pipe $k$ cannot be deflected eastward by any crossing in column $k$; it can leave column $k$ eastward only at a $\mathsf{C}$ tile $(r, k)$.
2. If pipe $k$ turned east at $(r, k)$ with $r > n + 1 - k$, then for every column $j \in \{k+1, \dots, n\}$ we have $r > n + 1 - k > n + 1 - j$, so by the inductive hypothesis cell $(r, j)$ carries vertical pipe $j > k$. Hence $(r, j)$ must be a crossing $\mathsf{P}$, where $\min(k, j) = k$ continues **straight east** into column $j + 1$. Thus pipe $k$ would exit the east boundary at row $r > n + 1 - k$, contradicting $\mathrm{kpi}(E)(n + 1 - k) = k$.
3. If pipe $k$ continued northward past row $n + 1 - k$ into row $r' < n + 1 - k$, then because wires in a bumpless pipe dream never move south, pipe $k$ could only exit the east boundary at some row $\le r' < n + 1 - k$, again contradicting $\mathrm{kpi}(E)(n + 1 - k) = k$.

Therefore pipe $k$ must travel straight north in column $k$ from $(n, k)$ to $(n + 1 - k, k)$, turn east at $(n + 1 - k, k) = \mathsf{C}$, and—by the same crossing check against vertical pipes $j > k$—pass straight east through $\mathsf{P}$ tiles at $(n + 1 - k, j)$ for all $j = k+1, \dots, n$. Finally, for the fourth assertion (vacuous when $k = n$, since $n + 1 - k = 1$), assume $k < n$ and consider any row $r$ with $1 \le r \le n - k$. Then $r + (k + 1) \le n + 1$, so by the inductive hypothesis on column $k + 1$ the eastern neighbor $(r, k + 1)$ is either $\mathsf{C}$ (when $r + k + 1 = n + 1$) or $\mathsf{B}$ (when $r + k + 1 \le n$). In either case $(r, k + 1)$ has **no west connection**, whence $(r, k)$ has **no east connection**. Going top-down for $r = 1, 2, \dots, n - k$, cell $(r, k)$ also has **no north connection** (the north boundary of the grid is empty for $r = 1$, and $(r - 1, k) = \mathsf{B}$ has no south connection for $r > 1$). Among the six bumpless pipe dream tiles $\{\mathsf{B}, \mathsf{H}, \mathsf{V}, \mathsf{J}, \mathsf{C}, \mathsf{P}\}$, every tile except $\mathsf{B}$ has either a north connection ($\mathsf{P}, \mathsf{V}, \mathsf{J}$) or an east connection ($\mathsf{P}, \mathsf{H}, \mathsf{C}$); therefore $(r, k) = \mathsf{B}$ for all $r < n + 1 - k$. This completes the induction on $k$.

After completing the induction for all $k = n, \dots, 1$, every cell $(r, c)$ with $r + c > n + 1$ is $\mathsf{P}$ (by bullet 3 for column $k = n + 1 - r < c$), every cell with $r + c = n + 1$ is $\mathsf{C}$ (by bullet 1 for column $c$), and every cell with $r + c \le n$ is $\mathsf{B}$ (by bullet 4 for column $c$). Thus $E = E_0$ is unique, so $D_0 = \mathrm{halve}(E_0)$ is the unique element of $\mathsf{InvBPD}_K(w_0^{(n)})$, with $\mathrm{blank}(D_0) = \mathrm{iD}(w_0^{(n)})$, $|\mathrm{blank}(D_0)| = \ell_{\mathrm{inv}}(w_0^{(n)})$, and $\mathrm{upturn}(D_0) = \varnothing$. Hence $R_{w_0^{(n)}} = \prod_{(i,j)\in\mathrm{iD}(w_0^{(n)})} x_{i\oplus j} = \widehat{\mathfrak{G}}^{(\beta)}_{w_0^{(n)}}$. $\square$

---

### Proof of the Main Theorem

Fix $n \ge 1$. For $n = 1$, $I_1 = \{1\}$, $w_0^{(1)} = 1$, and Lemma 5 gives $R_1 = 1 = \widehat{\mathfrak{G}}^{(\beta)}_1$. For $n \ge 2$, we prove $R_z = \widehat{\mathfrak{G}}^{(\beta)}_z$ for all $z \in I_n$ by downward induction on $\ell_{\mathrm{inv}}(z)$ from $\ell_{\mathrm{inv}}(w_0^{(n)}) = \lfloor n^2/4 \rfloor$.

- **Base case:** If $z = w_0^{(n)}$, then $R_{w_0^{(n)}} = \widehat{\mathfrak{G}}^{(\beta)}_{w_0^{(n)}}$ by Lemma 5.
- **Inductive step:** Let $z \in I_n \setminus \{w_0^{(n)}\}$. Since $z \neq w_0^{(n)}$, there exists $i \in [n-1]$ with $z(i) < z(i+1)$. Then $z' := s_i \circ z \circ s_i \in I_n$ satisfies $z' \neq z$ and $\ell_{\mathrm{inv}}(z') = \ell_{\mathrm{inv}}(z) + 1$. By Lemma 4(b), the inductive hypothesis for $z'$, and Definition 2.7(b):
  $$R_z = \overline{\partial}_i R_{z'} = \overline{\partial}_i \widehat{\mathfrak{G}}^{(\beta)}_{z'} = \widehat{\mathfrak{G}}^{(\beta)}_z.$$

This completes the induction and proves Conjecture 3.8 (`\label{iG-conj}`) for all $n \ge 1$ and all $z \in I_n$. $\blacksquare$

---

*Remark.* Setting $\beta = 1$ in the Main Theorem and summing over all $z \in I_n$ via Proposition 2.8 (`prop:partition function inv Grothendieck`) immediately recovers Proposition 7.1 (`iG-conj-cor`, Section 7.1, lines 6803–6811), whose proof was omitted from `arXiv:2611.19371v1`.

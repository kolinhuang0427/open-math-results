# Proof of OEIS A400812 (Star Triples in Level-$n$ Spectre Supertiles)

## 1. Statement

For $n \ge 0$, let $a(n)$ denote the number of star triples (sets of three Spectre tiles related by a $120^\circ$ rotation about a common boundary point) in a level-$n$ Spectre supertile $X_n$ formed by starting from any of the $8$ single-Spectre marked tiles $X \in \{\Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Phi, \Psi\}$ (distinct from the Mystic supertile $\Gamma_n$; all $8$ non-$\Gamma$ tiles yield identical star-triple counts) in the substitution tiling of Smith–Myers–Kaplan–Goodman-Strauss (`arXiv:2305.17743`, §4–5). We prove all four formulas conjectured by Boris K. Horvat in OEIS **A400812** (`rev. 50`, Nov 10 2026), together with the corresponding generating functions for major (**A400813**) and minor (**A400814**) star triples:

1. **Generating functions ($n \ge 0$):**
   $$G(x) = \sum_{n \ge 0} a(n) x^n = \frac{4x^3(7 + 2x)}{(1 - x)(1 - 8x + x^2)(1 - 4x - x^2)},$$
   with $G(x) = G_L(x) + G_S(x)$ where the major and minor star-triple counts satisfy
   $$G_L(x) = \frac{2x^3(9 + x)}{(1 - x)(1 - 8x + x^2)(1 - 4x - x^2)}, \qquad G_S(x) = \frac{2x^3(5 + 3x)}{(1 - x)(1 - 8x + x^2)(1 - 4x - x^2)}.$$
2. **Linear recurrence ($n \ge 5$):**
   $$a(n) = 13\,a(n-1) - 44\,a(n-2) + 28\,a(n-3) + 5\,a(n-4) - a(n-5),$$
   with $a(0)=a(1)=a(2)=0$, $a(3)=28$, $a(4)=372$.
3. **Exact Spectre-count and Fibonacci identity ($n \ge 1$):**
   $$a(n) = \mathrm{A057080}(n-1) - \frac{F(3n+2) - 3}{2} = \mathrm{A057080}(n-1) - \mathrm{A099919}(n) + 1,$$
   where $F(m) = \mathrm{A000045}(m)$ is the Fibonacci sequence ($F(0)=0, F(1)=1$) and $\mathrm{A099919}(n) = (F(3n+2) - 1)/2$.
4. **Asymptotic ratio:**
   $$\lim_{n \to \infty} \frac{a(n)}{\mathrm{A057080}(n)} = 4 - \sqrt{15}.$$

---

## 2. Exact Combinatorial and Geometric Realization of $S_8/S_9$

By Smith–Myers–Kaplan–Goodman-Strauss (`arXiv:2305.17743`, §4–5, Theorem 4.1 & Theorem 5.1, `fig:markedSpectres` and `fig:supertiles`), the nine marked hexagons
$$\mathcal{M} = \{\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Phi, \Psi\}$$
have counterclockwise boundary edge labels (indexed $0,1,2,3,4,5$):
- $\Gamma$: $(\alpha^-, \alpha^+, \gamma^-, \delta^-, \beta^+, \beta^-)$
- $\Delta$: $(\gamma^+, \beta^+, \epsilon^-, \alpha^+, \gamma^-, \zeta^-)$
- $\Theta$: $(\gamma^+, \beta^+, \theta^+, \beta^+, \eta, \beta^-)$
- $\Lambda$: $(\gamma^+, \beta^+, \epsilon^-, \alpha^+, \theta^-, \beta^-)$
- $\Xi$: $(\alpha^-, \epsilon^+, \theta^+, \beta^+, \eta, \beta^-)$
- $\Pi$: $(\alpha^-, \epsilon^+, \epsilon^-, \alpha^+, \theta^-, \beta^-)$
- $\Sigma$: $(\zeta^+, \beta^+, \epsilon^-, \alpha^+, \gamma^-, \delta^+)$
- $\Phi$: $(\gamma^+, \beta^+, \epsilon^-, \epsilon^+, \eta, \beta^-)$
- $\Psi$: $(\alpha^-, \epsilon^+, \epsilon^-, \epsilon^+, \eta, \beta^-)$

Each level-$n$ supertile $X_n$ ($X \in \mathcal{M}$) is formed inductively from level-$(n-1)$ supertiles by placing 7 ($\Gamma$) or 8 ($X \neq \Gamma$) reflected copies of level-$(n-1)$ child supertiles in the combinatorial template of `fig_hexsubsts.tex`, matching every interior edge along opposite labels ($\ell \leftrightarrow \overline{\ell}$, with $\overline{\eta} = \eta$). In this substitution:
- Each non-$\Gamma$ level-0 hexagon corresponds to a single **even** Spectre $\mathrm{Tile}(1,1)$ tile, and $\Gamma$ corresponds to a **Mystic** (one **odd** Spectre $B$ glued along 4 consecutive edges to one **even** Spectre $A$).
- Passing to $\mathbb{Z}[\zeta_{12}]$ ($\zeta_{12} = e^{i\pi/6}$) in the `fig:markedSpectres` orientation, the 14 unit edge directions $k \cdot 30^\circ$ of the standard even Spectre $W$ are
  $$(0, 3, 5, 2, 4, 4, 6, 9, 7, 10, 8, 11, 1, 10),$$
  with vertex $W_0 = (0,0,0,0)$ between edges $10$ and $0$ ($120^\circ$ interior angle) and $W_2$ between edges $3$ and $5$ ($120^\circ$ interior angle). Each of the 8 single-Spectre marked tiles $\Delta, \dots, \Psi$ realizes its 6 marked corners as exact vertices of $W$ (for $\Sigma$, the zero-thickness spur at $W_{11} + \zeta_{12}^5 + \zeta_{12}^3$ divides $\delta^+$ from $\zeta^+$ and matches the opposite $\delta^-$ concavity on $\Gamma$'s 20-edge boundary).

Checking every compatible pair $(\ell, \overline{\ell})$ directly in $\mathbb{Z}[\zeta_{12}]$ confirms that adjacent marked Spectres glue congruently edge-to-edge without overlap (`verify.py`, verified explicitly on all 559 Spectres of $\Delta_3$ and all 4401 Spectres of $\Delta_4$).

---

## 3. Characterization of Star Triples for All $n \ge 0$

**Lemma 3.1 (Period-2 Boundary Stabilization).** *In the combinatorial level-$n$ marked-hexagon substitution $X_n$ ($X \in \mathcal{M}$, $n \ge 0$):*
1. *Every boundary vertex of $X_n$ (either a macro-corner or an interior vertex of one of the 6 macro-sides) belongs to at most $2$ level-0 hexagons inside $X_n$.*
2. *The ordered list of macro-corner tuples (the $6 \times 2$ start/end corner tuples of the 6 macro-sides of all 9 supertiles) satisfies $\mathrm{corners}(n) = \mathrm{corners}(n-2)$ for all $n \ge 4$, hence is strictly periodic with period $2$ for all $n \ge 2$.*

*Proof.* We prove parts (1) and (2) jointly by induction via period-2 corner stabilization. For $n \ge 1$, every boundary vertex of $X_n$ is either a macro-corner of $X_n$, a newly formed piece-junction vertex along $\partial X_n$ (or a macro-corner inherited from $X_{n-1}$ children inside $X_1$), or an older interior boundary vertex of a child $Y_{n-1}$. Because every macro-side at level $n-1 \ge 1$ has length $\ge 2$, three child corners can never collide at a single boundary vertex; consequently, every newly formed boundary vertex (and macro-corner) of $X_n$ has its corner tuple (and hence level-0 hexagon degree) uniquely determined by $\mathrm{corners}(n-1)$ and the fixed $X_1$ boundary template—either a single child macro-corner (when two consecutive boundary edges belong to the same child) or the concatenation of two child macro-corners (when two children meet). Direct computation (`verify.py`) establishes for $n = 0, 1, 2, 3, 4, 5$ both that $\max \deg_{\partial X_n} \le 2$ (specifically $= 2$ for $n \ge 1$, with every child macro-corner entering any interior 3-child macro-vertex of $X_1$ having degree $1$) and that $\mathrm{corners}(4) = \mathrm{corners}(2)$ and $\mathrm{corners}(5) = \mathrm{corners}(3)$. By induction on $n \ge 4$, $\mathrm{corners}(n) = \mathrm{corners}(n-2)$ holds for all $n \ge 4$, so every newly formed boundary vertex (and macro-corner) at level $n$ has the exact same tuple—hence level-0 degree $\le 2$—as at level $n - 2$, while older boundary vertices along child sides inherit degree $\le 2$ from level $n - 1$. $\square$

**Lemma 3.2 (Stabilization of All 3-Hexagon Interior Vertices).** *Every interior 3-hexagon vertex type occurring in any $X_n$ ($n \ge 0$, $X \in \mathcal{M}$) belongs to the finite set $\mathcal{V}_{45}$ of $45$ directed 3-corner configurations already realized at $n \le 4$. Moreover, no configuration in $\mathcal{V}_{45}$ contains $\Gamma$ twice, and no two $\Gamma$ hexagons ever share an edge or vertex in any $X_n$.*

*Proof.* Any interior 3-hexagon vertex of $X_{n+1}$ arises either inside a child supertile $Y_n$, at an interior 3-child macro-vertex of $X_1$ (using only level-$n$ macro-corners of degree $1$), or at a piece-junction along one of the $134$ compatible edge seams (also using only level-$n$ macro-corners). By Lemma 3.1, for all $n \ge 4$ the level-$n$ macro-corners coincide with those at level $n-2 \ge 2$, so every new vertex created at level $n+1 \ge 5$ was already created at level $n-1 \ge 3$. Direct enumeration confirms $|\mathcal{V}(4)| = |\mathcal{V}(5)| = |\mathcal{V}(6)| = 45$ (`verify.py`), and every member of $\mathcal{V}_{45}$ contains at most one $\Gamma$.

For the $\Gamma$-isolation claim, let $S_\Gamma := \{\alpha^-, \beta^-, \gamma^+, \zeta^-, \delta^+\}$ and $\overline{S_\Gamma} = \{\alpha^+, \beta^+, \gamma^-, \zeta^+, \delta^-\}$ (noting $S_\Gamma \cap \overline{S_\Gamma} = \emptyset$). Direct inspection of `fig_hexsubsts.tex` (`verify.py`) establishes the exact closure property: (i) in every $X_1$, the unique child $\Gamma$ touches $\partial X_1$ only along macro-sides with labels in $S_\Gamma$ (and only at macro-corners shared by two $S_\Gamma$ sides, never at any endpoint of a side outside $S_\Gamma$); and (ii) every parent macro-side of $X_1$ whose label is outside $S_\Gamma$ decomposes exclusively into child sides whose labels are outside $S_\Gamma$ (indeed, child sides in $S_\Gamma$ appear on $\partial X_1$ only inside parent macro-sides in $S_\Gamma$: $\alpha^- \to \{\beta^-\}$, $\beta^- \to \{\alpha^-\}$, $\gamma^+ \to \{\beta^-\}$, $\zeta^- \to \{\alpha^-\}$, $\delta^+ \to \{\alpha^-, \beta^-\}$, and on none of the other $10$ labels). By induction on $n \ge 1$, no level-0 $\Gamma$ hexagon touches any macro-side of $X_n$ outside $S_\Gamma$ (including endpoints). Whenever two children $Y_n, Z_n$ meet along an interior seam of $X_{n+1}$ (opposite labels $\ell \leftrightarrow \overline{\ell}$), at most one side belongs to $S_\Gamma$, so no two level-0 $\Gamma$ hexagons meet along a seam; combined with every interior 3-hexagon vertex in $\mathcal{V}_{45}$ containing at most one $\Gamma$, no two $\Gamma$ hexagons ever share an edge or vertex in any $X_n$. $\square$

**Theorem 3.3 (Exact Bijection with $L$- and $S$-Corners).** *For every $n \ge 0$ and every $X \in \mathcal{M}$, the geometric star triples in the level-$n$ Spectre supertile $X_n$ are in exact bijection with the interior 3-hexagon vertices of $X_n$ belonging to the two families:*
- **Major star triples ($L$, circumradius $R_L = \sqrt{10 + 5\sqrt{3}}$):** *three hexagons from $\{\Pi, \Psi\}$ meeting at their directed $(\epsilon^+, \epsilon^-)$ corners (vertex $W_0$ of $W$);*
- **Minor star triples ($S$, circumradius $R_S = \sqrt{10 + 3\sqrt{3}}$):** *three $\Phi$ hexagons meeting at their directed $(\epsilon^-, \epsilon^+)$ corners (vertex $W_2$ of $W$).*

*Proof.* ($\Leftarrow$) By the $\mathbb{Z}[\zeta_{12}]$ edge matchings, each $(\epsilon^+, \epsilon^-)$ corner of $\Pi$ or $\Psi$ sits at $W_0$ flanked by incoming $\epsilon^+$ and outgoing $\epsilon^-$. When three hexagons from $\{\Pi, \Psi\}$ meet there, edge-matching $\epsilon^+ \leftrightarrow \epsilon^-$ rotates consecutive tiles by $+120^\circ$ about $W_0$, and since $\Pi$ and $\Psi$ share the identical unmarked polygon $W$, they form a major star triple of circumradius $\sqrt{10 + 5\sqrt{3}}$. Similarly, three $\Phi$ hexagons meeting at $(\epsilon^-, \epsilon^+)$ ($W_2$) are rotated by $0^\circ, 120^\circ, 240^\circ$ about $W_2$, forming a minor star triple of circumradius $\sqrt{10 + 3\sqrt{3}}$.

($\Rightarrow$) Conversely, suppose three tiles $\{T_1, T_2, T_3\}$ in $X_n$ are related by $120^\circ$ rotation around a common boundary point $P$. Because $\pm 120^\circ$ rotations preserve the parity of tile edge angles (`even` vs `odd`), all three tiles must have the same parity. By Lemma 3.2, no two $\Gamma$ hexagons meet in $X_n$, so odd tiles are pairwise disjoint and no point can touch three odd tiles; thus $T_1, T_2, T_3$ are three distinct **even** tiles. Each marked hexagon contains at most one even tile, so $P$ must lie on three distinct marked hexagons of $X_n$. By Lemma 3.1, no point of $\partial X_n$ touches more than $2$ hexagons, and along any 2-hexagon interior edge—even at the $\Sigma$–$\Gamma$ zero-thickness spur (where the $\delta^-$ edge of $\Gamma = W \cup B$, namely vertices `B_{13}, B_0, \dots, B_5`, lies strictly on $\Gamma$'s **odd** Spectre $B$, completely disjoint from $\Gamma$'s **even** Spectre $W$, which meets $B$ only along `B_7..B_{11} = W_5..W_1`)—$\Gamma$'s even tile never touches the $\Sigma$–$\Gamma$ spur, the spur tip, or the 4-hexagon geometric pinch at $\Sigma$'s corner $1$ ($W_{11}$). Likewise, $\Sigma$'s even tile does not reach the spur tip, and on $\partial X_n$ at most $2$ even tiles meet even at a spur base. Thus at every 4-hexagon pinch $(\Sigma, \Delta, \Gamma, X)$, the even Spectres touching $P$ are exclusively the three even tiles of the interior 3-hexagon vertex $(\Sigma, \Delta, X) \in \mathcal{V}_{45}$. Hence every geometric point $P$ touched by three even Spectres corresponds uniquely to an interior 3-hexagon vertex in $\mathcal{V}_{45}$ whose three hexagons supply those three even Spectres. Exhaustive $\mathbb{Z}[\zeta_{12}]$ realization of all $45$ configurations in $\mathcal{V}_{45}$ (`verify.py`) confirms that exactly $3$ $L$-configs ($\Pi^2\Psi, \Pi\Psi^2, \Psi^3$ at $(\epsilon^+, \epsilon^-)$) and $1$ $S$-config ($\Phi^3$ at $(\epsilon^-, \epsilon^+)$) contain a $120^\circ$-symmetric 3-tile triple, while the remaining $41$ configurations yield zero star triples. (As an independent check, full $\mathbb{Z}[\zeta_{12}]$ geometric construction of $\Delta_3$ (559 Spectres) and $\Delta_4$ (4401 Spectres) finds $18+10=28$ and $236+136=372$ star triples, matching these two classes 1-to-1.) $\square$

---

## 4. Exact Linear Transfer Matrix, Generating Function, and Recurrence

Let $\mathcal{S}$ be the set of all $134$ unordered pairs $((Y, s_1), (Z, s_2))$ ($Y, Z \in \mathcal{M}$, $s_1, s_2 \in \{0,\dots,5\}$) of compatible supertile boundary sides (having opposite edge labels $\ell$ and $\overline{\ell}$). For each $n \ge 0$ and $T \in \{L, S\}$, define the $143$-dimensional integer state vector
$$v_n^{(T)} = \bigl(\, T(Y_n)_{Y \in \mathcal{M}}, \; \mathrm{Seam}_T((Y_n, s_1), (Z_n, s_2))_{((Y,s_1),(Z,s_2)) \in \mathcal{S}} \,\bigr)^T,$$
where $T(Y_n)$ counts interior $T$-triples strictly inside $Y_n$, and $\mathrm{Seam}_T((Y_n, s_1), (Z_n, s_2))$ counts interior $T$-triples formed strictly along the glued interior of the two sides $(Y_n, s_1)$ and $(Z_n, s_2)$ (excluding their two macro-corner endpoints).

For every $n \ge 1$, substituting $X_{n+1}$ from level-$n$ children splits each $Y_{n+1}$ into its 7 or 8 child supertiles plus its internal child seams and 3-child interior macro-vertices, and splits each glued seam $((Y_{n+1}, s_1), (Z_{n+1}, s_2))$ into the corresponding child seams along the boundary decomposition of $(Y_1, s_1)$ and $\mathrm{rev}(Z_1, s_2)$ plus their piece-junction vertices (for all $134$ seams in $\mathcal{S}$, the child-side decompositions of $(Y_1, s_1)$ and $\mathrm{rev}(Z_1, s_2)$ have identical length and match opposite-labeled child sides 1-to-1, so glued child seams align 1-to-1 for all $n \ge 0$). Because tile chirality and all macro-corners depend only on $n \bmod 2$ for $n \ge 2$ (Lemma 3.1), all piece-junctions and 3-child interior macro-vertices at transition $n \to n+1$ depend **only** on $n \bmod 2$ for all $n \ge 2$:
$$v_{n+1}^{(T)} = A\, v_n^{(T)} + b_{\text{even}}^{(T)} \quad (n \ge 2 \text{ even}), \qquad v_{n+1}^{(T)} = A\, v_n^{(T)} + b_{\text{odd}}^{(T)} \quad (n \ge 3 \text{ odd}),$$
where $A \in \mathbb{Z}_{\ge 0}^{143 \times 143}$ is the fixed integer adjacency/decomposition matrix (`verify.py` verifies $b_2^{(T)} = b_4^{(T)}$ and $b_3^{(T)} = b_5^{(T)}$, which by Lemma 3.1 extends to all $n \ge 2$).

Restricting $A$ to the $60$-dimensional subspace reachable from the $8$ non-$\Gamma$ supertiles yields $A_r \in \mathbb{Z}^{60 \times 60}$. Exact Krylov computation over $\mathbb{Q}$ (`verify.py`) proves that for every row $i$ corresponding to $X \in \{\Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Phi, \Psi\}$, the minimal annihilating polynomial of $A_r^2$ on $e_i^T$ is identically
$$q(z) = z(z - 1)(z^2 - 62z + 1)(z^2 - 18z + 1).$$
Now split $v_{2m+2}^{(T)}$ ($m \ge 0$) and $v_{2m+3}^{(T)}$ ($m \ge 0$). Since
$$v_{n+2}^{(T)} = A_r^2 v_n^{(T)} + c_{n \bmod 2}^{(T)} \qquad (c_{\text{even}}^{(T)} = A_r b_{\text{even}}^{(T)} + b_{\text{odd}}^{(T)}, \; c_{\text{odd}}^{(T)} = A_r b_{\text{odd}}^{(T)} + b_{\text{even}}^{(T)}),$$
taking first differences $\Delta_m = v_{2m+4}^{(T)} - v_{2m+2}^{(T)}$ cancels the constant $c_{\text{even}}^{(T)}$ and gives $\Delta_m = A_r^{2m} \Delta_0$ for all $m \ge 0$. Since $e_i^T q(A_r^2) = 0$, the generating function $\sum_{m \ge 0} (1 - y) e_i^T v_{2m+2}^{(T)} y^m$ is annihilated for degrees $m \ge \deg q + 1 = 7$ by the reciprocal polynomial $Q_{\text{rev}}(y) = y^6 q(1/y) = (1 - y)(1 - 62y + y^2)(1 - 18y + y^2)$ (up to the single initial term), so $(1 - y) Q_{\text{rev}}(y) \sum_{m \ge 0} T(X_{2m+2}) y^m$ is a polynomial of degree $\le 6$ (and likewise for the odd subsequence $T(X_{2m+3})$). Computing these exact finite numerators from $m=0,\dots,6$ in `verify.py` (with $y = x^2$) and cancelling common factors in $\mathbb{Q}(x)$ yields, identically for all 8 non-$\Gamma$ supertiles $X \neq \Gamma$,
$$G_L(x) = \frac{2x^3(9 + x)}{(1 - x)(1 - 8x + x^2)(1 - 4x - x^2)}, \qquad G_S(x) = \frac{2x^3(5 + 3x)}{(1 - x)(1 - 8x + x^2)(1 - 4x - x^2)}.$$
Summing gives Conjecture 2:
$$G(x) = G_L(x) + G_S(x) = \frac{4x^3(7 + 2x)}{(1 - x)(1 - 8x + x^2)(1 - 4x - x^2)}.$$
Expanding the denominator gives
$$(1 - x)(1 - 8x + x^2)(1 - 4x - x^2) = 1 - 13x + 44x^2 - 28x^3 - 5x^4 + x^5.$$
Since the numerator $4x^3(7 + 2x)$ has degree $4 < 5$, extracting $[x^n]$ proves the 5-term recurrence
$$a(n) = 13\,a(n-1) - 44\,a(n-2) + 28\,a(n-3) + 5\,a(n-4) - a(n-5) \qquad \forall n \ge 5,$$
and the initial coefficients $n=0,\dots,11$ match OEIS A400812: `0, 0, 0, 28, 372, 3604, 31268, 258464, 2086984, 16651528, 132032296, 1043449220`.

---

## 5. Proof of the $\mathrm{A057080}$–Fibonacci Formula and Asymptotic Limit

Let $g(n)$ and $t(n) = \mathrm{A057080}(n)$ be the numbers of Spectre tiles in $\Gamma_n$ and in any non-$\Gamma$ supertile $X_n$. From the child counts in `fig:supertiles` (`fig_hexsubsts.tex` of `arXiv:2305.17743`: $\Gamma_1$ has one $\Gamma$ and $6$ non-$\Gamma$ children; $X_1$ has one $\Gamma$ and $7$ non-$\Gamma$ children),
$$\begin{pmatrix} g(n) \\ t(n) \end{pmatrix} = \begin{pmatrix} 1 & 6 \\ 1 & 7 \end{pmatrix} \begin{pmatrix} g(n-1) \\ t(n-1) \end{pmatrix}, \qquad \begin{pmatrix} g(0) \\ t(0) \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}.$$
The matrix $M_{\text{tile}} = \begin{pmatrix} 1 & 6 \\ 1 & 7 \end{pmatrix}$ has characteristic polynomial $\lambda^2 - 8\lambda + 1$, so $t(n) = 8t(n-1) - t(n-2)$ for $n \ge 2$ with $t(0)=1, t(1)=9$, giving
$$\sum_{n \ge 1} \mathrm{A057080}(n-1) x^n = x \sum_{n \ge 0} t(n) x^n = \frac{x(1 + x)}{1 - 8x + x^2}.$$
Likewise, for $f(n) = F(3n+2)$, the Fibonacci recurrence gives $f(n) = 4f(n-1) + f(n-2)$ ($\phi^3 + \psi^3 = 4, \phi^3\psi^3 = -1$) with $f(0) = F(2) = 1$, $f(1) = F(5) = 5$, so $\sum_{n \ge 0} F(3n+2) x^n = \frac{1 + x}{1 - 4x - x^2}$ and
$$\sum_{n \ge 1} \frac{F(3n+2) - 3}{2} x^n = \frac{1}{2}\left(\frac{1 + x}{1 - 4x - x^2} - 1 - \frac{3x}{1 - x}\right).$$
Direct rational algebra gives
$$\frac{x(1 + x)}{1 - 8x + x^2} - \frac{1}{2}\left(\frac{1 + x}{1 - 4x - x^2} - 1 - \frac{3x}{1 - x}\right) = \frac{4x^3(7 + 2x)}{(1 - x)(1 - 8x + x^2)(1 - 4x - x^2)} = G(x).$$
Equating coefficients for $n \ge 1$ proves
$$a(n) = \mathrm{A057080}(n-1) - \frac{F(3n+2) - 3}{2} = \mathrm{A057080}(n-1) - \mathrm{A099919}(n) + 1.$$

Finally, the roots of $\lambda^2 - 8\lambda + 1 = 0$ are $\lambda_+ = 4 + \sqrt{15} \approx 7.873$ and $\lambda_- = 4 - \sqrt{15} = \lambda_+^{-1} \in (0, 1)$, yielding $t(n) = c_+ \lambda_+^n + c_- \lambda_-^n$ with $c_+ = \frac{1}{2} + \frac{5}{2\sqrt{15}} > 0$. Meanwhile $F(3n+2) = O\!\left((2+\sqrt{5})^n\right)$ with $2 + \sqrt{5} \approx 4.236 < 4 + \sqrt{15}$. Dividing the exact formula $a(n) = t(n-1) - \frac{F(3n+2)-3}{2}$ by $t(n)$ gives
$$\lim_{n \to \infty} \frac{a(n)}{\mathrm{A057080}(n)} = \lim_{n \to \infty} \frac{t(n-1)}{t(n)} - 0 = \frac{1}{4 + \sqrt{15}} = 4 - \sqrt{15},$$
completing the proof of all four conjectures in OEIS **A400812**. $\blacksquare$

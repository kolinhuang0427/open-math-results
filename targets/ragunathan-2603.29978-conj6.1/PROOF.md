# Proof of Conjecture 6.1 of Ragunathan–Van Tuyl (`arXiv:2603.29978v2`)

## Primary Source & Exact Statement

From Naveena Ragunathan and Adam Van Tuyl, *"The van der Waerden Simplicial Complex and its Lefschetz Properties"*, `arXiv:2603.29978v2` (submitted 31 March 2026, revised 19 August 2026), Section 1 (lines 192–195), Section 2 (lines 511–529), and Section 6 (Conjecture 6.1, `\label{conjecture}`, lines 1384–1393):

- **Definition (`vdw(n, k)`):** Fix integers $n > k \ge 1$. The *van der Waerden simplicial complex* ${\tt vdw}(n, k)$ on vertex set $X = \{x_1, \dots, x_n\}$ (identified with $[n] = \{1, \dots, n\}$) is the pure $k$-dimensional simplicial complex whose facets are the $(k+1)$-element arithmetic progressions (progressions with $k$ jumps)
  $$\{i,\ i + d,\ i + 2d,\ \dots,\ i + kd\} \subseteq [n] \qquad (d \ge 1,\ 1 \le i,\ i + kd \le n).$$
  The integer $d$ is called the *jump factor* of the facet.
- **Artinian Ring:** Over a field $K$, define the standard graded Artinian ring
  $$A({\tt vdw}(n, k)) := K[x_1, \dots, x_n] / \bigl(I_{{\tt vdw}(n, k)} + \langle x_1^2, \dots, x_n^2 \rangle\bigr),$$
  where $I_{{\tt vdw}(n, k)}$ is the Stanley–Reisner ideal of ${\tt vdw}(n, k)$.
- **Weak Lefschetz Property (WLP):** $A({\tt vdw}(n, k))$ has the WLP over $K$ if for a general linear form $\ell \in A_1$, the multiplication map $\times \ell : A_r \to A_{r+1}$ has maximal rank $\min(\dim_K A_r, \dim_K A_{r+1})$ for all $r \ge 0$.

> **Conjecture 6.1 (`arXiv:2603.29978v2`, Section 6):** Suppose $\mathrm{char}(K) = 0$. Fix an integer $k \ge 3$.
> 1. If $k$ is odd, then there exists an $m$ such that $A({\tt vdw}(n, k))$ fails to have the WLP for $n \ge m$.
> 2. If $k$ is even, then $A({\tt vdw}(n, k))$ has the WLP for all $n > k$.

We prove both parts of Conjecture 6.1 unconditionally. Specifically:
- For every even $k \ge 2$ and every $n > k$, $A({\tt vdw}(n, k))$ has the WLP over any field $K$ of characteristic $0$ (settling Part (2) and recovering the $k = 2$ theorem of Ragunathan–Van Tuyl).
- For every odd $k \ge 5$, $A({\tt vdw}(n, k))$ fails to have the WLP in degree $(k+1)/2$ for all $n \ge 2k + 2$ (and for $k = 3$, fails in degree $2$ for all $n \ge 40$ by a self-contained argument below, as well as for all $n \ge 7$ by Theorem 4.2 of `arXiv:2603.29978v2`), settling Part (1) with explicit threshold $m = 2k + 2$ for all odd $k \ge 5$.

---

## 1. Preliminaries

For any simplicial complex $\Delta$ on $[n]$ and any integer $r \ge 0$, let $F_r(\Delta) := \{S \in \Delta : |S| = r\}$ denote the set of $r$-element faces of $\Delta$ (so $F_0(\Delta) = \{\emptyset\}$, and $F_r(\Delta) = \emptyset$ for $r > \dim(\Delta) + 1$). The squarefree monomials $\{\overline{x_S} : S \in F_r(\Delta)\}$ (where $x_S = \prod_{j \in S} x_j$) form a $K$-basis of $A(\Delta)_r$, so $\dim_K A(\Delta)_r = |F_r(\Delta)|$.

### Lemma 1 (Reduction to $\ell = x_1 + \cdots + x_n$ and Incidence Matrices)
Let $\Delta$ be any simplicial complex on $[n]$, let $K$ be a field with $\mathrm{char}(K) = 0$, and let $A = A(\Delta)$. Then $A$ has the WLP over $K$ if and only if for every $0 \le r \le \dim(\Delta)$, the $|F_{r+1}(\Delta)| \times |F_r(\Delta)|$ $\{0, 1\}$-incidence matrix $M_r$ with entries
$$(M_r)_{T, S} = \begin{cases} 1 & \text{if } S \subset T, \\ 0 & \text{otherwise} \end{cases} \qquad \bigl(T \in F_{r+1}(\Delta),\ S \in F_r(\Delta)\bigr)$$
has maximal rank $\min(|F_r(\Delta)|, |F_{r+1}(\Delta)|)$ over $\mathbb{R}$ (equivalently over $\mathbb{Q}$ or $K$).

*Proof.* Set $R = K[x_1, \dots, x_n]$ and $I = I_\Delta + \langle x_1^2, \dots, x_n^2 \rangle$. Because $\mathrm{char}(K) = 0$, the field $K$ is infinite, so $U = \{(c_1, \dots, c_n) \in K^n : c_1 \cdots c_n \neq 0\}$ is a nonempty Zariski-open subset of $K^n$. For any $c = (c_1, \dots, c_n) \in U$, the graded $K$-algebra automorphism $\phi_c : R \to R$ sending $x_j \mapsto c_j^{-1} x_j$ scales every monomial by a nonzero scalar, hence satisfies $\phi_c(I) = I$ and descends to a graded $K$-algebra automorphism $\bar{\phi}_c : A \to A$ taking $\ell_c = \sum_{j=1}^n c_j x_j$ to $\ell_1 = \sum_{j=1}^n x_j$. Consequently, for every $r \ge 0$, $\mathrm{rank}_K(\times \ell_c : A_r \to A_{r+1}) = \mathrm{rank}_K(\times \ell_1 : A_r \to A_{r+1})$ for all $c \in U$ (cf. Migliore–Miró-Roig–Nagel, Prop. 2.2; Lundqvist–Nicklasson, Prop. 4.3). Since maximal rank in degree $r$ is a Zariski-open condition on $c \in K^n$ and $U$ is Zariski-dense in $K^n$, a general linear form has maximal rank in all degrees if and only if $\ell_1$ does.

With respect to the squarefree monomial bases of $A_r$ and $A_{r+1}$, multiplication by $\ell_1$ maps $\overline{x_S}$ ($S \in F_r(\Delta)$) to $\sum_{T \in F_{r+1}(\Delta),\, S \subset T} \overline{x_T}$, whose matrix is $M_r$. Because $A_r = 0$ for $r > \dim(\Delta) + 1$, the map $\times \ell_1 : A_r \to A_{r+1}$ automatically has maximal rank for $r > \dim(\Delta)$. Finally, $M_r$ has integer entries and $\mathbb{Q} \hookrightarrow K$, $\mathbb{Q} \hookrightarrow \mathbb{R}$, so $\mathrm{rank}_K(M_r) = \mathrm{rank}_\mathbb{Q}(M_r) = \mathrm{rank}_\mathbb{R}(M_r)$. $\square$

### Lemma 2 (Boolean Lattice Commutator Identity)
Let $E$ be a finite set of cardinality $N \ge 1$. For each $0 \le s \le N$, let $V_s = \mathbb{R}^{\binom{E}{s}}$ with its standard orthonormal basis $\{e_S : S \in \binom{E}{s}\}$, and set $V_{-1} = V_{N+1} = \{0\}$. Define linear maps $U_s : V_s \to V_{s+1}$ ($0 \le s \le N - 1$, $U_N = 0$) and $D_s : V_s \to V_{s-1}$ ($1 \le s \le N$, $D_0 = 0$) by
$$U_s(e_S) = \sum_{x \in E \setminus S} e_{S \cup \{x\}}, \qquad D_s(e_T) = \sum_{y \in T} e_{T \setminus \{y\}}.$$
Then $D_{s+1} = U_s^T$ for $0 \le s \le N - 1$, and for every $0 \le s \le N$,
$$D_{s+1} U_s - U_{s-1} D_s = (N - 2s)\, I_{V_s}$$
(with $D_{N+1} U_N := 0$ and $U_{-1} D_0 := 0$). In particular:
1. If $2s < N$, then $U_s$ is injective.
2. If $2s > N$, then $D_s$ is injective.

*Proof.* For $0 \le s \le N - 1$, $\langle U_s e_S, e_T \rangle = \mathbf{1}_{S \subset T} = \langle e_S, D_{s+1} e_T \rangle$, so $D_{s+1} = U_s^T$. For any $0 \le s \le N$ and any $S \in \binom{E}{s}$:
- $D_{s+1} U_s(e_S) = (N - s)\, e_S + \sum_{x \in E \setminus S} \sum_{y \in S} e_{(S \setminus \{y\}) \cup \{x\}}$, where the diagonal coefficient counts choices $y = x \in E \setminus S$ (giving $0$ when $s = N$).
- $U_{s-1} D_s(e_S) = s\, e_S + \sum_{y \in S} \sum_{x \in E \setminus S} e_{(S \setminus \{y\}) \cup \{x\}}$, where the diagonal coefficient counts choices $x = y \in S$ (giving $0$ when $s = 0$).

Subtracting cancels every off-diagonal term identically, yielding $(D_{s+1} U_s - U_{s-1} D_s)(e_S) = (N - 2s) e_S$. Taking the inner product with any $v \in V_s$ gives
$$\|U_s v\|_2^2 - \|D_s v\|_2^2 = \langle D_{s+1} U_s v, v \rangle - \langle U_{s-1} D_s v, v \rangle = (N - 2s)\|v\|_2^2.$$
If $2s < N$ and $U_s v = 0$, then $0 \ge (N - 2s)\|v\|_2^2$ forces $v = 0$. If $2s > N$ and $D_s v = 0$, then $\|U_s v\|_2^2 + (2s - N)\|v\|_2^2 = 0$ forces $v = 0$. $\square$

---

## 2. Proof of Conjecture 6.1(2) (Even $k \ge 2$)

Fix an even integer $k = 2m$ ($m \ge 1$) and an integer $n > 2m$, and set $\Delta = {\tt vdw}(n, 2m)$. Every facet of $\Delta$ has cardinality $2m + 1$. By Lemma 1, it suffices to prove that $M_r$ is injective for $0 \le r \le m$ and surjective for $m + 1 \le r \le 2m$.

### Proposition 3 (Lower Half: $0 \le r \le m$)
For every $0 \le r \le m$, the incidence matrix $M_r : \mathbb{R}^{F_r(\Delta)} \to \mathbb{R}^{F_{r+1}(\Delta)}$ is injective.

*Proof.* Let $z \in \ker(M_r)$, so $\sum_{S \in \binom{T}{r}} z(S) = 0$ for every $T \in F_{r+1}(\Delta)$. Let $F$ be any facet of $\Delta$. Then $|F| = 2m + 1$, and every $(r+1)$-element subset $T \subseteq F$ belongs to $F_{r+1}(\Delta)$. Restricting $z$ to $z|_F \in \mathbb{R}^{\binom{F}{r}}$, the equations at all $T \in \binom{F}{r+1}$ assert precisely $U_r(z|_F) = 0$ on the Boolean lattice of $F$. Since $2r \le 2m < 2m + 1 = |F|$, Lemma 2(1) implies $z|_F = 0$. Because $\Delta$ is pure of dimension $2m$, every $r$-element face $S \in F_r(\Delta)$ is contained in at least one facet $F$, whence $z(S) = 0$ for all $S \in F_r(\Delta)$. Thus $z = 0$. $\square$

For any finite set of integers $X = \{a_1 < a_2 < \dots < a_t\}$ with $t \ge 2$, define
$$g(X) := \gcd(a_2 - a_1,\ a_3 - a_1,\ \dots,\ a_t - a_1) \ge 1.$$

### Lemma 4 (Unique Jump for Cardinality $\ge m + 2$)
Let $k = 2m$ ($m \ge 1$) and $m + 1 \le r \le 2m$. Every face $T \in F_{r+1}({\tt vdw}(n, 2m))$ determines the jump factor of any facet containing it uniquely: if $T \subseteq F$ for a facet $F$ of ${\tt vdw}(n, 2m)$ with jump factor $d$, then $d = g(T)$.

*Proof.* Write $T = \{a_1 < \dots < a_{r+1}\}$. Since $T \subseteq F$ and $F$ is a $(2m+1)$-element AP of jump $d$, every difference $a_j - a_1$ is a multiple of $d$, so $d \mid g(T)$. Write $g(T) = q d$ with $q \in \mathbb{Z}_{\ge 1}$. Each consecutive gap $a_{j+1} - a_j$ is a positive multiple of $g(T)$, so
$$(m + 1) q d \le r \cdot g(T) \le a_{r+1} - a_1 \le 2m \cdot d.$$
Hence $(m + 1) q \le 2m < 2(m + 1)$, which forces $q = 1$ and $d = g(T)$. $\square$

### Proposition 5 (Upper Half: $m + 1 \le r \le 2m$)
For every $m + 1 \le r \le 2m$, the incidence matrix $M_r : \mathbb{R}^{F_r(\Delta)} \to \mathbb{R}^{F_{r+1}(\Delta)}$ is surjective (i.e., $\ker(M_r^T) = \{0\}$).

*Proof.* Suppose for contradiction that there exists a nonzero vector $v \in \ker(M_r^T) \subset \mathbb{R}^{F_{r+1}(\Delta)}$. Thus for every $S \in F_r(\Delta)$,
$$\sum_{\substack{T \in F_{r+1}(\Delta) \\ S \subset T}} v(T) = 0. \tag{$\star$}$$
Define the maximum jump in the support of $v$:
$$d_{\max} := \max\bigl\{g(T) : T \in F_{r+1}(\Delta),\ v(T) \neq 0\bigr\} \ge 1.$$
For every $T \in F_{r+1}(\Delta)$ with $g(T) = d_{\max}$, Lemma 4 implies that $T$ lies in a facet of jump $d_{\max}$, so its scaled span $L(T) := (\max T - \min T)/d_{\max}$ is an integer in $\{r, r+1, \dots, 2m\}$. Define
$$L_{\max} := \max\bigl\{L(T) : T \in F_{r+1}(\Delta),\ g(T) = d_{\max},\ v(T) \neq 0\bigr\} \in \{r, r+1, \dots, 2m\}.$$
Choose $T_0 \in F_{r+1}(\Delta)$ with $g(T_0) = d_{\max}$, $L(T_0) = L_{\max}$, and $v(T_0) \neq 0$. Set $a := \min T_0$, $b := \max T_0 = a + L_{\max} d_{\max}$, and
$$I := \{a,\ a + d_{\max},\ a + 2 d_{\max},\ \dots,\ a + L_{\max} d_{\max}\}, \qquad I^\circ := I \setminus \{a, b\}.$$
Since $T_0$ lies in some facet $F$ of jump $d_{\max}$ (by Lemma 4) and $a, b \in T_0 \subseteq F$, we have $I \subseteq F \subseteq [n]$, so every subset of $I$ is a face of $\Delta$. Note that $|I^\circ| = L_{\max} - 1 \ge r - 1 \ge m \ge 1$.

Now take any $(r - 2)$-element subset $S^\circ \subseteq I^\circ$ (valid since $0 \le r - 2 \le L_{\max} - 2 < |I^\circ|$) and form $S := \{a, b\} \cup S^\circ \in F_r(\Delta)$. We claim that every $T \in F_{r+1}(\Delta)$ with $S \subset T$ and $v(T) \neq 0$ satisfies $T \subseteq I$.

Indeed, let $T \in F_{r+1}(\Delta)$ satisfy $S \subset T$ and $v(T) \neq 0$, and let $d' := g(T)$. By maximality of $d_{\max}$, we have $d' \le d_{\max}$. By Lemma 4, $T$ is contained in a facet of jump $d'$, so $\max T - \min T \le 2m \cdot d'$. Since $\{a, b\} \subseteq S \subset T$, we also have $\max T - \min T \ge b - a = L_{\max} d_{\max}$. We consider two cases for $L_{\max}$:
- **Case 1: $L_{\max} = 2m$.** Then $2m \cdot d_{\max} = b - a \le \max T - \min T \le 2m \cdot d'$, whence $d' \ge d_{\max}$ and therefore $d' = d_{\max}$.
- **Case 2: $r \le L_{\max} \le 2m - 1$.** Because $S \subseteq I \subseteq a + d_{\max}\mathbb{Z}$, we may write $g(S) = q d_{\max}$ for some integer $q \ge 1$. Since $|S| = r \ge m + 1$,
  $$m q d_{\max} \le (r - 1) q d_{\max} \le b - a = L_{\max} d_{\max} \le (2m - 1) d_{\max},$$
  forcing $q = 1$, i.e., $g(S) = d_{\max}$. As $S \subset T$ lies in a facet of jump $d'$, we have $d' \mid g(S) = d_{\max}$. If $d' < d_{\max}$, then $d' \le d_{\max}/2$, giving
  $$(m + 1) d_{\max} \le L_{\max} d_{\max} = b - a \le \max T - \min T \le 2m \cdot d' \le m d_{\max},$$
  a contradiction. Thus again $d' = d_{\max}$.

In both cases $g(T) = d_{\max}$. By maximality of $L_{\max}$, we have $\max T - \min T \le L_{\max} d_{\max} = b - a$; combined with $a, b \in T$, this forces $\min T = a$ and $\max T = b$. Since $T$ lies in a facet of jump $d_{\max}$ containing $a$, every element of $T$ belongs to $(a + d_{\max}\mathbb{Z}) \cap [a, b] = I$, proving the claim.

Consequently, every $T \in F_{r+1}(\Delta)$ with $S \subset T$ and $v(T) \neq 0$ has the form $T = \{a, b\} \cup T^\circ$ for a unique $T^\circ \in \binom{I^\circ}{r - 1}$ containing $S^\circ$. Defining $w \in \mathbb{R}^{\binom{I^\circ}{r - 1}}$ by $w(T^\circ) := v(\{a, b\} \cup T^\circ)$, equation $(\star)$ over all $S^\circ \in \binom{I^\circ}{r - 2}$ becomes $D_{r - 1} w = 0$ on the Boolean lattice of $I^\circ$. Here $N' = |I^\circ| = L_{\max} - 1$ and $s = r - 1$ satisfy $0 \le s \le N'$ and
$$2s - N' = 2(r - 1) - (L_{\max} - 1) = 2r - L_{\max} - 1 \ge 2(m + 1) - 2m - 1 = 1 > 0.$$
By Lemma 2(2), $D_{r - 1}$ is injective, so $w = 0$. This contradicts $w(T_0 \setminus \{a, b\}) = v(T_0) \neq 0$. Hence $\ker(M_r^T) = \{0\}$. $\square$

### Completion of Proof of Conjecture 6.1(2)
By Propositions 3 and 5, $M_r$ has maximal rank for all $0 \le r \le 2m$. By Lemma 1, $A({\tt vdw}(n, 2m))$ has the WLP over every field $K$ of characteristic $0$ for all $m \ge 1$ and all $n > 2m$. In particular, Conjecture 6.1(2) holds for all even $k \ge 4$ and all $n > k$. $\square$

---

## 3. Proof of Conjecture 6.1(1) (Odd $k \ge 3$)

We first record an exact formula counting faces of a given primitive shape with unique jump factor.

### Lemma 6 (Exact Counting of $Q = 1$ Primitive Shapes)
Fix integers $n > k \ge 2$ and $1 \le L \le k$, and let $P = (0 = p_1 < p_2 < \dots < p_r = L)$ be a tuple of integers with $\gcd(p_2, \dots, p_r) = 1$. For any $g \ge 1$, the number of integers $a_1 \in [1, n - Lg]$ such that $a_1 + g \cdot P := \{a_1 + g p_1, \dots, a_1 + g p_r\}$ is contained in a jump-$g$ facet of ${\tt vdw}(n, k)$ equals:
- $n - L g$, if $1 \le g \le g_1 := \lfloor n / (k + 1) \rfloor$;
- $(k - L + 1)(n - k g)$, if $g_1 < g \le g_2 := \lfloor (n - 1) / k \rfloor$;
- $0$, if $g > g_2$.

In particular, summing over all $g \ge 1$ (resp. all even $g \ge 1$) yields
$$N_1(L; n, k) := \sum_{g = 1}^{g_1} (n - L g) + (k - L + 1) \sum_{g = g_1 + 1}^{g_2} (n - k g),$$
$$N_{1,\mathrm{even}}(L; n, k) := \sum_{\substack{1 \le g \le g_1 \\ 2 \mid g}} (n - L g) + (k - L + 1) \sum_{\substack{g_1 < g \le g_2 \\ 2 \mid g}} (n - k g).$$

*Proof.* A jump-$g$ facet $\{i, i+g, \dots, i+kg\} \subseteq [1, n]$ contains $a_1 + g \cdot P$ if and only if $i = a_1 - t g$ for some integer $t \in \{0, 1, \dots, k - L\}$ satisfying $1 \le a_1 - t g$ and $a_1 - t g + k g \le n$, i.e.,
$$a_1 \in I_t := [1 + t g,\ n - (k - t) g].$$
If $g > g_2$, then $n - k g \le 0$, so every $I_t$ is empty. Assume $1 \le g \le g_2$; then each $I_t$ is a nonempty discrete interval of cardinality $n - k g$, with $\min I_0 = 1$ and $\max I_{k - L} = n - L g$. Comparing $\max I_t = n - (k - t)g$ with $\min I_{t+1} = 1 + (t + 1)g$:
- If $1 \le g \le g_1$, then $n \ge (k + 1) g$, so $\max I_t + 1 = n - k g + t g + 1 \ge 1 + (t + 1) g = \min I_{t+1}$. Hence the discrete intervals $I_0, \dots, I_{k - L}$ overlap or abut, and $\left|\bigcup_{t=0}^{k-L} I_t\right| = |[1, n - Lg]| = n - L g$.
- If $g_1 < g \le g_2$, then $n < (k + 1) g$, so $\max I_t < \min I_{t+1}$. Hence $I_0, \dots, I_{k - L}$ are pairwise disjoint, and $\left|\bigcup_{t=0}^{k-L} I_t\right| = (k - L + 1)(n - k g)$. $\square$

### 3.1. The Case $k = 3$

By Theorem 4.2 of Ragunathan–Van Tuyl (`arXiv:2603.29978v2`), $A({\tt vdw}(n, 3))$ fails to have the WLP for all $n \ge 7$. For complete self-containment, we also give a short proof for all $n \ge 40$:

Every $3$-element face $T = \{a_1 < a_2 < a_3\} \in F_3({\tt vdw}(n, 3))$ satisfies $a_3 - a_1 \le 3 d$ when $T$ lies in a jump-$d$ facet; writing $g(T) = q d$, we get $2 q d \le a_3 - a_1 \le 3 d$, forcing $q = 1$ and $d = g(T)$. Thus its primitive shape $P(T) = (0, p_2, p_3)$ ($p_3 \le 3$) is one of $(0, 1, 2)$ ($L = 2$), $(0, 1, 3)$ ($L = 3$), or $(0, 2, 3)$ ($L = 3$). By Lemma 6, with $g_1 = \lfloor n / 4 \rfloor$ and $g_2 = \lfloor (n - 1) / 3 \rfloor$,
$$\begin{aligned}
|F_3({\tt vdw}(n, 3))| &= N_1(2; n, 3) + 2 N_1(3; n, 3) \\
&= \sum_{g = 1}^{g_1} (3n - 8g) + 4 \sum_{g = g_1 + 1}^{g_2} (n - 3g) \\
&= \bigl(4n g_2 - 6 g_2^2 - 6 g_2\bigr) + \bigl(2 g_1^2 - n g_1 + 2 g_1\bigr).
\end{aligned}$$
Since $g_2 \in [\frac{n - 3}{3}, \frac{n}{3}]$, we have $|g_2 - \frac{n}{3}| \le 1$, so
$$4n g_2 - 6 g_2^2 - 6 g_2 = \frac{2}{3} n^2 - 6\left(g_2 - \frac{n}{3}\right)^2 - 6 g_2 \ge \frac{2}{3} n^2 - 2n - 6.$$
Moreover, $2 g_1^2 - n g_1 + 2 g_1 = 2\left(g_1 - \frac{n}{4}\right)^2 - \frac{1}{8} n^2 + 2 g_1 \ge -\frac{1}{8} n^2$. Hence, for every $n \ge 40$,
$$|F_3({\tt vdw}(n, 3))| - |F_2({\tt vdw}(n, 3))| \ge |F_3({\tt vdw}(n, 3))| - \binom{n}{2} \ge \frac{n^2 - 36n - 144}{24} > 0,$$
so $\min(|F_2|, |F_3|) = |F_2|$. On the other hand, defining $z \in \mathbb{Q}^{F_2({\tt vdw}(n, 3))}$ by $z(\{a, b\}) = (-1)^{v_2(b-a)} 2^{v_2(b-a)}$ (where $v_2(t)$ is the $2$-adic valuation of $t$), every $3$-face $\{a < b < c\} \in F_3({\tt vdw}(n, 3))$ has pairwise differences $\{d, d, 2d\}$ or $\{d, 2d, 3d\}$, whose $2$-adic valuations are $\{v, v, v+1\}$ ($v = v_2(d)$). Thus $(M_2 z)_{\{a, b, c\}} = 2(-1)^v 2^v + (-1)^{v+1} 2^{v+1} = 0$. Since $z \neq 0$, $\mathrm{rank}(M_2) \le |F_2| - 1 < \min(|F_2|, |F_3|)$, so WLP fails in degree $2$ for all $n \ge 40$.

### 3.2. The Case $k = 2m - 1 \ge 5$ ($m \ge 3$)

Fix an odd integer $k = 2m - 1 \ge 5$ ($m \ge 3$) and set $\Delta = {\tt vdw}(n, 2m - 1)$. We show that $A(\Delta)$ fails to have the WLP in degree $m$ for **every** $n \ge 4m = 2k + 2$.

### Proposition 7 (Explicit 4-Facet Kernel Vector in $\ker(M_m^T)$)
For every $m \ge 2$ and every $n \ge 4m$, there exists a nonzero vector $v \in \ker(M_m^T) \subset \mathbb{Q}^{F_{m+1}({\tt vdw}(n, 2m-1))}$.

*Proof.* Since $n \ge 4m$, partition $\{1, 2, \dots, 4m\} \subseteq [n]$ into four pairwise disjoint sets of size $m$:
$$\begin{aligned}
A &= \{1, 3, \dots, 2m - 1\}, & B &= \{2, 4, \dots, 2m\}, \\
C &= \{2m + 1, 2m + 3, \dots, 4m - 1\}, & D &= \{2m + 2, 2m + 4, \dots, 4m\}.
\end{aligned}$$
The four $(2m)$-element sets
$$F_1 := A \sqcup B = \{1, \dots, 2m\}, \qquad F_2 := C \sqcup D = \{2m + 1, \dots, 4m\},$$
$$F_{\mathrm{odd}} := A \sqcup C = \{1, 3, \dots, 4m - 1\}, \qquad F_{\mathrm{even}} := B \sqcup D = \{2, 4, \dots, 4m\}$$
are arithmetic progressions of $2m = k + 1$ elements in $[n]$ (with jumps $1, 1, 2, 2$), hence are facets of ${\tt vdw}(n, 2m - 1)$. Because every pairwise intersection among $\{F_1, F_2, F_{\mathrm{odd}}, F_{\mathrm{even}}\}$ has size $0$ or $m < m + 1$, the four families $\binom{F_1}{m+1}, \binom{F_2}{m+1}, \binom{F_{\mathrm{odd}}}{m+1}, \binom{F_{\mathrm{even}}}{m+1}$ of $(m+1)$-element faces are pairwise disjoint.

For $a \in \{1, 2, \dots, m\}$, define
$$w(a) := \frac{(-1)^a}{\binom{m - 1}{a - 1}} \in \mathbb{Q} \setminus \{0\}.$$
These weights satisfy three immediate identities:
1. $w(1) = -1$ and $w(m) = (-1)^m$;
2. $w(m + 1 - a) = (-1)^{m + 1} w(a)$ for all $1 \le a \le m$ (since $\binom{m-1}{m-a} = \binom{m-1}{a-1}$);
3. $(m - j) w(j + 1) + j w(j) = 0$ for all $1 \le j \le m - 1$ (since $j \binom{m-1}{j} = (m - j) \binom{m-1}{j-1}$).

Define $v \in \mathbb{Q}^{F_{m+1}(\Delta)}$ on the four disjoint families by
$$v(T) := \begin{cases}
+w(|T \cap A|) & \text{if } T \in \binom{F_1}{m+1}, \\
+w(|T \cap D|) & \text{if } T \in \binom{F_2}{m+1}, \\
-w(|T \cap A|) & \text{if } T \in \binom{F_{\mathrm{odd}}}{m+1}, \\
-w(|T \cap D|) & \text{if } T \in \binom{F_{\mathrm{even}}}{m+1}, \\
0 & \text{otherwise.}
\end{cases}$$
(Note that if $T \in \binom{X \sqcup Y}{m+1}$ with $|X| = |Y| = m$, then $1 \le |T \cap X| \le m$, so $v$ is well-defined; moreover $v(A \cup \{2\}) = w(m) = (-1)^m \neq 0$, so $v \neq 0$.)

We verify that $(M_m^T v)_S = \sum_{T \in F_{m+1}(\Delta),\, S \subset T} v(T) = 0$ for every $S \in F_m(\Delta)$. Any term with $v(T) \neq 0$ has $S \subset T \subset F_*$ for some $F_* \in \{F_1, F_2, F_{\mathrm{odd}}, F_{\mathrm{even}}\}$. If $S$ is not contained in any of these four facets, the sum is empty and equals $0$. Otherwise there are two cases:

- **Case 1: $S \notin \{A, B, C, D\}$.** Then $S$ lies in a unique facet $F_* = X \sqcup Y$ among $\{F_1, F_2, F_{\mathrm{odd}}, F_{\mathrm{even}}\}$ (with $X \in \{A, D\}$ and $Y \in \{B, C\}$), because $S$ intersects both $X$ and $Y$ nontrivially. Setting $j := |S \cap X| \in \{1, \dots, m - 1\}$ (so $|S \cap Y| = m - j$) and letting $\varepsilon \in \{+1, -1\}$ be the sign of $v$ on $\binom{F_*}{m+1}$, the extensions $T \subset F_*$ of $S$ are obtained either by adding one of the $m - j$ elements of $X \setminus S$ (giving $|T \cap X| = j + 1$) or by adding one of the $j$ elements of $Y \setminus S$ (giving $|T \cap X| = j$). Hence
  $$(M_m^T v)_S = \varepsilon\bigl((m - j) w(j + 1) + j w(j)\bigr) = 0.$$
- **Case 2: $S \in \{A, B, C, D\}$.** Each of the four sets lies in exactly two of the four facets, and its extensions cancel identically:
  - $S = A \subset F_1, F_{\mathrm{odd}}$: $m$ extensions $A \cup \{y\}$ ($y \in B$, weight $+w(m)$) and $m$ extensions $A \cup \{z\}$ ($z \in C$, weight $-w(m)$); sum $= m w(m) - m w(m) = 0$.
  - $S = B \subset F_1, F_{\mathrm{even}}$: $m$ extensions $B \cup \{x\}$ ($x \in A$, weight $+w(1)$) and $m$ extensions $B \cup \{u\}$ ($u \in D$, weight $-w(1)$); sum $= m w(1) - m w(1) = 0$.
  - $S = C \subset F_2, F_{\mathrm{odd}}$: $m$ extensions $C \cup \{u\}$ ($u \in D$, weight $+w(1)$) and $m$ extensions $C \cup \{x\}$ ($x \in A$, weight $-w(1)$); sum $= m w(1) - m w(1) = 0$.
  - $S = D \subset F_2, F_{\mathrm{even}}$: $m$ extensions $D \cup \{z\}$ ($z \in C$, weight $+w(m)$) and $m$ extensions $D \cup \{y\}$ ($y \in B$, weight $-w(m)$); sum $= m w(m) - m w(m) = 0$.

Thus $M_m^T v = 0$ and $v \neq 0$. $\square$

### Proposition 8 (Exact Face-Count Dominance $|F_m| > |F_{m+1}|$ via Catalan Numbers)
For every integer $m \ge 3$, $k = 2m - 1$, and every integer $n > k$,
$$\bigl|F_m({\tt vdw}(n, 2m - 1))\bigr| > \bigl|F_{m+1}({\tt vdw}(n, 2m - 1))\bigr|.$$

*Proof.* Every $r$-element subset $S = \{a_1 < \dots < a_r\} \subseteq [n]$ ($r \ge 2$) is uniquely encoded by $(a_1, g, P)$ where $g = g(S) \ge 1$, $P = (0 = p_1 < \dots < p_r)$ with $p_j = (a_j - a_1)/g$ satisfies $\gcd(p_2, \dots, p_r) = 1$, and $S = a_1 + g \cdot P$. If $S$ lies in a facet of jump $d$ of ${\tt vdw}(n, 2m - 1)$, then $d \mid g$ (write $g = q d$, $q \ge 1$) and $(r - 1) q d \le q p_r d = a_r - a_1 \le (2m - 1) d$, so $q p_r \le 2m - 1$.

1. **Exact count of $|F_{m+1}|$:** For $r = m + 1$, we have $m q \le q p_{m+1} \le 2m - 1 < 2m$, forcing $q = 1$ (so $d = g$). Moreover, every tuple $0 = x_1 < \dots < x_{m+1} \le 2m - 1$ is automatically primitive (if $\gcd(x_2, \dots, x_{m+1}) \ge 2$, then $x_{m+1} \ge 2m > 2m - 1$). For each span $L \in \{m, \dots, 2m - 1\}$, there are $\binom{L - 1}{m - 1}$ such tuples $P$, each contributing $N_1(L; n, k)$ faces by Lemma 6. Hence
   $$|F_{m+1}| = \sum_{L = m}^{2m - 1} \binom{L - 1}{m - 1} N_1(L; n, k).$$

2. **Exact count of $|F_m|$:** For $r = m \ge 3$, we have $(m - 1) q \le q p_m \le 2m - 1 < 3(m - 1)$, so $q \in \{1, 2\}$. Furthermore, $q = 2$ forces $2 p_m \le 2m - 1$, hence $p_m = m - 1$ and $P = P_0 := (0, 1, \dots, m - 1)$. Similarly, among all tuples $0 = x_1 < \dots < x_m \le 2m - 1$, the *only* non-primitive tuple is $(0, 2, 4, \dots, 2m - 2)$ (with $\gcd = 2$, span $2m - 2$).
   - Every primitive shape $P \neq P_0$ of span $L \in \{m, \dots, 2m - 1\}$ allows only $q = 1$, contributing $N_1(L; n, k)$ faces by Lemma 6. The number of such primitive shapes of span $L$ is $\binom{L - 1}{m - 2}$ for $L \neq 2m - 2$ and $\binom{2m - 3}{m - 2} - 1$ for $L = 2m - 2$.
   - For $P = P_0$ ($L = m - 1$):
     - If $g$ is odd, only $q = 1$ is possible, contributing $N_1(m - 1; n, k) - N_{1,\mathrm{even}}(m - 1; n, k)$ faces.
     - If $g = 2d$ is even ($d \ge 1$), then $S = a_1 + 2d \cdot P_0 = a_1 + d \cdot (0, 2, \dots, 2m - 2)$ lies in ${\tt vdw}(n, k)$ if and only if $S$ lies in a jump-$2d$ facet or a jump-$d$ facet. We claim that lying in a jump-$2d$ facet already implies lying in a jump-$d$ facet: indeed, if $S$ lies in a jump-$2d$ facet in $[1, n]$, then $n \ge 1 + k(2d) = 1 + (4m - 2) d > 2m d = (k + 1) d$, so $d \le \lfloor n / (k + 1) \rfloor = g_1$; since $1 \le a_1 \le n - (2m - 2) d$, Lemma 6 (first bullet, with span $2m - 2$) shows that every such $a_1$ lies in a jump-$d$ facet! Thus the count of even-$g$ faces of shape $P_0$ is *identically* $N_1(2m - 2; n, k)$.

   Combining both items, the $+N_1(2m - 2; n, k)$ from even-$g$ faces of $P_0$ cancels the $-N_1(2m - 2; n, k)$ from the unique non-primitive tuple $(0, 2, \dots, 2m - 2)$, leaving the exact identity
   $$|F_m| = \sum_{L = m - 1}^{2m - 1} \binom{L - 1}{m - 2} N_1(L; n, k) - N_{1,\mathrm{even}}(m - 1; n, k).$$

3. **Exact Catalan identity and positivity:** By the hockey-stick identity,
   $$\sum_{L = m - 1}^{2m - 1} \binom{L - 1}{m - 2} = \binom{2m - 1}{m - 1} = \binom{2m - 1}{m} = \sum_{L = m}^{2m - 1} \binom{L - 1}{m - 1},$$
   while
   $$\begin{aligned}
   \sum_{L = m}^{2m - 1} L \binom{L - 1}{m - 1} - \sum_{L = m - 1}^{2m - 1} L \binom{L - 1}{m - 2}
   &= m \sum_{L = m}^{2m - 1} \binom{L}{m} - (m - 1) \sum_{L = m - 1}^{2m - 1} \binom{L}{m - 1} \\
   &= m \binom{2m}{m + 1} - (m - 1) \binom{2m}{m} \\
   &= \left(\frac{m^2}{m + 1} - (m - 1)\right) \binom{2m}{m} = \frac{1}{m + 1} \binom{2m}{m} = C_m,
   \end{aligned}$$
   the $m$-th Catalan number. Substituting the linear dependence $N_1(L; n, k) = \bigl(\sum_{g=1}^{g_1} n + (k+1)\sum_{g=g_1+1}^{g_2} (n - kg)\bigr) - L\bigl(\sum_{g=1}^{g_1} g + \sum_{g=g_1+1}^{g_2} (n - kg)\bigr)$ cancels the $L$-independent terms identically and yields
   $$|F_m| - |F_{m+1}| = C_m \left(\sum_{g = 1}^{g_1} g + \sum_{g = g_1 + 1}^{g_2} (n - k g)\right) - \sum_{\substack{1 \le g \le g_1 \\ 2 \mid g}} \bigl(n - (m - 1) g\bigr) - (m + 1) \sum_{\substack{g_1 < g \le g_2 \\ 2 \mid g}} (n - k g).$$
   For all $m \ge 3$, an immediate induction using $C_3 = 5$ and $C_{m+1} = \frac{4m + 2}{m + 2} C_m \ge 2 C_m$ gives $C_m \ge m + 2 > m + 1$ and $2 C_m \ge 3m + 1$.
   - Since $n - k g \ge 1$ for every $g_1 < g \le g_2$ and $C_m > m + 1$, the difference of the $(g_1, g_2]$ sums is $\ge 0$.
   - For the $[1, g_1]$ sums, note that $n \ge 2m$ implies $g_1 = \lfloor n / (2m) \rfloor \ge 1$ and $n \le 2m(g_1 + 1) - 1$. Write $h := \lfloor g_1 / 2 \rfloor \ge 0$, so the even $g \in [1, g_1]$ are $2, 4, \dots, 2h$:
     - If $g_1 = 2h$ ($h \ge 1$):
       $$\sum_{j = 1}^h \bigl(n - 2(m - 1) j\bigr) = h n - (m - 1) h(h + 1) \le h\bigl(2m(2h + 1) - 1\bigr) - (m - 1)(h^2 + h) = (3m + 1) h^2 + m h,$$
       while $C_m \sum_{g=1}^{2h} g = C_m h(2h + 1) = 2 C_m h^2 + C_m h$. Their difference is at least $(2 C_m - 3m - 1) h^2 + (C_m - m) h \ge 2h > 0$.
     - If $g_1 = 2h + 1$ ($h \ge 0$):
       $$\sum_{j = 1}^h \bigl(n - 2(m - 1) j\bigr) \le h\bigl(2m(2h + 2) - 1\bigr) - (m - 1)(h^2 + h) = (3m + 1) h^2 + 3m h,$$
       while $C_m \sum_{g=1}^{2h+1} g = C_m(2h + 1)(h + 1) = 2 C_m h^2 + 3 C_m h + C_m$. Their difference is at least $(2 C_m - 3m - 1) h^2 + 3(C_m - m) h + C_m \ge C_m \ge 5 > 0$.

   In all cases $|F_m| - |F_{m+1}| > 0$. $\square$

### Completion of Proof of Conjecture 6.1(1)
For $k = 3$, $A({\tt vdw}(n, 3))$ fails the WLP for all $n \ge 40$ by Section 3.1 (and for all $n \ge 7$ by Theorem 4.2 of `arXiv:2603.29978v2`). For any odd $k = 2m - 1 \ge 5$ ($m \ge 3$) and any $n \ge 4m = 2k + 2$, Proposition 7 yields a nonzero vector in $\ker(M_m^T)$, so $\mathrm{rank}(M_m) = \mathrm{rank}(M_m^T) \le |F_{m+1}| - 1$. By Proposition 8, $\min(|F_m|, |F_{m+1}|) = |F_{m+1}|$, so $M_m$ does not have maximal rank. By Lemma 1, $A({\tt vdw}(n, k))$ fails to have the WLP over every field $K$ of characteristic $0$ for all $n \ge 2k + 2$. $\square$

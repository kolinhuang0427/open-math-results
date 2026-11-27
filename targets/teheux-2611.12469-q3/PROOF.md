# Proof of Teheux (`arXiv:2611.12469v1`), Section 8, Question 8.4 item (3)

## Target Statement

From Bruno Teheux, *Dualities and completions of median algebras and semilattices: a universal-algebraic approach*, `arXiv:2611.12469v1` (2026-11-09), Section 8, Question 8.4 (`\label{q:correspondence}`), item **(3)** (`Notes_definability_pocset.tex`, lines 3077–3079):

> **Question 8.4(3).** Does every universal sentence that holds in a median algebra $\mathbf{A}$ hold in $\hat{\mathbf{A}}$, that is, does every finite subalgebra of $\hat{\mathbf{A}}$ embed into $\mathbf{A}$?

**Answer:** **YES.**

---

## Main Theorem

**Theorem 1.** *Let $\mathbf{A}$ be a median algebra and let $\hat{\mathbf{A}}$ be its profinite completion. Then every finite median subalgebra $\mathbf{B}$ of $\hat{\mathbf{A}}$ embeds into $\mathbf{A}$. Equivalently, every universal first-order sentence in the language $L_{\mathsf{M}} = \{m\}$ that holds in $\mathbf{A}$ also holds in $\hat{\mathbf{A}}$.*

---

## Preliminaries and Notation

We follow the notation and results of Teheux (`arXiv:2611.12469v1`, Sections 2–4 and 7–8):
- A median algebra $\mathbf{A} = (A, m)$ satisfies symmetry, majority, and distributivity (`Definition 2.1`). By universal-algebraic convention, $A \neq \emptyset$. The variety $\mathsf{M} = \mathbb{ISP}(\mathbf{2})$ is locally finite (`Theorem 2.4` and lines 323–330).
- The canonical bounded poc set $\mathbf{A}^+ = (\mathsf{M}(\mathbf{A}, \mathbf{2}), \le, {}^\bullet, 0, 1)$ consists of all prime convex subsets of $\mathbf{A}$ (equivalently, homomorphisms $x \colon \mathbf{A} \to \mathbf{2}$), ordered pointwise on $A$, with involution $x^\bullet(a) = 1 - x(a)$ and bounds $0, 1$ (constant maps).
- Let $\mathbf{X} := \mathbf{A}^* \in \mathsf{Poc}_\tau = \mathbb{IS}_c\mathbb{P}^+(\utilde{\mathbf{2}}_\tau)$ be $\mathbf{A}^+$ equipped with the subspace topology inherited from the product space $\utilde{\mathbf{2}}_\tau^A$ (with $\{0, 1\}$ discrete). Then:
  1. $X$ is compact Hausdorff (closed in $\{0, 1\}^A$).
  2. The partial order $\le$ is closed in $X \times X$; in particular, for every $z \in X$, both $z^\uparrow := \{x \in X \mid z \le x\}$ and $z^\downarrow := \{x \in X \mid x \le z\}$ are closed in $X$.
  3. The involution $x \mapsto x^\bullet$ is an order-reversing involutive homeomorphism of $X$ exchanging $0$ and $1$ and satisfying $x \le x^\bullet \iff x = 0$ (`Definition 2.5`, lines 651–654).
  4. **Strong duality (`Theorem 3.4(1)`):** The evaluation map $e_{\mathbf{A}} \colon \mathbf{A} \to \mathbf{X}_* = \mathsf{Poc}_\tau(\mathbf{X}, \utilde{\mathbf{2}}_\tau)$, sending $a \in A$ to $\mathrm{ev}_a(x) := x(a)$, is an isomorphism of median algebras. Identifying each map $f \colon \mathbf{X} \to \utilde{\mathbf{2}}_\tau$ with $f^{-1}(1)$, the elements of $\mathbf{X}_*$ are precisely the **clopen ultrafilters** of $\mathbf{X}$, i.e., clopen up-sets $C \subseteq X$ such that $0 \notin C$, $1 \in C$, and $x \in C \iff x^\bullet \notin C$ (equivalently $C^\bullet = C^c$, where $S^\bullet := \{x^\bullet \mid x \in S\}$ and $S^c := X \setminus S$), with median
     $$m(C_1, C_2, C_3) = (C_1 \cap C_2) \cup (C_1 \cap C_3) \cup (C_2 \cap C_3).$$
  5. **Pointwise clopen separation:** If $y \not\le t$ in $\mathbf{X}$, then there exists $a \in A$ with $y(a) = 1$ and $t(a) = 0$. The set $C_a := \{x \in X \mid x(a) = 1\}$ is a clopen ultrafilter of $\mathbf{X}$ with $y \in C_a$ and $t \notin C_a$, so $C_a^c = C_a^\bullet$ is a clopen down-set containing $t$ and avoiding $y$. Hence for every $t \in X$,
     $$t^\downarrow = \bigcap \{H \subseteq X \mid H \text{ is a clopen down-set of } \mathbf{X} \text{ and } t \in H\}.$$
  6. **Profinite completion (`Corollary 4.6`):** $\hat{\mathbf{A}} \cong (\mathbf{X}^\flat)_+ = \mathsf{Poc}(\mathbf{X}^\flat, \utilde{\mathbf{2}})$ via an isomorphism fixing $\mathbf{A}$. Identifying elements of $(\mathbf{X}^\flat)_+$ with their preimages of $1$, the elements of $\hat{\mathbf{A}}$ are precisely all (not necessarily clopen) **ultrafilters** of $\mathbf{X}$ (up-sets $U \subseteq X$ with $0 \notin U$, $1 \in U$, and $U^\bullet = U^c$), with the same set-theoretic median $(U_1 \cap U_2) \cup (U_1 \cap U_3) \cup (U_2 \cap U_3)$.
- Two elements $p, q \in X \setminus \{0, 1\}$ are **transverse** (`Example 8.1`) if none of $p \le q$, $q \le p$, $p \le q^\bullet$, $p^\bullet \le q$ holds.
- The **rank** $\mathrm{rank}(\mathbf{A})$ is the largest $n \in \mathbb{N}$ such that $\mathbf{2}^n$ embeds into $\mathbf{A}$, or $\infty$ if no largest such $n$ exists (`Section 7`, lines 2609–2612).

---

## Proof of Theorem 1

### Equivalence of the Two Statements

If every finite subalgebra of $\hat{\mathbf{A}}$ embeds into $\mathbf{A}$, and a universal sentence $\varphi = \forall x_1 \cdots \forall x_n\, \psi(x_1, \dots, x_n)$ ($\psi$ quantifier-free) fails in $\hat{\mathbf{A}}$ at a tuple $(u_1, \dots, u_n)$, then $\varphi$ fails in the subalgebra $\mathbf{B} = \langle u_1, \dots, u_n \rangle \le \hat{\mathbf{A}}$. Because $\mathsf{M}$ is locally finite, $\mathbf{B}$ is finite, so $\mathbf{B}$ embeds into $\mathbf{A}$; hence $\varphi$ fails in $\mathbf{A}$. Conversely, if every universal sentence holding in $\mathbf{A}$ holds in $\hat{\mathbf{A}}$, then for every finite median algebra $\mathbf{B}$, applying this to the universal sentence $\varphi_{\mathbf{B}}$ of `Example 7.2` (which holds in a median algebra iff $\mathbf{B}$ does not embed into it) shows that $\mathbf{B} \hookrightarrow \hat{\mathbf{A}} \implies \mathbf{B} \hookrightarrow \mathbf{A}$.

---

### Reduction by Rank

Let $\mathbf{A}$ be a median algebra and let $\mathbf{B} \le (\mathbf{X}^\flat)_+ \cong \hat{\mathbf{A}}$ be a finite median subalgebra. If $|A| = 1$, then $\mathbf{A}$ is finite and $\hat{\mathbf{A}} \cong \mathbf{A}$, so the claim is trivial; assume $|A| \ge 2$.

**Case 1: $\mathrm{rank}(\mathbf{A}) = \infty$.**
By `Theorem 2.4`, $\mathbf{B}$ embeds into $\mathbf{2}^d$ where $d := |\mathsf{M}(\mathbf{B}, \mathbf{2})| < \infty$. Since $\mathrm{rank}(\mathbf{A}) = \infty$, there exists $n \ge d$ such that $\mathbf{2}^n$ embeds into $\mathbf{A}$. Composing $\mathbf{B} \hookrightarrow \mathbf{2}^d \hookrightarrow \mathbf{2}^n \hookrightarrow \mathbf{A}$ (where $\mathbf{2}^d \hookrightarrow \mathbf{2}^n$ pads coordinates by $0$) yields an embedding $\mathbf{B} \hookrightarrow \mathbf{A}$.

**Case 2: $\mathrm{rank}(\mathbf{A}) = r < \infty$.**
We first establish the link between $\mathrm{rank}(\mathbf{A})$ and pairwise transverse elements of $\mathbf{X} \setminus \{0, 1\}$ (a self-contained proof of the direction needed from `Example 8.1` / `Corollary 7.6`).

**Lemma 1 (Transversality bound).** *If $\mathrm{rank}(\mathbf{A}) = r < \infty$, then $\mathbf{X} \setminus \{0, 1\}$ contains at most $r$ pairwise transverse elements.*

*Proof.* Let $x_1, \dots, x_k \in \mathbf{X} \setminus \{0, 1\}$ be pairwise transverse. Identifying each $x_i$ with the nonempty proper prime convex subset $x_i^{-1}(1) \subseteq A$ and $x_i^\bullet$ with $A \setminus x_i^{-1}(1)$, transversality of $x_i$ and $x_j$ ($i \neq j$) means that all four intersections $x_i \cap x_j$, $x_i \cap x_j^\bullet$, $x_i^\bullet \cap x_j$, $x_i^\bullet \cap x_j^\bullet$ are nonempty.

We recall Helly's property for convex subsets of a median algebra: by induction on $m \ge 2$, any $m$ pairwise intersecting convex subsets $K_1, \dots, K_m \subseteq A$ have nonempty intersection. For $m = 2$ this is immediate; for $m \ge 3$, choosing $a \in \bigcap_{i \neq 1} K_i$, $b \in \bigcap_{i \neq 2} K_i$, and $c \in K_1 \cap K_2$, at least two of $a, b, c$ belong to each $K_i$, so $m(a, b, c) \in \bigcap_{i=1}^m K_i$ by convexity (`Definition 2.2`).

Hence, for every $\varepsilon = (\varepsilon_1, \dots, \varepsilon_k) \in \{0, 1\}^k$, putting $H_i = x_i$ if $\varepsilon_i = 1$ and $H_i = x_i^\bullet$ if $\varepsilon_i = 0$, the convex sets $H_1, \dots, H_k$ are nonempty and pairwise intersect, so $\bigcap_{i=1}^k H_i \neq \emptyset$. Therefore the homomorphism $\psi \colon \mathbf{A} \to \mathbf{2}^k$ given by $\psi(a) = (x_1(a), \dots, x_k(a))$ is surjective. By `Lemma 7.1`, surjectivity of $\psi$ implies $r = \mathrm{rank}(\mathbf{A}) \ge \mathrm{rank}(\mathbf{2}^k) = k$. $\square$

---

### Two Topological Lemmas on Finite-Rank Bounded Poc Sets

For any subset $U \subseteq X$, let $\overline{U}$ and $\mathrm{int}(U)$ denote its closure and interior in $\mathbf{X}$, and set
$$A_U := \overline{U} \setminus U, \qquad B_U := U \setminus \mathrm{int}(U).$$
When $U$ is an ultrafilter of $\mathbf{X}$, we have $U^\bullet = U^c$. Since ${}^\bullet$ is a homeomorphism,
$$(A_U)^\bullet = (\overline{U} \setminus U)^\bullet = \overline{U^\bullet} \setminus U^\bullet = \overline{U^c} \setminus U^c = (X \setminus \mathrm{int}(U)) \setminus (X \setminus U) = U \setminus \mathrm{int}(U) = B_U.$$

**Lemma 2 (Finite boundary).** *Assume $\mathrm{rank}(\mathbf{A}) = r < \infty$. For every ultrafilter $U \in (\mathbf{X}^\flat)_+$,*
$$|A_U \setminus \{0\}| \;\le\; r.$$
*In particular, $|A_U| \le r + 1$, $|B_U| = |A_U| \le r + 1$, and the topological boundary $\partial U = A_U \cup B_U$ is finite and closed under ${}^\bullet$.*

*Proof.* Suppose for contradiction that $A_U \setminus \{0\}$ contains $r + 1$ distinct elements $z_1, \dots, z_{r+1}$. Because $1 \in U$ and $z_i \notin U$, we have $z_1, \dots, z_{r+1} \in X \setminus \{0, 1\}$. Choose a linear extension of the partial order $\le$ restricted to $\{z_1, \dots, z_{r+1}\}$, relabeling if necessary so that
$$1 \le h < i \le r + 1 \implies z_i \not\le z_h.$$
We construct $x_1, \dots, x_{r+1} \in U \setminus \{0, 1\}$ inductively. At step $i \in \{1, \dots, r+1\}$, assume $x_1, \dots, x_{i-1} \in U \setminus \{0, 1\}$ have been chosen so that for every $h < i$ and every $j > h$, we have $x_h^\bullet \not\le z_j$ and $z_j \not\le x_h$. Define the set
$$O_i \;:=\; (X \setminus \{0, 1\}) \;\cap\; \bigcap_{j = i+1}^{r+1} \Bigl((X \setminus z_j^\downarrow)^\bullet \cap (X \setminus z_j^\uparrow)\Bigr) \;\cap\; \bigcap_{h = 1}^{i-1} \Bigl((X \setminus x_h^\uparrow) \cap (X \setminus (x_h^\bullet)^\uparrow) \cap (X \setminus x_h^\downarrow)\Bigr).$$
Every set in this finite intersection is open in $X$ (because $\{0, 1\}$, $z^\downarrow$, and $z^\uparrow$ are closed and ${}^\bullet$ is a homeomorphism). We verify that $z_i \in O_i$:
1. $z_i \notin \{0, 1\}$.
2. For $j > i$: since $z_i \notin U$ and $U$ is an ultrafilter, $z_i^\bullet \in U$; since $U$ is an up-set and $z_j \notin U$, we have $z_i^\bullet \not\le z_j$, i.e., $z_i \in (X \setminus z_j^\downarrow)^\bullet$. Also $z_j \not\le z_i$ by the choice of linear extension, so $z_i \in X \setminus z_j^\uparrow$.
3. For $h < i$: since $x_h \in U$, $z_i \notin U$, and $U$ is an up-set, $x_h \not\le z_i$, so $z_i \in X \setminus x_h^\uparrow$. By the inductive hypothesis at step $h$ (with $j = i > h$), we have $x_h^\bullet \not\le z_i$ and $z_i \not\le x_h$, so $z_i \in (X \setminus (x_h^\bullet)^\uparrow) \cap (X \setminus x_h^\downarrow)$.

Thus $O_i$ is an open neighborhood of $z_i$. Since $z_i \in \overline{U}$, we may pick $x_i \in O_i \cap U$. By definition of $O_i$, $x_i \in U \setminus \{0, 1\}$ preserves the inductive hypotheses ($x_i^\bullet \not\le z_j$ and $z_j \not\le x_i$ for all $j > i$), and for every $h < i$:
- $x_h \not\le x_i$ (from $x_i \in X \setminus x_h^\uparrow$),
- $x_h^\bullet \not\le x_i$ (from $x_i \in X \setminus (x_h^\bullet)^\uparrow$),
- $x_i \not\le x_h$ (from $x_i \in X \setminus x_h^\downarrow$),
- $x_h \not\le x_i^\bullet$ (since $x_h, x_i \in U$, so $x_i^\bullet \notin U$, and $U$ is an up-set).

Hence $x_1, \dots, x_{r+1} \in X \setminus \{0, 1\}$ are $r + 1$ pairwise transverse elements, contradicting Lemma 1. $\square$

---

**Lemma 3 (Local upward cone at boundary points).** *Assume $\mathrm{rank}(\mathbf{A}) = r < \infty$. For every ultrafilter $U \in (\mathbf{X}^\flat)_+$ and every $t \in A_U = \overline{U} \setminus U$, there exists an open neighborhood $W_{t, U}$ of $t$ in $X$ such that*
$$W_{t, U} \cap U \;\subseteq\; t^\uparrow.$$

*Proof.* If $t = 0$, then $0^\uparrow = X$ and we take $W_{0, U} := X$. Assume now that $t \neq 0$; since $1 \in U$ and $t \notin U$, we have $t \in X \setminus \{0, 1\}$.

Suppose for contradiction that no open neighborhood $W$ of $t$ satisfies $W \cap U \subseteq t^\uparrow$, i.e., every open neighborhood of $t$ meets $U \setminus t^\uparrow$. We construct $y_1, \dots, y_{r+1} \in (U \setminus t^\uparrow) \setminus \{0, 1\}$ inductively. At step $k \in \{1, \dots, r+1\}$, assume $y_1, \dots, y_{k-1} \in (U \setminus t^\uparrow) \setminus \{0, 1\}$ have been chosen so that $y_i^\bullet \not\le t$ for all $i < k$. Define
$$O_k \;:=\; (X \setminus \{0, 1\}) \;\cap\; (X \setminus t^\downarrow)^\bullet \;\cap\; \bigcap_{i = 1}^{k-1} \Bigl((X \setminus y_i^\uparrow) \cap (X \setminus (y_i^\bullet)^\uparrow) \cap (X \setminus y_i^\downarrow)\Bigr).$$
Each factor is open in $X$, and $t \in O_k$:
- $t \notin \{0, 1\}$.
- $t^\bullet \in U$ and $t \notin U$ imply $t^\bullet \not\le t$, so $t \in (X \setminus t^\downarrow)^\bullet$.
- For each $i < k$: $y_i \in U$ and $t \notin U$ imply $y_i \not\le t$; $y_i^\bullet \not\le t$ holds by the inductive hypothesis; and $y_i \notin t^\uparrow$ means $t \not\le y_i$, i.e., $t \in X \setminus y_i^\downarrow$.

Hence $O_k$ is an open neighborhood of $t$, so by the contradiction assumption we may pick $y_k \in O_k \cap (U \setminus t^\uparrow)$. Then $y_k \in (U \setminus t^\uparrow) \setminus \{0, 1\}$, $y_k^\bullet \not\le t$ (from $y_k \in (X \setminus t^\downarrow)^\bullet$), and for every $i < k$:
- $y_i \not\le y_k$, $y_i^\bullet \not\le y_k$, and $y_k \not\le y_i$ (by definition of $O_k$),
- $y_i \not\le y_k^\bullet$ (since $y_i, y_k \in U$ and $U$ is an up-set).

Thus $y_1, \dots, y_{r+1} \in X \setminus \{0, 1\}$ are $r + 1$ pairwise transverse elements, contradicting Lemma 1. $\square$

---

### Construction of the Clopen Retraction Map and Embedding $\mathbf{B} \hookrightarrow \mathbf{A}$

Return to Case 2 ($\mathrm{rank}(\mathbf{A}) = r < \infty$) with the finite subalgebra $\mathbf{B} \le (\mathbf{X}^\flat)_+$.

**Step 0 (Finite ${}^\bullet$-closed witness/boundary set and initial clopen separation).**
For each unordered pair of distinct $U, V \in \mathbf{B}$, choose a witness point $w \in U \triangle V$. Let $W \subseteq X$ be the finite set consisting of all chosen witnesses and their involutes $w^\bullet$. Define
$$T \;:=\; \{0, 1\} \;\cup\; W \;\cup\; \bigcup_{U \in \mathbf{B}} (A_U \cup B_U).$$
By Lemma 2 and the finiteness of $\mathbf{B}$, $T$ is a finite subset of $X$ containing $0, 1$ and satisfying $T^\bullet = T$.

For each ordered pair $(s, t) \in T \times T$ with $s \not\le t$, pointwise clopen separation provides a clopen ultrafilter $C_{s, t} \subseteq X$ with $s \in C_{s, t}$ and $t \notin C_{s, t}$. Note that $C_{s, t}^c = (C_{s, t})^\bullet$ is a clopen down-set containing both $t$ and $s^\bullet$ (since $s \in C_{s, t} \iff s^\bullet \notin C_{s, t}$). For every $t \in T$, define the clopen down-set
$$D_t^{(0)} \;:=\; \bigcap_{\substack{s \in T \\ s \not\le t}} C_{s, t}^c \;\cap\; \bigcap_{\substack{u \in T \\ t^\bullet \not\le u}} C_{t^\bullet, u}^c$$
(with the convention that an empty intersection equals $X$), and set $E_s^{(0)} := (D_{s^\bullet}^{(0)})^\bullet$, which is a clopen up-set. Then:
1. $t \in D_t^{(0)}$ for every $t \in T$: $t \in C_{s, t}^c$ whenever $s \not\le t$, and $t = (t^\bullet)^\bullet \in C_{t^\bullet, u}^c$ whenever $t^\bullet \not\le u$. Consequently $s \in E_s^{(0)}$ for every $s \in T$.
2. Whenever $s, t \in T$ satisfy $s \not\le t$, we have $E_s^{(0)} \cap D_t^{(0)} = \emptyset$: indeed, $(s^\bullet)^\bullet = s \not\le t$ implies $D_{s^\bullet}^{(0)} \subseteq C_{s, t}^c$, hence $E_s^{(0)} = (D_{s^\bullet}^{(0)})^\bullet \subseteq (C_{s, t}^c)^\bullet = C_{s, t}$, while $D_t^{(0)} \subseteq C_{s, t}^c$.
3. Putting $N_t^{(0)} := D_t^{(0)} \cap E_t^{(0)}$, the sets $\{N_t^{(0)} \mid t \in T\}$ are pairwise disjoint (for $s \neq t$ in $T$, either $s \not\le t$ or $t \not\le s$).
4. Since $s \le 1$ and $0 \le u$ for all $s, u \in T$, both intersections defining $D_1^{(0)}$ are empty, so $D_1^{(0)} = X$ and $E_0^{(0)} = X$.

---

**Step 1 (Inductive bottom-up construction of clopen down-sets $D_t$).**
Choose a linear extension $t_1, t_2, \dots, t_m$ of $(T, \le)$ (so $r < t$ in $T$ implies $r$ precedes $t$; note $t_1 = 0$ and $t_m = 1$). For every $U \in \mathbf{B}$ and every $r \in A_U$, fix an open neighborhood $W_{r, U}$ of $r$ with $W_{r, U} \cap U \subseteq r^\uparrow$ using Lemma 3.

We define clopen down-sets $D_{t_1}, \dots, D_{t_m}$ inductively so that $t_k \in D_{t_k} \subseteq D_{t_k}^{(0)}$. At step $k$, write $t := t_k$ and suppose $D_r$ has been constructed for all $r \in T$ with $r < t$. For each $U \in \mathbf{B}$ such that $t \notin U$, define the open set
$$\Omega_{t, U} \;:=\; \begin{cases} W_{t, U} \;\cup\; \displaystyle\bigcup_{\substack{r \in T,\, r < t \\ r \in A_U}} (D_r \cap W_{r, U}) & \text{if } t \in A_U, \\[2ex] \displaystyle\bigcup_{\substack{r \in T,\, r < t \\ r \in A_U}} (D_r \cap W_{r, U}) & \text{if } t \notin A_U. \end{cases}$$
We verify that $t^\downarrow \cap \overline{U} \subseteq \Omega_{t, U}$: if $z \in t^\downarrow \cap \overline{U}$, then $z \le t$ and $t \notin U$ imply $z \notin U$ (as $U$ is an up-set), so $z \in \overline{U} \setminus U = A_U \subseteq T$. If $z = t$, then $t \in A_U$ and $z \in W_{t, U} \subseteq \Omega_{t, U}$; if $z < t$, then $z \in D_z$ (by induction) and $z \in W_{z, U}$, so $z \in D_z \cap W_{z, U} \subseteq \Omega_{t, U}$.

Hence the set
$$F_t \;:=\; \bigcup_{\substack{U \in \mathbf{B} \\ t \notin U}} (\overline{U} \setminus \Omega_{t, U})$$
is a closed (hence compact) subset of $X$ disjoint from $t^\downarrow$. Because $t^\downarrow$ is the intersection of all clopen down-sets containing $t$, for each $y \in F_t$ there is a clopen down-set $H_y \ni t$ with $y \notin H_y$. By compactness of $F_t$, finitely many open complements $H_{y_1}^c, \dots, H_{y_p}^c$ cover $F_t$ (taking $p = 0$ if $F_t = \emptyset$). Define
$$D_t \;:=\; D_t^{(0)} \cap \bigcap_{j=1}^p H_{y_j}.$$
Then $D_t$ is a clopen down-set with $t \in D_t \subseteq D_t^{(0)}$ and $D_t \cap F_t = \emptyset$. (In particular, for $t = 1$, no $U \in \mathbf{B}$ satisfies $1 \notin U$, so $F_1 = \emptyset$ and $D_1 = D_1^{(0)} = X$.)

---

**Step 2 (Symmetric clopen neighborhoods and boundary-capture inclusions).**
After all $D_t$ ($t \in T$) have been constructed, define for every $s \in T$:
$$E_s \;:=\; (D_{s^\bullet})^\bullet, \qquad N_s \;:=\; D_s \cap E_s.$$
Then:
- Each $E_s$ is a clopen up-set satisfying $s \in E_s \subseteq E_s^{(0)}$, hence $s^\uparrow \subseteq E_s$.
- Each $N_s$ is clopen with $s \in N_s \subseteq N_s^{(0)}$, so the sets $\{N_s \mid s \in T\}$ are pairwise disjoint.
- $(N_s)^\bullet = (D_s)^\bullet \cap (E_s)^\bullet = E_{s^\bullet} \cap D_{s^\bullet} = N_{s^\bullet}$ for all $s \in T$.

**Claim (I).** *For every $t \in T$ and every $U \in \mathbf{B}$ with $t \notin U$, we have $D_t \cap U \subseteq \bigcup_{r \in T} N_r$.*

*Proof of Claim (I).* Let $x \in D_t \cap U$. Since $x \in U \subseteq \overline{U}$ and $D_t \cap F_t = \emptyset$, we have $x \in \Omega_{t, U} \cap U$.
- If $t \in A_U$ and $x \in W_{t, U} \cap U$, then Lemma 3 gives $x \in t^\uparrow \subseteq E_t$; combined with $x \in D_t$, this yields $x \in D_t \cap E_t = N_t$.
- Otherwise, $x \in D_r \cap W_{r, U} \cap U$ for some $r \in T$ with $r < t$ and $r \in A_U$; Lemma 3 gives $x \in r^\uparrow \subseteq E_r$, and combined with $x \in D_r$, this yields $x \in D_r \cap E_r = N_r$. $\square$

**Claim (II).** *For every $s \in T$ and every $U \in \mathbf{B}$ with $s \in U$, we have $E_s \cap U^c \subseteq \bigcup_{q \in T} N_q$.*

*Proof of Claim (II).* Let $y \in E_s \cap U^c$, and set $t := s^\bullet \in T$ and $x := y^\bullet$. Since $U$ is an ultrafilter, $s \in U$ implies $t \notin U$, and $y \notin U$ implies $x \in U$. Moreover $y \in E_s = (D_t)^\bullet$ implies $x \in D_t$. By Claim (I), $x \in \bigcup_{r \in T} N_r$, and applying ${}^\bullet$ gives $y = x^\bullet \in \bigcup_{r \in T} (N_r)^\bullet = \bigcup_{r \in T} N_{r^\bullet} = \bigcup_{q \in T} N_q$. $\square$

---

**Step 3 (The clopen ultrafilter pullbacks $\widetilde{U} = \pi^{-1}(U)$ and the embedding $\mathbf{B} \hookrightarrow \mathbf{A}$).**
Set $K := X \setminus \bigcup_{t \in T} N_t$, which is clopen and satisfies $K^\bullet = K$. Define $\pi \colon X \to X$ by
$$\pi(x) \;:=\; \begin{cases} t & \text{if } x \in N_t \text{ (the unique } t \in T \text{ with } x \in N_t\text{)}, \\ x & \text{if } x \in K. \end{cases}$$
Because $N_{t^\bullet} = (N_t)^\bullet$ and $K^\bullet = K$, the map $\pi$ commutes with ${}^\bullet$: $\pi(x^\bullet) = \pi(x)^\bullet$ for all $x \in X$. Moreover $\pi(t) = t$ for every $t \in T$.

For each $U \in \mathbf{B}$, define $\widetilde{U} := \pi^{-1}(U) \subseteq X$. We verify that $\widetilde{U}$ is a **clopen ultrafilter** of $\mathbf{X}$:
1. **Clopenness:** We have $\widetilde{U} = (U \cap K) \cup \bigcup_{t \in T \cap U} N_t$. Each $N_t$ and $K$ is clopen. Because $A_U \subseteq T \subseteq X \setminus K$, we have $\overline{U \cap K} \subseteq \overline{U} \cap K = (U \cup A_U) \cap K = U \cap K$, so $U \cap K$ is closed in $X$. Because $B_U \subseteq T \subseteq X \setminus K$, we have $U \cap K = (U \setminus B_U) \cap K = \mathrm{int}(U) \cap K$, so $U \cap K$ is open in $X$. Hence $\widetilde{U}$ is clopen in $X$.
2. **Bounds and involution:** Since $0, 1 \in T$, $\pi(0) = 0 \notin U$ and $\pi(1) = 1 \in U$, so $0 \notin \widetilde{U}$ and $1 \in \widetilde{U}$. Since $\pi(x^\bullet) = \pi(x)^\bullet$ and $U^\bullet = U^c$, we have $x \in \widetilde{U} \iff \pi(x) \in U \iff \pi(x)^\bullet \notin U \iff \pi(x^\bullet) \notin U \iff x^\bullet \notin \widetilde{U}$.
3. **Up-set property:** Let $x \le y$ in $X$ with $x \in \widetilde{U}$ (i.e., $\pi(x) \in U$). We check $\pi(y) \in U$ in all four cases:
   - *$x \in K, y \in K$:* $x = \pi(x) \in U$ and $x \le y$ imply $y = \pi(y) \in U$, since $U$ is an up-set.
   - *$x \in N_s, y \in N_t$ ($s, t \in T$):* Since $x \in E_s \subseteq E_s^{(0)}$, $x \le y$, and $E_s^{(0)}$ is an up-set, we have $y \in E_s^{(0)} \cap D_t^{(0)}$. By Step 0(2), this forces $s \le t$. Since $s = \pi(x) \in U$ and $U$ is an up-set, $t = \pi(y) \in U$.
   - *$x \in N_s, y \in K$ ($s \in T$):* Here $s = \pi(x) \in U$. Since $x \in E_s$, $x \le y$, and $E_s$ is an up-set, $y \in E_s$. If $y \notin U$, then Claim (II) yields $y \in E_s \cap U^c \subseteq \bigcup_{q \in T} N_q = X \setminus K$, contradicting $y \in K$. Thus $y = \pi(y) \in U$.
   - *$x \in K, y \in N_t$ ($t \in T$):* Here $x = \pi(x) \in U$. Since $y \in D_t$, $x \le y$, and $D_t$ is a down-set, $x \in D_t$. If $t \notin U$, then Claim (I) yields $x \in D_t \cap U \subseteq \bigcup_{r \in T} N_r = X \setminus K$, contradicting $x \in K$. Thus $t = \pi(y) \in U$.

Thus every $\widetilde{U}$ ($U \in \mathbf{B}$) is a clopen ultrafilter of $\mathbf{X}$, so its characteristic function belongs to $\mathbf{X}_* = \mathsf{Poc}_\tau(\mathbf{X}, \utilde{\mathbf{2}}_\tau)$. By strong duality (`Theorem 3.4(1)`), for each $U \in \mathbf{B}$ there is a unique element $a_U \in \mathbf{A}$ with $e_{\mathbf{A}}(a_U) = \chi_{\widetilde{U}}$.

Finally, because $\widetilde{U} = \pi^{-1}(U)$ is a set-theoretic preimage, it preserves intersections and unions, hence for all $U_1, U_2, U_3 \in \mathbf{B}$:
$$m(\widetilde{U}_1, \widetilde{U}_2, \widetilde{U}_3) = (\widetilde{U}_1 \cap \widetilde{U}_2) \cup (\widetilde{U}_1 \cap \widetilde{U}_3) \cup (\widetilde{U}_2 \cap \widetilde{U}_3) = \pi^{-1}\bigl(m(U_1, U_2, U_3)\bigr) = \widetilde{m(U_1, U_2, U_3)}.$$
Thus $U \mapsto a_U$ is a median algebra homomorphism $\mathbf{B} \to \mathbf{A}$. For any distinct $U, V \in \mathbf{B}$, the witness set $W \subseteq T$ contains $w \in U \triangle V$; since $\pi(w) = w$, we have $w \in \widetilde{U} \triangle \widetilde{V}$, whence $\widetilde{U} \neq \widetilde{V}$ and $a_U \neq a_V$. Therefore $U \mapsto a_U$ is an embedding of $\mathbf{B}$ into $\mathbf{A}$. $\blacksquare$

---

## Remark on the Role of Bounds ($0, 1$) vs. Unbounded Median Algebras

For $(0, 1)$-bounded distributive lattices $L = \mathrm{ClopUp}(P)$, universal sentences in $\{ \wedge, \vee, 0, 1 \}$ need not transfer to $L^\delta = \mathcal{U}(P)$: in the infinite-width zig-zag Priestley space $P = (\mathbb{N} \cup \{\infty\}) \times \{0, 1\}$ with $(n, 0) < (n, 1)$, $(n, 0) < (n+1, 1)$, and $(\infty, 0) < (\infty, 1)$, $\mathcal{U}(P)$ has a nontrivial complemented pair while $\mathrm{ClopUp}(P)$ does not. In the language $L_{\mathsf{M}} = \{m\}$ without $0, 1$ constants, this infinite-width obstruction vanishes via Case 1 ($\mathrm{rank}(\mathbf{A}) = \infty \implies \mathbf{2}^d \hookrightarrow \mathbf{A}$ for all $d$), whereas finite-rank bounded poc sets force every ultrafilter to have finite topological boundary (Lemma 2) and local upward cones (Lemma 3), enabling the symmetric clopen retraction $\pi$ of Steps 0–3.

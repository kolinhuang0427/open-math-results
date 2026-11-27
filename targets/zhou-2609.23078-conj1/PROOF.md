# Proof of Conjecture 1 of You Zhou (arXiv:2609.23078v1) in All Finite Types

## Target Statement

**Conjecture 1 (`conj:main1-all-types`, You Zhou, *Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module*, arXiv:2609.23078v1, §1 & §4, Conjecture 4.1):**
Let $\mathfrak{g}$ be any finite-dimensional complex simple Lie algebra with index set $I$, Cartan subalgebra $\mathfrak{h}$, simple roots $\{\alpha_i\}_{i \in I} \subset \mathfrak{h}^*$, simple coroots $\{\alpha_i^\vee\}_{i \in I} \subset \mathfrak{h}$, fundamental weights $\{\varpi_i\}_{i \in I}$, fundamental coweights $\{\varpi_i^\vee\}_{i \in I}$, root lattice $Q = \bigoplus_{i \in I} \mathbb{Z}\alpha_i$, positive root cone $Q^+ = \bigoplus_{i \in I} \mathbb{Z}_{\ge 0}\alpha_i$, dominant integral weights $P^+$, Weyl group $W$ with longest element $w_\circ$, and $\rho = \sum_{i \in I} \varpi_i$.

For every $\lambda \in P^+$, let $\mathcal{B}(\lambda)$ be the Kashiwara crystal basis of the irreducible highest-weight module $V(\lambda)$ with highest element $b_\lambda$ and lowest element $b_{w_\circ \lambda}$, and let:
- $\check{e}_i(b) := \tilde{f}_i \tilde{e}_i^{\max}(b)$ if $\tilde{e}_i(b) \ne 0$, and $\check{e}_i(b) := b$ if $\tilde{e}_i(b) = 0$;
- $\check{e}_{w_\circ} := \check{e}_{i_1} \cdots \check{e}_{i_\ell}$ for any reduced expression $w_\circ = s_{i_1} \cdots s_{i_\ell}$ (well-defined independently of the reduced expression by Proposition 3.12 of Zhou, since $\tilde{e}_i^{\max}(b_\rho \otimes b) = b_\rho \otimes \check{e}_i(b)$);
- $b_\star := \check{e}_{w_\circ}(b_{w_\circ \lambda})$, $\mathcal{C}_{b_\star} := \{c \in \mathcal{B}(\lambda) \mid \check{e}_{w_\circ}(c) = b_\star\}$, $\mathcal{F}(b_\star) := \{\tilde{f}_{i_1} \cdots \tilde{f}_{i_r}(b_\star) \mid r \ge 0,\ i_1, \dots, i_r \in I\} \setminus \{0\}$;
- $\Gamma_\lambda := \{b \in \mathcal{B}(\lambda) \mid \langle b \rangle_{\mathrm{Ext}} = \mathcal{B}(\lambda)\}$, where $\langle b \rangle_{\mathrm{Ext}}$ is the smallest extremal subset of $\mathcal{B}(\lambda)$ containing $b$.

Then for every finite-dimensional simple Lie algebra $\mathfrak{g}$ (all types $A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2$) and every $\lambda \in P^+$,
$$\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star},$$
and consequently $\mathcal{B}(\lambda) \setminus \mathcal{F}(b_\star)$ is the unique maximal proper extremal subset of $\mathcal{B}(\lambda)$.

---

## Proof Overview

You Zhou proved Conjecture 1 in type $A_{n-1}$ (`Theorem 1` / Theorem 4.4 / `thm:main1`) via a single type-$A$-specific ingredient (`Proposition 7.2` / `prop:w0Tgew0fiT`), established there using Greene's theorem, Dilworth's theorem, and the plactic monoid on semistandard Young tableaux:
$$\mathrm{wt}\bigl(\check{e}_{w_\circ}(b)\bigr) \ge \mathrm{wt}\bigl(\check{e}_{w_\circ}(\tilde{f}_i(b))\bigr) \qquad \text{whenever } b \in \mathcal{B}(\lambda),\ i \in I,\ \tilde{f}_i(b) \ne 0,$$
where $\mu_1 \ge \mu_2$ denotes the dominance order $\mu_1 - \mu_2 \in Q^+$.

We prove a strictly stronger **general tensor dominance monotonicity theorem** valid uniformly in **every** finite simple Lie type $\mathfrak{g}$ and for **arbitrary** $\mu, \lambda \in P^+$, $a \in \mathcal{B}(\mu)$, $b \in \mathcal{B}(\lambda)$: letting $H(x) := \mathrm{wt}(\tilde{e}_{w_\circ}^{\max}(x)) \in P^+$ denote the highest weight of the connected component $C(x) \subseteq \mathcal{B}(\mu) \otimes \mathcal{B}(\lambda)$,
$$H(a \otimes b) \ge H\bigl(a \otimes \tilde{f}_i(b)\bigr) \qquad (\text{whenever } \tilde{f}_i(b) \ne 0),$$
and dually $H(\tilde{f}_i(a) \otimes b) \ge H(a \otimes b)$ (whenever $\tilde{f}_i(a) \ne 0$).

The proof works in the Littelmann path model $\mathcal{P}(\mu) * \mathcal{P}(\lambda) \cong \mathcal{B}(\mu) \otimes \mathcal{B}(\lambda)$ together with the path-ordered exponential $g(\beta \eta)$ in the Langlands dual Lie algebra $\mathfrak{g}^\vee$ (inspired by Biane–Bougerol–O'Connell's continuous crystal and geometric Pitman transform, but completely self-contained here):
1. **Positivity in $\mathfrak{g}^\vee$ (Lemma 1):** Using Lusztig's canonical basis positivity for simply-laced Lie algebras together with diagram-automorphism folding $\mathfrak{g}^\vee = (\tilde{\mathfrak{g}}^\vee)^\sigma$ for non-simply-laced types, every $k \in I$ admits a $\mathfrak{g}^\vee$-module $V_k$ with a weight basis $\mathbf{B}_k$ in which all Chevalley generators $e_j^\vee, f_j^\vee$ have non-negative integer matrix entries, and extremal basis vectors $v_+ \in (V_k)_{\varpi_k^\vee}$, $v_- \in (V_k)_{w_\circ \varpi_k^\vee}$.
2. **Exact Gauge Identity (Lemma 2):** A 6-line ODE calculation proves $g(\psi_u)(t) = \exp(a(t) f_j^\vee)\, g(\psi)(t)\, \exp(-b f_j^\vee)$ for any shift $\psi_u(t) = \psi(t) + (\log u(t))\alpha_j$ with $u' = -b\, e^{-\langle \psi, \alpha_j^\vee \rangle}$.
3. **Tropical Limit & Pitman Invariance (Lemmas 3–4):** Taking $b = -1$ yields exact invariance of the extremal matrix entry $Z_k(\beta; \eta) = \langle v_+, g(\beta \eta) v_- \rangle$ under the geometric Pitman transform, and letting $\beta \to \infty$ gives $\langle H(a \otimes b), \varpi_k^\vee \rangle = M_k(\pi_1 * \pi_2)$.
4. **Positivity Monotonicity (Theorem 1):** Taking $b = b_\beta > 0$ on the second factor $\pi_2$ gives $Z_k(\beta; \pi_1 * \pi_2) = \langle v_+, g(\beta \pi_{2,\beta}) \exp(+b_\beta f_i^\vee) g(\beta \pi_1) v_- \rangle \ge Z_k(\beta; \pi_1 * \pi_{2,\beta})$ entry-by-entry because $\exp(+b_\beta f_i^\vee) \ge I$. Sending $\beta \to \infty$ yields $\langle H(a \otimes b), \varpi_k^\vee \rangle \ge \langle H(a \otimes \tilde{f}_i(b)), \varpi_k^\vee \rangle$ for every $k \in I$, hence $H(a \otimes b) - H(a \otimes \tilde{f}_i(b)) \in Q^+$.
5. **Deduction of Conjecture 1 (Theorem 2):** Specializing to $\mu = \rho$, $a = b_\rho$, shows that $\nu_0 := H(b_\rho \otimes b_{w_\circ \lambda})$ is the unique minimal highest weight of $V(\rho) \otimes V(\lambda)$, hence equals the PRV highest weight $\overline{\rho + w_\circ \lambda}$ (by PRV 1967, Theorem 2.1), and a 6-line cyclic-vector proof shows $\mathrm{mult}_{V(\rho) \otimes V(\lambda)}(V(\nu_0)) = 1$. This immediately yields $\mathcal{F}(\mathcal{C}_{b_\star}) \subseteq \mathcal{C}_{b_\star}$, hence $\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$ for every finite simple $\mathfrak{g}$ and every $\lambda \in P^+$.

---

## Conventions and Setup

Let $A = (a_{ij})_{i,j \in I}$ be the Cartan matrix of $\mathfrak{g}$, with $a_{ij} = \langle \alpha_j, \alpha_i^\vee \rangle$. We follow the Hong–Kang / You Zhou crystal tensor product convention (Hong–Kang 2002, §4.4; Zhou §2 & Proposition 3.12): for crystals $\mathcal{B}_1, \mathcal{B}_2$,
$$\mathrm{wt}(b_1 \otimes b_2) = \mathrm{wt}(b_1) + \mathrm{wt}(b_2), \qquad \varepsilon_i(b_1 \otimes b_2) = \max\bigl(\varepsilon_i(b_1),\ \varepsilon_i(b_2) - \langle \mathrm{wt}(b_1), \alpha_i^\vee \rangle\bigr),$$
$$\tilde{e}_i(b_1 \otimes b_2) = \begin{cases} \tilde{e}_i(b_1) \otimes b_2 & \text{if } \varphi_i(b_1) \ge \varepsilon_i(b_2), \\ b_1 \otimes \tilde{e}_i(b_2) & \text{if } \varphi_i(b_1) < \varepsilon_i(b_2), \end{cases} \qquad \tilde{f}_i(b_1 \otimes b_2) = \begin{cases} \tilde{f}_i(b_1) \otimes b_2 & \text{if } \varphi_i(b_1) > \varepsilon_i(b_2), \\ b_1 \otimes \tilde{f}_i(b_2) & \text{if } \varphi_i(b_1) \le \varepsilon_i(b_2). \end{cases}$$

Let $\mathfrak{g}^\vee$ be the Langlands dual complex simple Lie algebra, whose Cartan subalgebra we identify with $\mathfrak{h}^\vee := \mathfrak{h}^*$ (so weights of $\mathfrak{g}^\vee$ lie in $(\mathfrak{h}^\vee)^* = \mathfrak{h}$). Its simple roots are $\{\alpha_j^\vee\}_{j \in I} \subset \mathfrak{h}$, its simple coroots are $\{h_j^\vee := \alpha_j\}_{j \in I} \subset \mathfrak{h}^* = \mathfrak{h}^\vee$, its fundamental weights are $\{\varpi_k^\vee\}_{k \in I} \subset \mathfrak{h}$ satisfying $\langle \alpha_j, \varpi_k^\vee \rangle = \delta_{jk}$, and its Chevalley generators $\{e_j^\vee, f_j^\vee, h_j^\vee\}_{j \in I}$ satisfy, for all $x \in \mathfrak{h}^\vee = \mathfrak{h}^*$ and $i, j \in I$:
$$[x, e_j^\vee] = \langle x, \alpha_j^\vee \rangle e_j^\vee, \qquad [x, f_j^\vee] = -\langle x, \alpha_j^\vee \rangle f_j^\vee, \qquad [e_i^\vee, f_j^\vee] = \delta_{ij} \alpha_i.$$

---

## Section 1: Positive Representation Realization in $\mathfrak{g}^\vee$

### Lemma 1 (Non-negative Chevalley Realization for Every $k \in I$)
*For every finite-dimensional simple Lie algebra $\mathfrak{g}$ and every $k \in I$, there exists a finite-dimensional $\mathfrak{g}^\vee$-module $V_k$ equipped with a weight basis $\mathbf{B}_k$ and basis vectors $v_+, v_- \in \mathbf{B}_k$ of $\mathfrak{g}^\vee$-weights $\varpi_k^\vee$ and $w_\circ \varpi_k^\vee$, respectively, such that:*
1. *Every Chevalley generator $e_j^\vee$ and $f_j^\vee$ ($j \in I$) has all matrix entries in $\mathbb{Z}_{\ge 0}$ with respect to $\mathbf{B}_k$.*
2. *Let $\langle v_+ | \in V_k^*$ be the dual basis functional to $v_+ \in \mathbf{B}_k$ ($\langle v_+ | v_+ \rangle = 1$ and $\langle v_+ | v \rangle = 0$ for $v \in \mathbf{B}_k \setminus \{v_+\}$). Then $\langle v_+ | f_j^\vee = 0$ and $f_j^\vee v_- = 0$ for all $j \in I$.*
3. *Let $m := \mathrm{ht}(\varpi_k^\vee - w_\circ \varpi_k^\vee) \in \mathbb{Z}_{\ge 1}$ be the sum of the coefficients of $\varpi_k^\vee - w_\circ \varpi_k^\vee$ in the basis $\{\alpha_j^\vee\}_{j \in I}$. The set*
   $$\mathcal{W}_k := \bigl\{\mathbf{j} = (j_1, \dots, j_m) \in I^m \;\big|\; c_{\mathbf{j}} := \langle v_+, e_{j_m}^\vee \cdots e_{j_1}^\vee v_- \rangle > 0\bigr\}$$
   *is nonempty, every $\mathbf{j} \in \mathcal{W}_k$ satisfies $\sum_{r=1}^m \alpha_{j_r}^\vee = \varpi_k^\vee - w_\circ \varpi_k^\vee$, and $\langle v_+, e_{j_r}^\vee \cdots e_{j_1}^\vee v_- \rangle = 0$ for every tuple $(j_1, \dots, j_r)$ with $r \ne m$.*

#### Proof
We treat simply-laced and non-simply-laced $\mathfrak{g}^\vee$ uniformly via folding.

**Case 1: $\mathfrak{g}^\vee$ is simply-laced (types $A_n, D_n, E_6, E_7, E_8$).**
Take $V_k := V_{\mathfrak{g}^\vee}(\varpi_k^\vee)$, the $k$-th fundamental irreducible representation of $\mathfrak{g}^\vee$, and let $\mathbf{B}_k$ be Lusztig's canonical basis of $V_k$ specialized at $q = 1$ (Lusztig, *Introduction to Quantum Groups*, Birkhäuser 1993, Chapter 14 & Theorem 22.1.7). By Theorem 22.1.7 of Lusztig (1993), $\mathbf{B}_k$ is a weight basis in which every $e_j^\vee$ and $f_j^\vee$ ($j \in I$) acts with matrix entries in $\mathbb{Z}_{\ge 0}$, establishing (1). The highest weight space $(V_k)_{\varpi_k^\vee}$ and lowest weight space $(V_k)_{w_\circ \varpi_k^\vee}$ are $1$-dimensional, spanned by unique basis vectors $v_+, v_- \in \mathbf{B}_k$. Since $f_j^\vee$ lowers weight by $\alpha_j^\vee$, for every $v \in \mathbf{B}_k$ the vector $f_j^\vee v$ has weight $\mathrm{wt}(v) - \alpha_j^\vee \le \varpi_k^\vee - \alpha_j^\vee < \varpi_k^\vee$, so its $v_+$-coefficient vanishes; thus $\langle v_+ | f_j^\vee = 0$. Similarly, $w_\circ \varpi_k^\vee - \alpha_j^\vee$ is not a weight of $V_k$, so $f_j^\vee v_- = 0$, proving (2). Since $e_{j_r}^\vee \cdots e_{j_1}^\vee v_-$ has weight $w_\circ \varpi_k^\vee + \sum_{q=1}^r \alpha_{j_q}^\vee$, its $v_+$-coefficient can be nonzero only when $\sum_{q=1}^r \alpha_{j_q}^\vee = \varpi_k^\vee - w_\circ \varpi_k^\vee$, which forces $r = m$; by (1), $c_{\mathbf{j}} \in \mathbb{Z}_{\ge 0}$ for all $\mathbf{j} \in I^m$. Finally, since $V_k$ is irreducible, $U(\mathfrak{n}_+^\vee) v_- = V_k \ni v_+$, so $c_{\mathbf{j}} > 0$ for at least one $\mathbf{j} \in I^m$, proving (3).

**Case 2: $\mathfrak{g}^\vee$ is non-simply-laced (types $B_n, C_n, F_4, G_2$).**
Realize $\mathfrak{g}^\vee$ as the fixed-point subalgebra $(\tilde{\mathfrak{g}}^\vee)^\sigma$ of a simply-laced simple Lie algebra $\tilde{\mathfrak{g}}^\vee$ (specifically $D_{n+1} \to B_n$, $A_{2n-1} \to C_n$, $E_6 \to F_4$, $D_4 \to G_2$) under a Dynkin diagram automorphism $\sigma$ whose orbits $\mathcal{O}_j \subset \tilde{I}$ ($j \in I$) contain no adjacent vertices. Denoting the Chevalley generators of $\tilde{\mathfrak{g}}^\vee$ by $\tilde{e}_{j'}^\vee, \tilde{f}_{j'}^\vee, \tilde{h}_{j'}^\vee$ ($j' \in \tilde{I}$), the embedding $\mathfrak{g}^\vee \hookrightarrow \tilde{\mathfrak{g}}^\vee$ is given by
$$e_j^\vee = \sum_{j' \in \mathcal{O}_j} \tilde{e}_{j'}^\vee, \qquad f_j^\vee = \sum_{j' \in \mathcal{O}_j} \tilde{f}_{j'}^\vee, \qquad h_j^\vee = \sum_{j' \in \mathcal{O}_j} \tilde{h}_{j'}^\vee \qquad (j \in I).$$
(Because no two nodes in $\mathcal{O}_j$ are joined by an edge, $[\tilde{e}_{j_1'}^\vee, \tilde{f}_{j_2'}^\vee] = 0$ for distinct $j_1', j_2' \in \mathcal{O}_j$, and $[h_i^\vee, e_j^\vee] = \sum_{j' \in \mathcal{O}_j} (\sum_{i' \in \mathcal{O}_i} \tilde{a}_{i' j'}) \tilde{e}_{j'}^\vee = a_{ji} e_j^\vee$ matches the Cartan matrix $A^\top$ of $\mathfrak{g}^\vee$; in particular, every simple root $\tilde{\alpha}_{j'}^\vee$ with $j' \in \mathcal{O}_j$ restricts to $\alpha_j^\vee$ on $\mathfrak{h}^\vee = (\tilde{\mathfrak{h}}^\vee)^\sigma$.)

For a given $k \in I$, pick any $k' \in \mathcal{O}_k$ and let $V_k := V_{\tilde{\mathfrak{g}}^\vee}(\tilde{\varpi}_{k'}^\vee)$ viewed as a $\mathfrak{g}^\vee$-module by restriction, with $\mathbf{B}_k$ being Lusztig's canonical basis of $V_{\tilde{\mathfrak{g}}^\vee}(\tilde{\varpi}_{k'}^\vee)$ at $q = 1$, and $v_+ := v_{\tilde{\varpi}_{k'}^\vee}$, $v_- := v_{\tilde{w}_\circ \tilde{\varpi}_{k'}^\vee} \in \mathbf{B}_k$.
- Since each $\tilde{e}_{j'}^\vee, \tilde{f}_{j'}^\vee$ has matrix entries in $\mathbb{Z}_{\ge 0}$ in $\mathbf{B}_k$ (Lusztig 1993, Theorem 22.1.7), so do their sums $e_j^\vee$ and $f_j^\vee$, giving (1).
- For every $j' \in \tilde{I}$, $\langle v_+ | \tilde{f}_{j'}^\vee = 0$ and $\tilde{f}_{j'}^\vee v_- = 0$, so summing over $j' \in \mathcal{O}_j$ gives $\langle v_+ | f_j^\vee = 0$ and $f_j^\vee v_- = 0$, giving (2).
- On $\mathfrak{h}^\vee$, $h_j^\vee v_+ = \sum_{j' \in \mathcal{O}_j} \tilde{\varpi}_{k'}^\vee(\tilde{h}_{j'}^\vee) v_+ = \delta_{jk} v_+$, so $\mathrm{wt}_{\mathfrak{g}^\vee}(v_+) = \varpi_k^\vee$. Since $\sigma$ preserves positive roots of $\tilde{\mathfrak{g}}^\vee$, the longest element $\tilde{w}_\circ \in \tilde{W}$ is $\sigma$-fixed and restricts to $w_\circ \in W$ on $\mathfrak{h}^\vee$; hence $\mathrm{wt}_{\mathfrak{g}^\vee}(v_-) = w_\circ \varpi_k^\vee$.
- Every $\tilde{\mathfrak{g}}^\vee$-weight $\tilde{\gamma}$ of $V_k$ satisfies $\tilde{\gamma} - \tilde{w}_\circ \tilde{\varpi}_{k'}^\vee = \sum_{j' \in \tilde{I}} n_{j'} \tilde{\alpha}_{j'}^\vee$ with $n_{j'} \in \mathbb{Z}_{\ge 0}$. Restricting to $\mathfrak{h}^\vee$ yields $\mathrm{wt}_{\mathfrak{g}^\vee}(\tilde{\gamma}) - w_\circ \varpi_k^\vee = \sum_{j \in I} (\sum_{j' \in \mathcal{O}_j} n_{j'}) \alpha_j^\vee$. By linear independence of $\{\alpha_j^\vee\}_{j \in I}$ and non-negativity of $n_{j'}$, $\mathrm{wt}_{\mathfrak{g}^\vee}(\tilde{\gamma}) = w_\circ \varpi_k^\vee$ holds if and only if $n_{j'} = 0$ for all $j' \in \tilde{I}$, i.e., $\tilde{\gamma} = \tilde{w}_\circ \tilde{\varpi}_{k'}^\vee$. Hence the $w_\circ \varpi_k^\vee$-weight space of $V_k$ as a $\mathfrak{g}^\vee$-module is $1$-dimensional, spanned by $v_-$.
- Finally, $e_j^\vee v_+ = 0$ for all $j \in I$, so the $\mathfrak{g}^\vee$-submodule $U(\mathfrak{g}^\vee) v_+ \subseteq V_k$ is irreducible and isomorphic to $V_{\mathfrak{g}^\vee}(\varpi_k^\vee)$. Its lowest weight space has weight $w_\circ \varpi_k^\vee$, which is $1$-dimensional in $V_k$ and spanned by $v_-$; therefore $v_- \in U(\mathfrak{g}^\vee) v_+$. By irreducibility of $U(\mathfrak{g}^\vee) v_+$, $v_+ \in U(\mathfrak{n}_+^\vee) v_-$, so $\mathcal{W}_k$ is nonempty. The remaining assertions of (3) follow from weight grading exactly as in Case 1. $\square$

---

## Section 2: Path-Ordered Exponential and the Exact Gauge Identity

Fix $k \in I$ and let $(V_k, \mathbf{B}_k, v_+, v_-)$ be given by Lemma 1. Every $x \in \mathfrak{h}^\vee = \mathfrak{h}^*$ acts diagonally on $\mathbf{B}_k$ via $x \cdot v = \langle x, \mathrm{wt}_{\mathfrak{g}^\vee}(v) \rangle v$, so $e^x \in \mathrm{GL}(V_k)$ is diagonal with strictly positive entries in $\mathbf{B}_k$.

For any continuous piecewise-$C^1$ path $\psi \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ with $\psi(0) = 0$ ($T > 0$), let $U(\psi) \colon [0, T] \to \mathrm{GL}(V_k)$ be the unique $C^1$ solution of the linear initial value problem
$$\dot{U}(t) = A_\psi(t)\, U(t), \qquad A_\psi(t) := \sum_{j \in I} e^{-\langle \psi(t), \alpha_j^\vee \rangle} e_j^\vee, \qquad U(0) = I,$$
and define
$$g(\psi)(t) := e^{\psi(t)} U(\psi)(t) \in \mathrm{GL}(V_k), \qquad Z_k(\beta; \psi) := \langle v_+,\ g(\beta \psi)(T)\, v_- \rangle \quad (\beta > 0).$$

### Lemma 2 (Dyson Expansion, Concatenation, and Exact Gauge Identity)
*Let $\psi \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ be continuous and piecewise-$C^1$ with $\psi(0) = 0$.*
1. *(Positivity and Dyson expansion.) For every $t \in [0, T]$, all matrix entries of $g(\psi)(t)$ in $\mathbf{B}_k$ are non-negative. Moreover, for all $\beta > 0$,*
   $$Z_k(\beta; \psi) = \sum_{\mathbf{j} \in \mathcal{W}_k} c_{\mathbf{j}} \int_{0 \le s_1 \le \dots \le s_m \le T} \exp\Biggl(\beta\Bigl(\langle \psi(T), \varpi_k^\vee \rangle - \sum_{r=1}^m \langle \psi(s_r), \alpha_{j_r}^\vee \rangle\Bigr)\Biggr) ds_1 \cdots ds_m.$$
2. *(Concatenation.) If $\psi_1, \psi_2 \colon [0, 1] \to \mathfrak{h}_\mathbb{R}^*$ are continuous piecewise-$C^1$ with $\psi_1(0) = \psi_2(0) = 0$, and $\psi_1 * \psi_2 \colon [0, 2] \to \mathfrak{h}_\mathbb{R}^*$ is defined by $(\psi_1 * \psi_2)(t) = \psi_1(t)$ on $[0, 1]$ and $\psi_1(1) + \psi_2(t - 1)$ on $[1, 2]$, then*
   $$g(\psi_1 * \psi_2)(2) = g(\psi_2)(1)\, g(\psi_1)(1).$$
3. *(Exact Gauge Identity.) Fix $j \in I$, set $h(t) := \langle \psi(t), \alpha_j^\vee \rangle$, and let $u \colon [0, T] \to (0, \infty)$ be a $C^1$ function satisfying $u(0) = 1$ and $u'(t) = -b\, e^{-h(t)}$ for a constant $b \in \mathbb{R}$. Define*
   $$\psi_u(t) := \psi(t) + \bigl(\log u(t)\bigr)\alpha_j, \qquad a(t) := \frac{b}{u(t)\, e^{h(t)}}, \qquad y_j(s) := \exp(s\, f_j^\vee).$$
   *Then for all $t \in [0, T]$,*
   $$g(\psi_u)(t) = y_j\bigl(a(t)\bigr) \cdot g(\psi)(t) \cdot y_j(-b).$$

#### Proof
**(1)** Since each $e_j^\vee$ is nilpotent and strictly weight-raising on the finite-dimensional module $V_k$, the Picard–Dyson series for $U(\psi)(t)$ terminates at finite order:
$$U(\psi)(t) = I + \sum_{r \ge 1} \sum_{j_1, \dots, j_r \in I} \Biggl(\int_{0 \le s_1 \le \dots \le s_r \le t} \exp\Bigl(-\sum_{q=1}^r \langle \psi(s_q), \alpha_{j_q}^\vee \rangle\Bigr) ds_1 \cdots ds_r\Biggr) e_{j_r}^\vee \cdots e_{j_1}^\vee.$$
By Lemma 1(1), every $e_j^\vee$ has non-negative entries in $\mathbf{B}_k$, and $e^{\psi(t)}$ is positive diagonal, so $g(\psi)(t) = e^{\psi(t)} U(\psi)(t)$ has all matrix entries $\ge 0$ in $\mathbf{B}_k$. Replacing $\psi$ by $\beta \psi$, evaluating at $t = T$, noting $\langle v_+ | e^{\beta \psi(T)} = e^{\beta \langle \psi(T), \varpi_k^\vee \rangle} \langle v_+ |$, and applying Lemma 1(3) immediately gives the stated formula for $Z_k(\beta; \psi)$.

**(2)** On every subinterval of $[0, T]$ where $\psi$ is $C^1$, differentiating $g(\psi)(t) = e^{\psi(t)} U(\psi)(t)$ and using $e^{\psi(t)} e_j^\vee e^{-\psi(t)} = e^{\langle \psi(t), \alpha_j^\vee \rangle} e_j^\vee$ yields
$$\frac{d}{dt} g(\psi)(t) = \Bigl(\dot{\psi}(t) + \sum_{r \in I} e_r^\vee\Bigr) g(\psi)(t). \tag{$\ast$}$$
Now consider $\psi_1 * \psi_2$ on $[0, 2]$. On $[0, 1]$, $g(\psi_1 * \psi_2)(t) = g(\psi_1)(t)$, so at $t = 1$ we have $g(\psi_1 * \psi_2)(1) = g(\psi_1)(1)$. On $[1, 2]$, the continuous piecewise-$C^1$ function $G(t) := g(\psi_2)(t - 1)\, g(\psi_1)(1)$ satisfies $G(1) = g(\psi_1)(1)$ and, on every smooth subinterval of $[1, 2]$,
$$\dot{G}(t) = \Bigl(\dot{\psi}_2(t - 1) + \sum_{r \in I} e_r^\vee\Bigr) G(t) = \Bigl(\frac{d}{dt}(\psi_1 * \psi_2)(t) + \sum_{r \in I} e_r^\vee\Bigr) G(t).$$
By uniqueness of continuous piecewise-$C^1$ solutions to $(\ast)$ across the finitely many breakpoints, $g(\psi_1 * \psi_2)(t) = G(t)$ for all $t \in [1, 2]$; evaluating at $t = 2$ gives $g(\psi_1 * \psi_2)(2) = g(\psi_2)(1)\, g(\psi_1)(1)$.

**(3)** Set $N(t) := y_j(a(t))\, g(\psi)(t)\, y_j(-b)$. Since $\psi(0) = 0$ and $u(0) = 1$, we have $h(0) = 0$ and $a(0) = b$, whence $N(0) = y_j(b)\, I\, y_j(-b) = I = g(\psi_u)(0)$. Moreover, both $N(t)$ and $g(\psi_u)(t)$ are continuous on $[0, T]$ and $C^1$ on each of the finitely many smooth subintervals of $\psi$. On any such subinterval, using $(\ast)$ and $\frac{d}{dt} y_j(a(t)) = \dot{a}(t) f_j^\vee y_j(a(t))$, we compute:
$$\dot{N}(t)\, N(t)^{-1} = \dot{a}(t) f_j^\vee + \mathrm{Ad}\bigl(\exp(a(t) f_j^\vee)\bigr)\Bigl(\dot{\psi}(t) + \sum_{r \in I} e_r^\vee\Bigr).$$
We evaluate $\mathrm{Ad}(\exp(a f_j^\vee))(X) = \sum_{d \ge 0} \frac{a^d}{d!} (\mathrm{ad} f_j^\vee)^d(X)$ using the Chevalley relations in $\mathfrak{g}^\vee$:
- For $X = \dot{\psi}(t) \in \mathfrak{h}^\vee$: $[f_j^\vee, \dot{\psi}(t)] = \langle \dot{\psi}(t), \alpha_j^\vee \rangle f_j^\vee = \dot{h}(t) f_j^\vee$, and $[f_j^\vee, f_j^\vee] = 0$, so
  $$\mathrm{Ad}\bigl(\exp(a f_j^\vee)\bigr)(\dot{\psi}(t)) = \dot{\psi}(t) + a\, \dot{h}(t) f_j^\vee.$$
- For $X = e_r^\vee$ with $r \ne j$: $[f_j^\vee, e_r^\vee] = 0$, so $\mathrm{Ad}(\exp(a f_j^\vee))(e_r^\vee) = e_r^\vee$.
- For $X = e_j^\vee$: $[f_j^\vee, e_j^\vee] = -\alpha_j$, $[f_j^\vee, -\alpha_j] = [\alpha_j, f_j^\vee] = -2 f_j^\vee$, and $[f_j^\vee, -2 f_j^\vee] = 0$, so
  $$\mathrm{Ad}\bigl(\exp(a f_j^\vee)\bigr)(e_j^\vee) = e_j^\vee - a\,\alpha_j - a^2 f_j^\vee.$$

Summing these three contributions gives
$$\dot{N}(t)\, N(t)^{-1} = \dot{\psi}(t) - a(t)\alpha_j + \sum_{r \in I} e_r^\vee + \bigl(\dot{a}(t) + a(t)\dot{h}(t) - a(t)^2\bigr) f_j^\vee.$$
Now check the two scalar coefficients using $u'(t) = -b e^{-h(t)}$ and $a(t) = b u(t)^{-1} e^{-h(t)}$:
- $-a(t) = -\frac{b e^{-h(t)}}{u(t)} = \frac{u'(t)}{u(t)}$, so $\dot{\psi}(t) - a(t)\alpha_j = \dot{\psi}_u(t)$;
- $\dot{a}(t) = -b u(t)^{-2} u'(t) e^{-h(t)} - b u(t)^{-1} \dot{h}(t) e^{-h(t)} = b^2 u(t)^{-2} e^{-2h(t)} - a(t)\dot{h}(t) = a(t)^2 - a(t)\dot{h}(t)$, so $\dot{a}(t) + a(t)\dot{h}(t) - a(t)^2 = 0$.

Hence $\dot{N}(t) = \bigl(\dot{\psi}_u(t) + \sum_{r \in I} e_r^\vee\bigr) N(t)$ on every smooth subinterval. By uniqueness of continuous piecewise-$C^1$ solutions to $(\ast)$ with initial value $I$, $N(t) = g(\psi_u)(t)$ for all $t \in [0, T]$. $\square$

---

## Section 3: Tropical Limit, Pitman Invariance, and Littelmann Paths

For any continuous path $\eta \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ with $\eta(0) = 0$ and any $k \in I$, define
$$F_{\mathbf{j}}(\eta; \mathbf{s}) := \langle \eta(T), \varpi_k^\vee \rangle - \sum_{r=1}^m \langle \eta(s_r), \alpha_{j_r}^\vee \rangle, \qquad M_k(\eta) := \max_{\mathbf{j} \in \mathcal{W}_k} \max_{\mathbf{s} \in \Delta_m(T)} F_{\mathbf{j}}(\eta; \mathbf{s}),$$
where $\Delta_m(T) := \{(s_1, \dots, s_m) \in \mathbb{R}^m \mid 0 \le s_1 \le \dots \le s_m \le T\}$ is the compact $m$-simplex. Note that $M_k(\eta)$ is invariant under any continuous, strictly increasing reparametrization of the time interval $[0, T]$.

### Lemma 3 (Laplace Tropical Limit and Uniform Stability)
1. *For every continuous piecewise-$C^1$ path $\eta \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ with $\eta(0) = 0$,*
   $$\lim_{\beta \to \infty} \frac{1}{\beta} \log Z_k(\beta; \eta) = M_k(\eta).$$
2. *If $\{\eta^{(\beta)}\}_{\beta > 0}$ is a family of continuous piecewise-$C^1$ paths on $[0, T]$ with $\eta^{(\beta)}(0) = 0$ converging uniformly on $[0, T]$ to a continuous path $\zeta$ as $\beta \to \infty$, then*
   $$\lim_{\beta \to \infty} \frac{1}{\beta} \log Z_k(\beta; \eta^{(\beta)}) = M_k(\zeta).$$
3. *If $\zeta \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ is continuous with $\zeta(0) = 0$ and dominant ($\langle \zeta(t), \alpha_j^\vee \rangle \ge 0$ for all $t \in [0, T]$ and all $j \in I$), then $M_k(\zeta) = \langle \zeta(T), \varpi_k^\vee \rangle$.*

#### Proof
**(1)** By Lemma 2(1), with $C := \sum_{\mathbf{j} \in \mathcal{W}_k} c_{\mathbf{j}} > 0$ (nonempty by Lemma 1(3)),
$$Z_k(\beta; \eta) \le C \frac{T^m}{m!} e^{\beta M_k(\eta)} \implies \limsup_{\beta \to \infty} \frac{1}{\beta} \log Z_k(\beta; \eta) \le M_k(\eta).$$
Conversely, pick $(\mathbf{j}^*, \mathbf{s}^*) \in \mathcal{W}_k \times \Delta_m(T)$ attaining $M_k(\eta)$. For any $\varepsilon > 0$, continuity of $F_{\mathbf{j}^*}(\eta; \cdot)$ on $\Delta_m(T)$ gives a relatively open neighborhood $U \subseteq \Delta_m(T)$ of $\mathbf{s}^*$ of positive $m$-dimensional Lebesgue measure $\mathrm{vol}(U) > 0$ on which $F_{\mathbf{j}^*}(\eta; \mathbf{s}) \ge M_k(\eta) - \varepsilon$. Since every term in Lemma 2(1) is non-negative, $Z_k(\beta; \eta) \ge c_{\mathbf{j}^*} \mathrm{vol}(U)\, e^{\beta(M_k(\eta) - \varepsilon)}$, whence $\liminf_{\beta \to \infty} \frac{1}{\beta} \log Z_k(\beta; \eta) \ge M_k(\eta) - \varepsilon$. Letting $\varepsilon \downarrow 0$ proves (1).

**(2)** Fix a norm $\|\cdot\|$ on $\mathfrak{h}_\mathbb{R}^*$, and set $L_k := \|\varpi_k^\vee\|_{\mathrm{op}} + m \max_{j \in I} \|\alpha_j^\vee\|_{\mathrm{op}}$. For every $\mathbf{j} \in \mathcal{W}_k$ and $\mathbf{s} \in \Delta_m(T)$, $|F_{\mathbf{j}}(\eta^{(\beta)}; \mathbf{s}) - F_{\mathbf{j}}(\zeta; \mathbf{s})| \le L_k \|\eta^{(\beta)} - \zeta\|_\infty$. By Lemma 2(1), for any continuous path $\zeta$ the integral $Z_k(\beta; \zeta)$ is still well-defined by the Dyson formula and satisfies
$$e^{-\beta L_k \|\eta^{(\beta)} - \zeta\|_\infty} Z_k(\beta; \zeta) \le Z_k(\beta; \eta^{(\beta)}) \le e^{+\beta L_k \|\eta^{(\beta)} - \zeta\|_\infty} Z_k(\beta; \zeta).$$
Taking $\frac{1}{\beta} \log$ and letting $\beta \to \infty$, using $\|\eta^{(\beta)} - \zeta\|_\infty \to 0$ and the proof of (1) (which uses only continuity of $\zeta$), we obtain $\lim_{\beta \to \infty} \frac{1}{\beta} \log Z_k(\beta; \eta^{(\beta)}) = M_k(\zeta)$.

**(3)** Since $\langle \zeta(s_r), \alpha_{j_r}^\vee \rangle \ge 0$ for all $r$ and $s_r \in [0, T]$, we have $F_{\mathbf{j}}(\zeta; \mathbf{s}) \le \langle \zeta(T), \varpi_k^\vee \rangle$ for every $\mathbf{j} \in \mathcal{W}_k$ and $\mathbf{s} \in \Delta_m(T)$, with equality at $\mathbf{s} = (0, \dots, 0)$ since $\zeta(0) = 0$. Since $\mathcal{W}_k \ne \varnothing$, $M_k(\zeta) = \langle \zeta(T), \varpi_k^\vee \rangle$. $\square$

---

Now recall the **Littelmann path model** (Littelmann, *Ann. of Math.* 142 (1995), §1–§2 & Theorem 7.1; Kashiwara, *Similarity of crystal bases*, Contemp. Math. 194 (1996)). For any continuous piecewise-linear path $\eta \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ with $\eta(0) = 0$ and any $j \in I$, set
$$h_j(t) := \langle \eta(t), \alpha_j^\vee \rangle, \qquad m_j(t) := \min_{0 \le s \le t} h_j(s), \qquad M_j(t) := \min_{t \le s \le T} h_j(s), \qquad Q_j := m_j(T) = M_j(0) \le 0.$$
Littelmann's root operators $\tilde{e}_j, \tilde{f}_j$ (in the equivalent envelope formulation of Littelmann 1995, §1.1 and Biane–Bougerol–O'Connell, *Duke Math. J.* 130 (2005), §2.2) are given by:
- If $Q_j \le -1$, then $(\tilde{e}_j \eta)(t) := \eta(t) + \max\bigl(0,\ Q_j + 1 - m_j(t)\bigr)\alpha_j$; otherwise $\tilde{e}_j \eta := 0$.
- If $h_j(T) - Q_j \ge 1$, then $(\tilde{f}_j \eta)(t) := \eta(t) - \min\bigl(1,\ M_j(t) - Q_j\bigr)\alpha_j$; otherwise $\tilde{f}_j \eta := 0$.

(Indeed, partitioning $[0, T]$ into maximal intervals on which $M_j(t)$ is constant or strictly increasing, on intervals where $M_j(t) = h_j(t) \in [Q_j, Q_j + 1]$ the increment $\eta(t) - \eta(a)$ is replaced by $(\eta(t) - \eta(a)) - (h_j(t) - h_j(a))\alpha_j = s_j(\eta(t) - \eta(a))$, while all other intervals are merely translated; this is verbatim Littelmann's cutting-and-reflecting definition, and symmetrically for $\tilde{e}_j$.)

For each $\lambda \in P^+$, let $\mathcal{P}(\lambda)$ be the set of Lakshmibai–Seshadri (LS) paths on $[0, 1]$ generated from the straight-line path $\pi_\lambda(t) = t\lambda$ by the operators $\tilde{f}_j$ ($j \in I$). By Littelmann (1995, Theorem 7.1) and Kashiwara (1996):
- $\mathcal{P}(\lambda)$ is isomorphic as a crystal to $\mathcal{B}(\lambda)$, with $\mathrm{wt}(\pi) = \pi(1)$;
- for any $\mu, \lambda \in P^+$, the set of concatenations $\mathcal{P}(\mu) * \mathcal{P}(\lambda)$ (on $[0, 2]$) is isomorphic as a crystal to $\mathcal{B}(\mu) \otimes \mathcal{B}(\lambda)$ under the Hong–Kang tensor product rule stated above;
  *(Verification of tensor-rule alignment: for $\eta = \pi_1 * \pi_2$ on $[0, 2]$ with $Q_1 = -\varepsilon_j(\pi_1)$ and $Q_2 = -\varepsilon_j(\pi_2)$, the minimum of $h_j$ on $[0, 1]$ is $Q_1$ and on $[1, 2]$ is $\langle \pi_1(1), \alpha_j^\vee \rangle + Q_2 = Q_1 + \varphi_j(\pi_1) - \varepsilon_j(\pi_2)$. Thus $Q_j = -\max(\varepsilon_j(\pi_1), \varepsilon_j(\pi_2) - \langle \pi_1(1), \alpha_j^\vee \rangle)$. If $\varphi_j(\pi_1) \ge \varepsilon_j(\pi_2)$, then $Q_j = Q_1$ is already attained on $[0, 1]$, so $m_j(t) = Q_j$ on $[1, 2]$ and $\tilde{e}_j(\pi_1 * \pi_2) = (\tilde{e}_j \pi_1) * \pi_2$; if $\varphi_j(\pi_1) < \varepsilon_j(\pi_2)$, then $Q_j + 1 \le Q_1$ by integrality, so $m_j(t) \ge Q_j + 1$ on $[0, 1]$ and $\tilde{e}_j(\pi_1 * \pi_2) = \pi_1 * (\tilde{e}_j \pi_2)$. Symmetrically for $\tilde{f}_j$ using $M_j(t)$.)*
- every path $\eta \in \mathcal{P}(\mu) * \mathcal{P}(\lambda)$ satisfies Littelmann's **integrality property**: $Q_j = \min_{t \in [0, 2]} \langle \eta(t), \alpha_j^\vee \rangle \in \mathbb{Z}_{\le 0}$ for every $j \in I$.

For any continuous piecewise-linear path $\eta \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ with $\eta(0) = 0$ and $j \in I$, define the **Pitman operator**
$$(\mathcal{P}_j \eta)(t) := \eta(t) - m_j(t)\alpha_j, \qquad m_j(t) = \min_{0 \le s \le t} \langle \eta(s), \alpha_j^\vee \rangle.$$
Notice that $\mathcal{P}_j \eta$ is again continuous and piecewise-linear with $(\mathcal{P}_j \eta)(0) = 0$.

### Lemma 4 (Pitman Invariance of $M_k$ and Identification with Highest Weights)
1. *For every continuous piecewise-$C^1$ path $\eta \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ with $\eta(0) = 0$ and every $j, k \in I$,*
   $$M_k(\mathcal{P}_j \eta) = M_k(\eta).$$
2. *If $\eta \colon [0, T] \to \mathfrak{h}_\mathbb{R}^*$ is continuous piecewise-linear with $\eta(0) = 0$ and $Q_j = \min_{t \in [0, T]} \langle \eta(t), \alpha_j^\vee \rangle \in \mathbb{Z}_{\le 0}$, then $\tilde{e}_j^{\max}(\eta) = \mathcal{P}_j(\eta)$.*
3. *For any $\mu, \lambda \in P^+$, any $\pi_1 \in \mathcal{P}(\mu)$ corresponding to $a \in \mathcal{B}(\mu)$, and any $\pi_2 \in \mathcal{P}(\lambda)$ corresponding to $b \in \mathcal{B}(\lambda)$, the highest weight $H(a \otimes b) := \mathrm{wt}(\tilde{e}_{w_\circ}^{\max}(a \otimes b)) \in P^+$ satisfies*
   $$\langle H(a \otimes b),\ \varpi_k^\vee \rangle = M_k(\pi_1 * \pi_2) \qquad \text{for all } k \in I.$$

#### Proof
**(1)** For each $\beta > 0$, set $\tilde{u}_\beta(t) := 1 + \int_0^t e^{-\beta h_j(s)} ds$ ($t \in [0, T]$) and
$$\tilde{\eta}_j^{(\beta)}(t) := \eta(t) + \frac{1}{\beta} \bigl(\log \tilde{u}_\beta(t)\bigr) \alpha_j.$$
Then $\tilde{u}_\beta(0) = 1$, $\tilde{u}_\beta(t) \ge 1 > 0$, and $\tilde{u}_\beta'(t) = e^{-\beta h_j(t)}$, which satisfies the hypothesis of Lemma 2(3) for the path $\psi = \beta \eta$ with $b = -1$. Since $(\beta \eta)_{\tilde{u}_\beta} = \beta \tilde{\eta}_j^{(\beta)}$, Lemma 2(3) yields
$$g(\beta \tilde{\eta}_j^{(\beta)})(T) = y_j\bigl(\tilde{a}_\beta(T)\bigr) \cdot g(\beta \eta)(T) \cdot y_j(+1).$$
Applying $\langle v_+ | \cdots | v_- \rangle$ and using Lemma 1(2) ($\langle v_+ | y_j(\tilde{a}_\beta(T)) = \langle v_+ |$ and $y_j(+1) v_- = v_-$) gives the exact identity
$$Z_k(\beta; \tilde{\eta}_j^{(\beta)}) = Z_k(\beta; \eta) \qquad \text{for all } \beta > 0.$$
We show $\tilde{\eta}_j^{(\beta)} \to \mathcal{P}_j \eta$ uniformly on $[0, T]$ as $\beta \to \infty$, i.e., $\frac{1}{\beta} \log \tilde{u}_\beta(t) \to -m_j(t)$ uniformly on $[0, T]$.
- *Upper bound:* Since $m_j(t) \le h_j(0) = 0$, we have $1 \le e^{-\beta m_j(t)}$, so $\tilde{u}_\beta(t) \le 1 + T e^{-\beta m_j(t)} \le (1 + T) e^{-\beta m_j(t)}$; thus $\frac{1}{\beta} \log \tilde{u}_\beta(t) \le -m_j(t) + \frac{\log(1 + T)}{\beta}$ uniformly on $[0, T]$.
- *Lower bound:* Fix $\varepsilon > 0$. By uniform continuity of $h_j$ on $[0, T]$, pick $\delta_0 \in (0, T)$ such that $|s - s'| \le \delta_0 \implies |h_j(s) - h_j(s')| \le \varepsilon$.
  - If $t \in [0, \delta_0]$, then $-m_j(t) \le \varepsilon$ (since $h_j(0) = 0$), while $\frac{1}{\beta} \log \tilde{u}_\beta(t) \ge 0 \ge -m_j(t) - \varepsilon$.
  - If $t \in [\delta_0, T]$, pick $s^*(t) \in [0, t]$ with $h_j(s^*(t)) = m_j(t)$. Either $s^*(t) \ge \delta_0/2$ (so $[s^*(t) - \delta_0/2, s^*(t)] \subseteq [0, t]$) or $s^*(t) < \delta_0/2$ (so $[s^*(t), s^*(t) + \delta_0/2] \subseteq [0, \delta_0] \subseteq [0, t]$). In either case $[0, t]$ contains a subinterval of length $\delta_0/2$ on which $h_j(s) \le m_j(t) + \varepsilon$, giving $\tilde{u}_\beta(t) \ge \frac{\delta_0}{2} e^{-\beta(m_j(t) + \varepsilon)}$ and thus $\frac{1}{\beta} \log \tilde{u}_\beta(t) \ge -m_j(t) - \varepsilon + \frac{\log(\delta_0/2)}{\beta}$.

Hence $\sup_{t \in [0, T]} \bigl|\frac{1}{\beta} \log \tilde{u}_\beta(t) - (-m_j(t))\bigr| \to 0$ as $\beta \to \infty$, so $\tilde{\eta}_j^{(\beta)} \to \mathcal{P}_j \eta$ uniformly on $[0, T]$. Applying Lemma 3(1)–(2) to $Z_k(\beta; \tilde{\eta}_j^{(\beta)}) = Z_k(\beta; \eta)$ gives $M_k(\mathcal{P}_j \eta) = M_k(\eta)$.

**(2)** Set $q := -Q_j \in \mathbb{Z}_{\ge 0}$; we induct on $q$. If $q = 0$, then $Q_j = 0$, so $m_j(t) = 0$ for all $t$, $\tilde{e}_j(\eta) = 0$, and $\tilde{e}_j^{\max}(\eta) = \eta = \mathcal{P}_j(\eta)$. Assume $q \ge 1$ and the claim holds for $q - 1$. Set $\eta_1 := \tilde{e}_j(\eta)$, so $\eta_1(t) = \eta(t) + \max(0, Q_j + 1 - m_j(t))\alpha_j$, and let $h^{\mathrm{new}}(t) := \langle \eta_1(t), \alpha_j^\vee \rangle$ and $m^{\mathrm{new}}(t) := \min_{0 \le s \le t} h^{\mathrm{new}}(s)$. Let $t_* := \min\{t \in [0, T] \mid m_j(t) = Q_j + 1\}$ (well-defined since $m_j$ is continuous with $m_j(0) = 0 \ge Q_j + 1 > Q_j = m_j(T)$). Note that $h_j(t_*) = m_j(t_*) = Q_j + 1$ (if $t_* = 0$ then $Q_j + 1 = 0 = h_j(0)$; if $t_* > 0$ then $m_j(s) > m_j(t_*)$ for all $s < t_*$, forcing $h_j(t_*) = m_j(t_*)$).
- For $t \le t_*$, $m_j(t) \ge Q_j + 1$, so $\eta_1(t) = \eta(t)$ and $m^{\mathrm{new}}(t) = m_j(t) = \max(m_j(t), Q_j + 1)$.
- For $t \ge t_*$, $m_j(t) \le Q_j + 1$, so
  $$h^{\mathrm{new}}(t) = h_j(t) + 2(Q_j + 1 - m_j(t)) = (h_j(t) - m_j(t)) + (Q_j + 1 - m_j(t)) + (Q_j + 1) \ge Q_j + 1 = h^{\mathrm{new}}(t_*),$$
  whence $m^{\mathrm{new}}(t) = Q_j + 1 = \max(m_j(t), Q_j + 1)$.

Thus $m^{\mathrm{new}}(t) = \max(m_j(t), Q_j + 1)$ for all $t \in [0, T]$, with global minimum $Q_j + 1 = -(q - 1)$. By the induction hypothesis applied to $\eta_1$,
$$\tilde{e}_j^{\max}(\eta)(t) = \tilde{e}_j^{\max}(\eta_1)(t) = \eta_1(t) - m^{\mathrm{new}}(t)\alpha_j = \eta(t) + \Bigl(\max(0, Q_j + 1 - m_j(t)) - \max(m_j(t), Q_j + 1)\Bigr)\alpha_j.$$
Since $\max(0, Q_j + 1 - x) - \max(x, Q_j + 1) = -x$ identically for all $x \in \mathbb{R}$, we conclude $\tilde{e}_j^{\max}(\eta)(t) = \eta(t) - m_j(t)\alpha_j = (\mathcal{P}_j \eta)(t)$.

**(3)** Choose any reduced expression $w_\circ = s_{i_1} \cdots s_{i_\ell}$ and set $\eta := \pi_1 * \pi_2 \in \mathcal{P}(\mu) * \mathcal{P}(\lambda)$. Define $\eta^{(\ell)} := \eta$ and $\eta^{(r-1)} := \tilde{e}_{i_r}^{\max}(\eta^{(r)})$ for $r = \ell, \ell - 1, \dots, 1$. Every $\eta^{(r)}$ belongs to $\mathcal{P}(\mu) * \mathcal{P}(\lambda)$ and hence satisfies Littelmann's integrality property, so by (2), $\eta^{(r-1)} = \mathcal{P}_{i_r}(\eta^{(r)})$ for each $r$. Applying (1) inductively gives $M_k(\eta^{(0)}) = M_k(\eta)$. On the other hand, since $\mathcal{P}(\mu) * \mathcal{P}(\lambda) \cong \mathcal{B}(\mu) \otimes \mathcal{B}(\lambda)$ is a finite normal crystal, Kashiwara (1994, §7.2; Zhou, Proposition 2.2) ensures that $\zeta := \eta^{(0)} = \tilde{e}_{w_\circ}^{\max}(\eta)$ is the highest weight element of its connected component, with endpoint $\zeta(2) = H(a \otimes b)$. Because $\tilde{e}_j(\zeta) = 0$ for every $j \in I$ and $\zeta$ satisfies the integrality property, $\min_{t \in [0, 2]} \langle \zeta(t), \alpha_j^\vee \rangle = 0$ for all $j \in I$, i.e., $\zeta$ is a dominant path. By Lemma 3(3),
$$\langle H(a \otimes b), \varpi_k^\vee \rangle = \langle \zeta(2), \varpi_k^\vee \rangle = M_k(\zeta) = M_k(\pi_1 * \pi_2). \qquad \square$$

---

## Section 4: Tensor Dominance Monotonicity in All Finite Types

### Theorem 1 (General Tensor Dominance Monotonicity)
*Let $\mathfrak{g}$ be any finite-dimensional complex simple Lie algebra, let $\mu, \lambda \in P^+$, let $a \in \mathcal{B}(\mu)$, $b \in \mathcal{B}(\lambda)$, and let $i \in I$. Write $H(x) := \mathrm{wt}(\tilde{e}_{w_\circ}^{\max}(x)) \in P^+$ for the highest weight of the connected component of $x \in \mathcal{B}(\mu) \otimes \mathcal{B}(\lambda)$.*
1. *If $\tilde{f}_i(b) \ne 0$, then $H(a \otimes b) \ge H\bigl(a \otimes \tilde{f}_i(b)\bigr)$ (i.e., $H(a \otimes b) - H(a \otimes \tilde{f}_i(b)) \in Q^+$).*
2. *If $\tilde{f}_i(a) \ne 0$, then $H\bigl(\tilde{f}_i(a) \otimes b\bigr) \ge H(a \otimes b)$.*

#### Proof
Let $\pi_1 \in \mathcal{P}(\mu)$ and $\pi_2 \in \mathcal{P}(\lambda)$ be the LS paths corresponding to $a$ and $b$. We prove (1); the proof of (2) is identical and noted at the end.

Assume $\tilde{f}_i(b) \ne 0$, so $\tilde{f}_i(\pi_2) \ne 0$. Set $h(t) := \langle \pi_2(t), \alpha_i^\vee \rangle$ ($t \in [0, 1]$), $M(t) := \min_{t \le s \le 1} h(s)$, and $Q := M(0)$; then $h(1) - Q \ge 1$, and $(\tilde{f}_i \pi_2)(t) = \pi_2(t) - \min(1, M(t) - Q)\alpha_i$.

Fix $k \in I$ and let $(V_k, \mathbf{B}_k, v_+, v_-)$ be given by Lemma 1. For each $\beta > 0$, define on $[0, 1]$:
$$I_\beta(t) := \int_t^1 e^{-\beta h(s)} ds, \qquad b_\beta := \frac{1 - e^{-\beta}}{I_\beta(0)} > 0, \qquad u_\beta(t) := e^{-\beta} + (1 - e^{-\beta}) \frac{I_\beta(t)}{I_\beta(0)},$$
$$\pi_{2, \beta}(t) := \pi_2(t) + \frac{1}{\beta} \bigl(\log u_\beta(t)\bigr) \alpha_i.$$
Note that $u_\beta$ is $C^1$ on $[0, 1]$, takes values in $[e^{-\beta}, 1] \subset (0, \infty)$, and satisfies $u_\beta(0) = 1$, $u_\beta(1) = e^{-\beta}$, and $u_\beta'(t) = -b_\beta e^{-\beta h(t)}$.

**Step 1 (Finite-$\beta$ matrix inequality).**
Applying Lemma 2(3) to the path $\psi = \beta \pi_2$ on $[0, 1]$ with $j = i$, $u = u_\beta$, and $b = b_\beta$ (noting $(\beta \pi_2)_{u_\beta} = \beta \pi_{2,\beta}$) gives
$$g(\beta \pi_{2, \beta})(1) = y_i\bigl(a_\beta(1)\bigr) \cdot g(\beta \pi_2)(1) \cdot y_i(-b_\beta), \qquad a_\beta(1) = \frac{b_\beta}{e^{-\beta} e^{\beta h(1)}} > 0.$$
Inverting the outer $y_i$ factors gives
$$g(\beta \pi_2)(1) = y_i\bigl(-a_\beta(1)\bigr) \cdot g(\beta \pi_{2, \beta})(1) \cdot y_i(+b_\beta).$$
Multiply on the right by $g(\beta \pi_1)(1)$, use Lemma 2(2) ($g(\beta(\pi_1 * \pi_2))(2) = g(\beta \pi_2)(1)\, g(\beta \pi_1)(1)$), and take the $(v_+, v_-)$ matrix entry. By Lemma 1(2), $\langle v_+ | y_i(-a_\beta(1)) = \langle v_+ |$, so
$$Z_k(\beta; \pi_1 * \pi_2) = \langle v_+,\ g(\beta \pi_{2, \beta})(1) \cdot \exp(+b_\beta f_i^\vee) \cdot g(\beta \pi_1)(1)\, v_- \rangle.$$
Since $b_\beta > 0$ and all matrix entries of $f_i^\vee$ in $\mathbf{B}_k$ are non-negative (Lemma 1(1)), the exponential series $\exp(+b_\beta f_i^\vee) = I + \sum_{d \ge 1} \frac{b_\beta^d}{d!} (f_i^\vee)^d$ satisfies $\exp(+b_\beta f_i^\vee) \ge I$ entry-by-entry in $\mathbf{B}_k$. By Lemma 2(1), both $g(\beta \pi_{2, \beta})(1)$ and $g(\beta \pi_1)(1)$ also have all matrix entries $\ge 0$ in $\mathbf{B}_k$. Multiplying these entrywise non-negative inequalities and applying Lemma 2(2) yields
$$Z_k(\beta; \pi_1 * \pi_2) \ge \langle v_+,\ g(\beta \pi_{2, \beta})(1)\, g(\beta \pi_1)(1)\, v_- \rangle = Z_k(\beta; \pi_1 * \pi_{2, \beta}) \qquad \text{for all } \beta > 0. \tag{$\dagger$}$$

**Step 2 (Uniform convergence $\pi_{2, \beta} \to \tilde{f}_i \pi_2$).**
We verify that $-\frac{1}{\beta} \log u_\beta(t) \to \min(1, M(t) - Q)$ uniformly on $[0, 1]$ as $\beta \to \infty$. Fix $\varepsilon \in (0, 1)$.
- *Lower bound on $-\frac{1}{\beta} \log u_\beta(t)$:* Since $h$ is continuous with minimum $Q$, the set $\{s \in [0, 1] \mid h(s) \le Q + \varepsilon\}$ has positive Lebesgue measure $\mu_\varepsilon > 0$, so $I_\beta(0) \ge \mu_\varepsilon e^{-\beta(Q + \varepsilon)}$. On the other hand, $I_\beta(t) \le (1 - t) e^{-\beta M(t)} \le e^{-\beta M(t)}$ for all $t \in [0, 1]$. Hence
  $$u_\beta(t) \le e^{-\beta} + \frac{1}{\mu_\varepsilon} e^{-\beta(M(t) - Q - \varepsilon)} \le \Bigl(1 + \frac{1}{\mu_\varepsilon}\Bigr) e^{-\beta \min(1,\, M(t) - Q - \varepsilon)}.$$
  Taking $-\frac{1}{\beta} \log$ gives $-\frac{1}{\beta} \log u_\beta(t) \ge \min(1, M(t) - Q) - \varepsilon - \frac{\log(1 + \mu_\varepsilon^{-1})}{\beta}$ uniformly for all $t \in [0, 1]$.
- *Upper bound on $-\frac{1}{\beta} \log u_\beta(t)$:* Always $u_\beta(t) \ge e^{-\beta}$, so $-\frac{1}{\beta} \log u_\beta(t) \le 1$ on $[0, 1]$. If $M(t) - Q > 1 - \varepsilon$, then $\min(1, M(t) - Q) \ge 1 - \varepsilon$, so $-\frac{1}{\beta} \log u_\beta(t) \le \min(1, M(t) - Q) + \varepsilon$ immediately. Consider now the set $K_\varepsilon := \{t \in [0, 1] \mid M(t) - Q \le 1 - \varepsilon\}$. Because $h$ is continuous and $h(1) \ge Q + 1$, there exists $\eta_0 \in (0, 1)$ such that $h(s) > Q + 1 - \varepsilon/2$ for all $s \in [1 - \eta_0, 1]$. Hence for every $t \in K_\varepsilon$, the minimum $M(t) = \min_{s \in [t, 1]} h(s) \le Q + 1 - \varepsilon$ must be attained at some $s^*(t) \in [t, 1 - \eta_0]$. By uniform continuity of $h$ on $[0, 1]$, pick $\delta_0 \in (0, \eta_0)$ (independent of $t$) such that $|s - s'| \le \delta_0 \implies |h(s) - h(s')| \le \varepsilon$. Then $[s^*(t), s^*(t) + \delta_0] \subseteq [t, 1]$, and on this interval of length $\delta_0$ we have $h(s) \le M(t) + \varepsilon$. Thus $I_\beta(t) \ge \delta_0 e^{-\beta(M(t) + \varepsilon)}$, while $I_\beta(0) \le e^{-\beta Q}$, so for all $t \in K_\varepsilon$ and $\beta \ge 1$,
  $$u_\beta(t) \ge (1 - e^{-\beta}) \frac{I_\beta(t)}{I_\beta(0)} \ge (1 - e^{-1})\delta_0\, e^{-\beta(M(t) - Q + \varepsilon)},$$
  whence $-\frac{1}{\beta} \log u_\beta(t) \le M(t) - Q + \varepsilon - \frac{\log((1 - e^{-1})\delta_0)}{\beta} = \min(1, M(t) - Q) + \varepsilon - \frac{\log((1 - e^{-1})\delta_0)}{\beta}$.

Combining both bounds shows $\sup_{t \in [0, 1]} \bigl|-\frac{1}{\beta} \log u_\beta(t) - \min(1, M(t) - Q)\bigr| \to 0$ as $\beta \to \infty$, so $\pi_{2, \beta} \to \tilde{f}_i \pi_2$ uniformly on $[0, 1]$, and therefore $\pi_1 * \pi_{2, \beta} \to \pi_1 * \tilde{f}_i \pi_2$ uniformly on $[0, 2]$.

**Step 3 (Conclusion of (1) and (2)).**
Taking $\frac{1}{\beta} \log$ of $(\dagger)$ and sending $\beta \to \infty$, Lemma 3(1)–(2) and Lemma 4(3) give
$$\langle H(a \otimes b),\ \varpi_k^\vee \rangle = M_k(\pi_1 * \pi_2) \ge M_k(\pi_1 * \tilde{f}_i \pi_2) = \langle H(a \otimes \tilde{f}_i(b)),\ \varpi_k^\vee \rangle \qquad \text{for every } k \in I.$$
Since every weight of $\mathcal{B}(\mu) \otimes \mathcal{B}(\lambda)$ lies in $\mu + \lambda - Q$, the difference $\gamma := H(a \otimes b) - H(a \otimes \tilde{f}_i(b))$ belongs to the root lattice $Q = \bigoplus_{k \in I} \mathbb{Z}\alpha_k$. Its coefficient of $\alpha_k$ is $\langle \gamma, \varpi_k^\vee \rangle \ge 0$ for every $k \in I$, hence $\gamma \in Q^+$, proving (1).

For (2), applying Lemma 2(3) to $\pi_1$ instead of $\pi_2$ gives $g(\beta \pi_{1,\beta})(1) = y_i(+a_\beta(1))\, g(\beta \pi_1)(1)\, y_i(-b_\beta)$ with $a_\beta(1) > 0$. Multiplying on the left by $g(\beta \pi_2)(1)$, pairing with $\langle v_+ | \cdots | v_- \rangle$, and using $y_i(-b_\beta) v_- = v_-$ (Lemma 1(2)) and $y_i(+a_\beta(1)) \ge I$ yields $Z_k(\beta; \pi_{1,\beta} * \pi_2) \ge Z_k(\beta; \pi_1 * \pi_2)$; letting $\beta \to \infty$ gives $H(\tilde{f}_i(a) \otimes b) \ge H(a \otimes b)$. $\square$

---

## Section 5: Proof of Conjecture 1 for All Finite Simple Lie Algebras

### Theorem 2 (Conjecture 1 of arXiv:2609.23078v1)
*For every finite-dimensional complex simple Lie algebra $\mathfrak{g}$ and every dominant integral weight $\lambda \in P^+$, we have $\mathcal{F}(\mathcal{C}_{b_\star}) \subseteq \mathcal{C}_{b_\star}$, and therefore*
$$\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}.$$
*Consequently, $\mathcal{B}(\lambda) \setminus \mathcal{F}(b_\star)$ is the unique maximal proper extremal subset of $\mathcal{B}(\lambda)$.*

#### Proof
**Step 1 (General-type analogue of Proposition 7.2 of Zhou).**
Specialize Theorem 1(1) to $\mu = \rho$ and $a = b_\rho \in \mathcal{B}(\rho)$. By Proposition 3.12 of Zhou (`prop:eimax-to-chkw`, valid in all finite types since $\varepsilon_i(b_\rho) = 0$ and $\langle \rho, \alpha_i^\vee \rangle = 1$), $\tilde{e}_{w_\circ}^{\max}(b_\rho \otimes b) = b_\rho \otimes \check{e}_{w_\circ}(b)$ for all $b \in \mathcal{B}(\lambda)$, so $H(b_\rho \otimes b) = \rho + \mathrm{wt}(\check{e}_{w_\circ}(b))$. Hence for every $b \in \mathcal{B}(\lambda)$ and $i \in I$ with $\tilde{f}_i(b) \ne 0$,
$$\mathrm{wt}\bigl(\check{e}_{w_\circ}(b)\bigr) \ge \mathrm{wt}\bigl(\check{e}_{w_\circ}(\tilde{f}_i(b))\bigr). \tag{$\ddagger$}$$

**Step 2 (Minimality, PRV identification, and multiplicity-one of $C(b_\rho \otimes b_{w_\circ \lambda})$).**
Let $\nu_0 := H(b_\rho \otimes b_{w_\circ \lambda}) = \rho + \mathrm{wt}(b_\star) \in P^+$ be the highest weight of the connected component $C(b_\rho \otimes b_{w_\circ \lambda}) \cong \mathcal{B}(\nu_0)$.

1. *Every highest weight element of $\mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$ has the form $b_\rho \otimes d$ ($d \in \mathcal{B}(\lambda)$), and its weight $\eta$ satisfies $\eta \ge \nu_0$:*
   Let $a \otimes d \in \mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$ satisfy $\tilde{e}_i(a \otimes d) = 0$ for all $i \in I$. For each $i \in I$, if $\varphi_i(a) < \varepsilon_i(d)$, then $\varepsilon_i(d) > \varphi_i(a) \ge 0$, so $\tilde{e}_i(d) \ne 0$ and $\tilde{e}_i(a \otimes d) = a \otimes \tilde{e}_i(d) \ne 0$, a contradiction. Thus $\varphi_i(a) \ge \varepsilon_i(d)$, whence $0 = \tilde{e}_i(a \otimes d) = \tilde{e}_i(a) \otimes d$ and therefore $\tilde{e}_i(a) = 0$ for all $i \in I$, forcing $a = b_\rho$. Choosing $j_1, \dots, j_r \in I$ with $\tilde{f}_{j_1} \cdots \tilde{f}_{j_r}(d) = b_{w_\circ \lambda}$ and applying $(\ddagger)$ repeatedly (noting $\tilde{e}_{w_\circ}^{\max}(b_\rho \otimes d) = b_\rho \otimes d$, so $\check{e}_{w_\circ}(d) = d$), we obtain
   $$\eta = \mathrm{wt}(b_\rho \otimes d) = \rho + \mathrm{wt}\bigl(\check{e}_{w_\circ}(d)\bigr) \ge \cdots \ge \rho + \mathrm{wt}\bigl(\check{e}_{w_\circ}(b_{w_\circ \lambda})\bigr) = \rho + \mathrm{wt}(b_\star) = \nu_0.$$
   Hence every irreducible summand $V(\eta)$ of $V(\rho) \otimes V(\lambda)$ satisfies $\eta \ge \nu_0$.

2. *Identification $\nu_0 = \overline{\rho + w_\circ \lambda}$:*
   Let $\nu := \overline{\rho + w_\circ \lambda} \in P^+$ be the unique dominant weight in the Weyl group orbit $W(\rho + w_\circ \lambda)$. Since $b_\rho \otimes b_{w_\circ \lambda} \in C(b_\rho \otimes b_{w_\circ \lambda}) \cong \mathcal{B}(\nu_0)$, the weight $\rho + w_\circ \lambda$ occurs in $V(\nu_0)$; by $W$-invariance of the weights of $V(\nu_0)$, $\nu$ also occurs in $V(\nu_0)$, so $\nu_0 \ge \nu$. Conversely, by the Parthasarathy–Ranga Rao–Varadarajan theorem (Parthasarathy–Ranga Rao–Varadarajan, *Ann. of Math.* **85** (1967), Theorem 2.1, valid for every finite-dimensional complex simple Lie algebra $\mathfrak{g}$; see also Khare 2013, §3, cited in Zhou §7), $V(\nu)$ occurs with nonzero multiplicity in $V(\rho) \otimes V(\lambda)$. By (1), $\nu \ge \nu_0$. Antisymmetry of the dominance order ($Q^+ \cap (-Q^+) = \{0\}$) yields $\nu_0 = \nu = \overline{\rho + w_\circ \lambda}$.

3. *Multiplicity-one $\mathrm{mult}_{V(\rho) \otimes V(\lambda)}(V(\nu_0)) = 1$:*
   Because $C(b_\rho \otimes b_{w_\circ \lambda}) \cong \mathcal{B}(\nu_0)$ is a connected component of $\mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$, the multiplicity is at least $1$. For the upper bound, let $v_\rho \in V(\rho)_\rho$ and $v_{w_\circ \lambda} \in V(\lambda)_{w_\circ \lambda}$ be nonzero extremal weight vectors, and set $M := U(\mathfrak{g}) \cdot (v_\rho \otimes v_{w_\circ \lambda}) \subseteq V(\rho) \otimes V(\lambda)$.
   - For every $e \in \mathfrak{n}_+$ and $w \in V(\lambda)$, $e \cdot (v_\rho \otimes w) = (e v_\rho) \otimes w + v_\rho \otimes (e w) = v_\rho \otimes (e w)$, so by induction $X \cdot (v_\rho \otimes v_{w_\circ \lambda}) = v_\rho \otimes (X v_{w_\circ \lambda})$ for all $X \in U(\mathfrak{n}_+)$. Since $V(\lambda) = U(\mathfrak{n}_+) v_{w_\circ \lambda}$, we get $v_\rho \otimes V(\lambda) \subseteq M$.
   - We show $V(\rho)_\gamma \otimes V(\lambda) \subseteq M$ for every weight $\gamma$ of $V(\rho)$ by induction on $\mathrm{ht}(\rho - \gamma) \ge 0$. The base case $\gamma = \rho$ is $v_\rho \otimes V(\lambda) \subseteq M$. Since $V(\rho) = U(\mathfrak{n}_-) v_\rho$, every $V(\rho)_\gamma$ with $\gamma < \rho$ is spanned by elements $f_j v$ with $j \in I$ and $v \in V(\rho)_{\gamma + \alpha_j}$; for any $w \in V(\lambda)$,
     $$(f_j v) \otimes w = f_j(v \otimes w) - v \otimes (f_j w) \in M,$$
     because $v \otimes w \in M$ and $v \otimes (f_j w) \in V(\rho)_{\gamma + \alpha_j} \otimes V(\lambda) \subseteq M$ by the induction hypothesis. Thus $M = V(\rho) \otimes V(\lambda)$.

   Therefore every $\mathfrak{g}$-module homomorphism $\phi \in \mathrm{Hom}_{\mathfrak{g}}(V(\rho) \otimes V(\lambda), V(\nu_0))$ is uniquely determined by $\phi(v_\rho \otimes v_{w_\circ \lambda}) \in V(\nu_0)_{\rho + w_\circ \lambda}$. Since $\rho + w_\circ \lambda \in W \cdot \nu_0$ is an extremal weight of $V(\nu_0)$, we have $\dim V(\nu_0)_{\rho + w_\circ \lambda} = \dim V(\nu_0)_{\nu_0} = 1$, and hence
   $$\mathrm{mult}_{V(\rho) \otimes V(\lambda)}\bigl(V(\nu_0)\bigr) = \dim \mathrm{Hom}_{\mathfrak{g}}\bigl(V(\rho) \otimes V(\lambda),\ V(\nu_0)\bigr) \le \dim V(\nu_0)_{\rho + w_\circ \lambda} = 1.$$
   Thus $\mathrm{mult}_{V(\rho) \otimes V(\lambda)}(V(\nu_0)) = 1$, so $b_\rho \otimes b_\star = \tilde{e}_{w_\circ}^{\max}(b_\rho \otimes b_{w_\circ \lambda})$ is the unique highest weight element of weight $\nu_0$ in $\mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$.

**Step 3 ($\mathcal{F}$-stability of $\mathcal{C}_{b_\star}$).**
Let $b \in \mathcal{C}_{b_\star}$ and $i \in I$ be such that $\tilde{f}_i(b) \ne 0$. Since $b_{w_\circ \lambda}$ is the unique lowest element of $\mathcal{B}(\lambda)$, there exist $r \ge 0$ and $j_1, \dots, j_r \in I$ such that $\tilde{f}_{j_1} \cdots \tilde{f}_{j_r}(\tilde{f}_i(b)) = b_{w_\circ \lambda}$. Applying $(\ddagger)$ repeatedly and using $\check{e}_{w_\circ}(b) = b_\star = \check{e}_{w_\circ}(b_{w_\circ \lambda})$, we obtain
$$\mathrm{wt}(b_\star) = \mathrm{wt}\bigl(\check{e}_{w_\circ}(b)\bigr) \ge \mathrm{wt}\bigl(\check{e}_{w_\circ}(\tilde{f}_i(b))\bigr) \ge \cdots \ge \mathrm{wt}\bigl(\check{e}_{w_\circ}(b_{w_\circ \lambda})\bigr) = \mathrm{wt}(b_\star).$$
By antisymmetry of the dominance order ($Q^+ \cap (-Q^+) = \{0\}$), $\mathrm{wt}(\check{e}_{w_\circ}(\tilde{f}_i(b))) = \mathrm{wt}(b_\star)$, and hence
$$\mathrm{wt}\bigl(b_\rho \otimes \check{e}_{w_\circ}(\tilde{f}_i(b))\bigr) = \rho + \mathrm{wt}(b_\star) = \nu_0.$$
Because $b_\rho \otimes \check{e}_{w_\circ}(\tilde{f}_i(b)) = \tilde{e}_{w_\circ}^{\max}(b_\rho \otimes \tilde{f}_i(b))$ is a highest weight element of weight $\nu_0$ in $\mathcal{B}(\rho) \otimes \mathcal{B}(\lambda)$, Step 2 forces $b_\rho \otimes \check{e}_{w_\circ}(\tilde{f}_i(b)) = b_\rho \otimes b_\star$, so $\check{e}_{w_\circ}(\tilde{f}_i(b)) = b_\star$, i.e., $\tilde{f}_i(b) \in \mathcal{C}_{b_\star}$. Thus $\mathcal{F}(\mathcal{C}_{b_\star}) \subseteq \mathcal{C}_{b_\star}$.

**Step 4 (Deduction of $\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$).**
For completeness we recall the short type-independent deduction of Propositions 3.7 and 4.2 of Zhou:
- *$\mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$:* By Step 3, $\mathcal{F}(b_\star) \subseteq \mathcal{C}_{b_\star}$. Conversely, if $c \in \mathcal{C}_{b_\star}$, then $b_\star = \check{e}_{w_\circ}(c) = \tilde{e}_{i_1} \cdots \tilde{e}_{i_s}(c)$ for some $i_1, \dots, i_s \in I$ (each $\check{e}_i$ is a nonnegative power of $\tilde{e}_i$), so $c = \tilde{f}_{i_s} \cdots \tilde{f}_{i_1}(b_\star) \in \mathcal{F}(b_\star)$.
- *$\mathcal{C}_{b_\star} \subseteq \Gamma_\lambda$:* For any $b \in \mathcal{B}(\lambda)$ and $j \in I$, $\langle \check{e}_j(b) \rangle_{\mathrm{Ext}} = \langle b \rangle_{\mathrm{Ext}}$ (because $\check{e}_j(b) = \tilde{e}_j^p(b) \in \langle b \rangle_{\mathrm{Ext}}$ by $\tilde{e}_j$-stability of extremal subsets, while if $\check{e}_j(b) \ne b$ then $\check{e}_j(b)$ is a non-top element of the $j$-string $S^j(b)$, forcing $S^j(b) \subseteq \langle \check{e}_j(b) \rangle_{\mathrm{Ext}} \ni b$). Iterating along $w_\circ$ gives $\langle b_\star \rangle_{\mathrm{Ext}} = \langle b_{w_\circ \lambda} \rangle_{\mathrm{Ext}} = \mathcal{B}(\lambda)$, so $b_\star \in \Gamma_\lambda$. Since $\Gamma_\lambda$ is $\tilde{f}_i$-stable (if $c \in \Gamma_\lambda$ and $\tilde{f}_i(c) \ne 0$, then $c = \tilde{e}_i \tilde{f}_i(c) \in \langle \tilde{f}_i(c) \rangle_{\mathrm{Ext}}$, so $\langle \tilde{f}_i(c) \rangle_{\mathrm{Ext}} = \mathcal{B}(\lambda)$), we get $\mathcal{C}_{b_\star} = \mathcal{F}(b_\star) \subseteq \Gamma_\lambda$.
- *$\Gamma_\lambda \subseteq \mathcal{C}_{b_\star}$:* Let $S^i(c)$ be any $i$-string in $\mathcal{B}(\lambda)$. All elements of $S^i(c) \setminus \{\tilde{e}_i^{\max}(c)\}$ have the same $\check{e}_i$-image and hence the same $\check{e}_{w_\circ}$-image (since $\check{e}_{w_\circ} \check{e}_i = \check{e}_{w_\circ}$). Thus $\mathcal{C}_{b_\star} \cap S^i(c) \in \{\varnothing,\, S^i(c),\, S^i(c) \setminus \{\tilde{e}_i^{\max}(c)\},\, \{\tilde{e}_i^{\max}(c)\}\}$. By Step 3, $\mathcal{C}_{b_\star}$ is $\tilde{f}_i$-stable, ruling out $\{\tilde{e}_i^{\max}(c)\}$ whenever $|S^i(c)| > 1$. Taking complements gives $(\mathcal{B}(\lambda) \setminus \mathcal{C}_{b_\star}) \cap S^i(c) \in \{\varnothing,\, S^i(c),\, \{\tilde{e}_i^{\max}(c)\}\}$ for all $c, i$, so $\mathcal{B}(\lambda) \setminus \mathcal{C}_{b_\star}$ is a proper extremal subset of $\mathcal{B}(\lambda)$ (it omits $b_{w_\circ \lambda}$). Since every proper extremal subset is disjoint from $\Gamma_\lambda$, we obtain $\mathcal{B}(\lambda) \setminus \mathcal{C}_{b_\star} \subseteq \mathcal{B}(\lambda) \setminus \Gamma_\lambda$, i.e., $\Gamma_\lambda \subseteq \mathcal{C}_{b_\star}$.

Hence $\Gamma_\lambda = \mathcal{F}(b_\star) = \mathcal{C}_{b_\star}$, and since the union of all proper extremal subsets equals $\mathcal{B}(\lambda) \setminus \Gamma_\lambda$ (every $b \notin \Gamma_\lambda$ lies in the proper extremal subset $\langle b \rangle_{\mathrm{Ext}}$, and extremal subsets are closed under unions), $\mathcal{B}(\lambda) \setminus \mathcal{F}(b_\star)$ is the unique maximal proper extremal subset of $\mathcal{B}(\lambda)$. $\blacksquare$

---

## References
- P. Biane, P. Bougerol, and N. O'Connell, *Littelmann paths and Brownian paths*, Duke Math. J. **130** (2005), no. 1, 127–167.
- J. Hong and S.-J. Kang, *Introduction to Quantum Groups and Crystal Bases*, Graduate Studies in Mathematics, vol. 42, AMS, 2002.
- M. Kashiwara, *Crystal bases of modified quantized enveloping algebra*, Duke Math. J. **73** (1994), no. 2, 383–413.
- M. Kashiwara, *Similarity of crystal bases*, Lie Algebras and Their Representations, Contemp. Math. **194**, AMS, 1996, 177–186.
- A. Khare, *Representations of complex semi-simple Lie groups and Lie algebras*, in: Connected at Infinity II, Texts and Readings in Mathematics, vol. 67, Hindustan Book Agency, 2013, 85–129.
- P. Littelmann, *Paths and root operators in representation theory*, Ann. of Math. (2) **142** (1995), no. 3, 499–525.
- G. Lusztig, *Introduction to Quantum Groups*, Progress in Mathematics, vol. 110, Birkhäuser, 1993.
- K. R. Parthasarathy, R. Ranga Rao, and V. S. Varadarajan, *Representations of complex semi-simple Lie groups and Lie algebras*, Ann. of Math. (2) **85** (1967), no. 3, 383–429.
- Y. Zhou, *Maximal proper extremal subset in the crystal basis of a finite-dimensional irreducible module*, arXiv:2609.23078v1, 2026.

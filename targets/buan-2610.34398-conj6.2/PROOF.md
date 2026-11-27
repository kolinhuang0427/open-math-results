# Proof of Conjecture 7.2 (`\label{conj:TFordered}`) of Buan–Hanson–Marsh (`arXiv:2610.34398v1`)

- **Primary source:** Aslak B. Buan, Eric J. Hanson, and Bethany R. Marsh, *Lifting $\tau$-exceptional sequences*, `arXiv:2610.34398v1` (2026-10-25), Section 7.1 (`\subsection{TF-ordered $\tau$-rigid modules}`, `\label{sec:conj1}`), **Conjecture 7.2** (`\label{conj:TFordered}`, lines 1932–1938 of `lifting_arxiv_25102026.tex`; tracked under directory slug `targets/buan-2610.34398-conj6.2/`).
- **Result:** **PROVED** unconditionally for every $\tau$-tilting finite finite-dimensional $k$-algebra $\Lambda$, every two-sided ideal $I \subseteq \mathrm{rad}\Lambda$, and every TF-ordered $\tau_{\Lambda/I}$-rigid module $(M_1, \dots, M_t)$. In fact, we prove a strictly stronger 2-term presilting lifting theorem (**Theorem 1**), showing that the extension-of-scalars functor $F = (\Lambda/I) \otimes_\Lambda -$ maps the minimal projective presentation $P_{N_i}$ directly to $P_{M_i}^{r_i} \oplus \bigoplus_{j=i+1}^t P_{M_j}^{s_{ij}}$ in $K^b(\mathrm{proj}(\Lambda/I))$ with **no** shifted projective summands (equivalently preserving $g$-vectors: $g_{\Lambda/I}(F(N_i)) = g_\Lambda(N_i)$), from which Conjecture 7.2 follows immediately upon taking $H^0$ (**Corollary 2**). Moreover, primitivity of silting $g$-vectors yields the sharp multiplicity **$r_i = 1$** for every $1 \le i \le t$, and in particular **$F(Z) \cong C$** in [BHM, Prop. 4.8(b)] (**Corollary 3**).

---

## 1. Statement and Setup

Throughout, $k$ is a field and $A$ is a finite-dimensional $k$-algebra. We write $\mathrm{mod} A$ for the category of finite-dimensional left $A$-modules, $\mathrm{proj} A$ for the full subcategory of finitely generated projective left $A$-modules, $\mathrm{rk} A$ for the number of isomorphism classes of simple $A$-modules, and $K^b(\mathcal{A})$ for the bounded homotopy category of an additive category $\mathcal{A}$, with shift convention $(X[1])^m = X^{m+1}$ and $d_{X[1]} = -d_X$. For a basic module (or complex) $X$, we write $|X|$ for the number of pairwise non-isomorphic indecomposable direct summands of $X$, and for any object $X$ in a Krull–Schmidt category we write $\mathrm{basic}(X)$ for the direct sum of one representative from each isomorphism class of indecomposable direct summands of $X$.

For a module $X \in \mathrm{mod} A$, we fix a minimal projective presentation
$$
P_X := \bigl(Q_1 \xrightarrow{\;d_X\;} Q_0\bigr) \in K^b(\mathrm{proj} A)
$$
concentrated in degrees $-1$ and $0$, so that $H^0(P_X) \cong X$. A complex $T \in K^b(\mathrm{proj} A)$ is *2-term* if it is isomorphic to a complex concentrated in degrees $-1, 0$; it is *2-term presilting* if it is 2-term and $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(T, T[1]) = 0$ (equivalently $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(T, T[m]) = 0$ for all $m > 0$); and it is *2-term silting* if additionally $\mathrm{thick}(T) = K^b(\mathrm{proj} A)$. We write $2\text{-}\mathrm{silt}(A)$ for the set of isomorphism classes of basic 2-term silting complexes in $K^b(\mathrm{proj} A)$, and for a 2-term presilting complex $U$, we write $2\text{-}\mathrm{silt}_U(A)$ for the subset of those containing $U$ as a direct summand.

Recall the Adachi–Iyama–Reiten correspondence ([AIR, Thm. 3.2, Prop. 2.2]): the assignment $(M, P) \mapsto P_M \oplus P[1]$ is a bijection between isomorphism classes of basic $\tau_A$-rigid pairs $(M, P)$ (where $M \in \mathrm{mod} A$ is $\tau_A$-rigid, $P \in \mathrm{proj} A$, and $\mathrm{Hom}_A(P, M) = 0$) and isomorphism classes of basic 2-term presilting complexes in $K^b(\mathrm{proj} A)$. Moreover, $|M| + |P| \le \mathrm{rk} A$, with equality if and only if $(M, P)$ is a support $\tau_A$-tilting pair, if and only if $P_M \oplus P[1] \in 2\text{-}\mathrm{silt}(A)$. In a basic support $\tau_A$-tilting pair $(M, P)$, the projective $P$ is uniquely determined by $M$ as the basic direct sum of all indecomposable projectives $Q \in \mathrm{proj} A$ satisfying $\mathrm{Hom}_A(Q, M) = 0$ (since adding any further such $Q$ would yield a $\tau_A$-rigid pair with more than $\mathrm{rk} A$ summands); thus $S \mapsto \mathrm{basic}(H^0(S))$ is a bijection from $2\text{-}\mathrm{silt}(A)$ to the set $\mathrm{s}\tau\text{-}\mathrm{tilt}(A)$ of basic support $\tau_A$-tilting modules.

For any two modules $X, Y \in \mathrm{mod} A$, we recall the standard identity ([AIR, Lem. 3.4]):
$$
\mathrm{Hom}_{K^b(\mathrm{proj} A)}(P_X, P_Y[1]) \cong D\mathrm{Hom}_A(Y, \tau_A X), \tag{1}
$$
where $D = \mathrm{Hom}_k(-, k)$. Indeed, in $D^b(\mathrm{mod} A)$ we have a truncation triangle $H^{-1}(P_Y)[1] \to P_Y \to Y \to H^{-1}(P_Y)[2]$. Since $P_X$ is a complex of projectives concentrated in degrees $[-1, 0]$, we have $\mathrm{Hom}_{D^b(\mathrm{mod} A)}(P_X, M[m]) = 0$ for every $M \in \mathrm{mod} A$ and every $m \ge 2$. Applying $\mathrm{Hom}_{D^b(\mathrm{mod} A)}(P_X, -[1])$ to the truncation triangle gives
$$
\mathrm{Hom}_{K^b(\mathrm{proj} A)}(P_X, P_Y[1]) \cong \mathrm{Hom}_{D^b(\mathrm{mod} A)}(P_X, Y[1]) \cong \mathrm{coker}\!\bigl(\mathrm{Hom}_A(Q_0, Y) \xrightarrow{d_X^*} \mathrm{Hom}_A(Q_1, Y)\bigr).
$$
Dualizing via $D$ and using the Nakayama isomorphism $D\mathrm{Hom}_A(Q, Y) \cong \mathrm{Hom}_A(Y, \nu Q)$ for $Q \in \mathrm{proj} A$ (where $\nu = D\mathrm{Hom}_A(-, A)$) gives
$$
D\mathrm{Hom}_{K^b(\mathrm{proj} A)}(P_X, P_Y[1]) \cong \ker\!\bigl(\mathrm{Hom}_A(Y, \nu Q_1) \to \mathrm{Hom}_A(Y, \nu Q_0)\bigr) = \mathrm{Hom}_A\bigl(Y, \ker(\nu d_X)\bigr) = \mathrm{Hom}_A(Y, \tau_A X),
$$
proving (1).

Now let $\Lambda$ be a $\tau$-tilting finite finite-dimensional $k$-algebra and $I \subseteq \mathrm{rad}\Lambda$ a two-sided ideal. Let $F = (\Lambda/I) \otimes_\Lambda - \colon \mathrm{mod}\Lambda \to \mathrm{mod}(\Lambda/I)$ be the extension-of-scalars functor, and denote by the same symbol $F = (\Lambda/I) \otimes_\Lambda - \colon K^b(\mathrm{proj}\Lambda) \to K^b(\mathrm{proj}(\Lambda/I))$ the induced termwise triangle functor on bounded homotopy categories. Let $\Delta_I$ be the recursive injective map on $\tau$-exceptional sequences of [BHM, Thm. 1.1] (`\label{thm:main1}`), let $\omega$ and $\omega_I$ be the Mendoza–Treffinger bijections of [BHM, Thm. 7.1] (`\label{thm:TF-bij}`), and let $L_I = \omega^{-1} \Delta_I \omega_I$.

A sequence $(M_1, \dots, M_t)$ of indecomposable modules over $A$ is a *TF-ordered $\tau_A$-rigid module* if $\coprod_{j=1}^t M_j$ is $\tau_A$-rigid and $M_i \notin \mathrm{Gen}_A(\coprod_{j=i+1}^t M_j)$ for all $1 \le i \le t$.

**Theorem 1 (Strong Form of Conjecture 7.2).** *Let $\Lambda$ be a $\tau$-tilting finite finite-dimensional $k$-algebra, $I \subseteq \mathrm{rad}\Lambda$ a two-sided ideal, and $(M_1, M_2, \dots, M_t)$ a TF-ordered $\tau_{\Lambda/I}$-rigid module. Set $(N_1, N_2, \dots, N_t) := L_I(M_1, M_2, \dots, M_t)$. Then for every $1 \le i \le t$, there exist integers $r_i \ge 1$ and $s_{ij} \ge 0$ ($i < j \le t$) such that in $K^b(\mathrm{proj}(\Lambda/I))$,*
$$
F(P_{N_i}) \;\cong\; P_{M_i}^{r_i} \;\oplus\; \bigoplus_{j=i+1}^t P_{M_j}^{s_{ij}}. \tag{2}
$$

**Corollary 2 (Conjecture 7.2 / `\label{conj:TFordered}`).** *Under the hypotheses of Theorem 1, for every $1 \le i \le t$,*
$$
F(N_i) \;\cong\; M_i^{r_i} \amalg X, \qquad \text{where } X = \coprod_{j=i+1}^t M_j^{s_{ij}} \in \mathrm{add}\!\left(\coprod_{j=i+1}^t M_j\right) \text{ and } r_i \ge 1.
$$
*Proof of Corollary 2 from Theorem 1.* Since $F = (\Lambda/I) \otimes_\Lambda -$ is right exact, for every $N \in \mathrm{mod}\Lambda$ we have $H^0(F(P_N)) = \mathrm{coker}(F(d_N)) \cong F(\mathrm{coker}(d_N)) = F(N)$. Applying $H^0$ to (2) immediately yields $F(N_i) \cong M_i^{r_i} \amalg \coprod_{j=i+1}^t M_j^{s_{ij}}$. $\square$

**Corollary 3 (Sharp Multiplicity $r_i = 1$ and $F(Z) \cong C$).** *In Lemma 2.1(c) (sharpening [BHM, Prop. 4.8(b)]), one has $r = 1$, i.e., $F(P_Z) \cong P_C$ and $F(Z) \cong C$. Consequently, in Theorem 1 and Conjecture 7.2, one has $r_i = 1$ for every $1 \le i \le t$: $F(P_{N_i}) \cong P_{M_i} \oplus \bigoplus_{j=i+1}^t P_{M_j}^{s_{ij}}$ and $F(N_i) \cong M_i \amalg \coprod_{j=i+1}^t M_j^{s_{ij}}$.*

*Proof of Corollary 3 from Lemma 2.1(c) and the Proof of Theorem 1.* Let $A$ be a $\tau$-tilting finite finite-dimensional $k$-algebra and $J \subseteq \mathrm{rad} A$ a two-sided ideal, with $G = (A/J) \otimes_A -$. Because $J \subseteq \mathrm{rad} A$, $G$ induces a bijection between the isomorphism classes of indecomposable projective $A$-modules and those of $A/J$-modules (each indecomposable projective is determined up to isomorphism by its simple top, and $\mathrm{top}_{A/J}(G(Q)) \cong \mathrm{top}_A(Q)$), hence an isomorphism of free abelian groups $K_0(G) \colon K_0(\mathrm{proj} A) \xrightarrow{\sim} K_0(\mathrm{proj}(A/J)) \cong \mathbb{Z}^{\mathrm{rk} A}$. In Lemma 2.1(c), $G(P_Z) \cong P_C^r$ in $K^b(\mathrm{proj}(A/J))$ implies $K_0(G)([P_Z]) = r \cdot [P_C]$ in $K_0(\mathrm{proj}(A/J)) \cong \mathbb{Z}^{\mathrm{rk} A}$. Since $P_Z$ is an indecomposable direct summand of the basic 2-term silting complex $P_{B_Z} \in K^b(\mathrm{proj} A)$, and the classes of the indecomposable direct summands of any basic silting complex form a $\mathbb{Z}$-basis of $K_0(\mathrm{proj} A) \cong \mathbb{Z}^{\mathrm{rk} A}$ ([AI, Thm. 2.27], [AIR, Thm. 5.1]), the vector $[P_Z]$ is primitive in $\mathbb{Z}^{\mathrm{rk} A}$. Hence $K_0(G)([P_Z]) = r \cdot [P_C]$ with $r \ge 1$ forces $r = 1$, giving $G(P_Z) \cong P_C$ and $G(Z) \cong C$. Tracking the multiplicity $r_i$ through the induction in Section 3 (which equals $r = 1$ at the base step $i = t$ and is preserved verbatim in Step 4 from the inductive step for $(\Gamma, I_Z)$) yields $r_i = 1$ for all $1 \le i \le t$. $\square$

---

## 2. Core Lemmas

### Lemma 2.1 (Extension of Scalars on 2-Term Presilting Complexes)
Let $A$ be a finite-dimensional $k$-algebra, $J \subseteq \mathrm{rad} A$ a two-sided ideal, and $G = (A/J) \otimes_A -$.
- **(a)** If $T \in K^b(\mathrm{proj} A)$ is 2-term presilting, then $G(T) \in K^b(\mathrm{proj}(A/J))$ is 2-term presilting.
- **(b)** For every $X \in \mathrm{mod} A$, there exists $R \in \mathrm{proj}(A/J)$ such that $G(P_X) \cong P_{G(X)} \oplus R[1]$ in $K^b(\mathrm{proj}(A/J))$.
- **(c)** Assume $A$ is $\tau$-tilting finite. Let $C \in \mathrm{mod}(A/J)$ be an indecomposable $\tau_{A/J}$-rigid module, let $Z = P_s({}^\perp \mathrm{Filt}\mathsf{J}_{A/J}(C))$ be its lift as in [BHM, Setup 4.1], and let $B_Z := P({}^\perp \tau_A Z)$ and $B_C := P({}^{\perp_{A/J}} \tau_{A/J} C)$ be their respective Bongartz completions. Then
  $$
  G(P_{B_Z}) \cong P_{G(B_Z)}, \qquad \mathrm{add} G(P_{B_Z}) = \mathrm{add} P_{B_C}, \qquad \text{and} \qquad G(P_Z) \cong P_C^r
  $$
  for some integer $r \ge 1$.

*Proof.*
**(a)** Write $T = (T^{-1} \xrightarrow{d} T^0)$ in degrees $-1, 0$. Since $G(T)$ lives in degrees $[-1, 0]$ and $G(T)[1]$ lives in degrees $[-2, -1]$, every morphism $G(T) \to G(T)[1]$ in $K^b(\mathrm{proj}(A/J))$ is represented by a single $A/J$-linear map $f \colon G(T^{-1}) \to G(T^0)$ in degree $-1$ (the chain-map condition is vacuous). Under the canonical identifications $G(T^m) \cong T^m / J T^m$ with projections $\pi_m \colon T^m \twoheadrightarrow G(T^m)$, projectivity of $T^{-1}$ over $A$ and surjectivity of $\pi_0$ give an $A$-linear map $\tilde{f} \colon T^{-1} \to T^0$ with $\pi_0 \tilde{f} = f \pi_{-1}$, i.e., $G(\tilde{f}) = f$. Since $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(T, T[1]) = 0$, the chain map $\tilde{f} \colon T \to T[1]$ is null-homotopic: there exist $h^0 \colon T^0 \to T^0$ and $h^{-1} \colon T^{-1} \to T^{-1}$ such that $\tilde{f} = h^0 d - d h^{-1}$. Applying the additive functor $G$ yields $f = G(h^0) G(d) - G(d) G(h^{-1})$, so $f = 0$ in $K^b(\mathrm{proj}(A/J))$.

**(b)** Let $P_X = (Q_1 \xrightarrow{d_X} Q_0)$ be a minimal projective presentation of $X$. Since $Q_0 \twoheadrightarrow X$ is a projective cover, $\mathrm{Im}(d_X) \subseteq \mathrm{rad} Q_0$. Since $J \subseteq \mathrm{rad} A$, the projection $Q_0 \twoheadrightarrow G(Q_0) = Q_0 / J Q_0$ maps $\mathrm{rad} Q_0$ into $\mathrm{rad} G(Q_0)$, whence $\mathrm{Im}(G(d_X)) \subseteq \mathrm{rad} G(Q_0)$. Therefore $G(Q_0) \twoheadrightarrow \mathrm{coker}(G(d_X)) \cong G(X)$ is a projective cover over $A/J$. Let $Q'_1 \twoheadrightarrow \mathrm{Im}(G(d_X))$ be a projective cover over $A/J$. Because $G(Q_1) \in \mathrm{proj}(A/J)$ surjects onto $\mathrm{Im}(G(d_X))$ via $G(d_X)$, we obtain a direct-sum decomposition $G(Q_1) \cong Q'_1 \oplus R$ with $G(d_X)|_{Q'_1} \colon Q'_1 \twoheadrightarrow \mathrm{Im}(G(d_X))$ a projective cover and $G(d_X)|_R = 0$. Thus $G(P_X) \cong (Q'_1 \to G(Q_0)) \oplus (R \to 0) \cong P_{G(X)} \oplus R[1]$ in $K^b(\mathrm{proj}(A/J))$.

**(c)** By [AIR, Thm. 2.10], $B_Z$ is a basic $\tau_A$-tilting module and $B_C$ is a basic $\tau_{A/J}$-tilting module, so $|B_C| = \mathrm{rk}(A/J) = \mathrm{rk} A$. By (a) and (b), $G(P_{B_Z}) \cong P_{G(B_Z)} \oplus R[1]$ is a 2-term presilting complex in $K^b(\mathrm{proj}(A/J))$ for some $R \in \mathrm{proj}(A/J)$. By [AIR, Thm. 3.2], $(\mathrm{basic}(G(B_Z)), \mathrm{basic}(R))$ is a basic $\tau_{A/J}$-rigid pair. By [BHM, Prop. 4.8(a)], $\mathrm{add} G(B_Z) = \mathrm{add} B_C$, so $|\mathrm{basic}(G(B_Z))| = |B_C| = \mathrm{rk}(A/J)$. Since $|\mathrm{basic}(G(B_Z))| + |\mathrm{basic}(R)| \le \mathrm{rk}(A/J)$ by [AIR, Prop. 2.2(b)], we must have $R = 0$. Therefore $G(P_{B_Z}) \cong P_{G(B_Z)}$, which immediately yields $\mathrm{add} G(P_{B_Z}) = \mathrm{add} P_{B_C}$. Finally, $Z \in \mathrm{add} B_Z$ implies that $G(P_Z)$ is a direct summand of $G(P_{B_Z}) \cong P_{G(B_Z)}$, so $G(P_Z)$ also has no shifted projective summands: $G(P_Z) \cong P_{G(Z)} \cong P_C^r$ ($r \ge 1$) by [BHM, Prop. 4.8(b)]. $\square$

---

### Lemma 2.2 (2-Term Bongartz Presentations in $K^b(\mathrm{proj} A)$)
Let $A$ be a $\tau$-tilting finite finite-dimensional $k$-algebra, $Z \in \mathrm{mod} A$ an indecomposable $\tau_A$-rigid module, $B_Z := P({}^\perp \tau_A Z)$, and $B := P_{B_Z} \in K^b(\mathrm{proj} A)$. Define the additive functor
$$
\Phi_Z := f_Z \circ H^0 \colon \mathrm{add}(B) \longrightarrow \mathcal{P}(\mathsf{J}(Z)).
$$
Then the following hold:
- **(a)** *(Silting co-heart criterion)* Every object $K \in K^b(\mathrm{proj} A)$ satisfying $\mathrm{Hom}(B, K[m]) = 0$ and $\mathrm{Hom}(K, B[m]) = 0$ for all $m \ge 1$ lies in $\mathrm{add}(B)$.
- **(b)** Let $T \in K^b(\mathrm{proj} A)$ be a 2-term complex such that $T \oplus P_Z$ is 2-term presilting. Then a minimal right $\mathrm{add}(B)$-approximation $g \colon B_0 \to T$ fits into a distinguished triangle
  $$
  B_1 \xrightarrow{\;\phi\;} B_0 \xrightarrow{\;g\;} T \longrightarrow B_1[1] \tag{3}
  $$
  in $K^b(\mathrm{proj} A)$ with $B_0, B_1 \in \mathrm{add}(B)$. Moreover, for **any** distinguished triangle $B'_1 \xrightarrow{\phi'} B'_0 \xrightarrow{g'} T \to B'_1[1]$ with $B'_0, B'_1 \in \mathrm{add}(B)$, the 2-term complex $(B'_1 \xrightarrow{\phi'} B'_0)$ is isomorphic in $K^b(\mathrm{add} B)$ to $X_T^\bullet := (B_1 \xrightarrow{\phi} B_0)$.
- **(c)** Let $T, T' \in K^b(\mathrm{proj} A)$ be 2-term complexes compatible with $P_Z$ (i.e., $T \oplus P_Z$ and $T' \oplus P_Z$ are 2-term presilting). If $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(T, T'[1]) = 0$, then $\mathrm{Hom}_{K^b(\mathrm{add} B)}(X_T^\bullet, X_{T'}^\bullet[1]) = 0$. Furthermore, if $T$ is indecomposable then $X_T^\bullet$ is indecomposable in $K^b(\mathrm{add} B)$, and $X_T^\bullet \cong X_{T'}^\bullet$ in $K^b(\mathrm{add} B)$ implies $T \cong T'$ in $K^b(\mathrm{proj} A)$.
- **(d)** For every 2-term complex $T$ compatible with $P_Z$, we have $H^0\bigl(K^b(\Phi_Z)(X_T^\bullet)\bigr) \cong f_Z(H^0(T))$ in $\mathsf{J}(Z)$.

*Proof.*
**(a)** (Cf. [AI, Prop. 2.23].) For full subcategories $\mathcal{X}, \mathcal{Y} \subseteq K^b(\mathrm{proj} A)$, write $\mathcal{X} * \mathcal{Y}$ for the class of objects $E$ fitting in a distinguished triangle $X \to E \to Y \to X[1]$ with $X \in \mathcal{X}, Y \in \mathcal{Y}$. Let
$$
\mathcal{S} := \bigcup_{a \le b} \mathrm{add}(B)[a] * \mathrm{add}(B)[a+1] * \cdots * \mathrm{add}(B)[b],
$$
and let $\mathrm{smd}(\mathcal{S})$ be the class of direct summands of objects in $\mathcal{S}$. Since $B$ is silting, $\mathrm{Hom}(B[p], B[q+1]) = \mathrm{Hom}(B, B[q - p + 1]) = 0$ whenever $p \le q$; hence every triangle $B_q[q] \to E \to B_p[p] \to B_q[q+1]$ splits for $p \le q$. Therefore $\mathrm{add}(B)[q] * \mathrm{add}(B)[p] \subseteq \mathrm{add}(B)[p] * \mathrm{add}(B)[q]$ for $p < q$, and $\mathrm{add}(B)[p] * \mathrm{add}(B)[p] = \mathrm{add}(B)[p]$. By the octahedral axiom (associativity of $*$), it follows that $\mathcal{S}$ is closed under extensions and shifts. If $K_1 \mid X_1 \in \mathcal{S}$ and $K_2 \mid X_2 \in \mathcal{S}$ (say $X_1 = K_1 \oplus K'_1$, $X_2 = K_2 \oplus K'_2$), then any triangle $K_1 \to E \to K_2 \to K_1[1]$ yields by direct sum with $(K'_1 \xrightarrow{1} K'_1 \to 0 \to K'_1[1])$ and $(0 \to K'_2 \xrightarrow{1} K'_2 \to 0)$ a triangle $X_1 \to E \oplus K'_1 \oplus K'_2 \to X_2 \to X_1[1]$, so $E \mid (E \oplus K'_1 \oplus K'_2) \in \mathcal{S} * \mathcal{S} = \mathcal{S}$. Thus $\mathrm{smd}(\mathcal{S})$ is a thick triangulated subcategory containing $B$, hence $\mathrm{smd}(\mathcal{S}) = \mathrm{thick}(B) = K^b(\mathrm{proj} A)$.

Now let $K \in K^b(\mathrm{proj} A)$ satisfy $\mathrm{Hom}(B, K[m]) = \mathrm{Hom}(K, B[m]) = 0$ for all $m \ge 1$. Pick $a \le b$ minimal in $b - a$ such that $K$ is a direct summand of some $X \in \mathrm{add}(B)[a] * \cdots * \mathrm{add}(B)[b]$, with $\iota \colon K \to X$ and $\pi \colon X \to K$ satisfying $\pi\iota = \mathrm{id}_K$.
- If $b > 0$, there is a triangle $Y \xrightarrow{u} X \xrightarrow{v} B_b[b] \to Y[1]$ with $B_b \in \mathrm{add}(B)$ and $Y \in \mathrm{add}(B)[a] * \cdots * \mathrm{add}(B)[b-1]$. Since $b > 0$, $v\iota \in \mathrm{Hom}(K, B_b[b]) = 0$, so $\iota = u\iota'$ for some $\iota' \colon K \to Y$; then $(\pi u)\iota' = \mathrm{id}_K$, making $K$ a direct summand of $Y$, contradicting minimality. Hence $b \le 0$.
- If $a < 0$, there is a triangle $B_a[a] \xrightarrow{u} X \xrightarrow{v} W \to B_a[a+1]$ with $B_a \in \mathrm{add}(B)$ and $W \in \mathrm{add}(B)[a+1] * \cdots * \mathrm{add}(B)[b]$. Since $-a > 0$, $\pi u \in \mathrm{Hom}(B_a[a], K) \cong \mathrm{Hom}(B_a, K[-a]) = 0$, so $\pi = \pi' v$ for some $\pi' \colon W \to K$; then $\pi'(v\iota) = \mathrm{id}_K$, making $K$ a direct summand of $W$, contradicting minimality. Hence $a \ge 0$.

Therefore $a = b = 0$, so $K$ is a direct summand of an object in $\mathrm{add}(B)$, whence $K \in \mathrm{add}(B)$.

**(b)** First we show $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(B, T[m]) = 0$ for all $m \ge 1$. For $m \ge 2$, both $B$ and $T$ are concentrated in degrees $[-1, 0]$, while $T[m]$ lives in degrees $[-m-1, -m] \subseteq [-3, -2]$, so $\mathrm{Hom}(B, T[m]) = 0$ automatically. For $m = 1$, decompose $T \cong P_Y \oplus R[1]$ with $Y = H^0(T)$ and $R \in \mathrm{proj} A$. For the shifted-projective summand, $R[1][1] = R[2]$ is concentrated in degree $-2$, so $\mathrm{Hom}(B, R[2]) = 0$. For $P_Y$, since $P_Y \oplus P_Z$ is 2-term presilting, (1) gives $\mathrm{Hom}_A(Y, \tau_A Z) = 0$, so $Y \in {}^\perp \tau_A Z = \mathrm{Gen}(B_Z)$. Picking an epimorphism $B_Z^d \twoheadrightarrow Y$ induces an injection $\mathrm{Hom}_A(Y, \tau_A B_Z) \hookrightarrow \mathrm{Hom}_A(B_Z^d, \tau_A B_Z) = 0$ (as $B_Z$ is $\tau_A$-rigid), whence $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(B, P_Y[1]) = 0$ by (1). Thus $\mathrm{Hom}(B, T[m]) = 0$ for all $m \ge 1$.

Because $\mathrm{add}(B)$ has finite-dimensional Hom-spaces over $k$, $T$ admits a minimal right $\mathrm{add}(B)$-approximation $g \colon B_0 \to T$. Complete $g$ to a distinguished triangle $K \xrightarrow{\phi} B_0 \xrightarrow{g} T \to K[1]$ in $K^b(\mathrm{proj} A)$.
- Applying $\mathrm{Hom}(B, -)$ gives exact sequences
  $$
  \mathrm{Hom}(B, B_0[m-1]) \xrightarrow{g_*} \mathrm{Hom}(B, T[m-1]) \longrightarrow \mathrm{Hom}(B, K[m]) \longrightarrow \mathrm{Hom}(B, B_0[m]).
  $$
  For $m = 1$, $g_*$ is surjective (as $g$ is a right $\mathrm{add}(B)$-approximation) and $\mathrm{Hom}(B, B_0[1]) = 0$ (as $B$ is silting), so $\mathrm{Hom}(B, K[1]) = 0$. For $m \ge 2$, both $\mathrm{Hom}(B, T[m-1]) = 0$ (proved above) and $\mathrm{Hom}(B, B_0[m]) = 0$, so $\mathrm{Hom}(B, K[m]) = 0$.
- Applying $\mathrm{Hom}(-, B[m])$ for $m \ge 1$ gives exact sequences
  $$
  \mathrm{Hom}(B_0, B[m]) \longrightarrow \mathrm{Hom}(K, B[m]) \longrightarrow \mathrm{Hom}(T, B[m+1]).
  $$
  Here $\mathrm{Hom}(B_0, B[m]) = 0$ ($B$ is silting) and $\mathrm{Hom}(T, B[m+1]) = 0$ (since $m + 1 \ge 2$ and both $T, B$ are 2-term in $[-1, 0]$), so $\mathrm{Hom}(K, B[m]) = 0$ for all $m \ge 1$.

By part (a), $B_1 := K \in \mathrm{add}(B)$, establishing (3).

Now let $B'_1 \xrightarrow{\phi'} B'_0 \xrightarrow{g'} T \to B'_1[1]$ be any other distinguished triangle with $B'_0, B'_1 \in \mathrm{add}(B)$. Because $\mathrm{Hom}(B, B'_1[1]) = 0$, $g' \colon B'_0 \to T$ is also a right $\mathrm{add}(B)$-approximation of $T$. Hence there exist $r \colon B'_0 \to B_0$ with $g r = g'$ and $s \colon B_0 \to B'_0$ with $g' s = g$. Then $g(rs) = g$, so right minimality of $g$ implies that $rs$ is an isomorphism. Replacing $r$ by $(rs)^{-1} r$, we obtain $rs = \mathrm{id}_{B_0}$, giving a decomposition $B'_0 \cong B_0 \oplus S$ with $S \in \mathrm{add}(B)$ under which $g' = (g, 0) \colon B_0 \oplus S \to T$. Comparing the distinguished triangle $B'_1 \xrightarrow{\phi'} B_0 \oplus S \xrightarrow{(g,0)} T \to B'_1[1]$ with the direct-sum triangle $B_1 \oplus S \xrightarrow{\phi \oplus \mathrm{id}_S} B_0 \oplus S \xrightarrow{(g,0)} T \to (B_1 \oplus S)[1]$ via TR3 yields an isomorphism $w \colon B'_1 \xrightarrow{\sim} B_1 \oplus S$ such that $(\phi \oplus \mathrm{id}_S) w = \phi'$. Therefore, as complexes in $K^b(\mathrm{add} B)$,
$$
\bigl(B'_1 \xrightarrow{\phi'} B'_0\bigr) \;\cong\; \bigl(B_1 \xrightarrow{\phi} B_0\bigr) \oplus \bigl(S \xrightarrow{\mathrm{id}_S} S\bigr) \;\cong\; X_T^\bullet,
$$
since $(S \xrightarrow{\mathrm{id}_S} S)$ is contractible in $K^b(\mathrm{add} B)$.

**(c)** Let $B_1 \xrightarrow{\phi} B_0 \xrightarrow{g} T \xrightarrow{\delta} B_1[1]$ and $B'_1 \xrightarrow{\phi'} B'_0 \xrightarrow{g'} T' \xrightarrow{\delta'} B'_1[1]$ be the triangles of (b) for $T$ and $T'$. Any morphism $X_T^\bullet \to X_{T'}^\bullet[1]$ in $K^b(\mathrm{add} B)$ is given by a morphism $u \colon B_1 \to B'_0$ in $\mathrm{add}(B)$. Consider the composition $g' u \circ \delta[-1] \colon T[-1] \to T'$; since $\mathrm{Hom}_{K^b(\mathrm{proj} A)}(T[-1], T') \cong \mathrm{Hom}(T, T'[1]) = 0$, we have $g' u \circ \delta[-1] = 0$. From the rotated triangle $T[-1] \xrightarrow{\delta[-1]} B_1 \xrightarrow{\phi} B_0 \xrightarrow{g} T$, it follows that $g' u = v \phi$ for some $v \colon B_0 \to T'$. Since $\mathrm{Hom}(B_0, B'_1[1]) = 0$, $v$ lifts along $g'$ to $h_0 \colon B_0 \to B'_0$ with $g' h_0 = v$. Then $g'(u - h_0 \phi) = g' u - v \phi = 0$, so $u - h_0 \phi = \phi' h_1$ for some $h_1 \colon B_1 \to B'_1$. Thus $u = h_0 \phi + \phi' h_1$ is null-homotopic, proving $\mathrm{Hom}_{K^b(\mathrm{add} B)}(X_T^\bullet, X_{T'}^\bullet[1]) = 0$.

For the second assertion, decompose any 2-term complex $(B_1 \xrightarrow{\phi} B_0)$ in $\mathrm{add}(B)$ as $(B_1^{\min} \xrightarrow{\phi^{\min}} B_0^{\min}) \oplus (S \xrightarrow{\mathrm{id}_S} S)$ with $\phi^{\min} \in \mathrm{rad}(\mathrm{add} B)$ (by repeatedly splitting off any indecomposable summands on which $\phi$ restricts to an isomorphism). If $(a_1, a_0)$ and $(b_1, b_0)$ are mutually inverse homotopy equivalences between $(B_1^{\min} \xrightarrow{\phi^{\min}} B_0^{\min})$ and $(B_1'^{\min} \xrightarrow{\phi'^{\min}} B_0'^{\min})$, then $(b_1 a_1 - \mathrm{id}, b_0 a_0 - \mathrm{id}) = (h \phi^{\min}, \phi^{\min} h)$ and $(a_1 b_1 - \mathrm{id}, a_0 b_0 - \mathrm{id}) = (h' \phi'^{\min}, \phi'^{\min} h')$ lie in the Jacobson radical of the finite-dimensional $k$-algebras $\mathrm{End}(B_m^{\min})$ and $\mathrm{End}(B_m'^{\min})$; hence $a_1, a_0$ are isomorphisms in $\mathrm{add}(B)$. Taking cones in $K^b(\mathrm{proj} A)$ (and noting $\mathrm{cone}(S \xrightarrow{\mathrm{id}_S} S) = 0$) yields $T \cong \mathrm{cone}(\phi) \cong \mathrm{cone}(\phi^{\min}) \cong \mathrm{cone}(\phi'^{\min}) \cong \mathrm{cone}(\phi') \cong T'$. Similarly, any idempotent endomorphism $e$ of $X_T^{\min} := (B_1^{\min} \xrightarrow{\phi^{\min}} B_0^{\min})$ in $K^b(\mathrm{add} B)$ satisfies $e^2 - e \in \mathrm{rad}\mathrm{End}_{C^b(\mathrm{add} B)}(X_T^{\min})$ (as every null-homotopic endomorphism $(h\phi^{\min}, \phi^{\min} h)$ lies in the radical); since $\mathrm{End}_{C^b(\mathrm{add} B)}(X_T^{\min})$ is finite-dimensional over $k$, idempotents lift modulo the radical, so any direct-sum decomposition $X_T^\bullet \cong Y_1^\bullet \oplus Y_2^\bullet$ in $K^b(\mathrm{add} B)$ is realized strictly in $C^b(\mathrm{add} B)$ by 2-term complexes $Y_1^{\min} \oplus Y_2^{\min} = X_T^{\min}$. Taking cones gives $T \cong \mathrm{cone}(Y_1^{\min}) \oplus \mathrm{cone}(Y_2^{\min})$; if $T$ is indecomposable, one cone vanishes, meaning its differential is an isomorphism in $\mathrm{add}(B)$ and that summand is zero in $K^b(\mathrm{add} B)$. Thus $X_T^\bullet$ is indecomposable.

**(d)** Write $B_0 = P_{Q_0}$ and $B_1 = P_{Q_1}$ with $Q_0, Q_1 \in \mathrm{add}(B_Z)$. Since $B_1, B_0, T$ are concentrated in degrees $[-1, 0]$, we have $H^1(B_1) = 0$, so taking $H^0$ of (3) yields an exact sequence in $\mathrm{mod} A$:
$$
Q_1 \xrightarrow{\;H^0(\phi)\;} Q_0 \xrightarrow{\;H^0(g)\;} H^0(T) \longrightarrow 0. \tag{4}
$$
We claim that applying $f_Z$ yields an exact sequence in $\mathrm{mod} A$ (and hence in the wide subcategory $\mathsf{J}(Z)$):
$$
f_Z(Q_1) \xrightarrow{\;f_Z(H^0(\phi))\;} f_Z(Q_0) \xrightarrow{\;f_Z(H^0(g))\;} f_Z(H^0(T)) \longrightarrow 0. \tag{5}
$$
First, surjectivity of $H^0(g)$ implies surjectivity of $f_Z(H^0(g))$, and $f_Z(H^0(g)) \circ f_Z(H^0(\phi)) = 0$ by functoriality. For exactness at $f_Z(Q_0)$, we first show that $H^0(g)$ maps $t_Z(Q_0)$ onto $t_Z(H^0(T))$. Let $Y := H^0(T)$, so $T \cong P_Y \oplus R[1]$. Every morphism $u \colon Z \to Y$ in $\mathrm{mod} A$ lifts to a chain map $\tilde{u} \colon P_Z \to P_Y \hookrightarrow T$ in $K^b(\mathrm{proj} A)$. Because $P_Z \in \mathrm{add}(B)$ and $g \colon P_{Q_0} \to T$ is a right $\mathrm{add}(B)$-approximation, $\tilde{u}$ factors through $g$, so $u = H^0(\tilde{u})$ factors through $H^0(g) \colon Q_0 \to Y$. Since every morphism $Z \to Q_0$ lands in $t_Z(Q_0)$ and $t_Z(Y) \in \mathrm{Gen} Z$ is the sum of the images of all morphisms $Z \to Y$, we conclude $H^0(g)(t_Z(Q_0)) = t_Z(Y)$.

Now let $\pi_M \colon M \twoheadrightarrow f_Z(M) = M / t_Z(M)$ be the canonical projection. If $\pi_{Q_0}(q) \in \ker f_Z(H^0(g))$ for $q \in Q_0$, then $H^0(g)(q) \in t_Z(Y) = H^0(g)(t_Z(Q_0))$, so there exists $t \in t_Z(Q_0)$ with $H^0(g)(q - t) = 0$. By exactness of (4), $q - t = H^0(\phi)(q_1)$ for some $q_1 \in Q_1$, whence $\pi_{Q_0}(q) = \pi_{Q_0}(q - t) = f_Z(H^0(\phi))(\pi_{Q_1}(q_1))$. Thus (5) is exact, so $H^0(K^b(\Phi_Z)(X_T^\bullet)) = \mathrm{coker}(f_Z(H^0(\phi))) \cong f_Z(H^0(T))$. $\square$

---

### Proposition 2.3 (Silting Reduction via $K^b(\Phi_Z)$)
Under the hypotheses of Lemma 2.2:
- **(a)** For every $S \in 2\text{-}\mathrm{silt}_{P_Z}(A)$, the complex $K^b(\Phi_Z)(X_S^\bullet)$ is a 2-term silting complex in $K^b(\mathcal{P}(\mathsf{J}(Z)))$. Moreover, the assignment $S \mapsto \mathrm{basic}\bigl(K^b(\Phi_Z)(X_S^\bullet)\bigr)$ is a bijection
  $$
  \Psi_Z \colon 2\text{-}\mathrm{silt}_{P_Z}(A) \xrightarrow{\;\sim\;} 2\text{-}\mathrm{silt}(\mathsf{J}(Z)).
  $$
- **(b)** Let $T \in K^b(\mathrm{proj} A)$ be an indecomposable 2-term presilting complex such that $T \oplus P_Z$ is 2-term presilting.
  - If $T \cong P_Z$, then $K^b(\Phi_Z)(X_T^\bullet) = 0$.
  - If $T \not\cong P_Z$, then $K^b(\Phi_Z)(X_T^\bullet) \cong W_T^{c_T}$ for a **single** indecomposable 2-term presilting complex $W_T \in K^b(\mathcal{P}(\mathsf{J}(Z)))$ and an integer $c_T \ge 1$.

*Proof.*
**(a)** Let $n := \mathrm{rk} A$ and write $S = P_Z \oplus T_1 \oplus \cdots \oplus T_{n-1}$ as a basic 2-term silting complex in $K^b(\mathrm{proj} A)$. By Lemma 2.2(b), $X_S^\bullet \cong X_{P_Z}^\bullet \oplus \bigoplus_{k=1}^{n-1} X_{T_k}^\bullet$ in $K^b(\mathrm{add} B)$. By Lemma 2.2(c), $X_S^\bullet$ is a basic 2-term presilting complex in $K^b(\mathrm{add} B)$ with $n$ pairwise non-isomorphic indecomposable summands. Setting $\widetilde{A} := \mathrm{End}_{K^b(\mathrm{proj} A)}(B)^{\mathrm{op}}$ (a finite-dimensional $k$-algebra of rank $|B| = n$), we have an equivalence $K^b(\mathrm{add} B) \simeq K^b(\mathrm{proj} \widetilde{A})$ under which $X_S^\bullet$ is a basic 2-term presilting complex with $n = \mathrm{rk} \widetilde{A}$ summands; hence by [AIR, Thm. 3.2], $X_S^\bullet$ is a 2-term silting complex in $K^b(\mathrm{add} B)$, so $\mathrm{thick}(X_S^\bullet) = K^b(\mathrm{add} B)$.

Next, by [BHM, Lem. 5.7] (`\label{lem:fU-projectives}`), $f_Z \colon \mathrm{add}(B_Z) \to \mathcal{P}(\mathsf{J}(Z))$ is full and dense. Since $H^0 \colon \mathrm{Hom}_{K^b(\mathrm{proj} A)}(P_X, P_Y) \to \mathrm{Hom}_A(X, Y)$ is surjective for all $X, Y \in \mathrm{mod} A$, the composite additive functor $\Phi_Z = f_Z \circ H^0 \colon \mathrm{add}(B) \to \mathcal{P}(\mathsf{J}(Z))$ is **full and dense**.
- *Presilting:* By fullness of $\Phi_Z$, any morphism $K^b(\Phi_Z)(X_S^\bullet) \to K^b(\Phi_Z)(X_S^\bullet)[1]$ (a single map $\Phi_Z(B_1) \to \Phi_Z(B_0)$ in degree $-1$) lifts to a map $B_1 \to B_0$; because $\mathrm{Hom}_{K^b(\mathrm{add} B)}(X_S^\bullet, X_S^\bullet[1]) = 0$, this lift is null-homotopic in $K^b(\mathrm{add} B)$, and applying $\Phi_Z$ shows the original map is null-homotopic in $K^b(\mathcal{P}(\mathsf{J}(Z)))$.
- *Generating:* Since $K^b(\Phi_Z)$ is a triangle functor, $\Phi_Z$ is dense, and $\mathrm{thick}(X_S^\bullet) = K^b(\mathrm{add} B)$, every object of $\mathcal{P}(\mathsf{J}(Z))$ lies in $\mathrm{thick}(K^b(\Phi_Z)(X_S^\bullet))$, so $\mathrm{thick}(K^b(\Phi_Z)(X_S^\bullet)) = K^b(\mathcal{P}(\mathsf{J}(Z)))$.

Thus $K^b(\Phi_Z)(X_S^\bullet)$ is a 2-term silting complex in $K^b(\mathcal{P}(\mathsf{J}(Z)))$, so $\Psi_Z(S) := \mathrm{basic}(K^b(\Phi_Z)(X_S^\bullet)) \in 2\text{-}\mathrm{silt}(\mathsf{J}(Z))$ is well-defined. Moreover, by Lemma 2.2(d),
$$
\mathrm{basic}\!\bigl(H^0(\Psi_Z(S))\bigr) = \mathrm{basic}\!\bigl(H^0(K^b(\Phi_Z)(X_S^\bullet))\bigr) \cong \mathrm{basic}\!\bigl(f_Z(H^0(S))\bigr).
$$
Under the equivalence $\mathsf{J}(Z) \simeq \mathrm{mod}\Gamma$ of [BHM, Thm. 5.1] (Jasso [J, Thm. 1.4]), the maps $S \mapsto \mathrm{basic}(H^0(S))$ and $W \mapsto \mathrm{basic}(H^0(W))$ identify $2\text{-}\mathrm{silt}_{P_Z}(A)$ with $\mathrm{s}\tau\text{-}\mathrm{tilt}_Z(A)$ and $2\text{-}\mathrm{silt}(\mathsf{J}(Z))$ with $\mathrm{s}\tau\text{-}\mathrm{tilt}(\mathsf{J}(Z))$. By Jasso's $\tau$-tilting reduction theorem ([J, Thm. 3.16]), $M \mapsto \mathrm{basic}(f_Z(M))$ is a bijection $\mathrm{s}\tau\text{-}\mathrm{tilt}_Z(A) \xrightarrow{\sim} \mathrm{s}\tau\text{-}\mathrm{tilt}(\mathsf{J}(Z))$. Hence $\Psi_Z$ is a bijection.

**(b)** If $T \cong P_Z$, then $X_{P_Z}^\bullet = (0 \to P_Z)$ and $\Phi_Z(P_Z) = f_Z(Z) = 0$, so $K^b(\Phi_Z)(X_{P_Z}^\bullet) = 0$.

Now assume $T \not\cong P_Z$. Since $T \oplus P_Z$ is 2-term presilting and $A$ is $\tau$-tilting finite, [AIR, Thm. 2.10, Thm. 3.2] allows us to complete $P_Z \oplus T$ to a basic 2-term silting complex $S = P_Z \oplus T_1 \oplus \cdots \oplus T_{n-1} \in 2\text{-}\mathrm{silt}_{P_Z}(A)$ with $T_1 = T$. For each $k \in \{1, \dots, n - 1\}$, by [AIR, Thm. 2.18, Thm. 3.2], there is a unique other basic 2-term silting complex $S_k = P_Z \oplus T_k^* \oplus \bigoplus_{j \ne k} T_j \in 2\text{-}\mathrm{silt}_{P_Z}(A)$ obtained by mutating $S$ at $T_k$ (note that $P_Z$ remains a summand because $T_k \not\cong P_Z$). Since $S_k \not\cong S$ and $\Psi_Z$ is a bijection by (a), we have $\Psi_Z(S_k) \not\cong \Psi_Z(S)$.

Recall that $\mathrm{rk}\mathsf{J}(Z) = n - 1$ ([J, Thm. 3.8]), so every basic 2-term silting complex in $K^b(\mathcal{P}(\mathsf{J}(Z)))$ has exactly $n - 1$ pairwise non-isomorphic indecomposable summands. Since $K^b(\Phi_Z)(X_{P_Z}^\bullet) = 0$, we have
$$
K^b(\Phi_Z)(X_S^\bullet) \cong \bigoplus_{j=1}^{n-1} K^b(\Phi_Z)(X_{T_j}^\bullet) \qquad \text{and} \qquad K^b(\Phi_Z)(X_{S_k}^\bullet) \cong K^b(\Phi_Z)(X_{T_k^*}^\bullet) \oplus \bigoplus_{j \ne k} K^b(\Phi_Z)(X_{T_j}^\bullet).
$$
If every indecomposable summand of $\Psi_Z(S)$ belonged to $\mathrm{add}\bigl(\bigoplus_{j \ne k} K^b(\Phi_Z)(X_{T_j}^\bullet)\bigr)$, then $\Psi_Z(S)$ would be a direct summand of $\Psi_Z(S_k)$, forcing $\Psi_Z(S) \cong \Psi_Z(S_k)$ (both being basic with $n - 1$ summands), a contradiction. Therefore, for each $k \in \{1, \dots, n - 1\}$, there exists an indecomposable direct summand $W_k$ of $\Psi_Z(S)$ such that
$$
W_k \in \mathrm{add}\!\bigl(K^b(\Phi_Z)(X_{T_k}^\bullet)\bigr) \qquad \text{and} \qquad W_k \notin \mathrm{add}\!\bigl(K^b(\Phi_Z)(X_{T_j}^\bullet)\bigr) \quad \text{for all } j \ne k. \tag{6}
$$
In particular, $W_1, \dots, W_{n-1}$ are pairwise non-isomorphic, so they exhaust all $n - 1$ isomorphism classes of indecomposable direct summands of $\Psi_Z(S)$. Now let $W$ be any indecomposable direct summand of $K^b(\Phi_Z)(X_{T_k}^\bullet)$. Then $W \in \mathrm{add}(\Psi_Z(S))$, so $W \cong W_\ell$ for some $\ell \in \{1, \dots, n - 1\}$; by (6), we must have $\ell = k$. Hence $K^b(\Phi_Z)(X_{T_k}^\bullet) \cong W_k^{c_k}$ for some integer $c_k \ge 1$. Taking $k = 1$ gives the result for $T = T_1$. $\square$

---

### Lemma 2.4 (Uniqueness of Jasso Lift for $\tau$-Rigid Summands Outside $\mathrm{Gen} C$)
Let $A$ be a $\tau$-tilting finite finite-dimensional $k$-algebra and $C \in \mathrm{mod} A$ an indecomposable $\tau_A$-rigid module. Let $Y, M \in \mathrm{mod} A$ be indecomposable modules such that both $Y \amalg C$ and $M \amalg C$ are $\tau_A$-rigid. If $f_C(Y) \neq 0$ and $\mathrm{Gen}_{\mathsf{J}(C)}(f_C(Y)) = \mathrm{Gen}_{\mathsf{J}(C)}(f_C(M))$, then $Y \cong M$.

*Proof.* Set $\mathcal{T}_Y := \mathrm{Gen}_A(Y \amalg C)$ and $\mathcal{T}_M := \mathrm{Gen}_A(M \amalg C)$. Since $Y \amalg C$ and $M \amalg C$ are $\tau_A$-rigid, both $\mathcal{T}_Y$ and $\mathcal{T}_M$ lie in the interval $[\mathrm{Gen}_A C, {}^\perp \tau_A C]$ of $\mathrm{tors}(A)$. By Jasso's lattice isomorphism ([J, Thm. 3.23], cf. the proof of [BHM, Lem. 5.11]), the map $\mathcal{T} \mapsto f_C(\mathcal{T}) = \mathcal{T} \cap C^\perp$ is a bijection from $[\mathrm{Gen}_A C, {}^\perp \tau_A C]$ to $\mathrm{tors}(\mathsf{J}(C))$. For any $X \in \mathrm{Gen}_A(Y \amalg C)$, an epimorphism $(Y \amalg C)^d \twoheadrightarrow X$ maps under $f_C$ to an epimorphism $f_C(Y)^d \twoheadrightarrow f_C(X)$, so $f_C(\mathcal{T}_Y) \subseteq \mathrm{Gen}_{\mathsf{J}(C)}(f_C(Y))$; conversely $f_C(Y) \in f_C(\mathcal{T}_Y)$ and $f_C(\mathcal{T}_Y)$ is a torsion class in $\mathsf{J}(C)$, so $f_C(\mathcal{T}_Y) = \mathrm{Gen}_{\mathsf{J}(C)}(f_C(Y))$. The same holds for $M$, whence $f_C(\mathcal{T}_Y) = f_C(\mathcal{T}_M)$ and therefore $\mathcal{T}_Y = \mathcal{T}_M =: \mathcal{T}$.

Finally, since $\mathcal{T} = \mathrm{Gen}_A(Y \amalg C)$, every indecomposable split projective object of $\mathcal{T}$ is a direct summand of $Y \amalg C$ (as $P_s(\mathcal{T})$ is the minimal basic generator of $\mathcal{T}$; see [BHM, §2.2]). Because $f_C(Y) \neq 0$, we have $Y \notin \mathrm{Gen}_A C$, so $\mathcal{T} \neq \mathrm{Gen}_A C$ and $Y$ cannot be omitted from the generator $Y \amalg C$; thus $Y \in \mathrm{add} P_s(\mathcal{T})$. Hence $\mathrm{add}(P_s(\mathcal{T})) \setminus \mathrm{add}(C)$ has $Y$ as its unique indecomposable isomorphism class. By symmetry, $M$ is also the unique indecomposable isomorphism class in $\mathrm{add}(P_s(\mathcal{T})) \setminus \mathrm{add}(C)$, so $Y \cong M$. $\square$

---

### Lemma 2.5 (Inductive Reduction of TF-Ordered Modules and $L_I$)
Let $\Lambda$ be a $\tau$-tilting finite finite-dimensional $k$-algebra, $I \subseteq \mathrm{rad}\Lambda$ a two-sided ideal, and $(M_1, \dots, M_t)$ a TF-ordered $\tau_{\Lambda/I}$-rigid module with $t \ge 2$. Set $(N_1, \dots, N_t) := L_I(M_1, \dots, M_t)$, $C := M_t$, $Z := N_t$, $\overline{M}_j := f_C(M_j) \in \mathsf{J}_{\Lambda/I}(C)$, and $\overline{N}_j := f_Z(N_j) \in \mathsf{J}(Z)$ for $1 \le j \le t - 1$. Under the equivalences
$$
H \colon \mathsf{J}(Z) \xrightarrow{\;\sim\;} \mathrm{mod}\Gamma \qquad \text{and} \qquad H' \colon \mathsf{J}_{\Lambda/I}(C) \xrightarrow{\;\sim\;} \mathrm{mod}(\Gamma/I_Z)
$$
of [BHM, Thm. 5.10] (where $\Gamma$ is $\tau$-tilting finite, $I_Z \subseteq \mathrm{rad}\Gamma$, and $H' \circ F_Z \simeq ((\Gamma/I_Z) \otimes_\Gamma -) \circ H$ naturally):
- **(a)** $Z = P_s({}^\perp \mathrm{Filt}\mathsf{J}_{\Lambda/I}(C))$ is the lift of $C$ in [BHM, Setup 4.1].
- **(b)** $(\overline{M}_1, \dots, \overline{M}_{t-1})$ is a TF-ordered $\tau_{\mathsf{J}_{\Lambda/I}(C)}$-rigid module in $\mathsf{J}_{\Lambda/I}(C)$, and $(H(\overline{N}_1), \dots, H(\overline{N}_{t-1})) = L_{I_Z}(H'(\overline{M}_1), \dots, H'(\overline{M}_{t-1}))$.

*Proof.*
First, we check that for any $\tau$-tilting finite algebra $A$ and any TF-ordered $\tau_A$-rigid module $(U_1, \dots, U_t)$ ($t \ge 2$) with $U := U_t$ and $\overline{U}_j := f_U(U_j) \in \mathsf{J}(U)$ ($1 \le j \le t - 1$):
1. Since $\coprod_{j=1}^t U_j$ is $\tau_A$-rigid and $U_j \notin \mathrm{Gen}_A(\coprod_{k=j+1}^t U_k) \supseteq \mathrm{Gen}_A U$, each $\overline{U}_j = f_U(U_j)$ is nonzero, and by Jasso's reduction ([J, Thm. 3.16], [BM, Prop. 4.10]), each $\overline{U}_j$ is indecomposable and $\coprod_{j=1}^{t-1} \overline{U}_j$ is $\tau_{\mathsf{J}(U)}$-rigid.
2. For each $1 \le i \le t - 1$, let $\mathcal{U}_i := \mathrm{Gen}_A(\coprod_{k=i+1}^t U_k) \in [\mathrm{Gen}_A U, {}^\perp \tau_A U]$. As in Lemma 2.4, $f_U(\mathcal{U}_i) = \mathcal{U}_i \cap \mathsf{J}(U) = \mathrm{Gen}_{\mathsf{J}(U)}(\coprod_{k=i+1}^{t-1} \overline{U}_k)$. If $\overline{U}_i \in \mathrm{Gen}_{\mathsf{J}(U)}(\coprod_{k=i+1}^{t-1} \overline{U}_k) \subseteq \mathcal{U}_i$, then the canonical exact sequence $0 \to t_U(U_i) \to U_i \to \overline{U}_i \to 0$ (with $t_U(U_i) \in \mathrm{Gen}_A U \subseteq \mathcal{U}_i$) would place $U_i \in \mathcal{U}_i$ by extension-closure of $\mathcal{U}_i$, contradicting TF-ordering. Thus $(\overline{U}_1, \dots, \overline{U}_{t-1})$ is a TF-ordered $\tau_{\mathsf{J}(U)}$-rigid module in $\mathsf{J}(U)$.
3. For each $1 \le i \le t - 1$, let $\overline{\mathcal{U}}_i := \mathrm{Gen}_{\mathsf{J}(U)}(\coprod_{k=i+1}^{t-1} \overline{U}_k) = \mathcal{U}_i \cap \mathsf{J}(U)$, and consider the torsion-free quotient $f_{\overline{\mathcal{U}}_i}^{\mathsf{J}(U)}(\overline{U}_i)$ in $\mathsf{J}(U)$. The kernel of the composite surjection $U_i \twoheadrightarrow \overline{U}_i \twoheadrightarrow f_{\overline{\mathcal{U}}_i}^{\mathsf{J}(U)}(\overline{U}_i)$ is an extension of $t_{\overline{\mathcal{U}}_i}^{\mathsf{J}(U)}(\overline{U}_i) \in \overline{\mathcal{U}}_i \subseteq \mathcal{U}_i$ by $t_U(U_i) \in \mathrm{Gen}_A U \subseteq \mathcal{U}_i$, hence lies in $\mathcal{U}_i$. Moreover, $f_{\overline{\mathcal{U}}_i}^{\mathsf{J}(U)}(\overline{U}_i) \in \mathsf{J}(U) \cap \overline{\mathcal{U}}_i^{\perp_{\mathsf{J}(U)}} = \mathcal{U}_i^\perp$ (for any $X \in \mathcal{U}_i$, every morphism $X \to Y$ with $Y \in \mathsf{J}(U) \subseteq U^\perp$ factors through $f_U(X) \in \overline{\mathcal{U}}_i$, hence vanishes if $Y \in \overline{\mathcal{U}}_i^{\perp_{\mathsf{J}(U)}}$). By uniqueness of the canonical torsion-free quotient modulo $\mathcal{U}_i$, we obtain
   $$
   f_{\overline{U}_{i+1} \amalg \cdots \amalg \overline{U}_{t-1}}^{\mathsf{J}(U)}(\overline{U}_i) \;\cong\; f_{U_{i+1} \amalg \cdots \amalg U_t}(U_i) \qquad (1 \le i \le t - 1). \tag{7}
   $$
   Consequently, if $\omega_A(U_1, \dots, U_t) = (C_1, \dots, C_{t-1}, U)$, then $\omega_{\mathsf{J}(U)}(\overline{U}_1, \dots, \overline{U}_{t-1}) = (C_1, \dots, C_{t-1})$.

Now apply this to $(M_1, \dots, M_t)$ over $\Lambda/I$ and $(N_1, \dots, N_t)$ over $\Lambda$. Write $\omega_I(M_1, \dots, M_t) = (C_1, \dots, C_{t-1}, C)$ and $\Delta_I(C_1, \dots, C_{t-1}, C) = (Z_1, \dots, Z_{t-1}, Z_t)$. By the recursive definition of $\Delta_I$ in the proof of [BHM, Thm. 1.1] (lines 1604–1648 of `lifting_arxiv_25102026.tex`), $Z_t = P_s({}^\perp \mathrm{Filt}\mathsf{J}_{\Lambda/I}(C))$ is the Setup 4.1 lift of $C$, and under the equivalences $H, H'$ of [BHM, Thm. 5.10], $(H(Z_1), \dots, H(Z_{t-1})) = \Delta_{I_Z}(H'(C_1), \dots, H'(C_{t-1}))$. Since $\omega(N_1, \dots, N_t) = (Z_1, \dots, Z_{t-1}, Z_t)$, we have $Z = N_t = Z_t$, proving (a). By (7) applied over $\Lambda/I$ and $\Lambda$ (and the fact that the $k$-linear abelian equivalences $H, H'$ commute with the Mendoza–Treffinger bijections), we have
$$
\omega_{\Gamma}(H(\overline{N}_1), \dots, H(\overline{N}_{t-1})) = (H(Z_1), \dots, H(Z_{t-1})) = \Delta_{I_Z}(H'(C_1), \dots, H'(C_{t-1})) = \Delta_{I_Z} \omega_{\Gamma/I_Z}(H'(\overline{M}_1), \dots, H'(\overline{M}_{t-1})).
$$
Applying $\omega_\Gamma^{-1}$ gives $(H(\overline{N}_1), \dots, H(\overline{N}_{t-1})) = L_{I_Z}(H'(\overline{M}_1), \dots, H'(\overline{M}_{t-1}))$, proving (b). $\square$

---

## 3. Proof of Theorem 1

We prove Theorem 1 by induction on the length $t \ge 1$ over all $\tau$-tilting finite finite-dimensional $k$-algebras $\Lambda$ and all two-sided ideals $I \subseteq \mathrm{rad}\Lambda$.

### Base case ($t = 1$) and the final term ($i = t$ for any $t \ge 1$)
By Lemma 2.5(a) (and directly by definition of $\Delta_I$ when $t = 1$), $N_t = Z$ is the Setup 4.1 lift of $M_t = C$. By Lemma 2.1(c), $F(P_{N_t}) \cong P_{M_t}^{r_t}$ in $K^b(\mathrm{proj}(\Lambda/I))$ for some integer $r_t \ge 1$. This establishes both the base case $t = 1$ and the index $i = t$ for every $t \ge 1$.

### Inductive step ($t \ge 2$)
Assume Theorem 1 holds for all sequences of length $t - 1$ over every $\tau$-tilting finite algebra $\Gamma$ and ideal $J \subseteq \mathrm{rad}\Gamma$. Let $(M_1, \dots, M_t)$ be a TF-ordered $\tau_{\Lambda/I}$-rigid module and $(N_1, \dots, N_t) = L_I(M_1, \dots, M_t)$. Fix an index $1 \le i \le t - 1$.

Set $C := M_t$, $Z := N_t$, $\overline{M}_j := f_C(M_j) \in \mathsf{J}_{\Lambda/I}(C)$, and $\overline{N}_j := f_Z(N_j) \in \mathsf{J}(Z)$ for $1 \le j \le t - 1$. Let $B_Z := P({}^\perp \tau_\Lambda Z)$, $B := P_{B_Z} \in K^b(\mathrm{proj}\Lambda)$, $B_C := P({}^{\perp_{\Lambda/I}} \tau_{\Lambda/I} C)$, and $B' := P_{B_C} \in K^b(\mathrm{proj}(\Lambda/I))$.

**Step 1 (Commutative square on bounded homotopy categories).**
By Lemma 2.1(c), the functor $F$ restricts to an additive functor $F \colon \mathrm{add}(B) \to \mathrm{add}(B')$. Consider the diagram of additive functors
$$
\begin{array}{ccc}
\mathrm{add}(B) & \xrightarrow{\;\Phi_Z = f_Z \circ H^0\;} & \mathcal{P}(\mathsf{J}(Z)) \\[4pt]
\downarrow F & & \downarrow F_Z \\[4pt]
\mathrm{add}(B') & \xrightarrow{\;\Phi_C = f_C \circ H^0\;} & \mathcal{P}(\mathsf{J}_{\Lambda/I}(C)),
\end{array}
\tag{8}
$$
where $F_Z = f_C F|_{\mathsf{J}(Z)} \colon \mathsf{J}(Z) \to \mathsf{J}_{\Lambda/I}(C)$ is the right exact functor of [BHM, Prop. 5.6], which maps $\mathcal{P}(\mathsf{J}(Z))$ into $\mathcal{P}(\mathsf{J}_{\Lambda/I}(C))$ by [BHM, Prop. 5.8]. We verify that (8) commutes up to natural isomorphism: for every $X \in \mathrm{add}(B)$, right exactness of $F$ gives a canonical isomorphism $\alpha_X \colon F(H^0(X)) \xrightarrow{\sim} H^0(F(X))$ natural in $X \in K^b(\mathrm{proj}\Lambda)$. Since $H^0(X) \in \mathrm{add}(B_Z) \subseteq {}^\perp \tau_\Lambda Z$, [BHM, Prop. 5.6] supplies a natural isomorphism $\rho_{H^0(X)} \colon f_C F(H^0(X)) \xrightarrow{\sim} F_Z f_Z(H^0(X))$. Composing gives a natural isomorphism
$$
\theta_X := \rho_{H^0(X)} \circ f_C(\alpha_X)^{-1} \colon \Phi_C(F(X)) = f_C H^0(F(X)) \xrightarrow{\;\sim\;} F_Z f_Z(H^0(X)) = F_Z(\Phi_Z(X))
$$
for $X \in \mathrm{add}(B)$. Applying $K^b(-)$ termwise therefore yields a natural isomorphism of triangle functors
$$
K^b(\Phi_C) \circ K^b(F) \;\simeq\; K^b(F_Z) \circ K^b(\Phi_Z) \colon K^b(\mathrm{add} B) \longrightarrow K^b(\mathcal{P}(\mathsf{J}_{\Lambda/I}(C))). \tag{9}
$$

**Step 2 (Evaluating the right-then-down path on $X_{P_{N_i}}^\bullet$).**
Since $N_i \amalg Z$ is $\tau_\Lambda$-rigid, $P_{N_i} \oplus P_Z$ is 2-term presilting in $K^b(\mathrm{proj}\Lambda)$, so Lemma 2.2(b) gives a distinguished triangle
$$
B_1 \xrightarrow{\;\phi\;} B_0 \xrightarrow{\;g\;} P_{N_i} \longrightarrow B_1[1] \qquad (B_0, B_1 \in \mathrm{add} B) \tag{10}
$$
and the associated complex $X^\bullet := X_{P_{N_i}}^\bullet = (B_1 \xrightarrow{\phi} B_0) \in K^b(\mathrm{add} B)$. Since $(N_1, \dots, N_t)$ is TF-ordered, $N_i \notin \mathrm{Gen}_\Lambda Z$, so $P_{N_i} \not\cong P_Z$ and $\overline{N}_i = f_Z(N_i)$ is nonzero and indecomposable in $\mathsf{J}(Z)$ (Lemma 2.5(b)). By Proposition 2.3(b) and Lemma 2.2(d),
$$
K^b(\Phi_Z)(X^\bullet) \;\cong\; W^{c_0}
$$
for a single indecomposable 2-term presilting complex $W \in K^b(\mathcal{P}(\mathsf{J}(Z)))$ and an integer $c_0 \ge 1$, with $H^0(W)^{c_0} \cong H^0(K^b(\Phi_Z)(X^\bullet)) \cong f_Z(N_i) = \overline{N}_i$. Because $\overline{N}_i$ is nonzero and indecomposable in the Krull–Schmidt category $\mathsf{J}(Z)$, this forces $c_0 = 1$ and $H^0(W) \cong \overline{N}_i \neq 0$; hence $W$ cannot be a shifted projective and must equal the minimal projective presentation $P_{\overline{N}_i}^{\mathsf{J}(Z)}$ of $\overline{N}_i$ in $\mathsf{J}(Z)$:
$$
K^b(\Phi_Z)(X^\bullet) \;\cong\; P_{\overline{N}_i}^{\mathsf{J}(Z)}.
$$

Now let $H \colon \mathsf{J}(Z) \xrightarrow{\sim} \mathrm{mod}\Gamma$ and $H' \colon \mathsf{J}_{\Lambda/I}(C) \xrightarrow{\sim} \mathrm{mod}(\Gamma/I_Z)$ be the equivalences of [BHM, Thm. 5.10] (so $\Gamma$ is $\tau$-tilting finite by [J, Thm. 3.15], $I_Z \subseteq \mathrm{rad}\Gamma$, and $H' \circ F_Z \simeq ((\Gamma/I_Z) \otimes_\Gamma -) \circ H$ naturally). By Lemma 2.5(b), $(H(\overline{N}_1), \dots, H(\overline{N}_{t-1})) = L_{I_Z}(H'(\overline{M}_1), \dots, H'(\overline{M}_{t-1}))$. Applying the induction hypothesis for length $t - 1$ to $(\Gamma, I_Z)$ and transporting back along the exact equivalences $K^b(H) \colon K^b(\mathcal{P}(\mathsf{J}(Z))) \xrightarrow{\sim} K^b(\mathrm{proj}\Gamma)$ and $K^b(H') \colon K^b(\mathcal{P}(\mathsf{J}_{\Lambda/I}(C))) \xrightarrow{\sim} K^b(\mathrm{proj}(\Gamma/I_Z))$, we obtain integers $r_i \ge 1$ and $s_{ij} \ge 0$ ($i < j \le t - 1$) such that in $K^b(\mathcal{P}(\mathsf{J}_{\Lambda/I}(C)))$:
$$
K^b(F_Z)\bigl(K^b(\Phi_Z)(X^\bullet)\bigr) \;\cong\; K^b(F_Z)\bigl(P_{\overline{N}_i}^{\mathsf{J}(Z)}\bigr) \;\cong\; \bigl(P_{\overline{M}_i}^{\mathsf{J}_{\Lambda/I}(C)}\bigr)^{r_i} \;\oplus\; \bigoplus_{j=i+1}^{t-1} \bigl(P_{\overline{M}_j}^{\mathsf{J}_{\Lambda/I}(C)}\bigr)^{s_{ij}}. \tag{11}
$$

**Step 3 (Evaluating the down-then-right path on $X_{P_{N_i}}^\bullet$).**
Decompose $F(P_{N_i})$ into indecomposable objects in the Krull–Schmidt category $K^b(\mathrm{proj}(\Lambda/I))$:
$$
F(P_{N_i}) \;\cong\; \bigoplus_{\alpha=1}^m T_\alpha. \tag{12}
$$
Since $P_{N_i} \oplus P_Z$ is 2-term presilting in $K^b(\mathrm{proj}\Lambda)$, Lemma 2.1(a) and (c) show that
$$
F(P_{N_i} \oplus P_Z) \;\cong\; \left(\bigoplus_{\alpha=1}^m T_\alpha\right) \oplus P_C^{r_t}
$$
is 2-term presilting in $K^b(\mathrm{proj}(\Lambda/I))$. In particular, $T_\alpha \oplus P_C$ is 2-term presilting for every $1 \le \alpha \le m$.

Applying the triangle functor $F \colon K^b(\mathrm{proj}\Lambda) \to K^b(\mathrm{proj}(\Lambda/I))$ to the distinguished triangle (10) yields a distinguished triangle in $K^b(\mathrm{proj}(\Lambda/I))$:
$$
F(B_1) \xrightarrow{\;F(\phi)\;} F(B_0) \xrightarrow{\;F(g)\;} F(P_{N_i}) \longrightarrow F(B_1)[1], \qquad F(B_0), F(B_1) \in \mathrm{add}(B').
$$
On the other hand, applying Lemma 2.2(b) over $(\Lambda/I, C)$ to each $T_\alpha$ gives distinguished triangles $B'_{\alpha,1} \to B'_{\alpha,0} \to T_\alpha \to B'_{\alpha,1}[1]$ with $B'_{\alpha,0}, B'_{\alpha,1} \in \mathrm{add}(B')$; their direct sum is a distinguished triangle $B'_1 \to B'_0 \to F(P_{N_i}) \to B'_1[1]$ with $B'_0, B'_1 \in \mathrm{add}(B')$ whose associated 2-term complex is $\bigoplus_{\alpha=1}^m X_{T_\alpha}^\bullet$. By the uniqueness assertion of Lemma 2.2(b) applied to the 2-term complex $F(P_{N_i})$ over $(\Lambda/I, C)$, both $K^b(F)(X^\bullet)$ and $\bigoplus_{\alpha=1}^m X_{T_\alpha}^\bullet$ are isomorphic to $X_{F(P_{N_i})}^\bullet$ in $K^b(\mathrm{add} B')$, so
$$
K^b(F)(X^\bullet) = \bigl(F(B_1) \xrightarrow{F(\phi)} F(B_0)\bigr) \;\cong\; \bigoplus_{\alpha=1}^m X_{T_\alpha}^\bullet.
$$
Applying $K^b(\Phi_C)$ and Proposition 2.3(b) over $(\Lambda/I, C)$ yields
$$
K^b(\Phi_C)\bigl(K^b(F)(X^\bullet)\bigr) \;\cong\; \bigoplus_{\alpha=1}^m K^b(\Phi_C)(X_{T_\alpha}^\bullet) \;\cong\; \bigoplus_{\substack{1 \le \alpha \le m \\ T_\alpha \not\cong P_C}} W_\alpha^{c_\alpha}, \tag{13}
$$
where for each $\alpha$ with $T_\alpha \not\cong P_C$, $W_\alpha \in K^b(\mathcal{P}(\mathsf{J}_{\Lambda/I}(C)))$ is an indecomposable 2-term presilting complex, $c_\alpha \ge 1$, and $H^0(W_\alpha)^{c_\alpha} \cong f_C(H^0(T_\alpha))$ by Lemma 2.2(d).

**Step 4 (Matching summands via Krull–Schmidt).**
Combining (9), (11), and (13) gives an isomorphism in the Krull–Schmidt category $K^b(\mathcal{P}(\mathsf{J}_{\Lambda/I}(C)))$:
$$
\bigoplus_{\substack{1 \le \alpha \le m \\ T_\alpha \not\cong P_C}} W_\alpha^{c_\alpha} \;\cong\; \bigl(P_{\overline{M}_i}^{\mathsf{J}_{\Lambda/I}(C)}\bigr)^{r_i} \;\oplus\; \bigoplus_{j=i+1}^{t-1} \bigl(P_{\overline{M}_j}^{\mathsf{J}_{\Lambda/I}(C)}\bigr)^{s_{ij}}. \tag{14}
$$
Take any $\alpha \in \{1, \dots, m\}$ with $T_\alpha \not\cong P_C$. By the Krull–Schmidt theorem, there exists a unique index $j \in \{i, \dots, t - 1\}$ such that $W_\alpha \cong P_{\overline{M}_j}^{\mathsf{J}_{\Lambda/I}(C)}$. Taking $H^0$ gives
$$
f_C(H^0(T_\alpha)) \;\cong\; H^0(W_\alpha)^{c_\alpha} \;\cong\; \overline{M}_j^{c_\alpha} \neq 0.
$$
In particular, $H^0(T_\alpha) \neq 0$, so the indecomposable 2-term presilting complex $T_\alpha$ cannot be a shifted projective $Q[1]$; thus $T_\alpha \cong P_{Y_\alpha}$ for an indecomposable $\tau_{\Lambda/I}$-rigid module $Y_\alpha$ such that $Y_\alpha \amalg C$ is $\tau_{\Lambda/I}$-rigid and $f_C(Y_\alpha) \cong \overline{M}_j^{c_\alpha} \neq 0$. Therefore $\mathrm{Gen}_{\mathsf{J}_{\Lambda/I}(C)}(f_C(Y_\alpha)) = \mathrm{Gen}_{\mathsf{J}_{\Lambda/I}(C)}(\overline{M}_j) = \mathrm{Gen}_{\mathsf{J}_{\Lambda/I}(C)}(f_C(M_j))$, so Lemma 2.4 yields
$$
Y_\alpha \;\cong\; M_j, \qquad \text{and hence} \qquad T_\alpha \;\cong\; P_{M_j}.
$$
In addition, since $f_C(M_j) = \overline{M}_j$ is indecomposable, $f_C(Y_\alpha) \cong \overline{M}_j^{c_\alpha}$ forces $c_\alpha = 1$.

Now match multiplicities in (14): since $c_\alpha = 1$ for every $\alpha$ with $T_\alpha \not\cong P_C$, and the modules $\overline{M}_i, \dots, \overline{M}_{t-1}$ are pairwise non-isomorphic (as $(\overline{M}_1, \dots, \overline{M}_{t-1})$ is TF-ordered), the summands $T_\alpha \not\cong P_C$ in (12) consist of exactly $r_i \ge 1$ copies of $P_{M_i}$ and exactly $s_{ij} \ge 0$ copies of $P_{M_j}$ for each $i < j \le t - 1$. Every remaining summand $T_\alpha$ in (12) is isomorphic to $P_C = P_{M_t}$; letting $s_{it} \ge 0$ be the number of such summands, (12) becomes
$$
F(P_{N_i}) \;\cong\; P_{M_i}^{r_i} \;\oplus\; \bigoplus_{j=i+1}^t P_{M_j}^{s_{ij}} \qquad (r_i \ge 1,\; s_{ij} \ge 0).
$$
This completes the induction and proves Theorem 1 and Corollary 2 (Conjecture 7.2). $\square$

---

## References

- **[AI]** T. Aihara and O. Iyama, *Silting mutation in triangulated categories*, J. Lond. Math. Soc. (2) **85** (2012), no. 3, 633–668.
- **[AIR]** T. Adachi, O. Iyama, and I. Reiten, *$\tau$-tilting theory*, Compos. Math. **150** (2014), no. 3, 415–452.
- **[BHM]** A. B. Buan, E. J. Hanson, and B. R. Marsh, *Lifting $\tau$-exceptional sequences*, `arXiv:2610.34398v1` (2026-10-25).
- **[BM]** A. B. Buan and B. R. Marsh, *$\tau$-exceptional sequences*, J. Algebra **585** (2021), 36–68.
- **[J]** G. Jasso, *Reduction of $\tau$-tilting modules and torsion pairs*, Int. Math. Res. Not. IMRN **2015**, no. 16, 7190–7237.

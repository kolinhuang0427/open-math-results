# Exponential Separation of $1\text{-SRC-II}$ ($\mathrm{SRC}\text{-}\mathrm{II}[1]$) from Resolution (`arXiv:2606.25895v1`, §§ 2 & 6)

**Target:** Nikita Gaevoy, *The Power of Small Symmetries*, `arXiv:2606.25895v1` (MFCS 2026), Section 2 (*Preliminaries*, `static/definitions.tex` L127–142) and Section 6 (*Conclusion and Open Problems*, `static/open.tex` L3–5):

> We have shown that the systems $3\text{-SRC-I}$ and $6\text{-SR-I}$ are stronger than Resolution. The question of whether systems with smaller constraints are stronger than Resolution is open. It seems plausible that a separation exists even for $1\text{-SRC-II}$ and Resolution.

*(Note on notation: in Gaevoy's TeX source, `\SRCII[1]` compiles as $1\text{-SRC-II}$, denoting Resolution with local $1$-symmetries; `TARGET.md` writes $\mathrm{SRC}\text{-}\mathrm{II}[1]$.)*

**Answer:** **YES.** Resolution with local $1$-symmetries ($1\text{-SRC-II}$) is **exponentially separated** from Resolution ($\mathrm{Res}$), in the exact sense of Gaevoy's Definition 9 (`static/definitions.tex` L104). Moreover, applying the same guarded-clause construction to Gaevoy's toroidal-grid Tseitin formulas $T_n$ yields an exponential separation of $1\text{-SRC-II}$ even from bounded-depth Frege.

> **Main Theorem.** There exists a family of unsatisfiable bounded-width CNF formulas $\{\Phi_n\}_{n \ge 2}$ on $N_n = \Theta(n)$ variables and $M_n = \Theta(n)$ clauses (width $\le 17$) such that:
> $$S_{1\text{-SRC-II}}(\Phi_n) = O(n^2) = O(N_n^2) \qquad \text{and} \qquad S_{\mathrm{Res}}(\Phi_n) = 2^{\Omega(n)} = 2^{\Omega(N_n)}.$$
> In particular, $1\text{-SRC-II}$ is exponentially separated from $\mathrm{Res}$ (and $\mathrm{Res}$ does not p-simulate $1\text{-SRC-II}$).

**Proof Overview.** Given any connected bounded-degree graph $G = (V, E)$ with odd-sum charge $\alpha : V \to \mathbb{F}_2$, we introduce a **single** fresh guard variable $g \notin E$ and define the *guarded Tseitin formula*
$$\widetilde{\operatorname{Ts}}(G, \alpha) := \bigl\{C \lor \neg g : C \in \operatorname{Ts}(G, \alpha)\bigr\} \;\cup\; \bigl\{D \lor g : D \in \operatorname{All}(G)\bigr\},$$
where $\operatorname{Ts}(G, \alpha)$ consists of the standard Tseitin clauses forbidding invalid edge-parity assignments at each vertex, and $\operatorname{All}(G)$ consists of *all* $2^{\deg(v)}$ full clauses over the incident edges of each vertex $v \in V$.
- **Lower bound (Resolution and depth-$d$ Frege):** Setting $g = 1$ satisfies every clause $D \lor g$ and reduces $\widetilde{\operatorname{Ts}}(G, \alpha)$ identically to $\operatorname{Ts}(G, \alpha)$, so $S_{\mathrm{Res}}(\widetilde{\operatorname{Ts}}(G, \alpha)) \ge S_{\mathrm{Res}}(\operatorname{Ts}(G, \alpha))$. On any constant-degree expander family $\{G_n\}$, Ben-Sasson–Wigderson yields $S_{\mathrm{Res}}(\operatorname{Ts}(G_n, \alpha_n)) = 2^{\Omega(n)}$.
- **Upper bound ($1\text{-SRC-II}$):** Although $\widetilde{\operatorname{Ts}}(G, \alpha)$ has no nontrivial global $1$-symmetries, the single guard literal $g$ acts as a *local parity-flipping bridge*. Any derivation $\mathcal{B} \vdash A \lor \neg g$ from $\mathcal{B} \subseteq \{C \lor \neg g : C \in \operatorname{Ts}(U, \alpha)\}$ (for a vertex subset $U \subseteq V$) can simulate an *arbitrary* local sign-flip symmetry $\phi_F$ (flipping any edge set $F \subseteq E$ that has even degree at every $u \in U$) in $|F| + 2$ consecutive local $1$-symmetry steps:
  $$\mathcal{B} \xrightarrow{\;\phi_g\;} \phi_g(\mathcal{B}) \xrightarrow{\;\phi_{f_1}\;} \cdots \xrightarrow{\;\phi_{f_{|F|}}\;} \phi_F(\phi_g(\mathcal{B})) \xrightarrow{\;\phi_g\;} \phi_F(\mathcal{B}).$$
  Every intermediate premise set lies inside $\{D \lor g : D \in \operatorname{All}(U)\} \subseteq \widetilde{\operatorname{Ts}}(G, \alpha)$, and because every $u \in U$ has even degree in $F$, the final flip $\phi_g$ lands back inside $\{C \lor \neg g : C \in \operatorname{Ts}(U, \alpha)\} \subseteq \widetilde{\operatorname{Ts}}(G, \alpha)$. Growing $U$ vertex-by-vertex along a spanning tree of $G$ derives the unit clause $\neg g$ in $O(2^\Delta n |E|)$ steps, while resolving $\operatorname{All}(v_1) \lor g$ yields $g$ in $2^{\deg(v_1)} - 1$ steps; one final resolution on $g$ gives $\square$.

All components of the Main Theorem — including the existence of bounded-degree connected expanders (Lemma 1), the restriction lower bound (Lemma 2), the Tseitin width lower bound (Lemma 3), the size-width theorem (Lemma 4), and the explicit $1\text{-SRC-II}$ refutation (Theorem 5) — are proved completely and self-containedly below.

---

## 1. Exact Definitions (`arXiv:2606.25895v1`, Section 2 & Section 4)

We follow Gaevoy's exact definitions (`static/definitions.tex` Definitions 1, 2, 4, 8, 9; `static/tseitin.tex` Definition 21):

- A *clause* is a finite set (disjunction) of literals containing no complementary pair $\{x, \neg x\}$; the empty clause is $\square$. The *width* $w(C) := |C|$ is the number of literals in $C$; a $k$-CNF is a set of clauses of width at most $k$.
- A **$1$-symmetry** (Definition 1) is a bijection $\phi$ on literals satisfying $\phi(\neg x) = \neg \phi(x)$ and fixing all variables except at most one. The unique nontrivial $1$-symmetry supported on variable $v$ is the sign flip $\phi_v$ sending $v \mapsto \neg v$, $\neg v \mapsto v$, and $\ell \mapsto \ell$ for all literals $\ell \notin \{v, \neg v\}$. For a clause $C$, $\phi(C) := \{\phi(\ell) : \ell \in C\}$; for a set of clauses $\mathcal{B}$, $\phi(\mathcal{B}) := \{\phi(B) : B \in \mathcal{B}\}$.
- A **$1\text{-SRC-II}$ (Resolution with local $1$-symmetries) refutation** of a CNF $\Phi$ (Definitions 2 and 4) is a sequence of lines $(C_1, \dots, C_s)$ with $C_s = \square$, where each line $i$ carries a derived clause $C_i$ together with its premise set $L(i) \subseteq \Phi$ (representing the derived inference $L(i) \vdash C_i$), generated by one of:
  1. **Input:** $C_i \in \Phi$, with $L(i) := \{C_i\}$.
  2. **Resolution:** $C_i = (A \cup B)$ derived from earlier lines $C_{i_1} = A \cup \{x\}$ and $C_{i_2} = B \cup \{\neg x\}$ (assuming $A \cup B$ is non-tautological), with $L(i) := L(i_1) \cup L(i_2)$.
  3. **Local $1$-symmetry:** For a $1$-symmetry $\phi$ and an earlier line $j < i$ (providing the justification $L(j) \vdash C_j$), such that all clauses of $L(j)$ and all clauses of $\phi(L(j))$ belong to $\Phi$ and every clause of $\phi(L(j))$ has already appeared in the proof before line $i$, infer $C_i := \phi(C_j)$ with resulting inference $\phi(L(j)) \vdash \phi(C_j)$, i.e., $L(i) := \phi(L(j))$.
  The proof *size* is the number of steps $s$, and $S_{1\text{-SRC-II}}(\Phi)$ (Definition 8) is the minimum number of steps in any $1\text{-SRC-II}$ refutation of $\Phi$. (Similarly, $S_{\mathrm{Res}}(\Phi)$ is the minimum number of steps in a Resolution refutation using only rules 1–2.)
- For a finite graph $G = (V, E)$ and a charge function $\alpha : V \to \mathbb{F}_2$ with $\sum_{v \in V} \alpha(v) = 1 \pmod 2$, introduce one Boolean variable $x_e$ per edge $e \in E$ (we identify each edge $e$ with its variable $x_e$). For any subset $S \subseteq E$ and assignment $\sigma : S \to \{0, 1\}$, let
  $$C(\sigma) := \bigl\{\neg e : e \in S,\ \sigma(e) = 1\bigr\} \cup \bigl\{e : e \in S,\ \sigma(e) = 0\bigr\}$$
  be the unique clause over $S$ falsified by $\sigma$. For each vertex $v \in V$ with incident edge set $\partial(v) := \{e \in E : v \in e\}$:
  $$\operatorname{All}(v) := \bigl\{C(\sigma) : \sigma \in \{0, 1\}^{\partial(v)}\bigr\}, \qquad \operatorname{Ts}(v, \alpha) := \Bigl\{C(\sigma) \in \operatorname{All}(v) : \sum_{e \in \partial(v)} \sigma(e) \not\equiv \alpha(v) \pmod 2\Bigr\}.$$
  For $U \subseteq V$, set $\operatorname{Ts}(U, \alpha) := \bigcup_{u \in U} \operatorname{Ts}(u, \alpha)$, $\operatorname{All}(U) := \bigcup_{u \in U} \operatorname{All}(u)$, $\operatorname{Ts}(G, \alpha) := \operatorname{Ts}(V, \alpha)$, and $\operatorname{All}(G) := \operatorname{All}(V)$. Note that $|\operatorname{Ts}(v, \alpha)| = 2^{\deg(v) - 1}$ and $|\operatorname{All}(v)| = 2^{\deg(v)}$.
- Let $g \notin E$ be a single fresh Boolean variable. Define the **guarded Tseitin formula**
  $$\widetilde{\operatorname{Ts}}(G, \alpha) := \bigl\{C \lor \neg g : C \in \operatorname{Ts}(G, \alpha)\bigr\} \;\cup\; \bigl\{D \lor g : D \in \operatorname{All}(G)\bigr\},$$
  which has $N = |E| + 1$ variables, at most $\sum_{v \in V} 3 \cdot 2^{\deg(v) - 1}$ clauses (with equality for connected simple graphs on $|V| \ge 3$ vertices, where the incident edge sets $\partial(v)$ are pairwise distinct), and maximum clause width $\Delta(G) + 1$ (where $\Delta(G) := \max_{v \in V} \deg(v)$). It is unsatisfiable: setting $g = 1$ forces all parity equations $\sum_{e \ni v} x_e \equiv \alpha(v) \pmod 2$, whose sum over $V$ gives $0 \equiv \sum_{v \in V} \alpha(v) = 1 \pmod 2$; setting $g = 0$ leaves all $2^{\deg(v)}$ clauses of $\operatorname{All}(v)$ at every vertex $v \in V$, which forbid every assignment on $\partial(v)$.

---

## 2. Existence of Bounded-Degree Connected Expanders

For a graph $G = (V, E)$ on $n = |V| \ge 2$ vertices and any $U \subseteq V$, let $\partial_G(U) := \{\{u, w\} \in E : u \in U,\ w \in V \setminus U\}$ denote the edge boundary of $U$. Define the *edge expansion* of $G$ by
$$e(G) := \min_{1 \le |U| \le \lfloor n/2 \rfloor} \frac{|\partial_G(U)|}{|U|}.$$

### Lemma 1 (Self-Contained Expander Existence)
For every integer $n \ge 2$, there exists a simple connected graph $G_n = (V_n, E_n)$ on $n$ vertices with maximum degree $\Delta(G_n) \le 16$, edge count $n/2 \le |E_n| \le 8n$, and edge expansion $e(G_n) > 1/8$.

*Proof.* Let $V_n = \{1, \dots, n\}$, and sample $k = 8$ independent uniformly random permutations $\pi_1, \dots, \pi_8 \in S_n$. Form the simple undirected graph $G = (V_n, E)$ with edge set
$$E := \bigl\{\{v, \pi_i(v)\} : v \in V_n,\ 1 \le i \le 8,\ \pi_i(v) \neq v\bigr\}$$
(discarding self-loops and deduplicating parallel edges). Every vertex $v$ is incident only to edges $\{v, \pi_i(v)\}$ and $\{\pi_i^{-1}(v), v\}$ ($1 \le i \le 8$), so $\Delta(G) \le 16$ and hence $|E| \le \frac{1}{2} \cdot 16 n = 8n$.

Fix any integer $u$ with $1 \le u \le \lfloor n/2 \rfloor$, and set $s := \lfloor u/8 \rfloor$ and $t := u + s$. Notice that $s \le u/8 \le n/16 < n/2 \le n - u$, so $t < n$, and indeed $t \le \frac{9}{8} u \le \frac{9}{16} n$. Suppose some $u$-element subset $U \subseteq V_n$ satisfies $|\partial_G(U)| \le s$. Let $B := \{w \in V_n \setminus U : \exists\, v \in U,\ \{v, w\} \in E\}$. Since every $w \in B$ contributes at least one edge to $\partial_G(U)$, we have $|B| \le |\partial_G(U)| \le s$. Hence there exists a subset $T_0 \subseteq V_n \setminus U$ of cardinality exactly $s$ containing $B$. Putting $T := U \cup T_0$ ($|T| = t$), for every $v \in U$ and every $i \in \{1, \dots, 8\}$, either $\pi_i(v) \in U$ or $\{v, \pi_i(v)\} \in E$ (so $\pi_i(v) \in B \subseteq T_0$); in either case $\pi_i(U) \subseteq T$.

For a fixed pair $(U, T_0)$, each $\pi_i(U)$ is a uniformly random $u$-element subset of $V_n$, so by independence of $\pi_1, \dots, \pi_8$,
$$\mathbb{P}\bigl(\forall\, i \in \{1, \dots, 8\},\ \pi_i(U) \subseteq T\bigr) = \left(\frac{\binom{t}{u}}{\binom{n}{u}}\right)^8.$$
Since $t < n$, for every $0 \le j \le u - 1$ we have $(t - j)n - t(n - j) = j(t - n) \le 0$, so $\frac{t - j}{n - j} \le \frac{t}{n}$, giving
$$\frac{\binom{t}{u}}{\binom{n}{u}} = \prod_{j=0}^{u-1} \frac{t - j}{n - j} \le \left(\frac{t}{n}\right)^u \le \left(\frac{9u}{8n}\right)^u.$$
By the union bound over all $\binom{n}{u}$ choices of $U$ and $\binom{n - u}{s}$ choices of $T_0$, the probability $p_u$ that some $u$-element set $U$ has $|\partial_G(U)| \le s$ satisfies
$$p_u \le \binom{n}{u}\binom{n - u}{s}\left(\frac{9u}{8n}\right)^{8u}.$$
Recall the elementary bound $\binom{n}{r} \le \frac{n^r}{r!} \le \left(\frac{en}{r}\right)^r$ for $1 \le r \le n$ (since $e^r = \sum_{j \ge 0} r^j/j! \ge r^r/r!$) and $e = \sum_{j \ge 0} 1/j! \le 1 + 1 + \sum_{j \ge 2} 2^{-(j-1)} = 3$. Furthermore, the function $x \mapsto (en/x)^x$ has derivative $(en/x)^x \ln(n/x) > 0$ on $(0, n)$, so it is strictly increasing on $(0, n)$. Since $s \le u/8 < n$, we have $\binom{n - u}{s} \le \binom{n}{s} \le \left(\frac{8en}{u}\right)^{u/8}$ (which holds trivially when $s = 0$ as well, since $\binom{n-u}{0} = 1 < (8en/u)^{u/8}$). Combining these with $\binom{n}{u} \le (en/u)^u$, $e < 3$, and $u/n \le 1/2$ gives
$$p_u \le \left(\frac{3n}{u}\right)^u \left(\frac{24 n}{u}\right)^{u/8} \left(\frac{9u}{8n}\right)^{8u} = \left[ 3 \cdot 24^{1/8} \cdot \left(\frac{9}{8}\right)^8 \cdot \left(\frac{u}{n}\right)^{55/8} \right]^u \le \left[ 3 \cdot 24^{1/8} \cdot \left(\frac{9}{8}\right)^8 \cdot 2^{-55/8} \right]^u.$$
Raising the bracketed base $B$ to the $8$th power yields
$$(2 B)^8 = \frac{3^8 \cdot 24 \cdot 9^{64} \cdot 2^8}{8^{64} \cdot 2^{55}} = \frac{157464 \cdot 9^{64} \cdot 2^8}{2^{247}} < 1,$$
because $9^{64} = 3^{128}$ satisfies $3^5 = 243 < 2^8 = 256$, so $3^{128} = 3^3 \cdot (3^5)^{25} < 27 \cdot 2^{200} < 2^{205}$, while $157464 \cdot 2^8 < 2^{18} \cdot 2^8 = 2^{26}$, giving numerator $< 2^{231} < 2^{247}$. Hence $B < 1/2$, so $p_u < 2^{-u}$ for every $1 \le u \le \lfloor n/2 \rfloor$. Summing over $u$:
$$\mathbb{P}\!\left(\exists\, U \subseteq V_n,\ 1 \le |U| \le \lfloor n/2 \rfloor,\ |\partial_G(U)| \le \lfloor |U|/8 \rfloor\right) \le \sum_{u=1}^{\lfloor n/2 \rfloor} p_u < \sum_{u=1}^{\infty} 2^{-u} = 1.$$
Therefore there exists a simple graph $G_n$ on $n$ vertices with $\Delta(G_n) \le 16$ such that every $U \subseteq V_n$ with $1 \le |U| \le \lfloor n/2 \rfloor$ satisfies $|\partial_{G_n}(U)| \ge \lfloor |U|/8 \rfloor + 1 > |U|/8$. In particular $|\partial_{G_n}(U)| \ge 1$ for all such $U$, so $G_n$ is connected, every vertex has degree at least $1$, and $|E_n| \ge n/2$. $\square$

*(Remark: If an explicit polynomial-time constructible family is preferred over the probabilistic Lemma 1, one may identically substitute any explicit constant-degree simple expander family, such as Gabber–Galil $8$-regular expanders or Lubotzky–Phillips–Sarnak $6$-regular Ramanujan expanders.)*

---

## 3. Exponential Resolution Lower Bound for $\widetilde{\operatorname{Ts}}(G_n, \alpha_n)$

### Lemma 2 (Restriction Lower Bound)
For any finite graph $G = (V, E)$ and charge $\alpha : V \to \mathbb{F}_2$ with $\sum_{v \in V} \alpha(v) = 1 \pmod 2$,
$$S_{\mathrm{Res}}\bigl(\widetilde{\operatorname{Ts}}(G, \alpha)\bigr) \;\ge\; S_{\mathrm{Res}}\bigl(\operatorname{Ts}(G, \alpha)\bigr).$$

*Proof.* Let $\Pi = (C_1, \dots, C_s = \square)$ be a Resolution refutation of $\widetilde{\operatorname{Ts}}(G, \alpha)$, and let $\rho$ be the partial restriction $\{g \mapsto 1\}$. For any clause $C$ not containing the literal $g$, write $C|_{\rho} := C \setminus \{\neg g\}$. We construct inductively, for each index $i \in \{1, \dots, s\}$ such that $g \notin C_i$, a subclause $C'_i \subseteq C_i|_{\rho}$ derived from $\operatorname{Ts}(G, \alpha)$ in at most one new Resolution step (using no clauses containing $g$ or $\neg g$):
- **Input ($C_i \in \widetilde{\operatorname{Ts}}(G, \alpha)$ with $g \notin C_i$):** Then $C_i = C \lor \neg g$ for some $C \in \operatorname{Ts}(G, \alpha)$, so $C'_i := C = C_i|_{\rho} \in \operatorname{Ts}(G, \alpha)$ ($1$ input step).
- **Resolution ($C_i = A \cup B$ from $C_{i_1} = A \cup \{x\}$ and $C_{i_2} = B \cup \{\neg x\}$, with $g \notin C_i$):**
  - *Case 1 ($x = g$):* Without loss of generality $g \in C_{i_1}$ and $\neg g \in C_{i_2}$, so $C_{i_2} = B \cup \{\neg g\}$. Since $g \notin C_i = A \cup B$, we have $g \notin C_{i_2}$, so $C'_{i_2} \subseteq C_{i_2}|_{\rho} = B \subseteq A \cup B = C_i|_{\rho}$ was already derived. Set $C'_i := C'_{i_2}$ ($0$ new steps).
  - *Case 2 ($x \neq g$):* Since $g \notin C_i = A \cup B$ and $x \neq g$, neither $C_{i_1}$ nor $C_{i_2}$ contains $g$, so $C'_{i_1} \subseteq A|_{\rho} \cup \{x\}$ and $C'_{i_2} \subseteq B|_{\rho} \cup \{\neg x\}$ were already derived. If $x \notin C'_{i_1}$, set $C'_i := C'_{i_1} \subseteq A|_{\rho} \subseteq C_i|_{\rho}$ ($0$ new steps). Else if $\neg x \notin C'_{i_2}$, set $C'_i := C'_{i_2} \subseteq B|_{\rho} \subseteq C_i|_{\rho}$ ($0$ new steps). Otherwise $x \in C'_{i_1}$ and $\neg x \in C'_{i_2}$; since $C_i = A \cup B$ is non-tautological, $(C'_{i_1} \setminus \{x\}) \cup (C'_{i_2} \setminus \{\neg x\}) \subseteq A|_{\rho} \cup B|_{\rho} = C_i|_{\rho}$ is non-tautological and is obtained by resolving $C'_{i_1}$ and $C'_{i_2}$ on pivot $x$ ($1$ new step).

At $i = s$, $g \notin C_s = \square$, so $C'_s \subseteq \square|_{\rho} = \square$, hence $C'_s = \square$. Every kept line adds at most one step, so we obtain a valid Resolution refutation of $\operatorname{Ts}(G, \alpha)$ of size at most $s$. $\square$

### Lemma 3 (Tseitin Resolution Width Lower Bound; Ben-Sasson–Wigderson)
Let $G = (V, E)$ be a connected graph on $n = |V| \ge 2$ vertices with edge expansion $e(G)$, and let $\alpha : V \to \mathbb{F}_2$ satisfy $\sum_{v \in V} \alpha(v) = 1 \pmod 2$. Then every Resolution refutation of $\operatorname{Ts}(G, \alpha)$ contains a clause of width at least $e(G) \cdot n / 3$, i.e.,
$$W_{\mathrm{Res}}\bigl(\operatorname{Ts}(G, \alpha) \vdash \square\bigr) \;\ge\; \frac{e(G)\, n}{3}.$$

*Proof.* First observe that for every proper subset $U \subsetneq V$, the subformula $\operatorname{Ts}(U, \alpha)$ is satisfiable: pick any vertex $v^* \in V \setminus U$, and for each $u \in U$ with $\alpha(u) = 1$, choose a path $P_u$ in the connected graph $G$ from $u$ to $v^*$. Taking the edge set $F := \bigtriangleup_{u \in U : \alpha(u) = 1} P_u \subseteq E$ and setting $x_e = \mathbf{1}_{e \in F}$ gives $\sum_{e \ni u} x_e = \deg_F(u) \equiv \alpha(u) \pmod 2$ for every $u \in U$ (since each $P_u$ contributes odd degree only at $u$ and $v^* \notin U$).

Now let $\Pi$ be any Resolution refutation of $\operatorname{Ts}(G, \alpha)$. For each clause $C \in \Pi$, define
$$\mu(C) := \min\bigl\{|U| : U \subseteq V,\ \operatorname{Ts}(U, \alpha) \models C\bigr\}.$$
1. Every input clause $C \in \operatorname{Ts}(v, \alpha)$ has $\mu(C) \le 1$ (taking $U = \{v\}$).
2. By satisfiability of $\operatorname{Ts}(U, \alpha)$ for all $U \subsetneq V$, we have $\mu(\square) = n$.
3. If $C$ is resolved from $C_1$ and $C_2$, then $\operatorname{Ts}(U_1, \alpha) \models C_1$ and $\operatorname{Ts}(U_2, \alpha) \models C_2$ imply $\operatorname{Ts}(U_1 \cup U_2, \alpha) \models C$, so $\mu(C) \le \mu(C_1) + \mu(C_2)$.

Since $\mu(C) \le 1$ on input clauses and $\mu(\square) = n > n/3$ (for all $n \ge 2$), consider the first clause $C^*$ in $\Pi$ with $\mu(C^*) > n/3$. If $C^*$ is an input clause (which happens only when $n = 2$, where $\mu(C^*) = 1$), then $\mu(C^*) = 1 \le 2n/3$; otherwise $C^*$ is resolved from earlier clauses $C_1, C_2$ with $\mu(C_1), \mu(C_2) \le n/3$, so $\mu(C^*) \le \mu(C_1) + \mu(C_2) \le 2n/3$. In all cases,
$$\frac{n}{3} < \mu(C^*) \le \frac{2n}{3}.$$
Let $U^* \subseteq V$ achieve $|U^*| = \mu(C^*)$. We claim that *every* edge $e = \{u, w\} \in \partial_G(U^*)$ (with $u \in U^*$, $w \in V \setminus U^*$) must appear in $C^*$. Suppose to the contrary that $e$ does not appear in $C^*$, and set $U' := U^* \setminus \{u\}$. Since $|U'| = |U^*| - 1 < \mu(C^*)$, there exists an assignment $\sigma : E \to \{0, 1\}$ satisfying $\operatorname{Ts}(U', \alpha)$ while falsifying $C^*$. If $\sigma$ satisfies the parity constraint at $u$, then $\sigma$ satisfies $\operatorname{Ts}(U^*, \alpha)$ and falsifies $C^*$, contradicting $\operatorname{Ts}(U^*, \alpha) \models C^*$. If $\sigma$ violates the parity constraint at $u$, define $\sigma'$ by flipping the single coordinate $x_e$ of $\sigma$:
- Neither endpoint $u, w$ of $e$ belongs to $U'$, so $\sigma'$ still satisfies $\operatorname{Ts}(U', \alpha)$;
- Since $e \ni u$, flipping $x_e$ flips the parity at $u$, so $\sigma'$ satisfies $\operatorname{Ts}(u, \alpha)$ as well, hence $\sigma'$ satisfies $\operatorname{Ts}(U^*, \alpha)$;
- Since $e$ does not appear in $C^*$, $\sigma'$ still falsifies $C^*$, again contradicting $\operatorname{Ts}(U^*, \alpha) \models C^*$.

Therefore $w(C^*) \ge |\partial_G(U^*)|$. Since $\partial_G(U^*) = \partial_G(V \setminus U^*)$ and $\min(|U^*|, n - |U^*|) \in [n/3, \lfloor n/2 \rfloor]$, we conclude
$$w(C^*) \ge |\partial_G(U^*)| \ge e(G) \cdot \min(|U^*|, n - |U^*|) \ge \frac{e(G)\, n}{3}. \qquad \square$$

### Lemma 4 (Size-Width Tradeoff; Ben-Sasson–Wigderson)
Let $\Phi$ be an unsatisfiable $k$-CNF ($k \ge 1$) on $N \ge 1$ variables, and let $W := W_{\mathrm{Res}}(\Phi \vdash \square)$. If $W \ge k + 1$, then
$$S_{\mathrm{Res}}(\Phi) \;\ge\; \exp\!\left(\frac{(W - k - 1)^2}{8 N}\right).$$

*Proof.* If $W = k + 1$, the right-hand side is $1 \le S_{\mathrm{Res}}(\Phi)$ trivially. Assume $W \ge k + 2$, and note $W \le N$ because every non-tautological clause on $N$ variables has width at most $N$.

Fix $N_0 := N$ and an integer $d$ with $k \le d \le N_0 - 1$, and set $a := \left(1 - \frac{d}{2 N_0}\right)^{-1} > 1$ (well-defined since $\frac{d}{2 N_0} < \frac{1}{2}$). Call a clause *fat* if its width is strictly greater than $d$. We prove by induction on $m + r$ that for every $m \in \{0, 1, \dots, N_0\}$, every integer $r \ge 0$, every unsatisfiable $k$-CNF $\Psi$ on at most $m$ variables, and every Resolution refutation $\Pi$ of $\Psi$ containing $b$ fat clauses:
$$b < a^r \implies W_{\mathrm{Res}}(\Psi \vdash \square) \le d + r.$$
- *Base cases:* If $r = 0$, then $b < 1 \implies b = 0$, so $\Pi$ itself has width $\le d = d + 0$. If $m = 0$, then $\square \in \Psi$ and $W_{\mathrm{Res}}(\Psi \vdash \square) = 0 \le d + r$.
- *Inductive step ($m \ge 1$, $r \ge 1$):* If $b = 0$, then $W_{\mathrm{Res}}(\Psi \vdash \square) \le d \le d + r$. Assume $b \ge 1$. Each of the $b$ fat clauses contains at least $d + 1 > d$ literals chosen from the $2m \le 2 N_0$ literals over the variables of $\Psi$. By averaging, some literal $\ell$ occurs in strictly more than $\frac{d}{2m} b \ge \frac{d}{2 N_0} b$ fat clauses of $\Pi$.
  1. Restricting $\Pi$ by $\rho_1 = \{\ell \mapsto 1\}$ (via the proof of Lemma 2, where every kept clause is a subclause of a kept clause of $\Pi|_{\rho_1}$) produces a Resolution refutation $\Pi_1$ of the unsatisfiable $k$-CNF $\Psi|_{\rho_1}$ on at most $m - 1$ variables. Every fat clause of $\Pi_1$ arises from a fat clause of $\Pi$ not containing $\ell$, so the number $b_1$ of fat clauses in $\Pi_1$ satisfies
     $$b_1 < b - \frac{d}{2 N_0} b = a^{-1} b < a^{r - 1}.$$
     By the induction hypothesis on $(m - 1, r - 1)$, $\Psi|_{\rho_1}$ admits a Resolution refutation $\Sigma_1$ of width $\le d + r - 1$. Restoring $\neg \ell$ where needed: inductively, for each clause $C$ in $\Sigma_1$, we derive from $\Psi$ either $C$ or $C \lor \neg \ell$ (for an input $C \in \Psi|_{\rho_1}$, either $C \in \Psi$ or $C \lor \neg \ell \in \Psi$, both of width $\le k \le d < d + r$; for a resolution step on pivot $x \neq \mathrm{var}(\ell)$, resolving the corresponding lifted parents on $x$ yields either $C$ or $C \lor \neg \ell$ of width $\le w(C) + 1 \le d + r$). At the final line $C = \square$ of $\Sigma_1$, we have derived from $\Psi$ in width $\le d + r$ either $\square$ (done!) or the unit clause $\neg \ell$.
  2. Restricting $\Pi$ by $\rho_0 = \{\ell \mapsto 0\}$ similarly produces a Resolution refutation $\Pi_0$ of the unsatisfiable $k$-CNF $\Psi|_{\rho_0}$ on at most $m - 1$ variables with $b_0 \le b < a^r$ fat clauses. By the induction hypothesis on $(m - 1, r)$, $\Psi|_{\rho_0}$ admits a Resolution refutation $\Sigma_0$ of width $\le d + r$.
  3. To convert $\Sigma_0$ into a refutation of $\Psi$: whenever $\Sigma_0$ uses an input clause $C \in \Psi|_{\rho_0}$ that is not itself in $\Psi$, we have $C \lor \ell \in \Psi$ (width $\le k \le d + r$), and resolving $C \lor \ell$ with the already-derived unit clause $\neg \ell$ on pivot $\ell$ yields $C$ (width $\le k - 1 < d + r$). Appending $\Sigma_0$ gives a Resolution refutation of $\Psi$ of width $\le d + r$.

This completes the induction. Now apply the claim to $\Phi$ with $d := k + \lfloor (W - k - 1)/2 \rfloor$ and $r := \lceil (W - k - 1)/2 \rceil$. Since $W \ge k + 2$ and $W \le N$, we have $d \ge k$, $r \ge 1$, $d + r = W - 1 < W$, and $d = W - 1 - r \le N - 2 < N$. Because $W_{\mathrm{Res}}(\Phi \vdash \square) = W > d + r$, the contrapositive forces every Resolution refutation $\Pi$ of $\Phi$ of size $S$ to satisfy
$$S \ge b \ge a^r = \left(1 - \frac{d}{2N}\right)^{-r} \ge \exp\!\left(\frac{d r}{2N}\right),$$
using $1 - x \le e^{-x} \implies (1 - x)^{-1} \ge e^x$ for $x = \frac{d}{2N} \in (0, 1/2)$. Finally, since $k \ge 1$ implies $d \ge k + \frac{W - k - 2}{2} = \frac{W + k - 2}{2} \ge \frac{W - k - 1}{2}$ and $r \ge \frac{W - k - 1}{2}$, we obtain $dr \ge \frac{(W - k - 1)^2}{4}$ and hence $S_{\mathrm{Res}}(\Phi) \ge \exp\!\left(\frac{(W - k - 1)^2}{8N}\right)$. $\square$

---

## 4. Quadratic $1\text{-SRC-II}$ Upper Bound on Guarded Tseitin Formulas

### Theorem 5 (Universal Guarded Tseitin Refutation in $1\text{-SRC-II}$)
Let $G = (V, E)$ be any finite connected graph on $n = |V| \ge 2$ vertices and $m = |E|$ edges with maximum degree $\Delta := \Delta(G)$, and let $\alpha : V \to \mathbb{F}_2$ satisfy $\sum_{v \in V} \alpha(v) = 1 \pmod 2$. Then
$$S_{1\text{-SRC-II}}\bigl(\widetilde{\operatorname{Ts}}(G, \alpha)\bigr) \;\le\; \sum_{v \in V} 3 \cdot 2^{\deg(v) - 1} + (n - 1)\bigl(2^{\Delta - 1}(m + 4) - 1\bigr) + 2^\Delta \;=\; O(2^\Delta n m).$$

*Proof.* Set $\Phi := \widetilde{\operatorname{Ts}}(G, \alpha)$, and for any $U \subseteq V$ denote $\mathcal{L}_0(U) := \{C \lor \neg g : C \in \operatorname{Ts}(U, \alpha)\} \subseteq \Phi$, $\mathcal{L}_1(U) := \{D \lor g : D \in \operatorname{All}(U)\} \subseteq \Phi$, and $\alpha(U) := \sum_{u \in U} \alpha(u) \bmod 2 \in \{0, 1\}$.

**Phase 0 (Input lines).** List all clauses of $\Phi$ as the initial lines of the proof. This uses at most $\sum_{v \in V} (2^{\deg(v)-1} + 2^{\deg(v)}) = \sum_{v \in V} 3 \cdot 2^{\deg(v)-1}$ steps (with equality for $n \ge 3$), and ensures that every clause of $\Phi$ is already derived in the proof before any symmetry step is applied.

**Local Sign-Flip Simulation Subroutine.** Suppose we have derived a clause $A \lor \neg g$ with premise set $\mathcal{B} \subseteq \mathcal{L}_0(U)$ for some $U \subseteq V$, and let $F = \{f_1, \dots, f_s\} \subseteq E$ be any set of edges ($s \le m$) such that **every vertex $u \in U$ has even degree in $F$**, i.e., $|F \cap \partial(u)| \equiv 0 \pmod 2$. Writing $\phi_F := \phi_{f_s} \circ \dots \circ \phi_{f_1}$, we derive $\phi_F(A) \lor \neg g$ with premise set $\phi_F(\mathcal{B}) \subseteq \mathcal{L}_0(U)$ in at most $s + 2 \le m + 2$ local $1$-symmetry steps (or $0$ steps if $F = \emptyset$):
1. Apply $\phi_g$ to $\mathcal{B} \vdash A \lor \neg g$. Every clause in $\mathcal{B}$ has the form $C \lor \neg g$ with $C \in \operatorname{Ts}(U, \alpha) \subseteq \operatorname{All}(U)$, so $\phi_g(C \lor \neg g) = C \lor g \in \mathcal{L}_1(U) \subseteq \Phi$. Thus $\mathcal{B} \subseteq \Phi$ and $\phi_g(\mathcal{B}) \subseteq \Phi$ (all already present from Phase 0), yielding $\mathcal{B}^{(0)} \vdash A \lor g$ where $\mathcal{B}^{(0)} := \phi_g(\mathcal{B}) \subseteq \mathcal{L}_1(U)$.
2. For $j = 1, \dots, s$, apply $\phi_{f_j}$ to $\mathcal{B}^{(j-1)} \vdash \phi_{f_{j-1}} \cdots \phi_{f_1}(A) \lor g$. For every vertex $u \in U$, flipping any single edge variable $f_j$ maps the set of all $2^{\deg(u)}$ full clauses $\operatorname{All}(u)$ bijectively onto itself, hence maps $\mathcal{L}_1(U)$ onto $\mathcal{L}_1(U) \subseteq \Phi$. By induction, $\mathcal{B}^{(j-1)} \subseteq \mathcal{L}_1(U) \subseteq \Phi$ and $\mathcal{B}^{(j)} := \phi_{f_j}(\mathcal{B}^{(j-1)}) \subseteq \mathcal{L}_1(U) \subseteq \Phi$, so every step is a valid $1\text{-SRC-II}$ rule application. After $j = s$, we obtain $\mathcal{B}^{(s)} \vdash \phi_F(A) \lor g$, where $\mathcal{B}^{(s)} = \{\phi_F(C) \lor g : C \lor \neg g \in \mathcal{B}\}$.
3. Apply $\phi_g$ to $\mathcal{B}^{(s)} \vdash \phi_F(A) \lor g$. Every clause in $\phi_g(\mathcal{B}^{(s)})$ has the form $\phi_F(C) \lor \neg g$ for some $C \in \operatorname{Ts}(u, \alpha)$ with $u \in U$. Because $|F \cap \partial(u)|$ is even, flipping all variables in $F$ flips an even number of literals of $C$, preserving the parity of the forbidden assignment on $\partial(u)$. Hence $\phi_F(C) \in \operatorname{Ts}(u, \alpha)$, so $\phi_g(\mathcal{B}^{(s)}) = \phi_F(\mathcal{B}) \subseteq \mathcal{L}_0(U) \subseteq \Phi$. This valid $1\text{-SRC-II}$ step derives
   $$\phi_F(\mathcal{B}) \;\vdash\; \phi_F(A) \lor \neg g.$$

**Phase 1 (Spanning-tree induction).** Since $G$ is connected, fix a spanning tree $T$ of $G$ rooted at a vertex $v_1$, and order the vertices $v_1, v_2, \dots, v_n$ (e.g., by BFS from $v_1$) so that for every $t \in \{1, \dots, n\}$, the induced subgraph $T[U_t]$ on $U_t := \{v_1, \dots, v_t\}$ is connected (a tree).

We inductively derive, for each $t = 1, \dots, n$, a *basic cut clause* $B_t \lor \neg g$ with premise set $\mathcal{B}_t \subseteq \mathcal{L}_0(U_t)$, where:
- For $1 \le t \le n - 1$, $B_t = C(\sigma_t)$ for a chosen assignment $\sigma_t : \partial_G(U_t) \to \{0, 1\}$ satisfying $\sum_{e \in \partial_G(U_t)} \sigma_t(e) \not\equiv \alpha(U_t) \pmod 2$ (note $\partial_G(U_t) \neq \emptyset$ because $G$ is connected and $\emptyset \subsetneq U_t \subsetneq V$, so such $\sigma_t$ always exists).
- For $t = n$, $U_n = V$, $\partial_G(V) = \emptyset$, $\alpha(V) = 1$, and $B_n = C(\emptyset) = \square$, so $B_n \lor \neg g = \neg g$.

*Base $t = 1$:* $U_1 = \{v_1\}$, $\partial_G(U_1) = \partial(v_1)$, and $C(\sigma_1) \lor \neg g \in \mathcal{L}_0(v_1)$ is already an input line from Phase 0 ($0$ new steps).

*Inductive step $t - 1 \to t$ ($2 \le t \le n$):* We have derived $C(\sigma_{t-1}) \lor \neg g$ from $\mathcal{B}_{t-1} \subseteq \mathcal{L}_0(U_{t-1})$. Partition the incident edges of $v_t$ into
$$E_t := \partial(v_t) \cap \partial_G(U_{t-1}) \qquad \text{and} \qquad E'_t := \partial(v_t) \setminus E_t.$$
Because $T[U_t]$ is connected, $v_t$ has at least one neighbor in $U_{t-1}$, so $1 \le r_t := |E_t| \le \deg(v_t) \le \Delta$. Moreover, the new cut is the disjoint union $\partial_G(U_t) = (\partial_G(U_{t-1}) \setminus E_t) \sqcup E'_t$. Fix a forbidden assignment $\sigma_t = (\sigma_{t,1}, \sigma_{t,2})$ on $\partial_G(U_t)$ (with $\sigma_{t,1}$ on $\partial_G(U_{t-1}) \setminus E_t$ and $\sigma_{t,2}$ on $E'_t$; when $t = n$, both are empty) satisfying
$$\sum_{e \in \partial_G(U_{t-1}) \setminus E_t} \sigma_{t,1}(e) + \sum_{e \in E'_t} \sigma_{t,2}(e) \;\not\equiv\; \alpha(U_t) = \alpha(U_{t-1}) + \alpha(v_t) \pmod 2.$$
For each of the $2^{r_t}$ assignments $\tau : E_t \to \{0, 1\}$, consider the parity of $\tilde{\tau} := (\sigma_{t,1}, \tau)$ on $\partial_G(U_{t-1})$:

- **Case A ($\sum_{e \in \partial_G(U_{t-1})} \tilde{\tau}(e) \not\equiv \alpha(U_{t-1}) \pmod 2$):** This occurs for exactly $2^{r_t - 1}$ choices of $\tau$. Since both $\tilde{\tau}$ and $\sigma_{t-1}$ have parity distinct from $\alpha(U_{t-1})$, their difference set $S := \{e \in \partial_G(U_{t-1}) : \tilde{\tau}(e) \neq \sigma_{t-1}(e)\} \subseteq \partial_G(U_{t-1})$ has even cardinality. Let $W \subseteq U_{t-1}$ be the set of vertices $u \in U_{t-1}$ incident to an odd number of edges of $S$. Because every edge in $S \subseteq \partial_G(U_{t-1})$ has exactly one endpoint in $U_{t-1}$, we have $\sum_{u \in U_{t-1}} |S \cap \partial(u)| = |S| \equiv 0 \pmod 2$, so $|W|$ is even. Partition $W$ arbitrarily into $|W|/2$ disjoint pairs $(a_1, b_1), \dots, (a_q, b_q)$; for each $i$, let $P_i \subseteq E(T[U_{t-1}])$ be the unique path between $a_i$ and $b_i$ in the tree $T[U_{t-1}]$, and set
  $$F_1 := P_1 \triangle P_2 \triangle \dots \triangle P_q \subseteq E(T[U_{t-1}]), \qquad F := S \cup F_1.$$
  Notice $S \cap F_1 = \emptyset$ (edges of $F_1$ have both endpoints in $U_{t-1}$, while edges of $S$ cross $\partial_G(U_{t-1})$). For every $u \in U_{t-1}$, $u$ has odd degree in $F_1$ if and only if $u \in W$, which is if and only if $u$ has odd degree in $S$; hence $|F \cap \partial(u)| = |S \cap \partial(u)| + |F_1 \cap \partial(u)| \equiv 0 \pmod 2$. Moreover, $F \cap \partial_G(U_{t-1}) = S$, so $\phi_F(C(\sigma_{t-1})) = C(\tilde{\tau})$. Running the Local Sign-Flip Simulation Subroutine with $F$ derives
  $$C(\sigma_{t,1}) \lor C(\tau) \lor \neg g$$
  with premise set $\subseteq \mathcal{L}_0(U_{t-1})$ in at most $m + 2$ steps.
- **Case B ($\sum_{e \in \partial_G(U_{t-1})} \tilde{\tau}(e) \equiv \alpha(U_{t-1}) \pmod 2$):** Subtracting this congruence from the forbidden-parity relation for $\sigma_t$ yields
  $$\sum_{e \in E_t} \tau(e) + \sum_{e \in E'_t} \sigma_{t,2}(e) \;\not\equiv\; \alpha(v_t) \pmod 2.$$
  Hence $C(\tau) \lor C(\sigma_{t,2}) \lor \neg g \in \mathcal{L}_0(v_t) \subseteq \Phi$ is already an input clause from Phase 0 ($0$ new steps).

Write $E_t = \{e_1, \dots, e_{r_t}\}$, and resolve the $2^{r_t}$ clauses obtained above in a complete binary resolution tree of depth $r_t$ on pivots $e_1, e_2, \dots, e_{r_t}$ in order:
- At level $1$ (pivot $e_1$): for each $\tau' \in \{0, 1\}^{r_t - 1}$ on $\{e_2, \dots, e_{r_t}\}$, the two extensions $(0, \tau')$ and $(1, \tau')$ have opposite parities on $E_t$, so exactly one lies in Case A (giving $C(\sigma_{t,1}) \lor C(\tau') \lor \ell_1 \lor \neg g$) and the other lies in Case B (giving $C(\sigma_{t,2}) \lor C(\tau') \lor \neg \ell_1 \lor \neg g$). Because $\partial_G(U_{t-1}) \setminus E_t$, $E'_t$, $\{e_2, \dots, e_{r_t}\}$, $\{e_1\}$, and $\{g\}$ are pairwise disjoint, resolving them on $e_1$ is non-tautological and yields **exactly** $C(\sigma_{t,1}) \lor C(\sigma_{t,2}) \lor C(\tau') \lor \neg g = C(\sigma_t) \lor C(\tau') \lor \neg g$.
- At levels $j = 2, \dots, r_t$ (pivot $e_j$): each pair of sibling clauses has identical side literals $C(\sigma_t) \lor C(\tau'') \lor \neg g$ together with $e_j$ and $\neg e_j$, so resolving eliminates $e_j$.

After $2^{r_t} - 1$ Resolution steps, we obtain $C(\sigma_t) \lor \neg g$ with premise set $\mathcal{B}_t \subseteq \mathcal{L}_0(U_{t-1}) \cup \mathcal{L}_0(v_t) = \mathcal{L}_0(U_t)$. The total number of new steps in inductive step $t$ is at most
$$2^{r_t - 1}(m + 2) + (2^{r_t} - 1) = 2^{r_t - 1}(m + 4) - 1 \le 2^{\Delta - 1}(m + 4) - 1.$$

At $t = n$, Phase 1 concludes with the unit clause $\neg g$.

**Phase 2 (Deriving $g$ and $\square$).** Pick vertex $v_1$ (degree $d_1 \le \Delta$). Its $2^{d_1}$ clauses $\{D \lor g : D \in \operatorname{All}(v_1)\} \subseteq \Phi$ (already present from Phase 0) cover all $2^{d_1}$ truth assignments to $\partial(v_1)$. Resolving them in a complete binary tree on the $d_1$ incident edges of $v_1$ derives the unit clause $g$ in $2^{d_1} - 1 \le 2^\Delta - 1$ Resolution steps. Finally, resolve $g$ with $\neg g$ on pivot $g$ ($1$ step) to obtain $\square$.

Summing Phases 0, 1, and 2 gives total step count at most
$$\sum_{v \in V} 3 \cdot 2^{\deg(v) - 1} + (n - 1)\bigl(2^{\Delta - 1}(m + 4) - 1\bigr) + 2^\Delta = O(2^\Delta n m). \qquad \square$$

---

## 5. Proof of the Main Theorem and Bounded-Depth Frege Corollary

*Proof of Main Theorem.* For each integer $n \ge 2$, let $G_n = (V_n, E_n)$ be a connected simple graph from Lemma 1 ($\Delta(G_n) \le 16$, $n/2 \le m_n := |E_n| \le 8n$, and $e(G_n) > 1/8$). Fix a vertex $v_1 \in V_n$ and define $\alpha_n(v_1) := 1$ and $\alpha_n(v) := 0$ for all $v \in V_n \setminus \{v_1\}$, so $\sum_{v \in V_n} \alpha_n(v) = 1 \pmod 2$. Set
$$\Phi_n := \widetilde{\operatorname{Ts}}(G_n, \alpha_n).$$
Then $\Phi_n$ has $N_n = m_n + 1 \in [n/2 + 1,\, 8n + 1]$ variables ($\Theta(n)$), at most $3 \cdot 2^{15} n = \Theta(n)$ clauses, and clause width at most $17$.

- **Upper bound in $1\text{-SRC-II}$:** By Theorem 5 (with $\Delta \le 16$ and $m_n \le 8n$),
  $$S_{1\text{-SRC-II}}(\Phi_n) \le 3 \cdot 2^{15} n + (n - 1)\bigl(2^{15}(8n + 4) - 1\bigr) + 2^{16} = O(n^2) = O(N_n^2).$$
- **Lower bound in $\mathrm{Res}$:** By Lemma 3, $W_n := W_{\mathrm{Res}}(\operatorname{Ts}(G_n, \alpha_n) \vdash \square) \ge e(G_n) \cdot n/3 > n/24$. Since $\operatorname{Ts}(G_n, \alpha_n)$ is a $16$-CNF on $m_n \le 8n$ variables, for all $n \ge 816$ we have $W_n - 17 > n/24 - 17 \ge n/48 > 0$, so Lemmas 2 and 4 yield
  $$S_{\mathrm{Res}}(\Phi_n) \ge S_{\mathrm{Res}}\bigl(\operatorname{Ts}(G_n, \alpha_n)\bigr) \ge \exp\!\left(\frac{(n/48)^2}{8 \cdot 8n}\right) = \exp\!\left(\frac{n}{147456}\right) = 2^{\Omega(n)} = 2^{\Omega(N_n)}.$$

Therefore $1\text{-SRC-II}$ is exponentially separated from $\mathrm{Res}$ in the sense of Gaevoy Definition 9. $\square$

### Corollary (Exponential Separation of $1\text{-SRC-II}$ from Bounded-Depth Frege)
For odd $n \ge 3$, let $T_n = \operatorname{Ts}(H_n, \mathbf{1})$ be Gaevoy's Tseitin contradiction on the $n \times n$ toroidal rectangular grid $H_n$ ($\Delta = 4$, $|V| = n^2$, $|E| = 2n^2$; Gaevoy Section 4.1), and let $\widetilde{T}_n := \widetilde{\operatorname{Ts}}(H_n, \mathbf{1})$ ($N = 2n^2 + 1$ variables, $24n^2$ clauses of width $5$). Then:
1. $S_{1\text{-SRC-II}}(\widetilde{T}_n) = O(n^4)$ directly by Theorem 5 (and in fact $O(n^2)$ by simulating every $4$-symmetry in Gaevoy's $O(n^2)$ $4\text{-SRC-I}$ proof of $T_n$, Corollary 24, via $6$ local $1$-symmetry steps $\phi_g \to \phi_{e_1} \to \phi_{e_2} \to \phi_{e_3} \to \phi_{e_4} \to \phi_g$).
2. Since restricting $g \mapsto 1$ reduces $\widetilde{T}_n$ to $T_n$ and transforms any depth-$d$ Frege refutation of $\widetilde{T}_n$ into a depth-$d$ Frege refutation of $T_n$ without increasing size, Håstad's lower bound (Gaevoy Theorem 22, citing Håstad 2020) gives, for all sufficiently large odd $n$ and $d \le \frac{\log n}{59 \log \log n}$,
   $$S_{\text{depth-$d$ Frege}}(\widetilde{T}_n) \ge S_{\text{depth-$d$ Frege}}(T_n) = \exp\!\left(\Omega\!\left(n^{\frac{1}{58(d + 1)}}\right)\right).$$

---

## 6. Exact Computational Verification

The standalone exact-arithmetic (zero-float) script [`verify.py`](file:///Users/kolinhuang/Documents/open-math/targets/gaevoy-2606.25895-src2-1/verify.py) independently checks:

1. **Lemma 1 exact arithmetic:** Verifies the exact integer inequality $157464 \cdot 9^{64} \cdot 2^8 < 2^{247}$ and the exact rational union bound $\sum_{u=1}^{\lfloor n/2 \rfloor} \binom{n}{u}\binom{n-u}{\lfloor u/8 \rfloor} \bigl(\binom{u + \lfloor u/8 \rfloor}{u}/\binom{n}{u}\bigr)^8 < 1$ for all $2 \le n \le 30$.
2. **Theorem 5 strict $1\text{-SRC-II}$ proof verification:** Explicitly builds $\widetilde{\operatorname{Ts}}(G, \alpha)$ and its $1\text{-SRC-II}$ refutation on six diverse connected graphs — $K_4$ ($n=4$, $3$-regular), $K_{3,3}$ ($n=6$, $3$-regular), an irregular graph ($n=7$, degrees $2$ and $3$), the $3 \times 3$ toroidal grid $H_3$ ($n=9$, $4$-regular), the Petersen graph ($n=10$, $3$-regular), and the Möbius ladder $M_{20}$ ($n=20$, $3$-regular) — and checks every single input, resolution, and local $1$-symmetry step against a strict Cook-Reckhow verifier (checking $|\operatorname{supp}(\phi)| \le 1$, $L(j) \subseteq \Phi$, $\phi(L(j)) \subseteq \Phi$, prior derivation of all premises in $\phi(L(j))$, non-tautological resolution, final clause $\square$, and the exact step bound of Theorem 5).
3. **Full recursive unfolding & Lemma 2 restriction check:** On $K_4$ and $K_{3,3}$, recursively unfolds the entire $1\text{-SRC-II}$ refutation of $\widetilde{\operatorname{Ts}}(G, \alpha)$ into a pure Resolution refutation of $\widetilde{\operatorname{Ts}}(G, \alpha)$, verifies it with a standalone pure Resolution checker, then runs the Lemma 2 restriction algorithm ($\rho = \{g \mapsto 1\}$) and verifies the output is a valid pure Resolution refutation of $\operatorname{Ts}(G, \alpha)$ of smaller size.
4. **Lemma 3 exact expansion check:** Exhaustively computes exact `Fraction` edge expansion $e(G)$ on $K_4$ ($e = 2$), $K_{3,3}$ ($e = 5/3$), and the Petersen graph ($e = 1$).

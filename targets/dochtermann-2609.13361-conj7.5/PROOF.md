# Proof of Dochtermann–Huang–Mawhinney–Oh–Xu's Conjecture 7.5 (`arXiv:2609.13361v1`)

## 1. Statement and Main Result

**Primary source.** Anton Dochtermann, Evan Huang, Kai Mawhinney, Suho Oh, and Yuchen Xu, *Matroids with cycle systems are regular*, `arXiv:2609.13361v1` (2026-09-11; cached source `tools/.arxiv_cache/eprint/2609.13361/cyclesystem_reg.tex`), Section 7 (*Further questions*), **Conjecture 7.5** (`\label{conj:C>=3 ind}`, lines 1063–1065; also stated in Section 1, lines 221–224).

> **Conjecture 7.5 (`conj:C>=3 ind`).** *Let $M$ be a matroid with circuit system $\mathcal{C}$, where $\mathcal{C}_{[g]}$ is a circuit. Then $\mathcal{C}_{\ge 3}$ is independent.*

We prove a strictly stronger result: under these hypotheses, **no element can appear in three or more circuits of $\mathcal{C}$ at all**.

> **Main Theorem.** *Let $M$ be a matroid of corank $g := |E(M)| - r(M)$ with circuit system $\mathcal{C} = \{C_1, \dots, C_g\}$ such that $\mathcal{C}_{[g]}$ is a circuit of $M$. Then*
> $$\mathcal{C}_{\ge 3} = \emptyset.$$
> *In particular, $\mathcal{C}_{\ge 3}$ is independent in $M$, establishing Conjecture 7.5 (`conj:C>=3 ind`).*

As immediate corollaries, we also resolve **Conjecture 7.4** (`\label{conj:unique}`, lines 1057–1059) of `arXiv:2609.13361v1` and obtain a complete structural characterization of circuit systems with circuit total unique union:

> **Corollary 1 (Resolution of Conjecture 7.4 `conj:unique`).** *Let $M$ be a matroid with circuit system $\mathcal{C} = \{C_1, \dots, C_g\}$, and let $D \in \mathrm{Cir}(M)$ be a circuit of $M$. Then there exists a unique subset $S \subseteq [g]$ such that $\mathcal{C}_S = D$.*

> **Corollary 2 (Cographic Characterization).** *Let $M$ be a connected matroid of corank $g \ge 1$. Then $M$ admits a circuit system $\mathcal{C} = \{C_1, \dots, C_g\}$ whose total unique union $D = \mathcal{C}_{[g]}$ is a circuit if and only if $M$ is cographic; moreover, for every such circuit system $\mathcal{C}$, there exist a connected loopless graph $G$ on $g + 1$ vertices with edge set $E(M)$ satisfying $M = M(G)^*$ and a sink vertex $q \in V(G)$ such that $\mathcal{C} = \{\delta_G(v) : v \in V(G) \setminus \{q\}\}$ and $\delta_G(q) = D$.*

---

## 2. Preliminaries and Cited Results

We follow the exact definitions and compiled numbering of `arXiv:2609.13361v1` (`cyclesystem_reg.tex`):

- **Unique union (Definition 2.13, `def:uniqueunion`):** For subsets $A_1, \dots, A_k \subseteq E$ and $S \subseteq [k]$, $\mathcal{A}_S := *\{A_i : i \in S\}$ is the set of elements of $E$ appearing in **exactly one** $A_i$ for $i \in S$.
- **Cycle system and circuit system (Definition 2.14, lines 459–479):** For a matroid $M$ of corank $g = |E(M)| - r(M)$, a *cycle system* is a collection $\mathcal{C} = \{C_1, \dots, C_g\}$ of $g$ cycles (unions of circuits) such that $\mathcal{C}_S \notin \mathcal{I}(M)$ for every nonempty $S \subseteq [g]$. It is a *circuit system* if every $C_i$ is a circuit of $M$.
- **Multiplicity and $\mathcal{C}_{\ge 3}$ (Definition 6.6, lines 994–996):** For any $e \in E(M)$, write $\mathrm{mult}_{\mathcal{C}}(e) := |\{i \in [g] : e \in C_i\}|$. Then $\mathcal{C}_{[g]} = \{e \in E(M) : \mathrm{mult}_{\mathcal{C}}(e) = 1\}$ and $\mathcal{C}_{\ge 3} := \{e \in E(M) : \mathrm{mult}_{\mathcal{C}}(e) \ge 3\}$.
- **Symmetric difference and circuit space (Section 4.1, line 716):** For a binary matroid $N$ on ground set $E$, its *circuit space* $\mathcal{Z}(N) \subseteq \mathbb{F}_2^E$ is the $\mathbb{F}_2$-linear span of the indicator vectors of $\mathrm{Cir}(N)$, where addition corresponds to symmetric difference $\triangle$. Every element of $\mathcal{Z}(N)$ is a disjoint union of circuits of $N$, so every nonempty element of $\mathcal{Z}(N)$ is dependent in $N$. Furthermore, if $H$ is an $r(N) \times |E|$ full-row-rank $\mathbb{F}_2$-representation of $N$, every circuit indicator vector lies in $\ker_{\mathbb{F}_2}(H)$, whence $\mathcal{Z}(N) \subseteq \ker_{\mathbb{F}_2}(H)$ and
  $$\dim_{\mathbb{F}_2} \mathcal{Z}(N) \le |E| - r(N) = g(N).$$

We invoke the following results established in `arXiv:2609.13361v1` (and its precursor Corry–Dochtermann–McClain–Perkinson–Yi, `arXiv:2509.11460v1`):

1. **Proposition 2.19 (`prop:del-con cs`, citing `2509.11460v1` Proposition 3.6):** Let $M$ be a matroid with cycle system $\mathcal{C} = \{C_1, \dots, C_g\}$.
   - *(1) $*$-deletion:* If $e \in \mathcal{C}_{[g]} \cap C_i$, then $\mathcal{C} \setminus \{C_i\}$ is a cycle system for $M \setminus e$.
   - *(2) Contraction:* If $e \in E(M)$ is a non-loop of $M$, then $\{C_1 \setminus \{e\}, \dots, C_g \setminus \{e\}\}$ is a cycle system for $M / e$.
2. **Lemma 2.21 (`lem:circuitsys`, citing `2509.11460v1` Theorem 3.10):** If $M$ is a connected matroid with cycle system $\mathcal{C}$, then $\mathcal{C}$ is a circuit system.
3. **Theorem 2.22 (`thm:components`, citing `2509.11460v1` Theorem 3.13):** Let $W = \bigoplus_{j=1}^k W_j$ be the direct-sum decomposition of a matroid $W$ into connected components, and let $\mathcal{E}$ be a cycle system for $W$. Up to reordering the components $W_1, \dots, W_k$, there exist cycle systems $\mathcal{C}^{(j)}$ for $W_j$ ($1 \le j \le k$) such that $\mathcal{E} = \bigsqcup_{j=1}^k \widetilde{\mathcal{C}^{(j)}}$, where
   $$\widetilde{\mathcal{C}^{(j)}} = \left\{C \cup K_C \;\middle|\; C \in \mathcal{C}^{(j)},\; K_C \subseteq \bigsqcup_{t=1}^{j-1} E(W_t)\right\}.$$
   In particular, $\widetilde{\mathcal{C}^{(1)}} = \mathcal{C}^{(1)}$.
4. **Theorem 4.3 (`thm:cycle system binary`):** Every matroid admitting a cycle system is binary.
5. *(Used only for Corollary 1)* **Lemma 6.4 (`lem:reachable to D`)** and **Proposition 6.7 (`prop:C>=3`)**: For any matroid $M$ with cycle system $\mathcal{C}$ and any circuit $D \in \mathrm{Cir}(M)$, there is a unique subsystem $\mathcal{C}^D \subseteq \mathcal{C}$ reachable from $\mathcal{C}$ by a finite sequence of $*$-deletions whose total unique union is $D$; if $(\mathcal{C}^D)_{\ge 3}$ is independent in the resulting minor, then $|\{S \subseteq [g] : \mathcal{C}_S = D\}| = 1$.

---

## 3. Auxiliary Lemmas

**Lemma 1 (Linear independence of cycle systems and circuit-system bases).** *Let $N$ be a matroid of corank $g$ with cycle system $\mathcal{E} = \{E_1, \dots, E_g\}$.*
1. *The indicator vectors of $E_1, \dots, E_g$ are linearly independent in $\mathbb{F}_2^{E(N)}$.*
2. *If $N$ is binary and $\mathcal{E}$ is a circuit system, then the indicator vectors of $E_1, \dots, E_g$ lie in $\mathcal{Z}(N)$ and form an $\mathbb{F}_2$-basis of $\mathcal{Z}(N)$.*

*Proof.*
(1) Suppose for contradiction that $\triangle_{i \in S} E_i = \emptyset$ for some nonempty subset $S \subseteq [g]$. Then every element $e \in E(N)$ belongs to an even number of the sets $\{E_i : i \in S\}$, so no element belongs to exactly one of them. Hence $\mathcal{E}_S = \emptyset \in \mathcal{I}(N)$, contradicting that $\mathcal{E}$ is a cycle system.

(2) When $\mathcal{E}$ is a circuit system on a binary matroid $N$, each $E_i \in \mathrm{Cir}(N)$ belongs to $\mathcal{Z}(N)$. By (1), $E_1, \dots, E_g$ are $g$ linearly independent vectors in $\mathcal{Z}(N)$, and since $\dim_{\mathbb{F}_2} \mathcal{Z}(N) \le g(N) = g$, they form an $\mathbb{F}_2$-basis of $\mathcal{Z}(N)$. $\blacksquare$

**Lemma 2 (Rank criterion for connectedness and basic contraction facts).** *Let $M$ be a matroid on ground set $E$.*
1. *If $E = A \dot\cup B$ with $A, B \neq \emptyset$ and $r_M(A) + r_M(B) = r(M)$, then $M = (M | A) \oplus (M | B)$ is disconnected.*
2. *If $M$ is connected and $g(M) \ge 2$, then $M$ has no loops and no coloops; moreover, for any $x \in E$, the contraction $M / x$ has no coloops.*
3. *If $x \in E$ is a non-loop and $C \in \mathrm{Cir}(M)$ contains $x$, then $C \setminus \{x\} \in \mathrm{Cir}(M / x)$.*

*Proof.*
(1) Let $C$ be any circuit of $M$ and suppose $C$ intersects both $A$ and $B$. Then $C \cap A \subsetneq C$ and $C \cap B \subsetneq C$ are independent in $M | A$ and $M | B$, respectively, so they extend to bases $B_A$ of $M | A$ and $B_B$ of $M | B$. Since $B_A$ spans $A$ and $B_B$ spans $B$, $B_A \cup B_B$ spans $E$, so $r_M(B_A \cup B_B) = r(M) = r_M(A) + r_M(B) = |B_A| + |B_B| = |B_A \cup B_B|$. Thus $B_A \cup B_B$ is independent in $M$, contradicting $C \subseteq B_A \cup B_B$. Hence every circuit of $M$ lies entirely in $A$ or entirely in $B$, so $M = (M | A) \oplus (M | B)$.

(2) A loop forms a connected component of size $1$ and corank $1$; a coloop forms a connected component of size $1$ and corank $0$. Since $M$ is connected and $g(M) \ge 2$, $M$ has neither loops nor coloops. For any $x \in E$ and $y \in E \setminus \{x\}$, since $x$ is not a loop we have $r_{M/x}(A) = r_M(A \cup \{x\}) - 1$ for every $A \subseteq E \setminus \{x\}$. If $y$ were a coloop of $M / x$, then
$$r_M(E \setminus \{y\}) = r_{M/x}((E \setminus \{x\}) \setminus \{y\}) + 1 = (r(M / x) - 1) + 1 = r(M) - 1,$$
making $y$ a coloop of $M$, contradiction.

(3) For any non-loop $x$ and $I \subseteq E \setminus \{x\}$, $I \in \mathcal{I}(M / x) \iff I \cup \{x\} \in \mathcal{I}(M)$. Since $C \in \mathrm{Cir}(M)$ contains $x$, $(C \setminus \{x\}) \cup \{x\} = C$ is dependent in $M$, while for every proper subset $B \subsetneq C \setminus \{x\}$, $B \cup \{x\} \subsetneq C$ is independent in $M$. Thus $C \setminus \{x\}$ is minimal dependent in $M / x$. $\blacksquare$

**Lemma 3 (Parallel-connection circuit elimination).** *Let $M$ be a binary matroid, let $x \in E(M)$ be a non-loop, and suppose $M / x = W_1 \oplus W_{\mathrm{rest}}$ with disjoint nonempty ground sets $E_1 := E(W_1)$ and $E_{\mathrm{rest}} := E(W_{\mathrm{rest}})$. Let $C_1, D \in \mathrm{Cir}(M)$ satisfy $x \in C_1 \subseteq E_1 \cup \{x\}$ and $x \in D \subseteq E_{\mathrm{rest}} \cup \{x\}$. Then*
$$D \triangle C_1 = (C_1 \setminus \{x\}) \dot\cup (D \setminus \{x\})$$
*is a circuit of $M \setminus x$.*

*Proof.* Since $x$ is not a loop, $C_1 \setminus \{x\} \subseteq E_1$ and $D \setminus \{x\} \subseteq E_{\mathrm{rest}}$ are both nonempty and disjoint, so $C_1 \neq D$, $C_1 \cap D = \{x\}$, and $K^* := D \triangle C_1 = (C_1 \setminus \{x\}) \dot\cup (D \setminus \{x\})$. By circuit elimination on $C_1, D$ at $x$, there exists a circuit $K \in \mathrm{Cir}(M)$ with $K \subseteq K^*$. Set $K_1 := K \cap E_1 \subseteq C_1 \setminus \{x\}$ and $K_2 := K \cap E_{\mathrm{rest}} \subseteq D \setminus \{x\}$, so $K = K_1 \dot\cup K_2$.

- If $K_1 \subsetneq C_1 \setminus \{x\}$ and $K_2 \subsetneq D \setminus \{x\}$: by Lemma 2(3), $C_1 \setminus \{x\} \in \mathrm{Cir}(W_1)$ and $D \setminus \{x\} \in \mathrm{Cir}(W_{\mathrm{rest}})$, so $K_1 \in \mathcal{I}(W_1)$ and $K_2 \in \mathcal{I}(W_{\mathrm{rest}})$. Hence $K = K_1 \dot\cup K_2 \in \mathcal{I}(W_1 \oplus W_{\mathrm{rest}}) = \mathcal{I}(M / x)$, which implies $K \cup \{x\} \in \mathcal{I}(M)$ and therefore $K \in \mathcal{I}(M)$, contradicting $K \in \mathrm{Cir}(M)$.
- If $K_1 = C_1 \setminus \{x\}$ and $K_2 \subsetneq D \setminus \{x\}$: since $M$ is binary, $K \triangle C_1 = K_2 \dot\cup \{x\} \in \mathcal{Z}(M)$ is nonempty (as it contains $x$) and therefore dependent in $M$. Yet $K_2 \dot\cup \{x\} \subsetneq (D \setminus \{x\}) \dot\cup \{x\} = D$, contradicting $D \in \mathrm{Cir}(M)$.
- If $K_2 = D \setminus \{x\}$ and $K_1 \subsetneq C_1 \setminus \{x\}$: symmetrically, $K \triangle D = K_1 \dot\cup \{x\} \in \mathcal{Z}(M)$ is nonempty and strictly contained in $C_1$, contradicting $C_1 \in \mathrm{Cir}(M)$.

Consequently $K_1 = C_1 \setminus \{x\}$ and $K_2 = D \setminus \{x\}$, so $K = K^* = D \triangle C_1 \in \mathrm{Cir}(M)$. Since $x \notin K^*$, $D \triangle C_1 \in \mathrm{Cir}(M \setminus x)$. $\blacksquare$

---

## 4. Proof of the Main Theorem

*Proof of the Main Theorem.* We proceed by strong induction on $|E(M)|$. Let $M$ be a matroid of corank $g$ with circuit system $\mathcal{C} = \{C_1, \dots, C_g\}$ such that $D := \mathcal{C}_{[g]} \in \mathrm{Cir}(M)$. Since $D$ is nonempty, $g \ge 1$ and $|E(M)| \ge 1$. By Theorem 4.3 (`thm:cycle system binary`), $M$ is binary.

**Base case ($g = 1$).** If $g = 1$, then $|\mathcal{C}| = 1$, so $\mathrm{mult}_{\mathcal{C}}(e) \le 1$ for every $e \in E(M)$, and hence $\mathcal{C}_{\ge 3} = \emptyset$. (This covers $|E(M)| = 1$ in particular.) Assume henceforth that $g \ge 2$.

**Step 1 (Reduction to connected $M$).** Suppose $M$ is disconnected, with connected-component decomposition $M = M_1 \oplus \dots \oplus M_r$ ($r \ge 2$). Because every circuit of a direct sum lies in a single component, $\mathcal{C}$ partitions as $\mathcal{C} = \bigsqcup_{j=1}^r \mathcal{C}^{(j)}$, where $\mathcal{C}^{(j)} := \{C \in \mathcal{C} : C \subseteq E(M_j)\}$. By Lemma 1(2), $\mathcal{C}$ is linearly independent over $\mathbb{F}_2$ and consists of circuits, so each $\mathcal{C}^{(j)}$ is a linearly independent subset of $\mathcal{Z}(M_j)$; hence $|\mathcal{C}^{(j)}| \le \dim_{\mathbb{F}_2} \mathcal{Z}(M_j) \le g(M_j)$. Summing over $j = 1, \dots, r$ yields
$$g(M) = |\mathcal{C}| = \sum_{j=1}^r |\mathcal{C}^{(j)}| \le \sum_{j=1}^r g(M_j) = g(M),$$
so $|\mathcal{C}^{(j)}| = g(M_j)$ for every $j$. Every nonempty subset of $\mathcal{C}^{(j)}$ has dependent unique union (as a subset of $\mathcal{C}$), so $\mathcal{C}^{(j)}$ is a circuit system on $M_j$. Since $E(M_1), \dots, E(M_r)$ are pairwise disjoint,
$$D = \mathcal{C}_{[g]} = \bigsqcup_{j=1}^r (\mathcal{C}^{(j)})_{[g(M_j)]}.$$
For every $j$ with $g(M_j) \ge 1$, the set $(\mathcal{C}^{(j)})_{[g(M_j)]}$ is dependent in $M_j$, hence contains a circuit of $M_j$. Because $D$ is a single circuit of $M$ (it contains no proper dependent subset), exactly one component—say $M_1$—satisfies $g(M_1) = g \ge 1$, while $g(M_j) = 0$ (and $\mathcal{C}^{(j)} = \emptyset$) for all $j \ge 2$. Thus $\mathcal{C} = \mathcal{C}^{(1)}$ is a circuit system on $M_1$ with $\mathcal{C}_{[g]} = D \in \mathrm{Cir}(M_1)$ and the same $\mathcal{C}_{\ge 3}$. Since $r \ge 2$ implies $|E(M_1)| < |E(M)|$, the induction hypothesis gives $\mathcal{C}_{\ge 3} = \emptyset$.

**Step 2 (Contraction at an element $x \in D$).** Assume henceforth that $M$ is connected and $g \ge 2$. By Lemma 2(2), $M$ has no loops and no coloops. Choose any element $x \in D = \mathcal{C}_{[g]}$; relabeling if necessary, let $C_1 \in \mathcal{C}$ be the unique circuit in $\mathcal{C}$ containing $x$.

Consider the contraction $M / x$. Because $x$ is not a loop, $g(M / x) = |E(M) \setminus \{x\}| - (r(M) - 1) = g$, and by Proposition 2.19(2) (`prop:del-con cs`),
$$\mathcal{C}'' := \{C_1 \setminus \{x\}, C_2, \dots, C_g\}$$
is a cycle system on $M / x$. Its $g$ elements are pairwise distinct: for $2 \le i < j \le g$ we have $C_i \neq C_j$, while $C_1 \setminus \{x\} = C_j$ ($j \ge 2$) would give $C_j \subsetneq C_1$, impossible since $C_1, C_j \in \mathrm{Cir}(M)$. Moreover, since $x \in C_1$ and $x \notin C_2, \dots, C_g$, every $z \in E(M) \setminus \{x\}$ satisfies $\mathrm{mult}_{\mathcal{C}''}(z) = \mathrm{mult}_{\mathcal{C}}(z)$; in particular,
$$\mathcal{C}''_{[g]} = D \setminus \{x\} \qquad \text{and} \qquad \mathcal{C}''_{\ge 3} = \mathcal{C}_{\ge 3}.$$
By Lemma 2(3), $D \setminus \{x\} \in \mathrm{Cir}(M / x)$. We split into two cases according to the connectivity of $M / x$.

**Case 1: $M / x$ is connected.**
By Lemma 2.21 (`lem:circuitsys`), the cycle system $\mathcal{C}''$ on the connected matroid $M / x$ is in fact a circuit system. Since $\mathcal{C}''_{[g]} = D \setminus \{x\} \in \mathrm{Cir}(M / x)$ and $|E(M / x)| = |E(M)| - 1 < |E(M)|$, the induction hypothesis gives $\mathcal{C}_{\ge 3} = \mathcal{C}''_{\ge 3} = \emptyset$.

**Case 2: $M / x$ is disconnected.**
Let $M / x = W_1 \oplus W_2 \oplus \dots \oplus W_k$ ($k \ge 2$) be the connected-component decomposition of $M / x$, ordered according to Theorem 2.22 (`thm:components`) applied to the cycle system $\mathcal{C}''$: there exist cycle systems $\mathcal{C}^{(j)}$ on $W_j$ ($1 \le j \le k$) such that $\mathcal{C}'' = \bigsqcup_{j=1}^k \widetilde{\mathcal{C}^{(j)}}$, where every element of $\widetilde{\mathcal{C}^{(j)}}$ has the form $C \cup K_C$ with $C \in \mathcal{C}^{(j)}$ and $K_C \subseteq \bigsqcup_{t=1}^{j-1} E(W_t)$, and $\widetilde{\mathcal{C}^{(1)}} = \mathcal{C}^{(1)}$.

1. *Every component $W_j$ has $g(W_j) \ge 1$.* If $g(W_j) = 0$, then $W_j$ is connected with no circuits, so $|E(W_j)| = 1$ and its sole element is a coloop of $M / x$, contradicting Lemma 2(2).
2. *$D \setminus \{x\} \subseteq E(W_k)$.* Every element of $\widetilde{\mathcal{C}^{(j)}}$ for $j < k$ is disjoint from $E(W_k)$, while the elements of $\widetilde{\mathcal{C}^{(k)}}$ intersect $E(W_k)$ in precisely $\mathcal{C}^{(k)}$. Hence
   $$(D \setminus \{x\}) \cap E(W_k) = \mathcal{C}''_{[g]} \cap E(W_k) = (\mathcal{C}^{(k)})_{[g(W_k)]}.$$
   Since $g(W_k) \ge 1$ and $\mathcal{C}^{(k)}$ is a cycle system on $W_k$, $(\mathcal{C}^{(k)})_{[g(W_k)]}$ is dependent in $W_k$ and hence nonempty. Because $D \setminus \{x\}$ is a circuit of $M / x = \bigoplus_{j=1}^k W_j$, it lies in a single component, which must therefore be $W_k$.
3. *$C_1 \subseteq E(W_1) \cup \{x\}$.* Set $E_1 := E(W_1)$ and $E_{\mathrm{rest}} := \bigsqcup_{j=2}^k E(W_j) \neq \emptyset$, so $M / x = W_1 \oplus W_{\mathrm{rest}}$ with $W_{\mathrm{rest}} := \bigoplus_{j=2}^k W_j$. By Theorem 2.22, $\widetilde{\mathcal{C}^{(1)}} = \mathcal{C}^{(1)} \subseteq \mathcal{C}''$ consists of $g(W_1)$ distinct elements of $\mathcal{C}''$ contained in $E_1$. Let $I_1 := \{i \in [g] : C_i \setminus \{x\} \in \mathcal{C}^{(1)}\}$; because the elements of $\mathcal{C}''$ are pairwise distinct, $|I_1| = g(W_1)$, and $C_i \subseteq E_1 \cup \{x\}$ for all $i \in I_1$.

   Using $r_{M/x}(A) = r_M(A \cup \{x\}) - 1$ for $A \in \{E_1, E_{\mathrm{rest}}, E_1 \cup E_{\mathrm{rest}}\}$, the direct-sum rank equality $r_{M/x}(E_1) + r_{M/x}(E_{\mathrm{rest}}) = r(M / x)$ becomes
   $$r_M(E_1 \cup \{x\}) + r_M(E_{\mathrm{rest}} \cup \{x\}) = r(M) + 1.$$
   If $r_M(E_1) < r_M(E_1 \cup \{x\})$, then $r_M(E_1) = r_M(E_1 \cup \{x\}) - 1$ and thus $r_M(E_1) + r_M(E_{\mathrm{rest}} \cup \{x\}) = r(M)$, contradicting connectedness of $M$ by Lemma 2(1). Therefore $r_M(E_1) = r_M(E_1 \cup \{x\}) = r(W_1) + 1$, so the binary matroid $M | E_1$ satisfies
   $$\dim_{\mathbb{F}_2} \mathcal{Z}(M | E_1) \le g(M | E_1) = |E_1| - r_M(E_1) = |E_1| - r(W_1) - 1 = g(W_1) - 1.$$
   By Lemma 1(2), the $g(W_1)$ circuits $\{C_i : i \in I_1\}$ are linearly independent over $\mathbb{F}_2$. Since $g(W_1) > g(W_1) - 1 \ge \dim_{\mathbb{F}_2} \mathcal{Z}(M | E_1)$, not all of them can be contained in $E_1$. As $C_i \subseteq E_1 \cup \{x\}$ for all $i \in I_1$, some $i \in I_1$ satisfies $x \in C_i$. Since $C_1$ is the unique circuit of $\mathcal{C}$ containing $x$, we obtain $1 \in I_1$ and hence $C_1 \subseteq E_1 \cup \{x\}$.
4. *$D \triangle C_1 \in \mathrm{Cir}(M \setminus x)$.* Since $k \ge 2$, $E(W_k) \subseteq E_{\mathrm{rest}}$ is disjoint from $E_1$. Thus $x \in C_1 \subseteq E_1 \cup \{x\}$ and $x \in D \subseteq E_{\mathrm{rest}} \cup \{x\}$, so $D \cap C_1 = \{x\}$ and Lemma 3 implies that $D \triangle C_1 = (C_1 \setminus \{x\}) \dot\cup (D \setminus \{x\})$ is a circuit of $M \setminus x$.
5. *$*$-deletion at $x$ and induction.* By Proposition 2.19(1) (`prop:del-con cs`), $\mathcal{C}' := \mathcal{C} \setminus \{C_1\} = \{C_2, \dots, C_g\}$ is a cycle system on $M \setminus x$; since every $C_i$ ($i \ge 2$) is a circuit of $M$ avoiding $x$, $\mathcal{C}'$ is a **circuit system** on $M \setminus x$ (with corank $g(M \setminus x) = g - 1 \ge 1$). Let us determine $\mathcal{C}'_{[g-1]}$ by checking the multiplicity of every $z \in E(M) \setminus \{x\}$:
   - If $z \in D \setminus \{x\}$: since $D \cap C_1 = \{x\}$, $z \notin C_1$, so $\mathrm{mult}_{\mathcal{C}'}(z) = \mathrm{mult}_{\mathcal{C}}(z) = 1$, hence $z \in \mathcal{C}'_{[g-1]}$.
   - If $z \in C_1 \setminus \{x\}$: since $D \cap C_1 = \{x\}$, $z \notin D = \mathcal{C}_{[g]}$ while $z \in C_1$, so $\mathrm{mult}_{\mathcal{C}}(z) \ge 2$. Therefore $\mathrm{mult}_{\mathcal{C}'}(z) = \mathrm{mult}_{\mathcal{C}}(z) - 1$, which equals $1$ if and only if $\mathrm{mult}_{\mathcal{C}}(z) = 2$, and is $\ge 2$ if and only if $z \in C_1 \cap \mathcal{C}_{\ge 3}$.
   - If $z \notin D \cup C_1$: $\mathrm{mult}_{\mathcal{C}'}(z) = \mathrm{mult}_{\mathcal{C}}(z) \neq 1$, so $z \notin \mathcal{C}'_{[g-1]}$.

   Consequently,
   $$\mathcal{C}'_{[g-1]} = (D \setminus \{x\}) \dot\cup \{z \in C_1 \setminus \{x\} : \mathrm{mult}_{\mathcal{C}}(z) = 2\} = (D \triangle C_1) \setminus (C_1 \cap \mathcal{C}_{\ge 3}) \subseteq D \triangle C_1.$$
   Because $\mathcal{C}'$ is a circuit system on $M \setminus x$ with $g - 1 \ge 1$, $\mathcal{C}'_{[g-1]}$ is dependent in $M \setminus x$. Because $D \triangle C_1$ is a circuit of $M \setminus x$, no proper subset of $D \triangle C_1$ is dependent; therefore
   $$\mathcal{C}'_{[g-1]} = D \triangle C_1 \in \mathrm{Cir}(M \setminus x) \qquad \text{and} \qquad C_1 \cap \mathcal{C}_{\ge 3} = \emptyset.$$
   Since $x \in D$ and $C_1 \cap \mathcal{C}_{\ge 3} = \emptyset$, every element $z \in E(M) \setminus \{x\}$ satisfies $\mathrm{mult}_{\mathcal{C}'}(z) \ge 3 \iff \mathrm{mult}_{\mathcal{C}}(z) \ge 3$, so $\mathcal{C}'_{\ge 3} = \mathcal{C}_{\ge 3}$. Finally, $|E(M \setminus x)| = |E(M)| - 1 < |E(M)|$, so applying the induction hypothesis to $(M \setminus x, \mathcal{C}')$ gives $\mathcal{C}_{\ge 3} = \mathcal{C}'_{\ge 3} = \emptyset$.

This completes the induction and proves the Main Theorem. $\blacksquare$

*Remark (Necessity of Case 2).* Case 2 genuinely occurs even for every $x \in D$ simultaneously: take the planar necklace graph $G$ formed by a triangle $D = \{x, y, z\}$ with a parallel $2$-edge ear $\{e_1, e_2\}$, $\{f_1, f_2\}$, $\{h_1, h_2\}$ glued along each of $x, y, z$, and circuit system $C_1 = \{x, e_1, e_2\}$, $C_2 = \{y, f_1, f_2\}$, $C_3 = \{z, h_1, h_2\}$, $C_4 = \{e_1, e_2, f_1, f_2, h_1, h_2\}$ ($g = 4$, $\mathcal{C}_{[4]} = D$). For every $x \in D$, $M(G) / x$ is disconnected ($W_1 = \{e_1, e_2\}$ and $W_2 = G / x \setminus \{e_1, e_2\}$), and $C_4$ splits into two disjoint circuits in $M(G) / x$; Step 2 switches to $*$-deletion $M(G) \setminus x$, where $\mathcal{C}' = \{C_2, C_3, C_4\}$ has $\mathcal{C}'_{[3]} = \{e_1, e_2, y, z\} = D \triangle C_1 \in \mathrm{Cir}(M(G) \setminus x)$.

---

## 5. Proofs of Corollaries 1 and 2

*Proof of Corollary 1 (Conjecture 7.4 `conj:unique`).* Let $M$ be a matroid with circuit system $\mathcal{C} = \{C_1, \dots, C_g\}$ and let $D \in \mathrm{Cir}(M)$. By Lemma 6.4 (`lem:reachable to D`), there exists a subsystem $\mathcal{C}^D \subseteq \mathcal{C}$ reachable from $\mathcal{C}$ via a finite sequence of $*$-deletions removing elements $e_1, \dots, e_m \notin D$, such that $\mathcal{C}^D$ is a cycle system on $M^D := M \setminus \{e_1, \dots, e_m\}$ whose total unique union is $D$. Because every element of $\mathcal{C}^D \subseteq \mathcal{C}$ is a circuit of $M$ disjoint from $\{e_1, \dots, e_m\}$, it remains a circuit of $M^D$; hence $\mathcal{C}^D$ is a **circuit system** on $M^D$ with total unique union $D \in \mathrm{Cir}(M^D)$. Applying the Main Theorem to $(M^D, \mathcal{C}^D)$ yields $(\mathcal{C}^D)_{\ge 3} = \emptyset$, which is independent in $M^D$ (and $M$). Proposition 6.7 (`prop:C>=3`) therefore gives $|\{S \subseteq [g] : \mathcal{C}_S = D\}| = 1$. $\blacksquare$

*Proof of Corollary 2 (Cographic Characterization).*
$(\Rightarrow)$ Suppose $M$ is a connected matroid of corank $g \ge 1$ with circuit system $\mathcal{C} = \{C_1, \dots, C_g\}$ and $D := \mathcal{C}_{[g]} \in \mathrm{Cir}(M)$. By Theorem 4.3 and Lemma 1(2), $M$ is binary and $\mathcal{C}$ is an $\mathbb{F}_2$-basis of $\mathcal{Z}(M)$. By the Main Theorem, $\mathcal{C}_{\ge 3} = \emptyset$, so $\mathrm{mult}_{\mathcal{C}}(e) \le 2$ for every $e \in E(M)$. Furthermore, since $M$ is connected and $g \ge 1$, every $e \in E(M)$ belongs to some circuit $K \in \mathrm{Cir}(M)$ (if $|E(M)| = 1$ then $e$ is a loop; if $|E(M)| \ge 2$ then $M$ has no coloops); writing $K = \triangle_{i \in S} C_i \subseteq \bigcup_{i=1}^g C_i$ shows $\mathrm{mult}_{\mathcal{C}}(e) \ge 1$.

Set $C_0 := D$. Then every $e \in E(M)$ belongs to **exactly two** sets among $\{C_0, C_1, \dots, C_g\}$: if $e \in D = \mathcal{C}_{[g]}$, it lies in $C_0$ and in one $C_i$ ($i \ge 1$); if $e \notin D$, it does not lie in $C_0$ and satisfies $\mathrm{mult}_{\mathcal{C}}(e) = 2$. Define the graph $G$ on vertex set $V(G) = \{0, 1, \dots, g\}$ with edge set $E(M)$ by letting each $e \in E(M)$ join the unique pair $\{i, j\} \subseteq \{0, 1, \dots, g\}$ with $e \in C_i \cap C_j$. By construction, $G$ has no self-loops and $C_i = \delta_G(i)$ (the set of edges incident to vertex $i$) for every $0 \le i \le g$. If $G$ were disconnected, taking the union $B \subseteq \{1, \dots, g\}$ of all vertices in a component not containing $0$ would yield $\triangle_{i \in B} C_i = \triangle_{i \in B} \delta_G(i) = \delta_G(B) = \emptyset$, contradicting Lemma 1(1). Hence $G$ is connected, so $\{\delta_G(1), \dots, \delta_G(g)\}$ is an $\mathbb{F}_2$-basis of the cut space $\mathcal{Z}(M(G)^*)$. Thus $\mathcal{Z}(M) = \mathrm{span}_{\mathbb{F}_2}\{C_1, \dots, C_g\} = \mathcal{Z}(M(G)^*)$. Because the circuits of a binary matroid are the inclusion-minimal nonempty elements of its circuit space, $M = M(G)^*$, with $\mathcal{C} = \{\delta_G(1), \dots, \delta_G(g)\}$ and $\delta_G(0) = D$.

$(\Leftarrow)$ Conversely, if $M = M(G)^*$ is connected with $g \ge 1$ (discarding any isolated vertices of $G$), then $G$ is connected on $g + 1$ vertices, has no self-loops (which would be coloops of $M(G)^*$), and has no cut-vertices (so $G$ is $2$-connected for $g \ge 2$, or consists of parallel edges on $2$ vertices for $g = 1$). Hence for every vertex $v \in V(G)$, $G - v$ is connected, so $\delta_G(v)$ is a minimal cut (circuit of $M(G)^*$). Fixing any sink $q \in V(G)$ and setting $\mathcal{C} := \{\delta_G(v) : v \in V(G) \setminus \{q\}\}$, for every nonempty $S \subseteq V(G) \setminus \{q\}$ an edge lies in exactly one $\delta_G(v)$ ($v \in S$) if and only if it has one endpoint in $S$ and one in $V(G) \setminus S$; thus $\mathcal{C}_S = \delta_G(S)$ is a nonempty cut of the connected graph $G$ (hence dependent in $M(G)^*$), and $\mathcal{C}_{[g]} = \delta_G(V(G) \setminus \{q\}) = \delta_G(q) \in \mathrm{Cir}(M(G)^*)$. $\blacksquare$

---

## 6. Exact Verification

The standalone pure-integer verification script [`verify.py`](file:///Users/kolinhuang/Documents/open-math/targets/dochtermann-2609.13361-conj7.5/verify.py) (AST-audited for zero floating-point literals/calls and zero `/` divisions) independently verifies:
1. **Necklace Case-2 stress test:** Exact verification of Steps 1–5 of Case 2 (including `thm:components` triangular decomposition, rank identities, $D \cap C_1 = \{x\}$, $D \triangle C_1 \in \mathrm{Cir}(M \setminus x)$, and $*$-deletion reduction) for every $x \in D$ on the $6$-vertex, $9$-edge necklace graph where $M / x$ is disconnected for all $x \in D$.
2. **Exhaustive graphic matroids ($n \le 6, g \le 5$, plus $K_5$):** All biconnected simple graphs (planar and non-planar); verifies Main Theorem ($\mathcal{C}_{\ge 3} = \emptyset$), Case 1 / Case 2 inductive reduction for every $x \in D$, Corollary 1 (`conj:unique`) across all circuits $D$ of every circuit system (including all $5$ cone systems of $M(K_5)$, which have $\mathcal{C}_{[6]} \notin \mathrm{Cir}(M(K_5))$), and Corollary 2 (explicit graph reconstruction $M = M(G)^*$).
3. **Exhaustive cographic matroids ($4 \le n \le 6$):** All $69$ biconnected simple graphs (including $M(K_5)^*, M(K_{3,3})^*, M(K_6)^*$: $8{,}408$ circuit systems, $2{,}075$ with $\mathcal{C}_{[g]} \in \mathrm{Cir}(M)$); verifies $\mathcal{C}_{\ge 3} = \emptyset$, Case 1 / Case 2 reduction, and Corollary 2 reconstruction.
4. **Exhaustive rank-$2$ binary matroids (parallel extensions of $U_{2,3}$, $m \le 7$), disconnected matroids with coloops, and hypothesis-necessity examples** (`Example 6.8` $U_{1,6}$ and `Figure 2` non-circuit cycle system), plus an explicit circuit system on the non-graphic, non-cographic regular $2$-sum $M(K_5) \oplus_2 M(K_5)^*$.

# Proof of Conjecture 1 (`arXiv:2604.22375v1`, Section 3.1)

**Target:** `targets/ciobanu-2604.22375-conj1/`  
**Statement:** In every finitely generated group $G$, every $\mathbf{VPL}^\forall$ subset is recognisable, i.e.,
$$\mathbf{VPL}^\forall(G) = \mathbf{REG}^\forall(G).$$

---

## Proof

The inclusion $\mathbf{REG}^\forall(G) \subseteq \mathbf{VPL}^\forall(G)$ is immediate because every regular language over an alphabet $\Sigma$ is visibly pushdown (for instance with $\Sigma_i = \Sigma$ and $\Sigma_c = \Sigma_r = \emptyset$, or with an automaton ignoring stack symbols).

Conversely, let $S \in \mathbf{VPL}^\forall(G)$. By definition, there exist a finite generating set $\Sigma$ of $G$ (with surjective monoid homomorphism $\pi \colon \Sigma^\star \to G$) and a visibly pushdown partition $\Sigma = \Sigma_c \sqcup \Sigma_i \sqcup \Sigma_r$ such that $L := \pi^{-1}(S) \subseteq \Sigma^\star$ is accepted by a visibly pushdown automaton (VPA)
$$M = (Q, \Gamma, \delta, Q_0, F)$$
following the convention of Ciobanu–Turaev (`arXiv:2604.22375v1`, Section 1.1): there are no $\varepsilon$-transitions; the unique bottom-of-stack symbol $\bot \in \Gamma$ cannot be pushed by $\Sigma_c$ (the stack is empty iff only $\bot$ is on the stack); letters in $\Sigma_c$ push a symbol from $\Gamma \setminus \{\bot\}$; letters in $\Sigma_i$ leave the stack unchanged; letters in $\Sigma_r$ pop the top symbol of $\Gamma \setminus \{\bot\}$ if the stack is non-empty and read (without removing) $\bot$ if the stack is empty; and a word is accepted iff some run from $(q_0, \bot)$ ($q_0 \in Q_0$) ends in a state $q \in F$ (with arbitrary stack contents).

We prove that the left-stabilizer subgroup
$$H := \mathrm{Stab}_L(S) = \{ h \in G : h S = S \} \le G$$
has finite index in $G$, which implies $S \in \mathbf{REG}^\forall(G)$. (Indeed, $1_G \in H$, $h_1, h_2 \in H \implies (h_1 h_2) S = h_1 (h_2 S) = S$, and $h \in H \implies h^{-1} S = h^{-1} (h S) = S$, so $H$ is a subgroup of $G$.)

We consider two cases according to whether $\Sigma_r$ is empty.

---

### Case 1: $\Sigma_r = \emptyset$

Since $\Sigma_r = \emptyset$, no transition of $M$ ever inspects the stack. Projecting away the pushed stack symbols on $\Sigma_c$-transitions turns $M$ into an NFA $M' = (Q, \Sigma, \delta', Q_0, F)$ accepting the exact same language $L = \pi^{-1}(S)$, so $L$ is regular.

For $u \in \Sigma^\star$, let $R(u) \subseteq Q$ be the set of states reachable in $M'$ after reading $u$. If $R(u_1) = R(u_2)$, then for all $v \in \Sigma^\star$ we have $u_1 v \in L \iff u_2 v \in L$. For any $g \in G$, surjectivity of $\pi$ yields $v \in \Sigma^\star$ with $\pi(v) = \pi(u_2)^{-1} g$, so
$$\pi(u_1)\pi(u_2)^{-1} g \in S \iff u_1 v \in L \iff u_2 v \in L \iff g \in S.$$
Thus $\pi(u_1)\pi(u_2)^{-1} \in H$, i.e., $H \pi(u_1) = H \pi(u_2)$. Since $\pi \colon \Sigma^\star \to G$ is surjective and there are at most $2^{|Q|}$ subsets $R(u) \subseteq Q$, we obtain $[G : H] = |H \backslash G| \le 2^{|Q|} < \infty$.

---

### Case 2: $\Sigma_r \neq \emptyset$

Consider the matched-call (non-positive-suffix) sublanguage
$$\mathit{MC}(\Sigma) := \{ w \in \Sigma^\star : \text{every suffix } s \text{ of } w \text{ satisfies } \#_c(s) \le \#_r(s) \},$$
where $\#_c(s)$ and $\#_r(s)$ denote the numbers of letters from $\Sigma_c$ and $\Sigma_r$ in $s$, respectively. Set $M_{\mathrm{mc}} := \pi(\mathit{MC}(\Sigma)) \subseteq G$.

#### Lemma 1 ($\mathit{MC}(\Sigma)$ is a submonoid generating $G$ as a group)
1. $\varepsilon \in \mathit{MC}(\Sigma)$, and $\mathit{MC}(\Sigma)$ is closed under concatenation; hence $M_{\mathrm{mc}}$ is a submonoid of $G$.
2. $\Sigma_r \cup \Sigma_i \cup (\Sigma_c \Sigma_r) \subseteq \mathit{MC}(\Sigma)$. Consequently, $\langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}} = G$.

*Proof of Lemma 1.*
1. The only suffix of $\varepsilon$ is $\varepsilon$, which has $\#_c(\varepsilon) = 0 \le 0 = \#_r(\varepsilon)$. If $u, v \in \mathit{MC}(\Sigma)$ and $s$ is any suffix of $u v$, then either $s$ is a suffix of $v$ (so $\#_c(s) \le \#_r(s)$ since $v \in \mathit{MC}(\Sigma)$), or $s = s_u v$ for a suffix $s_u$ of $u$. In the latter case, since $s_u$ is a suffix of $u$ and $v$ is a suffix of $v$,
   $$\#_c(s) = \#_c(s_u) + \#_c(v) \le \#_r(s_u) + \#_r(v) = \#_r(s).$$
   Hence $u v \in \mathit{MC}(\Sigma)$, so $M_{\mathrm{mc}} = \pi(\mathit{MC}(\Sigma))$ is a submonoid of $G$.
2. For $y \in \Sigma_r$, the suffixes are $\varepsilon$ ($0 \le 0$) and $y$ ($0 \le 1$). For $z \in \Sigma_i$, the suffixes are $\varepsilon$ ($0 \le 0$) and $z$ ($0 \le 0$). For $x \in \Sigma_c$ and $y \in \Sigma_r$, the suffixes of $x y$ are $\varepsilon$ ($0 \le 0$), $y$ ($0 \le 1$), and $x y$ ($1 \le 1$). Since $\Sigma_r \neq \emptyset$, fix some $y_0 \in \Sigma_r$. Then $\pi(y_0) \in M_{\mathrm{mc}}$, and for every $x \in \Sigma_c$ we have $\pi(x y_0) = \pi(x) \pi(y_0) \in M_{\mathrm{mc}}$, whence
   $$\pi(x) = \pi(x y_0)\pi(y_0)^{-1} \in \langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}}.$$
   Also $\pi(\Sigma_r \cup \Sigma_i) \subseteq M_{\mathrm{mc}} \subseteq \langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}}$. Since $\Sigma = \Sigma_c \sqcup \Sigma_i \sqcup \Sigma_r$ generates $G$ as a monoid, $\langle M_{\mathrm{mc}} \rangle_{\mathrm{grp}} = G$. $\square$

#### Lemma 2 (Empty stack on $\mathit{MC}(\Sigma)$ and finite index of $\sim_0$)
1. Every valid run of $M$ on any word $u \in \mathit{MC}(\Sigma)$ starting with empty stack $\bot$ terminates with empty stack $\bot$.
2. Define $u_1 \sim_0 u_2$ on $\mathit{MC}(\Sigma)$ by $\forall v \in \Sigma^\star, (u_1 v \in L \iff u_2 v \in L)$. Then $|\mathit{MC}(\Sigma) / {\sim_0}| \le 2^{|Q|} < \infty$.
3. If $u_1, u_2 \in \mathit{MC}(\Sigma)$ satisfy $u_1 \sim_0 u_2$, then $H \pi(u_1) = H \pi(u_2)$.

*Proof of Lemma 2.*
1. Let $u = a_1 \cdots a_m \in \mathit{MC}(\Sigma)$, and let $(q_0, \sigma_0), (q_1, \sigma_1), \dots, (q_m, \sigma_m)$ be a run of $M$ on $u$ with $\sigma_0 = \bot$, where $h_k \ge 0$ denotes the number of symbols from $\Gamma \setminus \{\bot\}$ above $\bot$ on the stack $\sigma_k$ ($h_0 = 0$). Suppose for contradiction that $h_m > 0$, and let $j := \max\{ 0 \le k < m : h_k = 0 \}$. Then $h_k \ge 1$ for every $k \in \{j+1, \dots, m\}$. At step $j+1$, the stack height increases from $h_j = 0$ to $h_{j+1} \ge 1$, so $a_{j+1}$ must belong to $\Sigma_c$ and $h_{j+1} - h_j = 1$. For each $k \in \{j+2, \dots, m\}$, the stack prior to reading $a_k$ has height $h_{k-1} \ge 1$ (non-empty), so $h_k - h_{k-1}$ equals $+1$ if $a_k \in \Sigma_c$, $0$ if $a_k \in \Sigma_i$, and $-1$ if $a_k \in \Sigma_r$. Summing over $k = j+1, \dots, m$ on the suffix $s := a_{j+1}\cdots a_m$ of $u$ gives
   $$0 < h_m = h_m - h_j = \#_c(s) - \#_r(s),$$
   contradicting $u \in \mathit{MC}(\Sigma)$. Hence $h_m = 0$, i.e., $\sigma_m = \bot$.
2. For $u \in \mathit{MC}(\Sigma)$, let $R(u) \subseteq Q$ be the set of states $q \in Q$ such that some run of $M$ on $u$ from $(q_0, \bot)$ ($q_0 \in Q_0$) ends at $(q, \sigma)$; by part (1), every such run ends at $(q, \bot)$. Thus for any $v \in \Sigma^\star$, $u v \in L$ iff $M$ has an accepting run on $v$ starting from $(q, \bot)$ for some $q \in R(u)$. Hence $R(u_1) = R(u_2) \implies u_1 \sim_0 u_2$, giving $|\mathit{MC}(\Sigma) / {\sim_0}| \le 2^{|Q|} < \infty$. (Notice this also follows directly from Proposition 3 (`prop:CongsVPLs`) of `arXiv:2604.22375v1`.)
3. If $u_1 \sim_0 u_2$, then for every $g \in G$, choosing $v \in \Sigma^\star$ with $\pi(v) = \pi(u_2)^{-1} g$ gives
   $$\pi(u_1)\pi(u_2)^{-1} g \in S \iff u_1 v \in L \iff u_2 v \in L \iff g \in S.$$
   Hence $\pi(u_1)\pi(u_2)^{-1} \in H$, which means $H \pi(u_1) = H \pi(u_2)$. $\square$

#### Lemma 3 (Finite index of $H$)
We have $[G : H] = |H \backslash G| \le |\mathit{MC}(\Sigma) / {\sim_0}| \le 2^{|Q|} < \infty$.

*Proof of Lemma 3.*
Let $\Omega := \{ H m : m \in M_{\mathrm{mc}} \} \subseteq H \backslash G$. Since $\varepsilon \in \mathit{MC}(\Sigma)$, $H = H \cdot 1_G \in \Omega$. By Lemma 2(3), the map $[u]_{\sim_0} \mapsto H \pi(u)$ is well-defined and maps $\mathit{MC}(\Sigma) / {\sim_0}$ onto $\Omega$, so $1 \le |\Omega| \le |\mathit{MC}(\Sigma) / {\sim_0}| \le 2^{|Q|} < \infty$.

For each $g \in G$, right multiplication $\rho_g \colon H \backslash G \to H \backslash G$ defined by $\rho_g(H x) := H(x g)$ is a well-defined bijection on $H \backslash G$ with inverse $\rho_{g^{-1}}$. For any $m \in M_{\mathrm{mc}}$ and any $H m' \in \Omega$ ($m' \in M_{\mathrm{mc}}$), Lemma 1(1) gives $m' m \in M_{\mathrm{mc}}$, so $\rho_m(H m') = H(m' m) \in \Omega$. Thus $\rho_m(\Omega) \subseteq \Omega$. Since $\Omega$ is finite and $\rho_m$ is injective, $\rho_m(\Omega) = \Omega$, and therefore $\rho_{m^{-1}}(\Omega) = \Omega$ as well.

Consequently, the subgroup $K := \{ g \in G : \rho_g(\Omega) = \Omega \} \le G$ contains $M_{\mathrm{mc}}$. By Lemma 1(2), $K = G$. Since $H \in \Omega$, every $g \in G$ satisfies
$$H g = \rho_g(H) \in \rho_g(\Omega) = \Omega.$$
Therefore $\Omega = H \backslash G$, and $[G : H] = |\Omega| \le 2^{|Q|} < \infty$. $\square$

---

### Conclusion (Both Cases)

In both Case 1 and Case 2, $H = \mathrm{Stab}_L(S)$ has finite index $n := [G : H] < \infty$ in $G$. Let
$$N := \bigcap_{g \in G} g H g^{-1}$$
be the normal core of $H$ in $G$ (the kernel of the left-multiplication homomorphism $G \to \mathrm{Sym}(G / H)$). Then $N \trianglelefteq G$ is normal and $[G : N] \le n! < \infty$.

For any $s \in S$ and $n \in N$, we have $n \in H$, so $n s \in S$; moreover $s n = (s n s^{-1}) s \in S$ since $N \trianglelefteq G$ implies $s n s^{-1} \in N \le H$. Thus $N s \subseteq S$ for every $s \in S$, so
$$S = \bigcup_{s \in S} N s$$
is a union of cosets of $N$. Since $[G : N] < \infty$, $S$ is a finite union of cosets of a finite-index normal subgroup of $G$. Letting $\varphi \colon G \twoheadrightarrow G / N$ be the quotient map, $\pi^{-1}(S) = (\varphi \circ \pi)^{-1}(\varphi(S))$ is accepted by the finite-state automaton with state set $G / N$, initial state $1_{G/N}$, transitions $(q, a) \mapsto q \cdot \varphi(\pi(a))$, and accepting states $\varphi(S)$ (equivalently, $S \in \mathbf{REG}^\forall(G)$ by Proposition 4 (`prop:recsetsareficosets`) of `arXiv:2604.22375v1`). $\blacksquare$

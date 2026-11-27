# Proof of Conjecture 5 (`con:F_k(n)`) of Blanco–Golubyatnikov–Konstantinova–Maslova–Nikiforov (`arXiv:2511.16959v3`)

## Primary Source & Exact Statement

**Primary source:** Saúl A. Blanco, Mikhail P. Golubyatnikov, Elena V. Konstantinova, Natalia V. Maslova, and Luka A. Nikiforov, *"Generating the symmetric group by three prefix reversals"*, `arXiv:2511.16959v3` (submitted 21 Nov 2025, revised 22 Sep 2026; published in *Discrete Mathematics & Theoretical Computer Science* **28:1**, Permutation Patterns 2025 (2026), Paper #7, DOI `10.46298/dmtcs.16975`), Section 1 (`Final-DMTCS-Format.tex` lines 135–143), Section 2 (line 250), and Section 4.1, Conjecture 5 (`\label{con:F_k(n)}`, lines 948–960).

**Definitions (`Final-DMTCS-Format.tex` lines 135–143, 250):** Let $\Omega := \{1, 2, \ldots, n\}$ and let $\mathrm{Sym}_n$ and $\mathrm{Alt}_n$ denote the symmetric and alternating groups on $\Omega$, with right-to-left composition $(\sigma\pi)(x) = \sigma(\pi(x))$. For each integer $i$ with $1 < i \le n$, the *prefix reversal* $r_i \in \mathrm{Sym}_n$ is the involution
$$r_i(x) = \begin{cases} i + 1 - x & \text{if } 1 \le x \le i, \\ x & \text{if } i < x \le n, \end{cases}$$
which is the product of $\lfloor i/2 \rfloor$ disjoint transpositions $(1\ i)(2\ (i-1))\cdots(\lfloor i/2 \rfloor\ (i+1-\lfloor i/2\rfloor))$.

**Verbatim Conjecture 5 (`con:F_k(n)`, Section 4.1, `Final-DMTCS-Format.tex` lines 948–960):**
> Let
> $$F_k(n) = \{m \,:\, k < m < n,\, \langle r_n, r_m, r_k \rangle = \mathrm{Sym}_n\},$$
> then
> $$\max_{n > k+1} |F_k(n)| = \begin{cases} k + 1, & \text{if } k \text{ is even}; \\ \frac{k + 1}{2}, & \text{if } k \text{ is odd}. \end{cases}$$

Here $k \ge 2$ is any integer (the domain of prefix reversals $r_k$). We prove Conjecture 5 in full.

---

## Main Theorem

**Theorem.** *For every integer $k \ge 2$,*
$$\max_{n > k+1} |F_k(n)| = \begin{cases} k + 1 & \text{if } k \text{ is even}, \\ \frac{k + 1}{2} & \text{if } k \text{ is odd}. \end{cases}$$

---

## Section 1: Proof of the Upper Bound

We first give a self-contained proof of the non-generation bound (Conjecture 4 of `arXiv:2511.16959v3`, also proved in Y. Lei, J. Zhao, Z. Zhu, and Y. Wu, `arXiv:2610.30892v1`, Theorem 3.1).

**Proposition 1.1.** *Let $2 \le k < m < n$. If $\langle r_n, r_m, r_k \rangle = \mathrm{Sym}_n$, then $m + k \ge n$ when $n$ is even, and $m + k \ge n - 1$ when $n$ is odd.*

*Proof.* Set $G := \langle r_n, r_m, r_k \rangle$. For each $i \in \{n, m, k\}$, let $E_i := \{\{x, i + 1 - x\} : 1 \le x \le \lfloor i/2 \rfloor\}$ be the matching of size $\lfloor i/2 \rfloor$ on $\Omega = \{1, \ldots, n\}$ given by the $2$-cycles of $r_i$.

Consider the simple graph $H := (\Omega, E_m \cup E_k)$. First, $E_m \cap E_k = \emptyset$: if $\{x, m + 1 - x\} = \{y, k + 1 - y\}$, summing the two elements yields $m + 1 = k + 1$, contradicting $k < m$. Second, $H$ is acyclic: in any simple cycle $v_0 - v_1 - \cdots - v_{2\ell - 1} - v_0$ ($\ell \ge 2$) of $H$, the edges must alternate between the two disjoint matchings $E_k$ and $E_m$. Reindexing so that $\{v_0, v_1\} \in E_k$, each pair of consecutive steps $\{v_{2j}, v_{2j+1}\} \in E_k$ and $\{v_{2j+1}, v_{2j+2}\} \in E_m$ satisfies $v_{2j+1} = k + 1 - v_{2j}$ and $v_{2j+2} = m + 1 - v_{2j+1} = v_{2j} + (m - k)$. By induction, $v_{2\ell} = v_0 + \ell(m - k) > v_0$, contradicting $v_{2\ell} = v_0$.

Hence $H$ is a forest with $|E_m| + |E_k| = \lfloor m/2 \rfloor + \lfloor k/2 \rfloor$ edges, so $H$ has exactly
$$c(H) = n - \lfloor m/2 \rfloor - \lfloor k/2 \rfloor$$
connected components. Let $Q$ be the multigraph whose vertex set is the set $\pi_0(H)$ of connected components of $H$ (so $|V(Q)| = c(H)$) and whose $\lfloor n/2 \rfloor$ edges correspond to the pairs $\{x, n + 1 - x\} \in E_n$, each joining the component of $x$ to the component of $n + 1 - x$. Since $r_m$ and $r_k$ preserve each component of $H$ and $r_n$ moves vertices only along edges of $E_n$, if $G = \mathrm{Sym}_n$ (in particular, if $G$ is transitive on $\Omega$), then $Q$ must be connected.

- **Case 1: $n = 2t + 1$ is odd ($t \ge 2$) and $m + k < n - 1 = 2t$.** Then $m + k \le 2t - 1$, so
  $$\lfloor m/2 \rfloor + \lfloor k/2 \rfloor \le \left\lfloor \frac{m + k}{2} \right\rfloor \le \left\lfloor \frac{2t - 1}{2} \right\rfloor = t - 1,$$
  giving $|V(Q)| = c(H) \ge (2t + 1) - (t - 1) = t + 2 = |E(Q)| + 2$. A graph with $|E(Q)| \le |V(Q)| - 2$ is disconnected, so $G$ is intransitive and $G \neq \mathrm{Sym}_n$.

- **Case 2: $n = 2t$ is even ($t \ge 2$) and $m + k < n = 2t$.** Again $m + k \le 2t - 1$ gives $\lfloor m/2 \rfloor + \lfloor k/2 \rfloor \le t - 1$, so $|V(Q)| = c(H) \ge 2t - (t - 1) = t + 1 = |E(Q)| + 1$.
  - If $|V(Q)| \ge t + 2$ or $Q$ is disconnected, then $G$ is intransitive and $G \neq \mathrm{Sym}_n$.
  - If $Q$ is connected with $|V(Q)| = t + 1 = |E(Q)| + 1$, then $Q$ is a tree (in particular, loopless and bipartite). Let $\pi_0(H) = \mathcal{A} \sqcup \mathcal{B}$ be its bipartition ($\mathcal{A}, \mathcal{B} \neq \emptyset$), and set $A := \bigcup_{C \in \mathcal{A}} C$ and $B := \bigcup_{C \in \mathcal{B}} C$. Then $\Omega = A \sqcup B$ is a partition into two nonempty sets. Both $r_m$ and $r_k$ preserve every component $C \in \pi_0(H)$ and hence fix $A$ and $B$ setwise. Because $n = 2t$ is even, $r_n$ has no fixed points, and every pair $\{x, n + 1 - x\} \in E_n$ joins a component in $\mathcal{A}$ to a component in $\mathcal{B}$; thus $r_n(A) = B$ and $r_n(B) = A$, forcing $|A| = |B| = t$. Consequently every element of $G$ either fixes both $A$ and $B$ setwise or swaps $A$ and $B$, so
    $$|G| \le 2(t!)^2 < (2t)! = |\mathrm{Sym}_n|,$$
    using $\binom{2t}{t} \ge \binom{4}{2} = 6 > 2$ for $t \ge 2$. Hence $G \neq \mathrm{Sym}_n$. $\square$

**Proposition 1.2 (Upper Bound).** *For every integer $k \ge 2$ and every integer $n > k + 1$,*
$$|F_k(n)| \le \begin{cases} k + 1 & \text{if } k \text{ is even}, \\ \frac{k + 1}{2} & \text{if } k \text{ is odd}. \end{cases}$$

*Proof.*
1. **Suppose $k$ is even.** By Proposition 1.1:
   - If $n$ is even, every $m \in F_k(n)$ satisfies $n - k \le m \le n - 1$, giving $|F_k(n)| \le k < k + 1$.
   - If $n$ is odd, every $m \in F_k(n)$ satisfies $n - k - 1 \le m \le n - 1$, giving $|F_k(n)| \le k + 1$.

2. **Suppose $k$ is odd.** We first claim that every $m \in F_k(n)$ is even. Suppose to the contrary that $m \in F_k(n)$ is odd, and partition $\Omega = O \sqcup E$ into odd positions $O := \{x \in \Omega : x \text{ odd}\}$ and even positions $E := \{x \in \Omega : x \text{ even}\}$. For any odd integer $i \le n$, $r_i(x) = i + 1 - x \equiv x \pmod 2$ for $1 \le x \le i$ and $r_i(x) = x$ for $x > i$, so $r_i$ preserves both $O$ and $E$ setwise. Hence both $r_k$ and $r_m$ preserve $O$ and $E$ setwise.
   - If $n$ is odd, then $r_n$ also preserves $O$ and $E$ setwise; since $n \ge k + 2 \ge 5$, both $O$ and $E$ are nonempty, so $\langle r_n, r_m, r_k \rangle$ is intransitive, contradicting $m \in F_k(n)$.
   - If $n$ is even, then $n \ge k + 2 \ge 5$ forces $n \ge 6$, and $r_n(x) = n + 1 - x$ interchanges $O$ and $E$ (with $|O| = |E| = n/2 \ge 3$). Thus every element of $\langle r_n, r_m, r_k \rangle$ preserves the unordered partition $\{O, E\}$, giving $|\langle r_n, r_m, r_k \rangle| \le 2((n/2)!)^2 < n!$, again contradicting $m \in F_k(n)$.

   Therefore every $m \in F_k(n)$ is even. Combining this with Proposition 1.1:
   - If $n$ is odd, $F_k(n)$ is contained in the set of even integers in $\{n - k - 1, n - k, \ldots, n - 1\}$. Because $k + 1$ is even, these $k + 1$ consecutive integers contain exactly $\frac{k + 1}{2}$ even integers (namely $n - k, n - k + 2, \ldots, n - 1$), so $|F_k(n)| \le \frac{k + 1}{2}$.
   - If $n$ is even, $F_k(n)$ is contained in the set of even integers in $\{n - k, n - k + 1, \ldots, n - 1\}$. Both endpoints $n - k$ and $n - 1$ are odd, so this interval of $k$ integers contains exactly $\frac{k - 1}{2}$ even integers, giving $|F_k(n)| \le \frac{k - 1}{2} < \frac{k + 1}{2}$. $\square$

---

## Section 2: Self-Contained Permutation-Group Lemmas

For any permutation $g \in \mathrm{Sym}_n$, let $\mathrm{supp}(g) := \{x \in \Omega : g(x) \neq x\}$ denote its support. We write $[g, g'] := g g' g^{-1} (g')^{-1}$.

**Lemma 2.1 (Single-Overlap Commutator Lemma).** *If $g, g' \in \mathrm{Sym}_n$ satisfy $\mathrm{supp}(g) \cap \mathrm{supp}(g') = \{a\}$ for a single element $a \in \Omega$, then $[g, g']$ is the $3$-cycle $(a\ g(a)\ g'(a))$.*

*Proof.* Set $\Delta := \mathrm{supp}(g)$ and $\Delta' := \mathrm{supp}(g')$. Since $a \in \Delta$, both $g(a)$ and $g^{-1}(a)$ lie in $\Delta \setminus \{a\}$, so neither belongs to $\Delta'$ and both are fixed by $g'$ and $(g')^{-1}$. Likewise, $g'(a)$ and $(g')^{-1}(a)$ lie in $\Delta' \setminus \{a\}$, so neither belongs to $\Delta$ and both are fixed by $g$ and $g^{-1}$. In particular, $a \in \Delta \cap \Delta'$, $g(a) \in \Delta \setminus \Delta'$, and $g'(a) \in \Delta' \setminus \Delta$ are pairwise distinct. Evaluating $c := g g' g^{-1} (g')^{-1}$ (right-to-left) on every $x \in \Omega$:
1. $c(a) = g(g'(g^{-1}((g')^{-1}(a)))) = g(g'((g')^{-1}(a))) = g(a)$.
2. $c(g(a)) = g(g'(g^{-1}(g(a)))) = g(g'(a)) = g'(a)$.
3. $c(g'(a)) = g(g'(g^{-1}(a))) = g(g^{-1}(a)) = a$.
4. If $x \in \Delta' \setminus \{a, g'(a)\}$, then $y := (g')^{-1}(x) \in \Delta' \setminus \{a\}$ lies outside $\Delta$, so $g^{-1}(y) = y$, $g'(y) = x \notin \Delta$, and $g(x) = x$, giving $c(x) = x$.
5. If $x \in \Delta \setminus \{a, g(a)\}$, then $x \notin \Delta'$, so $(g')^{-1}(x) = x$; then $y := g^{-1}(x) \in \Delta \setminus \{a\}$ lies outside $\Delta'$, so $g'(y) = y$ and $g(y) = x$, giving $c(x) = x$.
6. If $x \notin \Delta \cup \Delta'$, then $x$ is fixed by $g, g^{-1}, g', (g')^{-1}$, so $c(x) = x$.

Thus $[g, g'] = (a\ g(a)\ g'(a))$. $\square$

**Lemma 2.2.** *Let $G \le \mathrm{Sym}_n$ ($n \ge 4$) be a $2$-transitive permutation group. If $G$ contains a $3$-cycle, then $\mathrm{Alt}_n \le G$.*

*Proof.* We first observe that if $M_1, M_2 \subseteq \Omega$ satisfy $|M_1| \ge 3$, $|M_2| \ge 3$, $\mathrm{Alt}(M_1) \le G$, $\mathrm{Alt}(M_2) \le G$, and $|M_1 \cap M_2| \ge 2$, then $\mathrm{Alt}(M_1 \cup M_2) \le G$. Indeed, pick distinct $a, b \in M_1 \cap M_2$ and set $S := M_1 \cup M_2$ and $K := \langle (a\ b\ z) : z \in S \setminus \{a, b\} \rangle$. Since every $z \in S \setminus \{a, b\}$ lies in $M_1$ or $M_2$, each $(a\ b\ z)$ lies in $\mathrm{Alt}(M_1) \cup \mathrm{Alt}(M_2) \subseteq G$, so $K \le G$. Moreover, $K$ contains every $3$-cycle on $S$:
- $(a\ b\ z)$ and $(a\ z\ b) = (a\ b\ z)^{-1}$ for all $z \in S \setminus \{a, b\}$;
- $(a\ z_2\ z_1) = (a\ b\ z_1)(a\ b\ z_2)^{-1}$ and $(b\ z_2\ z_1) = (a\ b\ z_1)^{-1}(a\ b\ z_2)$ for all distinct $z_1, z_2 \in S \setminus \{a, b\}$;
- $(x\ z\ y) = (a\ x\ y)^{-1}(a\ y\ z)(a\ x\ y)$ for all distinct $x, y, z \in S \setminus \{a, b\}$.

Since $\mathrm{Alt}(S)$ is generated by all $3$-cycles on $S$, we obtain $\mathrm{Alt}(S) \le K \le G$.

Now let $M \subseteq \Omega$ be a subset of maximum cardinality such that $\mathrm{Alt}(M) \le G$. Because $G$ contains a $3$-cycle, $|M| \ge 3$. Suppose for contradiction that $|M| < n$. Choose distinct $a, d \in M$ and any $c \in \Omega \setminus M$. Since $G$ is $2$-transitive, there exists $g \in G$ such that $g(a) = a$ and $g(d) = c$. Set $M' := g(M)$; then $\mathrm{Alt}(M') = g\mathrm{Alt}(M)g^{-1} \le G$, $|M'| = |M| \ge 3$, $a \in M \cap M'$, and $c \in M' \setminus M$.
- If $|M \cap M'| \ge 2$, the observation above gives $\mathrm{Alt}(M \cup M') \le G$ with $|M \cup M'| > |M|$, contradicting the maximality of $|M|$.
- If $|M \cap M'| = 1$, then $M \cap M' = \{a\}$. Since $|M| = |M'| \ge 3$, choose distinct $x, x' \in M \setminus \{a\}$ and distinct $y, y' \in M' \setminus \{a\}$. Then $\tau := (a\ x\ x') \in \mathrm{Alt}(M) \le G$ and $\sigma := (a\ y\ y') \in \mathrm{Alt}(M') \le G$ satisfy $\mathrm{supp}(\tau) \cap \mathrm{supp}(\sigma) = \{a\}$, so Lemma 2.1 gives $[\tau, \sigma] = (a\ x\ y) \in G$. Hence $\mathrm{Alt}(\{a, x, y\}) \le G$; applying the observation above to $M$ and $\{a, x, y\}$ (which intersect in $\{a, x\}$ of size $2$) yields $\mathrm{Alt}(M \cup \{y\}) \le G$ with $y \notin M$, again contradicting the maximality of $|M|$.

Therefore $|M| = n$, i.e., $\mathrm{Alt}_n \le G$. $\square$

**Lemma 2.3 (Second-Moment Minimal-Degree Bound).** *Let $G \le \mathrm{Sym}_n$ ($n \ge 4$) be a $2$-transitive permutation group containing a non-identity element $g \in G \setminus \{1\}$ with support size $s := |\mathrm{supp}(g)|$. If $(s - 1)^2 + 1 < n$, then $\mathrm{Alt}_n \le G$.*

*Proof.* Suppose for contradiction that $\mathrm{Alt}_n \not\le G$. Put $\Delta := \mathrm{supp}(g)$ (so $|\Delta| = s \ge 2$), and for each $h \in G$ define $X(h) := |\Delta \cap h(\Delta)| = |\mathrm{supp}(g) \cap \mathrm{supp}(h g h^{-1})| \in \mathbb{Z}_{\ge 0}$. By Lemmas 2.1 and 2.2, $G$ contains no $3$-cycle, so $X(h) \neq 1$ for every $h \in G$. Because every integer $X \in \mathbb{Z}_{\ge 0} \setminus \{1\}$ satisfies $X(X - 2) \ge 0$, averaging over $h \in G$ uniformly yields
$$\mathbb{E}[X(X - 1)] - \mathbb{E}[X] = \mathbb{E}[X(X - 2)] \ge 0.$$
Because $G$ is transitive on $\Omega$, for each $x \in \Delta$ the event $x \in h(\Delta)$ (equivalently $h^{-1}(x) \in \Delta$) holds for exactly a fraction $s/n$ of elements $h \in G$; hence $\mathbb{E}[X] = s \cdot (s/n) = s^2/n$. Because $G$ is $2$-transitive on $\Omega$, for each ordered pair $(x, y)$ of distinct elements of $\Delta$, the event $\{h^{-1}(x), h^{-1}(y)\} \subseteq \Delta$ holds for exactly a fraction $\frac{s(s-1)}{n(n-1)}$ of elements $h \in G$; hence
$$\mathbb{E}[X(X - 1)] = s(s - 1) \cdot \frac{s(s - 1)}{n(n - 1)} = \frac{s^2(s - 1)^2}{n(n - 1)}.$$
Therefore
$$0 \le \frac{s^2(s - 1)^2}{n(n - 1)} - \frac{s^2}{n} = \frac{s^2}{n}\left(\frac{(s - 1)^2}{n - 1} - 1\right),$$
so $(s - 1)^2 \ge n - 1$, i.e., $n \le (s - 1)^2 + 1$, contradicting the hypothesis. $\square$

*(Remark: Lemma 2.3 is a short self-contained $\sqrt{n}$-analogue of Bochert's classical minimal-degree theorem, A. Bochert, Math. Ann. 40 (1892), 176–193; H. Wielandt, Finite Permutation Groups, 1964, §15.)*

---

## Section 3: Proof of Attainment of Equality (Lower Bound)

Fix an arbitrary integer $k \ge 2$. Set
$$Q := 4 \prod_{\substack{3 \le q \le k + 1 \\ q \text{ prime}}} q.$$
For each odd prime $q \le k + 1$, the set $\{0 \bmod q,\ k \bmod q\}$ omits at least $q - 2 \ge 1$ residue classes modulo $q$; pick one such residue $r_q \in \mathbb{Z}/q\mathbb{Z}$ with $r_q \not\equiv 0 \pmod q$ and $r_q \not\equiv k \pmod q$. By the Chinese Remainder Theorem, there exists an integer $R$ satisfying
$$R \equiv 3 \pmod 4, \qquad R \equiv r_q \pmod q \quad \text{for every odd prime } q \le k + 1.$$
Since $R$ is odd and $q \nmid R$ for every odd prime $q \le k + 1$, we have $\gcd(R, Q) = 1$. By Dirichlet's theorem on primes in arithmetic progressions (P. G. L. Dirichlet, 1837), there exists a prime $n \equiv R \pmod Q$ such that
$$n > k^2 + 2.$$
Notice that $n > k^2 + 2 \ge 2k + 1$ for all $k \ge 2$ (as $(k - 1)^2 = k^2 - 2k + 1 \ge 1 > 0$), so $n - (k + 1) > k$. Define the target index set
$$M_k(n) := \begin{cases} \{n - a : a \in \{1, 2, \ldots, k + 1\}\} & \text{if } k \text{ is even}, \\ \{n - a : a \in \{1, 3, 5, \ldots, k\}\} & \text{if } k \text{ is odd}. \end{cases}$$
Every $m \in M_k(n)$ satisfies $k < m < n$, and $|M_k(n)|$ equals $k + 1$ if $k$ is even and $\frac{k + 1}{2}$ if $k$ is odd.

Put $b := n - k$. For every odd prime $q \le k + 1$, $b = n - k \equiv r_q - k \not\equiv 0 \pmod q$, so no odd prime $q \le k + 1$ divides $b$. Moreover, when $k$ is even, $n$ is odd and $k$ is even, so $b$ is odd and $2 \nmid b$ as well. Consequently:
- If $k$ is even, every $a \in \{1, 2, \ldots, k + 1\}$ has all its prime divisors $\le k + 1$, so $\gcd(a, b) = 1$.
- If $k$ is odd, every $a \in \{1, 3, \ldots, k\}$ is odd with all its prime divisors $\le k < k + 1$, so $\gcd(a, b) = 1$.

Thus $\gcd(a, b) = 1$ holds for every $m = n - a \in M_k(n)$.

**Proposition 3.1 (Transitivity).** *For every $m = n - a \in M_k(n)$, the subgroup $G := \langle r_n, r_m, r_k \rangle \le \mathrm{Sym}_n$ acts transitively on $\Omega = \{1, \ldots, n\}$.*

*Proof.* First consider the product $r_m r_n \in G$. For every $y \in \{a + 1, \ldots, n\}$, we have $r_n(y) = n + 1 - y \in \{1, \ldots, n - a\} = \{1, \ldots, m\}$, and therefore
$$(r_m r_n)(y) = r_m(n + 1 - y) = m + 1 - (n + 1 - y) = y - (n - m) = y - a.$$
Applying $r_m r_n$ repeatedly reduces any $y \in \Omega$ to its unique representative in $\{1, \ldots, a\}$ congruent to $y \pmod a$. Hence any two elements of $\Omega$ congruent modulo $a$ lie in the same $G$-orbit, so every $G$-orbit is a union of residue classes modulo $a$. Write $\overline{x} \in \mathbb{Z}/a\mathbb{Z}$ for the residue class of $x \bmod a$, and write $\overline{x} \sim_G \overline{y}$ if the corresponding subsets of $\Omega$ lie in the same $G$-orbit.

Next consider the product $r_n r_k \in G$. For every $x \in \{1, \ldots, k\}$, we have $r_k(x) = k + 1 - x \in \{1, \ldots, k\}$, and therefore
$$(r_n r_k)(x) = r_n(k + 1 - x) = n + 1 - (k + 1 - x) = x + (n - k) = x + b \in \Omega.$$
Thus $\overline{x} \sim_G \overline{x + b}$ holds for every $x \in \{1, \ldots, k\}$.
- If $1 \le a \le k$, then $\{1, \ldots, k\}$ represents every class in $\mathbb{Z}/a\mathbb{Z}$, so $\overline{x} \sim_G \overline{x + b}$ for all $\overline{x} \in \mathbb{Z}/a\mathbb{Z}$. Since $\gcd(a, b) = 1$, addition of $b$ acts transitively on $\mathbb{Z}/a\mathbb{Z}$, so all $a$ residue classes lie in a single $G$-orbit.
- If $a = k + 1$ (which occurs only when $k$ is even), then $\{1, \ldots, k\}$ represents every nonzero class in $(\mathbb{Z}/a\mathbb{Z}) \setminus \{\overline{0}\}$. Since $\gcd(a, b) = 1$, the classes $\overline{b}, \overline{2b}, \ldots, \overline{(a - 1)b}$ are precisely the $a - 1$ distinct nonzero residue classes in $\mathbb{Z}/a\mathbb{Z}$, and $\overline{ab} = \overline{0}$. Applying $\overline{x} \sim_G \overline{x + b}$ sequentially to $\overline{x} = \overline{jb}$ for $j = 1, 2, \ldots, a - 1$ yields
  $$\overline{b} \sim_G \overline{2b} \sim_G \cdots \sim_G \overline{(a - 1)b} \sim_G \overline{ab} = \overline{0},$$
  joining all $a$ residue classes into a single $G$-orbit.

In both cases $G$ has a single orbit on $\Omega$, so $G$ is transitive. $\square$

**Theorem 3.2 (Lower Bound).** *For the prime $n$ chosen above, $M_k(n) \subseteq F_k(n)$, and hence*
$$|F_k(n)| \ge \begin{cases} k + 1 & \text{if } k \text{ is even}, \\ \frac{k + 1}{2} & \text{if } k \text{ is odd}. \end{cases}$$

*Proof.* Fix any $m = n - a \in M_k(n)$ and set $G := \langle r_n, r_m, r_k \rangle \le \mathrm{Sym}_n$. By Proposition 3.1, $G$ is a transitive permutation group of prime degree $n$.

By Burnside's theorem on transitive permutation groups of prime degree (W. Burnside, *On some properties of groups of odd order*, *Proc. London Math. Soc.* (1) **33** (1901), 162–185; see also J. D. Dixon and B. Mortimer, *Permutation Groups*, GTM 163, Springer, 1996, Theorem 3.5B, and H. Wielandt, *Finite Permutation Groups*, Academic Press, 1964, Theorem 11.7), either $G$ is $2$-transitive on $\Omega$ or $G$ is permutation-isomorphic to a subgroup of the affine group $\mathrm{AGL}_1(n) = \{x \mapsto ux + v : u \in \mathbb{F}_n^*,\, v \in \mathbb{F}_n\}$.

Every non-identity element $x \mapsto ux + v$ of $\mathrm{AGL}_1(n)$ fixes at most one point of $\mathbb{F}_n$ (zero points if $u = 1, v \neq 0$, and the unique solution $x = v/(1 - u)$ if $u \neq 1$). By contrast, $r_k \in G$ is a non-identity permutation (since $k \ge 2$ implies $r_k(1) = k \neq 1$) that fixes all $n - k$ elements of $\{k + 1, \ldots, n\}$; because $n > k^2 + 2 \ge k + 2$, $r_k$ has at least $2$ fixed points. Hence $G$ cannot embed in $\mathrm{AGL}_1(n)$, and therefore $G$ is $2$-transitive on $\Omega$.

The support size of $r_k \in G \setminus \{1\}$ is $s := |\mathrm{supp}(r_k)| = 2\lfloor k/2 \rfloor \le k$. Because $n > k^2 + 2 > (k - 1)^2 + 1 \ge (s - 1)^2 + 1$, Lemma 2.3 implies $\mathrm{Alt}_n \le G$.

Finally, because $n \equiv R \equiv 3 \pmod 4$, the integer $\lfloor n/2 \rfloor = \frac{n - 1}{2}$ is odd, so $r_n$ is a product of an odd number of disjoint transpositions and hence $r_n \in G \setminus \mathrm{Alt}_n$. Since $\mathrm{Alt}_n \le G \le \mathrm{Sym}_n$ and $[\mathrm{Sym}_n : \mathrm{Alt}_n] = 2$, it follows that $G = \mathrm{Sym}_n$, so $m \in F_k(n)$. Thus $M_k(n) \subseteq F_k(n)$, giving $|F_k(n)| \ge |M_k(n)|$. $\square$

---

Combining Proposition 1.2 and Theorem 3.2 yields $\max_{n > k+1} |F_k(n)| = k + 1$ for even $k \ge 2$ and $\max_{n > k+1} |F_k(n)| = \frac{k + 1}{2}$ for odd $k \ge 3$, completing the proof of Conjecture 5. $\blacksquare$

# Negative Answer to Open Questions 2 and 3 of Vereshchagin (`arXiv:2611.30127v1`)

## 1. Problem Statement and Main Results

From Nikolay Vereshchagin, *"How Much Randomness is Needed to Convert MA Protocols to AM Protocols?"*, `arXiv:2611.30127v1` (23 November 2026; conference/ECCC versions CSR 2022 / ECCC TR22-060), Section 6 (`\section{Open questions}`, `main-eng.tex`, lines 774–780) and Section 1 (`main-eng.tex`, lines 101–106, 151–154):

> **Open Question 2.** Can we prove the inclusion $\mathrm{MA}[m, a] \subset \mathrm{AM}[*, p(a)]$ by algebrizing techniques (for some fixed polynomial $p$)?
>
> **Open Question 3.** Can we prove Conjecture 1 by algebrizing techniques?
>
> **Conjecture 1 (`[knop2015]`).** There is a polynomial $p$ such that if there is a heuristic Merlin-Arthur protocol for a language $L$ that on inputs of length $n$ and confidence $\delta$ uses $q(n/\delta)$ random bits ($q$ is a polynomial), then there is a heuristic Arthur-Merlin protocol for $L$ using $p(q(n/\delta))$ random bits.

**Answer: NO to both Open Question 2 and Open Question 3.**

We construct a single Boolean oracle $A : \{0,1\}^* \to \{0,1\}$ whose canonical multilinear extension $\widetilde{A}$ (in the sense of Aaronson and Wigderson `[AW]`, TOCT 2009) separates $\mathrm{MAP}^A[m, a] \subseteq \mathrm{MA}^A[m, a]$ from $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m', a', t']$ whenever $a'(n) \le m(n) - O(\log n)$ for infinitely many $n$, via length-only languages. This refutes algebrization of $\mathrm{MA}[m, a] \subset \mathrm{AM}[*, p(a)]$ (Open Question 2), $\mathrm{MA}[m, a] \subset \mathrm{PP}[p(a)]$, and Knop's Conjecture 1 (Open Question 3) simultaneously.

---

## 2. Preliminaries and Exact Algebrization Framework

Following Vereshchagin (`main-eng.tex`, Section 2, lines 213–320):
- A **polynomial** is a function $p : \mathbb{N} \to \mathbb{N}$ of the form $p(n) = b(n + 1)^c$ with positive integers $b, c \ge 1$. In particular, every polynomial $p$ is strictly increasing and satisfies $p(n) \ge n + 1$ for all $n \ge 0$.
- $\mathrm{MA}^A[m, a]$, $\mathrm{MAP}^A[m, a]$, $\mathrm{AM}^A[m, a]$, $\mathrm{PP}^A[r]$, $\mathrm{PP}\!\cdot\!\mathrm{NP}^A[m, a, t]$, $\mathrm{Heur}\text{-}\mathrm{MA}^A[m, a]$, and $\mathrm{Heur}\text{-}\mathrm{AM}^A[m, a]$ are defined verbatim as in `main-eng.tex` Definitions 1–6 (lines 222–320):
  - $L \in \mathrm{MAP}^A[m, a]$ if there is a polynomial-time oracle TM $V^A(x, y, z)$ with $|y| = m(|x|)$, $|z| = a(|x|)$ such that $x \in L \implies \exists y\,\Pr_z[V^A(x, y, z) = 1] = 1$ and $x \notin L \implies \forall y\,\Pr_z[V^A(x, y, z) = 1] < 1/2$. If moreover the soundness bound is $< 1/3$, then $L \in \mathrm{MAP}^A[m, a] \cap \mathrm{MA}^A[m, a]$.
  - $L \in \mathrm{PP}\!\cdot\!\mathrm{NP}^A[m', a', t']$ if there is an oracle TM $V^A(x, y', r)$ running in time at most $t'(|x|)$ with $|y'| = m'(|x|)$, $|r| = a'(|x|)$ such that for all $x \in \{0,1\}^*$,
    $$x \in L \iff \Pr_{r \in \{0,1\}^{a'(|x|)}}\bigl[\exists y' \in \{0,1\}^{m'(|x|)}\; V^A(x, y', r) = 1\bigr] > \frac{1}{2}.$$
  - $\mathrm{AM}^A[m', a'] \subseteq \mathrm{PP}\!\cdot\!\mathrm{NP}^A[m', a', *]$ and $\mathrm{PP}^A[a'] \subseteq \mathrm{PP}\!\cdot\!\mathrm{NP}^A[*, a', *]$ (ignoring a dummy witness $y' \in \{0,1\}^{n+1}$), where $*$ denotes union over all polynomials.
  - $L \in \mathrm{Heur}\text{-}\mathrm{AM}^A[m', a']$ if there is an oracle TM $V^A(x, y', r, \delta)$ running in time bounded by a polynomial of $|x|/\delta$ such that for every $n \in \mathbb{N}$ and every rational $\delta \in (0, 1]$, on all but at most a $\delta$ fraction of strings $x \in \{0,1\}^n$, both $x \in L \implies \Pr_{r \in \{0,1\}^{a'(n/\delta)}}[\exists y' \in \{0,1\}^{m'(n/\delta)} V^A(x, y', r, \delta) = 1] > 2/3$ and $x \notin L \implies \Pr_r[\exists y' V^A(x, y', r, \delta) = 1] < 1/3$ hold (and analogously for $\mathrm{Heur}\text{-}\mathrm{MA}^A[m, a]$; since $m, a$ are non-decreasing, $\mathrm{MA}^A[m, a] \subseteq \mathrm{Heur}\text{-}\mathrm{MA}^A[m, a]$ by ignoring $\delta$ and unused proof/random bits).

**Aaronson–Wigderson Algebraic Oracle (`[AW]`, Section 2):**
Given a Boolean oracle $A : \{0,1\}^* \to \{0,1\}$ (viewed as $A = \{A_k\}_{k \ge 0}$ with $A_k : \{0,1\}^k \to \{0,1\}$ and $A(\varepsilon) = 0$), its **canonical multilinear extension** $\widetilde{A}$ consists of the unique multilinear polynomials $\widetilde{A}_{k, \mathbb{F}} : \mathbb{F}^k \to \mathbb{F}$ over all finite fields $\mathbb{F}$ (in particular over all prime fields $\mathbb{F}_p$, and more generally over all prime-power fields $\mathbb{F}_q$):
$$\widetilde{A}_{k, \mathbb{F}}(u_1, \dots, u_k) := \sum_{s \in \{0,1\}^k} A_k(s) \prod_{j=1}^k \chi_{s_j}(u_j), \qquad \chi_1(u) := u,\quad \chi_0(u) := 1 - u,$$
with the empty product at $k = 0$ equal to $1$ (so $\widetilde{A}_{0, \mathbb{F}} = A(\varepsilon) = 0$). For every $k \ge 0$ and finite field $\mathbb{F}$, $\widetilde{A}_{k, \mathbb{F}}$ has individual degree at most $1$ in each variable, is linear in the truth table of $A_k$, and satisfies $\widetilde{A}_{k, \mathbb{F}}(s) = A_k(s)$ for all $s \in \{0,1\}^k$. In the `[AW]` query model, an oracle TM $V^{\widetilde{A}}$ running in time $t'(n)$ specifies each query $\langle k', \mathrm{desc}(\mathbb{F}_q), (u_1, \dots, u_{k'}) \rangle$ on its oracle tape and receives $\widetilde{A}_{k', \mathbb{F}_q}(u_1, \dots, u_{k'}) \in \mathbb{F}_q$; in at most $t'(n)$ steps:
1. $V$ makes at most $t'(n)$ oracle queries;
2. every queried length satisfies $k' \le t'(n)$ (as $k'$ coordinates are written on the query tape);
3. every queried finite field $\mathbb{F}_q$ has explicit representation length $\lceil \log_2 q \rceil \le t'(n)$ (in `[AW]` prime fields $\mathbb{F}_p$ have $p$ written in binary, taking $\lfloor \log_2 p \rfloor + 1 \ge \lceil \log_2 p \rceil$ bits, and for general finite fields $\mathbb{F}_q$ the standard explicit field/element encoding has at least $\lceil \log_2 q \rceil$ bits).

An inclusion $\mathcal{C}_1 \subseteq \mathcal{C}_2$ **algebrizes** in the sense of `[AW]` if $\mathcal{C}_1^A \subseteq \mathcal{C}_2^{\widetilde{A}}$ holds for every oracle $A$ and every low-degree extension $\widetilde{A}$ of $A$. Thus exhibiting an oracle $A$ whose canonical multilinear extension $\widetilde{A}$ satisfies $\mathcal{C}_1^A \not\subseteq \mathcal{C}_2^{\widetilde{A}}$ (which also implies $\mathcal{C}_1^{\widetilde{A}} \not\subseteq \mathcal{C}_2^{\widetilde{A}}$ since $A(s) = \widetilde{A}_{|s|, \mathbb{F}_2}(s)$ gives $\mathcal{C}_1^A \subseteq \mathcal{C}_1^{\widetilde{A}}$) proves that $\mathcal{C}_1 \subseteq \mathcal{C}_2$ cannot be proved by algebrizing techniques.

---

## 3. Main Theorems

**Theorem 1 (Algebrization Barrier for $\mathrm{MA}[m, a] \subset \mathrm{PP}\!\cdot\!\mathrm{NP}[*, a']$ — Answers Open Question 2: NO).**
*There exists a Boolean oracle $A : \{0,1\}^* \to \{0,1\}$ with canonical multilinear extension $\widetilde{A}$ such that for every pair of polynomials $(m, a)$, there is a length-only language $L \in \mathrm{MAP}^A[m, a] \cap \mathrm{MA}^A[m, a]$ that does not belong to $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m', a', t']$ for any polynomials $m', a', t'$ satisfying*
$$a'(n) \;\le\; m(n) - \log_2\!\bigl(2(a'(n) + m'(n) + 2 t'(n)^2) + 8\bigr) - 17 \qquad \text{for infinitely many } n.$$
*In particular, for every polynomial $p$, there exist polynomials $m, a$ such that*
$$\mathrm{MAP}^A[m, a] \cap \mathrm{MA}^A[m, a] \;\not\subseteq\; \mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[*, p(a)],$$
*and hence $\mathrm{MA}^A[m, a] \not\subseteq \mathrm{AM}^{\widetilde{A}}[*, p(a)]$ and $\mathrm{MA}^A[m, a] \not\subseteq \mathrm{PP}^{\widetilde{A}}[p(a)]$. Therefore, $\mathrm{MA}[m, a] \subset \mathrm{AM}[*, p(a)]$ cannot be proved by algebrizing techniques.*

**Theorem 2 (Algebrization Barrier for Knop's Conjecture 1 — Answers Open Question 3: NO).**
*For the same oracle $A$ and canonical multilinear extension $\widetilde{A}$ of Theorem 1, for every polynomial $p$, there exist polynomials $m, a$ and a length-only language $L \in \mathrm{MAP}^A[m, a] \subseteq \mathrm{MA}^A[m, a] \subseteq \mathrm{Heur}\text{-}\mathrm{MA}^A[m, a]$ such that $L \notin \mathrm{Heur}\text{-}\mathrm{AM}^{\widetilde{A}}[*, p(a)]$. Therefore, Conjecture 1 cannot be proved by algebrizing techniques.*

---

## 4. Elementary Error-Correcting Code Lemma

### Lemma 4.1 (Gilbert–Varshamov Code via Exact Integer Packing)
For every integer $L \ge 20$, letting $N := \lfloor L / 20 \rfloor \ge 1$ and $r := \lfloor L / 3 \rfloor$, there exists a canonically defined subset $\mathcal{C}_L \subseteq \{0,1\}^L$ of cardinality $|\mathcal{C}_L| = 2^N$ such that every two distinct codewords $c, c' \in \mathcal{C}_L$ have Hamming distance $d_H(c, c') \ge r + 1 > L / 3$.

**Proof.** For any $x \in (0, 1)$,
$$\sum_{j=0}^{r} \binom{L}{j} \;\le\; \sum_{j=0}^{r} \binom{L}{j} x^{j - r} \;\le\; x^{-r} \sum_{j=0}^{L} \binom{L}{j} x^j = x^{-r}(1 + x)^L.$$
Evaluating at $x = 1/2$ gives $\sum_{j=0}^{r} \binom{L}{j} \le 2^r (3/2)^L$. Cubing and using $3r \le L$ and $3N \le 3L/20$:
$$\left(2^N \sum_{j=0}^{r} \binom{L}{j}\right)^3 \;\le\; 2^{3N} \cdot 2^{3r} \cdot \left(\frac{3}{2}\right)^{3L} \;\le\; 2^{3L/20} \cdot 2^L \cdot \frac{27^L}{8^L} = 2^{3L} \cdot \left(\frac{8 \cdot 27^{20}}{32^{20}}\right)^{L/20}.$$
Direct integer arithmetic gives
$$8 \cdot 27^{20} = 339{,}129{,}266{,}201{,}729{,}628{,}114{,}355{,}465{,}608 \;<\; 1{,}267{,}650{,}600{,}228{,}229{,}401{,}496{,}703{,}205{,}376 = 32^{20}.$$
Hence $2^N \sum_{j=0}^{r} \binom{L}{j} < 2^L$. Starting with $\mathcal{C}_L = \emptyset$, at each step while $|\mathcal{C}_L| < 2^N$, the union of closed Hamming balls of radius $r$ around $\mathcal{C}_L$ has size at most $|\mathcal{C}_L| \sum_{j=0}^{r} \binom{L}{j} < 2^L$, so we greedily add the lexicographically smallest string in $\{0,1\}^L$ at Hamming distance $> r$ from all existing codewords. After $2^N$ steps we obtain $\mathcal{C}_L$ of size $2^N$ with pairwise Hamming distance $\ge r + 1 > L / 3$. Fix the order-preserving bijection $\mathrm{Enc}_L : \{0,1\}^N \to \mathcal{C}_L$. $\square$

---

## 5. Main Combinatorial Lemma: Rectangle-Shrinking and Ping-Pong Min-Entropy Restoration

Let $M, N, a', m', C$ be positive integers. Define $\mathrm{OR}_M \circ \mathrm{EQ}_N : (\{0,1\}^N)^M \times (\{0,1\}^N)^M \to \{0,1\}$ by
$$(\mathrm{OR}_M \circ \mathrm{EQ}_N)(X, W) = 1 \iff \exists y \in [M] \text{ such that } X_y = W_y.$$
Pairs with value $1$ are called **YES-instances**, and pairs with value $0$ are called **NO-instances**.

### Lemma 5.1 (No Low-Randomness $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\mathrm{cc}}$ Protocol for $\mathrm{OR}_M \circ \mathrm{EQ}_N$)
Suppose $\{\mathcal{U}_r\}_{r \in \{0,1\}^{a'}}$ is a family of subsets of $(\{0,1\}^N)^M \times (\{0,1\}^N)^M$ such that each $\mathcal{U}_r$ is a union of at most $2^{m' + C}$ combinatorial rectangles $A' \times B'$. Set
$$K := 2^{a' - 1} + 1, \qquad \Delta := 2(a' + m' + C) + 8.$$
Assume the four parameter conditions:
$$(\mathrm{P1})\; N \ge 100, \qquad (\mathrm{P2})\; 100 \Delta \le N, \qquad (\mathrm{P3})\; M \cdot 2^{-89 N / 100} < \frac{1}{4}, \qquad (\mathrm{P4})\; K \cdot \Delta \le 10^{-5} M.$$
Then $\{\mathcal{U}_r\}$ **cannot** decide $\mathrm{OR}_M \circ \mathrm{EQ}_N$ in the $\mathrm{PP}\!\cdot\!\mathrm{NP}$ sense; that is, there exists $(X^*, W^*) \in (\{0,1\}^N)^M \times (\{0,1\}^N)^M$ such that either $(X^*, W^*)$ is a YES-instance belonging to $\mathcal{U}_r$ for at most $2^{a'-1}$ strings $r$, or $(X^*, W^*)$ is a NO-instance belonging to $\mathcal{U}_r$ for at least $K = 2^{a'-1} + 1$ strings $r$.

**Proof.** Suppose for contradiction that every YES-instance belongs to $\mathcal{U}_r$ for at least $K = 2^{a'-1} + 1$ strings $r \in \{0,1\}^{a'}$, while every NO-instance belongs to $\mathcal{U}_r$ for at most $2^{a'-1}$ strings $r \in \{0,1\}^{a'}$.

For any partition $[M] = U \sqcup F$, fixed NO-tuples $x^*_F, w^*_F \in (\{0,1\}^N)^F$ (with $x^*_y \neq w^*_y$ for all $y \in F$), and non-empty subsets $\mathcal{A}, \mathcal{B} \subseteq (\{0,1\}^N)^U$, denote by $\overline{X}' \in (\{0,1\}^N)^M$ (resp. $\overline{W}'$) the extension of $X' \in \mathcal{A}$ by $x^*_F$ (resp. of $W' \in \mathcal{B}$ by $w^*_F$). Define the joint **deficiency**
$$D(\mathcal{A}, \mathcal{B}; U) := \log_2 \frac{2^{|U| N}}{|\mathcal{A}|} + \log_2 \frac{2^{|U| N}}{|\mathcal{B}|} \;\ge\; 0.$$
We say that a non-empty subset $\mathcal{S} \subseteq (\{0,1\}^N)^U$ is **$\gamma$-block-min-entropy dense** on $U$ if for every non-empty subset $S \subseteq U$ and every $v \in (\{0,1\}^N)^S$,
$$\Pr_{X' \sim \mathcal{S}}[X'_S = v] \;\le\; 2^{-\gamma N |S|},$$
where $X' \sim \mathcal{S}$ denotes the uniform distribution on $\mathcal{S}$.

We construct by induction on $i = 0, 1, \dots, K$ a partition $[M] = U_i \sqcup F_i$, fixed NO-tuples $(x^*_{F_i}, w^*_{F_i})$ ($x^*_y \neq w^*_y$ for all $y \in F_i$), pairwise distinct strings $r_1, \dots, r_i \in \{0,1\}^{a'}$, and non-empty subsets $\mathcal{A}_i, \mathcal{B}_i \subseteq (\{0,1\}^N)^{U_i}$ satisfying:
1. *(Acceptance)* For every $(X', W') \in \mathcal{A}_i \times \mathcal{B}_i$, $(\overline{X}', \overline{W}') \in \bigcap_{t=1}^i \mathcal{U}_{r_t}$.
2. *(Density)* Both $\mathcal{A}_i$ and $\mathcal{B}_i$ are $(0.9)$-block-min-entropy dense on $U_i$.
3. *(Potential)* $D_i + 0.09 N |F_i| \le i \cdot \Delta$, where $D_i := D(\mathcal{A}_i, \mathcal{B}_i; U_i)$.

**Base case ($i = 0$).** Take $U_0 = [M]$, $F_0 = \emptyset$, $\mathcal{A}_0 = \mathcal{B}_0 = (\{0,1\}^N)^M$. Condition (1) is vacuous, (2) holds because $\Pr[X_S = v] = 2^{-N|S|} \le 2^{-0.9 N|S|}$, and (3) holds since $D_0 + 0 = 0$.

**Inductive step ($i \to i + 1$, for $0 \le i < K$).** Assume (1)–(3) hold at step $i$.

*Step A (Selecting an almost-uniform active coordinate $y^* \in U_i$).*
Since $D_i \ge 0$, (3), $(\mathrm{P1})$, and $(\mathrm{P4})$ give
$$|F_i| \le \frac{i \Delta}{0.09 N} < \frac{K \Delta}{9} \le \frac{10^{-5} M}{9} < \frac{M}{2},$$
so $|U_i| = M - |F_i| > M / 2$. Let $p_y$ (resp. $q_y$) denote the marginal distribution of $X'_y$ for $X' \sim \mathcal{A}_i$ (resp. of $W'_y$ for $W' \sim \mathcal{B}_i$), and let $U_N$ be the uniform distribution on $\{0,1\}^N$. By subadditivity of Shannon entropy, $H(X') \le \sum_{y \in U_i} H(X'_y)$, so
$$\sum_{y \in U_i} D_{\mathrm{KL}}(p_y \| U_N) = \sum_{y \in U_i} \bigl(N - H(X'_y)\bigr) \le |U_i| N - H(X') = \log_2 \frac{2^{|U_i| N}}{|\mathcal{A}_i|}.$$
Adding the identical inequality for $W' \sim \mathcal{B}_i$ yields $\sum_{y \in U_i} \bigl(D_{\mathrm{KL}}(p_y \| U_N) + D_{\mathrm{KL}}(q_y \| U_N)\bigr) \le D_i \le K \Delta$. Choose $y^* \in U_i$ minimizing $D_{\mathrm{KL}}(p_{y^*} \| U_N) + D_{\mathrm{KL}}(q_{y^*} \| U_N)$; then by $(\mathrm{P4})$,
$$D_{\mathrm{KL}}(p_{y^*} \| U_N) + D_{\mathrm{KL}}(q_{y^*} \| U_N) \le \frac{D_i}{|U_i|} < \frac{2 K \Delta}{M} \le 2 \cdot 10^{-5}.$$
By Pinsker's inequality (with KL divergence in bits, $\|P - Q\|_1 \le \sqrt{2 (\ln 2)\, D_{\mathrm{KL}}(P \| Q)} < \sqrt{2 D_{\mathrm{KL}}(P \| Q)}$ since $\ln 2 < 1$),
$$\|p_{y^*} - U_N\|_1 < \sqrt{4 \cdot 10^{-5}} < \frac{1}{100}, \qquad \|q_{y^*} - U_N\|_1 < \frac{1}{100}.$$
Define
$$S_{\mathrm{good}} := \Bigl\{u \in \{0,1\}^N : \frac{1}{2} 2^{-N} \le p_{y^*}(u) \le 2 \cdot 2^{-N} \;\text{ and }\; \frac{1}{2} 2^{-N} \le q_{y^*}(u) \le 2 \cdot 2^{-N}\Bigr\}.$$
Every $u \in \{0,1\}^N$ violating the bounds on $p_{y^*}(u)$ satisfies $|p_{y^*}(u) - 2^{-N}| > \frac{1}{2} 2^{-N}$, so fewer than $\frac{1/100}{1/2} 2^N = \frac{1}{50} 2^N$ elements violate the $p_{y^*}$-bounds, and likewise fewer than $\frac{1}{50} 2^N$ violate the $q_{y^*}$-bounds. Hence
$$|S_{\mathrm{good}}| > \left(1 - \frac{2}{50}\right) 2^N = \frac{24}{25} 2^N > \frac{9}{10} 2^N.$$

*Step B (Averaging over new Arthur strings and Cauchy–Schwarz rectangle shrinking).*
Consider the set of good YES-pairs on row $y^*$:
$$\mathcal{Y}_{\mathrm{good}} := \bigl\{(X', W') \in \mathcal{A}_i \times \mathcal{B}_i : X'_{y^*} = W'_{y^*} \in S_{\mathrm{good}}\bigr\}.$$
For each $u \in S_{\mathrm{good}}$, there are $p_{y^*}(u) |\mathcal{A}_i| \ge \frac{1}{2} 2^{-N} |\mathcal{A}_i|$ choices for $X'$ and $q_{y^*}(u) |\mathcal{B}_i| \ge \frac{1}{2} 2^{-N} |\mathcal{B}_i|$ choices for $W'$, so
$$|\mathcal{Y}_{\mathrm{good}}| \ge |S_{\mathrm{good}}| \cdot \frac{1}{4} 2^{-2N} |\mathcal{A}_i| |\mathcal{B}_i| \ge \frac{9}{40} 2^{-N} |\mathcal{A}_i| |\mathcal{B}_i|.$$
For every $(X', W') \in \mathcal{Y}_{\mathrm{good}}$, the extended pair $(\overline{X}', \overline{W}')$ satisfies $\overline{X}'_{y^*} = \overline{W}'_{y^*}$ and is therefore a YES-instance. Hence $(\overline{X}', \overline{W}') \in \mathcal{U}_r$ for at least $K$ strings $r \in \{0,1\}^{a'}$. Since $i < K$, at least $K - i \ge 1$ of these strings lie outside $\{r_1, \dots, r_i\}$.

For each $r \in \{0,1\}^{a'} \setminus \{r_1, \dots, r_i\}$, each of the at most $2^{m' + C}$ combinatorial rectangles $A' \times B' \subseteq \mathcal{U}_r$ restricts on the fixed slice $(x^*_{F_i}, w^*_{F_i})$ to a combinatorial rectangle $A'_{U_i} \times B'_{U_i} \subseteq (\{0,1\}^N)^{U_i} \times (\{0,1\}^N)^{U_i}$, where $A'_{U_i} := \{X' : \overline{X}' \in A'\}$ and $B'_{U_i} := \{W' : \overline{W}' \in B'\}$. Across all $2^{a'} - i \le 2^{a'}$ unused strings $r$, there are at most $2^{a' + m' + C}$ such rectangles, and their union covers $\mathcal{Y}_{\mathrm{good}}$. By averaging, there exist $r_{i+1} \in \{0,1\}^{a'} \setminus \{r_1, \dots, r_i\}$ and a rectangle $A' \times B' \subseteq \mathcal{U}_{r_{i+1}}$ such that, letting $\widetilde{\mathcal{A}} := \mathcal{A}_i \cap A'_{U_i}$ and $\widetilde{\mathcal{B}} := \mathcal{B}_i \cap B'_{U_i}$,
$$Y_{\mathrm{new}} := |(\widetilde{\mathcal{A}} \times \widetilde{\mathcal{B}}) \cap \mathcal{Y}_{\mathrm{good}}| \;\ge\; 2^{-(a' + m' + C)} |\mathcal{Y}_{\mathrm{good}}| \;\ge\; \frac{9}{40} 2^{-(a' + m' + C)} 2^{-N} |\mathcal{A}_i| |\mathcal{B}_i|.$$
On the other hand, writing $a_u := |\{X' \in \widetilde{\mathcal{A}} : X'_{y^*} = u\}|$ and $b_u := |\{W' \in \widetilde{\mathcal{B}} : W'_{y^*} = u\}|$ for $u \in S_{\mathrm{good}}$, we have $a_u \le p_{y^*}(u) |\mathcal{A}_i| \le 2 \cdot 2^{-N} |\mathcal{A}_i|$, $b_u \le 2 \cdot 2^{-N} |\mathcal{B}_i|$, $\sum_{u \in S_{\mathrm{good}}} a_u \le |\widetilde{\mathcal{A}}|$, and $\sum_{u \in S_{\mathrm{good}}} b_u \le |\widetilde{\mathcal{B}}|$. Applying the Cauchy–Schwarz inequality:
$$\begin{aligned}
Y_{\mathrm{new}} = \sum_{u \in S_{\mathrm{good}}} a_u b_u
&\le \left(\sum_{u \in S_{\mathrm{good}}} a_u^2\right)^{1/2} \left(\sum_{u \in S_{\mathrm{good}}} b_u^2\right)^{1/2} \\
&\le \left(2 \cdot 2^{-N} |\mathcal{A}_i| |\widetilde{\mathcal{A}}|\right)^{1/2} \left(2 \cdot 2^{-N} |\mathcal{B}_i| |\widetilde{\mathcal{B}}|\right)^{1/2}
= 2 \cdot 2^{-N} \sqrt{|\mathcal{A}_i| |\mathcal{B}_i| |\widetilde{\mathcal{A}}| |\widetilde{\mathcal{B}}|}.
\end{aligned}$$
Comparing the lower and upper bounds on $Y_{\mathrm{new}}$, canceling $2^{-N} \sqrt{|\mathcal{A}_i| |\mathcal{B}_i|} > 0$, and using $\frac{9}{80} > \frac{1}{16} = 2^{-4}$ gives
$$\sqrt{\frac{|\widetilde{\mathcal{A}}| |\widetilde{\mathcal{B}}|}{|\mathcal{A}_i| |\mathcal{B}_i|}} \ge \frac{9}{80} 2^{-(a' + m' + C)} > 2^{-(a' + m' + C) - 4},$$
and squaring yields
$$\frac{|\widetilde{\mathcal{A}}| |\widetilde{\mathcal{B}}|}{|\mathcal{A}_i| |\mathcal{B}_i|} > 2^{-2(a' + m' + C) - 8} = 2^{-\Delta}.$$
Consequently:
- $D(\widetilde{\mathcal{A}}, \widetilde{\mathcal{B}}; U_i) < D_i + \Delta$, so $D(\widetilde{\mathcal{A}}, \widetilde{\mathcal{B}}; U_i) + 0.09 N |F_i| < (i + 1)\Delta$;
- Since $|\widetilde{\mathcal{A}}| \le |\mathcal{A}_i|$ and $|\widetilde{\mathcal{B}}| \le |\mathcal{B}_i|$, we have $|\widetilde{\mathcal{A}}| > 2^{-\Delta} |\mathcal{A}_i|$ and $|\widetilde{\mathcal{B}}| > 2^{-\Delta} |\mathcal{B}_i|$;
- For every non-empty $S \subseteq U_i$ and $v \in (\{0,1\}^N)^S$, using (2) and $(\mathrm{P2})$ ($\Delta \le 0.01 N \le 0.01 N |S|$),
  $$\Pr_{X' \sim \widetilde{\mathcal{A}}}[X'_S = v] \le \frac{|\{X' \in \mathcal{A}_i : X'_S = v\}|}{2^{-\Delta} |\mathcal{A}_i|} \le 2^{\Delta - 0.9 N |S|} \le 2^{-0.89 N |S|},$$
  and identically for $\widetilde{\mathcal{B}}$. Thus **both** $\widetilde{\mathcal{A}}$ and $\widetilde{\mathcal{B}}$ are $(0.89)$-block-min-entropy dense on $U_i$, and every $(X', W') \in \widetilde{\mathcal{A}} \times \widetilde{\mathcal{B}}$ satisfies $(\overline{X}', \overline{W}') \in \bigcap_{t=1}^{i+1} \mathcal{U}_{r_t}$.

*Step C (Ping-Pong $(0.9)$-Block-Min-Entropy Restoration).*
Initialize $(\mathcal{A}, \mathcal{B}, U, F) := (\widetilde{\mathcal{A}}, \widetilde{\mathcal{B}}, U_i, F_i)$ with the existing fixed NO-tuples on $F_i$. We maintain the **loop invariant** that:
- $(\mathrm{L1})$ Every $(X', W') \in \mathcal{A} \times \mathcal{B}$ extends to $\bigcap_{t=1}^{i+1} \mathcal{U}_{r_t}$, and $x^*_y \neq w^*_y$ for all $y \in F$;
- $(\mathrm{L2})$ $D(\mathcal{A}, \mathcal{B}; U) + 0.09 N |F| < (i + 1)\Delta$;
- $(\mathrm{L3})$ For each side in $\{\mathcal{A}, \mathcal{B}\}$, if it violates $(0.9)$-block-min-entropy density on $U$, then the *other* side is $(0.89)$-block-min-entropy dense on $U$.

*(Initialization satisfies $(\mathrm{L1})$–$(\mathrm{L3})$ because both $\widetilde{\mathcal{A}}$ and $\widetilde{\mathcal{B}}$ are $(0.89)$-dense on $U_i$.)*

While at least one of $\mathcal{A}, \mathcal{B}$ fails to be $(0.9)$-block-min-entropy dense on $U$:
- By symmetry between Alice and Bob, assume without loss of generality that $\mathcal{A}$ fails $(0.9)$-density on $U$; by $(\mathrm{L3})$, $\mathcal{B}$ is $(0.89)$-dense on $U$.
- Choose a non-empty subset $S \subseteq U$ of **maximum cardinality** for which there exists $v \in (\{0,1\}^N)^S$ with $\Pr_{X' \sim \mathcal{A}}[X'_S = v] > 2^{-0.9 N |S|}$. Note that $S \subsetneq U$ strictly: if $S = U$, then $\Pr_{\mathcal{A}}[X'_U = v] = 1 / |\mathcal{A}| > 2^{-0.9 N |U|}$ would force $\log_2(2^{|U|N}/|\mathcal{A}|) > 0.1 N |U|$, giving $D(\mathcal{A}, \mathcal{B}; U) + 0.09 N |F| > 0.1 N |U| + 0.09 N |F| \ge 0.09 N M \ge 9 M > 10^{-5} M \ge K \Delta \ge (i+1)\Delta$, contradicting $(\mathrm{L2})$. Hence $U' := U \setminus S$ is non-empty.
- Set $F' := F \sqcup S$ and $\mathcal{A}' := \{X'|_{U'} : X' \in \mathcal{A},\; X'_S = v\} \subseteq (\{0,1\}^N)^{U'}$. Since the restriction $X' \mapsto X'|_{U'}$ is a bijection on the fiber $\{X' \in \mathcal{A} : X'_S = v\}$, we have $|\mathcal{A}'| = \Pr_{\mathcal{A}}[X'_S = v] |\mathcal{A}| \ge 1$ (so $\mathcal{A}'$ is non-empty).
  - *Alice's density is restored to $(0.9)$:* For any non-empty $T \subseteq U'$ and any $u \in (\{0,1\}^N)^T$, maximality of $|S|$ implies $\Pr_{\mathcal{A}}[X'_S = v \text{ and } X'_T = u] \le 2^{-0.9 N(|S| + |T|)}$, so
    $$\Pr_{\mathcal{A}'}[X'_T = u] = \frac{\Pr_{\mathcal{A}}[X'_S = v \text{ and } X'_T = u]}{\Pr_{\mathcal{A}}[X'_S = v]} < \frac{2^{-0.9 N(|S| + |T|)}}{2^{-0.9 N |S|}} = 2^{-0.9 N |T|}.$$
    Hence $\mathcal{A}'$ is $(0.9)$-dense (and a fortiori $(0.89)$-dense) on $U'$.
  - *Alice's deficiency drops:*
    $$\log_2 \frac{2^{|U'| N}}{|\mathcal{A}'|} - \log_2 \frac{2^{|U| N}}{|\mathcal{A}|} = -|S| N + \log_2 \frac{1}{\Pr_{\mathcal{A}}[X'_S = v]} < -|S| N + 0.9 N |S| = -0.1 N |S|.$$
- *Bob freezes $S$ to a NO-tuple:* Since $\mathcal{B}$ is $(0.89)$-dense on $U$, for each $y \in S$ we have $\Pr_{W' \sim \mathcal{B}}[W'_y = v_y] \le 2^{-0.89 N}$. By the union bound and $(\mathrm{P3})$,
  $$\Pr_{W' \sim \mathcal{B}}[\exists y \in S : W'_y = v_y] \le |S| \cdot 2^{-0.89 N} \le M \cdot 2^{-0.89 N} < \frac{1}{4} < \frac{1}{2}.$$
  Thus $\mathcal{B}_{\mathrm{ok}} := \{W' \in \mathcal{B} : \forall y \in S,\; W'_y \neq v_y\}$ has size $|\mathcal{B}_{\mathrm{ok}}| > \frac{1}{2} |\mathcal{B}|$. The projection $W' \mapsto W'_S$ partitions $\mathcal{B}_{\mathrm{ok}}$ into fibers indexed by $\Omega_S := \{w \in (\{0,1\}^N)^S : \forall y \in S,\; w_y \neq v_y\}$, which has cardinality $(2^N - 1)^{|S|} < 2^{|S| N}$. By averaging, there exists $w^* \in \Omega_S$ such that $\mathcal{B}' := \{W'|_{U'} : W' \in \mathcal{B},\; W'_S = w^*\}$ (in bijection with the fiber $\{W' \in \mathcal{B} : W'_S = w^*\}$) satisfies
  $$|\mathcal{B}'| > \frac{\frac{1}{2} |\mathcal{B}|}{2^{|S| N}} = 2^{-|S| N - 1} |\mathcal{B}| > 0,$$
  so $\mathcal{B}'$ is non-empty. Freeze $x^*_S := v$ and $w^*_S := w^*$ (so $x^*_y \neq w^*_y$ for every $y \in S$). Bob's deficiency increases by
  $$\log_2 \frac{2^{|U'| N}}{|\mathcal{B}'|} - \log_2 \frac{2^{|U| N}}{|\mathcal{B}|} = -|S| N + \log_2 \frac{|\mathcal{B}|}{|\mathcal{B}'|} < 1.$$
- *Potential strictly decreases:* Combining Alice's drop, Bob's increase, and the freezing cost $0.09 N |S|$, using $(\mathrm{P1})$ ($N \ge 100$) and $|S| \ge 1$:
  $$\bigl(D(\mathcal{A}', \mathcal{B}'; U') + 0.09 N |F'|\bigr) - \bigl(D(\mathcal{A}, \mathcal{B}; U) + 0.09 N |F|\bigr) < -0.1 N |S| + 1 + 0.09 N |S| = -0.01 N |S| + 1 \le 0.$$
- Update $(\mathcal{A}, \mathcal{B}, U, F) \leftarrow (\mathcal{A}', \mathcal{B}', U', F')$. Since $\mathcal{A}'$ is $(0.9)$-dense (hence $(0.89)$-dense) on $U'$, if the loop continues then $\mathcal{B}'$ is the sole violating side while its other side $\mathcal{A}'$ is $(0.89)$-dense, preserving $(\mathrm{L3})$; $(\mathrm{L1})$ and $(\mathrm{L2})$ are preserved as well.

Because $|U|$ decreases by $|S| \ge 1$ in every iteration (and remains non-empty since $(\mathrm{L2})$ forces $|F| < K \Delta / (0.09 N) < M/2$), the loop terminates in at most $M$ iterations with $(\mathcal{A}_{i+1}, \mathcal{B}_{i+1}, U_{i+1}, F_{i+1})$ satisfying Invariants (1)–(3) at step $i + 1$.

**Final contradiction at $i = K$.**
Consider the non-empty rectangle $\mathcal{A}_K \times \mathcal{B}_K$ and draw $(X', W')$ uniformly from $\mathcal{A}_K \times \mathcal{B}_K$ (so $X'$ and $W'$ are independent).
- For every $y \in F_K$, $\overline{X}'_y = x^*_y \neq w^*_y = \overline{W}'_y$ deterministically.
- For every $y \in U_K$, conditioning on $W'_y = u$ and using $(0.9)$-density of $\mathcal{A}_K$ at $S = \{y\}$ gives $\Pr[X'_y = W'_y] \le \max_u \Pr_{\mathcal{A}_K}[X'_y = u] \le 2^{-0.9 N}$.
- By the union bound and $(\mathrm{P3})$,
  $$\Pr_{(X', W') \sim \mathcal{A}_K \times \mathcal{B}_K}[\exists y \in [M] : \overline{X}'_y = \overline{W}'_y] \le |U_K| \cdot 2^{-0.9 N} \le M \cdot 2^{-0.89 N} < \frac{1}{4} < 1.$$
Therefore $\mathcal{A}_K \times \mathcal{B}_K$ contains a **NO-instance** $(\overline{X}', \overline{W}')$ belonging to $\bigcap_{t=1}^K \mathcal{U}_{r_t}$, i.e., accepted on at least $K = 2^{a'-1} + 1 > 2^{a'-1}$ strings $r \in \{0,1\}^{a'}$, contradicting soundness of $\{\mathcal{U}_r\}$. $\square$

---

## 6. Proof of Theorem 1 (Oracle Construction, 2-Party Simulation, and Diagonalization)

### 6.1 Oracle Layout and Languages $L_i(A)$

Enumerate all pairs of polynomials $(m_1, a_1), (m_2, a_2), \dots$. For each $i \ge 1$, let $\hat{i} \in \{0,1\}^*$ be its prefix-free encoding obtained by doubling each bit of the binary expansion of $i$ and appending `01` (so $|\hat{i}| = 2\lfloor \log_2 i \rfloor + 4$, and $\hat{i}$ is never a prefix of $\hat{j}$ for $i \neq j$). For each $i \ge 1$ and $n \in \mathbb{N}$, define:
$$\ell_i(n) := \lfloor a_i(n) / 3 \rfloor, \qquad L_i(n) := 2^{\ell_i(n)}, \qquad N_i(n) := \lfloor L_i(n) / 20 \rfloor, \qquad M_i(n) := 2^{m_i(n)},$$
$$k_i(n) := |\hat{i}| + 1 + m_i(n) + \ell_i(n), \qquad n_0(i) := \min\{n \in \mathbb{N} : \ell_i(n) \ge 11\}.$$
Because $a_i(n) \ge n + 1$, $n_0(i) \le 32$ is finite, and for every $n \ge n_0(i)$ we have $L_i(n) \ge 2^{11} = 2048$ and $N_i(n) \ge 102 \ge 100$, so Lemma 4.1 provides the canonical code $\mathrm{Enc}_{L_i(n)} : \{0,1\}^{N_i(n)} \to \mathcal{C}_{L_i(n)} \subseteq \{0,1\}^{L_i(n)}$ with pairwise Hamming distance $> L_i(n) / 3$.

For each $i \ge 1$ and $n \ge n_0(i)$, define the **block** of oracle addresses
$$\mathcal{D}_{i, n} := \bigl\{\hat{i}\, b\, y\, z : b \in \{0,1\},\; y \in \{0,1\}^{m_i(n)},\; z \in \{0,1\}^{\ell_i(n)}\bigr\} \subseteq \{0,1\}^{k_i(n)}.$$
Notice that the blocks $\{\mathcal{D}_{i, n} : i \ge 1,\; n \ge n_0(i)\}$ are **pairwise disjoint**: for $i \neq j$, prefix-freeness of $\hat{i}, \hat{j}$ separates them; for $i = j$ and $n \neq n'$, strict monotonicity of $m_i(n)$ and monotonicity of $\ell_i(n)$ imply $k_i(n) \neq k_i(n')$.

Our oracle $A : \{0,1\}^* \to \{0,1\}$ will satisfy the **encoding invariant** that on every block $\mathcal{D}_{i, n}$ ($i \ge 1, n \ge n_0(i)$), there exist $X^{(i, n)}, W^{(i, n)} \in (\{0,1\}^{N_i(n)})^{M_i(n)}$ such that
$$A(\hat{i}\, 0\, y\, z) = \mathrm{Enc}_{L_i(n)}(X^{(i, n)}_y)[z], \qquad A(\hat{i}\, 1\, y\, z) = \mathrm{Enc}_{L_i(n)}(W^{(i, n)}_y)[z] \qquad \forall\, y \in \{0,1\}^{m_i(n)},\; z \in \{0,1\}^{\ell_i(n)},$$
and $A(s) = 0$ for all strings $s \notin \bigcup_{i \ge 1,\, n \ge n_0(i)} \mathcal{D}_{i, n}$.

For each $i \ge 1$, define the **length-only** language
$$L_i(A) := \bigl\{x \in \{0,1\}^* : |x| \ge n_0(i) \text{ and } (\mathrm{OR}_{M_i(|x|)} \circ \mathrm{EQ}_{N_i(|x|)})(X^{(i, |x|)}, W^{(i, |x|)}) = 1\bigr\}.$$

### Lemma 6.1 (Membership in $\mathrm{MAP}^A[m_i, a_i] \cap \mathrm{MA}^A[m_i, a_i]$)
For every oracle $A$ satisfying the encoding invariant and every $i \ge 1$, $L_i(A) \in \mathrm{MAP}^A[m_i, a_i] \cap \mathrm{MA}^A[m_i, a_i]$.

**Proof.** Fix $i \ge 1$. On input $(x, y, z)$ with $|x| = n$, $|y| = m_i(n)$, $|z| = a_i(n)$, the verifier $V_i^A$ proceeds as follows:
- If $n < n_0(i)$, reject immediately (output $0$).
- If $n \ge n_0(i)$, parse the first $3\ell_i(n) \le a_i(n)$ bits of $z$ as three independent uniform strings $(z_1, z_2, z_3) \in (\{0,1\}^{\ell_i(n)})^3$, make the $6$ queries $A(\hat{i}\, 0\, y\, z_t)$ and $A(\hat{i}\, 1\, y\, z_t)$ for $t = 1, 2, 3$, and accept iff $A(\hat{i}\, 0\, y\, z_t) = A(\hat{i}\, 1\, y\, z_t)$ for all $t \in \{1, 2, 3\}$.

Clearly $V_i^A$ runs in polynomial time in $n$.
- If $x \in L_i(A)$, then $n \ge n_0(i)$ and there exists $y \in \{0,1\}^{m_i(n)}$ with $X^{(i, n)}_y = W^{(i, n)}_y$, hence $\mathrm{Enc}_{L_i(n)}(X^{(i, n)}_y)[z_t] = \mathrm{Enc}_{L_i(n)}(W^{(i, n)}_y)[z_t]$ for all $z_t$; thus $V_i^A$ accepts with probability $1$.
- If $x \notin L_i(A)$, then either $n < n_0(i)$ (acceptance probability $0$) or $n \ge n_0(i)$ and for every $y \in \{0,1\}^{m_i(n)}$, $X^{(i, n)}_y \neq W^{(i, n)}_y$. By Lemma 4.1, $\mathrm{Enc}_{L_i(n)}(X^{(i, n)}_y)$ and $\mathrm{Enc}_{L_i(n)}(W^{(i, n)}_y)$ disagree on strictly more than $L_i(n) / 3$ coordinates, so each independent check agrees with probability strictly less than $2/3$. Therefore $V_i^A$ accepts with probability $< (2/3)^3 = 8/27 < 1/3 < 1/2$. $\square$

### 6.2 Two-Party Simulation of $\widetilde{A}$

### Lemma 6.2 (Additive Decomposition and Rectangle Representation)
Fix $i \ge 1$, $n \ge n_0(i)$, and an arbitrary fixed truth table for $A$ on all strings outside $\mathcal{D}_{i, n}$. Suppose $(X, W) \in (\{0,1\}^{N_i(n)})^{M_i(n)} \times (\{0,1\}^{N_i(n)})^{M_i(n)}$ determines $A$ on $\mathcal{D}_{i, n}$, and let $\widetilde{A}$ be the canonical multilinear extension of the resulting oracle $A$. Let $\widehat{V}^{\widetilde{A}}(1^n, y', r)$ be the $t'(n)$-step truncation of a deterministic oracle TM $V$ (simulating $V$ for at most $t'(n)$ steps and outputting $0$ if $V$ has not halted within $t'(n)$ steps). Then for every fixed $(y', r) \in \{0,1\}^{m'(n)} \times \{0,1\}^{a'(n)}$, Alice (holding $X$) and Bob (holding $W$) can deterministically simulate $\widehat{V}^{\widetilde{A}}(1^n, y', r)$ using at most $C := 2 t'(n)^2$ bits of communication. Consequently, for each $r \in \{0,1\}^{a'(n)}$, the set
$$\mathcal{U}_r := \bigl\{(X, W) : \exists y' \in \{0,1\}^{m'(n)}\; \widehat{V}^{\widetilde{A}}(1^n, y', r) = 1\bigr\}$$
is a union of at most $2^{m'(n) + C}$ combinatorial rectangles.

**Proof.** Fix $(y', r)$. Alice and Bob simulate $\widehat{V}^{\widetilde{A}}(1^n, y', r)$ step by step, keeping identical states. Whenever $\widehat{V}$ submits a query $\langle k', \mathrm{desc}(\mathbb{F}_q), \vec{u} \rangle$ with $\vec{u} = (u_1, \dots, u_{k'}) \in \mathbb{F}_q^{k'}$:
- If $k' \neq k_i(n)$, every entry of $A_{k'}$ lies outside $\mathcal{D}_{i, n}$ and is fixed and known to both parties, so both evaluate $\widetilde{A}_{k', \mathbb{F}_q}(\vec{u})$ locally with $0$ bits of communication.
- If $k' = k_i(n)$, partition $\{0,1\}^{k_i(n)}$ into the three disjoint sets
  $$S_A := \{\hat{i}\, 0\, y\, z\},\qquad S_B := \{\hat{i}\, 1\, y\, z\},\qquad S_{\mathrm{fix}} := \{0,1\}^{k_i(n)} \setminus (S_A \cup S_B).$$
  By linearity of the multilinear extension in the truth table of $A_{k_i(n)}$,
  $$\widetilde{A}_{k_i(n), \mathbb{F}_q}(\vec{u}) = \underbrace{\sum_{s \in S_A} A(s)\prod_{j=1}^{k_i(n)} \chi_{s_j}(u_j)}_{f_A(X) \in \mathbb{F}_q} \;+\; \underbrace{\sum_{s \in S_B} A(s)\prod_{j=1}^{k_i(n)} \chi_{s_j}(u_j)}_{f_B(W) \in \mathbb{F}_q} \;+\; \underbrace{\sum_{s \in S_{\mathrm{fix}}} A(s)\prod_{j=1}^{k_i(n)} \chi_{s_j}(u_j)}_{c_{\mathrm{fix}} \in \mathbb{F}_q}.$$
  Alice computes $f_A(X) \in \mathbb{F}_q$ locally, Bob computes $f_B(W) \in \mathbb{F}_q$ locally, and both compute $c_{\mathrm{fix}} \in \mathbb{F}_q$ locally. Alice sends $f_A(X)$ to Bob ($\lceil \log_2 q \rceil$ bits) and Bob sends $f_B(W)$ to Alice ($\lceil \log_2 q \rceil$ bits). Both add $f_A(X) + f_B(W) + c_{\mathrm{fix}}$ in $\mathbb{F}_q$ to obtain the exact oracle response and continue simulating $\widehat{V}$.

Since $\widehat{V}$ runs for at most $t'(n)$ steps, it makes at most $t'(n)$ queries, and every queried field satisfies $\lceil \log_2 q \rceil \le t'(n)$. Hence the total communication is at most $t'(n) \cdot 2 t'(n) = 2 t'(n)^2 = C$ bits. Because the length of each message is determined by the prior transcript, the deterministic protocol tree has depth at most $C$ and hence at most $2^C$ leaves, each corresponding to a combinatorial rectangle. Taking the union over all $2^{m'(n)}$ choices of $y' \in \{0,1\}^{m'(n)}$ shows that $\mathcal{U}_r$ is a union of at most $2^{m'(n) + C}$ combinatorial rectangles. $\square$

### 6.3 Stage-by-Stage Diagonalization

We construct $A$ in stages $s = 1, 2, \dots$, maintaining a strictly increasing integer bound $B_s \in \mathbb{N}$ ($B_0 := 0$) such that after stage $s$, all values of $A$ on strings of length $\le B_s$ are permanently frozen and satisfy the encoding invariant on every block $\mathcal{D}_{j, n'}$ with $k_j(n') \le B_s$.

For every block $\mathcal{D}_{j, n'}$ ($j \ge 1, n' \ge n_0(j)$) not explicitly modified at any stage, define its **default NO-encoding** by setting $X^{(j, n')}_y := 0^{N_j(n')}$ and $W^{(j, n')}_y := 1^{N_j(n')}$ for all $y \in \{0,1\}^{m_j(n')}$ (distinct since $N_j(n') \ge 102$). Outside all blocks $\mathcal{D}_{j, n'}$, set $A(s) := 0$.

Enumerate all 5-tuples $(i, m', a', t', V)$ (a countably infinite subset of $\mathbb{N}^+ \times \mathrm{Poly}^3 \times \mathrm{TM}$) where $i \ge 1$, $m', a', t'$ are polynomials, $V$ is a deterministic oracle TM, and
$$a'(n) \;\le\; m_i(n) - \log_2\!\bigl(2(a'(n) + m'(n) + 2 t'(n)^2) + 8\bigr) - 17 \qquad \text{for infinitely many } n.$$

**Stage $s$ (processing tuple $(i, m', a', t', V)$):**
Let $C(n) := 2 t'(n)^2$ and $\Delta(n) := 2(a'(n) + m'(n) + C(n)) + 8$. Because $a_i(n) \ge n + 1$, we have $N_i(n) = \lfloor 2^{\lfloor a_i(n)/3 \rfloor} / 20 \rfloor = \Omega(2^{n/3})$, whereas $m_i(n), m'(n), a'(n), t'(n), \Delta(n)$ are all bounded by polynomials in $n$. Thus conditions (1)–(3) below hold for all sufficiently large $n$, while (4) holds for infinitely many $n$; pick an integer $n \ge n_0(i)$ satisfying all four:
1. $k_i(n) > B_{s-1}$ (so no string of length $k_i(n)$ has been frozen at any earlier stage);
2. $N_i(n) \ge 100$ (automatic from $n \ge n_0(i)$) and $100 \Delta(n) \le N_i(n)$;
3. $2^{m_i(n)} \cdot 2^{-89 N_i(n) / 100} < 1/4$;
4. $a'(n) \le m_i(n) - \log_2 \Delta(n) - 17$, which (since $K(n) := 2^{a'(n)-1} + 1 \le 2^{a'(n)}$ for $a'(n) \ge 1$ and $2^{17} = 131{,}072 > 10^5$) implies $K(n) \cdot \Delta(n) \le 2^{-17} M_i(n) < 10^{-5} M_i(n)$.

Set $B_s := \max\{k_i(n),\; t'(n)\}$. Temporarily freeze every string of length $\le B_s$ outside $\mathcal{D}_{i, n}$ to its already-frozen value (if length $\le B_{s-1}$) or to its default value (default NO-encoding on untouched blocks $\mathcal{D}_{j, n'}$ with $B_{s-1} < k_j(n') \le B_s$ and $(j, n') \neq (i, n)$, and $0$ outside all blocks), and temporarily fix $A \equiv 0$ on lengths $> B_s$. Let $\widehat{V}$ be the $t'(n)$-step truncation of $V$. Because $\widehat{V}^{\widetilde{A}}(1^n, y', r)$ runs for at most $t'(n) \le B_s$ steps, its queries only access $\widetilde{A}_{k', \mathbb{F}_q}$ for lengths $k' \le B_s$, so its output on $(1^n, y', r)$ is completely independent of $A$ on lengths $> B_s$ and depends solely on $(X, W)$ on block $\mathcal{D}_{i, n}$.

By Lemma 6.2, for each $r \in \{0,1\}^{a'(n)}$, $\mathcal{U}_r = \{(X, W) : \exists y' \in \{0,1\}^{m'(n)}\; \widehat{V}^{\widetilde{A}}(1^n, y', r) = 1\}$ is a union of at most $2^{m'(n) + C(n)}$ combinatorial rectangles. All hypotheses $(\mathrm{P1})$–$(\mathrm{P4})$ of Lemma 5.1 hold for $(M_i(n), N_i(n), a'(n), m'(n), C(n))$, so there exists $(X^*, W^*) \in (\{0,1\}^{N_i(n)})^{M_i(n)} \times (\{0,1\}^{N_i(n)})^{M_i(n)}$ on which $(m', a', \widehat{V})$ errs on input $1^n$ for $L_i(A)$. Set block $\mathcal{D}_{i, n}$ to encode $(X^*, W^*)$, and permanently freeze all strings of length $\le B_s$.

Since $B_s \ge k_i(n) > B_{s-1}$, we have $B_s \to \infty$, so $A$ is completely defined on $\{0,1\}^*$ and satisfies the encoding invariant on every block $\mathcal{D}_{i, n}$. By Lemma 6.1, $L_i(A) \in \mathrm{MAP}^A[m_i, a_i] \cap \mathrm{MA}^A[m_i, a_i]$ for every $i \ge 1$. Moreover, for every tuple $(i, m', a', t', V)$ processed at stage $s$, no later stage modifies any string of length $\le B_s \ge t'(n)$, so on the final oracle $(A, \widetilde{A})$ either $V^{\widetilde{A}}(1^n, y', r)$ exceeds $t'(n)$ steps for some $(y', r)$ (violating the $t'$ time bound) or it halts within $t'(n)$ steps for all $(y', r)$ and agrees identically with $\widehat{V}^{\widetilde{A}}(1^n, y', r)$ (hence errs on $1^n$). In either case, $V$ cannot witness $L_i(A) \in \mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m', a', t']$.

Finally, for any polynomial $p(k) = b(k + 1)^c$ ($b, c \ge 1$), set $a(n) := n + 1$ and $m(n) := (b \cdot 2^c + 1)(n + 1)^{c + 1}$. Then $p(a(n)) = b(n + 2)^c \le b \cdot 2^c (n + 1)^c =: a'(n)$ for all $n \ge 0$ (where $a'$ is a polynomial of the form $b'(n+1)^{c'}$). Any $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m', p(a), t']$ protocol immediately yields a $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m', a', t'']$ protocol (for some polynomial $t''$) by ignoring the extra $a'(n) - p(a(n)) \ge 0$ uniform random bits without changing acceptance probabilities. Since $m(n) - a'(n) \ge (n + 1)^{c + 1} \ge (n + 1)^2$ strictly exceeds $\log_2(2(a'(n) + m'(n) + 2 t''(n)^2) + 8) + 17 = O(\log n)$ for all sufficiently large $n$, we conclude $L_i(A) \in \mathrm{MAP}^A[m, a] \cap \mathrm{MA}^A[m, a] \setminus \mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[*, p(a)]$. This proves Theorem 1. $\square$

---

## 7. Proof of Theorem 2 (Open Question 3: Non-Algebrizability of Knop's Conjecture 1)

Let $(A, \widetilde{A})$ be the oracle pair constructed in Theorem 1, and suppose for contradiction that for some polynomial $p(k) = b(k + 1)^c$ ($b, c \ge 1$), every pair of polynomials $(m, a)$ and every $L \in \mathrm{Heur}\text{-}\mathrm{MA}^A[m, a]$ satisfy $L \in \mathrm{Heur}\text{-}\mathrm{AM}^{\widetilde{A}}[*, p(a)]$.

Choose the polynomials
$$a(n) := n + 1, \qquad m(n) := (b \cdot 12^c + 2)(n + 1)^{c + 1}.$$
Let $L = L_i(A) \in \mathrm{MAP}^A[m, a] \cap \mathrm{MA}^A[m, a] \subseteq \mathrm{Heur}\text{-}\mathrm{MA}^A[m, a]$ be the corresponding length-only language from Theorem 1. By assumption, there exist a polynomial $m'(k) = b_1 (k + 1)^{c_1}$ ($b_1, c_1 \ge 1$) and an oracle TM $V^{\widetilde{A}}(x, y, z, \delta)$ running in time at most $t_V(|x| / \delta)$ (for some polynomial $t_V$) witnessing $L \in \mathrm{Heur}\text{-}\mathrm{AM}^{\widetilde{A}}[m', p \circ a]$.

Specialize to confidence parameter $\delta := 1/10$. For each $n \in \mathbb{N}$, let
$$a^*(n) := p(a(10n)) = b(10n + 2)^c \le b \cdot 12^c (n + 1)^c, \qquad m^*(n) := m'(10n) = b_1 (10n + 1)^{c_1} \le b_1 \cdot 11^{c_1} (n + 1)^{c_1}.$$
Define the polynomials (both of Vereshchagin's form $b'(n + 1)^{c'}$)
$$a''(n) := (b \cdot 12^c + 1)(n + 1)^c \;\ge\; n + a^*(n), \qquad m''(n) := b_1 \cdot 11^{c_1} (n + 1)^{c_1} \;\ge\; m^*(n).$$
Define a worst-case $\mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}$ verifier $W^{\widetilde{A}}(x_0, \tilde{y}, \tilde{r})$ on input $x_0$ of length $n = |x_0|$ with $|\tilde{y}| = m''(n)$ and $|\tilde{r}| = a''(n)$ as follows:
- Parse the first $n + a^*(n) \le a''(n)$ bits of Arthur's random string $\tilde{r}$ as a uniformly random pair $(x, z) \in \{0,1\}^n \times \{0,1\}^{a^*(n)}$ (ignoring any remaining bits of $\tilde{r}$), and let $y \in \{0,1\}^{m^*(n)}$ be the prefix of $\tilde{y}$ of length $m^*(n)$.
- Run and output $V^{\widetilde{A}}(x, y, z, 1/10)$.

Clearly $W^{\widetilde{A}}$ runs in time bounded by a polynomial $t''(n)$ (since $t_V(10n) + n + m''(n) + a''(n) = \mathrm{poly}(n)$). Fix any $n \in \mathbb{N}$ and any input $x_0 \in \{0,1\}^n$. Let $\gamma \in [0, 1/10]$ denote the fraction of strings $x \in \{0,1\}^n$ on which $V^{\widetilde{A}}(\cdot, \cdot, \cdot, 1/10)$ fails the $\mathrm{AM}$ completeness/soundness condition (so $1 - \gamma \ge 9/10 > 0$). Because $L$ is **length-only**, either all $x \in \{0,1\}^n$ belong to $L$ or none do:
- **If $x_0 \in L$:** Every $x \in \{0,1\}^n$ lies in $L$, so on the $(1 - \gamma)$ fraction of good strings $x$, $\Pr_z[\exists y : V^{\widetilde{A}}(x, y, z, 1/10) = 1] > 2/3$. Hence
  $$\Pr_{\tilde{r} \in \{0,1\}^{a''(n)}}\bigl[\exists \tilde{y} \in \{0,1\}^{m''(n)}\; W^{\widetilde{A}}(x_0, \tilde{y}, \tilde{r}) = 1\bigr] > (1 - \gamma) \cdot \frac{2}{3} \ge \frac{9}{10} \cdot \frac{2}{3} = \frac{3}{5} > \frac{1}{2}.$$
- **If $x_0 \notin L$:** No $x \in \{0,1\}^n$ lies in $L$, so on the $(1 - \gamma)$ fraction of good strings $x$, $\Pr_z[\exists y : V^{\widetilde{A}}(x, y, z, 1/10) = 1] < 1/3$, while on the $\gamma$ fraction of bad strings the probability is at most $1$. Hence
  $$\Pr_{\tilde{r} \in \{0,1\}^{a''(n)}}\bigl[\exists \tilde{y} \in \{0,1\}^{m''(n)}\; W^{\widetilde{A}}(x_0, \tilde{y}, \tilde{r}) = 1\bigr] < \gamma \cdot 1 + (1 - \gamma) \cdot \frac{1}{3} = \frac{1}{3} + \frac{2}{3}\gamma \le \frac{1}{3} + \frac{2}{30} = \frac{2}{5} < \frac{1}{2}.$$

Thus $L \in \mathrm{PP}\!\cdot\!\mathrm{NP}^{\widetilde{A}}[m'', a'', t'']$. However,
$$m(n) - a''(n) = (b \cdot 12^c + 2)(n + 1)^{c + 1} - (b \cdot 12^c + 1)(n + 1)^c \;\ge\; (n + 1)^{c + 1} \;\ge\; (n + 1)^2,$$
whereas $\log_2(2(a''(n) + m''(n) + 2 t''(n)^2) + 8) + 17 = O(\log n)$, so the randomness hypothesis of Theorem 1 holds for all sufficiently large $n$. This contradicts Theorem 1 and proves Theorem 2. $\blacksquare$

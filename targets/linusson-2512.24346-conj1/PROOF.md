# Proof of Conjecture 1 (Symmetry of Complements) of Linusson–Özdemir (`arXiv:2512.24346v1`)

## 1. Exact Statement and Primary Source

**Primary source:** Svante Linusson and Alperen Özdemir, *"The $k$-Plancherel Measure and a Finite Markov Chain"*, `arXiv:2512.24346v1` (2025-12-30), `Kplancherel.tex`, Section 3.3–3.4 (lines 299–312, 641–645).

For a fixed integer $k \ge 1$, let $\mathcal{P}_k$ denote the set of $k$-bounded partitions ($\lambda_1 \le k$), let $l_i(\lambda)$ denote the multiplicity of part $i$ in $\lambda$, and define the finite state space
$$\mathcal{R}_k := \{\lambda \in \mathcal{P}_k : l_i(\lambda) \le k - i \text{ for all } i = 1, \dots, k\}, \qquad |\mathcal{R}_k| = k!.$$
For $\lambda \in \mathcal{P}_k(n)$, let $s_\lambda^{(k)}[X]$ denote the $k$-Schur function (at $t = 1$) and let $d_\lambda^{(k)} := [x_1 x_2 \cdots x_n] s_\lambda^{(k)}[X] = \mathbf{K}_{\lambda, (1^n)}^{(k)} \ge 1$ be the number of standard strong marked tableaux of shape $\mathfrak{c}(\lambda)$ (Section 2.4, eq. `(10)` / lines 210–219). For each $i \in \{1, \dots, k\}$, let $\square_i := (i^{k-i+1})$ denote the $i$-th $k$-rectangle (of area $|\square_i| = i(k-i+1)$), and let $\mathrm{red}_k : \mathcal{P}_k \to \mathcal{R}_k$ be the projection obtained by deleting copies of $\square_i$ until $l_i \le k - i$ for all $i \in [k]$.

The **finite $k$-chain** is the discrete-time Markov chain on $\mathcal{R}_k$ obtained by projecting the infinite $k$-Plancherel growth chain $P(\lambda, \Lambda) = \frac{d_\Lambda^{(k)}}{(|\lambda| + 1) d_\lambda^{(k)}}$ ($\lambda \to_k \Lambda$ in weak order) via $\mathrm{red}_k$:
$$P(\lambda, \mu) = \sum_{\substack{\lambda \to_k \Lambda \\ \mathrm{red}_k(\Lambda) = \mu}} \frac{d_\Lambda^{(k)}}{(|\lambda| + 1) d_\lambda^{(k)}} \qquad (\lambda, \mu \in \mathcal{R}_k).$$
(As shown in Lemma 3 below, for all $k \ge 3$ at most one weak cover $\lambda \to_k \Lambda$ projects to any given $\mu \in \mathcal{R}_k$, so this coincides verbatim with the piecewise formula in Section 3.3, lines 307–311; at $k = 2$ and $(\lambda, \mu) = ((1), \emptyset)$, the two weak covers $(1) \to_2 (1, 1) = \square_1$ and $(1) \to_2 (2) = \square_2$ both project to $\emptyset$ and sum to $P((1), \emptyset) = \frac{1}{2} + \frac{1}{2} = 1$.)

For $\lambda \in \mathcal{R}_k$, define its complement $\lambda^{\mathrm{comp}} \in \mathcal{R}_k$ by
$$l_i(\lambda^{\mathrm{comp}}) = (k - i) - l_i(\lambda) \qquad \text{for all } i = 1, \dots, k,$$
so that $\lambda \cup \lambda^{\mathrm{comp}} = (k-1, (k-2)^2, \dots, i^{k-i}, \dots, 2^{k-2}, 1^{k-1})$.

> **Conjecture 1 (`\label{conj:complement}`, Symmetry of complements, Section 3.4, lines 643–645):**
> *For all $\lambda \in \mathcal{R}_k$, $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$.*

We prove the following stronger theorem giving an explicit closed-form stationary distribution via generalized detailed balance ($R$-reversibility), from which Conjecture 1 follows immediately.

---

## 2. Main Theorem

**Theorem 1 (Explicit Stationary Distribution and $R$-Reversibility).**
*For every integer $k \ge 1$, the finite $k$-chain on $\mathcal{R}_k$ is irreducible and has unique stationary distribution $\pi$ given explicitly by*
$$\pi(\lambda) = \frac{w(\lambda)}{Z_k}, \qquad w(\lambda) := \frac{d_\lambda^{(k)} \, d_{\lambda^{\mathrm{comp}}}^{(k)}}{|\lambda|! \, |\lambda^{\mathrm{comp}}|!}, \qquad Z_k := \sum_{\nu \in \mathcal{R}_k} w(\nu).$$
*Moreover, letting $R(\lambda) := \lambda^{\mathrm{comp}}$, the chain satisfies exact $R$-reversibility:*
$$\pi(\lambda) P(\lambda, \mu) = \pi(\mu) P(R(\mu), R(\lambda)) \qquad \text{for all } \lambda, \mu \in \mathcal{R}_k.$$

**Corollary 2 (Resolution of Conjecture 1).**
*For every integer $k \ge 1$ and every $\lambda \in \mathcal{R}_k$, $\pi(\lambda) = \pi(\lambda^{\mathrm{comp}})$.*

*Proof of Corollary 2 from Theorem 1:* Since $R(\lambda) = \lambda^{\mathrm{comp}}$ is an involution ($R(R(\lambda)) = \lambda$), the formula for $w(\lambda)$ is manifestly symmetric under $\lambda \leftrightarrow \lambda^{\mathrm{comp}}$, so $w(\lambda) = w(\lambda^{\mathrm{comp}})$ and hence $\pi(\lambda) = w(\lambda)/Z_k = w(\lambda^{\mathrm{comp}})/Z_k = \pi(\lambda^{\mathrm{comp}})$. $\blacksquare$

---

## 3. Preliminaries and Lemmas

For $k = 1$, $\mathcal{R}_1 = \{\emptyset\}$, $\emptyset^{\mathrm{comp}} = \emptyset$, $P(\emptyset, \emptyset) = 1$, $w(\emptyset) = 1$, and $Z_1 = 1$, so Theorem 1 holds trivially. Assume $k \ge 2$ below.

### Lemma 1 (Pieri Row-Stochasticity and $k$-Rectangle Dimension Identity)
*For every $\lambda \in \mathcal{P}_k$, $d_\lambda^{(k)} \ge 1$, and:*
1. *(Row-stochasticity)* $\sum_{\lambda \to_k \Lambda} \frac{d_\Lambda^{(k)}}{(|\lambda| + 1) d_\lambda^{(k)}} = 1$. Consequently $\sum_{\mu \in \mathcal{R}_k} P(\lambda, \mu) = 1$ for every $\lambda \in \mathcal{R}_k$.
2. *($k$-rectangle factorization)* *For every $\mu \in \mathcal{P}_k$ and every $i \in \{1, \dots, k\}$,*
   $$\frac{d_{\mu \cup \square_i}^{(k)}}{|\mu \cup \square_i|!} = \frac{d_{\square_i}}{|\square_i|!} \cdot \frac{d_\mu^{(k)}}{|\mu|!},$$
   *where $d_{\square_i} = [x_1 \cdots x_{|\square_i|}] s_{\square_i}[X] > 0$ is the number of standard Young tableaux of rectangular shape $\square_i = (i^{k-i+1})$.*

*Proof.*
For any $\lambda \in \mathcal{P}_k(n)$, the $k$-Schur function $s_\lambda^{(k)}$ expands Schur-positively with leading term $s_\lambda$ (alternatively, every $(k+1)$-core $\mathfrak{c}(\lambda)$ has at least one weak chain from $\emptyset$, hence at least one standard strong marked tableau), so $d_\lambda^{(k)} \ge d_\lambda \ge 1$.

For any two homogeneous symmetric functions $f, g$ of degrees $a, b \ge 0$, every term contributing to the square-free monomial $x_1 x_2 \cdots x_{a+b}$ in $f(X) g(X)$ arises uniquely from choosing an $a$-element subset $S \subseteq \{1, \dots, a+b\}$ for $f$ and its complement for $g$. By symmetry of $f$ and $g$, each of the $\binom{a+b}{a}$ choices contributes $([x_1 \cdots x_a] f)([x_1 \cdots x_b] g)$, giving
$$\frac{[x_1 \cdots x_{a+b}](f \cdot g)}{(a+b)!} = \frac{[x_1 \cdots x_a] f}{a!} \cdot \frac{[x_1 \cdots x_b] g}{b!}. \tag{1}$$

1. By the $k$-Schur Pieri rule (Lam–Lapointe–Morse–Schilling–Shimozono–Zabrocki 2014, §2.2; cited in `Kplancherel.tex` §3.2, line 282),
   $$h_1 \cdot s_\lambda^{(k)} = \sum_{\lambda \to_k \Lambda} s_\Lambda^{(k)}.$$
   Applying (1) with $f = h_1$ (degree $a = 1$, $[x_1] h_1 = 1$) and $g = s_\lambda^{(k)}$ (degree $b = |\lambda|$) gives $(|\lambda| + 1) d_\lambda^{(k)} = \sum_{\lambda \to_k \Lambda} d_\Lambda^{(k)}$, proving (1).

2. By the $k$-rectangle property of $k$-Schur functions (Lapointe–Morse 2007, Theorem 40; cited in `Kplancherel.tex` §3.3, line 300),
   $$s_{\square_i} \cdot s_\mu^{(k)} = s_{\mu \cup \square_i}^{(k)}.$$
   Applying (1) with $f = s_{\square_i}$ (degree $a = |\square_i|$) and $g = s_\mu^{(k)}$ (degree $b = |\mu|$) yields (2) directly. $\blacksquare$

---

### Lemma 2 (Maya Diagrams, Cyclic-Arc Formula, and Complementation = Cyclic Reversal)
*Identify $S_k$ with the set of cyclic permutations $\sigma$ of $\{1, 2, \dots, k+1\}$ oriented clockwise on the circle $\mathbb{Z}/(k+1)\mathbb{Z}$ (written in one-line notation with $k+1$ fixed in the last position). There is a bijection $\alpha : S_k \to \mathcal{R}_k$ given explicitly by*
$$l_m(\alpha(\sigma)) = \#\bigl\{p \in \{m+2, \dots, k+1\} : p \text{ lies strictly clockwise between } m \text{ and } m+1 \text{ in } \sigma\bigr\} \qquad (1 \le m \le k). \tag{2}$$
*Moreover:*
1. *For every $(k+1)$-core $\kappa \in \mathcal{C}_{k+1}$, let $\sigma(\kappa) \in S_k$ be the cyclic order of the residue classes mod $(k+1)$ of the $k+1$ leftmost occupied positions $b_1 < b_2 < \dots < b_{k+1}$ of its Maya diagram. Then $\mathrm{red}_k(\mathfrak{p}(\kappa)) = \alpha(\sigma(\kappa))$.*
2. *Letting $\sigma^{\mathrm{rev}} \in S_k$ denote the cyclic reversal of $\sigma$ (reversing the cyclic orientation on $\mathbb{Z}/(k+1)\mathbb{Z}$, keeping $k+1$ fixed at the end), we have*
   $$\alpha(\sigma^{\mathrm{rev}}) = \alpha(\sigma)^{\mathrm{comp}} = R(\alpha(\sigma)) \qquad \text{for all } \sigma \in S_k.$$

*(Remark: Note that line 517 of `Kplancherel.tex` inadvertently prints $\lambda^{\omega_k}$ where $\lambda^{\mathrm{comp}}$ is meant; Lemma 2(2) proves the exact correspondence with $\lambda^{\mathrm{comp}}$ directly from the core bijection.)*

*Proof.*
For any partition $\kappa = (\kappa_1 \ge \kappa_2 \ge \dots)$ (with $\kappa_r = 0$ for $r > l(\kappa)$), define its **vacant set** $V(\kappa) := \{\kappa_r - r : r \ge 1\} \subset \mathbb{Z}$ and its **occupied set** (Maya diagram) $M(\kappa) := \mathbb{Z} \setminus V(\kappa)$. For each $r \ge 1$, letting $y_r = \kappa_r - r \in V(\kappa)$ and choosing any $N > \max(l(\kappa), -y_r)$, the interval $[-N, y_r - 1]$ contains $y_r + N = \kappa_r - r + N$ integers of which exactly $N - r$ belong to $V(\kappa)$ (namely $y_{r+1}, \dots, y_N$); hence $\#\{x \in M(\kappa) : x < y_r\} = \kappa_r$. Listing these occupied positions in increasing order as $x_1 < \dots < x_{\kappa_r}$, cell $(r, c)$ ($1 \le c \le \kappa_r$) has arm length $\kappa_r - c = \#(M(\kappa) \cap (x_c, y_r))$ and leg length $\#\{r' > r : \kappa_{r'} \ge c\} = \#\{r' > r : y_{r'} > x_c\} = \#(V(\kappa) \cap (x_c, y_r))$, so its hook length is exactly
$$h(r, c) = 1 + \#(M(\kappa) \cap (x_c, y_r)) + \#(V(\kappa) \cap (x_c, y_r)) = y_r - x_c.$$

Hence $\kappa$ is a $(k+1)$-core (no hook of length $k+1$) if and only if $x \in M(\kappa) \implies x + (k+1) \in M(\kappa)$. Thus each residue class $r \in \mathbb{Z}/(k+1)\mathbb{Z}$ has a unique smallest occupied integer $b^{(r)} \in M(\kappa)$ with $b^{(r)} \equiv r \pmod{k+1}$, and $M(\kappa) = \bigsqcup_{r=0}^k \{b^{(r)} + t(k+1) : t \ge 0\}$. Sort these $k+1$ minima strictly increasingly as
$$b_1 < b_2 < \dots < b_{k+1},$$
and let $r_p := b_p \bmod (k+1) \in \mathbb{Z}/(k+1)\mathbb{Z}$. Placing label $p$ at residue $r_p$ on the clockwise-oriented circle $\mathbb{Z}/(k+1)\mathbb{Z}$ (with $+1 \pmod{k+1}$ moving clockwise) defines $\sigma(\kappa) \in S_k$.

By definition of $\mathfrak{p} : \mathcal{C}_{k+1} \to \mathcal{P}_k$ (`Kplancherel.tex` §2.2, lines 116–119), the length of row $r$ (vacant site $y = \kappa_r - r$) in $\mathfrak{p}(\kappa)$ is the number of cells in row $r$ with hook length $< k + 1$:
$$\#\{x \in M(\kappa) : y - (k+1) < x < y\} = \#\{p \in \{1, \dots, k+1\} : b_p < y\}.$$
Indeed, for each residue class $r_p \neq y \bmod (k+1)$, there is a unique integer $x \in (y - (k+1), y)$ with $x \equiv r_p \pmod{k+1}$, and $x \in M(\kappa) \iff b_p \le x \iff b_p < y$; meanwhile for the residue class $r_q = y \bmod (k+1)$, $y \in V(\kappa)$ implies $y < b_q$.

Consequently, for each $m \in \{1, \dots, k\}$, the parts of size $m$ in $\mathfrak{p}(\kappa)$ correspond bijectively to vacant sites $y \in V(\kappa)$ satisfying $b_m < y < b_{m+1}$. For any integer $y \in (b_m, b_{m+1})$ in residue class $r_p$, we have $y \in M(\kappa)$ if $p \le m$ (as $b_p \le b_m < y$) and $y \in V(\kappa)$ if $p \ge m+1$ (as $y < b_{m+1} \le b_p$). Hence
$$l_m(\mathfrak{p}(\kappa)) = \#\bigl\{y \in (b_m, b_{m+1}) : y \equiv r_p \pmod{k+1} \text{ for some } p \in \{m+1, \dots, k+1\}\bigr\}. \tag{3}$$
Write $b_{m+1} - b_m = q_m(k+1) + d_m$ with $q_m \in \mathbb{Z}_{\ge 0}$ and $1 \le d_m \le k$ ($d_m \neq 0$ since $r_{m+1} \neq r_m$). The $q_m$ full half-open periods $[b_m + d_m, b_{m+1})$ each contain exactly one element from each of the $k + 1 - m$ classes $\{r_{m+1}, \dots, r_{k+1}\}$, contributing $q_m(k+1-m)$ parts of size $m$ (i.e., $q_m$ copies of $\square_m$). The remaining open interval $(b_m, b_m + d_m)$ has residues strictly clockwise between $r_m$ and $r_{m+1}$ (excluding $r_{m+1}$, which sits at $b_m + d_m$), so its elements in $\{r_{m+1}, \dots, r_{k+1}\}$ are precisely those $r_p$ with $p \in \{m+2, \dots, k+1\}$ strictly clockwise between $r_m$ and $r_{m+1}$. Reducing modulo $k + 1 - m$ yields (2) and proves (1).

To see that $\alpha : S_k \to \mathcal{R}_k$ defined by (2) is a bijection: reconstruct $\sigma$ uniquely from $(l_1, \dots, l_k)$ by starting with $k+1$ and $k$ on the circle and, for $m = k-1, k-2, \dots, 1$, placing $m$ in the unique cyclic gap among $\{m+1, \dots, k+1\}$ such that exactly $l_m \in \{0, \dots, k-m\}$ elements of $\{m+2, \dots, k+1\}$ lie strictly clockwise from $m$ to $m+1$ (equivalently, $l_m$ steps counterclockwise from $m+1$ among $\{m+1, \dots, k+1\}$). Every tuple in $\prod_{m=1}^k \{0, \dots, k-m\}$ determines a unique $\sigma \in S_k$.

Finally, for any $\sigma \in S_k$, any $m \in \{1, \dots, k\}$, and any $p \in \{m+2, \dots, k+1\}$, label $p$ lies strictly clockwise between $m$ and $m+1$ in $\sigma^{\mathrm{rev}}$ if and only if $p$ does **not** lie strictly clockwise between $m$ and $m+1$ in $\sigma$. Summing over the $k - m$ elements of $\{m+2, \dots, k+1\}$ gives
$$l_m(\alpha(\sigma^{\mathrm{rev}})) + l_m(\alpha(\sigma)) = k - m \qquad (1 \le m \le k),$$
proving $\alpha(\sigma^{\mathrm{rev}}) = \alpha(\sigma)^{\mathrm{comp}}$. $\blacksquare$

---

### Lemma 3 (Weak Covers, TASEP Swaps, Rectangle Drops, and Reversal Bijection)
*Let $\lambda = \alpha(\sigma) \in \mathcal{R}_k$ with $\kappa = \mathfrak{c}(\lambda) \in \mathcal{C}_{k+1}$ (so $\sigma(\kappa) = \sigma$).*
1. *The weak covers $\lambda \to_k \Lambda$ (equivalently $\kappa \to_k \tau$ with $\Lambda = \mathfrak{p}(\tau)$) are in bijection with pairs $(j, i)$ such that $j$ sits immediately counterclockwise (to the left) of $i$ in $\sigma$ and $j > i$. Under the cover corresponding to $(j, i)$:*
   - *$\sigma(\tau)$ is obtained from $\sigma$ by swapping the adjacent pair $(j, i) \mapsto (i, j)$;*
   - *$\Lambda$ has $l_i(\Lambda) = l_i(\lambda) + 1$, $l_{i-1}(\Lambda) = l_{i-1}(\lambda) - 1$ (if $i \ge 2$), and $l_m(\Lambda) = l_m(\lambda)$ for $m \notin \{i-1, i\}$;*
   - *if $j \ge i + 2$, then $\Lambda \in \mathcal{R}_k$ (so $\mathrm{red}_k(\Lambda) = \Lambda = \alpha(\sigma(\tau))$ and no $k$-rectangle is dropped);*
   - *if $j = i + 1$, then $l_i(\lambda) = k - i$ and $\Lambda = \mu \cup \square_i$ with $\mu = \mathrm{red}_k(\Lambda) = \alpha(\sigma(\tau)) \in \mathcal{R}_k$ (so the unique $k$-rectangle $\square_i$ is dropped).*
2. *For $k \ge 3$, distinct weak covers from $\lambda \in \mathcal{R}_k$ project to distinct elements of $\mathcal{R}_k$.*
3. *(Exact Reversal of Transitions) A pair $(j, i)$ with $j > i$ is a valid swap from $\sigma$ to $\tau$ if and only if the **exact same** pair $(j, i)$ is a valid swap from $\tau^{\mathrm{rev}}$ to $\sigma^{\mathrm{rev}}$. In particular, if a weak cover $\lambda \to_k \Lambda$ projects to $\mu = \mathrm{red}_k(\Lambda)$ via swap $(j, i)$, then the corresponding weak cover from $R(\mu)$ projects to $R(\lambda)$ via the exact same swap $(j, i)$, dropping no rectangle if $j \ge i + 2$ and dropping the exact same rectangle $\square_i$ if $j = i + 1$.*

*Proof.*
1. By Definition 2.1 of `Kplancherel.tex` (line 148), $\kappa \to_k \tau$ means $\kappa \subsetneq \tau$ are $(k+1)$-cores such that all cells of $\tau \setminus \kappa$ have the same content $c \pmod{k+1}$. Adding a single cell to row $r$ of a partition replaces $y_r = \kappa_r - r \in V$ with $y_r + 1 \in M$ (shifting a particle left from $x = y_r + 1$ to $x - 1 = y_r$), and the newly added cell $(r, \kappa_r + 1)$ has content $(\kappa_r + 1) - r = y_r + 1 = x$. Since $k + 1 \ge 3$ (or for $k = 2$, $k + 1 = 3 \ge 2$), consecutive cells in the same row have distinct contents mod $(k+1)$, so $\tau \setminus \kappa$ contains at most one cell in each row, all of content $\equiv c \pmod{k+1}$. Hence $M(\tau)$ is obtained from $M(\kappa)$ by choosing a nonempty subset $A \subseteq S_c(\kappa) := \{x \equiv c \pmod{k+1} : x \in M(\kappa),\ x - 1 \in V(\kappa)\}$ and shifting every $x \in A$ to $x - 1$.

   Let $i, j \in \{1, \dots, k+1\}$ be the unique labels with $r_i \equiv c$ and $r_j \equiv c - 1 \pmod{k+1}$ (so $j$ is immediately counterclockwise of $i$ in $\sigma$). Because $x \in M(\kappa) \iff x \ge b_i$ (for $x \equiv c$) and $x - 1 \in V(\kappa) \iff x - 1 < b_j$ (for $x - 1 \equiv c - 1$), we have
   $$S_c(\kappa) = \{b_i + t(k+1) : t \ge 0,\ b_i + t(k+1) \le b_j - k\},$$
   which is nonempty if and only if $b_i < b_j$, i.e., $i < j$. Moreover, since $M(\tau)$ must be closed under $+ (k+1)$:
   - if $x \in A$, then $x - 1 \in M(\tau) \implies x - 1 + (k+1) \in M(\tau)$, forcing $x + (k+1) \in A$ whenever $x + (k+1) \in S_c(\kappa)$;
   - if $x \in S_c(\kappa) \setminus A$, then $x \in M(\tau) \implies x + (k+1) \in M(\tau)$, forcing $x + (k+1) \notin A$.
   Since $A \neq \emptyset$ and $S_c(\kappa)$ is a single $(k+1)$-progression, necessarily $A = S_c(\kappa)$.

   Moving all $x \in S_c(\kappa)$ to $x - 1$ shifts the leftmost occupied position in class $c - 1$ from $b_j$ to $b_i - 1$ and the leftmost occupied position in class $c$ from $b_i$ to $b_j + 1$, leaving all other residue classes unchanged. Note that $b_i - 1 \in V(\kappa)$ cannot equal any $b_p$, so $b_{i-1} < b_i - 1 < b_i$ (if $i \ge 2$); similarly $b_j + 1 \in M(\kappa) \setminus \{b_i\}$ (since $b_j + 1 > b_i$ and $b_j + 1 \equiv b_i \pmod{k+1}$) cannot equal any $b_p$, so $b_j < b_j + 1 < b_{j+1}$ (if $j \le k$). Thus the sorted minima of $M(\tau)$ are
   $$b'_i = b_i - 1 \ (\text{class } c-1), \qquad b'_j = b_j + 1 \ (\text{class } c), \qquad b'_p = b_p \ (p \notin \{i, j\}),$$
   so $\sigma(\tau)$ is obtained from $\sigma(\kappa)$ by swapping the adjacent pair $(j, i) \mapsto (i, j)$.

   Next compute $l_m(\Lambda) = l_m(\mathfrak{p}(\tau))$ from (3):
   - Every $x \in S_c(\kappa)$ swaps vacant $x - 1$ with occupied $x$. For $x \in S_c(\kappa) \setminus \{b_i\}$, neither $x - 1 \in V(\kappa)$ nor $x \in M(\kappa) \setminus \{b_i\}$ belongs to $\{b_1, \dots, b_{k+1}\}$, so $x - 1$ and $x$ lie in the same open interval $(b_m, b_{m+1}) = (b'_m, b'_{m+1})$, causing zero net change to $l_m$.
   - For $x = b_i$: $b_i - 1 \in V(\kappa)$ lies in $(b_{i-1}, b_i)$ (if $i \ge 2$) and becomes the new boundary $b'_i = b_i - 1 \in M(\tau)$, while $b_i \in M(\kappa)$ becomes vacant in $(b'_i, b'_{i+1})$ (since $b_i < b_{i+1} \le b'_{i+1}$). Thus $l_{i-1}$ decreases by $1$ (if $i \ge 2$) and $l_i$ increases by $1$.
   - At $b_j \mapsto b_j + 1$: both $b_j$ and $b_j + 1$ lie in $M(\kappa) \cap M(\tau)$, so shifting the boundary moves no vacant sites and causes zero net change to $l_{j-1}$ or $l_j$.

   Hence $l_i(\Lambda) = l_i(\lambda) + 1$, $l_{i-1}(\Lambda) = l_{i-1}(\lambda) - 1$ (if $i \ge 2$), and $l_m(\Lambda) = l_m(\lambda)$ for $m \notin \{i-1, i\}$. Since $\lambda \in \mathcal{R}_k$ ($l_m(\lambda) \le k - m$ for all $m$), $\Lambda$ leaves $\mathcal{R}_k$ if and only if $l_i(\lambda) = k - i$, in which case $l_i(\Lambda) = k - i + 1$ while $l_m(\Lambda) \le k - m$ for all $m \neq i$, so $\Lambda = \mu \cup \square_i$ where $\mu = \mathrm{red}_k(\Lambda) = \alpha(\sigma(\tau))$ by Lemma 2(1). By (2), $l_i(\lambda) = k - i$ holds iff all $k - i$ elements of $\{i+2, \dots, k+1\}$ lie strictly clockwise between $i$ and $i+1$ in $\sigma$, i.e., no element of $\{i+2, \dots, k+1\}$ lies strictly clockwise between $i+1$ and $i$. Because $j \ge i + 1$ sits immediately counterclockwise of $i$:
   - if $j \ge i + 2$, then $j$ does not lie strictly clockwise from $i$ to $i+1$, so $l_i(\lambda) \le k - i - 1$ and $\Lambda \in \mathcal{R}_k$;
   - if $j = i + 1$, then $i+1$ sits immediately counterclockwise of $i$, so all $k - i$ elements of $\{i+2, \dots, k+1\}$ lie strictly clockwise from $i$ to $i+1$, giving $l_i(\lambda) = k - i$ and $\Lambda = \mu \cup \square_i$.

2. Let $k \ge 3$ and suppose weak covers from $\lambda \in \mathcal{R}_k$ at distinct indices $i_1 < i_2$ produce $\mu^{(1)}, \mu^{(2)} \in \mathcal{R}_k$. Let $\Delta^{(s)}_m := l_m(\mu^{(s)}) - l_m(\lambda)$. For $i = 1$, $\Delta_1 \in \{+1, -(k-1)\}$ (both distinct from $-1$ since $k \ge 3$) and $\Delta_m = 0$ for $m \ge 2$. For $i \ge 2$, the smallest index $m \ge 1$ with $\Delta_m \neq 0$ is $m = i - 1$ with $\Delta_{i-1} = -1$. Thus the vectors $\Delta^{(1)}$ and $\Delta^{(2)}$ are distinct, so $\mu^{(1)} \neq \mu^{(2)}$.

3. Swapping adjacent entries $(j, i) \mapsto (i, j)$ in $\sigma = (\dots, j, i, \dots)$ produces $\tau = (\dots, i, j, \dots)$. Reversing both cyclic orientations gives $\tau^{\mathrm{rev}} = (\dots, j, i, \dots)$ and $\sigma^{\mathrm{rev}} = (\dots, i, j, \dots)$, which differ by the **exact same** adjacent swap $(j, i) \mapsto (i, j)$ with $j > i$. By Lemma 2(2) and Part 1, the induced transition $R(\mu) \to R(\lambda)$ drops no rectangle if $j \ge i + 2$ and drops the exact same rectangle $\square_i$ if $j = i + 1$. $\blacksquare$

---

### Lemma 4 (Irreducibility of the Finite $k$-Chain)
*For every $k \ge 2$, the finite $k$-chain on $\mathcal{R}_k$ is irreducible.*

*Proof.*
Every valid TASEP swap $(j, i) \mapsto (i, j)$ ($j > i$) has strictly positive transition probability $d_\Lambda^{(k)} / ((|\lambda| + 1) d_\lambda^{(k)}) > 0$. Identifying $\mathcal{R}_k$ with $S_k$ via $\alpha^{-1}$ (writing $\sigma = (\sigma_1, \dots, \sigma_k, k+1)$), the legal transitions are:
- *(Inversion reduction)* swapping any adjacent $(\sigma_p, \sigma_{p+1})$ with $1 \le p \le k-1$ and $\sigma_p > \sigma_{p+1}$;
- *(Left cyclic rotation)* swapping $(k+1, \sigma_1) \mapsto (\sigma_1, k+1)$, which shifts $(\sigma_1, \sigma_2, \dots, \sigma_k, k+1) \mapsto (\sigma_2, \dots, \sigma_k, \sigma_1, k+1)$ (always legal since $k + 1 > \sigma_1$).

Let $\mathrm{id} = (1, 2, \dots, k, k+1)$ and $\omega_0 = (k, k-1, \dots, 1, k+1)$. For any $\sigma, \tau \in S_k$, we construct a directed path $\sigma \to^* \mathrm{id} \to^* \omega_0 \to^* \tau$:
1. **$\sigma \to^* \mathrm{id}$:** As long as $\sigma \neq \mathrm{id}$, there is an adjacent inversion $\sigma_p > \sigma_{p+1}$; swapping it decreases the inversion count by $1$, terminating at $\mathrm{id}$.
2. **$\mathrm{id} \to^* \omega_0$:** By descending induction on $r = k - 1, k - 2, \dots, 0$, we reach $(1, \dots, r, k, k-1, \dots, r+1, k+1)$. For $r = k - 1$ this is $\mathrm{id}$. Given $(1, \dots, r, k, \dots, r+1, k+1)$ with $r \ge 1$, perform $r$ left cyclic rotations to obtain $(k, \dots, r+1, 1, \dots, r-1, r, k+1)$. Since $1 < 2 < \dots < r - 1 < r + 1 < \dots < k$, successively move $1$, then $2$, ..., then $r - 1$ left past $k, \dots, r + 1$ by legal inversion reductions, arriving at $(1, \dots, r-1, k, \dots, r+1, r, k+1)$. At $r = 0$ we reach $\omega_0$.
3. **$\omega_0 \to^* \tau$:** For $p = 1, 2, \dots, k$ in turn, suppose the current permutation already agrees with $\tau$ on positions $1, \dots, p - 1$ and its remaining entries in positions $p, \dots, k$ appear in strictly decreasing order (true for $p = 1$ at $\omega_0$). Then every entry lying strictly between position $p$ and $\tau_p$ is strictly larger than $\tau_p$, so $\tau_p$ can legally swap left into position $p$, preserving the strictly decreasing order of the remaining entries in positions $p+1, \dots, k$. After $p = k$ we reach $\tau$.

Hence every state communicates with every other state, so the Markov chain is irreducible. $\blacksquare$

---

## 4. Proof of Theorem 1

Let $k \ge 2$ and define, for each $\lambda \in \mathcal{R}_k$,
$$w(\lambda) := \frac{d_\lambda^{(k)} \, d_{R(\lambda)}^{(k)}}{|\lambda|! \, |R(\lambda)|!} > 0.$$
We prove that for every $\lambda = \alpha(\sigma)$ and $\mu = \alpha(\tau)$ in $\mathcal{R}_k$,
$$w(\lambda) P(\lambda, \mu) = w(\mu) P(R(\mu), R(\lambda)). \tag{4}$$

By Lemma 3(1) and 3(3), the set of valid TASEP swaps $e = (j, i)$ ($j > i$) carrying $\sigma$ to $\tau$ is identical to the set of valid TASEP swaps $e = (j, i)$ carrying $\tau^{\mathrm{rev}}$ to $\sigma^{\mathrm{rev}}$. Let $P_e(\lambda, \mu)$ denote the contribution of a single swap $e = (j, i)$ from $\sigma$ to $\tau$, so $P(\lambda, \mu) = \sum_{e : \sigma \to \tau} P_e(\lambda, \mu)$ and $P(R(\mu), R(\lambda)) = \sum_{e : \sigma \to \tau} P_e(R(\mu), R(\lambda))$. It suffices to verify $w(\lambda) P_e(\lambda, \mu) = w(\mu) P_e(R(\mu), R(\lambda))$ for each swap $e = (j, i)$ ($j > i$) from $\sigma$ to $\tau$.

**Case 1: $j \ge i + 2$ (no $k$-rectangle dropped).**
By Lemma 3(1) and 3(3), $\lambda \to_k \mu$ (with $|\mu| = |\lambda| + 1$) and $R(\mu) \to_k R(\lambda)$ (with $|R(\lambda)| = |R(\mu)| + 1$). Therefore
$$P_e(\lambda, \mu) = \frac{d_\mu^{(k)}}{(|\lambda| + 1) d_\lambda^{(k)}} = \frac{|\lambda|!}{|\mu|!} \cdot \frac{d_\mu^{(k)}}{d_\lambda^{(k)}}, \qquad P_e(R(\mu), R(\lambda)) = \frac{d_{R(\lambda)}^{(k)}}{(|R(\mu)| + 1) d_{R(\mu)}^{(k)}} = \frac{|R(\mu)|!}{|R(\lambda)|!} \cdot \frac{d_{R(\lambda)}^{(k)}}{d_{R(\mu)}^{(k)}}.$$
Multiplying by $w(\lambda)$ and $w(\mu)$ respectively yields
$$w(\lambda) P_e(\lambda, \mu) = \frac{d_\lambda^{(k)} d_{R(\lambda)}^{(k)}}{|\lambda|! \, |R(\lambda)|!} \cdot \frac{|\lambda|! \, d_\mu^{(k)}}{|\mu|! \, d_\lambda^{(k)}} = \frac{d_\mu^{(k)} d_{R(\lambda)}^{(k)}}{|\mu|! \, |R(\lambda)|!},$$
$$w(\mu) P_e(R(\mu), R(\lambda)) = \frac{d_\mu^{(k)} d_{R(\mu)}^{(k)}}{|\mu|! \, |R(\mu)|!} \cdot \frac{|R(\mu)|! \, d_{R(\lambda)}^{(k)}}{|R(\lambda)|! \, d_{R(\mu)}^{(k)}} = \frac{d_\mu^{(k)} d_{R(\lambda)}^{(k)}}{|\mu|! \, |R(\lambda)|!},$$
which are identically equal.

**Case 2: $j = i + 1$ ($k$-rectangle $\square_i$ dropped).**
By Lemma 3(1) and 3(3), $\lambda \to_k \Lambda = \mu \cup \square_i$ (with $|\Lambda| = |\lambda| + 1$) and $R(\mu) \to_k \tilde{\Lambda} = R(\lambda) \cup \square_i$ (with $|\tilde{\Lambda}| = |R(\mu)| + 1$), dropping the **exact same** rectangle $\square_i$. By Lemma 1(2),
$$\frac{d_\Lambda^{(k)}}{|\Lambda|!} = \frac{d_{\square_i}}{|\square_i|!} \cdot \frac{d_\mu^{(k)}}{|\mu|!}, \qquad \frac{d_{\tilde{\Lambda}}^{(k)}}{|\tilde{\Lambda}|!} = \frac{d_{\square_i}}{|\square_i|!} \cdot \frac{d_{R(\lambda)}^{(k)}}{|R(\lambda)|!}.$$
Hence
$$P_e(\lambda, \mu) = \frac{|\lambda|!}{|\Lambda|!} \cdot \frac{d_\Lambda^{(k)}}{d_\lambda^{(k)}} = \frac{d_{\square_i}}{|\square_i|!} \cdot \frac{|\lambda|! \, d_\mu^{(k)}}{|\mu|! \, d_\lambda^{(k)}}, \qquad P_e(R(\mu), R(\lambda)) = \frac{|R(\mu)|!}{|\tilde{\Lambda}|!} \cdot \frac{d_{\tilde{\Lambda}}^{(k)}}{d_{R(\mu)}^{(k)}} = \frac{d_{\square_i}}{|\square_i|!} \cdot \frac{|R(\mu)|! \, d_{R(\lambda)}^{(k)}}{|R(\lambda)|! \, d_{R(\mu)}^{(k)}}.$$
Multiplying by $w(\lambda)$ and $w(\mu)$ respectively yields
$$w(\lambda) P_e(\lambda, \mu) = \frac{d_{\square_i}}{|\square_i|!} \cdot \frac{d_\mu^{(k)} d_{R(\lambda)}^{(k)}}{|\mu|! \, |R(\lambda)|!} = w(\mu) P_e(R(\mu), R(\lambda)).$$

Summing over all swaps $e : \sigma \to \tau$ establishes (4) for all $\lambda, \mu \in \mathcal{R}_k$.

Now sum (4) over all $\lambda \in \mathcal{R}_k$. Since $R : \mathcal{R}_k \to \mathcal{R}_k$ is a bijection and $P$ is row-stochastic by Lemma 1(1),
$$\sum_{\lambda \in \mathcal{R}_k} w(\lambda) P(\lambda, \mu) = w(\mu) \sum_{\lambda \in \mathcal{R}_k} P(R(\mu), R(\lambda)) = w(\mu) \sum_{\nu \in \mathcal{R}_k} P(R(\mu), \nu) = w(\mu) \qquad \text{for all } \mu \in \mathcal{R}_k.$$
Thus $\pi(\lambda) := w(\lambda) / Z_k$ is a stationary probability distribution of the finite $k$-chain. By Lemma 4, the chain is finite and irreducible, so its stationary distribution is unique. Dividing (4) by $Z_k$ gives $\pi(\lambda) P(\lambda, \mu) = \pi(\mu) P(R(\mu), R(\lambda))$ for all $\lambda, \mu \in \mathcal{R}_k$. This completes the proof of Theorem 1 and Corollary 2 (Conjecture 1). $\blacksquare$

---

## 5. Verification

Run exact-arithmetic verification of all lemmas (Maya-diagram bijection, weak-cover swap correspondence, $k$-rectangle dimension identity, exact $R$-reversibility, closed-form $\pi(\lambda) = w(\lambda)/Z_k$ against exact rational stationary solve, and constructive irreducibility paths for $k = 1, 2, 3, 4, 5$):
```bash
.venv/bin/python targets/linusson-2512.24346-conj1/verify.py
```

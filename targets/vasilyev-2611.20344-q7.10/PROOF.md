# Proof of Question 7.10 (`arXiv:2611.20344v2`, `q:supremum`)

**Target:** Oleg Vasilyev, *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, `arXiv:2611.20344v2` (`updown.tex`), Section 5 (Definitions 5.3, 5.8, 5.10; Theorem 5.11; Table 5.3) and Section 7, **Question 7.10** (`q:supremum`, lines 2049–2052):

> **Question 7.10 (`q:supremum`).** Is the supremum of $\pi_C(S)$ over all uniformly descending periodic sets $S$ equal to $\log_3 2$? Modulo $16$ the largest value is $73/174 = 0.420$ (Table 5.3).

**Answer:** **YES.** The supremum of $\pi_C(S)$ over all uniformly descending periodic sets $S$ (periodic modulo a power of $2$) and all closed classes $C$ of $\mathcal{R}_k(S)$ is equal to $\log_3 2$.

More precisely, we prove the following stronger statement.

> **Main Theorem.**
> 1. For every $k \ge 1$, every uniformly descending set $S \subseteq \mathbb{N}$ periodic modulo $2^k$, and every closed class $C$ of $\mathcal{R}_k(S)$, we have $\pi_C(S) < \log_3 2$.
> 2. Conversely, for every $\varepsilon > 0$, there exists $n \ge 2$ and an explicit uniformly descending set $S_n \subseteq \mathbb{N}$ periodic modulo $2^n$ such that **every** closed class $C$ of $\mathcal{R}_n(S_n)$ satisfies
>    $$\pi_C(S_n) > \log_3 2 - \varepsilon,$$
>    and indeed its unique stationary distribution $\mu_C$ satisfies $\|\mu_C - \lambda_n\|_{\mathrm{TV}} < \varepsilon$, where $\lambda_n$ is the uniform distribution on $\mathbb{Z}/2^n\mathbb{Z}$.
>
> Consequently, $\sup_{S, C} \pi_C(S) = \log_3 2$.

---

## 1. Preliminaries and the Upper Bound $\pi_C(S) < \log_3 2$

Recall the exact definitions from `arXiv:2611.20344v2`, Section 1 (Definition 1.1) and Section 5 (Definitions 5.3, 5.8, 5.10).

- For $x \in \mathbb{N} = \{1, 2, 3, \dots\}$, let $U(x) := \lceil 3x/2 \rceil = (3x + (x \bmod 2))/2$ and $D(x) := \lceil x/2 \rceil = (x + (x \bmod 2))/2$. For $S \subseteq \mathbb{N}$, $T_S(x) := U(x)$ if $x \in S$ and $T_S(x) := D(x)$ if $x \notin S$.
- Let $k \ge 1$, $M = 2^k$, and let $S \subseteq \mathbb{N}$ be periodic modulo $M$ (meaning $x \in S \iff x + M \in S$ for all $x \ge 1$), identified with a subset of $\mathbb{Z}/M\mathbb{Z}$. For each residue $r \in \mathbb{Z}/M\mathbb{Z}$ with representative $\hat{r} \in \{1, \dots, M\}$, set
  $$g_S(r) := \begin{cases} U(\hat{r}) \bmod M & \text{if } r \in S, \\ D(\hat{r}) \bmod M & \text{if } r \notin S. \end{cases}$$
  The *residue graph* $\mathcal{R}_k(S)$ (Definition 5.3) is the directed graph on $\mathbb{Z}/M\mathbb{Z}$ with the two distinct out-edges $r \to g_S(r)$ and $r \to g_S(r) + M/2 \pmod M$ at each vertex $r$. The *residue chain* is the Markov chain on $\mathbb{Z}/M\mathbb{Z}$ with transition matrix $P_S$ taking each of the two out-edges with probability $1/2$.
  Notice that for every $x \in \mathbb{Z}$ with $x \equiv r \pmod M$, the two successors of $r$ in $\mathcal{R}_k(S)$ are precisely the two residues $s \in \mathbb{Z}/M\mathbb{Z}$ satisfying $s \equiv U(x) \pmod{M/2}$ (if $r \in S$) or $s \equiv D(x) \pmod{M/2}$ (if $r \notin S$), where for any $x \in \mathbb{Z}$ we extend $U(x) := (3x + e)/2$ and $D(x) := (x + e)/2$ with $e \in \{0, 1\}$, $e \equiv x \pmod 2$. Indeed, writing $x = \hat{r} + q M$ gives $U(x) = U(\hat{r}) + 3q(M/2) \equiv U(\hat{r}) \pmod{M/2}$ and $D(x) = D(\hat{r}) + q(M/2) \equiv D(\hat{r}) \pmod{M/2}$ (in particular $r = 0$ and $\hat{r} = M$ give the exact same pair of successors $\{0, M/2\}$).
- A *closed class* $C$ of $\mathcal{R}_k(S)$ (Definition 5.8) is a strongly connected component with no outgoing edges (a sink SCC). On $C$, $P_S$ restricts to an irreducible finite Markov chain with a unique stationary probability distribution $\mu_C$, and the *effective up-frequency* is
  $$\pi_C(S) := \sum_{r \in C \cap S} \mu_C(r).$$
  Every finite directed graph has at least one sink SCC, so $\mathcal{R}_k(S)$ always admits at least one closed class.
- $S$ is *uniformly descending* (Definition 5.10) if every directed cycle of $\mathcal{R}_k(S)$ of length $\ell \ge 1$ containing $a$ vertices in $S$ satisfies $3^a < 2^\ell$, equivalently $a/\ell < \log_3 2$.

### Proof of Part 1 (Upper Bound)

Let $S \subseteq \mathbb{Z}/2^k\mathbb{Z}$ be uniformly descending and let $C$ be a closed class of $\mathcal{R}_k(S)$ with stationary distribution $\mu_C$. Since $\mathcal{R}_k(S)$ is finite, it has only finitely many simple directed cycles, so
$$\mu^* := \max\left\{\frac{a}{\ell} : \text{simple directed cycle of } \mathcal{R}_k(S) \text{ of length } \ell \text{ with } a \text{ vertices in } S\right\} < \log_3 2.$$
Assign each directed edge $u \to v$ of $\mathcal{R}_k(S)$ the weight $w(u \to v) := \mu^* - \mathbf{1}_{u \in S}$. Every simple directed cycle has nonnegative total weight, hence every directed walk starting from any vertex has weight bounded below. Define for each $u \in C$
$$h(u) := \inf\left\{\sum_{i=0}^{t-1} \bigl(\mu^* - \mathbf{1}_{u_i \in S}\bigr) : t \ge 0,\ u = u_0 \to u_1 \to \dots \to u_t \text{ in } C\right\} \in (-\infty, 0],$$
which is finite because every walk can be decomposed into a simple path (of length $< |C|$) and simple cycles of nonnegative weight. For every directed edge $u \to v$ in $C$, prepending $u \to v$ to any walk from $v$ gives $h(u) \le (\mu^* - \mathbf{1}_{u \in S}) + h(v)$, i.e.,
$$\mathbf{1}_{u \in S} - \mu^* \le h(v) - h(u).$$
Averaging over the two out-edges of $u$ and integrating against $\mu_C$ (using $\sum_{u \in C} \mu_C(u) (P_S h)(u) = \sum_{v \in C} (\mu_C P_S)(v) h(v) = \sum_{v \in C} \mu_C(v) h(v)$) yields
$$\pi_C(S) - \mu^* = \sum_{u \in C} \mu_C(u)\bigl(\mathbf{1}_{u \in S} - \mu^*\bigr) \le \sum_{u \in C} \mu_C(u)\bigl((P_S h)(u) - h(u)\bigr) = 0.$$
Thus $\pi_C(S) \le \mu^* < \log_3 2$. (This also appears in Vasilyev §5.4 via circulation decomposition.) $\square$

---

## 2. Dyadic-Shell Base Sets and Exact $2$-adic Isometry

To prove Part 2, we first construct a family of periodic base sets $S_0(J)$ whose densities are dense in $[1/2, 1)$ and whose $2$-adic dynamics are *isometrically conjugate* to the one-sided full $2$-shift.

For any integer $m \ge 2$ and any subset $J \subseteq \{0, 1, \dots, m - 2\}$, define the periodic set $S_0 = S_0(J) \subseteq \mathbb{Z}/2^m\mathbb{Z}$ by
$$S_0(J) := \{r \in \mathbb{Z}/2^m\mathbb{Z} : r \text{ is odd}\} \cup \{r \in \mathbb{Z}/2^m\mathbb{Z} : r \equiv 2u \pmod{2^m},\ 1 \le u < 2^{m-1},\ v_2(u) \in J\},$$
where $v_2(u) := \max\{j \ge 0 : 2^j \mid u\}$ is the $2$-adic valuation (with $v_2(0) := \infty$).

Observe that for any $x = 2u \in \mathbb{Z}_2$ (the ring of $2$-adic integers):
- If $v_2(u) \in J$, then $v_2(u) \le m - 2$, so $x \not\equiv 0 \pmod{2^m}$ and $v_2(u)$ depends only on $x \bmod 2^m$ (for any $u' \equiv u \pmod{2^{m-1}}$, $v_2(u' - u) \ge m - 1 > v_2(u)$ implies $v_2(u') = v_2(u)$).
- If $v_2(u) \ge m - 1$ (including $x = 0$ and $x \equiv 2^m \pmod{2^m}$), then $v_2(u) \notin J$, so $x \bmod 2^m \notin S_0(J)$.

Hence the membership predicate $x \bmod 2^m \in S_0(J)$ is equivalent on all of $\mathbb{Z}_2$ to "$x$ is odd, or $x = 2u$ with $v_2(u) \in J$".

For each $j \in \{0, \dots, m - 2\}$, the number of $u \in \{1, \dots, 2^{m-1} - 1\}$ with $v_2(u) = j$ is $2^{m - 2 - j}$ (writing $u = 2^j(2w + 1)$ with $0 \le w < 2^{m - 2 - j}$). Combined with the $2^{m-1}$ odd residues modulo $2^m$, the density of $S_0(J)$ is
$$\lambda(S_0) := \frac{|S_0(J)|}{2^m} = \frac{1}{2} + \sum_{j \in J} 2^{-(j + 2)}.$$
As $m \ge 2$ and $J \subseteq \{0, \dots, m - 2\}$ vary, $\lambda(S_0)$ ranges over all dyadic rationals in $[1/2, 1)$ (every binary expansion $0.1\,b_0 b_1 \dots b_{m-2}$ with $b_j = \mathbf{1}_{j \in J}$).

Define the map $T_{S_0} : \mathbb{Z}_2 \to \mathbb{Z}_2$ by
$$T_{S_0}(x) := \begin{cases} (3x + 1)/2 & \text{if } x \text{ is odd}, \\ 3x/2 & \text{if } x = 2u \text{ is even and } v_2(u) \in J, \\ x/2 & \text{if } x = 2u \text{ is even and } v_2(u) \notin J. \end{cases}$$
On $\mathbb{N} \subset \mathbb{Z}_2$, this agrees identically with Vasilyev's map $T_{S_0}$.

### Lemma 1 (Exact $2$-adic Isometry and De Bruijn Mixing)
Fix $m \ge 2$ and $J \subseteq \{0, \dots, m - 2\}$, and let $S_0 = S_0(J)$.
- **(a) Forward Lipschitz property:** For all $x, x' \in \mathbb{Z}_2$ and all integers $d \ge 1$,
  $$x \equiv x' \pmod{2^d} \implies T_{S_0}(x) \equiv T_{S_0}(x') \pmod{2^{d-1}}.$$
- **(b) Exact $1/2$-contracting inverse branches:** Every $y \in \mathbb{Z}_2$ has exactly two preimages under $T_{S_0}$: a unique odd preimage $x_1(y) := 3^{-1}(2y - 1)$ and a unique even preimage
  $$x_0(y) := \begin{cases} 2 \cdot 3^{-1} y & \text{if } v_2(y) \in J, \\ 2y & \text{if } v_2(y) \notin J. \end{cases}$$
  For both $b \in \{0, 1\}$ and all $y, y' \in \mathbb{Z}_2$,
  $$v_2\bigl(x_b(y) - x_b(y')\bigr) = 1 + v_2(y - y').$$
- **(c) Exact De Bruijn conjugacy:** For every $n \ge 1$, the parity-coding map
  $$\Phi_n : \mathbb{Z}/2^n\mathbb{Z} \longrightarrow \{0, 1\}^n, \qquad \Phi_n(r) := \bigl(T_{S_0}^0(r) \bmod 2,\ T_{S_0}^1(r) \bmod 2,\ \dots,\ T_{S_0}^{n-1}(r) \bmod 2\bigr)$$
  is well-defined and bijective. For every $n \ge m$, let $S_0^{(n)} := \{r \in \mathbb{Z}/2^n\mathbb{Z} : r \bmod 2^m \in S_0\}$ and let $P_0$ be the transition matrix of $\mathcal{R}_n(S_0^{(n)})$. Then $\Phi_n$ conjugates $P_0$ to the uniform random walk on the $n$-bit binary De Bruijn graph $\{0, 1\}^n$ (from $(b_0, \dots, b_{n-1})$ to $(b_1, \dots, b_{n-1}, 0)$ and $(b_1, \dots, b_{n-1}, 1)$ with probability $1/2$ each). In particular,
  $$P_0^n = \mathbf{1}\lambda_n^\top,$$
  meaning $(P_0^n)(y, z) = 2^{-n}$ for all $y, z \in \mathbb{Z}/2^n\mathbb{Z}$.

*Proof.*
**(a)** Suppose $v_2(x - x') \ge d \ge 1$. Then $x$ and $x'$ have the same parity.
- If $x, x'$ are odd, $T_{S_0}(x) - T_{S_0}(x') = \frac{3}{2}(x - x')$, so $v_2(T_{S_0}(x) - T_{S_0}(x')) = v_2(x - x') - 1 \ge d - 1$.
- If $x = 2u$ and $x' = 2u'$ are even, then $v_2(u - u') \ge d - 1$. If $v_2(u) < d - 1$, the ultrametric inequality yields $v_2(u') = v_2(u)$, so $u, u'$ use the same multiplier $c \in \{1, 3\}$ and $v_2(T_{S_0}(x) - T_{S_0}(x')) = v_2(c(u - u')) \ge d - 1$. If instead $v_2(u) \ge d - 1$, then also $v_2(u') \ge d - 1$; since $T_{S_0}(2u) \in \{u, 3u\}$ and $T_{S_0}(2u') \in \{u', 3u'\}$, both $T_{S_0}(x)$ and $T_{S_0}(x')$ have valuation at least $d - 1$, so $v_2(T_{S_0}(x) - T_{S_0}(x')) \ge d - 1$.

**(b)** Since $3$ is a unit in $\mathbb{Z}_2$ ($v_2(3) = 0$), $(3x + 1)/2 = y$ has the unique solution $x = 3^{-1}(2y - 1)$, which is odd ($2y - 1$ is odd). For an even $x = 2u$, $T_{S_0}(2u) = c u$ with $c \in \{1, 3\}$ satisfies $v_2(T_{S_0}(2u)) = v_2(u)$. Thus $T_{S_0}(2u) = y$ forces $v_2(u) = v_2(y)$, which uniquely determines whether $v_2(u) \in J$: if $v_2(y) \in J$ the unique solution is $u = 3^{-1} y$ (which indeed satisfies $v_2(u) = v_2(y) \in J$ and $T_{S_0}(2u) = 3u = y$), and if $v_2(y) \notin J$ the unique solution is $u = y$ (which satisfies $v_2(u) = v_2(y) \notin J$ and $T_{S_0}(2u) = u = y$).

For the $2$-adic valuation identity, let $y \neq y' \in \mathbb{Z}_2$:
- For $b = 1$: $x_1(y) - x_1(y') = 2 \cdot 3^{-1}(y - y')$, so $v_2(x_1(y) - x_1(y')) = 1 + v_2(y - y')$.
- For $b = 0$: if $v_2(y) = v_2(y')$, then $y$ and $y'$ fall in the same branch ($v_2 \in J$ or $v_2 \notin J$), so $x_0(y) - x_0(y') = 2c(y - y')$ with $c \in \{1, 3^{-1}\}$, giving $v_2 = 1 + v_2(y - y')$. If $v_2(y) \neq v_2(y')$, say $v_2(y) < v_2(y')$, then $v_2(y - y') = v_2(y)$, whereas $v_2(x_0(y)) = 1 + v_2(y) < 1 + v_2(y') = v_2(x_0(y'))$; by the strong ultrametric triangle inequality, $v_2(x_0(y) - x_0(y')) = 1 + v_2(y) = 1 + v_2(y - y')$.

**(c)** By iterating (a) $i$ times ($0 \le i \le n - 1$), $T_{S_0}^i(x) \bmod 2^{n - i}$ — and hence $T_{S_0}^i(x) \bmod 2$ — depends only on $x \bmod 2^n$, so $\Phi_n$ is well-defined. We prove $\Phi_n$ is bijective by induction on $n \ge 1$. For $n = 1$, $\Phi_1(r) = (r \bmod 2)$ is the identity. Assuming $\Phi_n$ is bijective, take any $(b_0, b_1, \dots, b_n) \in \{0, 1\}^{n+1}$ and let $y \in \mathbb{Z}/2^n\mathbb{Z}$ be the unique class with $\Phi_n(y) = (b_1, \dots, b_n)$. By (b), $x_{b_0}(y) \bmod 2^{n+1}$ is well-defined and is the unique class $r \in \mathbb{Z}/2^{n+1}\mathbb{Z}$ with $r \equiv b_0 \pmod 2$ and $T_{S_0}(r) \equiv y \pmod{2^n}$, i.e., the unique class with $\Phi_{n+1}(r) = (b_0, b_1, \dots, b_n)$.

Now let $n \ge m$. For any $r \in \mathbb{Z}/2^n\mathbb{Z}$ with $\Phi_n(r) = (b_0, b_1, \dots, b_{n-1})$, its two successors $s_1, s_2$ in $\mathcal{R}_n(S_0^{(n)})$ are distinct modulo $2^n$ and both satisfy $s_j \equiv T_{S_0}(r) \pmod{2^{n-1}}$. By (a), the first $n - 1$ bits of $\Phi_n(s_j)$ equal $\Phi_{n-1}(T_{S_0}(r)) = (b_1, \dots, b_{n-1})$ for both $j = 1, 2$. Since $\Phi_n$ is bijective and $s_1 \neq s_2$, their last bits must differ, so $\{\Phi_n(s_1), \Phi_n(s_2)\} = \{(b_1, \dots, b_{n-1}, 0),\ (b_1, \dots, b_{n-1}, 1)\}$. Thus $\Phi_n$ conjugates $P_0$ to the binary De Bruijn walk on $\{0, 1\}^n$. After $n$ steps of the De Bruijn walk from any word, all $n$ initial bits have been shifted out and replaced by $n$ independent uniform bits, so every state is reached with probability exactly $2^{-n}$. $\square$

---

## 3. The Barina First-Exit Sieve and Uniform Descent

Fix $m \ge 2$, $J \subseteq \{0, \dots, m - 2\}$, a threshold $\mu$ satisfying
$$\lambda(S_0) < \mu < \log_3 2,$$
and a horizon integer $L \ge 1$. Set
$$n := m + L - 1 \ge m.$$
For any $r \in \mathbb{Z}/2^n\mathbb{Z}$ and $0 \le i \le L - 1$, Lemma 1(a) implies $T_{S_0}^i(r) \bmod 2^{n - i}$ is well-defined; since $n - i \ge n - (L - 1) = m$, the indicator $\mathbf{1}_{T_{S_0}^i(r) \in S_0} := \mathbf{1}_{(T_{S_0}^i(r) \bmod 2^m) \in S_0}$ is well-defined on $\mathbb{Z}/2^n\mathbb{Z}$. Define the partial sums
$$W_j(r) := \sum_{i=0}^{j-1} \bigl(\mathbf{1}_{T_{S_0}^i(r) \in S_0} - \mu\bigr) \qquad (1 \le j \le L),$$
the *bad set*
$$B_n := \bigl\{r \in \mathbb{Z}/2^n\mathbb{Z} : W_j(r) \ge 0 \text{ for all } j \in \{1, \dots, L\}\bigr\},$$
and the sieved periodic set
$$S_n := S_0^{(n)} \setminus B_n \subseteq \mathbb{Z}/2^n\mathbb{Z}.$$
Note that $B_n \subseteq S_0^{(n)}$ automatically: if $r \notin S_0^{(n)}$, then $W_1(r) = -\mu < 0$, so $r \notin B_n$.

Define the stopping time $\tau : \mathbb{Z}/2^n\mathbb{Z} \to \{1, \dots, L\}$ by
$$\tau(r) := \begin{cases} 1 & \text{if } r \in B_n, \\ \min\{j \in \{1, \dots, L\} : W_j(r) < 0\} & \text{if } r \notin B_n. \end{cases}$$

### Lemma 2 (First-Exit Lockout and Uniform Descent)
Let $P_n$ be the transition matrix of $\mathcal{R}_n(S_n)$.
- **(a) Lockout and negative weight:** For every $r \in \mathbb{Z}/2^n\mathbb{Z}$ and every directed path $r = u_0 \to u_1 \to \dots \to u_{\tau(r)}$ of length $\tau(r)$ in $\mathcal{R}_n(S_n)$,
  $$\sum_{s=0}^{\tau(r)-1} \bigl(\mathbf{1}_{u_s \in S_n} - \mu\bigr) < 0.$$
  Moreover, if $r \notin B_n$, then for every $s \in \{0, 1, \dots, \tau(r) - 1\}$ we have
  $$u_s \equiv T_{S_0}^s(r) \pmod{2^{n - s}} \qquad \text{and} \qquad u_s \notin B_n.$$
- **(b) Uniform descent:** The periodic set $S_n$ is uniformly descending; in fact every directed cycle of $\mathcal{R}_n(S_n)$ of length $\ell$ with $a$ vertices in $S_n$ satisfies $a / \ell < \mu < \log_3 2$ (hence $3^a < 2^\ell$).

*Proof.*
**(a)** If $r \in B_n$, then $\tau(r) = 1$ and $r \notin S_n$, so the sum is $\mathbf{1}_{r \in S_n} - \mu = -\mu < 0$.

Now suppose $r \notin B_n$, and let $r = u_0 \to u_1 \to \dots \to u_{\tau(r)}$ be any directed path in $\mathcal{R}_n(S_n)$. We prove by induction on $s \in \{0, 1, \dots, \tau(r) - 1\}$ that $u_s \equiv T_{S_0}^s(r) \pmod{2^{n - s}}$ and $u_s \notin B_n$.
- Base $s = 0$: $u_0 = r \equiv T_{S_0}^0(r) \pmod{2^n}$ and $u_0 = r \notin B_n$.
- Inductive step ($1 \le s \le \tau(r) - 1$): Assume the claim holds for $s - 1$. Since $u_{s-1} \notin B_n$, we have $u_{s-1} \in S_n \iff u_{s-1} \in S_0^{(n)}$, so the edge $u_{s-1} \to u_s$ in $\mathcal{R}_n(S_n)$ satisfies $u_s \equiv T_{S_0}(u_{s-1}) \pmod{2^{n-1}}$. Since $u_{s-1} \equiv T_{S_0}^{s-1}(r) \pmod{2^{n - s + 1}}$ and $n - s + 1 \ge 2$, Lemma 1(a) gives $T_{S_0}(u_{s-1}) \equiv T_{S_0}^s(r) \pmod{2^{n - s}}$. Because $n - s \le n - 1$, it follows that
  $$u_s \equiv T_{S_0}^s(r) \pmod{2^{n - s}}.$$
  To show $u_s \notin B_n$, set $j' := \tau(r) - s \in \{1, \dots, L - 1\}$. For every $0 \le i \le j' - 1 = \tau(r) - s - 1$, iterating Lemma 1(a) $i$ times yields
  $$T_{S_0}^i(u_s) \equiv T_{S_0}^{s + i}(r) \pmod{2^{n - s - i}}.$$
  Here the exponent satisfies $n - s - i \ge n - (\tau(r) - 1) = (m + L - 1) - \tau(r) + 1 = m + L - \tau(r) \ge m$ (as $\tau(r) \le L$). Hence $T_{S_0}^i(u_s) \equiv T_{S_0}^{s + i}(r) \pmod{2^m}$ for all $0 \le i \le j' - 1$, so
  $$W_{j'}(u_s) = \sum_{i=0}^{j'-1} \bigl(\mathbf{1}_{T_{S_0}^{s+i}(r) \in S_0} - \mu\bigr) = W_{\tau(r)}(r) - W_s(r).$$
  By definition of $\tau(r)$ as the *minimum* index with negative partial sum, $W_{\tau(r)}(r) < 0$ while $W_s(r) \ge 0$ (as $1 \le s < \tau(r)$). Therefore $W_{j'}(u_s) < 0$, which proves $u_s \notin B_n$, completing the induction.

Finally, for every $0 \le s \le \tau(r) - 1$, we have $u_s \notin B_n$ and $n - s \ge m$, so $\mathbf{1}_{u_s \in S_n} = \mathbf{1}_{u_s \in S_0^{(n)}} = \mathbf{1}_{T_{S_0}^s(r) \in S_0}$. Summing over $s$ gives $\sum_{s=0}^{\tau(r)-1} (\mathbf{1}_{u_s \in S_n} - \mu) = W_{\tau(r)}(r) < 0$.

**(b)** Let $v_0 \to v_1 \to \dots \to v_\ell = v_0$ be any directed cycle in $\mathcal{R}_n(S_n)$ (indices read modulo $\ell$). Define $a_0 := 0$ and $a_{q+1} := a_q + \tau(v_{a_q \bmod \ell})$ for $q \ge 0$. By the pigeonhole principle among $a_0, a_1, \dots, a_\ell$, there exist $0 \le p < q \le \ell$ with $a_p \equiv a_q \pmod \ell$, so $a_q - a_p = d\ell$ for an integer $d \ge 1$. The walk $(v_{a_p \bmod \ell}, \dots, v_{a_q \bmod \ell})$ traverses the cycle exactly $d$ times and partitions into $q - p \ge 1$ segments of lengths $\tau(v_{a_t \bmod \ell})$, each of strictly negative $(\mathbf{1}_{S_n} - \mu)$-weight by (a). Thus
$$d \sum_{i=0}^{\ell-1} \bigl(\mathbf{1}_{v_i \in S_n} - \mu\bigr) < 0,$$
giving $a/\ell < \mu < \log_3 2$ and hence $3^a < 2^\ell$. $\square$

---

## 4. Exponential Decay of $\lambda_n(B_n)$

Let $\lambda_n$ be the uniform probability distribution on $\mathbb{Z}/2^n\mathbb{Z}$, and set $\delta := \mu - \lambda(S_0) > 0$.

### Lemma 3 (Explicit Exponential Tail Bound)
For all $L \ge m$,
$$\lambda_n(B_n) = \frac{|B_n|}{2^n} \le m \exp\!\bigl(-2\delta^2 \lfloor L / m \rfloor\bigr).$$

*Proof.* Let $X$ be uniformly random on $\mathbb{Z}/2^n\mathbb{Z}$. By Lemma 1(c), $\Phi_n(X) = (b_0, b_1, \dots, b_{n-1})$ is uniformly distributed on $\{0, 1\}^n$, i.e., $b_0, \dots, b_{n-1}$ are i.i.d. $\mathrm{Bernoulli}(1/2)$. For each $i \in \{0, 1, \dots, L - 1\}$, we have $i + m - 1 \le L + m - 2 = n - 1$, and by definition of $\Phi_n$ and Lemma 1(a),
$$\Phi_m\bigl(T_{S_0}^i(X) \bmod 2^m\bigr) = (b_i, b_{i+1}, \dots, b_{i+m-1}).$$
Since $\Phi_m$ is a bijection, $Z_i := \mathbf{1}_{T_{S_0}^i(X) \in S_0} = \mathbf{1}_{\Phi_m(S_0)}(b_i, \dots, b_{i+m-1})$ is a $\mathrm{Bernoulli}(p)$ random variable with $p := \lambda(S_0) \in (0, 1)$.

Partition $\{0, 1, \dots, L - 1\}$ into the $m$ residue classes $I_r := \{i \in \{0, \dots, L - 1\} : i \equiv r \pmod m\}$ for $0 \le r \le m - 1$. Since $L \ge m$, each $I_r$ has size $N_r := |I_r| \ge \lfloor L/m \rfloor \ge 1$. Distinct $i < i'$ in $I_r$ satisfy $i' \ge i + m$, so their windows $\{i, \dots, i + m - 1\}$ and $\{i', \dots, i' + m - 1\}$ are disjoint; hence $\{Z_i : i \in I_r\}$ are mutually independent $\mathrm{Bernoulli}(p)$ random variables.

If $X \in B_n$, then $W_L(X) \ge 0$, which rewrites as
$$\sum_{r=0}^{m-1} \sum_{i \in I_r} (Z_i - p - \delta) = \sum_{i=0}^{L-1} (Z_i - \mu) \ge 0.$$
Hence at least one $r \in \{0, \dots, m - 1\}$ satisfies $\sum_{i \in I_r} (Z_i - p) \ge \delta N_r$.

For any $Z \sim \mathrm{Bernoulli}(p)$ and $t \in \mathbb{R}$, set $\psi(t) := \log \mathbb{E}[e^{t(Z - p)}] = \log(1 - p + p e^t) - pt$. Then $\psi(0) = 0$, $\psi'(t) = q(t) - p$ where $q(t) := \frac{p e^t}{1 - p + p e^t} \in (0, 1)$ (so $\psi'(0) = 0$), and $\psi''(t) = q(t)(1 - q(t)) \le 1/4$ for all $t \in \mathbb{R}$. By Taylor's theorem, $\psi(t) \le t^2 / 8$ for all $t \in \mathbb{R}$. Choosing $t = 4\delta > 0$, Markov's inequality and independence yield, for each $r$,
$$\mathbb{P}\!\left(\sum_{i \in I_r} (Z_i - p) \ge \delta N_r\right) \le e^{-t \delta N_r} \prod_{i \in I_r} \mathbb{E}\bigl[e^{t(Z_i - p)}\bigr] \le e^{-t \delta N_r + N_r t^2 / 8} = e^{-2\delta^2 N_r} \le e^{-2\delta^2 \lfloor L / m \rfloor}.$$
Summing over $r = 0, \dots, m - 1$ gives $\lambda_n(B_n) \le m \exp(-2\delta^2 \lfloor L / m \rfloor)$. $\square$

---

## 5. Path-Multiplicity Bound via Hit-Set Uniqueness and Nested Chains

The heart of the proof is showing that the $n$-step transition probabilities $P_n^n(y, z)$ of the perturbed residue chain $\mathcal{R}_n(S_n)$ remain uniformly bounded by $O_m(L) \cdot 2^{-n}$ — completely preventing any stationary distribution from concentrating on $B_n$.

For any directed path $\gamma = (x_0 \to x_1 \to \dots \to x_n)$ of length $n$ in $\mathcal{R}_n(S_n)$, define its *hit-set*
$$\mathcal{T}(\gamma) := \bigl\{t \in \{0, 1, \dots, n - 1\} : x_t \in B_n\bigr\}.$$

### Lemma 4 (Uniqueness of a Path Given Endpoints and Hit-Set)
Fix $y, z \in \mathbb{Z}/2^n\mathbb{Z}$ and $\mathcal{T} \subseteq \{0, 1, \dots, n - 1\}$.
- **(a) Forward determination:** For every path $\gamma = (x_0 \to \dots \to x_n)$ in $\mathcal{R}_n(S_n)$ with $x_0 = y$ and $\mathcal{T}(\gamma) = \mathcal{T}$, and every $t \in \{0, 1, \dots, n - 1\}$, the residue $x_t \bmod 2^{n - t}$ is uniquely determined by $(y, \mathcal{T} \cap \{0, \dots, t - 1\})$. In particular, the parity $p_t := x_t \bmod 2 \in \{0, 1\}$ is uniquely determined by $(y, \mathcal{T})$ for all $0 \le t \le n - 1$.
- **(b) Backward uniqueness:** There is **at most one** directed path $\gamma = (x_0 \to \dots \to x_n)$ of length $n$ in $\mathcal{R}_n(S_n)$ with $x_0 = y$, $x_n = z$, and $\mathcal{T}(\gamma) = \mathcal{T}$.

*Proof.*
**(a)** Induct on $t \in \{0, 1, \dots, n - 1\}$. For $t = 0$, $x_0 = y \bmod 2^n$ is given. For $0 \le t \le n - 2$ (so $n - t \ge 2$), assume $x_t \bmod 2^{n - t}$ is uniquely determined by $(y, \mathcal{T} \cap \{0, \dots, t - 1\})$.
- If $t \in \mathcal{T}$, then $x_t \in B_n$, so $x_t \notin S_n$ and the edge $x_t \to x_{t+1}$ satisfies $x_{t+1} \equiv D(x_t) \pmod{2^{n-1}}$. Since $a \equiv b \pmod{2^d}$ ($d \ge 2$) implies $(a \bmod 2) = (b \bmod 2)$ and $D(a) - D(b) = (a - b)/2 \equiv 0 \pmod{2^{d-1}}$, the class $D(x_t) \bmod 2^{n - t - 1}$ — and hence $x_{t+1} \bmod 2^{n - (t + 1)}$ (as $n - t - 1 \le n - 1$) — is uniquely determined by $x_t \bmod 2^{n - t}$.
- If $t \notin \mathcal{T}$, then $x_t \notin B_n$, so $x_t \in S_n \iff x_t \in S_0^{(n)}$ and $x_{t+1} \equiv T_{S_0}(x_t) \pmod{2^{n-1}}$. By Lemma 1(a), $T_{S_0}(x_t) \bmod 2^{n - t - 1}$ — and hence $x_{t+1} \bmod 2^{n - (t + 1)}$ — is uniquely determined by $x_t \bmod 2^{n - t}$.

Since $n - t \ge 1$ for all $0 \le t \le n - 1$, $p_t = x_t \bmod 2$ is uniquely determined.

**(b)** Fix $(y, z, \mathcal{T})$ and suppose $\gamma = (x_0 \to \dots \to x_n)$ realizes $(y, z, \mathcal{T})$. We prove $x_t \in \mathbb{Z}/2^n\mathbb{Z}$ is uniquely determined by backward induction from $t = n$ down to $0$. The base $t = n$ is $x_n = z$. Given $x_{t+1} \in \mathbb{Z}/2^n\mathbb{Z}$ for some $0 \le t \le n - 1$, both the condition "$t \in \mathcal{T}$" and the parity $p_t = x_t \bmod 2 \in \{0, 1\}$ (from (a)) are uniquely fixed:
- If $t \in \mathcal{T}$, then $x_t \notin S_n$, so $(x_t + p_t)/2 = D(x_t) \equiv x_{t+1} \pmod{2^{n-1}}$, which uniquely forces $x_t \equiv 2 x_{t+1} - p_t \pmod{2^n}$.
- If $t \notin \mathcal{T}$, then $T_{S_0}(x_t) \equiv x_{t+1} \pmod{2^{n-1}}$ and $x_t \equiv p_t \pmod 2$. By Lemma 1(b), the unique inverse branch $x_{p_t}$ satisfies $v_2(x_{p_t}(a) - x_{p_t}(b)) = 1 + v_2(a - b)$, so $x_t \equiv x_{p_t}(x_{t+1}) \pmod{2^n}$ is uniquely determined by $x_{t+1} \bmod 2^{n-1}$.

Hence the entire path $(x_0, \dots, x_n)$ is uniquely determined by $(y, z, \mathcal{T})$. $\square$

### Lemma 5 (Nested-Chain Bound on Feasible Hit-Sets and $P_n^n(y, z)$)
For any fixed $y \in \mathbb{Z}/2^n\mathbb{Z}$, let
$$\mathcal{F}(y) := \bigl\{\mathcal{T}(\gamma) : \gamma \text{ is a directed path of length } n \text{ in } \mathcal{R}_n(S_n) \text{ starting at } y\bigr\},$$
and let $\mathcal{F}_0(y) := \{\mathcal{T} \cap \{0, 1, \dots, L - 1\} : \mathcal{T} \in \mathcal{F}(y)\}$. Then:
- **(a)** $|\mathcal{F}_0(y)| \le L + 1$ (indeed, $\mathcal{F}_0(y)$ is totally ordered by inclusion).
- **(b)** $|\mathcal{F}(y)| \le 2^{m - 1}(L + 1)$.
- **(c)** For all $y, z \in \mathbb{Z}/2^n\mathbb{Z}$,
  $$P_n^n(y, z) \le 2^{-n} \cdot 2^{m - 1}(L + 1).$$

*Proof.*
**(a)** Suppose $A_1, A_2 \in \mathcal{F}_0(y)$ agree on $\{0, 1, \dots, t - 1\}$ and disagree at some $t \in \{0, 1, \dots, L - 1\}$, with $t \in A_1$ and $t \notin A_2$. We claim that
$$A_2 \cap \{t, t + 1, \dots, L - 1\} = \emptyset.$$
Let $\gamma^{(1)} = (x_0^{(1)} \to \dots \to x_n^{(1)})$ and $\gamma^{(2)} = (x_0^{(2)} \to \dots \to x_n^{(2)})$ be length-$n$ paths from $y$ in $\mathcal{R}_n(S_n)$ with $\mathcal{T}(\gamma^{(r)}) \cap \{0, \dots, L - 1\} = A_r$ ($r = 1, 2$). Since $\mathcal{T}(\gamma^{(1)})$ and $\mathcal{T}(\gamma^{(2)})$ coincide on $\{0, \dots, t - 1\}$, Lemma 4(a) yields
$$x_t^{(2)} \equiv x_t^{(1)} \pmod{2^{n - t}}.$$
For every $0 \le i \le L - 1 - t$, iterating Lemma 1(a) $i$ times gives
$$T_{S_0}^i\bigl(x_t^{(2)}\bigr) \equiv T_{S_0}^i\bigl(x_t^{(1)}\bigr) \pmod{2^{n - t - i}},$$
and the exponent satisfies $n - t - i \ge n - (L - 1) = m$. Thus $T_{S_0}^i(x_t^{(2)}) \equiv T_{S_0}^i(x_t^{(1)}) \pmod{2^m}$ for all $0 \le i \le L - 1 - t$. Because $t \in A_1$, we have $x_t^{(1)} \in B_n$, so $W_j(x_t^{(1)}) \ge 0$ for all $1 \le j \le L$. Consequently,
$$W_j\bigl(x_t^{(2)}\bigr) = W_j\bigl(x_t^{(1)}\bigr) \ge 0 \qquad \text{for all } 1 \le j \le L - t.$$
On the other hand, $t \notin A_2$ means $x_t^{(2)} \notin B_n$, so $\tau\bigl(x_t^{(2)}\bigr) = \min\{j \in \{1, \dots, L\} : W_j(x_t^{(2)}) < 0\}$ exists and must satisfy
$$\tau\bigl(x_t^{(2)}\bigr) \ge L - t + 1.$$
Since every vertex of $\mathcal{R}_n(S_n)$ has out-degree $2 \ge 1$, we may extend the subpath $x_t^{(2)} \to x_{t+1}^{(2)} \to \dots \to x_n^{(2)}$ arbitrarily if necessary to a directed path of length $\tau(x_t^{(2)})$ starting at $x_t^{(2)}$. By Lemma 2(a), every vertex $x_{t+s}^{(2)}$ with $0 \le s < \tau(x_t^{(2)})$ lies outside $B_n$. In particular, for every $u \in \{t, t + 1, \dots, L - 1\}$ (note $0 \le u - t \le L - 1 - t < \tau(x_t^{(2)})$ and $u \le L - 1 \le n - 1$), we have $x_u^{(2)} \notin B_n$, i.e., $u \notin A_2$. This proves the claim.

It follows immediately that $\mathcal{F}_0(y)$ is totally ordered by inclusion: for any distinct $A_1, A_2 \in \mathcal{F}_0(y)$, letting $t \in \{0, \dots, L - 1\}$ be the smallest index at which they differ and assuming $t \in A_1 \setminus A_2$, the claim gives $A_2 = A_1 \cap \{0, \dots, t - 1\} \subsetneq A_1$. A strictly increasing chain of subsets of the $L$-element set $\{0, \dots, L - 1\}$ has at most $L + 1$ elements, so $|\mathcal{F}_0(y)| \le L + 1$.

**(b)** Every $\mathcal{T} \in \mathcal{F}(y)$ is determined by $\mathcal{T} \cap \{0, \dots, L - 1\} \in \mathcal{F}_0(y)$ together with $\mathcal{T} \cap \{L, \dots, n - 1\}$. Since $|\{L, \dots, n - 1\}| = n - L = m - 1$, there are at most $2^{m-1}$ choices for the suffix, giving $|\mathcal{F}(y)| \le 2^{m - 1}(L + 1)$.

**(c)** Every vertex of $\mathcal{R}_n(S_n)$ has two distinct out-edges, each taken with probability $1/2$, so every directed path of length $n$ has probability $2^{-n}$. By Lemma 4(b), at most one length-$n$ path from $y$ to $z$ can have a given hit-set $\mathcal{T} \in \mathcal{F}(y)$. Therefore,
$$P_n^n(y, z) = 2^{-n} \cdot \#\{\text{length-}n \text{ paths from } y \text{ to } z\} \le 2^{-n} |\mathcal{F}(y)| \le 2^{-n} \cdot 2^{m - 1}(L + 1). \qquad \square$$

---

## 6. Stationary Measure Convergence and Completion of the Proof

### Theorem 6 (Quantitative Lower Bound on Every Closed Class)
Let $m \ge 2$, $J \subseteq \{0, \dots, m - 2\}$, $\lambda(S_0) < \mu < \log_3 2$, $\delta := \mu - \lambda(S_0) > 0$, $L \ge m$, and $n := m + L - 1$. Then $S_n = S_0^{(n)} \setminus B_n$ is uniformly descending, and for **every** closed class $C$ of $\mathcal{R}_n(S_n)$ with stationary distribution $\mu_C$ (viewed as a row vector on $\mathbb{Z}/2^n\mathbb{Z}$ supported on $C$), we have:
1. $\mu_C(B_n) \le 2^{m - 1}(L + 1)\,\lambda_n(B_n)$;
2. $\|\mu_C - \lambda_n\|_1 \le 2n\,\mu_C(B_n)$;
3. $\pi_C(S_n) \ge \lambda(S_0) - (n + 1)\,\mu_C(B_n) \ge \lambda(S_0) - (m + L)\,2^{m - 1}(L + 1)\,m \exp\!\bigl(-2\delta^2 \lfloor L / m \rfloor\bigr)$.

*Proof.* Uniform descent of $S_n$ is Lemma 2(b). Let $C$ be any closed class of $\mathcal{R}_n(S_n)$ and $\mu_C$ its stationary distribution, so $\mu_C P_n = \mu_C$ and hence $\mu_C P_n^n = \mu_C$.

1. Using Lemma 5(c):
   $$\mu_C(B_n) = \sum_{y \in \mathbb{Z}/2^n\mathbb{Z}} \mu_C(y) \sum_{z \in B_n} P_n^n(y, z) \le \sum_{y} \mu_C(y) \cdot |B_n| \cdot 2^{-n} \cdot 2^{m - 1}(L + 1) = 2^{m - 1}(L + 1)\,\lambda_n(B_n).$$

2. By Lemma 1(c), $P_0^n = \mathbf{1}\lambda_n^\top$, so $\mu_C P_0^n = \lambda_n$. Telescoping $\mu_C(P_n^n - P_0^n)$ and using $\mu_C P_n^t = \mu_C$ gives
   $$\mu_C - \lambda_n = \mu_C\bigl(P_n^n - P_0^n\bigr) = \sum_{t=0}^{n-1} \mu_C P_n^t (P_n - P_0) P_0^{n - 1 - t} = \sum_{t=0}^{n-1} \mu_C (P_n - P_0) P_0^{n - 1 - t}.$$
   Since $P_0$ is row-stochastic, $\|v P_0\|_1 = \sum_z |\sum_x v_x P_0(x, z)| \le \sum_x |v_x| \sum_z P_0(x, z) = \|v\|_1$ for every $v \in \mathbb{R}^{2^n}$. Moreover, row $x$ of $P_n - P_0$ vanishes for every $x \notin B_n$ (where $x \in S_n \iff x \in S_0^{(n)}$) and has $\ell_1$-norm at most $2$ for every $x \in B_n$ (being the difference of two probability distributions). Hence
   $$\|\mu_C (P_n - P_0)\|_1 \le \sum_{x \in B_n} \mu_C(x) \cdot 2 = 2\,\mu_C(B_n),$$
   and summing over $t = 0, \dots, n - 1$ yields $\|\mu_C - \lambda_n\|_1 \le 2n\,\mu_C(B_n)$.

3. For any two probability distributions $p, q$ on $\mathbb{Z}/2^n\mathbb{Z}$ and any event $A$, $|p(A) - q(A)| = \frac{1}{2}(|p(A) - q(A)| + |p(A^c) - q(A^c)|) \le \frac{1}{2}\|p - q\|_1$. Applying this to $A = S_0^{(n)}$ (which has $\lambda_n(S_0^{(n)}) = \lambda(S_0)$) and using $S_n = S_0^{(n)} \setminus B_n$ with $B_n \subseteq S_0^{(n)}$:
   $$\pi_C(S_n) = \mu_C(S_0^{(n)}) - \mu_C(B_n) \ge \lambda(S_0) - \frac{1}{2}\|\mu_C - \lambda_n\|_1 - \mu_C(B_n) \ge \lambda(S_0) - (n + 1)\,\mu_C(B_n).$$
   Substituting $n + 1 = m + L$, part (1), and Lemma 3 yields the explicit bound. $\square$

### Proof of Part 2 of the Main Theorem

Given any $\varepsilon > 0$: since $3 < 4$ and $2 < 3$, we have $\frac{1}{2} < \log_3 2 < 1$. Because the dyadic rationals $\frac{1}{2} + \sum_{j \in J} 2^{-(j+2)}$ ($m \ge 2$, $J \subseteq \{0, \dots, m - 2\}$) are dense in $[1/2, 1)$, choose $m \ge 2$ and $J \subseteq \{0, \dots, m - 2\}$ such that
$$\log_3 2 - \frac{\varepsilon}{2} < \lambda(S_0) < \log_3 2.$$
Fix $\mu := \frac{1}{2}(\lambda(S_0) + \log_3 2) \in (\lambda(S_0), \log_3 2)$, so $\delta = \mu - \lambda(S_0) > 0$. As $L \to \infty$ with $m, J, \delta$ fixed,
$$(m + L)\,2^{m - 1}(L + 1)\,m \exp\!\bigl(-2\delta^2 \lfloor L / m \rfloor\bigr) \longrightarrow 0$$
exponentially fast, and similarly $\|\mu_C - \lambda_n\|_{\mathrm{TV}} = \frac{1}{2}\|\mu_C - \lambda_n\|_1 \le n \cdot 2^{m - 1}(L + 1) \cdot m \exp(-2\delta^2 \lfloor L / m \rfloor) \to 0$. Choosing $L \ge m$ sufficiently large so that both quantities are strictly less than $\varepsilon / 2$ (and $<\varepsilon$ for TV), Theorem 6 shows that $S_n$ ($n = m + L - 1$) is uniformly descending and every closed class $C$ of $\mathcal{R}_n(S_n)$ satisfies
$$\pi_C(S_n) > \lambda(S_0) - \frac{\varepsilon}{2} > \log_3 2 - \varepsilon \qquad \text{and} \qquad \|\mu_C - \lambda_n\|_{\mathrm{TV}} < \varepsilon.$$
Together with Part 1 ($\pi_C(S) < \log_3 2$ for all uniformly descending periodic $S$ and closed classes $C$), this proves
$$\sup_{S, C} \pi_C(S) = \log_3 2. \qquad \square$$

---

## 7. Exact Computational Verification

The standalone exact-arithmetic (zero-float) script [`verify.py`](file:///Users/kolinhuang/Documents/open-math/targets/vasilyev-2611.20344-q7.10/verify.py) independently verifies every definition and every lemma of this proof using exact integer and `fractions.Fraction` arithmetic:

1. **Table 5.3 baseline:** Reproduces Vasilyev's exact maximum $\pi$ values modulo $4, 8, 16$ ($1/4$, $5/18$, $73/174$) directly from Definition 5.3.
2. **Lemma 1:** Verifies exact densities, forward Lipschitz property, $2$-to-$1$ inverse branch $1/2$-similarities, bijectivity of $\Phi_n$, and the exact matrix identity $P_0^n = 2^{-n}\mathbf{1}\mathbf{1}^\top$ across multiple dyadic-shell base sets $S_0(J)$ ($m = 2, 3, 4, 5$).
3. **Lemmas 2–5 and Theorem 6:** Verifies on explicit Barina sieve instances $S_n$ (for $m = 2, 3, 4$ up to $N = 2^7 = 128$): exact lockout and negative-weight stopping time $\tau(r)$, exact Karp maximum cycle mean $\mu^* < \mu$ with $3^{a} < 2^{\ell}$, exact rational Hoeffding upper bound, exact path uniqueness for every $(y, z, \mathcal{T})$ over all $2^n$ paths from every $y \in \mathbb{Z}/2^n\mathbb{Z}$, exact total-order (nested-chain) property of $\mathcal{F}_0(y)$ and $|\mathcal{F}(y)| \le 2^{m-1}(L+1)$, and exact `Fraction` stationary distributions $\mu_C$ on every sink SCC confirming all three inequalities of Theorem 6.

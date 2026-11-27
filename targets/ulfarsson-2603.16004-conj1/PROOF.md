# Proof of Úlfarsson's Conjecture 2.9 (`arXiv:2603.16004v1`)

## 1. Exact Target Statement and Main Theorem

**Primary source.** Henning Ulfarsson, *A Permutation Avoidance Game with Reverse Replies and Monotone Traps*, `arXiv:2603.16004v1` (2026-03-16; cached source `tools/.arxiv_cache/eprint/2603.16004v1/ItsAllFunAndGamesUntilMonotonicity.tex`), Section 2 (*Basic PAP analysis*), **Conjecture 2.9** (`\label{conj:general-reverse}`, lines 371–375). The game **PAP** (*Permutations Avoiding Patterns*) and Sprague–Grundy values $\mathrm{sg}(S_n, k)$ are defined in Section 1 (Definition 1.1, lines 59–64) and Section 2 (Definition 2.1, lines 120–135; Definition 2.10, lines 380–385).

> **Conjecture 2.9 (`conj:general-reverse`).** For every $k \geq 3$, there exists $n_0(k)$ such that the reverse strategy is a winning strategy for Player II on $S_n$ for all $n \geq n_0(k)$. In particular, $\mathrm{sg}(S_n, k) = 0$ for all such $n$.

We prove Conjecture 2.9 in full for every $k \geq 3$ with an explicit polynomial threshold $n_0(k)$.

**Main Theorem.** For every integer $k \geq 3$, set
$$n_0(k) := k + \bigl((2k+1)(k-1)\bigr)^2 + 1 = 4k^4 - 4k^3 - 3k^2 + 3k + 2.$$
Then for every $n \geq n_0(k)$, the move-by-move reverse strategy is a winning strategy for Player II in PAP with pattern length $k$ starting from $S_n$. In particular, $\mathrm{sg}(S_n, k) = 0$ for all $n \geq n_0(k)$.

---

## 2. Notation, Game Preliminaries, and Reduction

For $m \geq 1$, let $S_m$ denote the set of permutations of $\{1, \dots, m\}$ in one-line notation $\pi = \pi(1)\cdots\pi(m)$, with identity $\mathrm{id}_m = 12\cdots m$ and *reverse* $\pi^r = \pi(m)\cdots\pi(1)$. We identify $\pi \in S_m$ with its *plot*
$$\Gamma(\pi) := \{(i, \pi(i)) : 1 \leq i \leq m\} \subset \mathbb{R}^2.$$
For any finite point set $S \subset \mathbb{R}^2$ whose points have pairwise distinct $x$-coordinates and pairwise distinct $y$-coordinates, its *standardization* $\mathrm{std}(S) \in S_{|S|}$ is the unique permutation obtained by ordering $S$ by increasing $x$-coordinate and replacing the $y$-coordinates by their ranks in $\{1, \dots, |S|\}$. A permutation $\pi \in S_n$ *contains* a pattern $p \in S_k$ (written $p \leq \pi$) if there exists a $k$-point subset $S \subseteq \Gamma(\pi)$ with $\mathrm{std}(S) = p$; otherwise $\pi$ *avoids* $p$. Define the *$k$-shadow* of $\pi$ by
$$\mathrm{Sh}_k(\pi) := \{p \in S_k : p \leq \pi\},$$
and for any set $F \subseteq S_k$ of forbidden patterns, set
$$\mathrm{Av}_n(F) := \{\pi \in S_n : \mathrm{Sh}_k(\pi) \cap F = \emptyset\}.$$
We say $F \subseteq S_k$ is *reverse-closed* if $F^r := \{p^r : p \in F\} = F$, and a pattern $p \in S_k$ is *legal* from $F$ (at length $n$) if $p \in \mathrm{Sh}_k(\pi)$ for at least one $\pi \in \mathrm{Av}_n(F)$ (which automatically forces $p \notin F$).

In normal-play PAP with pattern length $k$ starting from $S_n$, a position is a subset $X \subseteq S_n$, and a legal move chooses $p \in S_k$ contained in at least one $\pi \in X$ and replaces $X$ by $\{\pi \in X : p \not\leq \pi\}$. After forbidden patterns $F \subseteq S_k$ have been chosen, the current position is $\mathrm{Av}_n(F)$. Under the *move-by-move reverse strategy*, whenever Player I plays $p \in S_k$, Player II replies with $p^r \in S_k$.

Note that for every $k \geq 3$ and every $p \in S_k$, we have $p^r(1) = p(k) \neq p(1)$ (as $p$ is a bijection and $1 \neq k$), so $p^r \neq p$. We also record the elementary inequalities satisfied by $n_0(k)$ for all $k \geq 3$: since $2k + 1 \geq 7$ and $k - 1 \geq 2$,
$$(2k+1)(k-1) \geq 2(2k+1) = 4k + 2 > 2k - 2 > k,$$
and hence for every $n \geq n_0(k)$:
1. $n > (k-1)^2 + 1$;
2. $n - k \geq \bigl((2k+1)(k-1)\bigr)^2 + 1 > 2k - 2 > k$;
3. $n - k + 1 > n - k > k$.

We first give a self-contained proof of the game reduction (corresponding to Lemma 2.11, Proposition 2.12, and Corollary 2.13 of `arXiv:2603.16004v1`).

**Proposition 1 (Monotone Trap and Conditional Reverse-Reply Criterion).**
*Fix $k \geq 3$ and $n \geq (k-1)^2 + 1$. Suppose that for every reverse-closed set $F \subseteq S_k$ containing neither monotone pattern ($\mathrm{id}_k, \mathrm{id}_k^r \notin F$) and every non-monotone pattern $p \in S_k \setminus F$ legal from $F$ at length $n$, its reverse $p^r$ is legal from $F \cup \{p\}$ at length $n$. Then the move-by-move reverse strategy is a winning strategy for Player II on $S_n$, and $\mathrm{sg}(S_n, k) = 0$.*

*Proof.* We maintain the invariant that at the start of every Player I turn (initially $F = \emptyset$), the current forbidden set $F \subseteq S_k$ is reverse-closed and contains neither $\mathrm{id}_k$ nor $\mathrm{id}_k^r$. Let Player I choose a legal move $p \in S_k \setminus F$ from $\mathrm{Av}_n(F)$.
- **Case A ($p$ is non-monotone):** By hypothesis, $p^r$ is legal from $F \cup \{p\}$, so Player II can legally reply with $p^r$. Since $p^r \neq p$ and $p^r$ is also non-monotone, the updated forbidden set $F' = F \cup \{p, p^r\}$ is again reverse-closed and monotone-free, restoring the invariant.
- **Case B ($p$ is monotone):** Say $p = \mathrm{id}_k$ (the case $p = \mathrm{id}_k^r$ is symmetric). Every $k$-point subpermutation of $\mathrm{id}_n^r$ is $\mathrm{id}_k^r \notin F \cup \{\mathrm{id}_k\}$, so $\mathrm{id}_n^r \in \mathrm{Av}_n(F \cup \{\mathrm{id}_k\})$ and contains $\mathrm{id}_k^r$. Hence Player II can legally reply with $p^r = \mathrm{id}_k^r$. After this reply, both $\mathrm{id}_k$ and $\mathrm{id}_k^r$ belong to the forbidden set. Because $n \geq (k-1)^2 + 1$, the Erdős–Szekeres theorem guarantees that every permutation in $S_n$ contains either $\mathrm{id}_k$ or $\mathrm{id}_k^r$, so $\mathrm{Av}_n(F \cup \{\mathrm{id}_k, \mathrm{id}_k^r\}) = \emptyset$. No legal moves remain, and Player II wins immediately.

Because each legal move strictly adds a previously unchosen pattern to $F \subseteq S_k$ (and strictly shrinks the finite position $X \subseteq S_n$), every play terminates after at most $k!$ moves. Since Player II always has a legal reverse reply, the game must end on Player II's turn (with no legal move for Player I), proving that the move-by-move reverse strategy wins for Player II.

Finally, PAP is a finite acyclic normal-play impartial game. By induction on $|X|$, any position $X$ from which Player II has a winning strategy has $\mathrm{sg}(X) = 0$: every follower $Y \in \mathcal{F}(X)$ has a follower $Z \in \mathcal{F}(Y)$ from which Player II has a winning strategy, so $\mathrm{sg}(Z) = 0$ by the induction hypothesis, giving $\mathrm{sg}(Y) = \mathrm{mex}\{\mathrm{sg}(W) : W \in \mathcal{F}(Y)\} \neq 0$ for every $Y \in \mathcal{F}(X)$, and therefore $\mathrm{sg}(X) = \mathrm{mex}\{\mathrm{sg}(Y) : Y \in \mathcal{F}(X)\} = 0$. In particular, $\mathrm{sg}(S_n, k) = 0$. $\blacksquare$

---

## 3. Monotone 1-Point Inflations

Given $\gamma \in S_m$, an index $j \in \{1, \dots, m\}$, an integer $t \geq 1$, and a sign $\varepsilon \in \{+, -\}$, let $v := \gamma(j)$. Define the *monotone 1-point inflation* $I_t(\gamma, j, \varepsilon) \in S_{m+t-1}$ as the permutation obtained from the one-line word of $\gamma$ by:
- leaving every entry $\gamma(i) < v$ unchanged;
- replacing every entry $\gamma(i) > v$ by $\gamma(i) + t - 1$;
- replacing the single entry $\gamma(j) = v$ by the contiguous length-$t$ monotone block
  $$(v, v+1, \dots, v+t-1) \quad (\text{if } \varepsilon = +) \qquad \text{or} \qquad (v+t-1, v+t-2, \dots, v) \quad (\text{if } \varepsilon = -).$$
Equivalently, in plot terms, $I_t(\gamma, j, \varepsilon)$ is obtained from $\Gamma(\gamma)$ by replacing the single point $(j, \gamma(j))$ with a monotone chain $W$ of $t$ points of sign $\varepsilon$ inside $(j - \tfrac{1}{2}, j + \tfrac{1}{2}) \times (v - \tfrac{1}{2}, v + \tfrac{1}{2})$ and standardizing. We call $W \subseteq \Gamma(I_t(\gamma, j, \varepsilon))$ the *inflated block*.

We record three elementary properties of $I_t(\gamma, j, \varepsilon)$.

**Lemma 0 (Properties of Monotone 1-Point Inflations).**
1. *(Reversal identity)* For all $\gamma \in S_m$, $j \in \{1, \dots, m\}$, $t \geq 1$, and $\varepsilon \in \{+, -\}$,
   $$\bigl(I_t(\gamma, j, \varepsilon)\bigr)^r = I_t(\gamma^r, m + 1 - j, -\varepsilon).$$
2. *(Shadow stabilization)* For all $k \geq 1$, $\gamma \in S_m$, $j \in \{1, \dots, m\}$, $\varepsilon \in \{+, -\}$, and $t \geq k$,
   $$\mathrm{Sh}_k\bigl(I_t(\gamma, j, \varepsilon)\bigr) = \mathrm{Sh}_k\bigl(I_k(\gamma, j, \varepsilon)\bigr).$$
3. *(Contiguous monotone-block inflation)* Let $\pi \in S_n$ have a partition $\Gamma(\pi) = A \sqcup B$, where $B$ is a monotone point set of sign $\varepsilon$ all of whose points lie in the same grid cell relative to $A$ (that is, for every $(x_a, y_a) \in A$, either $x_a < x_b$ for all $(x_b, y_b) \in B$ or $x_a > x_b$ for all $(x_b, y_b) \in B$, and analogously for $y$-coordinates). Let $R \subseteq \Gamma(\pi)$ be an $m$-point subset with $\tau := \mathrm{std}(R) \in S_m$, and suppose $s := |R \cap B| \geq 1$. Let $j \in \{1, \dots, m\}$ be the first index (in $x$-order) of $R \cap B$ inside $R$. Then for every integer $t \geq 1$ with $|B| \geq t + s - 1$ and every $(t + s - 1)$-element subset $B' \subseteq B$,
   $$\mathrm{std}\bigl((R \cap A) \cup B'\bigr) = I_t(\tau, j, \varepsilon).$$

*Proof.*
(1) Reversing the one-line word reflects the plot horizontally: the $j$-th entry $\gamma(j) = v$ moves to position $m + 1 - j$ in $\gamma^r$ with the same value $v = \gamma^r(m + 1 - j)$, the contiguous length-$t$ block on values $\{v, \dots, v+t-1\}$ remains contiguous and flips its monotonicity from $\varepsilon$ to $-\varepsilon$, while entries $< v$ remain unchanged and entries $> v$ remain shifted by $t - 1$.

(2) Let $\Gamma(I_t(\gamma, j, \varepsilon)) = A_0 \sqcup W_t$, where $W_t$ is the $t$-point inflated block. Since $t \geq k$, choosing any $k$-point subset $W' \subseteq W_t$ gives $\mathrm{std}(A_0 \cup W') = I_k(\gamma, j, \varepsilon) \leq I_t(\gamma, j, \varepsilon)$, whence $\mathrm{Sh}_k(I_k(\gamma, j, \varepsilon)) \subseteq \mathrm{Sh}_k(I_t(\gamma, j, \varepsilon))$. Conversely, any $k$-point subset $S \subseteq A_0 \sqcup W_t$ intersects $W_t$ in $r := |S \cap W_t| \leq k$ points. Because all points of $W_t$ have identical left/right and above/below relations with every point of $A_0$, and every $r$-element subset of $W_t$ is a monotone $\varepsilon$-chain, replacing $S \cap W_t$ with any $r$ points of the $k$-point block $W_k$ of $I_k(\gamma, j, \varepsilon)$ preserves all pairwise coordinate comparisons; hence $\mathrm{std}(S) \in \mathrm{Sh}_k(I_k(\gamma, j, \varepsilon))$.

(3) Since $R \cap A \subseteq A$, all points of $B$ (and in particular all points of $R \cap B$ and $B'$) lie in the same grid cell relative to $R \cap A$. Let $a_0$ (resp. $b_0$) be the number of points of $R \cap A$ lying to the left of $B$ (resp. below $B$). Then in $\tau = \mathrm{std}((R \cap A) \cup (R \cap B))$, the $s$ points of $R \cap B$ occupy the contiguous positions $j, j+1, \dots, j+s-1$ (where $j = a_0 + 1$) and the contiguous values $\{b_0 + 1, \dots, b_0 + s\}$, ordered as $(b_0 + 1, \dots, b_0 + s)$ if $\varepsilon = +$, or as $(b_0 + s, \dots, b_0 + 1)$ if $\varepsilon = -$.
- If $\varepsilon = +$: $\tau(j) = b_0 + 1$. Applying $I_t(\tau, j, +)$ leaves entries $\leq b_0$ (from $R \cap A$) unchanged, replaces $\tau(j)$ with $(b_0 + 1, \dots, b_0 + t)$, shifts $\tau(j+1), \dots, \tau(j+s-1)$ to $(b_0 + t + 1, \dots, b_0 + t + s - 1)$, and shifts entries $> b_0 + s$ (from $R \cap A$) up by $t - 1$. Thus positions $j, \dots, j + t + s - 2$ hold the increasing block $(b_0 + 1, \dots, b_0 + t + s - 1)$.
- If $\varepsilon = -$: $\tau(j) = b_0 + s$. Applying $I_t(\tau, j, -)$ leaves entries $< b_0 + s$ unchanged—namely all entries $\leq b_0$ (from $R \cap A$) together with $\tau(j+1), \dots, \tau(j+s-1) = (b_0 + s - 1, \dots, b_0 + 1)$—replaces $\tau(j)$ with $(b_0 + s + t - 1, \dots, b_0 + s)$, and shifts entries $> b_0 + s$ (from $R \cap A$) up by $t - 1$. Thus positions $j, \dots, j + t + s - 2$ hold the decreasing block $(b_0 + t + s - 1, \dots, b_0 + 1)$.

In both cases, $I_t(\tau, j, \varepsilon)$ places a monotone $\varepsilon$-block of length $t + s - 1$ on positions $\{a_0 + 1, \dots, a_0 + t + s - 1\}$ and values $\{b_0 + 1, \dots, b_0 + t + s - 1\}$, while keeping all points of $R \cap A$ below $B$ in $\{1, \dots, b_0\}$ and all points of $R \cap A$ above $B$ in $\{b_0 + t + s, \dots, m + t - 1\}$ in the same relative order as in $\tau$. This matches $\mathrm{std}((R \cap A) \cup B')$ verbatim. $\blacksquare$

---

## 4. Lemma 1: Erdős–Szekeres 1-Point Inflation Extraction

**Lemma 1 (1-Point Inflation Extraction).**
*Fix $k \geq 3$, $n \geq n_0(k)$, a forbidden set $F \subseteq S_k$, and a pattern $p \in S_k$ legal from $F$ at length $n$. Then there exists a permutation $\sigma \in \mathrm{Av}_n(F)$ whose plot decomposes as $\Gamma(\sigma) = P_0 \sqcup B_0$, where:*
1. *$\mathrm{std}(P_0) = p$ (so $|P_0| = k$);*
2. *$B_0$ is a monotone point set of length $|B_0| = n - k$ and sign $\varepsilon \in \{+, -\}$;*
3. *all points of $B_0$ lie in a single grid cell relative to $P_0$.*

*Proof.* Since $p$ is legal from $F$ at length $n$, choose $\pi \in \mathrm{Av}_n(F)$ containing $p$, and fix a $k$-point subset $P \subseteq \Gamma(\pi)$ with $\mathrm{std}(P) = p$. The complement $U := \Gamma(\pi) \setminus P$ has cardinality
$$|U| = n - k \geq \bigl((2k+1)(k-1)\bigr)^2 + 1.$$
By the Erdős–Szekeres theorem (applied to $\mathrm{std}(U)$), $U$ contains a monotone subset $M \subseteq U$ of sign $\varepsilon \in \{+, -\}$ and cardinality
$$L := (2k+1)(k-1) + 1.$$

Relative to $P$, each point $z = (x, y) \in U$ determines a grid cell $(a(z), b(z)) \in \{0, 1, \dots, k\}^2$, where
$$a(z) := \#\{(x', y') \in P : x' < x\}, \qquad b(z) := \#\{(x', y') \in P : y' < y\}.$$
List the points of $M$ in increasing order of $x$-coordinate as $z_1, z_2, \dots, z_L$. Then $a(z_1) \leq a(z_2) \leq \cdots \leq a(z_L)$.
- If $\varepsilon = +$, then $y(z_1) < \cdots < y(z_L)$, so $b(z_1) \leq \cdots \leq b(z_L)$. Hence the integer sum $a(z_r) + b(z_r) \in \{0, 1, \dots, 2k\}$ is weakly increasing and increases strictly whenever $(a(z_r), b(z_r)) \neq (a(z_{r+1}), b(z_{r+1}))$.
- If $\varepsilon = -$, then $y(z_1) > \cdots > y(z_L)$, so $b(z_1) \geq \cdots \geq b(z_L)$. Hence the integer difference $a(z_r) - b(z_r) \in \{-k, -k+1, \dots, k\}$ is weakly increasing and increases strictly whenever $(a(z_r), b(z_r)) \neq (a(z_{r+1}), b(z_{r+1}))$.

In both cases, the strictly increasing invariant takes values in a set of size $2k + 1$, so $M$ visits at most $2k + 1$ distinct grid cells. Since $|M| = (2k+1)(k-1) + 1$, the pigeonhole principle yields a grid cell $(a_0, b_0)$ containing at least $k$ points of $M$. Choose a $k$-point subset $Q \subseteq M$ inside cell $(a_0, b_0)$, and fix any point $x_0 \in Q$.

Set $\beta := \mathrm{std}(P \cup \{x_0\}) \in S_{k+1}$, in which $x_0$ occupies index $i_0 := a_0 + 1 \in \{1, \dots, k+1\}$. Applying Lemma 0(3) to $P \cup Q$ (with $A = P$, $B = Q$, $R = P \cup \{x_0\}$, $s = 1$, $t = k$, and $B' = Q$) gives
$$\mathrm{std}(P \cup Q) = I_k(\beta, i_0, \varepsilon).$$
Since $P \cup Q \subseteq \Gamma(\pi)$ and $\pi \in \mathrm{Av}_n(F)$, we have $\mathrm{Sh}_k(I_k(\beta, i_0, \varepsilon)) \cap F = \emptyset$.

Now define $\sigma := I_{n-k}(\beta, i_0, \varepsilon)$. Its length is $(k+1) + (n-k) - 1 = n$. Because $n - k \geq k$, Lemma 0(2) yields
$$\mathrm{Sh}_k(\sigma) = \mathrm{Sh}_k\bigl(I_k(\beta, i_0, \varepsilon)\bigr),$$
which is disjoint from $F$, so $\sigma \in \mathrm{Av}_n(F)$. Finally, letting $B_0$ be the inflated $(n-k)$-point monotone block of sign $\varepsilon$ in $\Gamma(\sigma)$ and $P_0 := \Gamma(\sigma) \setminus B_0$, all points of $B_0$ lie in cell $(a_0, b_0)$ relative to $P_0$, and deleting $B_0$ leaves the same relative order as deleting $x_0$ from $\beta$, so $\mathrm{std}(P_0) = \mathrm{std}(P) = p$. $\blacksquare$

---

## 5. Lemma 2: Reduction to the Self-Inflation Dichotomy

**Lemma 2 (Reduction to Self-Inflation Dichotomy).**
*Fix $k \geq 3$, $n \geq n_0(k)$, a reverse-closed set $F \subseteq S_k$, and a non-monotone pattern $p \in S_k \setminus F$ legal from $F$ at length $n$. Assume Theorem 3 below holds for $p$. Then $p^r$ is legal from $F \cup \{p\}$ at length $n$.*

*Proof.* By Lemma 1, there exists $\sigma \in \mathrm{Av}_n(F)$ with $\Gamma(\sigma) = P_0 \sqcup B_0$, where $\mathrm{std}(P_0) = p$, $B_0$ is a monotone set of length $|B_0| = n - k \geq 2k - 2$ and sign $\varepsilon \in \{+, -\}$, and all points of $B_0$ lie in a single grid cell relative to $P_0$.

Because $F$ is reverse-closed and $q \leq \tau \iff q^r \leq \tau^r$, we also have $\sigma^r \in \mathrm{Av}_n(F)$. Letting $\rho: (x, y) \mapsto (n + 1 - x, y)$ denote horizontal reflection of the plot, we obtain the decomposition $\Gamma(\sigma^r) = P_0^r \sqcup B_0^r$ (with $P_0^r := \rho(P_0)$ and $B_0^r := \rho(B_0)$), where $\mathrm{std}(P_0^r) = p^r$, $B_0^r$ is a monotone set of length $n - k \geq 2k - 2$ and sign $-\varepsilon$, and all points of $B_0^r$ lie in a single grid cell relative to $P_0^r$. In particular, $p^r \in \mathrm{Sh}_k(\sigma^r)$.

- **Case 1 ($p \notin \mathrm{Sh}_k(\sigma^r)$):** Then $\sigma^r \in \mathrm{Av}_n(F \cup \{p\})$ and $p^r \leq \sigma^r$, so $p^r$ is legal from $F \cup \{p\}$.

- **Case 2 ($p \in \mathrm{Sh}_k(\sigma^r)$):** Reversing gives $p^r \in \mathrm{Sh}_k(\sigma)$. Choose a $k$-point subset $R_1 \subseteq \Gamma(\sigma)$ with $\mathrm{std}(R_1) = p^r$, and put $s_1 := |R_1 \cap B_0|$.
  - If $s_1 = 0$, then $R_1 \subseteq P_0$; since $|R_1| = |P_0| = k$, this forces $R_1 = P_0$ and hence $p^r = \mathrm{std}(R_1) = \mathrm{std}(P_0) = p$, contradicting $p^r(1) = p(k) \neq p(1)$.
  - If $s_1 = k$, then $R_1 \subseteq B_0$ is monotone, contradicting that $p$ (and hence $p^r$) is non-monotone.

  Thus $1 \leq s_1 \leq k - 1$, so $k + s_1 - 1 \leq 2k - 2 \leq n - k = |B_0|$. Fix any $(k + s_1 - 1)$-element subset $B' \subseteq B_0$, and let $j_1 \in \{1, \dots, k\}$ be the first index of $R_1 \cap B_0$ inside $R_1$. By Lemma 0(3) (with $A = P_0$, $B = B_0$, $R = R_1$, $\tau = p^r$, $t = k$),
  $$\mathrm{std}\bigl((R_1 \cap P_0) \cup B'\bigr) = I_k(p^r, j_1, \varepsilon).$$
  Since $(R_1 \cap P_0) \cup B' \subseteq \Gamma(\sigma)$ and $\sigma \in \mathrm{Av}_n(F)$, we have $\mathrm{Sh}_k(I_k(p^r, j_1, \varepsilon)) \cap F = \emptyset$.

  Define $\omega_1 := I_{n-k+1}(p^r, j_1, \varepsilon) \in S_n$. Since $n - k + 1 > k$, Lemma 0(2) gives $\mathrm{Sh}_k(\omega_1) = \mathrm{Sh}_k(I_k(p^r, j_1, \varepsilon))$, so $\omega_1 \in \mathrm{Av}_n(F)$; moreover, keeping any single point of the inflated block together with the other $k - 1$ points shows $p^r \leq \omega_1$.

  - **Subcase 2a ($p \notin \mathrm{Sh}_k(I_k(p^r, j_1, \varepsilon))$):** Then $p \notin \mathrm{Sh}_k(\omega_1)$, so $\omega_1 \in \mathrm{Av}_n(F \cup \{p\})$ contains $p^r$, making $p^r$ legal from $F \cup \{p\}$.

  - **Subcase 2b ($p \in \mathrm{Sh}_k(I_k(p^r, j_1, \varepsilon))$):** Since $\mathrm{std}((R_1 \cap P_0) \cup B') = I_k(p^r, j_1, \varepsilon)$, there exists a $k$-point subset $P_2 \subseteq (R_1 \cap P_0) \cup B' \subseteq \Gamma(\sigma)$ with $\mathrm{std}(P_2) = p$. Set $s_2 := |P_2 \cap B_0|$. Because $P_2 \setminus B_0 \subseteq R_1 \cap P_0$ and $|R_1 \cap P_0| = k - s_1 \leq k - 1$, we have
    $$s_2 = |P_2| - |P_2 \setminus B_0| \geq k - (k - s_1) = s_1 \geq 1.$$
    Because $p$ is non-monotone and $B_0$ is monotone, we also have $s_2 \leq k - 1$.

    Now apply horizontal reflection $\rho$ to obtain $R_2 := \rho(P_2) \subseteq \Gamma(\sigma^r)$. Then $\mathrm{std}(R_2) = p^r$ and $|R_2 \cap B_0^r| = s_2 \in \{1, \dots, k - 1\}$. Since $k + s_2 - 1 \leq 2k - 2 \leq n - k = |B_0^r|$, fix any $(k + s_2 - 1)$-element subset $B'' \subseteq B_0^r$, and let $j_2 \in \{1, \dots, k\}$ be the first index of $R_2 \cap B_0^r$ inside $R_2$. Applying Lemma 0(3) to $\Gamma(\sigma^r) = P_0^r \sqcup B_0^r$ (of sign $-\varepsilon$) yields
    $$\mathrm{std}\bigl((R_2 \cap P_0^r) \cup B''\bigr) = I_k(p^r, j_2, -\varepsilon) \leq \sigma^r \in \mathrm{Av}_n(F).$$
    Define $\omega_2 := I_{n-k+1}(p^r, j_2, -\varepsilon) \in S_n$. By Lemma 0(2), $\mathrm{Sh}_k(\omega_2) = \mathrm{Sh}_k(I_k(p^r, j_2, -\varepsilon))$ is disjoint from $F$, so $\omega_2 \in \mathrm{Av}_n(F)$, and again $p^r \leq \omega_2$.

    Finally, since $\{\varepsilon, -\varepsilon\} = \{+, -\}$ and we are in Subcase 2b where $p \in \mathrm{Sh}_k(I_k(p^r, j_1, \varepsilon))$, **Theorem 3** forces
    $$p \notin \mathrm{Sh}_k\bigl(I_k(p^r, j_2, -\varepsilon)\bigr) = \mathrm{Sh}_k(\omega_2).$$
    Therefore $\omega_2 \in \mathrm{Av}_n(F \cup \{p\})$ contains $p^r$, so $p^r$ is legal from $F \cup \{p\}$. $\blacksquare$

---

## 6. Theorem 3: The Self-Inflation Dichotomy

For any permutation $\pi \in S_r$, define its ascent and descent counts by
$$\mathrm{asc}(\pi) := \#\{i \in \{1, \dots, r-1\} : \pi(i) < \pi(i+1)\}, \qquad \mathrm{des}(\pi) := \#\{i \in \{1, \dots, r-1\} : \pi(i) > \pi(i+1)\}.$$
Clearly $\mathrm{asc}(\pi^r) = \mathrm{des}(\pi)$ and $\mathrm{des}(\pi^r) = \mathrm{asc}(\pi)$.

**Theorem 3 (Self-Inflation Dichotomy).**
*For every integer $k \geq 3$ and every non-monotone permutation $p \in S_k$, there do not exist indices $j_1, j_2 \in \{1, \dots, k\}$ such that simultaneously*
$$p \in \mathrm{Sh}_k\bigl(I_k(p^r, j_1, +)\bigr) \qquad \text{and} \qquad p \in \mathrm{Sh}_k\bigl(I_k(p^r, j_2, -)\bigr).$$

We prove Theorem 3 via two elementary claims.

**Claim 3A (Monotone-block collapse from $I_k(p^r, j, \varepsilon)$).**
*Let $k \geq 3$, let $p \in S_k$ be non-monotone, and suppose $p \in \mathrm{Sh}_k(I_k(p^r, j, \varepsilon))$ for some $j \in \{1, \dots, k\}$ and $\varepsilon \in \{+, -\}$. Then there exists an integer $m$ with $2 \leq m \leq k - 1$ and a permutation $q \in S_m$ such that:*
1. *$q \leq p^r$, equivalently $q^r \leq p$;*
2. *$\mathrm{des}(q) = \mathrm{des}(p)$ if $\varepsilon = +$, and $\mathrm{asc}(q) = \mathrm{asc}(p)$ if $\varepsilon = -$;*
3. *$p(1) < p(k) \iff q(1) < q(m)$.*

*Proof of Claim 3A.* Write $\Gamma(I_k(p^r, j, \varepsilon)) = A \sqcup W$, where $W$ is the $k$-point inflated block of sign $\varepsilon$ and $|A| = k - 1$. Fix a $k$-point subset $S \subseteq A \sqcup W$ with $\mathrm{std}(S) = p$, and put $t := |S \cap W|$.
- Since $|A| = k - 1 < k$, we have $t \geq 1$.
- If $t = 1$, then $S = A \cup \{w_0\}$ for the unique point $w_0 \in S \cap W$; by definition of 1-point inflation, $\mathrm{std}(A \cup \{w_0\}) = p^r$, forcing $p = p^r$, impossible since $p(1) \neq p(k) = p^r(1)$ for $k \geq 3$. Thus $t \geq 2$.
- Since $p$ is non-monotone and $W$ is monotone, $t \leq k - 1$.

Hence $2 \leq t \leq k - 1$, so $m := k - t + 1$ satisfies $2 \leq m \leq k - 1$. Let $w_0$ be the leftmost point (smallest $x$-coordinate) of $S \cap W$, set $S' := (S \cap A) \cup \{w_0\}$, and define $q := \mathrm{std}(S') \in S_m$.
1. Since $S' \subseteq A \cup \{w_0\}$ and $\mathrm{std}(A \cup \{w_0\}) = p^r$, we have $q \leq p^r$, equivalently $q^r \leq p$.
2. Because all points of $S \cap W$ lie in the same grid cell relative to $S \cap A$ and form a monotone $\varepsilon$-chain of length $t$, inside $p = \mathrm{std}(S)$ the points of $S \cap W$ occupy a contiguous index interval $B = \{a, a+1, \dots, a+t-1\} \subseteq \{1, \dots, k\}$ whose entries $\{p(i) : i \in B\}$ form a contiguous value interval $\{b, b+1, \dots, b+t-1\} \subseteq \{1, \dots, k\}$, ordered increasingly if $\varepsilon = +$ and decreasingly if $\varepsilon = -$. Since $w_0$ corresponds to index $a$, $q = \mathrm{std}(p')$ where $p'$ is the length-$m$ subsequence obtained from $p$ by deleting positions $a+1, \dots, a+t-1$:
   $$p' = \bigl(p(1), \dots, p(a-1), \, p(a), \, p(a+t), \dots, p(k)\bigr).$$
   Standardization preserves all pairwise comparisons, so $\mathrm{asc}(q) = \mathrm{asc}(p')$ and $\mathrm{des}(q) = \mathrm{des}(p')$. Compare the consecutive pairs of $p'$ against those of $p$:
   - Every pair $(p(i), p(i+1))$ with $i \leq a - 1$ or $i \geq a + t$ appears identically in $p$ and $p'$.
   - The $t - 1$ internal pairs $(p(i), p(i+1))$ for $a \leq i \leq a + t - 2$ are deleted; all $t - 1$ are ascents if $\varepsilon = +$, and all $t - 1$ are descents if $\varepsilon = -$.
   - If $a + t \leq k$, the single right-boundary pair $(p(a+t-1), p(a+t))$ of $p$ is replaced in $p'$ by $(p(a), p(a+t))$. Since $p(a), p(a+t-1) \in \{b, \dots, b+t-1\}$ while $p(a+t) \notin \{b, \dots, b+t-1\}$ (as $p$ is a bijection and $a + t \notin B$), either $p(a+t) < b$ or $p(a+t) > b + t - 1$; in either case $p(a) < p(a+t) \iff p(a+t-1) < p(a+t)$.

   Therefore $\mathrm{des}(q) = \mathrm{des}(p)$ when $\varepsilon = +$, and $\mathrm{asc}(q) = \mathrm{asc}(p)$ when $\varepsilon = -$.
3. Because $|B| = t \leq k - 1 < k$, $B$ cannot contain both $1$ and $k$. We check $p(1) < p(k) \iff p'(1) < p'(m) \iff q(1) < q(m)$ in the three remaining cases:
   - If $k \notin B$ (whether $1 \notin B$ or $1 \in B$, in which case $a = 1$), then $p'(1) = p(1)$ and $p'(m) = p(k)$ identically.
   - If $k \in B$ (so $a + t - 1 = k$ and $1 \notin B$), then $p'(1) = p(1)$ and $p'(m) = p(a)$. Because $p(a), p(k) \in \{b, \dots, b+t-1\}$ while $p(1) \notin \{b, \dots, b+t-1\}$, we have $p(1) < p(k) \iff p(1) < b \iff p(1) < p(a) \iff p'(1) < p'(m)$. $\blacksquare$

**Claim 3B (Subpermutation Ascent/Descent Monotonicity and Equality Rigidity).**
*Let $\pi \in S_k$, and let $\tau = \mathrm{std}(\pi(r_1), \dots, \pi(r_m)) \in S_m$ be the pattern formed by a subsequence at indices $1 \leq r_1 < r_2 < \cdots < r_m \leq k$. Then:*
1. *$\mathrm{asc}(\tau) \leq \mathrm{asc}(\pi)$; moreover, if $\mathrm{asc}(\tau) = \mathrm{asc}(\pi)$, then $\pi(1) \geq \pi(r_1)$ and $\pi(r_m) \geq \pi(k)$.*
2. *$\mathrm{des}(\tau) \leq \mathrm{des}(\pi)$; moreover, if $\mathrm{des}(\tau) = \mathrm{des}(\pi)$, then $\pi(1) \leq \pi(r_1)$ and $\pi(r_m) \leq \pi(k)$.*

*Proof of Claim 3B.*
(1) For each ascent index $j \in \{1, \dots, m-1\}$ of $\tau$, we have $\pi(r_j) < \pi(r_{j+1})$, so it is impossible that $\pi(i) > \pi(i+1)$ for all $i \in \{r_j, \dots, r_{j+1}-1\}$. Hence each ascent $j$ of $\tau$ forces at least one ascent index $i \in \{r_j, \dots, r_{j+1}-1\}$ of $\pi$. Because the sets $\{r_j, \dots, r_{j+1}-1\}$ ($1 \leq j \leq m-1$) are pairwise disjoint subsets of $\{1, \dots, k-1\}$, we obtain $\mathrm{asc}(\tau) \leq \mathrm{asc}(\pi)$.

Moreover, every such interval is disjoint from $\{1, \dots, r_1 - 1\}$ and $\{r_m, \dots, k - 1\}$. Consequently, if $\mathrm{asc}(\tau) = \mathrm{asc}(\pi)$, then every ascent index of $\pi$ must lie inside $\bigcup_{j:\,\tau(j)<\tau(j+1)} \{r_j, \dots, r_{j+1}-1\}$, leaving zero ascents of $\pi$ in $\{1, \dots, r_1 - 1\}$ and zero ascents of $\pi$ in $\{r_m, \dots, k - 1\}$. Hence $\pi(1) > \pi(2) > \cdots > \pi(r_1)$ (trivially $\pi(1) = \pi(r_1)$ if $r_1 = 1$) and $\pi(r_m) > \pi(r_m + 1) > \cdots > \pi(k)$ (trivially $\pi(r_m) = \pi(k)$ if $r_m = k$), so $\pi(1) \geq \pi(r_1)$ and $\pi(r_m) \geq \pi(k)$.

(2) Applying (1) to the complement $\pi^c(i) := k + 1 - \pi(i)$ (which reverses all value inequalities and swaps ascents with descents) immediately yields $\mathrm{des}(\tau) \leq \mathrm{des}(\pi)$ and, upon equality, $\pi(1) \leq \pi(r_1)$ and $\pi(r_m) \leq \pi(k)$. $\blacksquare$

*Proof of Theorem 3.* Suppose for contradiction that a non-monotone $p \in S_k$ ($k \geq 3$) satisfies both $p \in \mathrm{Sh}_k(I_k(p^r, j_1, +))$ and $p \in \mathrm{Sh}_k(I_k(p^r, j_2, -))$ for some $j_1, j_2 \in \{1, \dots, k\}$.

- By Claim 3A with $\varepsilon = +$, there exist $2 \leq m_+ \leq k - 1$, $q_+ \in S_{m_+}$, and indices $1 \leq r_1 < \cdots < r_{m_+} \leq k$ such that $q_+^r = \mathrm{std}(p(r_1), \dots, p(r_{m_+}))$, $\mathrm{des}(q_+) = \mathrm{des}(p)$, and $p(1) < p(k) \iff q_+(1) < q_+(m_+)$.
- By Claim 3A with $\varepsilon = -$, there exist $2 \leq m_- \leq k - 1$, $q_- \in S_{m_-}$, and indices $1 \leq u_1 < \cdots < u_{m_-} \leq k$ such that $q_-^r = \mathrm{std}(p(u_1), \dots, p(u_{m_-}))$, $\mathrm{asc}(q_-) = \mathrm{asc}(p)$, and $p(1) > p(k) \iff q_-(1) > q_-(m_-)$.

Using $\mathrm{asc}(\tau^r) = \mathrm{des}(\tau)$, $\mathrm{des}(\tau^r) = \mathrm{asc}(\tau)$, and Claim 3B, we obtain the cyclic chain of inequalities
$$\mathrm{des}(p) = \mathrm{des}(q_+) = \mathrm{asc}(q_+^r) \leq \mathrm{asc}(p) = \mathrm{asc}(q_-) = \mathrm{des}(q_-^r) \leq \mathrm{des}(p).$$
Hence every inequality in this chain is an equality; in particular,
$$\mathrm{asc}(q_+^r) = \mathrm{asc}(p) \qquad \text{and} \qquad \mathrm{des}(q_-^r) = \mathrm{des}(p).$$
*(Remark: this already gives $\mathrm{asc}(p) = \mathrm{des}(p)$, an immediate contradiction for every even $k$ since $\mathrm{asc}(p) + \mathrm{des}(p) = k - 1$ is odd; the endpoint argument below handles all $k \geq 3$ uniformly.)*

By the equality rigidity in Claim 3B:
- $\mathrm{asc}(q_+^r) = \mathrm{asc}(p)$ implies $p(1) \geq p(r_1)$ and $p(r_{m_+}) \geq p(k)$;
- $\mathrm{des}(q_-^r) = \mathrm{des}(p)$ implies $p(1) \leq p(u_1)$ and $p(u_{m_-}) \leq p(k)$.

Since $p$ is a bijection on $\{1, \dots, k\}$ with $k \geq 3$, we have $p(1) \neq p(k)$.
- If $p(1) < p(k)$, then $q_+(1) < q_+(m_+)$, so $q_+^r(1) = q_+(m_+) > q_+(1) = q_+^r(m_+)$. Because $q_+^r = \mathrm{std}(p(r_1), \dots, p(r_{m_+}))$, this gives $p(r_1) > p(r_{m_+})$, whence
  $$p(1) \geq p(r_1) > p(r_{m_+}) \geq p(k),$$
  contradicting $p(1) < p(k)$.
- If $p(1) > p(k)$, then $q_-(1) > q_-(m_-)$, so $q_-^r(1) = q_-(m_-) < q_-(1) = q_-^r(m_-)$. Because $q_-^r = \mathrm{std}(p(u_1), \dots, p(u_{m_-}))$, this gives $p(u_1) < p(u_{m_-})$, whence
  $$p(1) \leq p(u_1) < p(u_{m_-}) \leq p(k),$$
  contradicting $p(1) > p(k)$.

Both cases yield a contradiction, completing the proof of Theorem 3. $\blacksquare$

---

## 7. Proof of the Main Theorem

*Proof of the Main Theorem.* Fix $k \geq 3$ and $n \geq n_0(k) = k + ((2k+1)(k-1))^2 + 1$. As noted in Section 2, $n > (k-1)^2 + 1$. Let $F \subseteq S_k$ be any reverse-closed set containing neither monotone pattern, and let $p \in S_k \setminus F$ be any non-monotone pattern legal from $F$ at length $n$. By Theorem 3 and Lemma 2, $p^r$ is legal from $F \cup \{p\}$ at length $n$. Applying Proposition 1, the move-by-move reverse strategy is a winning strategy for Player II on $S_n$, and in particular $\mathrm{sg}(S_n, k) = 0$. $\blacksquare$

---

## 8. Computational Verification

An exact-arithmetic (pure integer, zero floating-point operations) verification script is provided in [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/ulfarsson-2603.16004-conj1/verify.py). Running `.venv/bin/python targets/ulfarsson-2603.16004-conj1/verify.py` verifies:
1. All explicit threshold inequalities for $n_0(k)$ for $3 \leq k \leq 500$.
2. Lemma 0(1)–(3) exhaustively on small $k$ (reversal identity, shadow stabilization, and contiguous monotone-block inflation).
3. Lemma 2's full Case 1 / Subcase 2a / Subcase 2b witness construction exhaustively over all non-monotone $p \in S_k$, all 1-point extensions $\beta \in S_{k+1}$, and both signs $\varepsilon \in \{+, -\}$ for $k = 3, 4$.
4. Claim 3A, Claim 3B, and Theorem 3 exhaustively over all non-monotone $p \in S_k$ for $k = 3, 4, 5, 6$, and over all non-monotone $p \in S_7$ (5,038 permutations, including full rigidity checks on all 2,416 permutations with $\mathrm{asc}(p) = \mathrm{des}(p)$).
5. End-to-end exact PAP game tree verification for $k = 3$, $n \in \{5, 6\}$ confirming $\mathrm{sg}(S_n, 3) = 0$ and that the move-by-move reverse strategy wins every play.

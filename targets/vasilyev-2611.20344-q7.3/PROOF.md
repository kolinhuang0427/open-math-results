# Proof of Vasilyev (2026), Question 7.3 (`q:types`)

- **Primary source:** Oleg Vasilyev, *Up or down at every integer: Collatz-type maps of arbitrary sets and the up-down graph*, `arXiv:2611.20344v2` (2026-11-18, `updown.tex`), Section 7 (*Questions*), **Question 7.3** (`\label{q:types}`, lines 1991–1993; referencing **Remark 4.4** `\label{rem:types}`, lines 1134–1145).
- **Verbatim problem statement:**
  For $x \in \mathbb{N} = \{1, 2, 3, \dots\}$, let $U(x) = \lceil 3x/2 \rceil$ and $D(x) = \lceil x/2 \rceil$, and for $S \subseteq \mathbb{N}$ define $T_S : \mathbb{N} \to \mathbb{N}$ by $T_S(x) = U(x)$ if $x \in S$ and $T_S(x) = D(x)$ if $x \notin S$.
  > **Question 7.3 (`q:types`).** Is there a map with infinitely many cycles and a divergent orbit (Remark 4.4)?
- **Result:** **YES.** We explicitly construct a set $S \subseteq \mathbb{N}$ whose map $T_S$ has infinitely many pairwise disjoint cycles and a divergent orbit (in fact, in the notation of Remark 4.4, $T_S$ has exact orbit type $(k, l) = (\infty, 1)$: infinitely many cycles and a unique equivalence class of divergent orbits).
- **Verification:** Pure-integer (zero-float, zero external dependencies) verification script [`verify.py`](file:///Users/kolinhuang/Documents/open-math/targets/vasilyev-2611.20344-q7.3/verify.py), run via:
  ```bash
  .venv/bin/python -u targets/vasilyev-2611.20344-q7.3/verify.py
  ```
  (prints `PASS`, exit code `0`, runtime $\approx 0.14\text{ s}$).

---

## 1. Notation and Elementary Properties of $U$ and $D$

Throughout, $\mathbb{N} = \{1, 2, 3, \dots\}$. Following Section 2 of `arXiv:2611.20344v2` (Lemma 2.1 `lem:steps`, Definition 2.2 `def:G`, Proposition 2.3 `prop:dict`), the **up-down graph** $G$ has vertex set $\mathbb{N}$ and directed edges $x \to U(x)$ and $x \to D(x)$ for each $x \in \mathbb{N}$, where:
- $U(x) = \lceil 3x/2 \rceil = (3x + (x \bmod 2))/2$ is strictly increasing (hence injective), satisfies $U(x) \ge \frac{3}{2}x$ and $U(x) > x$ for all $x \in \mathbb{N}$, and satisfies $U(2m) = 3m$ and $U(2m-1) = 3m-1$ for all $m \ge 1$. In particular,
  $$\mathrm{Im}(U) = \{z \in \mathbb{N} : z \ge 2,\ z \not\equiv 1 \pmod 3\}. \tag{1.1}$$
- $D(x) = \lceil x/2 \rceil = (x + (x \bmod 2))/2$ is non-decreasing and satisfies $D(x) < x$ for all $x \ge 2$.
- For any $n \in \mathbb{N}$, $v_2(n)$ denotes the $2$-adic valuation of $n$ (the largest integer $e \ge 0$ with $2^e \mid n$).

Call a directed edge $x \to y$ of $G$ **admissible** if either:
1. $y = U(x)$ (with $x \in \mathbb{N}$ arbitrary), or
2. $y = D(x)$ and $x \equiv 2 \pmod 6$ (in which case $x$ is even and $y = x/2 \equiv 1 \pmod 3$, so $y \notin \mathrm{Im}(U)$ by (1.1)).

A (finite or infinite) path $(p_0, p_1, \dots)$ in $G$ is **simple** if its vertices are pairwise distinct, and **admissible** if every step $p_i \to p_{i+1}$ is admissible. An infinite simple path is a **ray**.

---

## 2. Two Core Lemmas

### Lemma 1 (Closed-Box Trap Lemma)
*Let $R \subseteq \mathbb{N}$ be any subset and let $B \ge 5$ be an integer with $B \equiv 5 \pmod 6$. Set $C := U(B) = \frac{3B + 1}{2}$, and suppose:*
- *(i) $U(\mathbb{N} \setminus R) \subseteq \mathbb{N} \setminus R$;*
- *(ii) $R \cap [B + 1,\, C - 1] = \emptyset$.*

*Then the finite set*
$$V(B) := [B + 1,\, 3B - 1] \setminus (R \cup \{2B\})$$
*is nonempty, and the map $f_B : V(B) \to \mathbb{N}$ defined by*
$$f_B(x) := \begin{cases} U(x) & \text{if } B + 1 \le x \le 2B - 1, \\ D(x) & \text{if } 2B + 1 \le x \le 3B - 1 \end{cases}$$
*satisfies $f_B(V(B)) \subseteq V(B)$ and $f_B(x) \ne x$ for all $x \in V(B)$. Consequently, $V(B)$ contains a simple cycle $C(B)$ of $G$ of length at least $2$ (using the $U$-edge at $x \le 2B - 1$ and the $D$-edge at $x \ge 2B + 1$), which is disjoint from $R$ and contained in $[B + 1,\, 3B - 1]$.*

*Proof.* Since $B \equiv 5 \pmod 6$ and $B \ge 5$, $B$ is odd with $B \equiv 2 \pmod 3$, so $C = \lceil 3B/2 \rceil = \frac{3B + 1}{2}$, $C - 1 = \frac{3B - 1}{2}$, and
$$B + 1 < C - 1 < 2B < 3B - 1.$$
Because $B + 1 \in [B + 1,\, C - 1]$, hypothesis (ii) gives $B + 1 \notin R$; as $B + 1 < 2B$, we have $B + 1 \in V(B)$, so $V(B)$ is nonempty. Moreover, since $2B \notin V(B)$, the two cases $B + 1 \le x \le 2B - 1$ and $2B + 1 \le x \le 3B - 1$ partition $V(B)$, so $f_B$ is well-defined. Every $x \in V(B)$ satisfies $x \ge B + 1 \ge 6 \ge 2$, whence $U(x) > x$ and $D(x) < x$, so $f_B(x) \ne x$.

Let $x \in V(B)$. We check $f_B(x) \in V(B)$ in both cases:
- **Case 1 ($B + 1 \le x \le 2B - 1$):** Here $f_B(x) = U(x)$.
  - $U(x) > x \ge B + 1$, and by monotonicity $U(x) \le U(2B - 1) = \lceil (6B - 3)/2 \rceil = 3B - 1$.
  - Since $x \in V(B)$, $x \notin R$, so $U(x) \notin R$ by hypothesis (i).
  - Since $B \equiv 2 \pmod 3$, we have $2B \equiv 1 \pmod 3$, so $2B \notin \mathrm{Im}(U)$ by (1.1); hence $U(x) \ne 2B$.
  Thus $U(x) \in V(B)$.
- **Case 2 ($2B + 1 \le x \le 3B - 1$):** Here $f_B(x) = D(x)$.
  - By monotonicity of $D$, $D(x) \ge D(2B + 1) = \lceil (2B + 1)/2 \rceil = B + 1$, and $D(x) \le D(3B - 1) = \lceil (3B - 1)/2 \rceil = \frac{3B - 1}{2} = C - 1$ (exact because $B$ is odd, so $3B - 1$ is even).
  - Since $[B + 1,\, C - 1] \subset [B + 1,\, 2B - 1] \subset [B + 1,\, 3B - 1]$, we have $D(x) \in [B + 1,\, 3B - 1]$ and $D(x) \ne 2B$.
  - By hypothesis (ii), $D(x) \in [B + 1,\, C - 1]$ implies $D(x) \notin R$.
  Thus $D(x) \in V(B)$.

Starting at $x_0 := B + 1 \in V(B)$ and iterating $x_{i+1} := f_B(x_i) \in V(B)$ produces an infinite sequence in the finite set $V(B)$. Let $j \ge 1$ be the smallest index such that $x_j = x_i$ for some $0 \le i < j$. Then $C(B) := (x_i, x_{i+1}, \dots, x_{j-1})$ is a simple cycle in $G$ contained in $V(B) \subseteq [B + 1,\, 3B - 1] \setminus R$, and $j - i \ge 2$ since $f_B(x) \ne x$. $\square$

---

### Lemma 2 (Admissible Ray $U$-Invariance)
*Let $R = (r_0, r_1, r_2, \dots)$ be any admissible ray in $G$ with $r_0 = 1$ (identifying $R$ with its underlying vertex set $\{r_t : t \ge 0\}$). Then $U(\mathbb{N} \setminus R) \subseteq \mathbb{N} \setminus R$.*

*Proof.* Suppose $x \in \mathbb{N}$ satisfies $U(x) = r_t$ for some $t \ge 0$. Since $U(x) \ge 2 > 1 = r_0$, we have $t \ge 1$. Consider the admissible edge $r_{t-1} \to r_t$: it cannot be a $D$-step, because every admissible $D$-step lands at a vertex $\equiv 1 \pmod 3$, contradicting $r_t = U(x) \in \mathrm{Im}(U)$ by (1.1). Hence $r_t = U(r_{t-1})$. By injectivity of $U$, $U(x) = U(r_{t-1})$ forces $x = r_{t-1} \in R$. Contrapositively, $x \notin R \implies U(x) \notin R$. $\square$

---

### Lemma 3 (Admissible Stage Extension)
*For every integer $H \ge 5$, there exist a finite simple admissible path $P = (p_0, p_1, \dots, p_L)$ ($L \ge 4$) in $G$ starting at $p_0 = H$ and an integer $B \equiv 5 \pmod 6$ with $B > 5H$ such that, setting $C := U(B) = \frac{3B + 1}{2}$ and $H' := p_L$:*
1. *$p_i > H$ for all $1 \le i \le L$, and the vertices $p_0, p_1, \dots, p_L$ are pairwise distinct;*
2. *$P \cap [B + 1,\, C - 1] = \emptyset$;*
3. *$H' = \max(P) > 3B$.*

*Proof.* We construct $P$ in three phases starting from $p_0 = H \ge 5$.

**Phase 1 (Climb above $5H$ to an odd integer via $U$-steps).** Take $4$ consecutive $U$-steps to $x_0 := U^4(H) \ge (\frac{3}{2})^4 H = \frac{81}{16} H > 5H \ge 25$. While the current vertex is even, continue applying $U$: since $U(2m) = 3m$ satisfies $v_2(U(2m)) = v_2(2m) - 1$, this terminates after $v_2(x_0)$ steps at an odd vertex $w_0 := U^{4 + v_2(x_0)}(H) \ge x_0 > 5H \ge 25$. Every step of Phase 1 is a strictly increasing $U$-step.

**Phase 2 (Reach $A \equiv 3 \pmod 4$, $B = U(A) \equiv 5 \pmod 6$, $C = U(B)$ with all prior vertices $< B$).** Starting from the odd vertex $w := w_0 > 5H \ge 25$, execute the following procedure:
- **Case A ($w \equiv 3 \pmod 4$):** Set $A := w$, and take two $U$-steps to $B := U(A)$ and $C := U(B)$. Stop Phase 2. Writing $A = 4j + 3$, we have $B = 6j + 5 \equiv 5 \pmod 6$, $C = \frac{3B + 1}{2}$, and all steps from $p_0 = H$ to $C$ are strictly increasing $U$-steps, so $B > w > 5H$ and every vertex of $P$ visited before $B$ is strictly $< B$.
- **Case B ($w \equiv 1 \pmod 4$):** Write $w = 4k + 1$ ($k \ge 6$ since $w > 25$). Note that $y := U(w) = 6k + 2 = 2(3k + 1) \equiv 2 \pmod 6$. Consider $k \bmod 4$:
  - **Subcase B1 ($k \equiv 0 \pmod 4$, $k = 4q$):** Take four consecutive $U$-steps:
    $$w = 16q + 1 \xrightarrow{U} y = 24q + 2 \xrightarrow{U} A := 36q + 3 \xrightarrow{U} B := U(A) \xrightarrow{U} C := U(B),$$
    and stop Phase 2. Here $A \equiv 3 \pmod 4$, so $B \equiv 5 \pmod 6$; all steps from $p_0$ to $C$ are strictly increasing $U$-steps, so $B > w > 5H$ and every prior vertex is $< B$.
  - **Subcase B2 ($k$ odd):** Take one $U$-step from $w$ to $y = 2(3k + 1) \equiv 2 \pmod 6$. Since $k$ is odd, $3k + 1$ is even; write $3k + 1 = 2^e u$ with $e \ge 1$ and $u$ odd. Because $3 \equiv -1 \pmod 4$ and $u$ is odd, $\{3^e u \bmod 4,\, 3^{e+1} u \bmod 4\} = \{1, 3\}$, so exactly one of $3^{e+1} u$ and $3^e u$ is $\equiv 3 \pmod 4$:
    - **Subcase B2a ($3^{e+1} u \equiv 3 \pmod 4$):** From $y = 2^{e+1} u$, take $e + 1$ consecutive $U$-steps. By induction via $U(2m) = 3m$, this visits $2^{e+1-i} 3^i u$ ($1 \le i \le e + 1$), reaching $A := 3^{e+1} u \equiv 3 \pmod 4$. Take two more $U$-steps to $B := U(A) \equiv 5 \pmod 6$ and $C := U(B)$, and stop Phase 2. All steps from $p_0$ to $C$ are strictly increasing $U$-steps, so $B > w > 5H$ and all prior vertices are $< B$.
    - **Subcase B2b ($3^e u \equiv 3 \pmod 4$):** From $y \equiv 2 \pmod 6$, take one admissible $D$-step to $d := D(y) = 3k + 1 = 2^e u \equiv 1 \pmod 3$, then take $e$ consecutive $U$-steps visiting $2^{e-i} 3^i u$ ($0 \le i \le e$) to reach $A := 3^e u \equiv 3 \pmod 4$, then take two $U$-steps to $B := U(A) \equiv 5 \pmod 6$ and $C := U(B)$, and stop Phase 2. We check:
      1. $d = 3k + 1 = \frac{3w + 1}{4} > \frac{3}{4} w > \frac{15}{4} H > H$, and all subsequent vertices $U^i(d)$ are strictly increasing, so every vertex after $p_0 = H$ is $> H$.
      2. $B > y$: if $e = 1$, then $y = 4u$, $A = 3u$, and $B = U(3u) = \frac{9u + 1}{2} = 4u + \frac{u + 1}{2} > 4u = y$; if $e \ge 2$, then $3^e > 2^{e+1}$ (as $3^2 = 9 > 8 = 2^3$ and $3/2 > 1$), so $B > A = 3^e u > 2^{e+1} u = y$. Hence $B > y > w > 5H$, and every vertex visited before $B$ is strictly $< B$.
  - **Subcase B3 ($k \equiv 2 \pmod 4$, $k = 4q + 2$):** Here $w = 16q + 9$ with $q \ge 2$ (as $w > 25$).
    - **Subcase B3a ($q = 2r$ even, $r \ge 1$):** Here $w = 32r + 9$. Take one $U$-step to $y = 48r + 14 \equiv 2 \pmod 6$, one admissible $D$-step to $d := D(y) = 24r + 7 \equiv 1 \pmod 3$, and three $U$-steps to
      $$A := U(d) = 36r + 11 \equiv 3 \pmod 4, \qquad B := U(A) = 54r + 17 \equiv 5 \pmod 6, \qquad C := U(B) = 81r + 26,$$
      and stop Phase 2. Then $d = \frac{3w + 1}{4} > \frac{15}{4} H > H$, $B = 54r + 17 > 48r + 14 = y > w > 5H$, and every vertex visited before $B$ is strictly $< B$.
    - **Subcase B3b ($q$ odd):** Take two consecutive $U$-steps:
      $$w = 16q + 9 \xrightarrow{U} 24q + 14 \xrightarrow{U} w' := 36q + 21$$
      (strictly increasing, $w' > w > 5H$, $w'$ odd), replace $w$ by $w'$, and repeat Case B.
      We verify termination of Subcase B3b:
      - If $q \equiv 3 \pmod 4$ ($q = 4r + 3$), then $w' = 144r + 129 = 4(36r + 32) + 1$ has $k' = 36r + 32 \equiv 0 \pmod 4$, so the next iteration immediately enters Subcase B1 and terminates.
      - If $q \equiv 1 \pmod 4$ ($q = 4r + 1$), then $w' = 144r + 57 = 16(9r + 3) + 9$ re-enters Subcase B3 with $q' := 9r + 3 = \frac{9q + 3}{4}$, which satisfies
        $$5q' + 3 = 5\cdot\frac{9q + 3}{4} + 3 = \frac{9(5q + 3)}{4} \implies v_2(5q' + 3) = v_2(5q + 3) - 2.$$
        Since $5q + 3 \ge 13$ is a finite positive integer, this loop can iterate at most $\lfloor v_2(5q_0 + 3)/2 \rfloor$ times before hitting either $q'$ even (Subcase B3a) or $q' \equiv 3 \pmod 4$ (leading to Subcase B1).

**Pairwise distinctness in Phase 2 (Subcases B2b and B3a).** In Cases A, B1, and B2a, all vertices from $p_0$ to $C$ are strictly increasing, hence pairwise distinct. In Subcases B2b and B3a, every step from $p_0 = H$ up to $p_{t_y} = y$ is a strictly increasing $U$-step (including all Phase 1 and Subcase B3b iterations), so $p_0 < p_1 < \dotsb < p_{t_y}$ and $p_j \in \mathrm{Im}(U)$ for all $1 \le j \le t_y$; after the single admissible $D$-step $y \to d$, the remaining vertices $U^i(d)$ ($0 \le i \le s$, ending at $C$) are strictly increasing with $d > H = p_0$ and $d \equiv 1 \pmod 3 \notin \mathrm{Im}(U)$. Could $U^i(d) = p_j$ for some $0 \le i \le s$ and $0 \le j \le t_y$? Since $U^i(d) \ge d > p_0$, we must have $j \ge 1$. If $i = 0$, this gives $d = p_j \in \mathrm{Im}(U)$, impossible. If $i \ge 1$, then $p_j = U(p_{j-1})$ and injectivity of $U$ yield $U^{i-1}(d) = p_{j-1}$. Repeating $\min(i, j)$ times produces either $d = p_{j-i}$ (impossible since $d > p_0$ when $j = i$, and $d \notin \mathrm{Im}(U)$ when $j > i$) or $U^{i-j}(d) = p_0$ (impossible since $U^{i-j}(d) \ge d > p_0$). Hence all vertices visited through $C$ are pairwise distinct.

**Phase 3 (Exit past $3B$ via two $U$-steps).** At the end of Phase 2, the current vertex is $C = U(B) = \frac{3B + 1}{2}$, and every vertex of $P$ visited prior to $C$ is $\le B < C$. Take two final $U$-steps: $p_{L-1} := U(C)$ and $H' := p_L := U^2(C)$. Since $U(x) \ge \frac{3}{2} x$,
$$C < U(C) < U^2(C) = H', \qquad H' \ge \frac{9}{4} C = \frac{9}{4}\cdot\frac{3B + 1}{2} = \frac{27B + 9}{8} > 3B.$$
Because $C < U(C) < H'$ all strictly exceed $C > B$, these two new vertices are distinct from all earlier vertices of $P$, lie strictly outside $[B + 1,\, C - 1]$, and satisfy $H' = \max(P) > 3B$. Since every vertex prior to $C$ is $\le B$, we also have $P \cap [B + 1,\, C - 1] = \emptyset$. All three conclusions of Lemma 3 hold. $\square$

---

## 3. Main Theorem (Affirmative Answer to Question 7.3)

**Theorem.** *There exists a subset $S \subseteq \mathbb{N}$ such that $T_S$ has infinitely many cycles and a divergent orbit. Moreover, $S$ can be chosen so that $T_S$ has exact orbit type $(k, l) = (\infty, 1)$ in the sense of Remark 4.4 (`rem:types`): infinitely many cycles and a unique equivalence class of divergent orbits.*

*Proof.* Set $P_0 := (1, 2, 3, 5)$ (three pure $U$-steps, pairwise distinct, admissible, with head $H_0 := 5 = \max(P_0)$). Inductively for each $m = 1, 2, 3, \dots$, apply Lemma 3 to $H_{m-1} \ge 5$ to obtain a finite simple admissible path $P_m$ from $H_{m-1}$ to $H_m := \max(P_m)$ and an integer $B_m \equiv 5 \pmod 6$ with $B_m > 5 H_{m-1} > H_{m-1}$, $C_m := U(B_m) = \frac{3B_m + 1}{2}$, $P_m \cap [B_m + 1,\, C_m - 1] = \emptyset$, and $H_m > 3 B_m$.

Concatenating $P_0, P_1, P_2, \dots$ (identifying each shared endpoint $H_{m-1}$) yields an infinite admissible path $R = (r_0, r_1, r_2, \dots)$ in $G$ starting at $r_0 = 1$.

1. **$R$ is a ray:** By Lemma 3(1),(3), for every $m \ge 1$ the vertices of $P_m \setminus \{H_{m-1}\}$ are pairwise distinct and lie in $(H_{m-1},\, H_m]$. Since $H_0 < H_1 < H_2 < \dotsb$, the sets $P_0 \subseteq [1,\, H_0]$ and $(H_{m-1},\, H_m]$ ($m \ge 1$) are pairwise disjoint; thus all vertices of $R$ are pairwise distinct, so $R$ is an admissible ray starting at $r_0 = 1$.
2. **Every $B_m$ satisfies Lemma 1 against the entire infinite ray $R$:**
   - Hypothesis (i) ($U(\mathbb{N} \setminus R) \subseteq \mathbb{N} \setminus R$) holds by Lemma 2.
   - For hypothesis (ii), fix $m \ge 1$ and check $P_j \cap [B_m + 1,\, C_m - 1]$ for all $j \ge 0$:
     - if $j < m$, every vertex of $P_j$ is $\le H_{m-1} < B_m < B_m + 1$;
     - if $j = m$, $P_m \cap [B_m + 1,\, C_m - 1] = \emptyset$ by Lemma 3(2);
     - if $j > m$, every vertex of $P_j \setminus \{H_{j-1}\}$ is $> H_{j-1} \ge H_m > 3B_m > C_m - 1$.
     Hence $R \cap [B_m + 1,\, C_m - 1] = \emptyset$.
3. **Infinitely many pairwise disjoint cycles all disjoint from $R$:** By Lemma 1, for each $m \ge 1$ there is a simple cycle $C(B_m)$ in $G$ contained in $V(B_m) \subseteq [B_m + 1,\, 3B_m - 1] \setminus R$. Because $3 B_m - 1 < H_m < B_{m+1} < B_{m+1} + 1$ for every $m \ge 1$, the intervals $[B_m + 1,\, 3B_m - 1]$ are pairwise disjoint. Therefore $R$ and $\{C(B_m)\}_{m \ge 1}$ are pairwise vertex-disjoint.
4. **Explicit definition of $S$ and exact orbit type $(k, l) = (\infty, 1)$:** Let $W := R \cup \bigcup_{m \ge 1} C(B_m)$ (disjoint union) and define
   $$S := \big\{r_t \in R : r_{t+1} = U(r_t)\big\} \cup \bigcup_{m \ge 1} \big\{x \in C(B_m) : B_m + 1 \le x \le 2B_m - 1\big\}.$$
   (This is the explicit realization of Vasilyev's Dictionary, Proposition 2.3 `prop:dict`.) By pairwise disjointness of $R$ and the cycles $C(B_m)$:
   - $T_S(r_t) = r_{t+1}$ for all $t \ge 0$, so the orbit of $1$ under $T_S$ is $R$, whose vertices are all distinct — hence a **divergent orbit**.
   - For every $m \ge 1$ and $x \in C(B_m)$, $T_S(x) = f_{B_m}(x)$ is the successor of $x$ on $C(B_m)$, so $\{C(B_m)\}_{m \ge 1}$ are **infinitely many pairwise disjoint cycles** of $T_S$.
   - Finally, every $x \in \mathbb{N} \setminus W$ satisfies $x \ge 2$ (as $1 \in R \subseteq W$) and $x \notin S$, hence $T_S(x) = D(x) < x$. By well-ordering of $\mathbb{N}$, every orbit starting outside $W$ strictly decreases until it enters $W$, where it either enters $R$ (so is equivalent to the divergent orbit of $1$) or enters some cycle $C(B_m)$. Thus $T_S$ has no other cycles and a unique equivalence class of divergent orbits: $(k, l) = (\infty, 1)$. $\blacksquare$

---

## 4. Verification Summary (`verify.py`)

Running `.venv/bin/python -u targets/vasilyev-2611.20344-q7.3/verify.py` (pure exact Python integer arithmetic, zero floats, runtime $\approx 0.14\text{ s}$) confirms:
1. All elementary $U/D$ identities, $\mathrm{Im}(U) \cap [1, 1000] = \{z \in [2, 1000] : z \not\equiv 1 \pmod 3\}$, trap endpoint formulas for $B \equiv 5 \pmod 6$ ($B < 1000$), and the Subcase B3b identity $4(5q' + 3) = 9(5q + 3)$ for $q \equiv 1 \pmod 4$ ($q < 10000$).
2. Exhaustive verification of Lemma 3 across all $4{,}996$ starting heads $H \in [5, 5000]$ (branch distribution: `A`: $2493$, `B1`: $830$, `B2a`: $617$, `B2b`: $641$, `B3a`: $415$; max `B3b` loop depth: $4$), asserting every admissibility, distinctness, gap-clearance, and upper-exit invariant.
3. Explicit 50-stage ray construction from $P_0 = (1, 2, 3, 5)$ ($550$ distinct vertices, $\max(R)$ is $310$-bit), confirming global $U$-invariance of $\mathbb{N} \setminus R$ on $[1, 50000]$, global gap clearance $R \cap [B_m + 1,\, C_m - 1] = \emptyset$, and strict disjointness across all $50$ trap boxes.
4. Exhaustive vertex-by-vertex check of Lemma 1 ($f_{B_m}(V(B_m)) \subseteq V(B_m)$) on Stages 1–2, explicit extraction of the first $4$ pairwise disjoint simple cycles $C(B_m)$ disjoint from $R$, and direct simulation of $T_S$ on all $549$ ray steps, all $4$ cycles, and all $x \in [1, 5397]$:

| Stage $m$ | Branch | $B_m$ ($\equiv 5 \pmod 6$) | $C_m = U(B_m)$ | Trap Box $[B_m+1,\, 3B_m-1]$ | Extracted Cycle $|C(B_m)|$ | Cycle Range |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `A` | $41$ | $62$ | $[42,\, 122]$ (`|V|=78`, exhaustive) | $43$ | $[42,\, 122]$ |
| 2 | `B3a` | $1799$ | $2699$ | $[1800,\, 5396]$ (`|V|=3594`, exhaustive) | $363$ | $[1803,\, 5382]$ |
| 3 | `A` | $350285$ | $525428$ | $[350286,\, 1050854]$ | $10857$ | $[350289,\, 1050758]$ |
| 4 | `A` | $8977433$ | $13466150$ | $[8977434,\, 26932298]$ | $35752$ | $[8977527,\, 26931726]$ |

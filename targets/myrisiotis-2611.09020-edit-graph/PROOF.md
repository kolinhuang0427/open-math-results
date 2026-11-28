# Proof: Positive Resolution of `op:edit-graph` (`myrisiotis-2611.09020-edit-graph`)

## Verdict

**YES.** We construct an explicit adjunction-universal machine $V$ (which by `lem:interpretation-completion` can also satisfy all three reference conditions with identical unconditional edit graphs) and a total computable function $b : \{0,1\}^* \to \mathbb{N}$ (with $b(x) \le 2^{|x|+2} + O(|x|)$) such that for every target $x \in \{0,1\}^*$, every budget $\ell \ge b(x)$, and every native deadline $t \in \mathbb{N}$, the edit graph $\mathcal{E}^t_{\ell, V}(x)$ is empty or connected.

---

## 1. Collision-Free Self-Delimiting Target Encoding and Bridge Language

Let $\mathrm{bin}(r)$ denote the canonical shortest binary representation of $r \in \mathbb{N}$ (with $\mathrm{bin}(0) = \texttt{0}$).

1. **Prefix-free target code $c(x)$:** For $x \in \{0,1\}^*$, put $m := |x| + 1 \ge 1$ and define
   $$c(x) := \texttt{1}^{|\mathrm{bin}(m)| - 1}\,\texttt{0}\,\mathrm{bin}(m)\,x.$$
   Since $|\mathrm{bin}(m)| - 1$ is recovered from the leading run of $\texttt{1}$s before the first $\texttt{0}$, $c : \{0,1\}^* \to \{0,1\}^*$ is injective, prefix-free, and decodable in one linear-time pass, with $|c(x)| = 2\lfloor\log_2(|x|+1)\rfloor + 2 + |x| \ge 2$.
2. **$\texttt{00}$-free encoding $P_x$:** Define the injective block morphism $\phi : \{0,1\}^* \to \{0,1\}^*$ by $\phi(\texttt{0}) = \texttt{01}$ and $\phi(\texttt{1}) = \texttt{011}$, and put
   $$P_x := \phi(c(x)), \qquad p_x := |P_x| \le 3|c(x)|, \qquad B_x := 5 + p_x \ge 9.$$
   Every nonempty prefix of $P_x$ starts with $\texttt{0}$, $P_x$ ends with $\texttt{1}$, and $P_x$ never contains $\texttt{00}$. Moreover, $\phi$ is uniquely left-to-right decodable because every $\texttt{0}$ marks a token boundary.
3. **Regular bridge-prefix language $\mathcal{U}$:** Define
   $$\mathcal{U} := \{\texttt{101},\, \texttt{1011},\, \texttt{10111}\} \cup \bigl\{\texttt{1011}\,Q\,\texttt{1} \;\big|\; Q \in \{\texttt{01}, \texttt{011}\}^*\{\varepsilon, \texttt{0}, \texttt{01}\}\bigr\}.$$
   Every $u \in \mathcal{U}$ starts with $\texttt{101}$, ends with $\texttt{1}$, has length $|u| \ge 3$, and contains **no** occurrence of $\texttt{00}$ (each $\texttt{0}$ inside $Q$ is both preceded and followed by $\texttt{1}$). Hence for every $u \in \mathcal{U}$ and every $p' \in \{0,1\}^*$, the first occurrence of $\texttt{000}$ (and even of $\texttt{00}$) in $u\,\texttt{000}\,p'$ lies at the exact boundary between $u$ and $\texttt{000}\,p'$.

---

## 2. Construction of the Adjunction-Universal Machine $V$

Let $A$ be the program-only realization of the rigid reference machine $U$ of `def:2.10` (`paper-arxiv.tex`, lines 920–927), with uniform simulation polynomial $q_A$. For any body length $n \ge 3$, let $a, K(n) = 2^a, k(n) = K(n) - 1$ (with $2K(n) - 1 \le n < 4K(n) - 1$), the syndrome coloring $D_n : \{0,1\}^n \to \mathbb{F}_2^a$, and shortlex label map $\lambda_a$ be as in `lem:connected-syndrome-coloring` (`lines 2187–2246`), writing $i(x) = 2^{|x|} - 1 + \mathrm{val}(x)$ (with $i(\varepsilon) = 0$) for the shortlex rank of $x \in \{0,1\}^*$.

Fix a constant $C_H \ge 20$ large enough for a multitape Turing machine to scan a hub prefix $\texttt{1001}\,P_x\,\texttt{1000}$, validate and decode $c(x)$, and write $x$ to the output tape in at most $C_H(p_x + 8)$ transitions. Set $L_1 := 2 C_H$, and choose a fixed nondecreasing polynomial $C(n)$ for $n \ge 3$ bounding the fixed-schedule Color Routine below and satisfying
$$C(n) > C_H(k(n) + 8) \qquad \text{for all } n \ge 3.$$
Put $S(n) := C(n) + 1$ for $n \ge 3$ and $S(n) := 1$ for $n < 3$.

On an input string $s \in \{0,1\}^*$, the program-only multitape machine $V$ halts in $\bot$ if $|s| < 3$; otherwise it writes $s = b_1 b_2 b_3\, p$ with $b_1 b_2 b_3 \in \{0,1\}^3$ and dispatches into eight disjoint cases:

- **`000`** ($s = \texttt{000}\,p$): runs the **Base Routine** on $(p, j = 0)$.
- **`001`** ($s = \texttt{001}\,p$): if $|p| < 3$, returns $\bot$; else runs the **Base Routine** on $(p, 0)$ when $\pi(p) = 0$, and the **Color Routine** on $p$ when $\pi(p) = 1$ (where $\pi(p) \in \{0,1\}$ is the parity of the Hamming weight of $p$).
- **`010`** ($s = \texttt{010}\,p$): if $|p| < 3$, returns $\bot$; else runs the **Color Routine** on $p$ when $\pi(p) = 0$, and the **Base Routine** on $(p, 0)$ when $\pi(p) = 1$.
- **`011`** ($s = \texttt{011}\,p$, primary core) and **`111`** ($s = \texttt{111}\,p$, mirror core): if $|p| < 3$, returns $\bot$; else runs the **Color Routine** on $p$.
- **`100`** ($s = \texttt{100}\,p$):
  - if $p$ is empty, returns $\bot$;
  - if $p = \texttt{0}\,p'$ (i.e. $s = \texttt{1000}\,p'$, Bridge $j = 1$), runs the **Base Routine** on $(p', 1)$;
  - if $p = \texttt{1}\,r$ (Hub 1), runs the **Hub Routine** on $r$.
- **`110`** ($s = \texttt{110}\,p$):
  - if $p = \texttt{00}\,p'$ (i.e. $s = \texttt{11000}\,p'$, Bridge $j = 2$), runs the **Base Routine** on $(p', 2)$;
  - if $p = \texttt{1}\,r$ (Hub 2), runs the **Hub Routine** on $r$;
  - otherwise returns $\bot$.
- **`101`** ($s = \texttt{101}\,p$, Bridge $j \ge 3$): finds the first occurrence of $\texttt{000}$ in $s$ (returning $\bot$ if none), splits $s = u\,\texttt{000}\,p'$, checks $u \in \mathcal{U}$ (returning $\bot$ if $u \notin \mathcal{U}$), and runs the **Base Routine** on $(p', j = |u|)$.

All eight 3-bit branches, and the subcases separated by bit 4 ($\texttt{1000}$ vs $\texttt{1001}$) and bits 4–5 ($\texttt{11000}$ vs $\texttt{1101}$), are pairwise disjoint and cover $\{0,1\}^*$.

### Subroutines and Exact Native Step Counts

1. **Hub Routine** on $r$: Finds the first occurrence of $\texttt{000}$ in $r$ (returning $\bot$ if none, or if the prefix before $\texttt{000}$ contains $\texttt{00}$ or does not have the form $P_x\,\texttt{1}$ for a valid $x = c^{-1}(\phi^{-1}(P_x))$). Without reading anything past $\texttt{000}$, writes $x$ to the output tape and pads to the exact duration
   $$H(x) := C_H \cdot (p_x + 8).$$
2. **Color Routine** on $p$ ($n = |p| \ge 3$): Using the fixed-duration length-dependent schedule of `lem:connected-syndrome-coloring` (`lines 2282–2305`), computes $j = D_n(p)$, $x = \lambda_a(j)$, and $B_x = 5 + p_x$ (note $|x| \le a \le \log_2 n$, so $B_x = O(\log n)$). **Guard:** if $B_x > k(n)$, halts with $\bot$ at the end of the fixed schedule; otherwise prints $x$ and halts normally at the common native time $C(n)$. Since $B_x \le k(n)$ implies $p_x + 8 \le k(n) + 3 < k(n) + 8$, every Color output $x$ at body length $n$ satisfies
   $$H(x) < C_H(k(n) + 8) < C(n).$$
3. **Base Routine** on $(p', j)$ with $n_{\mathrm{body}} := |p'| \ge 0$:
   - *Phase 1 (Prefix tally & body setup):* Scans the $j$ prefix bits ahead of the mode/delimiter in padded blocks of $L_1$ transitions per bit while writing $\texttt{1}^j$ onto a dedicated tally tape (with head left at cell $j$), reads the 3-bit delimiter in fixed time $L_0$, copies $p'$ onto a private input tape (with a left-end sentinel as in `lem:finite-target-completion`, `lines 2810–2821`), and performs the fixed-duration parity/syndrome scan of $p'$ (with duration $T_{\mathrm{prep}}(n_{\mathrm{body}})$ independent of $j$ and identical across modes $\texttt{000}, \texttt{001}, \texttt{010}$). Phase 1 takes exact time $L_1 j + L_0 + T_{\mathrm{prep}}(n_{\mathrm{body}})$.
   - *Phase 2 (Buffered $A$-simulation):* Simulates $A(p')$ in padded blocks of $L_A$ native steps per step of $A$, diverting output writes and head moves to a marked two-track buffer tape (as in `cor:7.18`, `lines 1459–1473`). If $A(p')$ diverges or enters $\bot$, $V$ does the same; if $A(p')$ normally halts with output $x$ in $T_A$ steps, Phase 2 takes time $T_{\mathrm{sim}}(p')$ depending only on $p'$.
   - *Phase 3 (Uniform $j$-cancellation & prelude wait):* Computes $B_x = 5 + p_x$ from the buffered output $x$ in time $T_B(x)$ depending only on $x$, and writes $\texttt{1}^{B_x}$ on a work tape. Next, scans $\texttt{1}^{B_x}$ left-to-right for $B_x$ iterations: while the tally head on $\texttt{1}^j$ has not yet reached its left-end sentinel (i.e. $j$ steps), moves that tally head left 1 cell in $1$ transition; on each remaining iteration ($B_x - j$ steps), waits $L_1 + 1$ transitions. If the tally head is not at its sentinel after scanning $\texttt{1}^{B_x}$ ($j > B_x$), enters $\bot$. For every $0 \le j \le B_x$, the combined Phase 1 prefix scan and Phase 3 tally scan take
     $$(L_1 j + L_0) + j + (L_1 + 1)(B_x - j) = L_0 + (L_1 + 1) B_x$$
     native transitions, **independent of $j$**. Finally, waits $S(n_{\mathrm{body}})$ padded steps, copies $x$ to the real output tape in time $T_{\mathrm{out}}(x)$, and halts normally.

Consequently, whenever $A(p')$ normally halts with output $x$ in $T_A$ steps and $0 \le j \le B_x$, the Base Routine halts with output $x$ at the **exact** common native time
$$T^*(n_{\mathrm{body}}, p', x) = L_0 + T_{\mathrm{prep}}(n_{\mathrm{body}}) + T_{\mathrm{sim}}(p') + T_B(x) + (L_1 + 1) B_x + S(n_{\mathrm{body}}) + T_{\mathrm{out}}(x),$$
which is identical across `000 p'`, the matching source helper (`001 p'` / `010 p'`), and every bridge $u\,\texttt{000}\,p'$ with $u \in \mathcal{U}$, $|u| \le B_x$. Moreover, since $L_1 = 2 C_H$, $(L_1 + 1) B_x = (2C_H + 1)(p_x + 5) > C_H(p_x + 8) = H(x)$, so
$$H(x) < T^*(n_{\mathrm{body}}, p', x) \qquad \text{and} \qquad n_{\mathrm{body}} \ge 3 \implies C(n_{\mathrm{body}}) < S(n_{\mathrm{body}}) < T^*(n_{\mathrm{body}}, p', x).$$

---

## 3. Proof of Adjunction-Universality and Edit-Graph Connectivity

**Lemma 1 ($V$ is adjunction-universal).** *The machine $V$ is efficient, onto, and satisfies the simulation property of `def:2.7`.*

*Proof.* By `fact:2.9`, every multitape Turing machine in the model of `def:2.5` is efficient. Onto-ness holds both via $V(h_x) = x$ (where $h_x = \texttt{1001}\,P_x\,\texttt{1000}$) and via base simulation. For the simulation property, set $\langle M \rangle_V := \texttt{000}\,\langle M \rangle$, which is computable in time and length polynomial in $|\langle M \rangle|$. For any $z \in \{0,1\}^*$, $V(\langle M \rangle_V z, \varepsilon) = V(\texttt{000}\,\langle M \rangle z)$ enters the Base Routine with $p' = \langle M \rangle z$ and $j = 0$: if $M(z)$ diverges, $A(\langle M \rangle z)$ diverges and so does $V$; if $M(z)$ halts in $T$ steps with output $x$, then $A(\langle M \rangle z)$ halts in $T_A \le q_A(T, |z|, |\langle M \rangle|)$ steps, $|x| \le T_A$ (`def:2.5`), $B_x = O(|x| + 1) = O(T_A + 1)$, $|p'| \le |\langle M \rangle_V| + |z|$, and all remaining polynomial routines ($T_{\mathrm{prep}}, S, T_B, T_{\mathrm{out}}$) sum to a uniform polynomial $q_V(T, |z|, |\langle M \rangle_V|)$ independent of $M$. (By `lem:interpretation-completion`, interpretation may also be added without changing any unconditional output, native halting time, or edit graph.) $\square$

**Definition of $b(x)$.** For each $x \in \{0,1\}^*$, let $N_x \ge 6$ be the smallest integer such that for $n = N - 3$:
$$i(x) < K(n) \qquad \text{and} \qquad B_x \le k(n) = K(n) - 1.$$
Since $K(n)$ and $k(n)$ are nondecreasing in $n$, both inequalities hold for **all** $N \ge N_x$ (explicitly, $K(n) \ge \max(i(x)+1, B_x+1)$ is guaranteed by $K(n) \le \max(2^{|x|+1}, 2B_x)$, so $n = 2K(n)-1 \le \max(2^{|x|+2}, 4B_x) - 1$ and $N_x \le \max(2^{|x|+2}, 4B_x) + 2$). Define the total computable function
$$b(x) := N_x + B_x.$$
Note the canonical hub $h_x := \texttt{1001}\,P_x\,\texttt{1000}$ has length $|h_x| = 3 + B_x < b(x)$.

**Theorem 1.** *For every target $x \in \{0,1\}^*$, every budget $\ell \ge b(x)$, and every deadline $t \in \mathbb{N}$, the edit graph $\mathcal{E}^t_{\ell, V}(x)$ is empty or connected.*

*Proof.* Suppose $\mathcal{E}^t_{\ell, V}(x)$ is nonempty and fix any vertex $s \in \mathcal{E}^t_{\ell, V}(x)$, so $|s| \le \ell$ and $V(s) = x$ normally within $t$ steps. By the timing bounds above, every program outputting $x$ in $V$ takes at least $H(x)$ steps, so $t \ge H(x)$; since $|h_x| < b(x) \le \ell$, the canonical hub $h_x$ lies in $\mathcal{E}^t_{\ell, V}(x)$. We construct an explicit walk in $\mathcal{E}^t_{\ell, V}(x)$ from $s$ to $h_x$:

1. **Hub vertices** ($s = \texttt{1001}\,P_x\,\texttt{1000}\,w$ or $s = \texttt{1101}\,P_x\,\texttt{1000}\,w$): If $s$ begins with $\texttt{110}$, flip bit 2 ($\texttt{110} \to \texttt{100}$) to obtain $\texttt{1001}\,P_x\,\texttt{1000}\,w$. Then delete the bits of $w$ one by one from the right end. Every intermediate string has length $\le |s| \le \ell$ and halts with output $x$ at time $H(x) \le t$, reaching $h_x$.
2. **Color vertices** ($s \in \{\texttt{011}\,p, \texttt{111}\,p\}$ or a router in $\{\texttt{001}\,p, \texttt{010}\,p\}$ with $n = |p| \ge 3$): Passing the Color Routine guard forces $B_x \le k(n)$ and $i(x) < K(n)$, hence $|s| = n + 3 \ge N_x$ and $t \ge C(n)$. Flipping at most two of the first three mode bits (first to $\texttt{011}\,p$ if router, then bit 1 to $\texttt{111}\,p$) preserves $p$, length $|s| \le \ell$, output $x$, and halting time $C(n) \le t$. Now construct $q = (u, v, b, w') \in \{0,1\}^n$ by setting $u$ to $\texttt{1}\,P_x\,\texttt{1000}\,0^{k(n) - B_x}$ (valid because $B_x \le k(n)$), $v = r_{i(x)}$ (weight $\le 1$ with $H r_{i(x)} = j_x$, the binary vector of $i(x)$), $b = \texttt{1}$, and $w' = 0^{n - 2k(n) - 1}$. By `lem:connected-syndrome-coloring` (`line 2196`), $D_n(q) = j_x$ and the color-$j_x$ class of $D_n$ is connected inside $\{0,1\}^n$, so a flip path inside $\texttt{111}\,D_n^{-1}(j_x)$ (all at length $|s| \le \ell$ and halting time $C(n) \le t$) leads from $\texttt{111}\,p$ to $\texttt{111}\,q = \texttt{1111}\,P_x\,\texttt{1000}\,w''$. Flipping bit 3 ($\texttt{111} \to \texttt{110}$) gives Hub 2 vertex $\texttt{1101}\,P_x\,\texttt{1000}\,w''$ (halting at $H(x) < C(n) \le t$), and Case 1 reaches $h_x$.
3. **Base, source-helper, and bridge vertices** ($s = \alpha(p')\,p'$ for a source helper, $s = \texttt{000}\,p'$, or $s = u\,\texttt{000}\,p'$ with $u \in \{\texttt{1}, \texttt{11}\} \cup \mathcal{U}$ and $1 \le |u| \le B_x$): Put $n_{\mathrm{body}} = |p'|$.
   - First, if $s$ is a source helper, flip its mode bit to $\texttt{000}\,p'$. If $s = u\,\texttt{000}\,p'$ is a bridge, apply single-bit deletions to strip $u$ back to $\varepsilon$: if $u = \texttt{1011}\,Q\,\texttt{1}$, delete the rightmost bit of $Q$ repeatedly (staying in $\mathcal{U}$ with $|u| \le B_x$) until $\texttt{10111}\,\texttt{000}\,p'$, then delete bits via $\texttt{10111} \to \texttt{1011} \to \texttt{101} \to \texttt{11} \to \texttt{1} \to \varepsilon$ to reach $\texttt{000}\,p'$. Every vertex along this path has length $\le |s| \le \ell$ and halts with output $x$ at the common time $T^*(n_{\mathrm{body}}, p', x) \le t$.
   - *Subcase 3a ($n_{\mathrm{body}} + 3 \ge N_x$):* Since $n_{\mathrm{body}} \ge N_x - 3 \ge 3$, we have $t \ge T^*(n_{\mathrm{body}}, p', x) > C(n_{\mathrm{body}})$, $B_x \le k(n_{\mathrm{body}})$, and $i(x) < K(n_{\mathrm{body}})$. Flip a mode bit of $\texttt{000}\,p'$ to enter its matching source helper $\alpha(p')\,p'$ ($\texttt{001}\,p'$ if $\pi(p')=0$, $\texttt{010}\,p'$ if $\pi(p')=1$; same length and halting time $T^* \le t$). By `lem:connected-syndrome-coloring` (`lines 2197, 2229`), $p'$ has a 1-bit neighbor $q'$ of opposite parity $\pi(q') \neq \pi(p')$ with $D_{n_{\mathrm{body}}}(q') = j_x$. Then $\alpha(p')\,q'$ is a router outputting $x$ at time $C(n_{\mathrm{body}}) < t$, reducing to Case 2.
   - *Subcase 3b ($n_{\mathrm{body}} + 3 < N_x$):* From $\texttt{000}\,p'$, insert bits to walk forward along the bridge:
     $$\texttt{000}\,p' \to \texttt{1000}\,p' \to \texttt{11000}\,p' \to \texttt{101000}\,p' \to \texttt{1011000}\,p' \to \texttt{10111000}\,p',$$
     and then insert the bits of $P_x$ one by one immediately before the guard $\texttt{1000}\,p'$, reaching $\texttt{1011}\,P_x\,\texttt{1000}\,p'$. Every intermediate prefix belongs to $\{\texttt{1}, \texttt{11}\} \cup \mathcal{U}$ and has length at most $p_x + 5 = B_x$, so every intermediate string halts with output $x$ at time $T^*(n_{\mathrm{body}}, p', x) \le t$, and has total length at most $(n_{\mathrm{body}} + 3) + B_x < N_x + B_x = b(x) \le \ell$. Finally, flip bit 3 ($\texttt{101} \to \texttt{100}$) to obtain Hub 1 vertex $\texttt{1001}\,P_x\,\texttt{1000}\,p'$ (halting at $H(x) < T^* \le t$), and apply Case 1 to reach $h_x$.

Since every vertex in $\mathcal{E}^t_{\ell, V}(x)$ connects to $h_x$ inside $\mathcal{E}^t_{\ell, V}(x)$, the edit graph $\mathcal{E}^t_{\ell, V}(x)$ is connected. $\square$

---

## Verification

Ran `.venv/bin/python -u targets/myrisiotis-2611.09020-edit-graph/verify.py`:
- Verified prefix-freeness, round-trip decoding, and $\texttt{00}$-freeness of $c(x)$ and $P_x = \phi(c(x))$, plus exhaustive 8-branch dispatch and determinism across all strings of length $0 \le N \le 14$;
- Verified exhaustive BFS connectivity and opposite-parity neighbor property of $D_n$ for $n = 3 \dots 13$, exact threshold $N_x$, timing inequalities $H(x) < C(n) < S(n)$, and core-to-hub attachment for all targets of length $0 \dots 5$ across 80 lengths above $N_x$;
- Verified full constructive edit-graph walks, step-by-step budget bounds $\le \ell$, and deadline bounds $\le t$ on adversarial base machines $A$ for all vertex classes (`000`, `001`, `010`, `011`, `111`, `1000`, `11000`, `101...`, `1001...`, `1101...`).
- Result: `OVERALL: PASS`.

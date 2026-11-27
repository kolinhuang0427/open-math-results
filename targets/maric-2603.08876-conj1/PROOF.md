# Proof of Global Optimality for Geometrically Weighted Lexicographic Max-Cut ($n \ge 7$)

## 1. Exact Statement, Primary Source, and Reduction

**Primary source:** Nevena Marić, *"Hierarchical threshold structure in Max-Cut with geometric edge weights"*, `arXiv:2603.08876v1` (2026-03-09), Section 5 (`\label{sec:global}`), **Conjecture 5.1 (`\label{conj:global}` [Global Optimality])**:

> **Conjecture 5.1 (Global Optimality).** For $n \geq 7$ and $r \in (r_k(n), r_{k-1}(n))$, the $k$-isolated cut $C_k$ achieves the maximum weight among all $2^{n-1}$ cuts.

**Definitions from Section 2 and Section 4 (`arXiv:2603.08876v1`):**
- Let $K_n$ be the complete graph on $[n] = \{1, \dots, n\}$ with $N = \binom{n}{2}$ edges ordered lexicographically: $(1,2), (1,3), \dots, (1,n), (2,3), \dots, (n-1,n)$. By Section 2 eq. (1), edge $(i, j)$ ($1 \le i < j \le n$) has lexicographic index $\mathrm{idx}(i, j) = (i - 1)n - \binom{i}{2} + (j - i)$ and weight
  $$w(i, j) := r^{N - \mathrm{idx}(i, j)} = r^{\binom{n - i + 1}{2} - (j - i)} \qquad (r > 1).$$
- A cut is a partition $S \mid S^c$ of $[n]$ normalized by $1 \in S$, equivalently a sign vector $\sigma \in \{+1, -1\}^n$ with $\sigma_1 = +1$ (where $\sigma_i = +1 \iff i \in S$), with weight
  $$W^n(\sigma; r) := \sum_{\substack{1 \le i < j \le n \\ \sigma_i \ne \sigma_j}} w(i, j).$$
- The **$k$-isolated cut** is $C_k := \{1, \dots, k\} \mid \{k+1, \dots, n\}$ ($\sigma = 1^k 0^{n-k}$ in $0$-$1$ notation).
- For $n \ge 6$ and $1 \le k \le \lfloor n/2 \rfloor - 1$, $P^{n,k}(r) := W^n(C_k; r) - W^n(C_{k+1}; r)$ has a unique root $r_k(n) \in (1, 2)$, satisfying $2 =: r_0(n) > r_1(n) > \cdots > r_{\lfloor n/2 \rfloor - 1}(n) > r_{\lfloor n/2 \rfloor}(n) := 1$ (Section 4, Theorems 4.7 and 4.9).
- **Marić's Theorem 4.10 (`\label{thm:isolated_optimality}`):** For $n \ge 6$, $1 \le k \le \lfloor n/2 \rfloor$, and $r \in (r_k(n), r_{k-1}(n))$, $C_k$ strictly maximizes $W^n(\cdot; r)$ among all $j$-isolated cuts with $1 \le j \le \lfloor n/2 \rfloor$.

We prove the following theorem, which settles Conjecture 5.1 completely (and in fact shows $C_k$ is the *unique* global maximizer on each threshold interval, and that no non-isolated cut is ever optimal for any $r > 1$):

> **Main Theorem.** For every integer $n \ge 7$ and every real $r > 1$, no non-isolated cut achieves the maximum weight $W^n(\cdot; r)$ among all $2^{n-1}$ cuts of $K_n$. Consequently, for every $1 \le k \le \lfloor n/2 \rfloor$ and every $r \in (r_k(n), r_{k-1}(n))$, the $k$-isolated cut $C_k$ strictly achieves the unique maximum weight among all $2^{n-1}$ cuts.

**Reduction to non-isolated cuts:** Every cut with $1 \in S$ is either:
1. $C_n = [n] \mid \emptyset$, which has $W^n(C_n; r) = 0 < W^n(C_1; r)$;
2. $C_j$ with $\lfloor n/2 \rfloor < j \le n - 1$: flipping vertex $j$ changes $C_j$ to $C_{j-1}$ with weight gain $\sum_{i=1}^{j-1} w(i, j) - \sum_{m=j+1}^n w(j, m) > 0$, because $j > \lfloor n/2 \rfloor \implies j - 1 \ge n - j$ and every edge $(i, j)$ precedes every edge $(j, m)$ in lexicographic order, so $w(i, j) > w(j, m)$ for all $r > 1$;
3. $C_j$ with $1 \le j \le \lfloor n/2 \rfloor$, among which $C_k$ is uniquely optimal on $(r_k(n), r_{k-1}(n))$ by Marić's Theorem 4.10; or
4. a **non-isolated cut**, whose sign vector $\sigma \in \{+1, -1\}^n$ ($\sigma_1 = +1$) is not of the form $1^j (-1)^{n-j}$ and hence begins with two maximal runs followed by a third run:
   $$\sigma = (+1)^a\, (-1)^{b - a}\, (+1)\, \sigma_{b+2}\cdots \sigma_n, \qquad 1 \le a < b \le n - 1.$$

It therefore suffices to show that for every $n \ge 7$, every $r > 1$, and every non-isolated cut $\sigma$, there exists an explicit move (a single-vertex flip, a two-vertex swap, a prefix flip, or for one finite subinterval of $n = 7$ a 3-vertex flip) strictly increasing $W^n(\sigma; r)$.

*(All finite rational inequalities, exact Sturm root-isolation checks, exact rational interval-arithmetic boxes, and exact integer dyadic polynomial certifications referenced in this proof are mechanically verified with zero floating-point arithmetic in [`verify.py`](verify.py).)*

---

## 2. Exact Rank-1 Factorization, Move-Gain Identities, and Scalar-$Q$ Reduction

Set $x := r^{-1} \in (0, 1)$ and $t := \ln r = -\ln x > 0$. Define
$$A_i := r^{\binom{n - i + 1}{2} + i} \quad (1 \le i \le n - 1), \qquad A_n := 0, \qquad B_j := r^{-j} = x^j \quad (1 \le j \le n).$$
Then for every $1 \le i < j \le n$,
$$A_i B_j = r^{\binom{n - i + 1}{2} + i - j} = r^{\binom{n - i + 1}{2} - (j - i)} = w(i, j),$$
and consecutive $A$-weights satisfy the exact ratio
$$\frac{A_i}{A_{i+1}} = r^{\binom{n-i+1}{2} + i - \binom{n-i}{2} - (i+1)} = r^{n - i - 1} = x^{-(n - i - 1)} \qquad (1 \le i \le n - 2).$$

For any cut $\sigma \in \{+1, -1\}^n$, since $\mathbf{1}(\sigma_i \ne \sigma_j) = \frac{1 - \sigma_i \sigma_j}{2}$, we have
$$W^n(\sigma; r) = \frac{1}{2}\sum_{1 \le i < j \le n} w(i, j) - \frac{1}{2}\sum_{1 \le i < j \le n} \sigma_i \sigma_j A_i B_j.$$
Define the prefix and suffix weighted sums for $1 \le u \le n$:
$$P_u := \sum_{i = 1}^{u - 1} \sigma_i A_i, \qquad Q_u := \sum_{j = u + 1}^{n} \sigma_j B_j, \qquad H_u := B_u P_u + A_u Q_u.$$

**Lemma 2.1 (Exact Move-Gain Identities).** For every cut $\sigma \in \{+1, -1\}^n$:
1. **Single-vertex flip** $\mathrm{flip}(u)$ ($\sigma_u \mapsto -\sigma_u$):
   $$\Delta W\bigl(\mathrm{flip}(u)\bigr) = \sigma_u H_u = \sigma_u (B_u P_u + A_u Q_u).$$
2. **Two-vertex swap** $\mathrm{swap}(u, v)$ ($1 \le u < v \le n$ with $\sigma_u = -\sigma_v$):
   $$\Delta W\bigl(\mathrm{swap}(u, v)\bigr) = \sigma_u \left[ (B_u - B_v) P_u + (A_u - A_v) Q_v + \sum_{u < m < v} \sigma_m (A_u B_m - A_m B_v) \right].$$
3. **Prefix flip** $\mathrm{flip}[1..k]$ ($1 \le k \le n - 1$, negating $\sigma_1, \dots, \sigma_k$):
   $$\Delta W\bigl(\mathrm{flip}[1..k]\bigr) = P_{k+1} \cdot Q_k.$$

*Proof.*
(1) The terms in $W^n(\sigma; r)$ involving $u$ sum to $-\frac{1}{2}\sigma_u\bigl(\sum_{i<u} \sigma_i A_i B_u + \sum_{j>u} \sigma_j A_u B_j\bigr) = -\frac{1}{2}\sigma_u H_u$; negating $\sigma_u$ adds $+\sigma_u H_u$.
(2) Negating both $\sigma_u$ and $\sigma_v$ leaves $\sigma_u \sigma_v$ unchanged and flips all edges $(i, u)$, $(i, v)$ ($i < u$), $(u, m)$, $(m, v)$ ($u < m < v$), and $(u, j)$, $(v, j)$ ($j > v$). Substituting $\sigma_v = -\sigma_u$ and collecting yields the bracketed formula.
(3) Negating $\sigma_1, \dots, \sigma_k$ flips precisely the edges $(i, j)$ with $1 \le i \le k < j \le n$, adding $\sum_{i=1}^k \sum_{j=k+1}^n \sigma_i \sigma_j A_i B_j = P_{k+1} Q_k$. $\blacksquare$

Now fix a non-isolated cut $\sigma = (+1)^a (-1)^{b-a} (+1) \sigma_{b+2}\cdots \sigma_n$ ($1 \le a < b \le n - 1$) and assume for contradiction that $\sigma$ is a global maximizer of $W^n(\cdot; r)$, so $\Delta W \le 0$ for every move. Introduce the parameters:
$$L := b - a \ge 1, \quad d := n - b - 1 \ge 0, \quad M := L + d = n - a - 1,$$
$$c_k := k M - \binom{k + 1}{2} \quad (0 \le k \le L), \qquad e_\theta := c_L = L d + \binom{L}{2},$$
$$v := x^L, \qquad u := x^M, \qquad \theta := x^{e_\theta}, \qquad y := L t, \qquad \Lambda_1 := e_\theta t, \qquad D_1 := \frac{e_\theta}{L} = d + \frac{L - 1}{2}, \qquad s := \frac{L}{2d + L - 1} = \frac{L}{2 D_1}.$$
Note that for $0 \le k \le L - 1$, $A_{a+1+k}/A_{a+1} = x^{c_k}$, and when $d \ge 1$ ($b + 1 \le n - 1$), $A_{b+1}/A_{a+1} = x^{e_\theta} = \theta$ and $A_b / A_a = x^{e_\theta + L} = \theta v$. Define
$$S(x) := \sum_{k=1}^{L-1} x^{c_k}, \qquad G(x) := \sum_{j=1}^L x^j = \frac{x(1 - v)}{1 - x}, \qquad H_{L, d}(x) := G(x) - 1 - S(x),$$
$$S_A := \sum_{i=1}^a A_i, \qquad M_A := \sum_{m=a+1}^b A_m = A_{a+1}\bigl(1 + S(x)\bigr), \qquad P_{b+1} = S_A - M_A,$$
$$Q := Q_{b+1} = \sum_{j=b+2}^n \sigma_j B_j \in [-T, T], \qquad T := \sum_{j=b+2}^n B_j = B_{a+1} \frac{x(v - u)}{1 - x}.$$

**Lemma 2.2 (Exact Scalar-$Q$ Optimality Constraints for $d \ge 1$).** When $d \ge 1$ ($b + 1 \le n - 1$), global optimality of $\sigma$ forces $Q \in [-T, T]$ to satisfy:
1. From $\mathrm{flip}(b + 1)$ ($\sigma_{b+1} = +1$):
   $$Q \le U_{\mathrm{fbp}} := -\frac{B_{b+1}}{A_{b+1}} P_{b+1}.$$
2. From $\mathrm{swap}(a + 1, b + 1)$ ($\sigma_{a+1} = -1, \sigma_{b+1} = +1$):
   $$Q \ge L_{\mathrm{sw}} := L_0 + \alpha_L (-P_{b+1}), \qquad L_0 := \frac{B_{a+1} H_{L, d}(x)}{1 - \theta}, \qquad \alpha_L := \frac{B_{a+1} - B_{b+1}}{A_{a+1} - A_{b+1}} = \frac{B_{a+1}}{A_{a+1}} \frac{1 - v}{1 - \theta}.$$
3. From $\mathrm{swap}(a, b)$ ($\sigma_a = +1, \sigma_b = -1$):
   $$Q \le U_{\mathrm{sw}} := U_0 + \alpha_U (-P_{b+1}), \qquad U_0 := \frac{B_{a+1} N_U(x)}{1 - \theta v}, \qquad \alpha_U := \frac{B_a - B_b}{A_a - A_b} = \frac{B_{a+1}}{A_{a+1}} \frac{x^{M-1}(1 - v)}{1 - \theta v},$$
   where $N_U(x) := x^{-2} G(x) - (1 - \theta v)(x^{L-1} + x^L) - x^{M-1}(1 + S(x))$. Moreover, $\alpha_L > \alpha_U$ identically.
4. From $\mathrm{flip}[1..k^*]$ when $P_{b+1} \le 0$: since $P_{a+1} = S_A > 0 \ge P_{b+1}$ and $P_{k+1}$ strictly decreases for $k = a, \dots, b$, there is a unique integer $r^* \in \{1, \dots, L - 1\}$ with
   $$\sum_{k=0}^{r^* - 1} x^{c_k} < \frac{S_A}{A_{a+1}} \le \sum_{k=0}^{r^*} x^{c_k}.$$
   Setting $k^* := a + r^* \in \{a + 1, \dots, b - 1\}$ gives $P_{k^* + 1} > 0$, so $\Delta W(\mathrm{flip}[1..k^*]) = P_{k^*+1} Q_{k^*} \le 0$ forces $Q_{k^*} = -\sum_{m=k^*+1}^b B_m + B_{b+1} + Q \le 0$, i.e.,
   $$Q \le \mathrm{hi}_p := \sum_{m = a + r^* + 1}^b B_m - B_{b+1} = B_{a+1}\left(\sum_{j = r^*}^{L - 1} x^j - v\right) = B_{a+1}\left(\frac{x^{r^*} - v}{1 - x} - v\right) > 0.$$
   (Positivity holds since $r^* \le L - 1 \implies \sum_{j=r^*}^{L-1} x^j - v \ge x^{L-1} - x^L = v(r - 1) > 0$.)

*Proof.*
(1) Directly from $\Delta W(\mathrm{flip}(b+1)) = B_{b+1} P_{b+1} + A_{b+1} Q \le 0$ with $A_{b+1} > 0$.
(2) From Lemma 2.1(2) with $(u, v) = (a+1, b+1)$, $\Delta W \le 0$ is $(A_{a+1} - A_{b+1}) Q \ge \sum_{m=a+2}^b (A_{a+1} B_m - A_m B_{b+1}) - (B_{a+1} - B_{b+1}) S_A$. Substituting $S_A = P_{b+1} + A_{a+1} + \sum_{m=a+2}^b A_m$ turns the right-hand side into
$$A_{a+1}\Bigl(\sum_{m=a+2}^{b+1} B_m - B_{a+1}\Bigr) - B_{a+1}\sum_{m=a+2}^b A_m + (B_{a+1} - B_{b+1})(-P_{b+1}) = A_{a+1} B_{a+1} H_{L,d}(x) + (B_{a+1} - B_{b+1})(-P_{b+1}).$$
Dividing by $A_{a+1} - A_{b+1} = A_{a+1}(1 - \theta) > 0$ yields $L_{\mathrm{sw}}$.
(3) From Lemma 2.1(2) with $(u, v) = (a, b)$, where $Q_b = B_{b+1} + Q$ and $P_a = S_A - A_a = P_{b+1} + M_A - A_a$, $\Delta W \le 0$ is
$$(A_a - A_b) Q \le -(A_a - A_b) B_{b+1} + \sum_{m=a+1}^{b-1}(A_a B_m - A_m B_b) - (B_a - B_b)(P_{b+1} + M_A - A_a).$$
Using $-\sum_{m=a+1}^{b-1} A_m B_b - (B_a - B_b) M_A = -B_a M_A + A_b B_b$, collecting the non-$P_{b+1}$ terms gives $A_a\bigl(B_a + \sum_{m=a+1}^{b-1} B_m - B_b - B_{b+1}\bigr) + A_b(B_b + B_{b+1}) - B_a M_A = A_a B_{a+1} N_U(x)$. Dividing by $A_a - A_b = A_a(1 - \theta v) > 0$ gives $U_{\mathrm{sw}}$. Since $(A_a - A_b) - r(A_{a+1} - A_{b+1}) = (r^M - r) A_{a+1} - (r^d - r) A_{b+1} > 0$ (as $M > d \ge 1$ and $A_{a+1} > A_{b+1}$), we have $\alpha_L > \alpha_U$.
(4) Immediate from Lemma 2.1(3) and $B_{a+1+j}/B_{a+1} = x^j$. $\blacksquare$

---

## 3. Complete Closure of All Boundary Cases ($n \ge 7$, All $r > 1$)

**Lemma 3.1 (Large First Run: $2a \ge n - 1$).** No non-isolated cut with $2a \ge n - 1$ is globally optimal for any $n \ge 3$ and $r > 1$.

*Proof.* We have $a \ge n - 1 - a = L + d$, the total number of indices in $\{a+1, \dots, b\} \cup \{b+2, \dots, n\}$. Since $1 \le i \le a < m \le b < b+1 < j \le n$ implies $w(i, b+1) > w(m, b+1)$ and $w(i, b+1) > w(b+1, j)$ (lexicographic dominance), pairing each $m \in \{a+1, \dots, b\}$ and each $j \in \{b+2, \dots, n\}$ injectively with a distinct $i \in \{1, \dots, a\}$ gives
$$\Delta W\bigl(\mathrm{flip}(b+1)\bigr) = \sum_{i=1}^a w(i, b+1) - \sum_{m=a+1}^b w(m, b+1) + \sum_{j=b+2}^n \sigma_j w(b+1, j) \ge \sum_{i=1}^a w(i, b+1) - \sum_{m=a+1}^b w(m, b+1) - \sum_{j=b+2}^n w(b+1, j) > 0. \quad \blacksquare$$

**Lemma 3.2 (Near-Isolated Boundary: $b + 1 = n$, i.e., $d = 0$, $S_a^* = 1^a 0^L 1$).** For $n \ge 7$ and $r > 1$, no cut with $b + 1 = n$ is globally optimal.

*Proof.* Here $d = 0$, $M = L = n - 1 - a$, $A_n = 0$, $Q = T = 0$.
- If $L \le 3$, then $n \ge 7 \implies a = n - 1 - L \ge n - 4 \ge (n - 1)/2$, contradicting Lemma 3.1.
- Now suppose $L \ge 4$. Optimality under $\mathrm{flip}(n)$ requires $P_n \le 0$, i.e.,
  $$x^{-L} = \frac{A_a}{A_{a+1}} \le \frac{S_A}{A_{a+1}} \le \frac{M_A}{A_{a+1}} = g_L(x) := 1 + \sum_{k=1}^{L-1} x^{c_k}, \qquad c_k = k L - \binom{k+1}{2}.$$
  Meanwhile, Lemma 2.2(2) (which holds verbatim with $A_n = 0, \theta = 0, Q = 0$) gives $0 \ge A_{a+1} B_{a+1} H_{L, 0}(x) + (B_{a+1} - B_n)(-P_n) \ge A_{a+1} B_{a+1} H_{L, 0}(x)$, forcing $H_{L, 0}(x) \le 0$. Since $c_k \ge k + 1$ for $1 \le k \le L - 1$,
  $$H_{L, 0}(x) = (x - 1) + \sum_{k=1}^{L-1}(x^{k+1} - x^{c_k}) = (1 - x)\left(-1 + \sum_{k=1}^{L-1}\sum_{m = k + 1}^{c_k - 1} x^m\right),$$
  so $H_{L, 0}(x)/(1 - x)$ is strictly increasing on $(0, 1)$.
  - **Subcase $L = 4$:** Here $c_1 = 3, c_2 = 5, c_3 = 6$, so $g_4(x) = 1 + x^3 + x^5 + x^6$ and $H_{4,0}(x)/(1-x) = -1 + x^2 + x^3 + 2x^4 + x^5$.
    For $x \in (0, 4/5]$, $x^{-4} \ge (5/4)^4 = \frac{625}{256} > 2.44 > 2.11 > 1 + (4/5)^3 + (4/5)^5 + (4/5)^6 \ge g_4(x)$, contradicting $x^{-4} \le g_4(x)$.
    For $x \in [4/5, 1)$, $H_{4,0}(x)/(1-x) \ge -1 + (4/5)^2 + (4/5)^3 + 2(4/5)^4 + (4/5)^5 = \frac{4059}{3125} > 0$, contradicting $H_{4,0}(x) \le 0$.
  - **Subcase $L \ge 5$:** Since $k + 1 \le L$, we have $c_k = k L - \frac{k(k+1)}{2} \ge \frac{k L}{2}$, so $g_L(x) \le \sum_{k=0}^{L-1} x^{k L / 2} < \frac{1}{1 - x^{L/2}}$.
    For $x \in (0, 7/10]$, $u_0 := x^L \le (7/10)^5 = \frac{16807}{100000}$, giving $x^{-L} = u_0^{-1} \ge \frac{100000}{16807} > 5.94 > 1.70 > \frac{1}{1 - \sqrt{u_0}} > g_L(x)$, contradicting $x^{-L} \le g_L(x)$.
    For $x \in [7/10, 1)$, $c_1 = L - 1 \ge 4$ contributes $x^2 + x^3$ and $c_2 = 2L - 3 \ge 7$ contributes $x^3 + x^4 + x^5 + x^6$, so $H_{L,0}(x)/(1-x) \ge -1 + x^2 + 2x^3 + x^4 \ge -1 + (7/10)^2 + 2(7/10)^3 + (7/10)^4 = \frac{4161}{10000} > 0$, contradicting $H_{L, 0}(x) \le 0$. $\blacksquare$

**Lemma 3.3 (Unit Middle Run: $L = 1$, i.e., $b = a + 1$).** For $n \ge 7$, $1 \le a \le (n - 2)/2$, $b = a + 1$, and $r > 1$, no such cut is globally optimal.

*Proof.* Here $d = n - a - 2 \ge 3$ (and $d = n - 3 \ge 4$ when $a = 1$).
- **Subcase $a = 1, b = 2$ ($\sigma = 1\,0\,1\cdots$):** Since $P_3 = A_1 - A_2 > 0$, $\mathrm{flip}[1..2]$ forces $Q \le -B_3$. Meanwhile:
  - By Lemma 2.2(2) with $L = 1$ ($H_{1,d}(x) = x - 1$, $P_3 = A_1 - A_2$), $(A_2 - A_3) L_{\mathrm{sw}} = A_2 B_2(x - 1) - (B_2 - B_3)(A_1 - A_2) = -(B_2 - B_3) A_1$. Hence $L_{\mathrm{sw}} > -B_3 \iff B_3(A_2 - A_3) > (B_2 - B_3) A_1 \iff \frac{A_2 - A_3}{r - 1} > A_1$. Dividing by $A_3$ (using $A_1/A_3 = r^{2n-5}$ and $A_2/A_3 = r^{n-3}$) gives
    $$L_{\mathrm{sw}} > -B_3 \iff r^{2n - 5} < \frac{r^{n - 3} - 1}{r - 1} = \sum_{j=0}^{n-4} r^j.$$
  - By Lemma 2.2(1), $-T > U_{\mathrm{fbp}} = -\frac{B_3}{A_3}(A_1 - A_2)$ holds iff $\frac{A_1 - A_2}{A_3} > \frac{T}{B_3} = \sum_{j=1}^{n-3} r^{-j}$. Multiplying by $r^{n-3}$ (using $\frac{A_1 - A_2}{A_3} = r^{n-3}(r^{n-2} - 1)$) gives
    $$-T > U_{\mathrm{fbp}} \iff r^{2n - 6}(r^{n - 2} - 1) > \sum_{j=0}^{n-4} r^j.$$
  - Now split at $r^{n-2} = r + 1$:
    - If $r^{n-2} \le r + 1$, then $r^{2n-5} = r^{-1}(r^{n-2})^2 \le r^{-1}(r + 1)^2 = r + 2 + r^{-1} < 1 + r + r^2 + r^3 \le \sum_{j=0}^{n-4} r^j$ (since $n \ge 7$ and $(1 + r + r^2 + r^3) - (r + 2 + r^{-1}) = (r - 1)(r^3 + 2r^2 + 2r + 1)/r > 0$), so $L_{\mathrm{sw}} > -B_3$, contradicting $Q \le -B_3$.
    - If $r^{n-2} > r + 1$, then $r^{2n-6}(r^{n-2} - 1) > r^{2n-5}$; thus either $r^{2n-5} < \sum_{j=0}^{n-4} r^j$ (giving $L_{\mathrm{sw}} > -B_3$) or $r^{2n-6}(r^{n-2} - 1) > \sum_{j=0}^{n-4} r^j$ (giving $-T > U_{\mathrm{fbp}}$). Hence one of $\mathrm{swap}(2, 3)$, $\mathrm{flip}[1..2]$, $\mathrm{flip}(3)$ strictly improves $\sigma$.
- **Subcase $a \ge 2, b = a + 1$:** Here $d = n - a - 2 \ge 3$, $A_{a+1}/A_{a+2} = r^d = x^{-d}$, $B_{a+1}/B_{a+2} = r = x^{-1}$, and $H_{1,d}(x) = x - 1$. Eliminating $Q$ between $L_{\mathrm{sw}}$ and $U_{\mathrm{fbp}}$ (Lemma 2.2(1)–(2)) gives
  $$\Delta_{\mathrm{comb}} := A_{a+2}(A_{a+1} - A_{a+2})(L_{\mathrm{sw}} - U_{\mathrm{fbp}}) = (A_{a+1} B_{a+2} - A_{a+2} B_{a+1}) P_{a+2} + A_{a+1} A_{a+2} B_{a+1}(x - 1).$$
  Dividing by $A_{a+1} A_{a+2} B_{a+1} = A_{a+1} A_{a+2} B_{a+2} x^{-1}$ and substituting $P_{a+2}/A_{a+1} = \frac{S_A}{A_{a+1}} - 1$ gives
  $$\frac{\Delta_{\mathrm{comb}}}{A_{a+1} A_{a+2} B_{a+1}} = (x - x^d)\left(\frac{S_A}{A_{a+1}} - 1\right) + (x - 1) = (x - x^d)\frac{S_A}{A_{a+1}} - (1 - x^d) = (1 - x^{d-1})\left(x\frac{S_A}{A_{a+1}}\right) - (1 - x^d).$$
  Since $a \ge 2$ and $M = d + 1 \ge 4$, we have $x\frac{S_A}{A_{a+1}} \ge x\bigl(\frac{A_a + A_{a-1}}{A_{a+1}}\bigr) = x^{-(M-1)} + x^{-2M} > 2$ for all $x \in (0, 1)$. Setting $f(x) := 2(1 - x^{d-1}) - (1 - x^d) = 1 - 2x^{d-1} + x^d$, we have $f(1) = 0$ and $f'(x) = x^{d-2}(dx - 2d + 2) < 0$ on $(0, 1)$ for all $d \ge 3$ (as $dx < d \le 2d - 2$), so $f(x) > 0$ on $(0, 1)$. Thus $\Delta_{\mathrm{comb}} > 0$, contradicting $L_{\mathrm{sw}} \le Q \le U_{\mathrm{fbp}}$. $\blacksquare$

By Lemmas 3.1–3.3, every remaining non-isolated cut is an **interior** triple $(n, a, b)$ satisfying
$$1 \le a \le \frac{n - 2}{2}, \qquad L = b - a \ge 2, \qquad d = n - b - 1 \ge 1.$$

---

## 4. Complete Closure of Region I ($P_{b+1} > 0$, All $n \ge 7$) and Exact Closure of $n = 7$

**Theorem 4.1 (Region I: $P_{b+1} > 0$, All $n \ge 7$, All $r > 1$).** No interior non-isolated cut with $P_{b+1} > 0$ is globally optimal for any $n \ge 7$ and $r > 1$.

*Proof.* Assume $\mathrm{flip}(b+1)$ does not beat $-T$ (i.e., $-T \le U_{\mathrm{fbp}}$) and $\mathrm{swap}(a+1, b+1)$ does not beat $\mathrm{flip}(b+1)$ (i.e., $L_{\mathrm{sw}} \le U_{\mathrm{fbp}}$).
1. **Exact positive-coefficient factorization of $H_{L,d}(x)$:** Since $c_k = k(L + d) - \binom{k+1}{2} \ge k + 1$ for $1 \le k \le L - 1$,
   $$H_{L,d}(x) = (x - 1) + \sum_{k=1}^{L-1}(x^{k+1} - x^{c_k}) = (1 - x)\left(-1 + \sum_{k=1}^{L-1}\sum_{m=k+1}^{c_k - 1} x^m\right),$$
   so $H_{L,d}(x)/(1 - x)$ is strictly increasing on $(0, 1)$ for every $(L, d) \ne (2, 1)$ (which holds for all interior triples with $n \ge 7$, since $(L, d) = (2, 1)$ forces $2a \le n - 2 \implies n \le 6$).
2. **Upper bound from $-T \le U_{\mathrm{fbp}}$:** Since $P_{b+1} \le \frac{A_{b+1}}{B_{b+1}} T = A_{b+1}\sum_{j=1}^d x^j$ and $S_A \ge A_a = x^{-M} A_{a+1}$,
   $$x^{-M} \le 1 + S(x) + E(x), \qquad E(x) := x^{e_\theta}\sum_{j=1}^d x^j. \qquad (\star)$$
3. **Elimination identity:** From Lemma 2.2(1)–(2),
   $$\Delta_{\mathrm{comb}} := A_{b+1}(A_{a+1} - A_{b+1})(L_{\mathrm{sw}} - U_{\mathrm{fbp}}) = (A_{a+1} B_{b+1} - A_{b+1} B_{a+1}) P_{b+1} + A_{a+1} A_{b+1} B_{a+1} H_{L,d}(x).$$
   Since $\frac{A_{a+1} B_{b+1}}{A_{b+1} B_{a+1}} = x^{-(e_\theta - L)} = x^{-(L(d-1) + \binom{L}{2})} > 1$ (as $L \ge 2, d \ge 1$) and $P_{b+1} > 0$, whenever $H_{L, d}(x) > 0$ we immediately get $\Delta_{\mathrm{comb}} > 0$, contradiction.
4. **Case $L = 2, d \ge 3$ ($M = d + 2 \ge 5$):** Take $x_* := 19/25$. For $x \in (0, x_*]$, $x^{-M} \ge (25/19)^5 > 3.94$, while $1 + S(x) + E(x) = 1 + x^{d+1} + x^{2d+1}\sum_{j=1}^d x^j < 1 + x_*^4 + \frac{x_*^8}{1 - x_*} < 1.80 < 3.94$, contradicting $(\star)$. Hence $x > x_*$, giving $\frac{H_{2,d}(x)}{1-x} = -1 + \sum_{m=2}^d x^m \ge -1 + x^2 + x^3 > -1 + (19/25)^2 + (19/25)^3 = \frac{259}{15625} > 0$.
5. **Case $L \ge 3, d \ge 1$ ($M \ge 4$):** Take $x_* := 7/10$. Since $c_1 = M - 1 \ge 3$ and $c_k - c_{k-1} = M - k \ge d + 1 \ge 2$, $S(x) \le \frac{x^3}{1 - x^2}$. Also $e_\theta + 1 \ge 7$, so $E(x) < \frac{x^7}{1 - x}$. For $x \in (0, x_*]$, $x^{-M} \ge (10/7)^4 > 4.16$, while $1 + S(x) + E(x) < 1 + \frac{(7/10)^3}{1 - (7/10)^2} + \frac{(7/10)^7}{3/10} < 1.95 < 4.16$, contradicting $(\star)$. Hence $x > x_*$, and since $c_1 \ge 3$ (contributing $x^2$) and $c_2 = 2M - 3 \ge 5$ (contributing $x^3 + x^4$), $\frac{H_{L,d}(x)}{1-x} \ge -1 + x^2 + x^3 + x^4 > -1 + (7/10)^2 + (7/10)^3 + (7/10)^4 = \frac{731}{10000} > 0$.
6. **Remaining $L = 2, d \le 2$ ($n \ge 7, 2a \le n - 2$):** $d = 1$ forces $2(n - 4) \le n - 2 \implies n \le 6$ (impossible). $d = 2$ forces $2(n - 5) \le n - 2 \implies (n, a, b) \in \{(7, 2, 4), (8, 3, 5)\}$. For both, $H_{2,2}(x) = -(1 - x)^2(1 + x)$, $\frac{A_{a+1} B_{b+1}}{A_{b+1} B_{a+1}} = x^{-3}$, and since $a \ge 2$ and $M = 4$, for all $x \in (0, 1)$,
   $$\frac{P_{b+1}}{A_{a+1}} \ge x^{-9} + x^{-4} - 1 - x^3 = (x^{-9} - 1) + (x^{-4} - x^3) > (x^{-9} - 1) + (x^{-4} - 1) > 9(1 - x) + 4(1 - x) = 13(1 - x),$$
   while $x^{-3} - 1 = (1 - x)(x^{-1} + x^{-2} + x^{-3}) > 3(1 - x)$. Hence
   $$\frac{\Delta_{\mathrm{comb}}}{A_{a+1} A_{b+1} B_{a+1}} = (x^{-3} - 1)\frac{P_{b+1}}{A_{a+1}} - (1 - x)^2(1 + x) > 39(1 - x)^2 - 2(1 - x)^2 = 37(1 - x)^2 > 0$$
   unconditionally for all $x \in (0, 1)$. $\blacksquare$

**Theorem 4.2 (Exact Finite Closure for $n = 7$, All $r > 1$).** No interior non-isolated cut of $K_7$ is globally optimal for any $r > 1$.

*Proof.* The interior triples of $n = 7$ ($1 \le a \le 2, L \ge 2, d \ge 1$) are $(7,1,3)$, $(7,1,4)$, $(7,1,5)$, $(7,2,4)$, and $(7,2,5)$. For each triple, every constraint $P_{b+1}$, $-T - U_{\mathrm{fbp}}$, $L_{\mathrm{sw}} - U_{\mathrm{fbp}}$, $L_{\mathrm{sw}} - U_{\mathrm{sw}}$, $L_{\mathrm{sw}} - T$, $P_{k+1}$, and $L_{\mathrm{sw}} - \delta_k$ (where $\delta_k := \sum_{m=k+1}^b B_m - B_{b+1}$) is an explicit rational function of $x \in (0, 1)$ with positive denominator on $(0, 1)$. Using exact integer Sturm chains (`sympy.count_roots`, Section 3 of `verify.py`), $(0, 1)$ is partitioned into dyadic subintervals certifying:
- For $(7, 1, 3)$, $(7, 1, 5)$, $(7, 2, 4)$, and $(7, 2, 5)$: on every subinterval, either $(P_{b+1} > 0) \land ((-T > U_{\mathrm{fbp}}) \lor (L_{\mathrm{sw}} > U_{\mathrm{fbp}}))$, or $(P_{b+1} \le 0) \land ((L_{\mathrm{sw}} > U_{\mathrm{sw}}) \lor (L_{\mathrm{sw}} > T) \lor \exists\,k\,(P_{k+1} > 0 \land L_{\mathrm{sw}} > \delta_k))$.
- For $(7, 1, 4)$ ($\sigma = 1\,0\,0\,0\,1\,\sigma_6\,\sigma_7$): the exact same disjunction covers all of $(0, 1) \setminus [q_1, q_2]$ where $[q_1, q_2] := \bigl[\frac{231}{256}, \frac{467}{512}\bigr]$. On $[q_1, q_2]$, exact Sturm counts confirm $P_5 < 0$ everywhere, $P_4 = A_1 - A_2 - A_3$ has its unique root inside $(q_1, q_2)$, and $L_{\mathrm{sw}} - U_{\mathrm{sw}}$ has its unique root inside $(q_1, q_2)$. Consider the 3-vertex flip $F := \{1, 3, 4\}$; since $6, 7 \notin F$, its weight gain $\Delta W(F)$ is an exact affine function of $Q = \sigma_6 B_6 + \sigma_7 B_7$:
  $$\Delta W(F) = \sum_{\substack{1 \le i < j \le 5 \\ |F \cap \{i,j\}| = 1}} \sigma_i \sigma_j A_i B_j + (A_1 - A_3 - A_4)\, Q.$$
  On $[q_1, q_2]$, any surviving cut has $Q \in [L_{\mathrm{sw}}, \min(U_{\mathrm{sw}}, \delta_3)]$ (since $\delta_3 = B_4 - B_5$ when $P_4 > 0$, and $U_{\mathrm{sw}}$ always applies). Exact Sturm chains (`verify.py` Section 3) verify that each of $\Delta W(F)\big|_{Q = L_{\mathrm{sw}}}$, $\Delta W(F)\big|_{Q = U_{\mathrm{sw}}}$, and $\Delta W(F)\big|_{Q = \delta_3}$ has **zero roots** on $[q_1, q_2]$ and is strictly positive at both endpoints $q_1, q_2$. By affineness in $Q$, $\Delta W(F) > 0$ for every $Q \in [L_{\mathrm{sw}}, \min(U_{\mathrm{sw}}, \delta_3)]$ and every $x \in [q_1, q_2]$. $\blacksquare$

---

## 5. Complete Closure of Region II/III ($P_{b+1} \le 0$, $n \ge 8$, All $r > 1$)

Assume henceforth that $n \ge 8$, $1 \le a \le (n - 2)/2$, $L \ge 2$, $d \ge 1$, and **$P_{b+1} \le 0$** (i.e., $S_A \le M_A$).

### 5.1 Structural Preliminaries and Exact Identities

**Proposition 5.0 (Preliminary Bounds & Exact $\mathcal{N}$-Decomposition).** Under $n \ge 8$ and $P_{b+1} \le 0$:
1. **$a < L$, $M \ge 5$, $(L, d) \notin \{(2, 1), (2, 2)\}$, and $a = 1 \implies M \ge 6$.**
   *Proof.* If $a \ge L$, then pairing each $A_{a+1+k}$ ($0 \le k \le L - 1$) with $A_{a-k} > A_{a+1+k}$ yields $S_A > M_A$, contradicting $P_{b+1} \le 0$. Thus $a \le L - 1$. Since $n = a + L + d + 1 \ge 8$, if $M = L + d \le 4$ then $a \le L - 1 \le 2$ gives $n \le 7$ (contradiction), and if $(L, d) = (2, 2)$ then $a = 1$ gives $n = 6 < 8$. For $a = 1$, $M = n - 2 \ge 6$.
2. **Universal compact-window bound $u = x^M > \phi^{-2} = \frac{3 - \sqrt{5}}{2} > \frac{38}{100}$:**
   Since $k + 1 \le L < M$, we have $c_k = k M - \binom{k+1}{2} > \frac{k M}{2}$ for all $1 \le k \le L - 1$, so $P_{b+1} \le 0$ gives
   $$u^{-1} = \frac{A_a}{A_{a+1}} \le \frac{S_A}{A_{a+1}} \le 1 + \sum_{k=1}^{L-1} x^{c_k} < \sum_{k=0}^\infty u^{k/2} = \frac{1}{1 - \sqrt{u}} \implies u + \sqrt{u} > 1 \implies u > \phi^{-2} > \frac{38}{100}.$$
   Also, $c_k = k d + k L - \frac{k(k+1)}{2} \ge k\bigl(d + \frac{L}{2}\bigr)$ for all $1 \le k \le L - 1$, so $x^{c_k} \le (u / \sqrt{v})^k$ and $1 + S(x) \le \frac{1 - (u/\sqrt{v})^L}{1 - u/\sqrt{v}} < \frac{1}{1 - u/\sqrt{v}}$.
3. **Exact $L_{\mathrm{sw}} - U_{\mathrm{sw}}$ core decomposition:** From Lemma 2.2(2)–(3),
   $$L_{\mathrm{sw}} - U_{\mathrm{sw}} = (\alpha_L - \alpha_U)(-P_{b+1}) + (L_0 - U_0), \qquad \frac{(1 - \theta)(1 - \theta v)}{B_{a+1}}(L_0 - U_0) = \mathcal{N}(L, d, x),$$
   where
   $$\mathcal{N}(L, d, x) := \theta(1 - v) H_{L, d}(x) + (1 - \theta)\bigl(W_0(L, d, x) - S_{\mathrm{err}}(L, d, x)\bigr),$$
   $$W_0(L, d, x) := (r - \theta) - (1 - v)\bigl[2(1 + r) - \theta(1 + v + vr)\bigr] = 4v - 3 - \theta v(2v - 1) + (r - 1)\bigl(2v - 1 + \theta v(1 - v)\bigr),$$
   $$S_{\mathrm{err}}(L, d, x) := \sum_{k=2}^{L-1} x^{c_k}(1 - x^{k-1}).$$
   *Proof.* $(1 - \theta v) H_{L,d} - (1 - \theta) N_U = \theta(1 - v) H_{L,d} + (1 - \theta)(H_{L,d} - N_U)$. Using $G(x) - x^{-2} G(x) = -(1 - v)(1 + r)$ and the exact shift identity $c_k + (M - 1) = c_{k+1} + k$ ($0 \le k \le L - 1$, with $c_L = e_\theta$), we telescope $(1 - x^{M-1})(1 + S(x)) = 1 - \theta v r + \sum_{k=2}^{L-1} x^{c_k}(1 - x^{k-1}) = 1 - \theta v r + S_{\mathrm{err}}$. Collecting the remaining terms yields $H_{L,d} - N_U = W_0 - S_{\mathrm{err}}$, and expanding $W_0$ in $(r - 1)$ gives the second form identically.
4. **Quadratic exponent parametrization and convex midpoint / chord bounds:** For every $1 \le k \le L - 1$,
   $$c_k = \frac{k}{L} e_\theta + \frac{k(L - k)}{2} \implies c_k t = \Lambda_1\, f(k/L), \qquad f(u) := u + s u(1 - u), \quad s = \frac{L}{2d + L - 1} \in (0, 1].$$
   Since $f$ is strictly increasing ($f'(u) = 1 + s(1 - 2u) \ge 1 - s \ge 0$) and concave ($f''(u) = -2s < 0$) on $[0, 1]$, the function $g(u) := e^{-\Lambda_1 f(u)}$ is strictly decreasing and **strictly convex** ($g''(u) = (\Lambda_1^2 f'(u)^2 + 2 s \Lambda_1) g(u) > 0$). Hence:
   - By the Hermite–Hadamard midpoint inequality on $[(k - \frac{1}{2})/L, (k + \frac{1}{2})/L]$,
     $$S(x) = \sum_{k=1}^{L-1} g(k/L) \le L \int_{1/(2L)}^{1 - 1/(2L)} g(u)\,du \le L \int_0^1 g(u)\,du - \frac{e^{-\Lambda_1/L} + \theta}{2},$$
     using $g(u) \ge g(\frac{1}{2L}) \ge e^{-\Lambda_1/L}$ on $[0, \frac{1}{2L}]$ (as $f(\frac{1}{2L}) < \frac{1}{L}$) and $g(u) \ge g(1) = \theta$ on $[1 - \frac{1}{2L}, 1]$.
   - For any $m \ge 1$, the inscribed $m$-piece polyline $f_m$ interpolating $f$ at $u_j = j/m$ satisfies $f_m(u) \le f(u)$ on $[0, 1]$ (concavity), so $I_0^{(m)}(\Lambda_1, s) := \int_0^1 e^{-\Lambda_1 f_m(u)}\,du \ge \int_0^1 g(u)\,du$ and $J_m(\Lambda_1, s) := 2 s \Lambda_1 \int_0^1 u e^{-\Lambda_1 f_m(u)}\,du \ge 2 s \Lambda_1 \int_0^1 u g(u)\,du$. Similarly, the circumscribed $m$-piece midpoint-tangent envelope $f_{\mathrm{tan}, m}$ satisfies $f_{\mathrm{tan}, m}(u) \ge f(u)$.
   - Since $1 - x^{k-1} \le (k - 1) t$, $L^2 t = 2 s \Lambda_1$, and $u g(u) \ge \frac{k-1}{L} g(k/L)$ on $[(k-1)/L, k/L]$,
     $$S_{\mathrm{err}}(L, d, x) \le (1 - x)\sum_{k=2}^{L-1}(k - 1) x^{c_k} \le 2 s \Lambda_1 \int_0^{(L-1)/L} u g(u)\,du \le J_m(\Lambda_1, s) < \frac{2}{\Lambda_1},$$
     where the last inequality uses $f(u) \ge u$ and $2 s \Lambda_1 \int_0^1 u e^{-\Lambda_1 u}\,du = 2s \frac{1 - (1+\Lambda_1)e^{-\Lambda_1}}{\Lambda_1} < \frac{2}{\Lambda_1}$.
   - Using $\frac{1}{e^t - 1} > \frac{1}{t} - \frac{1}{2}$ for all $t > 0$ (as $\frac{t}{2}\coth\frac{t}{2} > 1$), we have $G(x) = \frac{1-v}{e^t - 1} > L \phi_1(y) - \frac{1-v}{2}$, where $\phi_1(z) := \frac{1 - e^{-z}}{z}$ and $\phi_2(z) := \frac{1 - (1+z)e^{-z}}{z^2}$ are both strictly decreasing on $[0, \infty)$.
5. **Exact rational interval certification (`verify.py`):** All elementary transcendental functions ($e^{-q}$, $\ln(1/q)$, $\phi_1(q)$, $\phi_2(q)$, $\sqrt{q}$, $q^{p/r}$) are enclosed rigorously using exact alternating Taylor series / integer-power bisection over `fractions.Fraction` with outward dyadic rounding (zero floating-point operations). Univariate polynomials $P(x) = P_+(x) - P_-(x)$ ($P_\pm$ having nonnegative integer coefficients) are certified strictly positive on dyadic intervals $[p_{\mathrm{lo}}/2^k, p_{\mathrm{hi}}/2^k] \subset (0, 1)$ by exact integer verification of $2^{kD} P_+(p_{\mathrm{lo}}/2^k) > 2^{kD} P_-(p_{\mathrm{hi}}/2^k)$.

---

### 5.2 Theorem 5.1 (Lemma A — Small $r^L \le \frac{61}{50} = 1.22$, All $a \ge 1$)

**Theorem 5.1.** For all $n \ge 8$, $a \ge 1$, $M \ge 5$, $(L, d) \notin \{(2, 1), (2, 2)\}$, $P_{b+1} \le 0$, and $r^L \le \frac{61}{50}$ (equivalently $v \ge \frac{50}{61}$), we have $L_0 > U_0$ (and hence $L_{\mathrm{sw}} > U_{\mathrm{sw}}$).

*Proof.* By Proposition 5.0(3), it suffices to show $\mathcal{N}(L, d, x) > 0$.

1. **Case $L = 2, d \ge 3$:** Here $S_{\mathrm{err}} = 0$ identically, $v = x^2 \ge \frac{50}{61} > \frac{81}{100}$ (so $x > \frac{9}{10}$), and $H_{2,d}(x) > 0$ (Theorem 4.1(4)). In $W_0 = 4v - 3 - \theta v(2v - 1) + (r - 1)(2v - 1 + \theta v(1-v))$, the coefficient of $\theta = x^{2d+1}$ is $x - x^3 - x^4 = x(1 - x^2 - x^3) < 0$ on $x > \frac{9}{10}$, so $W_0(2, d, x)$ is strictly increasing in $d$. Hence
   $$\frac{W_0(2, d, x)}{1 - x} \ge \frac{W_0(2, 3, x)}{1 - x} = -x^{-1} - 3 - x + \sum_{k=2}^6 x^k + x^7(1 + x)(1 + x + x^2) > -\frac{10}{9} - 4 + \sum_{k=2}^6 \left(\frac{9}{10}\right)^k + \left(\frac{9}{10}\right)^7 \frac{19}{10} \cdot \frac{271}{100} > \frac{3}{5} > 0$$
   for all $x \in (\frac{9}{10}, 1)$. Thus $\mathcal{N}(2, d, x) > 0$.

Assume now $L \ge 3, d \ge 1, M \ge 5$, so $D_1 = d + \frac{L - 1}{2} = \frac{M + d - 1}{2} \ge \frac{5}{2}$ and $y = \frac{\Lambda_1}{D_1} \le \min\bigl(\ln\frac{61}{50}, \frac{2}{5}\Lambda_1\bigr)$.

2. **Case $\Lambda_1 \ge 8$ (A1):** Since $x \ge v^{1/3} \ge (50/61)^{1/3} > 0.935 > 7/10$, Theorem 4.1(5) gives $H_{L,d}(x) > 0$. Using $v \ge \frac{50}{61}$, $r > 1$, $\theta \le e^{-8}$, and Proposition 5.0(4),
   $$W_0 > 4v - 3 - \theta \ge \frac{17}{61} - e^{-8} > \frac{1}{4} \ge \frac{2}{\Lambda_1} > S_{\mathrm{err}},$$
   verified in exact rational arithmetic (`verify.py` Section 2). Hence $\mathcal{N}(L, d, x) > 0$.

3. **Case $0 < \Lambda_1 \le \frac{1}{5}$ (A2-small):** From $H_{L,d}(x) = (1 - x)\bigl(-1 + \sum_{k=1}^{L-1}\sum_{m=k+1}^{c_k - 1} x^m\bigr) \ge (1 - x)\bigl(-1 + \sum_{k=1}^{L-1}(c_k - k - 1) r x^{c_k}\bigr)$, $S_{\mathrm{err}} \le (1 - x)\sum_{k=2}^{L-1}(k - 1) x^{c_k}$, and the exact algebraic identity (verified symbolically in `verify.py` Section 1)
   $$(c_k - k - 1) - (k - 1) D_1 = d + \frac{k(L - k - 2) + L - 3}{2} \ge d - 1 \ge 0 \qquad (\forall\, 2 \le k \le L - 1),$$
   setting $\alpha := \frac{\theta(1 - v) r D_1}{1 - \theta} = \frac{\Lambda_1}{e^{\Lambda_1} - 1} \cdot \phi_1(y) \cdot r$ yields
   $$\frac{\mathcal{N}(L, d, x)}{1 - \theta} \ge W_0 + \frac{\theta(1 - v)}{1 - \theta}(1 - x)\bigl((M - 3) x^{M-2} - 1\bigr) - (1 - \alpha)_+ (1 - x)\sum_{k=2}^{L-1}(k - 1) x^{c_k}.$$
   Here $(M - 3) x^{M-2} - 1 > 0$ unconditionally: for $M = 5$ ($L \in \{3, 4\}$), $2 x^3 \ge 2 v \ge 100/61 > 1$; for $M \ge 6$, $(M - 3) x^{M-2} > 3 u > 3 \cdot \frac{38}{100} = 1.14 > 1$. Next, using $\frac{z}{e^z - 1} > 1 - \frac{z}{2}$ and $\phi_1(y) > 1 - \frac{y}{2}$ for all $z, y > 0$ together with $y \le \frac{2}{5}\Lambda_1$ and $r > 1$, we get $\alpha > (1 - \frac{\Lambda_1}{2})(1 - \frac{y}{2}) > 1 - \frac{\Lambda_1 + y}{2} \ge 1 - \frac{7}{10}\Lambda_1$, so $(1 - \alpha)_+ < \frac{7}{10}\Lambda_1$. Also $(1 - x)\sum_{k=2}^{L-1}(k-1)x^{c_k} < t \frac{L^2}{2} = s \Lambda_1 \le \Lambda_1$. Meanwhile, $1 - \theta \ge \Lambda_1 - \frac{\Lambda_1^2}{2}$, $v(2v - 1) = 1 - 3(1-v) + 2(1-v)^2 > 1 - 3y \ge 1 - \frac{6}{5}\Lambda_1$, and $(1-v)(3-2v) < y(1+2y) \le \frac{2}{5}\Lambda_1(1 + \frac{4}{5}\Lambda_1)$, so
   $$W_0 > (1 - \theta)v(2v - 1) - (1 - v)(3 - 2v) > \left(\Lambda_1 - \frac{\Lambda_1^2}{2}\right)\left(1 - \frac{6}{5}\Lambda_1\right) - \frac{2}{5}\Lambda_1\left(1 + \frac{4}{5}\Lambda_1\right).$$
   Subtracting $(1 - \alpha)_+ \Lambda_1 < \frac{7}{10}\Lambda_1^2$ gives, for all $\Lambda_1 \in (0, 1/5]$,
   $$\frac{\mathcal{N}(L, d, x)}{1 - \theta} > \Lambda_1\left(\frac{3}{5} - \frac{68}{25}\Lambda_1 + \frac{3}{5}\Lambda_1^2\right) > \Lambda_1\left(\frac{3}{5} - \frac{68}{125}\right) = \frac{7}{125}\Lambda_1 > 0.$$

4. **Case $\frac{1}{5} \le \Lambda_1 \le 8$, $L \ge 12$:** Combining Proposition 5.0(4) ($m = 4$), $W_0 > W_{0,r1} := 4v - 3 - \theta v(2v - 1)$, $e^{-\Lambda_1/L} \ge e^{-\Lambda_1/12}$, and $\frac{\theta(1-v)}{1-\theta} L = 2 s \frac{\theta}{\phi_1(\Lambda_1)} \phi_1(y)$ gives
   $$\frac{\mathcal{N}(L, d, x)}{1 - \theta} \ge \Phi_{12}(\Lambda_1, s, y) := W_{0,r1}(\Lambda_1, y) + 2 s \frac{\theta}{\phi_1(\Lambda_1)}\phi_1(y)\bigl(\phi_1(y) - I_0^{(4)}(\Lambda_1, s)\bigr) - \frac{\theta(1 - v)}{1 - \theta}\frac{3 - v - e^{-\Lambda_1/12} - \theta}{2} - J_4(\Lambda_1, s),$$
   on $(\Lambda_1, s) \in [\frac{1}{5}, 8] \times (0, 1]$ and $y \in (0, y_{\max}(\Lambda_1, s)]$ with $y_{\max}(\Lambda_1, s) := \min\bigl(\ln\frac{61}{50}, \frac{s\Lambda_1}{6}\bigr)$. On every sub-box where $\phi_1(y_{\max}) > I_0^{(4)}(\Lambda_1, s)$, every $y$-dependent term of $\Phi_{12}$ is strictly decreasing in $y$ (since $\frac{\partial W_{0,r1}}{\partial v} = 4 - \theta(4v - 1) > 0$, $\phi_1(y)$ is decreasing, and $(1-v)(3 - v - e^{-\Lambda_1/12} - \theta)$ is increasing in $y$), so $\Phi_{12}(\Lambda_1, s, y) \ge \Phi_{12}(\Lambda_1, s, y_{\max})$. Exact rational 2D box subdivision (`verify.py` Section 4a, 1,193 boxes) verifies both $\phi_1(y_{\max}) > I_0^{(4)}$ and $\Phi_{12}(\Lambda_1, s, y_{\max}) > 0$ on all of $[\frac{1}{5}, 8] \times [0, 1]$.

5. **Case $\frac{1}{5} \le \Lambda_1 \le 8$, $3 \le L \le 11$:** Setting $z := \theta^{1/L} = x^{d + (L-1)/2}$ and $w := x$ ($L$ odd) or $w := \sqrt{x}$ ($L$ even), we have $x^{c_k} = z^k x^{k(L-k)/2}$, so $Q_L(w, z) := x \cdot \mathcal{N}(L, d, x)$ is an explicit integer-coefficient bivariate polynomial in $(w, z)$ independent of $d$, on the compact region $w \in [(50/61)^{1/L}\text{ or }(50/61)^{1/(2L)},\, 1]$ and $z \in [e^{-8/L}, \min(e^{-1/(5L)}, w^{\eta_L})]$ where $d_0 := \max(1, 5 - L)$ and $\eta_L := d_0 + \frac{L-1}{2}$ ($L$ odd) or $2d_0 + L - 1$ ($L$ even). Since $z \le e^{-1/(5L)} < 1$, $Q_L(1, z) = (1 - z^L)^2 > 0$ has no singularity at $w = 1$. Exact rational first-order centered-form 2D subdivision (`verify.py` Section 4b, 1,182 boxes across $L = 3, \dots, 11$) certifies $Q_L(w, z) > 0$ everywhere on each feasible region. $\blacksquare$

---

### 5.3 Exact Linear $v$-Elimination Principle (Used in Theorems 5.2 and 5.4)

**Lemma 5.2 (Exact Linear $v$-Elimination of $L_{\mathrm{sw}} \le T$ and $L_{\mathrm{sw}} \le \mathrm{hi}_p$).** Suppose $P_{b+1} \le 0$ and write $S_0 := S_A / A_{a+1}$, $\Delta_P := 1 + S(x) - S_0 \ge 0$, $G_{r^*} := \sum_{j=1}^{r^* - 1} x^j$. If $\Delta_P < 2$ and
$$E(S_0, r^*) := 2\bigl(1 + u + G_{r^*} - r S_0\bigr) - \Delta_P\bigl(1 + u - (r - 1) G_{r^*}\bigr) > 0,$$
then $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$ holds strictly. Moreover, $(r - 1) G_{r^*} = 1 - x^{r^*-1} < 1$, so $1 + u - (r - 1) G_{r^*} > u > 0$, and for fixed $r^*$ the quantity $E(S_0, r^*)$ is strictly decreasing in $S_0$.

*Proof.* Recall $(1 - \theta) L_{\mathrm{sw}}/B_{a+1} = G(x) - v(1 + S(x)) - (1 - v) S_0 = G(x) - (S_0 + v \Delta_P)$. Assume for contradiction that both $L_{\mathrm{sw}} \le T$ and $L_{\mathrm{sw}} \le \mathrm{hi}_p$ hold.
- From $L_{\mathrm{sw}} \le T$, dropping $\theta T / B_{a+1} > 0$ gives $G(x) - T/B_{a+1} = \frac{x(1 - 2v + u)}{1 - x} < S_0 + v \Delta_P$, i.e., multiplying by $r - 1 = \frac{1 - x}{x} > 0$:
  $$\bigl(2 + (r - 1)\Delta_P\bigr) v > 1 + u - (r - 1) S_0. \qquad (E_1)$$
- From $L_{\mathrm{sw}} \le \mathrm{hi}_p$, since $G(x) - \mathrm{hi}_p / B_{a+1} = G_{r^*} + 2v$ and $\theta \mathrm{hi}_p / B_{a+1} > 0$, we obtain $G_{r^*} + 2v < S_0 + v \Delta_P$, i.e.,
  $$(2 - \Delta_P) v < S_0 - G_{r^*}. \qquad (E_2)$$
Multiplying $(E_1)$ by $(2 - \Delta_P) > 0$ and $(E_2)$ by $(2 + (r - 1)\Delta_P) > 0$ and eliminating $v$ gives
$$(2 - \Delta_P)\bigl(1 + u - (r - 1) S_0\bigr) < \bigl(2 + (r - 1)\Delta_P\bigr)(S_0 - G_{r^*}).$$
Expanding both sides cancels the $\pm (r - 1)\Delta_P S_0$ terms identically and rearranges to $E(S_0, r^*) < 0$, contradicting $E(S_0, r^*) > 0$. Finally, $(r - 1) G_{r^*} = (x^{-1} - 1)\sum_{j=1}^{r^*-1} x^j = 1 - x^{r^*-1} < 1$, and $\frac{\partial E}{\partial S_0} = -2r + 1 + u - (r - 1) G_{r^*} = -(2r - 1 - u) - (r - 1) G_{r^*} < 0$. $\blacksquare$

---

### 5.4 Theorem 5.2 (Lemma B1 — $a \ge 2$, $r^L \ge \frac{61}{50}$, $M \ge 5$)

**Theorem 5.2.** For all $n \ge 8$, $a \ge 2$, $M \ge 5$, $P_{b+1} \le 0$, and $r^L \ge \frac{61}{50}$ ($v \le \frac{50}{61}$), we have $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$.

*Proof.* Since $a \ge 2$, $S_0 = \frac{S_A}{A_{a+1}} \ge \frac{A_a + A_{a-1}}{A_{a+1}} = u^{-1} + r u^{-2} > u^{-1} + u^{-2}$. Since $L \le M - 1$, $1 + S(x) \le F_M(u) := 1 + \sum_{k=1}^{M-2} u^{k - k(k+1)/(2M)}$, which is strictly increasing in $u$. Moreover, for any $M \ge M_0$ and $K \le M_0$, every term $1 \le k \le K$ has $k - \frac{k(k+1)}{2M} \ge k - \frac{k(k+1)}{2M_0}$, while every $k > K$ has $k - \frac{k(k+1)}{2M} > \frac{k}{2}$, giving the uniform upper bound
$$F_M(u) < F_{M_0, K}^{\mathrm{ub}}(u) := 1 + \sum_{k=1}^K u^{k - k(k+1)/(2M_0)} + \frac{u^{(K+1)/2}}{1 - \sqrt{u}} \qquad (\forall\, M \ge M_0).$$

1. **Step 1 (Sharp bound $u > \frac{33}{50}$):** At $u_0 := \frac{33}{50}$, exact rational checks (`verify.py` Section 5) verify $F_{17, 13}^{\mathrm{ub}}(u_0) < u_0^{-1} + u_0^{-2}$ and $F_M(u_0) < u_0^{-1} + u_0^{-2}$ for all $5 \le M \le 16$. Since $F_M(u)$ increases and $u^{-1} + u^{-2}$ decreases in $u$, $P_{b+1} \le 0$ forces **$u > \frac{33}{50}$**.

2. **Step 2 (Regime $u \in (\frac{33}{50}, \frac{37}{50}]$, all $a \ge 2$):** Set $u_1 := \frac{37}{50}$. Exact rational checks (`verify.py` Section 5) verify:
   - $F_{30, 22}^{\mathrm{ub}}(u_1) < 5 < 2 + u_1^{-1} + u_1^{-2}$ and $F_M(u_1) < 5$ for all $5 \le M \le 29$. Hence $\Delta_P = 1 + S(x) - S_0 < F_M(u_1) - (u_1^{-1} + u_1^{-2}) < 2$ for ALL $M \ge 5$ and ALL $a \ge 2$.
   - $F_5(u_1) < u_1^{-1} + u_1^{-2}$, so $M = 5$ is impossible on $u \le u_1$.
   - Writing $S_r(u, M) := 1 + \sum_{k=1}^r u^{k - k(k+1)/(2M)}$ (decreasing in $M$), exact rational checks verify $S_3(u_1, 5) < u_1^{-1} + u_1^{-2}$ (so **$r^* \ge 4$ for all $M \ge 6$**) and $S_4(u_1, 17) < u_1^{-1} + u_1^{-2}$ (so **$r^* \ge 5$ for all $M \ge 17$**).
   - By Lemma 5.2, for any $a \ge 2$ and fixed $r^*$, $E(S_0, r^*)$ is strictly decreasing in $S_0 \in \bigl(S_{r^*-1}, \min(S_{r^*}, 1 + S(x))\bigr]$, so $E(S_0, r^*) \ge E(S_{r^*}, r^*)$ (with $\Delta_{r^*} = \sum_{k=r^*+1}^{L-1} x^{c_k} \le F_M - S_{r^*}$), and for $r^* \ge 6$, using $S_0 \le 1 + S(x) \le F_M(u)$ gives $E(S_0, r^*) \ge 2\bigl(1 + u + G_6 - r F_M(u)\bigr)$.
   - For **$M \ge 30$** ($r^* \ge 5$): exact rational 1D subdivision on $u \in [\frac{33}{50}, \frac{37}{50}]$ (`verify.py` Section 5) certifies both $E(S_5, 5) > 0$ (using $F_{30, 22}^{\mathrm{ub}}$) and $2(1 + u + G_6 - r F_{30, 22}^{\mathrm{ub}}) > 0$.
   - For **$6 \le M \le 29$**: exact integer dyadic monotone-splitting (`verify.py` Section 5, 84 total Step-2 boxes/leaves) certifies $x E(S_{r^*}, r^*) > 0$ for every feasible $r^* \in \{4, 5\}$ ($r^* = 4$ only for $M \le 16$, pruned by $S_{r^*} \ge u^{-1} + u^{-2}$) and $2x(1 + u + G_6 - r F_M(x)) > 0$ for $r^* \ge 6$ ($M \ge 8$).
   By Lemma 5.2, $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$ holds everywhere on $u \in (\frac{33}{50}, \frac{37}{50}]$.

3. **Step 3 (Regime $u \in [\frac{37}{50}, v)$):** Here we prove $L_0 > T$ (which implies $L_{\mathrm{sw}} > T$).
   - **Subcase $L \ge 12$:** Dropping $\theta T / B_{a+1} > 0$, $(1 - \theta)(L_0 - T)/B_{a+1} > \frac{x(1 - 2v + u)}{1 - x} - (1 + S(x)) > \bigl(\frac{12}{\ln(1/v)} - \frac{1}{2}\bigr)(1 - 2v + u) - \frac{1}{1 - u/\sqrt{v}}$. Exact rational 2D box subdivision on $\frac{37}{50} \le u \le v \le \frac{50}{61}$ (`verify.py` Section 5, 61 boxes) certifies this strictly positive.
   - **Subcase $L \le 11$:** First, $L = 3$ ($M \ge 5$) is impossible: $v \le \frac{50}{61} \implies u = v^{M/3} \le (\frac{50}{61})^{5/3} < \frac{3}{4}$ (as $(\frac{50}{61})^5 < (\frac{3}{4})^3$), giving $u^{-1} + u^{-2} > \frac{4}{3} + \frac{16}{9} = \frac{28}{9} > 3 > 1 + S(x)$. Similarly, $(L = 4, d \ge 2)$ ($M \ge 6$) is impossible: $x \le (\frac{50}{61})^{1/4}$ and $u \le (\frac{50}{61})^{3/2}$ give $1 + x^5 + x^9 + x^{12} < u^{-1} + u^{-2}$ (`verify.py` Section 5). Finally, $u = v^{1 + d/L} \ge \frac{37}{50}$ with $v \le \frac{50}{61}$ forces $d \le \bigl\lfloor(\frac{\ln(50/37)}{\ln(61/50)} - 1) L\bigr\rfloor$, leaving exactly **27** pairs $(L, d)$ with $4 \le L \le 11$. For every one of these 27 pairs, exact integer dyadic monotone-splitting (`verify.py` Section 5, 43 leaves) certifies $x^M(1 - \theta)(L_0 - T)/B_{a+1} > 0$. $\blacksquare$

---

### 5.5 Theorem 5.3 (Lemma B2 — $a = 1$, $r^* = 1$, $r^L \ge \frac{61}{50}$, $M \ge 6$)

**Theorem 5.3.** For all $n \ge 8$, $a = 1$, $M \ge 6$, $P_{b+1} \le 0$, $r^* = 1$ (equivalently $u^{-1} \le 1 + x^{M-1}$), and $r^L \ge \frac{61}{50}$, we have $(L_{\mathrm{sw}} > U_{\mathrm{sw}}) \lor (L_{\mathrm{sw}} > T)$.

*Proof.* First, $u^{-1} \le 1 + x^{M-1} = 1 + u^{1 - 1/M} \le 1 + u^{5/6}$ (since $M \ge 6$), and exact rational check (`verify.py` Section 6a) gives $\frac{1000}{603} > 1 + (\frac{603}{1000})^{5/6}$, forcing **$u > \frac{603}{1000}$**. Hence $L = 2$ is impossible ($r^2 \ge \frac{61}{50} \implies u \le (\frac{50}{61})^3 < \frac{603}{1000}$), so $L \ge 3$. Also $-P_{b+1}/A_2 = (1 + x^{M-1} - u^{-1}) + S_2(x) \ge S_2(x) := \sum_{k=2}^{L-1} x^{c_k}$. Split at $r^L = \frac{133}{100}$ ($v = \frac{100}{133}$):

1. **Part B2(a): $r^L \in \bigl[\frac{61}{50}, \frac{133}{100}\bigr]$ ($v \in \bigl[\frac{100}{133}, \frac{50}{61}\bigr]$).** We prove $L_{\mathrm{sw}} > U_{\mathrm{sw}}$. From Lemma 2.2 and Proposition 5.0(3),
   $$\frac{(1 - \theta)(1 - \theta v)}{B_2}(L_{\mathrm{sw}} - U_{\mathrm{sw}}) \ge \theta(1 - v) H_{L,d}(x) + (1 - \theta) W_0 + \sum_{k=2}^{L-1}\bigl(\mathrm{coef}_P - (1 - \theta)(1 - x^{k-1})\bigr) x^{c_k},$$
   where $\mathrm{coef}_P := (1 - v)\bigl[(1 - \theta v) - x^{M-1}(1 - \theta)\bigr]$. Since $M - 1 = L + d - 1 \ge L$, we have $x^{M-1} \le v$, so $(1 - \theta v) - x^{M-1}(1 - \theta) \ge (1 - \theta v) - v(1 - \theta) = 1 - v$, giving $\mathrm{coef}_P \ge (1 - v)^2$ and
   $$u_* := \frac{\mathrm{coef}_P}{(1 - \theta) y} \ge \frac{(1 - v)^2}{(1 - \theta) y} > \frac{(1 - e^{-y})^2}{y}.$$
   Since $\frac{d}{dy}\frac{(1 - e^{-y})^2}{y} = \frac{(1 - e^{-y})e^{-y}}{y^2}(1 + 2y - e^y) > 0$ on $(0, 1]$, we have $u_* > \frac{(11/61)^2}{\ln(61/50)} > \frac{163}{1000}$ (`verify.py` Section 2).
   - **Subcase $\Lambda_1 \ge 17$:** Since $x \ge v^{1/3} \ge (100/133)^{1/3} > 0.909 > 7/10$, Theorem 4.1(5) gives $H_{L,d}(x) > 0$. Dropping all nonnegative terms ($k - 1 \le u_* L$) in the sum divided by $(1 - \theta)$, and bounding the negative tail ($k - 1 > u_* L$) via $1 - x^{k-1} \le \frac{k-1}{L} y$, $L y = 2 s \Lambda_1$, and $f(u) \ge u$:
     $$\sum_{k-1 > u_* L} \left((1 - x^{k-1}) - \frac{\mathrm{coef}_P}{1 - \theta}\right) x^{c_k} \le y L \int_{u_*}^{(L-1)/L} (u - u_*) e^{-\Lambda_1 f(u)}\,du < 2 \Lambda_1 \int_{u_*}^\infty (u - u_*) e^{-\Lambda_1 u}\,du = \frac{2}{\Lambda_1} e^{-\Lambda_1 u_*}.$$
     Exact rational verification (`verify.py` Section 2) confirms $\frac{2}{17} e^{-17 \cdot 163/1000} < \frac{1}{133} - e^{-17} \le 4v - 3 - \theta < W_0$. Hence $L_{\mathrm{sw}} > U_{\mathrm{sw}}$.
   - **Subcase $\Lambda_1 \in [1, 17]$, $L \ge 11$:** Note $u = v^{1+d/L} > \frac{603}{1000}$ and $v \le \frac{50}{61}$ force $d/L < \frac{\ln(1000/603)}{\ln(61/50)} - 1 < 1.545$, hence $s = \frac{L}{2d+L-1} > \frac{1}{1 + 2(1.545)} > \frac{1}{5}$ and $\Lambda_1 = (d + \frac{L-1}{2}) y \ge 6 \ln\frac{61}{50} > 1$ (`verify.py` Section 6b). Furthermore, we have the exact identities
     $$M t = \frac{1 + s}{2 s} y + \frac{y^2}{4 s \Lambda_1}, \qquad (M - 1) t = \left(\frac{1 + s}{2 s} - \frac{1}{2 L}\right) y, \qquad r - 1 = e^t - 1 > t = \frac{y^2}{2 s \Lambda_1}.$$
     Splitting the $k$-sum at $u_*$:
     - The positive terms ($2 \le k \le \lfloor u_* L \rfloor$) are bounded below by $L(1 - \theta) y \int_{\min(2/L, u_*)}^{u_*} (u_* - u) e^{-\Lambda_1 f_{\mathrm{tan}, 4}(u)}\,du$ (taken as $0$ whenever $u_* \le 2/L$);
     - The negative tail ($k - 1 > u_* L$) is bounded above by $(1 - \theta) \cdot 2 s \Lambda_1 \int_{u_*}^1 (u - u_*) e^{-\Lambda_1 f_4(u)}\,du$;
     - $\theta(1 - v) H_{L,d} \ge 2 s \Lambda_1 \theta \phi_1(y)(\phi_1(y) - I_0^{(4)}) - \theta(1 - v)\frac{3 - v - e^{-\Lambda_1/11} - \theta}{2}$.
     Exact rational 3D box subdivision (`verify.py` Section 6b, pruning infeasible $2 s \Lambda_1 < 11 y$ and $M t \ge \ln(1000/603)$) certifies the combined lower bound strictly positive on $[1, 17] \times [\frac{1}{5}, 1] \times [\ln\frac{61}{50}, \ln\frac{133}{100}]$.
   - **Subcase $3 \le L \le 10$:** The bound $d \le \lfloor (\frac{\ln(1000/603)}{\ln(61/50)} - 1) L \rfloor$ with $L + d \ge 6$ yields **73** pairs $(L, d)$ (`verify.py` Section 6b, 1,175 dyadic leaves), each certified for $L_{\mathrm{sw}} > U_{\mathrm{sw}}$ on the feasible $r^* = 1$ window in $r^L \in [\frac{61}{50}, \frac{133}{100}]$ by exact integer dyadic monotone-splitting.

2. **Part B2(b): $r^L \ge \frac{133}{100}$ ($v \le \frac{100}{133}$).** Since $u^{-1} \le 1 + r u$,
   $$\frac{(1 - \theta)(L_{\mathrm{sw}} - T)}{B_2} \ge \frac{x(1 - 2v + u)}{1 - x} + \theta \frac{x(v - u)}{1 - x} - \frac{v}{1 - u/\sqrt{v}} - (1 - v)(1 + r u).$$
   - **Subcase $L \ge 9$:** Dropping the $\theta$ term and using $\frac{x}{1-x} > \frac{9}{\ln(1/v)} - \frac{1}{2}$ and $r = v^{-1/L} \le v^{-1/9}$, exact rational 2D box subdivision (`verify.py` Section 6c, 23 boxes) certifies the RHS strictly positive on all $\frac{603}{1000} \le u \le v \le \frac{100}{133}$ satisfying $u^{-1} \le 1 + v^{-1/9} u$.
   - **Subcase $L \le 8$:** For $L = 3$ ($M \ge 6$), $u \le (\frac{100}{133})^2 < \frac{603}{1000}$ (impossible). For $4 \le L \le 8$, $d \le \lfloor(\frac{\ln(1000/603)}{\ln(133/100)} - 1) L\rfloor$ leaves exactly **20** pairs $(L, d)$. Exact integer dyadic monotone-splitting (`verify.py` Section 6c, 48 leaves) certifies $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > U_{\mathrm{sw}})$ on every feasible point of all 20 pairs. $\blacksquare$

---

### 5.6 Theorem 5.4 (Lemma C — $a = 1$, $r^* \ge 2$, $r^L \ge \frac{61}{50}$, $M \ge 6$)

**Theorem 5.4.** For all $n \ge 8$, $a = 1$, $M \ge 6$, $P_{b+1} \le 0$, $r^* \ge 2$ (equivalently $u^{-1} > 1 + x^{M-1}$), and $r^L \ge \frac{61}{50}$, we have $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$.

*Proof.* Since $r^* \le L - 1$, $r^* \ge 2 \implies L \ge 3$. Also $u^{-1} > 1 + x^{M-1} = 1 + r u > 1 + u$ forces $u^2 + u < 1$, so $u < \phi^{-1} = \frac{\sqrt{5}-1}{2} < \frac{62}{100}$ (verified by $5 \cdot 100^2 < 224^2$). Combined with Proposition 5.0(2), $u \in \bigl(\frac{38}{100}, \frac{62}{100}\bigr)$.

1. **Verification of $\Delta_P < 2$ for all $M \ge 6$:** Here $S_0 = u^{-1}$ and $\Delta_P = 1 + S(x) - u^{-1} \le F_M(u) - u^{-1}$, which is strictly increasing in $u$! Exact rational checks (`verify.py` Section 7a) verify $F_{26, 24}^{\mathrm{ub}}(\frac{62}{100}) - \frac{100}{62} < 2$ (covering all $M \ge 26$) and $F_M(u_b) - u_a^{-1} < 2$ on 8 subintervals of $[\frac{38}{100}, \frac{62}{100}]$ for every $6 \le M \le 25$. Thus Lemma 5.2 applies unconditionally.

2. **Case $r^* \ge 3$ (all $M \ge 6$):** Here $G_{r^*} \ge x + x^2$. Exact rational 1D subdivision (`verify.py` Section 7b, 55 boxes) certifies $E(u^{-1}, r^*) > 0$ via $F_{26, 24}^{\mathrm{ub}}$ for all $M \ge 26$ and via exact $F_M$ for all $6 \le M \le 25$ (pruning infeasible regions where $u^{-1} > F_M$ or $u^{-1} \le 1 + x^{M-1} + x^{2M-3}$). By Lemma 5.2, $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$ holds.

3. **Case $r^* = 2$, $M \ge 35$:** Since $r^* = 2$, $u^{-1} \le 1 + x^{M-1} + x^{2M-3} = 1 + u^{1 - 1/M} + u^{2 - 3/M} \le 1 + u^{34/35} + u^{67/35}$, and exact rational check verifies $\frac{100}{51} > 1 + (\frac{51}{100})^{34/35} + (\frac{51}{100})^{67/35}$, forcing **$u > \frac{51}{100}$**. For $r^* = 2$, $G_2 = x$, so $(r - 1) G_2 = 1 - x$ gives $1 + u - (r - 1)x = u + x$ identically, and
   $$E(u^{-1}, 2) = 2(1 + u) + (2 - \Delta_P) x - 2 r u^{-1} - \Delta_P u.$$
   Since $2 - \Delta_P > 0$ and $r = 1/x$, $E(u^{-1}, 2)$ is strictly increasing in $x$ and strictly decreasing in $\Delta_P$. Replacing $x$ by $x_{\mathrm{lb}} = u_a^{1/35}$ and $\Delta_P$ by $\Delta_{P,\mathrm{ub}} = F_{35, 26}^{\mathrm{ub}}(u_b) - u_b^{-1}$ on subintervals $[u_a, u_b] \subset [\frac{51}{100}, \frac{62}{100}]$ (pruning $u_a^{-1} \le 1 + u_a$), exact rational 1D subdivision (`verify.py` Section 7c, 13 boxes) certifies $E(u^{-1}, 2) > 0$. By Lemma 5.2, $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$ holds.

4. **Case $r^* = 2$, $6 \le M \le 34$:** Since $M \ge 6$, $u^{-1} \le 1 + u^{5/6} + u^{3/2}$ forces **$u > \frac{1}{2}$** (verified in `verify.py` Section 7a: $1 + (\frac{1}{2})^{5/6} + (\frac{1}{2})^{3/2} < 2$). There are $\sum_{M=6}^{34}(M - 3) = 493$ pairs $(L, d)$ with $3 \le L \le M - 1$. For every one of these 493 pairs, exact integer dyadic monotone-splitting (`verify.py` Section 7d, 1,420 leaves) certifies that on every feasible point ($r^L \ge \frac{61}{50}$ and $1 + x^{M-1} < u^{-1} \le 1 + x^{M-1} + x^{2M-3}$), either $x^M(1 - \theta)(L_{\mathrm{sw}} - T)/B_2 > 0$ or $x^M(1 - \theta)(L_{\mathrm{sw}} - \mathrm{hi}_p)/B_2 > 0$. $\blacksquare$

---

## 6. Proof of the Main Theorem & Verification Summary

*Proof of Main Theorem.* Let $n \ge 7$ and $r > 1$, and let $\sigma$ be any non-isolated cut of $K_n$.
- If $2a \ge n - 1$, $\sigma$ is strictly improved by $\mathrm{flip}(b+1)$ (Lemma 3.1).
- If $b + 1 = n$, $\sigma$ is strictly improved by $\mathrm{flip}(n)$ or $\mathrm{swap}(a+1, n)$ (Lemma 3.2).
- If $L = 1$, $\sigma$ is strictly improved (Lemma 3.3).
- Otherwise $(n, a, b)$ is an interior triple ($1 \le a \le (n-2)/2, L \ge 2, d \ge 1$).
  - If $P_{b+1} > 0$, $\sigma$ is strictly improved by $\mathrm{flip}(b+1)$ or $\mathrm{swap}(a+1, b+1)$ (Theorem 4.1).
  - If $P_{b+1} \le 0$ and $n = 7$, $\sigma$ is strictly improved by Theorem 4.2.
  - If $P_{b+1} \le 0$ and $n \ge 8$:
    - If $r^L \le \frac{61}{50}$, then $L_{\mathrm{sw}} > U_{\mathrm{sw}}$ (Theorem 5.1), so $\mathrm{swap}(a+1, b+1)$ or $\mathrm{swap}(a, b)$ strictly improves $\sigma$.
    - If $r^L > \frac{61}{50}$ and $a \ge 2$, then $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$ (Theorem 5.2), so $\mathrm{swap}(a+1, b+1)$ or $\mathrm{flip}[1..k^*]$ strictly improves $\sigma$.
    - If $r^L > \frac{61}{50}$, $a = 1$, and $r^* = 1$, then $(L_{\mathrm{sw}} > U_{\mathrm{sw}}) \lor (L_{\mathrm{sw}} > T)$ (Theorem 5.3), so $\mathrm{swap}(2, b+1)$ or $\mathrm{swap}(1, b)$ strictly improves $\sigma$.
    - If $r^L > \frac{61}{50}$, $a = 1$, and $r^* \ge 2$, then $(L_{\mathrm{sw}} > T) \lor (L_{\mathrm{sw}} > \mathrm{hi}_p)$ (Theorem 5.4), so $\mathrm{swap}(2, b+1)$ or $\mathrm{flip}[1..k^*]$ strictly improves $\sigma$.

In every case no non-isolated cut is a global maximizer. Combined with the reduction in Section 1 and Marić's Theorem 4.10, Conjecture 5.1 is proved for all $n \ge 7$. $\blacksquare$

### Exact-Arithmetic Verification (`verify.py`)

Command: `.venv/bin/python targets/maric-2603.08876-conj1/verify.py` (strictly zero floating-point operations: uses only Python `int`, `fractions.Fraction`, and `sympy` exact `Rational`/`Poly` Sturm chains; exits 0 and prints `PASS`).

- **Stage 1:** Exact symbolic verification of $w(i, j) = A_i B_j$, Lemma 2.1, Lemma 2.2, Proposition 5.0(3) ($\mathcal{N}$-decomposition), the exponent identity $(c_k - k - 1) - (k-1)D_1 = d + \frac{k(L-k-2)+L-3}{2} \ge d - 1$, plus exhaustive verification of Conjecture 5.1 over all $2^{n-1}$ cuts for $n = 7, 8$ at rational $r$.
- **Stage 2:** Exact rational verification of all boundary/analytic constants (Lemma 3.2, Theorem 4.1, Theorem 5.1 Cases A1 and A2-small, and Theorem 5.3 B2(a) for $\Lambda_1 \ge 17$).
- **Stage 3:** Exact `sympy` Sturm-chain certification of all 5 interior triples of $n = 7$ across $(0, 1)$, including $\Delta W(\mathrm{flip}\{1, 3, 4\}) > 0$ on $[\frac{231}{256}, \frac{467}{512}]$ for $(7, 1, 4)$.
- **Stage 4 (Theorem 5.1 / A2):** Exact rational 2D box certification for $L \ge 12$ (with analytic $y$-monotonicity, 1,193 boxes) and centered-form 2D polynomial certification for $3 \le L \le 11$ (1,182 boxes).
- **Stage 5 (Theorem 5.2 / B1):** Exact rational certification of $u > \frac{33}{50}$, Step 2 ($M \ge 30$ + $6 \le M \le 29$, 84 boxes/leaves), and Step 3 ($L \ge 12$, 61 2D boxes; $4 \le L \le 11$, 27 pairs, 43 dyadic leaves).
- **Stage 6 (Theorem 5.3 / B2):** Exact rational certification of $u > \frac{603}{1000}$, B2(a) ($L \ge 11$, 2,337 3D boxes; $3 \le L \le 10$, 73 pairs, 1,175 dyadic leaves), and B2(b) ($L \ge 9$, 23 2D boxes; $4 \le L \le 8$, 20 pairs, 48 dyadic leaves).
- **Stage 7 (Theorem 5.4 / C):** Exact rational certification of $\Delta_P < 2$, $r^* \ge 3$ (55 boxes), $r^* = 2, M \ge 35$ (13 boxes), and $r^* = 2, 6 \le M \le 34$ (493 pairs, 1,420 dyadic leaves).

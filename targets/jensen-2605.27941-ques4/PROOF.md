# Proof: Complete Resolution of Question 4 (`jensen-2605.27941-ques4`)

## Statement
We completely resolve **Question 4** of Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, `arXiv:2605.27941v1` (`main.tex`, Section 5, lines 1158–1163) for every integer $k \ge 1$:

> **Theorem.**
> 1. For $k \in \{1, 2\}$, the answer is **YES**: $\mathsf{MLPS}_1 = (0, 1/2]$ is determined by the single speed tuple $(1)$, and $\mathsf{MLPS}_2 = \{(d_1, d_2) \in (0, 1/2]^2 : 2d_1 + d_2 \le 1,\; d_1 + 2d_2 \le 1\}$ is determined by the two ordered speed pairs $(1, 2)$ and $(2, 1)$ (equivalently, by the single unordered speed set $\{1, 2\}$).
> 2. For every integer $k \ge 3$, the answer is **NO**: $\mathsf{MLPS}_k$ is **not** determined by finitely many speed sets (whether "speed sets" refers to a finite family of ordered $k$-tuples of distinct positive integers or a finite family of unordered $k$-element subsets of $\mathbb{Z}_{>0}$).

---

## 1. Affirmative Cases ($k = 1$ and $k = 2$)
For any subset $\mathcal{S}$ of ordered $k$-tuples of distinct positive integers, write
$$U(\mathcal{S}) := \bigl\{\mathbf{d} \in (0, 1/2]^k : \forall \mathbf{s} = (s_1, \dots, s_k) \in \mathcal{S},\; \exists t \in \mathbb{R} \text{ such that } \|s_i t\| \ge d_i \;\forall i = 1, \dots, k\bigr\}.$$
Note that if $\mathcal{A}$ is a finite family of unordered $k$-element sets of positive integers, imposing $\mathsf{MLRC}(\mathbf{d})$ on every ordering of every $A \in \mathcal{A}$ equals $U(\mathcal{S}_{\mathcal{A}})$, where $\mathcal{S}_{\mathcal{A}} := \{(s_1, \dots, s_k) : \{s_1, \dots, s_k\} \in \mathcal{A}\}$ has finite cardinality $|\mathcal{S}_{\mathcal{A}}| = k! \cdot |\mathcal{A}|$.

- **Case $k = 1$:** For every $d_1 \in (0, 1/2]$ and every $s_1 \in \mathbb{Z}_{>0}$, taking $t = \frac{1}{2s_1}$ gives $\|s_1 t\| = \|1/2\| = \frac{1}{2} \ge d_1$. Thus $\mathsf{MLPS}_1 = (0, 1/2] = U(\{(1)\})$.
- **Case $k = 2$:** By Theorem A of Jensen (`arXiv:2605.27941v1`, Section 4, `main.tex` lines 877–1056), $\mathsf{MLPS}_2 = \{(d_1, d_2) \in (0, 1/2]^2 : 2d_1 + d_2 \le 1 \text{ and } d_1 + 2d_2 \le 1\}$. Let $\mathcal{S}_2 = \{(1, 2), (2, 1)\}$. Clearly $\mathsf{MLPS}_2 \subseteq U(\mathcal{S}_2)$. Conversely, for $(d_1, d_2) \in (0, 1/2]^2$:
  - Taking $\mathbf{s} = (1, 2)$ on $[0, 1)$, $\|t\| \ge d_1 \iff t \in [d_1, 1 - d_1]$ and $\|2t\| \ge d_2 \iff t \in [\frac{d_2}{2}, \frac{1 - d_2}{2}] \cup [\frac{1 + d_2}{2}, 1 - \frac{d_2}{2}]$. Since $d_1, d_2 \le \frac{1}{2}$, these intervals intersect iff $d_1 \le \frac{1 - d_2}{2} \iff 2d_1 + d_2 \le 1$.
  - Taking $\mathbf{s} = (2, 1)$ gives $d_1 + 2d_2 \le 1$ by symmetry.
  Hence $U(\{(1, 2), (2, 1)\}) = \{(d_1, d_2) \in (0, 1/2]^2 : 2d_1 + d_2 \le 1 \text{ and } d_1 + 2d_2 \le 1\} = \mathsf{MLPS}_2$.

---

## 2. Finite Speed Sets Always Produce a Finite Union of Convex Sets

### Lemma 0 (Piecewise-Affine Convexity)
For every $k \ge 1$ and every finite collection $\mathcal{S}$ of ordered $k$-tuples of distinct positive integers, $U(\mathcal{S}) \subseteq (0, 1/2]^k$ is a finite union of convex sets.

**Proof.** Fix a single speed tuple $\mathbf{s} = (s_1, \dots, s_k) \in \mathcal{S}$. By $1$-periodicity of $t \mapsto \|s_i t\|$, we have $\mathbf{d} \in U(\{\mathbf{s}\})$ if and only if there exists $t \in [0, 1]$ with $\|s_i t\| \ge d_i$ for all $i = 1, \dots, k$.

Let
$$B_{\mathbf{s}} := \left\{\frac{j}{2s_i} : 1 \le i \le k,\; 0 \le j \le 2s_i\right\} \subset [0, 1]$$
be the finite set of half-integer breakpoints, written in strictly increasing order as $0 = b_0 < b_1 < \dots < b_{M_{\mathbf{s}}} = 1$. On each closed subinterval $I_{\mathbf{s}, r} := [b_{r-1}, b_r]$ ($1 \le r \le M_{\mathbf{s}}$), for every $i \in \{1, \dots, k\}$ the open interval $(b_{r-1}, b_r)$ contains no point of $\frac{1}{2s_i}\mathbb{Z}$, so there exists an integer $j$ with $s_i t \in \bigl[\frac{j}{2}, \frac{j+1}{2}\bigr]$ for all $t \in I_{\mathbf{s}, r}$. Consequently, the map $t \mapsto \|s_i t\|$ is **affine** on $I_{\mathbf{s}, r}$: it equals $s_i t - m$ if $j = 2m$ is even, and $(m + 1) - s_i t$ if $j = 2m + 1$ is odd.

For each $r \in \{1, \dots, M_{\mathbf{s}}\}$, define
$$C_{\mathbf{s}, r} := \bigl\{\mathbf{d} \in (0, 1/2]^k : \exists t \in I_{\mathbf{s}, r} \text{ such that } \|s_i t\| \ge d_i \;\forall i = 1, \dots, k\bigr\}.$$
We verify that $C_{\mathbf{s}, r}$ is convex. If $\mathbf{d}, \mathbf{d}' \in C_{\mathbf{s}, r}$ are witnessed by $t, t' \in I_{\mathbf{s}, r}$ respectively and $\lambda \in [0, 1]$, then $t_\lambda := (1 - \lambda)t + \lambda t' \in I_{\mathbf{s}, r}$, and by affinity of $t \mapsto \|s_i t\|$ on $I_{\mathbf{s}, r}$,
$$\|s_i t_\lambda\| = (1 - \lambda)\|s_i t\| + \lambda \|s_i t'\| \ge (1 - \lambda)d_i + \lambda d'_i \qquad \text{for every } i = 1, \dots, k.$$
Moreover, $(1 - \lambda)\mathbf{d} + \lambda\mathbf{d}' \in (0, 1/2]^k$, so $(1 - \lambda)\mathbf{d} + \lambda\mathbf{d}' \in C_{\mathbf{s}, r}$.

Since $[0, 1] = \bigcup_{r=1}^{M_{\mathbf{s}}} I_{\mathbf{s}, r}$, we have $U(\{\mathbf{s}\}) = \bigcup_{r=1}^{M_{\mathbf{s}}} C_{\mathbf{s}, r}$. Taking the finite intersection over $\mathbf{s} \in \mathcal{S}$ and distributing intersection over finite unions yields
$$U(\mathcal{S}) = \bigcap_{\mathbf{s} \in \mathcal{S}} \bigcup_{r=1}^{M_{\mathbf{s}}} C_{\mathbf{s}, r} = \bigcup_{\phi \in \prod_{\mathbf{s} \in \mathcal{S}} \{1, \dots, M_{\mathbf{s}}\}} \left(\bigcap_{\mathbf{s} \in \mathcal{S}} C_{\mathbf{s}, \phi(\mathbf{s})}\right).$$
Because each intersection $\bigcap_{\mathbf{s} \in \mathcal{S}} C_{\mathbf{s}, \phi(\mathbf{s})}$ of convex sets is convex and $\prod_{\mathbf{s} \in \mathcal{S}} \{1, \dots, M_{\mathbf{s}}\}$ is finite, $U(\mathcal{S})$ is a finite union of convex sets. $\blacksquare$

---

## 3. For Every $k \ge 3$, $\mathsf{MLPS}_k$ Is Not a Finite Union of Convex Sets

To deduce a negative answer for Question 4 when $k \ge 3$, it suffices (by Lemma 0) to prove that $\mathsf{MLPS}_k$ is not a finite union of convex sets. We give the complete self-contained proof.

### 3.1 Explicit Construction
For every integer $n \ge 5$, define the exact rational quantities:
$$d_n := \frac{1}{2n+3}, \qquad \delta_n := \frac{1}{20(2n+3)^2}, \qquad x_n := d_n - \delta_n = \frac{20(2n+3)-1}{20(2n+3)^2},$$
$$\eta_n := \frac{2n+5}{4(n+1)(2n+3)}, \qquad y_n := \frac{1}{2} - \eta_n, \qquad \mu_n := \frac{3}{22}\delta_n^2 \eta_n.$$
For each integer $k \ge 3$, define $\varepsilon_{n,k} := \frac{\mu_n}{2k}$ and the vector
$$Q_n^{(k)} := \bigl(x_n,\; x_n,\; y_n,\; \underbrace{\varepsilon_{n,k}, \dots, \varepsilon_{n,k}}_{k-3}\bigr) \in (0, 1/2)^k.$$
(When $k = 3$, $Q_n^{(3)} = (x_n, x_n, y_n)$.)

For all $n \ge 5$:
- $0 < x_n < d_n \le \frac{1}{13}$;
- $0 < \varepsilon_{n,k} < \mu_n < \eta_n < \frac{1}{12}$, so $y_n \in (\frac{5}{12}, \frac{1}{2})$;
- $x_n$ is strictly decreasing in $n$:
  $$x_n - x_{n+1} = \frac{2}{(2n+3)(2n+5)}\left(1 - \frac{4n+8}{20(2n+3)(2n+5)}\right) > 0;$$
- $\eta_n = \frac{1}{2(2n+3)} + \frac{3}{4(n+1)(2n+3)}$ is strictly decreasing in $n$, so $y_n$ is strictly increasing in $n$.

### 3.2 Segment Obstruction (Lemmas 1 and 2)

#### Lemma 1 (Speed-tuple obstruction)
Let $n \ge 5$ and $k \ge 3$. Suppose $\mathbf{d} = (d_1, \dots, d_k) \in (0, 1/2]^k$ has $d_1 = d_2 = x$ and $d_3 = y$ satisfying
$$\frac{1}{2n+3} < x < \frac{1}{2n-1} \qquad\text{and}\qquad y > \frac{n - x}{2n+1}.$$
Then $\mathbf{d} \notin \mathsf{MLPS}_k$.

**Proof.** Choose $k$ distinct positive integer speeds $(s_1, \dots, s_k)$ with $s_1 = 2$, $s_2 = 2n+1$, $s_3 = 1$, and $s_4, \dots, s_k \in \mathbb{Z}_{>0} \setminus \{1, 2, 2n+1\}$ arbitrary distinct integers. Suppose for contradiction that there exists $t \in \mathbb{R}$ with $\|s_i t\| \ge d_i$ for all $i$. By $1$-periodicity and evenness $\|s(-t)\| = \|st\|$, we may assume $t \in [0, 1/2]$.

Since $n \ge 5$ and $x < \frac{1}{2n-1} \le \frac{1}{9}$, we have $y > \frac{n - x}{2n+1} > \frac{5 - 1/9}{11} > \frac{1}{3}$. On $[0, 1/2]$, $\|t\| = t \ge y$, so writing $t = \frac{1}{2} - u$ gives $0 \le u \le \frac{1}{2} - y < \frac{1}{6}$, whence $\|2t\| = \|1 - 2u\| = 2u \ge x$ forces $u \ge \frac{x}{2}$. Meanwhile, $\|(2n+1)t\| = \|\frac{1}{2} - (2n+1)u\|$. Since $(2n+3)x > 1$ and $(2n-1)x < 1$, we have
$$\frac{1}{2} - x < (2n+1)\frac{x}{2} < \frac{1}{2} + x.$$
Since $x < \frac{1}{9} < \frac{1}{2}$, any $u$ with $\frac{1}{2} - x < (2n+1)u < \frac{1}{2} + x$ has $\|\frac{1}{2} - (2n+1)u\| < x$. Combined with $u \ge \frac{x}{2}$ and $\|(2n+1)t\| \ge x$, this forces $(2n+1)u \ge \frac{1}{2} + x$, i.e., $u \ge \frac{1+2x}{2(2n+1)} = \frac{1}{2} - \frac{n-x}{2n+1}$, giving $y \le t = \frac{1}{2} - u \le \frac{n-x}{2n+1}$, contradiction. $\blacksquare$

#### Lemma 2 (Every segment $(Q_n^{(k)}, Q_m^{(k)})$ exits $\mathsf{MLPS}_k$)
Let $k \ge 3$ and let $5 \le m < n$. Set
$$x^* := \frac{1}{2n+3} + \delta_n = x_n + 2\delta_n, \qquad \lambda := \frac{x^* - x_n}{x_m - x_n} = \frac{2\delta_n}{x_m - x_n}.$$
Then $\lambda \in (0, 1)$ and $P := (1 - \lambda) Q_n^{(k)} + \lambda Q_m^{(k)} \notin \mathsf{MLPS}_k$.

**Proof.** Since $x_m \ge x_{n-1} = \frac{1}{2n+1} - \frac{1}{20(2n+1)^2}$, we have $x_{n-1} - x^* > \frac{2}{(2n+1)(2n+3)} - \frac{1}{10(2n+1)^2} > 0$, so $x_n < x^* < x_m$ and $\lambda \in (0, 1)$. Also $\frac{1}{2n-1} - x^* = \frac{4}{(2n-1)(2n+3)} - \frac{1}{20(2n+3)^2} > 0$, so $\frac{1}{2n+3} < x^* < \frac{1}{2n-1}$.

The first three coordinates of $P$ are $(x^*, x^*, y^*)$ where $y^* = y_n - \lambda(y_n - y_m)$. For $5 \le m < n$:
- Writing $x_m - x_n = \frac{2(n-m)}{(2m+3)(2n+3)}\left(1 - \frac{2m+2n+6}{20(2m+3)(2n+3)}\right)$ with $2m+2n+6 < 2(2n+3)$ and $2m+3 \ge 13$ gives
  $$x_m - x_n > \frac{129}{130} \cdot \frac{2(n-m)}{(2m+3)(2n+3)}.$$
- Using $\eta_t = \frac{1}{2(2t+3)} + \frac{3}{4(t+1)(2t+3)}$, we have
  $$y_n - y_m = \eta_m - \eta_n = \frac{n-m}{(2m+3)(2n+3)} + \frac{3}{4}\cdot\frac{(n-m)(2m+2n+5)}{(m+1)(2m+3)(n+1)(2n+3)}.$$
  Since $m+1 \ge 6$ and $n+1 \ge 7$, $\frac{2m+2n+5}{(m+1)(n+1)} = \frac{2}{n+1} + \frac{2}{m+1} + \frac{1}{(m+1)(n+1)} \le \frac{2}{7} + \frac{2}{6} + \frac{1}{42} = \frac{9}{14} < \frac{2}{3}$, so the second term is at most $\frac{27}{56}\cdot\frac{n-m}{(2m+3)(2n+3)} < \frac{1}{2}\cdot\frac{n-m}{(2m+3)(2n+3)}$. Thus
  $$y_n - y_m < \frac{3}{2}\cdot\frac{n-m}{(2m+3)(2n+3)}.$$
Dividing gives $0 < \frac{y_n - y_m}{x_m - x_n} < \frac{3}{4} \cdot \frac{130}{129} < 1$, so $y^* > y_n - 2\delta_n$.

Since $x^* > \frac{1}{2n+3}$, we have $1 + 2x^* > \frac{2n+5}{2n+3}$, so $\frac{n - x^*}{2n+1} = \frac{1}{2} - \frac{1+2x^*}{2(2n+1)} < \frac{1}{2} - \frac{2n+5}{2(2n+1)(2n+3)}$. Subtracting yields
$$y^* - \frac{n - x^*}{2n+1} > \frac{2n+5}{4(n+1)(2n+1)(2n+3)} - \frac{1}{10(2n+3)^2} = \frac{16n^2 + 74n + 73}{20(n+1)(2n+1)(2n+3)^2} > 0.$$
Hence Lemma 1 gives $P \notin \mathsf{MLPS}_k$. $\blacksquare$

### 3.3 Membership $Q_n^{(k)} \in \mathsf{MLPS}_k$ (Lemmas 3 and 4)
Let $\mu$ denote Lebesgue measure on $[0, 1)$, and for any triple of distinct positive integers $(s_1, s_2, s_3)$ set
$$S_{123}(s_1, s_2, s_3) := \bigl\{t \in [0, 1) : \|s_1 t\| \ge x_n,\; \|s_2 t\| \ge x_n,\; \|s_3 t\| \ge y_n\bigr\}.$$

#### Lemma 3a (Elementary Bad-Measure Bound)
For any closed interval $J \subseteq [0, 1)$ of length $L > 0$, any positive integer $s$, any $\theta \in \mathbb{R}$, and any $x \in (0, 1/2)$,
$$\mu\bigl(\{t \in J : \|st + \theta\| < x\}\bigr) \le 2xL + \frac{2x}{s}.$$

**Proof.** The set $\{t \in \mathbb{R} : \|st + \theta\| < x\}$ is $\frac{1}{s}$-periodic and on each period $\left[\frac{m-\theta}{s}, \frac{m+1-\theta}{s}\right)$ ($m \in \mathbb{Z}$) has measure $\frac{2x}{s}$. Partition $J$ into $\lfloor sL \rfloor$ subintervals of length $\frac{1}{s}$ plus one remainder subinterval of length $< \frac{1}{s}$. Each subinterval of length $\frac{1}{s}$ contributes bad measure $\frac{2x}{s}$, and the remainder contributes at most $\frac{2x}{s}$, giving total bad measure at most $(\lfloor sL \rfloor + 1)\cdot\frac{2x}{s} \le 2xL + \frac{2x}{s}$. $\blacksquare$

#### Lemma 3b (Midpoint Counting Lemma)
Fix $n \ge 5$, $s_3 \ge 1$, $t_k := \frac{2k+1}{2s_3}$ ($0 \le k \le s_3 - 1$), and $s \in \mathbb{Z}_{>0}$. Let $q := \frac{2s_3}{\gcd(s, 2s_3)}$.
1. If $q \ge 2$ (i.e., $2s_3 \nmid s$), then at least $\frac{2}{3} s_3$ indices $k \in \{0, \dots, s_3 - 1\}$ satisfy $\|s t_k\| \ge d_n$.
2. If $q \ge 3$, then for any $\theta \in \mathbb{R}$, at least $\frac{1}{2} s_3$ indices $k \in \{0, \dots, s_3 - 1\}$ satisfy $\|s t_k + \theta\| \ge d_n$.

**Proof.** Put $g_0 := \gcd(s, 2s_3)$, write $s = a g_0$ and $2s_3 = q g_0$ with $\gcd(a, q) = 1$, and write $s_3 = 2^\alpha u_0$, $g_0 = 2^\beta v_0$ with $u_0, v_0$ odd. As $k$ runs over $\mathbb{Z}/s_3\mathbb{Z}$, $s t_k = \frac{a(2k+1)}{q} \pmod 1$.
- **Case $q = 2$ ($\beta = \alpha$, $u_0 = v_0$, $a$ odd):** Here $s_3 = g_0$, so $s$ is an odd multiple of $s_3$, giving $s t_k \equiv \frac{2k+1}{2} \equiv \frac{1}{2} \pmod 1$ and $\|s t_k\| = \frac{1}{2} \ge d_n$ for all $s_3 \ge \frac{2}{3} s_3$ indices $k$.
- **Case $q$ odd ($\beta = \alpha + 1$, $q \mid s_3$, $\gcd(2a, q) = 1$):** Here $a(2k+1) \pmod q$ runs uniformly over $\mathbb{Z}/q\mathbb{Z}$, each residue occurring $\frac{s_3}{q}$ times. The residues $r \in \mathbb{Z}/q\mathbb{Z}$ with $\|r/q\| < d_n$ satisfy $|r| < q d_n$, of count $2\lceil q d_n \rceil - 1$. In general, any shifted set $\{\|r/q + \theta\| < d_n\}$ lies in an open interval of length $2 d_n$ on $\mathbb{R}/\mathbb{Z}$, which contains at most $\lceil 2 q d_n \rceil$ points of $\frac{1}{q}\mathbb{Z}/\mathbb{Z}$. For $d_n = \frac{1}{2n+3} \le \frac{1}{13}$ and odd $q \ge 3$:
  - Unshifted: $2\lceil q d_n \rceil - 1 \le \frac{q}{3}$ holds for $q = 3, \dots, 11$ ($2(1)-1 = 1 \le q/3$), for $q = 13$ ($2(1)-1 = 1 < 13/3$), and for $q \ge 15$ ($2(qd_n + 1) - 1 = 2qd_n + 1 \le \frac{2}{13}q + 1 < \frac{q}{3}$).
  - Shifted: $\lceil 2qd_n \rceil \le \frac{q}{2}$ holds for $q = 3, 5$ ($\lceil 6/13 \rceil = 1 < 3/2$, $\lceil 10/13 \rceil = 1 < 5/2$) and $q \ge 7$ ($\lceil \frac{2}{13}q \rceil < \frac{2}{13}q + 1 < \frac{q}{2}$).
- **Case $q \ge 4$ even ($0 \le \beta \le \alpha$, $a$ odd, $(q/2) \mid s_3$):** As $k$ varies mod $q/2$, $2k+1$ runs over the $q/2$ odd residues mod $q$, so $a(2k+1) \pmod q$ visits each odd residue mod $q$ exactly $\frac{2s_3}{q}$ times. For $q \ge 4$ even and $d_n \le \frac{1}{13}$:
  - Unshifted: odd integers $r$ with $|r| < qd_n$ have count $2\lceil \frac{qd_n - 1}{2} \rceil$. This is $0$ for $q \le 12$, and for $q \ge 14$, $2\lceil \frac{qd_n - 1}{2} \rceil < qd_n + 1 \le \frac{q}{13} + 1 < \frac{q}{6}$, so at most $\frac{q/2}{3}$ bad odd residues.
  - Shifted: an open interval of length $2d_n$ on $\mathbb{R}/\mathbb{Z}$ contains at most $\lceil q d_n \rceil$ points of $\frac{2\mathbb{Z}+1}{q}/\mathbb{Z}$. For $q = 4, 6, 8, 10, 12$, $\lceil q d_n \rceil \le 1 \le \frac{q}{4}$; for $q \ge 14$, $\lceil q d_n \rceil < \frac{q}{13} + 1 \le \frac{q}{4}$, so at most $\frac{1}{2}$ of the $q/2$ odd residues are bad. $\blacksquare$

#### Lemma 3c (Uniform 3-Runner Safe Measure)
For every $n \ge 5$ and every triple of distinct positive integers $(s_1, s_2, s_3)$,
$$\mu\bigl(S_{123}(s_1, s_2, s_3)\bigr) \ge \mu_n = \frac{3}{22}\delta_n^2 \eta_n.$$

**Proof.** Dividing by $g = \gcd(s_1, s_2, s_3)$ preserves $\mu(S_{123})$ via the $g$-to-$1$ measure-preserving map $t \mapsto gt \pmod 1$, so assume $\gcd(s_1, s_2, s_3) = 1$ and, by symmetry of the first two coordinates, $s_1 < s_2$.

Set $I_3 := \{t \in [0, 1) : \|s_3 t\| \ge y_n\} = \bigsqcup_{k=0}^{s_3 - 1} J_k$, where $J_k := \left[t_k - \frac{\eta_n}{s_3},\; t_k + \frac{\eta_n}{s_3}\right]$ has length $L_3 := \frac{2\eta_n}{s_3}$. Put $w_n := \delta_n \eta_n$, $W_n := \frac{1}{2}w_n$, and $M_n := \frac{4}{w_n}$.

- **Regime A ($s_1 \ge \frac{2s_3}{\eta_n}$):** Then $s_2 > s_1 \ge \frac{4}{L_3}$. By Lemma 3a, on each $J_k$ each $s_i$ ($i=1,2$) removes measure at most $\frac{5}{2}x_n L_3 < \frac{1}{4}L_3$ (as $x_n < \frac{1}{13}$), leaving $\mu(S_{123} \cap J_k) \ge \frac{1}{2}L_3$, so $\mu(S_{123}) \ge \eta_n > \mu_n$.

- **Regime B ($s_1 < \frac{2s_3}{\eta_n}$ and $s_2 \ge M_n s_3$):** First, $\{t \in I_3 : \|s_1 t\| \ge x_n\}$ contains pairwise disjoint intervals $K_r$ of length $\ge \frac{w_n}{s_3}$ and total measure $\ge W_n$:
  - If $2s_3 \nmid s_1$: by Lemma 3b(1), $> \frac{1}{2} s_3$ indices $k$ satisfy $\|s_1 t_k\| \ge d_n$. Around each, on $|t - t_k| \le \frac{w_n}{2s_3}$ we have $t \in J_k$ and $s_1|t - t_k| < \delta_n$, giving safe intervals of length $\frac{w_n}{s_3}$ and total measure $> W_n$.
  - If $2s_3 \mid s_1$: write $s_1 = 2m_1 s_3$ ($m_1 \ge 1$). On $J_k$, parameterize $t = t_k + \frac{u}{s_3}$ ($u \in [0, \eta_n]$), so $\|s_1 t\| = \|2m_1 u\|$. For $m_1 = 1$, $u \in [\frac{x_n}{2}, \eta_n]$ is safe with $u$-width $> \eta_n - \frac{d_n}{2} = \frac{3}{2(2n+2)(2n+3)} > w_n$ (since $\delta_n = \frac{1}{20(2n+3)^2}$). For $m_1 \ge 2$, $u \in [\frac{x_n}{2m_1}, \min(\eta_n, \frac{1-x_n}{2m_1})]$ is safe with $u$-width $> \min(\frac{\eta_n}{2}, \frac{11}{26}\eta_n) > w_n$. Thus total safe measure is $\ge w_n > W_n$.

  On each $K_r$ of length $L \ge \frac{w_n}{s_3}$, $s_2 \ge M_n s_3 = \frac{4s_3}{w_n} \ge \frac{4}{L}$, so Lemma 3a removes at most $\frac{5}{2}x_n L < \frac{1}{4}L$, leaving measure $\ge \frac{3}{4}W_n = \frac{3}{8}\delta_n \eta_n > \mu_n$.

- **Regime C ($s_1 < s_2 < M_n s_3$):** Set $q_i := \frac{2s_3}{\gcd(s_i, 2s_3)}$.
  - **Subcase C1 ($2s_3 \nmid s_1$ and $2s_3 \nmid s_2$):** By Lemma 3b(1), at least $\frac{1}{3} s_3$ indices $k$ satisfy both $\|s_1 t_k\| \ge d_n$ and $\|s_2 t_k\| \ge d_n$. Around each, $|t - t_k| \le \frac{\delta_n}{M_n s_3} = \frac{\delta_n^2 \eta_n}{4s_3} < \frac{\eta_n}{s_3}$ lies in $S_{123}$, giving measure $\ge \frac{2\delta_n}{3M_n} = \frac{1}{6}\delta_n^2 \eta_n > \mu_n$.
  - **Subcase C2 (One of $s_1, s_2$ is divisible by $2s_3$, and the other has $q \ge 3$):** Say $s_a = 2m_a s_3$ ($m_a \ge 1$) and $q_b \ge 3$. Put $u_0 := \frac{d_n}{2m_a}$ and $t_k^* := t_k + \frac{u_0}{s_3}$. Then $\|s_a t_k^*\| = d_n$, $\|s_3 t_k^*\| = \frac{1}{2} - u_0 \ge y_n + \gamma_n$ with $\gamma_n := \eta_n - \frac{d_n}{2} = \frac{3}{2(2n+2)(2n+3)} > \frac{\delta_n}{M_n}$, and by Lemma 3b(2) at least $\frac{1}{2} s_3$ indices $k$ satisfy $\|s_b t_k^*\| \ge d_n$. Around each $t_k^*$, $|t - t_k^*| \le \frac{\delta_n}{M_n s_3}$ lies in $S_{123}$, giving measure $\ge \frac{1}{4}\delta_n^2 \eta_n > \mu_n$.
  - **Subcase C3 (Remaining cases):** Here $2s_3 \mid s_a$ and $q_b \in \{1, 2\}$, so $s_3 \mid s_b$, forcing $s_3 = 1$ (since $\gcd(s_1, s_2, s_3) = 1$) and at least one of $s_1, s_2$ even.
    - **C3a ($s_1 = 2$, $s_3 = 1$):** Set $t^* = \frac{1}{2} + u^*$ with $u^* = \frac{d_n}{2}$ if $(2n+3) \nmid s_2$; $u^* = \frac{d_n}{2} + \frac{1}{2q(2n+3)^2}$ if $s_2 = 2q(2n+3)$; and $u^* = \frac{d_n}{2} + \frac{1}{r(2n+3)^2}$ if $s_2 = r(2n+3)$ with $r$ odd. Then $\|2t^*\| \ge d_n$, $\|s_2 t^*\| \ge d_n$, and $\|t^*\| \ge y_n + \gamma_n''$ where $\gamma_n'' := \eta_n - \frac{2n+5}{2(2n+3)^2} = \frac{2n+5}{2(2n+2)(2n+3)^2} > \frac{\delta_n}{M_n}$. Thus $|t - t^*| \le \frac{\delta_n}{M_n}$ lies in $S_{123}$, giving measure $\ge \frac{1}{2}\delta_n^2 \eta_n > \mu_n$.
    - **C3b ($s_3 = 1$, $2 \notin \{s_1, s_2\}$, at least one of $s_1, s_2$ even $\ge 4$):** For $t = \frac{1}{2} + u$ ($u \in [0, \eta_n]$), $\|t\| \ge y_n$ always holds. By Lemma 3a on $[0, \eta_n]$:
      - Any even $s \ge 4$ has $\|s(\frac{1}{2}+u)\| = \|su\|$, with bad measure $\le \frac{x_n}{s}$ when $s\eta_n \le 1 - x_n$ ($\le \frac{x_n}{4}$ for $s=4$, $\le \frac{x_n}{6}$ for $s \ge 6$), and $< 2x_n \eta_n + \frac{2x_n \eta_n}{1 - x_n} < \frac{25}{6} x_n \eta_n$ when $s\eta_n > 1 - x_n$.
      - Any odd $s \ge 3$ has $\|s(\frac{1}{2}+u)\| = \|su + \frac{1}{2}\|$, with bad measure $0$ when $s\eta_n \le \frac{1}{2} - x_n$, and $< 2x_n \eta_n + \frac{2x_n \eta_n}{1/2 - x_n} < \frac{74}{11} x_n \eta_n < 7 x_n \eta_n$ when $s\eta_n > \frac{1}{2} - x_n$.
      Since $s_1 \ne s_2$, the combined bad measure on $[0, \eta_n]$ is at most:
      1. $\frac{x_n}{4} + \frac{x_n}{6} = \frac{5}{12} x_n$, leaving $> \eta_n - \frac{5}{12(2n+3)} = \frac{n+10}{12(n+1)(2n+3)} > \mu_n$; or
      2. $\frac{x_n}{4} + 7 x_n \eta_n$, leaving $> \frac{2n^2 - 3n - 23}{4(n+1)(2n+3)^2} \ge \frac{3}{(n+1)(2n+3)^2} > \mu_n$ ($n \ge 5$); or
      3. $\frac{25}{6} x_n \eta_n + \frac{74}{11} x_n \eta_n = \frac{719}{66} x_n \eta_n < 11 x_n \eta_n$, leaving $> \eta_n(1 - \frac{11}{2n+3}) \ge \frac{2}{13}\eta_n > \mu_n$ ($n \ge 5$).

In every case, $\mu(S_{123}(s_1, s_2, s_3)) \ge \mu_n$. $\blacksquare$

#### Lemma 4 ($Q_n^{(k)} \in \mathsf{MLPS}_k$)
For all $n \ge 5$ and $k \ge 3$, $Q_n^{(k)} \in \mathsf{MLPS}_k$.

**Proof.** For any distinct positive integer speeds $(s_1, \dots, s_k)$, Lemma 3c gives $\mu(S_{123}(s_1, s_2, s_3)) \ge \mu_n$. Each remaining runner $j \in \{4, \dots, k\}$ removes bad measure $2\varepsilon_{n,k} = \frac{\mu_n}{k}$, so at most $\frac{k-3}{k}\mu_n < \mu_n$ in total. Hence a valid $t \in S_{123}$ remains for all $k$ runners. $\blacksquare$

---

## 4. Conclusion for Question 4 ($k \ge 3$)
Fix $k \ge 3$, and suppose for contradiction that $\mathsf{MLPS}_k$ is determined by a finite collection of speed sets—meaning $\mathsf{MLPS}_k = U(\mathcal{S})$ for some finite collection $\mathcal{S}$ of distinct-speed $k$-tuples. By Lemma 0, $U(\mathcal{S}) = \bigcup_{r=1}^N C_r$ is a finite union of convex sets. By Lemma 4, the infinitely many points $\{Q_n^{(k)}\}_{n \ge 5}$ all lie in $\mathsf{MLPS}_k = \bigcup_{r=1}^N C_r$. By the Pigeonhole Principle, there exist $5 \le m < n$ and an index $r \in \{1, \dots, N\}$ such that $Q_m^{(k)}, Q_n^{(k)} \in C_r$. By convexity of $C_r$, the segment $[Q_n^{(k)}, Q_m^{(k)}]$ lies in $C_r \subseteq \mathsf{MLPS}_k$, contradicting Lemma 2.

Hence, $\mathsf{MLPS}_k$ is determined by finitely many speed sets if and only if $k \in \{1, 2\}$. $\blacksquare$

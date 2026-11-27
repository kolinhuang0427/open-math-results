# Proof: Negative Resolution of Question 2 (`jensen-2605.27941-ques2`)

## Statement
We resolve **Question 2** of Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, `arXiv:2605.27941v1` (`main.tex`, Section 5, lines 1138–1140) completely in the negative for every dimension $k \ge 3$:

> **Theorem.** For every integer $k \ge 3$, the mixed loneliness parameter space $\mathsf{MLPS}_k \subseteq (0, 1/2]^k$ is **neither convex nor a finite union of convex sets**.
>
> Moreover, for every $k \ge 3$, we construct an explicit infinite sequence $\{Q_n^{(k)}\}_{n \ge 5} \subset \mathsf{MLPS}_k \cap (0, 1/2)^k$ such that for all $5 \le m < n$, the open line segment $(Q_n^{(k)}, Q_m^{(k)})$ is not contained in $\mathsf{MLPS}_k$; in particular, the midpoint $\frac{1}{2}(Q_5^{(k)} + Q_7^{(k)})$ already lies outside $\mathsf{MLPS}_k$.

*(Note: By Definition 2 of Jensen `arXiv:2605.27941v1`, $\mathsf{MLPS}_k \subseteq (0, 1/2]^k$ already excludes all coordinate planes $d_i = 0$; our points $Q_n^{(k)}$ moreover satisfy $0 < Q_{n,i}^{(k)} < 1/2$ in every coordinate.)*

---

## 1. Explicit Construction
For every integer $n \ge 5$, define the exact rational quantities:
$$d_n := \frac{1}{2n+3}, \qquad \delta_n := \frac{1}{20(2n+3)^2}, \qquad x_n := d_n - \delta_n = \frac{20(2n+3)-1}{20(2n+3)^2},$$
$$\eta_n := \frac{2n+5}{4(n+1)(2n+3)}, \qquad y_n := \frac{1}{2} - \eta_n, \qquad \mu_n := \frac{3}{22}\delta_n^2 \eta_n.$$
For each integer $k \ge 3$, define $\varepsilon_{n,k} := \frac{\mu_n}{2k}$ and the vector
$$Q_n^{(k)} := \bigl(x_n,\; x_n,\; y_n,\; \underbrace{\varepsilon_{n,k}, \dots, \varepsilon_{n,k}}_{k-3}\bigr) \in (0, 1/2)^k.$$
(When $k = 3$, there are zero trailing $\varepsilon_{n,k}$ coordinates, so $Q_n^{(3)} = (x_n, x_n, y_n)$.)

Note the elementary monotonicity and size properties for all $n \ge 5$:
- $0 < x_n < d_n \le \frac{1}{13}$,
- $0 < \varepsilon_{n,k} < \mu_n < \eta_n < \frac{1}{12}$, so $y_n \in (\frac{5}{12}, \frac{1}{2})$,
- $x_n$ is strictly decreasing in $n$:
  $$x_n - x_{n+1} = \frac{2}{(2n+3)(2n+5)}\left(1 - \frac{4n+8}{20(2n+3)(2n+5)}\right) > 0,$$
- $\eta_n = \frac{1}{2(2n+3)} + \frac{3}{4(n+1)(2n+3)}$ is strictly decreasing in $n$, so $y_n$ is strictly increasing in $n$.

---

## 2. Segment Obstruction (Lemmas 1 and 2)

### Lemma 1 (Speed-tuple obstruction)
Let $n \ge 5$ and $k \ge 3$. Suppose $\mathbf{d} = (d_1, \dots, d_k) \in (0, 1/2]^k$ has $d_1 = d_2 = x$ and $d_3 = y$ satisfying
$$\frac{1}{2n+3} < x < \frac{1}{2n-1} \qquad\text{and}\qquad y > \frac{n - x}{2n+1}.$$
Then $\mathbf{d} \notin \mathsf{MLPS}_k$.

**Proof.** Choose $k$ distinct positive integer speeds $(s_1, \dots, s_k)$ with $s_1 = 2$, $s_2 = 2n+1$, $s_3 = 1$, and $s_4, \dots, s_k \in \mathbb{Z}_{>0} \setminus \{1, 2, 2n+1\}$ arbitrary distinct integers. Suppose for contradiction that there exists $t \in \mathbb{R}$ with $\|s_i t\| \ge d_i$ for all $i$. By $1$-periodicity and evenness $\|s(-t)\| = \|st\|$, we may assume $t \in [0, 1/2]$.

Since $n \ge 5$ and $x < \frac{1}{2n-1} \le \frac{1}{9}$, we have
$$y > \frac{n - x}{2n+1} > \frac{5 - 1/9}{11} > \frac{1}{3}.$$
On $[0, 1/2]$, $\|1 \cdot t\| = t$, so $\|t\| \ge y$ implies $t \in [y, 1/2] \subset (1/3, 1/2]$. Writing $t = \frac{1}{2} - u$, we have $0 \le u \le \frac{1}{2} - y < \frac{1}{6}$, so $2u \in [0, 1/3)$ and $\|2t\| = \|1 - 2u\| = 2u$. Hence $\|2t\| \ge x$ forces $u \ge \frac{x}{2}$.

Meanwhile,
$$\|(2n+1)t\| = \left\|\frac{2n+1}{2} - (2n+1)u\right\| = \left\|\frac{1}{2} - (2n+1)u\right\|.$$
Because $x > \frac{1}{2n+3}$ and $x < \frac{1}{2n-1}$, we have $(2n+3)x > 1$ and $(2n-1)x < 1$, which rearrange to
$$\frac{1}{2} - x < (2n+1)\frac{x}{2} < \frac{1}{2} + x.$$
Since $x < \frac{1}{9} < \frac{1}{2}$, any $u$ satisfying $\frac{1}{2} - x < (2n+1)u < \frac{1}{2} + x$ has $\|\frac{1}{2} - (2n+1)u\| < x$. Together with $u \ge \frac{x}{2}$ and $\|(2n+1)t\| \ge x$, this forces
$$(2n+1)u \ge \frac{1}{2} + x \implies u \ge \frac{1 + 2x}{2(2n+1)} = \frac{1}{2} - \frac{n - x}{2n+1}.$$
Thus $y \le t = \frac{1}{2} - u \le \frac{n - x}{2n+1}$, contradicting $y > \frac{n - x}{2n+1}$. $\blacksquare$

### Lemma 2 (Every segment $(Q_n^{(k)}, Q_m^{(k)})$ exits $\mathsf{MLPS}_k$)
Let $k \ge 3$ and let $5 \le m < n$. Set
$$x^* := \frac{1}{2n+3} + \delta_n = x_n + 2\delta_n, \qquad \lambda := \frac{x^* - x_n}{x_m - x_n} = \frac{2\delta_n}{x_m - x_n}.$$
Then $\lambda \in (0, 1)$ and $P := (1 - \lambda) Q_n^{(k)} + \lambda Q_m^{(k)} \notin \mathsf{MLPS}_k$.

**Proof.** Since $x_m \ge x_{n-1} = \frac{1}{2n+1} - \frac{1}{20(2n+1)^2}$, we have
$$x_{n-1} - x^* = \frac{2}{(2n+1)(2n+3)} - \frac{1}{20(2n+1)^2} - \frac{1}{20(2n+3)^2} > \frac{2}{(2n+1)(2n+3)} - \frac{1}{10(2n+1)^2} > 0,$$
so $x_n < x^* < x_m$, whence $\lambda \in (0, 1)$. Moreover,
$$\frac{1}{2n-1} - x^* = \frac{4}{(2n-1)(2n+3)} - \frac{1}{20(2n+3)^2} > 0,$$
so $\frac{1}{2n+3} < x^* < \frac{1}{2n-1}$.

The first three coordinates of $P$ are $(x^*, x^*, y^*)$ where $y^* = y_n - \lambda(y_n - y_m)$. Let us bound the ratio $\frac{y_n - y_m}{x_m - x_n}$ for $5 \le m < n$:
- Writing $x_m - x_n = \frac{2(n-m)}{(2m+3)(2n+3)}\left(1 - \frac{2m+2n+6}{20(2m+3)(2n+3)}\right)$ and using $2m+2n+6 < 2(2n+3)$ and $2m+3 \ge 13$, we get
  $$x_m - x_n > \frac{2(n-m)}{(2m+3)(2n+3)}\left(1 - \frac{1}{130}\right) = \frac{129}{130} \cdot \frac{2(n-m)}{(2m+3)(2n+3)}.$$
- Using $\eta_t = \frac{1}{2(2t+3)} + \frac{3}{4(t+1)(2t+3)}$, we have
  $$y_n - y_m = \eta_m - \eta_n = \frac{n-m}{(2m+3)(2n+3)} + \frac{3}{4}\cdot\frac{(n-m)(2m+2n+5)}{(m+1)(2m+3)(n+1)(2n+3)}.$$
  Since $m+1 \ge 6$ and $n+1 \ge 7$, we have $\frac{2m+2n+5}{(m+1)(n+1)} = \frac{2}{n+1} + \frac{2}{m+1} + \frac{1}{(m+1)(n+1)} \le \frac{2}{7} + \frac{2}{6} + \frac{1}{42} = \frac{9}{14} < \frac{2}{3}$, so the second term is at most $\frac{3}{4} \cdot \frac{9}{14} \cdot \frac{n-m}{(2m+3)(2n+3)} = \frac{27}{56}\cdot\frac{n-m}{(2m+3)(2n+3)} < \frac{1}{2}\cdot\frac{n-m}{(2m+3)(2n+3)}$. Hence
  $$y_n - y_m < \frac{3}{2}\cdot\frac{n-m}{(2m+3)(2n+3)}.$$
Dividing yields $0 < \frac{y_n - y_m}{x_m - x_n} < \frac{3}{4} \cdot \frac{130}{129} < 1$, so $y^* > y_n - 2\delta_n$.

On the other hand, since $x^* > d_n = \frac{1}{2n+3}$, we have $1 + 2x^* > \frac{2n+5}{2n+3}$, and therefore
$$\frac{n - x^*}{2n+1} = \frac{1}{2} - \frac{1 + 2x^*}{2(2n+1)} < \frac{1}{2} - \frac{2n+5}{2(2n+1)(2n+3)}.$$
Subtracting gives
$$y^* - \frac{n - x^*}{2n+1} > \frac{2n+5}{2(2n+1)(2n+3)} - \frac{2n+5}{4(n+1)(2n+3)} - \frac{1}{10(2n+3)^2} = \frac{2n+5}{4(n+1)(2n+1)(2n+3)} - \frac{1}{10(2n+3)^2}.$$
Clearing the positive denominator $20(n+1)(2n+1)(2n+3)^2$, the numerator is
$$5(2n+5)(2n+3) - 2(n+1)(2n+1) = 16n^2 + 74n + 73 > 0.$$
Hence $y^* > \frac{n - x^*}{2n+1}$, and Lemma 1 implies $P \notin \mathsf{MLPS}_k$. $\blacksquare$

*(Explicit midpoint check for $m=5, n=7$:* Note also that the literal midpoint $\frac{1}{2}(Q_5^{(k)} + Q_7^{(k)})$ has first three coordinates $(\frac{66071}{976820}, \frac{66071}{976820}, \frac{6485}{14144})$, where $\frac{1}{15} < \frac{66071}{976820} < \frac{1}{11}$ and $\frac{6485}{14144} > \frac{6 - 66071/976820}{13}$, so it fails Lemma 1 for $n_{\text{obs}} = 6$, i.e. speed tuple $(2, 13, 1, \dots)$.)

---

## 3. Membership $Q_n^{(k)} \in \mathsf{MLPS}_k$ (Lemmas 3 and 4)

For any distinct positive integers $s_1, s_2, s_3$, denote the 3-runner safe set by
$$S_{123}(s_1, s_2, s_3) := \bigl\{t \in [0, 1) : \|s_1 t\| \ge x_n,\; \|s_2 t\| \ge x_n,\; \|s_3 t\| \ge y_n\bigr\},$$
and let $\mu(\cdot)$ denote Lebesgue measure on $[0, 1)$.

### Lemma 3a (Elementary Bad-Measure Bound)
For any interval $J \subset \mathbb{R}$ of length $L > 0$, any integer $s \ge 1$, any shift $\theta \in \mathbb{R}$, and any $x \in (0, 1/2)$,
$$\mu\bigl(\{t \in J : \|st + \theta\| < x\}\bigr) \le 2xL + \frac{2x}{s}.$$
**Proof.** The function $t \mapsto \|st + \theta\|$ has period $1/s$, and on any interval of length $1/s$ the subset where $\|st + \theta\| < x$ has measure $2x/s$. Partitioning $J$ into $\lfloor sL \rfloor$ intervals of length $1/s$ and one remainder interval of length $< 1/s$ gives bad measure at most $(\lfloor sL \rfloor + 1)\frac{2x}{s} \le 2xL + \frac{2x}{s}$. $\blacksquare$

### Lemma 3b (Midpoint Counting Lemma)
Let $n \ge 5$, $s_3 \in \mathbb{Z}_{>0}$, and $s \in \mathbb{Z}_{>0}$ with $2s_3 \nmid s$. Put $q := \frac{2s_3}{\gcd(s, 2s_3)} \ge 2$ and $t_k := \frac{2k+1}{2s_3}$ for $k \in \{0, 1, \dots, s_3 - 1\}$. Then for any $\theta \in \mathbb{R}$:
1. When $\theta = 0$, the fraction of indices $k \in \{0, \dots, s_3 - 1\}$ with $\|s t_k\| < d_n$ is at most $\frac{1}{3}$ (in particular, strictly less than $\frac{1}{2}$).
2. When $\theta \in \mathbb{R}$ is arbitrary and $q \ge 3$, the fraction of indices $k \in \{0, \dots, s_3 - 1\}$ with $\|s t_k + \theta\| < d_n$ is at most $\frac{1}{2}$.

**Proof.** Write $2s_3 = 2^\alpha m$ ($m$ odd, $\alpha \ge 1$) and $s = 2^\beta m'$ ($m'$ odd, $\beta \ge 0$), and $s/g = a$ where $g = \gcd(s, 2s_3)$ and $\gcd(a, q) = 1$. Then $s t_k = \frac{a(2k+1)}{q}$.
- **If $q$ is odd:** then $\beta \ge \alpha$, so $q \mid m \mid s_3$ and $\gcd(2a, q) = 1$. As $k$ runs over $\{0, \dots, s_3 - 1\}$, $a(2k+1) \bmod q$ hits every residue class modulo $q$ exactly $s_3/q$ times.
  - Note $q \ge 3$ (since $2s_3 \nmid s \implies q > 1$ and $q$ is odd).
  - For $\theta = 0$: $\|r/q\| < d_n = \frac{1}{2n+3}$ counts $1$ residue ($r \equiv 0$) when $q \le 2n+3$ (fraction $\frac{1}{q} \le \frac{1}{3}$). When $q \ge 2n+4 \ge 14$, $\|r/q\| < d_n$ holds for $1 + 2(\lceil q d_n \rceil - 1) = 2\lceil q d_n \rceil - 1 < 2q d_n + 1$ residues, giving fraction $< 2 d_n + \frac{1}{q} \le \frac{2}{13} + \frac{1}{15} = \frac{43}{195} < \frac{1}{3}$.
  - For arbitrary $\theta \in \mathbb{R}$: the open interval $(-d_n, d_n) \subset \mathbb{R}/\mathbb{Z}$ of length $2d_n \le \frac{2}{13}$ contains at most $\lceil 2q d_n \rceil$ points of $\frac{1}{q}\mathbb{Z} + \theta$.
    - If $q = 3$: $\lceil 6 d_n \rceil = 1$, fraction $\le \frac{1}{3}$.
    - If $q = 5$: $\lceil 10 d_n \rceil = 1$, fraction $\le \frac{1}{5}$.
    - If $q \ge 7$: $\frac{\lceil 2q d_n \rceil}{q} < 2 d_n + \frac{1}{q} \le \frac{2}{13} + \frac{1}{7} = \frac{27}{91} < \frac{1}{2}$.
- **If $q$ is even:** then $\beta \le \alpha - 1$, $a$ is odd, and $q/2 = 2^{\alpha - \beta - 1} (m / \gcd(m', m))$ divides $s_3 = 2^{\alpha - 1} m$. Thus as $k$ runs over $\{0, \dots, s_3 - 1\}$, $a(2k+1) \bmod q$ hits each of the $q/2$ odd residues modulo $q$ exactly $\frac{s_3}{q/2}$ times.
  - For $q = 2$: the sole odd residue is $1 \pmod 2$, giving $\|1/2 + 0\| = 1/2 \ge d_n$ (fraction $0$ when $\theta = 0$).
  - For $\theta = 0$ and $q \ge 4$ even: odd residues $r \in \{1, 3, \dots, q-1\}$ with $\min(r, q-r) < q d_n$ do not exist when $q d_n \le 1$ (fraction $0$). When $q d_n > 1$, since $q$ is even we have $q \ge 2n+4 \ge 14$, and the number of odd integers in $[1, q d_n)$ is $\lceil \frac{q d_n - 1}{2} \rceil < \frac{q d_n + 1}{2}$. Doubling for $r$ and $q-r$ and dividing by $q/2$ gives fraction $< 2 d_n + \frac{2}{q} \le \frac{2}{13} + \frac{2}{14} = \frac{27}{91} < \frac{1}{3}$.
  - For arbitrary $\theta \in \mathbb{R}$ and $q \ge 4$ even: the points $\frac{r}{q} + \theta$ ($r$ odd) form a coset of spacing $\frac{2}{q}$, so $(-d_n, d_n)$ contains at most $\lceil q d_n \rceil$ of them.
    - If $q = 4$: $\lceil 4 d_n \rceil = 1$, fraction $\le \frac{1}{2}$.
    - If $q = 6$: $\lceil 6 d_n \rceil = 1$, fraction $\le \frac{1}{3}$.
    - If $q \ge 8$: $\frac{\lceil q d_n \rceil}{q/2} < 2 d_n + \frac{2}{q} \le \frac{2}{13} + \frac{2}{8} = \frac{21}{52} < \frac{1}{2}$.

Hence when $\theta = 0$ (for all $q \ge 2$) the bad fraction is at most $\frac{1}{3}$ (so $< \frac{1}{2}$), and when $q \ge 3$ and $\theta \in \mathbb{R}$ is arbitrary, the bad fraction is at most $\frac{1}{2}$. $\blacksquare$

### Lemma 3c (Uniform 3-Runner Safe Measure)
For every $n \ge 5$ and every triple of distinct positive integers $(s_1, s_2, s_3)$,
$$\mu\bigl(S_{123}(s_1, s_2, s_3)\bigr) \ge \mu_n = \frac{3}{22}\delta_n^2 \eta_n.$$

**Proof.** Let $g = \gcd(s_1, s_2, s_3)$. Since $t \mapsto gt \pmod 1$ is a measure-preserving $g$-to-$1$ map on $[0, 1)$, we have $\mu(S_{123}(s_1, s_2, s_3)) = \mu(S_{123}(s_1/g, s_2/g, s_3/g))$. Thus we may assume $\gcd(s_1, s_2, s_3) = 1$, and by symmetry of the first two coordinates, $s_1 < s_2$.

Set $I_3 := \{t \in [0, 1) : \|s_3 t\| \ge y_n\} = \bigsqcup_{k=0}^{s_3 - 1} J_k$, where $J_k := \left[t_k - \frac{\eta_n}{s_3},\; t_k + \frac{\eta_n}{s_3}\right]$ and $t_k = \frac{2k+1}{2s_3}$. Each $J_k$ has length $L_3 := \frac{2\eta_n}{s_3}$, and $\mu(I_3) = 2\eta_n$. Put $w_n := \delta_n \eta_n$, $W_n := \frac{1}{2}w_n$, and $M_n := \frac{4}{w_n}$.

We split into three exhaustive regimes:

- **Regime A ($s_1 \ge \frac{2s_3}{\eta_n}$):** Then $s_2 > s_1 \ge \frac{4}{L_3}$. By Lemma 3a, on each $J_k$ each $s_i$ ($i=1,2$) removes measure at most $2x_n L_3 + \frac{2x_n}{s_i} \le \frac{5}{2}x_n L_3 < \frac{1}{4}L_3$ (since $x_n < \frac{1}{13}$). Hence $\mu(S_{123} \cap J_k) \ge \frac{1}{2}L_3$ for every $k$, giving $\mu(S_{123}) \ge \eta_n > \mu_n$.

- **Regime B ($s_1 < \frac{2s_3}{\eta_n}$ and $s_2 \ge M_n s_3$):** We show $\{t \in I_3 : \|s_1 t\| \ge x_n\}$ contains a finite disjoint union of intervals $K_r$, each of length at least $\frac{w_n}{s_3}$, of total measure at least $W_n$:
  - If $2s_3 \nmid s_1$: by Lemma 3b(1), at least $\frac{2}{3} s_3 > \frac{1}{2} s_3$ indices $k$ satisfy $\|s_1 t_k\| \ge d_n$. Around each such $t_k$, on $|t - t_k| \le \frac{w_n}{2s_3} = \frac{\delta_n \eta_n}{2s_3}$, we have $|t - t_k| < \frac{\eta_n}{s_3}$ (so $t \in J_k$) and $s_1|t - t_k| < \frac{2s_3}{\eta_n} \cdot \frac{\delta_n \eta_n}{2s_3} = \delta_n$ (so $\|s_1 t\| \ge d_n - \delta_n = x_n$). Each such interval has length $\frac{w_n}{s_3}$, total measure $> \frac{1}{2}s_3 \cdot \frac{w_n}{s_3} = W_n$.
  - If $2s_3 \mid s_1$: write $s_1 = 2m_1 s_3$ with $1 \le m_1 < \frac{1}{\eta_n}$. On each $J_k$, parameterize $t = t_k + \frac{u}{s_3}$ ($u \in [0, \eta_n]$), so $\|s_1 t\| = \|2m_1 u\|$.
    - If $m_1 = 1$: the interval $u \in [\frac{x_n}{2}, \eta_n]$ is safe, with $u$-width $\eta_n - \frac{x_n}{2} > \eta_n - \frac{d_n}{2} = \frac{3}{2(2n+2)(2n+3)} > w_n$ (since $\delta_n = \frac{1}{20(2n+3)^2}$).
    - If $m_1 \ge 2$: the interval $u \in [\frac{x_n}{2m_1}, \min(\eta_n, \frac{1-x_n}{2m_1})]$ is safe, with $u$-width at least $\min(\eta_n - \frac{x_n}{4}, \frac{1-2x_n}{2m_1}) > \min(\frac{\eta_n}{2}, \frac{11}{26}\eta_n) = \frac{11}{26}\eta_n > w_n$.
    Thus each of the $s_3$ intervals $J_k$ contains a safe sub-interval of length $\ge \frac{w_n}{s_3}$, total measure $\ge w_n > W_n$.

  Now on each interval $K_r$ of length $L \ge \frac{w_n}{s_3}$, we have $s_2 \ge M_n s_3 = \frac{4s_3}{w_n} \ge \frac{4}{L}$. By Lemma 3a, $s_2$ removes at most $\frac{5}{2}x_n L < \frac{1}{4}L$, leaving measure at least $\frac{3}{4}W_n = \frac{3}{8}\delta_n \eta_n > \mu_n$.

- **Regime C ($s_1 < s_2 < M_n s_3$):**
  For $i \in \{1, 2\}$, define $q_i := \frac{2s_3}{\gcd(s_i, 2s_3)}$.
  - **Subcase C1 ($2s_3 \nmid s_1$ and $2s_3 \nmid s_2$):** By Lemma 3b(1), each $s_i$ fails $\|s_i t_k\| \ge d_n$ for at most $\frac{1}{3}s_3$ indices $k$, so at least $\frac{1}{3}s_3$ indices $k$ satisfy BOTH $\|s_1 t_k\| \ge d_n$ and $\|s_2 t_k\| \ge d_n$. Around each such $t_k$, for $|t - t_k| \le \frac{\delta_n}{M_n s_3} = \frac{\delta_n^2 \eta_n}{4s_3} < \frac{\eta_n}{s_3}$, we have $s_i|t - t_k| < \delta_n$, hence $t \in S_{123}$. Summing over $\ge \frac{1}{3}s_3$ intervals of length $\frac{2\delta_n}{M_n s_3}$ gives measure at least $\frac{2\delta_n}{3M_n} = \frac{1}{6}\delta_n^2 \eta_n > \mu_n$.
  - **Subcase C2 (One of $s_1, s_2$ is divisible by $2s_3$, and the other has $q \ge 3$):** By symmetry of $(s_1, s_2)$, write $s_a = 2m_a s_3$ ($m_a \ge 1$) and let $s_b$ be the other speed with $q_b \ge 3$. Set $u_0 := \frac{d_n}{2m_a}$ and $t_k^* := t_k + \frac{u_0}{s_3}$. Then $\|s_a t_k^*\| = \|2m_a u_0\| = d_n$, and $\|s_3 t_k^*\| = \frac{1}{2} - u_0 \ge \frac{1}{2} - \frac{d_n}{2} = y_n + \gamma_n$, where $\gamma_n := \eta_n - \frac{d_n}{2} = \frac{3}{2(2n+2)(2n+3)} > 0$. By Lemma 3b(2) applied to $s_b$ with shift $\theta = \frac{s_b}{s_3} u_0$, at least $\frac{1}{2}s_3$ indices $k$ satisfy $\|s_b t_k^*\| \ge d_n$. Around each such $t_k^*$, for $|t - t_k^*| \le \frac{\delta_n}{M_n s_3}$ (noting $\frac{\delta_n}{M_n} = \frac{\delta_n^2 \eta_n}{4} < \gamma_n$), we have $t \in S_{123}$. Total measure is at least $\frac{1}{2} s_3 \cdot \frac{2\delta_n}{M_n s_3} = \frac{1}{4}\delta_n^2 \eta_n > \mu_n$.
  - **Subcase C3 (All remaining cases):** If neither $2s_3 \mid s_1$ nor $2s_3 \mid s_2$, we are in C1; if $2s_3 \mid s_a$ and $q_b \ge 3$, we are in C2. Thus $2s_3 \mid s_a$ and $q_b \in \{1, 2\}$, so $s_3 \mid s_b$ as well. Since $\gcd(s_1, s_2, s_3) = 1$, this forces $s_3 = 1$, and at least one of $s_1, s_2$ is even.
    - **C3a ($s_1 = 2$, $s_3 = 1$):** Consider $t^* = \frac{1}{2} + u^*$ with:
      - $u^* = \frac{d_n}{2}$ if $(2n+3) \nmid s_2$;
      - $u^* = \frac{d_n}{2} + \frac{1}{2q(2n+3)^2}$ if $s_2 = 2q(2n+3)$ ($q \ge 1$);
      - $u^* = \frac{d_n}{2} + \frac{1}{r(2n+3)^2}$ if $s_2 = r(2n+3)$ with $r \ge 1$ odd.
      In the first case, $\|2t^*\| = d_n$, $\|s_2 t^*\| \ge d_n$ (because if $s_2 = 2m$, $\|s_2 t^*\| = \|\frac{m}{2n+3}\| \ge \frac{1}{2n+3}$, while if $s_2 = 2j+1$, $\|s_2 t^*\| = \|\frac{1}{2} + \frac{2j+1}{2(2n+3)}\| \ge \frac{1}{2n+3}$ as $(2n+3) \nmid (2j+1)$), and $\|t^*\| = \frac{1}{2} - \frac{d_n}{2} > y_n + \gamma_n''$. In the second and third cases, $s_2 t^* \equiv \pm \frac{1}{2n+3} \pmod 1$ so $\|s_2 t^*\| = d_n$, $\|2t^*\| = 2u^* > d_n$, and $\|t^*\| = \frac{1}{2} - u^* \ge \frac{1}{2} - \frac{2n+5}{2(2n+3)^2} = y_n + \gamma_n''$, where $\gamma_n'' := \eta_n - \frac{2n+5}{2(2n+3)^2} = \frac{2n+5}{2(2n+2)(2n+3)^2} > 0$. Since $\frac{\delta_n}{M_n} = \frac{\delta_n^2 \eta_n}{4} < \gamma_n''$, the interval $|t - t^*| \le \frac{\delta_n}{M_n}$ lies in $S_{123}$, giving measure $\ge \frac{2\delta_n}{M_n} = \frac{1}{2}\delta_n^2 \eta_n > \mu_n$.
    - **C3b ($s_3 = 1$, $2 \notin \{s_1, s_2\}$, and at least one of $s_1, s_2$ is even $\ge 4$):** Parameterize $t = \frac{1}{2} + u$ with $u \in [0, \eta_n]$ (where $\|s_3 t\| \ge y_n$ holds identically). By Lemma 3a on $[0, \eta_n]$ (of length $\eta_n$):
      - Any even $s \ge 4$ has $\|s(\frac{1}{2}+u)\| = \|s u\|$. If $s\eta_n \le 1 - x_n$, the bad set in $[0, \eta_n]$ is $[0, \frac{x_n}{s})$ of measure $\frac{x_n}{s} \le \frac{x_n}{4}$ (and $\le \frac{x_n}{6}$ if $s \ge 6$). If $s\eta_n > 1 - x_n$, then $\frac{1}{s} < \frac{\eta_n}{1 - x_n}$, so Lemma 3a gives bad measure $\le 2x_n \eta_n + \frac{2x_n}{s} < 2x_n \eta_n + \frac{2x_n \eta_n}{1 - x_n} < \frac{25}{6}x_n \eta_n$ (using $x_n < \frac{1}{13}$).
      - Any odd $s \ge 3$ has $\|s(\frac{1}{2}+u)\| = \|s u + \frac{1}{2}\|$. If $s\eta_n \le \frac{1}{2} - x_n$, the bad measure on $[0, \eta_n]$ is $0$. If $s\eta_n > \frac{1}{2} - x_n$, then $\frac{1}{s} < \frac{\eta_n}{1/2 - x_n}$, so Lemma 3a gives bad measure $\le 2x_n \eta_n + \frac{2x_n}{s} < 2x_n \eta_n + \frac{2x_n \eta_n}{1/2 - x_n} < 7 x_n \eta_n$ (since $\frac{1}{1/2 - 1/13} = \frac{26}{11}$ and $2 + \frac{52}{11} = \frac{74}{11} < 7$).

      Because $s_1 \neq s_2$ and at least one is even $\ge 4$, the combined bad measure of $\{s_1, s_2\}$ on $[0, \eta_n]$ is at most:
      1. $\frac{x_n}{4} + \frac{x_n}{6} = \frac{5}{12} x_n$, giving remaining measure $> \eta_n - \frac{5}{12(2n+3)} = \frac{n+10}{12(n+1)(2n+3)} > \mu_n$; or
      2. $\frac{x_n}{4} + 7 x_n \eta_n$, giving remaining measure $> \eta_n - \frac{1}{4(2n+3)} - \frac{7\eta_n}{2n+3} = \frac{2n^2 - 3n - 23}{4(n+1)(2n+3)^2} \ge \frac{3}{(n+1)(2n+3)^2} > \mu_n$ for all $n \ge 5$; or
      3. $\frac{25}{6} x_n \eta_n + \frac{74}{11} x_n \eta_n = \frac{719}{66} x_n \eta_n < 11 x_n \eta_n$, giving remaining measure $> \eta_n\left(1 - \frac{11}{2n+3}\right) \ge \frac{2}{13}\eta_n > \mu_n$ for all $n \ge 5$.

In every regime and subcase, $\mu(S_{123}(s_1, s_2, s_3)) \ge \mu_n$. $\blacksquare$

### Lemma 4 ($Q_n^{(k)} \in \mathsf{MLPS}_k$)
For every $n \ge 5$ and every $k \ge 3$, $Q_n^{(k)} \in \mathsf{MLPS}_k$.

**Proof.** Let $(s_1, \dots, s_k)$ be any tuple of $k$ distinct positive integer speeds. By Lemma 3c, the set $S_{123}(s_1, s_2, s_3) \subseteq [0, 1)$ has Lebesgue measure at least $\mu_n > 0$. For $k = 3$, this already shows $S_{123} \neq \emptyset$. For $k \ge 4$, each $j \in \{4, \dots, k\}$ has bad set $\{t \in [0, 1) : \|s_j t\| < \varepsilon_{n,k}\}$ of Lebesgue measure $2\varepsilon_{n,k} = \frac{\mu_n}{k}$. Therefore the union of these $k - 3$ bad sets has measure at most
$$\frac{k-3}{k}\mu_n < \mu_n \le \mu(S_{123}(s_1, s_2, s_3)),$$
so there exists $t \in S_{123}(s_1, s_2, s_3)$ satisfying $\|s_j t\| \ge \varepsilon_{n,k}$ for all $j = 4, \dots, k$. Hence $Q_n^{(k)} \in \mathsf{MLPS}_k$. $\blacksquare$

---

## 4. Proof of the Main Theorem
Fix any $k \ge 3$. By Lemma 4, the infinite sequence $\{Q_n^{(k)}\}_{n \ge 5}$ lies entirely inside $\mathsf{MLPS}_k \subset (0, 1/2]^k$.

1. **Not convex:** By Lemma 2 (for $m = 5, n = 6$), $Q_5^{(k)}, Q_6^{(k)} \in \mathsf{MLPS}_k$ while the point $P = (1 - \lambda) Q_6^{(k)} + \lambda Q_5^{(k)}$ on the segment joining them lies outside $\mathsf{MLPS}_k$ (and likewise the midpoint $\frac{1}{2}(Q_5^{(k)} + Q_7^{(k)}) \notin \mathsf{MLPS}_k$ by Lemma 1 with speed $s_2 = 13$). Thus $\mathsf{MLPS}_k$ is not convex.
2. **Not a finite union of convex sets:** Suppose for contradiction that $\mathsf{MLPS}_k = \bigcup_{r=1}^N C_r$ for finitely many convex sets $C_1, \dots, C_N$. By the Pigeonhole Principle applied to the infinitely many points $\{Q_n^{(k)}\}_{n \ge 5} \subseteq \mathsf{MLPS}_k$, there exist integers $5 \le m < n$ and an index $r \in \{1, \dots, N\}$ such that $Q_m^{(k)}, Q_n^{(k)} \in C_r$. Since $C_r$ is convex, the entire line segment $[Q_n^{(k)}, Q_m^{(k)}]$ must lie in $C_r \subseteq \mathsf{MLPS}_k$, contradicting Lemma 2.

Hence, for every $k \ge 3$, $\mathsf{MLPS}_k$ is neither convex nor a finite union of convex sets. $\blacksquare$

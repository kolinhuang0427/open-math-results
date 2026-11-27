# Complete Proof of Conjecture 6.1 (`conj:ITCCTIsymmetry`) in Derycke–Dukes–Le Borgne (2024/2025)

**Primary source:** Henri Derycke, Mark Dukes, and Yvan Le Borgne, *The sandpile model on the complete split graph, $q,t$-Schröder polynomials, and sawtooth polyominoes*, [arXiv:2402.15372v3](https://arxiv.org/abs/2402.15372v3) (2025-12-19), Section 2 (lines 866–1165 of `qtss1.tex`) and Section 6 (*Conclusion*, lines 2659–2669 of `qtss1.tex`), **Conjecture 6.1** (`\label{conj:ITCCTIsymmetry}`). *(Note: `qtss1.tex` has a source comment `% SECTION 7` above `\section{Conclusion}`, which renders as Section 6 in LaTeX, so `\label{conj:ITCCTIsymmetry}` is Conjecture 6.1 and `\label{thm:schroeder}` is Conjecture 6.2.)*

**Verification status:** Written proof (supported by exact-arithmetic verification of direct Abelian sandpile CTI/ITC enumeration on $S_{n,d}$, both cell decompositions, the generating-function identities, and the core $q$-hypergeometric polynomial identity in [verify.py](file:///Users/kolinhuang/Documents/open-math/targets/derycke-2402.15372-conj7_1/verify.py)); not peer-reviewed.

---

## Problem Statement and Main Theorem

Let $n \ge 1$ and $d \ge 0$ be integers, and let $S_{n, d}$ be the complete split graph with vertex set $\{s\} \cup V \cup W$, where $s$ is the sink (in the clique), $V = \{v_1, \dots, v_n\}$ is the set of non-sink clique vertices (each of degree $\deg(v_i) = n + d$), and $W = \{w_1, \dots, w_d\}$ is the independent set (each of degree $\deg(w_j) = n + 1$, adjacent to $s$ and all of $V$, with no edges inside $W$). Let $\mathcal{R}_{\mathrm{dec}}(S_{n, d})$ denote the set of sorted (weakly decreasing) recurrent sandpile configurations $c = (a_1, \dots, a_n; b_1, \dots, b_d)$ with $n + d - 1 \ge a_1 \ge \dots \ge a_n \ge 0$ and $n \ge b_1 \ge \dots \ge b_d \ge 0$.

For $c \in \mathcal{R}_{\mathrm{dec}}(S_{n, d})$, define $\mathrm{height}(c) := \sum_{i=1}^n a_i + \sum_{j=1}^d b_j$ and
$$\mathrm{level}(c) := \mathrm{height}(c) - \left(\binom{n + d}{2} - \binom{d}{2}\right) = \mathrm{height}(c) - \left(nd + \binom{n}{2}\right).$$
Starting from $c$ after toppling the sink $s$ (which adds $1$ grain to every vertex of $V \cup W$):
- **CTI parallel toppling** alternates toppling all currently unstable vertices in $V$ in parallel and all currently unstable vertices in $W$ in parallel, recording $\mathrm{ToppleRecord}_{\mathrm{CTI}}(c) = (P_1, Q_1, \dots, P_k, Q_k)$ with $P_i \cup Q_i \neq \emptyset$ for all $1 \le i \le k$, $p_i := |P_i|$, $q_i := |Q_i|$, and $\mathrm{wtopple}_{\mathrm{CTI}}(c) := \sum_{i=1}^k i(p_i + q_i)$.
- **ITC parallel toppling** alternates toppling all currently unstable vertices in $W$ in parallel and all currently unstable vertices in $V$ in parallel, recording $\mathrm{ToppleRecord}_{\mathrm{ITC}}(c) = (Q'_1, P'_1, \dots, Q'_k, P'_k)$ with $Q'_i \cup P'_i \neq \emptyset$ for all $1 \le i \le k$, $b_i := |Q'_i|$, $a_i := |P'_i|$, and $\mathrm{wtopple}_{\mathrm{ITC}}(c) := \sum_{i=1}^k i(b_i + a_i)$.

The $q, t$-CTI and $q, t$-ITC polynomials are
$$\mathfrak{F}_{n, d}^{\mathrm{CTI}}(q, t) := \sum_{c \in \mathcal{R}_{\mathrm{dec}}(S_{n, d})} q^{\mathrm{level}(c)} t^{\mathrm{wtopple}_{\mathrm{CTI}}(c) - (n + d)}, \qquad \mathfrak{F}_{n, d}^{\mathrm{ITC}}(q, t) := \sum_{c \in \mathcal{R}_{\mathrm{dec}}(S_{n, d})} q^{\mathrm{level}(c)} t^{\mathrm{wtopple}_{\mathrm{ITC}}(c) - (n + d)}.$$

> **Conjecture 6.1 (Derycke–Dukes–Le Borgne, arXiv:2402.15372v3, Section 6, `conj:ITCCTIsymmetry`):** *For all $n \ge 1$ and $d \ge 0$,*
> $$\mathfrak{F}_{n, d}^{\mathrm{CTI}}(q, t) = \mathfrak{F}_{n, d}^{\mathrm{ITC}}(q, t).$$

We prove a **strictly stronger refined equality** holding for each fixed total number $r$ of vertices toppled in round $1$ ($p_1 + q_1 = r$ in CTI; $a_1 + b_1 = r$ in ITC). For $1 \le r \le n + d$, define
$$\mathfrak{F}_{n, d, r}^{\mathrm{CTI}}(q, t) := \sum_{\substack{c \in \mathcal{R}_{\mathrm{dec}}(S_{n, d}) \\ p_1(c) + q_1(c) = r}} q^{\mathrm{level}(c)} t^{\mathrm{wtopple}_{\mathrm{CTI}}(c) - (n + d)}, \qquad \mathfrak{F}_{n, d, r}^{\mathrm{ITC}}(q, t) := \sum_{\substack{c \in \mathcal{R}_{\mathrm{dec}}(S_{n, d}) \\ a_1(c) + b_1(c) = r}} q^{\mathrm{level}(c)} t^{\mathrm{wtopple}_{\mathrm{ITC}}(c) - (n + d)}.$$

**Main Theorem (Refined CTI–ITC Equality).** *For all integers $n \ge 1$, $d \ge 0$, and $1 \le r \le n + d$,*
$$\mathfrak{F}_{n, d, r}^{\mathrm{CTI}}(q, t) = \mathfrak{F}_{n, d, r}^{\mathrm{ITC}}(q, t).$$
*Summing over $r = 1, \dots, n + d$ proves Conjecture 6.1 (`conj:ITCCTIsymmetry`): $\mathfrak{F}_{n, d}^{\mathrm{CTI}}(q, t) = \mathfrak{F}_{n, d}^{\mathrm{ITC}}(q, t)$ for all $n \ge 1$ and $d \ge 0$.*

*(Scope note: Combined with Corollary 3.6 of arXiv:2402.15372v3, this immediately also proves Conjecture 6.2 (`thm:schroeder`). Conjecture 6.3 (`prop:itc-cti`), which asks for an explicit sandpile bijection $\Psi$ preserving $(\mathrm{height}, \mathrm{wtopple})$, is not addressed here.)*

---

## Notation for $q$-Binomials and $q$-Pochhammer Symbols

Throughout, for integers $m \ge 0$, set $[m]_q := \frac{1 - q^m}{1 - q}$, $[m]_q! := \prod_{j=1}^m [j]_q$ (with $[0]_q! = 1$), and for $0 \le k \le m$,
$$\binom{m}{k}_q := \frac{[m]_q!}{[k]_q!\,[m - k]_q!}, \qquad \binom{m}{k_1, k_2, k_3}_q := \frac{[m]_q!}{[k_1]_q!\,[k_2]_q!\,[k_3]_q!} \quad (k_1 + k_2 + k_3 = m),$$
with $\binom{m}{k}_q = 0$ if $k < 0$ or $k > m$. For an indeterminate $u$ and integer $m \ge 0$, set $(u; q)_m := \prod_{j=0}^{m-1} (1 - u q^j)$ (with $(u; q)_0 = 1$) and $(u; q)_\infty := \prod_{j=0}^\infty (1 - u q^j)$. Recall two elementary identities:
1. *(Partition generating function)* The generating function $\sum_{0 \le \delta_1 \le \dots \le \delta_m \le M} q^{\delta_1 + \dots + \delta_m}$ equals $\binom{m + M}{m}_q$.
2. *(Finite $q$-binomial theorem)* For every integer $r \ge 0$,
   $$\Pi_r(X, Y) := \prod_{j=0}^{r-1} (Y + q^j X) = \sum_{a=0}^r q^{\binom{a}{2}} \binom{r}{a}_q X^a Y^{r - a},$$
   verified immediately by induction on $r$ via $\Pi_{r+1}(X, Y) = (Y + q^r X) \Pi_r(X, Y)$, since $q^{\binom{a}{2}} \binom{r}{a}_q + q^r q^{\binom{a-1}{2}} \binom{r}{a-1}_q = q^{\binom{a}{2}}\bigl(\binom{r}{a}_q + q^{r + 1 - a} \binom{r}{a - 1}_q\bigr) = q^{\binom{a}{2}} \binom{r + 1}{a}_q$.

---

## Section 1: Exact CTI Cell Decomposition from Sandpile Definitions

Fix $n \ge 1$ and $d \ge 0$. Define the set $\mathsf{CTI}_{n, d}$ of valid CTI-toppling sequences to consist of all pairs $\bigl((p_1, \dots, p_k), (q_1, \dots, q_k)\bigr)$ of length $k \ge 1$ of non-negative integers satisfying:
$$\sum_{i=1}^k p_i = n, \qquad \sum_{i=1}^k q_i = d, \qquad p_1 + q_1 \ge 1, \qquad \text{and} \qquad p_i \ge 1 \quad \text{for all } 2 \le i \le k.$$

**Proposition 1.1 (Exact CTI cell formula).** *For all $n \ge 1$, $d \ge 0$, and $1 \le r \le n + d$,*
$$\mathfrak{F}_{n, d, r}^{\mathrm{CTI}}(q, t) = \sum_{\substack{((p_1, \dots, p_k), (q_1, \dots, q_k)) \in \mathsf{CTI}_{n, d} \\ p_1 + q_1 = r}} q^{\sum_{i=1}^k \binom{p_i}{2}} t^{\sum_{i=1}^k (i - 1)(p_i + q_i)} \binom{r}{q_1}_q \prod_{i=2}^k \binom{p_i + p_{i-1} + q_{i-1} - 1}{p_i}_q \binom{p_i + q_i - 1}{q_i}_q.$$

*Proof.* By Dhar's burning criterion (Proposition 2.1 of arXiv:2402.15372v3), a stable sorted configuration $c = (a_1, \dots, a_n; b_1, \dots, b_d)$ lies in $\mathcal{R}_{\mathrm{dec}}(S_{n, d})$ if and only if, after toppling the sink $s$, CTI parallel toppling topples every vertex of $V \cup W$ exactly once. Let $(P_1, Q_1, \dots, P_k, Q_k)$ be the CTI toppling record of $c$, with $p_i = |P_i|$ and $q_i = |Q_i|$. Clearly $\sum_{i=1}^k p_i = n$, $\sum_{i=1}^k q_i = d$, and $p_i + q_i \ge 1$ for all $i$. For $i \ge 2$, if $p_i = 0$ then no clique vertex is unstable after $Q_{i-1}$ topples, and since $W$ is an independent set, toppling $Q_{i-1}$ sends no grains to remaining vertices of $W$; thus no independent vertex can be unstable either, forcing $Q_i = \emptyset$, contradicting $P_i \cup Q_i \neq \emptyset$. Hence $((p_1, \dots, p_k), (q_1, \dots, q_k)) \in \mathsf{CTI}_{n, d}$.

Conversely, fix any $((p_1, \dots, p_k), (q_1, \dots, q_k)) \in \mathsf{CTI}_{n, d}$, and set partial sums $A_i := \sum_{j=1}^i p_j$ and $B_i := \sum_{j=1}^i q_j$ ($0 \le i \le k$, with $A_0 = B_0 = 0$). Track the exact number of grains received by each untoppled vertex before each parallel step:
- **Step $P_1$:** After $s$ topples, each $v \in V$ has $a_v + 1$ grains; since $a_v \le n + d - 1$, $v \in P_1 \iff a_v + 1 \ge n + d \iff a_v = n + d - 1$ (a singleton interval of width $0$).
- **Step $Q_1$:** After $s$ and $P_1$ topple, each $w \in W$ has received $1 + p_1$ grains; since $b_w \le n$, $w \in Q_1 \iff b_w + 1 + p_1 \ge n + 1 \iff n - p_1 \le b_w \le n$ (interval of width $p_1$).
- **Step $P_i$ ($2 \le i \le k$):** Before $P_i$, $\{s\} \cup \bigcup_{j=1}^{i-1} (P_j \cup Q_j)$ have toppled (sending $1 + A_{i-1} + B_{i-1}$ grains to every untoppled $v \in V$), while before $P_{i-1}$ only $1 + A_{i-2} + B_{i-2}$ grains had arrived. Hence
  $$v \in P_i \iff n + d - 1 - (A_{i-1} + B_{i-1}) \le a_v \le n + d - 2 - (A_{i-2} + B_{i-2}),$$
  an interval of width $p_{i-1} + q_{i-1} - 1 \ge 0$ (since $p_{i-1} + q_{i-1} \ge 1$) whose lower endpoint is $\ge 0$ (as $A_{i-1} + B_{i-1} \le n + d - (p_k + q_k) \le n + d - 1$ because $p_k \ge 1$).
- **Step $Q_i$ ($2 \le i \le k$):** Before $Q_i$, $\{s\} \cup \bigcup_{j=1}^i P_j$ have sent $1 + A_i$ grains to every untoppled $w \in W$ (topplings in $W$ send no grains to $W$), while before $Q_{i-1}$ only $1 + A_{i-1}$ grains had arrived. Hence
  $$w \in Q_i \iff n - A_i \le b_w \le n - 1 - A_{i-1},$$
  an interval of width $p_i - 1 \ge 0$ (since $p_i \ge 1$) whose lower endpoint is $\ge n - A_k = 0$.

As $i$ runs from $1$ to $k$, the $P_i$-intervals are pairwise disjoint and strictly decreasing, and the $Q_i$-intervals are pairwise disjoint and strictly decreasing. Thus choosing weakly decreasing values for the $p_i$ vertices of $P_i$ and the $q_i$ vertices of $Q_i$ in their respective intervals produces a bijection between $\mathcal{R}_{\mathrm{dec}}(S_{n, d})$ and the disjoint union over $\mathsf{CTI}_{n, d}$ of these products of intervals.

Summing $q^{\mathrm{height}(c)}$ over the cell indexed by $((p_1, \dots, p_k), (q_1, \dots, q_k))$ yields $q^{\mathrm{height}_{\min}}$ times the product of the partition generating functions of the blocks:
$$1 \cdot \binom{p_1 + q_1}{q_1}_q \prod_{i=2}^k \binom{p_i + p_{i-1} + q_{i-1} - 1}{p_i}_q \binom{p_i + q_i - 1}{q_i}_q.$$
The minimal height of the cell is
$$\begin{aligned}
\mathrm{height}_{\min} &= \sum_{i=1}^k p_i \bigl(n + d - 1 - A_{i-1} - B_{i-1}\bigr) + \sum_{i=1}^k q_i (n - A_i) \\
&= n(n + d - 1) + nd - \sum_{1 \le j < i \le k} p_i p_j - \left(\sum_{1 \le j < i \le k} p_i q_j + \sum_{1 \le j \le i \le k} p_j q_i\right).
\end{aligned}$$
Since $\sum_{j < i} p_i q_j + \sum_{j \le i} p_j q_i = (\sum_r p_r)(\sum_s q_s) = nd$ and $\sum_{j < i} p_i p_j = \binom{n}{2} - \sum_{i=1}^k \binom{p_i}{2}$, we obtain
$$\mathrm{level}_{\min} = \mathrm{height}_{\min} - \left(nd + \binom{n}{2}\right) = n(n + d - 1) - 2\binom{n}{2} - nd + \sum_{i=1}^k \binom{p_i}{2} = \sum_{i=1}^k \binom{p_i}{2}.$$
Finally, $\mathrm{wtopple}_{\mathrm{CTI}}(c) - (n + d) = \sum_{i=1}^k i(p_i + q_i) - \sum_{i=1}^k (p_i + q_i) = \sum_{i=1}^k (i - 1)(p_i + q_i)$. Restricting to $p_1 + q_1 = r$ gives the formula. $\square$

---

## Section 2: Exact ITC Cell Decomposition from Sandpile Definitions

For completeness (and to include $d = 0$ uniformly alongside Proposition 3.9 of arXiv:2402.15372v3), we record the parallel derivation for ITC toppling. By Theorem 2.7 of arXiv:2402.15372v3, the set $\mathsf{ITC}_{n, d}$ ($n \ge 1, d \ge 0$) consists of all pairs $((b_1, \dots, b_k), (a_1, \dots, a_k))$ of length $k \ge 1$ of non-negative integers with $\sum_{i=1}^k b_i = d$, $\sum_{i=1}^k a_i = n$, $a_1, \dots, a_{k-1} \ge 1$, $a_k \ge 0$, and $a_k + b_k \ge 1$ (note $a_1 \ge 1$ even when $k = 1$, since $a_1 = n \ge 1$). Set $a_0 := 1$.

**Proposition 2.1 (Exact ITC cell formula; cf. Proposition 3.9 of arXiv:2402.15372v3).** *For all $n \ge 1$, $d \ge 0$, and $1 \le r \le n + d$,*
$$\mathfrak{F}_{n, d, r}^{\mathrm{ITC}}(q, t) = \sum_{\substack{((b_1, \dots, b_k), (a_1, \dots, a_k)) \in \mathsf{ITC}_{n, d} \\ a_1 + b_1 = r}} \prod_{i=1}^k q^{\binom{a_i}{2}} \binom{a_i + b_i + a_{i-1} - 1}{a_i,\, b_i,\, a_{i-1} - 1}_q t^{(i - 1)(a_i + b_i)}.$$

*Proof.* Set $A'_i := \sum_{j=1}^i a_j$ and $B'_i := \sum_{j=1}^i b_j$ ($A'_0 = B'_0 = 0$). Under ITC toppling $(Q'_1, P'_1, \dots, Q'_k, P'_k)$ after toppling $s$, the exact threshold intervals are:
- $Q'_1$: $b_w = n$ (width $0$, factor $1$);
- $P'_1$: $n + d - 1 - b_1 \le a_v \le n + d - 1$ (width $b_1$, factor $\binom{a_1 + b_1}{a_1}_q = \binom{a_1 + b_1 + a_0 - 1}{a_1, b_1, a_0 - 1}_q$);
- $Q'_i$ ($2 \le i \le k$): $n - A'_{i-1} \le b_w \le n - 1 - A'_{i-2}$ (width $a_{i-1} - 1 \ge 0$, lower endpoint $\ge 0$, factor $\binom{b_i + a_{i-1} - 1}{b_i}_q$);
- $P'_i$ ($2 \le i \le k$): if $a_i \ge 1$, $n + d - 1 - A'_{i-1} - B'_i \le a_v \le n + d - 2 - A'_{i-2} - B'_{i-1}$ (width $a_{i-1} + b_i - 1 \ge 0$, lower endpoint $\ge n + d - 1 - (n - a_i + d) \ge 0$, factor $\binom{a_i + b_i + a_{i-1} - 1}{a_i}_q$); if $a_i = 0$ (only possible at $i = k$), $P'_k = \emptyset$ and the factor is $1 = \binom{0 + b_k + a_{k-1} - 1}{0}_q$.

For each $i \ge 2$, the product of the $Q'_i$ and $P'_i$ factors is
$$\binom{b_i + a_{i-1} - 1}{b_i}_q \binom{a_i + b_i + a_{i-1} - 1}{a_i}_q = \binom{a_i + b_i + a_{i-1} - 1}{a_i,\, b_i,\, a_{i-1} - 1}_q.$$
The minimal height is $\sum_{i=1}^k a_i(n + d - 1 - A'_{i-1} - B'_i) + \sum_{i=1}^k b_i(n - A'_{i-1})$. Since $\sum_{i=1}^k a_i B'_i + \sum_{i=1}^k b_i A'_{i-1} = \sum_{j \le i} a_i b_j + \sum_{j < i} b_i a_j = nd$, subtracting $nd + \binom{n}{2}$ again leaves $\mathrm{level}_{\min} = \sum_{i=1}^k \binom{a_i}{2}$. Restricting to $a_1 + b_1 = r$ gives the result. $\square$

---

## Section 3: Generating-Function Reformulation

Work in the formal power series ring $\mathbb{Z}[q, t][[X, Y]]$.

1. **ITC series $H_a(X, Y)$ and $P_r(X, Y)$:** Set $H_0(X, Y) := 1$. For $a \ge 1$, define $H_a(X, Y) = \sum_{n, d \ge 0} H(n, d, a) X^n Y^d \in \mathbb{Z}[q, t][[X, Y]]$ to be the unique formal power series solution to
   $$H_a(X, Y) = \frac{1}{(Y; q)_a} + \sum_{m=1}^\infty q^{\binom{m}{2}} \binom{m + a - 1}{m}_q \frac{X^m}{(Y; q)_{m + a}} H_m(tX, tY) \qquad (a \ge 1).$$
   Uniqueness and integrality follow by induction on the $X$-degree $n$: $[X^0] H_a(X, Y) = \frac{1}{(Y; q)_a} = \sum_{d \ge 0} \binom{d + a - 1}{d}_q Y^d$, and for $n \ge 1$, expanding $\frac{1}{(Y; q)_{m + a}} = \sum_{b \ge 0} \binom{m + b + a - 1}{b}_q Y^b$ and using $\binom{m + a - 1}{m}_q \binom{m + b + a - 1}{b}_q = \binom{m + b + a - 1}{m, b, a - 1}_q$ yields
   $$H(n, d, a) = \sum_{m=1}^n \sum_{b=0}^d q^{\binom{m}{2}} \binom{m + b + a - 1}{m, b, a - 1}_q t^{(n - m) + (d - b)} H(n - m, d - b, m).$$
   Unrolling this recurrence (noting that the base case $H(0, d', a') = \binom{d' + a' - 1}{d'}_q = \binom{0 + d' + a' - 1}{0, d', a' - 1}_q$ accounts for a final step with $a_k = 0, b_k = d' > 0$, while $H(0, 0, a') = 1$ terminates when $a_k > 0$) shows that for every $n \ge 1$, $d \ge 0$, and $1 \le r \le n + d$,
   $$\mathfrak{F}_{n, d, r}^{\mathrm{ITC}}(q, t) = \sum_{\substack{a_1 \ge 1,\, b_1 \ge 0 \\ a_1 + b_1 = r,\, a_1 \le n,\, b_1 \le d}} q^{\binom{a_1}{2}} \binom{r}{b_1}_q t^{n + d - r} H(n - a_1, d - b_1, a_1).$$
   Define, for every integer $r \ge 1$,
   $$P_r(X, Y) := \sum_{a=0}^r q^{\binom{a}{2}} \binom{r}{a}_q X^a Y^{r - a} H_a(X, Y) \in \mathbb{Z}[q, t][[X, Y]].$$
   Replacing $(X, Y)$ by $(tx, ty)$ and dividing by $t^r$, we have
   $$t^{-r} P_r(tx, ty) = \sum_{a=0}^r q^{\binom{a}{2}} \binom{r}{a}_q x^a y^{r - a} H_a(tx, ty) = y^r + \sum_{\substack{n \ge 1,\, d \ge 0}} \mathfrak{F}_{n, d, r}^{\mathrm{ITC}}(q, t)\, x^n y^d.$$

2. **CTI series $\widetilde{G}_r(X, Y)$ and $\widetilde{P}_r(X, Y)$:** For integers $r, r' \ge 1$, define the homogeneous polynomial of degree $r'$ in $(X, Y)$:
   $$K_{r, r'}(X, Y) := \sum_{p=1}^{r'} q^{\binom{p}{2}} \binom{p + r - 1}{p}_q \binom{r' - 1}{p - 1}_q X^p Y^{r' - p} \in \mathbb{Z}[q][X, Y].$$
   Define $\widetilde{G}_r(X, Y) \in \mathbb{Z}[q, t][[X, Y]]$ ($r \ge 1$) to be the unique formal power series solution to
   $$\widetilde{G}_r(X, Y) = 1 + \sum_{r'=1}^\infty K_{r, r'}(X, Y)\, \widetilde{G}_{r'}(tX, tY) = 1 + \sum_{p=1}^\infty \sum_{s=0}^\infty q^{\binom{p}{2}} \binom{p + r - 1}{p}_q \binom{p + s - 1}{s}_q X^p Y^s\, \widetilde{G}_{p + s}(tX, tY)$$
   (uniqueness follows immediately by induction on the total degree in $(X, Y)$, since $K_{r, r'}(X, Y)$ is homogeneous of degree $r' \ge 1$). Comparing $\widetilde{G}_r(tx, ty)$ with Proposition 1.1: step $i \ge 2$ contributes $q^{\binom{p_i}{2}} \binom{p_i + p_{i-1} + q_{i-1} - 1}{p_i}_q \binom{p_i + q_i - 1}{q_i}_q (t^{i-1} x)^{p_i} (t^{i-1} y)^{q_i}$, and the recursion terminates only at $(0, 0)$ with value $1$. Multiplying by the round-$1$ factor $\sum_{p_1 + q_1 = r} q^{\binom{p_1}{2}} \binom{r}{q_1}_q x^{p_1} y^{q_1} = \Pi_r(x, y)$ and defining
   $$\widetilde{P}_r(X, Y) := \Pi_r(X, Y)\, \widetilde{G}_r(X, Y) \in \mathbb{Z}[q, t][[X, Y]],$$
   we obtain (since $\Pi_r(tx, ty) = t^r \Pi_r(x, y)$)
   $$t^{-r} \widetilde{P}_r(tx, ty) = \Pi_r(x, y)\, \widetilde{G}_r(tx, ty) = y^r + \sum_{\substack{n \ge 1,\, d \ge 0}} \mathfrak{F}_{n, d, r}^{\mathrm{CTI}}(q, t)\, x^n y^d.$$

Consequently, the Main Theorem is **equivalent** to the power series identity
$$\widetilde{P}_r(X, Y) = P_r(X, Y) \qquad \text{in } \mathbb{Z}[q, t][[X, Y]] \quad \text{for all } r \ge 1.$$

---

## Section 4: Proof of $\widetilde{P}_r(X, Y) = P_r(X, Y)$

The entire proof hinges on a single finite polynomial symmetry identity (Lemma 4.3), which we prove self-containedly via Cauchy's $q$-binomial theorem and Heine's third transformation.

**Lemma 4.1 (Cauchy's $q$-binomial theorem).** *For real $q \in (0, 1)$, $a \in \mathbb{R}$, and $|z| < 1$,*
$$\sum_{n=0}^\infty \frac{(a; q)_n}{(q; q)_n} z^n = \frac{(az; q)_\infty}{(z; q)_\infty}.$$

*Proof.* Let $f(z) := \sum_{n=0}^\infty \frac{(a; q)_n}{(q; q)_n} z^n$, which converges absolutely on $|z| < 1$ by the ratio test (since $\lim_{n \to \infty} \frac{|1 - a q^n|}{1 - q^{n+1}} = 1$). Then
$$f(z) - f(qz) = \sum_{n=1}^\infty \frac{(a; q)_n}{(q; q)_{n-1}} z^n = z \sum_{m=0}^\infty \frac{(a; q)_m (1 - a q^m)}{(q; q)_m} z^m = z\bigl(f(z) - a f(qz)\bigr),$$
giving $f(z) = \frac{1 - az}{1 - z} f(qz)$. Iterating $M$ times yields $f(z) = \frac{(az; q)_M}{(z; q)_M} f(q^M z)$. Letting $M \to \infty$ (as $q^M z \to 0$ and $f$ is continuous at $0$ with $f(0) = 1$) gives $f(z) = \frac{(az; q)_\infty}{(z; q)_\infty}$. $\square$

**Lemma 4.2 (Heine's third transformation at coefficient level).** *For every integer $N \ge 0$, the following polynomial identity holds in $\mathbb{Q}(q)[a, b]$ (with $c := q^2$):*
$$\frac{(a; q)_N (b; q)_N}{(q; q)_N (c; q)_N} = \sum_{j=0}^N \frac{(ab/c; q)_{N - j}}{(q; q)_{N - j}} \cdot \frac{\bigl(\prod_{i=0}^{j-1}(a - c q^i)\bigr)\bigl(\prod_{i=0}^{j-1}(b - c q^i)\bigr)}{(q; q)_j (c; q)_j c^j}.$$

*Proof.* First recall Heine's first transformation: for any real $q \in (0, 1)$, $\alpha, \beta, \gamma, \zeta \in \mathbb{R}$ with $0 < \beta < 1$, $0 < \zeta < 1$, and $\gamma \notin \{q^{-k} : k \ge 0\}$,
$${}_2\phi_1\!\!\left(\begin{matrix} \alpha, \beta \\ \gamma \end{matrix}; q, \zeta\right) := \sum_{n=0}^\infty \frac{(\alpha; q)_n (\beta; q)_n}{(q; q)_n (\gamma; q)_n} \zeta^n = \frac{(\beta; q)_\infty (\alpha\zeta; q)_\infty}{(\gamma; q)_\infty (\zeta; q)_\infty}\, {}_2\phi_1\!\!\left(\begin{matrix} \gamma/\beta,\, \zeta \\ \alpha\zeta \end{matrix}; q, \beta\right).$$
Indeed, writing $\frac{(\beta; q)_n}{(\gamma; q)_n} = \frac{(\beta; q)_\infty}{(\gamma; q)_\infty} \frac{(\gamma q^n; q)_\infty}{(\beta q^n; q)_\infty} = \frac{(\beta; q)_\infty}{(\gamma; q)_\infty} \sum_{k=0}^\infty \frac{(\gamma/\beta; q)_k}{(q; q)_k} (\beta q^n)^k$ by Lemma 4.1 (valid since $0 < \beta q^n < 1$), we obtain a double sum bounded termwise by $\left(\sum_{n=0}^\infty \frac{(-|\alpha|; q)_n}{(q; q)_n} \zeta^n\right)\left(\sum_{k=0}^\infty \frac{(-|\gamma/\beta|; q)_k}{(q; q)_k} \beta^k\right) < \infty$ (since $q^{nk} \le 1$ and $0 < \beta, \zeta < 1$). Swapping sums by Fubini's theorem and applying Lemma 4.1 to the inner $n$-sum $\sum_{n=0}^\infty \frac{(\alpha; q)_n}{(q; q)_n} (q^k \zeta)^n = \frac{(\alpha q^k \zeta; q)_\infty}{(q^k \zeta; q)_\infty} = \frac{(\alpha\zeta; q)_\infty (\zeta; q)_k}{(\zeta; q)_\infty (\alpha\zeta; q)_k}$ yields Heine's first transformation.

Now fix real $(q, a, b, z)$ in the nonempty open region $0 < q < 1$, $0 < a < q^2$, $q^2 < b < 1$, $0 < z < 1$, and set $c := q^2$. Note that $0 < c/b = q^2/b < 1$, $0 < az < q^2 < 1$, $0 < bz < 1$, and $0 < abz/c = abz/q^2 < b < 1$. Applying Heine's first transformation three consecutive times — first to $(\alpha,\beta,\gamma,\zeta) = (a, b, c, z)$, next to $(z, c/b, az, b)$ (using symmetry of ${}_2\phi_1$ in its upper parameters), and third to $(b, abz/c, bz, c/b)$ — all hypotheses hold at every step and the infinite products telescope to give Heine's third transformation:
$$\begin{aligned}
{}_2\phi_1\!\!\left(\begin{matrix} a, b \\ c \end{matrix}; q, z\right)
&= \frac{(b; q)_\infty (az; q)_\infty}{(c; q)_\infty (z; q)_\infty}\, {}_2\phi_1\!\!\left(\begin{matrix} z,\, c/b \\ az \end{matrix}; q, b\right) \\
&= \frac{(c/b; q)_\infty (bz; q)_\infty}{(c; q)_\infty (z; q)_\infty}\, {}_2\phi_1\!\!\left(\begin{matrix} b,\, abz/c \\ bz \end{matrix}; q, \frac{c}{b}\right) \\
&= \frac{(abz/c; q)_\infty}{(z; q)_\infty}\, {}_2\phi_1\!\!\left(\begin{matrix} c/a,\, c/b \\ c \end{matrix}; q, \frac{abz}{c}\right).
\end{aligned}$$
On the right-hand side, expand $\frac{(abz/c; q)_\infty}{(z; q)_\infty} = \sum_{k=0}^\infty \frac{(ab/c; q)_k}{(q; q)_k} z^k$ (Lemma 4.1, since $|z| < 1$) and multiply by the absolutely convergent series $\sum_{j=0}^\infty \frac{(c/a; q)_j (c/b; q)_j}{(q; q)_j (c; q)_j} (ab/c)^j z^j$ (since $|abz/c| < 1$). Equating coefficients of $z^N$ ($N \ge 0$) and using $(c/a; q)_j a^j = \prod_{i=0}^{j-1}(a - c q^i)$ and $(c/b; q)_j b^j = \prod_{i=0}^{j-1}(b - c q^i)$ gives the stated identity for all $(q, a, b)$ in the nonempty open set $\{(q, a, b) \in \mathbb{R}^3 : 0 < q < 1,\, 0 < a < q^2,\, q^2 < b < 1\}$. Clearing the common denominator $(q; q)_N (q^2; q)_N q^{2N}$ makes both sides polynomials in $\mathbb{Q}[q, a, b]$ agreeing on a nonempty open subset of $\mathbb{R}^3$, hence identically equal in $\mathbb{Q}[q, a, b]$. $\square$

**Lemma 4.3 (Finite polynomial symmetry identity).** *For all integers $r, r' \ge 1$, the following polynomial identity holds in $\mathbb{Z}[q, X, Y]$:*
$$\Pi_r(X, Y)\, K_{r, r'}(X, Y) = \Pi_{r'}(X, Y) \sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q \binom{r' + a - 1}{r'}_q X^a Y^{r - a}.$$

*Proof.* Both sides are homogeneous polynomials of degree $r + r'$ in $(X, Y)$, so setting $X = u Y$ and dividing by $Y^{r + r'}$, it is equivalent to prove in $\mathbb{Z}[q, u]$ that
$$(-u; q)_r K_u(r, r') = (-u; q)_{r'} \sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q \binom{r' + a - 1}{r'}_q u^a,$$
where $K_u(r, r') := \sum_{p=1}^{r'} q^{\binom{p}{2}} \binom{p + r - 1}{p}_q \binom{r' - 1}{p - 1}_q u^p$. Notice first that for every $1 \le a \le r$,
$$\binom{r}{a}_q \binom{r' + a - 1}{r'}_q = \frac{[r]_q}{[r']_q} \binom{a + r' - 1}{a}_q \binom{r - 1}{a - 1}_q,$$
so the sum on the right-hand side equals $\frac{[r]_q}{[r']_q} K_u(r', r)$. Next, write $K_u(r, r')$ in $q$-hypergeometric form by shifting $j = p - 1$ ($0 \le j \le r' - 1$): using $\binom{j + r}{j + 1}_q = [r]_q \frac{(q^{r+1}; q)_j}{(q^2; q)_j}$ and
$$\frac{(q^{1 - r'}; q)_j}{(q; q)_j} = (-1)^j q^{(1 - r') j + \binom{j}{2}} \binom{r' - 1}{j}_q \implies \frac{(q^{1 - r'}; q)_j}{(q; q)_j} (-q^{r'} u)^j = q^{\binom{j+1}{2}} \binom{r' - 1}{j}_q u^j,$$
we obtain
$$K_u(r, r') = [r]_q u \sum_{j=0}^{r' - 1} \frac{(q^{r+1}; q)_j (q^{1 - r'}; q)_j}{(q; q)_j (q^2; q)_j} (-q^{r'} u)^j.$$

Now specialize the polynomial identity of Lemma 4.2 to $a = q^{r+1}$ and $b = q^{1 - r'}$ (with $c = q^2$), multiply by $z^N$, and sum over all $N \ge 0$ in the formal power series ring $\mathbb{Q}(q)[[z]]$. Since $(q^{1 - r'}; q)_N = 0$ for all $N \ge r'$ and $\prod_{i=0}^{j-1}(q^{r+1} - q^{i+2}) = q^{(r+1)j} (q^{1 - r}; q)_j = 0$ for all $j \ge r$, both sums in $j$ and $N$ terminate cleanly, giving in $\mathbb{Q}(q)[[z]]$:
$$\sum_{N=0}^{r' - 1} \frac{(q^{r+1}; q)_N (q^{1 - r'}; q)_N}{(q; q)_N (q^2; q)_N} z^N = \left(\sum_{k=0}^\infty \frac{(q^{r - r'}; q)_k}{(q; q)_k} z^k\right) \sum_{j=0}^{r - 1} \frac{(q^{1 - r}; q)_j (q^{r' + 1}; q)_j}{(q; q)_j (q^2; q)_j} (q^{r - r'} z)^j.$$
By Lemma 4.1 (comparing coefficients in $\mathbb{Q}(q)[[z]]$ via $(q^{r - r'} z; q)_\infty / (z; q)_\infty$), the factor $\sum_{k=0}^\infty \frac{(q^{r - r'}; q)_k}{(q; q)_k} z^k$ equals $(q^{r - r'} z; q)_{r' - r}$ when $r \le r'$ and $\frac{1}{(z; q)_{r - r'}}$ when $r \ge r'$. Substituting $z = -q^{r'} u$ (so $q^{r - r'} z = -q^r u$), in **both** cases ($r \le r'$ and $r \ge r'$) this factor equals $\frac{(-u; q)_{r'}}{(-u; q)_r}$ in $\mathbb{Q}(q)[[u]]$. Multiplying both sides by $[r]_q u\, (-u; q)_r$ yields
$$(-u; q)_r K_u(r, r') = [r]_q u\, (-u; q)_{r'} \sum_{j=0}^{r - 1} \frac{(q^{r' + 1}; q)_j (q^{1 - r}; q)_j}{(q; q)_j (q^2; q)_j} (-q^r u)^j = \frac{[r]_q}{[r']_q} (-u; q)_{r'} K_u(r', r),$$
completing the proof. $\square$

**Theorem 4.4.** *For every integer $r \ge 1$, $\widetilde{P}_r(X, Y) = P_r(X, Y)$ in $\mathbb{Z}[q, t][[X, Y]]$.*

*Proof.* For any $F \in \mathbb{Z}[q, t][[X, Y]]$, denote by $F^{(N)}(X, Y) \in \mathbb{Z}[q, t][X, Y]$ its homogeneous component of total degree $N$ in $(X, Y)$. We prove $\widetilde{P}_r^{(N)}(X, Y) = P_r^{(N)}(X, Y)$ simultaneously for all $r \ge 1$ by strong induction on $N \ge 1$.

- **Base cases ($N \le r$):** Both $\widetilde{P}_r(X, Y) = \Pi_r(X, Y) \widetilde{G}_r(X, Y)$ and $P_r(X, Y) = \sum_{a=0}^r q^{\binom{a}{2}} \binom{r}{a}_q X^a Y^{r - a} H_a(X, Y)$ vanish in total degrees $N < r$. At $N = r$, since $\widetilde{G}_r(X, Y) = 1 + O(\deg \ge 1)$ and $H_a(X, Y) = 1 + O(\deg \ge 1)$,
  $$\widetilde{P}_r^{(r)}(X, Y) = \Pi_r(X, Y) = \sum_{a=0}^r q^{\binom{a}{2}} \binom{r}{a}_q X^a Y^{r - a} = P_r^{(r)}(X, Y).$$

- **Inductive step ($N > r \ge 1$):** Assume $\widetilde{P}_{r'}^{(M)}(X, Y) = P_{r'}^{(M)}(X, Y)$ for all $r' \ge 1$ and all $M < N$. Extracting total degree $N - r > 0$ from $\widetilde{G}_r(X, Y) = 1 + \sum_{r'=1}^\infty K_{r, r'}(X, Y) \widetilde{G}_{r'}(tX, tY)$ (where $K_{r, r'}$ is homogeneous of degree $r'$) gives
  $$\widetilde{G}_r^{(N - r)}(X, Y) = \sum_{r'=1}^{N - r} t^{N - r - r'} K_{r, r'}(X, Y)\, \widetilde{G}_{r'}^{(N - r - r')}(X, Y).$$
  For each $1 \le r' \le N - r$, since $M := N - r < N$, the induction hypothesis gives
  $$\Pi_{r'}(X, Y)\, \widetilde{G}_{r'}^{(N - r - r')}(X, Y) = \widetilde{P}_{r'}^{(N - r)}(X, Y) = P_{r'}^{(N - r)}(X, Y).$$
  Working in $\mathbb{Q}(q, t)(X, Y)$ (where $\Pi_{r'}(X, Y) \neq 0$), multiplying $\widetilde{G}_r^{(N - r)}$ by $\Pi_r(X, Y)$ and applying Lemma 4.3 yields
  $$\begin{aligned}
  \widetilde{P}_r^{(N)}(X, Y) &= \sum_{r'=1}^{N - r} t^{N - r - r'} \frac{\Pi_r(X, Y)\, K_{r, r'}(X, Y)}{\Pi_{r'}(X, Y)}\, P_{r'}^{(N - r)}(X, Y) \\
  &= \sum_{r'=1}^{N - r} t^{N - r - r'} \left(\sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q \binom{r' + a - 1}{r'}_q X^a Y^{r - a}\right) \left(\sum_{m=0}^{r'} q^{\binom{m}{2}} \binom{r'}{m}_q X^m Y^{r' - m} H_m^{(N - r - r')}(X, Y)\right).
  \end{aligned}$$
  Split the inner sum into $m = 0$ and $1 \le m \le r'$:
  1. For $m = 0$, $H_0^{(N - r - r')} = \delta_{r',\, N - r}$, so only $r' = N - r$ contributes (with $t^0$), giving
     $$\sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q \binom{N - r + a - 1}{N - r}_q X^a Y^{N - a} = \left[\sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q \frac{X^a Y^{r - a}}{(Y; q)_a}\right]^{(N)}.$$
  2. For $1 \le m \le r'$, set $k := r' - m \ge 0$ and apply the telescoping $q$-binomial identity
     $$\binom{r' + a - 1}{r'}_q \binom{r'}{m}_q = \frac{[r' + a - 1]_q!}{[a - 1]_q!\,[m]_q!\,[r' - m]_q!} = \binom{m + a - 1}{m}_q \binom{m + a + k - 1}{k}_q.$$
     Reindexing the finite sum over $m \ge 1, k \ge 0$ with $m + k \le N - r$ (so $N - r - r' = N - r - m - k$) gives
     $$\begin{aligned}
     &\sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q X^a Y^{r - a} \sum_{\substack{m \ge 1,\, k \ge 0 \\ m + k \le N - r}} q^{\binom{m}{2}} \binom{m + a - 1}{m}_q \binom{m + a + k - 1}{k}_q X^m Y^k\, t^{N - r - m - k} H_m^{(N - r - m - k)}(X, Y) \\
     &\qquad = \left[\sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q X^a Y^{r - a} \sum_{m=1}^\infty q^{\binom{m}{2}} \binom{m + a - 1}{m}_q \frac{X^m}{(Y; q)_{m + a}} H_m(tX, tY)\right]^{(N)}.
     \end{aligned}$$

  Adding the $m = 0$ and $m \ge 1$ contributions and substituting the defining recurrence of $H_a(X, Y)$ gives
  $$\widetilde{P}_r^{(N)}(X, Y) = \left[\sum_{a=1}^r q^{\binom{a}{2}} \binom{r}{a}_q X^a Y^{r - a} H_a(X, Y)\right]^{(N)} = P_r^{(N)}(X, Y),$$
  since the $a = 0$ term $Y^r$ of $P_r(X, Y)$ has degree $r < N$. This completes the induction. $\square$

**Proof of the Main Theorem and Conjecture 6.1.** By Theorem 4.4 and Section 3, for every integer $r \ge 1$,
$$y^r + \sum_{\substack{n \ge 1,\, d \ge 0}} \mathfrak{F}_{n, d, r}^{\mathrm{CTI}}(q, t)\, x^n y^d = t^{-r} \widetilde{P}_r(tx, ty) = t^{-r} P_r(tx, ty) = y^r + \sum_{\substack{n \ge 1,\, d \ge 0}} \mathfrak{F}_{n, d, r}^{\mathrm{ITC}}(q, t)\, x^n y^d.$$
Extracting $[x^n y^d]$ yields $\mathfrak{F}_{n, d, r}^{\mathrm{CTI}}(q, t) = \mathfrak{F}_{n, d, r}^{\mathrm{ITC}}(q, t)$ for all $n \ge 1$, $d \ge 0$, and $1 \le r \le n + d$. Summing over $r = 1, \dots, n + d$ gives $\mathfrak{F}_{n, d}^{\mathrm{CTI}}(q, t) = \mathfrak{F}_{n, d}^{\mathrm{ITC}}(q, t)$, proving Conjecture 6.1 (`conj:ITCCTIsymmetry`). $\blacksquare$

---

## Exact-Arithmetic Verification

Run:
```bash
.venv/bin/python targets/derycke-2402.15372-conj7_1/verify.py
```
which checks (using 100% exact integer/polynomial arithmetic, zero floating-point operations) direct Abelian sandpile CTI and ITC enumeration on $S_{n, d}$ ($n + d \le 7$), the refined first-round equality $\mathfrak{F}_{n, d, r}^{\mathrm{CTI}} = \mathfrak{F}_{n, d, r}^{\mathrm{ITC}}$ via Propositions 1.1 and 2.1 ($n + d \le 10$), the generating-function identity $\widetilde{P}_r(X, Y) = P_r(X, Y)$ ($1 \le r \le 6$, $N \le 9$), Lemma 4.2's polynomial identity ($N \le 6$), and Lemma 4.3's finite polynomial symmetry identity ($1 \le r, r' \le 8$).

## References

- H. Derycke, M. Dukes, and Y. Le Borgne, *The sandpile model on the complete split graph, $q,t$-Schröder polynomials, and sawtooth polyominoes*, arXiv:2402.15372v3 (2025).
- D. Dhar, *Theoretical studies of self-organized criticality*, Physica A 369 (2006), 29–70.
- G. Gasper and M. Rahman, *Basic Hypergeometric Series*, 2nd ed., Cambridge University Press (2004).

# Proof of Conjecture 1 (`conj:e-23-e`) of Garrity–Osterman (`arXiv:2410.02032v2`)

**Result:** **TRUE.** Every $S(e, 23, e)$-adic language $\mathcal{L}$ (and each of its five conjugates and six twins) satisfies $p_{\mathcal{L}}(n) \le 3n$ for all $n \ge 1$.

---

## 1. Reduction to Extendable Double-Gauss Languages

1. **Conjugates and Twins:** By Propositions 18 and 19 (Section 7) of `arXiv:2410.02032v2` (`L1942`, `L1945`, `L1967`, `L1974`, and Section 12 Appendix item 4 at `L2889–2895`), every conjugate $\rho(\mathcal{L})$ and twin $R(\mathcal{L})$ of an $S(e, 23, e)$-adic language has the exact same factor complexity as an $S(e, 23, e)$-adic language. Thus it suffices to prove $p_{\mathcal{L}(\mathbf{\sigma})}(n) \le 3n$ for every coding sequence $\mathbf{\sigma} = (\sigma_0, \sigma_1, \dots) \in \{S_0, S_1\}^{\mathbb{N}}$, where
   $$S_0:\ 1 \mapsto 2,\ 2 \mapsto 13,\ 3 \mapsto 3; \qquad S_1:\ 1 \mapsto 1,\ 2 \mapsto 2,\ 3 \mapsto 13.$$

2. **Reduction to $(1, 1)$-tailed Double-Gauss Coding Sequences:** Fix any coding sequence $\mathbf{\sigma} = (\sigma_0, \sigma_1, \dots) \in \{S_0, S_1\}^{\mathbb{N}}$ and any length $n \ge 1$. Since every letter of $\mathcal{A}=\{1,2,3\}$ appears in $\bigcup_{c \in \mathcal{A}} \mathrm{Fac}(S_i(c))$ for $i \in \{0,1\}$, the finite factor sets $\bigcup_{c \in \mathcal{A}} \mathrm{Fac}((\sigma_0\circ\dots\circ\sigma_{N-1})(c))$ are non-decreasing in $N$. As $\mathcal{L}(\mathbf{\sigma})_n$ is finite (at most $3^n$ words), by Definition 12 (Section 4, `def:lang-coding-seq`, `L664`) there exists a single $N \ge 1$ such that every word in $\mathcal{L}(\mathbf{\sigma})_n$ is a factor of $(\sigma_0 \circ \dots \circ \sigma_{N-1})(c)$ for some $c \in \{1, 2, 3\}$. Set
   $$\mathbf{\sigma}' := (\sigma_0, \dots, \sigma_{N-1}, S_1, S_0, S_1, S_0, \dots).$$
   By Definition 12 applied to $\mathbf{\sigma}'$ at index $N$, $(\sigma_0 \circ \dots \circ \sigma_{N-1})(c) \in \mathcal{L}(\mathbf{\sigma}')$ for every $c \in \{1,2,3\}$, so $\mathcal{L}(\mathbf{\sigma})_n \subseteq \mathcal{L}(\mathbf{\sigma}')_n$ and $p_{\mathcal{L}(\mathbf{\sigma})}(n) \le p_{\mathcal{L}(\mathbf{\sigma}')}(n)$.

   Moreover, since $\mathbf{\sigma}'$ contains infinitely many $S_0$'s, grouping consecutive runs $G_k := S_1^k \circ S_0$ ($k \ge 0$) writes $\mathbf{\sigma}'$ uniquely as $(G_{k'_0}, G_{k'_1}, G_{k'_2}, \dots)$, and pairing them into $\tau_m := G_{j_m} \circ G_{k_m}$ yields $\mathbf{\sigma}' = (\tau_0, \tau_1, \tau_2, \dots)$ with $(j_m, k_m) \in \mathbb{Z}_{\ge 0}^2$ and $(j_m, k_m) = (1, 1)$ for all sufficiently large $m \ge M_0$. Explicitly, for any $j, k \ge 0$, $\tau_{j,k} := G_j \circ G_k$ acts by
   $$\tau_{j,k}:\quad 1 \mapsto 1^{j+1}3,\qquad 2 \mapsto 2^{k+1}1^j 3,\qquad 3 \mapsto 2^k 1^j 3,$$
   with abelianization matrix (acting on $\ell(v) := (|v|_1, |v|_2, |v|_3)^T \in \mathbb{Z}_{\ge 0}^3$)
   $$M_{j,k} = \begin{pmatrix} j+1 & j & j \\ 0 & k+1 & k \\ 1 & 1 & 1 \end{pmatrix}.$$
   For $\mathcal{L}^{(m)} := \mathcal{L}(\tau_m, \tau_{m+1}, \dots)$ ($m \ge 0$): since $(j_r, k_r) = (1, 1)$ for $r \ge M_0$, $M_{1,1}^2 > 0$ entrywise, so $\mathcal{L}^{(M_0)}$ is primitive, recurrent, and extendable with $|\mathcal{L}_1^{(M_0)}| = 3$; consequently every $\mathcal{L}^{(m)}$ ($0 \le m \le M_0$) is extendable with $|\mathcal{L}_1^{(m)}| = 3$ and $\mathcal{L}^{(m)} = \mathrm{Fac}\bigl(\tau_m(\mathcal{L}^{(m+1)})\bigr)$.

---

## 2. Unique Desubstitution and Extension-Set Maps (Proof of Section 10 Propositions)

Fix $m \ge 0$ and write $\tau = \tau_{j,k} = \tau_m$, $\mathcal{L} = \mathcal{L}^{(m)}$, and $\mathcal{L}' = \mathcal{L}^{(m+1)}$. Because $\mathcal{L}'$ is extendable, every $v \in \mathcal{L}'$ occurs with both a left neighbor and a right neighbor in $\mathcal{L}'$, and $E(v) = \{(c,d) \in \{1,2,3\}^2 : cvd \in \mathcal{L}'\}$ has $|E^-(v)|, |E^+(v)| \ge 1$.

**Proposition 1 (Antecedents and Bispecial Prefix/Suffix Form).** *Let $w \in \mathcal{L}$ contain at least one $3$.*
1. *There exist a unique $v \in \mathcal{L}'$, a nonempty suffix $a$ of $\tau(c)$ for some $c \in \{1,2,3\}$, and a proper prefix $b$ of $\tau(d)$ for some $d \in \{1,2,3\}$ such that $w = a\,\tau(v)\,b$.*
2. *If $w$ is left special in $\mathcal{L}$, then $a \in \{1^j 3,\; 2^k 1^j 3\}$ (with $a = 2^k 1^j 3$ possible only when $k \ge 1$).*
3. *If $w$ is right special in $\mathcal{L}$, then $b \in \{\varepsilon,\; 1^j\ (\text{if } k = 0),\; 2^k\ (\text{if } k \ge 1)\}$.*
4. *For any such $v, a, b$, defining the partial maps $\alpha^L_{a,k}, \alpha^R_{b,j,k} : \{1,2,3\} \to \{1,2,3, \varnothing\}$ by*
   $$\begin{array}{c|ccc}
   \alpha^L_{a,k} & a=1^j 3\ (k=0) & a=1^j 3\ (k\ge 1) & a=2^k 1^j 3\ (k\ge 1) \\ \hline
   1 & 1 & 1 & \varnothing \\
   2 & 2 & 2 & 2 \\
   3 & 3 & 2 & 3
   \end{array}$$
   $$\begin{array}{c|ccccccc}
   \alpha^R_{b,j,k} & \substack{j=0,k=0\\ b=\varepsilon} & \substack{j=0,k\ge 1\\ b=\varepsilon} & \substack{j=0,k\ge 1\\ b=2^k} & \substack{j\ge 1,k=0\\ b=\varepsilon} & \substack{j\ge 1,k=0\\ b=1^j} & \substack{j\ge 1,k\ge 1\\ b=\varepsilon} & \substack{j\ge 1,k\ge 1\\ b=2^k} \\ \hline
   1 & 1 & 1 & \varnothing & 1 & 1 & 1 & \varnothing \\
   2 & 2 & 2 & 2 & 2 & \varnothing & 2 & 2 \\
   3 & 3 & 2 & 3 & 1 & 3 & 2 & 1
   \end{array}$$
   *we have $E(w) = \{ (\alpha^L_{a,k}(c), \alpha^R_{b,j,k}(d)) : (c,d) \in E(v),\; \alpha^L_{a,k}(c) \neq \varnothing,\; \alpha^R_{b,j,k}(d) \neq \varnothing \}$.*

*Proof.*
1. Every $\tau(c)$ ($c \in \{1,2,3\}$) ends in $3$ and contains no other $3$. Hence the $3$'s in any $\tau(u)$ ($u \in \mathcal{L}'$) partition $\tau(u)$ into blocks $\tau(1) = 1^{j+1}3$, $\tau(2) = 2^{k+1}1^j 3$, $\tau(3) = 2^k 1^j 3$, which are pairwise distinct for all $j, k \ge 0$ (having counts $(|w|_1, |w|_2) = (j+1, 0), (j, k+1), (j, k)$). In $w$, let $a$ be the prefix up to and including the first $3$, and $b$ the suffix strictly after the last $3$; then the blocks strictly between the first and last $3$ decode uniquely to a word $v \in \mathcal{L}'$ with $w = a\,\tau(v)\,b$.
2. For $(x, y) \in \{1,2,3\}^2$, we have $x w y \in \mathcal{L}$ iff there exists $(c, d) \in E(v)$ such that $x a$ is a suffix of $\tau(c)$ (except when $a = \tau(c)$, where $x$ is the last letter of $\tau(c')$ for the preceding letter $c'$, namely $x = 3$!) and $b y$ is a prefix of $\tau(d)$ (when $b = \varepsilon$, $y$ is the first letter of $\tau(d)$). Checking every candidate nonempty suffix $a$ of $\tau(1), \tau(2), \tau(3)$:
   - If $a = 1^p 3$ with $0 \le p < j$, then in all three $\tau(c)$ ($c \in \{1,2,3\}$) $a$ is strictly shorter than $1^j 3$ and preceded only by $1$, so $|E^-(w)| = 1$.
   - If $a = 1^{j+1}3$, then $a = \tau(1)$ only, so $x = 3$ uniquely ($|E^-(w)| = 1$).
   - If $a = 2^p 1^j 3$ with $1 \le p < k$ ($k \ge 1$), then $a$ is strictly shorter than $2^k 1^j 3$ in $\tau(2)$ and $\tau(3)$ (and does not fit $\tau(1)$), so $x = 2$ uniquely ($|E^-(w)| = 1$).
   - If $a = 2^{k+1} 1^j 3$ ($k \ge 1$), then $a = \tau(2)$ only, so $x = 3$ uniquely ($|E^-(w)| = 1$).
   Thus only $a = 1^j 3$ and $a = 2^k 1^j 3$ ($k \ge 1$) can be left special.
3. Checking every proper prefix $b$ of $\tau(1), \tau(2), \tau(3)$:
   - If $k \ge 1$: for $b = 2^p$ ($1 \le p < k$), $b$ is followed only by $2$ in $\tau(2)$ and $\tau(3)$; for $b = 2^k 1^p$ ($1 \le p \le j$), $b$ is followed only by $1$ (if $p < j$) or $3$ (if $p = j$) in $\tau(2)$ and $\tau(3)$; for $b = 2^{k+1}1^p$ ($0 \le p \le j$), $b$ only fits $\tau(2)$; for $b = 1^p$ ($1 \le p \le j$), $b$ only fits $\tau(1)$. Thus only $b \in \{\varepsilon, 2^k\}$ can be right special.
   - If $k = 0$ and $j \ge 1$: for $b = 1^p$ ($1 \le p < j$), $b$ is followed only by $1$ in all three $\tau(c)$; for $b = 1^{j+1}$, $b$ only fits $\tau(1)$. Thus only $b \in \{\varepsilon, 1^j\}$ can be right special.
   - If $j = k = 0$: the only proper prefix is $b = \varepsilon$.
4. Direct inspection of the preceding/following letters in $\tau(1) = 1^{j+1}3$, $\tau(2) = 2^{k+1}1^j 3$, $\tau(3) = 2^k 1^j 3$ for each surviving $(a, b)$ gives the exact two tables above. (Notice $\alpha^L_{a,k}(c) = 3$ when $a = \tau(c)$ because every $\tau(c')$ ends in $3$ and $\mathcal{L}'$ is extendable.) $\square$

---

## 3. Age-0 ($3$-Free) Bispecial Words

**Lemma 2 ($3$-Free Bispecial Classification).** *In $\mathcal{L} = \mathcal{L}^{(m)}$ with $(j, k) = (j_m, k_m)$:*
1. *Every $3$-free word $w \in \mathcal{L} \setminus \{\varepsilon\}$ is of the form $1^r$ ($r \ge 1$), $2^r$ ($r \ge 1$), or $2^s 1^t$ ($s, t \ge 1$).*
2. *No $2^s 1^t$ ($s, t \ge 1$) is bispecial, and every bispecial $2^r$ ($r \ge 1$) is neutral ($m(2^r) = 0$).*
3. *For $w = 1^r$ ($r \ge 1$): if $j = 0$, $1^r$ is never bispecial; if $j \ge 1$, $1^r$ is neutral for $1 \le r < j$, non-bispecial for $r > j$, and for $r = j$ has:*
   - *If $k = 0$: $E(1^j) = \{(1,3),(2,3),(3,1),(3,3)\}$ ($3\times 2$, $m = 0$, since all three letters $1,2,3$ appear in every $\mathcal{L}^{(m)}$); if $k \ge 1$: $E(1^j) = E_{32}^- := \{(1,3),(2,3),(3,1)\}$ ($3\times 2$, $m = -1$).*
4. *For $w = \varepsilon$, $E(\varepsilon) = \mathcal{L}_2$ equals:*
   - $E_{33}^A := \{(1,3),(2,3),(3,1),(3,2),(3,3)\}$ ($m = 0$) if $j = k = 0$;
   - $E_{33}^B := \{(1,3),(2,2),(2,3),(3,1),(3,2)\}$ ($m = 0$) if $j = 0, k \ge 1$;
   - $E_{33}^C := \{(1,1),(1,3),(2,1),(3,1),(3,2)\}$ ($m = 0$) if $j \ge 1, k = 0$;
   - $E_{33}^+ := \{(1,1),(1,3),(2,1),(2,2),(3,1),(3,2)\}$ ($m = +1$) if $j \ge 1, k \ge 1$.

*Proof.* Since all three letters $1, 2, 3$ appear in $\mathcal{L}^{(M_0)}$ and every $\tau_{j',k'}(1)$ contains $1,3$ while $\tau_{j',k'}(2)$ contains $2$, all three letters $1,2,3$ appear in every $\mathcal{L}^{(m)}$ (and infinitely often, since $M_{1,1}^2 > 0$ in $\mathcal{L}^{(M_0)}$). Between consecutive $3$'s in $\tau(\mathcal{L}')$, only $1^{j+1}$, $2^{k+1}1^j$, and $2^k 1^j$ occur (immediately preceded and followed by $3$), proving (1) and giving $E(\varepsilon)$ directly in (4):
- Intra-block pairs: $13$ (always); $11$ (iff $j \ge 1$); $22$ (iff $k \ge 1$); $21$ (iff $j \ge 1$); $23$ (iff $j = 0$).
- Cross-block pairs (after $3$): $31$ (from $\tau(1)$, always), $32$ (from $\tau(2)$, always), $33$ (from $\tau(3)$ iff $j = k = 0$; otherwise $\tau(3)$ begins with $2$ if $k \ge 1$ or $1$ if $k=0, j\ge 1$).
(In particular, for $j \ge 1, k=0$, $\tau(2)=21^j 3$ contributes intra-block $(2,1)$ to $E_{33}^C$; for $j=0, k=0$, $\tau(2)=23$ contributes $(2,3)$ to $E_{33}^A$; for $j=0, k\ge 1$, $\tau(2)=2^{k+1}3$ contributes $22, 23$ to $E_{33}^B$; and for $j,k \ge 1$, $\tau(2)=2^{k+1}1^j 3$ contributes $22, 21, 11, 13$ to $E_{33}^+$.)
For (2): $2^s 1^t$ ($s,t \ge 1$) only occurs inside $2^{k+1}1^j 3$ or $2^k 1^j 3$, where every occurrence with $t < j$ is followed only by $1$ and every occurrence with $t = j$ is followed only by $3$, so $|E^+(2^s 1^t)| = 1$. For $2^r$ ($1 \le r \le k$ when $k \ge 1$): if $r < k$, its occurrences in $\tau(2) = 2^{k+1}1^j 3$ and $\tau(3) = 2^k 1^j 3$ give $E(2^r) = \{(3,2), (2,2), (2,y)\}$ where $y = 1$ ($j \ge 1$) or $3$ ($j = 0$); if $r = k$, $E(2^k) = \{(3,2), (2,y), (3,y)\}$; in both cases $|E| = 3, |E^-|=2, |E^+|=2$, so $m(2^r) = 0$. For $r = k+1$, $2^{k+1}$ only occurs in $\tau(2)$, giving $|E^-|=|E^+|=1$.
For (3): if $j = 0$, $1$ only occurs at the end of $13$, so $E^+(1) = \{3\}$. If $j \ge 1$: for $1 \le r < j$, every occurrence in $\tau(1)=1^{j+1}3$, $\tau(2)=2^{k+1}1^j 3$, and $\tau(3)=2^k 1^j 3$ (with $k \ge 0$) gives $E(1^r) = \{(1,1),(1,3),(2,1),(3,1)\}$ (which has $|E|=4, |E^-|=3, |E^+|=2, m = 0$); for $r > j$, $1^{j+1}$ only occurs in $\tau(1)$, not bispecial; and for $r = j$, its occurrences in $\tau(1) = 1^{j+1}3$ (giving $(3,1), (1,3)$), $\tau(2) = 2^{k+1}1^j 3$ (giving $(2,3)$), and $\tau(3) = 2^k 1^j 3$ (giving $(2,3)$ if $k \ge 1$, or $(3,3)$ if $k = 0$) yield $E(1^j) = \{(1,3),(2,3),(3,1),(3,3)\}$ ($m=0$) if $k = 0$ and $E_{32}^- = \{(1,3),(2,3),(3,1)\}$ ($m = -1$) if $k \ge 1$. $\square$

---

## 4. Exact Finite-State Bispecial Structure and Proof of $p_{\mathcal{L}}(n) \le 3n$

Define the following ten non-$E_{33}^A$ extension sets:
- **Root ($3\times 3$):** $E_{33}^+, E_{33}^B, E_{33}^C$ (from Lemma 2.4).
- **$3\times 2$:** $E_{32}^+ := \{(1,1),(2,1),(2,2),(3,1),(3,2)\}$ ($m = +1$), $E_{32}^- := \{(1,3),(2,3),(3,1)\}$ ($m = -1$).
- **$2\times 2$:** $A^+ := \{(1,1),(1,2),(2,1),(2,2)\}$ ($m = +1$), $B^+ := \{(2,1),(2,2),(3,1),(3,2)\}$ ($m = +1$), $A_1^- := \{(1,1),(2,2)\}$ ($m = -1$), $A_2^- := \{(1,3),(2,2)\}$ ($m = -1$), $B^- := \{(2,2),(3,1)\}$ ($m = -1$).

Let $\mathcal{N}_0 := \{N_0, N_1, \dots, N_{12}\}$ be the $13$-element neutral collection consisting of $N_0 := E_{33}^A$, the $9$ sets of size $3$ in $2\times 2$, and the $3$ neutral sets in $3\times 2$:
$$\begin{aligned}
N_0 &= \{(1,3),(2,3),(3,1),(3,2),(3,3)\} = E_{33}^A, & N_1 &= \{(1,1),(1,2),(2,1)\}, & N_2 &= \{(1,1),(2,1),(2,2)\}, \\
N_3 &= \{(1,2),(2,1),(2,2)\}, & N_4 &= \{(1,3),(2,2),(2,3)\}, & N_5 &= \{(2,1),(2,2),(3,2)\}, \\
N_6 &= \{(2,1),(3,1),(3,2)\}, & N_7 &= \{(2,2),(2,3),(3,2)\}, & N_8 &= \{(2,2),(3,1),(3,2)\}, \\
N_9 &= \{(2,3),(3,2),(3,3)\}, & N_{10} &= \{(1,1),(1,3),(2,1),(3,1)\}, & N_{11} &= \{(1,1),(2,1),(3,1),(3,2)\}, \\
N_{12} &= \{(1,3),(2,3),(3,1),(3,3)\}.
\end{aligned}$$
(Note that every age-$0$ neutral bispecial set of Lemma 2 lies in $\mathcal{N}_0$: $E_{33}^A = N_0$, $E(2^r) \in \{N_5, N_6, N_7, N_9\}$, $E(1^r) = N_{10}$ for $1 \le r < j$, and $E(1^j) = N_{12}$ when $j \ge 1, k = 0$.)

**Lemma 3 (Closure of Neutral Sets).** *Under Proposition 1.4 for all four parameter modes $(j>0, k>0) \in \{0,1\}^2$, every bispecial extended image of any set in $\mathcal{N}_0$ is again neutral and belongs to $\mathcal{N}_0$.*

*Proof.* Direct finite evaluation of $(\alpha^L_{a,k}, \alpha^R_{b,j,k})$ across the four modes $(j>0, k>0) \in \{0,1\}^2$ gives the complete list of bispecial extended images (every set satisfies $m=0$ and stays in $\mathcal{N}_0$; non-bispecial images are omitted):
$$\begin{array}{c|cccc}
\text{Set} & (0,0) & (0,1) & (1,0) & (1,1) \\ \hline
N_0 & N_0 & N_3, N_4, N_8, N_9 & N_{11}, N_{12} & N_3, N_2, N_8, N_6 \\
N_1,\; N_2,\; N_3,\; N_5,\; N_6,\; N_8 & N_i & N_i & N_i & N_i\ (\text{fixed}) \\
N_4 & N_4 & N_4 & N_2 & N_2 \\
N_7 & N_7 & N_7 & N_5 & N_5 \\
N_9 & N_9 & N_9 & N_6 & N_6 \\
N_{10} & N_{10} & N_1 & N_{10} & N_1 \\
N_{11} & N_{11} & N_2, N_6 & N_{11} & N_2, N_6 \\
N_{12} & N_{12} & N_3, N_8 & N_{12} & N_3, N_8
\end{array}$$
(Every entry is verified directly from Proposition 1.4.) $\square$

**Theorem 4 (Alternating Non-Neutral Sequence & Componentwise Monotonicity).** *For every $m \ge 0$ (starting from $M_0$ down to $0$), let $t_m \ge 0$ be the unique integer such that $(j_m, k_m) = \cdots = (j_{m+t_m-1}, k_{m+t_m-1}) = (0,0)$ and $(j_{m+t_m}, k_{m+t_m}) \neq (0,0)$ (well-defined since $(j_r, k_r) = (1,1)$ for $r \ge M_0$). Then $\mathcal{L}^{(m)}$ admits an infinite sequence of pairwise distinct bispecial words*
$$w_0^+, w_0^-, w_1^+, w_1^-, w_2^+, w_2^-, \dots$$
*(except possibly $w_0^+ = w_0^-$ when both have $m=0$) containing every non-neutral bispecial word of $\mathcal{L}^{(m)}$, where $(w_0^+, w_0^-)$ is given by:*
- *$w_0^+ = \varepsilon$ ($E_{33}^+, m=+1$) and $w_0^- = 1^{j_m}$ ($E_{32}^-, m=-1$) when $j_m, k_m \ge 1$ ($t_m = 0$);*
- *$w_0^+ = w_0^- = \varepsilon$ ($E_{33}^A, m=0$) when $t_m \ge 1$ and $j_{m+t_m}, k_{m+t_m} \ge 1$ (and here $w_1^+ = 3^{t_m}, w_1^- = 3^{t_m}(13^{t_m})^{j_{m+t_m}}$ with $(E_{33}^+, E_{32}^-)$, since the $t_m$-fold iterate of $v \mapsto 3\tau_{0,0}(v)$ maps $\varepsilon \mapsto 3^{t_m}$ and $1^j \mapsto 3^{t_m}(13^{t_m})^j$);*
- *$w_0^+ = w_0^- = 3^{t_m}$ ($m=0$, with $E(3^{t_m}) = E_{33}^B$ if $j_{m+t_m}=0, k_{m+t_m} \ge 1$, or $E_{33}^C$ if $j_{m+t_m} \ge 1, k_{m+t_m} = 0$) otherwise,*

*such that:*
1. *For every $r \ge 1$, $m(w_r^+) = +1$ and $m(w_r^-) = -1$; for $r = 0$, $(m(w_0^+), m(w_0^-)) = (+1, -1)$ if $j_m, k_m \ge 1$ and $(0, 0)$ otherwise.*
2. *Every bispecial word of $\mathcal{L}^{(m)}$ not appearing in $(w_r^+, w_r^-)_{r \ge 0}$ has extension set in $\mathcal{N}_0$ (hence is neutral).*
3. *Every pair $(E(w_r^+), E(w_r^-))$ for $r \ge 1$ lies in $\{(E_{33}^+, E_{32}^-),\; (E_{32}^+, E_{32}^-),\; (A^+, A_1^-),\; (A^+, A_2^-),\; (B^+, B^-)\}$, and every consecutive transition $(E(w_r^-), E(w_{r+1}^+))$ ($r \ge 1$) lies in $\mathcal{T}_{\ge 1} := \{(E_{32}^-, A^+),\; (A_1^-, B^+),\; (A_2^-, B^+),\; (B^-, A^+)\}$. For $r = 0$, $(E(w_0^-), E(w_1^+))$ lies in $\{(E_{33}^A, E_{33}^+),\; (E_{33}^B, A^+),\; (E_{33}^C, E_{32}^+),\; (E_{32}^-, A^+)\}$ (specifically $(E_{32}^-, A^+)$ whenever $j_m, k_m \ge 1$).*
4. *Componentwise abelianization monotonicity:* For all $r \ge 0$,
   $$\ell(w_r^-) \ge \ell(w_r^+) \qquad \text{and} \qquad \ell(w_{r+1}^+) \ge \ell(w_r^-),$$
   *with $\ell(w_1^+) - \ell(w_0^-) \ge (0,0,1)^T$ whenever $m(w_0^-) = 0$ and $E(w_0^-) \in \{E_{33}^B, E_{33}^C\}$, and whenever $(E(w_r^-), E(w_{r+1}^+)) \in \{(E_{32}^-, A^+),\; (B^-, A^+)\}$ ($r \ge 0$), we have*
   $$\bigl(\ell(w_{r+1}^+) - \ell(w_r^-)\bigr)_2 + \bigl(\ell(w_{r+1}^+) - \ell(w_r^-)\bigr)_3 \ge 1.$$

*Proof.* Note first that in every $\mathcal{L}^{(m)}$ below, age-$0$ words contain no $3$ while every extended image $a\tau(v)b$ from Proposition 1 contains at least one $3$, and distinct triples $(a, v, b)$ yield distinct words $a\tau(v)b$ by unique desubstitution (Proposition 1.1). Hence if the sequence in $\mathcal{L}'$ has pairwise distinct non-neutral terms, so does its lift in $\mathcal{L}$.

**Base Case ($\mathcal{L}^{(M_0)}$, where $(j_r, k_r) = (1, 1)$ for all $r \ge M_0$):**
Here $\tau = \tau_{1,1}$ is a fixed substitution with $\mathcal{L}^{(M_0)} = \mathrm{Fac}(\tau(\mathcal{L}^{(M_0)}))$ and $t_{M_0} = 0$. By Lemma 2, the $3$-free bispecials are $w_0^+ = \varepsilon$ ($E_{33}^+, m=+1$), $w_0^- = 1$ ($E_{32}^-, m=-1$), and neutral $2$ ($\in \mathcal{N}_0$). Here $\ell(w_0^-) - \ell(w_0^+) = (1,0,0)^T \ge 0$. Applying Proposition 1.4 with $(j,k)=(1,1)$ recursively by age:
- $w_0^+ = \varepsilon$ ($E_{33}^+$) lifts to $w_1^+ = 13$ ($A^+, m=+1$), $w_1^- = 132$ ($A_1^-, m=-1$), and $w_2^+ = 213$ ($B^+, m=+1$);
- $w_0^- = 1$ ($E_{32}^-$) lifts to $w_2^- = 213113$ ($B^-, m=-1$) (note $a=13$ gives neutral $N_3 \in \mathcal{N}_0$);
- for $r \ge 1$, each $(A^+, A_1^-)$ lifts uniquely to $(A^+, A_1^-)$, and each $(B^+, B^-)$ lifts uniquely to $(B^+, B^-)$, while $B^- \to A^+$ lifts to $B^- \to A^+$ (and $A_1^- \to B^+$ to $A_1^- \to B^+$).
Direct calculation for the initial segments gives $(E(w_0^-), E(w_1^+)) = (E_{32}^-, A^+)$ with $\ell(13)-\ell(1) = (0,0,1)^T$ ($\Delta_2+\Delta_3 = 1$), $\ell(132)-\ell(13) = (0,1,0)^T$, $\ell(213)-\ell(132) = (0,0,0)^T$, $\ell(213113)-\ell(213) = (2,0,1)^T$, and $\ell(13113213)-\ell(213113) = (1,0,1)^T$ ($\Delta_2+\Delta_3 = 1$). Since $M_{1,1} \ge 0$ and the inductive lifting rules below apply verbatim, (1)–(4) hold for all ages in $\mathcal{L}^{(M_0)}$.

**Inductive Step ($\mathcal{L}^{(m+1)} \to \mathcal{L}^{(m)}$ under $(j, k) := (j_m, k_m)$):**
Write $\mathcal{L}' = \mathcal{L}^{(m+1)}$, $\mathcal{L} = \mathcal{L}^{(m)}$, and $(v_r^+, v_r^-)_{r \ge 0}$ for the sequence of $\mathcal{L}'$. By Lemma 2 and Proposition 1, every bispecial word of $\mathcal{L}$ is either age $0$ (namely: $(\varepsilon, 1^j)$ when $j, k \ge 1$; $\varepsilon$ with $E(\varepsilon) \in \{E_{33}^A, E_{33}^B, E_{33}^C\}$ when $j=0$ or $k=0$; plus neutral $1^r, 2^r \in \mathcal{N}_0$) or an extended image $a\,\tau(v)\,b$ of a bispecial word $v \in \mathcal{L}'$ — either in $(v_r^\pm)_{r \ge 0}$ or outside it (hence in $\mathcal{N}_0$ by inductive hypothesis (2), producing only neutral images in $\mathcal{N}_0$ by Lemma 3).

First suppose $(j, k) = (0, 0)$, so $t_m = t_{m+1} + 1 \ge 1$ and
$$M_{0,0} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 1 & 1 & 1 \end{pmatrix}.$$
Notice that for any $\delta = (\delta_1,\delta_2,\delta_3)^T \ge 0$, $M_{0,0}\delta = (\delta_1,\delta_2,\delta_1+\delta_2+\delta_3)^T \ge 0$ preserves $\delta \ge 0$, preserves $\delta \ge (0,0,1)^T$, and preserves $\delta_2+\delta_3 \ge 1$ (since $(M_{0,0}\delta)_2+(M_{0,0}\delta)_3 = \delta_1+2\delta_2+\delta_3 \ge \delta_2+\delta_3 \ge 1$). Under $(0,0)$, age $0$ gives $\varepsilon$ with $E(\varepsilon) = E_{33}^A \in \mathcal{N}_0$, and Proposition 1.4 has unique $(a,b) = (3, \varepsilon)$ with $\alpha^L_{3,0} = \alpha^R_{\varepsilon,0,0} = \mathrm{id}$, so $v \mapsto 3\tau_{0,0}(v)$ maps every bispecial word $v \in \mathcal{L}'$ bijectively to $3\tau_{0,0}(v)$ with $E(3\tau_{0,0}(v)) = E_{\mathcal{L}'}(v)$ (and in particular $3\tau_{0,0}(1^j) = 3(13)^j$, $3\tau_{0,0}(3^t(13^t)^j) = 3^{t+1}(13^{t+1})^j$, $3\tau_{0,0}(3^t) = 3^{t+1}$):
- If $E_{\mathcal{L}'}(v_0^+) = E_{33}^+$ ($t_{m+1} = 0$, $v_0^+ = \varepsilon$, $v_0^- = 1^{j_{m+1}}$): $w_0^\pm := \varepsilon$ ($E_{33}^A \in \mathcal{N}_0$), $w_1^+ := 3$ ($E_{33}^+$), $w_1^- := 3(13)^{j_{m+1}}$ ($E_{32}^-$), and $w_r^\pm := 3\tau_{0,0}(v_{r-1}^\pm)$ for $r \ge 2$. Then $(E(w_0^-), E(w_1^+)) = (E_{33}^A, E_{33}^+)$, $\ell(w_1^+) - \ell(\varepsilon) = (0,0,1)^T \ge 0$, $\ell(w_1^-) - \ell(w_1^+) = (j_{m+1}, 0, j_{m+1})^T = M_{0,0}(j_{m+1},0,0)^T \ge 0$, and $\ell(w_2^+) - \ell(w_1^-) = \bigl((0,0,1)^T + M_{0,0}\ell(v_1^+)\bigr) - \bigl((0,0,1)^T + M_{0,0}\ell(v_0^-)\bigr) = M_{0,0}(\ell(v_1^+) - \ell(v_0^-))$ (preserving $\ge 0$ and $\Delta_2+\Delta_3 \ge 1$), while $M_{0,0}$ preserves all tail gaps $M_{0,0}(\ell(v_{r+1}^+)-\ell(v_r^-))$ and $M_{0,0}(\ell(v_r^-)-\ell(v_r^+))$.
- If $v_0^\pm = \varepsilon$ with $E(\varepsilon) = E_{33}^A$ ($t_{m+1} \ge 1$, $j_{m+1+t_{m+1}}, k_{m+1+t_{m+1}} \ge 1$): $w_0^\pm := \varepsilon$ ($E_{33}^A$), $3 = 3\tau_{0,0}(\varepsilon)$ also has $E_{33}^A \in \mathcal{N}_0$, and $w_r^\pm := 3\tau_{0,0}(v_r^\pm)$ for $r \ge 1$ (so $w_1^+ = 3^{t_m}, w_1^- = 3^{t_m}(13^{t_m})^{j_{m+t_m}}$ with $(E_{33}^+, E_{32}^-)$, $(E(w_0^-), E(w_1^+)) = (E_{33}^A, E_{33}^+)$, and all gaps mapped by $M_{0,0}$ preserve (4)).
- If $v_0^\pm = 3^{t_{m+1}}$ with $E(3^{t_{m+1}}) \in \{E_{33}^B, E_{33}^C\}$: $w_0^\pm := 3^{t_m} = 3\tau_{0,0}(3^{t_{m+1}})$ has $E(w_0^\pm) = E(v_0^\pm) \in \{E_{33}^B, E_{33}^C\}$ (and for $t_{m+1} \ge 1$, $\varepsilon$ also lifts to $3$ with $E(3) = E_{33}^A \in \mathcal{N}_0$), while $w_r^\pm := 3\tau_{0,0}(v_r^\pm)$ for $r \ge 1$, giving $\ell(w_1^+) - \ell(3^{t_m}) = M_{0,0}(\ell(v_1^+) - \ell(3^{t_{m+1}})) \ge (0,0,1)^T$ and preserving (1)–(4).

Now suppose $(j, k) \neq (0, 0)$, so $t_m = 0$. Let us check how every tail pair $(v_r^+, v_r^-)$ ($r \ge 1$) lifts under Proposition 1.4:
- **$(A^+, A_1^-)$ or $(A^+, A_2^-)$:** Both have $E^- = \{1,2\}$, so both receive the unique prefix $a = 1^j 3$. For $A^+$ ($E^+=\{1,2\}$), only $b = \varepsilon$ remains right special, giving $A^+$. For $A_1^-$ ($E^+=\{1,2\}$), only $b = \varepsilon$ remains right special, giving $A_1^-$. For $A_2^-$ ($E^+=\{2,3\}$), if $k = 0$ (hence $j \ge 1$, as $(j,k)\neq(0,0)$), then $\alpha^R_{\varepsilon, j, 0}(3)=1$, so $b = \varepsilon$ gives $A_1^-$ (while $b = 1^j$ maps $2 \mapsto \varnothing$, non-bispecial); if $k \ge 1$ then $b = \varepsilon$ collapses $E^+$ to $\{2\}$ while $b = 2^k$ gives $A_1^-$ (when $j \ge 1$) or $A_2^-$ (when $j = 0$). Thus $b(w_r^+) = \varepsilon$ and $b(w_r^-) \in \{\varepsilon, 2^k\}$, so $\ell(w_r^-) - \ell(w_r^+) \ge M_{j,k}(\ell(v_r^-) - \ell(v_r^+)) \ge 0$.
- **$(B^+, B^-)$:** Both have $E^- = \{2,3\}$ and $E^+ = \{1,2\}$, so both receive the same $(a, b) = (1^j 3, \varepsilon)$ (if $k=0$) or $(2^k 1^j 3, \varepsilon)$ (if $k \ge 1$), giving $(B^+, B^-)$ with $\ell(w_r^-) - \ell(w_r^+) = M_{j,k}(\ell(v_r^-) - \ell(v_r^+)) \ge 0$.
- **$(E_{32}^+, E_{32}^-)$:** If $k = 0$ (so $j \ge 1$): $E_{32}^+$ receives $a = 1^j 3, b = \varepsilon$ (giving $E_{32}^+$; $b = 1^j$ collapses $E^+$ to $\{1\}$) and $E_{32}^-$ receives $a = 1^j 3, b = 1^j$ (giving $E_{32}^-$, whereas $b=\varepsilon$ collapses $E^+$ to $\{1\}$), with $\ell(b(w_r^-)) = (j,0,0)^T \ge 0$. If $k \ge 1$: for $E_{32}^+$, $a = 1^j 3, b = \varepsilon$ gives neutral $N_2 \in \mathcal{N}_0$ and $a = 2^k 1^j 3, b = \varepsilon$ gives $B^+$; for $E_{32}^-$, $a = 1^j 3, b = \varepsilon$ gives neutral $N_3 \in \mathcal{N}_0$ and $a = 2^k 1^j 3, b = \varepsilon$ gives $B^-$. Both receive $(2^k 1^j 3, \varepsilon)$, preserving $\ell(w_r^-) - \ell(w_r^+) \ge 0$.
- **$(E_{33}^+, E_{32}^-)$ (which occurs at $r=1$ when $t_{m+1} \ge 1$ and $v_1^+ = 3^{t_{m+1}}$, or at $r=0$ when $j_{m+1}, k_{m+1} \ge 1$):**
  - If $j \ge 1, k = 0$: $E_{33}^+$ lifts to $1^j 3 \tau(v_r^+)$ ($E_{32}^+, m=+1$) and neutral $1^j 3 \tau(v_r^+) 1^j$ ($N_{10} \in \mathcal{N}_0$), while $E_{32}^-$ lifts to $1^j 3 \tau(v_r^-) 1^j$ ($E_{32}^-, m=-1$). Note $\ell(1^j 3\tau(v_r^+)) \ge (0,0,1)^T$ and $\ell(w_r^-)-\ell(w_r^+) = M_{j,0}(\ell(v_r^-)-\ell(v_r^+)) + (j,0,0)^T \ge 0$.
  - If $k \ge 1$: $E_{33}^+$ splits into $u_1 = 1^j 3 \tau(v_r^+)$ ($A^+, m=+1$), $u_2 = 1^j 3 \tau(v_r^+) 2^k$ ($A_1^-$ if $j \ge 1$, $A_2^-$ if $j = 0$, $m=-1$), and $u_3 = 2^k 1^j 3 \tau(v_r^+)$ ($B^+, m=+1$), while $E_{32}^-$ lifts to $u_4 = 2^k 1^j 3 \tau(v_r^-)$ ($B^-, m=-1$). Here $\ell(u_2) - \ell(u_1) = (0,k,0)^T \ge 0$, $\ell(u_3) - \ell(u_2) = (0,0,0)^T \ge 0$, $\ell(u_4) - \ell(u_3) = M_{j,k}(\ell(v_r^-) - \ell(v_r^+)) \ge 0$, and $(E(u_2), E(u_3)) \in \{(A_1^-, B^+), (A_2^-, B^+)\} \subset \mathcal{T}_{\ge 1}$.

Next check every consecutive gap $(v_r^-, v_{r+1}^+) \in \mathcal{T}_{\ge 1}$ ($r \ge 1$, and also $r = 0$ when $j_{m+1}, k_{m+1} \ge 1$, where $(E(v_0^-), E(v_1^+)) = (E_{32}^-, A^+) \in \mathcal{T}_{\ge 1}$) and set $\Delta := \ell(w_{r+1}^+) - \ell(w_r^-)$:
- $(A_1^-, B^+)$: $w_r^-$ receives $(1^j 3, \varepsilon)$, while $w_{r+1}^+$ receives $(1^j 3, \varepsilon)$ ($k=0$) or $(2^k 1^j 3, \varepsilon)$ ($k\ge 1$), giving lifted transition $(A_1^-, B^+) \in \mathcal{T}_{\ge 1}$ and $\Delta \ge M_{j,k}(\ell(v_{r+1}^+) - \ell(v_r^-)) \ge 0$.
- $(A_2^-, B^+)$: $w_r^-$ receives $(1^j 3, \varepsilon)$ ($j \ge 1, k=0$) or $(1^j 3, 2^k)$ ($k \ge 1$), while $w_{r+1}^+$ receives $(1^j 3, \varepsilon)$ ($k=0$) or $(2^k 1^j 3, \varepsilon)$ ($k \ge 1$). In both cases the $(a,b)$ abelianization difference is $(0,0,0)^T$, giving lifted transition $(A_1^-, B^+)$ ($j \ge 1$) or $(A_2^-, B^+)$ ($j=0$) in $\mathcal{T}_{\ge 1}$ and $\Delta = M_{j,k}(\ell(v_{r+1}^+) - \ell(v_r^-)) \ge 0$.
- $(E_{32}^-, A^+)$ or $(B^-, A^+)$: Let $\delta := \ell(v_{r+1}^+) - \ell(v_r^-)$. By the induction hypothesis, $\delta \ge (0,0,0)^T$ and $\delta_2 + \delta_3 \ge 1$. Under $(j, k)$, $w_r^-$ ($B^-$ or $E_{32}^-$) receives prefix $2^k 1^j 3$ (if $k \ge 1$) or $1^j 3$ (if $k=0$) and suffix $b = 1^j$ (when $k=0, j \ge 1$ and $v_r^- \in E_{32}^-$) or $b = \varepsilon$ (otherwise):
  - If $k = 0$ ($j \ge 1$): $w_r^-$ receives $(1^j 3, \varepsilon)$ (for $B^-$) or $(1^j 3, 1^j)$ (for $E_{32}^-$), while $w_{r+1}^+$ ($A^+$) receives $(1^j 3, \varepsilon)$. When $v_r^- \in E_{32}^-$, $(M_{j,0}\delta)_1 = (j+1)\delta_1 + j(\delta_2 + \delta_3) \ge j$ because $\delta_2 + \delta_3 \ge 1$; subtracting $\ell(1^j) = (j,0,0)^T$ leaves $\Delta_1 \ge 0$, $\Delta_2 = \delta_2 \ge 0$, $\Delta_3 = \delta_1 + \delta_2 + \delta_3 \ge 1$! The lifted transition is $(E_{32}^-, A^+)$ or $(B^-, A^+)$ in $\mathcal{T}_{\ge 1}$ and $\Delta_2 + \Delta_3 \ge 1$.
  - If $k \ge 1$: $w_r^-$ ($B^-$ or $E_{32}^-$) receives $(2^k 1^j 3, \varepsilon)$, while $w_{r+1}^+$ ($A^+$) receives $(1^j 3, \varepsilon)$, shifting by $(0, -k, 0)^T$. Since $\delta_2 + \delta_3 \ge 1$,
    $$\Delta_2 = (k+1)\delta_2 + k\delta_3 - k = k(\delta_2 + \delta_3 - 1) + \delta_2 \ge 0,$$
    $$\Delta_1 = (j+1)\delta_1 + j(\delta_2 + \delta_3) \ge 0, \qquad \Delta_3 = \delta_1 + \delta_2 + \delta_3 \ge 1,$$
    so $\Delta \ge 0$, the lifted transition $(w_r^-, w_{r+1}^+)$ is $(B^-, A^+) \in \mathcal{T}_{\ge 1}$, and $\Delta_2 + \Delta_3 \ge 1$!

Finally, check the $r=0$ head transitions (still with $(j, k) \neq (0,0)$):
- **$j_{m+1}, k_{m+1} \ge 1$ ($t_{m+1}=0$, $v_0^+ = \varepsilon$ has $E_{33}^+$, $v_0^- = 1^{j_{m+1}}$ has $E_{32}^-$):** $v_0^+$ lifts via the $(E_{33}^+, E_{32}^-)$ rule above, so:
  - If $j=0, k \ge 1$: $w_0^\pm = \varepsilon$ ($E_{33}^B$) and $w_1^+ = 3$ ($A^+$), giving $(E(w_0^-), E(w_1^+)) = (E_{33}^B, A^+)$ and $\ell(w_1^+) - \ell(\varepsilon) = (0,0,1)^T \ge 0$.
  - If $j \ge 1, k = 0$: $w_0^\pm = \varepsilon$ ($E_{33}^C$) and $w_1^+ = 1^j 3$ ($E_{32}^+$), giving $(E(w_0^-), E(w_1^+)) = (E_{33}^C, E_{32}^+)$ and $\ell(w_1^+) - \ell(\varepsilon) = (j,0,1)^T \ge (0,0,1)^T$.
  - If $j, k \ge 1$: $w_0^+ = \varepsilon$ ($E_{33}^+$), $w_0^- = 1^j$ ($E_{32}^-$), and $w_1^+ = 1^j 3$ ($A^+$), giving $(E(w_0^-), E(w_1^+)) = (E_{32}^-, A^+)$ and $\ell(w_1^+) - \ell(w_0^-) = (0,0,1)^T \ge 0$ with $\Delta_2 + \Delta_3 = 1$!
- **$E(v_0^\pm) = E_{33}^A$ ($t_{m+1} \ge 1$ and $j_{m+1+t_{m+1}}, k_{m+1+t_{m+1}} \ge 1$, so $v_0^\pm = \varepsilon$ and $v_1^+ = 3^{t_{m+1}}$ with $E(v_1^+) = E_{33}^+$):** Since $E_{33}^A \in \mathcal{N}_0$, $\varepsilon$ produces only neutral images in $\mathcal{N}_0$, while $v_1^+ = 3^{t_{m+1}}$ lifts by the $(E_{33}^+, E_{32}^-)$ rule above, giving $w_1^+ = 3\tau_{0,k}(3^{t_{m+1}})$ ($A^+$, if $j=0, k \ge 1$), $w_1^+ = 1^j 3 \tau_{j,0}(3^{t_{m+1}})$ ($E_{32}^+$, if $j \ge 1, k=0$), or $w_1^+ = 1^j 3 \tau_{j,k}(3^{t_{m+1}})$ ($A^+$, if $j,k \ge 1$ with $\ell(w_1^+)-\ell(1^j) = M_{j,k}(0,0,t_{m+1})^T + (0,0,1)^T \ge (0,0,1)^T$, $\Delta_2+\Delta_3 \ge 1$).
- **$v_0^\pm = 3^{t_{m+1}}$ with $E(3^{t_{m+1}}) = E_{33}^B$ ($t_{m+1} \ge 0$, and by inductive hypothesis (3)–(4), $E(v_1^+) = A^+$ and $\delta := \ell(v_1^+) - \ell(3^{t_{m+1}}) \ge (0,0,1)^T$):**
  - If $k \ge 1$: $E_{33}^B$ produces only neutral images in $\mathcal{N}_0$, while $v_1^+$ ($A^+$) lifts to $w_1^+ = 1^j 3 \tau_{j,k}(v_1^+)$ ($A^+$). For $j=0$: $w_0^\pm = \varepsilon$ ($E_{33}^B$), $(E(w_0^-), E(w_1^+)) = (E_{33}^B, A^+)$, and $\ell(w_1^+) \ge (0,0,1)^T$. For $j \ge 1$: $w_0^+ = \varepsilon$ ($E_{33}^+$), $w_0^- = 1^j$ ($E_{32}^-$), $(E(w_0^-), E(w_1^+)) = (E_{32}^-, A^+)$, and $\ell(w_1^+) - \ell(1^j) = (0,0,1)^T + M_{j,k}\ell(v_1^+) \ge (0,0,2)^T$ ($\Delta_2+\Delta_3 \ge 2$).
  - If $j \ge 1, k = 0$: $w_0^\pm = \varepsilon$ ($E_{33}^C$), $v_0^\pm = 3^{t_{m+1}}$ splits into $w_1^+ = 1^j 3 \tau_{j,0}(3^{t_{m+1}})$ ($E_{32}^+$) and $w_1^- = 1^j 3 \tau_{j,0}(3^{t_{m+1}}) 1^j$ ($E_{32}^-$), followed by $w_2^+ = 1^j 3 \tau_{j,0}(v_1^+)$ ($A^+$). Here $(E(w_0^-), E(w_1^+)) = (E_{33}^C, E_{32}^+)$, $(E(w_1^-), E(w_2^+)) = (E_{32}^-, A^+) \in \mathcal{T}_{\ge 1}$, $\ell(w_1^+) \ge (0,0,1)^T$, $\ell(w_1^-)-\ell(w_1^+) = (j,0,0)^T \ge 0$, and $\ell(w_2^+) - \ell(w_1^-) = M_{j,0}\delta - (j,0,0)^T \ge (0,0,1)^T$ since $\delta_2+\delta_3 \ge 1$!
- **$v_0^\pm = 3^{t_{m+1}}$ with $E(3^{t_{m+1}}) = E_{33}^C$ ($t_{m+1} \ge 0$, and by inductive hypothesis (3)–(4), $E(v_1^+) = E_{32}^+$ and $\delta := \ell(v_1^+) - \ell(3^{t_{m+1}}) \ge (0,0,1)^T$):**
  - If $j \ge 1, k = 0$: $E_{33}^C$ produces only neutral images in $\mathcal{N}_0$, $w_0^\pm = \varepsilon$ ($E_{33}^C$), and $v_1^+$ ($E_{32}^+$) lifts to $w_1^+ = 1^j 3 \tau_{j,0}(v_1^+)$ ($E_{32}^+$), giving $(E(w_0^-), E(w_1^+)) = (E_{33}^C, E_{32}^+)$ and $\ell(w_1^+) \ge (0,0,1)^T$.
  - If $k \ge 1$: $E_{33}^C$ on $3^{t_{m+1}}$ splits into $u_1 = 1^j 3 \tau_{j,k}(3^{t_{m+1}})$ ($A^+$), $u_2 = 1^j 3 \tau_{j,k}(3^{t_{m+1}}) 2^k$ ($A_1^-$ if $j \ge 1$, $A_2^-$ if $j = 0$), and neutral $2^k 1^j 3 \tau_{j,k}(3^{t_{m+1}})$ ($N_6 \in \mathcal{N}_0$ for both $j \ge 1$ and $j=0$), while $v_1^+$ ($E_{32}^+$) lifts to $u_3 = 2^k 1^j 3 \tau_{j,k}(v_1^+)$ ($B^+$) and neutral $1^j 3 \tau_{j,k}(v_1^+)$ ($N_2 \in \mathcal{N}_0$). For $j=0$, $w_0^\pm = \varepsilon$ ($E_{33}^B$) is followed by $w_1^+ = u_1$ ($A^+$, so $(E(w_0^-), E(w_1^+)) = (E_{33}^B, A^+)$ and $\ell(u_1) \ge (0,0,1)^T$); for $j \ge 1$, $w_0^+ = \varepsilon$ ($E_{33}^+$), $w_0^- = 1^j$ ($E_{32}^-$) is followed by $w_1^+ = u_1$ ($A^+$, so $(E(w_0^-), E(w_1^+)) = (E_{32}^-, A^+)$ and $\ell(u_1) - \ell(1^j) = M_{j,k}\ell(3^{t_{m+1}}) + (0,0,1)^T \ge (0,0,1)^T$ with $\Delta_2+\Delta_3 \ge 1$). In both cases $\ell(u_2) - \ell(u_1) = (0,k,0)^T \ge 0$, $\ell(u_3) - \ell(u_2) = (0,k,0)^T + M_{j,k}\delta - (0,k,0)^T = M_{j,k}\delta \ge 0$, and $(E(u_2), E(u_3)) \in \{(A_1^-, B^+), (A_2^-, B^+)\} \subset \mathcal{T}_{\ge 1}$!

Thus (1)–(4) hold for $\mathcal{L}^{(m)}$, completing the induction! $\square$

**Proof of Conjecture 1 (`conj:e-23-e`).**
For any $n \ge 1$, reduce $\mathcal{L}(\mathbf{\sigma})_n \subseteq \mathcal{L}(\mathbf{\sigma}')_n$ as in Section 1. By Theorem 4 applied to $\mathcal{L}' := \mathcal{L}(\mathbf{\sigma}')$, all non-neutral bispecial words of $\mathcal{L}'$ appear without repetition (with pairwise distinct words in $(w_r^+, w_r^-)$ whenever $m \neq 0$, and $m(w_0^\pm)=0$ otherwise) in $(w_r^+, w_r^-)_{r \ge 0}$ with $m(w_r^+) + m(w_r^-) = 0$, $m(w_r^+) \in \{0, 1\}$, and $|w_0^+| \le |w_0^-| \le |w_1^+| \le |w_1^-| \le \cdots$. Therefore, for every integer $N \ge 0$,
$$\sum_{\substack{w \in \mathcal{L}' \\ |w| \le N,\ w\text{ bispecial}}} m(w) \le 1$$
(every $w_r^-$ with $|w_r^-| \le N$ cancels the corresponding $w_r^+$ with $|w_r^+| \le |w_r^-| \le N$, leaving at most one unpaired $+1$). By Corollary 1 (`cor:bi-complex`, Section 5, `L753–759`) with $|\mathcal{L}'_1| = 3$,
$$p_{\mathcal{L}'}(n+1) - p_{\mathcal{L}'}(n) \le (3 - 1) + 1 = 3 \quad \text{for all } n \ge 1.$$
Since $p_{\mathcal{L}'}(1) = 3$, induction gives $p_{\mathcal{L}(\mathbf{\sigma})}(n) \le p_{\mathcal{L}'}(n) \le 3n$ for all $n \ge 1$. The same bound holds for all five conjugates and six twins of $S(e, 23, e)$. $\square$

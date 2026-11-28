# Proof: General Sublogarithmic Space Hierarchy in $\omega(\log\log n) \cap o(\log n)$ (`say-2611.32633-bqtisp-sublog`)

## Verdict

**YES.** We confirm the belief stated in `arXiv:2611.32633v1` (Section 5, lines 1924–1928) and prove a general sublogarithmic space hierarchy theorem throughout $\omega(\log\log n) \cap o(\log n)$ for polynomial-time quantum Turing machines (`BQTISP`), strictly generalizing Theorem `thm:hier` (`main.tex`, lines 1556–1559).

**Theorem 1 (General Sublogarithmic $\mathsf{BQTISP}$ Hierarchy):** *Let $s : \mathbb{N} \to \mathbb{N}$ be any function satisfying:*
1. *(Range)* $s(n) \in \omega(\log\log n) \cap o(\log n)$;
2. *(Monotonicity and doubling smoothness)* $s$ is nondecreasing for sufficiently large $n$ and there exists a constant $C \ge 1$ such that $s(2n) \le C \cdot s(n)$ for all sufficiently large $n$;
3. *(Log-constructibility)* there is a deterministic Turing machine that, on input $\mathrm{bin}(r)$ ($r \ge 1$), computes $\mathrm{bin}(g(r))$ in space $O(g(r))$ and time $2^{O(r)}$, where $g(r) := s(2^r)$.

*Then there exists a language $L_s \in \mathsf{TISP}(n^{O(1)}, O(s(n)))$ such that $L_s \notin \mathsf{BQTISP}_{\mathbb{C}}(n^{O(1)}, o(s(n)))$. Consequently,*
$$\mathsf{BQTISP}\bigl(n^{O(1)}, o(s(n))\bigr) \subsetneq \mathsf{BQTISP}\bigl(n^{O(1)}, O(s(n))\bigr),$$
*and likewise for $\mathsf{BQTISP}_{\mathbb{C}}$.*

*(In particular, this establishes the strict separation at $\Theta(s(n))$ for all standard sublogarithmic scales in $\omega(\log\log n) \cap o(\log n)$, including $(\log n)^\alpha$ for any rational $\alpha \in (0,1)$, $\frac{\log n}{(\log\log n)^c}$ for any rational $c > 0$, $\frac{\log n}{\log\log\log n}$, and $\log\log n \cdot \log\log\log n$, as well as Theorem `thm:hier` for $i \ge 1$ via $s(n) = \lfloor \log_2 n / (\log_2\log_2 n)^i \rfloor$.)*

---

## 1. Exact Length Estimate of $L_S$ in $O(\log\log n)$ Deterministic Space

As in Section 4 (`main.tex`, lines 1576–1585), for $l \ge 0$ let $\mathrm{bin}(l)$ be the shortest binary representation of $l$ (so $\mathrm{bin}(0) = 0$ has length $1$, and $|\mathrm{bin}(l)| = \lfloor \log_2 l \rfloor + 1$ for $l \ge 1$), and let
$$L_S = \{ \mathrm{bin}(0)\$\mathrm{bin}(1)\$\dots\$\mathrm{bin}(k) \mid k > 0 \}.$$
For each $k \ge 1$, let $u_k$ be the $k$-th string in $L_S$ and $N_k := |u_k|$.

**Lemma 1 (Exact formula and $O(\log\log n)$-space bit-length estimate):** *For every integer $k \ge 1$, putting $m := |\mathrm{bin}(k)| = \lfloor \log_2 k \rfloor + 1$:*
1. $N_k = (k + 1)(m + 1) - 2^m + 1$.
2. *For $m \ge 8$ (equivalently $k \ge 128$), set $t := \lceil \log_2(m + 1) \rceil + 3 < m$, let $K_{\mathrm{top}} := \lfloor k / 2^{m - t} \rfloor$ be the integer formed by the $t$ most significant bits of $\mathrm{bin}(k)$, and let $A := K_{\mathrm{top}}(m + 1) - 2^t$. Defining $\tilde{r}_k := (m - t) + \lfloor \log_2 A \rfloor$, we have $A \cdot 2^{m-t} \le N_k < 2A \cdot 2^{m-t}$, and hence*
   $$\tilde{r}_k \le \lfloor \log_2 N_k \rfloor \le \tilde{r}_k + 1, \qquad 2^{\tilde{r}_k} \le N_k < 2^{\tilde{r}_k + 2}.$$
3. *Given $u_k$ on the input tape, a deterministic Turing machine can verify $u_k \in L_S$ and compute $\mathrm{bin}(\tilde{r}_k)$ on its work tape in $O(\log\log N_k)$ space and $N_k^{O(1)}$ time.*

*Proof.*
1. The segment $\mathrm{bin}(0)$ plus its separator contributes $|\mathrm{bin}(0)| + 1 = 2$ symbols, and each $r \in \{1, \dots, k\}$ contributes $|\mathrm{bin}(r)| + 1$ symbols (with the final $\$$ omitted, giving $-1$ at the end). Grouping by $j = |\mathrm{bin}(r)| \in \{1, \dots, m\}$:
   $$N_k = 1 + \sum_{j=1}^{m-1} 2^{j-1}(j+1) + (k - 2^{m-1} + 1)(m+1).$$
   Using $\sum_{j=1}^{m-1} j 2^{j-1} = (m - 2)2^{m-1} + 1$ and $\sum_{j=1}^{m-1} 2^{j-1} = 2^{m-1} - 1$, the first sum is $(m - 1)2^{m-1}$, so
   $$N_k = 1 + (m-1)2^{m-1} + (k + 1)(m+1) - 2^{m-1}(m+1) = (k+1)(m+1) - 2^m + 1.$$
2. Write $k = K_{\mathrm{top}} 2^{m-t} + k_{\mathrm{rem}}$ with $2^{t-1} \le K_{\mathrm{top}} < 2^t$ and $0 \le k_{\mathrm{rem}} < 2^{m-t}$. Substituting into part (1) gives
   $$N_k = A \cdot 2^{m-t} + (k_{\mathrm{rem}} + 1)(m + 1) + 1.$$
   Since $m \ge 8$, we have $t = \lceil \log_2(m+1) \rceil + 3 \le m - 1$ (indeed $\lceil \log_2 9 \rceil + 3 = 7 < 8$, and $t$ grows logarithmically while $m$ grows linearly) and $2^{t-1} \ge 4(m+1)$. Thus
   $$A \ge 2^{t-1}(m+1) - 2^t = 2^{t-1}(m - 1) \ge 4(m+1)(m-1) > m + 2.$$
   On the other hand, $(k_{\mathrm{rem}} + 1)(m + 1) + 1 \le 2^{m-t}(m + 1) + 1 \le (m + 2) 2^{m-t} < A \cdot 2^{m-t}$. Therefore $A \cdot 2^{m-t} \le N_k < 2 A \cdot 2^{m-t}$. Taking $\lfloor \log_2(\cdot) \rfloor$ yields $\tilde{r}_k = (m - t) + \lfloor \log_2 A \rfloor \le \lfloor \log_2 N_k \rfloor \le \tilde{r}_k + 1$, and $2^{\tilde{r}_k} \le N_k < 2^{\tilde{r}_k + 2}$.
3. As shown in `main.tex` (lines 1580–1585, citing [SHL65]), a DTM recognizes $L_S$ in $O(\log\log N_k)$ space and $N_k^{O(1)}$ time, leaving $m = |\mathrm{bin}(k)| = O(\log N_k)$ in binary on $O(\log\log N_k)$ work-tape bits. Computing $t = \lceil \log_2(m+1) \rceil + 3$, copying the leftmost $t$ bits of the final segment $\mathrm{bin}(k)$ to obtain $K_{\mathrm{top}}$, and performing integer arithmetic on $O(\log\log N_k)$-bit integers to produce $\mathrm{bin}(\tilde{r}_k)$ all fit in $O(\log\log N_k)$ space and $\mathrm{poly}(\log N_k)$ time. $\square$

---

## 2. Witness Language $L_s$ and Upper Bound

Using the two-track alphabet $\Sigma = \{0,1,\$\} \times \{0,1,\#\}$ from Section 4 (`main.tex`, line 1589), fix $k_0 = 128$ (so $m \ge 8$ for all $k \ge k_0$) and a threshold $r_0 \ge 8$ large enough that for all $r \ge r_0$, $s$ is nondecreasing on $[2^{r_0}, \infty)$, $s(2n) \le C s(n)$ holds for $n \ge 2^{r_0}$, and $1 \le g(r) \le r - 2$ (possible since $s(n) \in \omega(\log\log n) \cap o(\log n)$, so $g(r) = s(2^r) \in \omega(\log r) \cap o(r)$). Fix $k_1 \ge k_0$ such that $\tilde{r}_k \ge r_0$ for all $k \ge k_1$ (note $\tilde{r}_k \ge m - 1$ for all $k \ge 128$).

Define $L_s \subseteq \Sigma^*$ to be the set of all strings $w$ of length $n$ such that:
- the upper track of $w$ is $u_k \in L_S$ for some $k \ge k_1$ (so $n = N_k$), and
- the lower track of $w$ is $p \#^{N_k - j_k}$, where $j_k := 2^{g(\tilde{r}_k)}$ and $p \in L_{\mathrm{pal}} \cap \{0,1\}^{j_k}$.

Note that for all $k \ge k_1$, $\tilde{r}_k \ge r_0$ implies $g(\tilde{r}_k) \le \tilde{r}_k - 2$, so $j_k = 2^{g(\tilde{r}_k)} \le 2^{\tilde{r}_k - 2} \le N_k / 4 < N_k$; thus $N_k - j_k > 0$ and the lower track is well-defined.

**Lemma 2 (Upper bound):** *$L_s \in \mathsf{TISP}(n^{O(1)}, O(s(n))) \subseteq \mathsf{BQTISP}(n^{O(1)}, O(s(n)))$.*

*Proof.* Consider the following DTM $M_s$ on input $w$ of length $n$:
1. *(Stage A)* Run Lemma 1(3) on the upper track to verify $w$'s upper track belongs to $L_S$ and compute $m = |\mathrm{bin}(k)|$. If the upper track is not in $L_S$ or $k < k_1$ (checking $m < |\mathrm{bin}(k_1)|$ or comparing the bounded-size prefix $k < k_1$ in $O(1)$ space), reject. Otherwise compute $\mathrm{bin}(\tilde{r}_k)$ in $O(\log\log n)$ deterministic space and $n^{O(1)}$ time.
2. *(Stage B)* Run the log-constructibility machine for $g$ on $\mathrm{bin}(\tilde{r}_k)$ to write $\mathrm{bin}(l_k)$ where $l_k := g(\tilde{r}_k)$. By hypothesis (3), this takes time $2^{O(\tilde{r}_k)} = n^{O(1)}$ and space $O(g(\tilde{r}_k)) = O(s(2^{\tilde{r}_k}))$. Since $2^{\tilde{r}_k} \le N_k = n$ (Lemma 1(2)) and $s$ is nondecreasing above $2^{r_0}$, $s(2^{\tilde{r}_k}) \le s(n)$, so Stage B uses $O(s(n))$ space.
3. *(Stage C)* Write $j_k = 2^{l_k}$ in binary (`1` followed by $l_k$ zeros) on the work tape using $l_k + 1 = O(s(n))$ bits.
4. *(Stages D–E)* Exactly as in Lemma `lem:dtm` (`main.tex`, lines 1625–1635), use $O(\log j_k) = O(l_k) = O(s(n))$ bits of counter space and $O(n^2)$ time to verify that the lower track has the form $p \#^{n - j_k}$ with $|p| = j_k$ and $p \in L_{\mathrm{pal}}$.

Since $s(n) \in \omega(\log\log n)$, Stage A's $O(\log\log n)$ space is $o(s(n))$, and Stages B–E use $O(s(n))$ space and $n^{O(1)}$ time in the worst case. As QTMs simulate DTMs exactly with no extra space or asymptotic time overhead (`main.tex`, line 1638), $L_s \in \mathsf{TISP}(n^{O(1)}, O(s(n))) \subseteq \mathsf{BQTISP}(n^{O(1)}, O(s(n)))$. $\square$

---

## 3. Nonregularity Lower Bound

**Lemma 3 (Lower bound):** *$L_s \notin \mathsf{BQTISP}_{\mathbb{C}}(n^{O(1)}, o(s(n)))$.*

*Proof.* At every populated length $N_k$ with $k \ge k_1$, $j_k = 2^{l_k}$ is even (since $l_k \ge 1$ for sufficiently large $k$, as $g(r) \in \omega(\log r)$). Let $W_{N_k}$ be the set of prefixes of length $j_k / 2$ of strings in $L_s \cap \Sigma^{N_k}$ (whose lower tracks range over all $\{0,1\}^{j_k / 2}$). Any two distinct prefixes in $W_{N_k}$ are $(L_s, N_k)$-dissimilar (`main.tex`, lines 1680–1699), giving
$$D_{L_s}(N_k) \ge |W_{N_k}| = 2^{j_k / 2} = 2^{2^{l_k - 1}}.$$
For any sufficiently large $n \ge N_{k_1}$, let $k \ge k_1$ be the unique integer with $N_k \le n < N_{k+1}$. Since $N_{k+1} - N_k = |\mathrm{bin}(k+1)| + 1 \le \log_2 n + 2$, for all sufficiently large $n$ we have $N_k \ge n / 2$. By Lemma 1(2), $2^{\tilde{r}_k} > N_k / 4 \ge n / 8$. Using monotonicity of $s$ and applying the doubling-smoothness bound $s(2x) \le C s(x)$ three times gives
$$s(n) \le s(8 \cdot 2^{\tilde{r}_k}) \le C^3 s(2^{\tilde{r}_k}) = C^3 g(\tilde{r}_k) = C^3 l_k.$$
Since $D_{L_s}$ is nondecreasing (`main.tex`, line 1740), setting $d_0 := \frac{1}{2} C^{-3} > 0$, we obtain for all sufficiently large $n$:
$$D_{L_s}(n) \ge D_{L_s}(N_k) \ge 2^{2^{C^{-3} s(n) - 1}} \ge 2^{2^{d_0 s(n)}}.$$

Suppose toward a contradiction that $L_s \in \mathsf{BQTISP}_{\mathbb{C}}(n^{O(1)}, s_0(n))$ via a bounded-error QTM running in expected time $t(n) \in n^{O(1)}$ and worst-case space $s_0(n) \in o(s(n))$. Then $\log_2 \log_2 D_{L_s}(n) \ge d_0 s(n)$, so $s_0(n) = o(\log\log D_{L_s}(n))$. Applying Remscrim's time-space tradeoff (Theorem `thm:remscrimQTMtradeoff`, `main.tex`, lines 1100–1105), there exists $b_0 > 0$ such that
$$t(n) \in \Omega\bigl(2^{-b_0 s_0(n)} D_{L_s}(n)^{2^{-b_0 s_0(n)}}\bigr) = \Omega\bigl(2^{2^{F(n)} - b_0 s_0(n)}\bigr),$$
where $F(n) := d_0 s(n) - b_0 s_0(n)$. Because $s_0(n) \in o(s(n))$, for all sufficiently large $n$ we have $b_0 s_0(n) \le \frac{d_0}{2} s(n)$, so $F(n) \ge \frac{d_0}{2} s(n)$. Since $s(n) \in \omega(\log\log n)$, we get $2^{F(n)} \ge 2^{\frac{d_0}{2} s(n)} \in \omega(\log n)$, whereas $b_0 s_0(n) \in o(s(n)) \subseteq o(\log n)$. Hence $2^{F(n)} - b_0 s_0(n) \in \omega(\log n)$, forcing $t(n) \in n^{\omega(1)}$, a contradiction. $\square$

Combining Lemmas 2 and 3 yields Theorem 1. $\qquad \square$

---

## Verification

Exact integer verification in `verify.py` (`OVERALL: PASS`) checks:
- Exact identity $N_k = (k+1)(|\mathrm{bin}(k)| + 1) - 2^{|\mathrm{bin}(k)|} + 1$ against direct string lengths of $u_k \in L_S$ for $k = 1, \dots, 5000$;
- Exact inequalities $A \cdot 2^{m-t} \le N_k < 2A \cdot 2^{m-t}$ and $\tilde{r}_k \le \lfloor \log_2 N_k \rfloor \le \tilde{r}_k + 1$ for all $k \in [128, 30000]$;
- Exact feasibility ($j_k = 2^{g(\tilde{r}_k)} \le N_k$, bounded space $g(\tilde{r}_k) \le s(N_k)$, and gap smoothness $n / 8 < 2^{\tilde{r}_k}$ for $N_k \le n < N_{k+1}$) on concrete monotone sublogarithmic families across $\omega(\log\log n) \cap o(\log n)$: $\lfloor \sqrt{\lfloor \log_2 n \rfloor} \rfloor$, $\lfloor \sqrt{\lfloor \log_2 n \rfloor} \rfloor \cdot \lfloor (\lfloor \log_2 n \rfloor)^{1/4} \rfloor$, and $\lfloor \log_2\lfloor \log_2 n \rfloor \rfloor \cdot \lfloor \log_2\lfloor \log_2\lfloor \log_2 n \rfloor \rfloor \rfloor$.

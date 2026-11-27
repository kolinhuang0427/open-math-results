# Proof of Conjecture 6.4 and Conjecture 6.3 (`arXiv:2310.15207v1`, Section 6)

We prove **Conjecture 6.4** (`\label{conj:4}`) and **Conjecture 6.3** (`\label{conj:3}`) of Victor J. W. Guo (`arXiv:2310.15207v1`, Section 6) unconditionally for every integer $n \equiv 1 \pmod 4$ with $n > 1$ and all positive integers $r > s$.

---

## 1. Setup and Telescoping Reduction

Fix an integer $n \equiv 1 \pmod 4$ with $n > 1$ and an integer $s \ge 1$. Write
$$N := n^s \equiv 1 \pmod 4, \qquad z := 1 - q^N.$$
Because $\Phi_N(q)$ divides $q^N - 1 = -z$ in $\mathbb{Z}[q]$, we have $z^2 \equiv 0 \pmod{\Phi_N(q)^2}$. Substituting $q^N = 1 - z$ yields, for every nonnegative integer $K$ and integer $a \in \{1, \dots, N-1\}$,
$$q^{a + KN} = q^a(1 - z)^K \equiv q^a(1 - Kz) \pmod{\Phi_N(q)^2},$$
and hence
$$1 - q^{a + KN} \equiv (1 - q^a) + K q^a z = (1 - q^a)\!\left(1 + K\frac{q^a}{1 - q^a}z\right) \pmod{\Phi_N(q)^2}, \tag{1}$$
where $1 - q^a$ is invertible in $\mathbb{Q}[q]/(\Phi_N(q)^2)$ because $\Phi_N(q)$ is irreducible over $\mathbb{Q}$ and $1 \le a < N$ implies $\Phi_N(q) \nmid (1 - q^a)$.

Moreover, for every $a \in \{1, \dots, N-1\}$, using $q^N \equiv 1 \pmod{\Phi_N(q)}$ gives $q^{N-a} \equiv q^{-a} \pmod{\Phi_N(q)}$, so in $\mathbb{Q}[q]/(\Phi_N(q))$:
$$\frac{q^a}{1 - q^a} + \frac{q^{N-a}}{1 - q^{N-a}} \equiv \frac{q^a}{1 - q^a} + \frac{q^{-a}}{1 - q^{-a}} = \frac{q^a}{1 - q^a} - \frac{1}{1 - q^a} = -1 \pmod{\Phi_N(q)}. \tag{2}$$

By induction on $r \ge s+1$, any congruence $R(n,r;q) \equiv R(n,s;q) \pmod{\Phi_N(q)^2}$ for rational functions $R(n,r;q) \in \mathbb{Q}(q)$ whose numerator and denominator (after cancelling common factors) are coprime to $\Phi_N(q)$ follows once we verify:
1. **Well-definedness:** $R(n,s;q)$ has denominator coprime to $\Phi_N(q)$ in $\mathbb{Q}[q]$; and
2. **One-step invariance:** for every $r \ge s+1$, the step ratio $T(n,r;q) := R(n,r;q)/R(n,r-1;q)$ has numerator and denominator coprime to $\Phi_N(q)$ and satisfies $T(n,r;q) \equiv 1 \pmod{\Phi_N(q)^2}$.

---

## 2. Proof of Conjecture 6.4

Define
$$R_4(n,r;q) := \frac{(q;q^2)_{(n^r-1)/4} (q^{2n};q^{2n})_{(n^{r-1}-1)/4}}{(q^2;q^2)_{(n^r-1)/4} (q^n;q^{2n})_{(n^{r-1}-1)/4}}.$$

### Step 2.1: Coprimality of $R_4(n,s;q)$ to $\Phi_N(q)$
In $R_4(n,s;q)$, the factors in $(q;q^2)_{(N-1)/4}$ and $(q^2;q^2)_{(N-1)/4}$ have exponents at most $2\bigl(\frac{N-1}{4}-1\bigr)+2 = \frac{N-1}{2} < N$, and the factors in $(q^n;q^{2n})_{(N/n-1)/4}$ and $(q^{2n};q^{2n})_{(N/n-1)/4}$ have exponents at most $n\cdot \frac{N/n-1}{2} < N$. Since every exponent $m$ satisfies $1 \le m < N$, no factor $1-q^m$ is divisible by $\Phi_N(q)$. Thus both numerator and denominator of $R_4(n,s;q)$ are coprime to $\Phi_N(q)$.

### Step 2.2: Exact cancellation of $n$-multiples in $T_4(n,r;q)$
Fix $r \ge s+1$ (so $r \ge 2$). Set
$$k_0 := \frac{n^{r-1}-1}{4}, \qquad k_1 := \frac{n^r-1}{4}, \qquad j_0 := \frac{n^{r-2}-1}{4} \in \mathbb{Z}_{\ge 0}.$$
Then
$$T_4(n,r;q) := \frac{R_4(n,r;q)}{R_4(n,r-1;q)} = \frac{\prod_{k=k_0}^{k_1-1}(1 - q^{2k+1})}{\prod_{k=k_0}^{k_1-1}(1 - q^{2k+2})} \cdot \frac{\prod_{j=j_0}^{k_0-1}(1 - q^{n(2j+2)})}{\prod_{j=j_0}^{k_0-1}(1 - q^{n(2j+1)})}.$$
Let us identify the factors $(1 - q^{2k+1})$ ($k_0 \le k \le k_1-1$) whose exponent is divisible by $n$. Since $n$ and $2k+1$ are odd, $n \mid (2k+1)$ holds if and only if $2k+1 = n(2j+1)$ for an integer $j$, with bounds
$$\frac{n^{r-1}+1}{2} = 2k_0+1 \le n(2j+1) \le 2k_1-1 = \frac{n^r-3}{2} \iff \frac{n^{r-2}}{2} + \frac{1}{2n} \le 2j+1 \le \frac{n^{r-1}}{2} - \frac{3}{2n}.$$
Since $n^{r-2} \equiv n^{r-1} \equiv 1 \pmod 4$, both $(n^{r-2}-1)/2$ and $(n^{r-1}-1)/2$ are even integers. Therefore, the odd integer $2j+1$ satisfies these inequalities if and only if
$$\frac{n^{r-2}+1}{2} \le 2j+1 \le \frac{n^{r-1}-3}{2} \iff j_0 \le j \le k_0 - 1.$$
Hence the subproduct of $(1-q^{2k+1})$ with $n \mid (2k+1)$ cancels identically with $\prod_{j=j_0}^{k_0-1}(1 - q^{n(2j+1)})$.

Similarly, $n \mid (2k+2)$ for $k_0 \le k \le k_1-1$ holds if and only if $2k+2 = n(2j+2)$ for an integer $j$ satisfying
$$\frac{n^{r-1}+3}{2} = 2k_0+2 \le n(2j+2) \le 2k_1 = \frac{n^r-1}{2} \iff \frac{n^{r-2}}{2} + \frac{3}{2n} \le 2j+2 \le \frac{n^{r-1}}{2} - \frac{1}{2n}.$$
Because $(n^{r-2}-1)/2$ and $(n^{r-1}-1)/2$ are even, the even integer $2j+2$ satisfies these inequalities if and only if
$$\frac{n^{r-2}+3}{2} \le 2j+2 \le \frac{n^{r-1}-1}{2} \iff j_0 \le j \le k_0 - 1.$$
Thus the factors $(1-q^{2k+2})$ with $n \mid (2k+2)$ cancel identically with $\prod_{j=j_0}^{k_0-1}(1 - q^{n(2j+2)})$, leaving
$$T_4(n,r;q) = \frac{\prod_{\substack{k=k_0 \\ n \nmid (2k+1)}}^{k_1-1}(1 - q^{2k+1})}{\prod_{\substack{k=k_0 \\ n \nmid (2k+2)}}^{k_1-1}(1 - q^{2k+2})}. \tag{3}$$
Every remaining factor $(1-q^m)$ satisfies $n \nmid m$, hence $N = n^s \nmid m$, so $\Phi_N(q) \nmid (1-q^m)$.

### Step 2.3: Block decomposition and evaluation of $\Delta Q_4(a)$
Let $K_0 := n^{r-1-s} \equiv 1 \pmod 4$, so $n^{r-1} = K_0 N$ and $M := \frac{n-1}{4} K_0 \in \mathbb{Z}_{\ge 1}$. Then $k_1 - k_0 = \frac{n^{r-1}(n-1)}{4} = MN$. Partition $k \in [k_0, k_1-1]$ into $M$ blocks $k = k_0 + tN + i$ with $0 \le t < M$ and $0 \le i < N$. Setting $c := (K_0-1)/2 \in \mathbb{Z}_{\ge 0}$, we have
$$2k_0 + 1 = \frac{K_0 N + 1}{2} = cN + \frac{N+1}{2}, \qquad 2k_0 + 2 = cN + \frac{N+3}{2},$$
so within block $t$ the numerator and denominator exponents are
$$e_{\text{num}}(t,i) = (2t+c)N + \left(\frac{N+1}{2} + 2i\right), \qquad e_{\text{den}}(t,i) = (2t+c)N + \left(\frac{N+3}{2} + 2i\right).$$
Since $\gcd(2,N)=1$, as $i$ ranges over $\{0,\dots,N-1\}$ each of $\frac{N+1}{2}+2i$ and $\frac{N+3}{2}+2i$ hits every residue $a \in \{0,1,\dots,N-1\}$ modulo $N$ exactly once, and the condition $n \nmid e(t,i)$ is equivalent to $n \nmid a$ (which excludes $a=0$ and all multiples of $n$).

For each $a \in \{1,\dots,N-1\}$, write
$$\frac{N+1}{2} + 2i = q_{\text{num}}(a)N + a, \qquad \frac{N+3}{2} + 2i' = q_{\text{den}}(a)N + a,$$
with $0 \le i, i' \le N-1$. Let us determine $q_{\text{num}}(a)$ and $q_{\text{den}}(a)$ explicitly:
- For $\frac{N+1}{2}+2i$: it ranges over all **odd** integers in $\bigl[\frac{N+1}{2}, \frac{5N-3}{2}\bigr] \subset (0, 3N)$ (note $\frac{N+1}{2}$ is odd because $N \equiv 1 \pmod 4$). Thus $q_{\text{num}}(a) \in \{0,1,2\}$:
  - $q_{\text{num}}(a) = 1 \iff N+a \in \bigl[\frac{N+1}{2}, \frac{5N-3}{2}\bigr]$ is odd $\iff$ $a$ is **even** (since $N$ is odd, and indeed $N+2 \ge \frac{N+1}{2}$ and $2N-2 \le \frac{5N-3}{2}$ for all $N \ge 5$).
  - $q_{\text{num}}(a) = 0 \iff a \in \bigl[\frac{N+1}{2}, N-1\bigr]$ is **odd**.
  - $q_{\text{num}}(a) = 2 \iff 2N+a \in \bigl[2N+1, \frac{5N-3}{2}\bigr]$ is odd $\iff a \in \bigl[1, \frac{N-1}{2}\bigr]$ is **odd** (since $\frac{N-1}{2}$ is even, its largest odd integer is $\frac{N-3}{2}$).
- For $\frac{N+3}{2}+2i'$: it ranges over all **even** integers in $\bigl[\frac{N+3}{2}, \frac{5N-1}{2}\bigr] \subset (0, 3N)$. Thus $q_{\text{den}}(a) \in \{0,1,2\}$:
  - $q_{\text{den}}(a) = 1 \iff N+a$ is even $\iff$ $a$ is **odd** (as $N+1 \ge \frac{N+3}{2}$ and $2N-1 \le \frac{5N-1}{2}$).
  - $q_{\text{den}}(a) = 0 \iff a \in \bigl[\frac{N+1}{2}, N-1\bigr]$ is **even** (the smallest even integer $\ge \frac{N+1}{2}$ is $\frac{N+3}{2}$).
  - $q_{\text{den}}(a) = 2 \iff a \in \bigl[1, \frac{N-1}{2}\bigr]$ is **even**.

Subtracting gives $\Delta Q_4(a) := q_{\text{num}}(a) - q_{\text{den}}(a)$ for every $1 \le a \le N-1$:
$$\Delta Q_4(a) = \begin{cases}
(-1)^{a-1} & \text{if } 1 \le a \le \frac{N-1}{2}, \\[4pt]
(-1)^a & \text{if } \frac{N+1}{2} \le a \le N-1.
\end{cases} \tag{4}$$

Applying (1) to every factor in (3), the $(1-q^a)$ factors cancel identically between numerator and denominator in every block $t$, and since $z^2 \equiv 0 \pmod{\Phi_N(q)^2}$, all $(2t+c)$ terms cancel in $\Delta Q_4(a)$:
$$T_4(n,r;q) \equiv \prod_{t=0}^{M-1} \prod_{\substack{1 \le a \le N-1 \\ n \nmid a}} \left(1 + \Delta Q_4(a)\frac{q^a}{1-q^a}z\right) \equiv 1 + Mz \sum_{\substack{1 \le a \le N-1 \\ n \nmid a}} \Delta Q_4(a)\frac{q^a}{1-q^a} \pmod{\Phi_N(q)^2}.$$

### Step 2.4: Pairing cancellation modulo $\Phi_N(q)$
Since $N$ is odd, $a \leftrightarrow N-a$ reverses parity and swaps $\bigl[1, \frac{N-1}{2}\bigr]$ with $\bigl[\frac{N+1}{2}, N-1\bigr]$, so (4) gives $\Delta Q_4(N-a) = \Delta Q_4(a)$. Pairing $\{a, N-a\}$ via (2) yields
$$\sum_{\substack{1 \le a \le N-1 \\ n \nmid a}} \Delta Q_4(a)\frac{q^a}{1-q^a} \equiv -\sum_{\substack{1 \le a \le (N-1)/2 \\ n \nmid a}} (-1)^{a-1} \pmod{\Phi_N(q)}.$$
Because $N \equiv 1 \pmod 4$, $(N-1)/2$ is even, so $\sum_{a=1}^{(N-1)/2} (-1)^{a-1} = 0$. The multiples of $n$ in $\bigl[1, \frac{N-1}{2}\bigr]$ are $a = nm$ for $1 \le m \le \frac{N/n - 1}{2}$. Since $n$ is odd we have $(-1)^{nm-1} = (-1)^{m-1}$, and since $N/n = n^{s-1} \equiv 1 \pmod 4$, $\frac{N/n-1}{2}$ is also even, so $\sum_{m=1}^{(N/n-1)/2} (-1)^{nm-1} = 0$. Subtracting gives
$$\sum_{\substack{1 \le a \le N-1 \\ n \nmid a}} \Delta Q_4(a)\frac{q^a}{1-q^a} \equiv 0 \pmod{\Phi_N(q)}.$$
Multiplying by $Mz$ (which is divisible by $\Phi_N(q)$) proves $T_4(n,r;q) \equiv 1 \pmod{\Phi_N(q)^2}$, completing the proof of Conjecture 6.4. $\blacksquare$

---

## 3. Proof of Conjecture 6.3

Define
$$R_3(n,r;q) := [n]\frac{(q^3;q^4)_{(n^r-1)/2} (q^{5n};q^{4n})_{(n^{r-1}-1)/2}}{(q^5;q^4)_{(n^r-1)/2} (q^{3n};q^{4n})_{(n^{r-1}-1)/2}}.$$

### Step 3.1: Coprimality of $R_3(n,s;q)$ to $\Phi_N(q)$
- **Case $s=1$ ($N=n$):** Here $(q^{3n};q^{4n})_0 = (q^{5n};q^{4n})_0 = 1$, and $(q^5;q^4)_{(n-1)/2}$ has exponents $4j+5 \in [5, 2n+1]$ ($0 \le j < \frac{n-1}{2}$). Since $4j+5$ is odd and $2n$ is even while $3n > 2n+1$, the only multiple of $n$ among these exponents is $n$ itself (at $j = (n-5)/4$), so $1-q^n$ cancels the numerator factor $1-q^n$ of $[n] = \frac{1-q^n}{1-q}$. The remaining denominator factors $(1-q)$ and $1-q^{4j+5}$ ($4j+5 \neq n$) are all coprime to $\Phi_n(q)$.
- **Case $s \ge 2$ ($N=n^s$):** In $(q^5;q^4)_{(N-1)/2}$, the exponents $4j+5 \in [5, 2N+1]$ are odd, so the unique multiple of $N$ is $N$ itself (at $j=(N-5)/4$). Meanwhile $N/n = n^{s-1} \equiv 1 \pmod 4$ satisfies $N/n \ge 5$, so in $(q^{5n};q^{4n})_{(N/n-1)/2}$ the index $i = (N/n-5)/4 \ge 0$ satisfies $i < (N/n-1)/2$ and gives $n(4i+5) = N$. In $(q^{3n};q^{4n})_{(N/n-1)/2}$, the exponents $n(4i+3) \in [3n, 2N-n]$ satisfy $4i+3 \neq N/n$ (since $N/n \equiv 1 \pmod 4$), so none are divisible by $N$. Cancelling $1-q^N$ between $(q^{5n};q^{4n})$ and $(q^5;q^4)$ leaves $R_3(n,s;q)$ with both numerator and denominator coprime to $\Phi_N(q)$.

### Step 3.2: Exact cancellation in $T_3(n,r;q) := R_3(n,r;q)/R_3(n,r-1;q)$
Fix $r \ge s+1 \ge 2$, and set $v_0 := \frac{n^{r-1}-1}{2}$, $v_1 := \frac{n^r-1}{2}$, $w_0 := \frac{n^{r-2}-1}{2}$. In $T_3(n,r;q)$, $[n]$ cancels identically.
- Among $4k+3$ for $v_0 \le k \le v_1 - 1$ (so $2n^{r-1}+1 \le 4k+3 \le 2n^r-1$), since $n \equiv 1 \pmod 4$, we have $n \mid (4k+3) \iff 4k+3 = n(4j+3)$ with $2n^{r-2}+\frac{1}{n} \le 4j+3 \le 2n^{r-1}-\frac{1}{n}$. Since $2n^{r-2}+1 \equiv 3 \pmod 4$ and $2n^{r-1}-3 \equiv 3 \pmod 4$, the integer $j$ runs precisely over $w_0 \le j \le v_0-1$, cancelling $\prod_{j=w_0}^{v_0-1}(1-q^{n(4j+3)})$ identically.
- Among $4k+5$ for $v_0 \le k \le v_1 - 1$ (so $2n^{r-1}+3 \le 4k+5 \le 2n^r+1$), $n \mid (4k+5) \iff 4k+5 = n(4j+5)$ with $2n^{r-2}+\frac{3}{n} \le 4j+5 \le 2n^{r-1}+\frac{1}{n}$. Since $2n^{r-2}+3 \equiv 1 \pmod 4$ and $2n^{r-1}+1 \equiv 3 \pmod 4$, $j$ runs precisely over $w_0 \le j \le v_0-1$, cancelling $\prod_{j=w_0}^{v_0-1}(1-q^{n(4j+5)})$ identically.

Thus
$$T_3(n,r;q) = \frac{\prod_{\substack{k=v_0 \\ n \nmid (4k+3)}}^{v_1-1}(1 - q^{4k+3})}{\prod_{\substack{k=v_0 \\ n \nmid (4k+5)}}^{v_1-1}(1 - q^{4k+5})}, \tag{5}$$
and every factor $(1-q^m)$ has $n \nmid m \implies N \nmid m$, hence is coprime to $\Phi_N(q)$.

### Step 3.3: Block decomposition and pairing cancellation
With $K_0 := n^{r-1-s} \equiv 1 \pmod 4$ and $M_3 := \frac{n-1}{2}K_0 \in \mathbb{Z}_{\ge 1}$, we have $v_1 - v_0 = M_3 N$. Partition $k = v_0 + tN + i$ ($0 \le t < M_3$, $0 \le i < N$). Since $4v_0 + 3 = 2n^{r-1}+1 = 2K_0 N + 1$ and $4v_0+5 = 2K_0 N + 3$, the exponents in block $t$ are
$$(4t + 2K_0)N + (4i+1) \quad (\text{numerator}), \qquad (4t + 2K_0)N + (4i+3) \quad (\text{denominator}).$$
Because $\gcd(4,N)=1$, as $i$ runs over $\{0,\dots,N-1\}$, $4i+1$ and $4i+3$ each hit every residue $a \in \{0,\dots,N-1\}$ modulo $N$ once, and $n \nmid (4k+3)$ (resp. $n \nmid (4k+5)$) matches $n \nmid a$. Writing
$$4i+1 = q_1(a)N + a, \qquad 4i'+3 = q_2(a)N + a \qquad (0 \le i,i' < N),$$
we have $1 \le 4i+1 \le 4N-3 < 4N$ and $3 \le 4i'+3 \le 4N-1 < 4N$, so $q_1(a), q_2(a) \in \{0,1,2,3\}$. Reducing modulo $4$ with $N \equiv 1 \pmod 4$ uniquely determines
$$q_1(a) \equiv 1 - a \pmod 4, \qquad q_2(a) \equiv 3 - a \pmod 4.$$
Hence $\Delta Q_3(a) := q_1(a) - q_2(a)$ depends only on $a \bmod 4$:
$$\Delta Q_3(a) = \begin{cases}
-2 & \text{if } a \equiv 0,1 \pmod 4, \\
+2 & \text{if } a \equiv 2,3 \pmod 4.
\end{cases} \tag{6}$$
By (1) and $z^2 \equiv 0 \pmod{\Phi_N(q)^2}$, (5) expands to
$$T_3(n,r;q) \equiv 1 + M_3 z \sum_{\substack{1 \le a \le N-1 \\ n \nmid a}} \Delta Q_3(a)\frac{q^a}{1-q^a} \pmod{\Phi_N(q)^2}.$$
Because $N \equiv 1 \pmod 4$, we have $N-a \equiv 1-a \pmod 4$, which swaps $\{0,1\} \leftrightarrow \{1,0\}$ and $\{2,3\} \leftrightarrow \{3,2\}$ modulo $4$, so $\Delta Q_3(N-a) = \Delta Q_3(a)$. Pairing $\{a, N-a\}$ via (2) gives
$$\sum_{\substack{1 \le a \le N-1 \\ n \nmid a}} \Delta Q_3(a)\frac{q^a}{1-q^a} \equiv -\sum_{\substack{1 \le a \le (N-1)/2 \\ n \nmid a}} \Delta Q_3(a) \pmod{\Phi_N(q)}.$$
Since $(N-1)/2$ is even, $\{1,\dots,(N-1)/2\}$ partitions into consecutive pairs $\{2m-1, 2m\}$ ($1 \le m \le (N-1)/4$), and for each $m$ one element is $\equiv 0,1 \pmod 4$ and the other is $\equiv 2,3 \pmod 4$, so $\Delta Q_3(2m-1) + \Delta Q_3(2m) = 0$. Moreover, for multiples of $n$ in $\bigl[1, \frac{N-1}{2}\bigr]$, $n \equiv 1 \pmod 4$ gives $\Delta Q_3(nm) = \Delta Q_3(m)$, and $(N/n-1)/2$ is even, so $\sum_{m=1}^{(N/n-1)/2} \Delta Q_3(nm) = 0$ as well. Subtracting yields $\sum_{\substack{1 \le a \le (N-1)/2 \\ n \nmid a}} \Delta Q_3(a) = 0$, hence $T_3(n,r;q) \equiv 1 \pmod{\Phi_N(q)^2}$, proving Conjecture 6.3. $\blacksquare$

# Proof of OEIS A286044 Conjecture (Yanev 2026)

## Theorem
Let $(a(n))_{n \ge 1}$ be **OEIS A286044**, the $\{011 \to 0\}$-transform of the Thue–Morse word **A010060** $(t_k)_{k \ge 0}$ ($t_k = s_2(k) \bmod 2$, where $s_2(k)$ is the binary digit sum of $k$), and let $(b(n))_{n \ge 1}$ be **OEIS A003160**, defined by $b(1) = b(2) = 1$ and
$$b(n) = n - b(b(n-1)) - b(b(n-2)) \quad (n \ge 3).$$
Then for every integer $n > 3$,
$$a(n) = b(b(n-2)) - b(b(n-3)).$$

---

## Proof

### 1. Vile numbers and Thue–Morse differences
Let $v_2(k)$ denote the $2$-adic valuation of $k \ge 1$, and define the *vile numbers* (**A003159**) and their complement in $\mathbb{Z}_{\ge 1}$:
$$V = \{k \ge 1 : v_2(k) \equiv 0 \pmod 2\}, \qquad \bar{V} = \mathbb{Z}_{\ge 1} \setminus V = \{k \ge 1 : v_2(k) \equiv 1 \pmod 2\}.$$
Write $V = \{v(1) < v(2) < v(3) < \cdots\}$ ($v(1)=1, v(2)=3, v(3)=4, \dots$), and for any set $S \subseteq \mathbb{Z}_{\ge 1}$ and $N \ge 0$ write $\pi_S(N) = |S \cap \{1, \dots, N\}|$.

- **Fact 1 (Self-similarity of $\bar{V}$):** Every odd positive integer has $v_2(k) = 0$ and hence lies in $V$. For every $k \ge 1$, $v_2(2k) = 1 + v_2(k)$, so $2k \in \bar{V} \iff k \in V$. Therefore
  $$\bar{V} = \{2v(1) < 2v(2) < 2v(3) < \cdots\}, \qquad \pi_{\bar{V}}(N) = \pi_V(\lfloor N/2 \rfloor) \quad (N \ge 0),$$
  and consequently $\pi_V(N) + \pi_V(\lfloor N/2 \rfloor) = N$.

- **Fact 2 (Thue–Morse steps):** For any $j \ge 0$, write $j + 1 = 2^r(2q+1)$ with $r = v_2(j+1) \ge 0$. Then $j = 2^r(2q) + (2^r - 1)$, so $s_2(j) = s_2(j+1) - 1 + r$. Reducing modulo $2$ gives $t_{j+1} - t_j \equiv 1 + v_2(j+1) \pmod 2$. Hence for all $j \ge 0$:
  $$t_{j+1} \ne t_j \iff j + 1 \in V, \qquad t_{j+1} = t_j \iff j + 1 \in \bar{V}.$$

---

### 2. Exact positions of $1$s in A286044
Since $s_2(2m) = s_2(m)$ and $s_2(2m+1) = s_2(m) + 1$, every $m \ge 0$ satisfies
$$(t_{2m}, t_{2m+1}) = (t_m, 1 - t_m) \in \{01, 10\}.$$
In particular, $t_{2m} \ne t_{2m+1}$ for all $m \ge 0$.

1. **Occurrences of `011`:** No `011` can begin at an odd index $2m+1$ (which would force $t_{2m+2} = t_{2m+3} = 1$). Thus every `011` begins at an even index $2m$ with $(t_{2m}, t_{2m+1}) = 01$ and $t_{2m+2} = 1$, i.e. $(t_m, t_{m+1}) = (0, 1)$, and is immediately followed by $t_{2m+3} = 0$. Since $2m+3$ is odd, the next `011` cannot begin before $2m+4$. Hence all occurrences of `011` in $(t_k)_{k \ge 0}$ are strictly disjoint, and the `{011 -> 0}`-transform simply deletes $(t_{2m+1}, t_{2m+2}) = (1, 1)$ for every $m \ge 0$ with $(t_m, t_{m+1}) = (0, 1)$, leaving every $0$ and every remaining $1$ intact.
2. **Surviving $1$s:** Notice $t_0 = 0$, so every $1$ in $t$ occurs at some $k \ge 1$:
   - If $k = 2j+1$ is odd ($j \ge 0$, so $t_j = 0$), $t_{2j+1} = 1$ is deleted iff $t_{2j+2} = t_{j+1} = 1$; thus it survives iff $(t_j, t_{j+1}) = (0, 0)$.
   - If $k = 2j+2$ is even ($j \ge 0$, so $t_{j+1} = 1$), $t_{2j+2} = 1$ is deleted iff $(t_{2j}, t_{2j+1}) = 01$, i.e. $t_j = 0$; thus it survives iff $(t_j, t_{j+1}) = (1, 1)$.

   By Fact 2, the indices $j \ge 0$ with $t_{j+1} = t_j$ are precisely $j + 1 \in \bar{V}$, ordered by $m \ge 1$ as
   $$j_m = 2v(m) - 1.$$
   Because $(t_{j_m}, t_{j_m+1}) \in \{(0,0), (1,1)\}$, every deleted pair $(2i+1, 2i+2)$ with $(t_i, t_{i+1}) = (0,1)$ lies either entirely before the surviving $1$ (when $i < j_m$, since $2i+2 \le 2j_m < k$) or entirely after it (when $i > j_m$, since $2i+1 \ge 2j_m + 3 > k$). Let $D(j_m) = |\{0 \le i < j_m : (t_i, t_{i+1}) = (0, 1)\}|$. Starting from $t_0 = 0$, the sequence $t_0, t_1, \dots, t_{j_m}$ makes $j_m$ steps in $\{0, 1\}$, of which $\pi_{\bar{V}}(j_m) = m - 1$ steps stay unchanged and the remaining $\pi_V(j_m)$ steps change bit:
   $$\pi_V(j_m) = j_m - (m - 1) = 2v(m) - m.$$
   - If $t_{j_m+1} = t_{j_m} = 0$, then $k = 2j_m + 1 = 4v(m) - 1$, and starting/ending at $0$ gives equally many $0 \to 1$ and $1 \to 0$ steps, so $2D(j_m) = \pi_V(j_m) = 2v(m) - m$. The $1$-based position in **A286044** is $(k+1) - 2D(j_m) = 4v(m) - (2v(m) - m) = 2v(m) + m$.
   - If $t_{j_m+1} = t_{j_m} = 1$, then $k = 2j_m + 2 = 4v(m)$, and $t_0 = 0, t_{j_m} = 1$ gives one more $0 \to 1$ step than $1 \to 0$ step, so $2D(j_m) = \pi_V(j_m) + 1 = 2v(m) - m + 1$. The $1$-based position in **A286044** is $(k+1) - 2D(j_m) = (4v(m)+1) - (2v(m) - m + 1) = 2v(m) + m$.

   In both cases, the $m$-th `1` in **A286044** lies at $1$-based index $2v(m) + m$.

3. **Even vile numbers:** Every even element of $V$ has the form $2r$ with $r \in \bar{V}$, hence $r = 2v(m)$ for a unique $m \ge 1$, so the $m$-th even element of $V$ is $4v(m)$. Using Fact 1 twice and $\pi_V(v(m)) = m$, its index $n$ in $V$ (meaning $v(n) = 4v(m)$) is
   $$n = \pi_V(4v(m)) = 4v(m) - \pi_V(2v(m)) = 4v(m) - (2v(m) - \pi_V(v(m))) = 2v(m) + m.$$
   Since $a(n) \in \{0, 1\}$ for all $n \ge 1$, we conclude that for every $n \ge 1$,
   $$a(n) = 1 \iff v(n) \text{ is even}.$$

---

### 3. Exact closed form for A003160
Define $g(0) = 0$ and $g(n) = v(n+1) - (n+1) = \pi_{\bar{V}}(v(n+1))$ for $n \ge 1$. Since all odd positive integers belong to $V$, $v(n+1) - v(n) \in \{1, 2\}$, so $g(n) - g(n-1) \in \{0, 1\}$ for all $n \ge 1$. Moreover, for $y \ge 1$,
$$g(n) = y \iff 2v(y) < v(n+1) < 2v(y+1)$$
(strict inequality since $V \cap \bar{V} = \emptyset$). Because $\pi_{\bar{V}}(2v(y)) = y$, there are $2v(y) - y$ elements of $V$ below $2v(y)$, so $g(n) = y$ iff $2v(y) - y + 1 \le n + 1 \le 2v(y+1) - (y+1)$, i.e., $2v(y) - y \le n \le 2v(y+1) - y - 2$. Substituting $v(y) = g(y-1) + y$ (valid for all $y \ge 1$) and $v(y+1) = g(y) + y + 1$, the level sets $I_y = \{n \ge 1 : g(n) = y\}$ are the contiguous blocks
$$I_y = [\,y + 2g(y-1),\; y + 2g(y)\,], \qquad |I_y| = 1 + 2(g(y) - g(y-1)) \in \{1, 3\}.$$

We check that $g$ satisfies the defining recurrence of $b$:
- Base cases: $v(2)=3 \implies g(1)=1$, $v(3)=4 \implies g(2)=1$, $v(4)=5 \implies g(3)=1$; and $3 - g(g(2)) - g(g(1)) = 3 - 1 - 1 = 1 = g(3)$.
- For $n \ge 4$, let $y = g(n) \ge 2$ (as $v(5) = 7 \implies g(4) = 2$):
  1. **Bottom of $I_y$:** $n = y + 2g(y-1)$. Then $n - 1 = (y-1) + 2g(y-1) \in I_{y-1}$, so $g(n-1) = y - 1$. If $|I_{y-1}| = 3$ (so $g(y-1) = g(y-2)+1$), then $n-2 \in I_{y-1}$ and $g(n-2) = y-1$; if $|I_{y-1}| = 1$ (so $g(y-1) = g(y-2)$), then $n-2 \in I_{y-2}$ and $g(n-2) = y-2$. In both cases $g(g(n-2)) = g(y-1)$, so $n - g(g(n-1)) - g(g(n-2)) = (y + 2g(y-1)) - 2g(y-1) = y = g(n)$.
  2. **Middle of $I_y$:** $n = y + 2g(y-1) + 1$ (here $|I_y| = 3$, so $g(y) = g(y-1) + 1$). Then $g(n-1) = y$ and $g(n-2) = y - 1$, giving $n - g(y) - g(y-1) = (y + 2g(y-1) + 1) - (2g(y-1) + 1) = y = g(n)$.
  3. **Top of $I_y$:** $n = y + 2g(y-1) + 2$ (here $|I_y| = 3$, $g(y) = g(y-1) + 1$). Then $g(n-1) = g(n-2) = y$, giving $n - 2g(y) = (y + 2g(y-1) + 2) - (2g(y-1) + 2) = y = g(n)$.

Since $g(1)=g(2)=1$, $1 \le g(k) < k$ for all $k \ge 2$, and $g$ satisfies $g(n) = n - g(g(n-1)) - g(g(n-2))$ for all $n \ge 3$, induction on $n$ proves
$$b(n) = g(n) = v(n+1) - (n+1) \qquad (\forall n \ge 1).$$

---

### 4. Double-difference identity and conclusion
Let $n > 3$ and put $m = n - 2 \ge 2$. Since $b(k) - b(k-1) \in \{0, 1\}$, we have $b(b(m)) - b(b(m-1)) \in \{0, 1\}$.

- **($\Rightarrow$)** Suppose $b(b(m)) - b(b(m-1)) = 1$. Then $b(m) - b(m-1) = 1$, say $y = b(m) = b(m-1) + 1 \ge 2$, and $b(y) - b(y-1) = 1$. Thus $m = y + 2b(y-1)$ is the bottom of block $I_y$ and $|I_y| = 3$, so $m+1$ and $m+2 = y + 2b(y)$ also lie in $I_y$, giving $b(m+1) = y$. Hence
  $$v(n) = v(m+2) = b(m+1) + (m+2) = y + (y + 2b(y)) = 2(y + b(y))$$
  is even.

- **($\Leftarrow$)** Suppose $v(n) = v(m+2) = 2k$ is even (since $n \ge 4$ and $v(4)=5, v(5)=7, v(6)=9, v(7)=11$ are odd, the smallest such index is $n = 8$ with $v(8) = 12$, so $k \ge 6$). Since $2k \in V$, Fact 1 gives $k \in \bar{V}$, so $v_2(k)$ is odd and $k$ is even. Thus $k - 1$ and $k + 1$ are odd, so $k - 1, k + 1 \in V$, which yields $2k - 2, 2k + 2 \in \bar{V}$, while $2k - 3, 2k - 1, 2k + 1$ are odd and lie in $V$. Because $v(m+2) = 2k$, we read off the adjacent values in $V$:
  $$v(m) = 2k - 3, \qquad v(m+1) = 2k - 1, \qquad v(m+2) = 2k, \qquad v(m+3) = 2k + 1.$$
  Let $y = b(m) = v(m+1) - (m+1) = 2k - m - 2 \ge 2$ (since $b(2)=1$ and $m \ge 2$, in fact $m \ge 6 \implies y \ge 4$). Then $b(m-1) = v(m) - m = (2k - 3) - m = y - 1$. Moreover, $y = \pi_{\bar{V}}(v(m+1)) = \pi_{\bar{V}}(2k - 1) = \pi_{\bar{V}}(2k - 2)$ since $2k - 1 \in V$ and $2k - 2 \in \bar{V}$. Hence $2k - 2$ is the $y$-th element of $\bar{V}$ and $2k + 2$ is the $(y+1)$-th element of $\bar{V}$ (as $2k-1, 2k, 2k+1 \in V$), which gives $2v(y) = 2k - 2$ and $2v(y+1) = 2k + 2$, i.e., $v(y) = k - 1$ and $v(y+1) = k + 1$. Therefore
  $$b(y) - b(y-1) = \bigl(v(y+1) - (y+1)\bigr) - \bigl(v(y) - y\bigr) = (k+1) - (k-1) - 1 = 1,$$
  so $b(b(m)) - b(b(m-1)) = b(y) - b(y-1) = 1$.

Combining Sections 2 and 4, both $a(n)$ and $b(b(n-2)) - b(b(n-3))$ equal the $\{0, 1\}$-indicator of $\{n : v(n) \text{ is even}\}$ for every $n > 3$. $\blacksquare$

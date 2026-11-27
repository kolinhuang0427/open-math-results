# Proof of OEIS A061313 (Zabolotskii Hirzebruch Continued Fraction Conjecture)

## Theorem
Let $(a(n))_{n \ge 1}$ be OEIS `A061313`, defined by $a(1) = 0$ and
$$a(2n) = a(n) + 1 \quad (n \ge 1), \qquad a(2n+1) = a(n+1) + 2 \quad (n \ge 1).$$
Let $r(n) = \mathrm{A007305}(n)/\mathrm{A007306}(n)$ ($n \ge 0$) be the Stern–Brocot subtree enumeration on $[0, 1]$, where $r(0) = 0/1$, $r(1) = 1/1$, and for each level $L \ge 1$ the terms at indices $n \in \{2^{L-1}+1, \dots, 2^L\}$ are the $2^{L-1}$ mediants of adjacent elements in the sorted list $\{r(j) : 0 \le j \le 2^{L-1}\}$.

For every $x \in \mathbb{Q}$, let $[[c_0; c_1, \dots, c_k]]$ denote its unique canonical **Hirzebruch (negative) continued fraction**:
$$x = c_0 - \cfrac{1}{c_1 - \cfrac{1}{c_2 - \ddots - \cfrac{1}{c_k}}}, \qquad c_0 \in \mathbb{Z},\quad c_1, \dots, c_k \in \mathbb{Z}_{\ge 2},$$
obtained iteratively by $c_0 = \lceil x \rceil$ and $x_{i+1} = 1/(c_i - x_i)$ until $c_k = x_k \in \mathbb{Z}$.

1. **Main Theorem ($n \ge 2$):** For every integer $n \ge 2$, the fraction $r(n) \in (0, 1)$ has canonical Hirzebruch continued fraction $[[1; c_1, \dots, c_k]]$ satisfying
   $$1 + c_1 + \dots + c_k = a(n) + 2.$$
2. **Boundary at $n = 1$:** At $n = 1$, $r(1) = 1/1$ has canonical Hirzebruch continued fraction $[[1]]$ (sum $1$), whereas $a(1) + 2 = 2$; thus the literal statement holds for all $n \ge 2$ and has $n = 1$ as its sole boundary exception.

*(Remark: The same matrix lemma immediately proves Andrei Zabolotskii's companion conjecture on OEIS `A008687` for all $n \ge 2$, namely that the number of terms $k + 1$ equals $\mathrm{A008687}(n) + 1$, with the same $n = 1$ boundary where $\mathrm{A008687}(1) + 1 = 2 \neq 1$.)*

---

## Proof

### Step 1: Stern–Brocot Tree Index Recursion ($m \ge 2$)
Associate to each $m \ge 2$ its Farey ancestor interval $\left[\frac{a_m}{b_m}, \frac{c_m}{d_m}\right] \subseteq [0, 1]$ (with $b_m c_m - a_m d_m = 1$) whose mediant is $r(m) = \frac{a_m + c_m}{b_m + d_m}$, encoded by the unimodular matrix
$$M(m) := \begin{pmatrix} c_m & a_m \\ d_m & b_m \end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z}).$$
- At level $L = 1$ ($m = 2$), the sole interval is $[0/1, 1/1]$, so $M(2) = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$ and $r(2) = 1/2$.
- Suppose at level $L - 1 \ge 1$ the fractions $\{r(m) : 2^{L-2} + 1 \le m \le 2^{L-1}\}$ split the $2^{L-2}$ existing intervals into $2^{L-1}$ adjacent intervals in increasing order, where $r(m) = \frac{a_m + c_m}{b_m + d_m}$ splits $\left[\frac{a_m}{b_m}, \frac{c_m}{d_m}\right]$ into
  $$\left[\frac{a_m}{b_m},\; \frac{a_m + c_m}{b_m + d_m}\right] \quad \text{and} \quad \left[\frac{a_m + c_m}{b_m + d_m},\; \frac{c_m}{d_m}\right].$$
  Writing $m = 2^{L-2} + j$ ($1 \le j \le 2^{L-2}$), these two subintervals are the $(2j-1)$-th and $(2j)$-th intervals at level $L$, so their mediants have indices $2^{L-1} + (2j - 1) = 2m - 1$ and $2^{L-1} + 2j = 2m$. Their matrices are
  $$M(2m - 1) = \begin{pmatrix} a_m + c_m & a_m \\ b_m + d_m & b_m \end{pmatrix} = M(m) L, \qquad M(2m) = \begin{pmatrix} c_m & a_m + c_m \\ d_m & b_m + d_m \end{pmatrix} = M(m) R,$$
  where
  $$L := \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \qquad R := \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.$$

### Step 2: Conjugation to Hirzebruch Matrices
For $c \in \mathbb{Z}$, define the Hirzebruch step matrix
$$H(c) := \begin{pmatrix} c & -1 \\ 1 & 0 \end{pmatrix} \in \mathrm{SL}_2(\mathbb{Z}).$$
Observe that $H(c)\binom{p'}{q'} = \binom{c p' - q'}{p'}$, so if $p'/q' = [[c_1; \dots, c_k]]$ (with $\gcd(p', q') = 1, q' > 0$) and $c_0 \ge 1$ ($c_1 \ge 2 \implies p' > q' > 0$), then $c_0 p' - q' > 0$ and $\gcd(c_0 p' - q', p') = 1$ with ratio $c_0 - \frac{q'}{p'} = [[c_0; c_1, \dots, c_k]]$. By induction on $k \ge 1$, the product $H(c_0) H(c_1) \cdots H(c_k)$ has first column $(p, q)^T$ equal to the reduced fraction $p/q = [[c_0; c_1, \dots, c_k]]$.

Let $J := H(1) = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}$, so $J^{-1} = \begin{pmatrix} 0 & 1 \\ -1 & 1 \end{pmatrix}$, and define $P(m) := M(m) J$ for all $m \ge 2$. Notice that the first column of $P(m)$ is $M(m)\binom{1}{1} = \binom{a_m + c_m}{b_m + d_m}$, which represents $r(m)$ in lowest terms (since $\det M(m) = 1 \implies \gcd(a_m + c_m, b_m + d_m) = 1$).

Direct $2 \times 2$ matrix multiplication gives:
1. $P(2) = M(2) J = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 2 & -1 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix} = H(1) H(2)$.
2. $J^{-1} L J = \begin{pmatrix} 0 & 1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ 1 & 0 \end{pmatrix} = H(2)$.
3. $J^{-1} R J = \begin{pmatrix} 0 & 1 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$, and for every integer $c$:
   $$H(c) (J^{-1} R J) = \begin{pmatrix} c & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} c + 1 & -1 \\ 1 & 0 \end{pmatrix} = H(c + 1).$$

### Step 3: Structural Induction on $n \ge 2$
We claim that for every $n \ge 2$, there exist $k \ge 1$ and integers $c_1, \dots, c_k \ge 2$ such that
$$P(n) = H(1) H(c_1) \cdots H(c_k).$$
- **Base case $n = 2$:** $P(2) = H(1) H(2)$ ($k = 1, c_1 = 2 \ge 2$).
- **Inductive step:** Assuming $P(m) = H(1) H(c_1) \cdots H(c_k)$ with $k \ge 1$ and $c_1, \dots, c_k \ge 2$:
  - For $n = 2m - 1$: $P(2m - 1) = M(m) L J = P(m) (J^{-1} L J) = H(1) H(c_1) \cdots H(c_k) H(2)$, appending $c_{k+1} = 2 \ge 2$.
  - For $n = 2m$: $P(2m) = M(m) R J = P(m) (J^{-1} R J) = H(1) H(c_1) \cdots H(c_{k-1}) H(c_k + 1)$, increasing the last term $c_k \mapsto c_k + 1 \ge 3$.

Since $c_1, \dots, c_k \ge 2$, $[[1; c_1, \dots, c_k]]$ is the unique canonical Hirzebruch continued fraction of $r(n)$ (the fraction represented by the first column of $P(n)$). Let $S(n) := 1 + c_1 + \dots + c_k$ be the sum of its terms for $n \ge 2$. By the induction step:
$$S(2) = 1 + 2 = 3, \qquad S(2m - 1) = S(m) + 2, \qquad S(2m) = S(m) + 1 \qquad (m \ge 2).$$

Meanwhile, the OEIS `A061313` recurrence gives $a(2) = a(1) + 1 = 1$, $a(2m) = a(m) + 1$, and $a(2m - 1) = a(2(m-1) + 1) = a(m) + 2$ for all $m \ge 2$. Hence $T(n) := a(n) + 2$ satisfies the identical initial value and recurrence:
$$T(2) = 3 = S(2), \qquad T(2m - 1) = T(m) + 2, \qquad T(2m) = T(m) + 1 \qquad (m \ge 2).$$
By induction on $n \ge 2$, $a(n) + 2 = S(n)$ for all $n \ge 2$.

Finally, at $n = 1$, $r(1) = 1/1$ has unique canonical Hirzebruch continued fraction $[[1]]$ with sum $1 \neq 2 = a(1) + 2$. $\square$

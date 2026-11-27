# Proof of OEIS A119262 Benedict W. J. Irwin (2017) Determinant Conjecture

## Theorem
Let $(a(n))_{n \ge 0}$ be defined by $a(0) = 0$, $a(1) = 1$, and
$$
a(n) = \sum_{k=1}^{\lfloor n/2 \rfloor} a(k)\binom{n - k - 1}{n - 2k} \qquad (n \ge 2).
$$
For each integer $n \ge 1$, let $M_n = (m_{i,j})_{1 \le i,j \le n}$ be the $n \times n$ matrix with entries
$$
m_{i,j} =
\begin{cases}
0 & \text{if } i < j - 1, \\
-1 & \text{if } i = j - 1, \\
\binom{i - j}{n - i} & \text{if } i \ge j,
\end{cases}
$$
where $\binom{u}{v} := 0$ whenever $u < v$ or $v < 0$. Then $\det(M_n) = a(n+1)$ for every integer $n \ge 1$.

## Proof

### Step 1: Index reversal to a fixed infinite upper-Hessenberg matrix
Fix $n \ge 1$ and reverse both row and column orders by setting $r = n - i$ and $c = n - j$ for $0 \le r, c \le n - 1$. Define the $n \times n$ matrix $B_n = (b_{r,c})_{0 \le r,c \le n-1}$ by $b_{r,c} := m_{n-r, n-c}$. Then:
- $n - r < (n - c) - 1 \iff r > c + 1$, giving $b_{r,c} = 0$;
- $n - r = (n - c) - 1 \iff r = c + 1$, giving $b_{r,c} = -1$;
- $n - r \ge n - c \iff r \le c$, giving $b_{r,c} = \binom{(n-r)-(n-c)}{n-(n-r)} = \binom{c - r}{r}$.

Since $B_n = P_n M_n P_n^{-1}$ where $P_n$ is the order-reversing permutation matrix, we have $\det(M_n) = \det(B_n)$. Moreover, the entry formula
$$
b_{r,c} =
\begin{cases}
0 & \text{if } r > c + 1, \\
-1 & \text{if } r = c + 1, \\
\binom{c - r}{r} & \text{if } r \le c
\end{cases}
$$
is independent of $n$, so each $B_n$ is the leading $n \times n$ principal submatrix ($0 \le r, c \le n - 1$) of a single infinite upper-Hessenberg matrix $B = (b_{r,c})_{r,c \ge 0}$.

### Step 2: Laplace expansion along the last column
Set $d_0 := 1$ and $d_n := \det(B_n)$ for $n \ge 1$ (so $d_1 = \det([\binom{0}{0}]) = 1$). Fix $n \ge 1$ and expand $\det(B_n)$ along its last column $c = n - 1$:
$$
d_n = \sum_{r=0}^{n-1} (-1)^{r + (n - 1)} b_{r, n-1} \det\bigl(B_n^{(r, n-1)}\bigr),
$$
where $B_n^{(r, n-1)}$ is the $(n-1) \times (n-1)$ submatrix obtained by deleting row $r$ and column $n - 1$.

Inspect the block structure of $B_n^{(r, n-1)}$ for each $0 \le r \le n - 1$:
- For rows $r' \in \{r + 1, \dots, n - 1\}$ and columns $c' \in \{0, \dots, r - 1\}$, we have $r' \ge r + 1 > (r - 1) + 1 \ge c' + 1$, so $b_{r', c'} = 0$. Hence $B_n^{(r, n-1)}$ is block upper-triangular with two diagonal blocks:
  1. The top-left $r \times r$ block (rows $0, \dots, r - 1$ and columns $0, \dots, r - 1$), which equals $B_r$ and has determinant $d_r$ (with the $0 \times 0$ block at $r = 0$ having determinant $1 = d_0$).
  2. The bottom-right $(n - 1 - r) \times (n - 1 - r)$ block (rows $r + 1, \dots, n - 1$ and columns $r, \dots, n - 2$). Indexing its entries by $0 \le t, s \le n - 2 - r$ with row $r + 1 + t$ and column $r + s$, we have $r + 1 + t > (r + s) + 1 \iff t > s$ (so all entries strictly below the main diagonal are $0$), while on the main diagonal $t = s$ the entries are $b_{r + 1 + t, r + t} = -1$. Thus this block is upper-triangular with determinant $(-1)^{n - 1 - r}$.

Multiplying the two block determinants gives $\det(B_n^{(r, n-1)}) = (-1)^{n - 1 - r} d_r$ for every $0 \le r \le n - 1$. Since $(-1)^{r + (n - 1)} (-1)^{n - 1 - r} = (-1)^{2(n-1)} = 1$ and $b_{r, n-1} = \binom{n - 1 - r}{r}$, we obtain for every $n \ge 1$:
$$
d_n = \sum_{r=0}^{n-1} \binom{n - 1 - r}{r} d_r.
$$

### Step 3: Identification with $a(n+1)$
Note that $\binom{n - 1 - r}{r} = 0$ whenever $r > \lfloor (n-1)/2 \rfloor$ (since then $0 \le n - 1 - r < r$). Reindexing by $k = r + 1$ ($1 \le k \le \lfloor (n+1)/2 \rfloor$) and using binomial symmetry $\binom{n - k}{k - 1} = \binom{n - k}{n + 1 - 2k}$ (for $k - 1 \le n - k$, i.e. $k \le \lfloor (n+1)/2 \rfloor$) gives
$$
d_n = \sum_{k=1}^{\lfloor (n+1)/2 \rfloor} d_{k-1} \binom{n - k}{n + 1 - 2k} \qquad (n \ge 1).
$$
Since $d_0 = 1 = a(1)$ and $a(n+1)$ satisfies the exact same recurrence $a(n+1) = \sum_{k=1}^{\lfloor (n+1)/2 \rfloor} a(k) \binom{n - k}{n + 1 - 2k}$ for all $n \ge 1$, strong induction on $n \ge 0$ yields $d_n = a(n+1)$ for all $n \ge 0$. In particular, $\det(M_n) = \det(B_n) = d_n = a(n+1)$ for every integer $n \ge 1$. $\blacksquare$

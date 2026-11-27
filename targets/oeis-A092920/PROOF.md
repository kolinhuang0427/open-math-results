# Proof of OEIS A092920 Conjecture (Kurkov 2023)

## Theorem
Let $a(n)$ ($n \ge 0$) be **OEIS A092920**, the number of strongly monotone partitions of $[n] = \{1, \dots, n\}$ (with $a(0) = 1$), i.e. set partitions whose blocks can be simultaneously ordered by increasing minimum element and increasing maximum element. Define $(b(r))_{r \ge 0}$ recursively by $b(0) = 1$ and, for $m, n \ge 0$,
$$b\bigl(2^m (2n + 1)\bigr) = \sum_{k=0}^{[m > 0](m-1)} \binom{m - 1}{k} b(2^k n)$$
(where for $m = 0$, the single term $k = 0$ uses $\binom{-1}{0} = 1$, giving $b(2n+1) = b(n)$). Then for all $n > 0$,
$$a(n) = \sum_{k=0}^{2^{n-1}-1} b(k).$$

---

## Proof

### 1. Generating function of strongly monotone partitions
Recall that a partition $\pi$ of $[n]$ ($n \ge 1$) is strongly monotone iff, ordering its blocks $B_1, \dots, B_q$ by $\min B_1 < \dots < \min B_q$, one also has $\max B_1 < \dots < \max B_q$. Let $\mathcal{M}_n$ be the set of labeled Motzkin paths of length $n$ from height $0$ to height $0$, where steps are:
- at height $0$: horizontal step $H_0$ (1 label) or up-step $U$ to height $1$ (1 label);
- at height $h \ge 1$: up-step $U$ to $h+1$ (1 label), down-step $D$ to $h-1$ (1 label), or horizontal step $H^{(r)}$ labeled by $r \in \{1, \dots, h\}$ ($h$ labels).

We construct an explicit bijection $\Phi$ between strongly monotone partitions $\pi$ of $[n]$ and $\mathcal{M}_n$. Scan $t = 1, 2, \dots, n$ while maintaining the queue $Q$ of currently open blocks $B$ with $\min B \le t < \max B$, ordered by $\min B$ (initially $Q$ is empty, and write $h = |Q|$):
- If $\{t\}$ is a singleton block in $\pi$, then no other block can have $\min B < t < \max B$ (otherwise $\{t\}$ would violate strong monotonicity relative to $B$: either $\min B < \min \{t\}$ with $\max B > \max \{t\}$, or vice versa). Thus $h = 0$, and we record step $H_0$.
- If $t = \min B$ for a non-singleton block $B$, we append $B$ to the back of $Q$ and record step $U$.
- If $t = \max B$ for a non-singleton block $B$, then because blocks in $Q$ were opened in increasing order of $\min$ and $\pi$ is strongly monotone, $B$ must be the earliest block $Q[0]$. We pop $Q[0]$ and record step $D$.
- Otherwise $\min B < t < \max B$, so $B = Q[r-1]$ for a unique $r \in \{1, \dots, h\}$ ($h \ge 1$), and we record $H^{(r)}$.

Conversely, given a path in $\mathcal{M}_n$, replaying these rules on a FIFO queue $Q$ of open blocks puts each $t$ into a unique block: $U$ opens a new block at the back of $Q$, $D$ closes $Q[0]$, $H^{(r)}$ inserts $t$ into $Q[r-1]$, and $H_0$ (only at $h=0$) creates singleton $\{t\}$. Non-singleton blocks are opened and closed in strict FIFO order so both $\min$ and $\max$ strictly increase, while singletons occur only when $Q$ is empty and therefore precede all later blocks and follow all earlier blocks in both $\min$ and $\max$. Hence $\Phi$ is a bijection.

For $m \ge 0$, let $P_m(x) \in 1 + x\mathbb{Q}[[x]]$ be the ordinary generating function of labeled Motzkin paths starting and ending at height $m$ without dropping below height $m$. By first-return decomposition at the base height $m$:
- At $m = 0$, $P_0(x) = 1 + x P_0(x) + x^2 P_1(x) P_0(x)$, so $A(x) := \sum_{n \ge 0} a(n) x^n = P_0(x) = \frac{1}{1 - x - x^2 P_1(x)}$.
- At $m \ge 1$, the horizontal step weight at base height $m$ is $m$, so $P_m(x) = 1 + m x P_m(x) + x^2 P_{m+1}(x) P_m(x)$. Setting $B_m(x) := P_{m+1}(x)$ for all $m \ge 0$, we obtain
  $$A(x) = \frac{1}{1 - x - x^2 B_0(x)}, \qquad B_m(x) = \frac{1}{1 - (m+1)x - x^2 B_{m+1}(x)} \quad (\forall m \ge 0).$$

---

### 2. Differential equation for the binary-sum EGF
For $N \ge 0$ and $j \ge 0$, define
$$R_j(N) = \sum_{r=0}^{2^N - 1} b(2^j r), \qquad F_N(z) = \sum_{j=0}^\infty R_j(N) \frac{z^j}{j!} \in \mathbb{Q}[[z]].$$
Note that $R_0(N) = \sum_{r=0}^{2^N-1} b(r)$ is the conjectured value of $a(N + 1)$ for $N \ge 0$.

- For $N = 0$, $R_j(0) = b(0) = 1$ for all $j \ge 0$, so $F_0(z) = e^z$.
- For $N \ge 1$, splitting $r \in \{0, \dots, 2^N - 1\}$ into even $r = 2y$ ($0 \le y < 2^{N-1}$) and odd $r = 2n + 1$ ($0 \le n < 2^{N-1}$):
  - When $j = 0$, using $b(2n+1) = b(n)$ gives
    $$R_0(N) = \sum_{y=0}^{2^{N-1}-1} b(2y) + \sum_{n=0}^{2^{N-1}-1} b(n) = R_1(N-1) + R_0(N-1).$$
  - When $j \ge 1$, $2^j(2n+1)$ has $2$-adic valuation $j \ge 1$, so the defining recurrence gives $b(2^j(2n+1)) = \sum_{k=0}^{j-1} \binom{j-1}{k} b(2^k n)$. Summing over $n$ and $y$ yields
    $$R_j(N) = R_{j+1}(N-1) + \sum_{k=0}^{j-1} \binom{j-1}{k} R_k(N-1) \quad (j \ge 1).$$

Multiplying by $\frac{z^{j-1}}{(j-1)!}$ and summing over $j \ge 1$ inside $\mathbb{Q}[[z]]$ gives, for all $N \ge 1$,
$$F_N'(z) = F_{N-1}''(z) + e^z F_{N-1}(z), \qquad F_N(0) = F_{N-1}(0) + F_{N-1}'(0).$$
By induction on $N \ge 0$, each $F_N(z)$ is a finite linear combination of $\{1, e^z, e^{2z}, \dots, e^{(N+1)z}\}$: $F_0(z) = e^z$, and if $F_{N-1}(z) = \sum_{k=0}^N c_k e^{kz}$, then $F_{N-1}''(z) + e^z F_{N-1}(z)$ has zero constant term and degree $\le N+1$ in $e^z$, so its unique antiderivative matching $F_N(0)$ at $z = 0$ has the same form with degree $\le N+1$.

Writing $u = e^z$ and defining the bivariate formal series
$$H(x, u) = 1 + x \sum_{N=0}^\infty F_N(z) x^N = \sum_{k=0}^\infty p_k(x) u^k,$$
we note that $H(x, 1) = 1 + \sum_{N=0}^\infty R_0(N) x^{N+1}$ is the conjectured generating function, and since $F_N(u)$ has $u$-degree $\le N+1$, each $p_k(x)$ lies in $x^k \mathbb{Q}[[x]]$. Summing $x^{N+1} F_N'(z) = x^{N+1}(F_{N-1}''(z) + e^z F_{N-1}(z))$ over $N \ge 1$ with $F_0'(z) = e^z$ gives, with $\partial_z = u \partial_u$:
$$\partial_z H - x e^z = x \partial_z^2 (H - 1) + x e^z (H - 1) \implies x \partial_z^2 H - \partial_z H + x e^z H = 0.$$
Substituting $\partial_z = u \partial_u$ and $\partial_z^2 = u \partial_u + u^2 \partial_u^2$ and dividing by $u$ yields
$$x u \, \partial_u^2 H(x, u) + (x - 1) \partial_u H(x, u) + x H(x, u) = 0.$$
Summing $F_N(0) = F_{N-1}(0) + F_{N-1}'(0)$ over $N \ge 1$ with $F_0(0) = 1$ gives $H(x, 1) - 1 = x H(x, 1) + x \partial_u H(x, 1)$, i.e.,
$$(1 - x) H(x, 1) - x \, \partial_u H(x, 1) = 1.$$

---

### 3. Hypergeometric solution and continued-fraction identification
Extracting $[u^k]$ from $x u \, \partial_u^2 H + (x - 1) \partial_u H + x H = 0$ for each $k \ge 0$ gives
$$(k + 1)\bigl((k + 1)x - 1\bigr) p_{k+1}(x) + x p_k(x) = 0 \implies p_{k+1}(x) = \frac{x}{(k+1)\bigl(1 - (k+1)x\bigr)} p_k(x).$$
Hence in $\mathbb{Q}[[x]]$,
$$p_k(x) = p_0(x) \, \frac{x^k}{k! \prod_{j=1}^k (1 - jx)} \qquad (\forall k \ge 0).$$
Since $p_k(x) \in x^k \mathbb{Q}[[x]]$, evaluation at $u = 1$ converges $x$-adically in $\mathbb{Q}[[x]]$:
$$H(x, 1) = p_0(x) S_0(x), \qquad \partial_u H(x, 1) = p_0(x) S_1(x),$$
where
$$S_0(x) = \sum_{k=0}^\infty \frac{x^k}{k! \prod_{j=1}^k (1 - jx)}, \qquad S_1(x) = \sum_{k=1}^\infty \frac{x^k}{(k-1)! \prod_{j=1}^k (1 - jx)}.$$
From $(1 - x) H(x, 1) - x \, \partial_u H(x, 1) = 1$, we obtain $p_0(x) = \bigl((1-x)S_0(x) - x S_1(x)\bigr)^{-1}$ and therefore
$$H(x, 1) = \frac{S_0(x)}{(1 - x) S_0(x) - x S_1(x)} = \frac{1}{1 - x - x \frac{S_1(x)}{S_0(x)}}.$$

For each $m \ge 0$, define the formal power series $U_m(x) = \sum_{r=0}^\infty c_{m, r}(x) \in 1 + x\mathbb{Q}[[x]]$, where
$$c_{m, r}(x) = \frac{x^r}{r! \prod_{j=1}^r \bigl(1 - (m + j)x\bigr)} \in x^r \mathbb{Q}[[x]].$$
Note that $U_0(x) = S_0(x)$, and for every $m \ge 0$ and $r \ge 1$,
$$r c_{m, r}(x) = \frac{x}{1 - (m+1)x} c_{m+1, r-1}(x) \implies \sum_{r=1}^\infty r c_{m, r}(x) = \frac{x}{1 - (m+1)x} U_{m+1}(x);$$
in particular ($m = 0$), $S_1(x) = \frac{x}{1 - x} U_1(x)$. Furthermore, for every $m \ge 0$ and $r \ge 0$,
$$(1 - (m+1)x) c_{m, r}(x) = \bigl(1 - (m + r + 1)x\bigr) c_{m+1, r}(x) = (1 - (m+1)x) c_{m+1, r}(x) - x \cdot r c_{m+1, r}(x)$$
(for $r = 0$ both sides equal $1 - (m+1)x$; for $r \ge 1$ both equal $\frac{x^r}{r! \prod_{j=2}^r (1 - (m+j)x)}$). Summing over $r \ge 0$ gives
$$(1 - (m+1)x) U_m(x) = (1 - (m+1)x) U_{m+1}(x) - \frac{x^2}{1 - (m+2)x} U_{m+2}(x).$$
Setting $C_m(x) := \frac{U_{m+1}(x)}{(1 - (m+1)x) U_m(x)} \in 1 + x\mathbb{Q}[[x]]$ ($m \ge 0$), dividing by $(1 - (m+1)x) U_{m+1}(x)$ gives
$$\frac{1}{(1 - (m+1)x) C_m(x)} = 1 - \frac{x^2}{1 - (m+1)x} C_{m+1}(x) \implies C_m(x) = \frac{1}{1 - (m+1)x - x^2 C_{m+1}(x)}.$$
Comparing with $B_m(x)$ from Section 1 (both lie in $1 + x\mathbb{Q}[[x]]$) gives
$$C_m(x) - B_m(x) = \frac{x^2 \bigl(C_{m+1}(x) - B_{m+1}(x)\bigr)}{\bigl(1 - (m+1)x - x^2 C_{m+1}(x)\bigr)\bigl(1 - (m+1)x - x^2 B_{m+1}(x)\bigr)} \in x^2\bigl(C_{m+1}(x) - B_{m+1}(x)\bigr)\mathbb{Q}[[x]].$$
By induction on $K \ge 1$, $C_0(x) - B_0(x) \in x^{2K} \mathbb{Q}[[x]]$ for all $K \ge 1$, hence $C_0(x) = B_0(x)$ in $\mathbb{Q}[[x]]$. Since $C_0(x) = \frac{U_1(x)}{(1-x) U_0(x)} = \frac{S_1(x)}{x S_0(x)}$, it follows that
$$H(x, 1) = \frac{1}{1 - x - x^2 C_0(x)} = \frac{1}{1 - x - x^2 B_0(x)} = A(x),$$
and equating coefficients of $x^n$ ($n > 0$) yields $a(n) = R_0(n-1) = \sum_{k=0}^{2^{n-1}-1} b(k)$. $\blacksquare$

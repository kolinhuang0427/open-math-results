# Proof of OEIS A125790 (Mikhail Kurkov 2025 Row Generating Function Conjecture)

## Theorem
Let $(T(n, k))_{n, k \ge 0}$ be the array defined in OEIS `A125790` by
$$T(0, k) = 1 \quad (k \ge 0), \qquad T(n, 0) = 1 \quad (n \ge 0), \qquad T(n, k) = T(n, k-1) + T(n-1, 2k) \quad (n, k \ge 1).$$
Then for every integer $n \ge 1$, the ordinary generating function of the $n$-th row $F_n(x) := \sum_{k=0}^{\infty} T(n, k) x^k$ is
$$F_n(x) = \frac{\sum_{i=0}^{n-1} x^i \sum_{j=0}^{i} \binom{n+1}{j} T(n, i - j) (-1)^j}{(1 - x)^{n+1}}.$$

---

## Proof

### Step 1: Polynomiality and Boundary Vanishing at $k = -1$
We prove by induction on $n \ge 0$ that there exists a polynomial $P_n(t) \in \mathbb{Q}[t]$ of degree at most $n$ such that:
1. $P_n(k) = T(n, k)$ for all integers $k \ge 0$, and
2. for all $n \ge 1$, $P_n(-1) = 0$.

**Base case $n = 0$:** Set $P_0(t) := 1 \in \mathbb{Q}[t]$, which has $\deg P_0 = 0 \le 0$ and $P_0(k) = 1 = T(0, k)$ for all $k \ge 0$.

**Inductive step ($n \ge 1$):** Assume $P_{n-1}(t) \in \mathbb{Q}[t]$ satisfies $\deg P_{n-1} \le n - 1$ and $P_{n-1}(k) = T(n-1, k)$ for all $k \ge 0$.
Since the backward difference operator $(\nabla f)(t) := f(t) - f(t-1)$ is a linear map from the $n$-dimensional $\mathbb{Q}$-vector space $V_n := \{f \in \mathbb{Q}[t] : \deg f \le n,\; f(0) = 0\}$ to the $n$-dimensional space $W_{n-1} := \{g \in \mathbb{Q}[t] : \deg g \le n - 1\}$ with trivial kernel (if $f(t) = f(t-1)$ for all $t$, then $f$ is constant, and $f(0)=0$ forces $f \equiv 0$), $\nabla : V_n \to W_{n-1}$ is an isomorphism. Hence there exists a unique polynomial $P_n(t) \in \mathbb{Q}[t]$ of degree at most $n$ such that
$$P_n(0) = 1 \qquad \text{and} \qquad P_n(t) - P_n(t - 1) = P_{n-1}(2t) \quad \text{in } \mathbb{Q}[t].$$
For $k \ge 0$, $P_n(0) = 1 = T(n, 0)$ and, by induction on $k \ge 1$,
$$P_n(k) = P_n(k - 1) + P_{n-1}(2k) = T(n, k - 1) + T(n - 1, 2k) = T(n, k),$$
giving (1). Moreover, evaluating the polynomial identity $P_n(t) - P_n(t - 1) = P_{n-1}(2t)$ at $t = 0$ yields
$$P_n(-1) = P_n(0) - P_{n-1}(0) = T(n, 0) - T(n - 1, 0) = 1 - 1 = 0,$$
giving (2).

### Step 2: Vanishing of Numerator Coefficients for $i \ge n$
Fix $n \ge 1$ and multiply $F_n(x) = \sum_{k=0}^{\infty} T(n, k) x^k$ by $(1 - x)^{n+1} = \sum_{j=0}^{n+1} \binom{n+1}{j} (-1)^j x^j$ in $\mathbb{Q}[[x]]$:
$$(1 - x)^{n+1} F_n(x) = \sum_{i=0}^{\infty} c_i x^i, \qquad c_i := \sum_{j=0}^{\min(i, n+1)} \binom{n+1}{j} (-1)^j T(n, i - j).$$
Note that for any polynomial $P(t)$ of degree $\le n$, the $(n+1)$-th backward difference vanishes identically:
$$\sum_{j=0}^{n+1} \binom{n+1}{j} (-1)^j P(i - j) = 0 \qquad \forall i \in \mathbb{Z}.$$
Applying this to $P = P_n$:
- For every $i \ge n + 1$, every index $i - j$ ($0 \le j \le n + 1$) satisfies $i - j \ge 0$, so $T(n, i - j) = P_n(i - j)$ and hence $c_i = 0$.
- For $i = n$, the indices $0 \le j \le n$ have $n - j \ge 0$ (where $T(n, n-j) = P_n(n-j)$), while the $j = n + 1$ term has $P_n(n - (n+1)) = P_n(-1) = 0$ by Step 1(2). Thus
  $$c_n = \sum_{j=0}^{n} \binom{n+1}{j} (-1)^j P_n(n - j) = \sum_{j=0}^{n+1} \binom{n+1}{j} (-1)^j P_n(n - j) = 0.$$

Therefore $c_i = 0$ for all $i \ge n$, so
$$(1 - x)^{n+1} F_n(x) = \sum_{i=0}^{n-1} x^i \sum_{j=0}^{i} \binom{n+1}{j} T(n, i - j) (-1)^j.$$
Dividing by $(1 - x)^{n+1}$ yields the conjectured identity for all $n \ge 1$. $\square$

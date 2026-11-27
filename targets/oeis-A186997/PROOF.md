# Proof of OEIS A186997 Peter Bala (2016) 2-Adic Valuation Conjectures

## Theorem
Let $A(x) = \sum_{k \ge 0} a(k) x^k \in \mathbb{Z}[[x]]$ be the unique formal power series satisfying
$$
A(x) = 1 + x A(x)^3 + x^2 A(x)^4,
$$
and let $C_m = \frac{1}{m+1}\binom{2m}{m}$ (`A000108`) denote the $m$-th Catalan number. Letting $v_2(\cdot)$ denote the $2$-adic valuation:
1. For every integer $m \ge 0$,
   $$v_2\bigl(a(2m+1)\bigr) = v_2(C_{2m+1}) = v_2(C_m).$$
2. For every integer $m \ge 2$,
   $$v_2\bigl(a(2m)\bigr) = 3 + v_2(C_{m-2}).$$

## Proof

### Step 1: Series reversion and binomial sum for $(2k+1) a(k)$
Define $W(x) := x A(x^2) = \sum_{k \ge 0} a(k) x^{2k+1} \in x\mathbb{Z}[[x]]$. Substituting $x \mapsto x^2$ into $A(x) = 1 + x A(x)^3 + x^2 A(x)^4$ and multiplying by $x$ gives
$$
W(x) = x + W(x)^3 + x W(x)^4 \iff W(x)\bigl(1 - W(x)^2\bigr) = x\bigl(1 + W(x)^4\bigr),
$$
so $\frac{W(x)(1 - W(x)^2)}{1 + W(x)^4} = x$ in $\mathbb{Z}[[x]]$. Applying the Lagrange Inversion Formula to $W(x) = x\,\phi(W(x))$ with $\phi(w) = \frac{1 + w^4}{1 - w^2}$, we obtain for every $k \ge 0$:
$$
a(k) = [x^{2k+1}] W(x) = \frac{1}{2k+1} [w^{2k}] \left(\frac{1 + w^4}{1 - w^2}\right)^{2k+1} = \frac{1}{2k+1} [z^k] \left(\frac{1 + z^2}{1 - z}\right)^{2k+1},
$$
setting $z = w^2$. Writing $1 + z^2 = (1 - z)^2 + 2z$ and expanding by the binomial theorem yields
$$
\left(\frac{1 + z^2}{1 - z}\right)^{2k+1} = \sum_{j=0}^{2k+1} \binom{2k+1}{j} (2z)^j (1 - z)^{2k+1-2j}.
$$
Terms with $j > k$ have no $z^k$ term, while for $0 \le j \le k$ the exponent $2k + 1 - 2j \ge 1$ is a positive integer, so extracting $[z^k]$ gives
$$
(2k+1)\, a(k) = \sum_{j=0}^{k} t_j, \qquad t_j := (-1)^{k-j} 2^j \binom{2k+1}{j} \binom{2k+1-2j}{k-j}.
$$
Since $2k + 1$ is odd, $v_2(a(k)) = v_2\bigl((2k+1) a(k)\bigr) = v_2\bigl(\sum_{j=0}^k t_j\bigr)$.

### Step 2: Legendre/Kummer valuation formulas
Let $s_2(M)$ denote the binary digit sum of $M \in \mathbb{Z}_{\ge 0}$. By Legendre's formula $v_2(M!) = M - s_2(M)$, we have $v_2\binom{a}{b} = s_2(b) + s_2(a-b) - s_2(a)$ for $0 \le b \le a$. In particular:
- Since $s_2(2m) = s_2(m)$ and $s_2(m+1) = s_2(m) + 1 - v_2(m+1)$,
  $$v_2(C_m) = v_2\binom{2m}{m} - v_2(m+1) = s_2(m) - v_2(m+1) = s_2(m+1) - 1 \qquad (m \ge 0).$$
- For every $0 \le j \le k$, since $2k+1-2j = 2(k-j)+1$ satisfies $s_2(2k+1-2j) = s_2(k-j) + 1$,
  $$v_2\binom{2k+1-2j}{k-j} = s_2(k-j) + s_2(k+1-j) - \bigl(s_2(k-j) + 1\bigr) = s_2(k+1-j) - 1,$$
  so
  $$v_2(t_j) = j + v_2\binom{2k+1}{j} + s_2(k+1-j) - 1.$$
- Since $v_2\binom{A+B}{A} \ge 0$, subadditivity $s_2(A) + s_2(B) \ge s_2(A+B)$ holds for all $A, B \ge 0$. Taking $A = k+1-j$ and $B = j$ gives $s_2(k+1-j) \ge s_2(k+1) - s_2(j)$.

### Step 3: Odd indices $k = 2m + 1$ ($m \ge 0$)
First, $v_2(C_{2m+1}) = s_2(2m+2) - 1 = s_2(m+1) - 1 = v_2(C_m)$.

Now analyze $t_j$ for $k = 2m + 1$:
- **$j = 0$:** $|t_0| = \binom{2k+1}{k} = (2k+1) C_k$, so $v_2(t_0) = v_2(C_{2m+1}) = v_2(C_m)$.
- **$j = 1$:** $|t_1| = 2(2k+1)\binom{2k-1}{k-1} = (2k+1)\binom{2k}{k} = (2k+1)(k+1) C_k$. Since $k+1 = 2(m+1)$ is even,
  $$v_2(t_1) = 1 + v_2(m+1) + v_2(C_k) > v_2(t_0).$$
- **$2 \le j \le k$:** Using $v_2\binom{2k+1}{j} \ge 0$ and $s_2(k+1-j) \ge s_2(k+1) - s_2(j)$,
  $$v_2(t_j) \ge j + s_2(k+1) - s_2(j) - 1 = \bigl(s_2(m+1) - 1\bigr) + \bigl(j - s_2(j)\bigr) = v_2(C_m) + v_2(j!).$$
  Since $v_2(j!) \ge 1$ for all $j \ge 2$, we have $v_2(t_j) \ge v_2(C_m) + 1 > v_2(t_0)$.

Since $v_2(t_j) > v_2(t_0)$ for every $1 \le j \le k$, the ultrametric inequality yields $v_2(a(2m+1)) = v_2(t_0) = v_2(C_{2m+1}) = v_2(C_m)$.

### Step 4: Even indices $k = 2m$ ($m \ge 2$)
Combine $t_0$ and $t_1$:
$$
t_0 + t_1 = \binom{2k+1}{k} - 2(2k+1)\binom{2k-1}{k-1} = \binom{2k+1}{k} - (k+1)\binom{2k+1}{k} = -k\binom{2k+1}{k}.
$$
With $k = 2m$, we have $s_2(4m+1) = s_2(2m+1) = s_2(m) + 1$ and $s_2(2m) = s_2(m)$, so $v_2\binom{4m+1}{2m} = s_2(m)$. Since $s_2(m-1) = s_2(m) - 1 + v_2(m)$ for $m \ge 2$,
$$
v_2(t_0 + t_1) = v_2(2m) + s_2(m) = 1 + v_2(m) + s_2(m) = 3 + \bigl(s_2(m-1) - 1\bigr) = 3 + v_2(C_{m-2}).
$$

Set $r := v_2(m) + 2 \ge 2$, so $v_2(4m) = r$ and $v_2(t_0 + t_1) = s_2(m) + r - 1$. Consider any $j \in \{2, \dots, k\}$:
- **Case A ($2 \le j \le 2^r - 1$):** Because $4m \equiv 0 \pmod{2^r}$, the binary expansion of $4m - 1$ ends in $r$ ones. Thus for every $1 \le i \le 2^r - 1$, subtracting $i - 1 \le 2^r - 2$ from $4m - 1$ produces no borrows, so $v_2\binom{4m-1}{i-1} = 0$ by Kummer's theorem. From $\binom{4m}{i} = \frac{4m}{i}\binom{4m-1}{i-1}$ we obtain $v_2\binom{4m}{i} = r - v_2(i)$ for all $1 \le i \le 2^r - 1$. Applying Pascal's identity $\binom{4m+1}{j} = \binom{4m}{j} + \binom{4m}{j-1}$ and noting that $\min(v_2(j), v_2(j-1)) = 0 \ne \max(v_2(j), v_2(j-1))$ gives
  $$v_2\binom{4m+1}{j} = \min\bigl(r - v_2(j),\, r - v_2(j-1)\bigr) = r - \max\bigl(v_2(j), v_2(j-1)\bigr).$$
  Together with $s_2(k+1-j) - 1 \ge s_2(2m+1) - 1 - s_2(j) = s_2(m) - s_2(j)$, this gives
  $$v_2(t_j) \ge s_2(m) + r + \Bigl(j - s_2(j) - \max\bigl(v_2(j), v_2(j-1)\bigr)\Bigr).$$
  We claim $j - s_2(j) - v \ge 0$ for all $j \ge 2$, where $v := \max(v_2(j), v_2(j-1)) \ge 1$. Indeed, for $j \in \{2, 3\}$ we have $v=1$ and $2-1-1 = 3-2-1 = 0$; for $j \ge 4$, write $j = 2^v q$ or $j = 2^v q + 1$ with odd $q \ge 1$ (and $q \ge 3$ if $v = 1$). Since $s_2(q) \le q$, in either case $s_2(j) \le q + 1$ with $s_2(2^v q) \le q$, so
  $$j - s_2(j) - v \ge (2^v - 1)q - v \ge 0.$$
  Hence $v_2(t_j) \ge s_2(m) + r > v_2(t_0 + t_1)$.
- **Case B ($j \ge 2^r$):** Using $v_2\binom{4m+1}{j} \ge 0$ and $s_2(k+1-j) - 1 \ge s_2(m) - s_2(j)$ gives $v_2(t_j) \ge s_2(m) + j - s_2(j)$. Writing $j = 2^b + d$ with $b = \lfloor \log_2 j \rfloor \ge r \ge 2$ and $0 \le d < 2^b$, we have $s_2(j) = 1 + s_2(d) \le 1 + d$, hence
  $$j - s_2(j) \ge 2^b - 1 \ge 2^r - 1 \ge r + 1 > r - 1 \qquad (\forall r \ge 2).$$
  Thus $v_2(t_j) \ge s_2(m) + r + 1 > v_2(t_0 + t_1)$.

Since $v_2(t_j) > v_2(t_0 + t_1)$ for every $2 \le j \le k$, the ultrametric inequality gives $v_2(a(2m)) = v_2(t_0 + t_1) = 3 + v_2(C_{m-2})$ for all $m \ge 2$. $\blacksquare$

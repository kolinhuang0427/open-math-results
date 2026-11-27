# Disproof of Conjecture 9 of Chervov et al. (arXiv:2509.19162v2)

## Result

**Conjecture 9 of Chervov et al. (`arXiv:2509.19162v2`) is FALSE.**

Let $U(n, \mathbb{F}_2) = U(n, \mathbb{Z}/2\mathbb{Z})$ denote the group of $n \times n$ upper unitriangular matrices over $\mathbb{F}_2$, with generating set $S = \{s_1, \dots, s_{n-1}\}$ where $s_k = I + E_{k, k+1}$ ($1 \le k \le n-1$, 1-indexed) are the fundamental root transvections. Since $s_k^2 = I$ in characteristic $2$, the undirected and oriented Cayley graphs coincide. Let $M(n)$ denote the number of isomorphism classes of metacyclic groups of order $2^n$ (OEIS A136184).

We prove:
1. **(Immediate small-case failure at $n = 2$):** $\mathrm{diam}(U(2, \mathbb{F}_2)) = 1 < 2 = M(2)$ (where the two metacyclic groups of order $4$ are $C_4$ and $C_2 \times C_2$).
2. **(Quadratic upper bound for all $n \ge 2$):**
   $$\mathrm{diam}(U(n, \mathbb{F}_2)) \le 2n^2 - 6n + 5.$$
3. **(Explicit cubic lower bound for $M(n)$):** For every $n \ge 6$, an explicit elementary family $\mathcal{F}_n$ gives at least
   $$M(n) \ge |\mathcal{F}_n| = \sum_{a=3}^{\lfloor n/2 \rfloor} \sum_{s=2}^{a-1} \bigl(\min(s, a-s) + 1\bigr) = \Theta(n^3)$$
   pairwise non-isomorphic metacyclic groups of order $2^n$.
4. **(Asymptotic & concrete refutation for all $n \ge 176$, $n \neq 177$):**
   Specifically, for $n = 176$,
   $$\mathrm{diam}(U(176, \mathbb{F}_2)) \le 2(176)^2 - 6(176) + 5 = 60901 < 61404 \le M(176),$$
   and for **every** $n \ge 178$,
   $$\mathrm{diam}(U(n, \mathbb{F}_2)) \le 2n^2 - 6n + 5 < |\mathcal{F}_n| \le M(n).$$
   Thus the conjectured equality $\mathrm{diam}(U(n, \mathbb{F}_2)) = M(n)$ holds at most for finitely many $n$ (among $2 \le n \le 6$, exact BFS gives diameters $1, 4, 8, 12, 19$, already failing at $n = 2$ ($1 < 2$) and matching $M(n)$ on $3 \le n \le 6$, while Parts 1–3 prove failure at $n = 176$ and for all $n \ge 178$).

---

## Proof of Part 1: Explicit $2n^2 - 6n + 5$ Word Factorization in $U(n, \mathbb{F}_2)$

Use $0$-indexed matrix coordinates $0, \dots, n-1$, so $s_k = I + E_{k-1, k}$ for $1 \le k \le n-1$. Left-multiplying a matrix $A$ by $s_k$ replaces row $k-1$ with $\mathrm{row}_{k-1} \oplus \mathrm{row}_k$; right-multiplying $A$ by $s_k$ replaces column $k$ with $\mathrm{col}_k \oplus \mathrm{col}_{k-1}$. Let $e_0, \dots, e_{n-1}$ be the standard basis row vectors over $\mathbb{F}_2$.

**Step 1 (Row-by-row decomposition).**
Given any $M \in U(n, \mathbb{F}_2)$, define for each $0 \le i \le n-2$ the single-row upper unitriangular matrix
$$U_i = I + \sum_{j = i+1}^{n-1} M_{i,j} E_{i,j}.$$
We claim $M = U_{n-2} U_{n-3} \cdots U_0$.
Indeed, let $P_k = U_k \cdots U_0$. For $k = 0$, row $0$ of $P_0 = U_0$ is row $0$ of $M$ and rows $> 0$ equal $e_r$. Inductively for $k \ge 1$: when multiplying $P_{k-1}$ on the left by $U_k$, every row $r < k$ of $U_k$ is $e_r$, so row $r$ of $U_k P_{k-1}$ equals row $r$ of $P_{k-1}$ (which is row $r$ of $M$); every row $r > k$ of both $U_k$ and $P_{k-1}$ is $e_r$; and row $k$ of $U_k P_{k-1}$ equals
$$(\mathrm{row}_k(U_k)) P_{k-1} = \sum_{j=k}^{n-1} (U_k)_{k,j} (e_j P_{k-1}) = \sum_{j=k}^{n-1} (U_k)_{k,j} e_j = \mathrm{row}_k(U_k) = \mathrm{row}_k(M),$$
since rows $j \ge k$ of $P_{k-1}$ equal $e_j$. Setting $k = n-2$ gives $P_{n-2} = M$.

**Step 2 (Word length of each $U_i$).**
- For $i = n-2$: $U_{n-2} \in \{I, s_{n-1}\}$, so its word length is at most $1$.
- Fix $0 \le i \le n-3$. If $U_i = I$, its word length is $0$. If $M_{i, i+1} = 1$ and $M_{i,j} = 0$ for all $j \ge i+2$, then $U_i = s_{i+1}$ has word length $1 \le 4(n-i-2)$.
- Otherwise, let $m = \max\{j \in \{i+2, \dots, n-1\} : M_{i,j} = 1\}$. Notice that for ANY $W \in \langle s_{i+2}, \dots, s_{n-1} \rangle$, the $i$-th column of $W^{-1}$ is $e_i^T$, so
  $$W^{-1} s_{i+1} W = I + W^{-1} E_{i, i+1} W = I + e_i^T \cdot \mathrm{row}_{i+1}(W).$$
  Construct $W$ starting from $I$ by right-multiplications:
  1. Right-multiply successively by $s_{i+2}, s_{i+3}, \dots, s_m$. Since row $i+1$ starts as $e_{i+1}$ and right-multiplying by $s_k$ adds column $k-1$ to column $k$, this successively sets entries $(i+1, i+2), \dots, (i+1, m)$ to $1$. Cost: $m - i - 1$ generators.
  2. Next, for $k = m, m-1, \dots, i+2$ in strictly decreasing order, if $M_{i,k} = 0$, right-multiply by $s_k$. Because $k$ is processed in decreasing order, when $s_k$ is applied, column $k-1$ of row $i+1$ is still $1$ and column $k$ is $1$, and no subsequent step $k' < k$ alters column $k$; thus entry $(i+1, k)$ flips from $1$ to $0$. Since $M_{i,m} = 1$, $k = m$ is never applied, so at most $m - i - 2$ generators are used.
  
  Hence $|W| \le (m - i - 1) + (m - i - 2) = 2(m - i) - 3 \le 2(n - i) - 5$. Since $s_k^{-1} = s_k$, $W^{-1}$ is the reversal of $W$, giving a word for $W^{-1} s_{i+1} W$ of length $2|W| + 1 \le 4(n - i) - 9$, whose row $i$ equals $e_i + e_{i+1} + \sum_{j=i+2}^m M_{i,j} e_j$.
  3. Finally, if $M_{i, i+1} = 0$, left-multiplying by $s_{i+1}$ adds row $i+1$ ($= e_{i+1}$) to row $i$, flipping $(i, i+1)$ from $1$ to $0$ without changing any other entry.
  
  In all cases, $U_i$ has word length at most $4(n-i)-9+1 = 4(n - i - 2)$.

**Step 3 (Total diameter bound).**
Summing the bounds for $U_{n-2} \cdots U_0$ yields for all $n \ge 2$:
$$\mathrm{diam}(U(n, \mathbb{F}_2)) \le 1 + \sum_{i=0}^{n-3} 4(n - i - 2) = 1 + 4\sum_{k=1}^{n-2} k = 1 + 2(n-2)(n-1) = 2n^2 - 6n + 5.$$
$\square$

---

## Proof of Part 2: Self-Contained $\Omega(n^3)$ Family of Metacyclic Groups of Order $2^n$

For any $n \ge 6$, let $\mathcal{F}_n$ be the set of integer triples $(a, c, s)$ satisfying:
$$3 \le a \le \lfloor n/2 \rfloor, \qquad 2 \le s \le a - 1, \qquad \max(s, d) \le c \le a, \quad \text{where } d := a - s \ge 1,$$
and set $b := n - a \ge a > d$.

For each $(a, c, s) \in \mathcal{F}_n$, let $A = 2^a$, $B = 2^b$, $C = 2^c$, $r = 1 + 2^s$, and define an operation on the set $G(a, c, s) := \{0, \dots, A-1\} \times \{0, \dots, B-1\}$ by
$$(i_1, j_1) \cdot (i_2, j_2) := \left(\bigl(i_1 + i_2 r^{j_1} + C \mathbf{1}_{j_1 + j_2 \ge B}\bigr) \bmod A,\; (j_1 + j_2) \bmod B\right).$$

**Claim 1: $G = G(a, c, s)$ is a metacyclic group of order $2^n$.**
Since $s \ge 2$, $\nu_2(r - 1) = s \ge 2$, so by Lifting the Exponent $\nu_2(r^{2^k} - 1) = s + k$ for all $k \ge 0$, and more generally $\nu_2(r^j - 1) = s + \nu_2(j)$ for all $j \ge 1$. Because $b \ge a > d = a - s$, we have $s + b > a$, so $r^B \equiv 1 \pmod A$. Also $c \ge d = a - s \implies c + s \ge a \implies C r \equiv C + 2^{c+s} \equiv C \pmod A$. Thus for any $(i_1,j_1), (i_2,j_2), (i_3,j_3) \in G$:
- $r^{(j_1+j_2) \bmod B} \equiv r^{j_1 + j_2} \pmod A$,
- $C r^{j_1} \equiv C \pmod A$,
- $\mathbf{1}_{j_1+j_2 \ge B} + \mathbf{1}_{((j_1+j_2)\bmod B)+j_3 \ge B} = \lfloor (j_1+j_2+j_3)/B \rfloor = \mathbf{1}_{j_2+j_3 \ge B} + \mathbf{1}_{j_1+((j_2+j_3)\bmod B) \ge B}$.

Hence multiplication is associative, $(0,0)$ is the identity, and every $(i, j) \in G$ has explicit two-sided inverse $\bigl((-i - C\mathbf{1}_{j > 0}) r^{-j} \bmod A,\; (-j) \bmod B\bigr)$ (well-defined since $r = 1 + 2^s$ is odd, hence invertible modulo $A = 2^a$, and verified using $r^B \equiv 1 \pmod A$ and $Cr \equiv C \pmod A$). Letting $x = (1, 0)$ and $y = (0, 1)$, every $(i, j) = x^i y^j$, $N := \langle x \rangle = \{(i, 0)\}$ is cyclic of order $2^a$, $y x y^{-1} = x^r \in N$ so $N \trianglelefteq G$, and $G / N \cong C_{2^b}$ is cyclic of order $2^b$. Hence $G(a, c, s)$ is a metacyclic group of order $2^n$, with presentation
$$G(a, c, s) = \langle x, y \mid x^{2^a} = 1,\; y^{2^b} = x^{2^c},\; y x y^{-1} = x^{1 + 2^s} \rangle.$$

**Claim 2: Distinct triples in $\mathcal{F}_n$ yield pairwise non-isomorphic groups.**
We recover $(a, c, s)$ uniquely from the isomorphism invariants $(G^{\mathrm{ab}}, Z(G))$:
1. *Commutator subgroup $G'$ and abelianization $G^{\mathrm{ab}} = G/G'$:*
   We have $[x, y^{-1}] = x^{-1} y x y^{-1} = x^{2^s} \in G'$. Since $N = \langle x \rangle \trianglelefteq G$ and $G/N$ is abelian, $G' \le N$. Conversely $G / \langle x^{2^s} \rangle$ is abelian (its generators commute modulo $x^{2^s}$), so $G' = \langle x^{2^s} \rangle$ has order $2^{a-s} = 2^d$.
   Because $c \ge \max(s, d) \ge s$, we have $y^{2^b} = x^{2^c} \in \langle x^{2^s} \rangle = G'$. Thus in $G^{\mathrm{ab}} = G/G'$, the images $\bar{x}, \bar{y}$ satisfy $\bar{x}^{2^s} = 1$, $\bar{y}^{2^b} = 1$, $[\bar{x}, \bar{y}] = 1$, and $|G^{\mathrm{ab}}| = 2^{n-d} = 2^{s+b}$, giving
   $$G^{\mathrm{ab}} \cong C_{2^s} \times C_{2^b} = C_{2^s} \times C_{2^{n-a}}.$$
   Since $s < a \le \lfloor n/2 \rfloor \le n - a = b$, the two invariant factor orders $2^s < 2^{n-a}$ are distinct, so $G^{\mathrm{ab}}$ uniquely determines $s$, $b = n - a$, $a$, and $d = a - s$.
2. *Center $Z(G)$:*
   An element $(i, j) = x^i y^j$ commutes with $x = (1,0)$ iff $r^j \equiv 1 \pmod{2^a}$, i.e., $j = 0$ or $s + \nu_2(j) \ge a$, which (since $b > d$) holds iff $2^d \mid j$. It commutes with $y = (0,1)$ iff $i r \equiv i \pmod{2^a}$, i.e., $2^s i \equiv 0 \pmod{2^a} \iff 2^d \mid i$. Thus $Z(G) = \langle u, v \rangle$ where $u := x^{2^d}$ (order $2^{a-d} = 2^s$) and $v := y^{2^d}$, with $|Z(G)| = 2^{a-d} \cdot 2^{b-d} = 2^{n-2d}$.
   Note $v^{2^{b-d}} = y^{2^b} = x^{2^c} = u^{2^{c-d}}$ (valid since $c \ge d$), which has order $2^{s-(c-d)} = 2^{a-c}$, and $Z(G)/\langle u \rangle \cong C_{2^{b-d}}$ generated by $\bar{v}$. Hence $\langle u \rangle \cap \langle v \rangle = \langle u^{2^{c-d}} \rangle$ and $v$ has order $2^{(b-d)+(a-c)} = 2^{n-c-d}$.
   Moreover $b - c \ge a - c \ge 0$, so $w := u v^{-2^{b-c}} \in Z(G)$ satisfies $\langle v, w \rangle = \langle v, u \rangle = Z(G)$ and $w^{2^{c-d}} = u^{2^{c-d}} v^{-2^{b-d}} = 1$. If $w^t \in \langle v \rangle$, then $u^t \in \langle v \rangle$, so $u^t \in \langle u^{2^{c-d}} \rangle$, forcing $2^{c-d} \mid t$ and $w^t = 1$. Thus $\langle w \rangle \cap \langle v \rangle = \{1\}$, $|\langle w \rangle| = 2^{c-d}$, and $|\langle v \rangle| \cdot |\langle w \rangle| = 2^{n-2d} = |Z(G)|$, giving
   $$Z(G) = \langle v \rangle \times \langle w \rangle \cong C_{2^{n-c-d}} \times C_{2^{c-d}}.$$
   Since $c \le a \le n/2$, we have $2c \le n \implies c - d \le n - c - d$. Under the $2$-component convention $C_{2^{e_1}} \times C_{2^{e_2}}$ with $e_1 \ge e_2 \ge 0$ (where $C_1$ is trivial when $c = d$), the smaller invariant factor exponent of $Z(G)$ equals $c - d$, which uniquely determines $c$ once $d$ is known from $G'$.

Consequently, $M(n) \ge |\mathcal{F}_n|$ for every $n \ge 6$. $\square$

---

## Proof of Part 3: Concrete Failure at $n = 2$, $n = 176$, and All $n \ge 178$

- At $n = 2$: $|U(2, \mathbb{F}_2)| = 2$ generated by $s_1$, so $\mathrm{diam}(U(2, \mathbb{F}_2)) = 1$, whereas $C_4$ and $C_2 \times C_2$ are $2$ non-isomorphic metacyclic groups of order $4$.
- Counting $|\mathcal{F}_n|$: let $m = \lfloor n/2 \rfloor$. Since $\max(s, a-s) = a - \min(s, a-s)$,
  $$|\mathcal{F}_n| = \sum_{a=3}^{m} \sum_{s=2}^{a-1} \bigl(\min(s, a-s) + 1\bigr).$$
  Since $\sum_{s=1}^{a-1} \min(s, a-s) = \lfloor a^2/4 \rfloor$, each $a$-summand equals $\lfloor a^2/4 \rfloor + a - 3 \ge \frac{a^2 + 4a - 13}{4}$.
  - Direct integer evaluation gives $|\mathcal{F}_{176}| = 61404 > 60901 = 2(176)^2 - 6(176) + 5$, and $|\mathcal{F}_n| > 2n^2 - 6n + 5$ for every $178 \le n \le 195$ (at $n = 178$: $63470 > 62305$).
  - For all $n \ge 195$, we have $m \ge \frac{n-1}{2} \ge 97$, and
    $$|\mathcal{F}_n| \ge \sum_{a=3}^m \frac{a^2 + 4a - 13}{4} = \frac{2m^3 + 15m^2 - 65m + 54}{24} > \frac{m^3}{12} \ge \frac{(n-1)^3}{96}$$
    (since $15m^2 - 65m + 54 > 0$ for all $m \ge 5$). Now
    $$(n-1)^3 - 96(2n^2 - 6n + 5) = n^3 - 195n^2 + 579n - 481 = n^2(n - 195) + (579n - 481) > 0$$
    for every $n \ge 195$.

Hence $\mathrm{diam}(U(n, \mathbb{F}_2)) \le 2n^2 - 6n + 5 < |\mathcal{F}_n| \le M(n)$ at $n = 176$ and for all $n \ge 178$. $\blacksquare$

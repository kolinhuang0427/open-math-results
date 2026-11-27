# Nonexistence of Proper Liftings of Algebraic Degree 2

**Target:** Question 2.3 (Section 2) and the existence question in Open Problem (iii) (Section 4) of Jan Kristian Haugland and Tron Omland, *"New classes of reversible cellular automata"*, `arXiv:2411.00721v2` (updated 2026-11-01; DOI `10.1007/s10623-026-01869-z`, cached TeX `haugland-omland-reversible-v2.tex`).

## 1. Exact Statement from the Primary Source

In Section 1 (`\label{prelims}`, lines 89–101 of `haugland-omland-reversible-v2.tex`), Haugland and Omland define:

> A Boolean function $f\colon\mathbb{F}_2^k\to\mathbb{F}_2$ induces a function $F\colon\mathbb{F}_2^n\to\mathbb{F}_2^n$ for every $n\geq k$, by
> \[
> F(x_1,x_2,\dotsc,x_n)=\big(f(x_1,x_2,\dotsc,x_k),f(x_2,x_3,\dotsc,x_{k+1}), \dotsc,f(x_n,x_1,\dotsc,x_{k-1})\big),
> \]
> which is shift-invariant (or rotation-symmetric), that is, commutes with the right shift operator. ... If $f$ has diameter~$k$, i.e., depends on both $x_1$ and $x_k$, and $F$ is bijective, we say that $f$ is a $(k,n)$-lifting. If $f$ is a $(k,n)$-lifting for every $n\geq k$, then $f$ is called a *proper lifting* (see [HO-1]).
>
> A Boolean function $f$ of diameter~$k$ also induces a function $F\colon\mathbb{F}_2^{\mathbb{Z}}\to\mathbb{F}_2^{\mathbb{Z}}$, defined by $F(x)_i = f(x_i, x_{i+1}, \dotsc, x_{i+k-1})$ for all $i \in \mathbb{Z}$, which is called a cellular automaton. It is known that $F$ is bijective if and only if $f$ is a proper lifting, see [Kari, Theorem 7], and in this case $F$ is called a *reversible cellular automaton*.

In Section 2 (Question 2.3, lines 327–331), they ask:

> **Question 2.3.** Does there exist a proper lifting of degree~$2$? We have checked that there are none of diameter~$\leq 7$, and that no composition of two proper liftings of degree~$\leq 6$ gives a degree~$2$ function. Moreover, by Proposition 1.5, every primitive landscape function has degree at least $3$.

This is reiterated in Section 4 (Open Problem (iii), line 455):

> **(iii)** Do proper liftings of algebraic degree~$2$ exist, or more generally, what is the minimal possible degree as a function of diameter?

We answer Question 2.3 (and the existence question in Open Problem (iii)) completely in the **negative** via a quantitative non-bijectivity theorem at a single power-of-two window size. *(The secondary question in Open Problem (iii)—determining the minimal possible algebraic degree of a proper lifting as a function of arbitrary diameter $k$—is outside the scope of this proof.)*

---

## 2. Main Result

Throughout, all arithmetic is over the binary field $\mathbb{F}_2$ (where addition is XOR and $+ = -$). For any integer $n \ge k \ge 1$, we index coordinates of $x \in \mathbb{F}_2^n$ by $r \in \mathbb{Z}/n\mathbb{Z}$ (identifying $(x_1,\dots,x_n)$ with $(x_0,\dots,x_{n-1})$ via $x_r^{\text{new}} = x_{r+1}^{\text{old}}$), so the shift-invariant map $F_n \colon \mathbb{F}_2^n \to \mathbb{F}_2^n$ induced by $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ is given by
$$F_n(x)_r = f(x_r, x_{r+1}, \dots, x_{r+k-1}) \qquad (r \in \mathbb{Z}/n\mathbb{Z}).$$

**Theorem 1.** *Let $k \ge 2$ be an integer, and let $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ be any Boolean function of algebraic degree $2$. Set*
$$s_{\max} := \lceil \log_2 k \rceil, \qquad N := 2^{s_{\max} + 1}.$$
*Then $2k \le N \le 4k - 4$, and the induced shift-invariant map $F_N \colon \mathbb{F}_2^N \to \mathbb{F}_2^N$ is not bijective. In fact, the proof constructively exhibits distinct vectors $x, x + u \in \mathbb{F}_2^N$ ($u \neq 0$) with $F_N(x + u) = F_N(x)$.*

**Corollary 2.** *There does not exist a proper lifting of algebraic degree $2$ (of any diameter $k \ge 1$). Equivalently, no reversible binary cellular automaton has a local rule of algebraic degree $2$, and every non-affine proper lifting has algebraic degree at least $3$.*

*Proof of Corollary 2 from Theorem 1.* For $k = 1$, every Boolean function $f \colon \mathbb{F}_2^1 \to \mathbb{F}_2$ has algebraic degree at most $1$. For $k \ge 2$, any Boolean function $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ of algebraic degree $2$ fails to induce a bijection $F_N \colon \mathbb{F}_2^N \to \mathbb{F}_2^N$ at $N = 2^{\lceil \log_2 k \rceil + 1} > k$ by Theorem 1, so $f$ is not a $(k, N)$-lifting and hence not a proper lifting. By Proposition 1.2 of `arXiv:2411.00721v2`, every proper lifting of degree $\le 1$ is affine of diameter $1$; hence every non-affine proper lifting has algebraic degree at least $3$. $\square$

---

## 3. Proof of Theorem 1

### 3.1. Directional Derivatives of Quadratic Shift-Invariant Maps

Every Boolean function $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ of algebraic degree at most $2$ has a unique Algebraic Normal Form (ANF) over $\mathbb{F}_2$:
$$f(y_0, y_1, \dots, y_{k-1}) = c_0 + \sum_{j=0}^{k-1} \ell_j y_j + \sum_{0 \le i < j \le k-1} q_{ij} y_i y_j$$
with $c_0, \ell_j, q_{ij} \in \mathbb{F}_2$, and $\deg(f) = 2$ if and only if $q_{ij} = 1$ for at least one pair $i < j$. Extend $(q_{ij})$ to a symmetric zero-diagonal matrix $Q = (q_{ij})_{0 \le i,j \le k-1} \in \mathbb{F}_2^{k \times k}$ by setting $q_{ii} := 0$ and $q_{ji} := q_{ij}$ for $0 \le i < j \le k-1$.

For any $n \ge k$ and any $x, u \in \mathbb{F}_2^n$, expanding $(x_{r+i} + u_{r+i})(x_{r+j} + u_{r+j}) + x_{r+i} x_{r+j} = u_{r+i} x_{r+j} + u_{r+j} x_{r+i} + u_{r+i} u_{r+j}$ over $\mathbb{F}_2$ yields, for every $r \in \mathbb{Z}/n\mathbb{Z}$,
$$\bigl(F_n(x + u) + F_n(x)\bigr)_r = \sum_{j=0}^{k-1} C_j(r)\, x_{r+j} + v(u)_r, \tag{1}$$
where $v(u) := F_n(u) + F_n(0) \in \mathbb{F}_2^n$ (with $v(u)_r = \sum_{j=0}^{k-1} \ell_j u_{r+j} + \sum_{0 \le i < j \le k-1} q_{ij} u_{r+i} u_{r+j}$) and
$$C_j(r) := \sum_{i=0}^{k-1} q_{ij} u_{r+i} \in \mathbb{F}_2 \qquad (0 \le j \le k-1,\ r \in \mathbb{Z}/n\mathbb{Z}). \tag{2}$$
In particular, for a fixed nonzero $u \in \mathbb{F}_2^n \setminus \{0\}$, the existence of $x \in \mathbb{F}_2^n$ satisfying $\sum_{j=0}^{k-1} C_j(r) x_{r+j} = v(u)_r$ for all $r \in \mathbb{Z}/n\mathbb{Z}$ gives $F_n(x + u) = F_n(x)$ with $x + u \neq x$, contradicting the bijectivity of $F_n$.

### 3.2. Power-of-Two Circulant Directional-Derivative Lemma

**Lemma 3.** *Let $k \ge 1$, let $f \colon \mathbb{F}_2^k \to \mathbb{F}_2$ have algebraic degree at most $2$, and let $s \ge 0$ and $M \ge 1$ be integers such that $N := 2^M$ satisfies $N \ge 2^s + k - 1$ (which automatically implies $N \ge k$ and $2^s \mid N$). Suppose that $F_N \colon \mathbb{F}_2^N \to \mathbb{F}_2^N$ is bijective, and let $u \in \mathbb{F}_2^N \setminus \{0\}$ be a nonzero $2^s$-periodic vector (i.e., $u_{r + 2^s} = u_r$ for all $r \in \mathbb{Z}/N\mathbb{Z}$) such that for each $j \in \{0, \dots, k-1\}$, the coefficient $C_j(r)$ in $(2)$ is independent of $r$: there exists $\gamma_j \in \mathbb{F}_2$ with*
$$C_j(r) = \gamma_j \qquad \text{for all } r \in \mathbb{Z}/N\mathbb{Z}.$$
*Then $\gamma_j = 0$ for all $j \in \{0, \dots, k-1\}$.*

*Proof.* Identify $\mathbb{F}_2^N$ with the quotient ring
$$R_N := \mathbb{F}_2[z]/(z^N + 1) = \mathbb{F}_2[z]/\bigl((z + 1)^N\bigr)$$
(using $(z + 1)^N = z^N + 1$ in characteristic $2$, since $N = 2^M$) via the $\mathbb{F}_2$-linear bijection $x = (x_0, \dots, x_{N-1}) \leftrightarrow X(z) := \sum_{r=0}^{N-1} x_r z^r \in R_N$. Under this identification, $z$ is a unit in $R_N$ with $z^N = 1$, and for each $j \in \{0, \dots, k-1\}$ the shifted vector $(x_{r+j})_{r \in \mathbb{Z}/N\mathbb{Z}}$ corresponds to
$$\sum_{r=0}^{N-1} x_{r+j} z^r = \sum_{m=0}^{N-1} x_m z^{m - j} = z^{-j} X(z) \in R_N.$$
Hence the vector $\bigl(\sum_{j=0}^{k-1} \gamma_j x_{r+j}\bigr)_{r \in \mathbb{Z}/N\mathbb{Z}}$ corresponds to $z^{-(k-1)} \widetilde{P}(z) X(z) \in R_N$, where
$$\widetilde{P}(z) := \sum_{j=0}^{k-1} \gamma_j z^{k - 1 - j} \in \mathbb{F}_2[z]$$
has degree at most $k - 1$.

Next, because $u$ is $2^s$-periodic, the vector $v(u) = F_N(u) + F_N(0)$ is also $2^s$-periodic:
$$v(u)_{r + 2^s} = f(u_{r+2^s}, \dots, u_{r+2^s+k-1}) + f(0, \dots, 0) = f(u_r, \dots, u_{r+k-1}) + f(0, \dots, 0) = v(u)_r.$$
Since $2^s \mid N = 2^M$, writing $L := 2^{M - s} \ge 1$ and $r = a + t \cdot 2^s$ ($0 \le a < 2^s$, $0 \le t < L$), the polynomial $V(z) := \sum_{r=0}^{N-1} v(u)_r z^r \in \mathbb{F}_2[z]$ factors as
$$V(z) = \widetilde{V}(z) \sum_{t=0}^{L - 1} \bigl(z^{2^s}\bigr)^t, \qquad \widetilde{V}(z) := \sum_{a=0}^{2^s - 1} v(u)_a z^a.$$
In the polynomial domain $\mathbb{F}_2[w]$, since $L = 2^{M-s}$ is a power of $2$,
$$(w + 1) \sum_{t=0}^{L - 1} w^t = w^L + 1 = (w + 1)^L \implies \sum_{t=0}^{L - 1} w^t = (w + 1)^{L - 1}. \tag{3}$$
Substituting $w = z^{2^s}$ and using $z^{2^s} + 1 = (z + 1)^{2^s}$ in $\mathbb{F}_2[z]$ gives
$$\sum_{t=0}^{L - 1} \bigl(z^{2^s}\bigr)^t = (z + 1)^{2^s (L - 1)} = (z + 1)^{N - 2^s},$$
so $V(z) = (z + 1)^{N - 2^s} \widetilde{V}(z)$ in $R_N$.

Suppose for contradiction that $(\gamma_0, \dots, \gamma_{k-1}) \neq (0, \dots, 0)$. Then $\widetilde{P}(z) \in \mathbb{F}_2[z]$ is nonzero of degree at most $k - 1$, so it factors in $\mathbb{F}_2[z]$ as
$$\widetilde{P}(z) = (z + 1)^e R(z),$$
where $0 \le e \le \deg \widetilde{P} \le k - 1$ and $R(z) \in \mathbb{F}_2[z]$ satisfies $R(1) = 1$. Since $R(1) = 1$, we have $\gcd(R(z), z + 1) = 1$ in $\mathbb{F}_2[z]$, hence $\gcd(R(z), (z + 1)^N) = 1$, so $R(z)$ is invertible in $R_N$. Moreover, the hypothesis $N \ge 2^s + k - 1$ gives $N - 2^s - e \ge (k - 1) - e \ge 0$. Therefore
$$X(z) := z^{k - 1} R(z)^{-1} (z + 1)^{N - 2^s - e} \widetilde{V}(z) \in R_N$$
is well-defined and satisfies
$$z^{-(k - 1)} \widetilde{P}(z) X(z) = z^{-(k - 1)} (z + 1)^e R(z) \cdot z^{k - 1} R(z)^{-1} (z + 1)^{N - 2^s - e} \widetilde{V}(z) = (z + 1)^{N - 2^s} \widetilde{V}(z) = V(z)$$
in $R_N$. Letting $x \in \mathbb{F}_2^N$ be the vector corresponding to $X(z)$, equation $(1)$ gives $F_N(x + u) + F_N(x) = 0$, so $F_N(x + u) = F_N(x)$ with $u \neq 0$, contradicting the bijectivity of $F_N$. Thus $\gamma_j = 0$ for all $j \in \{0, \dots, k - 1\}$. $\square$

### 3.3. Double Induction on Residue Sums Modulo $2^s$

*Proof of Theorem 1.* Let $k \ge 2$, $s_{\max} := \lceil \log_2 k \rceil \ge 1$, and $N := 2^{s_{\max} + 1}$. By definition of ceiling, $2^{s_{\max} - 1} \le k - 1 < k \le 2^{s_{\max}}$, so $k \le 2^{s_{\max}} \le 2k - 2$, and therefore
$$2k \le N = 2 \cdot 2^{s_{\max}} \le 4k - 4.$$
Moreover, for every integer $t \in \{0, 1, \dots, s_{\max}\}$,
$$2^t + k - 1 \le 2^{s_{\max}} + k - 1 < 2^{s_{\max}} + 2^{s_{\max}} = N, \tag{4}$$
so Lemma 3 applies at every period $2^t$ ($0 \le t \le s_{\max}$) with this fixed window size $N$.

Assume for contradiction that $F_N \colon \mathbb{F}_2^N \to \mathbb{F}_2^N$ is bijective. For each integer $s \in \{0, 1, \dots, s_{\max}\}$, each $j \in \{0, \dots, k - 1\}$, and each residue class $c \in \mathbb{Z}/2^s\mathbb{Z}$, define the residue sum
$$S_j^{(s)}(c) := \sum_{\substack{0 \le i \le k - 1 \\ i \equiv c \pmod{2^s}}} q_{ij} \in \mathbb{F}_2.$$
We prove by outer induction on $s \in \{0, 1, \dots, s_{\max}\}$ that
$$S_j^{(s)}(c) = 0 \qquad \text{for all } j \in \{0, \dots, k - 1\} \text{ and all } c \in \mathbb{Z}/2^s\mathbb{Z}. \tag{5}$$

**Base case ($s = 0$).** Take the all-ones vector $u = (1, 1, \dots, 1) \in \mathbb{F}_2^N$, which is nonzero and $2^0$-periodic. For every $j \in \{0, \dots, k - 1\}$ and every $r \in \mathbb{Z}/N\mathbb{Z}$,
$$C_j(r) = \sum_{i=0}^{k-1} q_{ij} u_{r+i} = \sum_{i=0}^{k-1} q_{ij} = S_j^{(0)}(0)$$
is independent of $r$. By Lemma 3 (with $t = 0$, valid by $(4)$), $S_j^{(0)}(0) = 0$ for all $j \in \{0, \dots, k - 1\}$.

**Inductive step ($s \to s + 1$, for $0 \le s < s_{\max}$).** Assume $(5)$ holds at level $s$, and set $P := 2^s$ (so $2P = 2^{s+1} \le 2^{s_{\max}}$ and $2P \mid N$). For each $j \in \{0, \dots, k - 1\}$ and $c \in \{0, \dots, 2P - 1\}$, abbreviate $a_j(c) := S_j^{(s+1)}(c \bmod 2P)$. Partitioning $\{0 \le i \le k - 1 : i \equiv b \pmod{P}\}$ into the two classes modulo $2P$ gives, for every $b \in \{0, \dots, P - 1\}$,
$$a_j(b) + a_j(b + P) = S_j^{(s)}(b) = 0 \implies a_j(b + P) = a_j(b). \tag{6}$$

Now let $w = (w_0, \dots, w_{P-1}) \in \mathbb{F}_2^P \setminus \{0\}$ be any nonzero vector. Define $u \in \mathbb{F}_2^N$ by letting $\bar{m} \in \{0, \dots, 2P - 1\}$ denote the remainder of $m \in \mathbb{Z}/N\mathbb{Z}$ modulo $2P$ (well-defined since $2P \mid N$) and setting
$$u_m := \begin{cases} w_{\bar{m}} & \text{if } 0 \le \bar{m} < P, \\ 0 & \text{if } P \le \bar{m} < 2P. \end{cases}$$
Then $u$ is $2P$-periodic, $u \neq 0$ (as $w \neq 0$ and $P < N$), and for every $m \in \mathbb{Z}/N\mathbb{Z}$:
- if $0 \le \bar{m} < P$, then $\overline{m + P} = \bar{m} + P \in [P, 2P)$, so $u_m + u_{m+P} = w_{\bar{m}} + 0 = w_{m \bmod P}$;
- if $P \le \bar{m} < 2P$, then $\overline{m + P} = \bar{m} - P \in [0, P)$, so $u_m + u_{m+P} = 0 + w_{\bar{m} - P} = w_{m \bmod P}$.

Thus $u_m + u_{m+P} = w_{m \bmod P}$ for all $m \in \mathbb{Z}/N\mathbb{Z}$. Grouping $(2)$ by $i \bmod 2P$ and pairing $c = b$ with $c = b + P$ via $(6)$, we obtain for every $j \in \{0, \dots, k - 1\}$ and every $r \in \mathbb{Z}/N\mathbb{Z}$:
$$C_j(r) = \sum_{c=0}^{2P - 1} u_{r+c}\, a_j(c) = \sum_{b=0}^{P - 1} \bigl(u_{r+b} + u_{r+b+P}\bigr)\, a_j(b) = \sum_{b=0}^{P - 1} w_{(r+b)\bmod P}\, a_j(b). \tag{7}$$
In particular, $C_j(r)$ depends only on $r \bmod P$.

Consider the commutative ring $R_P := \mathbb{F}_2[T]/(T^P + 1) = \mathbb{F}_2[T]/\bigl((T + 1)^P\bigr)$ (using $P = 2^s$), and define
$$W(T) := \sum_{m=0}^{P - 1} w_m T^m \in R_P, \qquad A_j^*(T) := \sum_{b=0}^{P - 1} a_j(b)\, T^{-b} \in R_P \qquad (0 \le j \le k - 1).$$
In $R_P$, the product $W(T) A_j^*(T) = \sum_{m=0}^{P-1} \sum_{b=0}^{P-1} w_m a_j(b) T^{m - b}$ has $T^r$-coefficient ($0 \le r \le P - 1$) equal to $\sum_{b=0}^{P-1} w_{(r+b)\bmod P} a_j(b)$, which by $(7)$ equals $C_j(r)$:
$$[T^{r \bmod P}]\bigl(W(T) A_j^*(T)\bigr) = C_j(r) \qquad \forall\, r \in \mathbb{Z}/N\mathbb{Z},\ \forall\, j \in \{0, \dots, k - 1\}. \tag{8}$$

We now prove by inner induction on $e \in \{0, 1, \dots, P\}$ that
$$(T + 1)^{P - e} A_j^*(T) = 0 \quad \text{in } R_P \qquad \text{for all } j \in \{0, \dots, k - 1\}. \tag{9}$$
- **Inner base case ($e = 0$):** $(T + 1)^P = 0$ in $R_P$, so $(9)$ holds trivially.
- **Inner inductive step ($e \to e + 1$, for $0 \le e \le P - 1$):** Assume $(9)$ holds at $e$. Choose
  $$W(T) := (T + 1)^{P - 1 - e} \bmod (T + 1)^P \in R_P,$$
  which has degree $P - 1 - e < P$ and leading coefficient $1$, so it defines a nonzero vector $w \in \mathbb{F}_2^P \setminus \{0\}$ (explicitly $w_m = \binom{P - 1 - e}{m} \bmod 2$), and hence a nonzero $2^{s+1}$-periodic vector $u \in \mathbb{F}_2^N \setminus \{0\}$. Set $H_j(T) := W(T) A_j^*(T) = (T + 1)^{P - 1 - e} A_j^*(T) \in R_P$. By the inner induction hypothesis at $e$,
  $$(T + 1) H_j(T) = (T + 1)^{P - e} A_j^*(T) = 0 \quad \text{in } R_P = \mathbb{F}_2[T]/\bigl((T + 1)^P\bigr).$$
  Taking the unique lift of $H_j(T)$ to $\mathbb{F}_2[T]$ of degree $< P$, divisibility $(T + 1)^P \mid (T + 1) H_j(T)$ in $\mathbb{F}_2[T]$ forces $(T + 1)^{P - 1} \mid H_j(T)$. Since $\deg H_j < P$, there exists a scalar $\gamma_j \in \mathbb{F}_2$ such that
  $$H_j(T) = \gamma_j (T + 1)^{P - 1} = \gamma_j \sum_{r=0}^{P - 1} T^r \quad \text{in } R_P,$$
  where the second equality is $(3)$ with $L = P = 2^s$. By $(8)$, it follows that $C_j(r) = \gamma_j$ is independent of $r \in \mathbb{Z}/N\mathbb{Z}$ for every $j \in \{0, \dots, k - 1\}$. Applying Lemma 3 to the nonzero $2^{s+1}$-periodic vector $u$ (valid by $(4)$ since $s + 1 \le s_{\max}$) forces $\gamma_j = 0$ for all $j \in \{0, \dots, k - 1\}$. Hence $H_j(T) = (T + 1)^{P - (e + 1)} A_j^*(T) = 0$ in $R_P$ for all $j$, completing the inner induction.

Setting $e = P$ in $(9)$ gives $A_j^*(T) = 0$ in $R_P$ for all $j \in \{0, \dots, k - 1\}$. Therefore $a_j(b) = 0$ for all $0 \le b \le P - 1$, and by $(6)$ also $a_j(b + P) = a_j(b) = 0$; that is, $S_j^{(s+1)}(c) = 0$ for all $j$ and all $c \in \mathbb{Z}/2^{s+1}\mathbb{Z}$. This completes the outer induction.

**Conclusion.** Evaluating $(5)$ at $s = s_{\max}$ where $2^{s_{\max}} \ge k$, the indices $0, 1, \dots, k - 1$ represent distinct residue classes modulo $2^{s_{\max}}$. Therefore, for every $i, j \in \{0, \dots, k - 1\}$,
$$q_{ij} = S_j^{(s_{\max})}(i \bmod 2^{s_{\max}}) = 0.$$
Hence $Q = 0$ and $\deg(f) \le 1$, contradicting $\deg(f) = 2$. Consequently, $F_N$ is not bijective. (Moreover, if $F_N$ were bijective for the first step $(s, e)$ where a nonzero $\gamma$ arises—which must occur since $Q \neq 0$—the explicit formula for $X(z)$ in Lemma 3 produces $x, x + u \in \mathbb{F}_2^N$ with $u \neq 0$ and $F_N(x + u) = F_N(x)$.) $\square$

---

## 4. Remark on Sharpness of the Power-of-Two Window Size

The exponent $\lceil \log_2 k \rceil + 1$ in Theorem 1 cannot be lowered to $\lceil \log_2 k \rceil$ in general. For every integer $m \ge 1$, set $k := 2^m + 2$ (so $\lceil \log_2 k \rceil = m + 1$, $2^{\lceil \log_2 k \rceil} = 2^{m+1}$, and $N = 2^{m+2}$) and define the algebraic degree-$2$, diameter-$k$ Boolean function
$$f_m(y_0, \dots, y_{2^m + 1}) := y_0 + (y_0 + y_{2^m})(y_1 + y_{2^m + 1}).$$
At $n = 2^{m+1} = 2^{\lceil \log_2 k \rceil}$, for any $x \in \mathbb{F}_2^n$ the difference $w_r := x_r + x_{r + 2^m}$ satisfies $w_{r + 2^m} = x_{r + 2^m} + x_r = w_r$ modulo $2^{m+1}$, so
$$F_n(x)_r = x_r + w_r w_{r+1}, \qquad F_n(x)_r + F_n(x)_{r + 2^m} = x_r + x_{r + 2^m} = w_r,$$
and therefore $F_n(F_n(x))_r = (x_r + w_r w_{r+1}) + w_r w_{r+1} = x_r$. Thus $F_{2^{\lceil \log_2 k \rceil}}$ is an involution (hence bijective), whereas Theorem 1 guarantees—and constructs—an explicit collision for $F_{2^{\lceil \log_2 k \rceil + 1}}$.

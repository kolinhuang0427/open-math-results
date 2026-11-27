# Proof of Yip's Conjecture on Restricted Sumsets in Squares (`arXiv:2309.10950v2`, Remark 3.3)

## Primary Source & Exact Statement

**Primary source:** Chi Hoi Yip, *"Restricted sumsets in multiplicative subgroups"*, `arXiv:2309.10950v2` [math.NT, math.CO] (`main.tex`), published in *Canadian Journal of Mathematics* **78**(2) (2026), 594–618 (DOI `10.4153/S0008414X24000920`).

In `main.tex`, `thm`, `cor`, `prop`, `lem`, and `rem` share a single section-level counter, so `\label{thm:VLM}` (lines 105–107 of `main.tex`) is **Theorem 1.7** and the Remark following its proof in Section 3.2 (lines 405–407 of `main.tex`) is **Remark 3.3** in the compiled PDF and published paper.

**Verbatim Theorem 1.7 (`thm:VLM`, Section 1, `main.tex` lines 105–107):**
> Let $d \geq 3$. Let $q \equiv 1 \pmod d$ be an odd prime power and a square. If $A \subset \mathbb{F}_q$ such that $A\hat{+}A \subset S_d \cup \{0\}$, then $|A| \leq \sqrt{q}$, with the equality holds if and only if $d \mid (\sqrt{q}+1)$ and $A=\alpha \mathbb{F}_{\sqrt{q}}$, where $\alpha \in S_d$.

Here $S_d = \{x^d : x \in \mathbb{F}_q^*\}$ and $A \hat{+} A = \{a + b : a, b \in A,\, a \neq b\}$.

**Verbatim Conjecture (Remark 3.3, Section 3.2, `main.tex` lines 405–407):**
> Our analysis cannot handle the case $d=2$. In fact, there is $A \subset \mathbb{F}_9$ with size $4$ such that $A \hat{+} A \subset S_2 (\mathbb{F}_9) \cup \{0\}$, and there are $15$ different $A \subset \mathbb{F}_{25}$ with size $5$ such that $A \hat{+} A \subset S_2 (\mathbb{F}_{25}) \cup \{0\}$. Nevertheless, we conjecture that when $q$ is an odd square and $q \geq 49$, the statement of Theorem~\ref{thm:VLM} also extends to the case $d=2$.

Note that for every odd square $q$, $\sqrt{q}$ is odd and hence $2 \mid (\sqrt{q} + 1)$ holds automatically. We prove the conjecture in full:

---

## Main Theorem

**Theorem.** *Let $q \ge 49$ be an odd prime power that is a square, and let $S_2 = \{x^2 : x \in \mathbb{F}_q^*\}$. If $A \subset \mathbb{F}_q$ satisfies $A \hat{+} A \subset S_2 \cup \{0\}$, then*
$$|A| \le \sqrt{q},$$
*with equality if and only if $A = \alpha \mathbb{F}_{\sqrt{q}}$ for some $\alpha \in S_2$.*

---

## Proof

Write $r := \sqrt{q}$, so $q = r^2$ and $r = p^s \ge 7$ is an odd prime power ($p$ an odd prime, $s \ge 1$). Let $N_2 := \mathbb{F}_q^* \setminus S_2$ denote the set of nonsquares in $\mathbb{F}_q^*$, and let $\chi: \mathbb{F}_q \to \{0, 1, -1\}$ be the quadratic character of $\mathbb{F}_q$ ($\chi(0) = 0$, $\chi|_{S_2} = +1$, $\chi|_{N_2} = -1$). Similarly, let $\chi_{\mathbb{F}_r}$ be the quadratic character of the subfield $\mathbb{F}_r$.

Let $N(x) := x^{r+1} \in \mathbb{F}_r$ and $\mathrm{Tr}(x) := x + x^r \in \mathbb{F}_r$ denote the field norm and trace of the quadratic extension $\mathbb{F}_{r^2}/\mathbb{F}_r$. We record three elementary facts used throughout:
1. **Subfield containment in $S_2$:** For every $x \in \mathbb{F}_r^*$, $x^{(r^2-1)/2} = (x^{r-1})^{(r+1)/2} = 1$, because $(r+1)/2 \in \mathbb{Z}$. Hence $\mathbb{F}_r^* \subset S_2$. In particular, $-1 \in S_2$ and $2 \in S_2$.
2. **Norm characterization of squares:** For every $x \in \mathbb{F}_{r^2}^*$,
   $$x \in S_2 \iff x^{\frac{r^2-1}{2}} = 1 \iff (x^{r+1})^{\frac{r-1}{2}} = 1 \iff N(x) \in S_2(\mathbb{F}_r),$$
   so $\chi(x) = \chi_{\mathbb{F}_r}(N(x))$ for all $x \in \mathbb{F}_{r^2}$.
3. **Sufficiency of canonical cosets:** If $\alpha \in S_2$ and $A = \alpha \mathbb{F}_r$, then $|A| = r$ and $A \hat{+} A \subset \alpha \mathbb{F}_r \subset S_2 \cup \{0\}$ by Fact 1.

We divide the proof into two cases according to whether $A + A \subset S_2 \cup \{0\}$.

---

### Case 1: $A + A \subset S_2 \cup \{0\}$

Consider the real symmetric $q \times q$ matrix $M$ indexed by $\mathbb{F}_q$ with entries $M_{x,y} = \chi(x+y)$. For $x, y \in \mathbb{F}_q$:
- $(M \mathbf{1})_x = \sum_{y \in \mathbb{F}_q} \chi(x+y) = 0$;
- $(M^2)_{x,y} = \sum_{z \in \mathbb{F}_q} \chi(x+z)\chi(y+z)$ equals $q - 1$ if $x = y$, and equals $\sum_{w \in \mathbb{F}_q^*} \chi(w)\chi(w + y - x) = \sum_{w \in \mathbb{F}_q^*} \chi(1 + (y-x)w^{-1}) = -1$ if $x \neq y$.

Thus $M^2 = q I - J$ (where $J = \mathbf{1}\mathbf{1}^T$), so the eigenvalues of $M$ are $0$ (on $\mathbb{R}\mathbf{1}$) and $\pm \sqrt{q}$ (on $\mathbf{1}^\perp$). Writing the indicator vector $\mathbf{1}_A = \frac{|A|}{q}\mathbf{1} + v$ with $v \perp \mathbf{1}$ gives $\|v\|_2^2 = |A|(1 - |A|/q)$, whence
$$\left|\sum_{a,b \in A} \chi(a+b)\right| = |\langle \mathbf{1}_A, M \mathbf{1}_A \rangle| = |\langle v, M v \rangle| \le \sqrt{q}\|v\|_2^2 = r|A|\left(1 - \frac{|A|}{r^2}\right).$$
On the other hand, since $A + A \subset S_2 \cup \{0\}$, every pair $(a,b) \in A^2$ satisfies $\chi(a+b) = 1$ unless $a + b = 0$, and for each $a \in A$ there is at most one $b \in A$ with $a + b = 0$ (namely $b = -a$). Hence
$$|A|^2 - |A| \le |A|^2 - |A \cap (-A)| = \sum_{a,b \in A} \chi(a+b) \le r|A|\left(1 - \frac{|A|}{r^2}\right),$$
which rearranges to $|A|(r + 1)(|A| - r) \le 0$. Thus $|A| \le r$.

If $|A| = r$, equality must hold in $|A \cap (-A)| \le |A|$, so $A = -A$. Since $r$ is odd and $a \mapsto -a$ is an involution on $A$ whose only fixed point in $\mathbb{F}_q$ is $0$, we must have $0 \in A$. Hence $A - A = A + A \subset S_2 \cup \{0\}$, and for any nonzero $\alpha \in A$ we have $\alpha = 0 + \alpha \in S_2$. Setting $A' := \alpha^{-1} A$, we have $0, 1 \in A'$, $|A'| = r$, and $A' - A' \subset S_2 \cup \{0\}$. By Blokhuis's theorem on the van Lint–MacWilliams conjecture (A. Blokhuis, *On subsets of $GF(q^2)$ with square differences*, Indag. Math. **46** (1984), 369–372), $A' = \mathbb{F}_r$, so $A = \alpha \mathbb{F}_r$ with $\alpha \in S_2$.

---

### Case 2: $A + A \not\subset S_2 \cup \{0\}$

We will prove that $|A| < r$. Suppose for the sake of contradiction that $|A| \ge r$. Since $A \hat{+} A \subset S_2 \cup \{0\}$ and $A + A \not\subset S_2 \cup \{0\}$, there exists $b_0 \in A$ with $2b_0 \notin S_2 \cup \{0\}$. Since $2 \in S_2$, this means $b_0 \in N_2$.

By replacing $A$ with an arbitrary subset of $A$ of size **exactly $r$** that contains $b_0$, we still have $A \hat{+} A \subset S_2 \cup \{0\}$, $|A| = r$, and $B := A \cap N_2 \neq \emptyset$. Set $A_S := A \setminus B = A \cap (S_2 \cup \{0\})$.

**Observation 2.1 ($0 \notin A$).** If $0 \in A$, then $0 \neq b_0$ gives $0 + b_0 = b_0 \in A \hat{+} A \subset S_2 \cup \{0\}$, contradicting $b_0 \in N_2$. Hence $0 \notin A$ and $A_S = A \cap S_2$, so $A = A_S \sqcup B$ is a partition of $A$ into nonzero squares and nonsquares.

---

#### Step 1: Auxiliary Polynomials via the Subfield Frobenius

Let $F(X) := \prod_{a \in A} (X - a) \in \mathbb{F}_q[X]$ (monic, squarefree of degree $r$), and for each $a \in A$ set
$$c_a := \frac{1}{F'(a)} = \prod_{x \in A \setminus \{a\}} (a - x)^{-1} \in \mathbb{F}_q^*.$$
By Lagrange interpolation, for every polynomial $P(X) \in \mathbb{F}_q[X]$ of degree at most $r - 1$, comparing the coefficients of $X^{r-1}$ in $P(X) = \sum_{a \in A} P(a) \frac{F(X)}{(X-a)F'(a)}$ yields
$$\sum_{a \in A} c_a P(a) = [X^{r-1}] P(X). \tag{1}$$

Set $K := \frac{r - 3}{2}$. Since $r \ge 7$ is odd, $K \ge 2$. For each integer $k$ with $0 \le k \le K$, define the polynomial $H_k(Y) \in \mathbb{F}_q[Y]$ by
$$H_k(Y) := \sum_{a \in A} c_a a^k (Y + a^r)^{\frac{r+1}{2}} - \delta_{k, K}.$$

**Lemma 2.2.** *For every $0 \le k \le K$:*
1. $\deg H_k(Y) \le \frac{r - 1}{2}$.
2. *For every $b \in A$,*
   $$H_k(b^r) = \begin{cases} 0 & \text{if } b \in A_S, \\ -2 c_b (2b)^{\frac{r+1}{2}} b^k & \text{if } b \in B. \end{cases}$$
*In particular, $H_k(b^r) \neq 0$ for every $b \in B$, and $H_k(Y)$ is not the zero polynomial.*

*Proof.*
1. The coefficient of $Y^{(r+1)/2}$ in $H_k(Y)$ is $\sum_{a \in A} c_a a^k$. Since $0 \le k \le K = \frac{r-3}{2} < r - 1$, identity (1) gives $\sum_{a \in A} c_a a^k = 0$. Hence $\deg H_k \le \frac{r-1}{2}$.
2. Fix $b \in A$. Because $x \mapsto x^r$ is a field automorphism of $\mathbb{F}_{r^2}$ (as $r = p^s$), we have $b^r + a^r = (b + a)^r$, and therefore
   $$(b^r + a^r)^{\frac{r+1}{2}} = (b + a)^{\frac{r(r+1)}{2}} = (b + a)^{\frac{r^2 - 1}{2}} (b + a)^{\frac{r+1}{2}}.$$
   Compare $(b+a)^{(r^2-1)/2}(b+a)^{(r+1)/2}$ with $(b+a)^{(r+1)/2}$ for each $a \in A$:
   - If $a \neq b$ and $a \neq -b$, then $b + a \in A \hat{+} A \setminus \{0\} \subset S_2$, so $(b+a)^{(r^2-1)/2} = 1$, and both expressions are equal.
   - If $a = -b$, then $b + a = 0$, and since $\frac{r+1}{2} \ge 1$, both expressions equal $0$.
   - If $a = b$, then $(2b)^{(r^2-1)/2} = \chi(2b) = \chi(b)$ (using $2 \in S_2$ and $b \neq 0$), which equals $+1$ if $b \in A_S$ and $-1$ if $b \in B$.

   Summing over $a \in A$ gives
   $$H_k(b^r) = \left(\sum_{a \in A} c_a a^k (b + a)^{\frac{r+1}{2}}\right) - \delta_{k,K} + c_b b^k (2b)^{\frac{r+1}{2}}\bigl(\chi(b) - 1\bigr).$$
   The polynomial $P_{b,k}(X) := X^k (b + X)^{(r+1)/2}$ is monic of degree $k + \frac{r+1}{2} \le K + \frac{r+1}{2} = r - 1$, with equality iff $k = K$. By (1), $\sum_{a \in A} c_a P_{b,k}(a) = \delta_{k, K}$, which cancels $-\delta_{k, K}$ exactly. Since $\chi(b) - 1$ equals $0$ for $b \in A_S$ and $-2$ for $b \in B$, part (2) follows. Because $p$ is odd and $c_b, b \in \mathbb{F}_q^*$, we have $H_k(b^r) \neq 0$ for all $b \in B$; since $B \neq \emptyset$, $H_k \not\equiv 0$. $\square$

---

#### Step 2: Algebraic Rigidity of $B$ (UFD Factorization)

**Lemma 2.3.** *There exist coprime polynomials $U(Y), V(Y) \in \mathbb{F}_q[Y]$ with $\max(\deg U, \deg V) = 1$ such that:*
1. $|A_S| \le 1$ *and* $|B| \ge r - 1$;
2. *for every $b \in B$, $U(b^r) \neq 0$ and $b = V(b^r) / U(b^r)$, i.e., $b\,U(b^r) - V(b^r) = 0$.*

*Proof.* For each $1 \le k \le K$, put $Q_k(Y) := H_0(Y) H_k(Y) - H_1(Y) H_{k-1}(Y) \in \mathbb{F}_q[Y]$. By Lemma 2.2(1), $\deg Q_k \le 2 \cdot \frac{r-1}{2} = r - 1$. By Lemma 2.2(2), $Q_k(b^r) = 0$ for every $b \in A_S$ (all factors vanish) and every $b \in B$ (as $1 \cdot b^k - b \cdot b^{k-1} = 0$). Since $b \mapsto b^r$ is bijective on $\mathbb{F}_q$, the set $\{b^r : b \in A\}$ consists of $r$ distinct roots of $Q_k$. Hence $Q_k \equiv 0$, i.e.,
$$H_0(Y) H_k(Y) = H_1(Y) H_{k-1}(Y) \qquad (1 \le k \le K).$$

Since $H_0 \not\equiv 0$, write $H_1(Y)/H_0(Y) = V(Y)/U(Y)$ in lowest terms in $\mathbb{F}_q(Y)$, with $U, V \in \mathbb{F}_q[Y]$ coprime and $U$ monic. By induction on $k$, $U(Y)^k H_k(Y) = V(Y)^k H_0(Y)$ for $0 \le k \le K$. Taking $k = K$, unique factorization in $\mathbb{F}_q[Y]$ and $\gcd(U^K, V^K) = 1$ yield a nonzero polynomial $W(Y) \in \mathbb{F}_q[Y]$ such that
$$H_0(Y) = W(Y) U(Y)^K, \qquad H_K(Y) = W(Y) V(Y)^K,$$
and $H_k(Y) = W(Y) U(Y)^{K-k} V(Y)^k$ for all $0 \le k \le K$.

For every $a \in A_S$, Lemma 2.2(2) gives $H_0(a^r) = H_K(a^r) = 0$. Since $\gcd(U, V) = 1$, $a^r$ cannot be a common root of $U$ and $V$, so necessarily $W(a^r) = 0$. Injectivity of $a \mapsto a^r$ therefore gives $|A_S| \le \deg W$.

By Lemma 2.2(1),
$$\deg W + K \cdot \max(\deg U, \deg V) = \max(\deg H_0, \deg H_K) \le \frac{r - 1}{2}. \tag{2}$$
Since $r \ge 7$ and $K = \frac{r-3}{2}$, we have $2K = r - 3 > \frac{r-1}{2}$ (as $r - 5 \ge 2 > 0$). Hence $\max(\deg U, \deg V) \le 1$.

If $\max(\deg U, \deg V) = 0$, then $U$ and $V$ are nonzero constants, so for every $b \in B$ we have $b = H_1(b^r)/H_0(b^r) = V/U$, forcing $|B| \le 1$; meanwhile (2) gives $|A_S| \le \deg W \le \frac{r-1}{2}$, so $|A| = |A_S| + |B| \le \frac{r+1}{2} < r$, a contradiction.

Thus $\max(\deg U, \deg V) = 1$. Inequality (2) now gives
$$|A_S| \le \deg W \le \frac{r - 1}{2} - \frac{r - 3}{2} = 1,$$
whence $|B| = r - |A_S| \ge r - 1$. Finally, for every $b \in B$, $H_0(b^r) = W(b^r) U(b^r)^K \neq 0$ implies $U(b^r) \neq 0$, and $b = H_1(b^r)/H_0(b^r) = V(b^r)/U(b^r)$. $\square$

---

#### Step 3: Geometric Classification of $B$ (Affine Lines and Norm Circles)

Write $U(Y) = u_1 Y + u_0$ and $V(Y) = v_1 Y + v_0$. By Lemma 2.3, $\max(\deg U, \deg V) = 1$, $\gcd(U, V) = 1$ (so $u_1 v_0 - u_0 v_1 \neq 0$), $|B| \ge r - 1 \ge 6$, and every $b \in B$ satisfies
$$u_1 b^{r+1} + u_0 b - v_1 b^r - v_0 = 0. \tag{3}$$

We analyze the two possibilities for $u_1$.

##### Subcase 3A: $u_1 = 0$ (Affine Line)

Then $u_0 \neq 0$ and $v_1 \neq 0$. Dividing (3) by $u_0$ yields $b - \alpha b^r = \beta$ for all $b \in B$, where $\alpha = v_1/u_0 \neq 0$ and $\beta = v_0/u_0$. The map $\varphi(z) = z - \alpha z^r$ is $\mathbb{F}_r$-linear on $\mathbb{F}_{r^2}$ (since $(tz)^r = t z^r$ for $t \in \mathbb{F}_r$) and is not identically zero (as $\deg(z - \alpha z^r) = r < r^2$). Hence $\dim_{\mathbb{F}_r} \ker \varphi \le 1$, so the fiber $L := \varphi^{-1}(\beta)$ has size $0$, $1$, or $r$. Since $|B| \ge r - 1 \ge 6 > 1$, $L$ must be an affine $\mathbb{F}_r$-line $L = z_0 + \eta \mathbb{F}_r$ ($\eta \in \mathbb{F}_{r^2}^*$) containing $B$.

- If $0 \in L$, then $L = \eta \mathbb{F}_r$. Since $B \subset L \cap N_2$ is nonempty and $\mathbb{F}_r^* \subset S_2$, we must have $\eta \in N_2$, so $L \cap S_2 = \emptyset$. For any distinct $b_1, b_2 \in B$, $b_1 + b_2 \in L \cap (S_2 \cup \{0\}) = \{0\}$, which forces $|B| \le 2 < r - 1$, a contradiction.
- If $0 \notin L$, then the $r$ nonzero points of $L$ lie on $r$ distinct $\mathbb{F}_r$-lines through $0$ (missing precisely the parallel line $\eta \mathbb{F}_r$). Since the $r + 1$ lines through $0$ in $\mathbb{F}_{r^2}$ partition into $\frac{r+1}{2}$ square lines ($\subset S_2 \cup \{0\}$) and $\frac{r+1}{2}$ nonsquare lines ($\subset N_2 \cup \{0\}$), we obtain
  $$|B| \le |L \cap N_2| \in \left\{\frac{r - 1}{2},\, \frac{r + 1}{2}\right\}.$$
  Hence $r - 1 \le \frac{r+1}{2}$, giving $r \le 3$, contradicting $r \ge 7$.

##### Subcase 3B: $u_1 \neq 0$ (Norm Circle)

Since $U$ is monic, $u_1 = 1$, so (3) reads
$$b^{r+1} + u_0 b - v_1 b^r - v_0 = 0 \qquad \forall b \in B.$$
Raising to the $r$-th power (using $b^{r^2} = b$) gives $b^{r+1} + u_0^r b^r - v_1^r b - v_0^r = 0$, and subtracting yields
$$(u_0 + v_1^r) b - (v_1 + u_0^r) b^r + (v_0^r - v_0) = 0 \qquad \forall b \in B.$$
If $u_0 + v_1^r \neq 0$, then $v_1 + u_0^r = (u_0 + v_1^r)^r \neq 0$ as well, so dividing by $u_0 + v_1^r$ places $B$ on an affine line $b - \alpha b^r = \beta$ ($\alpha \neq 0$), contradicting Subcase 3A. If $u_0 + v_1^r = 0$ and $v_0^r \neq v_0$, the equation has no solutions.

Hence $u_0 = -v_1^r$ and $v_0 \in \mathbb{F}_r$. Setting $c := v_1 \in \mathbb{F}_{r^2}$ and $\lambda := v_0 + c^{r+1} \in \mathbb{F}_r$, note that $\lambda = v_0 - u_0 v_1 = u_1 v_0 - u_0 v_1 \neq 0$ because $\gcd(U, V) = 1$. Equation (3) becomes
$$N(b - c) = (b - c)(b^r - c^r) = \lambda \in \mathbb{F}_r^* \qquad \forall b \in B.$$
Let $C := \{b \in \mathbb{F}_{r^2} : N(b - c) = \lambda\}$, a norm circle of size $r + 1$ containing $B$. We split according to whether $c = 0$, $N(c) = \lambda$, or $c \neq 0$ with $N(c) \neq \lambda$.

---

###### Subcase 3B(i): $c = 0$

Here $N(b) = \lambda$ for all $b \in B$. Fix $b_0 \in B \subset N_2$, and let $g$ be a generator of $\mathbb{F}_{r^2}^*$. Put $\xi := g^{(r-1)/2}$ and $\omega := \xi^2 = g^{r-1}$. Then $\omega$ generates the cyclic group $\mu_{r+1} = \{\zeta \in \mathbb{F}_{r^2}^* : \zeta^{r+1} = 1\}$ of even order $r + 1$, and $\xi^{r+1} = g^{(r^2-1)/2} = -1$, so $\xi^r = -\xi^{-1}$. Every $b \in B$ has the form $b = b_0 \omega^k$ for a unique $k \in \mathbb{Z}/(r+1)\mathbb{Z}$.

Suppose two distinct elements $b_1 = b_0 \omega^{k_1}$ and $b_2 = b_0 \omega^{k_2}$ in $B$ satisfy $k_1 \equiv k_2 \pmod 2$ and $b_1 + b_2 \neq 0$. Then
$$b_1 + b_2 = b_0 \xi^{k_1 + k_2} \bigl(\xi^{k_1 - k_2} + \xi^{-(k_1 - k_2)}\bigr).$$
Since $k_1 + k_2$ is even, $\xi^{k_1+k_2} = \left(g^{\frac{r-1}{2}\cdot\frac{k_1+k_2}{2}}\right)^2 \in S_2$. Since $k_1 - k_2$ is even, $T := \xi^{k_1-k_2} + \xi^{-(k_1-k_2)}$ is nonzero (as $b_1 + b_2 \neq 0$) and satisfies
$$T^r = (-\xi^{-1})^{k_1 - k_2} + (-\xi)^{k_1 - k_2} = (-1)^{k_1 - k_2} T = T,$$
so $T \in \mathbb{F}_r^* \subset S_2$. Since $b_0 \in N_2$, this implies $b_1 + b_2 \in N_2$, contradicting $b_1 + b_2 \in S_2 \cup \{0\}$.

Therefore, any two distinct elements of $B$ in the same parity class of $k \bmod 2$ must sum to $0$, so each of the two parity classes contains at most $2$ elements of $B$. Thus $|B| \le 4$, contradicting $|B| \ge r - 1 \ge 6$.

---

###### Subcase 3B(ii): $c \neq 0$ and Exact Count of $|C \cap N_2|$

Parametrize $C$ by $b = c + z$ with $N(z) = \lambda$, and put $w := c^r z$. Since $c \neq 0$, $z \mapsto w$ is a bijection between $\{z \in \mathbb{F}_{r^2} : N(z) = \lambda\}$ and $\{w \in \mathbb{F}_{r^2} : N(w) = \mu\}$, where $\mu := N(c)\lambda \in \mathbb{F}_r^*$. Moreover,
$$N(c + z) = N(c) + \lambda + c^r z + c z^r = s + \mathrm{Tr}(w), \qquad s := N(c) + \lambda \in \mathbb{F}_r.$$

**Claim 2.4.** *For each $t \in \mathbb{F}_r$, the number of elements $w \in \mathbb{F}_{r^2}$ with $N(w) = \mu$ and $\mathrm{Tr}(w) = t$ is exactly $1 - \chi_{\mathbb{F}_r}(t^2 - 4\mu)$.*

*Proof.* Such $w$ are precisely the roots of $T^2 - tT + \mu = 0$ in $\mathbb{F}_{r^2}$ satisfying $w^r = t - w$ (since then $w \cdot w^r = \mu$ follows from Vieta's formulas). Look at the discriminant $\Delta = t^2 - 4\mu \in \mathbb{F}_r$:
- If $\Delta \in S_2(\mathbb{F}_r)$, the quadratic has two distinct roots $w_1 \neq w_2$ in $\mathbb{F}_r$, each fixed by Frobenius ($w_i^r = w_i \neq w_{3-i} = t - w_i$), giving $0 = 1 - 1$ solutions.
- If $\Delta = 0$, the double root $w = t/2 \in \mathbb{F}_r$ satisfies $w^r = w = t - w$, giving $1 = 1 - 0$ solution.
- If $\Delta \in N_2(\mathbb{F}_r)$, the quadratic is irreducible over $\mathbb{F}_r$ and splits into two distinct Galois conjugates $w_1, w_2 = w_1^r \in \mathbb{F}_{r^2} \setminus \mathbb{F}_r$, both satisfying $w_i^r = t - w_i$, giving $2 = 1 - (-1)$ solutions. $\square$

We also use the elementary quadratic character sum identity: for any nonzero $a \in \mathbb{F}_r^*$,
$$\sum_{t \in \mathbb{F}_r} \chi_{\mathbb{F}_r}(t^2 - a) = -1. \tag{4}$$
(Indeed, if $a = u^2$ with $u \in \mathbb{F}_r^*$, setting $v = (t-u)/(t+u)$ bijects $t \in \mathbb{F}_r \setminus \{-u\}$ onto $v \in \mathbb{F}_r \setminus \{1\}$, giving $\sum_{v \neq 1} \chi_{\mathbb{F}_r}(v) = -1$; if $a \in N_2(\mathbb{F}_r)$, the bijection $w \mapsto \mathrm{Tr}(w)$ above with $\mu = a/4$ gives $r + 1 = |\{w : N(w) = a/4\}| = \sum_{t \in \mathbb{F}_r} (1 - \chi_{\mathbb{F}_r}(t^2 - a)) = r - \sum_t \chi_{\mathbb{F}_r}(t^2 - a)$, again yielding $-1$.)

Now separate the two subcases $\lambda = N(c)$ and $\lambda \neq N(c)$:

1. **If $\lambda = N(c)$ (so $0 \in C$):** Then $s = 2N(c) \neq 0$ and $4\mu = 4N(c)^2 = s^2$, so $t^2 - 4\mu = (t+s)(t-s)$. The unique point $b = 0 \in C$ corresponds to $w = -N(c)$ and $t = -s$. Every other $b \in C$ has $s + t \neq 0$, so $b \in N_2 \iff \chi_{\mathbb{F}_r}(s + t) = -1$, with indicator $\frac{1 - \chi_{\mathbb{F}_r}(s+t)}{2}$. Summing over $t \in \mathbb{F}_r \setminus \{-s\}$ via Claim 2.4, using $\chi_{\mathbb{F}_r}(t^2 - s^2)\chi_{\mathbb{F}_r}(s+t) = \chi_{\mathbb{F}_r}(t - s)$ for $t \neq -s$ and (4):
   \begin{align*}
   |C \cap N_2| &= \frac{1}{2}\sum_{t \neq -s} \bigl(1 - \chi_{\mathbb{F}_r}(t^2 - s^2) - \chi_{\mathbb{F}_r}(s + t) + \chi_{\mathbb{F}_r}(t - s)\bigr) \\
   &= \frac{(r - 1) - (-1) - 0 - \chi_{\mathbb{F}_r}(-2s)}{2} = \frac{r - \chi_{\mathbb{F}_r}(-N(c))}{2} \le \frac{r + 1}{2},
   \end{align*}
   since $\chi_{\mathbb{F}_r}(-2s) = \chi_{\mathbb{F}_r}(-4N(c)) = \chi_{\mathbb{F}_r}(-N(c))$. Thus $|B| \le \frac{r+1}{2} < r - 1$ (as $r \ge 7$), a contradiction.

2. **If $\lambda \neq N(c)$ (so $0 \notin C$):** Then $s + t \neq 0$ for every $t$ occurring as $\mathrm{Tr}(w)$ (indeed, $N(c+z) = 0 \iff z = -c \implies N(c) = N(z) = \lambda$, excluded). Equivalently, at $t = -s$ we have $(-s)^2 - 4\mu = (N(c) - \lambda)^2 \in S_2(\mathbb{F}_r)$, so the multiplicity factor $1 - \chi_{\mathbb{F}_r}(t^2 - 4\mu)$ vanishes at $t = -s$. Every $b \in C$ is therefore nonzero and lies in $N_2$ with indicator $\frac{1 - \chi_{\mathbb{F}_r}(s+t)}{2}$, and the $t = -s$ summand below vanishes automatically. By Claim 2.4, $\sum_{t \in \mathbb{F}_r} \chi_{\mathbb{F}_r}(s+t) = 0$, and (4):
   \begin{align*}
   |C \cap N_2| &= \frac{1}{2}\sum_{t \in \mathbb{F}_r} \bigl(1 - \chi_{\mathbb{F}_r}(t^2 - 4\mu)\bigr)\bigl(1 - \chi_{\mathbb{F}_r}(s + t)\bigr) \\
   &= \frac{r + 1}{2} + \frac{1}{2}\sum_{t \in \mathbb{F}_r} \chi_{\mathbb{F}_r}\!\bigl((s + t)(t^2 - 4\mu)\bigr). \tag{5}
   \end{align*}
   Notice that $f(t) := (s + t)(t^2 - 4\mu) \in \mathbb{F}_r[t]$ is a monic cubic with **three distinct roots** in $\overline{\mathbb{F}}_r$: the roots $\pm 2\sqrt{\mu}$ of $t^2 - 4\mu$ are distinct (since $4\mu \neq 0$ in odd characteristic), and $(-s)^2 - 4\mu = (N(c) - \lambda)^2 \neq 0$ (since $N(c) \neq \lambda$). Hence the projective cubic $E : Y^2 Z = (X + s Z)(X^2 - 4\mu Z^2)$ is a smooth projective curve of genus $1$ (an elliptic curve) over $\mathbb{F}_r$ (for every odd prime power $r$, including $\mathrm{char}(\mathbb{F}_r) = 3$). Counting its $\mathbb{F}_r$-rational points (including $[0:1:0]$) gives
   $$\#E(\mathbb{F}_r) = 1 + \sum_{t \in \mathbb{F}_r} \bigl(1 + \chi_{\mathbb{F}_r}(f(t))\bigr) = r + 1 + \sum_{t \in \mathbb{F}_r} \chi_{\mathbb{F}_r}(f(t)).$$
   By Hasse's theorem (H. Hasse, *Beweis des Analogons der Riemannschen Vermutung für die Artinschen und F. K. Schmidtschen Kongruenzzetafunktionen in gewissen elliptischen Fällen*, Nachr. Ges. Wiss. Göttingen (1933), 253–262), $|\#E(\mathbb{F}_r) - (r + 1)| \le 2\sqrt{r}$, so (5) yields
   $$r - 1 \le |B| \le |C \cap N_2| \le \frac{r + 1}{2} + \sqrt{r}. \tag{6}$$
   Rearranging (6) gives
   $$0 \ge r - 3 - 2\sqrt{r} = (\sqrt{r} - 3)(\sqrt{r} + 1) \implies r \le 9.$$

   This yields an immediate contradiction for **every odd prime power $r \ge 11$** (i.e., $q \ge 121$).

---

###### Subcase 3B(iii): The Two Boundary Cases $r = 7$ ($q = 49$) and $r = 9$ ($q = 81$)

It remains to dispose of the two boundary values $r = 7$ and $r = 9$ in Subcase 3B(ii), where $\lambda \neq N(c)$ and $c \neq 0$.

Put $\theta := \lambda / N(c) \in \mathbb{F}_r^* \setminus \{1\}$, and substitute $t = N(c)\tau$ in (5). Since $(s + N(c)\tau)((N(c)\tau)^2 - 4N(c)\lambda) = N(c)^3 (1 + \theta + \tau)(\tau^2 - 4\theta)$ and $\chi_{\mathbb{F}_r}(N(c)^3) = \chi_{\mathbb{F}_r}(N(c))$, equation (5) becomes
$$|C \cap N_2| = \frac{r + 1}{2} + \frac{1}{2}\chi_{\mathbb{F}_r}(N(c))\, S(\theta), \qquad S(\theta) := \sum_{\tau \in \mathbb{F}_r} \chi_{\mathbb{F}_r}\!\bigl((1 + \theta + \tau)(\tau^2 - 4\theta)\bigr). \tag{7}$$
Observe two symmetries of $S(\theta)$:
- Substituting $\tau = \theta \sigma$ yields $(1 + \theta + \theta\sigma)(\theta^2\sigma^2 - 4\theta) = \theta^3(\theta^{-1} + 1 + \sigma)(\sigma^2 - 4\theta^{-1})$, hence $S(\theta) = \chi_{\mathbb{F}_r}(\theta)\, S(\theta^{-1})$.
- Applying the Frobenius automorphism $x \mapsto x^p$ of $\mathbb{F}_r$ preserves $\chi_{\mathbb{F}_r}$, hence $S(\theta^p) = S(\theta)$.

Moreover, multiplication by any $\alpha \in S_2$ preserves $S_2$, $N_2$, and the condition $B \hat{+} B \subset S_2 \cup \{0\}$, and maps $C = \{N(b - c) = \lambda\}$ to $\{N(b - \alpha c) = N(\alpha)\lambda\}$ (preserving both $\theta$ and $\chi_{\mathbb{F}_r}(N(c))$). Since $S_2$ has index $2$ in $\mathbb{F}_{r^2}^*$, we may scale $A$ by an element of $S_2$ so that $c = 1$ if $c \in S_2$, or $c = g$ (a fixed element of $N_2$) if $c \in N_2$.

**Case $r = 7$ ($q = 49$).** Here $r - 1 = 6$, and (6) gives $|C \cap N_2| \le \lfloor 4 + \sqrt{7}\rfloor = 6$. Thus $|B| \ge 6$ forces $|C \cap N_2| = 6$, $B = C \cap N_2$, and $\chi_7(N(c)) S(\theta) = 4$. The squares in $\mathbb{F}_7^*$ are $\{1, 2, 4\}$ and the nonsquares are $\{3, 5, 6\}$. Compute $S(\theta)$ for $\theta \in \mathbb{F}_7^* \setminus \{1\} = \{2, 3, 4, 5, 6\}$:
- $\theta = 6 \equiv -1$: $(1 + 6 + \tau)(\tau^2 - 24) = \tau(\tau^2 + 4)$ is an odd function of $\tau$ and $\chi_7(-1) = -1$, so $S(6) = 0$.
- $\theta = 2$: $(\tau + 3)(\tau^2 - 1)$ at $\tau = 0,1,2,3,4,5,6$ equals $4, 0, 1, 6, 0, 3, 0 \pmod 7$, with $\chi_7$-values $+1, 0, +1, -1, 0, -1, 0$, so $S(2) = 0$, and $S(4) = \chi_7(2) S(2) = 0$.
- $\theta = 3$: $(\tau + 4)(\tau^2 + 2)$ at $\tau = 0,1,2,3,4,5,6$ equals $1, 1, 1, 0, 4, 5, 2 \pmod 7$, with $\chi_7$-values $+1, +1, +1, 0, +1, -1, +1$, so $S(3) = 4$, and $S(5) = \chi_7(3) S(3) = -4$.

Represent $\mathbb{F}_{49} = \mathbb{F}_7[u]/(u^2 + 1)$ (so $N(x + yu) = x^2 + y^2$, and $g := 2 + u \in N_2$ since $N(g) = 5 \in N_2(\mathbb{F}_7)$). By the calculation above, $\chi_7(N(c))S(\theta) = 4$ holds for precisely two scaled circles:
1. $c = 1$, $\lambda = \theta = 3$;
2. $c = g = 2 + u$, $\lambda = 5 \cdot N(g) \equiv 5 \cdot 5 \equiv 4 \pmod 7$.

In **both** circles, consider the two distinct elements $b_1 := 4 + u$ and $b_2 := 2 + 3u$ in $\mathbb{F}_{49}$:
- $N(b_1) = 4^2 + 1^2 = 17 \equiv 3 \in N_2(\mathbb{F}_7)$ and $N(b_2) = 2^2 + 3^2 = 13 \equiv 6 \in N_2(\mathbb{F}_7)$, so $b_1, b_2 \in N_2$.
- For Circle 1: $N(b_1 - 1) = N(3 + u) = 10 \equiv 3$ and $N(b_2 - 1) = N(1 + 3u) = 10 \equiv 3$, so $b_1, b_2 \in C \cap N_2 = B$.
- For Circle 2: $N(b_1 - (2+u)) = N(2) = 4$ and $N(b_2 - (2+u)) = N(2u) = 4$, so $b_1, b_2 \in C \cap N_2 = B$.
- Yet $b_1 + b_2 = 6 + 4u$ has $N(b_1 + b_2) = 6^2 + 4^2 = 52 \equiv 3 \in N_2(\mathbb{F}_7)$, so $b_1 + b_2 \in N_2$, contradicting $B \hat{+} B \subset S_2 \cup \{0\}$.

**Case $r = 9$ ($q = 81$).** Here $r - 1 = 8$, and (6) gives $|C \cap N_2| \le \frac{9+1}{2} + \sqrt{9} = 8$. Thus $|B| \ge 8$ forces $|C \cap N_2| = 8$, $B = C \cap N_2$, and $\chi_{\mathbb{F}_9}(N(c)) S(\theta) = 6$. Write $\mathbb{F}_9 = \mathbb{F}_3[i]/(i^2 + 1)$, so $S_2(\mathbb{F}_9) = \{1, -1, i, -i\}$ (as $(1+i)^2 = -i$, $(1-i)^2 = i$) and $N_2(\mathbb{F}_9) = \{1+i, 1-i, -1+i, -1-i\}$. Since $4 \equiv 1 \pmod 3$, $S(\theta) = \sum_{\tau \in \mathbb{F}_9} \chi_{\mathbb{F}_9}((1 + \theta + \tau)(\tau^2 - \theta))$. Under $\theta \mapsto \theta^3$ and $\theta \mapsto \theta^{-1}$, the $7$ elements of $\mathbb{F}_9^* \setminus \{1\}$ fall into three orbits:
- $\theta = -1$: $(1 - 1 + \tau)(\tau^2 + 1) = \tau(\tau^2 + 1)$ vanishes at $\tau \in \{0, i, -i\}$ and takes values $\pm 1 \in S_2(\mathbb{F}_9)$ at the remaining $6$ elements of $\mathbb{F}_9$ (for $\tau = \pm 1$, $\tau^3 + \tau = \mp 1$; for $\tau = \pm 1 \pm i$, $(\pm 1 \pm i)^3 + (\pm 1 \pm i) = (\pm 1 \mp i) + (\pm 1 \pm i) = \mp 1$). Hence $S(-1) = 6$.
- Orbit $\{i, -i\}$ ($i^3 = -i$): for $\theta = i$, $(1+i+\tau)(\tau^2 - i)$ vanishes at $\tau \in \{-1-i, 1-i, -1+i\}$ (since $(1-i)^2 = i$), and at $\tau = 0, 1, -1, i, -i, 1+i$ takes values $1-i, -i, 1+i, 1, -1-i, 1-i$ with $\chi_{\mathbb{F}_9}$-values $-1, +1, -1, +1, -1, -1$, so $S(i) = S(-i) = -2$.
- Orbit $\{1+i, 1-i, -1+i, -1-i\}$ (generated by $\theta \mapsto \theta^3$ and $\theta \mapsto \theta^{-1}$): for $\theta = 1+i$, $(-1+i+\tau)(\tau^2 - 1 - i)$ vanishes at $\tau = 1-i$, and at $\tau = 0, 1, -1, i, -i, 1+i, -1+i, -1-i$ takes values $-1, 1, 1-i, 1, -1+i, 1+i, -1+i, -1+i$ with $\chi_{\mathbb{F}_9}$-values $+1, +1, -1, +1, -1, -1, -1, -1$, so $S(1+i) = -2$, and hence $|S(\theta)| = 2$ throughout this orbit.

Therefore $\chi_{\mathbb{F}_9}(N(c))S(\theta) = 6$ holds **only** when $\theta = -1$ and $c \in S_2$, which scales to the unique circle
$$C = \{b \in \mathbb{F}_{81} : N(b - 1) = -1\} = \{1 + z : z \in \mathbb{F}_{81},\, z^{10} = -1\}.$$
Of the $10$ solutions of $z^{10} = -1$ in $\mathbb{F}_{81}^*$, the two solutions $z = \pm i \in \mathbb{F}_9$ give $1 \pm i \in \mathbb{F}_9^* \subset S_2$; since $|C| = 10$ and $|C \cap N_2| = 8$, the remaining $8$ solutions (those in $\mathbb{F}_{81} \setminus \mathbb{F}_9$) must form $C \cap N_2 = B$. Pick any $z \in \mathbb{F}_{81} \setminus \mathbb{F}_9$ with $z^{10} = -1$ (so $z$ has order $20$, $z^9 = -z^{-1}$, and $z^2 \neq -1$). Then $(z^3)^{10} = -1$, $z^3 \neq z$ (as $z^2 \neq 1$), and $z^3 \neq \pm i$ (as $(z^3)^2 = z^6 \neq -1$, since $\mathrm{ord}(z) = 20 \nmid 12$). Hence $b_1 := 1 + z$ and $b_2 := 1 + z^3$ are two distinct elements of $C \cap N_2 = B$.

Put $\beta := z - z^{-1} \in \mathbb{F}_{81}$. Then $\beta^9 = -z^{-1} + z = \beta$, so $\beta \in \mathbb{F}_9^*$. Moreover, since $z^{10} = -1$ and $z^2 \neq -1$, we have $z^8 - z^6 + z^4 - z^2 + 1 = 0$, i.e., $z^4 + z^{-4} - (z^2 + z^{-2}) + 1 = 0$. In characteristic $3$, using $z^2 + z^{-2} = \beta^2 - 1$ and $z^4 + z^{-4} = (z^2 + z^{-2})^2 + 1 = \beta^4 + \beta^2 - 1$, this reduces to
$$(\beta^4 + \beta^2 - 1) - (\beta^2 - 1) + 1 = \beta^4 + 1 = 0,$$
so $\beta^4 = -1$ in $\mathbb{F}_9$. Now compute the norm of $b_1 + b_2 = -1 + z + z^3$ (using $z^9 = -z^{-1}$ and $\beta^3 = z^3 - z^{-3}$ in characteristic $3$):
\begin{align*}
N(b_1 + b_2) &= (-1 + z + z^3)(-1 - z^{-1} - z^{-3}) \\
&= 1 + (z^{-1} + z^{-3} - z - z^3) - (2 + z^2 + z^{-2}) \\
&= -1 - (\beta^2 - 1) - \beta - \beta^3 = -\beta(\beta^2 + \beta + 1).
\end{align*}
Since $\beta \in \mathbb{F}_9$ and $\beta^4 = -1$, we have $(\beta^2 + \beta + 1)^3 = \beta^6 + \beta^3 + 1 = \beta^3 - \beta^2 + 1$, whence
$$(\beta^2 + \beta + 1)^4 = (\beta^3 - \beta^2 + 1)(\beta^2 + \beta + 1) = \beta^5 + \beta + 1 = -\beta + \beta + 1 = 1.$$
Consequently,
$$N(b_1 + b_2)^4 = (-\beta)^4 (\beta^2 + \beta + 1)^4 = (-1)(1) = -1,$$
so $N(b_1 + b_2) \in N_2(\mathbb{F}_9)$, i.e., $b_1 + b_2 \in N_2$, contradicting $B \hat{+} B \subset S_2 \cup \{0\}$.

---

This exhausts all subcases of Case 2 and proves $|A| < r$ whenever $A + A \not\subset S_2 \cup \{0\}$. Combined with Case 1, this completes the proof of the Theorem. $\blacksquare$

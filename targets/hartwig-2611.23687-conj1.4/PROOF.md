# Proof of Conjecture 1.4 (`\label{conj_denominator_N-truncated}`) of Hartwig–Shrivastava (`arXiv:2611.23687v1`)

## Theorem Statement

Let $\mathrm{Vir} = \mathrm{Vir}^- \oplus \mathfrak{h} \oplus \mathrm{Vir}^+$ be the complex Virasoro Lie algebra with basis $\{c, L_n : n \in \mathbb{Z}\}$, $\mathfrak{h} = \mathbb{C} L_0 \oplus \mathbb{C} c$, and brackets $[L_m, L_n] = (m-n)L_{m+n} + \frac{m^3-m}{12}\delta_{m+n,0}c$, $[L_n, c] = 0$. Let $P_N = \sum_{n=0}^N P[n]$ be the $N$-truncation of the Virasoro extremal projector, where $P[0] = 1$ and
$$P[n] = \sum_{\lambda, \mu \vdash n} b^{(n)}_{\lambda, \mu}(L_0, c) \, L_\lambda^\dagger L_\mu, \qquad b^{(n)}_{\lambda,\mu}(L_0,c) \in \mathbb{Q}(L_0, c).$$
For $r, s \ge 1$, let
$$\varphi_{r,s}(L_0, c) = L_0 - h_{r,s}(c), \qquad h_{r,s}(c) = \frac{(13-c)(r^2+s^2) - 24rs + 2(c-1) + (r^2-s^2)\sqrt{(c-1)(c-25)}}{48},$$
let $K_n(L_0, c) = c_n \prod_{rs=n} \varphi_{r,s}(L_0, c) \in \mathbb{Z}[L_0, c]$ be the primitive polynomial with positive leading coefficient in $L_0$, and let $\tau_{-n}$ be the automorphism of $\mathbb{C}(L_0, c)$ defined by $\tau_{-n}(L_0) = L_0 - n$, $\tau_{-n}(c) = c$. Define
$$D_N(L_0, c) = \prod_{n=1}^N \tau_{-n}\bigl(K_n(L_0, c)\bigr) = \prod_{n=1}^N K_n(L_0 - n, c).$$

**Theorem (Conjecture 1.4 of [arXiv:2611.23687v1]).** For every integer $N \ge 1$, $D_N P_N \in U(\mathrm{Vir})$, and $D_N$ divides every nonzero polynomial $Q(L_0, c) \in \mathbb{C}[L_0, c]$ satisfying $Q P_N \in U(\mathrm{Vir})$. In particular, $D_N$ is the unique (up to $\mathbb{C}^\times$) least-degree polynomial in $L_0, c$ regularizing $P_N$.

*(Remark: As noted after Conjecture 1.4 in `arXiv:2611.23687v1`, Conjecture 1.5 (`\label{conj_denominator_full}`) for the total denominator $D = \prod_{n=1}^\infty \tau_{-n}(K_n)$ follows immediately.)*

---

## Proof

### Step 1: PBW criterion for regularizing $P_N$

By the Poincaré–Birkhoff–Witt theorem for $\mathrm{Vir} = \mathrm{Vir}^- \oplus \mathfrak{h} \oplus \mathrm{Vir}^+$, the elements $\{L_\lambda^\dagger L_0^a c^b L_\mu\}_{\lambda,\mu \in \mathcal{P},\, a,b \ge 0}$ form a $\mathbb{C}$-basis of $U(\mathrm{Vir})$, where $\mathcal{P}$ is the set of all integer partitions, $L_\mu = L_{\mu_1}\cdots L_{\mu_r}$ ($\mu_1 \le \dots \le \mu_r$), and $L_\lambda^\dagger = L_{-\lambda_k}\cdots L_{-\lambda_1}$. By Lemma 3.1 (`\label{lem:shift-property}`), $L_\lambda^\dagger L_0^a c^b = (L_0 - |\lambda|)^a c^b L_\lambda^\dagger$, and $f \mapsto \tau_{-|\lambda|}(f)$ is an automorphism of $\mathbb{C}[L_0, c]$. Therefore $\{L_\lambda^\dagger L_\mu\}_{\lambda,\mu \in \mathcal{P}}$ is a free left $\mathbb{C}[L_0, c]$-basis of $U(\mathrm{Vir})$.

Consequently, a nonzero polynomial $Q \in \mathbb{C}[L_0, c]$ satisfies $Q P_N \in U(\mathrm{Vir})$ if and only if
$$Q(L_0, c) \, b^{(n)}_{\lambda, \mu}(L_0, c) \in \mathbb{C}[L_0, c] \qquad \text{for all } 1 \le n \le N \text{ and all } \lambda, \mu \vdash n.$$
Thus, if we prove by induction on $n \ge 1$ that
1. $D_n(L_0, c) \, b^{(n)}_{\lambda, \mu}(L_0, c) \in \mathbb{C}[L_0, c]$ for all $\lambda, \mu \vdash n$, and
2. every irreducible factor of $\tau_{-n}(K_n(L_0, c))$ in $\mathbb{C}[L_0, c]$ divides the denominator of at least one $b^{(n)}_{\lambda,\mu}(L_0, c)$ (in reduced form in the UFD $\mathbb{C}[L_0, c]$),

together with pairwise coprimality of the irreducible factors of $\tau_{-n}(K_n)$ across $n \ge 1$ (Step 2), it follows immediately that $D_N$ regularizes $P_N$ and divides every regularizing polynomial $Q \in \mathbb{C}[L_0, c]$.

---

### Step 2: Irreducible factorization and pairwise coprimality of $\tau_{-n}(K_m)$

For $r = s \ge 1$, we have $\varphi_{r,r}(L_0, c) = L_0 - \frac{(r^2-1)(1-c)}{24}$, which is linear in $L_0$ and irreducible in $\mathbb{C}[L_0, c]$. For $1 \le r < s$, the pair $(r,s)$ and $(s,r)$ contributes
$$P_{r,s}(L_0, c) := \varphi_{r,s}(L_0, c)\varphi_{s,r}(L_0, c) = \left(L_0 - \frac{(13-c)(r^2+s^2) - 24rs + 2(c-1)}{48}\right)^2 - \left(\frac{r^2-s^2}{48}\right)^2 (c-1)(c-25) \in \mathbb{Q}[L_0, c].$$
Since $r^2 - s^2 \neq 0$ and $(c-1)(c-25)$ has simple roots at $c=1, 25$ (hence is not a square in $\mathbb{C}[c]$), the quadratic discriminant of $P_{r,s}$ with respect to $L_0$ is not a square in $\mathbb{C}(c)$. Because $P_{r,s}$ is monic in $L_0$, it is irreducible in $\mathbb{C}(c)[L_0]$ and hence irreducible in $\mathbb{C}[L_0, c]$. Thus, up to nonzero scalar constants,
$$K_m(L_0, c) \propto \Bigl(\prod_{\substack{1 \le r < s \\ rs = m}} P_{r,s}(L_0, c)\Bigr) \cdot \begin{cases} \varphi_{\sqrt{m}, \sqrt{m}}(L_0, c) & \text{if } m \text{ is a square,} \\ 1 & \text{otherwise.} \end{cases}$$

We claim that all polynomials $\tau_{-n}(\varphi_{r,r})$ ($n \ge 1, r \ge 1$) and $\tau_{-n}(P_{r,s})$ ($n \ge 1, 1 \le r < s$) are pairwise non-associate in $\mathbb{C}[L_0, c]$:
- Comparing $L_0$-degrees separates linear factors $\tau_{-n}(\varphi_{r,r})$ from quadratic factors $\tau_{-n'}(P_{r',s'})$.
- If $\tau_{-n}(\varphi_{r,r}) = \tau_{-n'}(\varphi_{r',r'})$, comparing $c$-coefficients gives $r^2 - 1 = r'^2 - 1 \implies r = r'$, and comparing constant terms gives $n = n'$.
- If $\tau_{-n}(P_{r,s}) = \tau_{-n'}(P_{r',s'})$ with $1 \le r < s$ and $1 \le r' < s'$, comparing their $L_0$-discriminants gives $(s^2 - r^2)^2 = (s'^2 - r'^2)^2 \implies s^2 - r^2 = s'^2 - r'^2$, and comparing the $c$-coefficient of the $L_0^1$-term gives $r^2 + s^2 - 2 = r'^2 + s'^2 - 2$. Hence $r = r'$, $s = s'$, and comparing the constant coefficient of the $L_0^1$-term yields $n = n'$.

In particular, every $K_m(L_0, c)$ is squarefree in $\mathbb{C}[L_0, c]$, and $\gcd\bigl(\tau_{-n}(K_m),\, \tau_{-n'}(K_{m'})\bigr) = 1$ whenever $(n, m) \neq (n', m')$. Moreover, every $\tau_{-n}(K_m)$ has constant (nonzero) leading coefficient in $L_0$, so no nonconstant polynomial in $\mathbb{C}[c]$ divides $\tau_{-n}(K_m)$.

---

### Step 3: Local Smith Normal Form of the Shapovalov matrix at generic $c$

Fix $n \ge 1$. Let $Z_n \subset \mathbb{C}$ be the finite set consisting of $1$, $25$, and all roots of the nonzero $L_0$-resultants $\mathrm{Res}_{L_0}(Q_1, Q_2) \in \mathbb{C}[c] \setminus \{0\}$ as $Q_1 \neq Q_2$ range over all irreducible factors of $\prod_{1 \le m, k \le n} \tau_{-k}(K_m)$ and all irreducible factors of $\prod_{1 \le m \le n} K_m(L_0 + j, c)$ ($0 \le j \le n$). Fix any $c \in \mathbb{C} \setminus Z_n$. Then:
1. All roots $h_{r,s}(c)$ ($1 \le rs \le n$) are simple roots of $K_1 \cdots K_n$ and are pairwise distinct.
2. All shifted roots $h_{r,s}(c) + j$ ($1 \le rs \le n$, $0 \le j \le n$) are pairwise distinct.

Let $S^{(n)}(L_0, c)$ be the level-$n$ Shapovalov matrix with entries $S^{(n)}_{\mu,\eta}(L_0, c) \mathbf{1} = L_\mu L_\eta^\dagger \mathbf{1}$ ($\mu, \eta \vdash n$). By Kac's determinant formula (eq. (1.7) of `arXiv:2611.23687v1`),
$$\det S^{(n)}(L_0, c) = C_n \prod_{1 \le rs \le n} \varphi_{r,s}(L_0, c)^{p(n - rs)}, \qquad C_n \in \mathbb{Q}^\times.$$

Fix $(r, s)$ with $rs = m \le n$, and set $h_0 = h_{r,s}(c)$. Consider the Verma module $M(h_0, c) = U(\mathrm{Vir}) / (U(\mathrm{Vir})\mathrm{Vir}^+ + U(\mathrm{Vir})(L_0 - h_0) + U(\mathrm{Vir})(c - c))$ at specialized weight $h_0$ and central charge $c$. Let $\mathcal{O} = \mathbb{C}[L_0]_{(L_0 - h_0)}$ be the discrete valuation ring with uniformizer $\varepsilon = L_0 - h_0$.

- By choice of $c \notin Z_n$, $\det S^{(k)}(h_0, c) \neq 0$ for every $0 \le k < m$, whereas $\mathrm{ord}_{\varepsilon}(\det S^{(m)}(L_0, c)) = p(0) = 1$. Hence $\dim_{\mathbb{C}} \ker S^{(m)}(h_0, c) = 1$.
- Let $v_0 = \hat v_0 \mathbf{1} \in M(h_0, c)[-m] \setminus \{0\}$ ($\hat v_0 \in U(\mathrm{Vir}^-)_{-m} \setminus \{0\}$) span $\ker S^{(m)}(h_0, c)$. For every $1 \le j \le m$ and every $w \in M(h_0, c)[-(m-j)]$,
  $$\langle w \mid L_j v_0 \rangle = \langle L_{-j} w \mid v_0 \rangle = 0$$
  since $L_{-j} w \in M(h_0, c)[-m]$ and $v_0 \in \ker S^{(m)}(h_0, c)$. Because $S^{(m-j)}(h_0, c)$ is non-degenerate, $L_j v_0 = 0$ for all $1 \le j \le m$ (and trivially for $j > m$ as $M(h_0, c)[j - m] = 0$). Thus $v_0$ is a singular vector of weight $h_0 + m$.
- Consider the $p(n - m)$ vectors $\{L_\nu^\dagger v_0 : \nu \vdash n - m\} \subset M(h_0, c)[-n]$. Because $\mathrm{gr} U(\mathrm{Vir}^-) \cong \mathrm{Sym}(\mathrm{Vir}^-)$ is an integral domain, $U(\mathrm{Vir}^-)$ has no zero divisors; since $\{L_\nu^\dagger\}_{\nu \vdash n-m}$ are linearly independent in $U(\mathrm{Vir}^-)$ and $\hat v_0 \neq 0$, the elements $\{L_\nu^\dagger \hat v_0\}_{\nu \vdash n-m}$ are $\mathbb{C}$-linearly independent in $U(\mathrm{Vir}^-)$, so $\{L_\nu^\dagger v_0\}_{\nu \vdash n-m}$ is a $p(n-m)$-dimensional subspace of $M(h_0, c)[-n]$.
- Moreover, for every $\nu \vdash n - m$ and every $u \in M(h_0, c)[-n]$, since $(L_\nu^\dagger)^\dagger = L_\nu$ and $L_\nu u \in M(h_0, c)[-m]$,
  $$\langle u \mid L_\nu^\dagger v_0 \rangle = \langle L_\nu u \mid v_0 \rangle = 0.$$
  Hence $\mathrm{span}_{\mathbb{C}}\{L_\nu^\dagger v_0 : \nu \vdash n - m\} \subseteq \ker S^{(n)}(h_0, c)$, giving $\dim_{\mathbb{C}} \ker S^{(n)}(h_0, c) \ge p(n - m)$.
- By the Smith normal form over the PID $\mathcal{O}$, there exist $U, V \in \mathrm{GL}_{p(n)}(\mathcal{O})$ and integers $0 \le e_1 \le \dots \le e_{p(n)}$ such that
  $$S^{(n)}(L_0, c) = U(L_0) \, \mathrm{diag}(\varepsilon^{e_1}, \dots, \varepsilon^{e_{p(n)}}) \, V(L_0).$$
  On the other hand, $\sum_{i=1}^{p(n)} e_i = \mathrm{ord}_\varepsilon(\det S^{(n)}(L_0, c)) = p(n - m)$, while $\#\{i : e_i \ge 1\} = \dim_{\mathbb{C}} \ker S^{(n)}(h_0, c) \ge p(n - m)$. Since each $e_i \ge 1$ contributes at least $1$ to $\sum e_i$, we must have $e_i \in \{0, 1\}$ for all $i$, exactly $p(n-m)$ exponents equal to $1$, and
  $$\ker S^{(n)}(h_0, c) = \mathrm{span}_{\mathbb{C}}\{L_\nu^\dagger v_0 : \nu \vdash n - m\}.$$
  In particular, for $m = n$ ($p(0) = 1$), $\ker S^{(n)}(h_0, c) = \mathbb{C} v_0$.

---

### Step 4: Inductive proof of Claims 1 and 2

Let $B^{(n)}_{\mathrm{shifted}}(L_0, c)$ be the $p(n) \times p(n)$ matrix with $(\lambda, \mu)$-entry $b^{(n)}_{\lambda,\mu}(L_0 + n, c)$. Note that under $L_0 \mapsto L_0 + n$, the divisor $\tau_{-n}(K_m(L_0, c)) = K_m(L_0 - n, c)$ becomes $K_m(L_0, c)$. Thus Claims 1 and 2 at level $n$ are equivalent to:
- (1') $D_n(L_0 + n, c) B^{(n)}_{\mathrm{shifted}}(L_0, c)$ has entries in $\mathbb{C}[L_0, c]$;
- (2') every irreducible factor of $K_n(L_0, c)$ divides the denominator of some entry of $B^{(n)}_{\mathrm{shifted}}(L_0, c)$.

In Section 3.2 of `arXiv:2611.23687v1` (eqs. (3.24)–(3.31)), the defining condition $P_n|_{M[-n]} = 0$ yields
$$B^{(n)}_{\mathrm{shifted}}(L_0, c) \, S^{(n)}(L_0, c) = R^{(n)}(L_0, c),$$
where $R^{(n)}(L_0, c)$ is the $p(n) \times p(n)$ matrix encoding $-P_{n-1}|_{M[-n]}$ with $U(\mathfrak{h})$ placed on the right of $L_\lambda^\dagger$:
$$-P_{n-1}(L_\eta^\dagger \mathbf{1}) = \sum_{\lambda \vdash n} L_\lambda^\dagger R^{(n)}_{\lambda, \eta}(L_0, c) \mathbf{1}.$$
Specifically, since $P[0] = 1$ and $b^{(k)}_{\alpha,\beta}(L_0, c) L_\lambda^\dagger = L_\lambda^\dagger b^{(k)}_{\alpha,\beta}(L_0 + n, c)$ for $|\lambda| = n$, every entry of $R^{(n)}(L_0, c)$ is a $\mathbb{Q}[L_0, c]$-linear combination of $1$ and $b^{(k)}_{\alpha,\beta}(L_0 + n, c)$ for $1 \le k \le n - 1$, $\alpha, \beta \vdash k$.

We proceed by induction on $n \ge 1$. For the base case $n = 1$, $P[1] = b^{(1)}_{(1),(1)}(L_0, c) L_{-1} L_1$ with $b^{(1)}_{(1),(1)}(L_0, c) = -\frac{1}{2(L_0 - 1)}$, whose denominator is $\tau_{-1}(K_1) = L_0 - 1 = D_1$, verifying (1) and (2).

Now assume (1) and (2) hold for all $1 \le k \le n - 1$ ($n \ge 2$).
By the induction hypothesis, $D_{n-1}(L_0, c) b^{(k)}_{\alpha,\beta}(L_0, c) \in \mathbb{C}[L_0, c]$ for all $1 \le k \le n - 1$, so
$$D_{n-1}(L_0 + n, c) \, R^{(n)}(L_0, c) \in \mathrm{Mat}_{p(n)}\bigl(\mathbb{C}[L_0, c]\bigr).$$
Moreover, by Step 3 (and Cramer's rule with Kac's determinant), every entry of $S^{(n)}(L_0, c)^{-1}$ has denominator dividing $\det S^{(n)}(L_0, c)$, whose irreducible factors are precisely the irreducible factors of $K_1(L_0, c), \dots, K_n(L_0, c)$ (with no $c$-only factor, since $\det S^{(n)}$ has constant leading coefficient $C_n$ in $L_0$; indeed Theorem 1.3 already proves that $(K_1 \cdots K_n)(L_0, c) S^{(n)}(L_0, c)^{-1}$ has polynomial entries). Thus any irreducible factor dividing the denominator of any entry of $B^{(n)}_{\mathrm{shifted}}(L_0, c) = R^{(n)}(L_0, c) S^{(n)}(L_0, c)^{-1}$ divides
$$D_{n-1}(L_0 + n, c) \cdot \prod_{m=1}^n K_m(L_0, c).$$
Notice that $D_{n-1}(L_0 + n, c) = \prod_{k=1}^{n-1} K_k(L_0 + n - k, c)$ is coprime to $K_m(L_0, c)$ for every $1 \le m \le n$ by Step 2 (since $n - k \ge 1$). Furthermore, Theorem 1.3 (`\label{denominator-theorem}`) guarantees that every irreducible factor appears in the denominator of $b^{(n)}_{\lambda,\mu}$ with multiplicity at most $1$ (since $D'_n$ is squarefree!). (Alternatively, the simple-pole Smith normal form $e_i \in \{0, 1\}$ in Step 3 shows directly at generic $c$ that each $K_m$ divides the denominator to order at most $1$.)

Let $c \in \mathbb{C} \setminus Z_n$ be generic, and let $h_0 = h_{r,s}(c)$ with $rs = m \le n$. Since $D_{n-1}(h_0 + n, c) \neq 0$, every $b^{(k)}_{\alpha,\beta}(L_0 + n, c)$ ($1 \le k \le n - 1$) is regular at $L_0 = h_0$, so $R^{(n)}(L_0, c) \in \mathrm{Mat}_{p(n)}(\mathcal{O})$ and $R^{(n)}(h_0, c)$ represents $-P_{n-1}|_{M(h_0, c)[-n]}$.

**Proof of (1') (cancellation of all $K_m$ with $1 \le m < n$):**
Assume $1 \le m < n$. By Step 3, $\ker S^{(n)}(h_0, c) = \mathrm{span}_{\mathbb{C}}\{L_\nu^\dagger v_0 : \nu \vdash n - m\}$, where $v_0 \in M(h_0, c)[-m]$ is a singular vector ($L_j v_0 = 0$ for all $j \ge 1$, $L_0 v_0 = (h_0 + m) v_0$). Fix any $\nu \vdash n - m$:
- For $k > n - m$ and any $\beta \vdash k$, every PBW normal form term of $L_\beta L_\nu^\dagger$ has positive weight $k - (n - m) > 0$, hence takes the form $L_\gamma^\dagger L_0^a c^b L_\delta$ with $|\delta| - |\gamma| = k - (n - m) > 0$, forcing $|\delta| > 0$. Since $L_j v_0 = 0$ for all $j \ge 1$, we get $L_\beta(L_\nu^\dagger v_0) = 0$, and hence $P[k](L_\nu^\dagger v_0) = 0$ for all $n - m < k \le n - 1$.
- Consequently, $P_{n-1}(L_\nu^\dagger v_0) = P_{n-m}(L_\nu^\dagger v_0)$. Now $n - m \ge 1$, and because $v_0$ is a highest-weight vector of weight $h_0 + m$ in $M(h_0, c)$, the coefficients $b^{(k)}_{\alpha,\beta}(L_0, c)$ ($1 \le k \le n - m$) in $P_{n-m}(L_\nu^\dagger v_0)$ evaluate at $L_0 = (h_0 + m) + (n - m) = h_0 + n$. Since $D_{n-m}(h_0 + n, c) \neq 0$ (as $D_{n-m} \mid D_{n-1}$ and $D_{n-1}(h_0 + n, c) \neq 0$), the rational-function identity $P_{n-m}|_{M[-(n-m)]} = 0$ specializes without poles at $(h_0 + m, c)$, yielding $P_{n-m}(L_\nu^\dagger v_0) = 0$.

Therefore $R^{(n)}(h_0, c) \, \ker S^{(n)}(h_0, c) = 0$. Using the Smith normal form $S^{(n)}(L_0, c) = U(L_0) \mathrm{diag}(1, \dots, 1, \varepsilon, \dots, \varepsilon) V(L_0)$ from Step 3, $\ker S^{(n)}(h_0, c)$ is spanned by the last $p(n - m)$ columns of $V(h_0)^{-1}$. Thus the last $p(n - m)$ columns of $R^{(n)}(L_0, c) V(L_0)^{-1}$ vanish at $\varepsilon = 0$, hence are divisible by $\varepsilon$ in $\mathcal{O}$. Multiplying by $\mathrm{diag}(1, \dots, 1, \varepsilon^{-1}, \dots, \varepsilon^{-1}) U(L_0)^{-1}$ shows that
$$B^{(n)}_{\mathrm{shifted}}(L_0, c) = R^{(n)}(L_0, c) S^{(n)}(L_0, c)^{-1} \in \mathrm{Mat}_{p(n)}(\mathcal{O}),$$
so $B^{(n)}_{\mathrm{shifted}}(L_0, c)$ has no pole at $L_0 = h_0$.

Now let $q(L_0, c)$ be any irreducible factor of $K_m(L_0, c)$ ($1 \le m < n$), and write an entry of $B^{(n)}_{\mathrm{shifted}}(L_0, c)$ in lowest terms as $f(L_0, c)/g(L_0, c)$ in $\mathbb{C}[L_0, c]$. If $q \mid g$, then $\gcd(f, q) = 1$, so $\mathrm{Res}_{L_0}(f, q) \in \mathbb{C}[c] \setminus \{0\}$ has only finitely many roots. Picking $c \in \mathbb{C} \setminus Z_n$ avoiding those finitely many roots, any root $h_0 = h_{r,s}(c)$ of $q(L_0, c) = 0$ satisfies $g(h_0, c) = 0$ and $f(h_0, c) \neq 0$, giving a pole of $f/g$ at $L_0 = h_0$, contradiction. Hence $q \nmid g$.

Combining this with Theorem 1.3 (or with the simple-pole bound from Step 3), no irreducible factor of $K_m(L_0, c)$ ($1 \le m < n$) divides any denominator of $B^{(n)}_{\mathrm{shifted}}(L_0, c)$, leaving only factors dividing $D_{n-1}(L_0 + n, c) K_n(L_0, c) = D_n(L_0 + n, c)$. Shifting $L_0 \mapsto L_0 - n$ gives $D_n(L_0, c) b^{(n)}_{\lambda,\mu}(L_0, c) \in \mathbb{C}[L_0, c]$, proving (1') and (1).

**Proof of (2') (necessity of every factor of $K_n$):**
Let $q(L_0, c)$ be any irreducible factor of $K_n(L_0, c)$, corresponding to $(r, s)$ with $rs = n$, and suppose for contradiction that $q$ does not divide the denominator of any entry of $B^{(n)}_{\mathrm{shifted}}(L_0, c)$. Since $q$ is coprime to $D_n(L_0 + n, c) / K_n(L_0, c)$ and appears with multiplicity at most $1$ in $D_n(L_0 + n, c)$, all entries of $B^{(n)}_{\mathrm{shifted}}(L_0, c)$ have denominators coprime to $q$. Choose $c \in \mathbb{C} \setminus Z_n$ avoiding the finite set of roots of $\mathrm{Res}_{L_0}(q, g)$ for all reduced denominators $g$ of entries of $B^{(n)}_{\mathrm{shifted}}(L_0, c)$, and let $h_0 = h_{r,s}(c)$ be a root of $q(L_0, c) = 0$.

Then $B^{(n)}_{\mathrm{shifted}}(h_0, c)$ and $R^{(n)}(h_0, c)$ are finite matrices in $\mathrm{Mat}_{p(n)}(\mathbb{C})$ satisfying
$$B^{(n)}_{\mathrm{shifted}}(h_0, c) \, S^{(n)}(h_0, c) = R^{(n)}(h_0, c).$$
By Step 3 ($m = n$), $\ker S^{(n)}(h_0, c) = \mathbb{C} v_0$, where $v_0 \in M(h_0, c)[-n] \setminus \{0\}$ is a singular vector ($L_j v_0 = 0$ for all $j \ge 1$). Let $u_0 \in \mathbb{C}^{p(n)} \setminus \{0\}$ be the coordinate vector of $v_0$ in the basis $\{L_\eta^\dagger \mathbf{1}\}_{\eta \vdash n}$. Applying the matrix identity to $u_0$:
- Left-hand side: $B^{(n)}_{\mathrm{shifted}}(h_0, c) \bigl( S^{(n)}(h_0, c) u_0 \bigr) = 0$.
- Right-hand side: $R^{(n)}(h_0, c) u_0$ is the coordinate vector of $-P_{n-1}(v_0)$. Because $v_0$ is singular, $L_\beta v_0 = 0$ for every partition $\beta$ with $|\beta| = k \ge 1$, so $P[k](v_0) = 0$ for all $1 \le k \le n - 1$, while $P[0](v_0) = v_0$. Hence $-P_{n-1}(v_0) = -v_0$, so $R^{(n)}(h_0, c) u_0 = -u_0 \neq 0$.

Thus $0 = -u_0 \neq 0$, a contradiction. Therefore every irreducible factor of $K_n(L_0, c)$ divides the denominator of some entry of $B^{(n)}_{\mathrm{shifted}}(L_0, c)$, proving (2') and (2).

By induction, (1) and (2) hold for all $n \ge 1$. For any $N \ge 1$, $D_N = \prod_{n=1}^N \tau_{-n}(K_n)$ regularizes $P_1, \dots, P_N$ (since $D_n \mid D_N$ for $1 \le n \le N$), and every irreducible factor of $D_N$ divides the denominator of some $b^{(n)}_{\lambda,\mu}$ ($1 \le n \le N$), hence must divide every regularizing polynomial $Q \in \mathbb{C}[L_0, c]$. Since all irreducible factors of $D_N$ are pairwise non-associate and occur with multiplicity $1$, $D_N \mid Q$, proving that $D_N$ is the least-degree regularizing polynomial for $P_N$. $\blacksquare$

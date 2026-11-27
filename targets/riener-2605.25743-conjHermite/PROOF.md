# Proof of Conjecture 6.5 (`conj:hermite`) and Conjecture 1.1 (`conj:sos`) in Riener–Shapiro (`arXiv:2605.25743v3`)

## Primary Source and Statements

**Source:** Cordian Riener and Boris Shapiro, *"Discriminants of derivatives: square graphs and sums of squares"*, `arXiv:2605.25743v3` (2026-10-21; source file `article.tex`).

For an integer $n \ge 2$ and independent indeterminates $x_1, \ldots, x_n$, let
$$P(t) := \prod_{i=1}^n (t - x_i)$$
and for $0 \le k \le n - 2$ let $\mathcal{D}_k^{(n)} := \mathrm{disc}\bigl(P^{(k)}\bigr)$, with the standard leading-coefficient normalization (Section 1, `article.tex` lines 95–105): if $f(t) = c \prod_{j=1}^m (t - \theta_j)$, then
$$\mathrm{disc}(f) = c^{2m - 2} \prod_{1 \le a < b \le m} (\theta_a - \theta_b)^2.$$
For a monic polynomial $f$ of degree $r$ with roots $\theta_1, \ldots, \theta_r$ and Newton power sums $s_j(f) = \sum_{\ell=1}^r \theta_\ell^j$ ($s_0(f) = r$), its *ordinary Hermite matrix* is (Section 6, `article.tex` lines 1716–1725)
$$H(f) := \bigl(s_{i+j}(f)\bigr)_{0 \le i, j \le r - 1},$$
and an *SOS-matrix factorization* of $H(f)$ over a polynomial ring $R$ is an identity $H(f) = A^{\mathsf T} A$ for a matrix $A$ with entries in $R$.

We prove both open conjectures stated in `arXiv:2605.25743v3`:

> **Conjecture 6.5** (*Hermite-matrix SOS conjecture*, `\label{conj:hermite}`, Section 6, `article.tex` lines 1983–1987).
> For every $n \ge 2$ and $0 \le k \le n - 2$, the ordinary Hermite matrix of $P^{(k)}/\mathrm{lc}(P^{(k)})$ is an SOS matrix over $\mathbb{R}[x_1,\ldots,x_n]$.

> **Conjecture 1.1** (*sum-of-squares question*, `\label{conj:sos}`, Section 1, `article.tex` lines 123–126).
> For every $n \ge 2$ and every $0 \le k \le n - 2$, the polynomial $\mathcal{D}_k^{(n)}$ is a sum of squares of polynomials in the differences $x_i - x_j$.

In fact, our proof produces an explicit closed-form **positive-rational-weighted** SOS-matrix factorization of $H\bigl(P^{(k)}/\mathrm{lc}(P^{(k)})\bigr)$ over $\mathbb{Q}[x_1, \ldots, x_n]$ as well as an SOS-matrix factorization with exactly $\binom{n}{n - k - 1}$ rows over $\mathbb{R}[x_1, \ldots, x_n]$, and hence an explicit positive-rational-weighted sum-of-squares representation of $\mathcal{D}_k^{(n)}$ in $\mathbb{Q}[\{x_i - x_j\}]$.

---

## Proof

Fix integers $n \ge 2$ and $0 \le k \le n - 2$, and set $r := n - k$, so that $2 \le r \le n$. Write $[n] := \{1, \ldots, n\}$, and for any subset $S \subseteq [n]$ define the monic polynomial
$$P_S(t) := \prod_{i \in S} (t - x_i) \in \mathbb{Z}[t, x_1, \ldots, x_n]$$
(with $P_\emptyset(t) = 1$). Let $\binom{[n]}{m}$ denote the collection of all $m$-element subsets of $[n]$.

### Lemma 1 (Normalized derivative and subset-average identities)

Put $J_{n, r}(t) := P^{(k)}(t) / \mathrm{lc}(P^{(k)})$. Then $\mathrm{lc}(P^{(k)}) = \frac{n!}{r!}$, and
$$J_{n, r}(t) = \frac{r!}{n!} P^{(n - r)}(t) = \binom{n}{r}^{-1} \sum_{S \in \binom{[n]}{r}} P_S(t), \qquad J'_{n, r}(t) = r \binom{n}{r - 1}^{-1} \sum_{T \in \binom{[n]}{r - 1}} P_T(t).$$

*Proof.* Differentiating $P(t) = \prod_{i=1}^n (t - x_i)$ repeatedly $k = n - r$ times by the product rule produces the sum over all ordered $k$-tuples of distinct indices removed from $[n]$. Each remaining $r$-subset $S \in \binom{[n]}{r}$ arises from $k!$ orderings of $[n] \setminus S$, so $P^{(k)}(t) = k! \sum_{S \in \binom{[n]}{r}} P_S(t)$. Since each $P_S(t)$ is monic of degree $r$, the leading coefficient is $\mathrm{lc}(P^{(k)}) = k! \binom{n}{r} = \frac{n!}{r!}$, yielding the first identity. Differentiating once more gives $P^{(k + 1)}(t) = (k + 1)! \sum_{T \in \binom{[n]}{r - 1}} P_T(t)$, and dividing by $\frac{n!}{r!}$ gives $\frac{(k + 1)!\, r!}{n!} = r \binom{n}{r - 1}^{-1}$. $\square$

---

### Lemma 2 (Unimodular Bezoutian–Hermite congruence)

Let $f(t) = \sum_{d = 0}^r c_d t^{r - d}$ ($c_0 = 1$) be a monic polynomial of degree $r \ge 2$. Define its *Bezoutian matrix* $B(f) = (b_{i, j})_{0 \le i, j \le r - 1}$ by the bivariate polynomial identity
$$\sum_{i = 0}^{r - 1} \sum_{j = 0}^{r - 1} b_{i, j}\, s^i t^j = \frac{f(s) f'(t) - f'(s) f(t)}{s - t},$$
and let $T(f) = \bigl(T(f)_{i, a}\bigr)_{0 \le i, a \le r - 1}$ be the $r \times r$ matrix over $\mathbb{Z}[c_1, \ldots, c_{r - 1}]$ defined by
$$T(f)_{i, a} := \begin{cases} c_{r - 1 - i - a} & \text{if } i + a \le r - 1, \\ 0 & \text{if } i + a > r - 1. \end{cases}$$
Then as polynomial matrix identities over $\mathbb{Z}[c_1, \ldots, c_r]$:
1. $B(f) = T(f)\, H(f)\, T(f)^{\mathsf T}$,
2. $\det T(f) = (-1)^{\lfloor r/2 \rfloor} = (-1)^{\binom{r}{2}} = \pm 1$, and $T(f)^{-1} \in \mathbb{Z}[c_1, \ldots, c_{r - 1}]^{r \times r}$,
3. $H(f) = T(f)^{-1}\, B(f)\, \bigl(T(f)^{-1}\bigr)^{\mathsf T}$ and $\det H(f) = \mathrm{disc}(f)$.

*Proof.* Let $\theta_1, \ldots, \theta_r$ be independent indeterminates and consider the universal monic polynomial $f(t) = \prod_{\ell = 1}^r (t - \theta_\ell) = \sum_{d = 0}^r c_d t^{r - d}$, where $c_d = (-1)^d e_d(\theta_1, \ldots, \theta_r)$ are algebraically independent over $\mathbb{Z}$. For each $\ell \in \{1, \ldots, r\}$, the quotient $\frac{f(s)}{s - \theta_\ell} = \prod_{m \ne \ell} (s - \theta_m)$ is a polynomial in $\mathbb{Z}[s, \theta_1, \ldots, \theta_r]$, and $f'(s) = \sum_{\ell = 1}^r \frac{f(s)}{s - \theta_\ell}$. Multiplying the rational identity
$$\frac{1}{(s - \theta_\ell)(t - \theta_\ell)} = \frac{1}{s - t}\left(\frac{1}{t - \theta_\ell} - \frac{1}{s - \theta_\ell}\right)$$
by $f(s) f(t)$ and summing over $\ell = 1, \ldots, r$ gives
$$\sum_{\ell = 1}^r \frac{f(s)}{s - \theta_\ell}\, \frac{f(t)}{t - \theta_\ell} = \frac{f(s) f'(t) - f'(s) f(t)}{s - t} = \sum_{i, j = 0}^{r - 1} b_{i, j}\, s^i t^j.$$
On the other hand, since $f(\theta_\ell) = 0$, we have
$$\frac{f(s)}{s - \theta_\ell} = \frac{f(s) - f(\theta_\ell)}{s - \theta_\ell} = \sum_{d = 0}^{r - 1} c_d \frac{s^{r - d} - \theta_\ell^{r - d}}{s - \theta_\ell} = \sum_{d = 0}^{r - 1} c_d \sum_{\substack{i, a \ge 0 \\ i + a = r - 1 - d}} s^i \theta_\ell^a = \sum_{i = 0}^{r - 1} s^i \sum_{a = 0}^{r - 1 - i} c_{r - 1 - i - a}\, \theta_\ell^a.$$
Substituting this expansion (in $s$ and in $t$) into $\sum_{\ell = 1}^r \frac{f(s)}{s - \theta_\ell} \frac{f(t)}{t - \theta_\ell}$ yields
$$\sum_{i, j = 0}^{r - 1} b_{i, j}\, s^i t^j = \sum_{i, j = 0}^{r - 1} s^i t^j \sum_{a = 0}^{r - 1 - i} \sum_{b = 0}^{r - 1 - j} c_{r - 1 - i - a} \Biggl(\sum_{\ell = 1}^r \theta_\ell^{a + b}\Biggr) c_{r - 1 - j - b} = \sum_{i, j = 0}^{r - 1} \bigl(T(f)\, H(f)\, T(f)^{\mathsf T}\bigr)_{i, j}\, s^i t^j.$$
Equating coefficients of $s^i t^j$ proves $B(f) = T(f) H(f) T(f)^{\mathsf T}$. Because all entries of $B(f)$, $T(f)$, and $H(f)$ lie in $\mathbb{Z}[c_1, \ldots, c_r]$ (by Newton's identities for $s_m(f)$) and $c_1, \ldots, c_r$ are algebraically independent over $\mathbb{Z}$, identity (1) holds in $\mathbb{Z}[c_1, \ldots, c_r]^{r \times r}$.

For (2), let $J$ be the $r \times r$ order-reversal permutation matrix ($J_{i, j} = \delta_{i + j,\, r - 1}$), which satisfies $J^2 = I_r$ and is the product of $\lfloor r/2 \rfloor$ disjoint transpositions, so $\det J = (-1)^{\lfloor r/2 \rfloor} = (-1)^{\binom{r}{2}}$. Then $L(f) := J\, T(f)$ has entries
$$L(f)_{i, a} = T(f)_{r - 1 - i,\, a} = \begin{cases} c_{i - a} & \text{if } a \le i, \\ 0 & \text{if } a > i. \end{cases}$$
Since $c_0 = 1$, $L(f) = I_r + N(f)$ is unit lower triangular, where $N(f) \in \mathbb{Z}[c_1, \ldots, c_{r - 1}]^{r \times r}$ is strictly lower triangular and hence satisfies $N(f)^r = 0$. Therefore $\det L(f) = 1$, $\det T(f) = (\det J)(\det L(f)) = (-1)^{\lfloor r/2 \rfloor}$, and
$$L(f)^{-1} = \sum_{m = 0}^{r - 1} (-1)^m N(f)^m \in \mathbb{Z}[c_1, \ldots, c_{r - 1}]^{r \times r},$$
so $T(f)^{-1} = L(f)^{-1} J \in \mathbb{Z}[c_1, \ldots, c_{r - 1}]^{r \times r}$.

For (3), multiplying (1) on the left by $T(f)^{-1}$ and on the right by $\bigl(T(f)^{-1}\bigr)^{\mathsf T}$ gives $H(f) = T(f)^{-1} B(f) \bigl(T(f)^{-1}\bigr)^{\mathsf T}$. Finally, letting $V(\theta) = (\theta_\ell^a)_{1 \le \ell \le r,\, 0 \le a \le r - 1}$ be the Vandermonde matrix, we have $H(f) = V(\theta)^{\mathsf T} V(\theta)$ and hence $\det H(f) = (\det V(\theta))^2 = \prod_{1 \le a < b \le r} (\theta_b - \theta_a)^2 = \mathrm{disc}(f)$. $\square$

---

### Lemma 3 (Constant-matrix Bezoutian factorization in the subset basis)

Set $N := \binom{n}{r - 1}$, and define the symmetric rational constant matrix $\mathbf{W}_{n, r} \in \mathbb{Q}^{N \times N}$ indexed by $U, V \in \binom{[n]}{r - 1}$ by
$$(\mathbf{W}_{n, r})_{U, V} := \frac{r}{\binom{n}{r} \binom{n}{r - 1}} \cdot \frac{n - |U \cup V|}{|U \setminus V| + 1}.$$
Let $C(x) \in \mathbb{Z}[x_1, \ldots, x_n]^{N \times r}$ be the coefficient matrix of the polynomials $P_U$ ($U \in \binom{[n]}{r - 1}$), defined by
$$P_U(s) = \sum_{i = 0}^{r - 1} C_{U, i}(x)\, s^i \qquad \Bigl(\text{explicitly, } C_{U, i}(x) = (-1)^{r - 1 - i} e_{r - 1 - i}(x_U)\Bigr).$$
Then
$$\frac{J_{n, r}(s)\, J'_{n, r}(t) - J'_{n, r}(s)\, J_{n, r}(t)}{s - t} = \sum_{U, V \in \binom{[n]}{r - 1}} (\mathbf{W}_{n, r})_{U, V}\, P_U(s)\, P_V(t),$$
and equivalently
$$B(J_{n, r}) = C(x)^{\mathsf T}\, \mathbf{W}_{n, r}\, C(x) \qquad \text{in } \mathbb{Q}[x_1, \ldots, x_n]^{r \times r}.$$

*Proof.* First observe that $\mathbf{W}_{n, r}$ is symmetric: for any $U, V \in \binom{[n]}{r - 1}$, we have $|U \cup V| = |V \cup U|$ and $|U \setminus V| = |U| - |U \cap V| = (r - 1) - |U \cap V| = |V| - |U \cap V| = |V \setminus U|$.

By Lemma 1,
$$J_{n, r}(s)\, J'_{n, r}(t) - J'_{n, r}(s)\, J_{n, r}(t) = \frac{r}{\binom{n}{r} \binom{n}{r - 1}} \sum_{\substack{S \in \binom{[n]}{r} \\ T \in \binom{[n]}{r - 1}}} \bigl(P_S(s)\, P_T(t) - P_T(s)\, P_S(t)\bigr).$$
For every pair $(S, T) \in \binom{[n]}{r} \times \binom{[n]}{r - 1}$, we have $|S| = r > r - 1 = |T|$, so $S \setminus T$ is nonempty ($|S \setminus T| \ge 1$). Averaging $P_S(s) = (s - x_z) P_{S \setminus \{z\}}(s)$ over all $z \in S \setminus T$ gives
$$\sum_{\substack{S \in \binom{[n]}{r} \\ T \in \binom{[n]}{r - 1}}} P_S(s)\, P_T(t) = \sum_{\substack{S \in \binom{[n]}{r} \\ T \in \binom{[n]}{r - 1}}} \frac{1}{|S \setminus T|} \sum_{z \in S \setminus T} (s - x_z)\, P_{S \setminus \{z\}}(s)\, P_T(t).$$
Consider the map $(S, T, z) \mapsto (U, V, z) := (S \setminus \{z\}, T, z)$ from
$$\mathcal{X} := \left\{(S, T, z) : S \in \binom{[n]}{r},\; T \in \binom{[n]}{r - 1},\; z \in S \setminus T\right\}$$
to
$$\mathcal{Y} := \left\{(U, V, z) : U, V \in \binom{[n]}{r - 1},\; z \in [n] \setminus (U \cup V)\right\}.$$
If $(S, T, z) \in \mathcal{X}$, then $z \in S$ implies $|S \setminus \{z\}| = r - 1$ and $z \notin U$, while $z \notin T = V$ gives $z \in [n] \setminus (U \cup V)$; hence $(U, V, z) \in \mathcal{Y}$. Conversely, if $(U, V, z) \in \mathcal{Y}$, then $z \notin U \cup V$ implies $|U \cup \{z\}| = r$ and $z \in (U \cup \{z\}) \setminus V$, so $(U, V, z) \mapsto (U \cup \{z\}, V, z)$ is a two-sided inverse to the map above. Moreover, under this bijection $U \setminus V = (S \setminus T) \setminus \{z\}$, whence $|S \setminus T| = |U \setminus V| + 1$. Reindexing by this bijection yields
$$\sum_{\substack{S \in \binom{[n]}{r} \\ T \in \binom{[n]}{r - 1}}} P_S(s)\, P_T(t) = \sum_{U, V \in \binom{[n]}{r - 1}} \frac{1}{|U \setminus V| + 1} \sum_{z \in [n] \setminus (U \cup V)} (s - x_z)\, P_U(s)\, P_V(t).$$
Interchanging $s$ and $t$, and then relabeling $(U, V) \mapsto (V, U)$ (using $|V \setminus U| = |U \setminus V|$ and $V \cup U = U \cup V$), gives
$$\sum_{\substack{S \in \binom{[n]}{r} \\ T \in \binom{[n]}{r - 1}}} P_T(s)\, P_S(t) = \sum_{U, V \in \binom{[n]}{r - 1}} \frac{1}{|U \setminus V| + 1} \sum_{z \in [n] \setminus (U \cup V)} (t - x_z)\, P_U(s)\, P_V(t).$$
Subtracting the second sum from the first, the variable $x_z$ cancels pointwise in $(s - x_z) - (t - x_z) = s - t$, and the inner sum over $z \in [n] \setminus (U \cup V)$ consists of exactly $|[n] \setminus (U \cup V)| = n - |U \cup V|$ identical terms:
$$\sum_{\substack{S \in \binom{[n]}{r} \\ T \in \binom{[n]}{r - 1}}} \bigl(P_S(s)\, P_T(t) - P_T(s)\, P_S(t)\bigr) = (s - t) \sum_{U, V \in \binom{[n]}{r - 1}} \frac{n - |U \cup V|}{|U \setminus V| + 1}\, P_U(s)\, P_V(t).$$
Multiplying by $\frac{r}{\binom{n}{r} \binom{n}{r - 1}}$ and dividing by $s - t$ gives the bivariate identity. Comparing the coefficients of $s^i t^j$ ($0 \le i, j \le r - 1$) yields $B(J_{n, r}) = C(x)^{\mathsf T} \mathbf{W}_{n, r} C(x)$. $\square$

---

### Lemma 4 (Explicit positive-rational Gram decomposition and strict positive definiteness of $\mathbf{W}_{n, r}$)

For every $n \ge r \ge 2$, the matrix $\mathbf{W}_{n, r}$ satisfies the exact rank-1 decomposition
$$\mathbf{W}_{n, r} = \frac{r}{\binom{n}{r} \binom{n}{r - 1}} \sum_{z = 1}^n \sum_{S \subseteq [n] \setminus \{z\}} \gamma_{n, |S|}\, \chi_{z, S}\, \chi_{z, S}^{\mathsf T},$$
where $\chi_{z, S} \in \{-1, 0, 1\}^{\binom{[n]}{r - 1}}$ is the vector with entries
$$\chi_{z, S}(U) := \begin{cases} (-1)^{|S \cap U|} & \text{if } z \notin U, \\ 0 & \text{if } z \in U, \end{cases}$$
and for each $0 \le s \le n - 1$,
$$\gamma_{n, s} := \frac{1}{2^{n - 1}} \int_0^1 (1 + \sqrt{x})^{n - 1 - s} (1 - \sqrt{x})^s\, dx = \frac{1}{2^{n - 2}} \int_0^1 u\, (1 + u)^{n - 1 - s} (1 - u)^s\, du \in \mathbb{Q}_{> 0}.$$
Moreover, $\mathbf{W}_{n, r}$ is strictly positive definite ($\mathbf{W}_{n, r} \succ 0$). In particular, $\mathbf{W}_{n, r} = L^{\mathsf T} L$ for an invertible real matrix $L \in \mathbb{R}^{N \times N}$, and $\mathbf{W}_{n, r} = L_0 D L_0^{\mathsf T}$ for a unit lower-triangular rational matrix $L_0 \in \mathbb{Q}^{N \times N}$ and diagonal matrix $D = \mathrm{diag}(d_1, \ldots, d_N)$ with $d_1, \ldots, d_N \in \mathbb{Q}_{> 0}$.

*Proof.* Substituting $x = u^2$ ($dx = 2u\, du$) gives the second expression for $\gamma_{n, s}$. The integrand $u(1 + u)^{n - 1 - s}(1 - u)^s$ is a polynomial in $\mathbb{Z}[u]$ that is strictly positive on $(0, 1)$, so $\gamma_{n, s} \in \mathbb{Q}_{> 0}$ for all $0 \le s \le n - 1$.

Fix $z \in [n]$, subsets $U, V \in \binom{[n] \setminus \{z\}}{r - 1}$, and $x \in [0, 1]$. For every $i \in [n] \setminus \{z\}$, the exponent $\mathbf{1}_{i \in U} + \mathbf{1}_{i \in V}$ is even if $i \notin U \triangle V$ and equals $1$ if $i \in U \triangle V$, so
$$\frac{(1 + \sqrt{x}) + (1 - \sqrt{x})\, (-1)^{\mathbf{1}_{i \in U} + \mathbf{1}_{i \in V}}}{2} = \begin{cases} 1 & \text{if } i \notin U \triangle V, \\ \sqrt{x} & \text{if } i \in U \triangle V. \end{cases}$$
Because $|U| = |V| = r - 1$, the symmetric difference satisfies $|U \triangle V| = |U \setminus V| + |V \setminus U| = 2 |U \setminus V|$. Taking the product over all $i \in [n] \setminus \{z\}$ and expanding the product of $n - 1$ binomials gives
$$\begin{aligned}
x^{|U \setminus V|} &= (\sqrt{x})^{|U \triangle V|} = \frac{1}{2^{n - 1}} \prod_{i \in [n] \setminus \{z\}} \Bigl((1 + \sqrt{x}) + (1 - \sqrt{x})\, (-1)^{\mathbf{1}_{i \in U} + \mathbf{1}_{i \in V}}\Bigr) \\
&= \frac{1}{2^{n - 1}} \sum_{S \subseteq [n] \setminus \{z\}} (1 + \sqrt{x})^{n - 1 - |S|} (1 - \sqrt{x})^{|S|}\, (-1)^{|S \cap U| + |S \cap V|}.
\end{aligned}$$
Integrating both sides over $x \in [0, 1]$ yields
$$\frac{1}{|U \setminus V| + 1} = \sum_{S \subseteq [n] \setminus \{z\}} \gamma_{n, |S|}\, (-1)^{|S \cap U|}\, (-1)^{|S \cap V|} \qquad \left(U, V \in \binom{[n] \setminus \{z\}}{r - 1}\right).$$
Now let $U, V \in \binom{[n]}{r - 1}$ be arbitrary. By definition, $\chi_{z, S}(U)\, \chi_{z, S}(V) = (-1)^{|S \cap U| + |S \cap V|}$ if $z \notin U \cup V$ and $0$ if $z \in U \cup V$. Summing over $z \in [n]$ therefore yields
$$\sum_{z = 1}^n \sum_{S \subseteq [n] \setminus \{z\}} \gamma_{n, |S|}\, \chi_{z, S}(U)\, \chi_{z, S}(V) = \sum_{z \in [n] \setminus (U \cup V)} \frac{1}{|U \setminus V| + 1} = \frac{n - |U \cup V|}{|U \setminus V| + 1}.$$
Multiplying both sides by $\frac{r}{\binom{n}{r} \binom{n}{r - 1}}$ proves the stated rank-1 decomposition of $\mathbf{W}_{n, r}$.

To establish strict positive definiteness, let $v \in \mathbb{R}^{\binom{[n]}{r - 1}}$ be any vector. Then
$$v^{\mathsf T} \mathbf{W}_{n, r} v = \frac{r}{\binom{n}{r} \binom{n}{r - 1}} \sum_{z = 1}^n \sum_{S \subseteq [n] \setminus \{z\}} \gamma_{n, |S|} \bigl(\chi_{z, S}^{\mathsf T} v\bigr)^2 \ge 0.$$
Suppose $v^{\mathsf T} \mathbf{W}_{n, r} v = 0$. Since every $\gamma_{n, |S|} > 0$, we must have $\chi_{z, S}^{\mathsf T} v = 0$ for every $z \in [n]$ and every $S \subseteq [n] \setminus \{z\}$. Fix any $U_0 \in \binom{[n]}{r - 1}$. Since $|U_0| = r - 1 < n$, there exists an element $z \in [n] \setminus U_0$. Multiplying $\chi_{z, S}^{\mathsf T} v = 0$ by $(-1)^{|S \cap U_0|}$ and summing over all $S \subseteq [n] \setminus \{z\}$ gives
$$0 = \sum_{S \subseteq [n] \setminus \{z\}} (-1)^{|S \cap U_0|} \sum_{\substack{U \in \binom{[n]}{r - 1} \\ z \notin U}} (-1)^{|S \cap U|} v_U = \sum_{\substack{U \in \binom{[n]}{r - 1} \\ z \notin U}} v_U \sum_{S \subseteq [n] \setminus \{z\}} (-1)^{|S \cap (U \triangle U_0)|} = 2^{n - 1} v_{U_0},$$
since for any subset $D \subseteq [n] \setminus \{z\}$, $\sum_{S \subseteq [n] \setminus \{z\}} (-1)^{|S \cap D|} = \prod_{i \in D}(1 - 1) \cdot \prod_{i \in ([n] \setminus \{z\}) \setminus D} (1 + 1)$ equals $2^{n - 1}$ if $D = \emptyset$ (i.e., $U = U_0$) and $0$ otherwise. Thus $v_{U_0} = 0$ for every $U_0 \in \binom{[n]}{r - 1}$, so $v = 0$. Hence $\mathbf{W}_{n, r} \succ 0$.

Since $\mathbf{W}_{n, r} \in \mathbb{Q}^{N \times N}$ is symmetric and strictly positive definite, it admits both a real Cholesky factorization $\mathbf{W}_{n, r} = L^{\mathsf T} L$ ($L \in \mathbb{R}^{N \times N}$ invertible) and an exact rational $L_0 D L_0^{\mathsf T}$ factorization with $L_0 \in \mathbb{Q}^{N \times N}$ unit lower triangular and $D = \mathrm{diag}(d_1, \ldots, d_N)$, $d_j \in \mathbb{Q}_{> 0}$. $\square$

---

### Theorem 1 (Proof of Conjecture 6.5 / `conj:hermite`)

For every $n \ge 2$ and every $0 \le k \le n - 2$, setting $r = n - k$ and $N = \binom{n}{r - 1}$, the ordinary Hermite matrix $H\bigl(P^{(k)} / \mathrm{lc}(P^{(k)})\bigr) = H(J_{n, r})$ admits an SOS-matrix factorization
$$H(J_{n, r}) = A(x)^{\mathsf T} A(x), \qquad A(x) \in \mathbb{R}[x_1, \ldots, x_n]^{N \times r}.$$
Moreover, $H(J_{n, r})$ admits the completely explicit positive-rational-weighted factorization
$$H(J_{n, r}) = \frac{r}{\binom{n}{r} \binom{n}{r - 1}} \sum_{z = 1}^n \sum_{S \subseteq [n] \setminus \{z\}} \gamma_{n, |S|}\, w_{z, S}(x)\, w_{z, S}(x)^{\mathsf T},$$
where $w_{z, S}(x) := T(J_{n, r})^{-1} C(x)^{\mathsf T} \chi_{z, S} \in \mathbb{Q}[x_1, \ldots, x_n]^r$ and $\gamma_{n, |S|} \in \mathbb{Q}_{> 0}$.

*Proof.* By Lemma 1, $P^{(k)} / \mathrm{lc}(P^{(k)}) = J_{n, r}$ is a monic polynomial of degree $r \ge 2$ whose coefficients $c_1, \ldots, c_r$ belong to $\mathbb{Q}[x_1, \ldots, x_n]$. Specializing Lemma 2 to $f = J_{n, r}$ shows that $T(J_{n, r})^{-1} \in \mathbb{Q}[x_1, \ldots, x_n]^{r \times r}$ and
$$H(J_{n, r}) = T(J_{n, r})^{-1}\, B(J_{n, r})\, \bigl(T(J_{n, r})^{-1}\bigr)^{\mathsf T}.$$
Substituting Lemma 3 ($B(J_{n, r}) = C(x)^{\mathsf T} \mathbf{W}_{n, r} C(x)$) gives
$$H(J_{n, r}) = \Bigl(C(x)\, \bigl(T(J_{n, r})^{-1}\bigr)^{\mathsf T}\Bigr)^{\mathsf T} \mathbf{W}_{n, r} \Bigl(C(x)\, \bigl(T(J_{n, r})^{-1}\bigr)^{\mathsf T}\Bigr).$$
Writing $\mathbf{W}_{n, r} = L^{\mathsf T} L$ ($L \in \mathbb{R}^{N \times N}$) by Lemma 4 and setting
$$A(x) := L\, C(x)\, \bigl(T(J_{n, r})^{-1}\bigr)^{\mathsf T} \in \mathbb{R}[x_1, \ldots, x_n]^{N \times r},$$
we obtain $H(J_{n, r}) = A(x)^{\mathsf T} A(x)$. Substituting instead the explicit rank-1 decomposition of $\mathbf{W}_{n, r}$ from Lemma 4 immediately yields the stated positive-rational-weighted factorization over $\mathbb{Q}[x_1, \ldots, x_n]$. This proves Conjecture 6.5 (`conj:hermite`). $\square$

---

### Corollary 2 (Proof of Conjecture 1.1 / `conj:sos`)

For every $n \ge 2$ and every $0 \le k \le n - 2$, the polynomial $\mathcal{D}_k^{(n)} = \mathrm{disc}\bigl(P^{(k)}\bigr)$ is a sum of squares of polynomials in the differences $x_i - x_j$ (and in fact a positive-rational-weighted sum of squares of polynomials in $\mathbb{Q}[\{x_i - x_j\}]$).

*Proof.* Set $r := n - k \ge 2$ and $N := \binom{n}{r - 1}$. Introduce the centered variables
$$\overline{x} := \frac{1}{n} \sum_{j = 1}^n x_j, \qquad z_i := x_i - \overline{x} = \frac{1}{n} \sum_{j = 1}^n (x_i - x_j) \qquad (1 \le i \le n).$$
By Lemma 1, $\mathrm{lc}(P^{(k)}) = \frac{n!}{r!}$ and $P^{(k)} = \frac{n!}{r!} J_{n, r}$, so the leading-coefficient scaling of the discriminant gives
$$\mathcal{D}_k^{(n)} = \mathrm{disc}\bigl(P^{(k)}\bigr) = \left(\frac{n!}{r!}\right)^{2r - 2} \mathrm{disc}\bigl(J_{n, r}(\,\cdot\,; x)\bigr).$$
Using Lemma 1,
$$J_{n, r}(t; z) = \binom{n}{r}^{-1} \sum_{S \in \binom{[n]}{r}} \prod_{i \in S} (t - x_i + \overline{x}) = J_{n, r}(t + \overline{x}; x).$$
Thus the roots of $J_{n, r}(\,\cdot\,; z)$ are obtained from those of $J_{n, r}(\,\cdot\,; x)$ by shifting every root by $-\overline{x}$, which leaves all pairwise differences of roots unchanged. By Lemma 2(3),
$$\mathrm{disc}\bigl(J_{n, r}(\,\cdot\,; x)\bigr) = \mathrm{disc}\bigl(J_{n, r}(\,\cdot\,; z)\bigr) = \det H\bigl(J_{n, r}(\,\cdot\,; z)\bigr).$$
Evaluating the polynomial matrix identity of Theorem 1 at $x_i \mapsto z_i$ gives
$$H\bigl(J_{n, r}(\,\cdot\,; z)\bigr) = A(z)^{\mathsf T} A(z),$$
where $A(z) \in \mathbb{R}[z_1, \ldots, z_n]^{N \times r}$. Because $2 \le r \le n$, we always have $N = \binom{n}{r - 1} \ge \binom{r}{r - 1} = r$. Applying the Cauchy–Binet formula yields
$$\mathcal{D}_k^{(n)} = \left(\frac{n!}{r!}\right)^{2r - 2} \det\bigl(A(z)^{\mathsf T} A(z)\bigr) = \sum_{I \in \binom{[N]}{r}} \left(\left(\frac{n!}{r!}\right)^{r - 1} \det A_I(z)\right)^2,$$
where $A_I(z)$ is the $r \times r$ submatrix of $A(z)$ formed by the rows indexed by $I$. Since every $z_i = \frac{1}{n} \sum_{j = 1}^n (x_i - x_j)$ is a rational linear combination of the differences $x_i - x_j$, every polynomial $\left(\frac{n!}{r!}\right)^{r - 1} \det A_I(z)$ is a real polynomial in the differences $x_i - x_j$.

Finally, taking $\mathbf{W}_{n, r} = L_0 D L_0^{\mathsf T}$ from Lemma 4 with $D = \mathrm{diag}(d_1, \ldots, d_N)$ ($d_j \in \mathbb{Q}_{> 0}$) and setting $M(z) := L_0^{\mathsf T} C(z) \bigl(T(J_{n, r}(\,\cdot\,; z))^{-1}\bigr)^{\mathsf T} \in \mathbb{Q}[z_1, \ldots, z_n]^{N \times r}$, Cauchy–Binet gives the rational-weighted identity
$$\mathcal{D}_k^{(n)} = \sum_{I \in \binom{[N]}{r}} \Biggl(\prod_{a \in I} d_a\Biggr) \left(\left(\frac{n!}{r!}\right)^{r - 1} \det M_I(z)\right)^2$$
with $\prod_{a \in I} d_a \in \mathbb{Q}_{> 0}$ and $\left(\frac{n!}{r!}\right)^{r - 1} \det M_I(z) \in \mathbb{Q}[\{x_i - x_j\}]$. This proves Conjecture 1.1 (`conj:sos`). $\square$

---

## Independent Exact-Arithmetic Verification

The companion script [`verify.py`](./verify.py) independently checks every algebraic component of the proof in exact rational and polynomial-ring arithmetic (zero floating-point operations), including:
1. Symbolic verification over $\mathbb{Z}[\theta_1, \ldots, \theta_r]$ and $\mathbb{Z}[c_1, \ldots, c_r]$ of Lemma 2 ($B(f) = T(f) H(f) T(f)^{\mathsf T}$, $T(f)^{-1} \in \mathbb{Z}[c_1, \ldots, c_{r - 1}]^{r \times r}$, and $H(f) = V(\theta)^{\mathsf T} V(\theta)$) for $r = 2, \ldots, 6$.
2. Complete symbolic verification over $\mathbb{Q}[x_1, \ldots, x_n]$ of Lemmas 1, 3, 4 and Theorem 1 directly from $P^{(k)}$ for all $15$ pairs $2 \le r \le n \le 6$.
3. Exact verification of the Walsh–Hadamard decomposition of $\mathbf{W}_{n, r}$ for all $36$ pairs $2 \le r \le n \le 9$ and exact rational $L_0 D L_0^{\mathsf T}$ factorization ($d_j > 0$) across $29$ pairs including the first open case $(n, k) = (7, 2)$ ($r = 5$).
4. Exact rational evaluations directly from $P^{(k)}$ (in both original coordinates $x$ and centered coordinates $z$), Sylvester-resultant discriminant checks, and explicit Cauchy–Binet minor sums across $16$ full Cauchy–Binet cases plus $9$ open/higher cases including $(n, k) = (7, 2), (8, 2), (8, 3), (9, 2), (9, 3), (9, 4), (10, 4)$.

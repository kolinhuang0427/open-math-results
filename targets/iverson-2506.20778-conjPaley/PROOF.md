# Proof of Conjecture (`conj:Paley`) of Iverson and Mixon (arXiv:2506.20778v1)

## Primary Source and Exact Statement

**Source:** Joseph W. Iverson and Dustin G. Mixon, *"Asymmetric SICs over finite fields"*, `arXiv:2506.20778v1` (25 June 2025), Section 4, Conjecture 22 (`\label{conj:Paley}`, `2025.06.25.tex`, lines 829–840):

> **Conjecture (`conj:Paley`).** Given a prime power $q > 11$ with $q \equiv 3 \bmod 4$, consider the "Paley I" Hadamard matrix $H$ of order $d := q + 1$. Then the following hold:
> - **(a)** $\mathrm{Aut}_s(\tilde{H}) \cong P\Gamma L(2, q)$ has exactly two orbits on $[d] \times [d]$, namely, $\{(i, i) : i \in [d]\}$ and its complement, and
> - **(b)** for any prime $p \equiv 3 \bmod 4$ that divides $d - 8$, the SIC $\{x_{ij}\}$ in $\mathbb{F}_{p^2}^d$ constructed by Theorem 2 (`thm.main`) has $\mathrm{Aut}_s(\{x_{ij}\}) = \iota(\mathrm{Aut}_w(H))$ and $\mathrm{Aut}_w(\{x_{ij}\}) = \mathrm{Aut}_s(\tilde{H})$.
>
> In particular, there exist non-transitive SICs in infinitely many dimensions over various finite fields.

Throughout, we adopt the exact notation and definitions of `arXiv:2506.20778v1` (Sections 1–3):
- For a Hadamard matrix $H \in \{\pm 1\}^{X \times X}$ with $|X| = d$ and $i$th row $r_i^\top$, the symmetric graphical Hadamard matrix $\tilde{H} \in \{\pm 1\}^{X^2 \times X^2}$ is defined entrywise by $\tilde{H}_{(i, j), (k, l)} = [r_k r_i^\top]_{j, l} = H_{k, j} H_{i, l}$ (line 452).
- $\mathrm{Aut}_w(H) \le S_X \times S_X$ consists of pairs $(\pi, \sigma)$ for which there exist $\varepsilon_i, \varepsilon'_j \in \{\pm 1\}$ with $H_{\pi(i), \sigma(j)} = \varepsilon_i \varepsilon'_j H_{i, j}$ for all $i, j \in X$; $\mathrm{Aut}_s(\tilde{H}) \le S_{X^2}$ consists of permutations $\Phi$ for which there exist $\eta_x \in \{\pm 1\}$ with $\tilde{H}_{\Phi(x), \Phi(y)} = \eta_x \eta_y \tilde{H}_{x, y}$ for all $x, y \in X^2$ (Definition 11, lines 334–350).
- $\iota : S_X \times S_X \to S_{X^2}$ is $\iota(\pi, \sigma)(i, j) = (\pi(i), \sigma(j))$ (Theorem 15 / `thm:sandwich`, line 471).
- For a prime $p \equiv 3 \bmod 4$ dividing $d - 8$, $K = \mathbb{F}_p$, $L = \mathbb{F}_p[\mathrm{i}] \cong \mathbb{F}_{p^2}$ ($\mathrm{i}^2 = -1$), the sesquilinear form on $L^d$ is $(u, v) = u^* v$ (conjugate-linear in the first argument, linear in the second; line 50), and the SIC vectors of Theorem 2 (`thm.main`) are $x_{ij} = h_j \circ (\mathbf{1} + z e_i)$ with $z = -2(1 + \mathrm{i})$.

---

## 1. Paley I Matrix, Convention Invariance, and the $P\Gamma L(2, q)$ Subgroup

Let $q = p_0^r > 11$ be a prime power with $q \equiv 3 \pmod 4$, so $p_0 \equiv 3 \pmod 4$ is an odd prime and $r$ is odd. Set $d := q + 1$, let $X := PG(1, q) = \mathbb{F}_q \cup \{\infty\}$, and let $\chi : \mathbb{F}_q \to \{0, \pm 1\}$ be the quadratic character ($\chi(0) = 0$, $\chi(-1) = -1$). Because $p_0$ and $r$ are odd, every field automorphism $\gamma \in \mathrm{Gal}(\mathbb{F}_q / \mathbb{F}_{p_0})$ satisfies $\chi(a^\gamma) = \chi(a)$ for all $a \in \mathbb{F}_q$.

Let $H = I + S \in \{\pm 1\}^{X \times X}$ be the Paley type I skew-Hadamard matrix defined by
$$H_{a, a} = 1 \quad (a \in X), \qquad H_{\infty, a} = 1, \quad H_{a, \infty} = -1 \quad (a \in \mathbb{F}_q), \qquad H_{a, b} = \chi(a - b) \quad (a \neq b \in \mathbb{F}_q).$$
Then $S^\top = -S$, $H^\top = 2I - H$, $H H^\top = d I$, $S^2 = -q I$, $H^2 = 2S - (q - 1)I$, and $\sum_{m \in X} H_{a, m} = 0$ for every $a \in \mathbb{F}_q$. Representing each $a \in X$ by the column vector $v_\infty := (1, 0)^\top$ and $v_a := (a, 1)^\top$ ($a \in \mathbb{F}_q$) in $\mathbb{F}_q^2$, we have
$$S_{a, b} = \chi\bigl(\det(v_a, v_b)\bigr) \qquad \text{for all } a, b \in X.$$

**Remark (Invariance under standard Paley I conventions).** Suppose $H^{\mathrm{alt}}_{i, j} = \alpha_i \beta_j H_{i, j}$ is obtained from $H$ by arbitrary row and column sign switches $\alpha_i, \beta_j \in \{\pm 1\}$ (for instance, the normalized form with all-$+1$ first row and first column, obtained via $\alpha_\infty = 1$, $\alpha_a = -1$ for $a \in \mathbb{F}_q$, and $\beta_j \equiv 1$). Then:
1. $\mathrm{Aut}_w(H^{\mathrm{alt}}) = \mathrm{Aut}_w(H)$ identically as subgroups of $S_X \times S_X$;
2. $\tilde{H}^{\mathrm{alt}}_{(i, j), (k, l)} = (\alpha_i \beta_j)(\alpha_k \beta_l)\tilde{H}_{(i, j), (k, l)}$, so $\mathrm{Aut}_s(\tilde{H}^{\mathrm{alt}}) = \mathrm{Aut}_s(\tilde{H})$ identically as subgroups of $S_{X^2}$ (preserving $\Delta := \{(i, i) : i \in X\}$ and all orbits verbatim);
3. by Theorem 15(a) (`thm:sandwich`(a)) applied to $(\mathrm{id}, \mathrm{id})$, the corresponding SICs are strongly equivalent via the identity permutation, so their strong and weak automorphism groups coincide identically.

Similarly, replacing $H$ by $H^\top = I - S$ replaces $\tilde{H}$ by its conjugate under the coordinate swap $(i, j) \mapsto (j, i)$, which preserves $\Delta$ and all conclusions below. Thus we work without loss of generality with $H = I + S$.

### Lemma 1 ($P\Gamma L(2, q)$ embedding and Kantor's theorem)
For every $g = (M, \gamma) \in P\Gamma L(2, q)$ acting on $X = PG(1, q)$ by $M v_a^\gamma = \lambda_a v_{g(a)}$ ($\lambda_a \in \mathbb{F}_q^\times$), set $\varepsilon_a := \chi(\lambda_a) \in \{\pm 1\}$ and $\eta(g) := \chi(\det M) \in \{\pm 1\}$. Then:
1. For all $a, b \in X$,
   $$H_{g(a), g(b)} = \begin{cases} \varepsilon_a \varepsilon_b H_{a, b} & \text{if } g \in P\Sigma L(2, q) \text{ (i.e., } \eta(g) = +1\text{)}, \\ \varepsilon_a \varepsilon_b H_{b, a} & \text{if } g \in P\Gamma L(2, q) \setminus P\Sigma L(2, q) \text{ (i.e., } \eta(g) = -1\text{)}. \end{cases}$$
2. Since $q > 11$, $\mathrm{Aut}_w(H) = \{(g, g) : g \in P\Sigma L(2, q)\}$.
3. The map $\psi : P\Gamma L(2, q) \to S_{X^2}$ defined by
   $$\psi(g)(i, j) := \begin{cases} (g(i), g(j)) & \text{if } g \in P\Sigma L(2, q), \\ (g(j), g(i)) & \text{if } g \in P\Gamma L(2, q) \setminus P\Sigma L(2, q) \end{cases}$$
   is an injective group homomorphism into $\mathrm{Aut}_s(\tilde{H})$ whose image has exactly two orbits on $X^2$: the diagonal $\Delta = \{(i, i) : i \in X\}$ (size $d$) and its complement $X^2 \setminus \Delta$ (size $d(d - 1)$).

*Proof.*
(1) Taking determinants in $M v_a^\gamma = \lambda_a v_{g(a)}$ gives $\lambda_a \lambda_b \det(v_{g(a)}, v_{g(b)}) = (\det M)\det(v_a, v_b)^\gamma$. Applying $\chi$ (which is $\gamma$-invariant since $r$ is odd) yields $S_{g(a), g(b)} = \eta(g) \varepsilon_a \varepsilon_b S_{a, b}$. Since $S_{b, a} = -S_{a, b}$ and $H_{g(a), g(a)} = 1 = \varepsilon_a^2 H_{a, a}$, adding $I$ gives (1).

(2) By (1), the diagonal subgroup $G_{\mathrm{diag}} := \{(g, g) : g \in P\Sigma L(2, q)\}$ is contained in $\mathrm{Aut}_w(H)$ and has order $|P\Sigma L(2, q)|$. By Kantor (1969; cited in `2025.06.25.tex`, line 820), for every prime power $q > 11$ with $q \equiv 3 \pmod 4$, $\mathrm{Aut}_w(H) \cong P\Sigma L(2, q)$. Comparing finite orders forces $\mathrm{Aut}_w(H) = G_{\mathrm{diag}}$.

(3) Since $\eta : P\Gamma L(2, q) \to \{\pm 1\}$ is a homomorphism and the coordinate swap $(i, j) \mapsto (j, i)$ commutes with $(i, j) \mapsto (g(i), g(j))$, $\psi$ is a group homomorphism. Because $\psi(g)(i, i) = (g(i), g(i))$ and $P\Gamma L(2, q)$ acts faithfully on $X$, $\psi$ is injective. For $g \in P\Sigma L(2, q)$, (1) gives
$$\tilde{H}_{(g(i), g(j)), (g(k), g(l))} = H_{g(k), g(j)} H_{g(i), g(l)} = (\varepsilon_i \varepsilon_j)(\varepsilon_k \varepsilon_l)\tilde{H}_{(i, j), (k, l)},$$
while for $g \in P\Gamma L(2, q) \setminus P\Sigma L(2, q)$, (1) gives
$$\tilde{H}_{(g(j), g(i)), (g(l), g(k))} = H_{g(l), g(i)} H_{g(j), g(k)} = (\varepsilon_l \varepsilon_i H_{i, l})(\varepsilon_j \varepsilon_k H_{k, j}) = (\varepsilon_i \varepsilon_j)(\varepsilon_k \varepsilon_l)\tilde{H}_{(i, j), (k, l)}.$$
Hence $\psi(P\Gamma L(2, q)) \le \mathrm{Aut}_s(\tilde{H})$. Since $PSL(2, q) \le P\Sigma L(2, q)$ is $2$-transitive on $X$, $\psi(P\Gamma L(2, q))$ acts transitively on both $\Delta$ and $X^2 \setminus \Delta$, while preserving $\Delta$. $\square$

---

## 2. Elliptic-Curve Hasse Bounds and Diagonal-Preserving Strong Equivalences

### Lemma 2 (Hasse bounds on $4$-column and $\Delta$-signature sums)
Let $q > 11$ be a prime power with $q \equiv 3 \pmod 4$ and $H = I + S$ as above.
1. For any four distinct $j_1, j_2, r_1, r_2 \in X$,
   $$\bigl|T_4^{\mathrm{col}}(j_1, j_2, r_1, r_2)\bigr| := \left|\sum_{k \in X} H_{k, j_1} H_{k, j_2} H_{k, r_1} H_{k, r_2}\right| \le 2\sqrt{q} + 4.$$
2. For each $(i, j) \in X^2 \setminus \Delta$, define its $\Delta$-signature vector $v_{ij} \in \{\pm 1\}^X$ by $(v_{ij})_k := \tilde{H}_{(i, j), (k, k)} = H_{k, j} H_{i, k}$. Then:
   - $\langle v_{ij}, v_{ji} \rangle = d - 4 = q - 3$ for all $i \neq j$;
   - for all off-diagonal $(u, v) \notin \{(i, j), (j, i)\}$,
     $$\bigl|\langle v_{ij}, v_{uv} \rangle\bigr| \le 2\sqrt{q} + 4 < q - 3 = d - 4.$$

*Proof.*
(1) By Lemma 1(1), replacing $(j_1, j_2, r_1, r_2)$ by $(g(j_1), g(j_2), g(r_1), g(r_2))$ for $g \in PSL(2, q)$ multiplies $T_4^{\mathrm{col}}$ by $\varepsilon_{j_1}\varepsilon_{j_2}\varepsilon_{r_1}\varepsilon_{r_2} \in \{\pm 1\}$ (since $\varepsilon_k^4 = 1$). By $2$-transitivity of $PSL(2, q)$ on $X$, we may assume $j_1 = \infty$ and $j_2 = 0$, with $r_1, r_2 \in \mathbb{F}_q^\times$ distinct.
- For $k \in \mathbb{F}_q \setminus \{0, r_1, r_2\}$, we have $H_{k, \infty} H_{k, 0} H_{k, r_1} H_{k, r_2} = (-1)\chi(k)\chi(k - r_1)\chi(k - r_2) = -\chi(k(k - r_1)(k - r_2))$.
- For the four remaining indices $k \in \{\infty, 0, r_1, r_2\}$, setting $a := \chi(r_1)$, $b := \chi(r_2)$, $c := \chi(r_1 - r_2) \in \{\pm 1\}$ and using $\chi(-1) = -1$:
  - $k = \infty$: $(+1)^4 = 1$;
  - $k = 0$: $(-1)(+1)\chi(-r_1)\chi(-r_2) = -ab$;
  - $k = r_1$: $(-1)\chi(r_1)(+1)\chi(r_1 - r_2) = -ac$;
  - $k = r_2$: $(-1)\chi(r_2)\chi(r_2 - r_1)(+1) = +bc$.
  Their sum is $B^{\mathrm{col}}(r_1, r_2) = (1 - ab) - c(a - b)$, which equals $0$ if $a = b$ and $2(1 - ac) \in \{0, 4\}$ if $a = -b$.

Since $\mathrm{char}(\mathbb{F}_q) \neq 2$ and $0, r_1, r_2 \in \mathbb{F}_q$ are distinct, $E : y^2 = x(x - r_1)(x - r_2)$ is a smooth elliptic curve over $\mathbb{F}_q$ with Frobenius trace $a_q(E) = q + 1 - \#E(\mathbb{F}_q) = -\sum_{k \in \mathbb{F}_q} \chi(k(k - r_1)(k - r_2))$. By Hasse's theorem, $|a_q(E)| \le 2\sqrt{q}$, whence
$$\bigl|T_4^{\mathrm{col}}(\infty, 0, r_1, r_2)\bigr| = \bigl|a_q(E) + B^{\mathrm{col}}(r_1, r_2)\bigr| \le 2\sqrt{q} + 4.$$

(2) First, for any $i \neq j$,
$$\langle v_{ij}, v_{ji} \rangle = \sum_{k \in X} (H_{i, k} H_{k, i})(H_{j, k} H_{k, j}) = (d - 2)(+1) + 2(-1) = d - 4 = q - 3,$$
since $H_{a, k} H_{k, a} = -1$ for $k \neq a$ and $+1$ for $k = a$.

Now let $(u, v) \in X^2 \setminus \Delta$ with $(u, v) \notin \{(i, j), (j, i)\}$.
- **Case 2a ($u = i$ or $v = j$):** If $u = i$ (and $v \neq j$), then $\langle v_{ij}, v_{iv} \rangle = \sum_k H_{k, j} H_{k, v} = 0$ by column orthogonality of $H$; if $v = j$ (and $u \neq i$), then $\langle v_{ij}, v_{uj} \rangle = \sum_k H_{i, k} H_{u, k} = 0$ by row orthogonality.
- **Case 2b ($u = j, v \neq i$ or $v = i, u \neq j$):** If $u = j$ and $v \neq i$, using $H_{k, j} H_{j, k} = -1$ for $k \neq j$ and $+1$ for $k = j$, together with $(H^2)_{i, v} = (2S - (q - 1)I)_{i, v} = 2 H_{i, v}$ for $i \neq v$, we obtain
  $$\langle v_{ij}, v_{jv} \rangle = \sum_{k \in X} (H_{k, j} H_{j, k}) H_{i, k} H_{k, v} = -(H^2)_{i, v} + 2 H_{i, j} H_{j, v} = -2 H_{i, v} + 2 H_{i, j} H_{j, v} \in \{0, \pm 4\}.$$
  The case $v = i, u \neq j$ follows by symmetry $\langle v_{ij}, v_{ui} \rangle = \langle v_{ui}, v_{ij} \rangle$.
- **Case 2c ($i, j, u, v$ pairwise distinct):** For $g \in PSL(2, q)$, Lemma 1(1) gives $(v_{g(i), g(j)})_{g(k)} = \varepsilon_i \varepsilon_j (v_{ij})_k$, preserving $|\langle v_{ij}, v_{uv} \rangle|$. By $2$-transitivity of $PSL(2, q)$, we may assume $i = \infty$ and $j = 0$, with $u, v \in \mathbb{F}_q^\times$ distinct.
  - For $k \in \mathbb{F}_q \setminus \{0, u, v\}$, we have $H_{k, 0} H_{\infty, k} H_{k, v} H_{u, k} = \chi(k)\chi(k - v)\chi(u - k) = -\chi(k(k - u)(k - v))$.
  - For $k \in \{\infty, 0, u, v\}$, setting $a := \chi(u)$, $b := \chi(v)$, $c := \chi(u - v) \in \{\pm 1\}$:
    - $k = \infty$: $(+1)(+1)(+1)(-1) = -1$;
    - $k = 0$: $(+1)(+1)\chi(-v)\chi(u) = -ab$;
    - $k = u$: $\chi(u)(+1)\chi(u - v)(+1) = +ac$;
    - $k = v$: $\chi(v)(+1)(+1)\chi(u - v) = +bc$.
    Their sum is $B(u, v) = -(1 + ab) + c(a + b)$, which equals $0$ if $a = -b$ and $-2(1 - ac) \in \{0, -4\}$ if $a = b$.

  By Hasse's theorem on the smooth elliptic curve $E_{u, v} : y^2 = x(x - u)(x - v)$ over $\mathbb{F}_q$,
  $$\bigl|\langle v_{\infty, 0}, v_{u, v} \rangle\bigr| = \bigl|a_q(E_{u, v}) + B(u, v)\bigr| \le 2\sqrt{q} + 4.$$

Finally, because $q > 11$ and $q \equiv 3 \pmod 4$, we have $q \ge 19$, so $(q - 7)^2 - 4q = (q - 9)^2 - 32 \ge 10^2 - 32 = 68 > 0$. Since $q - 7 > 0$, this yields $2\sqrt{q} < q - 7$, i.e., $2\sqrt{q} + 4 < q - 3 = d - 4$ (which also dominates $4$ in Case 2b). $\square$

### Lemma 3 (Rigidity of diagonal-preserving strong equivalences)
Let $q > 11$ be a prime power with $q \equiv 3 \pmod 4$, let $H = I + S$ be the Paley I matrix of order $d = q + 1$, and let $H' = I + S' \in \{\pm 1\}^{X \times X}$ be **any** skew-Hadamard matrix ($H'_{i, i} = 1$ for all $i \in X$, $(S')^\top = -S'$). Suppose $\Psi \in S_{X^2}$ induces a strong equivalence from $\tilde{H}'$ to $\tilde{H}$ satisfying $\Psi(\Delta) = \Delta$. Define $\tau \in S_X$ by $\Psi(i, i) = (\tau(i), \tau(i))$ for $i \in X$. Then there exist $\eta \in \{+1, -1\}$ and signs $\delta_i \in \{\pm 1\}$ ($i \in X$) such that:
1. for all $i, j \in X$,
   $$H_{\tau(i), \tau(j)} = \begin{cases} \delta_i \delta_j H'_{i, j} & \text{if } \eta = +1, \\ \delta_i \delta_j H'_{j, i} & \text{if } \eta = -1; \end{cases}$$
2. for all $(i, j) \in X^2$,
   $$\Psi(i, j) = \begin{cases} (\tau(i), \tau(j)) & \text{if } \eta = +1, \\ (\tau(j), \tau(i)) & \text{if } \eta = -1. \end{cases}$$

*Proof.* Let $\mu_{i, j} \in \{\pm 1\}$ satisfy $\tilde{H}_{\Psi(i, j), \Psi(k, l)} = \mu_{i, j} \mu_{k, l} \tilde{H}'_{(i, j), (k, l)}$ for all $(i, j), (k, l) \in X^2$. Since both $H$ and $H'$ are skew-Hadamard, for all $i \neq k$ we have $\tilde{H}_{(i, i), (k, k)} = H_{k, i} H_{i, k} = -1$ and similarly $\tilde{H}'_{(i, i), (k, k)} = -1$. Restricting to $\Delta \times \Delta$ gives $-1 = \mu_{i, i} \mu_{k, k}(-1)$, so $\mu_{i, i} \mu_{k, k} = 1$ for all $i \neq k$. Since $d \ge 3$, $\mu_{i, i}$ is constant on $\Delta$; negating all $\mu$ if necessary, we may assume $\mu_{k, k} = +1$ for every $k \in X$.

For each $i \neq j$ in $X$, let $(w'_{i, j})_k := \tilde{H}'_{(i, j), (k, k)} = H'_{k, j} H'_{i, k}$. Then for all $k \in X$,
$$(v_{\Psi(i, j)})_{\tau(k)} = \tilde{H}_{\Psi(i, j), (\tau(k), \tau(k))} = \mu_{i, j} (w'_{i, j})_k.$$
Consequently, $\langle v_{\Psi(i, j)}, v_{\Psi(j, i)} \rangle = \mu_{i, j} \mu_{j, i} \langle w'_{i, j}, w'_{j, i} \rangle$, and by the same computation as in Lemma 2(2) (which uses only that $H'$ is skew-Hadamard), $\langle w'_{i, j}, w'_{j, i} \rangle = d - 4$. Hence $|\langle v_{\Psi(i, j)}, v_{\Psi(j, i)} \rangle| = d - 4$. By Lemma 2(2), the unique partner of any off-diagonal $(u, v)$ achieving $|\langle v_{u, v}, v_{u', v'} \rangle| = d - 4$ is $(v, u)$. Writing $\Psi(i, j) = (u, v)$, we must therefore have $\Psi(j, i) = (v, u)$. Comparing the entrywise products
$$(v_{u, v})_{\tau(k)} (v_{v, u})_{\tau(k)} = \mu_{i, j} \mu_{j, i} (w'_{i, j})_k (w'_{j, i})_k,$$
we see that the left-hand side takes the value $-1$ precisely at $\tau(k) \in \{u, v\}$ and $+1$ at all other $d - 2$ indices, while $(w'_{i, j})_k (w'_{j, i})_k$ takes the value $-1$ precisely at $k \in \{i, j\}$ and $+1$ at all other $d - 2$ indices. Because $d - 2 > 2$, we must have $\mu_{i, j} \mu_{j, i} = +1$ and $\{u, v\} = \{\tau(i), \tau(j)\}$.

Thus, for each ordered pair $(i, j)$ with $i \neq j$, there is a sign $s(i, j) \in \{+1, -1\}$ such that $\Psi(i, j) = (\tau(i), \tau(j))$ if $s(i, j) = +1$, and $\Psi(i, j) = (\tau(j), \tau(i))$ if $s(i, j) = -1$ (and clearly $s(j, i) = s(i, j)$). Evaluate $(v_{\Psi(i, j)})_{\tau(k)} = \mu_{i, j} (w'_{i, j})_k$ at $k = i$ and at any $k \notin \{i, j\}$:
- At $k = i$: $(w'_{i, j})_i = H'_{i, j} H'_{i, i} = S'_{i, j}$. Meanwhile $(v_{\tau(i), \tau(j)})_{\tau(i)} = S_{\tau(i), \tau(j)}$ and $(v_{\tau(j), \tau(i)})_{\tau(i)} = S_{\tau(j), \tau(i)} = -S_{\tau(i), \tau(j)}$. Hence in both cases,
  $$S_{\tau(i), \tau(j)} = s(i, j) \mu_{i, j} S'_{i, j}, \qquad \text{so} \qquad \mu_{i, j} = s(i, j) S_{\tau(i), \tau(j)} S'_{i, j}.$$
- At $k \notin \{i, j\}$: $(w'_{i, j})_k = S'_{k, j} S'_{i, k}$. Meanwhile $(v_{\tau(i), \tau(j)})_{\tau(k)} = S_{\tau(k), \tau(j)} S_{\tau(i), \tau(k)}$ and $(v_{\tau(j), \tau(i)})_{\tau(k)} = S_{\tau(k), \tau(i)} S_{\tau(j), \tau(k)} = (-S_{\tau(i), \tau(k)})(-S_{\tau(k), \tau(j)}) = S_{\tau(k), \tau(j)} S_{\tau(i), \tau(k)}$. Substituting $\mu_{i, j}$ gives
  $$S_{\tau(i), \tau(k)} S_{\tau(k), \tau(j)} = s(i, j) S_{\tau(i), \tau(j)} S'_{i, j} S'_{i, k} S'_{k, j}.$$
  Multiplying both sides by $S_{\tau(j), \tau(i)}$ (using $S_{\tau(i), \tau(j)} S_{\tau(j), \tau(i)} = -1$ and $-S'_{i, j} = S'_{j, i}$) yields
  $$S_{\tau(i), \tau(k)} S_{\tau(k), \tau(j)} S_{\tau(j), \tau(i)} = s(i, j) S'_{i, k} S'_{k, j} S'_{j, i} \qquad \text{for all distinct } i, j, k \in X.$$

Since both $S_{\tau(i), \tau(k)} S_{\tau(k), \tau(j)} S_{\tau(j), \tau(i)}$ and $S'_{i, k} S'_{k, j} S'_{j, i}$ are invariant under cyclic permutations of $(i, j, k)$ and negate under transpositions, their ratio $s(i, j)$ is invariant under all permutations of $\{i, j, k\}$. Hence $s(i, j) = s(j, k) = s(k, i)$ for all distinct $i, j, k \in X$. As $d \ge 4$, $s(i, j) = \eta \in \{+1, -1\}$ is constant for all $i \neq j$, proving (2).

Finally, fix any $a_0 \in X$, set $\delta_{a_0} := 1$, and define $\delta_k := \eta S_{\tau(a_0), \tau(k)} S'_{a_0, k} \in \{\pm 1\}$ for $k \neq a_0$. For any distinct $i, j \in X \setminus \{a_0\}$, applying the triple-product identity to $(a_0, i, j)$ and using $S_{\tau(j), \tau(a_0)} = -S_{\tau(a_0), \tau(j)}$ and $S'_{j, a_0} = -S'_{a_0, j}$ gives
$$S_{\tau(i), \tau(j)} = \eta \bigl(S_{\tau(a_0), \tau(i)} S'_{a_0, i}\bigr)\bigl(S_{\tau(a_0), \tau(j)} S'_{a_0, j}\bigr) S'_{i, j} = \eta \, \delta_i \delta_j S'_{i, j},$$
and this also holds for $i = a_0$ or $j = a_0$ by definition of $\delta_k$ and skew-symmetry of $S, S'$. Since $H_{\tau(i), \tau(i)} = 1 = \delta_i^2 H'_{i, i}$ and $-S'_{i, j} = S'_{j, i}$ for $i \neq j$, adding $I$ yields (1). $\square$

---

## 3. Characterization of $d$-Cliques and Proof of Part (a)

Call a $d$-element subset $C \subset X^2$ a **$d$-clique of the two-graph of $\tilde{H}$** if
$$\tilde{H}_{x, y} \tilde{H}_{y, z} \tilde{H}_{z, x} = -1 \qquad \text{for all distinct } x, y, z \in C.$$
Notice that $\Delta$ is a $d$-clique (since $\tilde{H}_{(i, i), (k, k)} = -1$ for $i \neq k$), and every $\Phi \in \mathrm{Aut}_s(\tilde{H})$ preserves triple products $\tilde{H}_{x, y}\tilde{H}_{y, z}\tilde{H}_{z, x}$ and therefore maps $d$-cliques to $d$-cliques.

### Lemma 4 (Every $d$-clique of $\tilde{H}$ is a permutation graph)
For every prime power $q > 11$ with $q \equiv 3 \pmod 4$, every $d$-clique $C \subset X^2$ of the two-graph of $\tilde{H}$ contains exactly one element in each row $\{i\} \times X$ and each column $X \times \{j\}$; that is, $C = \{(i, \sigma(i)) : i \in X\}$ for some bijection $\sigma \in S_X$.

*Proof.* First observe that if two distinct elements of $C$ lie in the same row, say $(i, j_1), (i, j_2) \in C$ ($j_1 \neq j_2$), then for every third element $(k, l) \in C \setminus \{(i, j_1), (i, j_2)\}$,
$$-1 = \tilde{H}_{(i, j_1), (i, j_2)} \tilde{H}_{(i, j_2), (k, l)} \tilde{H}_{(k, l), (i, j_1)} = (H_{i, j_1} H_{i, j_2})(H_{k, j_2} H_{i, l})(H_{i, l} H_{k, j_1}) = H_{i, j_1} H_{i, j_2} H_{k, j_1} H_{k, j_2}.$$
In particular, $k \neq i$ (otherwise the right-hand side equals $(H_{i, j_1} H_{i, j_2})^2 = +1$), so **every row contains at most $2$ elements of $C$**. By the exact same calculation for two elements $(i_1, j), (i_2, j) \in C$ in the same column,
$$-1 = \tilde{H}_{(i_1, j), (i_2, j)} \tilde{H}_{(i_2, j), (k, l)} \tilde{H}_{(k, l), (i_1, j)} = H_{i_1, j} H_{i_2, j} H_{i_1, l} H_{i_2, l},$$
which forces $l \neq j$, so **every column also contains at most $2$ elements of $C$**.

Suppose for contradiction that some row $i_1 \in X$ contains $2$ elements $(i_1, j_1), (i_1, j_2) \in C$ ($j_1 \neq j_2$). Set $\eta_1 := -H_{i_1, j_1} H_{i_1, j_2} \in \{\pm 1\}$ and
$$R_1 := \{k \in X : H_{k, j_1} H_{k, j_2} = \eta_1\}.$$
By column orthogonality of $H$, $|R_1| = d / 2$ (and $i_1 \notin R_1$). By the triple-product identity above, every $(k, l) \in C \setminus \{(i_1, j_1), (i_1, j_2)\}$ satisfies $k \in R_1$. Letting $m_1$ and $m_2$ be the numbers of rows in $R_1$ containing $1$ and $2$ elements of $C$, respectively, we have $m_1 + m_2 \le |R_1| = d/2$ and $m_1 + 2 m_2 = d - 2$, whence $m_2 \ge \frac{d}{2} - 2$.

Since column $j_1$ already contains $(i_1, j_1)$ and column $j_2$ already contains $(i_1, j_2)$, and each column contains at most $2$ elements of $C$, at most $2$ rows in $R_1$ contain an element of $C$ in column $j_1$ or $j_2$. Because $d = q + 1 \ge 20$, we have $m_2 - 2 \ge \frac{d}{2} - 4 \ge 6 \ge 1$. Hence there exists a row $i_3 \in R_1$ containing $2$ elements $(i_3, r_1), (i_3, r_2) \in C$ such that $j_1, j_2, r_1, r_2 \in X$ are four distinct columns. Set $\eta_3 := -H_{i_3, r_1} H_{i_3, r_2} \in \{\pm 1\}$ and
$$R_3 := \{k \in X : H_{k, r_1} H_{k, r_2} = \eta_3\}.$$
Every element $(k, l) \in C \setminus \{(i_1, j_1), (i_1, j_2), (i_3, r_1), (i_3, r_2)\}$ must have $k \in R_1 \cap R_3$. Since there are $d - 4$ such elements and each row contains at most $2$ elements of $C$, we obtain
$$|R_1 \cap R_3| \ge \frac{d - 4}{2} = \frac{d}{2} - 2.$$
On the other hand, using indicator functions $\mathbf{1}_{k \in R_1} = \frac{1 + \eta_1 H_{k, j_1} H_{k, j_2}}{2}$ and $\mathbf{1}_{k \in R_3} = \frac{1 + \eta_3 H_{k, r_1} H_{k, r_2}}{2}$ together with column orthogonality of $H$,
$$|R_1 \cap R_3| = \frac{d + \eta_1 \eta_3 T_4^{\mathrm{col}}(j_1, j_2, r_1, r_2)}{4} \le \frac{d + 2\sqrt{q} + 4}{4}$$
by Lemma 2(1).

- **Case $q \ge 23$:** We have $(q - 11)^2 - 4q = (q - 13)^2 - 48 \ge 10^2 - 48 = 52 > 0$. Since $q - 11 > 0$, this gives $2\sqrt{q} < q - 11$, so $2\sqrt{q} + 4 < q - 7 = d - 8$, and therefore
  $$|R_1 \cap R_3| \le \frac{d + 2\sqrt{q} + 4}{4} < \frac{2d - 8}{4} = \frac{d}{2} - 2,$$
  a contradiction.
- **Case $q = 19$ ($d = 20$):** Here $\frac{d}{2} - 2 = 8$, so $|R_1 \cap R_3| \ge 8$ requires $\eta_1 \eta_3 T_4^{\mathrm{col}}(j_1, j_2, r_1, r_2) \ge 12$. By $2$-transitivity of $PSL(2, 19)$ on $PG(1, 19)$ (which preserves $H$ up to signs via Lemma 1(1), hence preserves $d$-cliques up to signs and preserves $|T_4^{\mathrm{col}}|$), we may assume $\{j_1, j_2\} = \{\infty, 0\}$ and $\{r_1, r_2\} \subset \mathbb{F}_{19}^\times$. Under the $9$ square scalings $t \mapsto s t$ ($s \in (\mathbb{F}_{19}^\times)^2$) fixing $\infty$ and $0$, the $\binom{18}{2} = 153$ unordered pairs $\{r_1, r_2\} \subset \mathbb{F}_{19}^\times$ partition into $17$ orbits of size $9$, with $T_4^{\mathrm{col}}(\infty, 0, r_1, r_2)$ constant on each orbit. Direct exact evaluation (verified in `verify.py`) shows that $16$ of these $17$ orbits satisfy $T_4^{\mathrm{col}}(\infty, 0, r_1, r_2) \in \{-4, +4\}$ (giving $|R_1 \cap R_3| \le 6 < 8$), and only the single orbit represented by $\{r_1, r_2\} = \{1, 12\}$ satisfies $T_4^{\mathrm{col}}(\infty, 0, 1, 12) = +12$.

  Thus, after scaling by a square, $\{r_1, r_2\} = \{1, 12\}$, $\eta_1 = \eta_3 \in \{+1, -1\}$, and $|R_1 \cap R_3| = 8 = \frac{d}{2} - 2$. Because the $16$ elements of $C \setminus \{(i_1, \infty), (i_1, 0), (i_3, 1), (i_3, 12)\}$ lie in the $8$ rows of $R_1 \cap R_3$ with at most $2$ per row, **every** row of $R_1 \cap R_3$ contains exactly $2$ elements of $C$. Moreover, $i_1 \in R_3 \setminus R_1$ and $i_3 \in R_1 \setminus R_3$ (each difference set having size $10 - 8 = 2$), so $C$ consists of $2$ elements in each row of the $10$-element set $R_C := (R_1 \cap R_3) \cup \{i_1, i_3\}$. Consequently, for every row $r \in R_C$, its pair of columns $\{c_1, c_2\} \subset PG(1, 19)$ must satisfy
  $$H_{k, c_1} H_{k, c_2} = -H_{r, c_1} H_{r, c_2} \qquad \text{for all } k \in R_C \setminus \{r\}.$$
  Explicitly for $\{j_1, j_2\} = \{\infty, 0\}$ and $\{r_1, r_2\} = \{1, 12\}$:
  - When $\eta_1 = \eta_3 = +1$: $R_1 \cap R_3 = \{2, 3, 10, 12, 14, 15, 18, \infty\}$, $R_3 \setminus R_1 = \{11, 17\}$, and $R_1 \setminus R_3 = \{8, 13\}$. For all $4$ choices of $(i_1, i_3) \in \{11, 17\} \times \{8, 13\}$, direct check over all $\binom{20}{2} = 190$ column pairs $\{c_1, c_2\}$ shows that row $r = \infty \in R_C$ admits **no** column pair satisfying $H_{k, c_1} H_{k, c_2} = -H_{\infty, c_1} H_{\infty, c_2} = -1$ for all $k \in R_C \setminus \{\infty\}$.
  - When $\eta_1 = \eta_3 = -1$: $R_1 \cap R_3 = \{0, 1, 4, 5, 6, 7, 9, 16\}$, $R_3 \setminus R_1 = \{8, 13\}$, and $R_1 \setminus R_3 = \{11, 17\}$. For all $4$ choices of $(i_1, i_3) \in \{8, 13\} \times \{11, 17\}$, direct check over all $190$ column pairs shows that row $r = 0 \in R_C$ admits **no** column pair satisfying $H_{k, c_1} H_{k, c_2} = -H_{0, c_1} H_{0, c_2}$ for all $k \in R_C \setminus \{0\}$.

  This eliminates $q = 19$ as well.

Therefore no row contains $2$ elements of $C$. Since $|C| = d$, each of the $d$ rows contains exactly $1$ element of $C$. By the exact same argument with rows and columns interchanged (note that $H^\top$ is strongly equivalent to $H$ via any $g_0 \in P\Gamma L(2, q) \setminus P\Sigma L(2, q)$ by Lemma 1(1), so the row-column transpose $(i, j) \mapsto (j, i)$ sends $d$-cliques of $\tilde{H}$ to $d$-cliques of $\widetilde{H^\top}$, which is strongly equivalent to $\tilde{H}$), no column contains $2$ elements of $C$ either. Hence $C = \{(i, \sigma(i)) : i \in X\}$ for a bijection $\sigma \in S_X$. $\square$

### Theorem 1 (Proof of Conjecture `conj:Paley`(a))
For every prime power $q > 11$ with $q \equiv 3 \pmod 4$, $\mathrm{Aut}_s(\tilde{H}) = \psi(P\Gamma L(2, q)) \cong P\Gamma L(2, q)$, which has exactly two orbits on $X^2$: $\Delta = \{(i, i) : i \in X\}$ and $X^2 \setminus \Delta$.

*Proof.* We first prove that every $\Phi \in \mathrm{Aut}_s(\tilde{H})$ holds $\Delta$ invariant. Suppose for contradiction that there exists $\Phi \in \mathrm{Aut}_s(\tilde{H})$ with $C := \Phi(\Delta) \neq \Delta$. Since $C$ is a $d$-clique of the two-graph of $\tilde{H}$, Lemma 4 yields a non-identity bijection $\sigma \in S_X$ such that $C = \{(i, \sigma(i)) : i \in X\}$. Pick $a \in X$ with $\sigma(a) \neq a$. Because $PSL(2, q)$ is $2$-transitive on $X$, there exists $g \in PSL(2, q)$ with $g(a) = \infty$ and $g(\sigma(a)) = 0$. Replacing $\Phi$ by $\psi(g) \circ \Phi \in \mathrm{Aut}_s(\tilde{H})$ replaces $C$ by $\{(i, (g \sigma g^{-1})(i)) : i \in X\}$, so we may assume without loss of generality that $\sigma(\infty) = 0$.

Since $C$ is a $d$-clique, fixing $\varepsilon_\infty := 1$ and defining $\varepsilon_i := -\tilde{H}_{(\infty, 0), (i, \sigma(i))}$ for $i \in \mathbb{F}_q$ yields signs $\varepsilon_i \in \{\pm 1\}$ ($i \in X$) such that
$$H_{k, \sigma(i)} H_{i, \sigma(k)} = \tilde{H}_{(i, \sigma(i)), (k, \sigma(k))} = -\varepsilon_i \varepsilon_k \qquad \text{for all } i \neq k \in X.$$
Setting $i = \infty$ (where $\sigma(\infty) = 0$ and $H_{\infty, m} = 1$ for all $m \in X$) gives $H_{k, 0} = -\varepsilon_k$, i.e., $\varepsilon_k = -H_{k, 0}$ for all $k \in \mathbb{F}_q$. Substituting this into the displayed equation for distinct $i, k \in \mathbb{F}_q$ yields
$$H_{i, \sigma(k)} = -H_{i, 0} H_{k, 0} H_{k, \sigma(i)} \qquad \text{for all } i \neq k \in \mathbb{F}_q.$$
Now fix any $i \in \mathbb{F}_q$, put $y := \sigma(i) \neq 0$, and sum both sides over all $k \in \mathbb{F}_q \setminus \{i\}$:
- As $k$ runs over $\mathbb{F}_q \setminus \{i\}$, $\sigma(k)$ runs bijectively over $X \setminus \{0, y\}$. Using $\sum_{m \in X} H_{i, m} = 0$, the left-hand side equals $-H_{i, 0} - H_{i, y}$.
- On the right-hand side, since $y \neq 0$, column orthogonality $\sum_{k \in X} H_{k, 0} H_{k, y} = 0$ together with $H_{\infty, 0} H_{\infty, y} = 1$ gives
  $$-H_{i, 0}\Bigl(0 - 1 - H_{i, 0} H_{i, y}\Bigr) = H_{i, 0} + H_{i, y}.$$
Equating the two sides gives $-H_{i, 0} - H_{i, y} = H_{i, 0} + H_{i, y}$, so $H_{i, \sigma(i)} = -H_{i, 0}$ for every $i \in \mathbb{F}_q$.

Define the Hadamard matrix $H' \in \{\pm 1\}^{X \times X}$ by $H'_{i, k} := \varepsilon_i H_{i, \sigma(k)}$. Then:
- $H'_{\infty, \infty} = \varepsilon_\infty H_{\infty, 0} = (+1)(+1) = +1$, and for all $i \in \mathbb{F}_q$, $H'_{i, i} = \varepsilon_i H_{i, \sigma(i)} = (-H_{i, 0})(-H_{i, 0}) = +1$;
- for all $i \neq k \in X$, $H'_{i, k} H'_{k, i} = (\varepsilon_i H_{i, \sigma(k)})(\varepsilon_k H_{k, \sigma(i)}) = -1$, so $H'_{k, i} = -H'_{i, k}$.

Hence $H' = I + S'$ is a skew-Hadamard matrix! Moreover, for all $(i, j), (k, l) \in X^2$,
$$\tilde{H}'_{(i, j), (k, l)} = H'_{k, j} H'_{i, l} = \varepsilon_i \varepsilon_k H_{k, \sigma(j)} H_{i, \sigma(l)} = \varepsilon_i \varepsilon_k \tilde{H}_{(i, \sigma(j)), (k, \sigma(l))}.$$
Thus $\iota(\mathrm{id}, \sigma) : (i, j) \mapsto (i, \sigma(j))$ induces a strong equivalence from $\tilde{H}'$ to $\tilde{H}$ sending $\Delta$ onto $C$. Composing with $\Phi^{-1} \in \mathrm{Aut}_s(\tilde{H})$ (which sends $C$ onto $\Delta$), the permutation $\Psi := \Phi^{-1} \circ \iota(\mathrm{id}, \sigma) \in S_{X^2}$ induces a strong equivalence from $\tilde{H}'$ to $\tilde{H}$ satisfying $\Psi(\Delta) = \Delta$.

Applying Lemma 3 to $\Psi$ yields $\tau \in S_X$, signs $\delta_i \in \{\pm 1\}$, and $\eta \in \{+1, -1\}$ such that:
- **If $\eta = +1$:** $H_{\tau(i), \tau(j)} = \delta_i \delta_j H'_{i, j} = (\delta_i \varepsilon_i) \delta_j H_{i, \sigma(j)}$ for all $i, j \in X$. Substituting $j \mapsto \sigma^{-1}(j)$ yields
  $$H_{\tau(i), (\tau \sigma^{-1})(j)} = (\delta_i \varepsilon_i) \delta_{\sigma^{-1}(j)} H_{i, j} \qquad \text{for all } i, j \in X,$$
  so $(\tau, \tau \sigma^{-1}) \in \mathrm{Aut}_w(H)$. By Lemma 1(2) (Kantor's theorem), $\tau = \tau \sigma^{-1}$, whence $\sigma = \mathrm{id}$, a contradiction.
- **If $\eta = -1$:** $H_{\tau(i), \tau(j)} = \delta_i \delta_j H'_{j, i} = \delta_i (\delta_j \varepsilon_j) H_{j, \sigma(i)}$ for all $i, j \in X$. Pick any fixed $g_0 \in P\Gamma L(2, q) \setminus P\Sigma L(2, q)$ with signs $\alpha_a \in \{\pm 1\}$ satisfying $H_{g_0(a), g_0(b)} = \alpha_a \alpha_b H_{b, a}$ by Lemma 1(1). Applying this to $a = \tau(j)$, $b = \tau(i)$ gives
  $$H_{(g_0 \tau)(j), (g_0 \tau)(i)} = \alpha_{\tau(j)} \alpha_{\tau(i)} H_{\tau(i), \tau(j)} = \bigl(\alpha_{\tau(j)} \delta_j \varepsilon_j\bigr)\bigl(\alpha_{\tau(i)} \delta_i\bigr) H_{j, \sigma(i)}.$$
  Substituting $i \mapsto \sigma^{-1}(i)$ shows $(g_0 \tau, g_0 \tau \sigma^{-1}) \in \mathrm{Aut}_w(H)$. Again by Lemma 1(2), $g_0 \tau = g_0 \tau \sigma^{-1}$, forcing $\sigma = \mathrm{id}$, a contradiction.

Thus every $\Phi \in \mathrm{Aut}_s(\tilde{H})$ satisfies $\Phi(\Delta) = \Delta$. Now apply Lemma 3 with $H' = H$ to any $\Phi \in \mathrm{Aut}_s(\tilde{H})$:
- If $\eta = +1$, then $H_{\tau(i), \tau(j)} = \delta_i \delta_j H_{i, j}$, so $(\tau, \tau) \in \mathrm{Aut}_w(H)$, whence $\tau \in P\Sigma L(2, q)$ by Lemma 1(2) and $\Phi(i, j) = (\tau(i), \tau(j)) = \psi(\tau)(i, j)$.
- If $\eta = -1$, then $H_{\tau(i), \tau(j)} = \delta_i \delta_j H_{j, i}$, so $(g_0 \tau, g_0 \tau) \in \mathrm{Aut}_w(H)$ (with $g_0 \in P\Gamma L(2, q) \setminus P\Sigma L(2, q)$ as above), whence $g_0 \tau \in P\Sigma L(2, q)$, so $\tau \in P\Gamma L(2, q) \setminus P\Sigma L(2, q)$ and $\Phi(i, j) = (\tau(j), \tau(i)) = \psi(\tau)(i, j)$.

Therefore $\mathrm{Aut}_s(\tilde{H}) = \psi(P\Gamma L(2, q)) \cong P\Gamma L(2, q)$, and its orbits on $X^2$ are $\Delta$ and $X^2 \setminus \Delta$ by Lemma 1(3). $\square$

---

## 4. Proof of Part (b) and the Non-Transitive SIC Corollary

### Theorem 2 (Proof of Conjecture `conj:Paley`(b))
Let $q > 11$ be a prime power with $q \equiv 3 \pmod 4$, let $d := q + 1$, and let $p \equiv 3 \pmod 4$ be any prime dividing $d - 8$. For the SIC $\{x_{ij}\}_{(i, j) \in X^2}$ in $\mathbb{F}_{p^2}^d$ constructed from the Paley I matrix $H$ by Theorem 2 (`thm.main`), we have
$$\mathrm{Aut}_s(\{x_{ij}\}) = \iota(\mathrm{Aut}_w(H)) \qquad \text{and} \qquad \mathrm{Aut}_w(\{x_{ij}\}) = \mathrm{Aut}_s(\tilde{H}).$$

*Proof.* By Theorem 15(c) (`thm:sandwich`(c)),
$$\iota(\mathrm{Aut}_w(H)) \le \mathrm{Aut}_s(\{x_{ij}\}) \le \mathrm{Aut}_w(\{x_{ij}\}) \le \mathrm{Aut}_s(\tilde{H}).$$
By Lemma 1(2) and Theorem 1, $\iota(\mathrm{Aut}_w(H)) = \psi(P\Sigma L(2, q))$ has index $2$ in $\mathrm{Aut}_s(\tilde{H}) = \psi(P\Gamma L(2, q))$. Fix any $g_0 \in P\Gamma L(2, q) \setminus P\Sigma L(2, q)$ and set $\pi := \psi(g_0) : (i, j) \mapsto (g_0(j), g_0(i))$. Since $\psi(P\Gamma L(2, q)) = \langle \psi(P\Sigma L(2, q)), \pi \rangle$, it suffices to prove that $\pi \in \mathrm{Aut}_w(\{x_{ij}\})$ and $\pi \notin \mathrm{Aut}_s(\{x_{ij}\})$.

**Step 1: $\pi \in \mathrm{Aut}_w(\{x_{ij}\})$.**
By Lemma 1(1), there exist signs $\varepsilon_a \in \{\pm 1\}$ ($a \in X$) such that $H_{g_0(a), g_0(b)} = \varepsilon_a \varepsilon_b H_{b, a}$ for all $a, b \in X$. Set $\omega_{i, j} := \varepsilon_i H_{i, j} \in \{\pm 1\}$ for $(i, j) \in X^2$. We verify that
$$\bigl(x_{\pi(i, j)}, x_{\pi(k, l)}\bigr) = \omega_{i, j} \omega_{k, l} \, \overline{(x_{i, j}, x_{k, l})} \qquad \text{for all } (i, j), (k, l) \in X^2.$$
For $s, t \in \{\pm 1\}$, let $\Phi(s, t) := -\frac{1}{2}(s + t) + \frac{\mathrm{i}}{2}(s - t) \in \{\pm 1, \pm \mathrm{i}\}$ be the factor in Lemma 3 (`lem.gram matrix`, eq. (1)). Observe that $\Phi(-s, -t) = -\Phi(s, t)$ and that for all $a, b, c, e \in \{\pm 1\}$,
$$\Phi(a c, b e) = a e \, \overline{\Phi(a b, c e)}.$$
Indeed, since $\overline{\Phi(u, v)} = -\frac{1}{2}(u + v) - \frac{\mathrm{i}}{2}(u - v) = \Phi(v, u)$, when $a e = +1$ (so $e = a$) we have $\Phi(ac, ba) = a\Phi(c, b) = a\overline{\Phi(b, c)} = \overline{\Phi(ab, ca)}$; when $a e = -1$ (so $e = -a$) we have $\Phi(ac, -ba) = a\bigl(-\frac{1}{2}(c - b) + \frac{\mathrm{i}}{2}(c + b)\bigr)$ while $-\overline{\Phi(ab, -ca)} = -a\bigl(-\frac{1}{2}(b - c) - \frac{\mathrm{i}}{2}(b + c)\bigr) = a\bigl(-\frac{1}{2}(c - b) + \frac{\mathrm{i}}{2}(c + b)\bigr)$.

Now check the four cases for $(i, j), (k, l) \in X^2$ using Lemma 3 (`lem.gram matrix`) and Theorem 2:
- **Diagonal ($(i, j) = (k, l)$):** Both sides equal $12 \in \mathbb{F}_p$ (since $\omega_{i, j}^2 = 1$).
- **Case I ($i \neq k$, $j \neq l$):** Here $g_0(j) \neq g_0(l)$ and $g_0(i) \neq g_0(k)$. Substituting $H_{g_0(a), g_0(b)} = \varepsilon_a \varepsilon_b H_{b, a}$ yields
  $$\begin{aligned}
  \bigl(x_{g_0(j), g_0(i)}, x_{g_0(l), g_0(k)}\bigr)
  &= 4\,\Phi\bigl(H_{g_0(j), g_0(i)} H_{g_0(j), g_0(k)},\; H_{g_0(l), g_0(i)} H_{g_0(l), g_0(k)}\bigr) \\
  &= 4\,\Phi\bigl(\varepsilon_i \varepsilon_k H_{i, j} H_{k, j},\; \varepsilon_i \varepsilon_k H_{i, l} H_{k, l}\bigr) \\
  &= 4\,\varepsilon_i \varepsilon_k H_{i, j} H_{k, l} \, \overline{\Phi(H_{i, j} H_{i, l},\; H_{k, j} H_{k, l})}
  = \omega_{i, j} \omega_{k, l} \, \overline{(x_{i, j}, x_{k, l})}.
  \end{aligned}$$
- **Case II ($i \neq k$, $j = l$):** Here $(x_{i, j}, x_{k, j}) = 4$ (Case II), whereas $\pi(i, j) = (g_0(j), g_0(i))$ and $\pi(k, j) = (g_0(j), g_0(k))$ share their first index and have distinct second indices, so Case III of Lemma 3 gives
  $$\bigl(x_{g_0(j), g_0(i)}, x_{g_0(j), g_0(k)}\bigr) = 4\, H_{g_0(j), g_0(i)} H_{g_0(j), g_0(k)} = 4 (\varepsilon_i H_{i, j})(\varepsilon_k H_{k, j}) = \omega_{i, j} \omega_{k, j} \, \overline{4}.$$
- **Case III ($i = k$, $j \neq l$):** Here $(x_{i, j}, x_{i, l}) = 4 H_{i, j} H_{i, l}$ (Case III), whereas $\pi(i, j) = (g_0(j), g_0(i))$ and $\pi(i, l) = (g_0(l), g_0(i))$ have distinct first indices and share their second index, so Case II of Lemma 3 gives
  $$\bigl(x_{g_0(j), g_0(i)}, x_{g_0(l), g_0(i)}\bigr) = 4 = (\varepsilon_i H_{i, j})(\varepsilon_i H_{i, l}) \cdot 4 H_{i, j} H_{i, l} = \omega_{i, j} \omega_{i, l} \, \overline{(x_{i, j}, x_{i, l})}.$$

Setting $y_{i, j} := \omega_{i, j} \overline{x_{\pi(i, j)}} \in L^d$ (componentwise conjugation on $L^d = \mathbb{F}_{p^2}^d$), we obtain
$$(y_{i, j}, y_{k, l}) = \omega_{i, j} \omega_{k, l} \overline{\bigl(x_{\pi(i, j)}, x_{\pi(k, l)}\bigr)} = (x_{i, j}, x_{k, l}) \qquad \text{for all } (i, j), (k, l) \in X^2.$$
Because both $\{x_{i, j}\}$ and $\{y_{i, j}\}$ span $L^d$ (Theorem 2 / Definition 1(d)), the identical argument as in Proposition 17(a) (`2025.06.25.tex`, lines 747–759) shows that $U(x_{i, j}) := y_{i, j}$ extends to a well-defined invertible linear map $U : L^d \to L^d$ preserving $(\cdot, \cdot)$ such that $x_{\pi(i, j)} = \omega_{i, j} \overline{U x_{i, j}}$ (with constant $\overline{\omega_{i, j}} \omega_{i, j} = 1$). By Definition 13(a), $\pi \in \mathrm{Aut}_w(\{x_{ij}\})$, so $\mathrm{Aut}_w(\{x_{ij}\}) = \mathrm{Aut}_s(\tilde{H})$.

**Step 2: $\pi \notin \mathrm{Aut}_s(\{x_{ij}\})$.**
Suppose for contradiction that $\pi \in \mathrm{Aut}_s(\{x_{ij}\})$. By Lemma 16 (`lem:omegas`) with $\gamma = \mathrm{id}$, there exist $\varepsilon \in \{\pm 1\}$ and $\mu_u \in \{\pm 1, \pm \mathrm{i}\}$ ($u \in X^2$) such that
$$\bigl(x_{\pi(u)}, x_{\pi(v)}\bigr) = \varepsilon \mu_u \overline{\mu_v} (x_u, x_v) \qquad \text{for all } u, v \in X^2.$$
For any three distinct indices $u, v, w \in X^2$, define the triple product $T(u, v, w) := (x_u, x_v)(x_v, x_w)(x_w, x_u) \in L$. Computing $T(\pi(u), \pi(v), \pi(w))$ in two ways—using the assumption above (with $|\mu_u|^2 = 1$ and $\varepsilon^3 = \varepsilon$) and using Step 1 (with $\omega_u^2 = 1$)—gives
$$\varepsilon \, T(u, v, w) = T\bigl(\pi(u), \pi(v), \pi(w)\bigr) = \overline{T(u, v, w)} \qquad \text{for all distinct } u, v, w \in X^2.$$
Now evaluate $T$ on two explicit triples (possible since $d \ge 20 \ge 3$):
1. Pick any three distinct elements $a, b, c \in X$ and take $u_1 = (a, a)$, $v_1 = (b, a)$, $w_1 = (c, a)$. By Case II of Lemma 3, each inner product equals $4$, so $T(u_1, v_1, w_1) = 64 \in \mathbb{F}_p^\times$ (nonzero since $p$ is odd). Thus $\overline{T(u_1, v_1, w_1)} = T(u_1, v_1, w_1)$, forcing $\varepsilon = +1$.
2. Pick any two distinct elements $a, b \in X$ and take $u_2 = (a, a)$, $v_2 = (a, b)$, $w_2 = (b, b)$. By Lemma 3:
   - $(x_{a, a}, x_{a, b}) = 4 H_{a, a} H_{a, b} = 4 H_{a, b}$ (Case III),
   - $(x_{a, b}, x_{b, b}) = 4$ (Case II),
   - $(x_{b, b}, x_{a, a}) = 4\,\Phi(H_{b, b} H_{b, a},\; H_{a, b} H_{a, a}) = 4\,\Phi(H_{b, a}, -H_{b, a}) = \pm 4\mathrm{i}$ (Case I, since $H_{a, a} = H_{b, b} = 1$ and $H_{a, b} = -H_{b, a}$).
   Hence $T(u_2, v_2, w_2) = \pm 64\mathrm{i}$. Since $p \equiv 3 \pmod 4$ is odd, $64\mathrm{i} \neq 0$ and $\overline{\pm 64\mathrm{i}} = -(\pm 64\mathrm{i})$, forcing $\varepsilon = -1$.

Since $1 \neq -1$ in $\mathbb{F}_p$, we have a contradiction. Thus $\pi \notin \mathrm{Aut}_s(\{x_{ij}\})$, and hence $\mathrm{Aut}_s(\{x_{ij}\}) = \iota(\mathrm{Aut}_w(H))$.

**Corollary (Infinitely many non-transitive SICs over finite fields).** For every prime $p \equiv 3 \pmod 4$ with $p \neq 7$, Dirichlet's theorem on primes in arithmetic progressions yields infinitely many primes $q > 11$ with $q \equiv 7 \pmod{4p}$ (so $q \equiv 3 \pmod 4$ and $p \mid (q - 7) = d - 8$); for $p = 7$, every odd prime power $q = 7^r$ with $r \ge 3$ likewise satisfies $q > 11$, $q \equiv 3 \pmod 4$, and $7 \mid (7^r - 7) = d - 8$. By Theorems 1 and 2, each such pair $(q, p)$ gives a SIC in $\mathbb{F}_{p^2}^{q+1}$ whose weak automorphism group $\mathrm{Aut}_w(\{x_{ij}\}) = \mathrm{Aut}_s(\tilde{H})$ has two orbits (of sizes $q + 1$ and $q(q + 1)$) and is therefore non-transitive. $\square$

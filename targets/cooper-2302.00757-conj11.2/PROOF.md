# Proof of Conjecture 11.2 of Cooper (arXiv:2302.00757v2)

**Theorem (Conjecture 11.2 of `arXiv:2302.00757v2`).** Let $\{T_{11}(n)\}_{n \ge 0}$ be the level-$11$ integer sequence defined by $T_{11}(0) = 1$, $T_{11}(-1) = T_{11}(-2) = 0$, and
$$(n+1)^3 T_{11}(n+1) = 2(2n+1)(5n^2+5n+2) T_{11}(n) - 8n(7n^2+1) T_{11}(n-1) + 22n(2n-1)(n-1) T_{11}(n-2).$$
Then for every integer $n \ge 1$ (and trivially $n = 0$):
1. $T_{11}(3n) \equiv T_{11}(n) + 3n \pmod{9}$;
2. $T_{11}(5n) \equiv T_{11}(n) \pmod{25}$ if and only if $5 \mid n$.

---

## 1. Modular Parametrization and Graded Ring Setup

By Cooper (`arXiv:2302.00757v2`, Section 5, lines 1611–1632, applying Theorem 3.1 / `\ref{interesting}`), setting
$$f(q) := \sum_{j,k \in \mathbb{Z}} q^{j^2+jk+3k^2}, \qquad U_1(q) := Z(q) = f(q)^2, \qquad V_1(q) := \eta(q)^2 \eta(q^{11})^2 = q \prod_{m=1}^{\infty} (1-q^m)^2 (1-q^{11m})^2,$$
and $X_1(q) := X(q) = V_1(q)/U_1(q)$, we have the power series identity in $\mathbb{Z}[[q]]$ ($q = e^{2\pi i \tau}$):
$$U_1(q) = \sum_{n=0}^{\infty} T_{11}(n)\, X_1(q)^n,$$
with $T_{11}(n) \in \mathbb{Z}$ for all $n \ge 0$.

**Lemma 1 (Modular forms on $\Gamma_0(11)$ and $\Gamma_0(11p)$).**
1. $U_1 \in M_2(\Gamma_0(11)) \cap \mathbb{Z}[[q]]$ and $V_1 \in S_2(\Gamma_0(11)) \cap \mathbb{Z}[[q]]$ (both with trivial character).
2. For any prime $p$, setting $U_p(q) := U_1(q^p)$ and $V_p(q) := V_1(q^p)$, we have $U_p, V_p \in M_2(\Gamma_0(11p)) \cap \mathbb{Z}[[q]]$ (with trivial character). Consequently, any homogeneous polynomial $F(U_1, V_1, U_p, V_p) \in \mathbb{Z}[U_1, V_1, U_p, V_p]$ of total degree $d$ lies in $M_{2d}(\Gamma_0(11p)) \cap \mathbb{Z}[[q]]$.
3. Since $U_1(q) = 1 + 4q + \cdots \in 1 + q\mathbb{Z}[[q]]$ and $V_1(q) = q - 2q^2 + \cdots \in q + q^2\mathbb{Z}[[q]]$, we have $X_1(q) \in q + q^2\mathbb{Z}[[q]]$. Therefore, for every integer $m \ge 1$, the substitution map $(\mathbb{Z}/m\mathbb{Z})[[X]] \to (\mathbb{Z}/m\mathbb{Z})[[q]]$, $A(X) \mapsto A(X_1(q))$, is injective.

*Proof.*
For (1), the binary quadratic form $Q(j,k) = j^2 + jk + 3k^2$ is positive definite of discriminant $-11$, with even Gram matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 6 \end{pmatrix}$ satisfying $\det A = 11$ and $11 A^{-1}$ even integral. By Schoeneberg's theorem on lattice theta series, $f(\tau) \in M_1(\Gamma_0(11), (\frac{\cdot}{11}))$, so $U_1 = f^2 \in M_2(\Gamma_0(11))$ has trivial character. (Equivalently, $\dim M_2(\Gamma_0(11)) = 2$ with basis $E_{2,11}(q) = \frac{11 P(q^{11}) - P(q)}{10}$ and $V_1(q)$, where $P(q) = 1 - 24\sum_{n\ge 1}\sigma_1(n)q^n$, and comparing $q^0, q^1, q^2$ coefficients gives $U_1 = E_{2,11} + \frac{8}{5}V_1$.) Also $\eta(\tau)^2 \eta(11\tau)^2$ has level $11$, weight $2$, and trivial character since $2(1+11) = 24$ and $1^2 \cdot 11^2$ is a square. Part (2) follows from the standard $V_p$-operator ($g(\tau) \mapsto g(p\tau) : M_k(\Gamma_0(N)) \to M_k(\Gamma_0(pN))$) and closure of $M_*(\Gamma_0(11p))$ under addition and multiplication. For (3), if $A(X) = \sum_{n \ge n_0} c_n X^n$ has $c_{n_0} \not\equiv 0 \pmod m$, then $[q^{n_0}] A(X_1(q)) = c_{n_0} \cdot 1^{n_0} \not\equiv 0 \pmod m$. $\square$

**Lemma 2 (Sturm's theorem).** Let $G \in M_k(\Gamma_0(N)) \cap \mathbb{Z}[[q]]$ and $m \ge 1$. If $[q^j] G \equiv 0 \pmod m$ for all $0 \le j \le B(k, N) := \lfloor \frac{k}{12} [\mathrm{SL}_2(\mathbb{Z}) : \Gamma_0(N)] \rfloor$, then $G \equiv 0 \pmod{m \mathbb{Z}[[q]]}$. (This is Sturm's congruence theorem, 1987, applied separately to each prime-power factor of $m$.) For $N = 11, 33, 55$ the subgroup index $[\mathrm{SL}_2(\mathbb{Z}) : \Gamma_0(N)] = N \prod_{\ell \mid N}(1 + 1/\ell)$ equals $12, 48, 72$, so:
- $B(k, 11) = k$,
- $B(k, 33) = 4k$,
- $B(k, 55) = 6k$.

---

## 2. Proof of Part (1): $T_{11}(3n) \equiv T_{11}(n) + 3n \pmod{9}$

Let $Z(X) := \sum_{n=0}^{\infty} T_{11}(n) X^n \in \mathbb{Z}[[X]]$.

**Step 2.1 (Mod-$3$ base congruence).**
Consider $U_1(q) - V_1(q) \in M_2(\Gamma_0(11)) \cap \mathbb{Z}[[q]]$. From $U_1 = E_{2,11} + \frac{8}{5} V_1$ and $E_{2,11}(q) = 1 + \frac{12}{5} \sum_{n \ge 1}(\sigma_1(n) - 11\sigma_1(n/11)) q^n$, we have in $\mathbb{Z}_{(3)}[[q]]$:
$$U_1(q) - V_1(q) = 1 + \frac{12}{5} \sum_{n \ge 1}(\sigma_1(n) - 11\sigma_1(n/11)) q^n + \frac{3}{5} V_1(q) \equiv 1 \pmod{3\mathbb{Z}_{(3)}[[q]]}.$$
(This also matches $Z(q) - V_1(q)$ modulo $3$ up to $q^2$, Sturm bound $B(2, 11) = 2$ once multiplied by a mod-$3$ level-1 form of weight $2$, or directly from the explicit $q$-series above.) Since $U_1(q) - V_1(q) = U_1(q)(1 - X_1(q))$, we get $(1 - X_1(q)) Z(X_1(q)) \equiv 1 \pmod 3$. By Lemma 1(3), $(1 - X) Z(X) \equiv 1 \pmod 3$ in $\mathbb{F}_3[[X]]$, i.e.,
$$T_{11}(n) \equiv 1 \pmod 3 \qquad \text{for all } n \ge 0.$$
Consequently, we may write $Z(X) = \frac{1}{1-X} + 3 F(X)$ with $F(X) = \sum_{n=0}^{\infty} f(n) X^n \in \mathbb{Z}[[X]]$, where $f(n) := \frac{T_{11}(n) - 1}{3} \in \mathbb{Z}$. Moreover, differentiating $Z(X) \equiv (1-X)^{-1} \pmod 3$ termwise gives
$$Z'(X) \equiv \frac{1}{(1-X)^2} \pmod 3.$$

**Step 2.2 ($p$-adic Taylor expansion at $p = 3$).**
Let $X_3(q) := X_1(q^3) = V_3(q)/U_3(q) \in q^3 \mathbb{Z}[[q]]$. By Fermat's Little Theorem on coefficients, $X_1(q)^3 \equiv X_3(q) \pmod{3\mathbb{Z}[[q]]}$, so $X_1(q)^3 = X_3(q) + 3 \Delta_3(q)$ for some $\Delta_3(q) \in q \mathbb{Z}[[q]]$. For every $n \ge 0$, expanding $(X_3(q) + 3\Delta_3(q))^n$ gives
$$(X_1(q)^3)^n \equiv X_3(q)^n + 3n \Delta_3(q) X_3(q)^{n-1} \pmod{9\mathbb{Z}[[q]]}.$$
Summing over $n \ge 0$ with integer coefficients $T_{11}(n)$ (which converges $q$-adically since $X_3, \Delta_3 \in q\mathbb{Z}[[q]]$) and substituting $Z'(X) \equiv (1-X)^{-2} \pmod 3$ gives
$$Z(X_1(q)^3) \equiv U_3(q) + \frac{X_1(q)^3 - X_3(q)}{(1 - X_3(q))^2} \pmod{9\mathbb{Z}[[q]]}.$$

**Step 2.3 (Weight-$30$ modular form congruence on $\Gamma_0(33)$).**
Define the polynomial $N_3(X) := X + 2X^2 + X^3 + X^4 + X^6 \in \mathbb{Z}[X]$ and consider the $\Gamma_0(33)$ relation
$$(1 - X_1(q)) U_1(q) - (1 - X_1(q)^3) \left( U_3(q) + \frac{X_1(q)^3 - X_3(q)}{(1 - X_3(q))^2} \right) - 3 \frac{N_3(X_1(q))}{(1 - X_1(q)^3)^2} \equiv 0 \pmod{9}.$$
To put every term in the same weight $k = 30$ without affecting validity modulo $9$, multiply the two weight-$0$ terms $\frac{X_1^3 - X_3}{(1-X_3)^2}$ and $3\frac{N_3(X_1)}{(1-X_1^3)^2}$ (both already divisible by $3$ in $\mathbb{Z}[[q]]$) by $U_1(q) - V_1(q) \in M_2(\Gamma_0(11))$, which satisfies $U_1 - V_1 \equiv 1 \pmod{3\mathbb{Z}[[q]]}$ by Step 2.1, and clear denominators by multiplying by
$$D_3(q) := U_1(q)^6 (U_1(q)^3 - V_1(q)^3)^2 (U_3(q) - V_3(q))^2 \in M_{28}(\Gamma_0(33)) \cap \mathbb{Z}[[q]].$$
Explicitly, define $G_3 \in M_{30}(\Gamma_0(33)) \cap \mathbb{Z}[[q]]$ by
$$G_3 := (U_1 - V_1) D_3 - (U_1^3 - V_1^3)^3 U_3 U_1^3 (U_3 - V_3)^2 - (U_1^3 - V_1^3)^3 (V_1^3 U_3 - U_1^3 V_3) U_3 (U_1 - V_1) - 3\,\widetilde{N}_3(U_1, V_1)(U_1 - V_1) U_1^6 (U_3 - V_3)^2,$$
where $\widetilde{N}_3(U_1, V_1) = V_1 U_1^5 + 2 V_1^2 U_1^4 + V_1^3 U_1^3 + V_1^4 U_1^2 + V_1^6$.
By Lemma 2, $B(30, 33) = 4 \cdot 30 = 120$. Direct exact $q$-series expansion (`verify.py`) shows $[q^j] G_3 \equiv 0 \pmod 9$ for all $0 \le j \le 130$ (exceeding $120$), so $G_3 \equiv 0 \pmod{9\mathbb{Z}[[q]]}$ by Sturm's theorem. Since $D_3(0) = 1$, $D_3$ is a unit in $\mathbb{Z}[[q]]$, and by Step 2.2 we deduce
$$(1 - X_1(q)) Z(X_1(q)) - (1 - X_1(q)^3) Z(X_1(q)^3) \equiv 3 \frac{N_3(X_1(q))}{(1 - X_1(q)^3)^2} \pmod{9\mathbb{Z}[[q]]}.$$
Wait: clearing $(1 - X_1(q)^3)^2$ and applying Lemma 1(3) yields in $(\mathbb{Z}/9\mathbb{Z})[[X]]$:
$$(1 - X) Z(X) - (1 - X^3) Z(X^3) \equiv 3 \frac{X + 2X^2 + X^3 + X^4 + X^6}{(1 - X^3)^2} \pmod 9.$$

**Step 2.4 (Coefficient extraction).**
Substituting $Z(X) = (1-X)^{-1} + 3 F(X)$ gives $(1-X)Z(X) - (1-X^3)Z(X^3) = 3((1-X)F(X) - (1-X^3)F(X^3))$, so dividing by $3$ and dividing by $1-X$ in $\mathbb{F}_3[[X]]$ gives
$$F(X) - (1 + X + X^2) F(X^3) \equiv \frac{X + 2X^2 + X^3 + X^4 + X^6}{(1-X)(1-X^3)^2} \pmod 3.$$
A direct polynomial check in $\mathbb{F}_3[X]$ gives $(1 - X)(X^3 - X^5 + X(1 - X^3)) \equiv X + 2X^2 + X^3 + X^4 + X^6 \pmod 3$, hence
$$F(X) - (1 + X + X^2) F(X^3) \equiv \frac{X^3}{(1-X^3)^2} + \frac{X}{1 - X^3} - \frac{X^5}{(1-X^3)^2} \equiv \sum_{k=0}^{\infty} \bigl( k X^{3k} + X^{3k+1} - k X^{3k+2} \bigr) \pmod 3.$$
Reading off $[X^{3n}]$ for any $n \ge 0$ gives $f(3n) - f(n) \equiv n \pmod 3$, and multiplying by $3$ yields $T_{11}(3n) - T_{11}(n) \equiv 3n \pmod 9$. This proves Part (1).

---

## 3. Proof of Part (2): $T_{11}(5n) \equiv T_{11}(n) \pmod{25} \iff 5 \mid n$

Let $P_5(X) := 1 + 4X + 3X^2 + 3X^3 + 4X^4 = \sum_{r=0}^4 (T_{11}(r) \bmod 5) X^r$, and define the degree-$24$ polynomial
$$R_{25}(X) := \sum_{m=0}^{24} r_m X^m \in \mathbb{Z}[X], \qquad r_m := \frac{(T_{11}(m) - P_5[m \bmod 5]\, T_{11}(\lfloor m/5 \rfloor)) \bmod 25}{5}$$
(computed explicitly in `verify.py` as $R_{25}(X) = 3X^3 + X^5 + 2X^6 + X^7 + 2X^8 + 4X^9 + 3X^{10} + 4X^{12} + 4X^{13} + X^{14} + 4X^{15} + X^{16} + X^{17} + 4X^{18} + 4X^{19} + 2X^{20} + 2X^{21} + 4X^{22} + 2X^{23} + X^{24}$). Denote by $\widetilde{P}_5(U, V) := U^4 + 4VU^3 + 3V^2U^2 + 3V^3U + 4V^4$, $\widetilde{P}_5'(U, V) := 4U^3 + V U^2 + 4V^2 U + V^3$, and $\widetilde{R}_{25}(U, V) := \sum_{m=0}^{24} r_m V^m U^{24-m}$ their homogenizations.

**Step 3.1 (Mod-$5$ Lucas congruence).**
Let $G_{5,\text{luc}} := U_1^5 - \widetilde{P}_5(U_1, V_1) U_5 \in M_{10}(\Gamma_0(55)) \cap \mathbb{Z}[[q]]$.
By Lemma 2, $B(10, 55) = 6 \cdot 10 = 60$. Direct $q$-series computation (`verify.py`) confirms $[q^j] G_{5,\text{luc}} \equiv 0 \pmod 5$ for all $0 \le j \le 80$, so $G_{5,\text{luc}} \equiv 0 \pmod{5\mathbb{Z}[[q]]}$. Since $U_1(0) = 1$, $U_1$ is a unit in $\mathbb{Z}[[q]]$. Because $X_1(q)^5 \equiv X_5(q) \pmod{5\mathbb{Z}[[q]]}$ where $X_5(q) := X_1(q^5) = V_5/U_5$, we have $Z(X_1(q)^5) \equiv Z(X_5(q)) = U_5(q) \pmod 5$. Thus
$$Z(X_1(q)) = U_1(q) \equiv P_5(X_1(q))\, U_5(q) \equiv P_5(X_1(q))\, Z(X_1(q)^5) \pmod{5\mathbb{Z}[[q]]}.$$
By Lemma 1(3), $Z(X) \equiv P_5(X) Z(X^5) \pmod{5\mathbb{Z}[[X]]}$. Consequently:
1. $T_{11}(5k + r) \equiv T_{11}(r) T_{11}(k) \pmod 5$ for all $k \ge 0$ and $0 \le r \le 4$. Since $T_{11}(0..4) \equiv 1, 4, 3, 3, 4 \pmod 5$ are all nonzero modulo $5$, induction on $k$ gives **$T_{11}(k) \not\equiv 0 \pmod 5$ for all $k \ge 0$**.
2. Differentiating $Z(X) \equiv P_5(X) Z(X^5) \pmod 5$ in $\mathbb{F}_5[[X]]$ gives $Z'(X) \equiv P_5'(X) Z(X^5) \equiv \frac{P_5'(X)}{P_5(X)} Z(X) \pmod 5$ (as $P_5(0) = 1$).

**Step 3.2 ($p$-adic Taylor expansion at $p = 5$).**
Write $X_1(q)^5 = X_5(q) + 5\Delta_5(q)$ with $\Delta_5(q) \in q\mathbb{Z}[[q]]$. For every $n \ge 0$, $(X_5(q) + 5\Delta_5(q))^n \equiv X_5(q)^n + 5n\Delta_5(q) X_5(q)^{n-1} \pmod{25\mathbb{Z}[[q]]}$. Summing over $n \ge 0$ and using Step 3.1(2) at $X = X_5(q)$ gives
$$Z(X_1(q)^5) \equiv U_5(q) + (X_1(q)^5 - X_5(q))\, \frac{P_5'(X_5(q))}{P_5(X_5(q))}\, U_5(q) \pmod{25\mathbb{Z}[[q]]}.$$

**Step 3.3 (Weight-$66$ modular form congruence on $\Gamma_0(55)$).**
Define $G_5 \in M_{66}(\Gamma_0(55)) \cap \mathbb{Z}[[q]]$ by
$$G_5 := U_1^{25} U_5^4 \widetilde{P}_5(U_5, V_5) - \widetilde{P}_5(U_1, V_1) U_1^{20} U_5^5 \widetilde{P}_5(U_5, V_5) - \widetilde{P}_5(U_1, V_1) (V_1^5 U_5 - U_1^5 V_5) \widetilde{P}_5'(U_5, V_5) U_1^{15} U_5^5 - 5\, \widetilde{R}_{25}(U_1, V_1) U_5^9.$$
By Lemma 2, $B(66, 55) = 6 \cdot 66 = 396$. Direct exact $q$-series expansion (`verify.py`) confirms $[q^j] G_5 \equiv 0 \pmod{25}$ for all $0 \le j \le 400$ (exceeding $396$), so $G_5 \equiv 0 \pmod{25\mathbb{Z}[[q]]}$ by Sturm's theorem. Dividing by the unit $D_5 := U_1^{24} U_5^4 \widetilde{P}_5(U_5, V_5) \in 1 + q\mathbb{Z}[[q]]$ and using Step 3.2 yields
$$Z(X_1(q)) - P_5(X_1(q)) Z(X_1(q)^5) \equiv 5 R_{25}(X_1(q))\, \frac{U_5(q)}{P_5(X_5(q))} \pmod{25\mathbb{Z}[[q]]}.$$
By Step 3.1 evaluated at $X = X_5(q)$, $\frac{U_5(q)}{P_5(X_5(q))} = \frac{Z(X_5(q))}{P_5(X_5(q))} \equiv Z(X_5(q)^5) \equiv Z(X_1(q)^{25}) \pmod{5\mathbb{Z}[[q]]}$. Multiplying by $5 R_{25}(X_1(q))$ and applying Lemma 1(3) gives the exact power series identity in $(\mathbb{Z}/25\mathbb{Z})[[X]]$:
$$Z(X) \equiv P_5(X)\, Z(X^5) + 5 R_{25}(X)\, Z(X^{25}) \pmod{25}.$$

**Step 3.4 (Coefficient extraction).**
Write any positive integer $n = 5k + r$ with $k \ge 0$ and $0 \le r \le 4$. Reading off $[X^{5n}] = [X^{25k + 5r}]$ on both sides (since $\deg P_5 = 4 < 5$ and $\deg R_{25} = 24 < 25$):
$$T_{11}(5n) \equiv P_5[0]\, T_{11}(n) + 5 R_{25}[5r]\, T_{11}(k) = T_{11}(n) + 5\, r_{5r}\, T_{11}(k) \pmod{25}.$$
By Step 3.1(1), $T_{11}(k) \not\equiv 0 \pmod 5$ for all $k \ge 0$, while $(r_0, r_5, r_{10}, r_{15}, r_{20}) = (0, 1, 3, 4, 2)$. Therefore $5\, r_{5r}\, T_{11}(k) \equiv 0 \pmod{25}$ if and only if $r = 0$, i.e., $5 \mid n$. This proves Part (2) and completes the proof of Conjecture 11.2. $\square$

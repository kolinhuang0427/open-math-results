# Proof: $\mathsf{IOpen} + (\mathrm{Exp})$ is Conservative Over $\mathsf{IOpen}$

**Target:** Question 3.5(1) (and consequently Question 3.5(2)) of Konstantin Kovalyov, *Some conservativity results for weak arithmetic theories in a language with exponentiation*, `arXiv:2611.32205v1` (`math.LO`, Section 3).

**Claim:** $\mathsf{IOpen} + (\mathrm{Exp})$ is **conservative** over $\mathsf{IOpen}$ (with respect to all first-order $\mathcal{L}_{\mathrm{OSR}}$-sentences). Consequently, the $\mathcal{L}_{\mathrm{OSR}}$-fragment of $\mathsf{IOpen} + (\mathrm{Exp})$ is $\mathsf{IOpen}$ itself.

---

## 1. Reduction to Finite Linear Games via Recursive Saturation

Let $\mathcal{M}_0^+ \models \mathsf{IOpen}$ be any model of $\mathsf{IOpen}$, and let $T^* := \mathrm{Th}_{\mathcal{L}_{\mathrm{OSR}}}(\mathcal{M}_0^+)$. To prove conservativity, it suffices to show that $T^* + (\mathrm{Exp})$ is consistent.

Since $T^*$ is a complete consistent theory in the finite language $\mathcal{L}_{\mathrm{OSR}} = (+, \cdot, 0, 1, \leq)$, it admits a **countable recursively saturated** model $\mathcal{M}^+ \models T^*$. We will construct an expansion $(\mathcal{M}^+, \exp) \models \mathsf{IOpen} + (\mathrm{Exp})$ directly on $\mathcal{M}^+$.

For integers $n \ge 1$ and $M \ge 1$, define the $n$-round game $G_{n, M}(\mathcal{M}^+)$ between Challenger and Exp-er:
- In round $i \in \{1, \dots, n\}$, Challenger picks $a_i \in M^+$, and Exp-er responds with $b_i \in M^{>0}$.
- Exp-er wins the play $(a_1, b_1, \dots, a_n, b_n)$ iff for every coefficient tuple $\vec{c} = (c_0, c_1, \dots, c_n) \in [-M, M]^{n+1}$, writing
  $$L_+(\vec{a}) := \sum_{c_i > 0} c_i a_i + \max(0, c_0), \qquad L_-(\vec{a}) := \sum_{c_i < 0} (-c_i) a_i + \max(0, -c_0),$$
  $$P_+(\vec{b}) := 2^{\max(0, c_0)} \prod_{c_i > 0} b_i^{c_i}, \qquad P_-(\vec{b}) := 2^{\max(0, -c_0)} \prod_{c_i < 0} b_i^{-c_i},$$
  the winning condition $\mathrm{Win}_{n, M}(\vec{a}, \vec{b})$ holds:
  1. if $L_+(\vec{a}) = L_-(\vec{a})$, then $P_+(\vec{b}) = P_-(\vec{b})$;
  2. if $L_+(\vec{a}) > L_-(\vec{a})$, then there exists $z \in M^{>0}$ such that $z \cdot P_-(\vec{b}) = P_+(\vec{b})$ and $z + L_-(\vec{a}) > L_+(\vec{a})$ (equivalently, in the fraction field of the discretely ordered ring $\mathcal{M}$, $P_+(\vec{b}) / P_-(\vec{b}) \in M^+$ and $P_+(\vec{b}) / P_-(\vec{b}) > L_+(\vec{a}) - L_-(\vec{a})$).

Notice that $\mathrm{Win}_{n, M}(\vec{a}, \vec{b})$ is a finite $\mathcal{L}_{\mathrm{OSR}}$-formula, computable uniformly in $(n, M)$. For $0 \le k \le n$, let $\sigma^k_{n, M}(a_1, b_1, \dots, a_k, b_k)$ denote the $\mathcal{L}_{\mathrm{OSR}}$-formula
$$\forall a_{k+1} \in M^+\; \exists b_{k+1} \in M^{>0} \cdots \forall a_n \in M^+\; \exists b_n \in M^{>0}\;\; \mathrm{Win}_{n, M}(a_1, \dots, a_n, b_1, \dots, b_n),$$
expressing that Exp-er has a winning strategy in the remaining $n - k$ rounds of $G_{n, M}(\mathcal{M}^+)$ from $(a_1, b_1, \dots, a_k, b_k)$. Note the monotonicity property: if $n' \ge n$ and $M' \ge M$, then $\sigma^k_{n', M'}$ implies $\sigma^k_{n, M}$ (by allowing Challenger's extra moves $a_{n+1} = \dots = a_{n'} = 0$ and restricting $\vec{c}$ to $c_j = 0$ for $j > n$ and $|c_i| \le M$).

**Lemma 1.** *If $\mathcal{M}^+ \models \sigma^0_{n, M}$ for all $n, M \ge 1$, then $\mathcal{M}^+$ expands to a model $(\mathcal{M}^+, \exp) \models \mathsf{IOpen} + (\mathrm{Exp})$.*

*Proof.* Fix an injective enumeration (bijection) $M^+ = \{a_1, a_2, a_3, \dots\}$. By induction on $k = 1, 2, \dots$, suppose $b_1, \dots, b_{k-1} \in M^{>0}$ have been chosen so that $\mathcal{M}^+ \models \sigma^{k-1}_{n, M}(a_1, b_1, \dots, a_{k-1}, b_{k-1})$ for all $n \ge \max(1, k-1)$ and $M \ge 1$. Consider the recursive $\mathcal{L}_{\mathrm{OSR}}$-type in one variable $x$ over the finite tuple of parameters $(a_1, b_1, \dots, a_{k-1}, b_{k-1}, a_k)$:
$$\Gamma_k(x) := \{ x > 0 \} \cup \big\{ \sigma^k_{n, M}(a_1, b_1, \dots, a_{k-1}, b_{k-1}, a_k, x) \;\big|\; n \ge k,\; M \ge 1 \big\}.$$
By monotonicity in $(n, M)$, any finite subset of $\Gamma_k(x)$ is implied by $\{x > 0, \sigma^k_{n^*, M^*}(\dots, a_k, x)\}$ for sufficiently large $n^* \ge k, M^* \ge 1$. Since $\mathcal{M}^+ \models \sigma^{k-1}_{n^*, M^*}(a_1, b_1, \dots, a_{k-1}, b_{k-1})$, instantiating the universal quantifier $\forall a_k$ gives $\mathcal{M}^+ \models \exists x > 0\; \sigma^k_{n^*, M^*}(\dots, a_k, x)$. Hence $\Gamma_k(x)$ is finitely satisfiable in $\mathcal{M}^+$. By recursive saturation of $\mathcal{M}^+$, there exists $b_k \in M^{>0}$ realizing $\Gamma_k(x)$.

Define $\exp : M^+ \to M^+$ by $\exp(a_k) := b_k$ for all $k \ge 1$. Then:
- Taking $k$ with $a_k = 1$ and $(c_k = 1, c_0 = -1)$ in $\mathrm{Win}_{k, 1}$ gives $a_k - 1 = 0 \implies \exp(1) = b_k = 2$.
- For any $x, y \in M^+$, pick $i, j, \ell$ with $a_i = x, a_j = y, a_\ell = x + y$, and let $n = \max(i, j, \ell)$. Then taking $(c_i = 1, c_j = 1, c_\ell = -1)$ when $i, j, \ell$ are pairwise distinct, $(c_i = 2, c_\ell = -1)$ when $i = j \ne \ell$, $(c_j = 1)$ when $i = \ell \ne j$ (so $y = 0 \implies b_j = \exp(0) = 1$ by the next bullet), $(c_i = 1)$ when $j = \ell \ne i$ (so $x = 0 \implies b_i = \exp(0) = 1$), and $(c_i = 1)$ when $i = j = \ell$ ($x = y = 0 \implies b_i = 1$) in $\mathrm{Win}_{n, 2}$ gives $\exp(x)\exp(y) = \exp(x+y)$.
- For any $x = a_k \in M^+$, taking $(c_k = 1)$ in $\mathrm{Win}_{k, 1}$ gives: if $x = 0$, $b_k = 1 > 0$; if $x > 0$, $b_k > x$.

Thus $(\mathcal{M}^+, \exp) \models \mathsf{IOpen} + (\mathrm{Exp})$. $\square$

---

## 2. Explicit Winning Strategy in $G_{n, M}(\mathcal{M}^+)$

Fix $n \ge 1$ and $M \ge 1$, and let $\mathcal{M}^+ \models \mathsf{IOpen}$ (in fact, $\mathcal{M}^+ \models \mathbb{Z}\text{-}\mathsf{DOSR}$ suffices), with discretely ordered ring $\mathcal{M}$ and fraction field $\mathcal{F}(\mathcal{M})$. We work inside $\mathcal{M}$ using standard signed linear combinations $L(\vec{a}) := c_0 + \sum_{i=1}^k c_i a_i \in M$.

### 2.1. Standard Parameters

Define the following standard positive integers depending only on $(n, M)$:
- **Coefficient bounds:** $B_n := M$, and $B_{k-1} := 2 B_k^2 + B_k$ for $k = n, n-1, \dots, 2$.
- **Standard-cut thresholds:** $N_n := M$, and $N_{k-1} := 2 B_k N_k + B_{k-1}$ for $k = n, n-1, \dots, 2$.
- **Divisibility step factors:** $F_{n+1} := 1$, and $F_k := 2 (B_k!)^2 F_{k+1}$ for $k = n, n-1, \dots, 1$.
- **Congruence moduli:** $\mu_n := B_n!$, and $\mu_{k-1} := B_k! \cdot \mu_k$ for $k = n, n-1, \dots, 1$. (Set $\mu_0 := B_1! \cdot \mu_1$.)
- **Exponent cap $K$:** Recursively set $E_1 := F_1$, $E_k := B_k \cdot k \cdot E_{k-1} + F_k$, and $E_{0, 1} := \mu_0 + N_1$, $E_{0, k} := (3 B_1)^k N_1 + B_k + B_k \cdot k \cdot E_{0, k-1} + \mu_0$. Put
  $$K := n \cdot M \cdot \max(E_n, E_{0, n}) + M + 10.$$

### 2.2. Bases, Thresholds, and Inductive Invariant

Exp-er maintains a list of bases $V_1, \dots, V_s \in M^{>0}$ ($0 \le s \le k$ at round $k$), associated scale terms $S_1, \dots, S_s \in M^{>0}$, and for each $i \in \{1, \dots, k\}$ an integer exponent vector $\vec{e}_i = (e_{i, 0}, e_{i, 1}, \dots, e_{i, s}) \in \mathbb{Z}^{s+1}$ defining
$$b_i := 2^{e_{i, 0}} \prod_{r=1}^s V_r^{e_{i, r}} \in \mathcal{F}(\mathcal{M})^{>0}.$$
For each $r \in \{1, \dots, s\}$ and $j \in \{1, \dots, n\}$, define the round-$j$ scale threshold
$$T_{r, j} := (4 B_1)^j S_r + (4 B_1)^{j+1} N_1 \in M^{>0}.$$
Note that if $S_r > T_{r-1, k_r}$ when $V_r$ is created at round $k_r \ge 1$, then:
- for all $j \in \{2, \dots, n\}$, $T_{r, j} - B_j N_j > T_{r, j-1}$ (since $(4B_1 - 1) T_{r, j-1} \ge 3 B_1 (4 B_1)^j N_1 > B_j N_j$);
- for all $j \in \{1, \dots, n\}$, $T_{r, j} > T_{r-1, j}$ (since $S_r > T_{r-1, k_r} > S_{r-1}$ and $k_r \ge 1$), and $T_{1, j} > N_j$.

Whenever a new base $V_{s+1}$ is created at round $k$ with $S_{s+1} := B_k \sum_{i=1}^k a_i + B_k + 1$, we set
$$U_{s+1} := (4 B_1)^{n+1} S_{s+1} + (4 B_1)^{n+2} N_1 + 1 > T_{s+1, n}, \qquad V_{s+1} := U_{s+1} \cdot 2^K \prod_{j=1}^s V_j^K \in M^{>0},$$
and pad earlier exponent vectors with $e_{i, s+1} := 0$ for $i < k$.

**Inductive Invariant $\mathcal{I}_k$ (after round $k \le n$):**
For all $i \le k$, $|e_{i, r}| \le E_k$ ($1 \le r \le s$), $|e_{i, 0}| \le E_{0, k}$, $F_{k+1} \mid e_{i, r}$ ($1 \le r \le s$), and $e_{i, 0} \equiv a_i \pmod{\mu_k}$ in $\mathcal{M}$. Moreover, for every tuple $(c_0, c_1, \dots, c_k) \in [-B_k, B_k]^{k+1}$, letting $L(\vec{a}) := c_0 + \sum_{i=1}^k c_i a_i$ and $v_r := \sum_{i=1}^k c_i e_{i, r}$ ($1 \le r \le s$), $v_0 := c_0 + \sum_{i=1}^k c_i e_{i, 0}$:
1. *(Small standard exactness)* If $|L(\vec{a})| \le N_k$, then $v_1 = \dots = v_s = 0$ and $v_0 = L(\vec{a})$ (as integers).
2. *(Lexicographic positivity and scale dominance)* If $L(\vec{a}) > N_k$, then either:
   - $v_1 = \dots = v_s = 0$, $L(\vec{a}) \in \mathbb{Z}_{>0}$ with $L(\vec{a}) \le (3 B_1)^k N_1$, and $v_0 = L(\vec{a})$; or
   - letting $r \in \{1, \dots, s\}$ be the largest index with $v_r \ne 0$, we have $v_r \ge 1$ and $L(\vec{a}) \le T_{r, k}$.
3. *(Upper cap)* If $s \ge 1$, then $B_k \sum_{i=1}^k a_i + B_k \le T_{s, k}$; if $s = 0$, then $B_k \sum_{i=1}^k a_i + B_k \le N_k$.

*(Remark: Notice that $\mathcal{I}_k$ holds trivially at $k = 0$ with $s = 0$, and at $k = n$, $\mathcal{I}_n$ implies $\mathrm{Win}_{n, M}$: for every $(c_0, \dots, c_n) \in [-M, M]^{n+1}$ with $L(\vec{a}) \ge 0$, if $L(\vec{a}) = 0$ then $v_0 = \dots = v_s = 0$ so $P_+(\vec{b}) = P_-(\vec{b})$. If $L(\vec{a}) > 0$ and all $v_r = 0$ ($r \ge 1$), then $v_0 = L(\vec{a}) > 0$, so $P_+(\vec{b}) / P_-(\vec{b}) = 2^{L(\vec{a})} \in M^{>0}$ and $> L(\vec{a})$. If $L(\vec{a}) > 0$ has highest nonzero $v_r \ge 1$ ($r \ge 1$), then since $K > |v_0|, |v_1|, \dots, |v_{r-1}|$ and $V_r = U_r \cdot 2^K \prod_{j<r} V_j^K$, one factor of $V_r$ clears all negative powers of $2, V_1, \dots, V_{r-1}$ while leaving $U_r > T_{r, n} \ge L(\vec{a})$, so $P_+(\vec{b}) / P_-(\vec{b}) \in M^{>0}$ and $> L(\vec{a})$. Note also that $b_i \in M^{>0}$ itself follows by taking $L(\vec{a}) = a_i \ge 0$.)*

### 2.3. Construction at Round $k$ ($1 \le k \le n$)

Given $\mathcal{I}_{k-1}$ and Challenger's move $a_k \in M^+$:

**Step 1 (Scale check).** Let $S_{\mathrm{curr}} := B_k \sum_{i=1}^k a_i + B_k + 1$.
- If $s = 0$ and $S_{\mathrm{curr}} > N_k + 1$ (i.e. $B_k \sum a_i + B_k > N_k$), or if $s \ge 1$ and $B_k \sum_{i=1}^k a_i + B_k > T_{s, k}$: create $V_{s+1}$ with $S_{s+1} := S_{\mathrm{curr}}$ as in Section 2.2, and increment $s \leftarrow s + 1$.
  - Notice that if $s_{\mathrm{old}} \ge 1$ and $V_{s+1}$ is created at round $k$ (so $k \ge 2$), then since $B_{k-1} \sum_{i<k} a_i + B_{k-1} \le T_{s_{\mathrm{old}}, k-1}$, we have $B_k a_k > (4B_1 - 1) T_{s_{\mathrm{old}}, k-1} \ge 3 B_1 (B_{k-1} \sum_{i<k} a_i + B_{k-1})$, hence $a_k > B_k \sum_{i<k} a_i + B_k + N_k$; thus no tuple with $c_k < 0$ satisfies $L(\vec{a}) \ge -N_k$.
  - If instead $s_{\mathrm{old}} = 0$ and $V_1$ is created at round $k$, then either $k = 1$ (so $\sum_{i<k} a_i = 0$) or by $\mathcal{I}_{k-1}(3)$ we have $B_{k-1} \sum_{i<k} a_i + B_{k-1} \le N_{k-1}$, whence $B_k \sum_{i<k} a_i \le \frac{B_k}{B_{k-1}}(N_{k-1} - B_{k-1}) = \frac{2 B_k^2 N_k}{2B_k^2 + B_k} < N_k$, so $B_k \sum_{i<k} a_i \le N_k - 1$. Consequently, if round $k$ proceeds to Step 3 (unpinned, so $a_k \ge N_k + 1$ and $B_k \le N_k$), every tuple with $c_k \le -1$ satisfies $L(\vec{a}) \le B_k + (N_k - 1) - (N_k + 1) = B_k - 2 < N_k$ (and similarly $\le B_1 - (N_1 + 1) < N_1$ when $k = 1$), so it cannot belong to $\mathcal{T}_k$.

**Step 2 (Pinned case).** Let $\mathcal{T}_k$ be the finite set of tuples $(c_0, c_1, \dots, c_k) \in [-B_k, B_k]^{k+1}$ with $c_k \ne 0$ and $L(\vec{a}) \ge 0$ (covering all $L(\vec{a}) < 0$ by negation). Note that any tuple with $c_k = 0$ does not depend on round $k$ (for $k=1$, $L = c_0 \in [-B_1, B_1] \subseteq [-N_1, N_1]$ gives $v_0 = c_0$ and $v_r = 0$; for $k \ge 2$, it inherits $\mathcal{I}_k$ directly from $\mathcal{I}_{k-1}$ because $B_k \le B_{k-1}$, $N_k \le N_{k-1}$, $T_{r, k-1} < T_{r, k}$, $(3 B_1)^{k-1} N_1 < (3 B_1)^k N_1$, and $e_{i, s} = 0$ for $i < k$ on any newly created base).

Suppose there exists $(c_0^{(1)}, \dots, c_k^{(1)}) \in \mathcal{T}_k$ such that $L_1(\vec{a}) = d_1 \in [0, N_k]$. Set:
$$e_{k, r} := \frac{-\sum_{i=1}^{k-1} c_i^{(1)} e_{i, r}}{c_k^{(1)}} \quad (1 \le r \le s), \qquad e_{k, 0} := \frac{d_1 - c_0^{(1)} - \sum_{i=1}^{k-1} c_i^{(1)} e_{i, 0}}{c_k^{(1)}}.$$
- *Integrality & bounds:* For $r \ge 1$, $F_k = 2(B_k!)^2 F_{k+1} \mid e_{i, r}$ ($i < k$, empty sum $0$ when $k=1$) and $|c_k^{(1)}| \le B_k \mid B_k!$, so $e_{k, r} \in \mathbb{Z}$ and $F_{k+1} \mid e_{k, r}$, with $|e_{k, r}| \le B_k k E_{k-1} \le E_k$ (for $k=1$, $e_{1,r} = 0$). For $r = 0$, $e_{i, 0} \equiv a_i \pmod{\mu_{k-1}}$ for $i < k$ (vacuous at $k=1$) implies $d_1 - c_0^{(1)} - \sum_{i<k} c_i^{(1)} e_{i, 0} \equiv c_k^{(1)} a_k \pmod{\mu_{k-1}}$; since $c_k^{(1)} \mid B_k! \mid \mu_{k-1}$ and $\mu_{k-1} / B_k! = \mu_k$ (and for $k = 1$, $d_1 - c_0^{(1)} = c_1^{(1)} a_1$ is already exact in $\mathcal{M}$, so $e_{1, 0} = a_1 \in \mathbb{Z}$), we get $e_{k, 0} \in \mathbb{Z}$ and $e_{k, 0} \equiv a_k \pmod{\mu_k}$, with $|e_{k, 0}| \le E_{0, k}$.
- *Verification of $\mathcal{I}_k$:*
  - *Base case $k = 1$:* If $k = 1$ is pinned via $c_0^{(1)} + c_1^{(1)} a_1 = d_1 \in [0, N_1]$ ($c_1^{(1)} \ne 0$), then $a_1 \in \mathbb{Z}_{\ge 0}$ with $a_1 \le N_1 + B_1$, $e_{1, r} = 0$ ($1 \le r \le s$), and $e_{1, 0} = a_1 \le N_1 + B_1 \le \mu_0 + N_1 = E_{0, 1}$ (since $B_1 \le B_1! \le \mu_0$). Hence every $(c_0, c_1) \in [-B_1, B_1]^2$ has $v_r(L) = 0$ ($r \ge 1$), $v_0(L) = L(\vec{a}) \in \mathbb{Z}$, and when $L(\vec{a}) > N_1$ we have $L(\vec{a}) \le B_1 + B_1(N_1 + B_1) = B_1(N_1 + B_1 + 1) \le 3 B_1 N_1 = (3 B_1)^1 N_1$ (since $1 \le B_1 \le N_1$).
  - *Inductive step $k \ge 2$:* For any $(c_0, \dots, c_k) \in \mathcal{T}_k$, eliminate $a_k$ to form $L^*(\vec{a}) := c_k^{(1)} L(\vec{a}) - c_k L_1(\vec{a}) = c_k^{(1)} L(\vec{a}) - c_k d_1$ (wlog $c_k^{(1)} > 0$ by negating $L_1$ if needed, which replaces $d_1$ by $-d_1 \in [-N_k, N_k]$). Its coefficients lie in $[-2B_k^2, 2B_k^2] \subseteq [-B_{k-1}, B_{k-1}]$, and $v_r(L^*) = c_k^{(1)} v_r(L)$ ($r \ge 1$), $v_0(L^*) = c_k^{(1)} v_0(L) - c_k d_1$.
    - If $|L(\vec{a})| \le N_k$, then $|L^*(\vec{a})| \le 2 B_k N_k \le N_{k-1}$, so $\mathcal{I}_{k-1}$ yields $v_r(L^*) = 0$ ($r \ge 1$) and $v_0(L^*) = L^*(\vec{a})$, whence $v_r(L) = 0$ ($r \ge 1$) and $v_0(L) = L(\vec{a})$.
    - If $L(\vec{a}) > N_k$ and $L^*(\vec{a}) \le N_{k-1}$, note also $L^*(\vec{a}) = c_k^{(1)} L(\vec{a}) - c_k d_1 > N_k - B_k N_k > -N_{k-1}$, so $|L^*(\vec{a})| \le N_{k-1}$. Thus $\mathcal{I}_{k-1}$ yields $L^*(\vec{a}) \in \mathbb{Z}$, $v_r(L) = 0$ ($r \ge 1$), and $v_0(L^*) = L^*(\vec{a})$, so $L(\vec{a}) \in \mathbb{Z}_{>0}$ with $L(\vec{a}) \le c_k^{(1)} L(\vec{a}) = L^*(\vec{a}) + c_k d_1 \le N_{k-1} + B_k N_k \le 2 B_1 N_1 \le (3 B_1)^k N_1$, and $v_0(L) = L(\vec{a})$.
    - If $L^*(\vec{a}) > N_{k-1}$ with $v_1(L^*) = \dots = v_s(L^*) = 0$, then $\mathcal{I}_{k-1}$ yields $L^*(\vec{a}) \in \mathbb{Z}_{>0}$ with $L^*(\vec{a}) \le (3 B_1)^{k-1} N_1$ and $v_0(L^*) = L^*(\vec{a})$, whence $v_r(L) = 0$ ($r \ge 1$), $L(\vec{a}) \in \mathbb{Z}_{>0}$ with $L(\vec{a}) \le (3 B_1)^{k-1} N_1 + B_k N_k \le (3 B_1)^k N_1$, and $v_0(L) = L(\vec{a})$.
    - Otherwise $L^*(\vec{a}) > N_{k-1}$ has highest nonzero $v_r(L^*) = c_k^{(1)} v_r(L) \ge 1$ ($r \ge 1$), so $v_r(L) \ge 1$, and $L^*(\vec{a}) \le T_{r, k-1}$, whence $L(\vec{a}) \le c_k^{(1)} L(\vec{a}) = L^*(\vec{a}) + c_k d_1 \le T_{r, k-1} + B_k N_k < T_{r, k}$.

**Step 3 (Unpinned case).** Suppose every $(c_0, \dots, c_k) \in \mathcal{T}_k$ satisfies $L(\vec{a}) > N_k$. In particular $a_k > N_k$, so $B_k \sum_{i=1}^k a_i + B_k > N_k$, and Step 1 ensures $s \ge 1$. We choose $e_{k, r}$ top-down for $r = s, s-1, \dots, 1$, maintaining the set $\mathcal{A}_r \subseteq \mathcal{T}_k$ of tuples with $v_j = 0$ for all $j > r$ (initially $\mathcal{A}_s = \mathcal{T}_k$).

At level $r \in \{s, \dots, 1\}$, set $T_{0, k} := N_k$. Each $(c_0, \dots, c_k) \in \mathcal{A}_r$ requires $c_k x + \sum_{i<k} c_i e_{i, r} \ge 1$ if $L(\vec{a}) > T_{r-1, k}$ (strict), and $\ge 0$ if $L(\vec{a}) \le T_{r-1, k}$ (weak). Note that every $L \in \mathcal{A}_r$ has $L(\vec{a}) \le T_{r, k}$ (by Step 1 for $r = s$, and by induction from level $r + 1$ for $r < s$).
- If $V_r$ was just created at round $k$ ($r = s$), Step 1 guarantees every tuple in $\mathcal{A}_s = \mathcal{T}_k$ (where $L(\vec{a}) > N_k$) has $c_k > 0$, giving only lower bounds $x > 0$ (or $x \ge 0$), satisfied by $x = F_{k+1}$.
- Otherwise (so $k \ge 2$, and $e_{i, r}$ for $i < k$ all satisfy $\mathcal{I}_{k-1}$): write the rational lower and upper endpoints for each $(c_0, \dots, c_k) \in \mathcal{A}_r$ as
  $$\alpha(L) := \frac{-\sum_{i<k} c_i e_{i, r}}{c_k} \quad (c_k > 0), \qquad \beta(L') := \frac{\sum_{i<k} c'_i e_{i, r}}{m_k} \quad (c'_k = -m_k < 0).$$
  Since $F_k = 2(B_k!)^2 F_{k+1} \mid e_{i, r}$ ($i < k$) and $c_k, m_k \mid B_k!$, both $\alpha(L)$ and $\beta(L')$ are integer multiples of $2 B_k! F_{k+1}$ (hence of $F_{k+1}$) with $|\alpha(L)|, |\beta(L')| \le B_k(k-1)E_{k-1}$. For $x \in F_{k+1}\mathbb{Z}$, a strict bound requires $x \ge \alpha(L) + F_{k+1}$ (resp. $x \le \beta(L') - F_{k+1}$), and a weak bound requires $x \ge \alpha(L)$ (resp. $x \le \beta(L')$). Comparing any lower bound $L$ ($c_k > 0$) against any upper bound $L'$ ($c'_k = -m_k < 0$) by eliminating $a_k$ gives $L^*(\vec{a}) := m_k L(\vec{a}) + c_k L'(\vec{a}) > 2 N_k > 0$ with coefficients in $[-B_{k-1}, B_{k-1}]$ and $v_j(L^*) = 0$ for all $j > r$, where $\beta(L') - \alpha(L) = v_r(L^*)/(m_k c_k)$.
  - For $r \ge 2$: if either $L$ or $L'$ is strict, then $L^*(\vec{a}) > T_{r-1, k} > T_{r-1, k-1}$, so $\mathcal{I}_{k-1}$ forces $v_r(L^*) \ge 1$; divisibility by $F_k = 2(B_k!)^2 F_{k+1}$ gives $v_r(L^*) \ge F_k$, hence $\beta(L') - \alpha(L) \ge 2 F_{k+1}$. If both $L$ and $L'$ are weak, $\mathcal{I}_{k-1}$ on $L^*(\vec{a}) > 0$ gives $v_r(L^*) \ge 0$, so $\beta(L') - \alpha(L) \ge 0$. Checking all four pairings (strict-strict has $\beta - \alpha \ge 2 F_{k+1}$; strict-weak and weak-strict have $\beta - \alpha \ge 2 F_{k+1} > F_{k+1}$; weak-weak has $\beta - \alpha \ge 0$), the closed interval
    $$I_r := \Big[\max\big(\max_{\text{weak}} \alpha(L),\; \max_{\text{strict}}(\alpha(L) + F_{k+1})\big),\;\; \min\big(\min_{\text{weak}} \beta(L'),\; \min_{\text{strict}}(\beta(L') - F_{k+1})\big)\Big]$$
    is nonempty, and its finite endpoint(s) are multiples of $F_{k+1}$ of magnitude $\le B_k(k-1)E_{k-1} + F_{k+1} \le E_k$. Choose $x$ to be the left endpoint of $I_r$ if lower bounds exist, the right endpoint if only upper bounds exist, or $0$ if $\mathcal{A}_r = \emptyset$.
  - For $r = 1$: for every pair $(L, L')$, $\mathcal{I}_{k-1}$ on $L^*(\vec{a}) > 0$ gives $v_1(L^*) \ge 0$, so $\beta(L') - \alpha(L) \ge 0$. If $v_1(L^*) \ge 1$ whenever at least one of $L, L'$ is strict, then $I_1$ is nonempty exactly as above (and we pick $x$ as the left endpoint if lower bounds exist, the right endpoint if only upper bounds exist, or $0$ if $\mathcal{A}_1 = \emptyset$). Otherwise, some pair $(L, L')$ with at least one strict bound has $v_1(L^*) = 0$, so $\alpha(L) = \beta(L')$ and the tightest lower bound $\mathrm{LB} := \max \alpha(L)$ equals the tightest upper bound $\mathrm{UB} := \min \beta(L')$; we set $x := \mathrm{LB} = \mathrm{UB}$ (a multiple of $F_{k+1}$ with $|x| \le B_k(k-1)E_{k-1} \le E_k$). For any tight pair attaining $\mathrm{LB} = \mathrm{UB}$, $v_1(L^*) = 0$ and $\mathcal{I}_{k-1}$ imply $L^*(\vec{a}) \in \mathbb{Z}_{>0}$ with $L^*(\vec{a}) \le (3 B_1)^{k-1} N_1$ and $v_0(L^*) = L^*(\vec{a})$; since $L(\vec{a}), L'(\vec{a}) > 0$, both $L(\vec{a}), L'(\vec{a}) \in \mathbb{Z}_{>0}$ are standard integers.

Finally, choose $e_{k, 0}$:
- If the collision $\mathrm{LB} = \mathrm{UB}$ occurred at $r = 1$ (so $k \ge 2$), pick one tight tuple $(c_0^\dagger, \dots, c_k^\dagger) \in \mathcal{A}_1$ attaining $\mathrm{LB}$ (so $v_1(L^\dagger) = 0$ and $0 < L^\dagger(\vec{a}) = d^\dagger \le L^*(\vec{a}) \le (3 B_1)^{k-1} N_1$) and pin $e_{k, 0} := (d^\dagger - c_0^\dagger - \sum_{i<k} c_i^\dagger e_{i, 0}) / c_k^\dagger$. By $\mathcal{I}_{k-1}$, $e_{k, 0} \in \mathbb{Z}$, $e_{k, 0} \equiv a_k \pmod{\mu_k}$, $|e_{k, 0}| \le E_{0, k}$. For any $L'' \in \mathcal{A}_1$ with $v_1(L'') = 0$, form $L^{**} := c_k^\dagger L'' - c_k'' L^\dagger$ (wlog $c_k^\dagger > 0$, after possibly negating $L^\dagger$ and $d^\dagger$ together, and note $L^{**}(\vec{a})$ may be negative); applying $\mathcal{I}_{k-1}$ to $\pm L^{**}$ (since $v_j(L^{**}) = 0$ for all $j \ge 1$) forces $L^{**}(\vec{a}) \in \mathbb{Z}$ with $|L^{**}(\vec{a})| \le (3 B_1)^{k-1} N_1$ and $v_0(L^{**}) = L^{**}(\vec{a})$, whence $L''(\vec{a}) \in \mathbb{Z}_{>0}$ with $L''(\vec{a}) \le c_k^\dagger L''(\vec{a}) = L^{**}(\vec{a}) + c_k'' d^\dagger \le (B_k + 1)(3 B_1)^{k-1} N_1 \le (3 B_1)^k N_1$ and $v_0(L'') = L''(\vec{a})$.
- Otherwise (no collision at $r = 1$, so every tuple in $\mathcal{T}_k$ has some $r \ge 1$ with $v_r \ge 1$): take $e_{k, 0} := a_k \bmod \mu_k \in [0, \mu_k - 1]$ (which exists since $\mathcal{M}^+ \models \mathbb{Z}\text{-}\mathsf{DOSR}$).

In all cases, $\mathcal{I}_k$ holds at round $k$. By induction, $\mathcal{I}_n$ holds at round $n$, so Exp-er has a winning strategy in $G_{n, M}(\mathcal{M}^+)$ for every $n, M \ge 1$. By Lemma 1, every model of $\mathsf{IOpen}$ is elementarily equivalent to a reduct of a model of $\mathsf{IOpen} + (\mathrm{Exp})$, hence $\mathsf{IOpen} + (\mathrm{Exp})$ is conservative over $\mathsf{IOpen}$. $\blacksquare$
